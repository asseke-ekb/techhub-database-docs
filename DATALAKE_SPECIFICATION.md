# TechHub Data Lake - Техническая спецификация

## 📋 Обзор проекта

**Источник:** PostgreSQL база данных TechHub (Django)
**Целевая платформа:** MinIO Data Lake
**Общий объём:** ~5.12 GB
**Таблиц:** 157
**Записей:** ~3.5M+

---

## 🏗️ Архитектура Data Lake

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                              DATA LAKE ARCHITECTURE                          │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   ┌──────────────┐     ┌──────────────┐     ┌──────────────┐               │
│   │   BRONZE     │     │   SILVER     │     │    GOLD      │               │
│   │   (Raw)      │────▶│  (Cleaned)   │────▶│  (Analytics) │               │
│   └──────────────┘     └──────────────┘     └──────────────┘               │
│         │                    │                    │                         │
│         ▼                    ▼                    ▼                         │
│   ┌──────────────┐     ┌──────────────┐     ┌──────────────┐               │
│   │   MinIO      │     │   MinIO      │     │   MinIO      │               │
│   │ /bronze/     │     │ /silver/     │     │ /gold/       │               │
│   │  techhub/    │     │  techhub/    │     │  techhub/    │               │
│   └──────────────┘     └──────────────┘     └──────────────┘               │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘

PostgreSQL ──CDC──▶ Bronze (Parquet) ──ETL──▶ Silver (Delta) ──▶ Gold (Marts)
```

---

## 📊 Слой BRONZE (Raw Data)

### Структура в MinIO

```
s3://datalake/bronze/techhub/
├── account/
│   ├── user/
│   │   ├── year=2024/month=01/
│   │   │   └── data_20240101.parquet
│   │   └── year=2025/month=12/
│   │       └── data_20251204.parquet
│   ├── company/
│   ├── usercompany/
│   └── activation/
├── core/
│   ├── event/
│   ├── vacancy/
│   ├── blog/
│   ├── techtask/
│   └── comment/
├── service/
│   ├── service/
│   ├── servicerequest/
│   ├── hubform/
│   └── hubformdata/
├── booking/
│   ├── room/
│   └── booking/
├── techorda/
│   ├── school/
│   ├── course/
│   └── flow/
└── _metadata/
    ├── schema_versions/
    └── extraction_logs/
```

### Приоритет таблиц для загрузки

#### 🔴 Критические (загружать первыми)

| Таблица | Размер | Записей | Частота обновления |
|---------|--------|---------|-------------------|
| `user_sessions_session` | 1.27 GB | 2.9M | Высокая (исключить из DL?) |
| `core_actionlog` | 1.01 GB | 125K | Высокая |
| `service_hubformdata` | 599 MB | 61K | Средняя |
| `account_user` | 308 MB | 54K | Низкая |
| `service_servicerequest` | 243 MB | 56K | Средняя |

#### 🟡 Важные

| Таблица | Размер | Записей |
|---------|--------|---------|
| `core_blog` | 399 MB | 1.8K |
| `account_company` | 20 MB | 6.6K |
| `core_event` | ~15 MB | 1.4K |
| `core_vacancy` | 8.8 MB | 1.2K |
| `booking_booking` | ~5 MB | 8.6K |

#### 🟢 Справочники (редко меняются)

| Таблица | Записей | Тип |
|---------|---------|-----|
| `core_organization` | 45 | Dimension |
| `core_category` | 14 | Dimension |
| `core_city` | 16 | Dimension |
| `core_country` | 1 | Dimension |
| `booking_room` | 16 | Dimension |
| `service_service` | 310 | Dimension |

---

## 📊 Слой SILVER (Cleaned & Normalized)

### Трансформации

#### 1. Распаковка JSONB полей

```python
# account_user.data -> отдельные колонки
{
    "goals": ["vacancies", "networking"],
    "auth_flow": {"type": "phone_registration"},
    "hard_skills": [...],
    "soft_skills": [...]
}

