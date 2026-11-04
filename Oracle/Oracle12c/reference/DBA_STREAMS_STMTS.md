---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_STREAMS_STMTS.html
tags:
  - oracle
  - 12c
  - reference
---

`DBA_STREAMS_STMTS` displays information about the statements in all Streams statement DML handlers in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `HANDLER_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the statement handler |
| `EXECUTION_SEQUENCE` | `NUMBER` | `NOT NULL` | Execution sequence of the statement |
| `STATEMENT` | `CLOB` |  | Text of the SQL statement |
| `CREATION_TIME` | `TIMESTAMP(6)` |  | Timestamp for statement creation |
| `MODIFICATION_TIME` | `TIMESTAMP(6)` |  | Timestamp for statement modification |