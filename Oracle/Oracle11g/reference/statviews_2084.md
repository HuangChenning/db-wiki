---
title: ALL_STREAMS_STMT_HANDLERS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2084.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_STREAMS_STMT_HANDLERS` displays information about all statement DML handlers in the database.

Related View

`DBA_STREAMS_STMT_HANDLERS` displays information about all statement DML handlers in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `HANDLER_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the statement handler |
| `HANDLER_COMMENT` | `VARCHAR2(4000)` |  | Comment specified with the statement handler |
| `CREATION_TIME` | `TIMESTAMP(6)` |  | Timestamp for script creation |
| `MODIFICATION_TIME` | `TIMESTAMP(6)` |  | Timestamp for script modification |

See Also:

["DBA\_STREAMS\_STMT\_HANDLERS"](statviews_5017.md)

Note:

The `ALL_STREAMS_STMT_HANDLERS` view is not available starting with Oracle Database 11g Release 2 (11.2.0.2).