# Результат в Silver:
| user_id | goal_vacancies | goal_networking | auth_flow_type | hard_skills_array |
```

#### 2. Мультиязычные поля (title, content)

```python
# core_event.title JSONB:
{"ru": "Конференция", "kk": "Конференция", "en": "Conference"}

# Результат в Silver:
| event_id | title_ru | title_kk | title_en |
```

#### 3. Нормализация тегов компаний

```python
# account_company JSONB теги:
tag_startup, tag_it_company, tag_techpark, tag_ts_member...

# Результат в Silver - отдельная таблица:
company_tags:
| company_id | tag_type | status | verified_at | verified_by |
```

### JSONB поля для распаковки

| Таблица | Поле | Ключи внутри |
|---------|------|--------------|
| `account_user` | `data` | goals, auth_flow, hard_skills, soft_skills, extra_courses |
| `account_user` | `tags` | article, ... |
| `account_user` | `permissions` | documentolog, ... |
| `account_company` | `tag_startup` | data, status, moderation_data |
| `account_company` | `tag_it_company` | data, status, moderation_data |
| `account_company` | `basic_info` | company_tag |
| `service_hubformdata` | `data` | Risks, Full_name, Sales_market, Priority_area, ... (динамические поля форм!) |
| `service_servicerequest` | `data` | signatures, reject_detail |
| `core_event` | `title` | ru, kk, en |
| `core_event` | `content` | ru, kk, en |
| `core_event` | `contact_info` | email, phone, full_name |

---

## 📊 Слой GOLD (Analytics / Data Marts)

### Предлагаемые Data Marts

#### 1. `dm_users` - Профиль пользователя
```sql
CREATE TABLE gold.dm_users AS
SELECT
    u.id as user_id,
    u.email,
    u.first_name,
    u.last_name,
    u.role,
    u.is_active,
    u.created_at as registered_at,
    -- Из JSONB
    u.data->>'goals' as goals,
    -- Компания
    c.id as primary_company_id,
    c.name as primary_company_name,
    -- Агрегаты
    COUNT(DISTINCT uc.company_id) as companies_count,
    COUNT(DISTINCT sr.id) as service_requests_count,
    COUNT(DISTINCT b.id) as events_attended
FROM account_user u
LEFT JOIN account_company c ON u.company_id = c.id
LEFT JOIN account_usercompany uc ON u.id = uc.user_id
LEFT JOIN service_servicerequest sr ON u.id = sr.author_id
LEFT JOIN core_eventparticipant ep ON u.id = ep.author_id
GROUP BY u.id, c.id;
```

#### 2. `dm_companies` - Профиль компании
```sql
CREATE TABLE gold.dm_companies AS
SELECT
    c.id as company_id,
    c.tin,
    c.name,
    c.company_type,
    c.status,
    c.verified,
    c.created_at,
    -- Теги (из JSONB)
    (c.tag_startup->>'status')::varchar as startup_status,
    (c.tag_it_company->>'status')::varchar as it_company_status,
    -- Агрегаты
    COUNT(DISTINCT uc.user_id) as employees_count,
    COUNT(DISTINCT e.id) as events_count,
    COUNT(DISTINCT v.id) as vacancies_count,
    COUNT(DISTINCT sr.id) as service_requests_count,
    SUM(CASE WHEN sr.status = 'success' THEN 1 ELSE 0 END) as successful_requests
FROM account_company c
LEFT JOIN account_usercompany uc ON c.id = uc.company_id
LEFT JOIN core_event e ON c.id = e.company_id
LEFT JOIN core_vacancy v ON c.id = v.company_id
LEFT JOIN service_servicerequest sr ON c.id = sr.company_id
GROUP BY c.id;
```

#### 3. `dm_service_funnel` - Воронка заявок
```sql
CREATE TABLE gold.dm_service_funnel AS
SELECT
    s.code as service_code,
    s.data->>'name' as service_name,
    DATE_TRUNC('month', sr.created_at) as month,
    COUNT(*) as total_requests,
    SUM(CASE WHEN sr.status = 'draft' THEN 1 ELSE 0 END) as draft,
    SUM(CASE WHEN sr.status = 'sent' THEN 1 ELSE 0 END) as sent,
    SUM(CASE WHEN sr.status = 'approved' THEN 1 ELSE 0 END) as approved,
    SUM(CASE WHEN sr.status = 'success' THEN 1 ELSE 0 END) as success,
    SUM(CASE WHEN sr.status IN ('reject', 'rejected') THEN 1 ELSE 0 END) as rejected
