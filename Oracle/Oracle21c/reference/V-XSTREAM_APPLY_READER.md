---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-XSTREAM_APPLY_READER.html
tags:
  - oracle
  - 21c
  - reference
---

## 10.138 V$XSTREAM\_APPLY\_READER

The apply reader is a process which reads (dequeues) messages from the queue, computes message dependencies, and builds transactions. It passes the transactions on to the coordinator in commit order for assignment to the apply servers. An apply reader is a subcomponent of an apply process, outbound server, or inbound server.

| Column | Datatype | Description |
| --- | --- | --- |
| `SID` | `NUMBER` | Session ID of the reader's session |
| `SERIAL#` | `NUMBER` | Serial number of the reader's session |
| `APPLY#` | `NUMBER` | Apply process number. An apply process is an Oracle background process, prefixed by `ap`. |
| `APPLY_NAME` | `VARCHAR2(128)` | Name of the apply process |
| `STATE` | `VARCHAR2(36)` | Shows the state of the apply reader and the hash server. The possible values include:  - `INITIALIZING` - Starting up - `IDLE` - Performing no work - `DEQUEUE MESSAGES` - Dequeuing messages from the queue - `SCHEDULE MESSAGES` - Computing dependencies between messages and assembling messages into transactions - `SPILLING` - Spilling unapplied messages from memory to hard disk - `PAUSED - WAITING FOR DDL TO COMPLETE` - Waiting for a data definition language (DDL) logical change record (LCR) to be applied  The state of the apply reader is displayed first, followed by the state of the hash server. A semicolon separates the apply reader state from the hash server state. |
| `TOTAL_MESSAGES_DEQUEUED` | `NUMBER` | Total number of messages dequeued since the apply process was last started |
| `TOTAL_MESSAGES_SPILLED` | `NUMBER` | Number of messages spilled by the reader since the apply process was last started |
| `DEQUEUE_TIME` | `DATE` | Time when the last message was received |
| `DEQUEUED_MESSAGE_NUMBER` | `NUMBER` | Number of the last message received |
| `DEQUEUED_MESSAGE_CREATE_TIME` | `DATE` | For captured messages, creation time at the source database of the last message received. For user-enqueued messages, time when the message was enqueued into the queue at the local database. |
| `SGA_USED` | `NUMBER` | Amount (in bytes) of SGA memory used by the apply process since it was last started |
| `ELAPSED_DEQUEUE_TIME` | `NUMBER` | Time elapsed (in hundredths of a second) dequeuing messages since the apply process was last started |
| `ELAPSED_SCHEDULE_TIME` | `NUMBER` | Time elapsed (in hundredths of a second) scheduling messages since the apply process was last started. Scheduling includes computing dependencies between messages and assembling messages into transactions. |
| `ELAPSED_SPILL_TIME` | `NUMBER` | Elapsed time (in hundredths of a second) spent spilling messages since the apply process was last started |
| `OLDEST_SCN_NUM` | `NUMBER` | Oldest SCN |
| `OLDEST_XIDUSN` | `NUMBER` | Transaction ID undo segment number of the oldest transaction that either has been applied or is being applied |
| `OLDEST_XIDSLT` | `NUMBER` | Transaction ID slot number of the oldest transaction that either has been applied or is being applied |
| `OLDEST_XIDSQN` | `NUMBER` | Transaction ID sequence number of the oldest transaction that either has been applied or is being applied |
| `SPILL_LWM_SCN` | `NUMBER` | Spill low-watermark SCN |
| `PROXY_SID` | `NUMBER` | When the apply process uses combined capture and apply, the session ID of the propagation receiver that is responsible for direct communication between capture and apply. If the apply process does not use combined capture and apply, then this column is `0`. |
| `PROXY_SERIAL` | `NUMBER` | When the apply process uses combined capture and apply, the serial number of the propagation receiver that is responsible for direct communication between capture and apply. If the apply process does not use combined capture and apply, then this column is `0`. |
| `PROXY_SPID` | `VARCHAR2(12)` | When the apply process uses combined capture and apply, the process identification number of the propagation receiver that is responsible for direct communication between capture and apply. If the apply process does not use combined capture and apply, then this column is `0`. |
| `BYTES_RECEIVED` | `NUMBER` | When the apply process uses combined capture and apply, the number of bytes received by the apply process from the capture process since the apply process last started. If the apply process does not use combined capture and apply, then this column is not populated. |
| `DEQUEUED_POSITION` | `RAW(64)` | Dequeued position. This column is populated only for an apply process that is functioning as an XStream inbound server. |
| `SPILL_LWM_POSITION` | `RAW(64)` | Spill low-watermark position. This column is populated only for an apply process that is functioning as an XStream inbound server. |
| `OLDEST_TRANSACTION_ID` | `VARCHAR2(128)` | Oldest transaction ID |
| `TOTAL_LCRS_WITH_DEP` | `NUMBER` | Total number of LCRs with row-level dependencies since the apply process last started |
| `TOTAL_LCRS_WITH_WMDEP` | `NUMBER` | Total number of LCRs with watermark dependencies since the apply process last started.  A watermark dependency occurs when an apply process must wait until the apply process's low watermark reaches a particular threshold. |
| `TOTAL_IN_MEMORY_LCRS` | `NUMBER` | Total number of LCRs currently in memory |
| `SGA_ALLOCATED` | `NUMBER` | The total amount of shared memory (in bytes) allocated from the XStreams pool for the apply process since the apply process last started |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

Note:

The `ELAPSED_SCHEDULE_TIME` column is only populated if the `TIMED_STATISTICS` initialization parameter is set to `true`, or if the `STATISTICS_LEVEL` initialization parameter is set to `TYPICAL` or `ALL`.

See Also:

- " [TIMED\_STATISTICS](TIMED_STATISTICS.md) "
- " [STATISTICS\_LEVEL](STATISTICS_LEVEL.md) "