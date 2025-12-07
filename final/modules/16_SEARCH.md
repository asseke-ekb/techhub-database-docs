# Модуль SEARCH

**Описание:** Поисковые запросы

**Таблиц в модуле:** 1

---

| Таблица | Записей | Описание |
|---------|---------|----------|
| `search_search` | 7,607 | - |

### search_search

**Количество записей:** 7,607

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('search_search_id_seq'::regclass... | Уникальный идентификатор |
| 2 | `created_at` | timestamp with time zone | Нет | - | Дата и время создания |
| 3 | `updated_at` | timestamp with time zone | Нет | - | Дата и время обновления |
| 4 | `source` | character varying(30) | Нет | - |  |
| 5 | `primary_key` | character varying(200) | Нет | - |  |
| 6 | `path` | character varying(1000) | Нет | - |  |
| 7 | `title_en` | text | Нет | - |  |
| 8 | `title_kk` | text | Нет | - |  |
| 9 | `title_ru` | text | Нет | - |  |
| 10 | `published` | boolean | Нет | - | Признак публикации |
| 11 | `author` | text | Нет | - |  |
| 12 | `content_en` | text | Нет | - |  |
| 13 | `content_kk` | text | Нет | - |  |
| 14 | `content_ru` | text | Нет | - |  |
| 15 | `search_vector_en` | tsvector | Да | - |  |
| 16 | `search_vector_kk` | tsvector | Да | - |  |
| 17 | `search_vector_ru` | tsvector | Да | - |  |

---