FROM service_servicerequest sr
JOIN service_service s ON sr.service_id = s.code
GROUP BY s.code, s.data->>'name', DATE_TRUNC('month', sr.created_at);
```

#### 4. `dm_events_analytics` - Аналитика событий
```sql
CREATE TABLE gold.dm_events_analytics AS
SELECT
    e.id as event_id,
    e.title->>'ru' as title,
    e.status,
    e.event_type,
    e.event_format,
    e.datetime_start,
    e.datetime_end,
    e.published,
    c.name as company_name,
    o.name->>'ru' as organization_name,
    COUNT(DISTINCT ep.id) as participants_count,
    e.view_count
FROM core_event e
LEFT JOIN account_company c ON e.company_id = c.id
LEFT JOIN core_organization o ON e.organization_id = o.code
LEFT JOIN core_eventparticipant ep ON e.id = ep.event_id
GROUP BY e.id, c.name, o.name;
```

#### 5. `dm_vacancies_market` - Рынок вакансий
```sql
CREATE TABLE gold.dm_vacancies_market AS
SELECT
    v.id as vacancy_id,
    v.title->>'ru' as title,
    v.status,
    v.vacancy_type,
    v.salary_min,
    v.salary_max,
    (v.salary_min + v.salary_max) / 2 as salary_avg,
    c.name as company_name,
    c.verified as company_verified,
    city.name as city_name,
    v.created_at,
    COUNT(DISTINCT vc.id) as candidates_count
FROM core_vacancy v
LEFT JOIN account_company c ON v.company_id = c.id
LEFT JOIN core_city city ON v.city_id = city.id
LEFT JOIN core_vacancycandidate vc ON v.id = vc.vacancy_id
GROUP BY v.id, c.name, c.verified, city.name;
```

---

## 🔄 ETL Pipeline

### Стратегия загрузки

```
┌─────────────────────────────────────────────────────────────────┐
│                     ETL STRATEGY                                │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  FULL LOAD (первичная + периодическая):                        │
│  ├── Справочники (core_organization, core_city, etc.)          │
│  ├── Малые таблицы (< 10K записей)                             │
│  └── Периодичность: 1 раз в день                               │
│                                                                 │
│  INCREMENTAL (CDC):                                            │
│  ├── account_user (по updated_at)                              │
│  ├── account_company (по updated_at)                           │
│  ├── service_servicerequest (по created_at, updated_at)        │
│  ├── core_event (по updated_at)                                │
│  ├── core_blog (по updated_at)                                 │
│  └── Периодичность: каждые 15-30 минут                         │
│                                                                 │
│  APPEND-ONLY:                                                  │
│  ├── core_actionlog (только новые по created_at)               │
│  ├── service_servicerequestlog                                 │
│  ├── booking_bookingstatus                                     │
│  └── Периодичность: каждые 5-15 минут                          │
│                                                                 │
│  EXCLUDE (не загружать):                                       │
│  ├── user_sessions_session (1.27 GB, операционные данные)      │
│  ├── django_session                                            │
│  ├── silk_* (профилирование)                                   │
│  └── hub_cache_table                                           │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Watermark поля для CDC

| Таблица | Watermark поле | Тип |
|---------|---------------|-----|
| `account_user` | `updated_at` | Incremental |
| `account_company` | `updated_at` | Incremental |
| `service_servicerequest` | `updated_at` | Incremental |
| `core_event` | `updated_at` | Incremental |
| `core_blog` | `updated_at` | Incremental |
| `core_actionlog` | `created_at` | Append-only |
| `booking_booking` | `updated_at` | Incremental |

### Пример ETL скрипта (Python + MinIO)

