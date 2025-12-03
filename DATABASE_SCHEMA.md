# TechHub Database Schema Documentation

## Обзор
- **Всего таблиц:** 157
- **Всего связей (FK):** 218
- **Django приложений:** 27

## Структура по модулям (Django Apps)

### account
- `account_activation` (1810 записей)
- `account_certificate` (1 записей)
- `account_company` (6639 записей)
- `account_complaint` (20 записей)
- `account_contactpress` (0 записей)
- `account_contactrequest` (0 записей)
- `account_course` (1 записей)
- `account_education` (1 записей)
- `account_emaildigest` (31474 записей)
- `account_experience` (0 записей)
- `account_user` (54062 записей)
- `account_user_groups` (109 записей)
- `account_user_user_permissions` (2289 записей)
- `account_usercompany` (4536 записей)
- `account_usercompanyinvitation` (2 записей)
- `account_usercompanyrequest` (254 записей)

### admin
- `admin_honeypot_loginattempt` (69000 записей)

### astanahub
- `astanahub_shared_contextdata` (0 записей)
- `astanahub_shared_seodata` (0 записей)
- `astanahub_shared_smslog` (651 записей)

### auth
- `auth_group` (11 записей)
- `auth_group_permissions` (1114 записей)
- `auth_permission` (625 записей)

### authtoken
- `authtoken_token` (1138 записей)

### awsdjangoses
- `awsdjangoses_awsblacklist` (200 записей)

### booking
- `booking_booking` (8673 записей)
- `booking_bookingstatus` (8691 записей)
- `booking_room` (16 записей)

### community
- `community_companyfollow` (3 записей)
- `community_userfollow` (18 записей)

### core
- `core_actionlog` (124975 записей)
- `core_article` (83 записей)
- `core_banner` (27 записей)
- `core_blog` (1801 записей)
- `core_category` (14 записей)
- `core_city` (16 записей)
- `core_comment` (2585 записей)
- `core_country` (1 записей)
- `core_discussion` (157 записей)
- `core_discussionvote` (335 записей)
- `core_elabsannouncement` (70 записей)
- `core_event` (1459 записей)
- `core_eventparticipant` (864 записей)
- `core_faq` (7 записей)
- `core_faqitem` (46 записей)
- `core_feed` (4789 записей)
- `core_floordata` (16 записей)
- `core_infrastructure` (504 записей)
- `core_infrastructureimage` (397 записей)
- `core_infrastructurerequest` (37 записей)
- `core_notification` (1233 записей)
- `core_organization` (45 записей)
- `core_techtask` (247 записей)
- `core_techtasksolution` (232 записей)
- `core_vacancy` (1205 записей)
- `core_vacancycandidate` (5344 записей)
- `core_vacancycandidate_certificates` (192 записей)

### django
- `django_admin_log` (42696 записей)
- `django_content_type` (155 записей)
- `django_dramatiq_task` (0 записей)
- `django_migrations` (819 записей)
- `django_session` (0 записей)

### explorer
- `explorer_query` (6 записей)
- `explorer_queryfavorite` (0 записей)
- `explorer_querylog` (1129 записей)

### hub
- `hub_cache_table` (63 записей)

### journeymap
- `journeymap_companystate` (0 записей)
- `journeymap_journeymap` (0 записей)
- `journeymap_question` (0 записей)
- `journeymap_step` (0 записей)
- `journeymap_step_next_steps` (0 записей)
- `journeymap_task` (0 записей)
- `journeymap_userstate` (0 записей)

### landing
- `landing_component` (2790 записей)
- `landing_landing` (8 записей)
- `landing_page` (562 записей)
- `landing_pagemediafile` (18517 записей)
- `landing_section` (560 записей)

### matchmaking
- `matchmaking_match` (31 записей)
- `matchmaking_profile` (19 записей)

### niokr
- `niokr_niokrnotification` (3 записей)
- `niokr_niokrnotification_projects` (2 записей)
- `niokr_niokrproject` (1 записей)
- `niokr_niokrprojectexecutor` (1 записей)
- `niokr_niokrprojectexecutor_projects` (1 записей)

### oauth2
- `oauth2_provider_accesstoken` (9 записей)
- `oauth2_provider_application` (8 записей)
- `oauth2_provider_grant` (1037 записей)
- `oauth2_provider_idtoken` (0 записей)
- `oauth2_provider_refreshtoken` (0 записей)

### reversion
- `reversion_revision` (19559 записей)
- `reversion_version` (9281 записей)

### search
- `search_search` (7607 записей)

### service
- `service_amolog` (0 записей)
- `service_boxstorage` (691 записей)
- `service_documentologlog` (1117 записей)
- `service_expertdocument` (0 записей)
- `service_expertise` (787 записей)
- `service_expertisegroup` (13 записей)
- `service_expertisegroup_users` (25 записей)
- `service_externaldocument` (195 записей)
- `service_externalhooklog` (2092 записей)
- `service_extradocument` (101 записей)
- `service_guppurchaseapplication` (15 записей)
- `service_guppurchaseplan` (32 записей)
- `service_gupreport` (267 записей)
- `service_hubform` (282 записей)
- `service_hubformdata` (61635 записей)
- `service_hubformfield` (6603 записей)
- `service_hubformstep` (569 записей)
- `service_pitchinggrade` (1538 записей)
- `service_protocol` (104 записей)
- `service_protocol_accepted` (467 записей)
- `service_protocol_rejected` (606 записей)
- `service_report` (13110 записей)
- `service_seedmoneyreport` (333 записей)
- `service_service` (310 записей)
- `service_service_users` (906 записей)
- `service_servicenote` (2 записей)
- `service_servicerequest` (56322 записей)
- `service_servicerequestbpstatus` (82810 записей)
- `service_servicerequestlog` (4571 записей)
- `service_servicerequeststatus` (2031 записей)
- `service_techordareport` (503 записей)
- `service_techordareportstudent` (4 записей)
- `service_techordastudent` (3307 записей)
- `service_vote` (12945 записей)

### shared
- `shared_contextdata` (243 записей)
- `shared_largecache` (2 записей)
- `shared_mediafile` (50936 записей)
- `shared_protectedmediafile` (92960 записей)
- `shared_seodata` (97 записей)
- `shared_smslog` (0 записей)

### silk
- `silk_profile` (0 записей)
- `silk_profile_queries` (0 записей)
- `silk_request` (73 записей)
- `silk_response` (73 записей)
- `silk_sqlquery` (571 записей)

### social
- `social_auth_association` (0 записей)
- `social_auth_code` (0 записей)
- `social_auth_nonce` (0 записей)
- `social_auth_partial` (0 записей)
- `social_auth_usersocialauth` (19505 записей)

### techorda
- `techorda_applicationform` (19 записей)
- `techorda_assessment` (45 записей)
- `techorda_course` (203 записей)
- `techorda_courseapplication` (15 записей)
- `techorda_coursefavorite` (16 записей)
- `techorda_flow` (4 записей)
- `techorda_school` (82 записей)

### thumbnail
- `thumbnail_kvstore` (230644 записей)

### user
- `user_sessions_session` (2952040 записей)

### waffle
- `waffle_flag` (56 записей)
- `waffle_flag_groups` (2 записей)
- `waffle_flag_users` (24 записей)
- `waffle_sample` (0 записей)
- `waffle_switch` (44 записей)

---

## Детальное описание таблиц

### account_activation

**Записей в таблице:** 1810

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| created_at | timestamp with time zone | ✗ | - |
| updated_at | timestamp with time zone | ✗ | - |
| uuid | uuid | ✗ | - |
| email | character varying(200) | ✓ | - |
| phone | character varying(20) | ✓ | - |
| code | character varying(6) | ✗ | - |
| is_active | boolean | ✗ | - |
| iteration | integer | ✗ | - |
| data | jsonb | ✗ | - |
| type | character varying(30) | ✗ | - |
| user_id | integer | ✓ | - |

**Связи (Foreign Keys):**
- `user_id` → `account_user.id`

---

### account_certificate

**Записей в таблице:** 1

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | - |
| created_at | timestamp with time zone | ✗ | - |
| updated_at | timestamp with time zone | ✗ | - |
| name | character varying(255) | ✗ | - |
| organization | character varying(255) | ✗ | - |
| issue_date | date | ✗ | - |
| user_id | integer | ✗ | - |

**Связи (Foreign Keys):**
- `user_id` → `account_user.id`

---

### account_company

**Записей в таблице:** 6639

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | nextval('account_company_id_seq'::regclass) |
| created_at | timestamp with time zone | ✗ | - |
| updated_at | timestamp with time zone | ✗ | - |
| tin | character varying(12) | ✓ | - |
| name | character varying(1000) | ✗ | - |
| address | character varying(2000) | ✗ | - |
| short_name | character varying(200) | ✗ | - |
| bank | character varying(200) | ✗ | - |
| kbe | smallint | ✓ | - |
| iik | character varying(20) | ✗ | - |
| bik | character varying(20) | ✗ | - |
| company_type | character varying(30) | ✗ | - |
| verified | boolean | ✗ | - |
| search_field | text | ✗ | - |
| tag_it_company | jsonb | ✗ | - |
| tag_startup | jsonb | ✗ | - |
| tag_techpark | jsonb | ✗ | - |
| tag_ts_member | jsonb | ✗ | - |
| description | text | ✗ | - |
| email | character varying(200) | ✗ | - |
| facebook_url | character varying(200) | ✗ | - |
| gis_url | character varying(200) | ✗ | - |
| instagram_url | character varying(200) | ✗ | - |
| linkedin_url | character varying(200) | ✗ | - |
| phone | character varying(30) | ✗ | - |
| website | character varying(1000) | ✗ | - |
| author_id | integer | ✓ | - |
| status | character varying(20) | ✗ | - |
| image_id | uuid | ✓ | - |
| tag_corp_partner | jsonb | ✗ | - |
| city_phone | character varying(50) | ✗ | - |
| director_first_name | character varying(200) | ✗ | - |
| director_last_name | character varying(200) | ✗ | - |
| job_fair | boolean | ✗ | - |
| service_provider | boolean | ✗ | - |
| games_data | jsonb | ✗ | - |
| tag_nii | jsonb | ✗ | - |
| tag_nedrouser | jsonb | ✗ | - |
| hub_space_member | boolean | ✗ | - |
| adoption | jsonb | ✗ | - |
| basic_info | jsonb | ✗ | - |
| company_files | jsonb | ✗ | - |
| expertise | jsonb | ✗ | - |
| fundraising | jsonb | ✗ | - |
| headline | character varying(220) | ✓ | - |
| investments | jsonb | ✗ | - |
| links | jsonb | ✗ | - |
| profile_cover | character varying(100) | ✓ | - |
| questions | jsonb | ✗ | - |
| revenues | jsonb | ✗ | - |
| visibility_settings | jsonb | ✗ | - |
| product_link | character varying(200) | ✓ | - |
| profile_cover_selected | character varying | ✓ | - |
| popularity_score | integer | ✓ | - |
| profile_score | integer | ✓ | - |
| upcoming_events_count | integer | ✓ | - |
| vacancies_count | integer | ✓ | - |
| data | jsonb | ✗ | - |
| customers_market | jsonb | ✗ | - |
| product_market | jsonb | ✗ | - |
| team | jsonb | ✗ | - |

**Связи (Foreign Keys):**
- `author_id` → `account_user.id`

---

### account_complaint

**Записей в таблице:** 20

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | nextval('account_complaint_id_seq'::regclass) |
| created_at | timestamp with time zone | ✗ | - |
| updated_at | timestamp with time zone | ✗ | - |
| reason | character varying(100) | ✗ | - |
| comment | character varying(500) | ✗ | - |
| author_id | integer | ✗ | - |
| company_id | integer | ✓ | - |
| user_id | integer | ✓ | - |
| viewed | ARRAY | ✗ | - |

**Связи (Foreign Keys):**
- `author_id` → `account_user.id`
- `company_id` → `account_company.id`
- `user_id` → `account_user.id`

---

### account_contactpress

**Записей в таблице:** 0

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | nextval('account_contactpress_id_seq'::regclass) |
| created_at | timestamp with time zone | ✗ | - |
| updated_at | timestamp with time zone | ✗ | - |
| author_id | integer | ✗ | - |
| company_id | integer | ✓ | - |
| user_id | integer | ✓ | - |

**Связи (Foreign Keys):**
- `author_id` → `account_user.id`
- `company_id` → `account_company.id`
- `user_id` → `account_user.id`

---

### account_contactrequest

**Записей в таблице:** 0

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | nextval('account_contactrequest_id_seq'::regclass) |
| created_at | timestamp with time zone | ✗ | - |
| updated_at | timestamp with time zone | ✗ | - |
| first_name | character varying(200) | ✗ | - |
| last_name | character varying(200) | ✗ | - |
| email | character varying(200) | ✗ | - |
| description | text | ✗ | - |
| user_id | integer | ✗ | - |
| phone | character varying(200) | ✗ | - |
| author_id | integer | ✓ | - |

**Связи (Foreign Keys):**
- `author_id` → `account_user.id`
- `user_id` → `account_user.id`

---

### account_course

**Записей в таблице:** 1

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | - |
| created_at | timestamp with time zone | ✗ | - |
| updated_at | timestamp with time zone | ✗ | - |
| name | character varying(255) | ✗ | - |
| top_skills | ARRAY | ✗ | - |
| graduation_date | date | ✗ | - |
| user_id | integer | ✗ | - |

**Связи (Foreign Keys):**
- `user_id` → `account_user.id`

---

### account_education

**Записей в таблице:** 1

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | - |
| created_at | timestamp with time zone | ✗ | - |
| updated_at | timestamp with time zone | ✗ | - |
| name | character varying(255) | ✗ | - |
| degree | character varying(50) | ✗ | - |
| graduation_year | integer | ✗ | - |
| faculty | character varying(255) | ✗ | - |
| user_id | integer | ✗ | - |

**Связи (Foreign Keys):**
- `user_id` → `account_user.id`

