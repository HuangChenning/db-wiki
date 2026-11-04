---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_CAPTURE.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.117 ALL\_CAPTURE

`ALL_CAPTURE` displays information about the capture processes that enqueue the captured changes into queues accessible to the current user.

Related View

`DBA_CAPTURE` displays information about all capture processes in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `CAPTURE_NAME` | `VARCHAR2(128)` |  | Name of the capture process |
| `QUEUE_NAME` | `VARCHAR2(128)` |  | Name of the queue used for staging captured changes |
| `QUEUE_OWNER` | `VARCHAR2(128)` |  | Owner of the queue used for staging captured changes |
| `RULE_SET_NAME` | `VARCHAR2(128)` |  | Name of the positive rule set used by the capture process for filtering |
| `RULE_SET_OWNER` | `VARCHAR2(128)` |  | Owner of the positive rule set |
| `CAPTURE_USER` | `VARCHAR2(128)` |  | Current user who is enqueuing captured messages |
| `START_SCN` | `NUMBER` |  | System change number (SCN) from which the capture process will start to capture changes. `START_SCN` is only modified as the result of an `ALTER_CAPTURE` statement or if the `FIRST_SCN` moves beyond the existing `START_SCN`. |
| `STATUS` | `VARCHAR2(8)` |  | Status of the capture process:  - `DISABLED` - `ENABLED` - `ABORTED` |
| `CAPTURED_SCN` | `NUMBER` |  | System change number (SCN) of the last redo log record scanned |
| `APPLIED_SCN` | `NUMBER` |  | System change number (SCN) of the most recent message dequeued by the relevant apply processes. All changes below this SCN have been dequeued by all apply processes that apply changes captured by this capture process. |
| `USE_DATABASE_LINK` | `VARCHAR2(3)` |  | Indicates whether the source database name is used as the database link to connect to the source database from the downstream database (`YES`) or not (`NO`). If the capture process was created at the source database, then this column will be NULL. |
| `FIRST_SCN` | `NUMBER` |  | System change number (SCN) from which the capture process can be restarted. `FIRST_SCN` indicates the lowest SCN to which the capture can be repositioned. |
| `SOURCE_DATABASE` | `VARCHAR2(128)` |  | Global name of the source database |
| `SOURCE_DBID` | `NUMBER` |  | Database ID of the source database |
| `SOURCE_RESETLOGS_SCN` | `NUMBER` |  | Resetlogs system change number (SCN) of the source database |
| `SOURCE_RESETLOGS_TIME` | `NUMBER` |  | Resetlogs time of the source database |
| `LOGMINER_ID` | `NUMBER` |  | Session ID of the Oracle LogMiner session associated with the capture process |
| `NEGATIVE_RULE_SET_NAME` | `VARCHAR2(128)` |  | Name of the negative rule set used by the capture process for filtering |
| `NEGATIVE_RULE_SET_OWNER` | `VARCHAR2(128)` |  | Owner of the negative rule set used by the capture process for filtering |
| `MAX_CHECKPOINT_SCN` | `NUMBER` |  | System change number (SCN) at which the last checkpoint was taken by the capture process |
| `REQUIRED_CHECKPOINT_SCN` | `NUMBER` |  | Lowest checkpoint SCN for which the capture process requires redo information.  Note: This SCN value does not necessarily correspond with a checkpoint SCN value. |
| `LOGFILE_ASSIGNMENT` | `VARCHAR2(8)` |  | Logfile assignment type for the capture process:  - `IMPLICIT` - `EXPLICIT` |
| `STATUS_CHANGE_TIME` | `DATE` |  | Time that the `STATUS` of the capture process was changed |
| `ERROR_NUMBER` | `NUMBER` |  | Error number if the capture process was terminated |
| `ERROR_MESSAGE` | `VARCHAR2(4000)` |  | Error message if the capture process was terminated |
| `VERSION` | `VARCHAR2(64)` |  | Version number of the capture process |
| `CAPTURE_TYPE` | `VARCHAR2(10)` |  | Type of the capture process:  - `DOWNSTREAM` - `LOCAL` |
| `LAST_ENQUEUED_SCN` | `NUMBER` |  | Last enqueued system change number (SCN) |
| `CHECKPOINT_RETENTION_TIME` | `NUMBER` |  | Checkpoint retention time  Note: When the checkpoint retention time for a capture process is set to `INFINITE`, then the value displayed in this column is 4294967295. |
| `START_TIME` | `TIMESTAMP(6)` |  | Time from which the capture process will start to capture changes. `START_TIME` is related to `START_SCN` and can only be modified by an `ALTER_CAPTURE` statement.  You can modify either `START_SCN` or `START_TIME`, but not both at the same time. |
| `PURPOSE` | `VARCHAR2(19)` |  | Purpose of the capture process:  - `GoldenGate Capture` - A capture process configured using Oracle GoldenGate Extract in integrated capture mode - `XStream` `Out` - A capture process in an XStream Out configuration - `AUDIT` `VAULT` - A capture process in an audit vault configuration |
| `SOURCE_ROOT_NAME` | `VARCHAR2(128)` |  | The global name of the source root database |
| `CLIENT_NAME` | `VARCHAR2(4000)` |  | Client name of the capture process. This is the outbound name for XStream Out, and the extract name for GoldenGate. |
| `CLIENT_STATUS` | `VARCHAR2(8)` |  | Status of the client process:  - `DISABLED` - For XStream Out if the outbound server is not running; for GoldenGate if the capture process is not running - `DETACHED` - For XStream Out if the outbound server is running, but the XStream client application is not attached to it; For GoldenGate if the capture process is running, but the extract process is not attached to it - `ATTACHED` - For XStream out if the outbound server is running and the XStream client application is attached to it; For GoldenGate if the capture process is running and the extract process is attached to it - `ABORTED` - For XStream out if the outbound server became disabled because it encountered an error; for GoldenGate if the capture process became disabled because it encountered an error |
| `OLDEST_SCN` | `NUMBER` |  | Oldest SCN of the transactions currently being processed |
| `FILTERED_SCN` | `NUMBER` |  | SCN of the low watermark transaction processed |

See Also:

- " [DBA\_CAPTURE](DBA_CAPTURE.md) "
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ARPLS70187) for more information about the `DBMS_XSTREAM_ADM.ENABLE_GG_XSTREAM_FOR_STREAMS` procedure