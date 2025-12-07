# Модуль DJANGO

**Описание:** Системные таблицы Django (миграции, сессии, логи)

**Таблиц в модуле:** 5

---

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