---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/FLASHBACK_TRANSACTION_QUERY.html
tags:
  - oracle
  - 19c
  - reference
---

## 6.186 FLASHBACK\_TRANSACTION\_QUERY

`FLASHBACK_TRANSACTION_QUERY` displays information about all flashback transaction queries in the database.

The database must have at least minimal supplemental logging enabled to avoid unpredictable behavior.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `XID` | `RAW(8)` |  | Transaction identifier |
| `START_SCN` | `NUMBER` |  | Transaction start system change number (SCN) |
| `START_TIMESTAMP` | `DATE` |  | Transaction start timestamp |
| `COMMIT_SCN` | `NUMBER` |  | Transaction commit system change number; NULL for active transactions |
| `COMMIT_TIMESTAMP` | `DATE` |  | Transaction commit timestamp; NULL for active transactions |
| `LOGON_USER` | `VARCHAR2(128)` |  | Logon user for the transaction |
| `UNDO_CHANGE#` | `NUMBER` |  | Undo system change number (`1` or higher) |
| `OPERATION` | `VARCHAR2(32)` |  | Forward-going DML operation performed by the transaction:  - `D` - Delete - `I` - Insert - `U` - Update - `B` - `UNKNOWN` |
| `TABLE_NAME` | `VARCHAR2(256)` |  | Name of the table to which the DML applies |
| `TABLE_OWNER` | `VARCHAR2(386)` |  | Owner of the table to which the DML applies |
| `ROW_ID` | `VARCHAR2(19)` |  | Rowid of the row that was modified by the DML |
| `UNDO_SQL` | `VARCHAR2(4000)` |  | SQL to undo the DML indicated by `OPERATION` |

Note:

Starting with Oracle Database 19c, Release Update 19.32, unified auditing records the use of the `SELECT` `ANY` `TRANSACTION` privilege when accessing `FLASHBACK_TRANSACTION_QUERY`. This feature provides administrators with more complete audit visibility for privileged access to historical transaction data.

See Also:

[Oracle Database Utilities](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/refrn&id=SUTIL1584) for information on how to enable minimal supplemental logging