# Модуль ADMIN

**Описание:** Административные функции Django

**Таблиц в модуле:** 1

---

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