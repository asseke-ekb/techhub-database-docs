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
        c.character_maximum_length
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

# 5. Количество записей
table_counts = {}
for table in tables:
    try:
        cur.execute(f'SELECT COUNT(*) FROM "{table}"')
        table_counts[table] = cur.fetchone()[0]
    except:
        table_counts[table] = 0
        conn.rollback()

cur.close()
conn.close()

# Организуем данные
table_columns = defaultdict(list)
for row in columns_data:
    table_columns[row[0]].append(row[1:])

table_fks = defaultdict(list)
fk_relations = []
for row in fk_data:
    from_tbl = str(row[0])
    to_tbl = str(row[2])
    table_fks[from_tbl].append((row[1], to_tbl, row[3]))
    fk_relations.append((from_tbl, row[1], to_tbl, row[3]))

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

# Описания сущностей
entity_descriptions = {
    # Account
    'account_user': 'Пользователь системы - основная сущность для аутентификации и авторизации',
    'account_company': 'Компания (юр.лицо или ИП) - резидент платформы',
    'account_usercompany': 'Связь пользователя с компанией (M:N) с указанием роли',
    'account_activation': 'Коды активации для подтверждения email/телефона',
    'account_certificate': 'Сертификаты и достижения пользователя',
    'account_education': 'Образование пользователя',
    'account_experience': 'Опыт работы пользователя',
    'account_course': 'Пройденные курсы пользователя',
    'account_complaint': 'Жалобы на пользователей или компании',
    'account_contactpress': 'Контакты для прессы',
    'account_contactrequest': 'Запросы на контакт',
    'account_emaildigest': 'Подписки на email-рассылки',
    'account_usercompanyinvitation': 'Приглашения в компанию',
    'account_usercompanyrequest': 'Запросы на вступление в компанию',
    'account_user_groups': 'Связь пользователей с группами Django',
    'account_user_user_permissions': 'Индивидуальные права пользователей',

    # Core
    'core_organization': 'Организация-партнёр платформы (справочник)',
    'core_event': 'Событие/мероприятие',
    'core_eventparticipant': 'Участник события',
    'core_vacancy': 'Вакансия от компании',
    'core_vacancycandidate': 'Кандидат на вакансию',
    'core_vacancycandidate_certificates': 'Сертификаты кандидата',
    'core_blog': 'Блог-пост пользователя или компании',
    'core_article': 'Официальная статья платформы',
    'core_techtask': 'Техническое задание на разработку',
    'core_techtasksolution': 'Решение технического задания',
    'core_discussion': 'Обсуждение/дискуссия',
    'core_discussionvote': 'Голос в обсуждении',
    'core_comment': 'Комментарий (полиморфный - к любой сущности)',
    'core_category': 'Категория контента',
    'core_feed': 'Лента новостей (агрегатор контента)',
    'core_notification': 'Уведомление пользователю',
    'core_city': 'Справочник городов',
    'core_country': 'Справочник стран',
    'core_faq': 'Раздел FAQ',
    'core_faqitem': 'Вопрос-ответ в FAQ',
    'core_banner': 'Баннер на сайте',
    'core_actionlog': 'Лог действий пользователей',
    'core_infrastructure': 'Инфраструктурный объект',
    'core_infrastructureimage': 'Изображение инфраструктуры',
    'core_infrastructurerequest': 'Заявка на инфраструктуру',
    'core_floordata': 'Данные этажа здания',
    'core_elabsannouncement': 'Объявление E-Labs',

    # Service
    'service_service': 'Услуга/сервис платформы (справочник)',
    'service_servicerequest': 'Заявка на услугу',
    'service_servicerequestlog': 'Лог изменений заявки',
    'service_servicerequeststatus': 'История статусов заявки',
    'service_servicerequestbpstatus': 'Статус бизнес-процесса заявки',
    'service_hubform': 'Шаблон формы для заявки',
    'service_hubformstep': 'Шаг формы',
    'service_hubformfield': 'Поле формы',
    'service_hubformdata': 'Заполненные данные формы',
    'service_expertise': 'Экспертиза заявки',
    'service_expertisegroup': 'Группа экспертов для услуги',
    'service_expertisegroup_users': 'Эксперты в группе',
    'service_expertdocument': 'Документ от эксперта',
    'service_externaldocument': 'Внешний документ заявки',
    'service_extradocument': 'Дополнительный документ',
    'service_vote': 'Голос эксперта по заявке',
    'service_protocol': 'Протокол комиссии',
    'service_protocol_accepted': 'Одобренные заявки в протоколе',
    'service_protocol_rejected': 'Отклонённые заявки в протоколе',
    'service_report': 'Отчёт по заявке',
    'service_servicenote': 'Заметка к услуге',
    'service_service_users': 'Менеджеры услуги',
    'service_seedmoneyreport': 'Отчёт по гранту Seed Money',
    'service_techordareport': 'Отчёт TechOrda',
    'service_techordareportstudent': 'Студент в отчёте TechOrda',
    'service_techordastudent': 'Студент TechOrda',
    'service_guppurchaseplan': 'План закупок ГУП',
    'service_guppurchaseapplication': 'Заявка на закупку ГУП',
    'service_gupreport': 'Отчёт ГУП',
    'service_pitchinggrade': 'Оценка питчинга',
    'service_amolog': 'Лог интеграции с AmoCRM',
    'service_documentologlog': 'Лог интеграции с Documentolog',
    'service_externalhooklog': 'Лог внешних webhook',
    'service_boxstorage': 'Хранилище файлов',

    # Booking
    'booking_room': 'Комната для бронирования',
    'booking_booking': 'Бронирование комнаты',
    'booking_bookingstatus': 'История статусов бронирования',

    # TechOrda
    'techorda_school': 'Школа/провайдер обучения',
    'techorda_course': 'Курс обучения',
    'techorda_flow': 'Поток обучения (набор)',
    'techorda_applicationform': 'Форма заявки на обучение',
    'techorda_assessment': 'Оценка/тестирование',
    'techorda_courseapplication': 'Заявка на курс',
    'techorda_coursefavorite': 'Избранный курс пользователя',

    # Landing
    'landing_landing': 'Лендинг (устаревший)',
    'landing_page': 'Страница CMS',
    'landing_section': 'Секция страницы',
    'landing_component': 'Компонент секции',
    'landing_pagemediafile': 'Медиафайл страницы',

    # Community
    'community_userfollow': 'Подписка на пользователя',
    'community_companyfollow': 'Подписка на компанию',

    # Matchmaking
    'matchmaking_profile': 'Профиль для нетворкинга',
    'matchmaking_match': 'Мэтч между пользователями',

    # JourneyMap
    'journeymap_journeymap': 'Карта развития',
    'journeymap_step': 'Шаг карты развития',
    'journeymap_step_next_steps': 'Связи между шагами',
    'journeymap_task': 'Задача в шаге',
    'journeymap_question': 'Вопрос в задаче',
    'journeymap_userstate': 'Состояние пользователя на карте',
    'journeymap_companystate': 'Состояние компании на карте',

    # NIOKR
    'niokr_niokrproject': 'Проект НИОКР',
    'niokr_niokrprojectexecutor': 'Исполнитель проекта НИОКР',
    'niokr_niokrprojectexecutor_projects': 'Связь исполнитель-проект',
    'niokr_niokrnotification': 'Уведомление НИОКР',
    'niokr_niokrnotification_projects': 'Связь уведомление-проект',

    # Shared
    'shared_mediafile': 'Медиафайл (публичный)',
    'shared_protectedmediafile': 'Медиафайл (защищённый)',
    'shared_seodata': 'SEO данные страницы',
    'shared_contextdata': 'Контекстные данные',
    'shared_smslog': 'Лог SMS сообщений',
    'shared_largecache': 'Кэш больших объектов',

    # Auth/Django
    'auth_group': 'Группа пользователей Django',
    'auth_permission': 'Разрешение Django',
    'auth_group_permissions': 'Разрешения группы',
    'django_content_type': 'Тип контента Django',
    'django_admin_log': 'Лог админ-панели',
    'django_migrations': 'История миграций',
    'django_session': 'Сессии Django',
    'django_dramatiq_task': 'Фоновые задачи Dramatiq',

    # Other
    'authtoken_token': 'API токен пользователя',
    'social_auth_usersocialauth': 'OAuth привязка (Google и др.)',
    'social_auth_association': 'OAuth ассоциация',
    'social_auth_code': 'OAuth код',
    'social_auth_nonce': 'OAuth nonce',
    'social_auth_partial': 'OAuth частичные данные',
    'oauth2_provider_application': 'OAuth2 приложение',
    'oauth2_provider_accesstoken': 'OAuth2 access token',
    'oauth2_provider_refreshtoken': 'OAuth2 refresh token',
    'oauth2_provider_grant': 'OAuth2 grant',
    'oauth2_provider_idtoken': 'OAuth2 ID token',
    'reversion_revision': 'Ревизия объекта',
    'reversion_version': 'Версия объекта',
    'explorer_query': 'Сохранённый SQL запрос',
    'explorer_queryfavorite': 'Избранный SQL запрос',
    'explorer_querylog': 'Лог выполнения запросов',
    'search_search': 'Поисковый запрос',
    'thumbnail_kvstore': 'Кэш превью изображений',
    'user_sessions_session': 'Расширенная сессия пользователя',
    'silk_request': 'Профилирование запроса',
    'silk_response': 'Профилирование ответа',
    'silk_sqlquery': 'Профилирование SQL',
    'silk_profile': 'Профиль производительности',
    'silk_profile_queries': 'Связь профиль-запросы',
    'waffle_flag': 'Feature flag',
    'waffle_flag_groups': 'Feature flag для групп',
    'waffle_flag_users': 'Feature flag для пользователей',
    'waffle_sample': 'Семплирование feature',
    'waffle_switch': 'Переключатель feature',
    'awsdjangoses_awsblacklist': 'Чёрный список AWS SES',
    'admin_honeypot_loginattempt': 'Попытки входа в honeypot',
    'hub_cache_table': 'Кэш-таблица',
    'astanahub_shared_contextdata': 'Контекстные данные AstanaHub',
    'astanahub_shared_seodata': 'SEO данные AstanaHub',
    'astanahub_shared_smslog': 'SMS лог AstanaHub',
    'view_niokr_organizations': 'Представление организаций НИОКР',
}

