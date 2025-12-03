import psycopg2
from collections import defaultdict

conn = psycopg2.connect(
    dbname='techhub',
    user='dgabbassov',
    password='sVLKLeM5D%',
    host='188.130.234.92',
    port='50693'
)

cur = conn.cursor()

# 1. Получаем все таблицы
cur.execute("""
    SELECT table_name
    FROM information_schema.tables
    WHERE table_schema = 'public' AND table_type = 'BASE TABLE'
    ORDER BY table_name
""")
tables = [row[0] for row in cur.fetchall()]

# 2. Получаем структуру колонок
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
columns_data = cur.fetchall()

# 3. Получаем FK
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
fk_data = cur.fetchall()

# 4. Получаем Primary Keys
cur.execute("""
    SELECT
        tc.table_name,
        kcu.column_name
    FROM information_schema.table_constraints tc
    JOIN information_schema.key_column_usage kcu
        ON tc.constraint_name = kcu.constraint_name
    WHERE tc.constraint_type = 'PRIMARY KEY' AND tc.table_schema = 'public'
    ORDER BY tc.table_name
""")
pk_data = cur.fetchall()

# 5. Получаем количество записей в каждой таблице
table_counts = {}
for table in tables:
    try:
        cur.execute(f'SELECT COUNT(*) FROM "{table}"')
        table_counts[table] = cur.fetchone()[0]
    except:
        table_counts[table] = 'N/A'

cur.close()
conn.close()

# Организуем данные
table_columns = defaultdict(list)
for row in columns_data:
    table_columns[row[0]].append(row[1:])

table_fks = defaultdict(list)
for row in fk_data:
    table_fks[str(row[0])].append((row[1], str(row[2]), row[3]))

table_pks = defaultdict(list)
for row in pk_data:
    table_pks[row[0]].append(row[1])

# Группируем таблицы по модулям (Django apps)
modules = defaultdict(list)
for table in tables:
    if '_' in table:
        module = table.split('_')[0]
    else:
        module = 'other'
    modules[module].append(table)

# Генерируем документацию
output = []
output.append("# TechHub Database Schema Documentation")
output.append("")
output.append("## Обзор")
output.append(f"- **Всего таблиц:** {len(tables)}")
output.append(f"- **Всего связей (FK):** {len(fk_data)}")
output.append(f"- **Django приложений:** {len(modules)}")
output.append("")

output.append("## Структура по модулям (Django Apps)")
output.append("")
for module in sorted(modules.keys()):
    output.append(f"### {module}")
    for table in modules[module]:
        count = table_counts.get(table, 0)
        output.append(f"- `{table}` ({count} записей)")
    output.append("")

output.append("---")
output.append("")
output.append("## Детальное описание таблиц")
output.append("")

for table in tables:
    output.append(f"### {table}")
    output.append("")

    count = table_counts.get(table, 0)
    output.append(f"**Записей в таблице:** {count}")
    output.append("")

    # Primary Keys
    pks = table_pks.get(table, [])
    if pks:
        output.append(f"**Primary Key:** {', '.join(pks)}")
        output.append("")

    # Columns
    output.append("| Колонка | Тип | Nullable | Default |")
    output.append("|---------|-----|----------|---------|")

    for col_data in table_columns.get(table, []):
        col_name, dtype, nullable, default, max_len = col_data
        nullable_str = "✓" if nullable == "YES" else "✗"
        dtype_str = f"{dtype}({max_len})" if max_len else dtype
        default_str = str(default)[:50] + "..." if default and len(str(default)) > 50 else (default or "-")
        output.append(f"| {col_name} | {dtype_str} | {nullable_str} | {default_str} |")

    output.append("")

    # Foreign Keys
    fks = table_fks.get(table, [])
    if fks:
        output.append("**Связи (Foreign Keys):**")
        for fk in fks:
            from_col, to_table, to_col = fk
            output.append(f"- `{from_col}` → `{to_table}.{to_col}`")
        output.append("")

    output.append("---")
    output.append("")

# Записываем в файл
with open("DATABASE_SCHEMA.md", "w", encoding="utf-8") as f:
    f.write("\n".join(output))

print(f"Документация сгенерирована: DATABASE_SCHEMA.md")
print(f"Таблиц: {len(tables)}")
print(f"FK связей: {len(fk_data)}")
