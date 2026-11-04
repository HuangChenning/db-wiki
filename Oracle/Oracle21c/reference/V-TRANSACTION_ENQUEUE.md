---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-TRANSACTION_ENQUEUE.html
tags:
  - oracle
  - 21c
  - reference
---

## 10.122 V$TRANSACTION\_ENQUEUE

`V$TRANSACTION_ENQUEUE` displays locks owned by transaction state objects.

| Column | Datatype | Description |
| --- | --- | --- |
| `ADDR` | `RAW(4 \| 8)` | Address of lock state object |
| `KADDR` | `RAW(4 \| 8)` | Address of lock |
| `SID` | `NUMBER` | Identifier for session holding or acquiring the lock |
| `TYPE` | `VARCHAR2(2)` | Type of lock. TX indicates transaction enqueue. |
| `ID1` | `NUMBER` | Lock identifier #1 (depends on type) |
| `ID2` | `NUMBER` | Lock identifier #2 (depends on type) |
| `LMODE` | `NUMBER` | Lock mode in which the session holds the lock:  - `0` - none - `1` - null (NULL) - `2` - row-S (SS) - `3` - row-X (SX) - `4` - share (S) - `5` - S/Row-X (SSX) - `6` - exclusive (X) |
| `REQUEST` | `NUMBER` | Lock mode in which the process requests the lock:  - `0` - none - `1` - null (NULL) - `2` - row-S (SS) - `3` - row-X (SX) - `4` - share (S) - `5` - S/Row-X (SSX) - `6` - exclusive (X) |
| `CTIME` | `NUMBER` | Time since current mode was granted |
| `BLOCK` | `NUMBER` | The lock is blocking another lock |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |