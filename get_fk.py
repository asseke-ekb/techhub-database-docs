import psycopg2

conn = psycopg2.connect(
    dbname='techhub',
    user='dgabbassov',
    password='sVLKLeM5D%',
    host='188.130.234.92',
    port='50693'
)

cur = conn.cursor()

# Получаем все Foreign Keys
cur.execute("""
    SELECT
        tc.table_name AS from_table,
        kcu.column_name AS from_column,
        ccu.table_name AS to_table,
        ccu.column_name AS to_column
    FROM information_schema.table_constraints AS tc
    JOIN information_schema.key_column_usage AS kcu
        ON tc.constraint_name = kcu.constraint_name
        AND tc.table_schema = kcu.table_schema
    JOIN information_schema.constraint_column_usage AS ccu
        ON ccu.constraint_name = tc.constraint_name
        AND ccu.table_schema = tc.table_schema
    WHERE tc.constraint_type = 'FOREIGN KEY'
    ORDER BY tc.table_name, kcu.column_name
""")

results = cur.fetchall()

print("=== FOREIGN KEY RELATIONSHIPS ===\n")
for row in results:
    from_table, from_col, to_table, to_col = row
    print(f"{from_table}.{from_col} -> {to_table}.{to_col}")

cur.close()
conn.close()
