# Модуль SILK

**Описание:** Профилирование запросов (для разработки)

**Таблиц в модуле:** 5

---

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