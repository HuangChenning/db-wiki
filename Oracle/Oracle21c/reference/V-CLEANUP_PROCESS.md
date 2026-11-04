---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-CLEANUP_PROCESS.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.124 V$CLEANUP\_PROCESS

`V$CLEANUP_PROCESS` provides information on the PMON processes.

| Column | Datatype | Description |
| --- | --- | --- |
| `NAME` | `VARCHAR2(5)` | Name of the cleanup process (PMON, CLMN, CL\*\*) |
| `PADDR` | `RAW(8)` | Process pointer for the cleanup process (can join with `V$PROCESS`) |
| `SADDR` | `RAW(8)` | Session pointer for the cleanup process (can join with `V$SESSION`) |
| `STATE` | `VARCHAR2(4)` | Cleanup process state:  - `IDLE`: Not currently performing cleanup - `BUSY`: Currently performing cleanup |
| `DEAD_IN_CLEANUP` | `RAW(8)` | Pointer to the root of the tree in cleanup (can join with `ROOT_ADDR` in `V$DEAD_CLEANUP`) |
| `CLEANUP_TIME` | `NUMBER` | If `STATE` = `BUSY`, the time spent in the current cleanup attempt (in seconds). Otherwise, `0`. |
| `TIME_SINCE_LAST_CLEANUP` | `NUMBER` | If `STATE` = `IDLE`, time since last needed to perform cleanup (in seconds). Otherwise, `0`. |
| `NUM_CLEANED` | `NUMBER` | Number of trees cleaned up by the cleanup process. Increased by one every time a root tree is attempted. |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire multitenant container database (CDB). This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

" [V$DEAD\_CLEANUP](V-DEAD_CLEANUP.md) "