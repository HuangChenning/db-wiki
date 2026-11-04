---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/ALL_SQL_TRANSLATION_PROFILES.html
tags:
  - oracle
  - 12c
  - reference
---

`ALL_SQL_TRANSLATION_PROFILES` describes all SQL translation profiles accessible to the user.

Related Views

- `DBA_SQL_TRANSLATION_PROFILES` describes all SQL translation profiles in the database.
- `USER_SQL_TRANSLATION_PROFILES` describes all SQL translation profiles owned by the user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the SQL translation profile |
| `PROFILE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the SQL translation profile |
| `TRANSLATOR` | `VARCHAR2(261)` |  | The translator package |
| `FOREIGN_SQL_SYNTAX` | `VARCHAR2(5)` |  | Indicates whether the SQL syntax is foreign.  Possible values:  - `TRUE` - `FALSE` |
| `TRANSLATE_NEW_SQL` | `VARCHAR2(5)` |  | Indicates whether to translate new SQL statements and errors using the translator.  Possible values:  - `TRUE` - `FALSE` |
| `RAISE_TRANSLATION_ERROR` | `VARCHAR2(5)` |  | Indicates whether to raise translation error.  Possible values:  - `TRUE` - `FALSE` |
| `LOG_TRANSLATION_ERROR` | `VARCHAR2(5)` |  | Indicates whether to log translation error.  Possible values:  - `TRUE` - `FALSE` |
| `TRACE_TRANSLATION` | `VARCHAR2(5)` |  | Indicates whether to trace translation.  Possible values:  - `TRUE` - `FALSE` |
| `LOG_ERRORS` | `VARCHAR2(5)` |  | Indicates whether there are log errors (`TRUE`) or not (`FALSE`)  This column is available starting with Oracle Database 12c Release 2 (12.2.0.1). |

See Also:

- " [DBA\_SQL\_TRANSLATION\_PROFILES](DBA_SQL_TRANSLATION_PROFILES.md) "
- " [USER\_SQL\_TRANSLATION\_PROFILES](USER_SQL_TRANSLATION_PROFILES.md) "