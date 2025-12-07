# Модуль AUTH

**Описание:** Стандартная аутентификация Django (группы, права)

**Таблиц в модуле:** 3

---

| Таблица | Записей | Описание |
|---------|---------|----------|
| `auth_group` | 11 | - |
| `auth_group_permissions` | 1,114 | - |
| `auth_permission` | 625 | - |

### auth_group

**Количество записей:** 11

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('auth_group_id_seq'::regclass) | Уникальный идентификатор |
| 2 | `name` | character varying(150) | Нет | - | Наименование |

---

### auth_group_permissions

**Количество записей:** 1,114

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('auth_group_permissions_id_seq':... | Уникальный идентификатор |
| 2 | `group_id` | integer | Нет | - | FK на group |
| 3 | `permission_id` | integer | Нет | - | FK на permission |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `group_id` | `auth_group.id` |
| `permission_id` | `auth_permission.id` |

---

### auth_permission

**Количество записей:** 625

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('auth_permission_id_seq'::regcla... | Уникальный идентификатор |
| 2 | `name` | character varying(255) | Нет | - | Наименование |
| 3 | `content_type_id` | integer | Нет | - | FK на content_type |
| 4 | `codename` | character varying(100) | Нет | - |  |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `content_type_id` | `django_content_type.id` |

---