# Форматы выгрузки сущностей

## Обзор

Данный документ описывает структуру данных для выгрузки из TechHub.

---

## 1. Выгрузка пользователей

### Таблица: account_user

**Записей:** 54,063

### Поля для выгрузки

| Поле | Тип | Описание | Пример |
|------|-----|----------|--------|
| id | integer | PK | 12345 |
| email | varchar(400) | Email | user@example.com |
| phone | varchar(100) | Телефон | +77001234567 |
| first_name | varchar(400) | Имя | Иван |
| last_name | varchar(400) | Фамилия | Иванов |
| iin | varchar(100) | ИИН | 123456789012 |
| role | varchar(50) | Роль | user |
| is_active | boolean | Активен | true |
| blocked | boolean | Заблокирован | false |
| email_verified | boolean | Email подтверждён | true |
| phone_verified | boolean | Телефон подтверждён | true |
| created_at | timestamp | Дата регистрации | 2024-01-15 10:30:00 |
| last_login | timestamp | Последний вход | 2024-12-07 09:00:00 |
| company_id | integer | FK на компанию | 6789 |

### Теги пользователя (JSONB)

| Поле | Описание |
|------|----------|
| tag_it_specialist | IT-специалист |
| tag_investor | Инвестор |
| tag_intern | Стажёр (выпускник TechOrda) |
| tag_expert | Эксперт |
| tag_startup_member | Член стартапа |
| tag_company_member | Сотрудник компании |

### Формат тега

```json
{
  "status": "active",
  "date_from": "2024-01-15",
  "date_to": null,
  "data": {}
}
```

---

## 2. Выгрузка компаний

### Таблица: account_company

**Записей:** 6,639

### Поля для выгрузки

| Поле | Тип | Описание | Пример |
|------|-----|----------|--------|
| id | integer | PK | 6789 |
| name | varchar(1000) | Полное название | ТОО "Компания" |
| short_name | varchar(200) | Краткое название | Компания |
| tin | varchar(12) | БИН/ИИН | 123456789012 |
| company_type | varchar(30) | Тип | law |
| status | varchar(20) | Статус | active |
| verified | boolean | Верифицирована | true |
| address | varchar(2000) | Адрес | г. Астана, ... |
| email | varchar(200) | Email | info@company.kz |
| phone | varchar(30) | Телефон | +77172123456 |
| website | varchar(1000) | Сайт | https://company.kz |
| created_at | timestamp | Дата регистрации | 2024-01-10 12:00:00 |
| author_id | integer | FK на создателя | 12345 |

### Банковские реквизиты

| Поле | Описание |
|------|----------|
| bank | Название банка |
| iik | ИИК (расчётный счёт) |
| bik | БИК |
| kbe | КБе |

### Теги компании (JSONB)

| Поле | Описание | Бизнес-значение |
|------|----------|-----------------|
| tag_it_company | IT-компания | Аккредитация, налоговые льготы |
| tag_startup | Стартап | В реестре стартапов РК |
| tag_techpark | Резидент | Резидент Astana Hub |
| tag_corp_partner | Корп. партнёр | Партнёрская программа |
| tag_nii | НИИ | Научный институт |
| tag_nedrouser | Недропользователь | Для НИОКР |

---

## 3. Выгрузка членства в компаниях

### Таблица: account_usercompany

**Записей:** 4,536

### Поля для выгрузки

| Поле | Тип | Описание | Пример |
|------|-----|----------|--------|
| id | integer | PK | 4536 |
| user_id | integer | FK на пользователя | 12345 |
| company_id | integer | FK на компанию | 6789 |
| role | varchar(20) | Роль в компании | owner |
| verified | boolean | Подтверждено | true |

### Роли

| Значение | Описание |
|----------|----------|
| owner | Владелец (один на компанию) |
| member | Сотрудник |
| advisor | Консультант |

---

## 4. Выгрузка заявок на услуги

### Таблица: service_servicerequest

**Записей:** 56,322

### Поля для выгрузки

| Поле | Тип | Описание | Пример |
|------|-----|----------|--------|
| id | integer | PK | 56322 |
| service_id | integer | FK на услугу | 1 |
| author_id | integer | FK на заявителя | 12345 |
| company_id | integer | FK на компанию | 6789 |
| status | varchar(30) | Статус | success |
| created_at | timestamp | Дата подачи | 2024-01-20 14:30:00 |
| updated_at | timestamp | Дата изменения | 2024-02-01 10:00:00 |

### Связь с услугой

Для получения кода услуги — JOIN с `service_service`:

| Поле | Описание |
|------|----------|
| service_service.id | PK услуги |
| service_service.code | Код услуги (accreditation, startup_register, ...) |
| service_service.name | Название (JSONB, мультиязычное) |

---

## 5. Выгрузка событий

### Таблица: core_event

**Записей:** 1,459

### Поля для выгрузки

| Поле | Тип | Описание |
|------|-----|----------|
| id | integer | PK |
| title | jsonb | Название (ru/kk/en) |
| content | jsonb | Описание (ru/kk/en) |
| event_type | varchar(30) | Тип (open_event, closed_event) |
| event_format | varchar(30) | Формат (astanahub, online, hybrid) |
| status | varchar(30) | Статус публикации |
| start_date | timestamp | Начало |
| end_date | timestamp | Окончание |
| author_id | integer | FK на организатора |
| company_id | integer | FK на компанию |
| created_at | timestamp | Дата создания |

### Извлечение мультиязычного текста

```sql
-- Русский текст
SELECT title->>'ru' as title_ru FROM core_event;

-- С fallback
SELECT COALESCE(title->>'ru', title->>'kk', title->>'en') as title
FROM core_event;
```

---

## 6. Выгрузка вакансий

### Таблица: core_vacancy

**Записей:** 1,205

### Поля для выгрузки

| Поле | Тип | Описание |
|------|-----|----------|
| id | integer | PK |
| title | jsonb | Название (ru/kk/en) |
| content | jsonb | Описание (ru/kk/en) |
| vacancy_type | varchar(30) | Тип занятости |
| status | varchar(30) | Статус публикации |
| salary_from | integer | Зарплата от |
| salary_to | integer | Зарплата до |
| company_id | integer | FK на компанию |
| author_id | integer | FK на автора |
| created_at | timestamp | Дата создания |

---

## 7. Выгрузка бронирований

### Таблица: booking_booking

**Записей:** 8,628

### Поля для выгрузки

| Поле | Тип | Описание |
|------|-----|----------|
| id | integer | PK |
| room_id | integer | FK на комнату |
| user_id | integer | FK на пользователя |
| start_time | timestamp | Начало брони |
| end_time | timestamp | Окончание брони |
| status | varchar(20) | Статус (active, finished, deactivated) |
| created_at | timestamp | Дата создания |

---

## Рекомендации по выгрузке

### Фильтрация по дате

```sql
-- Записи за последний месяц
WHERE created_at >= NOW() - INTERVAL '1 month'

-- Записи за период
WHERE created_at BETWEEN '2024-01-01' AND '2024-12-31'
```

### Фильтрация по статусу

```sql
-- Только активные
WHERE status = 'active'
WHERE is_active = true

-- Только опубликованные
WHERE status = 'success'
```

### Фильтрация по тегам

```sql
-- IT-компании
WHERE tag_it_company->>'status' = 'active'

-- Стартапы
WHERE tag_startup->>'status' = 'active'

-- Резиденты
WHERE tag_techpark->>'status' = 'active'
```

### Инкрементальная выгрузка

```sql
-- Изменённые после определённой даты
WHERE updated_at > '2024-12-01T00:00:00Z'
```
