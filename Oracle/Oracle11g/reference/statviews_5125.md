---
title: FLASHBACK_TRANSACTION_QUERY
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5125.htm
tags:
  - oracle
  - 11g
  - reference
---

`FLASHBACK_TRANSACTION_QUERY` displays information about all flashback transaction queries in the database. The database must have at least minimal supplemental logging enabled to avoid unpredictable behavior.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `XID` | `RAW(8)` |  | Transaction identifier |
| `START_SCN` | `NUMBER` |  | Transaction start system change number (SCN) |
| `START_TIMESTAMP` | `DATE` |  | Transaction start timestamp |
| `COMMIT_SCN` | `NUMBER` |  | Transaction commit system change number; NULL for active transactions |
| `COMMIT_TIMESTAMP` | `DATE` |  | Transaction commit timestamp; NULL for active transactions |
| `LOGON_USER` | `VARCHAR2(30)` |  | Logon user for the transaction |
| `UNDO_CHANGE#` | `NUMBER` |  | Undo system change number (`1` or higher) |
| `OPERATION` | `VARCHAR2(32)` |  | Forward-going DML operation performed by the transaction: |
| `TABLE_NAME` | `VARCHAR2(256)` |  | Name of the table to which the DML applies |
| `TABLE_OWNER` | `VARCHAR2(32)` |  | Owner of the table to which the DML applies |
| `ROW_ID` | `VARCHAR2(19)` |  | Rowid of the row that was modified by the DML |
| `UNDO_SQL` | `VARCHAR2(4000)` |  | SQL to undo the DML indicated by `OPERATION` |

See Also:

[Oracle Database Utilities](https://docs.oracle.com/cd/E11882_01/server.112/e22490/toc.htm) for information on how to enable minimal supplemental logging