---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/V-DEAD_CLEANUP.html
tags:
  - oracle
  - 12c
  - reference
---

`V$DEAD_CLEANUP` shows the dead processes and killed sessions present in the instance and their cleanup status.

| Column | Datatype | Description |
| --- | --- | --- |
| `TYPE` | `VARCHAR2(64)` | Indicates whether a row contains a `DEAD PROCESS` or `KILLED SESSION` |
| `PADDR` | `RAW(8)` | Process pointer. Can be joined with `V$PROCESS`. For a killed session, this is the owner of the session, which can be NULL. |
| `SADDR` | `RAW(8)` | Session pointer. Can be joined with `V$SESSION`. For a dead process, this is the user session. |
| `ROOT_ADDR` | `RAW(8)` | Pointer to the root of the tree |
| `CLEANUP_OWNER` | `VARCHAR2(64)` | Indicates which process is responsible for cleanup of this tree:  - `CLEANUP PROCESS` - a cleanup process is responsible - `OWNER PROCESS` - the root owner is responsible |
| `STATE` | `VARCHAR2(64)` | Cleanup state:  - `CLEANUP PENDING` - Occurs for a dead process / killed session that can be cleaned up, but PMON has not yet made an attempt - `IN PROGRESS` - A cleanup attempt is currently in progress - `RESOURCES FREED` - Occurs for a dead process / killed session where all children have been freed, but the process / killed session itself is not yet freed - `PARTIAL CLEANUP` - Occurs if some of the children have been cleaned up |
| `DEAD_TIME` | `NUMBER` | Time since the process was marked dead or the session was marked killed (in seconds) |
| `CLEANUP_ATTEMPTS` | `NUMBER` | Number of times PMON has attempted cleanup |
| `LAST_ATTEMPT` | `NUMBER` | How long ago the last cleanup attempt occurred (in seconds) |
| `CLEANUP_PROCESS` | `RAW(8)` | Process pointer for the cleanup process currently cleaning up this tree (can join with `V$CLEANUP_PROCESS`). It will be NULL if cleanup is not currently in progress or if the owner is responsible for cleanup. |
| `CLEANUP_TIME` | `NUMBER` | Total amount of time PMON has spent on cleanup of the process/session (in seconds) |
| `NUM_BLOCKED` | `NUMBER` | Number of sessions blocked on cleanup of this session |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

" [V$CLEANUP\_PROCESS](V-CLEANUP_PROCESS.md) "