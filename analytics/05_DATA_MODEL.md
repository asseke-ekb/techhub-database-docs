# Модель данных TechHub

## Общая статистика

| Показатель | Значение |
|------------|----------|
| Всего таблиц | 157 |
| Бизнес-таблиц | 103 |
| Технических таблиц | 54 |
| Внешних ключей (FK) | 218 |

---

## ER-диаграмма: Ядро системы

```mermaid
erDiagram
    account_user ||--o{ account_usercompany : "состоит в"
    account_company ||--o{ account_usercompany : "имеет сотрудников"
    account_user ||--o{ service_servicerequest : "подаёт заявки"
    account_company ||--o{ service_servicerequest : "от имени"
    service_service ||--o{ service_servicerequest : "на услугу"
    account_user ||--o{ core_event : "создаёт"
    account_company ||--o{ core_event : "организует"
    account_user ||--o{ core_vacancy : "создаёт"
    account_company ||--o{ core_vacancy : "размещает"
    account_user ||--o{ booking_booking : "бронирует"
    booking_room ||--o{ booking_booking : "бронируется"

    account_user {
        int id PK
        varchar email
        varchar phone
        varchar role
        boolean is_active
    }

    account_company {
        int id PK
        varchar name
        varchar tin
        varchar status
        jsonb tag_it_company
        jsonb tag_startup
    }

    account_usercompany {
        int id PK
        int user_id FK
        int company_id FK
        varchar role
    }

    service_service {
        int id PK
        varchar code
        jsonb name
    }

    service_servicerequest {
        int id PK
        int service_id FK
        int author_id FK
        int company_id FK
        varchar status
    }

    core_event {
        int id PK
        jsonb title
        varchar status
        int author_id FK
        int company_id FK
    }

    core_vacancy {
        int id PK
        jsonb title
        varchar status
        int company_id FK
    }

    booking_booking {
        int id PK
        int room_id FK
        int user_id FK
        varchar status
    }

    booking_room {
        int id PK
        varchar name
    }
```

---

## Домен ACCOUNT

### Таблицы и связи

| Таблица | Записей | PK | Основные FK |
|---------|---------|----|--------------|
| account_user | 54,063 | id | company_id → account_company |
| account_company | 6,639 | id | author_id → account_user |
| account_usercompany | 4,536 | id | user_id, company_id |
| account_activation | 1,810 | uuid | user_id → account_user |
| account_usercompanyrequest | 254 | id | user_id, company_id |
| account_emaildigest | 31,474 | id | — |
| account_complaint | 20 | id | author_id, user_id, company_id |
| account_usercompanyinvitation | 2 | id | company_id, author_id, invited_user_id |

### ER-диаграмма ACCOUNT

```mermaid
erDiagram
    account_user ||--o{ account_usercompany : "членство"
    account_company ||--o{ account_usercompany : "сотрудники"
    account_user ||--o{ account_activation : "коды"
    account_user ||--o{ account_usercompanyrequest : "заявки"
    account_company ||--o{ account_usercompanyrequest : "получает"
    account_user ||--o{ account_complaint : "подаёт"
    account_company ||--o{ account_complaint : "на компанию"

    account_user {
        int id PK
        varchar email UK
        varchar phone
        varchar first_name
        varchar last_name
        varchar iin
        varchar role
        boolean is_active
        boolean blocked
        boolean email_verified
        boolean phone_verified
        int company_id FK
        timestamp created_at
        timestamp last_login
    }

    account_company {
        int id PK
        varchar name
        varchar tin UK
        varchar company_type
        varchar status
        boolean verified
        int author_id FK
        jsonb tag_it_company
        jsonb tag_startup
        jsonb tag_techpark
        timestamp created_at
    }

    account_usercompany {
        int id PK
        int user_id FK
        int company_id FK
        varchar role
        boolean verified
    }
```

---

## Домен SERVICE

### Таблицы и связи

