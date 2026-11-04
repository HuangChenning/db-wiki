---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-FAST_START_TRANSACTIONS.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.225 V$FAST\_START\_TRANSACTIONS

`V$FAST_START_TRANSACTIONS` displays information about the progress of the transactions that Oracle is recovering.

This view displays only transactions recovered in parallel. Recovery progress for serial transactions is not displayed.

| Column | Datatype | Description |
| --- | --- | --- |
| `USN` | `NUMBER` | Undo segment number of the transaction |
| `SLT` | `NUMBER` | Slot within the rollback segment |
| `SEQ` | `NUMBER` | Incarnation number of the slot |
| `STATE` | `VARCHAR2(16)` | State of the transaction (may be `TO BE RECOVERED`, `RECOVERED`, or `RECOVERING`) |
| `UNDOBLOCKSDONE` | `NUMBER` | Number of undo blocks completed on the transaction |
| `UNDOBLOCKSTOTAL` | `NUMBER` | Total number of undo blocks that need recovery |
| `PID` | `NUMBER` | ID of the current server it has been assigned to |
| `CPUTIME` | `NUMBER` | Time for which recovery has progressed (in seconds) |
| `PARENTUSN` | `NUMBER` | Undo segment number of the parent transaction in PDML |
| `PARENTSLT` | `NUMBER` | Slot of the parent transaction in PDML |
| `PARENTSEQ` | `NUMBER` | Sequence number of the parent transaction in PDML |
| `XID` | `RAW(8)` | Transaction ID |
| `PXID` | `RAW(8)` | Parent transaction ID |
| `RCVSERVERS` | `NUMBER` | Number of servers used in the last recovery |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |