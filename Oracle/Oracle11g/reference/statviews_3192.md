---
title: DBA_FLASHBACK_TXN_REPORT
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_3192.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_FLASHBACK_TXN_REPORT` displays information about all compensating transactions that have been committed in the database. Each row in this view is associated with one compensating transaction.

Related View

`USER_FLASHBACK_TXN_REPORT` displays information about the compensating transactions owned by the current user that have been committed in the database. This view does not display the `USERNAME` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `COMPENSATING_XID` | `RAW(8)` | `NOT NULL` | Transaction responsible for backout |
| `COMPENSATING_TXN_NAME` | `VARCHAR2(256)` |  | Name of the compensating transaction |
| `COMMIT_TIME` | `DATE` |  | Timestamp when the compensating transaction committed |
| `XID_REPORT` | `CLOB` |  | An XML report describing the details of the transactions backed out by the compensating transaction |
| `USERNAME` | `VARCHAR2(30)` | `NOT NULL` | User who is executing the compensating transaction |

See Also:

["USER\_FLASHBACK\_TXN\_REPORT"](statviews_5312.md)