---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/DBA_XSTREAM_STMT_HANDLERS.html
tags:
  - oracle
  - 19c
  - reference
---

## 6.160 DBA\_XSTREAM\_STMT\_HANDLERS

`DBA_XSTREAM_STMT_HANDLERS` displays information about all XStream statement DML handlers in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `HANDLER_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the statement handler |
| `HANDLER_COMMENT` | `VARCHAR2(4000)` |  | Comment of the statement handler |
| `CREATION_TIME` | `TIMESTAMP(6)` |  | Timestamp for script creation |
| `MODIFICATION_TIME` | `TIMESTAMP(6)` |  | Timestamp for script modification |