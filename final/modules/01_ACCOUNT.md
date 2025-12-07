# Модуль ACCOUNT

**Описание:** Управление пользователями, компаниями, аутентификацией и авторизацией

**Таблиц в модуле:** 16

---

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