```python
import psycopg2
import pyarrow as pa
import pyarrow.parquet as pq
from minio import Minio
from datetime import datetime, timedelta
import io

# Конфигурация
PG_CONFIG = {
    'dbname': 'techhub',
    'user': 'dgabbassov',
    'password': 'sVLKLeM5D%',
    'host': '188.130.234.92',
    'port': '50693'
}

MINIO_CONFIG = {
    'endpoint': 'minio.example.com:9000',
    'access_key': 'YOUR_ACCESS_KEY',
    'secret_key': 'YOUR_SECRET_KEY',
    'secure': True
}

BUCKET = 'datalake'

def extract_incremental(table_name, watermark_field, last_watermark):
    """Извлечение инкрементальных данных"""
    conn = psycopg2.connect(**PG_CONFIG)

    query = f"""
        SELECT *
        FROM {table_name}
        WHERE {watermark_field} > %s
        ORDER BY {watermark_field}
    """

    df = pd.read_sql(query, conn, params=[last_watermark])
    conn.close()
    return df

def transform_jsonb_fields(df, jsonb_columns):
    """Распаковка JSONB полей"""
    for col in jsonb_columns:
        if col in df.columns:
            # Нормализация JSON в отдельные колонки
            json_df = pd.json_normalize(df[col].apply(
                lambda x: x if isinstance(x, dict) else {}
            ))
            json_df.columns = [f"{col}_{c}" for c in json_df.columns]
            df = pd.concat([df.drop(columns=[col]), json_df], axis=1)
    return df

def load_to_minio(df, table_name, partition_date):
    """Загрузка в MinIO как Parquet"""
    client = Minio(**MINIO_CONFIG)

    # Конвертация в Parquet
    table = pa.Table.from_pandas(df)
    buffer = io.BytesIO()
    pq.write_table(table, buffer, compression='snappy')
    buffer.seek(0)

    # Путь с партиционированием
    year = partition_date.strftime('%Y')
    month = partition_date.strftime('%m')
    day = partition_date.strftime('%d')

    object_path = f"bronze/techhub/{table_name}/year={year}/month={month}/data_{year}{month}{day}.parquet"

    client.put_object(
        BUCKET,
        object_path,
        buffer,
        buffer.getbuffer().nbytes,
        content_type='application/octet-stream'
    )

    return object_path

# Пример использования
if __name__ == '__main__':
    # Инкрементальная загрузка account_user
    last_watermark = datetime.now() - timedelta(hours=1)

    df = extract_incremental('account_user', 'updated_at', last_watermark)
    df = transform_jsonb_fields(df, ['data', 'tags', 'permissions'])

    path = load_to_minio(df, 'account/user', datetime.now())
    print(f"Loaded to: {path}")
```

---

## 📈 Data Quality Rules

### Критические проверки

| Таблица | Поле | Правило | Текущее состояние |
|---------|------|---------|------------------|
| `account_user` | `email` | NOT NULL для активных | 39% NULL ⚠️ |
| `account_user` | `iin` | 12 символов | 99.8% NULL (норма - не все указывают) |
| `account_company` | `tin` | 12 символов, уникальный | 11.2% NULL ⚠️ |
| `account_company` | `bank`, `iik`, `bik` | NOT NULL для verified | 95% NULL ⚠️ |
| `service_servicerequest` | `company_id` | NOT NULL | 92.6% NULL (норма - физ.лица) |
| `core_vacancy` | `salary_min/max` | min <= max | 43-48% NULL |

### Рекомендации по очистке

```python
# Silver layer transformations
def clean_account_user(df):
    # Нормализация email
    df['email_clean'] = df['email'].str.lower().str.strip()

    # Флаг качества данных
    df['dq_has_email'] = df['email'].notna()
    df['dq_has_phone'] = df['phone'].notna() & (df['phone'] != '')
    df['dq_profile_complete'] = df['dq_has_email'] & df['dq_has_phone']

    return df

def clean_account_company(df):
    # Валидация БИН/ИИН
    df['tin_valid'] = df['tin'].str.match(r'^\d{12}$', na=False)

    # Нормализация типа компании
    df['company_type_clean'] = df['company_type'].replace({
        '': 'unknown',
        None: 'unknown'
    })

    return df
```

