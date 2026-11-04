---
title: "V$FAST_START_TRANSACTIONS"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1135.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$FAST_START_TRANSACTIONS` displays information about the progress of the transactions that Oracle is recovering.

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