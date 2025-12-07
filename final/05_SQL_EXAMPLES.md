# TechHub - SQL-запросы для аналитиков

## 1. Пользователи

### 1.1. Общая статистика

```sql
-- Количество пользователей
SELECT COUNT(*) as total_users FROM account_user;

-- Активные пользователи
SELECT COUNT(*) as active_users
FROM account_user
WHERE is_active = true AND blocked = false;

-- Пользователи по ролям
SELECT
    role,
    COUNT(*) as count
FROM account_user
WHERE is_active = true
GROUP BY role
ORDER BY count DESC;
```

### 1.2. Регистрации по периодам

```sql
-- По месяцам
SELECT
    DATE_TRUNC('month', created_at) as month,
    COUNT(*) as registrations
FROM account_user
GROUP BY DATE_TRUNC('month', created_at)
ORDER BY month DESC;

-- По дням за последний месяц
SELECT
    DATE(created_at) as day,
    COUNT(*) as registrations
FROM account_user
WHERE created_at >= CURRENT_DATE - INTERVAL '30 days'
GROUP BY DATE(created_at)
ORDER BY day DESC;

-- По годам
SELECT
    EXTRACT(YEAR FROM created_at) as year,
    COUNT(*) as registrations
FROM account_user
GROUP BY EXTRACT(YEAR FROM created_at)
ORDER BY year DESC;
```

### 1.3. Верификация

```sql
-- Статистика верификации
SELECT
    email_verified,
    phone_verified,
    COUNT(*) as count
FROM account_user
WHERE is_active = true
GROUP BY email_verified, phone_verified;
```

---

## 2. Компании

### 2.1. Общая статистика

```sql
-- Всего компаний
SELECT COUNT(*) as total_companies FROM account_company;

-- По типам
SELECT
    company_type,
    COUNT(*) as count
FROM account_company
GROUP BY company_type
ORDER BY count DESC;

-- По статусам
SELECT
    status,
    verified,
    COUNT(*) as count
FROM account_company
GROUP BY status, verified
ORDER BY count DESC;
```

### 2.2. Стартапы

```sql
-- Активные стартапы
SELECT
    id,
    name,
    tin,
    tag_startup->>'date_from' as startup_since,
    created_at
FROM account_company
WHERE tag_startup->>'status' = 'active'
ORDER BY created_at DESC;

-- Количество стартапов по годам
SELECT
    EXTRACT(YEAR FROM (tag_startup->>'date_from')::date) as year,
    COUNT(*) as count
FROM account_company
WHERE tag_startup->>'status' = 'active'
  AND tag_startup->>'date_from' IS NOT NULL
GROUP BY EXTRACT(YEAR FROM (tag_startup->>'date_from')::date)
ORDER BY year DESC;
```

### 2.3. IT-компании (аккредитованные)

```sql
-- Аккредитованные IT-компании
SELECT
    id,
    name,
    tin,
    tag_it_company->>'date_from' as accredited_since,
    created_at
FROM account_company
WHERE tag_it_company->>'status' = 'active'
ORDER BY created_at DESC;

-- Количество по типу компании
SELECT
    company_type,
    COUNT(*) as count
FROM account_company
WHERE tag_it_company->>'status' = 'active'
GROUP BY company_type;
```

### 2.4. Резиденты технопарка

```sql
-- Резиденты
SELECT
    id,
    name,
    tin,
    tag_techpark->>'date_from' as resident_since
FROM account_company
WHERE tag_techpark->>'status' = 'active'
ORDER BY (tag_techpark->>'date_from')::date DESC;
```

### 2.5. Компании с несколькими тегами

```sql
-- Компании, которые одновременно стартап И IT-компания
SELECT
    id,
    name,
    tin
FROM account_company
WHERE tag_startup->>'status' = 'active'
  AND tag_it_company->>'status' = 'active';

-- Полная матрица тегов
SELECT
    CASE WHEN tag_startup->>'status' = 'active' THEN 'Да' ELSE 'Нет' END as startup,
    CASE WHEN tag_it_company->>'status' = 'active' THEN 'Да' ELSE 'Нет' END as it_company,
    CASE WHEN tag_techpark->>'status' = 'active' THEN 'Да' ELSE 'Нет' END as techpark,
    COUNT(*) as count
FROM account_company
WHERE status = 'active'
GROUP BY
    tag_startup->>'status',
    tag_it_company->>'status',
    tag_techpark->>'status'
ORDER BY count DESC;
```

---

## 3. Связь пользователей и компаний