---

## 🗓️ Партиционирование

### Рекомендации

| Таблица | Партиционирование | Причина |
|---------|------------------|---------|
| `account_user` | `year/month` по `created_at` | Средний рост |
| `service_servicerequest` | `year/month` по `created_at` | 56K записей, растёт |
| `core_actionlog` | `year/month/day` по `created_at` | 125K, быстро растёт |
| `core_event` | `year` по `datetime_start` | 1.4K, медленный рост |
| `booking_booking` | `year/month` по `start` | 8.6K |

### Формат файлов

```
Bronze: Parquet (snappy compression)
Silver: Delta Lake или Parquet
Gold:   Parquet / Delta для BI инструментов
```

---

## 🔗 Lineage (Происхождение данных)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           DATA LINEAGE                                       │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  PostgreSQL                      Bronze                Silver               │
│  ──────────                      ──────                ──────               │
│                                                                              │
│  account_user ──────────────────▶ user.parquet ──────▶ dim_user            │
│       │                               │                    │                │
│       │ (company_id)                  │                    │                │
│       ▼                               ▼                    ▼                │
│  account_company ───────────────▶ company.parquet ───▶ dim_company         │
│       │                               │                    │                │
│       │ (id)                          │                    │                │
│       ▼                               ▼                    ▼                │
│  service_servicerequest ────────▶ request.parquet ───▶ fact_requests       │
│       │                               │                    │                │
│       │ (service_id)                  │                    │                │
│       ▼                               ▼                    ▼                │
│  service_service ───────────────▶ service.parquet ───▶ dim_service         │
│                                                                              │
│                                                              │               │
│                                                              ▼               │
│                                                        Gold Layer           │
│                                                        ──────────           │
│                                                        dm_users             │
│                                                        dm_companies         │
│                                                        dm_service_funnel    │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 📊 Топ сервисов (для понимания бизнеса)

| Код сервиса | Заявок | Описание |
|-------------|--------|----------|
| `ast_startup_school` | 6,812 | Startup School |
| `mat_pass` | 6,012 | Материальный пропуск |
| `ast_nocode` | 4,923 | NoCode курс |
| `ast_BetaCareer2022` | 3,094 | Beta Career 2022 |
| `techorda_graduate_v2` | 2,809 | TechOrda выпускники |

---

## 🛠️ Инструменты для реализации

### Рекомендуемый стек

```
┌─────────────────────────────────────────────────────────────────┐
│                     RECOMMENDED STACK                           │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Orchestration:     Apache Airflow / Dagster                   │
│  ETL:               PySpark / Polars / DuckDB                  │
│  Storage:           MinIO (S3-compatible)                      │
│  Format:            Parquet + Delta Lake                       │
│  Catalog:           Apache Hive Metastore / AWS Glue Catalog   │
│  Query Engine:      Trino / DuckDB / Spark SQL                 │
│  BI:                Apache Superset / Metabase                 │
│  Data Quality:      Great Expectations / Soda                  │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 📝 Checklist для реализации

### Phase 1: Bronze Layer
- [ ] Настроить MinIO bucket структуру
- [ ] Создать ETL для справочников (Full Load)
- [ ] Создать ETL для основных таблиц (Incremental)
- [ ] Настроить партиционирование
- [ ] Реализовать логирование загрузок

### Phase 2: Silver Layer
- [ ] Распаковка JSONB полей
- [ ] Нормализация мультиязычных полей
- [ ] Data Quality проверки
- [ ] Создание dimension таблиц
- [ ] SCD Type 2 для медленно меняющихся измерений

### Phase 3: Gold Layer
- [ ] dm_users
- [ ] dm_companies
- [ ] dm_service_funnel
- [ ] dm_events_analytics
- [ ] dm_vacancies_market

### Phase 4: Analytics
- [ ] Подключить BI инструмент
- [ ] Создать дашборды
- [ ] Настроить алерты

---

*Документ создан: 2025-12-04*
*Версия: 1.0*
