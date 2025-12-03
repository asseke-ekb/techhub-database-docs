import psycopg2
import json
from collections import defaultdict

conn = psycopg2.connect(
    dbname='techhub',
    user='dgabbassov',
    password='sVLKLeM5D%',
    host='188.130.234.92',
    port='50693'
)

cur = conn.cursor()

print("=" * 80)
print("DATA LAKE ANALYSIS - TechHub Database")
print("=" * 80)

# 1. Анализ объёмов данных и скорости роста
print("\n\n### 1. VOLUME ANALYSIS (для планирования storage) ###\n")

volume_query = """
SELECT
    relname as table_name,
    pg_size_pretty(pg_total_relation_size(relid)) as total_size,
    pg_total_relation_size(relid) as size_bytes,
    n_live_tup as row_count
FROM pg_stat_user_tables
WHERE schemaname = 'public'
ORDER BY pg_total_relation_size(relid) DESC
LIMIT 30
"""
cur.execute(volume_query)
results = cur.fetchall()
print(f"{'Table':<45} {'Size':<15} {'Rows':<15}")
print("-" * 75)
total_bytes = 0
for r in results:
    print(f"{r[0]:<45} {r[1]:<15} {r[3]:<15,}")
    total_bytes += r[2]
print(f"\nTotal DB Size: {total_bytes / (1024**3):.2f} GB")


# 2. Анализ JSONB полей - что внутри
print("\n\n### 2. JSONB FIELDS STRUCTURE ###\n")

jsonb_tables = [
    ("account_user", "data", 5),
    ("account_user", "tags", 5),
    ("account_user", "permissions", 3),
    ("account_company", "tag_startup", 5),
    ("account_company", "tag_it_company", 5),
    ("account_company", "data", 3),
    ("account_company", "basic_info", 3),
    ("service_service", "data", 3),
    ("service_hubformdata", "data", 3),
    ("service_servicerequest", "data", 3),
    ("core_event", "title", 5),
    ("core_event", "content", 3),
    ("core_event", "contact_info", 5),
    ("core_blog", "title", 5),
    ("core_vacancy", "title", 5),
]

for table, field, limit in jsonb_tables:
    try:
        cur.execute(f"""
            SELECT {field}
            FROM {table}
            WHERE {field} IS NOT NULL AND {field}::text != '{{}}' AND {field}::text != 'null'
            LIMIT {limit}
        """)
        results = cur.fetchall()
        if results:
            print(f"\n--- {table}.{field} ---")
            for i, r in enumerate(results[:2]):
                data = r[0]
                if isinstance(data, dict):
                    keys = list(data.keys())[:10]
                    print(f"  Keys: {keys}")
                    # Показать пример значений
                    sample = {k: str(v)[:50] for k, v in list(data.items())[:5]}
                    print(f"  Sample: {sample}")
                    break
    except Exception as e:
        print(f"  {table}.{field}: ERROR - {e}")
        conn.rollback()


# 3. Временные паттерны - для инкрементальной загрузки
print("\n\n### 3. TEMPORAL PATTERNS (для CDC/инкрементальной загрузки) ###\n")

temporal_queries = [
    ("account_user", "created_at"),
    ("account_company", "created_at"),
    ("service_servicerequest", "created_at"),
    ("core_event", "created_at"),
    ("booking_booking", "created_at"),
    ("core_blog", "created_at"),
]

for table, date_field in temporal_queries:
    try:
        cur.execute(f"""
            SELECT
                DATE_TRUNC('month', {date_field}) as month,
                COUNT(*) as count
            FROM {table}
            WHERE {date_field} IS NOT NULL
            GROUP BY DATE_TRUNC('month', {date_field})
            ORDER BY month DESC
            LIMIT 12
        """)
        results = cur.fetchall()
        print(f"\n{table} (by {date_field}):")
        for r in results[:6]:
            if r[0]:
                print(f"  {r[0].strftime('%Y-%m')}: {r[1]:,} records")
    except Exception as e:
        print(f"  {table}: ERROR - {e}")
        conn.rollback()


# 4. Анализ NULL значений - Data Quality
print("\n\n### 4. DATA QUALITY - NULL Analysis ###\n")

