import psycopg2

conn = psycopg2.connect(
    dbname='techhub',
    user='dgabbassov',
    password='sVLKLeM5D%',
    host='188.130.234.92',
    port='50693'
)

cur = conn.cursor()

# Получаем структуру всех таблиц с типами данных
cur.execute("""
    SELECT
        t.table_name,
        c.column_name,
        c.data_type,
        c.is_nullable,
        c.column_default,
        c.character_maximum_length
    FROM information_schema.tables t
    JOIN information_schema.columns c ON t.table_name = c.table_name
    WHERE t.table_schema = 'public' AND t.table_type = 'BASE TABLE'
    ORDER BY t.table_name, c.ordinal_position
""")

results = cur.fetchall()

current_table = ''
for row in results:
    table, column, dtype, nullable, default, max_len = row
    if table != current_table:
        print(f'\n\n=== {table} ===')
        current_table = table

    nullable_str = 'NULL' if nullable == 'YES' else 'NOT NULL'
    len_str = f'({max_len})' if max_len else ''
    default_str = f' DEFAULT {default[:50]}...' if default and len(default) > 50 else (f' DEFAULT {default}' if default else '')
    print(f'  {column}: {dtype}{len_str} {nullable_str}{default_str}')

cur.close()
conn.close()
