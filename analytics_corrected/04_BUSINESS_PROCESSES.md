# Бизнес-процессы (фактические статусы/поля)

## 1. Заявка на услугу (SERVICE)
Участники: Автор (user), Компания (optional), Исполнитель/Эксперт (user), Модератор.

Жизненный цикл:
```
draft -> created -> sent -> (correction -> sent) -> approved -> success / reject|rejected
```

Критичные данные для аналитики:
- `service_servicerequest`: `status`, `service_id`, `author_id`, `company_id`, `assignee_id`, `expert_id`, `parent_id`, `created_at`, `updated_at`, `hub_form_data_id`, `second_hub_form_data_id`.
- История статусов: `service_servicerequeststatus` (кто/когда).
- Экспертизы/голоса: `service_expertise`, `service_vote`.
- Протоколы/отчёты: `service_protocol_*`, `service_report`, `service_seedmoneyreport`, `service_techordareport`.
- Данные формы: `service_hubformdata.data` (JSONB), привязка через поля заявки.

Метрики: конверсия по статусам, T2Approve/T2Success, доля отклонений, нагрузка по исполнителям/экспертам, успешность по услугам.

## 2. Контент (CORE) — события/вакансии/блоги/статьи
Жизненный цикл (общий): `draft -> sent -> correction -> success | reject | deleted`

События (`core_event`):
- Поля: `event_type`, `event_format`, `status`, `datetime_start/end`, `published`, `company_id/organization_id`, `view_count`, `contact_info (jsonb)`.
- Участники: `core_eventparticipant`.
Метрики: публикации, регистрации/участники, просмотры, конверсия участник/просмотр, по организаторам.

Вакансии (`core_vacancy`):
- Поля: `vacancy_type`, `status`, `salary_min/max`, `city_id`, `company_id`, `published`.
- Кандидаты: `core_vacancycandidate`.
Метрики: активные вакансии, кандидаты/вакансию, средние зарплаты, время жизни вакансии.

Блоги/статьи (`core_blog`, `core_article`):
- Поля: мультиязычное `title/content`, `status`, `published`, `author_id/company_id`, `category_id`, `view_count`, реакции.
Метрики: публикации, просмотры, реакции, по авторам/компаниям.

Комментарии (`core_comment`):
- Поля: `source`, `primary_key`, `parent_id`, `user_id`, `status`, реакции.
Метрики: активность комментариев по типам контента.

Лента (`core_feed`):
- Ссылается на article/blog/discussion/event/techtask/vacancy.
Использование: агрегаты по типам контента, “топы”.

## 3. Бронирование (BOOKING)
Процесс: создать бронь → активна → завершается по времени или отменяется.
- Таблицы: `booking_room`, `booking_booking`, `booking_bookingstatus`.
- Поля важные: `room_id`, `author_id`, `company_id`, `start`, `end`, `status`.
- Метрики: загрузка комнат, отмены, пересечения (DQ), длительность.

## 4. TechOrda (обучение)
- Сущности: `techorda_course`, `techorda_flow`, `techorda_school`, заявки/избранное курсов; в сервисах — `service_techordastudent`, `service_techordareport`.
- Процессы: запись на курс (через service), обучение, отчётность.
- Метрики: заявки/студенты по курсам/школам, выпуск/отчёты.

## 5. Медиа/SEO/файлы (SHARED)
- `shared_mediafile`, `shared_protectedmediafile`, `shared_contextdata`, `shared_seodata`, `shared_smslog`.
- Использование: ресурсы для контента/лендингов, лог SMS.

## 6. Авторизация/безопасность
- Таблицы: `auth_*`, `oauth2_*`, `authtoken_token`, `waffle_*`, `awsdjangoses_*`, `social_auth_*`.
- Метрики: не для BI контента; использовать аккуратно для аудита/безопасности.

## 7. Технические/шумовые
- `user_sessions_session`, `django_session`, `silk_*`, `hub_cache_table`, `thumbnail_kvstore` и др. — исключать из аналитических витрин (шум/кеш).

