# TechHub Database Documentation

Документация базы данных платформы TechHub (Astana Hub) - технопарка для IT-компаний и стартапов Казахстана.

## Статистика базы данных

- **Таблиц:** 157
- **FK связей:** 218
- **Модулей Django:** 27
- **Размер БД:** ~5.12 GB

## Структура документации

### Основные документы системного аналитика

| Файл | Описание |
|------|----------|
| [SA_FULL_DATA_DICTIONARY.md](SA_FULL_DATA_DICTIONARY.md) | Полный словарь данных (все 157 таблиц) |
| [SA_FULL_ENTITY_ANALYSIS.md](SA_FULL_ENTITY_ANALYSIS.md) | Полный анализ сущностей + ER-диаграммы |
| [SA_BUSINESS_PROCESSES.md](SA_BUSINESS_PROCESSES.md) | Бизнес-процессы (BPMN, Use Cases) |
| [SA_ENTITY_RELATIONSHIP.md](SA_ENTITY_RELATIONSHIP.md) | Матрица связей между сущностями |
| [SA_DATA_DICTIONARY.md](SA_DATA_DICTIONARY.md) | Словарь данных (ключевые сущности) |

### Дополнительные документы

| Файл | Описание |
|------|----------|
| [DATABASE_SCHEMA.md](DATABASE_SCHEMA.md) | Общая схема базы данных |
| [TECHHUB_FULL_DOCUMENTATION.md](TECHHUB_FULL_DOCUMENTATION.md) | Полная документация с бизнес-логикой |
| [ER_DIAGRAM.puml](ER_DIAGRAM.puml) | ER-диаграмма (PlantUML) |
| [ER_DIAGRAM.html](ER_DIAGRAM.html) | Интерактивная ER-диаграмма (Mermaid) |

### Документация Data Lake

| Файл | Описание |
|------|----------|
| [DATALAKE_SPECIFICATION.md](DATALAKE_SPECIFICATION.md) | Спецификация для Data Lake |
| [DATA_FLOWS.md](DATA_FLOWS.md) | Потоки данных |

## Основные модули системы

1. **account** - Пользователи и компании
2. **service** - Государственные услуги и заявки
3. **core** - Контент (события, вакансии, блоги)
4. **booking** - Бронирование помещений
5. **techorda** - Образовательные программы
6. **landing** - CMS для страниц

## Ключевые сущности

- `account_user` - 54,063 пользователей
- `account_company` - 6,639 компаний
- `service_servicerequest` - 56,322 заявок на услуги
- `core_event` - 1,459 мероприятий
- `core_vacancy` - 1,205 вакансий

## Технологический стек

- **Backend:** Django (Python)
- **Database:** PostgreSQL
- **Multilingual:** JSONB поля (ru, kk, en)

---

*Документация сгенерирована автоматически на основе анализа структуры базы данных.*