# Типы сущностей
entity_types = {
    # Справочники
    'core_organization': 'Справочник',
    'core_category': 'Справочник',
    'core_city': 'Справочник',
    'core_country': 'Справочник',
    'core_faq': 'Справочник',
    'service_service': 'Справочник',
    'booking_room': 'Справочник',
    'auth_group': 'Справочник',
    'auth_permission': 'Справочник',
    'django_content_type': 'Справочник',
    'waffle_flag': 'Справочник',
    'waffle_switch': 'Справочник',
    'techorda_flow': 'Справочник',

    # Основные сущности
    'account_user': 'Основная',
    'account_company': 'Основная',
    'core_event': 'Основная',
    'core_vacancy': 'Основная',
    'core_blog': 'Основная',
    'core_article': 'Основная',
    'core_techtask': 'Основная',
    'service_servicerequest': 'Основная',
    'booking_booking': 'Основная',
    'techorda_school': 'Основная',
    'techorda_course': 'Основная',
    'landing_page': 'Основная',
    'core_infrastructure': 'Основная',
    'niokr_niokrproject': 'Основная',
    'journeymap_journeymap': 'Основная',

    # Связующие таблицы
    'account_usercompany': 'Связующая',
    'account_user_groups': 'Связующая',
    'account_user_user_permissions': 'Связующая',
    'auth_group_permissions': 'Связующая',
    'service_expertisegroup_users': 'Связующая',
    'service_service_users': 'Связующая',
    'service_protocol_accepted': 'Связующая',
    'service_protocol_rejected': 'Связующая',
    'journeymap_step_next_steps': 'Связующая',
    'niokr_niokrprojectexecutor_projects': 'Связующая',
    'niokr_niokrnotification_projects': 'Связующая',
    'waffle_flag_groups': 'Связующая',
    'waffle_flag_users': 'Связующая',
    'silk_profile_queries': 'Связующая',
    'core_vacancycandidate_certificates': 'Связующая',

    # Логи и история
    'core_actionlog': 'Лог',
    'service_servicerequestlog': 'Лог',
    'service_amolog': 'Лог',
    'service_documentologlog': 'Лог',
    'service_externalhooklog': 'Лог',
    'shared_smslog': 'Лог',
    'astanahub_shared_smslog': 'Лог',
    'django_admin_log': 'Лог',
    'explorer_querylog': 'Лог',
    'admin_honeypot_loginattempt': 'Лог',

    # Формы и данные форм
    'service_hubform': 'Форма',
    'service_hubformstep': 'Форма',
    'service_hubformfield': 'Форма',
    'service_hubformdata': 'Данные формы',
    'techorda_applicationform': 'Форма',
}

