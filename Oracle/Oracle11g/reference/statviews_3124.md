---
title: DBA_CQ_NOTIFICATION_QUERIES
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_3124.htm
tags:
  - oracle
  - 11g
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

["USER\_CQ\_NOTIFICATION\_QUERIES"](statviews_5260.md)