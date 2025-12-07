# Модуль USER

**Описание:** Сессии пользователей

**Таблиц в модуле:** 1

---

| Таблица | Записей | Описание |
|---------|---------|----------|
| `user_sessions_session` | 2,952,046 | - |

### user_sessions_session

**Количество записей:** 2,952,046

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `session_key` | character varying(40) | Нет | - |  |
| 2 | `session_data` | text | Нет | - |  |
| 3 | `expire_date` | timestamp with time zone | Нет | - |  |
| 4 | `user_agent` | character varying(200) | Да | - |  |
| 5 | `last_activity` | timestamp with time zone | Нет | - |  |
| 6 | `ip` | inet | Да | - |  |
| 7 | `user_id` | integer | Да | - | FK на user |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `user_id` | `account_user.id` |

---