import psycopg2
import json

conn = psycopg2.connect(
    dbname='techhub',
    user='dgabbassov',
    password='sVLKLeM5D%',
    host='188.130.234.92',
    port='50693'
)

cur = conn.cursor()

# 1. Получаем уникальные значения для полей типа status, type, role
print("=== ENUM VALUES (statuses, types, roles) ===\n")

enum_queries = [
    ("account_user.role", "SELECT DISTINCT role FROM account_user WHERE role IS NOT NULL AND role != '' ORDER BY role"),
    ("account_company.company_type", "SELECT DISTINCT company_type FROM account_company WHERE company_type IS NOT NULL ORDER BY company_type"),
    ("account_company.status", "SELECT DISTINCT status FROM account_company WHERE status IS NOT NULL ORDER BY status"),
    ("account_usercompany.role", "SELECT DISTINCT role FROM account_usercompany WHERE role IS NOT NULL ORDER BY role"),
    ("booking_booking.status", "SELECT DISTINCT status FROM booking_booking ORDER BY status"),
    ("core_article.status", "SELECT DISTINCT status FROM core_article ORDER BY status"),
    ("core_blog.status", "SELECT DISTINCT status FROM core_blog ORDER BY status"),
    ("core_event.status", "SELECT DISTINCT status FROM core_event ORDER BY status"),
    ("core_event.event_type", "SELECT DISTINCT event_type FROM core_event WHERE event_type IS NOT NULL ORDER BY event_type"),
    ("core_event.event_format", "SELECT DISTINCT event_format FROM core_event WHERE event_format IS NOT NULL ORDER BY event_format"),
    ("core_vacancy.status", "SELECT DISTINCT status FROM core_vacancy ORDER BY status"),
    ("core_vacancy.vacancy_type", "SELECT DISTINCT vacancy_type FROM core_vacancy WHERE vacancy_type IS NOT NULL ORDER BY vacancy_type"),
    ("core_techtask.status", "SELECT DISTINCT status FROM core_techtask ORDER BY status"),
    ("core_discussion.status", "SELECT DISTINCT status FROM core_discussion ORDER BY status"),
    ("core_comment.status", "SELECT DISTINCT status FROM core_comment ORDER BY status"),
    ("core_infrastructure.status", "SELECT DISTINCT status FROM core_infrastructure ORDER BY status"),
    ("core_infrastructure.type", "SELECT DISTINCT type FROM core_infrastructure WHERE type IS NOT NULL ORDER BY type"),
    ("service_service.code", "SELECT code, (data->>'name')::text as name FROM service_service ORDER BY code LIMIT 30"),
    ("service_servicerequest.status", "SELECT DISTINCT status FROM service_servicerequest WHERE status IS NOT NULL ORDER BY status"),
    ("core_organization.code", "SELECT code, (name->>'ru')::text as name FROM core_organization ORDER BY code"),
]

for name, query in enum_queries:
    try:
        cur.execute(query)
        results = cur.fetchall()
        values = [str(r[0]) if len(r) == 1 else f"{r[0]}: {r[1]}" for r in results]
        print(f"{name}:")
        for v in values[:20]:
            print(f"  - {v}")
        if len(values) > 20:
            print(f"  ... и ещё {len(values) - 20}")
        print()
    except Exception as e:
        print(f"{name}: ERROR - {e}\n")
        conn.rollback()

# 2. Примеры данных из ключевых таблиц
print("\n=== SAMPLE DATA ===\n")

samples = [
    ("account_user (5 примеров)", """
        SELECT id, email, first_name, last_name, role, is_active, created_at::date
        FROM account_user
        WHERE email IS NOT NULL AND email != ''
        ORDER BY id DESC LIMIT 5
    """),
    ("account_company (5 примеров)", """
        SELECT id, name, tin, company_type, status, verified, created_at::date
        FROM account_company
        ORDER BY id DESC LIMIT 5
    """),
    ("core_event (5 примеров)", """
        SELECT id, (title->>'ru')::varchar(50), status, event_type, datetime_start::date
        FROM core_event
        ORDER BY id DESC LIMIT 5
    """),
    ("service_servicerequest (5 примеров)", """
        SELECT id, service_id, status, created_at::date, company_id
        FROM service_servicerequest
        ORDER BY id DESC LIMIT 5
    """),
    ("core_vacancy (5 примеров)", """
        SELECT id, (title->>'ru')::varchar(50), status, vacancy_type, salary_min, salary_max
        FROM core_vacancy
        ORDER BY id DESC LIMIT 5
    """),
]

for name, query in samples:
    try:
        cur.execute(query)
        results = cur.fetchall()
        print(f"{name}:")
        for r in results:
            print(f"  {r}")
        print()
    except Exception as e:
        print(f"{name}: ERROR - {e}\n")
        conn.rollback()

# 3. Статистика по модулям
print("\n=== MODULE STATISTICS ===\n")

stats = [
    ("Пользователи", "SELECT COUNT(*) FROM account_user"),
    ("Активные пользователи", "SELECT COUNT(*) FROM account_user WHERE is_active = true"),
    ("Компании", "SELECT COUNT(*) FROM account_company"),
    ("Верифицированные компании", "SELECT COUNT(*) FROM account_company WHERE verified = true"),
    ("События", "SELECT COUNT(*) FROM core_event"),
    ("Опубликованные события", "SELECT COUNT(*) FROM core_event WHERE published = true"),
    ("Вакансии", "SELECT COUNT(*) FROM core_vacancy"),
    ("Заявки на сервисы", "SELECT COUNT(*) FROM service_servicerequest"),
    ("Сервисы (услуги)", "SELECT COUNT(*) FROM service_service"),
    ("Блоги", "SELECT COUNT(*) FROM core_blog"),
    ("Бронирования", "SELECT COUNT(*) FROM booking_booking"),
    ("Комментарии", "SELECT COUNT(*) FROM core_comment"),
    ("Технические задания", "SELECT COUNT(*) FROM core_techtask"),
]

for name, query in stats:
    cur.execute(query)
    count = cur.fetchone()[0]
    print(f"{name}: {count:,}")

cur.close()
conn.close()