| Таблица | Записей | PK | Основные FK |
|---------|---------|----|--------------|
| service_service | 310 | id | — |
| service_servicerequest | 56,322 | id | service_id, author_id, company_id |
| service_hubform | 282 | id | service_id |
| service_hubformfield | 6,603 | id | form_id |
| service_hubformdata | 61,635 | id | request_id, field_id |
| service_expertise | 787 | id | request_id, expert_id |
| service_protocol | 104 | id | — |
| service_report | 13,110 | id | request_id |
| service_pitchinggrade | 1,538 | id | request_id |
| service_vote | 12,945 | id | request_id, user_id |

### ER-диаграмма SERVICE

```mermaid
erDiagram
    service_service ||--o{ service_servicerequest : "заявки"
    service_service ||--o{ service_hubform : "формы"
    service_hubform ||--o{ service_hubformfield : "поля"
    service_hubform ||--o{ service_hubformstep : "шаги"
    service_servicerequest ||--o{ service_hubformdata : "данные"
    service_hubformfield ||--o{ service_hubformdata : "значения"
    service_servicerequest ||--o{ service_expertise : "экспертизы"
    service_servicerequest ||--o{ service_report : "отчёты"
    service_servicerequest ||--o{ service_servicerequeststatus : "история"
    service_servicerequest ||--o{ service_pitchinggrade : "оценки питчинга"
    service_servicerequest ||--o{ service_vote : "голоса"

    service_service {
        int id PK
        varchar code UK
        jsonb name
        jsonb description
        boolean is_active
    }

    service_servicerequest {
        int id PK
        int service_id FK
        int author_id FK
        int company_id FK
        varchar status
        jsonb data
        timestamp created_at
    }

    service_hubform {
        int id PK
        int service_id FK
        varchar code
        boolean is_active
    }

    service_hubformfield {
        int id PK
        int form_id FK
        varchar field_type
        jsonb label
        boolean required
        int order
    }

    service_hubformdata {
        int id PK
        int request_id FK
        int field_id FK
        jsonb value
    }

    service_expertise {
        int id PK
        int request_id FK
        int expert_id FK
        int score
        text comment
    }
```

---

## Домен CORE

### Таблицы и связи

| Таблица | Записей | PK | Основные FK |
|---------|---------|----|--------------|
| core_event | 1,459 | id | author_id, company_id, organization_id |
| core_eventparticipant | 864 | id | event_id, user_id |
| core_vacancy | 1,205 | id | author_id, company_id |
| core_vacancycandidate | 5,344 | id | vacancy_id, user_id |
| core_blog | 1,801 | id | author_id, company_id |
| core_article | 83 | id | author_id |
| core_comment | 2,585 | id | author_id (полиморфная связь) |
| core_feed | 4,789 | id | (полиморфная связь) |
| core_notification | 1,233 | id | user_id |
| core_actionlog | 124,987 | id | user_id |

### ER-диаграмма CORE

```mermaid
erDiagram
    account_user ||--o{ core_event : "создаёт"
    account_company ||--o{ core_event : "организует"
    core_event ||--o{ core_eventparticipant : "участники"
    account_user ||--o{ core_eventparticipant : "регистрируется"

    account_company ||--o{ core_vacancy : "размещает"
    core_vacancy ||--o{ core_vacancycandidate : "отклики"
    account_user ||--o{ core_vacancycandidate : "откликается"

    account_user ||--o{ core_blog : "пишет"
    account_company ||--o{ core_blog : "публикует"

    core_event {
        int id PK
        jsonb title
        jsonb content
        varchar event_type
        varchar event_format
        varchar status
        timestamp start_date
        timestamp end_date
        int author_id FK
        int company_id FK
    }

    core_vacancy {
        int id PK
        jsonb title
        jsonb content
        varchar vacancy_type
        varchar status
        int salary_from
        int salary_to
        int company_id FK
        int author_id FK
    }

    core_blog {
        int id PK
        jsonb title
        jsonb content
        varchar status
        int author_id FK
        int company_id FK
    }

    core_eventparticipant {
        int id PK
        int event_id FK
        int user_id FK
        timestamp created_at
    }

    core_vacancycandidate {
        int id PK
        int vacancy_id FK
        int user_id FK
        text cover_letter
        timestamp created_at
    }
```

---

## Домен BOOKING

