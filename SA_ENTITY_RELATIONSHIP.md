# Матрица связей между сущностями
## Информационная система TechHub

**Версия:** 1.0
**Дата:** 2025-12-04

---

## 1. Матрица связей (Relationship Matrix)

### 1.1. Основные сущности

|  | account_user | account_company | core_event | core_vacancy | core_blog | service_request | booking |
|--|--------------|-----------------|------------|--------------|-----------|-----------------|---------|
| **account_user** | - | M:N (usercompany) | 1:N (author) | 1:N (author) | 1:N (author) | 1:N (author) | 1:N (author) |
| **account_company** | M:N (usercompany) | - | 1:N (company) | 1:N (company) | 1:N (company) | 1:N (company) | 1:N (company) |
| **core_event** | N:1 (author) | N:1 (company) | - | - | - | - | - |
| **core_vacancy** | N:1 (author) | N:1 (company) | - | - | - | - | - |
| **core_blog** | N:1 (author) | N:1 (company) | - | - | - | - | - |
| **service_request** | N:1 (author) | N:1 (company) | - | - | - | - | - |
| **booking** | N:1 (author) | N:1 (company) | - | - | - | - | - |

**Легенда:**
- `1:N` - один ко многим
- `N:1` - многие к одному
- `M:N` - многие ко многим
- `-` - нет прямой связи

---

## 2. Детализация связей по модулям

