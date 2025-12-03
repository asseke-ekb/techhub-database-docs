# Полный словарь данных ИС TechHub
## Все таблицы базы данных

**Версия:** 1.0
**Дата:** 2025-12-04
**Всего таблиц:** 157
**Всего FK связей:** 218

---

## Оглавление

1. [account](#account) - Управление пользователями, компаниями, аутентификацией и авторизацией
2. [admin](#admin) - Административные функции Django
3. [astanahub](#astanahub) - Общие данные платформы Астана Хаб
4. [auth](#auth) - Стандартная аутентификация Django (группы, права)
5. [authtoken](#authtoken) - API токены для REST авторизации
6. [awsdjangoses](#awsdjangoses) - Интеграция с AWS SES (email)
7. [booking](#booking) - Бронирование переговорных комнат и помещений
8. [community](#community) - Социальные связи (подписки, фолловинг)
9. [core](#core) - Основной контент: события, вакансии, блоги, статьи, тех.задания
10. [django](#django) - Системные таблицы Django (миграции, сессии, логи)
11. [explorer](#explorer) - SQL Explorer для аналитики
12. [hub](#hub) - Кэш-таблицы
13. [journeymap](#journeymap) - Карты развития для компаний и пользователей
14. [landing](#landing) - CMS для лендингов и страниц
15. [matchmaking](#matchmaking) - Нетворкинг и мэтчинг пользователей
16. [niokr](#niokr) - Научно-исследовательские проекты (НИОКР)
17. [oauth2](#oauth2) - OAuth2 авторизация
18. [reversion](#reversion) - Версионирование объектов (история изменений)
19. [search](#search) - Поисковые запросы
20. [service](#service) - Государственные услуги, заявки, формы, экспертиза
21. [shared](#shared) - Общие ресурсы (медиафайлы, SEO, контекст)
22. [silk](#silk) - Профилирование запросов (для разработки)
23. [social](#social) - Социальная авторизация (Google, Facebook и др.)
24. [techorda](#techorda) - Образовательные программы TechOrda
25. [thumbnail](#thumbnail) - Хранение превью изображений
26. [user](#user) - Сессии пользователей
27. [waffle](#waffle) - Feature flags (включение/выключение функций)

---

## account

**Описание:** Управление пользователями, компаниями, аутентификацией и авторизацией

**Таблиц в модуле:** 16

| Таблица | Записей | Описание |
|---------|---------|----------|
| `account_activation` | 1,810 | - |
| `account_certificate` | 1 | - |
| `account_company` | 6,639 | - |
| `account_complaint` | 20 | - |
| `account_contactpress` | 0 | - |
| `account_contactrequest` | 0 | - |
| `account_course` | 1 | - |
| `account_education` | 1 | - |
| `account_emaildigest` | 31,474 | - |
| `account_experience` | 0 | - |
| `account_user` | 54,063 | - |
| `account_user_groups` | 109 | - |
| `account_user_user_permissions` | 2,289 | - |
| `account_usercompany` | 4,536 | - |
| `account_usercompanyinvitation` | 2 | - |
| `account_usercompanyrequest` | 254 | - |

### account_activation

**Количество записей:** 1,810

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 2 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 3 | `uuid` | uuid | Нет | - |  |
| 4 | `email` | character varying(200) | Да | - | Электронная почта |
| 5 | `phone` | character varying(20) | Да | - | Номер телефона |
| 6 | `code` | character varying(6) | Нет | - |  |
| 7 | `is_active` | boolean | Нет | - | Признак активности |
| 8 | `iteration` | integer | Нет | - |  |
| 9 | `data` | jsonb | Нет | - | Дополнительные данные (JSON) |
| 10 | `type` | character varying(30) | Нет | - |  |
| 11 | `user_id` | integer | Да | - | FK на user |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `user_id` | `account_user.id` |

---

### account_certificate

**Количество записей:** 1

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | - | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `name` | character varying(255) | Нет | - | Наименование |
| 5 | `organization` | character varying(255) | Нет | - |  |
| 6 | `issue_date` | date | Нет | - |  |
| 7 | `user_id` | integer | Нет | - | FK на user |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `user_id` | `account_user.id` |

---

### account_company

**Количество записей:** 6,639

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('account_company_id_seq'::regcla... | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `tin` | character varying(12) | Да | - |  |
| 5 | `name` | character varying(1000) | Нет | - | Наименование |
| 6 | `address` | character varying(2000) | Нет | - |  |
| 7 | `short_name` | character varying(200) | Нет | - |  |
| 8 | `bank` | character varying(200) | Нет | - |  |
| 9 | `kbe` | smallint | Да | - |  |
| 10 | `iik` | character varying(20) | Нет | - |  |
| 11 | `bik` | character varying(20) | Нет | - |  |
| 12 | `company_type` | character varying(30) | Нет | - |  |
| 13 | `verified` | boolean | Нет | - | Признак верификации |
| 14 | `search_field` | text | Нет | - |  |
| 15 | `tag_it_company` | jsonb | Нет | - |  |
| 16 | `tag_startup` | jsonb | Нет | - |  |
| 17 | `tag_techpark` | jsonb | Нет | - |  |
| 18 | `tag_ts_member` | jsonb | Нет | - |  |
| 19 | `description` | text | Нет | - |  |
| 20 | `email` | character varying(200) | Нет | - | Электронная почта |
| 21 | `facebook_url` | character varying(200) | Нет | - |  |
| 22 | `gis_url` | character varying(200) | Нет | - |  |
| 23 | `instagram_url` | character varying(200) | Нет | - |  |
| 24 | `linkedin_url` | character varying(200) | Нет | - |  |
| 25 | `phone` | character varying(30) | Нет | - | Номер телефона |
| 26 | `website` | character varying(1000) | Нет | - |  |
| 27 | `author_id` | integer | Да | - | FK на author |
| 28 | `status` | character varying(20) | Нет | - | Статус записи |
| 29 | `image_id` | uuid | Да | - | FK на image |
| 30 | `tag_corp_partner` | jsonb | Нет | - |  |
| 31 | `city_phone` | character varying(50) | Нет | - |  |
| 32 | `director_first_name` | character varying(200) | Нет | - |  |
| 33 | `director_last_name` | character varying(200) | Нет | - |  |
| 34 | `job_fair` | boolean | Нет | - |  |
| 35 | `service_provider` | boolean | Нет | - |  |
| 36 | `games_data` | jsonb | Нет | - |  |
| 37 | `tag_nii` | jsonb | Нет | - |  |
| 38 | `tag_nedrouser` | jsonb | Нет | - |  |
| 39 | `hub_space_member` | boolean | Нет | - |  |
| 40 | `adoption` | jsonb | Нет | - |  |
| 41 | `basic_info` | jsonb | Нет | - |  |
| 42 | `company_files` | jsonb | Нет | - |  |
| 43 | `expertise` | jsonb | Нет | - |  |
| 44 | `fundraising` | jsonb | Нет | - |  |
| 45 | `headline` | character varying(220) | Да | - |  |
| 46 | `investments` | jsonb | Нет | - |  |
| 47 | `links` | jsonb | Нет | - |  |
| 48 | `profile_cover` | character varying(100) | Да | - |  |
| 49 | `questions` | jsonb | Нет | - |  |
| 50 | `revenues` | jsonb | Нет | - |  |
| 51 | `visibility_settings` | jsonb | Нет | - |  |
| 52 | `product_link` | character varying(200) | Да | - |  |
| 53 | `profile_cover_selected` | character varying | Да | - |  |
| 54 | `popularity_score` | integer | Да | - |  |
| 55 | `profile_score` | integer | Да | - |  |
| 56 | `upcoming_events_count` | integer | Да | - |  |
| 57 | `vacancies_count` | integer | Да | - |  |
| 58 | `data` | jsonb | Нет | - | Дополнительные данные (JSON) |
| 59 | `customers_market` | jsonb | Нет | - |  |
| 60 | `product_market` | jsonb | Нет | - |  |
| 61 | `team` | jsonb | Нет | - |  |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `author_id` | `account_user.id` |

---

### account_complaint

**Количество записей:** 20

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('account_complaint_id_seq'::regc... | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `reason` | character varying(100) | Нет | - |  |
| 5 | `comment` | character varying(500) | Нет | - |  |
| 6 | `author_id` | integer | Нет | - | FK на author |
| 7 | `company_id` | integer | Да | - | FK на company |
| 8 | `user_id` | integer | Да | - | FK на user |
| 9 | `viewed` | ARRAY | Нет | - |  |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `author_id` | `account_user.id` |
| `company_id` | `account_company.id` |
| `user_id` | `account_user.id` |

---

### account_contactpress

**Количество записей:** 0

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('account_contactpress_id_seq'::r... | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `author_id` | integer | Нет | - | FK на author |
| 5 | `company_id` | integer | Да | - | FK на company |
| 6 | `user_id` | integer | Да | - | FK на user |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `author_id` | `account_user.id` |
| `company_id` | `account_company.id` |
| `user_id` | `account_user.id` |

---

### account_contactrequest

**Количество записей:** 0

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('account_contactrequest_id_seq':... | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `first_name` | character varying(200) | Нет | - |  |
| 5 | `last_name` | character varying(200) | Нет | - |  |
| 6 | `email` | character varying(200) | Нет | - | Электронная почта |
| 7 | `description` | text | Нет | - |  |
| 8 | `user_id` | integer | Нет | - | FK на user |
| 9 | `phone` | character varying(200) | Нет | - | Номер телефона |
| 10 | `author_id` | integer | Да | - | FK на author |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `author_id` | `account_user.id` |
| `user_id` | `account_user.id` |

---

### account_course

**Количество записей:** 1

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | - | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `name` | character varying(255) | Нет | - | Наименование |
| 5 | `top_skills` | ARRAY | Нет | - |  |
| 6 | `graduation_date` | date | Нет | - |  |
| 7 | `user_id` | integer | Нет | - | FK на user |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `user_id` | `account_user.id` |

---

### account_education

**Количество записей:** 1

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | - | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `name` | character varying(255) | Нет | - | Наименование |
| 5 | `degree` | character varying(50) | Нет | - |  |
| 6 | `graduation_year` | integer | Нет | - |  |
| 7 | `faculty` | character varying(255) | Нет | - |  |
| 8 | `user_id` | integer | Нет | - | FK на user |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `user_id` | `account_user.id` |

---

### account_emaildigest

**Количество записей:** 31,474

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('account_emaildigest_id_seq'::re... | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `email` | character varying(200) | Нет | - | Электронная почта |
| 5 | `name` | character varying(200) | Да | - | Наименование |

---

### account_experience

**Количество записей:** 0

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | - | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `name` | character varying(255) | Нет | - | Наименование |
| 5 | `position` | character varying(255) | Нет | - |  |
| 6 | `description` | text | Нет | - |  |
| 7 | `start_date` | date | Нет | - |  |
| 8 | `current_workplace` | boolean | Нет | - |  |
| 9 | `end_date` | date | Да | - |  |
| 10 | `company_id` | integer | Да | - | FK на company |
| 11 | `user_id` | integer | Нет | - | FK на user |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `company_id` | `account_company.id` |
| `user_id` | `account_user.id` |

---

### account_user

**Количество записей:** 54,063

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('account_user_id_seq'::regclass) | Уникальный идентификатор |
| 2 | `password` | character varying(128) | Нет | - |  |
| 3 | `last_login` | timestamp with time zone | Да | - |  |
| 4 | `is_superuser` | boolean | Нет | - |  |
| 5 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 6 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 7 | `iin` | character varying(100) | Да | - |  |
| 8 | `email` | character varying(400) | Да | - | Электронная почта |
| 9 | `phone` | character varying(100) | Нет | - | Номер телефона |
| 10 | `first_name` | character varying(400) | Нет | - |  |
| 11 | `last_name` | character varying(400) | Нет | - |  |
| 12 | `role` | character varying(50) | Нет | - |  |
| 13 | `is_staff` | boolean | Нет | - |  |
| 14 | `is_active` | boolean | Нет | - | Признак активности |
| 15 | `company_id` | integer | Да | - | FK на company |
| 16 | `organization_id` | character varying(20) | Да | - | FK на organization |
| 17 | `arm_permissions` | jsonb | Нет | - |  |
| 18 | `tags` | jsonb | Нет | - |  |
| 19 | `permissions` | jsonb | Нет | - |  |
| 20 | `search_field` | text | Нет | - |  |
| 21 | `tag_investor` | jsonb | Нет | - |  |
| 22 | `data` | jsonb | Нет | - | Дополнительные данные (JSON) |
| 23 | `tag_it_specialist` | jsonb | Нет | - |  |
| 24 | `facebook_url` | character varying(1000) | Нет | - |  |
| 25 | `linkedin_url` | character varying(1000) | Нет | - |  |
| 26 | `website` | character varying(1000) | Нет | - |  |
| 27 | `tag_intern` | jsonb | Нет | - |  |
| 28 | `certificates` | jsonb | Нет | - |  |
| 29 | `universities` | jsonb | Нет | - |  |
| 30 | `image_id` | uuid | Да | - | FK на image |
| 31 | `tag_international_agent` | jsonb | Нет | - |  |
| 32 | `hook_services` | ARRAY | Нет | - |  |
| 33 | `contact_email` | character varying(400) | Да | - |  |
| 34 | `blocked` | boolean | Нет | - |  |
| 35 | `email_verified` | boolean | Нет | - |  |
| 36 | `phone_verified` | boolean | Нет | - |  |
| 37 | `tag_expert` | jsonb | Нет | - |  |
| 38 | `games_blacklist` | boolean | Нет | - |  |
| 39 | `tag_community_manager` | jsonb | Нет | - |  |
| 40 | `tag_company_member` | jsonb | Нет | - |  |
| 41 | `tag_startup_member` | jsonb | Нет | - |  |
| 42 | `tag_tracker` | jsonb | Нет | - |  |
| 43 | `games_data` | jsonb | Нет | - |  |
| 44 | `tag_ai_specialist` | jsonb | Нет | - |  |
| 45 | `tag_schoolchild` | jsonb | Нет | - |  |
| 46 | `tag_student` | jsonb | Нет | - |  |
| 47 | `tag_teacher` | jsonb | Нет | - |  |
| 48 | `tag_scientist` | jsonb | Нет | - |  |
| 49 | `egov_sign_data` | jsonb | Нет | - |  |
| 50 | `birth_date` | date | Да | - |  |
| 51 | `city` | character varying(128) | Нет | - |  |
| 52 | `country` | character varying(128) | Нет | - |  |
| 53 | `gender` | character varying(50) | Нет | - |  |
| 54 | `region` | character varying(128) | Нет | - |  |
| 55 | `work_experience` | jsonb | Нет | - |  |
| 56 | `contact_phone` | character varying(100) | Да | - |  |
| 57 | `headline` | character varying(220) | Да | - |  |
| 58 | `links` | jsonb | Нет | - |  |
| 59 | `preferences` | jsonb | Нет | - |  |
| 60 | `profile_cover` | character varying(100) | Да | - |  |
| 61 | `skills` | jsonb | Нет | - |  |
| 62 | `visibility_settings` | jsonb | Нет | - |  |
| 63 | `portfolio_url` | character varying(1000) | Нет | - |  |
| 64 | `community_role` | character varying(30) | Да | - |  |
| 65 | `profile_cover_selected` | character varying | Да | - |  |
| 66 | `specific_role` | character varying(30) | Да | - |  |
| 67 | `popularity_score` | integer | Да | - |  |
| 68 | `profile_score` | integer | Да | - |  |
| 69 | `privacy_policy_accepted` | boolean | Нет | - |  |
| 70 | `signup_flow_completed` | boolean | Нет | - |  |
| 71 | `onboarding_data` | jsonb | Нет | - |  |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `company_id` | `account_company.id` |
| `organization_id` | `core_organization.code` |

---

### account_user_groups

**Количество записей:** 109

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('account_user_groups_id_seq'::re... | Уникальный идентификатор |
| 2 | `user_id` | integer | Нет | - | FK на user |
| 3 | `group_id` | integer | Нет | - | FK на group |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `group_id` | `auth_group.id` |
| `user_id` | `account_user.id` |

---

### account_user_user_permissions

**Количество записей:** 2,289

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('account_user_user_permissions_i... | Уникальный идентификатор |
| 2 | `user_id` | integer | Нет | - | FK на user |
| 3 | `permission_id` | integer | Нет | - | FK на permission |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `permission_id` | `auth_permission.id` |
| `user_id` | `account_user.id` |

---

### account_usercompany

**Количество записей:** 4,536

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('account_usercompany_id_seq'::re... | Уникальный идентификатор |
| 2 | `company_id` | integer | Нет | - | FK на company |
| 3 | `user_id` | integer | Нет | - | FK на user |
| 4 | `verified` | boolean | Нет | - | Признак верификации |
| 5 | `role` | character varying(20) | Нет | - |  |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `company_id` | `account_company.id` |
| `user_id` | `account_user.id` |

---

### account_usercompanyinvitation

**Количество записей:** 2

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | - | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `role` | character varying(20) | Нет | - |  |
| 5 | `status` | character varying(20) | Нет | - | Статус записи |
| 6 | `company_id` | integer | Нет | - | FK на company |
| 7 | `author_id` | integer | Нет | - | FK на author |
| 8 | `invited_user_id` | integer | Нет | - | FK на invited_user |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `author_id` | `account_user.id` |
| `company_id` | `account_company.id` |
| `invited_user_id` | `account_user.id` |

---

### account_usercompanyrequest

**Количество записей:** 254

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('account_usercompanyrequest_id_s... | Уникальный идентификатор |
| 2 | `status` | character varying(20) | Нет | - | Статус записи |
| 3 | `company_id` | integer | Нет | - | FK на company |
| 4 | `user_id` | integer | Нет | - | FK на user |
| 5 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 6 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `company_id` | `account_company.id` |
| `user_id` | `account_user.id` |

---

## admin

**Описание:** Административные функции Django

**Таблиц в модуле:** 1

| Таблица | Записей | Описание |
|---------|---------|----------|
| `admin_honeypot_loginattempt` | 69,000 | - |

### admin_honeypot_loginattempt

**Количество записей:** 69,000

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('admin_honeypot_loginattempt_id_... | Уникальный идентификатор |
| 2 | `username` | character varying(255) | Да | - |  |
| 3 | `ip_address` | inet | Да | - |  |
| 4 | `session_key` | character varying(50) | Да | - |  |
| 5 | `user_agent` | text | Да | - |  |
| 6 | `timestamp` | timestamp with time zone | Нет | - |  |
| 7 | `path` | text | Да | - |  |

---

## astanahub

**Описание:** Общие данные платформы Астана Хаб

**Таблиц в модуле:** 3

| Таблица | Записей | Описание |
|---------|---------|----------|
| `astanahub_shared_contextdata` | 0 | - |
| `astanahub_shared_seodata` | 0 | - |
| `astanahub_shared_smslog` | 651 | - |

### astanahub_shared_contextdata

**Количество записей:** 0

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 2 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 3 | `key` | character varying(30) | Нет | - |  |
| 4 | `data` | jsonb | Нет | - | Дополнительные данные (JSON) |
| 5 | `description` | character varying(200) | Нет | - |  |

---

### astanahub_shared_seodata

**Количество записей:** 0

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 2 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 3 | `key` | character varying(30) | Нет | - |  |
| 4 | `title` | jsonb | Нет | - | Заголовок |
| 5 | `description` | jsonb | Нет | - |  |
| 6 | `keywords` | jsonb | Нет | - |  |

---

### astanahub_shared_smslog

**Количество записей:** 651

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | bigint | Нет | - | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `phone` | character varying(100) | Нет | - | Номер телефона |
| 5 | `request` | text | Нет | - |  |
| 6 | `response` | text | Нет | - |  |

---

## auth

**Описание:** Стандартная аутентификация Django (группы, права)

**Таблиц в модуле:** 3

| Таблица | Записей | Описание |
|---------|---------|----------|
| `auth_group` | 11 | - |
| `auth_group_permissions` | 1,114 | - |
| `auth_permission` | 625 | - |

### auth_group

**Количество записей:** 11

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('auth_group_id_seq'::regclass) | Уникальный идентификатор |
| 2 | `name` | character varying(150) | Нет | - | Наименование |

---

### auth_group_permissions

**Количество записей:** 1,114

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('auth_group_permissions_id_seq':... | Уникальный идентификатор |
| 2 | `group_id` | integer | Нет | - | FK на group |
| 3 | `permission_id` | integer | Нет | - | FK на permission |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `group_id` | `auth_group.id` |
| `permission_id` | `auth_permission.id` |

---

### auth_permission

**Количество записей:** 625

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('auth_permission_id_seq'::regcla... | Уникальный идентификатор |
| 2 | `name` | character varying(255) | Нет | - | Наименование |
| 3 | `content_type_id` | integer | Нет | - | FK на content_type |
| 4 | `codename` | character varying(100) | Нет | - |  |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `content_type_id` | `django_content_type.id` |

---

## authtoken

**Описание:** API токены для REST авторизации

**Таблиц в модуле:** 1

| Таблица | Записей | Описание |
|---------|---------|----------|
| `authtoken_token` | 1,138 | - |

### authtoken_token

**Количество записей:** 1,138

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `key` | character varying(40) | Нет | - |  |
| 2 | `created` | timestamp with time zone | Нет | - |  |
| 3 | `user_id` | integer | Нет | - | FK на user |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `user_id` | `account_user.id` |

---

## awsdjangoses

**Описание:** Интеграция с AWS SES (email)

**Таблиц в модуле:** 1

| Таблица | Записей | Описание |
|---------|---------|----------|
| `awsdjangoses_awsblacklist` | 200 | - |

### awsdjangoses_awsblacklist

**Количество записей:** 200

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `email` | character varying(500) | Нет | - | Электронная почта |
| 2 | `bounce` | boolean | Нет | - |  |
| 3 | `complaint` | boolean | Нет | - |  |

---

## booking

**Описание:** Бронирование переговорных комнат и помещений

**Таблиц в модуле:** 3

| Таблица | Записей | Описание |
|---------|---------|----------|
| `booking_booking` | 8,673 | - |
| `booking_bookingstatus` | 8,691 | - |
| `booking_room` | 16 | - |

### booking_booking

**Количество записей:** 8,673

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('booking_booking_id_seq'::regcla... | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `status` | character varying(20) | Нет | - | Статус записи |
| 5 | `full_name` | character varying(200) | Нет | - |  |
| 6 | `email` | character varying(200) | Нет | - | Электронная почта |
| 7 | `phone` | character varying(30) | Нет | - | Номер телефона |
| 8 | `company_name_old` | character varying(200) | Нет | - |  |
| 9 | `title` | character varying(100) | Нет | - | Заголовок |
| 10 | `start` | timestamp with time zone | Нет | - |  |
| 11 | `end` | timestamp with time zone | Нет | - |  |
| 12 | `author_id` | integer | Нет | - | FK на author |
| 13 | `room_id` | integer | Нет | - | FK на room |
| 14 | `data` | jsonb | Нет | - | Дополнительные данные (JSON) |
| 15 | `company_id` | integer | Да | - | FK на company |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `author_id` | `account_user.id` |
| `company_id` | `account_company.id` |
| `room_id` | `booking_room.id` |

---

### booking_bookingstatus

**Количество записей:** 8,691

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('booking_bookingstatus_id_seq'::... | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `status` | character varying(20) | Нет | - | Статус записи |
| 5 | `comment` | character varying(200) | Нет | - |  |
| 6 | `data` | jsonb | Нет | - | Дополнительные данные (JSON) |
| 7 | `booking_id` | integer | Нет | - | FK на booking |
| 8 | `start` | timestamp with time zone | Да | - |  |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `booking_id` | `booking_booking.id` |

---

### booking_room

**Количество записей:** 16

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('booking_room_id_seq'::regclass) | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `name` | character varying(50) | Нет | - | Наименование |
| 5 | `floor` | smallint | Нет | - |  |
| 6 | `max_people` | smallint | Нет | - |  |
| 7 | `external_id` | character varying(200) | Нет | - | FK на external |
| 8 | `data` | jsonb | Нет | - | Дополнительные данные (JSON) |
| 9 | `image_id` | uuid | Да | - | FK на image |
| 10 | `pavilion` | character varying(10) | Да | - |  |
| 11 | `is_active` | boolean | Нет | - | Признак активности |

---

## community

**Описание:** Социальные связи (подписки, фолловинг)

**Таблиц в модуле:** 2

| Таблица | Записей | Описание |
|---------|---------|----------|
| `community_companyfollow` | 3 | - |
| `community_userfollow` | 18 | - |

### community_companyfollow

**Количество записей:** 3

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | - | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `followed_id` | integer | Нет | - | FK на followed |
| 5 | `follower_id` | integer | Нет | - | FK на follower |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `followed_id` | `account_company.id` |
| `follower_id` | `account_user.id` |

---

### community_userfollow

**Количество записей:** 18

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | - | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `followed_id` | integer | Нет | - | FK на followed |
| 5 | `follower_id` | integer | Нет | - | FK на follower |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `followed_id` | `account_user.id` |
| `follower_id` | `account_user.id` |

---

## core

**Описание:** Основной контент: события, вакансии, блоги, статьи, тех.задания

**Таблиц в модуле:** 27

| Таблица | Записей | Описание |
|---------|---------|----------|
| `core_actionlog` | 124,987 | - |
| `core_article` | 83 | - |
| `core_banner` | 27 | - |
| `core_blog` | 1,801 | - |
| `core_category` | 14 | - |
| `core_city` | 16 | - |
| `core_comment` | 2,585 | - |
| `core_country` | 1 | - |
| `core_discussion` | 157 | - |
| `core_discussionvote` | 335 | - |
| `core_elabsannouncement` | 70 | - |
| `core_event` | 1,459 | - |
| `core_eventparticipant` | 864 | - |
| `core_faq` | 7 | - |
| `core_faqitem` | 46 | - |
| `core_feed` | 4,789 | - |
| `core_floordata` | 16 | - |
| `core_infrastructure` | 504 | - |
| `core_infrastructureimage` | 397 | - |
| `core_infrastructurerequest` | 37 | - |
| `core_notification` | 1,233 | - |
| `core_organization` | 45 | - |
| `core_techtask` | 247 | - |
| `core_techtasksolution` | 232 | - |
| `core_vacancy` | 1,205 | - |
| `core_vacancycandidate` | 5,344 | - |
| `core_vacancycandidate_certificates` | 192 | - |

### core_actionlog

**Количество записей:** 124,987

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('core_actionlog_id_seq'::regclas... | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `data` | jsonb | Нет | - | Дополнительные данные (JSON) |
| 5 | `action` | character varying(50) | Нет | - |  |
| 6 | `log_type` | character varying(50) | Нет | - |  |
| 7 | `primary_key` | character varying(50) | Да | - |  |
| 8 | `source` | character varying(25) | Нет | - |  |
| 9 | `user_id` | integer | Да | - | FK на user |
| 10 | `body` | text | Да | - |  |
| 11 | `headers` | text | Да | - |  |
| 12 | `query_params` | text | Да | - |  |
| 13 | `metadata` | jsonb | Нет | - |  |
| 14 | `service` | character varying(20) | Нет | - |  |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `user_id` | `account_user.id` |

---

### core_article

**Количество записей:** 83

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('core_article_id_seq'::regclass) | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `status` | character varying(20) | Нет | - | Статус записи |
| 5 | `title` | jsonb | Нет | - | Заголовок |
| 6 | `subtitle` | jsonb | Нет | - |  |
| 7 | `slug` | character varying(250) | Нет | - | URL-идентификатор |
| 8 | `content` | jsonb | Нет | - | Содержимое |
| 9 | `tags` | ARRAY | Нет | - |  |
| 10 | `featured` | boolean | Нет | - |  |
| 11 | `published` | boolean | Нет | - | Признак публикации |
| 12 | `publish_date` | timestamp with time zone | Да | - |  |
| 13 | `search_field` | text | Нет | - |  |
| 14 | `author_id` | integer | Нет | - | FK на author |
| 15 | `category_id` | integer | Да | - | FK на category |
| 16 | `view_count` | integer | Нет | - |  |
| 17 | `comment` | character varying(1000) | Нет | - |  |
| 18 | `show_in_feed` | boolean | Нет | - |  |
| 19 | `image_id` | uuid | Да | - | FK на image |
| 20 | `favorite_users` | ARRAY | Нет | - |  |
| 21 | `reaction_down_users` | ARRAY | Нет | - |  |
| 22 | `reaction_up_users` | ARRAY | Нет | - |  |
| 23 | `comments_count` | integer | Нет | - |  |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `author_id` | `account_user.id` |
| `category_id` | `core_category.id` |

---

### core_banner

**Количество записей:** 27

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | - | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `name` | character varying(50) | Нет | - | Наименование |
| 5 | `data` | jsonb | Нет | - | Дополнительные данные (JSON) |
| 6 | `active` | boolean | Нет | - |  |
| 7 | `position` | smallint | Нет | - |  |
| 8 | `template` | character varying(100) | Нет | - |  |
| 9 | `type` | smallint | Нет | - |  |
| 10 | `types` | ARRAY | Нет | - |  |

---

### core_blog

**Количество записей:** 1,801

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('core_blog_id_seq'::regclass) | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `liked_users` | ARRAY | Нет | - |  |
| 5 | `status` | character varying(20) | Нет | - | Статус записи |
| 6 | `title` | jsonb | Нет | - | Заголовок |
| 7 | `subtitle` | jsonb | Нет | - |  |
| 8 | `slug` | character varying(250) | Нет | - | URL-идентификатор |
| 9 | `content` | jsonb | Нет | - | Содержимое |
| 10 | `tags` | ARRAY | Нет | - |  |
| 11 | `featured` | boolean | Нет | - |  |
| 12 | `published` | boolean | Нет | - | Признак публикации |
| 13 | `comment` | character varying(1000) | Нет | - |  |
| 14 | `search_field` | text | Нет | - |  |
| 15 | `author_id` | integer | Нет | - | FK на author |
| 16 | `category_id` | integer | Да | - | FK на category |
| 17 | `view_count` | integer | Нет | - |  |
| 18 | `reaction_down_users` | ARRAY | Нет | - |  |
| 19 | `reaction_up_users` | ARRAY | Нет | - |  |
| 20 | `show_in_feed` | boolean | Нет | - |  |
| 21 | `publish_date` | timestamp with time zone | Да | - |  |
| 22 | `image_id` | uuid | Да | - | FK на image |
| 23 | `cover` | character varying(20) | Нет | - |  |
| 24 | `favorite_users` | ARRAY | Нет | - |  |
| 25 | `tag` | jsonb | Нет | - |  |
| 26 | `image_en_id` | uuid | Да | - | FK на image_en |
| 27 | `image_kk_id` | uuid | Да | - | FK на image_kk |
| 28 | `image_ru_id` | uuid | Да | - | FK на image_ru |
| 29 | `youtube_link` | jsonb | Нет | - |  |
| 30 | `main_language` | character varying(3) | Нет | - |  |
| 31 | `translation_config` | jsonb | Нет | - |  |
| 32 | `games_data` | jsonb | Нет | - |  |
| 33 | `sent_to_moderation_at` | timestamp with time zone | Да | - |  |
| 34 | `company_id` | integer | Да | - | FK на company |
| 35 | `engagement_rate` | double precision | Да | - |  |
| 36 | `comments_count` | integer | Нет | - |  |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `author_id` | `account_user.id` |
| `category_id` | `core_category.id` |
| `company_id` | `account_company.id` |

---

### core_category

**Количество записей:** 14

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('core_category_id_seq'::regclass... | Уникальный идентификатор |
| 2 | `name` | jsonb | Нет | - | Наименование |
| 3 | `description` | jsonb | Нет | - |  |
| 4 | `featured` | boolean | Нет | - |  |
| 5 | `image_id` | uuid | Да | - | FK на image |
| 6 | `position` | smallint | Нет | - |  |
| 7 | `reaction_down_users` | ARRAY | Нет | - |  |
| 8 | `reaction_up_users` | ARRAY | Нет | - |  |
| 9 | `slug` | character varying(250) | Нет | - | URL-идентификатор |
| 10 | `background_id` | uuid | Да | - | FK на background |
| 11 | `following_users` | ARRAY | Нет | - |  |
| 12 | `is_active` | boolean | Нет | - | Признак активности |
| 13 | `show_top_authors` | boolean | Нет | - |  |
| 14 | `can_publish` | boolean | Нет | - |  |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `background_id` | `shared_mediafile.id` |

---

### core_city

**Количество записей:** 16

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('core_city_id_seq'::regclass) | Уникальный идентификатор |
| 2 | `name` | character varying(200) | Нет | - | Наименование |
| 3 | `name_ru` | character varying(200) | Да | - |  |
| 4 | `name_kk` | character varying(200) | Да | - |  |
| 5 | `name_en` | character varying(200) | Да | - |  |
| 6 | `country_id` | integer | Нет | - | FK на country |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `country_id` | `core_country.id` |

---

### core_comment

**Количество записей:** 2,585

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('core_comment_id_seq'::regclass) | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `message` | text | Нет | - |  |
| 5 | `source` | character varying(50) | Нет | - |  |
| 6 | `primary_key` | character varying(20) | Нет | - |  |
| 7 | `user_id` | integer | Нет | - | FK на user |
| 8 | `parent_id` | integer | Да | - | FK на parent |
| 9 | `reaction_down_users` | ARRAY | Нет | - |  |
| 10 | `reaction_up_users` | ARRAY | Нет | - |  |
| 11 | `status` | character varying(20) | Нет | - | Статус записи |
| 12 | `viewed` | ARRAY | Нет | - |  |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `parent_id` | `core_comment.id` |
| `user_id` | `account_user.id` |

---

### core_country

**Количество записей:** 1

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('core_country_id_seq'::regclass) | Уникальный идентификатор |
| 2 | `name` | character varying(200) | Нет | - | Наименование |
| 3 | `name_ru` | character varying(200) | Да | - |  |
| 4 | `name_kk` | character varying(200) | Да | - |  |
| 5 | `name_en` | character varying(200) | Да | - |  |

---

### core_discussion

**Количество записей:** 157

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('core_discussion_id_seq'::regcla... | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `view_count` | integer | Нет | - |  |
| 5 | `reaction_up_users` | ARRAY | Нет | - |  |
| 6 | `reaction_down_users` | ARRAY | Нет | - |  |
| 7 | `status` | character varying(20) | Нет | - | Статус записи |
| 8 | `title` | jsonb | Нет | - | Заголовок |
| 9 | `slug` | character varying(250) | Нет | - | URL-идентификатор |
| 10 | `content` | jsonb | Нет | - | Содержимое |
| 11 | `tags` | ARRAY | Нет | - |  |
| 12 | `featured` | boolean | Нет | - |  |
| 13 | `published` | boolean | Нет | - | Признак публикации |
| 14 | `comment` | character varying(1000) | Нет | - |  |
| 15 | `search_field` | text | Нет | - |  |
| 16 | `author_id` | integer | Нет | - | FK на author |
| 17 | `category_id` | integer | Да | - | FK на category |
| 18 | `signature` | jsonb | Нет | - |  |
| 19 | `show_in_feed` | boolean | Нет | - |  |
| 20 | `publication_policy_accepted` | boolean | Нет | - |  |
| 21 | `publish_date` | timestamp with time zone | Да | - |  |
| 22 | `image_id` | uuid | Да | - | FK на image |
| 23 | `files` | ARRAY | Нет | - |  |
| 24 | `files_for` | character varying(50) | Нет | - |  |
| 25 | `statuses` | jsonb | Нет | - |  |
| 26 | `notification_data` | jsonb | Нет | - |  |
| 27 | `favorite_users` | ARRAY | Нет | - |  |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `author_id` | `account_user.id` |
| `category_id` | `core_category.id` |

---

### core_discussionvote

**Количество записей:** 335

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('core_discussionvote_id_seq'::re... | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `choice` | character varying(20) | Нет | - |  |
| 5 | `signature` | jsonb | Нет | - |  |
| 6 | `discussion_id` | integer | Нет | - | FK на discussion |
| 7 | `user_id` | integer | Нет | - | FK на user |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `discussion_id` | `core_discussion.id` |
| `user_id` | `account_user.id` |

---

### core_elabsannouncement

**Количество записей:** 70

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | - | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `status` | character varying(20) | Нет | - | Статус записи |
| 5 | `product_name` | text | Нет | - |  |
| 6 | `organizer_name` | text | Нет | - |  |
| 7 | `organizer_bin` | text | Нет | - |  |
| 8 | `organizer_address` | text | Нет | - |  |
| 9 | `organizer_contacts` | text | Нет | - |  |
| 10 | `organizer_email` | text | Нет | - |  |
| 11 | `available_count` | integer | Нет | - |  |
| 12 | `price` | integer | Да | - |  |
| 13 | `supply_place` | text | Нет | - |  |
| 14 | `supply_date` | date | Да | - |  |
| 15 | `proposals_address` | text | Нет | - |  |
| 16 | `proposals_end_date` | date | Да | - |  |
| 17 | `envelope_opening_date` | date | Да | - |  |
| 18 | `envelope_opening_address` | text | Нет | - |  |
| 19 | `authorized_representative` | text | Нет | - |  |
| 20 | `author_id` | integer | Нет | - | FK на author |
| 21 | `characteristics_id` | uuid | Да | - | FK на characteristics |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `author_id` | `account_user.id` |

---

### core_event

**Количество записей:** 1,459

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('core_event_id_seq'::regclass) | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `status` | character varying(20) | Нет | - | Статус записи |
| 5 | `title` | jsonb | Нет | - | Заголовок |
| 6 | `category` | character varying(20) | Да | - |  |
| 7 | `slug` | character varying(250) | Нет | - | URL-идентификатор |
| 8 | `content` | jsonb | Нет | - | Содержимое |
| 9 | `datetime_start` | timestamp with time zone | Да | - |  |
| 10 | `datetime_end` | timestamp with time zone | Да | - |  |
| 11 | `event_format` | character varying(20) | Нет | - |  |
| 12 | `event_type` | character varying(20) | Нет | - |  |
| 13 | `hall` | character varying(100) | Да | - |  |
| 14 | `visitors_count` | smallint | Да | - |  |
| 15 | `conference_link` | character varying(1000) | Да | - |  |
| 16 | `contact_info` | jsonb | Нет | - |  |
| 17 | `published` | boolean | Нет | - | Признак публикации |
| 18 | `available` | boolean | Нет | - |  |
| 19 | `comment` | character varying(1000) | Нет | - |  |
| 20 | `search_field` | text | Нет | - |  |
| 21 | `author_id` | integer | Нет | - | FK на author |
| 22 | `organization_id` | character varying(20) | Да | - | FK на organization |
| 23 | `view_count` | integer | Нет | - |  |
| 24 | `image_id` | uuid | Да | - | FK на image |
| 25 | `event_form` | character varying(20) | Да | - |  |
| 26 | `city` | character varying(200) | Да | - |  |
| 27 | `country` | character varying(200) | Да | - |  |
| 28 | `form_link` | character varying(1000) | Да | - |  |
| 29 | `favorite_users` | ARRAY | Нет | - |  |
| 30 | `show_in_feed` | boolean | Нет | - |  |
| 31 | `event_for` | character varying(100) | Да | - |  |
| 32 | `address` | character varying(150) | Да | - |  |
| 33 | `company_id` | integer | Да | - | FK на company |
| 34 | `event_location` | character varying(100) | Да | - |  |
| 35 | `latitude` | numeric | Да | - |  |
| 36 | `longitude` | numeric | Да | - |  |
| 37 | `online_link` | character varying(1000) | Да | - |  |
| 38 | `record_link` | character varying(1000) | Да | - |  |
| 39 | `games_data` | jsonb | Нет | - |  |
| 40 | `featured` | boolean | Нет | - |  |
| 41 | `scope` | ARRAY | Нет | - |  |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `author_id` | `account_user.id` |
| `company_id` | `account_company.id` |
| `organization_id` | `core_organization.code` |

---

### core_eventparticipant

**Количество записей:** 864

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('core_eventparticipant_id_seq'::... | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `status` | character varying(20) | Нет | - | Статус записи |
| 5 | `email` | character varying(200) | Да | - | Электронная почта |
| 6 | `phone` | character varying(200) | Да | - | Номер телефона |
| 7 | `full_name` | character varying(200) | Нет | - |  |
| 8 | `qrcode` | character varying(20) | Нет | - |  |
| 9 | `author_id` | integer | Нет | - | FK на author |
| 10 | `event_id` | integer | Нет | - | FK на event |
| 11 | `role` | character varying(100) | Да | - |  |
| 12 | `participated_at` | timestamp with time zone | Да | - |  |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `author_id` | `account_user.id` |
| `event_id` | `core_event.id` |

---

### core_faq

**Количество записей:** 7

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `code` | character varying(20) | Нет | - |  |
| 2 | `title` | character varying(200) | Нет | - | Заголовок |
| 3 | `title_ru` | character varying(200) | Да | - |  |
| 4 | `title_kk` | character varying(200) | Да | - |  |
| 5 | `title_en` | character varying(200) | Да | - |  |
| 6 | `position` | smallint | Нет | - |  |
| 7 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 8 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |

---

### core_faqitem

**Количество записей:** 46

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('core_faqitem_id_seq'::regclass) | Уникальный идентификатор |
| 2 | `title` | character varying(200) | Нет | - | Заголовок |
| 3 | `title_ru` | character varying(200) | Да | - |  |
| 4 | `title_kk` | character varying(200) | Да | - |  |
| 5 | `title_en` | character varying(200) | Да | - |  |
| 6 | `description` | text | Нет | - |  |
| 7 | `description_ru` | text | Да | - |  |
| 8 | `description_kk` | text | Да | - |  |
| 9 | `description_en` | text | Да | - |  |
| 10 | `position` | smallint | Нет | - |  |
| 11 | `faq_id` | character varying(20) | Нет | - | FK на faq |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `faq_id` | `core_faq.code` |

---

### core_feed

**Количество записей:** 4,789

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('core_feed_id_seq'::regclass) | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `source` | character varying(50) | Нет | - |  |
| 5 | `primary_key` | character varying(20) | Нет | - |  |
| 6 | `published` | boolean | Нет | - | Признак публикации |
| 7 | `published_at` | timestamp with time zone | Нет | - |  |
| 8 | `featured` | boolean | Нет | - |  |
| 9 | `article_id` | integer | Да | - | FK на article |
| 10 | `blog_id` | integer | Да | - | FK на blog |
| 11 | `discussion_id` | integer | Да | - | FK на discussion |
| 12 | `tags` | ARRAY | Нет | - |  |
| 13 | `show_in_feed` | boolean | Нет | - |  |
| 14 | `tech_task_id` | integer | Да | - | FK на tech_task |
| 15 | `event_id` | integer | Да | - | FK на event |
| 16 | `vacancy_id` | integer | Да | - | FK на vacancy |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `article_id` | `core_article.id` |
| `blog_id` | `core_blog.id` |
| `discussion_id` | `core_discussion.id` |
| `event_id` | `core_event.id` |
| `tech_task_id` | `core_techtask.id` |
| `vacancy_id` | `core_vacancy.id` |

---

### core_floordata

**Количество записей:** 16

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('core_floordata_id_seq'::regclas... | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `pavilion` | character varying(10) | Нет | - |  |
| 5 | `floor` | integer | Нет | - |  |
| 6 | `data` | jsonb | Нет | - | Дополнительные данные (JSON) |
| 7 | `is_active` | boolean | Нет | - | Признак активности |
| 8 | `template` | character varying(100) | Нет | - |  |

---

### core_infrastructure

**Количество записей:** 504

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | - | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `favorite_users` | ARRAY | Нет | - |  |
| 5 | `name` | jsonb | Нет | - | Наименование |
| 6 | `active` | boolean | Нет | - |  |
| 7 | `type` | character varying(100) | Да | - |  |
| 8 | `subtype` | character varying(100) | Да | - |  |
| 9 | `kind` | character varying(100) | Да | - |  |
| 10 | `price` | numeric | Да | - |  |
| 11 | `unit` | character varying(100) | Да | - |  |
| 12 | `phone` | character varying(20) | Да | - | Номер телефона |
| 13 | `email` | character varying(100) | Да | - | Электронная почта |
| 14 | `city` | character varying(100) | Да | - |  |
| 15 | `data` | jsonb | Нет | - | Дополнительные данные (JSON) |
| 16 | `author_id` | integer | Нет | - | FK на author |
| 17 | `organization_id` | character varying(20) | Да | - | FK на organization |
| 18 | `parent_id` | integer | Да | - | FK на parent |
| 19 | `status` | character varying(20) | Нет | - | Статус записи |
| 20 | `categories` | ARRAY | Нет | - |  |
| 21 | `company_id` | integer | Да | - | FK на company |
| 22 | `scope` | character varying(100) | Да | - |  |
| 23 | `comment` | character varying(1000) | Нет | - |  |
| 24 | `view_count` | integer | Нет | - |  |
| 25 | `signature` | jsonb | Нет | - |  |
| 26 | `search_field` | text | Нет | - |  |
| 27 | `priority` | smallint | Да | - |  |
| 28 | `accreditation` | text | Да | - |  |
| 29 | `employees_number` | integer | Да | - |  |
| 30 | `equipment_percentage` | integer | Да | - |  |
| 31 | `job_title_1` | character varying(200) | Да | - |  |
| 32 | `job_title_2` | character varying(200) | Да | - |  |
| 33 | `job_title_3` | character varying(200) | Да | - |  |
| 34 | `job_title_4` | character varying(200) | Да | - |  |
| 35 | `head` | character varying(200) | Да | - |  |
| 36 | `license` | text | Да | - |  |
| 37 | `other_documentation` | text | Да | - |  |
| 38 | `regime_commission_permission` | text | Да | - |  |
| 39 | `total_number` | integer | Да | - |  |
| 40 | `equipment_data` | jsonb | Нет | - |  |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `author_id` | `account_user.id` |
| `company_id` | `account_company.id` |
| `organization_id` | `core_organization.code` |
| `parent_id` | `core_infrastructure.id` |

---

### core_infrastructureimage

**Количество записей:** 397

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | - | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `image` | character varying(100) | Нет | - |  |
| 5 | `primary` | boolean | Нет | - |  |
| 6 | `author_id` | integer | Нет | - | FK на author |
| 7 | `infrastructure_id` | integer | Нет | - | FK на infrastructure |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `author_id` | `account_user.id` |
| `infrastructure_id` | `core_infrastructure.id` |

---

### core_infrastructurerequest

**Количество записей:** 37

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | - | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `phone` | character varying(30) | Нет | - | Номер телефона |
| 5 | `contact_name` | character varying(100) | Нет | - |  |
| 6 | `comment` | character varying(1000) | Нет | - |  |
| 7 | `response_comment` | character varying(1000) | Нет | - |  |
| 8 | `status` | character varying(20) | Нет | - | Статус записи |
| 9 | `author_id` | integer | Нет | - | FK на author |
| 10 | `infrastructure_id` | integer | Нет | - | FK на infrastructure |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `author_id` | `account_user.id` |
| `infrastructure_id` | `core_infrastructure.id` |

---

### core_notification

**Количество записей:** 1,233

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('core_notification_id_seq'::regc... | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `title` | jsonb | Нет | - | Заголовок |
| 5 | `description` | jsonb | Нет | - |  |
| 6 | `user_id` | integer | Нет | - | FK на user |
| 7 | `url` | character varying(1000) | Нет | - |  |
| 8 | `is_read` | boolean | Нет | - |  |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `user_id` | `account_user.id` |

---

### core_organization

**Количество записей:** 45

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 2 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 3 | `code` | character varying(20) | Нет | - |  |
| 4 | `logo` | character varying(100) | Да | - |  |
| 5 | `data` | jsonb | Нет | - | Дополнительные данные (JSON) |
| 6 | `active` | boolean | Нет | - |  |
| 7 | `name` | jsonb | Нет | - | Наименование |

---

### core_techtask

**Количество записей:** 247

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('core_techtask_id_seq'::regclass... | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `status` | character varying(20) | Нет | - | Статус записи |
| 5 | `show_in_feed` | boolean | Нет | - |  |
| 6 | `title` | jsonb | Нет | - | Заголовок |
| 7 | `description` | jsonb | Нет | - |  |
| 8 | `problem_description` | jsonb | Нет | - |  |
| 9 | `product_type_software` | boolean | Нет | - |  |
| 10 | `product_type_mobile` | boolean | Нет | - |  |
| 11 | `product_type_other` | boolean | Нет | - |  |
| 12 | `other_product_type` | jsonb | Нет | - |  |
| 13 | `effect` | jsonb | Нет | - |  |
| 14 | `development_country` | character varying(10) | Нет | - |  |
| 15 | `product_status` | character varying(10) | Нет | - |  |
| 16 | `other_status` | jsonb | Нет | - |  |
| 17 | `reward` | jsonb | Нет | - |  |
| 18 | `contact_name` | jsonb | Нет | - |  |
| 19 | `phone` | character varying(30) | Нет | - | Номер телефона |
| 20 | `notes` | jsonb | Нет | - |  |
| 21 | `tags` | ARRAY | Нет | - |  |
| 22 | `featured` | boolean | Нет | - |  |
| 23 | `published` | boolean | Нет | - | Признак публикации |
| 24 | `publish_date` | timestamp with time zone | Да | - |  |
| 25 | `comment` | character varying(1000) | Нет | - |  |
| 26 | `search_field` | text | Нет | - |  |
| 27 | `slug` | character varying(250) | Нет | - | URL-идентификатор |
| 28 | `author_id` | integer | Нет | - | FK на author |
| 29 | `specification_id` | uuid | Да | - | FK на specification |
| 30 | `view_count` | integer | Нет | - |  |
| 31 | `deadline` | timestamp with time zone | Да | - |  |
| 32 | `notification_data` | jsonb | Нет | - |  |
| 33 | `favorite_users` | ARRAY | Нет | - |  |
| 34 | `company_name` | character varying(200) | Нет | - |  |
| 35 | `amount` | integer | Да | - |  |
| 36 | `task_area` | character varying(500) | Нет | - |  |
| 37 | `scope` | character varying(1000) | Нет | - |  |
| 38 | `application_type` | character varying(20) | Да | - |  |
| 39 | `games_data` | jsonb | Нет | - |  |
| 40 | `priority` | smallint | Да | - |  |
| 41 | `extra_data` | jsonb | Нет | - |  |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `author_id` | `account_user.id` |

---

### core_techtasksolution

**Количество записей:** 232

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('core_techtasksolution_id_seq'::... | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `company_name` | jsonb | Нет | - |  |
| 5 | `company_tin` | character varying(12) | Нет | - |  |
| 6 | `website` | character varying(1000) | Нет | - |  |
| 7 | `phone` | character varying(30) | Нет | - | Номер телефона |
| 8 | `contact_name` | jsonb | Нет | - |  |
| 9 | `launch_date` | date | Нет | - |  |
| 10 | `notes` | jsonb | Нет | - |  |
| 11 | `author_id` | integer | Нет | - | FK на author |
| 12 | `product_presentation_id` | uuid | Да | - | FK на product_presentation |
| 13 | `tech_task_id` | integer | Нет | - | FK на tech_task |
| 14 | `status` | character varying(20) | Нет | - | Статус записи |
| 15 | `product_status` | character varying(20) | Нет | - |  |
| 16 | `comment` | character varying(1000) | Нет | - |  |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `author_id` | `account_user.id` |
| `tech_task_id` | `core_techtask.id` |

---

### core_vacancy

**Количество записей:** 1,205

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('core_vacancy_id_seq'::regclass) | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `status` | character varying(20) | Нет | - | Статус записи |
| 5 | `title` | jsonb | Нет | - | Заголовок |
| 6 | `vacancy_type` | character varying(20) | Да | - |  |
| 7 | `salary_min` | integer | Да | - |  |
| 8 | `salary_max` | integer | Да | - |  |
| 9 | `place` | character varying(20) | Да | - |  |
| 10 | `description` | jsonb | Нет | - |  |
| 11 | `email` | character varying(254) | Нет | - | Электронная почта |
| 12 | `published` | boolean | Нет | - | Признак публикации |
| 13 | `comment` | character varying(1000) | Нет | - |  |
| 14 | `author_id` | integer | Нет | - | FK на author |
| 15 | `city_id` | integer | Да | - | FK на city |
| 16 | `view_count` | integer | Нет | - |  |
| 17 | `short_description` | jsonb | Нет | - |  |
| 18 | `company_id` | integer | Да | - | FK на company |
| 19 | `specializations` | ARRAY | Нет | - |  |
| 20 | `favorite_users` | ARRAY | Нет | - |  |
| 21 | `show_in_feed` | boolean | Нет | - |  |
| 22 | `search_field` | text | Нет | - |  |
| 23 | `games_data` | jsonb | Нет | - |  |
| 24 | `direction` | character varying | Да | - |  |
| 25 | `education` | character varying | Нет | - |  |
| 26 | `experience` | character varying | Да | - |  |
| 27 | `opened` | boolean | Нет | - |  |
| 28 | `additional_place` | ARRAY | Нет | - |  |
| 29 | `region` | character varying(50) | Да | - |  |
| 30 | `published_at` | timestamp with time zone | Да | - |  |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `author_id` | `account_user.id` |
| `city_id` | `core_city.id` |
| `company_id` | `account_company.id` |

---

### core_vacancycandidate

**Количество записей:** 5,344

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('core_vacancycandidate_id_seq'::... | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `status` | character varying(20) | Нет | - | Статус записи |
| 5 | `email` | character varying(200) | Нет | - | Электронная почта |
| 6 | `phone` | character varying(200) | Нет | - | Номер телефона |
| 7 | `full_name` | character varying(200) | Нет | - |  |
| 8 | `linkedin` | character varying(500) | Нет | - |  |
| 9 | `description` | text | Нет | - |  |
| 10 | `author_id` | integer | Нет | - | FK на author |
| 11 | `vacancy_id` | integer | Нет | - | FK на vacancy |
| 12 | `cv_id` | uuid | Да | - | FK на cv |
| 13 | `portfolio_url` | character varying(500) | Да | - |  |
| 14 | `candidate_status` | character varying(30) | Нет | - |  |
| 15 | `offer_file_id` | uuid | Да | - | FK на offer_file |
| 16 | `offer_text` | text | Да | - |  |
| 17 | `reject_reason_recruiter` | text | Да | - |  |
| 18 | `reject_reason_seeker` | text | Да | - |  |
| 19 | `work_experience` | character varying(1000) | Да | - |  |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `author_id` | `account_user.id` |
| `vacancy_id` | `core_vacancy.id` |

---

### core_vacancycandidate_certificates

**Количество записей:** 192

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | - | Уникальный идентификатор |
| 2 | `vacancycandidate_id` | integer | Нет | - | FK на vacancycandidate |
| 3 | `mediafile_id` | uuid | Нет | - | FK на mediafile |

---

## django

**Описание:** Системные таблицы Django (миграции, сессии, логи)

**Таблиц в модуле:** 5

| Таблица | Записей | Описание |
|---------|---------|----------|
| `django_admin_log` | 42,696 | - |
| `django_content_type` | 155 | - |
| `django_dramatiq_task` | 0 | - |
| `django_migrations` | 819 | - |
| `django_session` | 0 | - |

### django_admin_log

**Количество записей:** 42,696

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('django_admin_log_id_seq'::regcl... | Уникальный идентификатор |
| 2 | `action_time` | timestamp with time zone | Нет | - |  |
| 3 | `object_id` | text | Да | - | FK на object |
| 4 | `object_repr` | character varying(200) | Нет | - |  |
| 5 | `action_flag` | smallint | Нет | - |  |
| 6 | `change_message` | text | Нет | - |  |
| 7 | `content_type_id` | integer | Да | - | FK на content_type |
| 8 | `user_id` | integer | Нет | - | FK на user |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `content_type_id` | `django_content_type.id` |
| `user_id` | `account_user.id` |

---

### django_content_type

**Количество записей:** 155

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('django_content_type_id_seq'::re... | Уникальный идентификатор |
| 2 | `app_label` | character varying(100) | Нет | - |  |
| 3 | `model` | character varying(100) | Нет | - |  |

---

### django_dramatiq_task

**Количество записей:** 0

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | uuid | Нет | - | Уникальный идентификатор |
| 2 | `status` | character varying(8) | Нет | - | Статус записи |
| 3 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 4 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 5 | `message_data` | bytea | Нет | - |  |
| 6 | `actor_name` | character varying(300) | Да | - |  |
| 7 | `queue_name` | character varying(100) | Да | - |  |

---

### django_migrations

**Количество записей:** 819

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('django_migrations_id_seq'::regc... | Уникальный идентификатор |
| 2 | `app` | character varying(255) | Нет | - |  |
| 3 | `name` | character varying(255) | Нет | - | Наименование |
| 4 | `applied` | timestamp with time zone | Нет | - |  |

---

### django_session

**Количество записей:** 0

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `session_key` | character varying(40) | Нет | - |  |
| 2 | `session_data` | text | Нет | - |  |
| 3 | `expire_date` | timestamp with time zone | Нет | - |  |

---

## explorer

**Описание:** SQL Explorer для аналитики

**Таблиц в модуле:** 3

| Таблица | Записей | Описание |
|---------|---------|----------|
| `explorer_query` | 6 | - |
| `explorer_queryfavorite` | 0 | - |
| `explorer_querylog` | 1,129 | - |

### explorer_query

**Количество записей:** 6

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | - | Уникальный идентификатор |
| 2 | `title` | character varying(255) | Нет | - | Заголовок |
| 3 | `sql` | text | Нет | - |  |
| 4 | `description` | text | Нет | - |  |
| 5 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 6 | `last_run_date` | timestamp with time zone | Нет | - |  |
| 7 | `created_by_user_id` | integer | Да | - | FK на created_by_user |
| 8 | `snapshot` | boolean | Нет | - |  |
| 9 | `connection` | character varying(128) | Нет | - |  |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `created_by_user_id` | `account_user.id` |

---

### explorer_queryfavorite

**Количество записей:** 0

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | - | Уникальный идентификатор |
| 2 | `query_id` | integer | Нет | - | FK на query |
| 3 | `user_id` | integer | Нет | - | FK на user |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `query_id` | `explorer_query.id` |
| `user_id` | `account_user.id` |

---

### explorer_querylog

**Количество записей:** 1,129

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | - | Уникальный идентификатор |
| 2 | `sql` | text | Нет | - |  |
| 3 | `run_at` | timestamp with time zone | Нет | - |  |
| 4 | `query_id` | integer | Да | - | FK на query |
| 5 | `run_by_user_id` | integer | Да | - | FK на run_by_user |
| 6 | `duration` | double precision | Да | - |  |
| 7 | `connection` | character varying(128) | Нет | - |  |
| 8 | `error` | text | Да | - |  |
| 9 | `success` | boolean | Нет | - |  |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `query_id` | `explorer_query.id` |
| `run_by_user_id` | `account_user.id` |

---

## hub

**Описание:** Кэш-таблицы

**Таблиц в модуле:** 1

| Таблица | Записей | Описание |
|---------|---------|----------|
| `hub_cache_table` | 63 | - |

### hub_cache_table

**Количество записей:** 63

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `cache_key` | character varying(255) | Нет | - |  |
| 2 | `value` | text | Нет | - |  |
| 3 | `expires` | timestamp with time zone | Нет | - |  |

---

## journeymap

**Описание:** Карты развития для компаний и пользователей

**Таблиц в модуле:** 7

| Таблица | Записей | Описание |
|---------|---------|----------|
| `journeymap_companystate` | 0 | - |
| `journeymap_journeymap` | 0 | - |
| `journeymap_question` | 0 | - |
| `journeymap_step` | 0 | - |
| `journeymap_step_next_steps` | 0 | - |
| `journeymap_task` | 0 | - |
| `journeymap_userstate` | 0 | - |

### journeymap_companystate

**Количество записей:** 0

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | bigint | Нет | - | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `step_data` | jsonb | Нет | - |  |
| 5 | `company_id` | integer | Нет | - | FK на company |
| 6 | `journeymap_id` | character varying(50) | Нет | - | FK на journeymap |
| 7 | `task_data` | jsonb | Нет | - |  |
| 8 | `journeymap_data` | jsonb | Нет | - |  |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `company_id` | `account_company.id` |
| `journeymap_id` | `journeymap_journeymap.key` |

---

### journeymap_journeymap

**Количество записей:** 0

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 2 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 3 | `key` | character varying(50) | Нет | - |  |
| 4 | `name` | character varying(100) | Нет | - | Наименование |
| 5 | `config` | jsonb | Нет | - |  |

---

### journeymap_question

**Количество записей:** 0

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | bigint | Нет | - | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `type` | character varying(40) | Нет | - |  |
| 5 | `name` | character varying(100) | Нет | - | Наименование |
| 6 | `title` | jsonb | Нет | - | Заголовок |
| 7 | `config` | jsonb | Нет | - |  |
| 8 | `position` | smallint | Нет | - |  |
| 9 | `task_id` | bigint | Нет | - | FK на task |
| 10 | `key` | character varying(100) | Нет | - |  |
| 11 | `company_experience_points` | integer | Нет | - |  |
| 12 | `experience_points` | integer | Нет | - |  |
| 13 | `social_coins` | integer | Нет | - |  |
| 14 | `st` | integer | Нет | - |  |
| 15 | `condition` | character varying(200) | Нет | - |  |
| 16 | `can_skip` | boolean | Нет | - |  |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `task_id` | `journeymap_task.id` |

---

### journeymap_step

**Количество записей:** 0

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | bigint | Нет | - | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `name` | character varying(100) | Нет | - | Наименование |
| 5 | `title` | jsonb | Нет | - | Заголовок |
| 6 | `config` | jsonb | Нет | - |  |
| 7 | `position` | smallint | Нет | - |  |
| 8 | `type` | character varying(20) | Нет | - |  |
| 9 | `journeymap_id` | character varying(50) | Нет | - | FK на journeymap |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `journeymap_id` | `journeymap_journeymap.key` |

---

### journeymap_step_next_steps

**Количество записей:** 0

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | - | Уникальный идентификатор |
| 2 | `from_step_id` | bigint | Нет | - | FK на from_step |
| 3 | `to_step_id` | bigint | Нет | - | FK на to_step |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `from_step_id` | `journeymap_step.id` |
| `to_step_id` | `journeymap_step.id` |

---

### journeymap_task

**Количество записей:** 0

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | bigint | Нет | - | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `name` | character varying(100) | Нет | - | Наименование |
| 5 | `title` | jsonb | Нет | - | Заголовок |
| 6 | `position` | smallint | Нет | - |  |
| 7 | `config` | jsonb | Нет | - |  |
| 8 | `type` | character varying(20) | Нет | - |  |
| 9 | `event_code` | character varying(100) | Нет | - |  |
| 10 | `completion_code` | text | Нет | - |  |
| 11 | `step_id` | bigint | Нет | - | FK на step |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `step_id` | `journeymap_step.id` |

---

### journeymap_userstate

**Количество записей:** 0

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | bigint | Нет | - | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `step_data` | jsonb | Нет | - |  |
| 5 | `journeymap_id` | character varying(50) | Нет | - | FK на journeymap |
| 6 | `user_id` | integer | Нет | - | FK на user |
| 7 | `task_data` | jsonb | Нет | - |  |
| 8 | `journeymap_data` | jsonb | Нет | - |  |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `journeymap_id` | `journeymap_journeymap.key` |
| `user_id` | `account_user.id` |

---

## landing

**Описание:** CMS для лендингов и страниц

**Таблиц в модуле:** 5

| Таблица | Записей | Описание |
|---------|---------|----------|
| `landing_component` | 2,790 | - |
| `landing_landing` | 8 | - |
| `landing_page` | 562 | - |
| `landing_pagemediafile` | 18,517 | - |
| `landing_section` | 560 | - |

### landing_component

**Количество записей:** 2,790

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('landing_component_id_seq'::regc... | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `container_type` | character varying(50) | Нет | - |  |
| 5 | `component_type` | character varying(50) | Нет | - |  |
| 6 | `position` | smallint | Нет | - |  |
| 7 | `data` | jsonb | Нет | - | Дополнительные данные (JSON) |
| 8 | `section_id` | integer | Нет | - | FK на section |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `section_id` | `landing_section.id` |

---

### landing_landing

**Количество записей:** 8

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('landing_landing_id_seq'::regcla... | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `name` | jsonb | Нет | - | Наименование |
| 5 | `endpoint` | character varying(200) | Нет | - |  |
| 6 | `template` | character varying(200) | Нет | - |  |
| 7 | `data` | jsonb | Нет | - | Дополнительные данные (JSON) |
| 8 | `published` | boolean | Нет | - | Признак публикации |
| 9 | `show_crm_button` | boolean | Нет | - |  |
| 10 | `extra_context` | jsonb | Нет | - |  |

---

### landing_page

**Количество записей:** 562

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('landing_page_id_seq'::regclass) | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `name` | character varying(200) | Нет | - | Наименование |
| 5 | `endpoint` | character varying(200) | Нет | - |  |
| 6 | `page_type` | character varying(500) | Нет | - |  |
| 7 | `data` | jsonb | Нет | - | Дополнительные данные (JSON) |
| 8 | `published` | boolean | Нет | - | Признак публикации |
| 9 | `publish_date` | timestamp with time zone | Да | - |  |
| 10 | `organization_id` | character varying(20) | Да | - | FK на organization |
| 11 | `view_count` | integer | Нет | - |  |
| 12 | `show_crm_button` | boolean | Нет | - |  |
| 13 | `extra_css` | text | Нет | - |  |
| 14 | `extra_js` | text | Нет | - |  |
| 15 | `author_id` | integer | Да | - | FK на author |
| 16 | `authorization_required` | boolean | Нет | - |  |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `author_id` | `account_user.id` |
| `organization_id` | `core_organization.code` |

---

### landing_pagemediafile

**Количество записей:** 18,517

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('landing_pagemediafile_id_seq'::... | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `file` | character varying(100) | Нет | - |  |
| 5 | `thumbnail` | character varying(100) | Да | - |  |
| 6 | `mime_type` | character varying(50) | Нет | - |  |
| 7 | `size` | double precision | Нет | - |  |
| 8 | `page_id` | integer | Нет | - | FK на page |
| 9 | `thumbnail_150` | character varying(100) | Да | - |  |
| 10 | `thumbnail_1500` | character varying(100) | Да | - |  |
| 11 | `thumbnail_800` | character varying(100) | Да | - |  |
| 12 | `author_id` | integer | Да | - | FK на author |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `author_id` | `account_user.id` |
| `page_id` | `landing_page.id` |

---

### landing_section

**Количество записей:** 560

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('landing_section_id_seq'::regcla... | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `section_type` | character varying(500) | Нет | - |  |
| 5 | `position` | smallint | Нет | - |  |
| 6 | `data` | jsonb | Нет | - | Дополнительные данные (JSON) |
| 7 | `page_id` | integer | Нет | - | FK на page |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `page_id` | `landing_page.id` |

---

## matchmaking

**Описание:** Нетворкинг и мэтчинг пользователей

**Таблиц в модуле:** 2

| Таблица | Записей | Описание |
|---------|---------|----------|
| `matchmaking_match` | 31 | - |
| `matchmaking_profile` | 19 | - |

### matchmaking_match

**Количество записей:** 31

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | - | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `date` | date | Нет | - |  |
| 5 | `user_a_id` | integer | Нет | - | FK на user_a |
| 6 | `user_b_id` | integer | Нет | - | FK на user_b |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `user_a_id` | `account_user.id` |
| `user_b_id` | `account_user.id` |

---

### matchmaking_profile

**Количество записей:** 19

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | - | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `activity` | character varying(255) | Нет | - |  |
| 5 | `contact` | character varying(255) | Нет | - |  |
| 6 | `data` | jsonb | Нет | - | Дополнительные данные (JSON) |
| 7 | `user_id` | integer | Нет | - | FK на user |
| 8 | `is_active` | boolean | Нет | - | Признак активности |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `user_id` | `account_user.id` |

---

## niokr

**Описание:** Научно-исследовательские проекты (НИОКР)

**Таблиц в модуле:** 5

| Таблица | Записей | Описание |
|---------|---------|----------|
| `niokr_niokrnotification` | 3 | - |
| `niokr_niokrnotification_projects` | 2 | - |
| `niokr_niokrproject` | 1 | - |
| `niokr_niokrprojectexecutor` | 1 | - |
| `niokr_niokrprojectexecutor_projects` | 1 | - |

### niokr_niokrnotification

**Количество записей:** 3

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | bigint | Нет | - | Уникальный идентификатор |
| 2 | `text` | text | Нет | - |  |
| 3 | `title` | character varying(255) | Нет | - | Заголовок |
| 4 | `notification_type` | character varying(30) | Нет | - |  |
| 5 | `data` | jsonb | Нет | - | Дополнительные данные (JSON) |
| 6 | `unread` | boolean | Нет | - |  |

---

### niokr_niokrnotification_projects

**Количество записей:** 2

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | - | Уникальный идентификатор |
| 2 | `niokrnotification_id` | bigint | Нет | - | FK на niokrnotification |
| 3 | `niokrproject_id` | bigint | Нет | - | FK на niokrproject |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `niokrnotification_id` | `niokr_niokrnotification.id` |
| `niokrproject_id` | `niokr_niokrproject.id` |

---

### niokr_niokrproject

**Количество записей:** 1

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | bigint | Нет | - | Уникальный идентификатор |
| 2 | `organization_bin` | character varying(12) | Да | - |  |
| 3 | `registered_in_state` | boolean | Нет | - |  |
| 4 | `work_title` | jsonb | Да | - |  |
| 5 | `project_type` | text | Нет | - |  |
| 6 | `status` | character varying(300) | Нет | - | Статус записи |
| 7 | `state_registration_number` | character varying(100) | Нет | - |  |
| 8 | `modified_registration_number` | character varying(100) | Да | - |  |
| 9 | `outgoing_number` | character varying(100) | Нет | - |  |
| 10 | `outgoing_date` | date | Да | - |  |
| 11 | `start_date` | date | Да | - |  |
| 12 | `end_date` | date | Да | - |  |
| 13 | `program_code` | character varying(50) | Нет | - |  |
| 14 | `task_code` | character varying(50) | Да | - |  |
| 15 | `work_basis` | character varying(100) | Нет | - |  |
| 16 | `work_type` | character varying(50) | Нет | - |  |
| 17 | `geofund_code` | character varying(50) | Да | - |  |
| 18 | `year` | integer | Да | - |  |
| 19 | `state_budget_funds` | integer | Да | - |  |
| 20 | `customer_funds` | integer | Да | - |  |
| 21 | `own_funds` | integer | Да | - |  |
| 22 | `international_grants` | integer | Да | - |  |
| 23 | `other_funds` | integer | Да | - |  |
| 24 | `goals` | jsonb | Да | - |  |
| 25 | `research_objects` | jsonb | Да | - |  |
| 26 | `application_areas` | jsonb | Да | - |  |
| 27 | `expected_results` | jsonb | Да | - |  |
| 28 | `ministry_name` | character varying(200) | Нет | - |  |
| 29 | `organization_full_name` | character varying(200) | Нет | - |  |
| 30 | `organization_short_name` | character varying(200) | Нет | - |  |
| 31 | `phone` | character varying(20) | Нет | - | Номер телефона |
| 32 | `fax` | text | Да | - |  |
| 33 | `email` | character varying(100) | Нет | - | Электронная почта |
| 34 | `organization_location` | character varying(200) | Нет | - |  |
| 35 | `coexecutor_name` | character varying(200) | Да | - |  |
| 36 | `coexecutor_location` | text | Да | - |  |
| 37 | `udc_indices` | text | Нет | - |  |
| 38 | `code_number` | character varying(50) | Нет | - |  |
| 39 | `code_description` | character varying(200) | Нет | - |  |
| 40 | `keywords` | jsonb | Да | - |  |
| 41 | `project_leader` | character varying(200) | Да | - |  |
| 42 | `leader_fullname` | character varying(200) | Нет | - |  |
| 43 | `leader_degree_title` | character varying(200) | Нет | - |  |
| 44 | `organization_head` | character varying(200) | Нет | - |  |
| 45 | `head_fullname` | character varying(200) | Нет | - |  |
| 46 | `head_degree_title` | character varying(200) | Нет | - |  |
| 47 | `scanned_cover_letter` | text | Нет | - |  |
| 48 | `funding_document` | text | Нет | - |  |
| 49 | `document_date` | date | Да | - |  |
| 50 | `irn` | character varying(200) | Да | - |  |
| 51 | `name` | jsonb | Да | - | Наименование |
| 52 | `application_language` | character varying(50) | Нет | - |  |
| 53 | `project_topic` | jsonb | Да | - |  |
| 54 | `report_status` | character varying(200) | Нет | - |  |
| 55 | `submission_year` | character varying | Да | - |  |
| 56 | `implementation_period` | character varying(200) | Нет | - |  |
| 57 | `customer` | character varying(200) | Нет | - |  |
| 58 | `applicant` | character varying(200) | Нет | - |  |
| 59 | `grantee` | character varying(200) | Да | - |  |
| 60 | `implementation_mechanism` | text | Да | - |  |
| 61 | `gnte_group` | character varying(500) | Нет | - |  |
| 62 | `funding_type` | character varying(100) | Нет | - |  |
| 63 | `gnte_object_type` | character varying(100) | Нет | - |  |
| 64 | `research_type` | character varying(100) | Нет | - |  |
| 65 | `report_type` | character varying(100) | Нет | - |  |
| 66 | `creation_date` | date | Да | - |  |
| 67 | `priority_area` | text | Нет | - |  |
| 68 | `specialized_area` | text | Нет | - |  |
| 69 | `subject_area` | text | Нет | - |  |
| 70 | `rubric_level_1` | text | Нет | - |  |
| 71 | `rubric_level_2` | text | Нет | - |  |
| 72 | `rubric_level_3` | text | Нет | - |  |
| 73 | `code` | character varying(100) | Нет | - |  |
| 74 | `science_rubric_1` | text | Нет | - |  |
| 75 | `science_rubric_2` | text | Нет | - |  |
| 76 | `science_rubric_3` | text | Нет | - |  |
| 77 | `science_keywords` | jsonb | Да | - |  |
| 78 | `funding_volume` | integer | Да | - |  |
| 79 | `cofunding_organization` | character varying(200) | Нет | - |  |
| 80 | `cofunding_amount` | integer | Да | - |  |
| 81 | `report` | jsonb | Нет | - |  |
| 82 | `report_work_goal` | jsonb | Да | - |  |
| 83 | `report_research_methods` | jsonb | Да | - |  |
| 84 | `report_results_and_novelty` | jsonb | Да | - |  |
| 85 | `tech_economic_indicators` | jsonb | Да | - |  |
| 86 | `implementation_level` | jsonb | Да | - |  |
| 87 | `effectiveness` | jsonb | Да | - |  |
| 88 | `application_area` | jsonb | Да | - |  |
| 89 | `report_publications_form` | text | Нет | - |  |
| 90 | `security_docs_info` | text | Нет | - |  |
| 91 | `implementation_info` | text | Нет | - |  |
| 92 | `comments` | jsonb | Нет | - |  |

---

### niokr_niokrprojectexecutor

**Количество записей:** 1

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | bigint | Нет | - | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `executor_type` | character varying(50) | Нет | - |  |
| 5 | `official_name` | character varying(512) | Нет | - |  |
| 6 | `short_name` | character varying(255) | Нет | - |  |
| 7 | `executor_bin` | character varying(12) | Нет | - |  |
| 8 | `head_full_name` | character varying(255) | Нет | - |  |
| 9 | `region` | character varying(100) | Да | - |  |
| 10 | `city` | character varying(100) | Да | - |  |
| 11 | `address` | character varying(255) | Да | - |  |
| 12 | `postal_code` | character varying(50) | Да | - |  |
| 13 | `contact_info` | character varying(50) | Да | - |  |
| 14 | `email` | character varying(254) | Нет | - | Электронная почта |
| 15 | `legal_form` | character varying(50) | Нет | - |  |
| 16 | `ministry` | character varying(255) | Нет | - |  |
| 17 | `order_number` | character varying(50) | Нет | - |  |
| 18 | `order_date` | date | Да | - |  |
| 19 | `organization_type` | character varying(255) | Нет | - |  |
| 20 | `accredited` | boolean | Нет | - |  |
| 21 | `accreditation_number` | character varying(50) | Да | - |  |
| 22 | `accreditation_date` | date | Да | - |  |
| 23 | `accreditation_certificate` | character varying(500) | Нет | - |  |
| 24 | `registration_certificate` | character varying(500) | Нет | - |  |
| 25 | `status` | character varying(50) | Нет | - | Статус записи |

---

### niokr_niokrprojectexecutor_projects

**Количество записей:** 1

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | - | Уникальный идентификатор |
| 2 | `niokrprojectexecutor_id` | bigint | Нет | - | FK на niokrprojectexecutor |
| 3 | `niokrproject_id` | bigint | Нет | - | FK на niokrproject |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `niokrproject_id` | `niokr_niokrproject.id` |
| `niokrprojectexecutor_id` | `niokr_niokrprojectexecutor.id` |

---

## oauth2

**Описание:** OAuth2 авторизация

**Таблиц в модуле:** 5

| Таблица | Записей | Описание |
|---------|---------|----------|
| `oauth2_provider_accesstoken` | 9 | - |
| `oauth2_provider_application` | 8 | - |
| `oauth2_provider_grant` | 1,037 | - |
| `oauth2_provider_idtoken` | 0 | - |
| `oauth2_provider_refreshtoken` | 0 | - |

### oauth2_provider_accesstoken

**Количество записей:** 9

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | bigint | Нет | nextval('oauth2_provider_accesstoken_id_... | Уникальный идентификатор |
| 2 | `token` | text | Нет | - |  |
| 3 | `expires` | timestamp with time zone | Нет | - |  |
| 4 | `scope` | text | Нет | - |  |
| 5 | `application_id` | bigint | Да | - | FK на application |
| 6 | `user_id` | integer | Да | - | FK на user |
| 7 | `created` | timestamp with time zone | Нет | - |  |
| 8 | `updated` | timestamp with time zone | Нет | - |  |
| 9 | `source_refresh_token_id` | bigint | Да | - | FK на source_refresh_token |
| 10 | `id_token_id` | bigint | Да | - | FK на id_token |
| 11 | `token_checksum` | character varying(64) | Нет | - |  |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `application_id` | `oauth2_provider_application.id` |
| `id_token_id` | `oauth2_provider_idtoken.id` |
| `source_refresh_token_id` | `oauth2_provider_refreshtoken.id` |
| `user_id` | `account_user.id` |

---

### oauth2_provider_application

**Количество записей:** 8

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | bigint | Нет | nextval('oauth2_provider_application_id_... | Уникальный идентификатор |
| 2 | `client_id` | character varying(100) | Нет | - | FK на client |
| 3 | `redirect_uris` | text | Нет | - |  |
| 4 | `client_type` | character varying(32) | Нет | - |  |
| 5 | `authorization_grant_type` | character varying(32) | Нет | - |  |
| 6 | `client_secret` | character varying(255) | Нет | - |  |
| 7 | `name` | character varying(255) | Нет | - | Наименование |
| 8 | `user_id` | integer | Да | - | FK на user |
| 9 | `skip_authorization` | boolean | Нет | - |  |
| 10 | `created` | timestamp with time zone | Нет | - |  |
| 11 | `updated` | timestamp with time zone | Нет | - |  |
| 12 | `algorithm` | character varying(5) | Нет | - |  |
| 13 | `post_logout_redirect_uris` | text | Нет | - |  |
| 14 | `hash_client_secret` | boolean | Нет | - |  |
| 15 | `allowed_origins` | text | Нет | - |  |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `user_id` | `account_user.id` |

---

### oauth2_provider_grant

**Количество записей:** 1,037

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | bigint | Нет | nextval('oauth2_provider_grant_id_seq'::... | Уникальный идентификатор |
| 2 | `code` | character varying(255) | Нет | - |  |
| 3 | `expires` | timestamp with time zone | Нет | - |  |
| 4 | `redirect_uri` | text | Нет | - |  |
| 5 | `scope` | text | Нет | - |  |
| 6 | `application_id` | bigint | Нет | - | FK на application |
| 7 | `user_id` | integer | Нет | - | FK на user |
| 8 | `created` | timestamp with time zone | Нет | - |  |
| 9 | `updated` | timestamp with time zone | Нет | - |  |
| 10 | `code_challenge` | character varying(128) | Нет | - |  |
| 11 | `code_challenge_method` | character varying(10) | Нет | - |  |
| 12 | `nonce` | character varying(255) | Нет | - |  |
| 13 | `claims` | text | Нет | - |  |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `application_id` | `oauth2_provider_application.id` |
| `user_id` | `account_user.id` |

---

### oauth2_provider_idtoken

**Количество записей:** 0

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | bigint | Нет | nextval('oauth2_provider_idtoken_id_seq'... | Уникальный идентификатор |
| 2 | `jti` | uuid | Нет | - |  |
| 3 | `expires` | timestamp with time zone | Нет | - |  |
| 4 | `scope` | text | Нет | - |  |
| 5 | `created` | timestamp with time zone | Нет | - |  |
| 6 | `updated` | timestamp with time zone | Нет | - |  |
| 7 | `application_id` | bigint | Да | - | FK на application |
| 8 | `user_id` | integer | Да | - | FK на user |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `application_id` | `oauth2_provider_application.id` |
| `user_id` | `account_user.id` |

---

### oauth2_provider_refreshtoken

**Количество записей:** 0

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | bigint | Нет | nextval('oauth2_provider_refreshtoken_id... | Уникальный идентификатор |
| 2 | `token` | character varying(255) | Нет | - |  |
| 3 | `access_token_id` | bigint | Да | - | FK на access_token |
| 4 | `application_id` | bigint | Нет | - | FK на application |
| 5 | `user_id` | integer | Нет | - | FK на user |
| 6 | `created` | timestamp with time zone | Нет | - |  |
| 7 | `updated` | timestamp with time zone | Нет | - |  |
| 8 | `revoked` | timestamp with time zone | Да | - |  |
| 9 | `token_family` | uuid | Да | - |  |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `access_token_id` | `oauth2_provider_accesstoken.id` |
| `application_id` | `oauth2_provider_application.id` |
| `user_id` | `account_user.id` |

---

## reversion

**Описание:** Версионирование объектов (история изменений)

**Таблиц в модуле:** 2

| Таблица | Записей | Описание |
|---------|---------|----------|
| `reversion_revision` | 19,559 | - |
| `reversion_version` | 9,281 | - |

### reversion_revision

**Количество записей:** 19,559

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('reversion_revision_id_seq'::reg... | Уникальный идентификатор |
| 2 | `date_created` | timestamp with time zone | Нет | - |  |
| 3 | `comment` | text | Нет | - |  |
| 4 | `user_id` | integer | Да | - | FK на user |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `user_id` | `account_user.id` |

---

### reversion_version

**Количество записей:** 9,281

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('reversion_version_id_seq'::regc... | Уникальный идентификатор |
| 2 | `object_id` | character varying(191) | Нет | - | FK на object |
| 3 | `format` | character varying(255) | Нет | - |  |
| 4 | `serialized_data` | text | Нет | - |  |
| 5 | `object_repr` | text | Нет | - |  |
| 6 | `content_type_id` | integer | Нет | - | FK на content_type |
| 7 | `revision_id` | integer | Нет | - | FK на revision |
| 8 | `db` | character varying(191) | Нет | - |  |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `content_type_id` | `django_content_type.id` |
| `revision_id` | `reversion_revision.id` |

---

## search

**Описание:** Поисковые запросы

**Таблиц в модуле:** 1

| Таблица | Записей | Описание |
|---------|---------|----------|
| `search_search` | 7,607 | - |

### search_search

**Количество записей:** 7,607

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('search_search_id_seq'::regclass... | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `source` | character varying(30) | Нет | - |  |
| 5 | `primary_key` | character varying(200) | Нет | - |  |
| 6 | `path` | character varying(1000) | Нет | - |  |
| 7 | `title_en` | text | Нет | - |  |
| 8 | `title_kk` | text | Нет | - |  |
| 9 | `title_ru` | text | Нет | - |  |
| 10 | `published` | boolean | Нет | - | Признак публикации |
| 11 | `author` | text | Нет | - |  |
| 12 | `content_en` | text | Нет | - |  |
| 13 | `content_kk` | text | Нет | - |  |
| 14 | `content_ru` | text | Нет | - |  |
| 15 | `search_vector_en` | tsvector | Да | - |  |
| 16 | `search_vector_kk` | tsvector | Да | - |  |
| 17 | `search_vector_ru` | tsvector | Да | - |  |

---

## service

**Описание:** Государственные услуги, заявки, формы, экспертиза

**Таблиц в модуле:** 34

| Таблица | Записей | Описание |
|---------|---------|----------|
| `service_amolog` | 0 | - |
| `service_boxstorage` | 691 | - |
| `service_documentologlog` | 1,117 | - |
| `service_expertdocument` | 0 | - |
| `service_expertise` | 787 | - |
| `service_expertisegroup` | 13 | - |
| `service_expertisegroup_users` | 25 | - |
| `service_externaldocument` | 195 | - |
| `service_externalhooklog` | 2,092 | - |
| `service_extradocument` | 101 | - |
| `service_guppurchaseapplication` | 15 | - |
| `service_guppurchaseplan` | 32 | - |
| `service_gupreport` | 267 | - |
| `service_hubform` | 282 | - |
| `service_hubformdata` | 61,635 | - |
| `service_hubformfield` | 6,603 | - |
| `service_hubformstep` | 569 | - |
| `service_pitchinggrade` | 1,538 | - |
| `service_protocol` | 104 | - |
| `service_protocol_accepted` | 467 | - |
| `service_protocol_rejected` | 606 | - |
| `service_report` | 13,110 | - |
| `service_seedmoneyreport` | 333 | - |
| `service_service` | 310 | - |
| `service_service_users` | 906 | - |
| `service_servicenote` | 2 | - |
| `service_servicerequest` | 56,322 | - |
| `service_servicerequestbpstatus` | 82,810 | - |
| `service_servicerequestlog` | 4,571 | - |
| `service_servicerequeststatus` | 2,031 | - |
| `service_techordareport` | 503 | - |
| `service_techordareportstudent` | 4 | - |
| `service_techordastudent` | 3,307 | - |
| `service_vote` | 12,945 | - |

### service_amolog

**Количество записей:** 0

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('service_amolog_id_seq'::regclas... | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `request_data` | jsonb | Нет | - |  |
| 5 | `response_data` | jsonb | Нет | - |  |
| 6 | `service_request_id` | integer | Да | - | FK на service_request |
| 7 | `delivered` | boolean | Нет | - |  |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `service_request_id` | `service_servicerequest.id` |

---

### service_boxstorage

**Количество записей:** 691

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('service_boxstorage_id_seq'::reg... | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `last_box_id` | integer | Нет | - | FK на last_box |

---

### service_documentologlog

**Количество записей:** 1,117

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('service_documentologlog_id_seq'... | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `data` | jsonb | Да | - | Дополнительные данные (JSON) |
| 5 | `log_type` | character varying(50) | Нет | - |  |
| 6 | `request_data` | jsonb | Да | - |  |

---

### service_expertdocument

**Количество записей:** 0

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('service_expertdocument_id_seq':... | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `name` | character varying(200) | Нет | - | Наименование |
| 5 | `file` | character varying(100) | Нет | - |  |
| 6 | `user_id` | integer | Нет | - | FK на user |
| 7 | `service_request_id` | integer | Нет | - | FK на service_request |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `service_request_id` | `service_servicerequest.id` |
| `user_id` | `account_user.id` |

---

### service_expertise

**Количество записей:** 787

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('service_expertise_id_seq'::regc... | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `expertise_type` | character varying(20) | Нет | - |  |
| 5 | `status` | character varying(20) | Нет | - | Статус записи |
| 6 | `data` | jsonb | Нет | - | Дополнительные данные (JSON) |
| 7 | `service_request_id` | integer | Нет | - | FK на service_request |
| 8 | `user_id` | integer | Нет | - | FK на user |
| 9 | `cep_status` | character varying(30) | Нет | - |  |
| 10 | `status_data` | jsonb | Нет | - |  |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `service_request_id` | `service_servicerequest.id` |
| `user_id` | `account_user.id` |

---

### service_expertisegroup

**Количество записей:** 13

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | - | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `key` | character varying(1000) | Нет | - |  |
| 5 | `service_id` | character varying(30) | Нет | - | FK на service |
| 6 | `data` | jsonb | Да | - | Дополнительные данные (JSON) |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `service_id` | `service_service.code` |

---

### service_expertisegroup_users

**Количество записей:** 25

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | - | Уникальный идентификатор |
| 2 | `expertisegroup_id` | integer | Нет | - | FK на expertisegroup |
| 3 | `user_id` | integer | Нет | - | FK на user |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `expertisegroup_id` | `service_expertisegroup.id` |
| `user_id` | `account_user.id` |

---

### service_externaldocument

**Количество записей:** 195

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 2 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 3 | `external_id` | character varying(100) | Нет | - | FK на external |
| 4 | `data` | jsonb | Нет | - | Дополнительные данные (JSON) |
| 5 | `service_request_id` | integer | Нет | - | FK на service_request |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `service_request_id` | `service_servicerequest.id` |

---

### service_externalhooklog

**Количество записей:** 2,092

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('service_externalhooklog_id_seq'... | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `request_data` | jsonb | Нет | - |  |
| 5 | `service_request_id` | integer | Нет | - | FK на service_request |
| 6 | `user_id` | integer | Нет | - | FK на user |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `service_request_id` | `service_servicerequest.id` |
| `user_id` | `account_user.id` |

---

### service_extradocument

**Количество записей:** 101

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('service_extradocument_id_seq'::... | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `name` | character varying(200) | Нет | - | Наименование |
| 5 | `file` | character varying(100) | Нет | - |  |
| 6 | `service_request_id` | integer | Нет | - | FK на service_request |
| 7 | `user_id` | integer | Нет | - | FK на user |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `service_request_id` | `service_servicerequest.id` |
| `user_id` | `account_user.id` |

---

### service_guppurchaseapplication

**Количество записей:** 15

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('service_guppurchaseapplication_... | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `data` | jsonb | Нет | - | Дополнительные данные (JSON) |
| 5 | `status` | character varying(50) | Нет | - | Статус записи |
| 6 | `author_id` | integer | Нет | - | FK на author |
| 7 | `service_request_id` | integer | Нет | - | FK на service_request |
| 8 | `comment` | character varying(1000) | Нет | - |  |
| 9 | `search_field` | text | Нет | - |  |
| 10 | `purchase_method` | character varying(30) | Да | - |  |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `author_id` | `account_user.id` |
| `service_request_id` | `service_servicerequest.id` |

---

### service_guppurchaseplan

**Количество записей:** 32

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('service_guppurchaseplan_id_seq'... | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `data` | jsonb | Нет | - | Дополнительные данные (JSON) |
| 5 | `status` | character varying(20) | Нет | - | Статус записи |
| 6 | `author_id` | integer | Нет | - | FK на author |
| 7 | `service_request_id` | integer | Нет | - | FK на service_request |
| 8 | `comment` | character varying(1000) | Нет | - |  |
| 9 | `search_field` | text | Нет | - |  |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `author_id` | `account_user.id` |
| `service_request_id` | `service_servicerequest.id` |

---

### service_gupreport

**Количество записей:** 267

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('service_gupreport_id_seq'::regc... | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `viewed` | ARRAY | Нет | - |  |
| 5 | `report_type` | character varying(20) | Нет | - |  |
| 6 | `data` | jsonb | Нет | - | Дополнительные данные (JSON) |
| 7 | `status` | character varying(20) | Нет | - | Статус записи |
| 8 | `author_id` | integer | Нет | - | FK на author |
| 9 | `service_request_id` | integer | Нет | - | FK на service_request |
| 10 | `comment` | character varying(1000) | Нет | - |  |
| 11 | `search_field` | text | Нет | - |  |
| 12 | `assignee_id` | integer | Да | - | FK на assignee |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `assignee_id` | `account_user.id` |
| `author_id` | `account_user.id` |
| `service_request_id` | `service_servicerequest.id` |

---

### service_hubform

**Количество записей:** 282

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('service_hubform_id_seq'::regcla... | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `name` | jsonb | Нет | - | Наименование |
| 5 | `description` | jsonb | Нет | - |  |
| 6 | `need_signature` | boolean | Нет | - |  |
| 7 | `search_field` | text | Нет | - |  |
| 8 | `organization_id` | character varying(20) | Нет | - | FK на organization |
| 9 | `amocrm_data` | jsonb | Нет | - |  |
| 10 | `extra_css` | text | Нет | - |  |
| 11 | `extra_js` | text | Нет | - |  |
| 12 | `multilanguage` | boolean | Нет | - |  |
| 13 | `is_hidden` | boolean | Да | - |  |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `organization_id` | `core_organization.code` |

---

### service_hubformdata

**Количество записей:** 61,635

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('service_hubformdata_id_seq'::re... | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `data` | jsonb | Нет | - | Дополнительные данные (JSON) |
| 5 | `signature` | jsonb | Нет | - |  |
| 6 | `hub_form_id` | integer | Нет | - | FK на hub_form |
| 7 | `data_en` | jsonb | Нет | - |  |
| 8 | `data_kk` | jsonb | Нет | - |  |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `hub_form_id` | `service_hubform.id` |

---

### service_hubformfield

**Количество записей:** 6,603

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('service_hubformfield_id_seq'::r... | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `title` | jsonb | Нет | - | Заголовок |
| 5 | `subtitle` | jsonb | Нет | - |  |
| 6 | `placeholder` | jsonb | Нет | - |  |
| 7 | `key` | character varying(51) | Нет | - |  |
| 8 | `error_message` | jsonb | Нет | - |  |
| 9 | `field_type` | character varying(40) | Нет | - |  |
| 10 | `required` | boolean | Нет | - |  |
| 11 | `multiple_answers` | boolean | Нет | - |  |
| 12 | `position` | smallint | Нет | - |  |
| 13 | `data` | jsonb | Нет | - | Дополнительные данные (JSON) |
| 14 | `hub_form_step_id` | integer | Нет | - | FK на hub_form_step |
| 15 | `group` | character varying(50) | Да | - |  |
| 16 | `example_id` | uuid | Да | - | FK на example |
| 17 | `prefill_value` | character varying(300) | Да | - |  |
| 18 | `helper_text` | jsonb | Нет | - |  |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `hub_form_step_id` | `service_hubformstep.id` |

---

### service_hubformstep

**Количество записей:** 569

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('service_hubformstep_id_seq'::re... | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `name` | jsonb | Нет | - | Наименование |
| 5 | `position` | smallint | Нет | - |  |
| 6 | `hub_form_id` | integer | Нет | - | FK на hub_form |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `hub_form_id` | `service_hubform.id` |

---

### service_pitchinggrade

**Количество записей:** 1,538

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('service_pitchinggrade_id_seq'::... | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `total` | smallint | Нет | - |  |
| 5 | `data` | jsonb | Нет | - | Дополнительные данные (JSON) |
| 6 | `service_request_id` | integer | Нет | - | FK на service_request |
| 7 | `user_id` | integer | Нет | - | FK на user |
| 8 | `pitching_type` | character varying(20) | Нет | - |  |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `service_request_id` | `service_servicerequest.id` |
| `user_id` | `account_user.id` |

---

### service_protocol

**Количество записей:** 104

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('service_protocol_id_seq'::regcl... | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `data` | jsonb | Нет | - | Дополнительные данные (JSON) |
| 5 | `signature` | jsonb | Нет | - |  |
| 6 | `service_id` | character varying(30) | Нет | - | FK на service |
| 7 | `status` | character varying(20) | Нет | - | Статус записи |
| 8 | `protocol_type` | character varying(20) | Нет | - |  |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `service_id` | `service_service.code` |

---

### service_protocol_accepted

**Количество записей:** 467

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('service_protocol_accepted_id_se... | Уникальный идентификатор |
| 2 | `protocol_id` | integer | Нет | - | FK на protocol |
| 3 | `servicerequest_id` | integer | Нет | - | FK на servicerequest |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `protocol_id` | `service_protocol.id` |
| `servicerequest_id` | `service_servicerequest.id` |

---

### service_protocol_rejected

**Количество записей:** 606

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('service_protocol_rejected_id_se... | Уникальный идентификатор |
| 2 | `protocol_id` | integer | Нет | - | FK на protocol |
| 3 | `servicerequest_id` | integer | Нет | - | FK на servicerequest |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `protocol_id` | `service_protocol.id` |
| `servicerequest_id` | `service_servicerequest.id` |

---

### service_report

**Количество записей:** 13,110

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('service_report_id_seq'::regclas... | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `year` | smallint | Нет | - |  |
| 5 | `report_type` | character varying(20) | Нет | - |  |
| 6 | `data` | jsonb | Нет | - | Дополнительные данные (JSON) |
| 7 | `signature` | jsonb | Нет | - |  |
| 8 | `status` | character varying(20) | Нет | - | Статус записи |
| 9 | `author_id` | integer | Нет | - | FK на author |
| 10 | `service_request_id` | integer | Нет | - | FK на service_request |
| 11 | `viewed` | ARRAY | Нет | - |  |
| 12 | `signed_at` | timestamp with time zone | Да | - |  |
| 13 | `version` | character varying(10) | Нет | - |  |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `author_id` | `account_user.id` |
| `service_request_id` | `service_servicerequest.id` |

---

### service_seedmoneyreport

**Количество записей:** 333

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('service_seedmoneyreport_id_seq'... | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `viewed` | ARRAY | Нет | - |  |
| 5 | `report_type` | character varying(20) | Нет | - |  |
| 6 | `data` | jsonb | Нет | - | Дополнительные данные (JSON) |
| 7 | `status` | character varying(20) | Нет | - | Статус записи |
| 8 | `comment` | text | Нет | - |  |
| 9 | `search_field` | text | Нет | - |  |
| 10 | `author_id` | integer | Нет | - | FK на author |
| 11 | `company_id` | integer | Да | - | FK на company |
| 12 | `service_request_id` | integer | Нет | - | FK на service_request |
| 13 | `signature` | jsonb | Нет | - |  |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `author_id` | `account_user.id` |
| `company_id` | `account_company.id` |
| `service_request_id` | `service_servicerequest.id` |

---

### service_service

**Количество записей:** 310

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 2 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 3 | `code` | character varying(30) | Нет | - |  |
| 4 | `name` | jsonb | Нет | - | Наименование |
| 5 | `description` | jsonb | Нет | - |  |
| 6 | `business_process` | character varying(30) | Нет | - |  |
| 7 | `date_start` | date | Да | - |  |
| 8 | `date_end` | date | Да | - |  |
| 9 | `published` | boolean | Нет | - | Признак публикации |
| 10 | `available` | boolean | Нет | - |  |
| 11 | `form_count` | smallint | Нет | - |  |
| 12 | `category` | character varying(30) | Нет | - |  |
| 13 | `hub_form_id` | integer | Нет | - | FK на hub_form |
| 14 | `organization_id` | character varying(20) | Нет | - | FK на organization |
| 15 | `page_id` | integer | Да | - | FK на page |
| 16 | `second_hub_form_id` | integer | Да | - | FK на second_hub_form |
| 17 | `categories` | ARRAY | Нет | - |  |
| 18 | `priority` | smallint | Нет | - |  |
| 19 | `roles` | ARRAY | Нет | - |  |
| 20 | `lms_data` | jsonb | Нет | - |  |
| 21 | `notifications` | jsonb | Нет | - |  |
| 22 | `image_id` | uuid | Да | - | FK на image |
| 23 | `actual` | boolean | Нет | - |  |
| 24 | `data` | jsonb | Нет | - | Дополнительные данные (JSON) |
| 25 | `status` | character varying(30) | Нет | - | Статус записи |
| 26 | `popular` | boolean | Нет | - |  |
| 27 | `games_data` | jsonb | Нет | - |  |
| 28 | `absolute_url` | character varying(100) | Нет | - |  |
| 29 | `favorite_users` | ARRAY | Нет | - |  |
| 30 | `acceptance_order` | jsonb | Нет | - |  |
| 31 | `goals` | jsonb | Нет | - |  |
| 32 | `show_on_mobile` | boolean | Нет | - |  |
| 33 | `show_register_button` | boolean | Нет | - |  |
| 34 | `time_end` | time without time zone | Да | - |  |
| 35 | `time_start` | time without time zone | Да | - |  |
| 36 | `is_hidden` | boolean | Да | - |  |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `hub_form_id` | `service_hubform.id` |
| `organization_id` | `core_organization.code` |
| `page_id` | `landing_page.id` |
| `second_hub_form_id` | `service_hubform.id` |

---

### service_service_users

**Количество записей:** 906

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('service_service_users_id_seq'::... | Уникальный идентификатор |
| 2 | `service_id` | character varying(30) | Нет | - | FK на service |
| 3 | `user_id` | integer | Нет | - | FK на user |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `service_id` | `service_service.code` |
| `user_id` | `account_user.id` |

---

### service_servicenote

**Количество записей:** 2

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('service_servicenote_id_seq'::re... | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `text` | text | Нет | - |  |
| 5 | `author_id` | integer | Нет | - | FK на author |
| 6 | `service_id` | character varying(30) | Нет | - | FK на service |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `author_id` | `account_user.id` |
| `service_id` | `service_service.code` |

---

### service_servicerequest

**Количество записей:** 56,322

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('service_servicerequest_id_seq':... | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `status` | character varying(50) | Нет | - | Статус записи |
| 5 | `search_field` | text | Нет | - |  |
| 6 | `assignee_id` | integer | Да | - | FK на assignee |
| 7 | `author_id` | integer | Нет | - | FK на author |
| 8 | `hub_form_data_id` | integer | Нет | - | FK на hub_form_data |
| 9 | `second_hub_form_data_id` | integer | Да | - | FK на second_hub_form_data |
| 10 | `service_id` | character varying(50) | Нет | - | FK на service |
| 11 | `bp_status` | character varying(50) | Нет | - |  |
| 12 | `data` | jsonb | Нет | - | Дополнительные данные (JSON) |
| 13 | `expert_id` | integer | Да | - | FK на expert |
| 14 | `viewed` | ARRAY | Нет | - |  |
| 15 | `company_id` | integer | Да | - | FK на company |
| 16 | `number` | integer | Да | - |  |
| 17 | `sent_at` | timestamp with time zone | Да | - |  |
| 18 | `parent_id` | integer | Да | - | FK на parent |
| 19 | `games_data` | jsonb | Нет | - |  |
| 20 | `egov_sign_data` | jsonb | Нет | - |  |
| 21 | `is_hidden` | boolean | Да | - |  |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `assignee_id` | `account_user.id` |
| `author_id` | `account_user.id` |
| `company_id` | `account_company.id` |
| `expert_id` | `account_user.id` |
| `hub_form_data_id` | `service_hubformdata.id` |
| `parent_id` | `service_servicerequest.id` |
| `second_hub_form_data_id` | `service_hubformdata.id` |
| `service_id` | `service_service.code` |

---

### service_servicerequestbpstatus

**Количество записей:** 82,810

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('service_servicerequestbpstatus_... | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `bp_status` | character varying(50) | Нет | - |  |
| 5 | `service_request_id` | integer | Нет | - | FK на service_request |
| 6 | `user_id` | integer | Нет | - | FK на user |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `service_request_id` | `service_servicerequest.id` |
| `user_id` | `account_user.id` |

---

### service_servicerequestlog

**Количество записей:** 4,571

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('service_servicerequestlog_id_se... | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `text` | text | Нет | - |  |
| 5 | `data` | jsonb | Нет | - | Дополнительные данные (JSON) |
| 6 | `service_request_id` | integer | Нет | - | FK на service_request |
| 7 | `user_id` | integer | Нет | - | FK на user |
| 8 | `bp_status` | character varying(50) | Нет | - |  |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `service_request_id` | `service_servicerequest.id` |
| `user_id` | `account_user.id` |

---

### service_servicerequeststatus

**Количество записей:** 2,031

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('service_servicerequeststatus_id... | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `status` | character varying(50) | Нет | - | Статус записи |
| 5 | `service_request_id` | integer | Нет | - | FK на service_request |
| 6 | `user_id` | integer | Нет | - | FK на user |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `service_request_id` | `service_servicerequest.id` |
| `user_id` | `account_user.id` |

---

### service_techordareport

**Количество записей:** 503

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('service_techordareport_id_seq':... | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `viewed` | ARRAY | Нет | - |  |
| 5 | `year` | smallint | Нет | - |  |
| 6 | `month` | smallint | Нет | - |  |
| 7 | `data` | jsonb | Нет | - | Дополнительные данные (JSON) |
| 8 | `signature` | jsonb | Нет | - |  |
| 9 | `signed_at` | timestamp with time zone | Да | - |  |
| 10 | `status` | character varying(20) | Нет | - | Статус записи |
| 11 | `author_id` | integer | Нет | - | FK на author |
| 12 | `service_request_id` | integer | Нет | - | FK на service_request |
| 13 | `comment` | character varying(500) | Нет | - |  |
| 14 | `flow` | smallint | Нет | - |  |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `author_id` | `account_user.id` |
| `service_request_id` | `service_servicerequest.id` |

---

### service_techordareportstudent

**Количество записей:** 4

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('service_techordareportstudent_i... | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `data` | jsonb | Нет | - | Дополнительные данные (JSON) |
| 5 | `signature` | jsonb | Нет | - |  |
| 6 | `signed_at` | timestamp with time zone | Да | - |  |
| 7 | `position` | smallint | Нет | - |  |
| 8 | `status` | character varying(20) | Нет | - | Статус записи |
| 9 | `user_id` | integer | Нет | - | FK на user |
| 10 | `form_data` | jsonb | Нет | - |  |
| 11 | `month` | smallint | Нет | - |  |
| 12 | `tin` | character varying(12) | Нет | - |  |
| 13 | `year` | smallint | Нет | - |  |
| 14 | `service_request_id` | integer | Да | - | FK на service_request |
| 15 | `flow` | smallint | Нет | - |  |
| 16 | `survey_data` | jsonb | Нет | - |  |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `service_request_id` | `service_servicerequest.id` |
| `user_id` | `account_user.id` |

---

### service_techordastudent

**Количество записей:** 3,307

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('service_techordastudent_id_seq'... | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `tin` | character varying(12) | Нет | - |  |
| 5 | `iin` | character varying(12) | Нет | - |  |
| 6 | `data` | jsonb | Нет | - | Дополнительные данные (JSON) |
| 7 | `status` | character varying(20) | Нет | - | Статус записи |
| 8 | `flow` | smallint | Нет | - |  |
| 9 | `can_reapply` | boolean | Нет | - |  |

---

### service_vote

**Количество записей:** 12,945

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('service_vote_id_seq'::regclass) | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `choice` | character varying(20) | Нет | - |  |
| 5 | `data` | jsonb | Нет | - | Дополнительные данные (JSON) |
| 6 | `hub_form_data_id` | integer | Нет | - | FK на hub_form_data |
| 7 | `user_id` | integer | Нет | - | FK на user |
| 8 | `service_request_id` | integer | Да | - | FK на service_request |
| 9 | `active` | boolean | Нет | - |  |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `hub_form_data_id` | `service_hubformdata.id` |
| `service_request_id` | `service_servicerequest.id` |
| `user_id` | `account_user.id` |

---

## shared

**Описание:** Общие ресурсы (медиафайлы, SEO, контекст)

**Таблиц в модуле:** 6

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

## silk

**Описание:** Профилирование запросов (для разработки)

**Таблиц в модуле:** 5

| Таблица | Записей | Описание |
|---------|---------|----------|
| `silk_profile` | 0 | - |
| `silk_profile_queries` | 0 | - |
| `silk_request` | 73 | - |
| `silk_response` | 73 | - |
| `silk_sqlquery` | 571 | - |

### silk_profile

**Количество записей:** 0

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | - | Уникальный идентификатор |
| 2 | `name` | character varying(300) | Нет | - | Наименование |
| 3 | `start_time` | timestamp with time zone | Нет | - |  |
| 4 | `end_time` | timestamp with time zone | Да | - |  |
| 5 | `time_taken` | double precision | Да | - |  |
| 6 | `file_path` | character varying(300) | Нет | - |  |
| 7 | `line_num` | integer | Да | - |  |
| 8 | `end_line_num` | integer | Да | - |  |
| 9 | `func_name` | character varying(300) | Нет | - |  |
| 10 | `exception_raised` | boolean | Нет | - |  |
| 11 | `dynamic` | boolean | Нет | - |  |
| 12 | `request_id` | character varying(36) | Да | - | FK на request |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `request_id` | `silk_request.id` |

---

### silk_profile_queries

**Количество записей:** 0

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | - | Уникальный идентификатор |
| 2 | `profile_id` | integer | Нет | - | FK на profile |
| 3 | `sqlquery_id` | integer | Нет | - | FK на sqlquery |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `profile_id` | `silk_profile.id` |
| `sqlquery_id` | `silk_sqlquery.id` |

---

### silk_request

**Количество записей:** 73

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | character varying(36) | Нет | - | Уникальный идентификатор |
| 2 | `path` | character varying(190) | Нет | - |  |
| 3 | `query_params` | text | Нет | - |  |
| 4 | `raw_body` | text | Нет | - |  |
| 5 | `body` | text | Нет | - |  |
| 6 | `method` | character varying(10) | Нет | - |  |
| 7 | `start_time` | timestamp with time zone | Нет | - |  |
| 8 | `view_name` | character varying(190) | Да | - |  |
| 9 | `end_time` | timestamp with time zone | Да | - |  |
| 10 | `time_taken` | double precision | Да | - |  |
| 11 | `encoded_headers` | text | Нет | - |  |
| 12 | `meta_time` | double precision | Да | - |  |
| 13 | `meta_num_queries` | integer | Да | - |  |
| 14 | `meta_time_spent_queries` | double precision | Да | - |  |
| 15 | `pyprofile` | text | Нет | - |  |
| 16 | `num_sql_queries` | integer | Нет | - |  |
| 17 | `prof_file` | character varying(300) | Нет | - |  |

---

### silk_response

**Количество записей:** 73

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | character varying(36) | Нет | - | Уникальный идентификатор |
| 2 | `status_code` | integer | Нет | - |  |
| 3 | `raw_body` | text | Нет | - |  |
| 4 | `body` | text | Нет | - |  |
| 5 | `encoded_headers` | text | Нет | - |  |
| 6 | `request_id` | character varying(36) | Нет | - | FK на request |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `request_id` | `silk_request.id` |

---

### silk_sqlquery

**Количество записей:** 571

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | - | Уникальный идентификатор |
| 2 | `query` | text | Нет | - |  |
| 3 | `start_time` | timestamp with time zone | Да | - |  |
| 4 | `end_time` | timestamp with time zone | Да | - |  |
| 5 | `time_taken` | double precision | Да | - |  |
| 6 | `traceback` | text | Нет | - |  |
| 7 | `request_id` | character varying(36) | Да | - | FK на request |
| 8 | `identifier` | integer | Нет | - |  |
| 9 | `analysis` | text | Да | - |  |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `request_id` | `silk_request.id` |

---

## social

**Описание:** Социальная авторизация (Google, Facebook и др.)

**Таблиц в модуле:** 5

| Таблица | Записей | Описание |
|---------|---------|----------|
| `social_auth_association` | 0 | - |
| `social_auth_code` | 0 | - |
| `social_auth_nonce` | 0 | - |
| `social_auth_partial` | 0 | - |
| `social_auth_usersocialauth` | 19,505 | - |

### social_auth_association

**Количество записей:** 0

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('social_auth_association_id_seq'... | Уникальный идентификатор |
| 2 | `server_url` | character varying(255) | Нет | - |  |
| 3 | `handle` | character varying(255) | Нет | - |  |
| 4 | `secret` | character varying(255) | Нет | - |  |
| 5 | `issued` | integer | Нет | - |  |
| 6 | `lifetime` | integer | Нет | - |  |
| 7 | `assoc_type` | character varying(64) | Нет | - |  |

---

### social_auth_code

**Количество записей:** 0

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('social_auth_code_id_seq'::regcl... | Уникальный идентификатор |
| 2 | `email` | character varying(254) | Нет | - | Электронная почта |
| 3 | `code` | character varying(32) | Нет | - |  |
| 4 | `verified` | boolean | Нет | - | Признак верификации |
| 5 | `timestamp` | timestamp with time zone | Нет | - |  |

---

### social_auth_nonce

**Количество записей:** 0

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('social_auth_nonce_id_seq'::regc... | Уникальный идентификатор |
| 2 | `server_url` | character varying(255) | Нет | - |  |
| 3 | `timestamp` | integer | Нет | - |  |
| 4 | `salt` | character varying(65) | Нет | - |  |

---

### social_auth_partial

**Количество записей:** 0

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('social_auth_partial_id_seq'::re... | Уникальный идентификатор |
| 2 | `token` | character varying(32) | Нет | - |  |
| 3 | `next_step` | smallint | Нет | - |  |
| 4 | `backend` | character varying(32) | Нет | - |  |
| 5 | `timestamp` | timestamp with time zone | Нет | - |  |
| 6 | `data` | jsonb | Нет | - | Дополнительные данные (JSON) |

---

### social_auth_usersocialauth

**Количество записей:** 19,505

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('social_auth_usersocialauth_id_s... | Уникальный идентификатор |
| 2 | `provider` | character varying(32) | Нет | - |  |
| 3 | `uid` | character varying(255) | Нет | - |  |
| 4 | `user_id` | integer | Нет | - | FK на user |
| 5 | `created` | timestamp with time zone | Нет | - |  |
| 6 | `modified` | timestamp with time zone | Нет | - |  |
| 7 | `extra_data` | jsonb | Нет | - |  |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `user_id` | `account_user.id` |

---

## techorda

**Описание:** Образовательные программы TechOrda

**Таблиц в модуле:** 7

| Таблица | Записей | Описание |
|---------|---------|----------|
| `techorda_applicationform` | 19 | - |
| `techorda_assessment` | 45 | - |
| `techorda_course` | 203 | - |
| `techorda_courseapplication` | 15 | - |
| `techorda_coursefavorite` | 16 | - |
| `techorda_flow` | 4 | - |
| `techorda_school` | 82 | - |

### techorda_applicationform

**Количество записей:** 19

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | - | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `assessment_passed` | boolean | Нет | - |  |
| 5 | `data` | jsonb | Нет | - | Дополнительные данные (JSON) |
| 6 | `status` | character varying(20) | Нет | - | Статус записи |
| 7 | `assessment_id` | integer | Да | - | FK на assessment |
| 8 | `author_id` | integer | Нет | - | FK на author |
| 9 | `flow_id` | integer | Нет | - | FK на flow |
| 10 | `course_chosen` | boolean | Нет | - |  |
| 11 | `is_grant` | boolean | Нет | - |  |
| 12 | `assessment_result` | jsonb | Нет | - |  |
| 13 | `is_resident` | boolean | Нет | - |  |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `assessment_id` | `techorda_assessment.id` |
| `author_id` | `account_user.id` |
| `flow_id` | `techorda_flow.id` |

---

### techorda_assessment

**Количество записей:** 45

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | - | Уникальный идентификатор |
| 2 | `unique_id` | character varying(10) | Нет | - | FK на unique |
| 3 | `url` | character varying(500) | Нет | - |  |
| 4 | `used` | boolean | Нет | - |  |
| 5 | `result_url` | character varying(500) | Нет | - |  |

---

### techorda_course

**Количество записей:** 203

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | - | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `name` | jsonb | Нет | - | Наименование |
| 5 | `price` | numeric | Нет | - |  |
| 6 | `description` | jsonb | Нет | - |  |
| 7 | `study_format` | character varying(100) | Нет | - |  |
| 8 | `activity_field` | character varying(200) | Нет | - |  |
| 9 | `has_entrance_exams` | boolean | Нет | - |  |
| 10 | `study_lang` | character varying(50) | Нет | - |  |
| 11 | `teaching_methodology` | character varying(200) | Нет | - |  |
| 12 | `start_date` | character varying(100) | Нет | - |  |
| 13 | `classes_format` | jsonb | Нет | - |  |
| 14 | `duration_in_week` | smallint | Нет | - |  |
| 15 | `duration_in_hour` | smallint | Нет | - |  |
| 16 | `level` | character varying(50) | Нет | - |  |
| 17 | `quotas` | smallint | Нет | - |  |
| 18 | `classes_days_of_week` | jsonb | Нет | - |  |
| 19 | `classes_time_of_day` | character varying(50) | Нет | - |  |
| 20 | `skills` | jsonb | Нет | - |  |
| 21 | `qualification` | jsonb | Нет | - |  |
| 22 | `special_condition` | jsonb | Нет | - |  |
| 23 | `active` | boolean | Нет | - |  |
| 24 | `data` | jsonb | Нет | - | Дополнительные данные (JSON) |
| 25 | `flow_id` | integer | Нет | - | FK на flow |
| 26 | `image_id` | uuid | Да | - | FK на image |
| 27 | `school_id` | integer | Нет | - | FK на school |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `flow_id` | `techorda_flow.id` |
| `school_id` | `techorda_school.id` |

---

### techorda_courseapplication

**Количество записей:** 15

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | - | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `status` | character varying(100) | Нет | - | Статус записи |
| 5 | `applicant_status` | character varying(100) | Нет | - |  |
| 6 | `round` | character varying(10) | Нет | - |  |
| 7 | `data` | jsonb | Нет | - | Дополнительные данные (JSON) |
| 8 | `application_form_id` | integer | Нет | - | FK на application_form |
| 9 | `course_id` | integer | Да | - | FK на course |
| 10 | `flow_id` | integer | Нет | - | FK на flow |
| 11 | `signature` | jsonb | Нет | - |  |
| 12 | `open_modal_window` | boolean | Нет | - |  |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `application_form_id` | `techorda_applicationform.id` |
| `course_id` | `techorda_course.id` |
| `flow_id` | `techorda_flow.id` |

---

### techorda_coursefavorite

**Количество записей:** 16

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | - | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `course_id` | integer | Нет | - | FK на course |
| 5 | `user_id` | integer | Нет | - | FK на user |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `course_id` | `techorda_course.id` |
| `user_id` | `account_user.id` |

---

### techorda_flow

**Количество записей:** 4

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | - | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `year` | integer | Нет | - |  |
| 5 | `number` | smallint | Нет | - |  |
| 6 | `active` | boolean | Нет | - |  |
| 7 | `status` | character varying(15) | Нет | - | Статус записи |
| 8 | `max_application_count` | smallint | Нет | - |  |
| 9 | `round_1_end_at` | timestamp with time zone | Да | - |  |
| 10 | `round_1_start_at` | timestamp with time zone | Да | - |  |
| 11 | `round_2_end_at` | timestamp with time zone | Да | - |  |
| 12 | `round_2_start_at` | timestamp with time zone | Да | - |  |
| 13 | `round_3_end_at` | timestamp with time zone | Да | - |  |
| 14 | `round_3_start_at` | timestamp with time zone | Да | - |  |
| 15 | `accepting_applications_end_at` | timestamp with time zone | Да | - |  |
| 16 | `accepting_applications_start_at` | timestamp with time zone | Да | - |  |
| 17 | `school_round_1_end_at` | timestamp with time zone | Да | - |  |
| 18 | `school_round_1_start_at` | timestamp with time zone | Да | - |  |
| 19 | `school_round_2_end_at` | timestamp with time zone | Да | - |  |
| 20 | `school_round_2_start_at` | timestamp with time zone | Да | - |  |
| 21 | `school_round_3_end_at` | timestamp with time zone | Да | - |  |
| 22 | `school_round_3_start_at` | timestamp with time zone | Да | - |  |

---

### techorda_school

**Количество записей:** 82

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | - | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `name` | jsonb | Нет | - | Наименование |
| 5 | `legal_address` | jsonb | Нет | - |  |
| 6 | `actual_address` | jsonb | Нет | - |  |
| 7 | `website` | character varying(100) | Нет | - |  |
| 8 | `phone` | character varying(30) | Нет | - | Номер телефона |
| 9 | `city_phone` | character varying(50) | Нет | - |  |
| 10 | `description` | jsonb | Нет | - |  |
| 11 | `short_description` | jsonb | Нет | - |  |
| 12 | `about` | jsonb | Нет | - |  |
| 13 | `instagram_url` | character varying(100) | Нет | - |  |
| 14 | `area` | character varying(100) | Нет | - |  |
| 15 | `city` | character varying(100) | Нет | - |  |
| 16 | `active` | boolean | Нет | - |  |
| 17 | `data` | jsonb | Нет | - | Дополнительные данные (JSON) |
| 18 | `rating` | double precision | Нет | - |  |
| 19 | `author_id` | integer | Нет | - | FK на author |
| 20 | `company_id` | integer | Нет | - | FK на company |
| 21 | `image_id` | uuid | Да | - | FK на image |
| 22 | `logo_id` | uuid | Да | - | FK на logo |
| 23 | `application_confirmed` | boolean | Нет | - |  |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `author_id` | `account_user.id` |
| `company_id` | `account_company.id` |

---

## thumbnail

**Описание:** Хранение превью изображений

**Таблиц в модуле:** 1

| Таблица | Записей | Описание |
|---------|---------|----------|
| `thumbnail_kvstore` | 230,644 | - |

### thumbnail_kvstore

**Количество записей:** 230,644

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `key` | character varying(200) | Нет | - |  |
| 2 | `value` | text | Нет | - |  |

---

## user

**Описание:** Сессии пользователей

**Таблиц в модуле:** 1

| Таблица | Записей | Описание |
|---------|---------|----------|
| `user_sessions_session` | 2,952,046 | - |

### user_sessions_session

**Количество записей:** 2,952,046

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `session_key` | character varying(40) | Нет | - |  |
| 2 | `session_data` | text | Нет | - |  |
| 3 | `expire_date` | timestamp with time zone | Нет | - |  |
| 4 | `user_agent` | character varying(200) | Да | - |  |
| 5 | `last_activity` | timestamp with time zone | Нет | - |  |
| 6 | `ip` | inet | Да | - |  |
| 7 | `user_id` | integer | Да | - | FK на user |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `user_id` | `account_user.id` |

---

## waffle

**Описание:** Feature flags (включение/выключение функций)

**Таблиц в модуле:** 5

| Таблица | Записей | Описание |
|---------|---------|----------|
| `waffle_flag` | 56 | - |
| `waffle_flag_groups` | 2 | - |
| `waffle_flag_users` | 24 | - |
| `waffle_sample` | 0 | - |
| `waffle_switch` | 44 | - |

### waffle_flag

**Количество записей:** 56

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('waffle_flag_id_seq'::regclass) | Уникальный идентификатор |
| 2 | `name` | character varying(100) | Нет | - | Наименование |
| 3 | `everyone` | boolean | Да | - |  |
| 4 | `percent` | numeric | Да | - |  |
| 5 | `testing` | boolean | Нет | - |  |
| 6 | `superusers` | boolean | Нет | - |  |
| 7 | `staff` | boolean | Нет | - |  |
| 8 | `authenticated` | boolean | Нет | - |  |
| 9 | `languages` | text | Нет | - |  |
| 10 | `rollout` | boolean | Нет | - |  |
| 11 | `note` | text | Нет | - |  |
| 12 | `created` | timestamp with time zone | Нет | - |  |
| 13 | `modified` | timestamp with time zone | Нет | - |  |

---

### waffle_flag_groups

**Количество записей:** 2

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('waffle_flag_groups_id_seq'::reg... | Уникальный идентификатор |
| 2 | `flag_id` | integer | Нет | - | FK на flag |
| 3 | `group_id` | integer | Нет | - | FK на group |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `flag_id` | `waffle_flag.id` |
| `group_id` | `auth_group.id` |

---

### waffle_flag_users

**Количество записей:** 24

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('waffle_flag_users_id_seq'::regc... | Уникальный идентификатор |
| 2 | `flag_id` | integer | Нет | - | FK на flag |
| 3 | `user_id` | integer | Нет | - | FK на user |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `flag_id` | `waffle_flag.id` |
| `user_id` | `account_user.id` |

---

### waffle_sample

**Количество записей:** 0

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('waffle_sample_id_seq'::regclass... | Уникальный идентификатор |
| 2 | `name` | character varying(100) | Нет | - | Наименование |
| 3 | `percent` | numeric | Нет | - |  |
| 4 | `note` | text | Нет | - |  |
| 5 | `created` | timestamp with time zone | Нет | - |  |
| 6 | `modified` | timestamp with time zone | Нет | - |  |

---

### waffle_switch

**Количество записей:** 44

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('waffle_switch_id_seq'::regclass... | Уникальный идентификатор |
| 2 | `name` | character varying(100) | Нет | - | Наименование |
| 3 | `active` | boolean | Нет | - |  |
| 4 | `note` | text | Нет | - |  |
| 5 | `created` | timestamp with time zone | Нет | - |  |
| 6 | `modified` | timestamp with time zone | Нет | - |  |

---

## Приложение: Полный список Foreign Key связей

| № | Таблица | Поле | Ссылается на таблицу | Поле |
|---|---------|------|---------------------|------|
| 1 | `account_activation` | `user_id` | `account_user` | `id` |
| 2 | `account_certificate` | `user_id` | `account_user` | `id` |
| 3 | `account_company` | `author_id` | `account_user` | `id` |
| 4 | `account_complaint` | `author_id` | `account_user` | `id` |
| 5 | `account_complaint` | `company_id` | `account_company` | `id` |
| 6 | `account_complaint` | `user_id` | `account_user` | `id` |
| 7 | `account_contactpress` | `author_id` | `account_user` | `id` |
| 8 | `account_contactpress` | `company_id` | `account_company` | `id` |
| 9 | `account_contactpress` | `user_id` | `account_user` | `id` |
| 10 | `account_contactrequest` | `author_id` | `account_user` | `id` |
| 11 | `account_contactrequest` | `user_id` | `account_user` | `id` |
| 12 | `account_course` | `user_id` | `account_user` | `id` |
| 13 | `account_education` | `user_id` | `account_user` | `id` |
| 14 | `account_experience` | `company_id` | `account_company` | `id` |
| 15 | `account_experience` | `user_id` | `account_user` | `id` |
| 16 | `account_user` | `company_id` | `account_company` | `id` |
| 17 | `account_user` | `organization_id` | `core_organization` | `code` |
| 18 | `account_usercompany` | `company_id` | `account_company` | `id` |
| 19 | `account_usercompany` | `user_id` | `account_user` | `id` |
| 20 | `account_usercompanyinvitation` | `author_id` | `account_user` | `id` |
| 21 | `account_usercompanyinvitation` | `company_id` | `account_company` | `id` |
| 22 | `account_usercompanyinvitation` | `invited_user_id` | `account_user` | `id` |
| 23 | `account_usercompanyrequest` | `company_id` | `account_company` | `id` |
| 24 | `account_usercompanyrequest` | `user_id` | `account_user` | `id` |
| 25 | `account_user_groups` | `group_id` | `auth_group` | `id` |
| 26 | `account_user_groups` | `user_id` | `account_user` | `id` |
| 27 | `account_user_user_permissions` | `permission_id` | `auth_permission` | `id` |
| 28 | `account_user_user_permissions` | `user_id` | `account_user` | `id` |
| 29 | `auth_group_permissions` | `group_id` | `auth_group` | `id` |
| 30 | `auth_group_permissions` | `permission_id` | `auth_permission` | `id` |
| 31 | `auth_permission` | `content_type_id` | `django_content_type` | `id` |
| 32 | `authtoken_token` | `user_id` | `account_user` | `id` |
| 33 | `booking_booking` | `author_id` | `account_user` | `id` |
| 34 | `booking_booking` | `company_id` | `account_company` | `id` |
| 35 | `booking_booking` | `room_id` | `booking_room` | `id` |
| 36 | `booking_bookingstatus` | `booking_id` | `booking_booking` | `id` |
| 37 | `community_companyfollow` | `followed_id` | `account_company` | `id` |
| 38 | `community_companyfollow` | `follower_id` | `account_user` | `id` |
| 39 | `community_userfollow` | `followed_id` | `account_user` | `id` |
| 40 | `community_userfollow` | `follower_id` | `account_user` | `id` |
| 41 | `core_actionlog` | `user_id` | `account_user` | `id` |
| 42 | `core_article` | `author_id` | `account_user` | `id` |
| 43 | `core_article` | `category_id` | `core_category` | `id` |
| 44 | `core_blog` | `author_id` | `account_user` | `id` |
| 45 | `core_blog` | `category_id` | `core_category` | `id` |
| 46 | `core_blog` | `company_id` | `account_company` | `id` |
| 47 | `core_category` | `background_id` | `shared_mediafile` | `id` |
| 48 | `core_city` | `country_id` | `core_country` | `id` |
| 49 | `core_comment` | `parent_id` | `core_comment` | `id` |
| 50 | `core_comment` | `user_id` | `account_user` | `id` |
| 51 | `core_discussion` | `author_id` | `account_user` | `id` |
| 52 | `core_discussion` | `category_id` | `core_category` | `id` |
| 53 | `core_discussionvote` | `discussion_id` | `core_discussion` | `id` |
| 54 | `core_discussionvote` | `user_id` | `account_user` | `id` |
| 55 | `core_elabsannouncement` | `author_id` | `account_user` | `id` |
| 56 | `core_event` | `author_id` | `account_user` | `id` |
| 57 | `core_event` | `company_id` | `account_company` | `id` |
| 58 | `core_event` | `organization_id` | `core_organization` | `code` |
| 59 | `core_eventparticipant` | `author_id` | `account_user` | `id` |
| 60 | `core_eventparticipant` | `event_id` | `core_event` | `id` |
| 61 | `core_faqitem` | `faq_id` | `core_faq` | `code` |
| 62 | `core_feed` | `article_id` | `core_article` | `id` |
| 63 | `core_feed` | `blog_id` | `core_blog` | `id` |
| 64 | `core_feed` | `discussion_id` | `core_discussion` | `id` |
| 65 | `core_feed` | `event_id` | `core_event` | `id` |
| 66 | `core_feed` | `tech_task_id` | `core_techtask` | `id` |
| 67 | `core_feed` | `vacancy_id` | `core_vacancy` | `id` |
| 68 | `core_infrastructure` | `author_id` | `account_user` | `id` |
| 69 | `core_infrastructure` | `company_id` | `account_company` | `id` |
| 70 | `core_infrastructure` | `organization_id` | `core_organization` | `code` |
| 71 | `core_infrastructure` | `parent_id` | `core_infrastructure` | `id` |
| 72 | `core_infrastructureimage` | `author_id` | `account_user` | `id` |
| 73 | `core_infrastructureimage` | `infrastructure_id` | `core_infrastructure` | `id` |
| 74 | `core_infrastructurerequest` | `author_id` | `account_user` | `id` |
| 75 | `core_infrastructurerequest` | `infrastructure_id` | `core_infrastructure` | `id` |
| 76 | `core_notification` | `user_id` | `account_user` | `id` |
| 77 | `core_techtask` | `author_id` | `account_user` | `id` |
| 78 | `core_techtasksolution` | `author_id` | `account_user` | `id` |
| 79 | `core_techtasksolution` | `tech_task_id` | `core_techtask` | `id` |
| 80 | `core_vacancy` | `author_id` | `account_user` | `id` |
| 81 | `core_vacancy` | `city_id` | `core_city` | `id` |
| 82 | `core_vacancy` | `company_id` | `account_company` | `id` |
| 83 | `core_vacancycandidate` | `author_id` | `account_user` | `id` |
| 84 | `core_vacancycandidate` | `vacancy_id` | `core_vacancy` | `id` |
| 85 | `django_admin_log` | `content_type_id` | `django_content_type` | `id` |
| 86 | `django_admin_log` | `user_id` | `account_user` | `id` |
| 87 | `explorer_query` | `created_by_user_id` | `account_user` | `id` |
| 88 | `explorer_queryfavorite` | `query_id` | `explorer_query` | `id` |
| 89 | `explorer_queryfavorite` | `user_id` | `account_user` | `id` |
| 90 | `explorer_querylog` | `query_id` | `explorer_query` | `id` |
| 91 | `explorer_querylog` | `run_by_user_id` | `account_user` | `id` |
| 92 | `journeymap_companystate` | `company_id` | `account_company` | `id` |
| 93 | `journeymap_companystate` | `journeymap_id` | `journeymap_journeymap` | `key` |
| 94 | `journeymap_question` | `task_id` | `journeymap_task` | `id` |
| 95 | `journeymap_step` | `journeymap_id` | `journeymap_journeymap` | `key` |
| 96 | `journeymap_step_next_steps` | `from_step_id` | `journeymap_step` | `id` |
| 97 | `journeymap_step_next_steps` | `to_step_id` | `journeymap_step` | `id` |
| 98 | `journeymap_task` | `step_id` | `journeymap_step` | `id` |
| 99 | `journeymap_userstate` | `journeymap_id` | `journeymap_journeymap` | `key` |
| 100 | `journeymap_userstate` | `user_id` | `account_user` | `id` |
| 101 | `landing_component` | `section_id` | `landing_section` | `id` |
| 102 | `landing_page` | `author_id` | `account_user` | `id` |
| 103 | `landing_page` | `organization_id` | `core_organization` | `code` |
| 104 | `landing_pagemediafile` | `author_id` | `account_user` | `id` |
| 105 | `landing_pagemediafile` | `page_id` | `landing_page` | `id` |
| 106 | `landing_section` | `page_id` | `landing_page` | `id` |
| 107 | `matchmaking_match` | `user_a_id` | `account_user` | `id` |
| 108 | `matchmaking_match` | `user_b_id` | `account_user` | `id` |
| 109 | `matchmaking_profile` | `user_id` | `account_user` | `id` |
| 110 | `niokr_niokrnotification_projects` | `niokrnotification_id` | `niokr_niokrnotification` | `id` |
| 111 | `niokr_niokrnotification_projects` | `niokrproject_id` | `niokr_niokrproject` | `id` |
| 112 | `niokr_niokrprojectexecutor_projects` | `niokrproject_id` | `niokr_niokrproject` | `id` |
| 113 | `niokr_niokrprojectexecutor_projects` | `niokrprojectexecutor_id` | `niokr_niokrprojectexecutor` | `id` |
| 114 | `oauth2_provider_accesstoken` | `application_id` | `oauth2_provider_application` | `id` |
| 115 | `oauth2_provider_accesstoken` | `id_token_id` | `oauth2_provider_idtoken` | `id` |
| 116 | `oauth2_provider_accesstoken` | `source_refresh_token_id` | `oauth2_provider_refreshtoken` | `id` |
| 117 | `oauth2_provider_accesstoken` | `user_id` | `account_user` | `id` |
| 118 | `oauth2_provider_application` | `user_id` | `account_user` | `id` |
| 119 | `oauth2_provider_grant` | `application_id` | `oauth2_provider_application` | `id` |
| 120 | `oauth2_provider_grant` | `user_id` | `account_user` | `id` |
| 121 | `oauth2_provider_idtoken` | `application_id` | `oauth2_provider_application` | `id` |
| 122 | `oauth2_provider_idtoken` | `user_id` | `account_user` | `id` |
| 123 | `oauth2_provider_refreshtoken` | `access_token_id` | `oauth2_provider_accesstoken` | `id` |
| 124 | `oauth2_provider_refreshtoken` | `application_id` | `oauth2_provider_application` | `id` |
| 125 | `oauth2_provider_refreshtoken` | `user_id` | `account_user` | `id` |
| 126 | `reversion_revision` | `user_id` | `account_user` | `id` |
| 127 | `reversion_version` | `content_type_id` | `django_content_type` | `id` |
| 128 | `reversion_version` | `revision_id` | `reversion_revision` | `id` |
| 129 | `service_amolog` | `service_request_id` | `service_servicerequest` | `id` |
| 130 | `service_expertdocument` | `service_request_id` | `service_servicerequest` | `id` |
| 131 | `service_expertdocument` | `user_id` | `account_user` | `id` |
| 132 | `service_expertise` | `service_request_id` | `service_servicerequest` | `id` |
| 133 | `service_expertise` | `user_id` | `account_user` | `id` |
| 134 | `service_expertisegroup` | `service_id` | `service_service` | `code` |
| 135 | `service_expertisegroup_users` | `expertisegroup_id` | `service_expertisegroup` | `id` |
| 136 | `service_expertisegroup_users` | `user_id` | `account_user` | `id` |
| 137 | `service_externaldocument` | `service_request_id` | `service_servicerequest` | `id` |
| 138 | `service_externalhooklog` | `service_request_id` | `service_servicerequest` | `id` |
| 139 | `service_externalhooklog` | `user_id` | `account_user` | `id` |
| 140 | `service_extradocument` | `service_request_id` | `service_servicerequest` | `id` |
| 141 | `service_extradocument` | `user_id` | `account_user` | `id` |
| 142 | `service_guppurchaseapplication` | `author_id` | `account_user` | `id` |
| 143 | `service_guppurchaseapplication` | `service_request_id` | `service_servicerequest` | `id` |
| 144 | `service_guppurchaseplan` | `author_id` | `account_user` | `id` |
| 145 | `service_guppurchaseplan` | `service_request_id` | `service_servicerequest` | `id` |
| 146 | `service_gupreport` | `assignee_id` | `account_user` | `id` |
| 147 | `service_gupreport` | `author_id` | `account_user` | `id` |
| 148 | `service_gupreport` | `service_request_id` | `service_servicerequest` | `id` |
| 149 | `service_hubform` | `organization_id` | `core_organization` | `code` |
| 150 | `service_hubformdata` | `hub_form_id` | `service_hubform` | `id` |
| 151 | `service_hubformfield` | `hub_form_step_id` | `service_hubformstep` | `id` |
| 152 | `service_hubformstep` | `hub_form_id` | `service_hubform` | `id` |
| 153 | `service_pitchinggrade` | `service_request_id` | `service_servicerequest` | `id` |
| 154 | `service_pitchinggrade` | `user_id` | `account_user` | `id` |
| 155 | `service_protocol` | `service_id` | `service_service` | `code` |
| 156 | `service_protocol_accepted` | `protocol_id` | `service_protocol` | `id` |
| 157 | `service_protocol_accepted` | `servicerequest_id` | `service_servicerequest` | `id` |
| 158 | `service_protocol_rejected` | `protocol_id` | `service_protocol` | `id` |
| 159 | `service_protocol_rejected` | `servicerequest_id` | `service_servicerequest` | `id` |
| 160 | `service_report` | `author_id` | `account_user` | `id` |
| 161 | `service_report` | `service_request_id` | `service_servicerequest` | `id` |
| 162 | `service_seedmoneyreport` | `author_id` | `account_user` | `id` |
| 163 | `service_seedmoneyreport` | `company_id` | `account_company` | `id` |
| 164 | `service_seedmoneyreport` | `service_request_id` | `service_servicerequest` | `id` |
| 165 | `service_service` | `hub_form_id` | `service_hubform` | `id` |
| 166 | `service_service` | `organization_id` | `core_organization` | `code` |
| 167 | `service_service` | `page_id` | `landing_page` | `id` |
| 168 | `service_service` | `second_hub_form_id` | `service_hubform` | `id` |
| 169 | `service_servicenote` | `author_id` | `account_user` | `id` |
| 170 | `service_servicenote` | `service_id` | `service_service` | `code` |
| 171 | `service_servicerequest` | `assignee_id` | `account_user` | `id` |
| 172 | `service_servicerequest` | `author_id` | `account_user` | `id` |
| 173 | `service_servicerequest` | `company_id` | `account_company` | `id` |
| 174 | `service_servicerequest` | `expert_id` | `account_user` | `id` |
| 175 | `service_servicerequest` | `hub_form_data_id` | `service_hubformdata` | `id` |
| 176 | `service_servicerequest` | `parent_id` | `service_servicerequest` | `id` |
| 177 | `service_servicerequest` | `second_hub_form_data_id` | `service_hubformdata` | `id` |
| 178 | `service_servicerequest` | `service_id` | `service_service` | `code` |
| 179 | `service_servicerequestbpstatus` | `service_request_id` | `service_servicerequest` | `id` |
| 180 | `service_servicerequestbpstatus` | `user_id` | `account_user` | `id` |
| 181 | `service_servicerequestlog` | `service_request_id` | `service_servicerequest` | `id` |
| 182 | `service_servicerequestlog` | `user_id` | `account_user` | `id` |
| 183 | `service_servicerequeststatus` | `service_request_id` | `service_servicerequest` | `id` |
| 184 | `service_servicerequeststatus` | `user_id` | `account_user` | `id` |
| 185 | `service_service_users` | `service_id` | `service_service` | `code` |
| 186 | `service_service_users` | `user_id` | `account_user` | `id` |
| 187 | `service_techordareport` | `author_id` | `account_user` | `id` |
| 188 | `service_techordareport` | `service_request_id` | `service_servicerequest` | `id` |
| 189 | `service_techordareportstudent` | `service_request_id` | `service_servicerequest` | `id` |
| 190 | `service_techordareportstudent` | `user_id` | `account_user` | `id` |
| 191 | `service_vote` | `hub_form_data_id` | `service_hubformdata` | `id` |
| 192 | `service_vote` | `service_request_id` | `service_servicerequest` | `id` |
| 193 | `service_vote` | `user_id` | `account_user` | `id` |
| 194 | `shared_mediafile` | `author_id` | `account_user` | `id` |
| 195 | `shared_protectedmediafile` | `author_id` | `account_user` | `id` |
| 196 | `silk_profile` | `request_id` | `silk_request` | `id` |
| 197 | `silk_profile_queries` | `profile_id` | `silk_profile` | `id` |
| 198 | `silk_profile_queries` | `sqlquery_id` | `silk_sqlquery` | `id` |
| 199 | `silk_response` | `request_id` | `silk_request` | `id` |
| 200 | `silk_sqlquery` | `request_id` | `silk_request` | `id` |
| 201 | `social_auth_usersocialauth` | `user_id` | `account_user` | `id` |
| 202 | `techorda_applicationform` | `assessment_id` | `techorda_assessment` | `id` |
| 203 | `techorda_applicationform` | `author_id` | `account_user` | `id` |
| 204 | `techorda_applicationform` | `flow_id` | `techorda_flow` | `id` |
| 205 | `techorda_course` | `flow_id` | `techorda_flow` | `id` |
| 206 | `techorda_course` | `school_id` | `techorda_school` | `id` |
| 207 | `techorda_courseapplication` | `application_form_id` | `techorda_applicationform` | `id` |
| 208 | `techorda_courseapplication` | `course_id` | `techorda_course` | `id` |
| 209 | `techorda_courseapplication` | `flow_id` | `techorda_flow` | `id` |
| 210 | `techorda_coursefavorite` | `course_id` | `techorda_course` | `id` |
| 211 | `techorda_coursefavorite` | `user_id` | `account_user` | `id` |
| 212 | `techorda_school` | `author_id` | `account_user` | `id` |
| 213 | `techorda_school` | `company_id` | `account_company` | `id` |
| 214 | `user_sessions_session` | `user_id` | `account_user` | `id` |
| 215 | `waffle_flag_groups` | `flag_id` | `waffle_flag` | `id` |
| 216 | `waffle_flag_groups` | `group_id` | `auth_group` | `id` |
| 217 | `waffle_flag_users` | `flag_id` | `waffle_flag` | `id` |
| 218 | `waffle_flag_users` | `user_id` | `account_user` | `id` |
