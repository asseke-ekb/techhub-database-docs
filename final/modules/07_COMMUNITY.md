# Модуль COMMUNITY

**Описание:** Социальные связи (подписки, фолловинг)

**Таблиц в модуле:** 2

---

| Таблица | Записей | Описание |
|---------|---------|----------|
| `community_companyfollow` | 3 | - |
| `community_userfollow` | 18 | - |

### community_companyfollow

**Количество записей:** 3

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | - | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `followed_id` | integer | Нет | - | FK на followed |
| 5 | `follower_id` | integer | Нет | - | FK на follower |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `followed_id` | `account_company.id` |
| `follower_id` | `account_user.id` |

---

### community_userfollow

**Количество записей:** 18

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | - | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `followed_id` | integer | Нет | - | FK на followed |
| 5 | `follower_id` | integer | Нет | - | FK на follower |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `followed_id` | `account_user.id` |
| `follower_id` | `account_user.id` |

---