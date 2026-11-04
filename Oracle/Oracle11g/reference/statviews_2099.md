---
title: ALL_SYNC_CAPTURE_TABLES
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2099.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_SYNC_CAPTURE_TABLES` displays information about the tables accessible to the current user that are captured by synchronous Streams captures.

Related View

`DBA_SYNC_CAPTURE_TABLES` displays information about all tables in the database that are captured by synchronous Streams captures.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `TABLE_OWNER` | `VARCHAR2(30)` |  | Owner of the synchronous capture table |
| `TABLE_NAME` | `VARCHAR2(30)` |  | Name of the synchronous capture table |
| `ENABLED` | `VARCHAR2(3)` |  | Indicates whether synchronous Streams capture is enabled for the table (`YES`) or not (`NO`) |

See Also:

["DBA\_SYNC\_CAPTURE\_TABLES"](statviews_5039.md)