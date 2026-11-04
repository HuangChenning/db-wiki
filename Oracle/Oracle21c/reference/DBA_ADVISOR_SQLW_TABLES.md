---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_ADVISOR_SQLW_TABLES.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.48 DBA\_ADVISOR\_SQLW\_TABLES

`DBA_ADVISOR_SQLW_TABLES` displays cross references between the workload statements and the tables referenced in the statement.

Related View

`USER_ADVISOR_SQLW_TABLES` displays cross references between the workload statements and the tables referenced in the statement. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` |  | Owner of the workload object |
| `WORKLOAD_ID` | `NUMBER` |  | Unique identifier number of the workload object |
| `WORKLOAD_NAME` | `VARCHAR2(128)` |  | Name of the workload |
| `SQL_ID` | `NUMBER` |  | Identifier of the statement |
| `TABLE_OWNER` | `VARCHAR2(128)` |  | Owner of the table |
| `TABLE_NAME` | `VARCHAR2(128)` |  | Name of the table |

See Also:

" [USER\_ADVISOR\_SQLW\_TABLES](USER_ADVISOR_SQLW_TABLES.md) "