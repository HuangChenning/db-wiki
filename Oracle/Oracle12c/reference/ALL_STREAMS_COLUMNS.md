---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/ALL_STREAMS_COLUMNS.html
tags:
  - oracle
  - 12c
  - reference
---

`ALL_STREAMS_COLUMNS` displays information about the Streams unsupported columns accessible to the current user.

Related View

`DBA_STREAMS_COLUMNS` displays information about all Streams unsupported columns in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` |  | Owner of the table |
| `TABLE_NAME` | `VARCHAR2(128)` |  | Name of the table |
| `COLUMN_NAME` | `VARCHAR2(128)` |  | Name of the column |
| `SYNC_CAPTURE_VERSION` | `NUMBER` |  | Version of the synchronous capture that supports this column |
| `SYNC_CAPTURE_REASON` | `VARCHAR2(39)` |  | Reason why this column is not supported by synchronous capture |
| `APPLY_VERSION` | `NUMBER` |  | Version of apply that supports this column |
| `APPLY_REASON` | `VARCHAR2(40)` |  | Reason why this column is not supported by apply |

See Also:

" [DBA\_STREAMS\_COLUMNS](DBA_STREAMS_COLUMNS.md) "