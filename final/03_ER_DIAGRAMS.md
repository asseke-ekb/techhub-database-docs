# TechHub - ER-диаграммы

> **Примечание:** Диаграммы в формате Mermaid. Для просмотра используйте:
> - GitHub / GitLab (рендерит автоматически)
> - VS Code с расширением "Markdown Preview Mermaid Support"
> - https://mermaid.live (онлайн-редактор)
> - Confluence / Notion (поддерживают Mermaid)

---

## 1. Общая диаграмма связей (High-Level)

```mermaid
erDiagram
    USER ||--o{ USERCOMPANY : "работает в"
    COMPANY ||--o{ USERCOMPANY : "имеет сотрудников"

    USER ||--o{ EVENT : "создаёт"
    USER ||--o{ VACANCY : "публикует"
    USER ||--o{ BLOG : "пишет"
    USER ||--o{ BOOKING : "бронирует"
    USER ||--o{ SERVICEREQUEST : "подаёт"

    COMPANY ||--o{ EVENT : "организует"
    COMPANY ||--o{ VACANCY : "размещает"
    COMPANY ||--o{ SERVICEREQUEST : "заявитель"

    SERVICE ||--o{ SERVICEREQUEST : "имеет заявки"

    ROOM ||--o{ BOOKING : "бронируется"

    USER {
        int id PK
        string email UK
        string phone UK
        string first_name
        string last_name
        string role
        boolean is_active
    }

    COMPANY {
        int id PK
        string tin UK
        string name
        string company_type
        string status
        boolean verified
    }

    SERVICE {
        int id PK
        string code UK
        jsonb data
    }

    SERVICEREQUEST {
        int id PK
        string status
        int service_id FK
        int company_id FK
        int author_id FK
    }

    EVENT {
        int id PK
        jsonb title
        string status
        timestamp datetime_start
        boolean published
    }

    VACANCY {
        int id PK
        jsonb title
        string status
        int salary_min
        int salary_max
    }

    BLOG {
        int id PK
        jsonb title
        jsonb content
        string status
        boolean published
    }

    BOOKING {
        int id PK
        string status
        timestamp start
        timestamp end
        int room_id FK
    }

    ROOM {
        int id PK
        string name
        int floor
        int max_people
    }
```

---

## 2. Модуль Account (Пользователи и Компании)

```mermaid
erDiagram
    ORGANIZATION ||--o{ USER : "сотрудники"

    USER ||--o{ USERCOMPANY : "связи с компаниями"
    USER ||--o{ ACTIVATION : "коды активации"
    USER ||--o{ EDUCATION : "образование"
    USER ||--o{ EXPERIENCE : "опыт работы"
    USER ||--o{ CERTIFICATE : "сертификаты"
    USER }o--|| COMPANY : "основная компания"

    COMPANY ||--o{ USERCOMPANY : "сотрудники"
    COMPANY ||--o{ COMPLAINT : "жалобы"
    USER ||--o{ COMPLAINT : "автор жалобы"

    USER {
        int id PK
        string email UK
        string phone UK
        string iin
        string first_name
        string last_name
        string role
        boolean is_active
        boolean blocked
        boolean email_verified
        boolean phone_verified
        int company_id FK
        string organization_id FK
        jsonb data
        jsonb tags
        timestamp created_at
    }

    COMPANY {
        int id PK
        string tin UK
        string name
        string short_name
        string company_type
        string status
        boolean verified
        string address
        string email
        string phone
        jsonb tag_startup
        jsonb tag_it_company
        jsonb tag_techpark
        int author_id FK
        timestamp created_at
    }

    USERCOMPANY {
        int id PK
        int user_id FK
        int company_id FK
        string role
        boolean verified
    }

    ORGANIZATION {
        string code PK
        jsonb name
        boolean active
    }

    ACTIVATION {
        uuid uuid PK
        string email
        string phone
        string code
        string type
        boolean is_active
        int iteration
        int user_id FK
    }

    EDUCATION {
        int id PK
        string name
        string degree
        int graduation_year
        int user_id FK
    }

    EXPERIENCE {
        int id PK
        string name
        string position
        date start_date
        date end_date
        int user_id FK
        int company_id FK
    }

    CERTIFICATE {
        int id PK
        string name
        string organization
        date issue_date
        int user_id FK
    }

    COMPLAINT {
        int id PK
        string reason
        string comment
        int author_id FK
        int user_id FK
        int company_id FK
    }
```

---

## 3. Модуль Service (Государственные услуги)

