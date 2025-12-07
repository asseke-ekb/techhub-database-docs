# Модуль SHARED

**Описание:** Общие ресурсы (медиафайлы, SEO, контекст)

**Таблиц в модуле:** 6

---

| Таблица | Записей | Описание |
|---------|---------|----------|
| `shared_contextdata` | 243 | - |
| `shared_largecache` | 2 | - |
| `shared_mediafile` | 50,936 | - |
| `shared_protectedmediafile` | 92,960 | - |
| `shared_seodata` | 97 | - |
| `shared_smslog` | 0 | - |

### shared_contextdata

**Количество записей:** 243

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 2 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 3 | `data` | jsonb | Нет | - | Дополнительные данные (JSON) |
| 4 | `code` | character varying(100) | Нет | - |  |
| 5 | `description` | character varying(200) | Нет | - |  |
| 6 | `version` | character varying(10) | Нет | - |  |

---

### shared_largecache

**Количество записей:** 2

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 2 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 3 | `name` | character varying(200) | Нет | - | Наименование |
| 4 | `data` | jsonb | Нет | - | Дополнительные данные (JSON) |
| 5 | `timeout` | integer | Нет | - |  |

---

### shared_mediafile

**Количество записей:** 50,936

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 2 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 3 | `file` | character varying(1000) | Нет | - |  |
| 4 | `thumbnail` | character varying(1000) | Да | - |  |
| 5 | `mime_type` | character varying(500) | Нет | - |  |
| 6 | `size` | double precision | Нет | - |  |
| 7 | `author_id` | integer | Да | - | FK на author |
| 8 | `thumbnail_150` | character varying(1000) | Да | - |  |
| 9 | `thumbnail_1500` | character varying(1000) | Да | - |  |
| 10 | `thumbnail_210` | character varying(1000) | Да | - |  |
| 11 | `thumbnail_800` | character varying(1000) | Да | - |  |
| 12 | `id` | uuid | Нет | - | Уникальный идентификатор |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `author_id` | `account_user.id` |

---

### shared_protectedmediafile

**Количество записей:** 92,960

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 2 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 3 | `id` | uuid | Нет | - | Уникальный идентификатор |
| 4 | `file` | character varying(2000) | Нет | - |  |
| 5 | `primary_key` | character varying(20) | Нет | - |  |
| 6 | `source` | character varying(20) | Нет | - |  |
| 7 | `author_id` | integer | Нет | - | FK на author |
| 8 | `mime_type` | character varying(500) | Нет | - |  |
| 9 | `size` | double precision | Нет | - |  |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `author_id` | `account_user.id` |

---

### shared_seodata

**Количество записей:** 97

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 2 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 3 | `path` | character varying | Нет | - |  |
| 4 | `title` | jsonb | Нет | - | Заголовок |
| 5 | `description` | jsonb | Нет | - |  |
| 6 | `keywords` | jsonb | Нет | - |  |

---

### shared_smslog

**Количество записей:** 0

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('shared_smslog_id_seq'::regclass... | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `number` | character varying(100) | Нет | - |  |
| 5 | `request` | text | Нет | - |  |
| 6 | `response` | text | Нет | - |  |

---