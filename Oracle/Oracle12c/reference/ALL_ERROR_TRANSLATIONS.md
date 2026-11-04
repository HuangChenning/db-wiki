---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/ALL_ERROR_TRANSLATIONS.html
tags:
  - oracle
  - 12c
  - reference
---

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