```mermaid
erDiagram
    ORGANIZATION ||--o{ SERVICE : "владелец"
    SERVICE ||--|| HUBFORM : "форма заявки"
    SERVICE ||--o{ SERVICEREQUEST : "заявки"

    SERVICEREQUEST ||--|| HUBFORMDATA : "данные формы"
    SERVICEREQUEST ||--o{ EXPERTISE : "экспертизы"
    SERVICEREQUEST ||--o{ VOTE : "голоса"
    SERVICEREQUEST ||--o{ REPORT : "отчёты"
    SERVICEREQUEST ||--o{ REQUESTLOG : "история"
    SERVICEREQUEST }o--|| USER : "автор"
    SERVICEREQUEST }o--|| COMPANY : "компания"
    SERVICEREQUEST }o--o| USER : "исполнитель"
    SERVICEREQUEST }o--o| USER : "эксперт"
    SERVICEREQUEST }o--o| SERVICEREQUEST : "родительская"

    HUBFORM ||--o{ HUBFORMSTEP : "шаги"
    HUBFORMSTEP ||--o{ HUBFORMFIELD : "поля"

    USER ||--o{ EXPERTISE : "проводит"
    USER ||--o{ VOTE : "голосует"
    USER ||--o{ REPORT : "создаёт"

    SERVICE {
        int id PK
        string code UK
        jsonb data
        string organization_id FK
        int hub_form_id FK
    }

    SERVICEREQUEST {
        int id PK
        string status
        int service_id FK
        int author_id FK
        int company_id FK
        int assignee_id FK
        int expert_id FK
        int hub_form_data_id FK
        int parent_id FK
        jsonb data
        timestamp created_at
        timestamp updated_at
    }

    HUBFORM {
        int id PK
        string organization_id FK
        jsonb data
    }

    HUBFORMDATA {
        int id PK
        int hub_form_id FK
        jsonb data
    }

    HUBFORMSTEP {
        int id PK
        int hub_form_id FK
        jsonb data
        int position
    }

    HUBFORMFIELD {
        int id PK
        int hub_form_step_id FK
        string field_type
        jsonb data
        int position
    }

    EXPERTISE {
        int id PK
        int request_id FK
        int user_id FK
        string status
        jsonb data
    }

    VOTE {
        int id PK
        int request_id FK
        int user_id FK
        string decision
        text comment
    }

    REPORT {
        int id PK
        int request_id FK
        int author_id FK
        jsonb data
    }

    REQUESTLOG {
        int id PK
        int request_id FK
        string action
        jsonb data
        timestamp created_at
    }

    USER {
        int id PK
        string email
        string first_name
        string last_name
    }

    COMPANY {
        int id PK
        string name
        string tin
    }

    ORGANIZATION {
        string code PK
        jsonb name
    }
```

---

## 4. Модуль Core (Контент)

```mermaid
erDiagram
    USER ||--o{ EVENT : "создаёт"
    USER ||--o{ VACANCY : "публикует"
    USER ||--o{ BLOG : "пишет"
    USER ||--o{ ARTICLE : "пишет"
    USER ||--o{ TECHTASK : "создаёт"
    USER ||--o{ COMMENT : "комментирует"
    USER ||--o{ DISCUSSION : "обсуждает"

    COMPANY ||--o{ EVENT : "организует"
    COMPANY ||--o{ VACANCY : "размещает"
    COMPANY ||--o{ BLOG : "от имени"

    ORGANIZATION ||--o{ EVENT : "организует"

    CATEGORY ||--o{ BLOG : "категория"
    CITY ||--o{ VACANCY : "город"

    EVENT ||--o{ EVENTPARTICIPANT : "участники"
    VACANCY ||--o{ VACANCYCANDIDATE : "отклики"
    TECHTASK ||--o{ TECHTASKSOLUTION : "решения"

    USER ||--o{ EVENTPARTICIPANT : "участвует"
    USER ||--o{ VACANCYCANDIDATE : "откликается"
    USER ||--o{ TECHTASKSOLUTION : "решает"

    EVENT {
        int id PK
        jsonb title
        jsonb content
        string slug UK
        string status
        string event_type
        string event_format
        timestamp datetime_start
        timestamp datetime_end
        boolean published
        int view_count
        int author_id FK
        int company_id FK
        string organization_id FK
    }

    VACANCY {
        int id PK
        jsonb title
        jsonb description
        string status
        string vacancy_type
        int salary_min
        int salary_max
        boolean published
        int author_id FK
        int company_id FK
        int city_id FK
    }

    BLOG {
        int id PK
        jsonb title
        jsonb subtitle
        jsonb content
        string slug UK
        string status
        boolean published
        int view_count
        array tags
        int author_id FK
        int company_id FK
        int category_id FK
    }

    ARTICLE {
        int id PK
        jsonb title
        jsonb content
        string slug UK
        string status
        boolean published
        int author_id FK
    }

    TECHTASK {
        int id PK
        jsonb title
        jsonb description
        string status
        boolean published
        int author_id FK
    }

    DISCUSSION {
        int id PK
        jsonb title
        jsonb content
        string status
        int author_id FK
    }

    COMMENT {
        int id PK
        text message
        string source
        string primary_key
        string status
        int user_id FK
        int parent_id FK
    }

    EVENTPARTICIPANT {
        int id PK
        int event_id FK
        int author_id FK
        string status
    }

    VACANCYCANDIDATE {
        int id PK
        int vacancy_id FK
        int author_id FK
        string status
        jsonb data
    }

    TECHTASKSOLUTION {
        int id PK
        int tech_task_id FK
        int author_id FK
        text solution
    }

    CATEGORY {
        int id PK
        jsonb name
        string slug UK
        boolean is_active
    }

    CITY {
        int id PK
        string name
        string name_ru
        string name_kk
        string name_en
    }

    USER {
        int id PK
        string email
        string first_name
        string last_name
    }

    COMPANY {
        int id PK
        string name
    }

    ORGANIZATION {
        string code PK
        jsonb name
    }
```

