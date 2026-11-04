---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_FLASHBACK_TXN_REPORT.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.332 DBA\_FLASHBACK\_TXN\_REPORT

`DBA_FLASHBACK_TXN_REPORT` displays information about all compensating transactions that have been committed in the database.

Each row in this view is associated with one compensating transaction.

Related View

`USER_FLASHBACK_TXN_REPORT` displays information about the compensating transactions owned by the current user that have been committed in the database. This view does not display the `USERNAME` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `COMPENSATING_XID` | `RAW(8)` | `NOT NULL` | Transaction responsible for backout |
| `COMPENSATING_TXN_NAME` | `VARCHAR2(256)` |  | Name of the compensating transaction |
| `COMMIT_TIME` | `DATE` |  | Timestamp when the compensating transaction committed |
| `XID_REPORT` | `CLOB` |  | An XML report describing the details of the transactions backed out by the compensating transaction |
| `USERNAME` | `VARCHAR2(128)` | `NOT NULL` | User who is executing the compensating transaction |

See Also:

" [USER\_FLASHBACK\_TXN\_REPORT](USER_FLASHBACK_TXN_REPORT.md) "