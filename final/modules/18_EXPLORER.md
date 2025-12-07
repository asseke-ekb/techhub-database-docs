# Модуль EXPLORER

**Описание:** SQL Explorer для аналитики

**Таблиц в модуле:** 3

---

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