---

## 5. Модуль Booking (Бронирование)

```mermaid
erDiagram
    USER ||--o{ BOOKING : "бронирует"
    COMPANY ||--o{ BOOKING : "от имени"
    ROOM ||--o{ BOOKING : "бронируется"
    BOOKING ||--o{ BOOKINGSTATUS : "история статусов"

    ROOM {
        int id PK
        string name
        smallint floor
        smallint max_people
        string pavilion
        boolean is_active
        string external_id
    }

    BOOKING {
        int id PK
        string status
        string title
        timestamp start
        timestamp end
        string full_name
        string email
        string phone
        int room_id FK
        int author_id FK
        int company_id FK
        timestamp created_at
    }

    BOOKINGSTATUS {
        int id PK
        string status
        timestamp created_at
        int booking_id FK
    }

    USER {
        int id PK
        string email
        string first_name
        string last_name
    }

    COMPANY {
        int id PK
        string name
    }
```

---

## 6. Модуль TechOrda (Образование)

```mermaid
erDiagram
    COMPANY ||--o{ SCHOOL : "провайдер"
    USER ||--o{ SCHOOL : "создатель"

    SCHOOL ||--o{ COURSE : "курсы"
    FLOW ||--o{ COURSE : "поток"
    COURSE ||--o{ COURSEAPPLICATION : "заявки"

    HUBFORM ||--o{ COURSEAPPLICATION : "форма заявки"

    SCHOOL {
        int id PK
        jsonb name
        jsonb description
        string status
        int author_id FK
        int company_id FK
    }

    COURSE {
        int id PK
        jsonb name
        jsonb description
        string status
        timestamp start_date
        timestamp end_date
        int school_id FK
        int flow_id FK
    }

    FLOW {
        int id PK
        string name
        int year
    }

    COURSEAPPLICATION {
        int id PK
        string status
        int course_id FK
        int flow_id FK
        int form_id FK
    }

    HUBFORM {
        int id PK
        jsonb data
    }

    USER {
        int id PK
        string first_name
        string last_name
    }

    COMPANY {
        int id PK
        string name
    }
```

---

## 7. Полиморфные связи

### core_comment (Комментарии)

Комментарии используют полиморфную связь для привязки к разным сущностям:

```
┌─────────────────────────────────────────────────────────────────┐
│                    POLYMORPHIC: core_comment                     │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  source = 'blog'     + primary_key ──────► core_blog.id         │
│  source = 'event'    + primary_key ──────► core_event.id        │
│  source = 'vacancy'  + primary_key ──────► core_vacancy.id      │
│  source = 'techtask' + primary_key ──────► core_techtask.id     │
│  source = 'discussion' + primary_key ───► core_discussion.id    │
│                                                                  │
│  parent_id FK ──────► core_comment.id (вложенные комментарии)   │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### core_feed (Лента)

Лента агрегирует контент из разных источников:

```
┌─────────────────────────────────────────────────────────────────┐
│                    POLYMORPHIC: core_feed                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  source = 'blog'       ──► blog_id FK                           │
│  source = 'event'      ──► event_id FK                          │
│  source = 'article'    ──► article_id FK                        │
│  source = 'techtask'   ──► tech_task_id FK                      │
│  source = 'discussion' ──► discussion_id FK                     │
│  source = 'vacancy'    ──► vacancy_id FK                        │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 8. Матрица связей

|  | user | company | event | vacancy | blog | service_request | booking |
|--|------|---------|-------|---------|------|-----------------|---------|
| **user** | - | M:N | 1:N | 1:N | 1:N | 1:N | 1:N |
| **company** | M:N | - | 1:N | 1:N | 1:N | 1:N | 1:N |
| **event** | N:1 | N:1 | - | - | - | - | - |
| **vacancy** | N:1 | N:1 | - | - | - | - | - |
| **blog** | N:1 | N:1 | - | - | - | - | - |
| **service_request** | N:1 | N:1 | - | - | - | - | - |
| **booking** | N:1 | N:1 | - | - | - | - | - |

**Легенда:**
- `1:N` — один ко многим
- `N:1` — многие к одному
- `M:N` — многие ко многим (через промежуточную таблицу)

---

*Далее: [04_DICTIONARIES.md](04_DICTIONARIES.md) — Справочники значений*
