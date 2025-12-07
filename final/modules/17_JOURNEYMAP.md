# Модуль JOURNEYMAP

**Описание:** Карты развития для компаний и пользователей

**Таблиц в модуле:** 7

---

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