# ================== ГЕНЕРАЦИЯ ДОКУМЕНТАЦИИ ==================

output = []
output.append("# Полный анализ сущностей ИС TechHub")
output.append("## 157 таблиц базы данных")
output.append("")
output.append("**Версия:** 1.0")
output.append("**Дата:** 2025-12-04")
output.append("")
output.append("---")
output.append("")
output.append("## Содержание")
output.append("")
output.append("1. [Сводная таблица всех сущностей](#1-сводная-таблица-всех-сущностей)")
output.append("2. [Классификация сущностей по типам](#2-классификация-сущностей-по-типам)")
output.append("3. [Анализ сущностей по модулям](#3-анализ-сущностей-по-модулям)")
output.append("4. [Матрица связей](#4-матрица-связей)")
output.append("5. [ER-диаграмма (PlantUML)](#5-er-диаграмма-plantuml)")
output.append("6. [ER-диаграмма (Mermaid)](#6-er-диаграмма-mermaid)")
output.append("")
output.append("---")
output.append("")

# 1. Сводная таблица
output.append("## 1. Сводная таблица всех сущностей")
output.append("")
output.append("| № | Таблица | Модуль | Тип | Записей | PK | FK | Описание |")
output.append("|---|---------|--------|-----|---------|----|----|----------|")

