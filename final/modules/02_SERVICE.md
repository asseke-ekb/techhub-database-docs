# Модуль SERVICE

**Описание:** Государственные услуги, заявки, формы, экспертиза

**Таблиц в модуле:** 34

---

| Таблица | Записей | Описание |
|---------|---------|----------|
| `service_amolog` | 0 | - |
| `service_boxstorage` | 691 | - |
| `service_documentologlog` | 1,117 | - |
| `service_expertdocument` | 0 | - |
| `service_expertise` | 787 | - |
| `service_expertisegroup` | 13 | - |
| `service_expertisegroup_users` | 25 | - |
| `service_externaldocument` | 195 | - |
| `service_externalhooklog` | 2,092 | - |
| `service_extradocument` | 101 | - |
| `service_guppurchaseapplication` | 15 | - |
| `service_guppurchaseplan` | 32 | - |
| `service_gupreport` | 267 | - |
| `service_hubform` | 282 | - |
| `service_hubformdata` | 61,635 | - |
| `service_hubformfield` | 6,603 | - |
| `service_hubformstep` | 569 | - |
| `service_pitchinggrade` | 1,538 | - |
| `service_protocol` | 104 | - |
| `service_protocol_accepted` | 467 | - |
| `service_protocol_rejected` | 606 | - |
| `service_report` | 13,110 | - |
| `service_seedmoneyreport` | 333 | - |
| `service_service` | 310 | - |
| `service_service_users` | 906 | - |
| `service_servicenote` | 2 | - |
| `service_servicerequest` | 56,322 | - |
| `service_servicerequestbpstatus` | 82,810 | - |
| `service_servicerequestlog` | 4,571 | - |
| `service_servicerequeststatus` | 2,031 | - |
| `service_techordareport` | 503 | - |
| `service_techordareportstudent` | 4 | - |
| `service_techordastudent` | 3,307 | - |
| `service_vote` | 12,945 | - |

### service_amolog

