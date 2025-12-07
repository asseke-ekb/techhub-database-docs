# Контракты данных для интеграций

## 1. Пользователь (User)

### Структура данных

```json
{
  "id": 12345,
  "email": "user@example.com",
  "phone": "+77001234567",
  "first_name": "Иван",
  "last_name": "Иванов",
  "iin": "123456789012",
  "role": "user",
  "is_active": true,
  "blocked": false,
  "email_verified": true,
  "phone_verified": true,
  "created_at": "2024-01-15T10:30:00Z",
  "last_login": "2024-12-07T09:00:00Z",
  "company_id": 6789,
  "tags": {
    "tag_it_specialist": {"status": "active", "date_from": "2024-01-15"},
    "tag_investor": null
  }
}
```

### Описание полей

| Поле | Тип | Обязательное | Описание |
|------|-----|--------------|----------|
| id | integer | Да | Уникальный идентификатор |
| email | string | Нет | Email (может быть null при регистрации по телефону) |
| phone | string | Да | Телефон в формате +7XXXXXXXXXX |
| first_name | string | Да | Имя |
| last_name | string | Да | Фамилия |
| iin | string(12) | Нет | ИИН (индивидуальный идентификационный номер) |
| role | string | Да | Системная роль (см. справочник) |
| is_active | boolean | Да | Активен ли аккаунт |
| blocked | boolean | Да | Заблокирован ли администратором |
| email_verified | boolean | Да | Подтверждён ли email |
| phone_verified | boolean | Да | Подтверждён ли телефон |
| created_at | datetime | Да | Дата регистрации (ISO 8601) |
| last_login | datetime | Нет | Последний вход |
| company_id | integer | Нет | ID основной компании |
| tags | object | Нет | Теги пользователя |

### Возможные роли (role)

| Значение | Описание |
|----------|----------|
| `user` | Обычный пользователь |
| `admin` | Администратор |
| `superadmin` | Суперадминистратор |
| `moderator` | Модератор контента |
| `expert` | Эксперт для оценки заявок |
| `manager` | Менеджер услуг |

---

## 2. Компания (Company)

### Структура данных

```json
{
  "id": 6789,
  "name": "ТОО \"Компания\"",
  "short_name": "Компания",
  "tin": "123456789012",
  "company_type": "law",
  "status": "active",
  "verified": true,
  "address": "г. Астана, ул. Примерная, 1",
  "email": "info@company.kz",
  "phone": "+77172123456",
  "website": "https://company.kz",
  "created_at": "2024-01-10T12:00:00Z",
  "author_id": 12345,
  "tags": {
    "tag_it_company": {
      "status": "active",
      "date_from": "2024-02-01",
      "date_to": null,
      "data": {"certificate_number": "IT-2024-001"}
    },
    "tag_startup": {
      "status": "active",
      "date_from": "2024-03-15",
      "date_to": null
    },
    "tag_techpark": null
  },
  "bank_details": {
    "bank": "Kaspi Bank",
    "iik": "KZ123456789012345678",
    "bik": "CASPKZKA"
  }
}
```

### Описание полей

| Поле | Тип | Обязательное | Описание |
|------|-----|--------------|----------|
| id | integer | Да | Уникальный идентификатор |
| name | string | Да | Полное наименование |
| short_name | string | Нет | Краткое наименование |
| tin | string(12) | Нет | БИН/ИИН компании |
| company_type | string | Да | Тип компании |
| status | string | Да | Статус в системе |
| verified | boolean | Да | Прошла ли верификацию |
| address | string | Нет | Юридический адрес |
| email | string | Нет | Контактный email |
| phone | string | Нет | Контактный телефон |
| website | string | Нет | Сайт компании |
| created_at | datetime | Да | Дата регистрации |
| author_id | integer | Да | ID создателя |
| tags | object | Нет | Теги-статусы компании |
| bank_details | object | Нет | Банковские реквизиты |

### Типы компаний (company_type)

| Значение | Описание |
|----------|----------|
| `law` | Юридическое лицо (ТОО, АО) |
| `ip` | Индивидуальный предприниматель |
| `unknown` | Не определено |

### Статусы компании (status)

| Значение | Описание |
|----------|----------|
| `active` | Активна |
| `blocked` | Заблокирована |

### Теги компании

| Тег | Описание |
|-----|----------|
| `tag_it_company` | Аккредитованная IT-компания |
| `tag_startup` | В реестре стартапов |
| `tag_techpark` | Резидент технопарка |
| `tag_corp_partner` | Корпоративный партнёр |
| `tag_nii` | НИИ |
| `tag_nedrouser` | Недропользователь |

