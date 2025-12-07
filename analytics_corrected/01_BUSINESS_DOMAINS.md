# Бизнес-домены TechHub (актуально по схеме БД)

## Домены и их роли
| Домен | Префиксы таблиц | Назначение | Ключевые сущности |
|-------|-----------------|------------|-------------------|
| ACCOUNT | `account_` | Идентификация пользователей и компаний | user, company, usercompany, activation, complaint |
| SERVICE | `service_` | Каталог услуг и заявки, экспертиза, формы | service, servicerequest, hubform, hubformdata, expertise, report, protocol, vote |
| CORE | `core_` | Контент: события, вакансии, блоги, статьи, лента, комментарии | event, eventparticipant, vacancy, vacancycandidate, blog, article, comment, feed, notification, actionlog |
| BOOKING | `booking_` | Бронирование комнат | room, booking, bookingstatus |
| TECHORDA | `techorda_` (+ часть `service_`) | Образовательные программы TechOrda | course, flow, school, courseapplication, coursefavorite; в сервисах — techordastudent/report |
| LANDING | `landing_` | CMS для лендингов | landing, page, section, component, pagemediafile |
| SHARED | `shared_` | Общие файлы/медиа/контекст | mediafile, protectedmediafile, contextdata, seodata, smslog, largecache |
| AUTH/SECURITY | `auth_`, `oauth2_`, `authtoken_`, `waffle_`, `awsdjangoses_` | Авторизация, токены, feature-flags, почта | группы/права, OAuth2, токены, флаги |
| Технические | `django_`, `silk_`, `social_auth_`, `thumbnail_`, `user_sessions_`, `hub_cache_table` | Логи, профилирование, сессии, кеши | как в схеме |

## Основные объёмы (по анализу схемы)
- Пользователи: `account_user` ~54k
- Компании: `account_company` ~6.6k
- Заявки на услуги: `service_servicerequest` ~56k
- Данные форм: `service_hubformdata` ~61k
- События: `core_event` ~1.5k; участники ~0.8k
- Вакансии: `core_vacancy` ~1.2k; кандидаты ~5.3k
- Бронирования: `booking_booking` ~8.7k
- Логи действий: `core_actionlog` ~125k
- Сессии: `user_sessions_session` ~2.9M (шум для аналитики)

## Взаимосвязи доменов
- ACCOUNT → SERVICE: автор/компания в заявках; эксперты/исполнители.
- ACCOUNT → CORE: авторы контента, организаторы событий/вакансий/блогов.
- ACCOUNT → BOOKING: автор бронирования.
- ACCOUNT → TECHORDA: студенты/заявки через сервисные таблицы.
- SERVICE → CORE/BOOKING: нет прямых связей, только через пользователей/компании.
- SHARED используется для медиа и SEO/контента в CORE/LANDING/SERVICE.

## Что важно для аналитики
- Статусы и временные метки: заявки, контент, бронирования.
- Теги и JSONB: `account_company.tag_*`, `account_user.data/tags/permissions`, мультиязычные поля `title/content` (ru/kk/en).
- Счётчики и связи M:N: `account_usercompany`, `core_feed`, полиморфные `core_comment`.
- Исключаем из витрин как шум: `user_sessions_session`, `django_session`, `silk_*`, `hub_cache_table`, часть технических кешей.

