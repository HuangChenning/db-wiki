---
title: ALL_CAPTURE
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1025.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_CAPTURE` displays information about the capture processes that enqueue the captured changes into queues accessible to the current user.

Related View

`DBA_CAPTURE` displays information about all capture processes in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `CAPTURE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the capture process |
| `QUEUE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the queue used for staging captured changes |
| `QUEUE_OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the queue used for staging captured changes |
| `RULE_SET_NAME` | `VARCHAR2(30)` |  | Name of the positive rule set used by the capture process for filtering |
| `RULE_SET_OWNER` | `VARCHAR2(30)` |  | Owner of the positive rule set |
| `CAPTURE_USER` | `VARCHAR2(30)` |  | Current user who is enqueuing captured messages |
| `START_SCN` | `NUMBER` |  | System change number (SCN) from which the capture process will start to capture changes |
| `STATUS` | `VARCHAR2(8)` |  | Status of the capture process: - `DISABLED` - `ENABLED` - `ABORTED` |
| `CAPTURED_SCN` | `NUMBER` |  | System change number (SCN) of the last redo log record scanned |
| `APPLIED_SCN` | `NUMBER` |  | System change number (SCN) of the most recent message dequeued by the relevant apply processes. All changes below this SCN have been dequeued by all apply processes that apply changes captured by this capture process. |
| `USE_DATABASE_LINK` | `VARCHAR2(3)` |  | Indicates whether the source database name is used as the database link to connect to the source database from the downstream database (`YES`) or not (`NO`). If the capture process was created at the source database, then this column will be NULL. |
| `FIRST_SCN` | `NUMBER` |  | System change number (SCN) from which the capture process can be restarted |
| `SOURCE_DATABASE` | `VARCHAR2(128)` |  | Global name of the source database |
| `SOURCE_DBID` | `NUMBER` |  | Database ID of the source database |
| `SOURCE_RESETLOGS_SCN` | `NUMBER` |  | Resetlogs system change number (SCN) of the source database |
| `SOURCE_RESETLOGS_TIME` | `NUMBER` |  | Resetlogs time of the source database |
| `LOGMINER_ID` | `NUMBER` |  | Session ID of the LogMiner session associated with the capture process |
| `NEGATIVE_RULE_SET_NAME` | `VARCHAR2(30)` |  | Name of the negative rule set used by the capture process for filtering |
| `NEGATIVE_RULE_SET_OWNER` | `VARCHAR2(30)` |  | Owner of the negative rule set used by the capture process for filtering |
| `MAX_CHECKPOINT_SCN` | `NUMBER` |  | System change number (SCN) at which the last checkpoint was taken by the capture process |
| `REQUIRED_CHECKPOINT_SCN` | `NUMBER` |  | Lowest checkpoint SCN for which the capture process requires redo information |
| `LOGFILE_ASSIGNMENT` | `VARCHAR2(8)` |  | Logfile assignment type for the capture process: - `IMPLICIT` - `EXPLICIT` |
| `STATUS_CHANGE_TIME` | `DATE` |  | Time that the `STATUS` of the capture process was changed |
| `ERROR_NUMBER` | `NUMBER` |  | Error number if the capture process was aborted |
| `ERROR_MESSAGE` | `VARCHAR2(4000)` |  | Error message if the capture process was aborted |
| `VERSION` | `VARCHAR2(64)` |  | Version number of the capture process |
| `CAPTURE_TYPE` | `VARCHAR2(10)` |  | Type of the capture process: - `DOWNSTREAM` - `LOCAL` |
| `LAST_ENQUEUED_SCN` | `NUMBER` |  | Last enqueued system change number (SCN) |
| `CHECKPOINT_RETENTION_TIME` | `NUMBER` |  | Checkpoint retention time  Note: When the checkpoint retention time for a capture process is set to `INFINITE`, then the value displayed in this column is 4294967295. |
| `START_TIME` <sup>Foot 1</sup> | `TIMESTAMP(6)` |  | Time from which the capture process will start to capture changes |
| `PURPOSE` <sup>Footref 1</sup> | `VARCHAR2(19)` |  | Purpose of the capture process: - `Streams` - A capture process in an Oracle Streams configuration - `XStream` `Streams` - A capture process in an Oracle Streams configuration with XStream capabilities enabled by the `DBMS_XSTREAM_ADM`.`ENABLE_GG_XSTREAM_FOR_STREAMS` procedure - `XStream` `Out` - A capture process in an XStream Out configuration - `AUDIT` `VAULT` - A capture process in an audit vault configuration - `CHANGE` `DATA` `CAPTURE` - A capture process in a change data capture configuration |
| `CLIENT_NAME` <sup>Foot 2</sup> | `VARCHAR2(4000)` |  | Client name of the capture process. This is the outbound name for XStream Out, and the extract name for GoldenGate. |
| `CLIENT_STATUS` <sup>Footref 2</sup> | `VARCHAR2(8)` |  | Status of the client process: - `DISABLED` - For XStream Out if the outbound server is not running; for GoldenGate if the capture process is not running - `DETACHED` - For XStream Out if the outbound server is running, but the XStream client application is not attached to it; For GoldenGate if the capture process is running, but the extract process is not attached to it - `ATTACHED` - For XStream out if the outbound server is running and the XStream client application is attached to it; For GoldenGate if the capture process is running and the extract process is attached to it - `ABORTED` - For XStream out if the outbound server became disabled because it encountered an error; for GoldenGate if the capture process became disabled because it encountered an error |
| `OLDEST_SCN` <sup>Footref 2</sup> | `NUMBER` |  | Oldest SCN of the transactions currently being processed |
| `FILTERED_SCN<sup>Footref&nbsp;2</sup>` | `NUMBER` |  | SCN of the low watermark transaction processed |

<sup>Footnote 1</sup> This column is available starting with Oracle Database 11g Release 2 (11.2.0.2).

<sup>Footnote 2</sup> This column is available starting with Oracle Database 11g Release 2 (11.2.0.4)

See Also:

["DBA\_CAPTURE"](statviews_3097.md)