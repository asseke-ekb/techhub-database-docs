# TechHub – аналитическая документация (актуальная по схеме БД)

## Структура набора документов
| Файл | Назначение |
|------|------------|
| 01_BUSINESS_DOMAINS.md | Доменные области и роли данных |
| 02_ENTITIES.md | Ключевые сущности и бизнес-описания |
| 03_DICTIONARIES.md | Справочники и статусы (фактические) |
| 04_BUSINESS_PROCESSES.md | Процессы и точки данных для аналитики |
| 05_DATA_MODEL.md | Укрупнённая модель данных (по реальной схеме) |

## Источник правды
- PostgreSQL база `techhub`, схема `public` (157 таблиц, 218 FK) — см. `SA_FULL_ENTITY_ANALYSIS.md` в корне.
- Основные домены: `account`, `service`, `core`, `booking`, `techorda`, `landing`, `shared` + тех.таблицы Django/Auth/Logs.
- PK/FK и поля выровнены по фактической схеме (например, `service_service.code` — PK; `service_servicerequest` имеет `assignee_id`, `expert_id`, `hub_form_data_id`, `second_hub_form_data_id`, `parent_id`; `booking_room` = 16 строк, `booking_bookingstatus` есть, `booking_worktime` нет).

## Чем отличаются от старых файлов
- Убраны несуществующие таблицы (`booking_worktime`, `techorda_program/stream`, `shared_file/region` и т.п.).
- Добавлены реальные сущности (`techorda_course/flow/school`, `service_*` поля, `shared_mediafile/protectedmediafile`, `landing_*`).
- Исправлены PK/FK, статусы, мультиязычные и JSONB поля, численности записей.

