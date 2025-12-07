# Модуль BOOKING

**Описание:** Бронирование переговорных комнат и помещений

**Таблиц в модуле:** 3

---

| Таблица | Записей | Описание |
|---------|---------|----------|
| `booking_booking` | 8,673 | - |
| `booking_bookingstatus` | 8,691 | - |
| `booking_room` | 16 | - |

### booking_booking

**Количество записей:** 8,673

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('booking_booking_id_seq'::regcla... | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `status` | character varying(20) | Нет | - | Статус записи |
| 5 | `full_name` | character varying(200) | Нет | - |  |
| 6 | `email` | character varying(200) | Нет | - | Электронная почта |
| 7 | `phone` | character varying(30) | Нет | - | Номер телефона |
| 8 | `company_name_old` | character varying(200) | Нет | - |  |
| 9 | `title` | character varying(100) | Нет | - | Заголовок |
| 10 | `start` | timestamp with time zone | Нет | - |  |
| 11 | `end` | timestamp with time zone | Нет | - |  |
| 12 | `author_id` | integer | Нет | - | FK на author |
| 13 | `room_id` | integer | Нет | - | FK на room |
| 14 | `data` | jsonb | Нет | - | Дополнительные данные (JSON) |
| 15 | `company_id` | integer | Да | - | FK на company |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `author_id` | `account_user.id` |
| `company_id` | `account_company.id` |
| `room_id` | `booking_room.id` |

---

### booking_bookingstatus

**Количество записей:** 8,691

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('booking_bookingstatus_id_seq'::... | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `status` | character varying(20) | Нет | - | Статус записи |
| 5 | `comment` | character varying(200) | Нет | - |  |
| 6 | `data` | jsonb | Нет | - | Дополнительные данные (JSON) |
| 7 | `booking_id` | integer | Нет | - | FK на booking |
| 8 | `start` | timestamp with time zone | Да | - |  |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `booking_id` | `booking_booking.id` |

---

### booking_room

**Количество записей:** 16

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('booking_room_id_seq'::regclass) | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `name` | character varying(50) | Нет | - | Наименование |
| 5 | `floor` | smallint | Нет | - |  |
| 6 | `max_people` | smallint | Нет | - |  |
| 7 | `external_id` | character varying(200) | Нет | - | FK на external |
| 8 | `data` | jsonb | Нет | - | Дополнительные данные (JSON) |
| 9 | `image_id` | uuid | Да | - | FK на image |
| 10 | `pavilion` | character varying(10) | Да | - |  |
| 11 | `is_active` | boolean | Нет | - | Признак активности |

---