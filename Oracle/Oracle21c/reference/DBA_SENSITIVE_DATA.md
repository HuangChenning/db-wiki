---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_SENSITIVE_DATA.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.356 DBA\_SENSITIVE\_DATA

`DBA_SENSITIVE_DATA` describes the sensitive columns in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SENSITIVE#` | `NUMBER` | `NOT NULL` | Dictionary ID for the sensitive data |
| `SCHEMA_NAME` | `VARCHAR2(128)` | `NOT NULL` | The schema containing the sensitive data |
| `TABLE_NAME` | `VARCHAR2(128)` | `NOT NULL` | The table containing the sensitive data |
| `COLUMN_NAME` | `VARCHAR2(128)` | `NOT NULL` | The name of the column identified as sensitive |
| `SENSITIVE_TYPE` | `VARCHAR2(128)` |  | The sensitive column type of the data |
| `SOURCE_NAME` | `VARCHAR2(128)` |  | The name of the discovery source for the sensitive data |
| `USER_COMMENT` | `VARCHAR2(4000)` |  | User comment on the sensitive data |
| `TS` | `TIMESTAMP(6)` |  | The time when the data was identified as sensitive in the database |

See Also:

[Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=DBSEG856) for more information about transparent sensitive data protection