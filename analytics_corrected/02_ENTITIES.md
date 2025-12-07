# Ключевые сущности (по реальной схеме БД)

## 1. Пользователь — `account_user`
- Регистрируется по email или телефону; email/phone могут быть подтверждены.
- Роли/права — через Django группы/permissions; доп. права в JSONB `permissions`.
- Основная компания (`company_id`), организация (`organization_id`), теги/данные в JSONB `data`, `tags`.

Ключевые поля: `id (PK)`, `email`, `phone`, `first_name/last_name`, `iin`, `role`, `is_active/blocked`, `email_verified/phone_verified`, `company_id (FK account_company)`, `organization_id (FK core_organization)`, `created_at`, `updated_at`, `last_login`, `data (jsonb)`, `tags (jsonb)`, `permissions (jsonb)`.

Связи: заявки (`service_servicerequest` автор/исполнитель/эксперт), контент (`core_event/core_vacancy/core_blog`), брони (`booking_booking`), членство (`account_usercompany`), OAuth/токены, комментарии.

## 2. Компания — `account_company`
- Юр.лицо/ИП; получает статусы/теги через услуги (IT-компания, стартап, резидент и др.).
- Автор компании — пользователь; верификация/блокировка.
- Теги в JSONB: `tag_it_company`, `tag_startup`, `tag_techpark`, `tag_corp_partner`, `tag_nii`, `tag_nedrouser`, `tag_ts_member` и др.

Ключевые поля: `id (PK)`, `tin`, `name/short_name`, `company_type`, `status`, `verified`, `address`, `email/phone/website`, `author_id (FK account_user)`, `bank/iik/bik/kbe`, `description`, `tag_* (jsonb)`, `basic_info (jsonb)`, `created_at`, `updated_at`.

Связи: сотрудники (`account_usercompany`), заявки (`service_servicerequest`), события/вакансии (`core_event/core_vacancy`), блоги, TechOrda школы.

## 3. Связь пользователь–компания — `account_usercompany`
- M:N связь с ролью (owner/member/advisor), подтверждение `verified`.
Поля: `id (PK)`, `user_id (FK account_user)`, `company_id (FK account_company)`, `role`, `verified`.

## 4. Услуга — `service_service`
- Каталог услуг; PK — `code` (varchar). Мультиязычные `data` (название/описание), связь с формой/страницей.
Поля: `code (PK)`, `data (jsonb)`, `organization_id (FK core_organization)`, `hub_form_id/second_hub_form_id (FK service_hubform)`, `page_id (FK landing_page)`, статусы активности.

## 5. Заявка на услугу — `service_servicerequest`
- Автор (user), возможно компания, исполнитель/эксперт, родительская заявка, до двух форм данных.
- Статусы: `draft/created/sent/approved/success/reject/rejected`.
Поля (ключевые): `id (PK)`, `service_id (FK service_service.code)`, `status`, `author_id (FK account_user)`, `company_id (FK account_company)`, `assignee_id (FK account_user)`, `expert_id (FK account_user)`, `hub_form_data_id`, `second_hub_form_data_id` (FK service_hubformdata), `parent_id (self)`, `data (jsonb)`, `created_at`, `updated_at`.
Связанные таблицы: `service_servicerequeststatus` (история статусов), `service_servicerequestlog`, `service_expertise`, `service_vote`, `service_report`, `service_protocol_*`, `service_external*`.

## 6. Формы и данные — `service_hubform`, `service_hubformstep`, `service_hubformfield`, `service_hubformdata`
- `service_hubform` — шаблон формы (может быть у услуги 1 или 2).
- `service_hubformdata` — JSONB blob с заполненными данными; привязка к заявке через поля в `service_servicerequest`.
- `service_hubformstep` / `service_hubformfield` — структура формы.

## 7. Событие — `core_event`
- Контент с модерацией, мультиязычные `title/content`, форматы/типы.
Поля: `id (PK)`, `title (jsonb)`, `content (jsonb)`, `slug`, `status`, `event_type`, `event_format`, `datetime_start/end`, `published`, `author_id (FK account_user)`, `company_id (FK account_company)`, `organization_id (FK core_organization)`, `view_count`, `contact_info (jsonb)`.
Связи: участники `core_eventparticipant`, комментарии, лента `core_feed`.

## 8. Вакансия — `core_vacancy`
- Мультиязычные `title/description`, тип занятости, зарплатный диапазон.
Поля: `id (PK)`, `title (jsonb)`, `description (jsonb)`, `status`, `vacancy_type`, `salary_min/max`, `published`, `author_id`, `company_id`, `city_id`.
Связи: отклики `core_vacancycandidate`, лента `core_feed`.

## 9. Блог/Статья — `core_blog`, `core_article`
- Мультиязычные поля, статусы модерации, просмотры/реакции.
Поля: `id (PK)`, `title (jsonb)`, `content (jsonb)`, `slug`, `status`, `published`, `author_id`, `company_id`, `category_id`, `tags/arrays`, `view_count`.

## 10. Комментарий — `core_comment`
- Полиморфная привязка: `source` + `primary_key`, self-FK `parent_id`.
Поля: `id (PK)`, `message`, `source`, `primary_key`, `user_id (FK account_user)`, `parent_id (self)`, `status`, реакции (arrays).

## 11. Лента — `core_feed`
- Агрегатор контента: ссылки на article/blog/discussion/event/techtask/vacancy.
Поля: `id (PK)`, FK на разные сущности, `created_at`, `published`, `status`.

## 12. Бронирование — `booking_room`, `booking_booking`, `booking_bookingstatus`
- `booking_room`: справочник комнат (16 строк).
- `booking_booking`: факт брони с `room_id`, `author_id`, `company_id`, `start/end`, `status (active/finished/deactivated)`.
- `booking_bookingstatus`: история смены статусов.

## 13. TechOrda (обучение)
- Таблицы: `techorda_course`, `techorda_flow`, `techorda_school`, `techorda_applicationform`, `techorda_courseapplication`, `techorda_coursefavorite`.
- В сервисах: `service_techordastudent`, `service_techordareport`, `service_techordareportstudent`.

## 14. Медиа и SEO — `shared_mediafile`, `shared_protectedmediafile`, `shared_contextdata`, `shared_seodata`, `shared_smslog`, `shared_largecache`.
- Публичные/защищённые файлы, SEO/контекст, SMS логи.

