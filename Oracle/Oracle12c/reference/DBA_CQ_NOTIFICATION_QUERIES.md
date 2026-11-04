---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_CQ_NOTIFICATION_QUERIES.html
tags:
  - oracle
  - 12c
  - reference
---

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