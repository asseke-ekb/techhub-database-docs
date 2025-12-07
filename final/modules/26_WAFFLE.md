# Модуль WAFFLE

**Описание:** Feature flags (включение/выключение функций)

**Таблиц в модуле:** 5

---

| Таблица | Записей | Описание |
|---------|---------|----------|
| `waffle_flag` | 56 | - |
| `waffle_flag_groups` | 2 | - |
| `waffle_flag_users` | 24 | - |
| `waffle_sample` | 0 | - |
| `waffle_switch` | 44 | - |

### waffle_flag

**Количество записей:** 56

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('waffle_flag_id_seq'::regclass) | Уникальный идентификатор |
| 2 | `name` | character varying(100) | Нет | - | Наименование |
| 3 | `everyone` | boolean | Да | - |  |
| 4 | `percent` | numeric | Да | - |  |
| 5 | `testing` | boolean | Нет | - |  |
| 6 | `superusers` | boolean | Нет | - |  |
| 7 | `staff` | boolean | Нет | - |  |
| 8 | `authenticated` | boolean | Нет | - |  |
| 9 | `languages` | text | Нет | - |  |
| 10 | `rollout` | boolean | Нет | - |  |
| 11 | `note` | text | Нет | - |  |
| 12 | `created` | timestamp with time zone | Нет | - |  |
| 13 | `modified` | timestamp with time zone | Нет | - |  |

---

### waffle_flag_groups