```sql
-- Сколько пользователей в компаниях
SELECT
    uc.role,
    COUNT(*) as count
FROM account_usercompany uc
GROUP BY uc.role;

-- Топ-10 компаний по количеству сотрудников
SELECT
    c.id,
    c.name,
    COUNT(uc.id) as employees
FROM account_company c
JOIN account_usercompany uc ON uc.company_id = c.id
WHERE uc.verified = true
GROUP BY c.id, c.name
ORDER BY employees DESC
LIMIT 10;

-- Пользователи, связанные с несколькими компаниями
SELECT
    u.id,
    u.email,
    u.first_name,
    u.last_name,
    COUNT(uc.company_id) as companies_count
FROM account_user u
JOIN account_usercompany uc ON uc.user_id = u.id
GROUP BY u.id, u.email, u.first_name, u.last_name
HAVING COUNT(uc.company_id) > 1
ORDER BY companies_count DESC;
```

---

## 4. Заявки на услуги

### 4.1. Общая статистика

```sql
-- Всего заявок
SELECT COUNT(*) as total_requests FROM service_servicerequest;

-- По статусам
SELECT
    status,
    COUNT(*) as count
FROM service_servicerequest
GROUP BY status
ORDER BY count DESC;

-- По услугам
SELECT
    s.code,
    s.data->>'name' as service_name,
    COUNT(sr.id) as requests_count
FROM service_service s
LEFT JOIN service_servicerequest sr ON sr.service_id = s.id
GROUP BY s.id, s.code, s.data
ORDER BY requests_count DESC;
```

### 4.2. Воронка заявок

```sql
-- Конверсия по статусам
SELECT
    s.code as service_code,
    COUNT(*) as total,
    COUNT(*) FILTER (WHERE sr.status = 'draft') as draft,
    COUNT(*) FILTER (WHERE sr.status = 'sent') as sent,
    COUNT(*) FILTER (WHERE sr.status = 'approved') as approved,
    COUNT(*) FILTER (WHERE sr.status = 'success') as success,
    COUNT(*) FILTER (WHERE sr.status IN ('reject', 'rejected')) as rejected,
    ROUND(
        100.0 * COUNT(*) FILTER (WHERE sr.status = 'success') / NULLIF(COUNT(*), 0),
        1
    ) as success_rate
FROM service_servicerequest sr
JOIN service_service s ON s.id = sr.service_id
GROUP BY s.code
ORDER BY total DESC;
```

### 4.3. Заявки по периодам

```sql
-- По месяцам
SELECT
    DATE_TRUNC('month', created_at) as month,
    COUNT(*) as requests
FROM service_servicerequest
GROUP BY DATE_TRUNC('month', created_at)
ORDER BY month DESC;

-- По услугам за последний год
SELECT
    s.code,
    DATE_TRUNC('month', sr.created_at) as month,
    COUNT(*) as requests
FROM service_servicerequest sr
JOIN service_service s ON s.id = sr.service_id
WHERE sr.created_at >= CURRENT_DATE - INTERVAL '1 year'
GROUP BY s.code, DATE_TRUNC('month', sr.created_at)
ORDER BY s.code, month;
```

### 4.4. Среднее время обработки

```sql
-- Среднее время от создания до успеха (в днях)
SELECT
    s.code,
    ROUND(AVG(EXTRACT(EPOCH FROM (sr.updated_at - sr.created_at)) / 86400), 1) as avg_days
FROM service_servicerequest sr
JOIN service_service s ON s.id = sr.service_id
WHERE sr.status = 'success'
GROUP BY s.code
ORDER BY avg_days;
```

---

## 5. События

### 5.1. Статистика событий

```sql
-- Всего событий
SELECT
    status,
    COUNT(*) as count
FROM core_event
GROUP BY status;

-- По форматам
SELECT
    event_format,
    COUNT(*) as count
FROM core_event
WHERE status = 'success'
GROUP BY event_format;

-- По типам
SELECT
    event_type,
    COUNT(*) as count
FROM core_event
WHERE status = 'success'
GROUP BY event_type;
```

### 5.2. Календарь событий

```sql
-- Предстоящие события
SELECT
    id,
    title->>'ru' as title,
    event_format,
    datetime_start,
    datetime_end
FROM core_event
WHERE status = 'success'
  AND published = true
  AND datetime_start >= CURRENT_TIMESTAMP
ORDER BY datetime_start
LIMIT 20;

-- События за период
SELECT
    id,
    title->>'ru' as title,
    event_type,
    event_format,
    datetime_start,
    view_count
FROM core_event
WHERE datetime_start BETWEEN '2024-01-01' AND '2024-12-31'
  AND status = 'success'
ORDER BY datetime_start;

-- Количество событий по месяцам
SELECT
    DATE_TRUNC('month', datetime_start) as month,
    COUNT(*) as events
FROM core_event
WHERE status = 'success'
  AND datetime_start IS NOT NULL
GROUP BY DATE_TRUNC('month', datetime_start)
ORDER BY month DESC;
```

### 5.3. Топ событий по просмотрам

