---
title: ALL_SYNC_CAPTURE_PREPARED_TABS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2098.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_SYNC_CAPTURE_PREPARED_TABS` displays information about the tables accessible to the current user that are prepared for synchronous capture instantiation.

Related View

`DBA_SYNC_CAPTURE_PREPARED_TABS` displays information about all tables in the database that are prepared for synchronous capture instantiation.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `TABLE_OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the table prepared for synchronous capture instantiation |
| `TABLE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the table prepared for synchronous capture instantiation |
| `SCN` | `NUMBER` | `NOT NULL` | SCN from which changes can be captured |
| `TIMESTAMP` | `DATE` |  | Time at which the table was ready to be instantiated |

See Also:

["DBA\_SYNC\_CAPTURE\_PREPARED\_TABS"](statviews_5038.md)