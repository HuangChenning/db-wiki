---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/DBA_DDL_LOCKS.html
tags:
  - oracle
  - 19c
  - reference
---

## 4.255 DBA\_DDL\_LOCKS

`DBA_DDL_LOCKS` lists all DDL locks held in the database and all outstanding requests for a DDL lock.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SESSION_ID` | `NUMBER` |  | Session identifier |
| `OWNER` | `VARCHAR2(128)` |  | Owner of the lock |
| `NAME` | `VARCHAR2(1000)` |  | Name of the lock |
| `TYPE` | `VARCHAR2(40)` |  | Lock type:  - `Cursor` - `Table/Procedure/Type` - `Body` - `Trigger` - `Index` - `Cluster` - `Java Source` - `Java Resource` - `Java Data` |
| `MODE_HELD` | `VARCHAR2(9)` |  | Lock mode:  - `None` - `Null` - `Share` - `Exclusive` |
| `MODE_REQUESTED` | `VARCHAR2(9)` |  | Lock request type:  - `None` - `Null` - `Share` - `Exclusive` |

See Also:

[Oracle Database Concepts](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/refrn&id=CNCPT1351) for more information about DDL locks