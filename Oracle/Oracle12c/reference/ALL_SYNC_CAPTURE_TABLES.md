---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/ALL_SYNC_CAPTURE_TABLES.html
tags:
  - oracle
  - 12c
  - reference
---

`ALL_SYNC_CAPTURE_TABLES` displays information about the tables accessible to the current user that are captured by synchronous Streams captures.

Related View

`DBA_SYNC_CAPTURE_TABLES` displays information about all tables in the database that are captured by synchronous Streams captures.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `TABLE_OWNER` | `VARCHAR2(128)` |  | Owner of the synchronous capture table |
| `TABLE_NAME` | `VARCHAR2(128)` |  | Name of the synchronous capture table |
| `ENABLED` | `VARCHAR2(3)` |  | Indicates whether synchronous Streams capture is enabled for the table (`YES`) or not (`NO`) |

See Also:

" [DBA\_SYNC\_CAPTURE\_TABLES](DBA_SYNC_CAPTURE_TABLES.md) "