---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_QUEUE_SCHEDULES.html
tags:
  - oracle
  - 21c
  - reference
---

## 4.20 ALL\_QUEUE\_SCHEDULES

`ALL_QUEUE_SCHEDULES` describes the propagation schedules whose source queues are accessible to the current user.

Related Views

- `DBA_QUEUE_SCHEDULES` describes all propagation schedules in the database.
- `USER_QUEUE_SCHEDULES` describes the propagation schedules whose source queues are owned by the current user. This view does not display the `SCHEMA` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SCHEMA` | `VARCHAR2(128)` |  | Source queue owner |
| `QNAME` | `VARCHAR2(128)` |  | Source queue name |
| `DESTINATION` | `VARCHAR2(395)` |  | Destination name, currently limited to be a `DBLINK` name |
| `START_DATE` | `TIMESTAMP(6) WITH TIME ZONE` |  | Date at which to start propagation |
| `START_TIME` | `VARCHAR2(8)` |  | Time of day at which to start propagation (in `HH:MI:SS` format) |
| `PROPAGATION_WINDOW` | `NUMBER` |  | Duration for the propagation window (in seconds) |
| `NEXT_TIME` | `VARCHAR2(4000)` |  | Function to compute the start of the next propagation window |
| `LATENCY` | `NUMBER` |  | Maximum wait time to propagate a message during the propagation window |
| `SCHEDULE_DISABLED` | `VARCHAR2(1)` |  | Indicates whether the schedule is disabled (`Y`) or enabled (`N`). If disabled, then the schedule will not be executed. |
| `PROCESS_NAME` | `VARCHAR2(4)` |  | Name of the process executing the schedule; `NULL` if not currently executing |
| `SESSION_ID` | `VARCHAR2(82)` |  | Session ID and session serial number of the job executing this schedule (SID, SERIAL#); `NULL` if not currently executing |
| `INSTANCE` | `NUMBER` |  | Cluster database instance number executing the schedule |
| `LAST_RUN_DATE` | `TIMESTAMP(6) WITH TIME ZONE` |  | Date of the last successful execution |
| `LAST_RUN_TIME` | `VARCHAR2(8)` |  | Time of day of the last successful execution (in `HH:MI:SS` format) |
| `CURRENT_START_DATE` | `TIMESTAMP(6) WITH TIME ZONE` |  | Date at which the current window of this schedule was started |
| `CURRENT_START_TIME` | `VARCHAR2(8)` |  | Time of day at which the current window of this schedule was started (in `HH:MI:SS` format) |
| `NEXT_RUN_DATE` | `TIMESTAMP(6) WITH TIME ZONE` |  | Date at which the next window of this schedule will be started |
| `NEXT_RUN_TIME` | `VARCHAR2(8)` |  | Time of day at which the next window of this schedule will be started (in `HH:MI:SS` format) |
| `TOTAL_TIME` | `NUMBER` |  | Total time spent by the system in executing this schedule (in seconds) |
| `TOTAL_NUMBER` | `NUMBER` |  | Total number of messages propagated in this schedule |
| `TOTAL_BYTES` | `NUMBER` |  | Total number of bytes propagated in this schedule |
| `MAX_NUMBER` | `NUMBER` |  | Maximum number of messages propagated in a propagation window |
| `MAX_BYTES` | `NUMBER` |  | Maximum number of bytes propagated in a propagation window |
| `AVG_NUMBER` | `NUMBER` |  | Average number of messages propagated in a propagation window |
| `AVG_SIZE` | `NUMBER` |  | Average size of a propagated message (in bytes) |
| `AVG_TIME` | `NUMBER` |  | Average time to propagate a message (in seconds) |
| `FAILURES` | `NUMBER` |  | Number of consecutive times schedule execution has failed, if any. After 16 consecutive failures, a propagation job becomes disabled automatically. |
| `LAST_ERROR_DATE` | `DATE` |  | Date of the last unsuccessful execution |
| `LAST_ERROR_TIME` | `VARCHAR2(8)` |  | Time of day of the last unsuccessful execution (in `HH:MI:SS` format) |
| `LAST_ERROR_MSG` | `VARCHAR2(4000)` |  | Error number and error message text of the last unsuccessful execution |
| `MESSAGE_DELIVERY_MODE` | `VARCHAR2(10)` |  | Message delivery mode:  - `PERSISTENT` - `BUFFERED` |
| `ELAPSED_DEQUEUE_TIME` | `NUMBER` |  | Elapsed dequeue time (in hundredths of a second) |
| `ELAPSED_PICKLE_TIME` | `NUMBER` |  | Elapsed pickle time (time taken to linearize a logical change record (LCR) into a stream of bytes that can be sent over the network) (in hundredths of a second) |
| `JOB_NAME` | `VARCHAR2(128)` |  | Name of the Scheduler job |

See Also:

- " [DBA\_QUEUE\_SCHEDULES](DBA_QUEUE_SCHEDULES.md) "
- " [USER\_QUEUE\_SCHEDULES](USER_QUEUE_SCHEDULES.md) "