### 2.1. Модуль Account (Пользователи и компании)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         ACCOUNT MODULE RELATIONSHIPS                         │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│                        ┌─────────────────┐                                  │
│                        │ core_organization│                                  │
│                        │     (45 записей)│                                  │
│                        └────────┬────────┘                                  │
│                                 │                                            │
│                                 │ 1:N (organization_id)                      │
│                                 ▼                                            │
│  ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐         │
│  │ account_        │    │  account_user   │    │   account_      │         │
│  │ activation      │───▶│   (54K записей) │◀───│  certificate    │         │
│  │ (1.8K записей)  │    └────────┬────────┘    │   (1 запись)    │         │
│  │                 │             │              └─────────────────┘         │
│  │ user_id FK      │             │                                          │
│  └─────────────────┘             │                                          │
│                                  │                                          │
│                    ┌─────────────┼─────────────┐                            │
│                    │             │             │                            │
│                    ▼             ▼             ▼                            │
│           ┌──────────────┐ ┌──────────┐ ┌──────────────┐                   │
│           │account_      │ │account_  │ │ account_     │                   │
│           │education     │ │experience│ │   course     │                   │
│           │(1 запись)    │ │(0 записей│ │ (1 запись)   │                   │
│           │              │ │          │ │              │                   │
│           │ user_id FK   │ │user_id FK│ │ user_id FK   │                   │
│           └──────────────┘ └──────────┘ └──────────────┘                   │
│                                  │                                          │
│                                  │ company_id FK (N:1)                      │
│                                  ▼                                          │
│                        ┌─────────────────┐                                  │
│                        │ account_company │                                  │
│                        │  (6.6K записей) │                                  │
│                        └────────┬────────┘                                  │
│                                 │                                            │
│                                 │                                            │
│           ┌─────────────────────┼─────────────────────┐                     │
│           │                     │                     │                     │
│           ▼                     ▼                     ▼                     │
│  ┌─────────────────┐   ┌─────────────────┐   ┌─────────────────┐          │
│  │ account_        │   │ account_        │   │ account_        │          │
│  │ usercompany     │   │ usercompany     │   │ complaint       │          │
│  │ (4.5K записей)  │   │ invitation      │   │ (20 записей)    │          │
│  │                 │   │ (2 записи)      │   │                 │          │
│  │ user_id FK      │   │                 │   │ company_id FK   │          │
│  │ company_id FK   │   │ company_id FK   │   │ user_id FK      │          │
│  │                 │   │ author_id FK    │   │ author_id FK    │          │
│  └─────────────────┘   │ invited_user FK │   └─────────────────┘          │
│                        └─────────────────┘                                  │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 2.2. Модуль Service (Государственные услуги)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         SERVICE MODULE RELATIONSHIPS                         │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌─────────────────┐         ┌─────────────────┐                           │
│  │ core_organization│────────▶│ service_service │                           │
│  │                 │  1:N     │  (310 записей)  │                           │
│  └─────────────────┘         └────────┬────────┘                           │
│                                       │                                      │
│                                       │ 1:N (service_id)                     │
│                                       ▼                                      │
│  ┌─────────────────┐         ┌─────────────────┐         ┌───────────────┐ │
│  │  account_user   │────────▶│ service_        │◀────────│account_company│ │
│  │                 │  1:N    │ servicerequest  │   N:1   │               │ │
│  │                 │ author  │  (56K записей)  │ company │               │ │
│  └─────────────────┘         └────────┬────────┘         └───────────────┘ │
│         │                             │                                      │
│         │ 1:N (assignee, expert)      │                                      │
│         └─────────────────────────────┤                                      │
│                                       │                                      │
│         ┌─────────────────────────────┼─────────────────────────────┐       │
│         │                             │                             │       │
│         ▼                             ▼                             ▼       │
│  ┌─────────────────┐         ┌─────────────────┐         ┌───────────────┐ │
│  │ service_        │         │ service_        │         │ service_      │ │
│  │ expertise       │         │ report          │         │ vote          │ │
│  │ (787 записей)   │         │ (13K записей)   │         │ (13K записей) │ │
│  │                 │         │                 │         │               │ │
│  │ request_id FK   │         │ request_id FK   │         │ request_id FK │ │
│  │ user_id FK      │         │ author_id FK    │         │ user_id FK    │ │
│  └─────────────────┘         └─────────────────┘         └───────────────┘ │
│                                       │                                      │
│                                       │ hub_form_data_id FK                  │
│                                       ▼                                      │
│                              ┌─────────────────┐                            │
│                              │ service_        │                            │
│                              │ hubformdata     │                            │
│                              │ (62K записей)   │                            │
│                              └────────┬────────┘                            │
│                                       │                                      │
│                                       │ hub_form_id FK                       │
│                                       ▼                                      │
│                              ┌─────────────────┐                            │
│                              │ service_hubform │                            │
│                              │ (282 записи)    │                            │
│                              └────────┬────────┘                            │
│                                       │                                      │
│                                       │ 1:N                                  │
│                                       ▼                                      │
│                              ┌─────────────────┐                            │
│                              │ service_        │                            │
│                              │ hubformstep     │                            │
│                              │ (569 записей)   │                            │
│                              └────────┬────────┘                            │
│                                       │                                      │
│                                       │ 1:N                                  │
│                                       ▼                                      │
│                              ┌─────────────────┐                            │
│                              │ service_        │                            │
│                              │ hubformfield    │                            │
│                              │ (6.6K записей)  │                            │
│                              └─────────────────┘                            │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 2.3. Модуль Core (Контент)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          CORE MODULE RELATIONSHIPS                           │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌─────────────────┐                                    ┌─────────────────┐ │
│  │  account_user   │                                    │ account_company │ │
│  │   (author)      │                                    │   (company)     │ │
│  └────────┬────────┘                                    └────────┬────────┘ │
│           │                                                      │          │
│           │ 1:N                                            N:1   │          │
│           │                                                      │          │
│           ▼                                                      ▼          │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                         CONTENT ENTITIES                             │   │
│  │                                                                      │   │
│  │  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  ┌──────────┐ │   │
│  │  │  core_event  │  │ core_vacancy │  │  core_blog   │  │core_     │ │   │
│  │  │ (1.4K)       │  │  (1.2K)      │  │  (1.8K)      │  │techtask  │ │   │
│  │  │              │  │              │  │              │  │(247)     │ │   │
│  │  │ author_id FK │  │ author_id FK │  │ author_id FK │  │author_id │ │   │
│  │  │ company_id FK│  │ company_id FK│  │ company_id FK│  │   FK     │ │   │
│  │  │ org_id FK    │  │ city_id FK   │  │ category_id  │  │          │ │   │
│  │  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘  └────┬─────┘ │   │
│  │         │                 │                 │               │       │   │
│  └─────────┼─────────────────┼─────────────────┼───────────────┼───────┘   │
│            │                 │                 │               │            │
│            │                 │                 │               │            │
│            ▼                 ▼                 │               ▼            │
│  ┌──────────────────┐ ┌──────────────────┐    │    ┌──────────────────┐   │
│  │core_event        │ │core_vacancy      │    │    │core_techtask     │   │
│  │  participant     │ │   candidate      │    │    │    solution      │   │
│  │ (864 записи)     │ │ (5.3K записей)   │    │    │ (232 записи)     │   │
│  │                  │ │                  │    │    │                  │   │
│  │ event_id FK      │ │ vacancy_id FK    │    │    │ tech_task_id FK  │   │
│  │ author_id FK     │ │ author_id FK     │    │    │ author_id FK     │   │
│  └──────────────────┘ └──────────────────┘    │    └──────────────────┘   │
│                                               │                            │
│                                               ▼                            │
│                                    ┌──────────────────┐                   │
│                                    │  core_category   │                   │
│                                    │  (14 записей)    │                   │
│                                    └──────────────────┘                   │
│                                                                            │
│  ┌─────────────────────────────────────────────────────────────────────┐  │
│  │                    POLYMORPHIC: core_comment                         │  │
│  │                                                                      │  │
│  │  source = 'blog'     + primary_key ──────▶ core_blog.id             │  │
│  │  source = 'event'    + primary_key ──────▶ core_event.id            │  │
│  │  source = 'vacancy'  + primary_key ──────▶ core_vacancy.id          │  │
│  │  source = 'techtask' + primary_key ──────▶ core_techtask.id         │  │
│  │                                                                      │  │
│  │  parent_id FK ──────▶ core_comment.id (для вложенных комментариев)  │  │
│  │                                                                      │  │
│  └─────────────────────────────────────────────────────────────────────┘  │
│                                                                            │
│  ┌─────────────────────────────────────────────────────────────────────┐  │
│  │                    POLYMORPHIC: core_feed                            │  │
│  │                                                                      │  │
│  │  source = 'blog'       ──▶ blog_id FK                               │  │
│  │  source = 'event'      ──▶ event_id FK                              │  │
│  │  source = 'article'    ──▶ article_id FK                            │  │
│  │  source = 'techtask'   ──▶ tech_task_id FK                          │  │
│  │  source = 'discussion' ──▶ discussion_id FK                         │  │
│  │  source = 'vacancy'    ──▶ vacancy_id FK                            │  │
│  │                                                                      │  │
│  └─────────────────────────────────────────────────────────────────────┘  │
│                                                                            │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 2.4. Модуль Booking (Бронирование)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        BOOKING MODULE RELATIONSHIPS                          │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌─────────────────┐                           ┌─────────────────┐          │
│  │  account_user   │                           │ account_company │          │
│  └────────┬────────┘                           └────────┬────────┘          │
│           │                                             │                    │
│           │ 1:N (author_id)                       N:1   │ (company_id)       │
│           │                                             │                    │
│           └──────────────────┬──────────────────────────┘                    │
│                              │                                               │
│                              ▼                                               │
│  ┌─────────────────┐  ┌─────────────────┐                                   │
│  │  booking_room   │──│ booking_booking │                                   │
│  │  (16 записей)   │  │  (8.6K записей) │                                   │
│  │                 │  │                 │                                   │
│  │                 │  │ room_id FK      │                                   │
│  │                 │  │ author_id FK    │                                   │
│  │                 │  │ company_id FK   │                                   │
│  └─────────────────┘  └────────┬────────┘                                   │
│         │                      │                                             │
│         │ 1:N                  │ 1:N                                         │
│         │                      ▼                                             │
│         │              ┌─────────────────┐                                   │
│         │              │booking_booking  │                                   │
│         │              │    status       │                                   │
│         │              │ (8.7K записей)  │                                   │
│         │              │                 │                                   │
│         │              │ booking_id FK   │                                   │
│         │              └─────────────────┘                                   │
│         │                                                                    │
│         └─ Комнаты: C3 (этаж 3), C4 (этаж 4), etc.                          │
│            Вместимость: от 4 до 100+ человек                                 │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 2.5. Модуль TechOrda (Образование)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        TECHORDA MODULE RELATIONSHIPS                         │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌─────────────────┐                           ┌─────────────────┐          │
│  │  account_user   │                           │ account_company │          │
│  └────────┬────────┘                           └────────┬────────┘          │
│           │                                             │                    │
│           │ 1:N (author_id)                       N:1   │ (company_id)       │
│           │                                             │                    │
│           └──────────────────┬──────────────────────────┘                    │
│                              │                                               │
│                              ▼                                               │
│                     ┌─────────────────┐                                     │
│                     │ techorda_school │                                     │
│                     │  (82 записи)    │                                     │
│                     │                 │                                     │
│                     │ author_id FK    │                                     │
│                     │ company_id FK   │                                     │
│                     └────────┬────────┘                                     │
│                              │                                               │
│                              │ 1:N (school_id)                               │
│                              ▼                                               │
│  ┌─────────────────┐  ┌─────────────────┐                                   │
│  │ techorda_flow   │──│ techorda_course │                                   │
│  │  (4 записи)     │  │  (203 записи)   │                                   │
│  │                 │  │                 │                                   │
│  │                 │  │ school_id FK    │                                   │
│  │                 │  │ flow_id FK      │                                   │
│  └─────────────────┘  └────────┬────────┘                                   │
│         │                      │                                             │
│         │ 1:N (flow_id)        │ 1:N (course_id)                             │
│         │                      ▼                                             │
│         │              ┌─────────────────┐                                   │
│         │              │techorda_course  │                                   │
│         └─────────────▶│  application    │                                   │
│                        │ (15 записей)    │                                   │
│                        │                 │                                   │
│                        │ course_id FK    │                                   │
│                        │ flow_id FK      │                                   │
│                        │ form_id FK      │                                   │
│                        └─────────────────┘                                   │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Список всех Foreign Key связей

### 3.1. Связи с account_user

| Таблица | Поле FK | Описание |
|---------|---------|----------|
| account_activation | user_id | Пользователь для активации |
| account_certificate | user_id | Владелец сертификата |
| account_company | author_id | Создатель компании |
| account_complaint | author_id | Автор жалобы |
| account_complaint | user_id | Пользователь, на которого жалоба |
| account_contactpress | author_id | Автор контакта |
| account_contactrequest | user_id | Пользователь запроса |
| account_course | user_id | Владелец курса |
| account_education | user_id | Владелец образования |
| account_experience | user_id | Владелец опыта |
| account_usercompany | user_id | Пользователь в связи |
| account_usercompanyinvitation | author_id | Автор приглашения |
| account_usercompanyinvitation | invited_user_id | Приглашённый |
| booking_booking | author_id | Автор брони |
| core_article | author_id | Автор статьи |
| core_blog | author_id | Автор блога |
| core_comment | user_id | Автор комментария |
| core_event | author_id | Автор события |
| core_eventparticipant | author_id | Участник |
| core_techtask | author_id | Автор тех.задания |
| core_vacancy | author_id | Автор вакансии |
| core_vacancycandidate | author_id | Кандидат |
| service_servicerequest | author_id | Автор заявки |
| service_servicerequest | assignee_id | Исполнитель |
| service_servicerequest | expert_id | Эксперт |
| service_expertise | user_id | Эксперт |
| service_report | author_id | Автор отчёта |
| service_vote | user_id | Голосующий |

### 3.2. Связи с account_company

| Таблица | Поле FK | Описание |
|---------|---------|----------|
| account_user | company_id | Основная компания пользователя |
| account_usercompany | company_id | Компания в связи |
| account_complaint | company_id | Компания-объект жалобы |
| booking_booking | company_id | Компания-заказчик брони |
| core_blog | company_id | Компания-автор блога |
| core_event | company_id | Компания-организатор |
| core_vacancy | company_id | Компания-работодатель |
| service_servicerequest | company_id | Компания-заявитель |
| techorda_school | company_id | Компания-провайдер |

### 3.3. Связи с core_organization

| Таблица | Поле FK | Описание |
|---------|---------|----------|
| account_user | organization_id | Организация сотрудника |
| core_event | organization_id | Организация-владелец события |
| service_service | organization_id | Организация-владелец услуги |
| service_hubform | organization_id | Организация формы |
| landing_page | organization_id | Организация лендинга |

---

## 4. Кардинальность связей (Cardinality)

| Связь | Тип | Описание |
|-------|-----|----------|
| user → company (primary) | N:1 | Пользователь может иметь одну основную компанию |
| user ↔ company (usercompany) | M:N | Пользователь может быть в нескольких компаниях |
| user → event | 1:N | Пользователь может создать много событий |
| company → event | 1:N | Компания может иметь много событий |
| user → vacancy | 1:N | Пользователь может создать много вакансий |
| company → vacancy | 1:N | Компания может иметь много вакансий |
| vacancy → candidate | 1:N | Вакансия может иметь много кандидатов |
| user → servicerequest | 1:N | Пользователь может подать много заявок |
| service → servicerequest | 1:N | Услуга может иметь много заявок |
| room → booking | 1:N | Комната может иметь много бронирований |
| school → course | 1:N | Школа может иметь много курсов |
| flow → course | 1:N | Поток может включать много курсов |
| comment → comment | 1:N | Комментарий может иметь много ответов |

---

## 5. Индексы и оптимизация

### Таблицы с наибольшим количеством индексов

| Таблица | Кол-во индексов | Основные индексы |
|---------|-----------------|------------------|
| account_user | 42 | email, phone, iin, company_id, created_at |
| core_vacancy | 24 | status, company_id, city_id, published |
| core_event | 23 | status, company_id, datetime_start, published |
| account_company | 21 | tin, status, verified, created_at |
| core_blog | 21 | status, category_id, published, author_id |
| service_servicerequest | 17 | service_id, status, author_id, company_id |

---

*Документ является частью технической документации ИС TechHub*