### ER-диаграмма BOOKING

```mermaid
erDiagram
    booking_room ||--o{ booking_booking : "бронирования"
    account_user ||--o{ booking_booking : "бронирует"
    booking_room ||--o{ booking_worktime : "расписание"

    booking_room {
        int id PK
        varchar name
        varchar description
        int capacity
        boolean is_active
    }

    booking_booking {
        int id PK
        int room_id FK
        int user_id FK
        timestamp start_time
        timestamp end_time
        varchar status
        timestamp created_at
    }

    booking_worktime {
        int id PK
        int room_id FK
        int day_of_week
        time start_time
        time end_time
    }
```

---

## Домен TECHORDA

### ER-диаграмма TECHORDA

```mermaid
erDiagram
    techorda_program ||--o{ techorda_stream : "потоки"
    techorda_stream ||--o{ service_techordastudent : "студенты"
    techorda_school ||--o{ techorda_stream : "проводит"
    account_user ||--o{ service_techordastudent : "обучается"

    techorda_program {
        int id PK
        varchar name
        varchar description
        boolean is_active
    }

    techorda_stream {
        int id PK
        int program_id FK
        int school_id FK
        date start_date
        date end_date
        varchar status
    }

    techorda_school {
        int id PK
        varchar name
        varchar city
    }

    service_techordastudent {
        int id PK
        int stream_id FK
        int user_id FK
        int request_id FK
        varchar status
    }
```

---

## Полиморфные связи

### core_comment (Комментарии)

Комментарии могут быть привязаны к разным типам контента через комбинацию полей:

| Поле | Описание |
|------|----------|
| source | Тип контента: 'event', 'vacancy', 'blog', 'article' |
| primary_key | ID записи в соответствующей таблице |

```
core_comment
├── source='event' + primary_key=123 → core_event.id=123
├── source='vacancy' + primary_key=456 → core_vacancy.id=456
└── source='blog' + primary_key=789 → core_blog.id=789
```

### core_feed (Лента)

Аналогично комментариям, лента агрегирует разные типы контента.

---

## Мультиязычные поля (JSONB)

Многие текстовые поля хранят данные на трёх языках:

```json
{
  "ru": "Текст на русском",
  "kk": "Қазақша мәтін",
  "en": "English text"
}
```

**Таблицы с мультиязычностью:**

| Таблица | Поля |
|---------|------|
| core_event | title, content, address |
| core_vacancy | title, content, requirements |
| core_blog | title, content |
| core_article | title, content |
| service_service | name, description |
| service_hubformfield | label, placeholder, help_text |
| core_category | name |
| core_city | name |

---

## Теги как JSONB

Теги компаний и пользователей хранятся в JSONB-полях:

```json
{
  "status": "active",
  "date_from": "2024-01-15",
  "date_to": null,
  "data": {
    "certificate_number": "123",
    "approved_by": 456
  }
}
```

**Проверка активного тега:**
```
tag_it_company->>'status' = 'active'
```

---

## Индексы и производительность

### Рекомендуемые индексы для аналитики

| Таблица | Поля | Назначение |
|---------|------|------------|
| account_user | created_at | Динамика регистраций |
| account_user | role | Фильтрация по ролям |
| account_company | created_at | Динамика регистраций |
| service_servicerequest | status, created_at | Аналитика заявок |
| service_servicerequest | service_id | Группировка по услугам |
| core_event | status, start_date | Активные события |
| core_vacancy | status, created_at | Активные вакансии |
| booking_booking | status, start_time | Активные брони |

---

## Сводка по доменам

| Домен | Таблиц | Ключевые сущности |
|-------|--------|-------------------|
| ACCOUNT | 16 | user, company, usercompany |
| SERVICE | 34 | service, servicerequest, hubform, hubformdata |
| CORE | 27 | event, vacancy, blog, comment |
| BOOKING | 3 | room, booking |
| TECHORDA | 7 | program, stream, school |
| NIOKR | 5 | project, request |
| SHARED | 6 | file, region |
| *Технические* | 54 | auth, django, logs |

---

## Возврат к содержанию

[README.md](README.md) — Главная страница документации
