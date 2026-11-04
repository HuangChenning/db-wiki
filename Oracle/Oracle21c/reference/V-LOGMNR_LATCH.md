---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-LOGMNR_LATCH.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.53 V$LOGMNR\_LATCH

`V$LOGMNR_LATCH` can be joined with the `V$LATCH` and the `V$LATCH_CHILDREN` views to obtain statistics about different latches used by active LogMiner persistent sessions.

A persistent LogMiner session is created either by starting Data Guard SQL Apply on a logical standby database for the first time or by creating a Replication capture.

| Column | Datatype | Description |
| --- | --- | --- |
| `SESSION_ID` | `NUMBER` | Unique identifier of the LogMiner persistent session |
| `NAME` | `VARCHAR2(32)` | Name of the Latch:  - `LogMiner internal state` - Identifies the latch that protects communications between the LogMiner `READER`, `PREPARER`, and `BUILDER` processes - `LogMiner memory allocation` - Identifies the latch that protects all memory allocation and deallocation inside LogMiner - `LogMiner transaction list` - Identifies the latch that protects interaction between the LogMiner layer and its clients during Data Guard SQL Apply on a logical standby database |
| `CHILD_ADDR` | `RAW(4 \| 8)` | Address of the child latch object. This column matches the corresponding `ADDR` column in the `V$LATCH_CHLDREN` view |
| `STATE` | `VARCHAR2(6)` | State of the Latch:  - `UNINIT` - The latch structure is uninitialized; that is, it is not currently assigned to any LogMiner persistent session - `READY` - The latch structure is being used by a persistent LogMiner session |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

- " [V$LATCH](V-LATCH.md) "
- " [V$LATCH\_CHILDREN](V-LATCH_CHILDREN.md) "