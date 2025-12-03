import psycopg2

conn = psycopg2.connect(
    dbname='techhub',
    user='dgabbassov',
    password='sVLKLeM5D%',
    host='188.130.234.92',
    port='50693'
)

cur = conn.cursor()

# Альтернативный способ получить FK через pg_constraint
cur.execute("""
    SELECT
        conrelid::regclass AS from_table,
        a.attname AS from_column,
        confrelid::regclass AS to_table,
        af.attname AS to_column
    FROM pg_constraint c
    JOIN pg_attribute a ON a.attnum = ANY(c.conkey) AND a.attrelid = c.conrelid
    JOIN pg_attribute af ON af.attnum = ANY(c.confkey) AND af.attrelid = c.confrelid
    WHERE c.contype = 'f'
    ORDER BY conrelid::regclass::text, a.attname
""")

results = cur.fetchall()

print(f"=== FOREIGN KEY RELATIONSHIPS ({len(results)} total) ===\n")
for row in results:
    from_table, from_col, to_table, to_col = row
    print(f"{from_table}.{from_col} -> {to_table}.{to_col}")

cur.close()
conn.close()