for i, table in enumerate(tables, 1):
    module = table.split('_')[0] if '_' in table else 'other'
    etype = entity_types.get(table, 'Транзакционная')
    count = table_counts.get(table, 0)
    pk = ', '.join(table_pks.get(table, ['-']))
    fk_count = len(table_fks.get(table, []))
    desc = entity_descriptions.get(table, '-')
    output.append(f"| {i} | `{table}` | {module} | {etype} | {count:,} | {pk} | {fk_count} | {desc} |")

output.append("")
output.append("---")
output.append("")

# 2. Классификация по типам
output.append("## 2. Классификация сущностей по типам")
output.append("")

types_grouped = defaultdict(list)
for table in tables:
    etype = entity_types.get(table, 'Транзакционная')
    types_grouped[etype].append(table)

type_order = ['Основная', 'Справочник', 'Связующая', 'Форма', 'Данные формы', 'Лог', 'Транзакционная']
for etype in type_order:
    if etype in types_grouped:
        output.append(f"### {etype} ({len(types_grouped[etype])} таблиц)")
        output.append("")
        for table in types_grouped[etype]:
            desc = entity_descriptions.get(table, '')
            output.append(f"- `{table}` - {desc}")
        output.append("")

output.append("---")
output.append("")

# 3. Анализ по модулям
output.append("## 3. Анализ сущностей по модулям")
output.append("")

module_descriptions = {
    'account': 'Управление пользователями и компаниями',
    'core': 'Основной контент платформы',
    'service': 'Государственные услуги и заявки',
    'booking': 'Бронирование помещений',
    'techorda': 'Образовательные программы',
    'landing': 'CMS для страниц',
    'community': 'Социальные связи',
    'matchmaking': 'Нетворкинг',
    'journeymap': 'Карты развития',
    'niokr': 'Научные проекты',
    'shared': 'Общие ресурсы',
    'auth': 'Аутентификация Django',
    'django': 'Системные таблицы',
    'oauth2': 'OAuth2 авторизация',
    'social': 'Социальная авторизация',
    'reversion': 'Версионирование',
    'explorer': 'SQL аналитика',
    'search': 'Поиск',
    'silk': 'Профилирование',
    'waffle': 'Feature flags',
    'thumbnail': 'Превью изображений',
    'user': 'Сессии',
    'admin': 'Honeypot админки',
    'authtoken': 'API токены',
    'awsdjangoses': 'AWS SES интеграция',
    'hub': 'Кэш',
    'astanahub': 'Данные AstanaHub',
    'view': 'Представления БД',
}