**Количество записей:** 0

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('service_amolog_id_seq'::regclas... | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `request_data` | jsonb | Нет | - |  |
| 5 | `response_data` | jsonb | Нет | - |  |
| 6 | `service_request_id` | integer | Да | - | FK на service_request |
| 7 | `delivered` | boolean | Нет | - |  |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `service_request_id` | `service_servicerequest.id` |

---

### service_boxstorage

**Количество записей:** 691

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('service_boxstorage_id_seq'::reg... | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `last_box_id` | integer | Нет | - | FK на last_box |

---

### service_documentologlog

**Количество записей:** 1,117

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('service_documentologlog_id_seq'... | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `data` | jsonb | Да | - | Дополнительные данные (JSON) |
| 5 | `log_type` | character varying(50) | Нет | - |  |
| 6 | `request_data` | jsonb | Да | - |  |

---

### service_expertdocument

**Количество записей:** 0

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('service_expertdocument_id_seq':... | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `name` | character varying(200) | Нет | - | Наименование |
| 5 | `file` | character varying(100) | Нет | - |  |
| 6 | `user_id` | integer | Нет | - | FK на user |
| 7 | `service_request_id` | integer | Нет | - | FK на service_request |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `service_request_id` | `service_servicerequest.id` |
| `user_id` | `account_user.id` |

---

### service_expertise

**Количество записей:** 787

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('service_expertise_id_seq'::regc... | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `expertise_type` | character varying(20) | Нет | - |  |
| 5 | `status` | character varying(20) | Нет | - | Статус записи |
| 6 | `data` | jsonb | Нет | - | Дополнительные данные (JSON) |
| 7 | `service_request_id` | integer | Нет | - | FK на service_request |
| 8 | `user_id` | integer | Нет | - | FK на user |
| 9 | `cep_status` | character varying(30) | Нет | - |  |
| 10 | `status_data` | jsonb | Нет | - |  |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `service_request_id` | `service_servicerequest.id` |
| `user_id` | `account_user.id` |

---

### service_expertisegroup

**Количество записей:** 13

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | - | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `key` | character varying(1000) | Нет | - |  |
| 5 | `service_id` | character varying(30) | Нет | - | FK на service |
| 6 | `data` | jsonb | Да | - | Дополнительные данные (JSON) |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `service_id` | `service_service.code` |

---

### service_expertisegroup_users

**Количество записей:** 25

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | - | Уникальный идентификатор |
| 2 | `expertisegroup_id` | integer | Нет | - | FK на expertisegroup |
| 3 | `user_id` | integer | Нет | - | FK на user |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `expertisegroup_id` | `service_expertisegroup.id` |
| `user_id` | `account_user.id` |

---

### service_externaldocument

**Количество записей:** 195

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 2 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 3 | `external_id` | character varying(100) | Нет | - | FK на external |
| 4 | `data` | jsonb | Нет | - | Дополнительные данные (JSON) |
| 5 | `service_request_id` | integer | Нет | - | FK на service_request |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `service_request_id` | `service_servicerequest.id` |

---

### service_externalhooklog

**Количество записей:** 2,092

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('service_externalhooklog_id_seq'... | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `request_data` | jsonb | Нет | - |  |
| 5 | `service_request_id` | integer | Нет | - | FK на service_request |
| 6 | `user_id` | integer | Нет | - | FK на user |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `service_request_id` | `service_servicerequest.id` |
| `user_id` | `account_user.id` |

---

### service_extradocument

**Количество записей:** 101

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('service_extradocument_id_seq'::... | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `name` | character varying(200) | Нет | - | Наименование |
| 5 | `file` | character varying(100) | Нет | - |  |
| 6 | `service_request_id` | integer | Нет | - | FK на service_request |
| 7 | `user_id` | integer | Нет | - | FK на user |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `service_request_id` | `service_servicerequest.id` |
| `user_id` | `account_user.id` |

---

### service_guppurchaseapplication

**Количество записей:** 15

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('service_guppurchaseapplication_... | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `data` | jsonb | Нет | - | Дополнительные данные (JSON) |
| 5 | `status` | character varying(50) | Нет | - | Статус записи |
| 6 | `author_id` | integer | Нет | - | FK на author |
| 7 | `service_request_id` | integer | Нет | - | FK на service_request |
| 8 | `comment` | character varying(1000) | Нет | - |  |
| 9 | `search_field` | text | Нет | - |  |
| 10 | `purchase_method` | character varying(30) | Да | - |  |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `author_id` | `account_user.id` |
| `service_request_id` | `service_servicerequest.id` |

---

### service_guppurchaseplan

**Количество записей:** 32

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('service_guppurchaseplan_id_seq'... | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `data` | jsonb | Нет | - | Дополнительные данные (JSON) |
| 5 | `status` | character varying(20) | Нет | - | Статус записи |
| 6 | `author_id` | integer | Нет | - | FK на author |
| 7 | `service_request_id` | integer | Нет | - | FK на service_request |
| 8 | `comment` | character varying(1000) | Нет | - |  |
| 9 | `search_field` | text | Нет | - |  |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `author_id` | `account_user.id` |
| `service_request_id` | `service_servicerequest.id` |

---

### service_gupreport

**Количество записей:** 267

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('service_gupreport_id_seq'::regc... | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `viewed` | ARRAY | Нет | - |  |
| 5 | `report_type` | character varying(20) | Нет | - |  |
| 6 | `data` | jsonb | Нет | - | Дополнительные данные (JSON) |
| 7 | `status` | character varying(20) | Нет | - | Статус записи |
| 8 | `author_id` | integer | Нет | - | FK на author |
| 9 | `service_request_id` | integer | Нет | - | FK на service_request |
| 10 | `comment` | character varying(1000) | Нет | - |  |
| 11 | `search_field` | text | Нет | - |  |
| 12 | `assignee_id` | integer | Да | - | FK на assignee |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `assignee_id` | `account_user.id` |
| `author_id` | `account_user.id` |
| `service_request_id` | `service_servicerequest.id` |

---

### service_hubform

**Количество записей:** 282

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('service_hubform_id_seq'::regcla... | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `name` | jsonb | Нет | - | Наименование |
| 5 | `description` | jsonb | Нет | - |  |
| 6 | `need_signature` | boolean | Нет | - |  |
| 7 | `search_field` | text | Нет | - |  |
| 8 | `organization_id` | character varying(20) | Нет | - | FK на organization |
| 9 | `amocrm_data` | jsonb | Нет | - |  |
| 10 | `extra_css` | text | Нет | - |  |
| 11 | `extra_js` | text | Нет | - |  |
| 12 | `multilanguage` | boolean | Нет | - |  |
| 13 | `is_hidden` | boolean | Да | - |  |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `organization_id` | `core_organization.code` |

---

### service_hubformdata

**Количество записей:** 61,635

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('service_hubformdata_id_seq'::re... | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `data` | jsonb | Нет | - | Дополнительные данные (JSON) |
| 5 | `signature` | jsonb | Нет | - |  |
| 6 | `hub_form_id` | integer | Нет | - | FK на hub_form |
| 7 | `data_en` | jsonb | Нет | - |  |
| 8 | `data_kk` | jsonb | Нет | - |  |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `hub_form_id` | `service_hubform.id` |

---

### service_hubformfield

**Количество записей:** 6,603

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('service_hubformfield_id_seq'::r... | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `title` | jsonb | Нет | - | Заголовок |
| 5 | `subtitle` | jsonb | Нет | - |  |
| 6 | `placeholder` | jsonb | Нет | - |  |
| 7 | `key` | character varying(51) | Нет | - |  |
| 8 | `error_message` | jsonb | Нет | - |  |
| 9 | `field_type` | character varying(40) | Нет | - |  |
| 10 | `required` | boolean | Нет | - |  |
| 11 | `multiple_answers` | boolean | Нет | - |  |
| 12 | `position` | smallint | Нет | - |  |
| 13 | `data` | jsonb | Нет | - | Дополнительные данные (JSON) |
| 14 | `hub_form_step_id` | integer | Нет | - | FK на hub_form_step |
| 15 | `group` | character varying(50) | Да | - |  |
| 16 | `example_id` | uuid | Да | - | FK на example |
| 17 | `prefill_value` | character varying(300) | Да | - |  |
| 18 | `helper_text` | jsonb | Нет | - |  |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `hub_form_step_id` | `service_hubformstep.id` |

---

### service_hubformstep

**Количество записей:** 569

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('service_hubformstep_id_seq'::re... | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `name` | jsonb | Нет | - | Наименование |
| 5 | `position` | smallint | Нет | - |  |
| 6 | `hub_form_id` | integer | Нет | - | FK на hub_form |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `hub_form_id` | `service_hubform.id` |

---

### service_pitchinggrade

**Количество записей:** 1,538

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('service_pitchinggrade_id_seq'::... | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `total` | smallint | Нет | - |  |
| 5 | `data` | jsonb | Нет | - | Дополнительные данные (JSON) |
| 6 | `service_request_id` | integer | Нет | - | FK на service_request |
| 7 | `user_id` | integer | Нет | - | FK на user |
| 8 | `pitching_type` | character varying(20) | Нет | - |  |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `service_request_id` | `service_servicerequest.id` |
| `user_id` | `account_user.id` |

---

### service_protocol

**Количество записей:** 104

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('service_protocol_id_seq'::regcl... | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `data` | jsonb | Нет | - | Дополнительные данные (JSON) |
| 5 | `signature` | jsonb | Нет | - |  |
| 6 | `service_id` | character varying(30) | Нет | - | FK на service |
| 7 | `status` | character varying(20) | Нет | - | Статус записи |
| 8 | `protocol_type` | character varying(20) | Нет | - |  |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `service_id` | `service_service.code` |

---

### service_protocol_accepted

**Количество записей:** 467

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('service_protocol_accepted_id_se... | Уникальный идентификатор |
| 2 | `protocol_id` | integer | Нет | - | FK на protocol |
| 3 | `servicerequest_id` | integer | Нет | - | FK на servicerequest |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `protocol_id` | `service_protocol.id` |
| `servicerequest_id` | `service_servicerequest.id` |

---

### service_protocol_rejected

**Количество записей:** 606

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('service_protocol_rejected_id_se... | Уникальный идентификатор |
| 2 | `protocol_id` | integer | Нет | - | FK на protocol |
| 3 | `servicerequest_id` | integer | Нет | - | FK на servicerequest |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `protocol_id` | `service_protocol.id` |
| `servicerequest_id` | `service_servicerequest.id` |

---

### service_report

**Количество записей:** 13,110

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('service_report_id_seq'::regclas... | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `year` | smallint | Нет | - |  |
| 5 | `report_type` | character varying(20) | Нет | - |  |
| 6 | `data` | jsonb | Нет | - | Дополнительные данные (JSON) |
| 7 | `signature` | jsonb | Нет | - |  |
| 8 | `status` | character varying(20) | Нет | - | Статус записи |
| 9 | `author_id` | integer | Нет | - | FK на author |
| 10 | `service_request_id` | integer | Нет | - | FK на service_request |
| 11 | `viewed` | ARRAY | Нет | - |  |
| 12 | `signed_at` | timestamp with time zone | Да | - |  |
| 13 | `version` | character varying(10) | Нет | - |  |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `author_id` | `account_user.id` |
| `service_request_id` | `service_servicerequest.id` |

---

### service_seedmoneyreport

**Количество записей:** 333

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('service_seedmoneyreport_id_seq'... | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `viewed` | ARRAY | Нет | - |  |
| 5 | `report_type` | character varying(20) | Нет | - |  |
| 6 | `data` | jsonb | Нет | - | Дополнительные данные (JSON) |
| 7 | `status` | character varying(20) | Нет | - | Статус записи |
| 8 | `comment` | text | Нет | - |  |
| 9 | `search_field` | text | Нет | - |  |
| 10 | `author_id` | integer | Нет | - | FK на author |
| 11 | `company_id` | integer | Да | - | FK на company |
| 12 | `service_request_id` | integer | Нет | - | FK на service_request |
| 13 | `signature` | jsonb | Нет | - |  |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `author_id` | `account_user.id` |
| `company_id` | `account_company.id` |
| `service_request_id` | `service_servicerequest.id` |

---

### service_service

**Количество записей:** 310

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 2 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 3 | `code` | character varying(30) | Нет | - |  |
| 4 | `name` | jsonb | Нет | - | Наименование |
| 5 | `description` | jsonb | Нет | - |  |
| 6 | `business_process` | character varying(30) | Нет | - |  |
| 7 | `date_start` | date | Да | - |  |
| 8 | `date_end` | date | Да | - |  |
| 9 | `published` | boolean | Нет | - | Признак публикации |
| 10 | `available` | boolean | Нет | - |  |
| 11 | `form_count` | smallint | Нет | - |  |
| 12 | `category` | character varying(30) | Нет | - |  |
| 13 | `hub_form_id` | integer | Нет | - | FK на hub_form |
| 14 | `organization_id` | character varying(20) | Нет | - | FK на organization |
| 15 | `page_id` | integer | Да | - | FK на page |
| 16 | `second_hub_form_id` | integer | Да | - | FK на second_hub_form |
| 17 | `categories` | ARRAY | Нет | - |  |
| 18 | `priority` | smallint | Нет | - |  |
| 19 | `roles` | ARRAY | Нет | - |  |
| 20 | `lms_data` | jsonb | Нет | - |  |
| 21 | `notifications` | jsonb | Нет | - |  |
| 22 | `image_id` | uuid | Да | - | FK на image |
| 23 | `actual` | boolean | Нет | - |  |
| 24 | `data` | jsonb | Нет | - | Дополнительные данные (JSON) |
| 25 | `status` | character varying(30) | Нет | - | Статус записи |
| 26 | `popular` | boolean | Нет | - |  |
| 27 | `games_data` | jsonb | Нет | - |  |
| 28 | `absolute_url` | character varying(100) | Нет | - |  |
| 29 | `favorite_users` | ARRAY | Нет | - |  |
| 30 | `acceptance_order` | jsonb | Нет | - |  |
| 31 | `goals` | jsonb | Нет | - |  |
| 32 | `show_on_mobile` | boolean | Нет | - |  |
| 33 | `show_register_button` | boolean | Нет | - |  |
| 34 | `time_end` | time without time zone | Да | - |  |
| 35 | `time_start` | time without time zone | Да | - |  |
| 36 | `is_hidden` | boolean | Да | - |  |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `hub_form_id` | `service_hubform.id` |
| `organization_id` | `core_organization.code` |
| `page_id` | `landing_page.id` |
| `second_hub_form_id` | `service_hubform.id` |

---

### service_service_users

**Количество записей:** 906

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('service_service_users_id_seq'::... | Уникальный идентификатор |
| 2 | `service_id` | character varying(30) | Нет | - | FK на service |
| 3 | `user_id` | integer | Нет | - | FK на user |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `service_id` | `service_service.code` |
| `user_id` | `account_user.id` |

---

### service_servicenote

**Количество записей:** 2

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('service_servicenote_id_seq'::re... | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `text` | text | Нет | - |  |
| 5 | `author_id` | integer | Нет | - | FK на author |
| 6 | `service_id` | character varying(30) | Нет | - | FK на service |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `author_id` | `account_user.id` |
| `service_id` | `service_service.code` |

---

### service_servicerequest

**Количество записей:** 56,322

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('service_servicerequest_id_seq':... | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `status` | character varying(50) | Нет | - | Статус записи |
| 5 | `search_field` | text | Нет | - |  |
| 6 | `assignee_id` | integer | Да | - | FK на assignee |
| 7 | `author_id` | integer | Нет | - | FK на author |
| 8 | `hub_form_data_id` | integer | Нет | - | FK на hub_form_data |
| 9 | `second_hub_form_data_id` | integer | Да | - | FK на second_hub_form_data |
| 10 | `service_id` | character varying(50) | Нет | - | FK на service |
| 11 | `bp_status` | character varying(50) | Нет | - |  |
| 12 | `data` | jsonb | Нет | - | Дополнительные данные (JSON) |
| 13 | `expert_id` | integer | Да | - | FK на expert |
| 14 | `viewed` | ARRAY | Нет | - |  |
| 15 | `company_id` | integer | Да | - | FK на company |
| 16 | `number` | integer | Да | - |  |
| 17 | `sent_at` | timestamp with time zone | Да | - |  |
| 18 | `parent_id` | integer | Да | - | FK на parent |
| 19 | `games_data` | jsonb | Нет | - |  |
| 20 | `egov_sign_data` | jsonb | Нет | - |  |
| 21 | `is_hidden` | boolean | Да | - |  |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `assignee_id` | `account_user.id` |
| `author_id` | `account_user.id` |
| `company_id` | `account_company.id` |
| `expert_id` | `account_user.id` |
| `hub_form_data_id` | `service_hubformdata.id` |
| `parent_id` | `service_servicerequest.id` |
| `second_hub_form_data_id` | `service_hubformdata.id` |
| `service_id` | `service_service.code` |

---

### service_servicerequestbpstatus

**Количество записей:** 82,810

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('service_servicerequestbpstatus_... | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `bp_status` | character varying(50) | Нет | - |  |
| 5 | `service_request_id` | integer | Нет | - | FK на service_request |
| 6 | `user_id` | integer | Нет | - | FK на user |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `service_request_id` | `service_servicerequest.id` |
| `user_id` | `account_user.id` |

---

### service_servicerequestlog

**Количество записей:** 4,571

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('service_servicerequestlog_id_se... | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `text` | text | Нет | - |  |
| 5 | `data` | jsonb | Нет | - | Дополнительные данные (JSON) |
| 6 | `service_request_id` | integer | Нет | - | FK на service_request |
| 7 | `user_id` | integer | Нет | - | FK на user |
| 8 | `bp_status` | character varying(50) | Нет | - |  |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `service_request_id` | `service_servicerequest.id` |
| `user_id` | `account_user.id` |

---

### service_servicerequeststatus

**Количество записей:** 2,031

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('service_servicerequeststatus_id... | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `status` | character varying(50) | Нет | - | Статус записи |
| 5 | `service_request_id` | integer | Нет | - | FK на service_request |
| 6 | `user_id` | integer | Нет | - | FK на user |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `service_request_id` | `service_servicerequest.id` |
| `user_id` | `account_user.id` |

---

### service_techordareport

**Количество записей:** 503

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('service_techordareport_id_seq':... | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `viewed` | ARRAY | Нет | - |  |
| 5 | `year` | smallint | Нет | - |  |
| 6 | `month` | smallint | Нет | - |  |
| 7 | `data` | jsonb | Нет | - | Дополнительные данные (JSON) |
| 8 | `signature` | jsonb | Нет | - |  |
| 9 | `signed_at` | timestamp with time zone | Да | - |  |
| 10 | `status` | character varying(20) | Нет | - | Статус записи |
| 11 | `author_id` | integer | Нет | - | FK на author |
| 12 | `service_request_id` | integer | Нет | - | FK на service_request |
| 13 | `comment` | character varying(500) | Нет | - |  |
| 14 | `flow` | smallint | Нет | - |  |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `author_id` | `account_user.id` |
| `service_request_id` | `service_servicerequest.id` |

---

### service_techordareportstudent

**Количество записей:** 4

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('service_techordareportstudent_i... | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `data` | jsonb | Нет | - | Дополнительные данные (JSON) |
| 5 | `signature` | jsonb | Нет | - |  |
| 6 | `signed_at` | timestamp with time zone | Да | - |  |
| 7 | `position` | smallint | Нет | - |  |
| 8 | `status` | character varying(20) | Нет | - | Статус записи |
| 9 | `user_id` | integer | Нет | - | FK на user |
| 10 | `form_data` | jsonb | Нет | - |  |
| 11 | `month` | smallint | Нет | - |  |
| 12 | `tin` | character varying(12) | Нет | - |  |
| 13 | `year` | smallint | Нет | - |  |
| 14 | `service_request_id` | integer | Да | - | FK на service_request |
| 15 | `flow` | smallint | Нет | - |  |
| 16 | `survey_data` | jsonb | Нет | - |  |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `service_request_id` | `service_servicerequest.id` |
| `user_id` | `account_user.id` |

---

### service_techordastudent

**Количество записей:** 3,307

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('service_techordastudent_id_seq'... | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `tin` | character varying(12) | Нет | - |  |
| 5 | `iin` | character varying(12) | Нет | - |  |
| 6 | `data` | jsonb | Нет | - | Дополнительные данные (JSON) |
| 7 | `status` | character varying(20) | Нет | - | Статус записи |
| 8 | `flow` | smallint | Нет | - |  |
| 9 | `can_reapply` | boolean | Нет | - |  |

---

### service_vote

**Количество записей:** 12,945

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('service_vote_id_seq'::regclass) | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `choice` | character varying(20) | Нет | - |  |
| 5 | `data` | jsonb | Нет | - | Дополнительные данные (JSON) |
| 6 | `hub_form_data_id` | integer | Нет | - | FK на hub_form_data |
| 7 | `user_id` | integer | Нет | - | FK на user |
| 8 | `service_request_id` | integer | Да | - | FK на service_request |
| 9 | `active` | boolean | Нет | - |  |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `hub_form_data_id` | `service_hubformdata.id` |
| `service_request_id` | `service_servicerequest.id` |
| `user_id` | `account_user.id` |

---