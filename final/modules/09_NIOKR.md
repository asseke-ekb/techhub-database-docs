# Модуль NIOKR

**Описание:** Научно-исследовательские проекты (НИОКР)

**Таблиц в модуле:** 5

---

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