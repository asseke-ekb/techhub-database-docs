# Модуль ASTANAHUB

**Описание:** Общие данные платформы Астана Хаб

**Таблиц в модуле:** 3

---

| Таблица | Записей | Описание |
|---------|---------|----------|
| `astanahub_shared_contextdata` | 0 | - |
| `astanahub_shared_seodata` | 0 | - |
| `astanahub_shared_smslog` | 651 | - |

### astanahub_shared_contextdata

**Количество записей:** 0

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 2 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 3 | `key` | character varying(30) | Нет | - |  |
| 4 | `data` | jsonb | Нет | - | Дополнительные данные (JSON) |
| 5 | `description` | character varying(200) | Нет | - |  |

---

### astanahub_shared_seodata

**Количество записей:** 0

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 2 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 3 | `key` | character varying(30) | Нет | - |  |
| 4 | `title` | jsonb | Нет | - | Заголовок |
| 5 | `description` | jsonb | Нет | - |  |
| 6 | `keywords` | jsonb | Нет | - |  |

---

### astanahub_shared_smslog

**Количество записей:** 651

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | bigint | Нет | - | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `phone` | character varying(100) | Нет | - | Номер телефона |
| 5 | `request` | text | Нет | - |  |
| 6 | `response` | text | Нет | - |  |

---