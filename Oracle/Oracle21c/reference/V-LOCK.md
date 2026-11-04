---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-LOCK.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.41 V$LOCK

`V$LOCK` lists the locks currently held by the Oracle Database and outstanding requests for a lock or latch.

| Column | Datatype | Description |
| --- | --- | --- |
| `ADDR` | `RAW(4 \| 8)` | Address of lock state object |
| `KADDR` | `RAW(4 \| 8)` | Address of lock |
| `SID` | `NUMBER` | Identifier for session holding or acquiring the lock |
| `TYPE` | `VARCHAR2(2)` | Type of user or system lock  The locks on the user types are obtained by user applications. Any process that is blocking others is likely to be holding one of these locks. The user type locks are:  `TM` - DML enqueue  `TX` - Transaction enqueue  `UL` - User supplied  The system type locks are listed in Table 9-1. Be aware that not all types of locks are documented. To find a complete list of locks for the current release, query the `V$LOCK_TYPE` data dictionary view, described on " [V$LOCK\_TYPE](V-LOCK_TYPE.md) ". |
| `ID1` | `NUMBER` | Lock identifier #1 (depends on type) |
| `ID2` | `NUMBER` | Lock identifier #2 (depends on type) |
| `LMODE` | `NUMBER` | Lock mode in which the session holds the lock:  - `0` - none - `1` - null (NULL) - `2` - row-S (SS) - `3` - row-X (SX) - `4` - share (S) - `5` - S/Row-X (SSX) - `6` - exclusive (X) |
| `REQUEST` | `NUMBER` | Lock mode in which the process requests the lock:  - `0` - none - `1` - null (NULL) - `2` - row-S (SS) - `3` - row-X (SX) - `4` - share (S) - `5` - S/Row-X (SSX) - `6` - exclusive (X) |
| `CTIME` | `NUMBER` | Time since current mode was granted |
| `BLOCK` | `NUMBER` | Indicates whether the lock in question is blocking other processes. The possible values are:  - `0` - The lock is not blocking any other processes - `1` - The lock is blocking other processes - `2` - The lock is not blocking any blocked processes on the local node, but it may or may not be blocking processes on remote nodes. This value is used only in Oracle Real Application Clusters (Oracle RAC) configurations (not in single instance configurations). |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

Table 9-1 Values for the TYPE Column: System Types

| System Type | Description | System Type | Description |
| --- | --- | --- | --- |
| `AE` | Edition enqueue | MR | Media recovery |
| `AT` | Lock held for the `ALTER TABLE` statement | NA..NZ | Library cache pin instance (`A..Z` = namespace) |
| `BL` | Buffer hash table instance | `PF` | Password File |
| `CF` | Control file schema global enqueue | `PI, PS` | Parallel operation |
| `CI` | Cross-instance function invocation instance | `PR` | Process startup |
| `CU` | Cursor bind | `QA..QZ` | Row cache instance (`A..Z` = cache) |
| `DF` | datafile instance | `RT` | Redo thread global enqueue |
| `DL` | Direct loader parallel index create | `SC` | System change number instance |
| `DM` | Mount/startup db primary/secondary instance | `SM` | SMON |
| `DR` | Distributed recovery process | `SN` | Sequence number instance |
| `DX` | Distributed transaction entry | `SQ` | Sequence number enqueue |
| `FS` | File set | `SS` | Sort segment |
| `HW` | Space management operations on a specific segment | `ST` | Space transaction enqueue |
| `IN` | Instance number | `SV` | Sequence number value |
| `IR` | Instance recovery serialization global enqueue | `TA` | Generic enqueue |
| `IS` | Instance state | `TS` | Temporary segment enqueue (ID2=0) |
| `IV` | Library cache invalidation instance | `TS` | New block allocation enqueue (ID2=1) |
| `JQ` | Job queue | `TT` | Temporary table enqueue |
| `KK` | Thread kick | `UN` | User name |
| `LA .. LP` | Library cache lock instance lock (A..P = namespace) | `US` | Undo segment DDL |
| `MM` | Mount definition global enqueue | `WL` | Being-written redo log instance |