for module in sorted(modules.keys()):
    tbl_list = modules[module]
    total_records = sum(table_counts.get(t, 0) for t in tbl_list)
    desc = module_descriptions.get(module, '')

    output.append(f"### Модуль: {module}")
    output.append("")
    output.append(f"**Описание:** {desc}")
    output.append(f"**Таблиц:** {len(tbl_list)}")
    output.append(f"**Всего записей:** {total_records:,}")
    output.append("")
    output.append("| Таблица | Тип | Записей | Описание |")
    output.append("|---------|-----|---------|----------|")

    for table in tbl_list:
        etype = entity_types.get(table, 'Транзакционная')
        count = table_counts.get(table, 0)
        desc = entity_descriptions.get(table, '-')
        output.append(f"| `{table}` | {etype} | {count:,} | {desc} |")

    output.append("")

output.append("---")
output.append("")

# 4. Матрица связей
output.append("## 4. Матрица связей")
output.append("")
output.append("### 4.1. Все Foreign Key связи (218 связей)")
output.append("")
output.append("| № | От таблицы | Поле | К таблице | Поле |")
output.append("|---|------------|------|-----------|------|")

for i, (from_tbl, from_col, to_tbl, to_col) in enumerate(fk_relations, 1):
    output.append(f"| {i} | `{from_tbl}` | `{from_col}` | `{to_tbl}` | `{to_col}` |")

output.append("")

# Статистика связей
output.append("### 4.2. Статистика связей")
output.append("")

# Входящие связи (на какие таблицы ссылаются)
incoming = defaultdict(int)
for from_tbl, from_col, to_tbl, to_col in fk_relations:
    incoming[to_tbl] += 1

output.append("**Таблицы с наибольшим количеством входящих связей (на них ссылаются):**")
output.append("")
output.append("| Таблица | Входящих FK |")
output.append("|---------|-------------|")
for tbl, cnt in sorted(incoming.items(), key=lambda x: -x[1])[:20]:
    output.append(f"| `{tbl}` | {cnt} |")
output.append("")

# Исходящие связи
outgoing = defaultdict(int)
for from_tbl, from_col, to_tbl, to_col in fk_relations:
    outgoing[from_tbl] += 1

output.append("**Таблицы с наибольшим количеством исходящих связей (ссылаются на другие):**")
output.append("")
output.append("| Таблица | Исходящих FK |")
output.append("|---------|--------------|")
for tbl, cnt in sorted(outgoing.items(), key=lambda x: -x[1])[:20]:
    output.append(f"| `{tbl}` | {cnt} |")
output.append("")

output.append("---")
output.append("")

# 5. PlantUML ER диаграмма
output.append("## 5. ER-диаграмма (PlantUML)")
output.append("")
output.append("Сохраните код ниже в файл с расширением `.puml` и откройте в PlantUML viewer.")
output.append("")
output.append("```plantuml")
output.append("@startuml TechHub_Full_ER")
output.append("")
output.append("!define TABLE(name) entity name << (T,#FFAAAA) >>")
output.append("!define PRIMARY_KEY(x) <b><u>x</u></b>")
output.append("!define FOREIGN_KEY(x) <i>x</i>")
output.append("")
output.append("skinparam linetype ortho")
output.append("skinparam nodesep 20")
output.append("skinparam ranksep 30")
output.append("hide circle")
output.append("skinparam class {")
output.append("  BackgroundColor White")
output.append("  BorderColor Black")
output.append("}")
output.append("")

