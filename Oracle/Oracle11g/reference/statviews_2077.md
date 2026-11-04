---
title: ALL_STREAMS_COLUMNS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2077.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_STREAMS_COLUMNS` displays information about the Streams unsupported columns accessible to the current user.

Related View

`DBA_STREAMS_COLUMNS` displays information about all Streams unsupported columns in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` |  | Owner of the table |
| `TABLE_NAME` | `VARCHAR2(30)` |  | Name of the table |
| `COLUMN_NAME` | `VARCHAR2(30)` |  | Name of the column |
| `SYNC_CAPTURE_VERSION` | `NUMBER` |  | Version of the synchronous capture that supports this column |
| `SYNC_CAPTURE_REASON` | `VARCHAR2(39)` |  | Reason why this column is not supported by synchronous capture |
| `APPLY_VERSION` | `NUMBER` |  | Version of apply that supports this column |
| `APPLY_REASON` | `VARCHAR2(40)` |  | Reason why this column is not supported by apply |

See Also:

["DBA\_STREAMS\_COLUMNS"](statviews_5003.md)