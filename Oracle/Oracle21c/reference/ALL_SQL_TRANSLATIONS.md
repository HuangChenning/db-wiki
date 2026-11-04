---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_SQL_TRANSLATIONS.html
tags:
  - oracle
  - 21c
  - reference
---

## 4.77 ALL\_SQL\_TRANSLATIONS

`ALL_SQL_TRANSLATIONS` describes all SQL translations accessible to the user.

Related Views

- `DBA_SQL_TRANSLATIONS` describes all SQL translations in the database.
- `USER_SQL_TRANSLATIONS` describes all SQL translations owned by the user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the SQL translation profile |
| `PROFILE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the SQL translation profile |
| `SQL_TEXT` | `CLOB` | `NOT NULL` | The SQL statement |
| `TRANSLATED_TEXT` | `CLOB` |  | The translated SQL statement |
| `SQL_ID` | `VARCHAR2(13)` | `NOT NULL` | SQL identifier of the SQL statement |
| `HASH_VALUE` | `NUMBER` | `NOT NULL` | Hash value of the SQL statement |
| `ENABLED` | `VARCHAR2(5)` |  | Displays whether the translation is enabled. Possible values:  - `TRUE` - `FALSE` |
| `REGISTRATION_TIME` | `TIMESTAMP(6)` |  | Time the translation was registered |
| `CLIENT_INFO` | `VARCHAR2(64)` |  | Client information when the SQL was parsed and the translation was registered |
| `MODULE` | `VARCHAR2(64)` |  | Module when the SQL was parsed and the translation was registered |
| `ACTION` | `VARCHAR2(64)` |  | Action when the SQL was parsed and the translation was registered |
| `PARSING_USER_ID` | `NUMBER` |  | Current user ID when the SQL was parsed and the translation was registered |
| `PARSING_SCHEMA_ID` | `NUMBER` |  | Current schema ID when the SQL was parsed and the translation was registered |