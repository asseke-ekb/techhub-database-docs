# TechHub - Документация для аналитиков

## О платформе

**TechHub** — цифровая платформа технопарка «Астана Хаб» для поддержки IT-компаний, стартапов и предоставления государственных услуг.

| Метрика | Значение |
|---------|----------|
| Пользователей | 54,000+ |
| Компаний | 6,600+ |
| Заявок на услуги | 56,000+ |
| Таблиц в БД | 157 |

---

## Содержание документации

| # | Документ | Описание |
|---|----------|----------|
| 1 | [01_OVERVIEW.md](01_OVERVIEW.md) | Обзор системы, архитектура, модули |
| 2 | [02_ENTITIES.md](02_ENTITIES.md) | Детальное описание ключевых сущностей |
| 3 | [03_ER_DIAGRAMS.md](03_ER_DIAGRAMS.md) | ER-диаграммы связей (Mermaid) |
| 4 | [04_DICTIONARIES.md](04_DICTIONARIES.md) | Справочники значений (статусы, роли, типы) |
| 5 | [05_SQL_EXAMPLES.md](05_SQL_EXAMPLES.md) | Готовые SQL-запросы для аналитики |

---

## Модули базы данных

Полное описание всех 157 таблиц по модулям:

### Бизнес-модули (основные)

| # | Модуль | Таблиц | Описание |
|---|--------|--------|----------|
| 01 | [ACCOUNT](modules/01_ACCOUNT.md) | 16 | Пользователи, компании, аутентификация |
| 02 | [SERVICE](modules/02_SERVICE.md) | 34 | Услуги, заявки, формы, экспертиза |
| 03 | [CORE](modules/03_CORE.md) | 27 | События, вакансии, блоги, статьи |
| 04 | [BOOKING](modules/04_BOOKING.md) | 3 | Бронирование переговорок |
| 05 | [TECHORDA](modules/05_TECHORDA.md) | 7 | Образовательные программы TechOrda |
| 06 | [LANDING](modules/06_LANDING.md) | 5 | Лендинговые страницы |
| 07 | [COMMUNITY](modules/07_COMMUNITY.md) | 2 | Сообщества |
| 08 | [MATCHMAKING](modules/08_MATCHMAKING.md) | 2 | Подбор партнёров |
| 09 | [NIOKR](modules/09_NIOKR.md) | 5 | Научно-исследовательские проекты |
| 10 | [SHARED](modules/10_SHARED.md) | 6 | Общие компоненты |

### Технические модули

| # | Модуль | Таблиц | Описание |
|---|--------|--------|----------|
| 11 | [AUTH](modules/11_AUTH.md) | 3 | Django-аутентификация |
| 12 | [AUTHTOKEN](modules/12_AUTHTOKEN.md) | 1 | Токены API |
| 14 | [DJANGO](modules/14_DJANGO.md) | 5 | Системные таблицы Django |
| 15 | [REVERSION](modules/15_REVERSION.md) | 2 | Версионирование |
| 16 | [SEARCH](modules/16_SEARCH.md) | 1 | Поисковые индексы |
| 17 | [JOURNEYMAP](modules/17_JOURNEYMAP.md) | 7 | Карты пользователя |
| 18 | [EXPLORER](modules/18_EXPLORER.md) | 3 | SQL Explorer |
| 19 | [ADMIN](modules/19_ADMIN.md) | 1 | Журнал действий админки |
| 20 | [HUB](modules/20_HUB.md) | 1 | Настройки хаба |
| 21 | [ASTANAHUB](modules/21_ASTANAHUB.md) | 3 | Специфичные для Астана Хаб |
| 22 | [SILK](modules/22_SILK.md) | 5 | Профилирование запросов |
| 23 | [SOCIAL](modules/23_SOCIAL.md) | 5 | Социальная авторизация |
| 24 | [THUMBNAIL](modules/24_THUMBNAIL.md) | 1 | Превью изображений |
| 25 | [USER](modules/25_USER.md) | 1 | Расширение пользователя |
| 26 | [WAFFLE](modules/26_WAFFLE.md) | 5 | Feature flags |
| 27 | [AWSDJANGOSES](modules/27_AWSDJANGOSES.md) | 1 | AWS SES bounce |

---

## Быстрый старт

### Ключевые таблицы

| Сущность | Таблица | Записей |
|----------|---------|---------|
| Пользователи | `account_user` | 54,063 |
| Компании | `account_company` | 6,639 |
| Связь User-Company | `account_usercompany` | 4,536 |
| Услуги | `service_service` | 310 |
| Заявки | `service_servicerequest` | 56,000+ |
| События | `core_event` | 1,400+ |
| Вакансии | `core_vacancy` | 1,200+ |
| Бронирования | `booking_booking` | 8,600+ |

### Основные связи

```
USER ←→ COMPANY (через account_usercompany)
  │
  ├── создаёт → EVENT, VACANCY, BLOG
  └── подаёт  → SERVICE_REQUEST

COMPANY
  ├── организует → EVENT
  ├── размещает  → VACANCY
  └── подаёт     → SERVICE_REQUEST
```

### Мультиязычные поля

Текстовые поля хранятся как JSONB с ключами `ru`, `kk`, `en`:

```sql
-- Извлечение русского текста
SELECT title->>'ru' FROM core_event;

-- С fallback
SELECT COALESCE(title->>'ru', title->>'kk', title->>'en') FROM core_event;
```

---

## Просмотр диаграмм

ER-диаграммы в формате **Mermaid**. Для просмотра:

- **GitHub/GitLab** — рендерит автоматически
- **VS Code** — расширение "Markdown Preview Mermaid Support"
- **Онлайн** — https://mermaid.live
- **Confluence/Notion** — поддерживают Mermaid

---

## Контакты

При возникновении вопросов обращайтесь к команде разработки.

---

**Версия:** 1.0
**Дата:** 2025-12-07
