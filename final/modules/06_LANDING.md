# Модуль LANDING

**Описание:** CMS для лендингов и страниц

**Таблиц в модуле:** 5

---

| Таблица | Записей | Описание |
|---------|---------|----------|
| `landing_component` | 2,790 | - |
| `landing_landing` | 8 | - |
| `landing_page` | 562 | - |
| `landing_pagemediafile` | 18,517 | - |
| `landing_section` | 560 | - |

### landing_component

**Количество записей:** 2,790

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('landing_component_id_seq'::regc... | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `container_type` | character varying(50) | Нет | - |  |
| 5 | `component_type` | character varying(50) | Нет | - |  |
| 6 | `position` | smallint | Нет | - |  |
| 7 | `data` | jsonb | Нет | - | Дополнительные данные (JSON) |
| 8 | `section_id` | integer | Нет | - | FK на section |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `section_id` | `landing_section.id` |

---

### landing_landing

**Количество записей:** 8

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('landing_landing_id_seq'::regcla... | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `name` | jsonb | Нет | - | Наименование |
| 5 | `endpoint` | character varying(200) | Нет | - |  |
| 6 | `template` | character varying(200) | Нет | - |  |
| 7 | `data` | jsonb | Нет | - | Дополнительные данные (JSON) |
| 8 | `published` | boolean | Нет | - | Признак публикации |
| 9 | `show_crm_button` | boolean | Нет | - |  |
| 10 | `extra_context` | jsonb | Нет | - |  |

---

### landing_page

**Количество записей:** 562

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('landing_page_id_seq'::regclass) | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `name` | character varying(200) | Нет | - | Наименование |
| 5 | `endpoint` | character varying(200) | Нет | - |  |
| 6 | `page_type` | character varying(500) | Нет | - |  |
| 7 | `data` | jsonb | Нет | - | Дополнительные данные (JSON) |
| 8 | `published` | boolean | Нет | - | Признак публикации |
| 9 | `publish_date` | timestamp with time zone | Да | - |  |
| 10 | `organization_id` | character varying(20) | Да | - | FK на organization |
| 11 | `view_count` | integer | Нет | - |  |
| 12 | `show_crm_button` | boolean | Нет | - |  |
| 13 | `extra_css` | text | Нет | - |  |
| 14 | `extra_js` | text | Нет | - |  |
| 15 | `author_id` | integer | Да | - | FK на author |
| 16 | `authorization_required` | boolean | Нет | - |  |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `author_id` | `account_user.id` |
| `organization_id` | `core_organization.code` |

---

### landing_pagemediafile

**Количество записей:** 18,517

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('landing_pagemediafile_id_seq'::... | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `file` | character varying(100) | Нет | - |  |
| 5 | `thumbnail` | character varying(100) | Да | - |  |
| 6 | `mime_type` | character varying(50) | Нет | - |  |
| 7 | `size` | double precision | Нет | - |  |
| 8 | `page_id` | integer | Нет | - | FK на page |
| 9 | `thumbnail_150` | character varying(100) | Да | - |  |
| 10 | `thumbnail_1500` | character varying(100) | Да | - |  |
| 11 | `thumbnail_800` | character varying(100) | Да | - |  |
| 12 | `author_id` | integer | Да | - | FK на author |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `author_id` | `account_user.id` |
| `page_id` | `landing_page.id` |

---

### landing_section

**Количество записей:** 560

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('landing_section_id_seq'::regcla... | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `section_type` | character varying(500) | Нет | - |  |
| 5 | `position` | smallint | Нет | - |  |
| 6 | `data` | jsonb | Нет | - | Дополнительные данные (JSON) |
| 7 | `page_id` | integer | Нет | - | FK на page |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `page_id` | `landing_page.id` |

---