```sql
SELECT
    id,
    title->>'ru' as title,
    event_format,
    datetime_start,
    view_count
FROM core_event
WHERE status = 'success'
ORDER BY view_count DESC
LIMIT 10;
```

---

## 6. Вакансии

### 6.1. Статистика вакансий

```sql
-- По статусам
SELECT
    status,
    COUNT(*) as count
FROM core_vacancy
GROUP BY status;

-- По типам занятости
SELECT
    vacancy_type,
    COUNT(*) as count
FROM core_vacancy
WHERE status = 'success'
GROUP BY vacancy_type
ORDER BY count DESC;

-- Активные вакансии
SELECT
    v.id,
    v.title->>'ru' as title,
    c.name as company,
    v.vacancy_type,
    v.salary_min,
    v.salary_max,
    v.created_at
FROM core_vacancy v
JOIN account_company c ON c.id = v.company_id
WHERE v.status = 'success'
  AND v.published = true
ORDER BY v.created_at DESC
LIMIT 20;
```

### 6.2. Анализ зарплат

```sql
-- Средние зарплаты по типам
SELECT
    vacancy_type,
    COUNT(*) as vacancies,
    ROUND(AVG(salary_min)) as avg_min,
    ROUND(AVG(salary_max)) as avg_max,
    MIN(salary_min) as min_salary,
    MAX(salary_max) as max_salary
FROM core_vacancy
WHERE status = 'success'
  AND salary_min IS NOT NULL
  AND salary_max IS NOT NULL
GROUP BY vacancy_type
ORDER BY avg_max DESC;

-- Распределение зарплат
SELECT
    CASE
        WHEN salary_max < 300000 THEN '< 300K'
        WHEN salary_max < 500000 THEN '300K-500K'
        WHEN salary_max < 1000000 THEN '500K-1M'
        WHEN salary_max < 2000000 THEN '1M-2M'
        ELSE '> 2M'
    END as salary_range,
    COUNT(*) as count
FROM core_vacancy
WHERE status = 'success' AND salary_max IS NOT NULL
GROUP BY 1
ORDER BY
    CASE
        WHEN salary_max < 300000 THEN 1
        WHEN salary_max < 500000 THEN 2
        WHEN salary_max < 1000000 THEN 3
        WHEN salary_max < 2000000 THEN 4
        ELSE 5
    END;
```

### 6.3. Топ работодателей

```sql
-- Компании с наибольшим количеством вакансий
SELECT
    c.id,
    c.name,
    COUNT(v.id) as vacancies_count
FROM account_company c
JOIN core_vacancy v ON v.company_id = c.id
WHERE v.status = 'success'
GROUP BY c.id, c.name
ORDER BY vacancies_count DESC
LIMIT 10;
```

---

## 7. Бронирования

### 7.1. Статистика

```sql
-- По статусам
SELECT
    status,
    COUNT(*) as count
FROM booking_booking
GROUP BY status;

-- По комнатам
SELECT
    r.name as room,
    r.floor,
    r.max_people,
    COUNT(b.id) as bookings
FROM booking_room r
LEFT JOIN booking_booking b ON b.room_id = r.id
GROUP BY r.id, r.name, r.floor, r.max_people
ORDER BY bookings DESC;
```

### 7.2. Загруженность

```sql
-- Бронирования по дням недели
SELECT
    EXTRACT(DOW FROM start) as day_of_week,
    CASE EXTRACT(DOW FROM start)
        WHEN 0 THEN 'Воскресенье'
        WHEN 1 THEN 'Понедельник'
        WHEN 2 THEN 'Вторник'
        WHEN 3 THEN 'Среда'
        WHEN 4 THEN 'Четверг'
        WHEN 5 THEN 'Пятница'
        WHEN 6 THEN 'Суббота'
    END as day_name,
    COUNT(*) as bookings
FROM booking_booking
WHERE status = 'active' OR status = 'finished'
GROUP BY EXTRACT(DOW FROM start)
ORDER BY day_of_week;

-- Бронирования по часам
SELECT
    EXTRACT(HOUR FROM start) as hour,
    COUNT(*) as bookings
FROM booking_booking
WHERE status IN ('active', 'finished')
GROUP BY EXTRACT(HOUR FROM start)
ORDER BY hour;

-- Средняя продолжительность бронирования (в минутах)
SELECT
    r.name as room,
    ROUND(AVG(EXTRACT(EPOCH FROM ("end" - start)) / 60)) as avg_duration_min
FROM booking_booking b
JOIN booking_room r ON r.id = b.room_id
WHERE b.status IN ('active', 'finished')
GROUP BY r.name
ORDER BY avg_duration_min DESC;
```

---

## 8. Работа с JSONB

### 8.1. Извлечение мультиязычных полей

