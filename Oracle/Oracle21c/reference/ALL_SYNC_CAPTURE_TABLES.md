---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_SYNC_CAPTURE_TABLES.html
tags:
  - oracle
  - 21c
  - reference
---

## 4.102 ALL\_SYNC\_CAPTURE\_TABLES

`ALL_SYNC_CAPTURE_TABLES` displays information about the tables accessible to the current user that are captured by synchronous captures.

Related View

`DBA_SYNC_CAPTURE_TABLES` displays information about all tables in the database that are captured by synchronous captures.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `TABLE_OWNER` | `VARCHAR2(128)` |  | Owner of the synchronous capture table |
| `TABLE_NAME` | `VARCHAR2(128)` |  | Name of the synchronous capture table |
| `ENABLED` | `VARCHAR2(3)` |  | Indicates whether synchronous capture is enabled for the table (`YES`) or not (`NO`) |

See Also:

" [DBA\_SYNC\_CAPTURE\_TABLES](DBA_SYNC_CAPTURE_TABLES.md) "