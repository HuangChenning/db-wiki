---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_SENSITIVE_COLUMN_TYPES.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.355 DBA\_SENSITIVE\_COLUMN\_TYPES

`DBA_SENSITIVE_COLUMN_TYPES` describes sensitive column types in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `NAME` | `VARCHAR2(128)` |  | The name of the sensitive column type |
| `USER_COMMENT` | `VARCHAR2(4000)` |  | User comment on the sensitive column type |
| `SOURCE_NAME` | `VARCHAR2(128)` |  | The name of the discovery source for the sensitive column type |
| `SOURCE_TYPE` | `VARCHAR2(3)` |  | The type of the discovery source:  - `ADM`: import from ADM - `DB`: added within the database |

See Also:

[Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=DBSEG856) for more information about transparent sensitive data protection