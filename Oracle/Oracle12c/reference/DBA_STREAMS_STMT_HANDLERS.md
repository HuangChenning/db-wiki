---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_STREAMS_STMT_HANDLERS.html
tags:
  - oracle
  - 12c
  - reference
---

`DBA_STREAMS_STMT_HANDLERS` displays information about all Streams statement DML handlers in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `HANDLER_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the statement handler |
| `HANDLER_COMMENT` | `VARCHAR2(4000)` |  | Comment specified with the statement handler |
| `CREATION_TIME` | `TIMESTAMP(6)` |  | Timestamp for script creation |
| `MODIFICATION_TIME` | `TIMESTAMP(6)` |  | Timestamp for script modification |