---

### account_emaildigest

**Записей в таблице:** 31474

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | nextval('account_emaildigest_id_seq'::regclass) |
| created_at | timestamp with time zone | ✗ | - |
| updated_at | timestamp with time zone | ✗ | - |
| email | character varying(200) | ✗ | - |
| name | character varying(200) | ✓ | - |

---

### account_experience

**Записей в таблице:** 0

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | - |
| created_at | timestamp with time zone | ✗ | - |
| updated_at | timestamp with time zone | ✗ | - |
| name | character varying(255) | ✗ | - |
| position | character varying(255) | ✗ | - |
| description | text | ✗ | - |
| start_date | date | ✗ | - |
| current_workplace | boolean | ✗ | - |
| end_date | date | ✓ | - |
| company_id | integer | ✓ | - |
| user_id | integer | ✗ | - |

**Связи (Foreign Keys):**
- `company_id` → `account_company.id`
- `user_id` → `account_user.id`

---

### account_user

**Записей в таблице:** 54062

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | nextval('account_user_id_seq'::regclass) |
| password | character varying(128) | ✗ | - |
| last_login | timestamp with time zone | ✓ | - |
| is_superuser | boolean | ✗ | - |
| created_at | timestamp with time zone | ✗ | - |
| updated_at | timestamp with time zone | ✗ | - |
| iin | character varying(100) | ✓ | - |
| email | character varying(400) | ✓ | - |
| phone | character varying(100) | ✗ | - |
| first_name | character varying(400) | ✗ | - |
| last_name | character varying(400) | ✗ | - |
| role | character varying(50) | ✗ | - |
| is_staff | boolean | ✗ | - |
| is_active | boolean | ✗ | - |
| company_id | integer | ✓ | - |
| organization_id | character varying(20) | ✓ | - |
| arm_permissions | jsonb | ✗ | - |
| tags | jsonb | ✗ | - |
| permissions | jsonb | ✗ | - |
| search_field | text | ✗ | - |
| tag_investor | jsonb | ✗ | - |
| data | jsonb | ✗ | - |
| tag_it_specialist | jsonb | ✗ | - |
| facebook_url | character varying(1000) | ✗ | - |
| linkedin_url | character varying(1000) | ✗ | - |
| website | character varying(1000) | ✗ | - |
| tag_intern | jsonb | ✗ | - |
| certificates | jsonb | ✗ | - |
| universities | jsonb | ✗ | - |
| image_id | uuid | ✓ | - |
| tag_international_agent | jsonb | ✗ | - |
| hook_services | ARRAY | ✗ | - |
| contact_email | character varying(400) | ✓ | - |
| blocked | boolean | ✗ | - |
| email_verified | boolean | ✗ | - |
| phone_verified | boolean | ✗ | - |
| tag_expert | jsonb | ✗ | - |
| games_blacklist | boolean | ✗ | - |
| tag_community_manager | jsonb | ✗ | - |
| tag_company_member | jsonb | ✗ | - |
| tag_startup_member | jsonb | ✗ | - |
| tag_tracker | jsonb | ✗ | - |
| games_data | jsonb | ✗ | - |
| tag_ai_specialist | jsonb | ✗ | - |
| tag_schoolchild | jsonb | ✗ | - |
| tag_student | jsonb | ✗ | - |
| tag_teacher | jsonb | ✗ | - |
| tag_scientist | jsonb | ✗ | - |
| egov_sign_data | jsonb | ✗ | - |
| birth_date | date | ✓ | - |
| city | character varying(128) | ✗ | - |
| country | character varying(128) | ✗ | - |
| gender | character varying(50) | ✗ | - |
| region | character varying(128) | ✗ | - |
| work_experience | jsonb | ✗ | - |
| contact_phone | character varying(100) | ✓ | - |
| headline | character varying(220) | ✓ | - |
| links | jsonb | ✗ | - |
| preferences | jsonb | ✗ | - |
| profile_cover | character varying(100) | ✓ | - |
| skills | jsonb | ✗ | - |
| visibility_settings | jsonb | ✗ | - |
| portfolio_url | character varying(1000) | ✗ | - |
| community_role | character varying(30) | ✓ | - |
| profile_cover_selected | character varying | ✓ | - |
| specific_role | character varying(30) | ✓ | - |
| popularity_score | integer | ✓ | - |
| profile_score | integer | ✓ | - |
| privacy_policy_accepted | boolean | ✗ | - |
| signup_flow_completed | boolean | ✗ | - |
| onboarding_data | jsonb | ✗ | - |

**Связи (Foreign Keys):**
- `company_id` → `account_company.id`
- `organization_id` → `core_organization.code`

---

### account_user_groups

**Записей в таблице:** 109

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | nextval('account_user_groups_id_seq'::regclass) |
| user_id | integer | ✗ | - |
| group_id | integer | ✗ | - |

**Связи (Foreign Keys):**
- `group_id` → `auth_group.id`
- `user_id` → `account_user.id`

---

### account_user_user_permissions