quality_tables = [
    "account_user",
    "account_company",
    "service_servicerequest",
    "core_event",
    "core_vacancy",
]

for table in quality_tables:
    cur.execute(f"""
        SELECT column_name
        FROM information_schema.columns
        WHERE table_name = '{table}' AND table_schema = 'public'
    """)
    columns = [r[0] for r in cur.fetchall()]

    print(f"\n{table}:")
    cur.execute(f"SELECT COUNT(*) FROM {table}")
    total = cur.fetchone()[0]

    for col in columns[:15]:  # первые 15 колонок
        try:
            cur.execute(f"SELECT COUNT(*) FROM {table} WHERE {col} IS NULL OR {col}::text = ''")
            null_count = cur.fetchone()[0]
            if null_count > 0:
                pct = (null_count / total * 100) if total > 0 else 0
                if pct > 5:  # только если > 5% NULL
                    print(f"  {col}: {null_count:,} nulls ({pct:.1f}%)")
        except:
            conn.rollback()


# 5. Связи между сущностями - для построения графа
print("\n\n### 5. RELATIONSHIP CARDINALITY ###\n")

cardinality_queries = [
    ("Users per Company", """
        SELECT company_id, COUNT(*) as user_count
        FROM account_usercompany
        GROUP BY company_id
        ORDER BY user_count DESC
        LIMIT 10
    """),
    ("Requests per Service", """
        SELECT service_id, COUNT(*) as request_count
        FROM service_servicerequest
        GROUP BY service_id
        ORDER BY request_count DESC
        LIMIT 10
    """),
    ("Events per Company", """
        SELECT company_id, COUNT(*) as event_count
        FROM core_event
        WHERE company_id IS NOT NULL
        GROUP BY company_id
        ORDER BY event_count DESC
        LIMIT 10
    """),
    ("Vacancies per Company", """
        SELECT company_id, COUNT(*) as vacancy_count
        FROM core_vacancy
        WHERE company_id IS NOT NULL
        GROUP BY company_id
        ORDER BY vacancy_count DESC
        LIMIT 10
    """),
]

for name, query in cardinality_queries:
    try:
        cur.execute(query)
        results = cur.fetchall()
        print(f"\n{name}:")
        for r in results[:5]:
            print(f"  ID {r[0]}: {r[1]} items")
    except Exception as e:
        print(f"  ERROR: {e}")
        conn.rollback()


# 6. Индексы - важно для ETL
print("\n\n### 6. EXISTING INDEXES (для оптимизации ETL) ###\n")

cur.execute("""
    SELECT
        tablename,
        indexname,
        indexdef
    FROM pg_indexes
    WHERE schemaname = 'public'
    ORDER BY tablename
""")
results = cur.fetchall()

indexes_by_table = defaultdict(list)
for r in results:
    indexes_by_table[r[0]].append(r[1])

print("Tables with most indexes:")
for table, indexes in sorted(indexes_by_table.items(), key=lambda x: -len(x[1]))[:15]:
    print(f"  {table}: {len(indexes)} indexes")


# 7. Уникальные ключи кроме PK
print("\n\n### 7. UNIQUE CONSTRAINTS (natural keys для Data Lake) ###\n")

cur.execute("""
    SELECT
        tc.table_name,
        tc.constraint_name,
        kcu.column_name
    FROM information_schema.table_constraints tc
    JOIN information_schema.key_column_usage kcu
        ON tc.constraint_name = kcu.constraint_name
    WHERE tc.constraint_type = 'UNIQUE' AND tc.table_schema = 'public'
    ORDER BY tc.table_name
""")
results = cur.fetchall()
for r in results:
    print(f"  {r[0]}.{r[2]} (constraint: {r[1]})")


# 8. Sequences - для понимания ID генерации
print("\n\n### 8. SEQUENCES (ID generation) ###\n")

cur.execute("""
    SELECT sequencename, last_value
    FROM pg_sequences
    WHERE schemaname = 'public'
    ORDER BY last_value DESC
    LIMIT 15
""")
results = cur.fetchall()
for r in results:
    print(f"  {r[0]}: last_value = {r[1]:,}")

cur.close()
conn.close()

print("\n\n" + "=" * 80)
print("Analysis complete!")
print("=" * 80)