# Группируем по модулям в PlantUML
for module in sorted(modules.keys()):
    tbl_list = modules[module]
    color = {
        'account': '#E3F2FD',
        'core': '#E8F5E9',
        'service': '#FFF3E0',
        'booking': '#FCE4EC',
        'techorda': '#E0F7FA',
        'landing': '#FFF8E1',
        'community': '#F3E5F5',
        'matchmaking': '#E8EAF6',
    }.get(module, '#FAFAFA')

    output.append(f"package \"{module}\" {color} {{")

    for table in tbl_list:
        pk_cols = table_pks.get(table, ['id'])
        fks = table_fks.get(table, [])
        cols = table_columns.get(table, [])

        output.append(f"  entity {table} {{")

        # PK
        for pk in pk_cols:
            output.append(f"    * {pk} : PK")
        output.append("    --")

        # Остальные колонки (только первые 5)
        shown = 0
        for col_data in cols:
            col_name = col_data[0]
            if col_name not in pk_cols and shown < 5:
                dtype = col_data[1]
                if dtype == 'character varying':
                    dtype = 'varchar'
                elif dtype == 'timestamp with time zone':
                    dtype = 'timestamp'
                fk_mark = ' FK' if any(fk[0] == col_name for fk in fks) else ''
                output.append(f"    {col_name} : {dtype}{fk_mark}")
                shown += 1

        if len(cols) > shown + len(pk_cols):
            output.append(f"    ... (+{len(cols) - shown - len(pk_cols)} fields)")

        output.append("  }")
        output.append("")

    output.append("}")
    output.append("")

# Связи
output.append("' === RELATIONSHIPS ===")
for from_tbl, from_col, to_tbl, to_col in fk_relations:
    output.append(f"{from_tbl} " + "}o--|| " + f"{to_tbl}")

output.append("")
output.append("@enduml")
output.append("```")
output.append("")
output.append("---")
output.append("")

# 6. Mermaid ER диаграмма (разбитая по модулям)
output.append("## 6. ER-диаграмма (Mermaid)")
output.append("")
output.append("Из-за большого количества таблиц, диаграмма разбита по модулям.")
output.append("")

for module in ['account', 'core', 'service', 'booking', 'techorda', 'landing']:
    if module not in modules:
        continue

    tbl_list = modules[module]
    output.append(f"### 6.{list(modules.keys()).index(module)+1}. Модуль {module}")
    output.append("")
    output.append("```mermaid")
    output.append("erDiagram")

    # Сущности модуля
    for table in tbl_list:
        pk_cols = table_pks.get(table, ['id'])
        cols = table_columns.get(table, [])

        output.append(f"    {table} {{")
        for pk in pk_cols:
            output.append(f"        int {pk} PK")

        shown = 0
        for col_data in cols:
            col_name = col_data[0]
            dtype = col_data[1]
            if col_name not in pk_cols and shown < 4:
                if 'int' in dtype:
                    mtype = 'int'
                elif 'varchar' in dtype or 'character' in dtype or 'text' in dtype:
                    mtype = 'string'
                elif 'bool' in dtype:
                    mtype = 'boolean'
                elif 'timestamp' in dtype or 'date' in dtype:
                    mtype = 'datetime'
                elif 'json' in dtype:
                    mtype = 'json'
                else:
                    mtype = 'string'
                output.append(f"        {mtype} {col_name}")
                shown += 1
        output.append("    }")

    # Связи внутри модуля
    for from_tbl, from_col, to_tbl, to_col in fk_relations:
        if from_tbl in tbl_list and to_tbl in tbl_list:
            output.append(f"    {from_tbl} }}o--|| {to_tbl} : \"{from_col}\"")
        elif from_tbl in tbl_list and to_tbl == 'account_user':
            output.append(f"    {from_tbl} }}o--|| account_user : \"{from_col}\"")
        elif from_tbl in tbl_list and to_tbl == 'account_company':
            output.append(f"    {from_tbl} }}o--|| account_company : \"{from_col}\"")

    output.append("```")
    output.append("")

output.append("---")
output.append("")
output.append("*Документ сгенерирован автоматически на основе анализа схемы БД TechHub*")

# Записываем в файл
with open("SA_FULL_ENTITY_ANALYSIS.md", "w", encoding="utf-8") as f:
    f.write("\n".join(output))

print(f"Создан файл: SA_FULL_ENTITY_ANALYSIS.md")
print(f"Таблиц: {len(tables)}")
print(f"FK связей: {len(fk_relations)}")
print(f"Модулей: {len(modules)}")