**Записей в таблице:** 2289

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | nextval('account_user_user_permissions_id_seq'::re... |
| user_id | integer | ✗ | - |
| permission_id | integer | ✗ | - |

**Связи (Foreign Keys):**
- `permission_id` → `auth_permission.id`
- `user_id` → `account_user.id`

---

### account_usercompany

**Записей в таблице:** 4536

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | nextval('account_usercompany_id_seq'::regclass) |
| company_id | integer | ✗ | - |
| user_id | integer | ✗ | - |
| verified | boolean | ✗ | - |
| role | character varying(20) | ✗ | - |

**Связи (Foreign Keys):**
- `company_id` → `account_company.id`
- `user_id` → `account_user.id`

---

### account_usercompanyinvitation

**Записей в таблице:** 2

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | - |
| created_at | timestamp with time zone | ✗ | - |
| updated_at | timestamp with time zone | ✗ | - |
| role | character varying(20) | ✗ | - |
| status | character varying(20) | ✗ | - |
| company_id | integer | ✗ | - |
| author_id | integer | ✗ | - |
| invited_user_id | integer | ✗ | - |

**Связи (Foreign Keys):**
- `author_id` → `account_user.id`
- `company_id` → `account_company.id`
- `invited_user_id` → `account_user.id`

---

### account_usercompanyrequest

**Записей в таблице:** 254

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | nextval('account_usercompanyrequest_id_seq'::regcl... |
| status | character varying(20) | ✗ | - |
| company_id | integer | ✗ | - |
| user_id | integer | ✗ | - |
| created_at | timestamp with time zone | ✗ | - |
| updated_at | timestamp with time zone | ✗ | - |

**Связи (Foreign Keys):**
- `company_id` → `account_company.id`
- `user_id` → `account_user.id`

---

### admin_honeypot_loginattempt

**Записей в таблице:** 69000

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | nextval('admin_honeypot_loginattempt_id_seq'::regc... |
| username | character varying(255) | ✓ | - |
| ip_address | inet | ✓ | - |
| session_key | character varying(50) | ✓ | - |
| user_agent | text | ✓ | - |
| timestamp | timestamp with time zone | ✗ | - |
| path | text | ✓ | - |

---

### astanahub_shared_contextdata

**Записей в таблице:** 0

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| created_at | timestamp with time zone | ✗ | - |
| updated_at | timestamp with time zone | ✗ | - |
| key | character varying(30) | ✗ | - |
| data | jsonb | ✗ | - |
| description | character varying(200) | ✗ | - |

---

### astanahub_shared_seodata

**Записей в таблице:** 0

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| created_at | timestamp with time zone | ✗ | - |
| updated_at | timestamp with time zone | ✗ | - |
| key | character varying(30) | ✗ | - |
| title | jsonb | ✗ | - |
| description | jsonb | ✗ | - |
| keywords | jsonb | ✗ | - |

---

### astanahub_shared_smslog

**Записей в таблице:** 651

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | bigint | ✗ | - |
| created_at | timestamp with time zone | ✗ | - |
| updated_at | timestamp with time zone | ✗ | - |
| phone | character varying(100) | ✗ | - |
| request | text | ✗ | - |
| response | text | ✗ | - |

---

### auth_group

**Записей в таблице:** 11

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | nextval('auth_group_id_seq'::regclass) |
| name | character varying(150) | ✗ | - |

---

### auth_group_permissions

**Записей в таблице:** 1114

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | nextval('auth_group_permissions_id_seq'::regclass) |
| group_id | integer | ✗ | - |
| permission_id | integer | ✗ | - |

**Связи (Foreign Keys):**
- `group_id` → `auth_group.id`
- `permission_id` → `auth_permission.id`

---

### auth_permission

**Записей в таблице:** 625

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | nextval('auth_permission_id_seq'::regclass) |
| name | character varying(255) | ✗ | - |
| content_type_id | integer | ✗ | - |
| codename | character varying(100) | ✗ | - |

**Связи (Foreign Keys):**
- `content_type_id` → `django_content_type.id`

---

### authtoken_token

**Записей в таблице:** 1138

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| key | character varying(40) | ✗ | - |
| created | timestamp with time zone | ✗ | - |
| user_id | integer | ✗ | - |

**Связи (Foreign Keys):**
- `user_id` → `account_user.id`

---

### awsdjangoses_awsblacklist

**Записей в таблице:** 200

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| email | character varying(500) | ✗ | - |
| bounce | boolean | ✗ | - |
| complaint | boolean | ✗ | - |

---

### booking_booking

**Записей в таблице:** 8673

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | nextval('booking_booking_id_seq'::regclass) |
| created_at | timestamp with time zone | ✗ | - |
| updated_at | timestamp with time zone | ✗ | - |
| status | character varying(20) | ✗ | - |
| full_name | character varying(200) | ✗ | - |
| email | character varying(200) | ✗ | - |
| phone | character varying(30) | ✗ | - |
| company_name_old | character varying(200) | ✗ | - |
| title | character varying(100) | ✗ | - |
| start | timestamp with time zone | ✗ | - |
| end | timestamp with time zone | ✗ | - |
| author_id | integer | ✗ | - |
| room_id | integer | ✗ | - |
| data | jsonb | ✗ | - |
| company_id | integer | ✓ | - |

**Связи (Foreign Keys):**
- `author_id` → `account_user.id`
- `company_id` → `account_company.id`
- `room_id` → `booking_room.id`

---

### booking_bookingstatus

**Записей в таблице:** 8691

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | nextval('booking_bookingstatus_id_seq'::regclass) |
| created_at | timestamp with time zone | ✗ | - |
| updated_at | timestamp with time zone | ✗ | - |
| status | character varying(20) | ✗ | - |
| comment | character varying(200) | ✗ | - |
| data | jsonb | ✗ | - |
| booking_id | integer | ✗ | - |
| start | timestamp with time zone | ✓ | - |

**Связи (Foreign Keys):**
- `booking_id` → `booking_booking.id`

---

### booking_room

**Записей в таблице:** 16

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | nextval('booking_room_id_seq'::regclass) |
| created_at | timestamp with time zone | ✗ | - |
| updated_at | timestamp with time zone | ✗ | - |
| name | character varying(50) | ✗ | - |
| floor | smallint | ✗ | - |
| max_people | smallint | ✗ | - |
| external_id | character varying(200) | ✗ | - |
| data | jsonb | ✗ | - |
| image_id | uuid | ✓ | - |
| pavilion | character varying(10) | ✓ | - |
| is_active | boolean | ✗ | - |

---

### community_companyfollow

**Записей в таблице:** 3

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | - |
| created_at | timestamp with time zone | ✗ | - |
| updated_at | timestamp with time zone | ✗ | - |
| followed_id | integer | ✗ | - |
| follower_id | integer | ✗ | - |

**Связи (Foreign Keys):**
- `followed_id` → `account_company.id`
- `follower_id` → `account_user.id`

---

### community_userfollow

**Записей в таблице:** 18

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | - |
| created_at | timestamp with time zone | ✗ | - |
| updated_at | timestamp with time zone | ✗ | - |
| followed_id | integer | ✗ | - |
| follower_id | integer | ✗ | - |

**Связи (Foreign Keys):**
- `followed_id` → `account_user.id`
- `follower_id` → `account_user.id`

---

### core_actionlog

**Записей в таблице:** 124975

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | nextval('core_actionlog_id_seq'::regclass) |
| created_at | timestamp with time zone | ✗ | - |
| updated_at | timestamp with time zone | ✗ | - |
| data | jsonb | ✗ | - |
| action | character varying(50) | ✗ | - |
| log_type | character varying(50) | ✗ | - |
| primary_key | character varying(50) | ✓ | - |
| source | character varying(25) | ✗ | - |
| user_id | integer | ✓ | - |
| body | text | ✓ | - |
| headers | text | ✓ | - |
| query_params | text | ✓ | - |
| metadata | jsonb | ✗ | - |
| service | character varying(20) | ✗ | - |

**Связи (Foreign Keys):**
- `user_id` → `account_user.id`

---

### core_article

**Записей в таблице:** 83

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | nextval('core_article_id_seq'::regclass) |
| created_at | timestamp with time zone | ✗ | - |
| updated_at | timestamp with time zone | ✗ | - |
| status | character varying(20) | ✗ | - |
| title | jsonb | ✗ | - |
| subtitle | jsonb | ✗ | - |
| slug | character varying(250) | ✗ | - |
| content | jsonb | ✗ | - |
| tags | ARRAY | ✗ | - |
| featured | boolean | ✗ | - |
| published | boolean | ✗ | - |
| publish_date | timestamp with time zone | ✓ | - |
| search_field | text | ✗ | - |
| author_id | integer | ✗ | - |
| category_id | integer | ✓ | - |
| view_count | integer | ✗ | - |
| comment | character varying(1000) | ✗ | - |
| show_in_feed | boolean | ✗ | - |
| image_id | uuid | ✓ | - |
| favorite_users | ARRAY | ✗ | - |
| reaction_down_users | ARRAY | ✗ | - |
| reaction_up_users | ARRAY | ✗ | - |
| comments_count | integer | ✗ | - |

**Связи (Foreign Keys):**
- `author_id` → `account_user.id`
- `category_id` → `core_category.id`

---

### core_banner

**Записей в таблице:** 27

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | - |
| created_at | timestamp with time zone | ✗ | - |
| updated_at | timestamp with time zone | ✗ | - |
| name | character varying(50) | ✗ | - |
| data | jsonb | ✗ | - |
| active | boolean | ✗ | - |
| position | smallint | ✗ | - |
| template | character varying(100) | ✗ | - |
| type | smallint | ✗ | - |
| types | ARRAY | ✗ | - |

---

### core_blog

**Записей в таблице:** 1801

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | nextval('core_blog_id_seq'::regclass) |
| created_at | timestamp with time zone | ✗ | - |
| updated_at | timestamp with time zone | ✗ | - |
| liked_users | ARRAY | ✗ | - |
| status | character varying(20) | ✗ | - |
| title | jsonb | ✗ | - |
| subtitle | jsonb | ✗ | - |
| slug | character varying(250) | ✗ | - |
| content | jsonb | ✗ | - |
| tags | ARRAY | ✗ | - |
| featured | boolean | ✗ | - |
| published | boolean | ✗ | - |
| comment | character varying(1000) | ✗ | - |
| search_field | text | ✗ | - |
| author_id | integer | ✗ | - |
| category_id | integer | ✓ | - |
| view_count | integer | ✗ | - |
| reaction_down_users | ARRAY | ✗ | - |
| reaction_up_users | ARRAY | ✗ | - |
| show_in_feed | boolean | ✗ | - |
| publish_date | timestamp with time zone | ✓ | - |
| image_id | uuid | ✓ | - |
| cover | character varying(20) | ✗ | - |
| favorite_users | ARRAY | ✗ | - |
| tag | jsonb | ✗ | - |
| image_en_id | uuid | ✓ | - |
| image_kk_id | uuid | ✓ | - |
| image_ru_id | uuid | ✓ | - |
| youtube_link | jsonb | ✗ | - |
| main_language | character varying(3) | ✗ | - |
| translation_config | jsonb | ✗ | - |
| games_data | jsonb | ✗ | - |
| sent_to_moderation_at | timestamp with time zone | ✓ | - |
| company_id | integer | ✓ | - |
| engagement_rate | double precision | ✓ | - |
| comments_count | integer | ✗ | - |

**Связи (Foreign Keys):**
- `author_id` → `account_user.id`
- `category_id` → `core_category.id`
- `company_id` → `account_company.id`

---

### core_category

**Записей в таблице:** 14

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | nextval('core_category_id_seq'::regclass) |
| name | jsonb | ✗ | - |
| description | jsonb | ✗ | - |
| featured | boolean | ✗ | - |
| image_id | uuid | ✓ | - |
| position | smallint | ✗ | - |
| reaction_down_users | ARRAY | ✗ | - |
| reaction_up_users | ARRAY | ✗ | - |
| slug | character varying(250) | ✗ | - |
| background_id | uuid | ✓ | - |
| following_users | ARRAY | ✗ | - |
| is_active | boolean | ✗ | - |
| show_top_authors | boolean | ✗ | - |
| can_publish | boolean | ✗ | - |

**Связи (Foreign Keys):**
- `background_id` → `shared_mediafile.id`

---

### core_city

**Записей в таблице:** 16

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | nextval('core_city_id_seq'::regclass) |
| name | character varying(200) | ✗ | - |
| name_ru | character varying(200) | ✓ | - |
| name_kk | character varying(200) | ✓ | - |
| name_en | character varying(200) | ✓ | - |
| country_id | integer | ✗ | - |

**Связи (Foreign Keys):**
- `country_id` → `core_country.id`

---

### core_comment

**Записей в таблице:** 2585

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | nextval('core_comment_id_seq'::regclass) |
| created_at | timestamp with time zone | ✗ | - |
| updated_at | timestamp with time zone | ✗ | - |
| message | text | ✗ | - |
| source | character varying(50) | ✗ | - |
| primary_key | character varying(20) | ✗ | - |
| user_id | integer | ✗ | - |
| parent_id | integer | ✓ | - |
| reaction_down_users | ARRAY | ✗ | - |
| reaction_up_users | ARRAY | ✗ | - |
| status | character varying(20) | ✗ | - |
| viewed | ARRAY | ✗ | - |

**Связи (Foreign Keys):**
- `parent_id` → `core_comment.id`
- `user_id` → `account_user.id`

---

### core_country

**Записей в таблице:** 1

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | nextval('core_country_id_seq'::regclass) |
| name | character varying(200) | ✗ | - |
| name_ru | character varying(200) | ✓ | - |
| name_kk | character varying(200) | ✓ | - |
| name_en | character varying(200) | ✓ | - |

---

### core_discussion

**Записей в таблице:** 157

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | nextval('core_discussion_id_seq'::regclass) |
| created_at | timestamp with time zone | ✗ | - |
| updated_at | timestamp with time zone | ✗ | - |
| view_count | integer | ✗ | - |
| reaction_up_users | ARRAY | ✗ | - |
| reaction_down_users | ARRAY | ✗ | - |
| status | character varying(20) | ✗ | - |
| title | jsonb | ✗ | - |
| slug | character varying(250) | ✗ | - |
| content | jsonb | ✗ | - |
| tags | ARRAY | ✗ | - |
| featured | boolean | ✗ | - |
| published | boolean | ✗ | - |
| comment | character varying(1000) | ✗ | - |
| search_field | text | ✗ | - |
| author_id | integer | ✗ | - |
| category_id | integer | ✓ | - |
| signature | jsonb | ✗ | - |
| show_in_feed | boolean | ✗ | - |
| publication_policy_accepted | boolean | ✗ | - |
| publish_date | timestamp with time zone | ✓ | - |
| image_id | uuid | ✓ | - |
| files | ARRAY | ✗ | - |
| files_for | character varying(50) | ✗ | - |
| statuses | jsonb | ✗ | - |
| notification_data | jsonb | ✗ | - |
| favorite_users | ARRAY | ✗ | - |

**Связи (Foreign Keys):**
- `author_id` → `account_user.id`
- `category_id` → `core_category.id`

---

### core_discussionvote

**Записей в таблице:** 335

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | nextval('core_discussionvote_id_seq'::regclass) |
| created_at | timestamp with time zone | ✗ | - |
| updated_at | timestamp with time zone | ✗ | - |
| choice | character varying(20) | ✗ | - |
| signature | jsonb | ✗ | - |
| discussion_id | integer | ✗ | - |
| user_id | integer | ✗ | - |

**Связи (Foreign Keys):**
- `discussion_id` → `core_discussion.id`
- `user_id` → `account_user.id`

---

### core_elabsannouncement

**Записей в таблице:** 70

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | - |
| created_at | timestamp with time zone | ✗ | - |
| updated_at | timestamp with time zone | ✗ | - |
| status | character varying(20) | ✗ | - |
| product_name | text | ✗ | - |
| organizer_name | text | ✗ | - |
| organizer_bin | text | ✗ | - |
| organizer_address | text | ✗ | - |
| organizer_contacts | text | ✗ | - |
| organizer_email | text | ✗ | - |
| available_count | integer | ✗ | - |
| price | integer | ✓ | - |
| supply_place | text | ✗ | - |
| supply_date | date | ✓ | - |
| proposals_address | text | ✗ | - |
| proposals_end_date | date | ✓ | - |
| envelope_opening_date | date | ✓ | - |
| envelope_opening_address | text | ✗ | - |
| authorized_representative | text | ✗ | - |
| author_id | integer | ✗ | - |
| characteristics_id | uuid | ✓ | - |

**Связи (Foreign Keys):**
- `author_id` → `account_user.id`

---

### core_event

**Записей в таблице:** 1459

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | nextval('core_event_id_seq'::regclass) |
| created_at | timestamp with time zone | ✗ | - |
| updated_at | timestamp with time zone | ✗ | - |
| status | character varying(20) | ✗ | - |
| title | jsonb | ✗ | - |
| category | character varying(20) | ✓ | - |
| slug | character varying(250) | ✗ | - |
| content | jsonb | ✗ | - |
| datetime_start | timestamp with time zone | ✓ | - |
| datetime_end | timestamp with time zone | ✓ | - |
| event_format | character varying(20) | ✗ | - |
| event_type | character varying(20) | ✗ | - |
| hall | character varying(100) | ✓ | - |
| visitors_count | smallint | ✓ | - |
| conference_link | character varying(1000) | ✓ | - |
| contact_info | jsonb | ✗ | - |
| published | boolean | ✗ | - |
| available | boolean | ✗ | - |
| comment | character varying(1000) | ✗ | - |
| search_field | text | ✗ | - |
| author_id | integer | ✗ | - |
| organization_id | character varying(20) | ✓ | - |
| view_count | integer | ✗ | - |
| image_id | uuid | ✓ | - |
| event_form | character varying(20) | ✓ | - |
| city | character varying(200) | ✓ | - |
| country | character varying(200) | ✓ | - |
| form_link | character varying(1000) | ✓ | - |
| favorite_users | ARRAY | ✗ | - |
| show_in_feed | boolean | ✗ | - |
| event_for | character varying(100) | ✓ | - |
| address | character varying(150) | ✓ | - |
| company_id | integer | ✓ | - |
| event_location | character varying(100) | ✓ | - |
| latitude | numeric | ✓ | - |
| longitude | numeric | ✓ | - |
| online_link | character varying(1000) | ✓ | - |
| record_link | character varying(1000) | ✓ | - |
| games_data | jsonb | ✗ | - |
| featured | boolean | ✗ | - |
| scope | ARRAY | ✗ | - |

**Связи (Foreign Keys):**
- `author_id` → `account_user.id`
- `company_id` → `account_company.id`
- `organization_id` → `core_organization.code`

---

### core_eventparticipant

**Записей в таблице:** 864

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | nextval('core_eventparticipant_id_seq'::regclass) |
| created_at | timestamp with time zone | ✗ | - |
| updated_at | timestamp with time zone | ✗ | - |
| status | character varying(20) | ✗ | - |
| email | character varying(200) | ✓ | - |
| phone | character varying(200) | ✓ | - |
| full_name | character varying(200) | ✗ | - |
| qrcode | character varying(20) | ✗ | - |
| author_id | integer | ✗ | - |
| event_id | integer | ✗ | - |
| role | character varying(100) | ✓ | - |
| participated_at | timestamp with time zone | ✓ | - |

**Связи (Foreign Keys):**
- `author_id` → `account_user.id`
- `event_id` → `core_event.id`

---

### core_faq

**Записей в таблице:** 7

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| code | character varying(20) | ✗ | - |
| title | character varying(200) | ✗ | - |
| title_ru | character varying(200) | ✓ | - |
| title_kk | character varying(200) | ✓ | - |
| title_en | character varying(200) | ✓ | - |
| position | smallint | ✗ | - |
| created_at | timestamp with time zone | ✗ | - |
| updated_at | timestamp with time zone | ✗ | - |

---

### core_faqitem

**Записей в таблице:** 46

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | nextval('core_faqitem_id_seq'::regclass) |
| title | character varying(200) | ✗ | - |
| title_ru | character varying(200) | ✓ | - |
| title_kk | character varying(200) | ✓ | - |
| title_en | character varying(200) | ✓ | - |
| description | text | ✗ | - |
| description_ru | text | ✓ | - |
| description_kk | text | ✓ | - |
| description_en | text | ✓ | - |
| position | smallint | ✗ | - |
| faq_id | character varying(20) | ✗ | - |

**Связи (Foreign Keys):**
- `faq_id` → `core_faq.code`

---

### core_feed

**Записей в таблице:** 4789

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | nextval('core_feed_id_seq'::regclass) |
| created_at | timestamp with time zone | ✗ | - |
| updated_at | timestamp with time zone | ✗ | - |
| source | character varying(50) | ✗ | - |
| primary_key | character varying(20) | ✗ | - |
| published | boolean | ✗ | - |
| published_at | timestamp with time zone | ✗ | - |
| featured | boolean | ✗ | - |
| article_id | integer | ✓ | - |
| blog_id | integer | ✓ | - |
| discussion_id | integer | ✓ | - |
| tags | ARRAY | ✗ | - |
| show_in_feed | boolean | ✗ | - |
| tech_task_id | integer | ✓ | - |
| event_id | integer | ✓ | - |
| vacancy_id | integer | ✓ | - |

**Связи (Foreign Keys):**
- `article_id` → `core_article.id`
- `blog_id` → `core_blog.id`
- `discussion_id` → `core_discussion.id`
- `event_id` → `core_event.id`
- `tech_task_id` → `core_techtask.id`
- `vacancy_id` → `core_vacancy.id`

---

### core_floordata

**Записей в таблице:** 16

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | nextval('core_floordata_id_seq'::regclass) |
| created_at | timestamp with time zone | ✗ | - |
| updated_at | timestamp with time zone | ✗ | - |
| pavilion | character varying(10) | ✗ | - |
| floor | integer | ✗ | - |
| data | jsonb | ✗ | - |
| is_active | boolean | ✗ | - |
| template | character varying(100) | ✗ | - |

---

### core_infrastructure

**Записей в таблице:** 504

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | - |
| created_at | timestamp with time zone | ✗ | - |
| updated_at | timestamp with time zone | ✗ | - |
| favorite_users | ARRAY | ✗ | - |
| name | jsonb | ✗ | - |
| active | boolean | ✗ | - |
| type | character varying(100) | ✓ | - |
| subtype | character varying(100) | ✓ | - |
| kind | character varying(100) | ✓ | - |
| price | numeric | ✓ | - |
| unit | character varying(100) | ✓ | - |
| phone | character varying(20) | ✓ | - |
| email | character varying(100) | ✓ | - |
| city | character varying(100) | ✓ | - |
| data | jsonb | ✗ | - |
| author_id | integer | ✗ | - |
| organization_id | character varying(20) | ✓ | - |
| parent_id | integer | ✓ | - |
| status | character varying(20) | ✗ | - |
| categories | ARRAY | ✗ | - |
| company_id | integer | ✓ | - |
| scope | character varying(100) | ✓ | - |
| comment | character varying(1000) | ✗ | - |
| view_count | integer | ✗ | - |
| signature | jsonb | ✗ | - |
| search_field | text | ✗ | - |
| priority | smallint | ✓ | - |
| accreditation | text | ✓ | - |
| employees_number | integer | ✓ | - |
| equipment_percentage | integer | ✓ | - |
| job_title_1 | character varying(200) | ✓ | - |
| job_title_2 | character varying(200) | ✓ | - |
| job_title_3 | character varying(200) | ✓ | - |
| job_title_4 | character varying(200) | ✓ | - |
| head | character varying(200) | ✓ | - |
| license | text | ✓ | - |
| other_documentation | text | ✓ | - |
| regime_commission_permission | text | ✓ | - |
| total_number | integer | ✓ | - |
| equipment_data | jsonb | ✗ | - |

**Связи (Foreign Keys):**
- `author_id` → `account_user.id`
- `company_id` → `account_company.id`
- `organization_id` → `core_organization.code`
- `parent_id` → `core_infrastructure.id`

---

### core_infrastructureimage

**Записей в таблице:** 397

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | - |
| created_at | timestamp with time zone | ✗ | - |
| updated_at | timestamp with time zone | ✗ | - |
| image | character varying(100) | ✗ | - |
| primary | boolean | ✗ | - |
| author_id | integer | ✗ | - |
| infrastructure_id | integer | ✗ | - |

**Связи (Foreign Keys):**
- `author_id` → `account_user.id`
- `infrastructure_id` → `core_infrastructure.id`

---

### core_infrastructurerequest

**Записей в таблице:** 37

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | - |
| created_at | timestamp with time zone | ✗ | - |
| updated_at | timestamp with time zone | ✗ | - |
| phone | character varying(30) | ✗ | - |
| contact_name | character varying(100) | ✗ | - |
| comment | character varying(1000) | ✗ | - |
| response_comment | character varying(1000) | ✗ | - |
| status | character varying(20) | ✗ | - |
| author_id | integer | ✗ | - |
| infrastructure_id | integer | ✗ | - |

**Связи (Foreign Keys):**
- `author_id` → `account_user.id`
- `infrastructure_id` → `core_infrastructure.id`

---

### core_notification

**Записей в таблице:** 1233

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | nextval('core_notification_id_seq'::regclass) |
| created_at | timestamp with time zone | ✗ | - |
| updated_at | timestamp with time zone | ✗ | - |
| title | jsonb | ✗ | - |
| description | jsonb | ✗ | - |
| user_id | integer | ✗ | - |
| url | character varying(1000) | ✗ | - |
| is_read | boolean | ✗ | - |

**Связи (Foreign Keys):**
- `user_id` → `account_user.id`

---

### core_organization

**Записей в таблице:** 45

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| created_at | timestamp with time zone | ✗ | - |
| updated_at | timestamp with time zone | ✗ | - |
| code | character varying(20) | ✗ | - |
| logo | character varying(100) | ✓ | - |
| data | jsonb | ✗ | - |
| active | boolean | ✗ | - |
| name | jsonb | ✗ | - |

---

### core_techtask

**Записей в таблице:** 247

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | nextval('core_techtask_id_seq'::regclass) |
| created_at | timestamp with time zone | ✗ | - |
| updated_at | timestamp with time zone | ✗ | - |
| status | character varying(20) | ✗ | - |
| show_in_feed | boolean | ✗ | - |
| title | jsonb | ✗ | - |
| description | jsonb | ✗ | - |
| problem_description | jsonb | ✗ | - |
| product_type_software | boolean | ✗ | - |
| product_type_mobile | boolean | ✗ | - |
| product_type_other | boolean | ✗ | - |
| other_product_type | jsonb | ✗ | - |
| effect | jsonb | ✗ | - |
| development_country | character varying(10) | ✗ | - |
| product_status | character varying(10) | ✗ | - |
| other_status | jsonb | ✗ | - |
| reward | jsonb | ✗ | - |
| contact_name | jsonb | ✗ | - |
| phone | character varying(30) | ✗ | - |
| notes | jsonb | ✗ | - |
| tags | ARRAY | ✗ | - |
| featured | boolean | ✗ | - |
| published | boolean | ✗ | - |
| publish_date | timestamp with time zone | ✓ | - |
| comment | character varying(1000) | ✗ | - |
| search_field | text | ✗ | - |
| slug | character varying(250) | ✗ | - |
| author_id | integer | ✗ | - |
| specification_id | uuid | ✓ | - |
| view_count | integer | ✗ | - |
| deadline | timestamp with time zone | ✓ | - |
| notification_data | jsonb | ✗ | - |
| favorite_users | ARRAY | ✗ | - |
| company_name | character varying(200) | ✗ | - |
| amount | integer | ✓ | - |
| task_area | character varying(500) | ✗ | - |
| scope | character varying(1000) | ✗ | - |
| application_type | character varying(20) | ✓ | - |
| games_data | jsonb | ✗ | - |
| priority | smallint | ✓ | - |
| extra_data | jsonb | ✗ | - |

**Связи (Foreign Keys):**
- `author_id` → `account_user.id`

---

### core_techtasksolution

**Записей в таблице:** 232

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | nextval('core_techtasksolution_id_seq'::regclass) |
| created_at | timestamp with time zone | ✗ | - |
| updated_at | timestamp with time zone | ✗ | - |
| company_name | jsonb | ✗ | - |
| company_tin | character varying(12) | ✗ | - |
| website | character varying(1000) | ✗ | - |
| phone | character varying(30) | ✗ | - |
| contact_name | jsonb | ✗ | - |
| launch_date | date | ✗ | - |
| notes | jsonb | ✗ | - |
| author_id | integer | ✗ | - |
| product_presentation_id | uuid | ✓ | - |
| tech_task_id | integer | ✗ | - |
| status | character varying(20) | ✗ | - |
| product_status | character varying(20) | ✗ | - |
| comment | character varying(1000) | ✗ | - |

**Связи (Foreign Keys):**
- `author_id` → `account_user.id`
- `tech_task_id` → `core_techtask.id`

---

### core_vacancy

**Записей в таблице:** 1205

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | nextval('core_vacancy_id_seq'::regclass) |
| created_at | timestamp with time zone | ✗ | - |
| updated_at | timestamp with time zone | ✗ | - |
| status | character varying(20) | ✗ | - |
| title | jsonb | ✗ | - |
| vacancy_type | character varying(20) | ✓ | - |
| salary_min | integer | ✓ | - |
| salary_max | integer | ✓ | - |
| place | character varying(20) | ✓ | - |
| description | jsonb | ✗ | - |
| email | character varying(254) | ✗ | - |
| published | boolean | ✗ | - |
| comment | character varying(1000) | ✗ | - |
| author_id | integer | ✗ | - |
| city_id | integer | ✓ | - |
| view_count | integer | ✗ | - |
| short_description | jsonb | ✗ | - |
| company_id | integer | ✓ | - |
| specializations | ARRAY | ✗ | - |
| favorite_users | ARRAY | ✗ | - |
| show_in_feed | boolean | ✗ | - |
| search_field | text | ✗ | - |
| games_data | jsonb | ✗ | - |
| direction | character varying | ✓ | - |
| education | character varying | ✗ | - |
| experience | character varying | ✓ | - |
| opened | boolean | ✗ | - |
| additional_place | ARRAY | ✗ | - |
| region | character varying(50) | ✓ | - |
| published_at | timestamp with time zone | ✓ | - |

**Связи (Foreign Keys):**
- `author_id` → `account_user.id`
- `city_id` → `core_city.id`
- `company_id` → `account_company.id`

---

### core_vacancycandidate

**Записей в таблице:** 5344

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | nextval('core_vacancycandidate_id_seq'::regclass) |
| created_at | timestamp with time zone | ✗ | - |
| updated_at | timestamp with time zone | ✗ | - |
| status | character varying(20) | ✗ | - |
| email | character varying(200) | ✗ | - |
| phone | character varying(200) | ✗ | - |
| full_name | character varying(200) | ✗ | - |
| linkedin | character varying(500) | ✗ | - |
| description | text | ✗ | - |
| author_id | integer | ✗ | - |
| vacancy_id | integer | ✗ | - |
| cv_id | uuid | ✓ | - |
| portfolio_url | character varying(500) | ✓ | - |
| candidate_status | character varying(30) | ✗ | - |
| offer_file_id | uuid | ✓ | - |
| offer_text | text | ✓ | - |
| reject_reason_recruiter | text | ✓ | - |
| reject_reason_seeker | text | ✓ | - |
| work_experience | character varying(1000) | ✓ | - |

**Связи (Foreign Keys):**
- `author_id` → `account_user.id`
- `vacancy_id` → `core_vacancy.id`

---

### core_vacancycandidate_certificates

**Записей в таблице:** 192

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | - |
| vacancycandidate_id | integer | ✗ | - |
| mediafile_id | uuid | ✗ | - |

---

### django_admin_log

**Записей в таблице:** 42696

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | nextval('django_admin_log_id_seq'::regclass) |
| action_time | timestamp with time zone | ✗ | - |
| object_id | text | ✓ | - |
| object_repr | character varying(200) | ✗ | - |
| action_flag | smallint | ✗ | - |
| change_message | text | ✗ | - |
| content_type_id | integer | ✓ | - |
| user_id | integer | ✗ | - |

**Связи (Foreign Keys):**
- `content_type_id` → `django_content_type.id`
- `user_id` → `account_user.id`

---

### django_content_type

**Записей в таблице:** 155

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | nextval('django_content_type_id_seq'::regclass) |
| app_label | character varying(100) | ✗ | - |
| model | character varying(100) | ✗ | - |

---

### django_dramatiq_task

**Записей в таблице:** 0

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | uuid | ✗ | - |
| status | character varying(8) | ✗ | - |
| created_at | timestamp with time zone | ✗ | - |
| updated_at | timestamp with time zone | ✗ | - |
| message_data | bytea | ✗ | - |
| actor_name | character varying(300) | ✓ | - |
| queue_name | character varying(100) | ✓ | - |

---

### django_migrations

**Записей в таблице:** 819

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | nextval('django_migrations_id_seq'::regclass) |
| app | character varying(255) | ✗ | - |
| name | character varying(255) | ✗ | - |
| applied | timestamp with time zone | ✗ | - |

---

### django_session

**Записей в таблице:** 0

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| session_key | character varying(40) | ✗ | - |
| session_data | text | ✗ | - |
| expire_date | timestamp with time zone | ✗ | - |

---

### explorer_query

**Записей в таблице:** 6

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | - |
| title | character varying(255) | ✗ | - |
| sql | text | ✗ | - |
| description | text | ✗ | - |
| created_at | timestamp with time zone | ✗ | - |
| last_run_date | timestamp with time zone | ✗ | - |
| created_by_user_id | integer | ✓ | - |
| snapshot | boolean | ✗ | - |
| connection | character varying(128) | ✗ | - |

**Связи (Foreign Keys):**
- `created_by_user_id` → `account_user.id`

---

### explorer_queryfavorite

**Записей в таблице:** 0

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | - |
| query_id | integer | ✗ | - |
| user_id | integer | ✗ | - |

**Связи (Foreign Keys):**
- `query_id` → `explorer_query.id`
- `user_id` → `account_user.id`

---

### explorer_querylog

**Записей в таблице:** 1129

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | - |
| sql | text | ✗ | - |
| run_at | timestamp with time zone | ✗ | - |
| query_id | integer | ✓ | - |
| run_by_user_id | integer | ✓ | - |
| duration | double precision | ✓ | - |
| connection | character varying(128) | ✗ | - |
| error | text | ✓ | - |
| success | boolean | ✗ | - |

**Связи (Foreign Keys):**
- `query_id` → `explorer_query.id`
- `run_by_user_id` → `account_user.id`

---

### hub_cache_table

**Записей в таблице:** 63

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| cache_key | character varying(255) | ✗ | - |
| value | text | ✗ | - |
| expires | timestamp with time zone | ✗ | - |

---

### journeymap_companystate

**Записей в таблице:** 0

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | bigint | ✗ | - |
| created_at | timestamp with time zone | ✗ | - |
| updated_at | timestamp with time zone | ✗ | - |
| step_data | jsonb | ✗ | - |
| company_id | integer | ✗ | - |
| journeymap_id | character varying(50) | ✗ | - |
| task_data | jsonb | ✗ | - |
| journeymap_data | jsonb | ✗ | - |

**Связи (Foreign Keys):**
- `company_id` → `account_company.id`
- `journeymap_id` → `journeymap_journeymap.key`

---

### journeymap_journeymap

**Записей в таблице:** 0

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| created_at | timestamp with time zone | ✗ | - |
| updated_at | timestamp with time zone | ✗ | - |
| key | character varying(50) | ✗ | - |
| name | character varying(100) | ✗ | - |
| config | jsonb | ✗ | - |

---

### journeymap_question

**Записей в таблице:** 0

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | bigint | ✗ | - |
| created_at | timestamp with time zone | ✗ | - |
| updated_at | timestamp with time zone | ✗ | - |
| type | character varying(40) | ✗ | - |
| name | character varying(100) | ✗ | - |
| title | jsonb | ✗ | - |
| config | jsonb | ✗ | - |
| position | smallint | ✗ | - |
| task_id | bigint | ✗ | - |
| key | character varying(100) | ✗ | - |
| company_experience_points | integer | ✗ | - |
| experience_points | integer | ✗ | - |
| social_coins | integer | ✗ | - |
| st | integer | ✗ | - |
| condition | character varying(200) | ✗ | - |
| can_skip | boolean | ✗ | - |

**Связи (Foreign Keys):**
- `task_id` → `journeymap_task.id`

---

### journeymap_step

**Записей в таблице:** 0

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | bigint | ✗ | - |
| created_at | timestamp with time zone | ✗ | - |
| updated_at | timestamp with time zone | ✗ | - |
| name | character varying(100) | ✗ | - |
| title | jsonb | ✗ | - |
| config | jsonb | ✗ | - |
| position | smallint | ✗ | - |
| type | character varying(20) | ✗ | - |
| journeymap_id | character varying(50) | ✗ | - |

**Связи (Foreign Keys):**
- `journeymap_id` → `journeymap_journeymap.key`

---

### journeymap_step_next_steps

**Записей в таблице:** 0

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | - |
| from_step_id | bigint | ✗ | - |
| to_step_id | bigint | ✗ | - |

**Связи (Foreign Keys):**
- `from_step_id` → `journeymap_step.id`
- `to_step_id` → `journeymap_step.id`

---

### journeymap_task

**Записей в таблице:** 0

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | bigint | ✗ | - |
| created_at | timestamp with time zone | ✗ | - |
| updated_at | timestamp with time zone | ✗ | - |
| name | character varying(100) | ✗ | - |
| title | jsonb | ✗ | - |
| position | smallint | ✗ | - |
| config | jsonb | ✗ | - |
| type | character varying(20) | ✗ | - |
| event_code | character varying(100) | ✗ | - |
| completion_code | text | ✗ | - |
| step_id | bigint | ✗ | - |

**Связи (Foreign Keys):**
- `step_id` → `journeymap_step.id`

---

### journeymap_userstate

**Записей в таблице:** 0

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | bigint | ✗ | - |
| created_at | timestamp with time zone | ✗ | - |
| updated_at | timestamp with time zone | ✗ | - |
| step_data | jsonb | ✗ | - |
| journeymap_id | character varying(50) | ✗ | - |
| user_id | integer | ✗ | - |
| task_data | jsonb | ✗ | - |
| journeymap_data | jsonb | ✗ | - |

**Связи (Foreign Keys):**
- `journeymap_id` → `journeymap_journeymap.key`
- `user_id` → `account_user.id`

---

### landing_component

**Записей в таблице:** 2790

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | nextval('landing_component_id_seq'::regclass) |
| created_at | timestamp with time zone | ✗ | - |
| updated_at | timestamp with time zone | ✗ | - |
| container_type | character varying(50) | ✗ | - |
| component_type | character varying(50) | ✗ | - |
| position | smallint | ✗ | - |
| data | jsonb | ✗ | - |
| section_id | integer | ✗ | - |

**Связи (Foreign Keys):**
- `section_id` → `landing_section.id`

---

### landing_landing

**Записей в таблице:** 8

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | nextval('landing_landing_id_seq'::regclass) |
| created_at | timestamp with time zone | ✗ | - |
| updated_at | timestamp with time zone | ✗ | - |
| name | jsonb | ✗ | - |
| endpoint | character varying(200) | ✗ | - |
| template | character varying(200) | ✗ | - |
| data | jsonb | ✗ | - |
| published | boolean | ✗ | - |
| show_crm_button | boolean | ✗ | - |
| extra_context | jsonb | ✗ | - |

---

### landing_page

**Записей в таблице:** 562

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | nextval('landing_page_id_seq'::regclass) |
| created_at | timestamp with time zone | ✗ | - |
| updated_at | timestamp with time zone | ✗ | - |
| name | character varying(200) | ✗ | - |
| endpoint | character varying(200) | ✗ | - |
| page_type | character varying(500) | ✗ | - |
| data | jsonb | ✗ | - |
| published | boolean | ✗ | - |
| publish_date | timestamp with time zone | ✓ | - |
| organization_id | character varying(20) | ✓ | - |
| view_count | integer | ✗ | - |
| show_crm_button | boolean | ✗ | - |
| extra_css | text | ✗ | - |
| extra_js | text | ✗ | - |
| author_id | integer | ✓ | - |
| authorization_required | boolean | ✗ | - |

**Связи (Foreign Keys):**
- `author_id` → `account_user.id`
- `organization_id` → `core_organization.code`

---

### landing_pagemediafile

**Записей в таблице:** 18517

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | nextval('landing_pagemediafile_id_seq'::regclass) |
| created_at | timestamp with time zone | ✗ | - |
| updated_at | timestamp with time zone | ✗ | - |
| file | character varying(100) | ✗ | - |
| thumbnail | character varying(100) | ✓ | - |
| mime_type | character varying(50) | ✗ | - |
| size | double precision | ✗ | - |
| page_id | integer | ✗ | - |
| thumbnail_150 | character varying(100) | ✓ | - |
| thumbnail_1500 | character varying(100) | ✓ | - |
| thumbnail_800 | character varying(100) | ✓ | - |
| author_id | integer | ✓ | - |

**Связи (Foreign Keys):**
- `author_id` → `account_user.id`
- `page_id` → `landing_page.id`

---

### landing_section

**Записей в таблице:** 560

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | nextval('landing_section_id_seq'::regclass) |
| created_at | timestamp with time zone | ✗ | - |
| updated_at | timestamp with time zone | ✗ | - |
| section_type | character varying(500) | ✗ | - |
| position | smallint | ✗ | - |
| data | jsonb | ✗ | - |
| page_id | integer | ✗ | - |

**Связи (Foreign Keys):**
- `page_id` → `landing_page.id`

---

### matchmaking_match

**Записей в таблице:** 31

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | - |
| created_at | timestamp with time zone | ✗ | - |
| updated_at | timestamp with time zone | ✗ | - |
| date | date | ✗ | - |
| user_a_id | integer | ✗ | - |
| user_b_id | integer | ✗ | - |

**Связи (Foreign Keys):**
- `user_a_id` → `account_user.id`
- `user_b_id` → `account_user.id`

---

### matchmaking_profile

**Записей в таблице:** 19

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | - |
| created_at | timestamp with time zone | ✗ | - |
| updated_at | timestamp with time zone | ✗ | - |
| activity | character varying(255) | ✗ | - |
| contact | character varying(255) | ✗ | - |
| data | jsonb | ✗ | - |
| user_id | integer | ✗ | - |
| is_active | boolean | ✗ | - |

**Связи (Foreign Keys):**
- `user_id` → `account_user.id`

---

### niokr_niokrnotification

**Записей в таблице:** 3

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | bigint | ✗ | - |
| text | text | ✗ | - |
| title | character varying(255) | ✗ | - |
| notification_type | character varying(30) | ✗ | - |
| data | jsonb | ✗ | - |
| unread | boolean | ✗ | - |

---

### niokr_niokrnotification_projects

**Записей в таблице:** 2

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | - |
| niokrnotification_id | bigint | ✗ | - |
| niokrproject_id | bigint | ✗ | - |

**Связи (Foreign Keys):**
- `niokrnotification_id` → `niokr_niokrnotification.id`
- `niokrproject_id` → `niokr_niokrproject.id`

---

### niokr_niokrproject

**Записей в таблице:** 1

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | bigint | ✗ | - |
| organization_bin | character varying(12) | ✓ | - |
| registered_in_state | boolean | ✗ | - |
| work_title | jsonb | ✓ | - |
| project_type | text | ✗ | - |
| status | character varying(300) | ✗ | - |
| state_registration_number | character varying(100) | ✗ | - |
| modified_registration_number | character varying(100) | ✓ | - |
| outgoing_number | character varying(100) | ✗ | - |
| outgoing_date | date | ✓ | - |
| start_date | date | ✓ | - |
| end_date | date | ✓ | - |
| program_code | character varying(50) | ✗ | - |
| task_code | character varying(50) | ✓ | - |
| work_basis | character varying(100) | ✗ | - |
| work_type | character varying(50) | ✗ | - |
| geofund_code | character varying(50) | ✓ | - |
| year | integer | ✓ | - |
| state_budget_funds | integer | ✓ | - |
| customer_funds | integer | ✓ | - |
| own_funds | integer | ✓ | - |
| international_grants | integer | ✓ | - |
| other_funds | integer | ✓ | - |
| goals | jsonb | ✓ | - |
| research_objects | jsonb | ✓ | - |
| application_areas | jsonb | ✓ | - |
| expected_results | jsonb | ✓ | - |
| ministry_name | character varying(200) | ✗ | - |
| organization_full_name | character varying(200) | ✗ | - |
| organization_short_name | character varying(200) | ✗ | - |
| phone | character varying(20) | ✗ | - |
| fax | text | ✓ | - |
| email | character varying(100) | ✗ | - |
| organization_location | character varying(200) | ✗ | - |
| coexecutor_name | character varying(200) | ✓ | - |
| coexecutor_location | text | ✓ | - |
| udc_indices | text | ✗ | - |
| code_number | character varying(50) | ✗ | - |
| code_description | character varying(200) | ✗ | - |
| keywords | jsonb | ✓ | - |
| project_leader | character varying(200) | ✓ | - |
| leader_fullname | character varying(200) | ✗ | - |
| leader_degree_title | character varying(200) | ✗ | - |
| organization_head | character varying(200) | ✗ | - |
| head_fullname | character varying(200) | ✗ | - |
| head_degree_title | character varying(200) | ✗ | - |
| scanned_cover_letter | text | ✗ | - |
| funding_document | text | ✗ | - |
| document_date | date | ✓ | - |
| irn | character varying(200) | ✓ | - |
| name | jsonb | ✓ | - |
| application_language | character varying(50) | ✗ | - |
| project_topic | jsonb | ✓ | - |
| report_status | character varying(200) | ✗ | - |
| submission_year | character varying | ✓ | - |
| implementation_period | character varying(200) | ✗ | - |
| customer | character varying(200) | ✗ | - |
| applicant | character varying(200) | ✗ | - |
| grantee | character varying(200) | ✓ | - |
| implementation_mechanism | text | ✓ | - |
| gnte_group | character varying(500) | ✗ | - |
| funding_type | character varying(100) | ✗ | - |
| gnte_object_type | character varying(100) | ✗ | - |
| research_type | character varying(100) | ✗ | - |
| report_type | character varying(100) | ✗ | - |
| creation_date | date | ✓ | - |
| priority_area | text | ✗ | - |
| specialized_area | text | ✗ | - |
| subject_area | text | ✗ | - |
| rubric_level_1 | text | ✗ | - |
| rubric_level_2 | text | ✗ | - |
| rubric_level_3 | text | ✗ | - |
| code | character varying(100) | ✗ | - |
| science_rubric_1 | text | ✗ | - |
| science_rubric_2 | text | ✗ | - |
| science_rubric_3 | text | ✗ | - |
| science_keywords | jsonb | ✓ | - |
| funding_volume | integer | ✓ | - |
| cofunding_organization | character varying(200) | ✗ | - |
| cofunding_amount | integer | ✓ | - |
| report | jsonb | ✗ | - |
| report_work_goal | jsonb | ✓ | - |
| report_research_methods | jsonb | ✓ | - |
| report_results_and_novelty | jsonb | ✓ | - |
| tech_economic_indicators | jsonb | ✓ | - |
| implementation_level | jsonb | ✓ | - |
| effectiveness | jsonb | ✓ | - |
| application_area | jsonb | ✓ | - |
| report_publications_form | text | ✗ | - |
| security_docs_info | text | ✗ | - |
| implementation_info | text | ✗ | - |
| comments | jsonb | ✗ | - |

---

### niokr_niokrprojectexecutor

**Записей в таблице:** 1

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | bigint | ✗ | - |
| created_at | timestamp with time zone | ✗ | - |
| updated_at | timestamp with time zone | ✗ | - |
| executor_type | character varying(50) | ✗ | - |
| official_name | character varying(512) | ✗ | - |
| short_name | character varying(255) | ✗ | - |
| executor_bin | character varying(12) | ✗ | - |
| head_full_name | character varying(255) | ✗ | - |
| region | character varying(100) | ✓ | - |
| city | character varying(100) | ✓ | - |
| address | character varying(255) | ✓ | - |
| postal_code | character varying(50) | ✓ | - |
| contact_info | character varying(50) | ✓ | - |
| email | character varying(254) | ✗ | - |
| legal_form | character varying(50) | ✗ | - |
| ministry | character varying(255) | ✗ | - |
| order_number | character varying(50) | ✗ | - |
| order_date | date | ✓ | - |
| organization_type | character varying(255) | ✗ | - |
| accredited | boolean | ✗ | - |
| accreditation_number | character varying(50) | ✓ | - |
| accreditation_date | date | ✓ | - |
| accreditation_certificate | character varying(500) | ✗ | - |
| registration_certificate | character varying(500) | ✗ | - |
| status | character varying(50) | ✗ | - |

---

### niokr_niokrprojectexecutor_projects

**Записей в таблице:** 1

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | - |
| niokrprojectexecutor_id | bigint | ✗ | - |
| niokrproject_id | bigint | ✗ | - |

**Связи (Foreign Keys):**
- `niokrproject_id` → `niokr_niokrproject.id`
- `niokrprojectexecutor_id` → `niokr_niokrprojectexecutor.id`

---

### oauth2_provider_accesstoken

**Записей в таблице:** 9

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | bigint | ✗ | nextval('oauth2_provider_accesstoken_id_seq'::regc... |
| token | text | ✗ | - |
| expires | timestamp with time zone | ✗ | - |
| scope | text | ✗ | - |
| application_id | bigint | ✓ | - |
| user_id | integer | ✓ | - |
| created | timestamp with time zone | ✗ | - |
| updated | timestamp with time zone | ✗ | - |
| source_refresh_token_id | bigint | ✓ | - |
| id_token_id | bigint | ✓ | - |
| token_checksum | character varying(64) | ✗ | - |

**Связи (Foreign Keys):**
- `application_id` → `oauth2_provider_application.id`
- `id_token_id` → `oauth2_provider_idtoken.id`
- `source_refresh_token_id` → `oauth2_provider_refreshtoken.id`
- `user_id` → `account_user.id`

---

### oauth2_provider_application

**Записей в таблице:** 8

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | bigint | ✗ | nextval('oauth2_provider_application_id_seq'::regc... |
| client_id | character varying(100) | ✗ | - |
| redirect_uris | text | ✗ | - |
| client_type | character varying(32) | ✗ | - |
| authorization_grant_type | character varying(32) | ✗ | - |
| client_secret | character varying(255) | ✗ | - |
| name | character varying(255) | ✗ | - |
| user_id | integer | ✓ | - |
| skip_authorization | boolean | ✗ | - |
| created | timestamp with time zone | ✗ | - |
| updated | timestamp with time zone | ✗ | - |
| algorithm | character varying(5) | ✗ | - |
| post_logout_redirect_uris | text | ✗ | - |
| hash_client_secret | boolean | ✗ | - |
| allowed_origins | text | ✗ | - |

**Связи (Foreign Keys):**
- `user_id` → `account_user.id`

---

### oauth2_provider_grant

**Записей в таблице:** 1037

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | bigint | ✗ | nextval('oauth2_provider_grant_id_seq'::regclass) |
| code | character varying(255) | ✗ | - |
| expires | timestamp with time zone | ✗ | - |
| redirect_uri | text | ✗ | - |
| scope | text | ✗ | - |
| application_id | bigint | ✗ | - |
| user_id | integer | ✗ | - |
| created | timestamp with time zone | ✗ | - |
| updated | timestamp with time zone | ✗ | - |
| code_challenge | character varying(128) | ✗ | - |
| code_challenge_method | character varying(10) | ✗ | - |
| nonce | character varying(255) | ✗ | - |
| claims | text | ✗ | - |

**Связи (Foreign Keys):**
- `application_id` → `oauth2_provider_application.id`
- `user_id` → `account_user.id`

---

### oauth2_provider_idtoken

**Записей в таблице:** 0

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | bigint | ✗ | nextval('oauth2_provider_idtoken_id_seq'::regclass... |
| jti | uuid | ✗ | - |
| expires | timestamp with time zone | ✗ | - |
| scope | text | ✗ | - |
| created | timestamp with time zone | ✗ | - |
| updated | timestamp with time zone | ✗ | - |
| application_id | bigint | ✓ | - |
| user_id | integer | ✓ | - |

**Связи (Foreign Keys):**
- `application_id` → `oauth2_provider_application.id`
- `user_id` → `account_user.id`

---

### oauth2_provider_refreshtoken

**Записей в таблице:** 0

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | bigint | ✗ | nextval('oauth2_provider_refreshtoken_id_seq'::reg... |
| token | character varying(255) | ✗ | - |
| access_token_id | bigint | ✓ | - |
| application_id | bigint | ✗ | - |
| user_id | integer | ✗ | - |
| created | timestamp with time zone | ✗ | - |
| updated | timestamp with time zone | ✗ | - |
| revoked | timestamp with time zone | ✓ | - |
| token_family | uuid | ✓ | - |

**Связи (Foreign Keys):**
- `access_token_id` → `oauth2_provider_accesstoken.id`
- `application_id` → `oauth2_provider_application.id`
- `user_id` → `account_user.id`

---

### reversion_revision

**Записей в таблице:** 19559

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | nextval('reversion_revision_id_seq'::regclass) |
| date_created | timestamp with time zone | ✗ | - |
| comment | text | ✗ | - |
| user_id | integer | ✓ | - |

**Связи (Foreign Keys):**
- `user_id` → `account_user.id`

---

### reversion_version

**Записей в таблице:** 9281

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | nextval('reversion_version_id_seq'::regclass) |
| object_id | character varying(191) | ✗ | - |
| format | character varying(255) | ✗ | - |
| serialized_data | text | ✗ | - |
| object_repr | text | ✗ | - |
| content_type_id | integer | ✗ | - |
| revision_id | integer | ✗ | - |
| db | character varying(191) | ✗ | - |

**Связи (Foreign Keys):**
- `content_type_id` → `django_content_type.id`
- `revision_id` → `reversion_revision.id`

---

### search_search

**Записей в таблице:** 7607

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | nextval('search_search_id_seq'::regclass) |
| created_at | timestamp with time zone | ✗ | - |
| updated_at | timestamp with time zone | ✗ | - |
| source | character varying(30) | ✗ | - |
| primary_key | character varying(200) | ✗ | - |
| path | character varying(1000) | ✗ | - |
| title_en | text | ✗ | - |
| title_kk | text | ✗ | - |
| title_ru | text | ✗ | - |
| published | boolean | ✗ | - |
| author | text | ✗ | - |
| content_en | text | ✗ | - |
| content_kk | text | ✗ | - |
| content_ru | text | ✗ | - |
| search_vector_en | tsvector | ✓ | - |
| search_vector_kk | tsvector | ✓ | - |
| search_vector_ru | tsvector | ✓ | - |

---

### service_amolog

**Записей в таблице:** 0

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | nextval('service_amolog_id_seq'::regclass) |
| created_at | timestamp with time zone | ✗ | - |
| updated_at | timestamp with time zone | ✗ | - |
| request_data | jsonb | ✗ | - |
| response_data | jsonb | ✗ | - |
| service_request_id | integer | ✓ | - |
| delivered | boolean | ✗ | - |

**Связи (Foreign Keys):**
- `service_request_id` → `service_servicerequest.id`

---

### service_boxstorage

**Записей в таблице:** 691

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | nextval('service_boxstorage_id_seq'::regclass) |
| created_at | timestamp with time zone | ✗ | - |
| updated_at | timestamp with time zone | ✗ | - |
| last_box_id | integer | ✗ | - |

---

### service_documentologlog

**Записей в таблице:** 1117

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | nextval('service_documentologlog_id_seq'::regclass... |
| created_at | timestamp with time zone | ✗ | - |
| updated_at | timestamp with time zone | ✗ | - |
| data | jsonb | ✓ | - |
| log_type | character varying(50) | ✗ | - |
| request_data | jsonb | ✓ | - |

---

### service_expertdocument

**Записей в таблице:** 0

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | nextval('service_expertdocument_id_seq'::regclass) |
| created_at | timestamp with time zone | ✗ | - |
| updated_at | timestamp with time zone | ✗ | - |
| name | character varying(200) | ✗ | - |
| file | character varying(100) | ✗ | - |
| user_id | integer | ✗ | - |
| service_request_id | integer | ✗ | - |

**Связи (Foreign Keys):**
- `service_request_id` → `service_servicerequest.id`
- `user_id` → `account_user.id`

---

### service_expertise

**Записей в таблице:** 787

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | nextval('service_expertise_id_seq'::regclass) |
| created_at | timestamp with time zone | ✗ | - |
| updated_at | timestamp with time zone | ✗ | - |
| expertise_type | character varying(20) | ✗ | - |
| status | character varying(20) | ✗ | - |
| data | jsonb | ✗ | - |
| service_request_id | integer | ✗ | - |
| user_id | integer | ✗ | - |
| cep_status | character varying(30) | ✗ | - |
| status_data | jsonb | ✗ | - |

**Связи (Foreign Keys):**
- `service_request_id` → `service_servicerequest.id`
- `user_id` → `account_user.id`

---

### service_expertisegroup

**Записей в таблице:** 13

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | - |
| created_at | timestamp with time zone | ✗ | - |
| updated_at | timestamp with time zone | ✗ | - |
| key | character varying(1000) | ✗ | - |
| service_id | character varying(30) | ✗ | - |
| data | jsonb | ✓ | - |

**Связи (Foreign Keys):**
- `service_id` → `service_service.code`

---

### service_expertisegroup_users

**Записей в таблице:** 25

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | - |
| expertisegroup_id | integer | ✗ | - |
| user_id | integer | ✗ | - |

**Связи (Foreign Keys):**
- `expertisegroup_id` → `service_expertisegroup.id`
- `user_id` → `account_user.id`

---

### service_externaldocument

**Записей в таблице:** 195

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| created_at | timestamp with time zone | ✗ | - |
| updated_at | timestamp with time zone | ✗ | - |
| external_id | character varying(100) | ✗ | - |
| data | jsonb | ✗ | - |
| service_request_id | integer | ✗ | - |

**Связи (Foreign Keys):**
- `service_request_id` → `service_servicerequest.id`

---

### service_externalhooklog

**Записей в таблице:** 2092

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | nextval('service_externalhooklog_id_seq'::regclass... |
| created_at | timestamp with time zone | ✗ | - |
| updated_at | timestamp with time zone | ✗ | - |
| request_data | jsonb | ✗ | - |
| service_request_id | integer | ✗ | - |
| user_id | integer | ✗ | - |

**Связи (Foreign Keys):**
- `service_request_id` → `service_servicerequest.id`
- `user_id` → `account_user.id`

---

### service_extradocument

**Записей в таблице:** 101

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | nextval('service_extradocument_id_seq'::regclass) |
| created_at | timestamp with time zone | ✗ | - |
| updated_at | timestamp with time zone | ✗ | - |
| name | character varying(200) | ✗ | - |
| file | character varying(100) | ✗ | - |
| service_request_id | integer | ✗ | - |
| user_id | integer | ✗ | - |

**Связи (Foreign Keys):**
- `service_request_id` → `service_servicerequest.id`
- `user_id` → `account_user.id`

---

### service_guppurchaseapplication

**Записей в таблице:** 15

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | nextval('service_guppurchaseapplication_id_seq'::r... |
| created_at | timestamp with time zone | ✗ | - |
| updated_at | timestamp with time zone | ✗ | - |
| data | jsonb | ✗ | - |
| status | character varying(50) | ✗ | - |
| author_id | integer | ✗ | - |
| service_request_id | integer | ✗ | - |
| comment | character varying(1000) | ✗ | - |
| search_field | text | ✗ | - |
| purchase_method | character varying(30) | ✓ | - |

**Связи (Foreign Keys):**
- `author_id` → `account_user.id`
- `service_request_id` → `service_servicerequest.id`

---

### service_guppurchaseplan

**Записей в таблице:** 32

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | nextval('service_guppurchaseplan_id_seq'::regclass... |
| created_at | timestamp with time zone | ✗ | - |
| updated_at | timestamp with time zone | ✗ | - |
| data | jsonb | ✗ | - |
| status | character varying(20) | ✗ | - |
| author_id | integer | ✗ | - |
| service_request_id | integer | ✗ | - |
| comment | character varying(1000) | ✗ | - |
| search_field | text | ✗ | - |

**Связи (Foreign Keys):**
- `author_id` → `account_user.id`
- `service_request_id` → `service_servicerequest.id`

---

### service_gupreport

**Записей в таблице:** 267

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | nextval('service_gupreport_id_seq'::regclass) |
| created_at | timestamp with time zone | ✗ | - |
| updated_at | timestamp with time zone | ✗ | - |
| viewed | ARRAY | ✗ | - |
| report_type | character varying(20) | ✗ | - |
| data | jsonb | ✗ | - |
| status | character varying(20) | ✗ | - |
| author_id | integer | ✗ | - |
| service_request_id | integer | ✗ | - |
| comment | character varying(1000) | ✗ | - |
| search_field | text | ✗ | - |
| assignee_id | integer | ✓ | - |

**Связи (Foreign Keys):**
- `assignee_id` → `account_user.id`
- `author_id` → `account_user.id`
- `service_request_id` → `service_servicerequest.id`

---

### service_hubform

**Записей в таблице:** 282

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | nextval('service_hubform_id_seq'::regclass) |
| created_at | timestamp with time zone | ✗ | - |
| updated_at | timestamp with time zone | ✗ | - |
| name | jsonb | ✗ | - |
| description | jsonb | ✗ | - |
| need_signature | boolean | ✗ | - |
| search_field | text | ✗ | - |
| organization_id | character varying(20) | ✗ | - |
| amocrm_data | jsonb | ✗ | - |
| extra_css | text | ✗ | - |
| extra_js | text | ✗ | - |
| multilanguage | boolean | ✗ | - |
| is_hidden | boolean | ✓ | - |

**Связи (Foreign Keys):**
- `organization_id` → `core_organization.code`

---

### service_hubformdata

**Записей в таблице:** 61635

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | nextval('service_hubformdata_id_seq'::regclass) |
| created_at | timestamp with time zone | ✗ | - |
| updated_at | timestamp with time zone | ✗ | - |
| data | jsonb | ✗ | - |
| signature | jsonb | ✗ | - |
| hub_form_id | integer | ✗ | - |
| data_en | jsonb | ✗ | - |
| data_kk | jsonb | ✗ | - |

**Связи (Foreign Keys):**
- `hub_form_id` → `service_hubform.id`

---

### service_hubformfield

**Записей в таблице:** 6603

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | nextval('service_hubformfield_id_seq'::regclass) |
| created_at | timestamp with time zone | ✗ | - |
| updated_at | timestamp with time zone | ✗ | - |
| title | jsonb | ✗ | - |
| subtitle | jsonb | ✗ | - |
| placeholder | jsonb | ✗ | - |
| key | character varying(51) | ✗ | - |
| error_message | jsonb | ✗ | - |
| field_type | character varying(40) | ✗ | - |
| required | boolean | ✗ | - |
| multiple_answers | boolean | ✗ | - |
| position | smallint | ✗ | - |
| data | jsonb | ✗ | - |
| hub_form_step_id | integer | ✗ | - |
| group | character varying(50) | ✓ | - |
| example_id | uuid | ✓ | - |
| prefill_value | character varying(300) | ✓ | - |
| helper_text | jsonb | ✗ | - |

**Связи (Foreign Keys):**
- `hub_form_step_id` → `service_hubformstep.id`

---

### service_hubformstep

**Записей в таблице:** 569

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | nextval('service_hubformstep_id_seq'::regclass) |
| created_at | timestamp with time zone | ✗ | - |
| updated_at | timestamp with time zone | ✗ | - |
| name | jsonb | ✗ | - |
| position | smallint | ✗ | - |
| hub_form_id | integer | ✗ | - |

**Связи (Foreign Keys):**
- `hub_form_id` → `service_hubform.id`

---

### service_pitchinggrade

**Записей в таблице:** 1538

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | nextval('service_pitchinggrade_id_seq'::regclass) |
| created_at | timestamp with time zone | ✗ | - |
| updated_at | timestamp with time zone | ✗ | - |
| total | smallint | ✗ | - |
| data | jsonb | ✗ | - |
| service_request_id | integer | ✗ | - |
| user_id | integer | ✗ | - |
| pitching_type | character varying(20) | ✗ | - |

**Связи (Foreign Keys):**
- `service_request_id` → `service_servicerequest.id`
- `user_id` → `account_user.id`

---

### service_protocol

**Записей в таблице:** 104

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | nextval('service_protocol_id_seq'::regclass) |
| created_at | timestamp with time zone | ✗ | - |
| updated_at | timestamp with time zone | ✗ | - |
| data | jsonb | ✗ | - |
| signature | jsonb | ✗ | - |
| service_id | character varying(30) | ✗ | - |
| status | character varying(20) | ✗ | - |
| protocol_type | character varying(20) | ✗ | - |

**Связи (Foreign Keys):**
- `service_id` → `service_service.code`

---

### service_protocol_accepted

**Записей в таблице:** 467

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | nextval('service_protocol_accepted_id_seq'::regcla... |
| protocol_id | integer | ✗ | - |
| servicerequest_id | integer | ✗ | - |

**Связи (Foreign Keys):**
- `protocol_id` → `service_protocol.id`
- `servicerequest_id` → `service_servicerequest.id`

---

### service_protocol_rejected

**Записей в таблице:** 606

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | nextval('service_protocol_rejected_id_seq'::regcla... |
| protocol_id | integer | ✗ | - |
| servicerequest_id | integer | ✗ | - |

**Связи (Foreign Keys):**
- `protocol_id` → `service_protocol.id`
- `servicerequest_id` → `service_servicerequest.id`

---

### service_report

**Записей в таблице:** 13110

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | nextval('service_report_id_seq'::regclass) |
| created_at | timestamp with time zone | ✗ | - |
| updated_at | timestamp with time zone | ✗ | - |
| year | smallint | ✗ | - |
| report_type | character varying(20) | ✗ | - |
| data | jsonb | ✗ | - |
| signature | jsonb | ✗ | - |
| status | character varying(20) | ✗ | - |
| author_id | integer | ✗ | - |
| service_request_id | integer | ✗ | - |
| viewed | ARRAY | ✗ | - |
| signed_at | timestamp with time zone | ✓ | - |
| version | character varying(10) | ✗ | - |

**Связи (Foreign Keys):**
- `author_id` → `account_user.id`
- `service_request_id` → `service_servicerequest.id`

---

### service_seedmoneyreport

**Записей в таблице:** 333

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | nextval('service_seedmoneyreport_id_seq'::regclass... |
| created_at | timestamp with time zone | ✗ | - |
| updated_at | timestamp with time zone | ✗ | - |
| viewed | ARRAY | ✗ | - |
| report_type | character varying(20) | ✗ | - |
| data | jsonb | ✗ | - |
| status | character varying(20) | ✗ | - |
| comment | text | ✗ | - |
| search_field | text | ✗ | - |
| author_id | integer | ✗ | - |
| company_id | integer | ✓ | - |
| service_request_id | integer | ✗ | - |
| signature | jsonb | ✗ | - |

**Связи (Foreign Keys):**
- `author_id` → `account_user.id`
- `company_id` → `account_company.id`
- `service_request_id` → `service_servicerequest.id`

---

### service_service

**Записей в таблице:** 310

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| created_at | timestamp with time zone | ✗ | - |
| updated_at | timestamp with time zone | ✗ | - |
| code | character varying(30) | ✗ | - |
| name | jsonb | ✗ | - |
| description | jsonb | ✗ | - |
| business_process | character varying(30) | ✗ | - |
| date_start | date | ✓ | - |
| date_end | date | ✓ | - |
| published | boolean | ✗ | - |
| available | boolean | ✗ | - |
| form_count | smallint | ✗ | - |
| category | character varying(30) | ✗ | - |
| hub_form_id | integer | ✗ | - |
| organization_id | character varying(20) | ✗ | - |
| page_id | integer | ✓ | - |
| second_hub_form_id | integer | ✓ | - |
| categories | ARRAY | ✗ | - |
| priority | smallint | ✗ | - |
| roles | ARRAY | ✗ | - |
| lms_data | jsonb | ✗ | - |
| notifications | jsonb | ✗ | - |
| image_id | uuid | ✓ | - |
| actual | boolean | ✗ | - |
| data | jsonb | ✗ | - |
| status | character varying(30) | ✗ | - |
| popular | boolean | ✗ | - |
| games_data | jsonb | ✗ | - |
| absolute_url | character varying(100) | ✗ | - |
| favorite_users | ARRAY | ✗ | - |
| acceptance_order | jsonb | ✗ | - |
| goals | jsonb | ✗ | - |
| show_on_mobile | boolean | ✗ | - |
| show_register_button | boolean | ✗ | - |
| time_end | time without time zone | ✓ | - |
| time_start | time without time zone | ✓ | - |
| is_hidden | boolean | ✓ | - |

**Связи (Foreign Keys):**
- `hub_form_id` → `service_hubform.id`
- `organization_id` → `core_organization.code`
- `page_id` → `landing_page.id`
- `second_hub_form_id` → `service_hubform.id`

---

### service_service_users

**Записей в таблице:** 906

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | nextval('service_service_users_id_seq'::regclass) |
| service_id | character varying(30) | ✗ | - |
| user_id | integer | ✗ | - |

**Связи (Foreign Keys):**
- `service_id` → `service_service.code`
- `user_id` → `account_user.id`

---

### service_servicenote

**Записей в таблице:** 2

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | nextval('service_servicenote_id_seq'::regclass) |
| created_at | timestamp with time zone | ✗ | - |
| updated_at | timestamp with time zone | ✗ | - |
| text | text | ✗ | - |
| author_id | integer | ✗ | - |
| service_id | character varying(30) | ✗ | - |

**Связи (Foreign Keys):**
- `author_id` → `account_user.id`
- `service_id` → `service_service.code`

---

### service_servicerequest

**Записей в таблице:** 56322

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | nextval('service_servicerequest_id_seq'::regclass) |
| created_at | timestamp with time zone | ✗ | - |
| updated_at | timestamp with time zone | ✗ | - |
| status | character varying(50) | ✗ | - |
| search_field | text | ✗ | - |
| assignee_id | integer | ✓ | - |
| author_id | integer | ✗ | - |
| hub_form_data_id | integer | ✗ | - |
| second_hub_form_data_id | integer | ✓ | - |
| service_id | character varying(50) | ✗ | - |
| bp_status | character varying(50) | ✗ | - |
| data | jsonb | ✗ | - |
| expert_id | integer | ✓ | - |
| viewed | ARRAY | ✗ | - |
| company_id | integer | ✓ | - |
| number | integer | ✓ | - |
| sent_at | timestamp with time zone | ✓ | - |
| parent_id | integer | ✓ | - |
| games_data | jsonb | ✗ | - |
| egov_sign_data | jsonb | ✗ | - |
| is_hidden | boolean | ✓ | - |

**Связи (Foreign Keys):**
- `assignee_id` → `account_user.id`
- `author_id` → `account_user.id`
- `company_id` → `account_company.id`
- `expert_id` → `account_user.id`
- `hub_form_data_id` → `service_hubformdata.id`
- `parent_id` → `service_servicerequest.id`
- `second_hub_form_data_id` → `service_hubformdata.id`
- `service_id` → `service_service.code`

---

### service_servicerequestbpstatus

**Записей в таблице:** 82810

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | nextval('service_servicerequestbpstatus_id_seq'::r... |
| created_at | timestamp with time zone | ✗ | - |
| updated_at | timestamp with time zone | ✗ | - |
| bp_status | character varying(50) | ✗ | - |
| service_request_id | integer | ✗ | - |
| user_id | integer | ✗ | - |

**Связи (Foreign Keys):**
- `service_request_id` → `service_servicerequest.id`
- `user_id` → `account_user.id`

---

### service_servicerequestlog

**Записей в таблице:** 4571

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | nextval('service_servicerequestlog_id_seq'::regcla... |
| created_at | timestamp with time zone | ✗ | - |
| updated_at | timestamp with time zone | ✗ | - |
| text | text | ✗ | - |
| data | jsonb | ✗ | - |
| service_request_id | integer | ✗ | - |
| user_id | integer | ✗ | - |
| bp_status | character varying(50) | ✗ | - |

**Связи (Foreign Keys):**
- `service_request_id` → `service_servicerequest.id`
- `user_id` → `account_user.id`

---

### service_servicerequeststatus

**Записей в таблице:** 2031

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | nextval('service_servicerequeststatus_id_seq'::reg... |
| created_at | timestamp with time zone | ✗ | - |
| updated_at | timestamp with time zone | ✗ | - |
| status | character varying(50) | ✗ | - |
| service_request_id | integer | ✗ | - |
| user_id | integer | ✗ | - |

**Связи (Foreign Keys):**
- `service_request_id` → `service_servicerequest.id`
- `user_id` → `account_user.id`

---

### service_techordareport

**Записей в таблице:** 503

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | nextval('service_techordareport_id_seq'::regclass) |
| created_at | timestamp with time zone | ✗ | - |
| updated_at | timestamp with time zone | ✗ | - |
| viewed | ARRAY | ✗ | - |
| year | smallint | ✗ | - |
| month | smallint | ✗ | - |
| data | jsonb | ✗ | - |
| signature | jsonb | ✗ | - |
| signed_at | timestamp with time zone | ✓ | - |
| status | character varying(20) | ✗ | - |
| author_id | integer | ✗ | - |
| service_request_id | integer | ✗ | - |
| comment | character varying(500) | ✗ | - |
| flow | smallint | ✗ | - |

**Связи (Foreign Keys):**
- `author_id` → `account_user.id`
- `service_request_id` → `service_servicerequest.id`

---

### service_techordareportstudent

**Записей в таблице:** 4

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | nextval('service_techordareportstudent_id_seq'::re... |
| created_at | timestamp with time zone | ✗ | - |
| updated_at | timestamp with time zone | ✗ | - |
| data | jsonb | ✗ | - |
| signature | jsonb | ✗ | - |
| signed_at | timestamp with time zone | ✓ | - |
| position | smallint | ✗ | - |
| status | character varying(20) | ✗ | - |
| user_id | integer | ✗ | - |
| form_data | jsonb | ✗ | - |
| month | smallint | ✗ | - |
| tin | character varying(12) | ✗ | - |
| year | smallint | ✗ | - |
| service_request_id | integer | ✓ | - |
| flow | smallint | ✗ | - |
| survey_data | jsonb | ✗ | - |

**Связи (Foreign Keys):**
- `service_request_id` → `service_servicerequest.id`
- `user_id` → `account_user.id`

---

### service_techordastudent

**Записей в таблице:** 3307

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | nextval('service_techordastudent_id_seq'::regclass... |
| created_at | timestamp with time zone | ✗ | - |
| updated_at | timestamp with time zone | ✗ | - |
| tin | character varying(12) | ✗ | - |
| iin | character varying(12) | ✗ | - |
| data | jsonb | ✗ | - |
| status | character varying(20) | ✗ | - |
| flow | smallint | ✗ | - |
| can_reapply | boolean | ✗ | - |

---

### service_vote

**Записей в таблице:** 12945

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | nextval('service_vote_id_seq'::regclass) |
| created_at | timestamp with time zone | ✗ | - |
| updated_at | timestamp with time zone | ✗ | - |
| choice | character varying(20) | ✗ | - |
| data | jsonb | ✗ | - |
| hub_form_data_id | integer | ✗ | - |
| user_id | integer | ✗ | - |
| service_request_id | integer | ✓ | - |
| active | boolean | ✗ | - |

**Связи (Foreign Keys):**
- `hub_form_data_id` → `service_hubformdata.id`
- `service_request_id` → `service_servicerequest.id`
- `user_id` → `account_user.id`

---

### shared_contextdata

**Записей в таблице:** 243

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| created_at | timestamp with time zone | ✗ | - |
| updated_at | timestamp with time zone | ✗ | - |
| data | jsonb | ✗ | - |
| code | character varying(100) | ✗ | - |
| description | character varying(200) | ✗ | - |
| version | character varying(10) | ✗ | - |

---

### shared_largecache

**Записей в таблице:** 2

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| created_at | timestamp with time zone | ✗ | - |
| updated_at | timestamp with time zone | ✗ | - |
| name | character varying(200) | ✗ | - |
| data | jsonb | ✗ | - |
| timeout | integer | ✗ | - |

---

### shared_mediafile

**Записей в таблице:** 50936

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| created_at | timestamp with time zone | ✗ | - |
| updated_at | timestamp with time zone | ✗ | - |
| file | character varying(1000) | ✗ | - |
| thumbnail | character varying(1000) | ✓ | - |
| mime_type | character varying(500) | ✗ | - |
| size | double precision | ✗ | - |
| author_id | integer | ✓ | - |
| thumbnail_150 | character varying(1000) | ✓ | - |
| thumbnail_1500 | character varying(1000) | ✓ | - |
| thumbnail_210 | character varying(1000) | ✓ | - |
| thumbnail_800 | character varying(1000) | ✓ | - |
| id | uuid | ✗ | - |

**Связи (Foreign Keys):**
- `author_id` → `account_user.id`

---

### shared_protectedmediafile

**Записей в таблице:** 92960

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| created_at | timestamp with time zone | ✗ | - |
| updated_at | timestamp with time zone | ✗ | - |
| id | uuid | ✗ | - |
| file | character varying(2000) | ✗ | - |
| primary_key | character varying(20) | ✗ | - |
| source | character varying(20) | ✗ | - |
| author_id | integer | ✗ | - |
| mime_type | character varying(500) | ✗ | - |
| size | double precision | ✗ | - |

**Связи (Foreign Keys):**
- `author_id` → `account_user.id`

---

### shared_seodata

**Записей в таблице:** 97

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| created_at | timestamp with time zone | ✗ | - |
| updated_at | timestamp with time zone | ✗ | - |
| path | character varying | ✗ | - |
| title | jsonb | ✗ | - |
| description | jsonb | ✗ | - |
| keywords | jsonb | ✗ | - |

---

### shared_smslog

**Записей в таблице:** 0

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | nextval('shared_smslog_id_seq'::regclass) |
| created_at | timestamp with time zone | ✗ | - |
| updated_at | timestamp with time zone | ✗ | - |
| number | character varying(100) | ✗ | - |
| request | text | ✗ | - |
| response | text | ✗ | - |

---

### silk_profile

**Записей в таблице:** 0

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | - |
| name | character varying(300) | ✗ | - |
| start_time | timestamp with time zone | ✗ | - |
| end_time | timestamp with time zone | ✓ | - |
| time_taken | double precision | ✓ | - |
| file_path | character varying(300) | ✗ | - |
| line_num | integer | ✓ | - |
| end_line_num | integer | ✓ | - |
| func_name | character varying(300) | ✗ | - |
| exception_raised | boolean | ✗ | - |
| dynamic | boolean | ✗ | - |
| request_id | character varying(36) | ✓ | - |

**Связи (Foreign Keys):**
- `request_id` → `silk_request.id`

---

### silk_profile_queries

**Записей в таблице:** 0

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | - |
| profile_id | integer | ✗ | - |
| sqlquery_id | integer | ✗ | - |

**Связи (Foreign Keys):**
- `profile_id` → `silk_profile.id`
- `sqlquery_id` → `silk_sqlquery.id`

---

### silk_request

**Записей в таблице:** 73

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | character varying(36) | ✗ | - |
| path | character varying(190) | ✗ | - |
| query_params | text | ✗ | - |
| raw_body | text | ✗ | - |
| body | text | ✗ | - |
| method | character varying(10) | ✗ | - |
| start_time | timestamp with time zone | ✗ | - |
| view_name | character varying(190) | ✓ | - |
| end_time | timestamp with time zone | ✓ | - |
| time_taken | double precision | ✓ | - |
| encoded_headers | text | ✗ | - |
| meta_time | double precision | ✓ | - |
| meta_num_queries | integer | ✓ | - |
| meta_time_spent_queries | double precision | ✓ | - |
| pyprofile | text | ✗ | - |
| num_sql_queries | integer | ✗ | - |
| prof_file | character varying(300) | ✗ | - |

---

### silk_response

**Записей в таблице:** 73

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | character varying(36) | ✗ | - |
| status_code | integer | ✗ | - |
| raw_body | text | ✗ | - |
| body | text | ✗ | - |
| encoded_headers | text | ✗ | - |
| request_id | character varying(36) | ✗ | - |

**Связи (Foreign Keys):**
- `request_id` → `silk_request.id`

---

### silk_sqlquery

**Записей в таблице:** 571

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | - |
| query | text | ✗ | - |
| start_time | timestamp with time zone | ✓ | - |
| end_time | timestamp with time zone | ✓ | - |
| time_taken | double precision | ✓ | - |
| traceback | text | ✗ | - |
| request_id | character varying(36) | ✓ | - |
| identifier | integer | ✗ | - |
| analysis | text | ✓ | - |

**Связи (Foreign Keys):**
- `request_id` → `silk_request.id`

---

### social_auth_association

**Записей в таблице:** 0

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | nextval('social_auth_association_id_seq'::regclass... |
| server_url | character varying(255) | ✗ | - |
| handle | character varying(255) | ✗ | - |
| secret | character varying(255) | ✗ | - |
| issued | integer | ✗ | - |
| lifetime | integer | ✗ | - |
| assoc_type | character varying(64) | ✗ | - |

---

### social_auth_code

**Записей в таблице:** 0

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | nextval('social_auth_code_id_seq'::regclass) |
| email | character varying(254) | ✗ | - |
| code | character varying(32) | ✗ | - |
| verified | boolean | ✗ | - |
| timestamp | timestamp with time zone | ✗ | - |

---

### social_auth_nonce

**Записей в таблице:** 0

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | nextval('social_auth_nonce_id_seq'::regclass) |
| server_url | character varying(255) | ✗ | - |
| timestamp | integer | ✗ | - |
| salt | character varying(65) | ✗ | - |

---

### social_auth_partial

**Записей в таблице:** 0

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | nextval('social_auth_partial_id_seq'::regclass) |
| token | character varying(32) | ✗ | - |
| next_step | smallint | ✗ | - |
| backend | character varying(32) | ✗ | - |
| timestamp | timestamp with time zone | ✗ | - |
| data | jsonb | ✗ | - |

---

### social_auth_usersocialauth

**Записей в таблице:** 19505

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | nextval('social_auth_usersocialauth_id_seq'::regcl... |
| provider | character varying(32) | ✗ | - |
| uid | character varying(255) | ✗ | - |
| user_id | integer | ✗ | - |
| created | timestamp with time zone | ✗ | - |
| modified | timestamp with time zone | ✗ | - |
| extra_data | jsonb | ✗ | - |

**Связи (Foreign Keys):**
- `user_id` → `account_user.id`

---

### techorda_applicationform

**Записей в таблице:** 19

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | - |
| created_at | timestamp with time zone | ✗ | - |
| updated_at | timestamp with time zone | ✗ | - |
| assessment_passed | boolean | ✗ | - |
| data | jsonb | ✗ | - |
| status | character varying(20) | ✗ | - |
| assessment_id | integer | ✓ | - |
| author_id | integer | ✗ | - |
| flow_id | integer | ✗ | - |
| course_chosen | boolean | ✗ | - |
| is_grant | boolean | ✗ | - |
| assessment_result | jsonb | ✗ | - |
| is_resident | boolean | ✗ | - |

**Связи (Foreign Keys):**
- `assessment_id` → `techorda_assessment.id`
- `author_id` → `account_user.id`
- `flow_id` → `techorda_flow.id`

---

### techorda_assessment

**Записей в таблице:** 45

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | - |
| unique_id | character varying(10) | ✗ | - |
| url | character varying(500) | ✗ | - |
| used | boolean | ✗ | - |
| result_url | character varying(500) | ✗ | - |

---

### techorda_course

**Записей в таблице:** 203

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | - |
| created_at | timestamp with time zone | ✗ | - |
| updated_at | timestamp with time zone | ✗ | - |
| name | jsonb | ✗ | - |
| price | numeric | ✗ | - |
| description | jsonb | ✗ | - |
| study_format | character varying(100) | ✗ | - |
| activity_field | character varying(200) | ✗ | - |
| has_entrance_exams | boolean | ✗ | - |
| study_lang | character varying(50) | ✗ | - |
| teaching_methodology | character varying(200) | ✗ | - |
| start_date | character varying(100) | ✗ | - |
| classes_format | jsonb | ✗ | - |
| duration_in_week | smallint | ✗ | - |
| duration_in_hour | smallint | ✗ | - |
| level | character varying(50) | ✗ | - |
| quotas | smallint | ✗ | - |
| classes_days_of_week | jsonb | ✗ | - |
| classes_time_of_day | character varying(50) | ✗ | - |
| skills | jsonb | ✗ | - |
| qualification | jsonb | ✗ | - |
| special_condition | jsonb | ✗ | - |
| active | boolean | ✗ | - |
| data | jsonb | ✗ | - |
| flow_id | integer | ✗ | - |
| image_id | uuid | ✓ | - |
| school_id | integer | ✗ | - |

**Связи (Foreign Keys):**
- `flow_id` → `techorda_flow.id`
- `school_id` → `techorda_school.id`

---

### techorda_courseapplication

**Записей в таблице:** 15

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | - |
| created_at | timestamp with time zone | ✗ | - |
| updated_at | timestamp with time zone | ✗ | - |
| status | character varying(100) | ✗ | - |
| applicant_status | character varying(100) | ✗ | - |
| round | character varying(10) | ✗ | - |
| data | jsonb | ✗ | - |
| application_form_id | integer | ✗ | - |
| course_id | integer | ✓ | - |
| flow_id | integer | ✗ | - |
| signature | jsonb | ✗ | - |
| open_modal_window | boolean | ✗ | - |

**Связи (Foreign Keys):**
- `application_form_id` → `techorda_applicationform.id`
- `course_id` → `techorda_course.id`
- `flow_id` → `techorda_flow.id`

---

### techorda_coursefavorite

**Записей в таблице:** 16

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | - |
| created_at | timestamp with time zone | ✗ | - |
| updated_at | timestamp with time zone | ✗ | - |
| course_id | integer | ✗ | - |
| user_id | integer | ✗ | - |

**Связи (Foreign Keys):**
- `course_id` → `techorda_course.id`
- `user_id` → `account_user.id`

---

### techorda_flow

**Записей в таблице:** 4

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | - |
| created_at | timestamp with time zone | ✗ | - |
| updated_at | timestamp with time zone | ✗ | - |
| year | integer | ✗ | - |
| number | smallint | ✗ | - |
| active | boolean | ✗ | - |
| status | character varying(15) | ✗ | - |
| max_application_count | smallint | ✗ | - |
| round_1_end_at | timestamp with time zone | ✓ | - |
| round_1_start_at | timestamp with time zone | ✓ | - |
| round_2_end_at | timestamp with time zone | ✓ | - |
| round_2_start_at | timestamp with time zone | ✓ | - |
| round_3_end_at | timestamp with time zone | ✓ | - |
| round_3_start_at | timestamp with time zone | ✓ | - |
| accepting_applications_end_at | timestamp with time zone | ✓ | - |
| accepting_applications_start_at | timestamp with time zone | ✓ | - |
| school_round_1_end_at | timestamp with time zone | ✓ | - |
| school_round_1_start_at | timestamp with time zone | ✓ | - |
| school_round_2_end_at | timestamp with time zone | ✓ | - |
| school_round_2_start_at | timestamp with time zone | ✓ | - |
| school_round_3_end_at | timestamp with time zone | ✓ | - |
| school_round_3_start_at | timestamp with time zone | ✓ | - |

---

### techorda_school

**Записей в таблице:** 82

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | - |
| created_at | timestamp with time zone | ✗ | - |
| updated_at | timestamp with time zone | ✗ | - |
| name | jsonb | ✗ | - |
| legal_address | jsonb | ✗ | - |
| actual_address | jsonb | ✗ | - |
| website | character varying(100) | ✗ | - |
| phone | character varying(30) | ✗ | - |
| city_phone | character varying(50) | ✗ | - |
| description | jsonb | ✗ | - |
| short_description | jsonb | ✗ | - |
| about | jsonb | ✗ | - |
| instagram_url | character varying(100) | ✗ | - |
| area | character varying(100) | ✗ | - |
| city | character varying(100) | ✗ | - |
| active | boolean | ✗ | - |
| data | jsonb | ✗ | - |
| rating | double precision | ✗ | - |
| author_id | integer | ✗ | - |
| company_id | integer | ✗ | - |
| image_id | uuid | ✓ | - |
| logo_id | uuid | ✓ | - |
| application_confirmed | boolean | ✗ | - |

**Связи (Foreign Keys):**
- `author_id` → `account_user.id`
- `company_id` → `account_company.id`

---

### thumbnail_kvstore

**Записей в таблице:** 230644

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| key | character varying(200) | ✗ | - |
| value | text | ✗ | - |

---

### user_sessions_session

**Записей в таблице:** 2952040

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| session_key | character varying(40) | ✗ | - |
| session_data | text | ✗ | - |
| expire_date | timestamp with time zone | ✗ | - |
| user_agent | character varying(200) | ✓ | - |
| last_activity | timestamp with time zone | ✗ | - |
| ip | inet | ✓ | - |
| user_id | integer | ✓ | - |

**Связи (Foreign Keys):**
- `user_id` → `account_user.id`

---

### waffle_flag

**Записей в таблице:** 56

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | nextval('waffle_flag_id_seq'::regclass) |
| name | character varying(100) | ✗ | - |
| everyone | boolean | ✓ | - |
| percent | numeric | ✓ | - |
| testing | boolean | ✗ | - |
| superusers | boolean | ✗ | - |
| staff | boolean | ✗ | - |
| authenticated | boolean | ✗ | - |
| languages | text | ✗ | - |
| rollout | boolean | ✗ | - |
| note | text | ✗ | - |
| created | timestamp with time zone | ✗ | - |
| modified | timestamp with time zone | ✗ | - |

---

### waffle_flag_groups

**Записей в таблице:** 2

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | nextval('waffle_flag_groups_id_seq'::regclass) |
| flag_id | integer | ✗ | - |
| group_id | integer | ✗ | - |

**Связи (Foreign Keys):**
- `flag_id` → `waffle_flag.id`
- `group_id` → `auth_group.id`

---

### waffle_flag_users

**Записей в таблице:** 24

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | nextval('waffle_flag_users_id_seq'::regclass) |
| flag_id | integer | ✗ | - |
| user_id | integer | ✗ | - |

**Связи (Foreign Keys):**
- `flag_id` → `waffle_flag.id`
- `user_id` → `account_user.id`

---

### waffle_sample

**Записей в таблице:** 0

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | nextval('waffle_sample_id_seq'::regclass) |
| name | character varying(100) | ✗ | - |
| percent | numeric | ✗ | - |
| note | text | ✗ | - |
| created | timestamp with time zone | ✗ | - |
| modified | timestamp with time zone | ✗ | - |

---

### waffle_switch

**Записей в таблице:** 44

| Колонка | Тип | Nullable | Default |
|---------|-----|----------|---------|
| id | integer | ✗ | nextval('waffle_switch_id_seq'::regclass) |
| name | character varying(100) | ✗ | - |
| active | boolean | ✗ | - |
| note | text | ✗ | - |
| created | timestamp with time zone | ✗ | - |
| modified | timestamp with time zone | ✗ | - |

---
