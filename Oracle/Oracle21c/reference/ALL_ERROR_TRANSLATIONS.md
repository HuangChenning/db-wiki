---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_ERROR_TRANSLATIONS.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.182 ALL\_ERROR\_TRANSLATIONS

`ALL_ERROR_TRANSLATIONS` describes all error translations accessible to the user.

Related Views

- `DBA_ERROR_TRANSLATIONS` describes all error translations in the database.
- `USER_ERROR_TRANSLATIONS` describes all error translations owned by the user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the SQL translation profile |
| `PROFILE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the SQL translation profile |
| `ERROR_CODE` | `NUMBER` | `NOT NULL` | The Oracle error code |
| `TRANSLATED_CODE` | `NUMBER` |  | The translated error code |
| `TRANSLATED_SQLSTATE` | `VARCHAR2(5)` |  | The translated SQLSTATE |
| `ENABLED` | `VARCHAR2(5)` |  | `TRUE` if the translation is enabled, `FALSE` otherwise. |
| `REGISTRATION_TIME` | `TIMESTAMP(6)` |  | Time the translation was registered |