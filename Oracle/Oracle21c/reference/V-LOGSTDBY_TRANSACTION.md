---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-LOGSTDBY_TRANSACTION.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.64 V$LOGSTDBY\_TRANSACTION

`V$LOGSTDBY_TRANSACTION` displays all transactions that are actively being processed by SQL Apply.

The transaction identifiers shown in this view are those mined from the redo stream and correspond to transaction identifiers assigned at the primary database, and do not correspond to the transactions that are active at the logical standby database. For information regarding transactions active in the logical standby database, including those created as part of SQL Apply, query the `V$TRANSACTION` view at the logical standby database.

| Column | Datatype | Description |
| --- | --- | --- |
| `PRIMARY_XIDUSN` | `NUMBER` | Undo segment number of the transaction |
| `PRIMARY_XIDSLT` | `NUMBER` | Slot number of the transaction |
| `PRIMARY_XIDSQN` | `NUMBER` | Sequence number of the transaction |
| `PRIMARY_XID` | `RAW(8)` | Transaction ID |
| `PRIMARY_START_SCN` | `NUMBER` | Start system change number (SCN) base |
| `PRIMARY_START_TIME` | `DATE` | Start time |
| `PRIMARY_PARENT_XIDUSN` | `NUMBER` | Undo segment number of the parent transaction |
| `PRIMARY_PARENT_XIDSLT` | `NUMBER` | Slot number of the parent transaction |
| `PRIMARY_PARENT_XIDSQN` | `NUMBER` | Sequence number of the parent transaction |
| `PRIMARY_PARENT_XID` | `RAW(8)` | Transaction ID of the parent transaction (PDML) |
| `TYPE` | `VARCHAR2(32)` | Type:  - `PL/SQL` - Transaction was done as part of a supported PL/SQL procedure - `Direct Path Load` - Transaction is a direct path load - `CTAS` - Transaction contains at least one `CREATE TABLE ... AS SELECT` operation - `DDL` - Transaction contains one or more DDL operations - `PDML Child` - Transaction is a child transaction - `DML` - Transaction contains only DML operations |
| `MINING_STATUS` | `VARCHAR2(32)` | Mining status:  - `ACTIVE` - Transaction is still being mined by LogMiner. At least part of this transaction is ready to be applied or has already been applied. - `COMPLETE` - Transaction is complete and ready to be applied. LogMiner has finished mining. |
| `SRC_CON_ID` | `NUMBER` | Contains the PDB ID (the `PDB_ID` column from the `DBA_PDBS` view) of the source database that generated the change for this transaction. |
| `APPLY_STATUS` | `VARCHAR2(6)` | - `ACTIVE` - Transaction has been assigned to an apply server. It is in one of the following states: 	\- The transaction is being actively applied 	\- The transaction is being held by an apply server waiting for certain events to occur 	\- The transaction is being held by an apply server waiting for subsequent parts of this transaction - `NONE` - Transaction has not yet been assigned to an apply server |
| `SID` | `NUMBER` | Session ID of the apply server's session; Null if `APPLY_STATUS` is `NONE` |
| `SERIAL#` | `NUMBER` | Serial number of the apply server's session; Null if `APPLY_STATUS` is `NONE` |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

" [V$TRANSACTION](V-TRANSACTION.md) "