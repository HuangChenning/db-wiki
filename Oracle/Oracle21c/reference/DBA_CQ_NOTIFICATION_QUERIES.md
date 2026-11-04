---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_CQ_NOTIFICATION_QUERIES.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.250 DBA\_CQ\_NOTIFICATION\_QUERIES

`DBA_CQ_NOTIFICATION_QUERIES` describes the registered queries for all CQ notifications in the database.

Related View

`USER_CQ_NOTIFICATION_QUERIES` describes the registered queries for the CQ notifications owned by the current user. This view does not display the `USERNAME` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `QUERYID` | `NUMBER` |  | ID of the query |
| `QUERYTEXT` | `CLOB` |  | Text of the query |
| `REGID` | `NUMBER` |  | Registration ID that the query is registered with |
| `USERNAME` | `VARCHAR2(31)` |  | Name of the user who registered the query |

See Also:

" [USER\_CQ\_NOTIFICATION\_QUERIES](USER_CQ_NOTIFICATION_QUERIES.md) "