```sql
-- Русский текст
SELECT title->>'ru' as title_ru FROM core_event;

-- С fallback (если нет русского - казахский, потом английский)
SELECT
    id,
    COALESCE(
        title->>'ru',
        title->>'kk',
        title->>'en'
    ) as title
FROM core_event;
```

### 8.2. Поиск по JSONB

```sql
-- Поиск по названию
SELECT * FROM core_event
WHERE title->>'ru' ILIKE '%конференция%';

-- Проверка наличия ключа
SELECT * FROM account_company
WHERE tag_startup ? 'status';

-- Фильтрация по значению внутри JSON
SELECT * FROM account_company
WHERE tag_startup->>'status' = 'active';
```

### 8.3. Агрегация JSONB

```sql
-- Подсчёт по значению внутри JSON
SELECT
    tag_startup->>'status' as startup_status,
    COUNT(*) as count
FROM account_company
WHERE tag_startup IS NOT NULL
  AND tag_startup != '{}'::jsonb
GROUP BY tag_startup->>'status';
```

---

## 9. Полезные запросы

### 9.1. Проверка "сирот" (orphaned records)

```sql
-- Заявки без компании (если company_id указан)
SELECT sr.id, sr.company_id
FROM service_servicerequest sr
LEFT JOIN account_company c ON c.id = sr.company_id
WHERE c.id IS NULL AND sr.company_id IS NOT NULL;

-- Вакансии от несуществующих компаний
SELECT v.id, v.company_id
FROM core_vacancy v
LEFT JOIN account_company c ON c.id = v.company_id
WHERE c.id IS NULL AND v.company_id IS NOT NULL;
```

### 9.2. Дубликаты

```sql
-- Компании с одинаковым БИН
SELECT tin, COUNT(*) as count
FROM account_company
WHERE tin IS NOT NULL AND tin != ''
GROUP BY tin
HAVING COUNT(*) > 1;

-- Пользователи с одинаковым email
SELECT email, COUNT(*) as count
FROM account_user
WHERE email IS NOT NULL AND email != ''
GROUP BY email
HAVING COUNT(*) > 1;
```

### 9.3. Временные зоны

```sql
-- Конвертация в локальное время Казахстана
SELECT
    id,
    created_at AT TIME ZONE 'Asia/Almaty' as local_time
FROM account_user
LIMIT 10;
```

---

## 10. Шаблоны отчётов

### 10.1. Ежемесячный отчёт

```sql
-- Сводка за месяц
WITH month_data AS (
    SELECT
        DATE_TRUNC('month', CURRENT_DATE - INTERVAL '1 month') as report_month
)
SELECT
    'Новые пользователи' as metric,
    COUNT(*)::text as value
FROM account_user, month_data
WHERE DATE_TRUNC('month', created_at) = report_month

UNION ALL

SELECT
    'Новые компании',
    COUNT(*)::text
FROM account_company, month_data
WHERE DATE_TRUNC('month', created_at) = report_month

UNION ALL

SELECT
    'Заявки на услуги',
    COUNT(*)::text
FROM service_servicerequest, month_data
WHERE DATE_TRUNC('month', created_at) = report_month

UNION ALL

SELECT
    'Одобренные заявки',
    COUNT(*)::text
FROM service_servicerequest, month_data
WHERE DATE_TRUNC('month', created_at) = report_month
  AND status = 'success'

UNION ALL

SELECT
    'События проведено',
    COUNT(*)::text
FROM core_event, month_data
WHERE DATE_TRUNC('month', datetime_start) = report_month
  AND status = 'success'

UNION ALL

SELECT
    'Вакансий опубликовано',
    COUNT(*)::text
FROM core_vacancy, month_data
WHERE DATE_TRUNC('month', created_at) = report_month
  AND status = 'success';
```

### 10.2. Сравнение периодов

```sql
-- Сравнение текущего и прошлого месяца
SELECT
    'Регистрации' as metric,
    COUNT(*) FILTER (
        WHERE created_at >= DATE_TRUNC('month', CURRENT_DATE)
    ) as current_month,
    COUNT(*) FILTER (
        WHERE created_at >= DATE_TRUNC('month', CURRENT_DATE - INTERVAL '1 month')
          AND created_at < DATE_TRUNC('month', CURRENT_DATE)
    ) as previous_month
FROM account_user

UNION ALL

SELECT
    'Заявки',
    COUNT(*) FILTER (
        WHERE created_at >= DATE_TRUNC('month', CURRENT_DATE)
    ),
    COUNT(*) FILTER (
        WHERE created_at >= DATE_TRUNC('month', CURRENT_DATE - INTERVAL '1 month')
          AND created_at < DATE_TRUNC('month', CURRENT_DATE)
    )
FROM service_servicerequest;
```

---

*Вернуться: [README.md](README.md)*
