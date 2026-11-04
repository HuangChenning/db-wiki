---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-XSTREAM_APPLY_COORDINATOR.html
tags:
  - oracle
  - 21c
  - reference
---

## 10.137 V$XSTREAM\_APPLY\_COORDINATOR

The coordinator for an apply process gets transactions from the apply process reader and passes them to apply servers. An apply process coordinator is a subcomponent of an apply process, outbound server, or inbound server.

| Column | Datatype | Description |
| --- | --- | --- |
| `SID` | `NUMBER` | Session ID of the coordinator's session |
| `SERIAL#` | `NUMBER` | Serial number of the coordinator's session |
| `STATE` | `VARCHAR2(21)` | State of the coordinator:  - `INITIALIZING` - Starting up - `IDLE` - Performing no work - `APPLYING` - Passing transactions to apply servers - `SHUTTING DOWN CLEANLY` - Stopping without an error - `ABORTING` - Stopping because of an apply error |
| `APPLY#` | `NUMBER` | Apply process number. An apply process coordinator is an Oracle background process, prefixed by `ap`. |
| `APPLY_NAME` | `VARCHAR2(128)` | Name of the apply process |
| `TOTAL_APPLIED` | `NUMBER` | Total number of transactions applied by the apply process since the apply process was last started |
| `TOTAL_WAIT_DEPS` | `NUMBER` | Number of times since the apply process was last started that an apply server waited to apply a logical change record (LCR) in a transaction until another apply server applied a transaction because of a dependency between the transactions |
| `TOTAL_WAIT_COMMITS` | `NUMBER` | Number of times since the apply process was last started that an apply server waited to commit a transaction until another apply server committed a transaction to serialize commits |
| `TOTAL_ADMIN` | `NUMBER` | Number of administrative jobs issued since the apply process was last started |
| `TOTAL_ASSIGNED` | `NUMBER` | Number of transactions assigned to apply servers since the apply process was last started |
| `TOTAL_RECEIVED` | `NUMBER` | Total number of transactions received by the coordinator process since the apply process was last started |
| `TOTAL_IGNORED` | `NUMBER` | Number of transactions which were received by the coordinator but were ignored because they had been previously applied |
| `TOTAL_ROLLBACKS` | `NUMBER` | Number of transactions which were rolled back due to unexpected contention |
| `TOTAL_ERRORS` | `NUMBER` | Number of transactions applied by the apply process that resulted in an apply error since the apply process was last started |
| `UNASSIGNED_COMPLETE_TXNS` | `NUMBER` | Total number of complete transactions that the coordinator has not assigned to any apply servers |
| `LWM_TIME` | `DATE` | Time when the message with the lowest message number was recorded. The creation time of the message with the lowest message number was also recorded at this time. |
| `LWM_MESSAGE_NUMBER` | `NUMBER` | Number of the message corresponding to the low watermark. That is, messages with a commit message number less than or equal to this message number have definitely been applied, but some messages with a higher commit message number also may have been applied. |
| `LWM_MESSAGE_CREATE_TIME` | `DATE` | For captured messages, creation time at the source database of the message corresponding to the low watermark. For user-enqueued messages, time when the message corresponding to the low watermark was enqueued into the queue at the local database. |
| `HWM_TIME` | `DATE` | Time when the message with the highest message number was recorded. The creation time of the message with the highest message number was also recorded at this time. |
| `HWM_MESSAGE_NUMBER` | `NUMBER` | Number of the message corresponding to the high watermark. That is, no messages with a commit message number greater than this message number have been applied. |
| `HWM_MESSAGE_CREATE_TIME` | `DATE` | For captured messages, creation time at the source database of the message corresponding to the high watermark. For user-enqueued messages, time when the message corresponding to the high watermark was enqueued into the queue at the local database. |
| `STARTUP_TIME` | `DATE` | Time when the apply process was last started |
| `ELAPSED_SCHEDULE_TIME` | `NUMBER` | Time elapsed (in hundredths of a second) scheduling messages since the apply process was last started |
| `ELAPSED_IDLE_TIME` | `NUMBER` | Elapsed idle time |
| `LWM_POSITION` | `RAW(64)` | Position of the low-watermark LCR |
| `HWM_POSITION` | `RAW(64)` | Position of the high-watermark LCR |
| `PROCESSED_MESSAGE_NUMBER` | `NUMBER` | Message number currently processed by the apply coordinator |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |
| `ACTIVE_SERVER_COUNT` | `NUMBER` | Active server count |

Note:

The `ELAPSED_SCHEDULE_TIME` column is only populated if the `TIMED_STATISTICS` initialization parameter is set to `true`, or if the `STATISTICS_LEVEL` initialization parameter is set to `TYPICAL` or `ALL`.

See Also:

- " [TIMED\_STATISTICS](TIMED_STATISTICS.md) "
- " [STATISTICS\_LEVEL](STATISTICS_LEVEL.md) "