# Модуль TECHORDA

**Описание:** Образовательные программы TechOrda

**Таблиц в модуле:** 7

---

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