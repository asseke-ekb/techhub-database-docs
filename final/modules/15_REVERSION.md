# Модуль REVERSION

**Описание:** Версионирование объектов (история изменений)

**Таблиц в модуле:** 2

---

| Таблица | Записей | Описание |
|---------|---------|----------|
| `reversion_revision` | 19,559 | - |
| `reversion_version` | 9,281 | - |

### reversion_revision

**Количество записей:** 19,559

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('reversion_revision_id_seq'::reg... | Уникальный идентификатор |
| 2 | `date_created` | timestamp with time zone | Нет | - |  |
| 3 | `comment` | text | Нет | - |  |
| 4 | `user_id` | integer | Да | - | FK на user |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `user_id` | `account_user.id` |

---

### reversion_version

**Количество записей:** 9,281

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('reversion_version_id_seq'::regc... | Уникальный идентификатор |
| 2 | `object_id` | character varying(191) | Нет | - | FK на object |
| 3 | `format` | character varying(255) | Нет | - |  |
| 4 | `serialized_data` | text | Нет | - |  |
| 5 | `object_repr` | text | Нет | - |  |
| 6 | `content_type_id` | integer | Нет | - | FK на content_type |
| 7 | `revision_id` | integer | Нет | - | FK на revision |
| 8 | `db` | character varying(191) | Нет | - |  |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `content_type_id` | `django_content_type.id` |
| `revision_id` | `reversion_revision.id` |

---