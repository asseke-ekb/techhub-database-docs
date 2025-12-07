# Справочники и статусы (фактические)

## Статусы заявок `service_servicerequest.status`
| Код | Описание |
|-----|----------|
| draft | Черновик |
| created | Создана (для части услуг) |
| sent | На рассмотрении |
| correction | На доработке |
| approved | Предварительно одобрена |
| success | Успешно завершена |
| reject | Отклонена |
| rejected | Отклонена (альт. код) |

## Статусы контента (события/вакансии/блоги/статьи)
| Код | Описание |
|-----|----------|
| draft | Черновик |
| sent | На модерации |
| correction | На доработке |
| success | Опубликовано |
| reject | Отклонено |
| deleted | Удалено |

## Бронирование `booking_booking.status`
| Код | Описание |
|-----|----------|
| active | Подтверждено |
| finished | Завершено |
| deactivated | Отменено |

## Мероприятия
- `core_event.event_type`: `open_event`, `closed_event`
- `core_event.event_format`: `astanahub`, `online`, `hybrid`

## Вакансии
- `core_vacancy.vacancy_type`: `fulltime`, `parttime`, `internship`, `project`, `volunteering`, `absense_period`

## Компании
- `account_company.company_type`: `law`, `ip`, `unknown`
- `account_company.status`: `active`, `blocked`
- Теги (JSONB): `tag_it_company`, `tag_startup`, `tag_techpark`, `tag_corp_partner`, `tag_nii`, `tag_nedrouser`, `tag_ts_member`, …

## Пользователи
- Системные роли (ключевые): `user`, `admin`, `superadmin`, `moderator`, `expert`, `manager`, `techorda_manager`, `niokr_admin`, др.
- Теги (JSONB `data`/`tags`): `tag_investor`, `tag_it_specialist`, `tag_intern`, `tag_expert`, `tag_startup_member`, `tag_company_member`, `tag_student`, `tag_teacher`, `tag_scientist`, `tag_ai_specialist`, …

## Мультиязычные поля (JSONB ru/kk/en)
Таблицы: `core_event`, `core_vacancy`, `core_blog`, `core_article`, `service_service`, `service_hubformfield`, `core_category`, `core_city`, `core_organization` (name), `landing_*` контент.

Пример структуры:
```json
{"ru": "Заголовок", "kk": "Тақырып", "en": "Title"}
```

## Поля JSONB (ключевые для разворота в Silver/BI)
- `account_user.data`, `account_user.tags`, `account_user.permissions`
- `account_company.tag_*`, `account_company.basic_info`
- `service_hubformdata.data` (динамические формы услуг)
- `service_service.data` (название/описание услуг)
- `core_event.contact_info`, `core_event.title/content`, `core_vacancy.title/description`, `core_blog.title/content`

