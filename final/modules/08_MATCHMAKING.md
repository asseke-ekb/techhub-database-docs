# Модуль MATCHMAKING

**Описание:** Нетворкинг и мэтчинг пользователей

**Таблиц в модуле:** 2

---

| Таблица | Записей | Описание |
|---------|---------|----------|
| `matchmaking_match` | 31 | - |
| `matchmaking_profile` | 19 | - |

### matchmaking_match

**Количество записей:** 31

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | - | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `date` | date | Нет | - |  |
| 5 | `user_a_id` | integer | Нет | - | FK на user_a |
| 6 | `user_b_id` | integer | Нет | - | FK на user_b |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `user_a_id` | `account_user.id` |
| `user_b_id` | `account_user.id` |

---

### matchmaking_profile

**Количество записей:** 19

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | - | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `activity` | character varying(255) | Нет | - |  |
| 5 | `contact` | character varying(255) | Нет | - |  |
| 6 | `data` | jsonb | Нет | - | Дополнительные данные (JSON) |
| 7 | `user_id` | integer | Нет | - | FK на user |
| 8 | `is_active` | boolean | Нет | - | Признак активности |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `user_id` | `account_user.id` |

---