# Модуль SOCIAL

**Описание:** Социальная авторизация (Google, Facebook и др.)

**Таблиц в модуле:** 5

---

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