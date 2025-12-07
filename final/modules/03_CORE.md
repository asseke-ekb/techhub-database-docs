# Модуль CORE

**Описание:** Основной контент: события, вакансии, блоги, статьи, тех.задания

**Таблиц в модуле:** 27

---

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