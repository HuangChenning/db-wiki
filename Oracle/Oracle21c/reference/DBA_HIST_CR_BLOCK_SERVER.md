---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_HIST_CR_BLOCK_SERVER.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.393 DBA\_HIST\_CR\_BLOCK\_SERVER

`DBA_HIST_CR_BLOCK_SERVER` displays historical statistics on the Global Cache Service processes (LMS) used in cache fusion.

This view contains snapshots of `V$CR_BLOCK_SERVER`.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` | `NOT NULL` | Unique snapshot ID |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID for the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` | `NOT NULL` | Instance number for the snapshot |
| `CR_REQUESTS` | `NUMBER` |  | Number of CR blocks served due to remote CR block requests |
| `CURRENT_REQUESTS` | `NUMBER` |  | Number of current blocks served due to remote CR block requests  `CR_REQUESTS` + `CURRENT_REQUESTS` = global cache CR blocks served (from `V$SYSSTAT`). |
| `DATA_REQUESTS` | `NUMBER` |  | Number of current or CR requests for data blocks |
| `UNDO_REQUESTS` | `NUMBER` |  | Number of CR requests for undo blocks |
| `TX_REQUESTS` | `NUMBER` |  | Number of CR requests for undo segment header blocks  `DATA_REQUESTS` + `UNDO_REQUESTS` + `TX_REQUESTS` = total number of requests handled by the LMS processes |
| `CURRENT_RESULTS` | `NUMBER` |  | Number of requests for which no changes were rolled out of the block returned to the requesting instance |
| `PRIVATE_RESULTS` | `NUMBER` |  | Number of requests for which changes were rolled out of the block returned to the requesting instance, and only the requesting transaction can use the resulting CR block |
| `ZERO_RESULTS` | `NUMBER` |  | Number of requests for which changes were rolled out of the block returned to the requesting instance. Only zero-XID transactions can use the block. |
| `DISK_READ_RESULTS` | `NUMBER` |  | Number of requests for which the requesting instance had to read the requested block from disk |
| `FAIL_RESULTS` | `NUMBER` |  | Number of requests that failed; the requesting transaction must reissue the request |
| `FAIRNESS_DOWN_CONVERTS` | `NUMBER` |  | Number of times an instance receiving a request has down-converted an X lock on a block because it was not modifying the block |
| `FLUSHES` | `NUMBER` |  | Number of times the log has been flushed by an LMS process |
| `FLUSHES` | `NUMBER` |  | Number of times the log has been flushed by an LMS process |
| `BUILDS` | `NUMBER` |  | Number of requests for which the server had to fabricate a CR block |
| `LIGHT_WORKS` | `NUMBER` |  | Number of times the light-work rule was evoked. This rule prevents the LMS processes from going to disk while responding to CR requests for data, undo, or undo segment header blocks. This rule can prevent the LMS process from completing its response to the CR request. |
| `ERRORS` | `NUMBER` |  | Number of times an error was signalled by an LMS process |
| `CON_DBID` | `NUMBER` |  | The database ID of the PDB for the sampled session |
| `CON_ID` | `NUMBER` |  | The ID of the container that `CON_DBID` identifies. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

" [V$CR\_BLOCK\_SERVER](V-CR_BLOCK_SERVER.md) "