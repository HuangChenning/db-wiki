---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_DML_LOCKS.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.293 DBA\_DML\_LOCKS

`DBA_DML_LOCKS` lists all DML locks held in the database and all outstanding requests for a DML lock.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SESSION_ID` | `NUMBER` |  | Session holding or acquiring the lock |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the lock |
| `NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the lock |
| `MODE_HELD` | `VARCHAR2(13)` |  | The type of lock held. The values are:  - `ROWS_S` (`SS`): row share lock - `ROW-X` (`SX`): row exclusive lock - `SHARE` (`S`): share lock - `S/ROW-X` (`SSX`): exclusive lock - `NONE`: lock requested but not yet obtained |
| `MODE_REQUESTED` | `VARCHAR2(13)` |  | Lock request type. The values are:  - `ROWS_S` (`SS`): row share lock - `ROW-X` (`SX`): row exclusive lock - `SHARE` (`S`): share lock - `S/ROW-X` (`SSX`): exclusive lock - `NONE`: Lock identifier obtained; lock not held or requested |
| `LAST_CONVERT` | `NUMBER` |  | Time since current mode was granted |
| `BLOCKING_OTHERS` | `VARCHAR2(40)` |  | Blocking others |

See Also:

[Oracle Database Concepts](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=CNCPT1342) for more information about lock modes for table locks