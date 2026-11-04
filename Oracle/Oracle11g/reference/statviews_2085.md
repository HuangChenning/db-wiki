---
title: ALL_STREAMS_STMTS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2085.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_STREAMS_STMTS` displays information about the statements in all statement DML handlers in the database.

Related View

`DBA_STREAMS_STMTS` displays information about the statements in all statement DML handlers in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `HANDLER_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the statement handler |
| `EXECUTION_SEQUENCE` | `NUMBER` | `NOT NULL` | Execution sequence of the statement |
| `STATEMENT` | `CLOB` |  | Text of the statement |
| `CREATION_TIME` | `TIMESTAMP(6)` |  | Timestamp for statement creation |
| `MODIFICATION_TIME` | `TIMESTAMP(6)` |  | Timestamp for statement modification |

See Also:

["DBA\_STREAMS\_STMTS"](statviews_5018.md)

Note:

The `ALL_STREAMS_STMTS` view is not available starting with Oracle Database 11g Release 2 (11.2.0.2).