---

## 3. Заявка на услугу (ServiceRequest)

### Структура данных

```json
{
  "id": 56322,
  "service_id": 1,
  "service_code": "accreditation",
  "author_id": 12345,
  "company_id": 6789,
  "status": "success",
  "created_at": "2024-01-20T14:30:00Z",
  "updated_at": "2024-02-01T10:00:00Z",
  "data": {
    "additional_info": "..."
  }
}
```

### Описание полей

| Поле | Тип | Обязательное | Описание |
|------|-----|--------------|----------|
| id | integer | Да | Уникальный идентификатор |
| service_id | integer | Да | ID услуги |
| service_code | string | Да | Код услуги |
| author_id | integer | Да | ID заявителя |
| company_id | integer | Нет | ID компании (если применимо) |
| status | string | Да | Статус заявки |
| created_at | datetime | Да | Дата подачи |
| updated_at | datetime | Да | Дата последнего изменения |
| data | object | Нет | Дополнительные данные |

### Статусы заявки (status)

| Значение | Описание |
|----------|----------|
| `draft` | Черновик |
| `sent` | На рассмотрении |
| `correction` | На доработке |
| `approved` | Предварительно одобрена |
| `success` | Успешно завершена |
| `reject` | Отклонена |

### Коды услуг (service_code)

| Код | Название |
|-----|----------|
| `accreditation` | Аккредитация IT-компании |
| `startup_register` | Реестр стартапов |
| `techpark_register` | Резидентство технопарка |
| `seedmoney` | Грант Seed Money |
| `techorda_request` | Заявка на TechOrda |
| `visa_support` | Визовая поддержка |

---

## 4. Событие (Event)

### Структура данных

```json
{
  "id": 1459,
  "title": {
    "ru": "IT-конференция 2024",
    "kk": "IT-конференция 2024",
    "en": "IT Conference 2024"
  },
  "content": {
    "ru": "Описание мероприятия...",
    "kk": "Іс-шара сипаттамасы...",
    "en": "Event description..."
  },
  "event_type": "open_event",
  "event_format": "hybrid",
  "status": "success",
  "start_date": "2024-12-15T10:00:00Z",
  "end_date": "2024-12-15T18:00:00Z",
  "author_id": 12345,
  "company_id": 6789,
  "created_at": "2024-11-01T09:00:00Z"
}
```

### Типы событий (event_type)

| Значение | Описание |
|----------|----------|
| `open_event` | Открытое для всех |
| `closed_event` | Закрытое (по приглашениям) |

### Форматы событий (event_format)

| Значение | Описание |
|----------|----------|
| `astanahub` | Офлайн (в Astana Hub) |
| `online` | Онлайн |
| `hybrid` | Гибрид |

---

## 5. Вакансия (Vacancy)

### Структура данных

```json
{
  "id": 1205,
  "title": {
    "ru": "Backend-разработчик",
    "kk": "Backend-әзірлеуші",
    "en": "Backend Developer"
  },
  "content": {
    "ru": "Описание вакансии...",
    "kk": "Бос орын сипаттамасы...",
    "en": "Job description..."
  },
  "vacancy_type": "fulltime",
  "status": "success",
  "salary_from": 500000,
  "salary_to": 800000,
  "company_id": 6789,
  "author_id": 12345,
  "created_at": "2024-11-15T12:00:00Z"
}
```

### Типы вакансий (vacancy_type)

| Значение | Описание |
|----------|----------|
| `fulltime` | Полная занятость |
| `parttime` | Частичная занятость |
| `internship` | Стажировка |
| `project` | Проектная работа |
| `volunteering` | Волонтёрство |

---

## 6. Членство в компании (UserCompany)

### Структура данных

```json
{
  "id": 4536,
  "user_id": 12345,
  "company_id": 6789,
  "role": "owner",
  "verified": true
}
```

### Роли в компании (role)

| Значение | Описание |
|----------|----------|
| `owner` | Владелец (только один на компанию) |
| `member` | Сотрудник |
| `advisor` | Консультант |

---

## Форматы дат

Все даты в формате **ISO 8601**:
- `2024-12-07T10:30:00Z` — дата и время в UTC
- `2024-12-07` — только дата

---

## Пагинация (для списков)

```json
{
  "count": 54063,
  "next": "?page=2",
  "previous": null,
  "results": [...]
}
```

| Поле | Описание |
|------|----------|
| count | Общее количество записей |
| next | URL следующей страницы |
| previous | URL предыдущей страницы |
| results | Массив данных |
