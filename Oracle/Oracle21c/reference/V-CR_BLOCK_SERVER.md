---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-CR_BLOCK_SERVER.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.151 V$CR\_BLOCK\_SERVER

`V$CR_BLOCK_SERVER` displays statistics on the Global Cache Service processes (LMS) used in cache fusion.

| Column | Datatype | Description |
| --- | --- | --- |
| `CR_REQUESTS` | `NUMBER` | Number of CR blocks served due to remote CR block requests |
| `CURRENT_REQUESTS` | `NUMBER` | Number of current blocks served due to remote CR block requests  `CR_REQUESTS` + `CURRENT_REQUESTS` = global cache CR clocks served (from `V$SYSSTAT`). |
| `DATA_REQUESTS` | `NUMBER` | Number of current or CR requests for data blocks |
| `UNDO_REQUESTS` | `NUMBER` | Number of CR requests for undo blocks |
| `TX_REQUESTS` | `NUMBER` | Number of CR requests for undo segment header blocks |
| `OTHER_REQUESTS` | `NUMBER` | Number of CR requests for other types of blocks  `DATA_REQUESTS` + `UNDO_REQUESTS` + `TX_REQUESTS` + `OTHER_REQUESTS` = total number of requests handled by the LMS processes |
| `CURRENT_RESULTS` | `NUMBER` | Number of requests for which no changes were rolled out of the block returned to the requesting instance |
| `PRIVATE_RESULTS` | `NUMBER` | Number of requests for which changes were rolled out of the block returned to the requesting instance, and only the requesting transaction can use the resulting CR block |
| `ZERO_RESULTS` | `NUMBER` | Number of requests for which changes were rolled out of the block returned to the requesting instance. Only zero-XID transactions can use the block. |
| `DISK_READ_RESULTS` | `NUMBER` | Number of requests for which the requesting instance had to read the requested block from disk |
| `FAIL_RESULTS` | `NUMBER` | Number of requests that failed; the requesting transaction must reissue the request |
| `STALE` | `NUMBER` | Number of requests for which the disk read of the requested block was stale |
| `FAIRNESS_DOWN_CONVERTS` | `NUMBER` | Number of times an instance receiving a request has down-converted an X lock on a block because it was not modifying the block |
| `FAIRNESS_CLEARS` | `NUMBER` | Number of times the "fairness counter" was cleared. This counter tracks the number of times a block was modified after it was served. |
| `FREE_GC_ELEMENTS` | `NUMBER` | Number of times a request was received from another instance and the X lock had no buffers |
| `FLUSHES` | `NUMBER` | Number of times the log has been flushed by an LMS process |
| `FLUSHES_QUEUED` | `NUMBER` | Number of flushes queued by an LMS process |
| `FLUSH_QUEUE_FULL` | `NUMBER` | Number of times the flush queue was full |
| `FLUSH_MAX_TIME` | `NUMBER` | Maximum time for flush |
| `LIGHT_WORKS` | `NUMBER` | Number of times the light-work rule was evoked. This rule prevents the LMS processes from going to disk while responding to CR requests for data, undo, or undo segment header blocks. This rule can prevent the LMS process from completing its response to the CR request. |
| `ERRORS` | `NUMBER` | Number of times an error was signalled by an LMS process |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

Note:

This view contains internal diagnostic information for use by Oracle Support Services. It is subject to change without notice.