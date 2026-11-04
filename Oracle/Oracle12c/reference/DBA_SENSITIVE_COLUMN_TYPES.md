---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_SENSITIVE_COLUMN_TYPES.html
tags:
  - oracle
  - 12c
  - reference
---

`DBA_SENSITIVE_COLUMN_TYPES` describes sensitive column types in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `NAME` | `VARCHAR2(128)` |  | The name of the sensitive column type |
| `USER_COMMENT` | `VARCHAR2(4000)` |  | User comment on the sensitive column type |
| `SOURCE_NAME` | `VARCHAR2(128)` |  | The name of the discovery source for the sensitive column type |
| `SOURCE_TYPE` | `VARCHAR2(3)` |  | The type of the discovery source:  - `ADM`: import from ADM - `DB`: added within the database |

See Also:

[Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=DBSEG856) for more information about transparent sensitive data protection