**Количество записей:** 2

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('waffle_flag_groups_id_seq'::reg... | Уникальный идентификатор |
| 2 | `flag_id` | integer | Нет | - | FK на flag |
| 3 | `group_id` | integer | Нет | - | FK на group |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `flag_id` | `waffle_flag.id` |
| `group_id` | `auth_group.id` |

---

### waffle_flag_users

**Количество записей:** 24

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('waffle_flag_users_id_seq'::regc... | Уникальный идентификатор |
| 2 | `flag_id` | integer | Нет | - | FK на flag |
| 3 | `user_id` | integer | Нет | - | FK на user |

**Внешние ключи (FK):**

| Поле | Ссылается на |
|------|--------------|
| `flag_id` | `waffle_flag.id` |
| `user_id` | `account_user.id` |

---

### waffle_sample

**Количество записей:** 0

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('waffle_sample_id_seq'::regclass... | Уникальный идентификатор |
| 2 | `name` | character varying(100) | Нет | - | Наименование |
| 3 | `percent` | numeric | Нет | - |  |
| 4 | `note` | text | Нет | - |  |
| 5 | `created` | timestamp with time zone | Нет | - |  |
| 6 | `modified` | timestamp with time zone | Нет | - |  |

---

### waffle_switch

**Количество записей:** 44

**Структура:**

| № | Атрибут | Тип данных | NULL | По умолчанию | Описание |
|---|---------|------------|------|--------------|----------|
| 1 | `id` | integer | Нет | nextval('waffle_switch_id_seq'::regclass... | Уникальный идентификатор |
| 2 | `name` | character varying(100) | Нет | - | Наименование |
| 3 | `active` | boolean | Нет | - |  |
| 4 | `note` | text | Нет | - |  |
| 5 | `created` | timestamp with time zone | Нет | - |  |
| 6 | `modified` | timestamp with time zone | Нет | - |  |

---

## Приложение: Полный список Foreign Key связей

| № | Таблица | Поле | Ссылается на таблицу | Поле |
|---|---------|------|---------------------|------|
| 1 | `account_activation` | `user_id` | `account_user` | `id` |
| 2 | `account_certificate` | `user_id` | `account_user` | `id` |
| 3 | `account_company` | `author_id` | `account_user` | `id` |
| 4 | `account_complaint` | `author_id` | `account_user` | `id` |
| 5 | `account_complaint` | `company_id` | `account_company` | `id` |
| 6 | `account_complaint` | `user_id` | `account_user` | `id` |
| 7 | `account_contactpress` | `author_id` | `account_user` | `id` |
| 8 | `account_contactpress` | `company_id` | `account_company` | `id` |
| 9 | `account_contactpress` | `user_id` | `account_user` | `id` |
| 10 | `account_contactrequest` | `author_id` | `account_user` | `id` |
| 11 | `account_contactrequest` | `user_id` | `account_user` | `id` |
| 12 | `account_course` | `user_id` | `account_user` | `id` |
| 13 | `account_education` | `user_id` | `account_user` | `id` |
| 14 | `account_experience` | `company_id` | `account_company` | `id` |
| 15 | `account_experience` | `user_id` | `account_user` | `id` |
| 16 | `account_user` | `company_id` | `account_company` | `id` |
| 17 | `account_user` | `organization_id` | `core_organization` | `code` |
| 18 | `account_usercompany` | `company_id` | `account_company` | `id` |
| 19 | `account_usercompany` | `user_id` | `account_user` | `id` |
| 20 | `account_usercompanyinvitation` | `author_id` | `account_user` | `id` |
| 21 | `account_usercompanyinvitation` | `company_id` | `account_company` | `id` |
| 22 | `account_usercompanyinvitation` | `invited_user_id` | `account_user` | `id` |
| 23 | `account_usercompanyrequest` | `company_id` | `account_company` | `id` |
| 24 | `account_usercompanyrequest` | `user_id` | `account_user` | `id` |
| 25 | `account_user_groups` | `group_id` | `auth_group` | `id` |
| 26 | `account_user_groups` | `user_id` | `account_user` | `id` |
| 27 | `account_user_user_permissions` | `permission_id` | `auth_permission` | `id` |
| 28 | `account_user_user_permissions` | `user_id` | `account_user` | `id` |
| 29 | `auth_group_permissions` | `group_id` | `auth_group` | `id` |
| 30 | `auth_group_permissions` | `permission_id` | `auth_permission` | `id` |
| 31 | `auth_permission` | `content_type_id` | `django_content_type` | `id` |
| 32 | `authtoken_token` | `user_id` | `account_user` | `id` |
| 33 | `booking_booking` | `author_id` | `account_user` | `id` |
| 34 | `booking_booking` | `company_id` | `account_company` | `id` |
| 35 | `booking_booking` | `room_id` | `booking_room` | `id` |
| 36 | `booking_bookingstatus` | `booking_id` | `booking_booking` | `id` |
| 37 | `community_companyfollow` | `followed_id` | `account_company` | `id` |
| 38 | `community_companyfollow` | `follower_id` | `account_user` | `id` |
| 39 | `community_userfollow` | `followed_id` | `account_user` | `id` |
| 40 | `community_userfollow` | `follower_id` | `account_user` | `id` |
| 41 | `core_actionlog` | `user_id` | `account_user` | `id` |
| 42 | `core_article` | `author_id` | `account_user` | `id` |
| 43 | `core_article` | `category_id` | `core_category` | `id` |
| 44 | `core_blog` | `author_id` | `account_user` | `id` |
| 45 | `core_blog` | `category_id` | `core_category` | `id` |
| 46 | `core_blog` | `company_id` | `account_company` | `id` |
| 47 | `core_category` | `background_id` | `shared_mediafile` | `id` |
| 48 | `core_city` | `country_id` | `core_country` | `id` |
| 49 | `core_comment` | `parent_id` | `core_comment` | `id` |
| 50 | `core_comment` | `user_id` | `account_user` | `id` |
| 51 | `core_discussion` | `author_id` | `account_user` | `id` |
| 52 | `core_discussion` | `category_id` | `core_category` | `id` |
| 53 | `core_discussionvote` | `discussion_id` | `core_discussion` | `id` |
| 54 | `core_discussionvote` | `user_id` | `account_user` | `id` |
| 55 | `core_elabsannouncement` | `author_id` | `account_user` | `id` |
| 56 | `core_event` | `author_id` | `account_user` | `id` |
| 57 | `core_event` | `company_id` | `account_company` | `id` |
| 58 | `core_event` | `organization_id` | `core_organization` | `code` |
| 59 | `core_eventparticipant` | `author_id` | `account_user` | `id` |
| 60 | `core_eventparticipant` | `event_id` | `core_event` | `id` |
| 61 | `core_faqitem` | `faq_id` | `core_faq` | `code` |
| 62 | `core_feed` | `article_id` | `core_article` | `id` |
| 63 | `core_feed` | `blog_id` | `core_blog` | `id` |
| 64 | `core_feed` | `discussion_id` | `core_discussion` | `id` |
| 65 | `core_feed` | `event_id` | `core_event` | `id` |
| 66 | `core_feed` | `tech_task_id` | `core_techtask` | `id` |
| 67 | `core_feed` | `vacancy_id` | `core_vacancy` | `id` |
| 68 | `core_infrastructure` | `author_id` | `account_user` | `id` |
| 69 | `core_infrastructure` | `company_id` | `account_company` | `id` |
| 70 | `core_infrastructure` | `organization_id` | `core_organization` | `code` |
| 71 | `core_infrastructure` | `parent_id` | `core_infrastructure` | `id` |
| 72 | `core_infrastructureimage` | `author_id` | `account_user` | `id` |
| 73 | `core_infrastructureimage` | `infrastructure_id` | `core_infrastructure` | `id` |
| 74 | `core_infrastructurerequest` | `author_id` | `account_user` | `id` |
| 75 | `core_infrastructurerequest` | `infrastructure_id` | `core_infrastructure` | `id` |
| 76 | `core_notification` | `user_id` | `account_user` | `id` |
| 77 | `core_techtask` | `author_id` | `account_user` | `id` |
| 78 | `core_techtasksolution` | `author_id` | `account_user` | `id` |
| 79 | `core_techtasksolution` | `tech_task_id` | `core_techtask` | `id` |
| 80 | `core_vacancy` | `author_id` | `account_user` | `id` |
| 81 | `core_vacancy` | `city_id` | `core_city` | `id` |
| 82 | `core_vacancy` | `company_id` | `account_company` | `id` |
| 83 | `core_vacancycandidate` | `author_id` | `account_user` | `id` |
| 84 | `core_vacancycandidate` | `vacancy_id` | `core_vacancy` | `id` |
| 85 | `django_admin_log` | `content_type_id` | `django_content_type` | `id` |
| 86 | `django_admin_log` | `user_id` | `account_user` | `id` |
| 87 | `explorer_query` | `created_by_user_id` | `account_user` | `id` |
| 88 | `explorer_queryfavorite` | `query_id` | `explorer_query` | `id` |
| 89 | `explorer_queryfavorite` | `user_id` | `account_user` | `id` |
| 90 | `explorer_querylog` | `query_id` | `explorer_query` | `id` |
| 91 | `explorer_querylog` | `run_by_user_id` | `account_user` | `id` |
| 92 | `journeymap_companystate` | `company_id` | `account_company` | `id` |
| 93 | `journeymap_companystate` | `journeymap_id` | `journeymap_journeymap` | `key` |
| 94 | `journeymap_question` | `task_id` | `journeymap_task` | `id` |
| 95 | `journeymap_step` | `journeymap_id` | `journeymap_journeymap` | `key` |
| 96 | `journeymap_step_next_steps` | `from_step_id` | `journeymap_step` | `id` |
| 97 | `journeymap_step_next_steps` | `to_step_id` | `journeymap_step` | `id` |
| 98 | `journeymap_task` | `step_id` | `journeymap_step` | `id` |
| 99 | `journeymap_userstate` | `journeymap_id` | `journeymap_journeymap` | `key` |
| 100 | `journeymap_userstate` | `user_id` | `account_user` | `id` |
| 101 | `landing_component` | `section_id` | `landing_section` | `id` |
| 102 | `landing_page` | `author_id` | `account_user` | `id` |
| 103 | `landing_page` | `organization_id` | `core_organization` | `code` |
| 104 | `landing_pagemediafile` | `author_id` | `account_user` | `id` |
| 105 | `landing_pagemediafile` | `page_id` | `landing_page` | `id` |
| 106 | `landing_section` | `page_id` | `landing_page` | `id` |
| 107 | `matchmaking_match` | `user_a_id` | `account_user` | `id` |
| 108 | `matchmaking_match` | `user_b_id` | `account_user` | `id` |
| 109 | `matchmaking_profile` | `user_id` | `account_user` | `id` |
| 110 | `niokr_niokrnotification_projects` | `niokrnotification_id` | `niokr_niokrnotification` | `id` |
| 111 | `niokr_niokrnotification_projects` | `niokrproject_id` | `niokr_niokrproject` | `id` |
| 112 | `niokr_niokrprojectexecutor_projects` | `niokrproject_id` | `niokr_niokrproject` | `id` |
| 113 | `niokr_niokrprojectexecutor_projects` | `niokrprojectexecutor_id` | `niokr_niokrprojectexecutor` | `id` |
| 114 | `oauth2_provider_accesstoken` | `application_id` | `oauth2_provider_application` | `id` |
| 115 | `oauth2_provider_accesstoken` | `id_token_id` | `oauth2_provider_idtoken` | `id` |
| 116 | `oauth2_provider_accesstoken` | `source_refresh_token_id` | `oauth2_provider_refreshtoken` | `id` |
| 117 | `oauth2_provider_accesstoken` | `user_id` | `account_user` | `id` |
| 118 | `oauth2_provider_application` | `user_id` | `account_user` | `id` |
| 119 | `oauth2_provider_grant` | `application_id` | `oauth2_provider_application` | `id` |
| 120 | `oauth2_provider_grant` | `user_id` | `account_user` | `id` |
| 121 | `oauth2_provider_idtoken` | `application_id` | `oauth2_provider_application` | `id` |
| 122 | `oauth2_provider_idtoken` | `user_id` | `account_user` | `id` |
| 123 | `oauth2_provider_refreshtoken` | `access_token_id` | `oauth2_provider_accesstoken` | `id` |
| 124 | `oauth2_provider_refreshtoken` | `application_id` | `oauth2_provider_application` | `id` |
| 125 | `oauth2_provider_refreshtoken` | `user_id` | `account_user` | `id` |
| 126 | `reversion_revision` | `user_id` | `account_user` | `id` |
| 127 | `reversion_version` | `content_type_id` | `django_content_type` | `id` |
| 128 | `reversion_version` | `revision_id` | `reversion_revision` | `id` |
| 129 | `service_amolog` | `service_request_id` | `service_servicerequest` | `id` |
| 130 | `service_expertdocument` | `service_request_id` | `service_servicerequest` | `id` |
| 131 | `service_expertdocument` | `user_id` | `account_user` | `id` |
| 132 | `service_expertise` | `service_request_id` | `service_servicerequest` | `id` |
| 133 | `service_expertise` | `user_id` | `account_user` | `id` |
| 134 | `service_expertisegroup` | `service_id` | `service_service` | `code` |
| 135 | `service_expertisegroup_users` | `expertisegroup_id` | `service_expertisegroup` | `id` |
| 136 | `service_expertisegroup_users` | `user_id` | `account_user` | `id` |
| 137 | `service_externaldocument` | `service_request_id` | `service_servicerequest` | `id` |
| 138 | `service_externalhooklog` | `service_request_id` | `service_servicerequest` | `id` |
| 139 | `service_externalhooklog` | `user_id` | `account_user` | `id` |
| 140 | `service_extradocument` | `service_request_id` | `service_servicerequest` | `id` |
| 141 | `service_extradocument` | `user_id` | `account_user` | `id` |
| 142 | `service_guppurchaseapplication` | `author_id` | `account_user` | `id` |
| 143 | `service_guppurchaseapplication` | `service_request_id` | `service_servicerequest` | `id` |
| 144 | `service_guppurchaseplan` | `author_id` | `account_user` | `id` |
| 145 | `service_guppurchaseplan` | `service_request_id` | `service_servicerequest` | `id` |
| 146 | `service_gupreport` | `assignee_id` | `account_user` | `id` |
| 147 | `service_gupreport` | `author_id` | `account_user` | `id` |
| 148 | `service_gupreport` | `service_request_id` | `service_servicerequest` | `id` |
| 149 | `service_hubform` | `organization_id` | `core_organization` | `code` |
| 150 | `service_hubformdata` | `hub_form_id` | `service_hubform` | `id` |
| 151 | `service_hubformfield` | `hub_form_step_id` | `service_hubformstep` | `id` |
| 152 | `service_hubformstep` | `hub_form_id` | `service_hubform` | `id` |
| 153 | `service_pitchinggrade` | `service_request_id` | `service_servicerequest` | `id` |
| 154 | `service_pitchinggrade` | `user_id` | `account_user` | `id` |
| 155 | `service_protocol` | `service_id` | `service_service` | `code` |
| 156 | `service_protocol_accepted` | `protocol_id` | `service_protocol` | `id` |
| 157 | `service_protocol_accepted` | `servicerequest_id` | `service_servicerequest` | `id` |
| 158 | `service_protocol_rejected` | `protocol_id` | `service_protocol` | `id` |
| 159 | `service_protocol_rejected` | `servicerequest_id` | `service_servicerequest` | `id` |
| 160 | `service_report` | `author_id` | `account_user` | `id` |
| 161 | `service_report` | `service_request_id` | `service_servicerequest` | `id` |
| 162 | `service_seedmoneyreport` | `author_id` | `account_user` | `id` |
| 163 | `service_seedmoneyreport` | `company_id` | `account_company` | `id` |
| 164 | `service_seedmoneyreport` | `service_request_id` | `service_servicerequest` | `id` |
| 165 | `service_service` | `hub_form_id` | `service_hubform` | `id` |
| 166 | `service_service` | `organization_id` | `core_organization` | `code` |
| 167 | `service_service` | `page_id` | `landing_page` | `id` |
| 168 | `service_service` | `second_hub_form_id` | `service_hubform` | `id` |
| 169 | `service_servicenote` | `author_id` | `account_user` | `id` |
| 170 | `service_servicenote` | `service_id` | `service_service` | `code` |
| 171 | `service_servicerequest` | `assignee_id` | `account_user` | `id` |
| 172 | `service_servicerequest` | `author_id` | `account_user` | `id` |
| 173 | `service_servicerequest` | `company_id` | `account_company` | `id` |
| 174 | `service_servicerequest` | `expert_id` | `account_user` | `id` |
| 175 | `service_servicerequest` | `hub_form_data_id` | `service_hubformdata` | `id` |
| 176 | `service_servicerequest` | `parent_id` | `service_servicerequest` | `id` |
| 177 | `service_servicerequest` | `second_hub_form_data_id` | `service_hubformdata` | `id` |
| 178 | `service_servicerequest` | `service_id` | `service_service` | `code` |
| 179 | `service_servicerequestbpstatus` | `service_request_id` | `service_servicerequest` | `id` |
| 180 | `service_servicerequestbpstatus` | `user_id` | `account_user` | `id` |
| 181 | `service_servicerequestlog` | `service_request_id` | `service_servicerequest` | `id` |
| 182 | `service_servicerequestlog` | `user_id` | `account_user` | `id` |
| 183 | `service_servicerequeststatus` | `service_request_id` | `service_servicerequest` | `id` |
| 184 | `service_servicerequeststatus` | `user_id` | `account_user` | `id` |
| 185 | `service_service_users` | `service_id` | `service_service` | `code` |
| 186 | `service_service_users` | `user_id` | `account_user` | `id` |
| 187 | `service_techordareport` | `author_id` | `account_user` | `id` |
| 188 | `service_techordareport` | `service_request_id` | `service_servicerequest` | `id` |
| 189 | `service_techordareportstudent` | `service_request_id` | `service_servicerequest` | `id` |
| 190 | `service_techordareportstudent` | `user_id` | `account_user` | `id` |
| 191 | `service_vote` | `hub_form_data_id` | `service_hubformdata` | `id` |
| 192 | `service_vote` | `service_request_id` | `service_servicerequest` | `id` |
| 193 | `service_vote` | `user_id` | `account_user` | `id` |
| 194 | `shared_mediafile` | `author_id` | `account_user` | `id` |
| 195 | `shared_protectedmediafile` | `author_id` | `account_user` | `id` |
| 196 | `silk_profile` | `request_id` | `silk_request` | `id` |
| 197 | `silk_profile_queries` | `profile_id` | `silk_profile` | `id` |
| 198 | `silk_profile_queries` | `sqlquery_id` | `silk_sqlquery` | `id` |
| 199 | `silk_response` | `request_id` | `silk_request` | `id` |
| 200 | `silk_sqlquery` | `request_id` | `silk_request` | `id` |
| 201 | `social_auth_usersocialauth` | `user_id` | `account_user` | `id` |
| 202 | `techorda_applicationform` | `assessment_id` | `techorda_assessment` | `id` |
| 203 | `techorda_applicationform` | `author_id` | `account_user` | `id` |
| 204 | `techorda_applicationform` | `flow_id` | `techorda_flow` | `id` |
| 205 | `techorda_course` | `flow_id` | `techorda_flow` | `id` |
| 206 | `techorda_course` | `school_id` | `techorda_school` | `id` |
| 207 | `techorda_courseapplication` | `application_form_id` | `techorda_applicationform` | `id` |
| 208 | `techorda_courseapplication` | `course_id` | `techorda_course` | `id` |
| 209 | `techorda_courseapplication` | `flow_id` | `techorda_flow` | `id` |
| 210 | `techorda_coursefavorite` | `course_id` | `techorda_course` | `id` |
| 211 | `techorda_coursefavorite` | `user_id` | `account_user` | `id` |
| 212 | `techorda_school` | `author_id` | `account_user` | `id` |
| 213 | `techorda_school` | `company_id` | `account_company` | `id` |
| 214 | `user_sessions_session` | `user_id` | `account_user` | `id` |
| 215 | `waffle_flag_groups` | `flag_id` | `waffle_flag` | `id` |
| 216 | `waffle_flag_groups` | `group_id` | `auth_group` | `id` |
| 217 | `waffle_flag_users` | `flag_id` | `waffle_flag` | `id` |
| 218 | `waffle_flag_users` | `user_id` | `account_user` | `id` |