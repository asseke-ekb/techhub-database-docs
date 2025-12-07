"""
Скрипт для разбиения SA_FULL_DATA_DICTIONARY.md на модули
"""

import re
import os

# Читаем исходный файл
with open('SA_FULL_DATA_DICTIONARY.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Папка для модулей
modules_dir = 'final/modules'
os.makedirs(modules_dir, exist_ok=True)

# Регулярка для поиска модулей
# Ищем паттерн ## module_name\n\n**Описание:**...
module_pattern = r'^## ([a-z_]+)\n\n\*\*Описание:\*\* (.+?)\n\n\*\*Таблиц в модуле:\*\* (\d+)\n\n((?:(?!^## [a-z_]+\n).)*)'

modules = re.findall(module_pattern, content, re.MULTILINE | re.DOTALL)

# Бизнес-модули которые важны для аналитиков
important_modules = {
    'account': '01',
    'service': '02',
    'core': '03',
    'booking': '04',
    'techorda': '05',
    'landing': '06',
    'community': '07',
    'matchmaking': '08',
    'niokr': '09',
    'shared': '10',
}

# Технические модули
tech_modules = {
    'auth': '11',
    'authtoken': '12',
    'oauth2': '13',
    'django': '14',
    'reversion': '15',
    'search': '16',
    'journeymap': '17',
    'explorer': '18',
    'admin': '19',
    'hub': '20',
    'astanahub': '21',
    'silk': '22',
    'social': '23',
    'thumbnail': '24',
    'user': '25',
    'waffle': '26',
    'awsdjangoses': '27',
}

all_modules = {**important_modules, **tech_modules}

print(f"Найдено модулей в файле: {len(modules)}")

for module_name, description, table_count, content_body in modules:
    if module_name in all_modules:
        prefix = all_modules[module_name]
        filename = f"{prefix}_{module_name.upper()}.md"

        # Формируем заголовок
        header = f"""# Модуль {module_name.upper()}

**Описание:** {description}

**Таблиц в модуле:** {table_count}

---

"""
        # Сохраняем файл
        filepath = os.path.join(modules_dir, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(header)
            f.write(content_body.strip())

        print(f"+ Создан: {filename} ({table_count} таблиц)")
    else:
        print(f"? Пропущен модуль: {module_name}")

print(f"\nГотово! Файлы сохранены в папке: {modules_dir}")
