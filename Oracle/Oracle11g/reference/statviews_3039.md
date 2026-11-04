---
title: DBA_ADVISOR_SQLW_TABLES
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_3039.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_ADVISOR_SQLW_TABLES` displays cross references between the workload statements and the tables referenced in the statement.

Related View

`USER_ADVISOR_SQLW_TABLES` displays cross references between the workload statements and the tables referenced in the statement. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` |  | Owner of the workload object |
| `WORKLOAD_ID` | `NUMBER` |  | Unique identifier number of the workload object |
| `WORKLOAD_NAME` | `VARCHAR2(30)` |  | Name of the workload |
| `SQL_ID` | `NUMBER` |  | Identifier of the statement |
| `TABLE_OWNER` | `VARCHAR2(30)` |  | Owner of the table |
| `TABLE_NAME` | `VARCHAR2(30)` |  | Name of the table |

See Also:

["USER\_ADVISOR\_SQLW\_TABLES"](statviews_5221.md)