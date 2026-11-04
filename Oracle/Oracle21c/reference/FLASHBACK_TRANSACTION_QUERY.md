---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/FLASHBACK_TRANSACTION_QUERY.html
tags:
  - oracle
  - 21c
  - reference
---

## 7.189 FLASHBACK\_TRANSACTION\_QUERY

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

See Also:

[Oracle Database Utilities](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=SUTIL1584) for information on how to enable minimal supplemental logging