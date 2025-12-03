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
        c.character_maximum_length,
        c.ordinal_position
    FROM information_schema.tables t
    JOIN information_schema.columns c ON t.table_name = c.table_name AND t.table_schema = c.table_schema
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
        ON tc.constraint_name = kcu.constraint_name AND tc.table_schema = kcu.table_schema
    WHERE tc.constraint_type = 'PRIMARY KEY' AND tc.table_schema = 'public'
    ORDER BY tc.table_name
""")
pk_data = cur.fetchall()

# 5. Получаем количество записей
table_counts = {}
for table in tables:
    try:
        cur.execute(f'SELECT COUNT(*) FROM "{table}"')
        table_counts[table] = cur.fetchone()[0]
    except:
        table_counts[table] = 'N/A'
        conn.rollback()

# 6. Получаем комментарии к таблицам (если есть)
cur.execute("""
    SELECT c.relname, d.description
    FROM pg_class c
    LEFT JOIN pg_description d ON c.oid = d.objoid AND d.objsubid = 0
    WHERE c.relkind = 'r' AND c.relnamespace = (SELECT oid FROM pg_namespace WHERE nspname = 'public')
""")
table_comments = {row[0]: row[1] for row in cur.fetchall() if row[1]}

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

# Группируем по модулям
modules = defaultdict(list)
for table in tables:
    if '_' in table:
        module = table.split('_')[0]
    else:
        module = 'other'
    modules[module].append(table)

# Описания модулей
module_descriptions = {
    'account': 'Управление пользователями, компаниями, аутентификацией и авторизацией',
    'admin': 'Административные функции Django',
    'astanahub': 'Общие данные платформы Астана Хаб',
    'auth': 'Стандартная аутентификация Django (группы, права)',
    'authtoken': 'API токены для REST авторизации',
    'awsdjangoses': 'Интеграция с AWS SES (email)',
    'booking': 'Бронирование переговорных комнат и помещений',
    'community': 'Социальные связи (подписки, фолловинг)',
    'core': 'Основной контент: события, вакансии, блоги, статьи, тех.задания',
    'django': 'Системные таблицы Django (миграции, сессии, логи)',
    'explorer': 'SQL Explorer для аналитики',
    'hub': 'Кэш-таблицы',
    'journeymap': 'Карты развития для компаний и пользователей',
    'landing': 'CMS для лендингов и страниц',
    'matchmaking': 'Нетворкинг и мэтчинг пользователей',
    'niokr': 'Научно-исследовательские проекты (НИОКР)',
    'oauth2': 'OAuth2 авторизация',
    'reversion': 'Версионирование объектов (история изменений)',
    'search': 'Поисковые запросы',
    'service': 'Государственные услуги, заявки, формы, экспертиза',
    'shared': 'Общие ресурсы (медиафайлы, SEO, контекст)',
    'silk': 'Профилирование запросов (для разработки)',
    'social': 'Социальная авторизация (Google, Facebook и др.)',
    'techorda': 'Образовательные программы TechOrda',
    'thumbnail': 'Хранение превью изображений',
    'user': 'Сессии пользователей',
    'view': 'Представления базы данных',
    'waffle': 'Feature flags (включение/выключение функций)',
}

# Генерируем документацию
output = []
output.append("# Полный словарь данных ИС TechHub")
output.append("## Все таблицы базы данных")
output.append("")
output.append("**Версия:** 1.0")
output.append("**Дата:** 2025-12-04")
output.append(f"**Всего таблиц:** {len(tables)}")
output.append(f"**Всего FK связей:** {len(fk_data)}")
output.append("")
output.append("---")
output.append("")

# Оглавление
output.append("## Оглавление")
output.append("")
for i, module in enumerate(sorted(modules.keys()), 1):
    desc = module_descriptions.get(module, '')
    output.append(f"{i}. [{module}](#{module}) - {desc}")
output.append("")
output.append("---")
output.append("")

# По каждому модулю
for module in sorted(modules.keys()):
    desc = module_descriptions.get(module, 'Нет описания')
    output.append(f"## {module}")
    output.append("")
    output.append(f"**Описание:** {desc}")
    output.append("")
    output.append(f"**Таблиц в модуле:** {len(modules[module])}")
    output.append("")

    # Список таблиц модуля
    output.append("| Таблица | Записей | Описание |")
    output.append("|---------|---------|----------|")
    for table in modules[module]:
        count = table_counts.get(table, 0)
        comment = table_comments.get(table, '-')
        output.append(f"| `{table}` | {count:,} | {comment} |")
    output.append("")

    # Детальное описание каждой таблицы
    for table in modules[module]:
        output.append(f"### {table}")
        output.append("")

        count = table_counts.get(table, 0)
        output.append(f"**Количество записей:** {count:,}")
        output.append("")

        # Primary Key
        pks = table_pks.get(table, [])
        if pks:
            output.append(f"**Первичный ключ:** `{', '.join(pks)}`")
            output.append("")

        # Структура таблицы
        output.append("**Структура:**")
        output.append("")
        output.append("| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |")
        output.append("|---|---------|------------|------|--------------|----------|")

        for i, col_data in enumerate(table_columns.get(table, []), 1):
            col_name, dtype, nullable, default, max_len, ordinal = col_data
            nullable_str = "Да" if nullable == "YES" else "Нет"
            dtype_str = f"{dtype}({max_len})" if max_len else dtype

            # Сокращаем default если слишком длинный
            if default:
                default_str = str(default)[:40] + "..." if len(str(default)) > 40 else str(default)
            else:
                default_str = "-"

            # Определяем описание по имени колонки
            col_desc = ""
            if col_name == "id":
                col_desc = "Уникальный идентификатор"
            elif col_name == "created_at":
                col_desc = "Дата и время создания"
            elif col_name == "updated_at":
                col_desc = "Дата и время обновления"
            elif col_name.endswith("_id") and col_name != "id":
                col_desc = f"FK на {col_name.replace('_id', '')}"
            elif col_name == "status":
                col_desc = "Статус записи"
            elif col_name == "is_active":
                col_desc = "Признак активности"
            elif col_name == "data":
                col_desc = "Дополнительные данные (JSON)"
            elif col_name == "email":
                col_desc = "Электронная почта"
            elif col_name == "phone":
                col_desc = "Номер телефона"
            elif col_name == "name":
                col_desc = "Наименование"
            elif col_name == "title":
                col_desc = "Заголовок"
            elif col_name == "content":
                col_desc = "Содержимое"
            elif col_name == "slug":
                col_desc = "URL-идентификатор"
            elif col_name == "published":
                col_desc = "Признак публикации"
            elif col_name == "verified":
                col_desc = "Признак верификации"

            output.append(f"| {i} | `{col_name}` | {dtype_str} | {nullable_str} | {default_str} | {col_desc} |")

        output.append("")

        # Foreign Keys
        fks = table_fks.get(table, [])
        if fks:
            output.append("**Внешние ключи (FK):**")
            output.append("")
            output.append("| Поле | Ссылается на |")
            output.append("|------|--------------|")
            for fk in fks:
                from_col, to_table, to_col = fk
                output.append(f"| `{from_col}` | `{to_table}.{to_col}` |")
            output.append("")

        output.append("---")
        output.append("")

# Сводная таблица всех FK
output.append("## Приложение: Полный список Foreign Key связей")
output.append("")
output.append("| № | Таблица | Поле | Ссылается на таблицу | Поле |")
output.append("|---|---------|------|---------------------|------|")
for i, fk in enumerate(fk_data, 1):
    output.append(f"| {i} | `{fk[0]}` | `{fk[1]}` | `{fk[2]}` | `{fk[3]}` |")
output.append("")

# Записываем в файл
with open("SA_FULL_DATA_DICTIONARY.md", "w", encoding="utf-8") as f:
    f.write("\n".join(output))

print(f"Документация сгенерирована: SA_FULL_DATA_DICTIONARY.md")
print(f"Таблиц: {len(tables)}")
print(f"Модулей: {len(modules)}")
print(f"FK связей: {len(fk_data)}")
