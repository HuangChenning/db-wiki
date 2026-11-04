---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_HIST_PERSISTENT_SUBS.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.23 DBA\_HIST\_PERSISTENT\_SUBS

`DBA_HIST_PERSISTENT_SUBS` displays Oracle Database AQ persistent queue subscribers historical statistics information.

This view contains snapshots of `V$PERSISTENT_SUBSCRIBERS`.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` | `NOT NULL` | Unique snapshot ID |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID for the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` | `NOT NULL` | Instance number for the snapshot |
| `QUEUE_SCHEMA` | `VARCHAR2(128)` | `NOT NULL` | Owner of the queue |
| `QUEUE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the queue |
| `SUBSCRIBER_ID` | `NUMBER` | `NOT NULL` | Internal subscriber number |
| `SUBSCRIBER_NAME` | `VARCHAR2(128)` |  | Name of the subscriber |
| `SUBSCRIBER_ADDRESS` | `VARCHAR2(1024)` |  | Address of the subscribing agent |
| `SUBSCRIBER_TYPE` | `VARCHAR2(128)` |  | Type of the subscriber:  - `PROXY` - Propagation subscriber - `SUBSCRIBER` - Normal subscriber - `RECIPIENT` - Recipient |
| `FIRST_ACTIVITY_TIME` | `TIMESTAMP(6)` |  | First subscriber activity time since database startup |
| `ENQUEUED_MSGS` | `NUMBER` |  | Number of messages enqueued since `FIRST_ACTIVITY_TIME` |
| `DEQUEUED_MSGS` | `NUMBER` |  | Number of messages dequeued since `FIRST_ACTIVITY_TIME` |
| `AVG_MSG_AGE` | `NUMBER` |  | Average age of messages in the queue |
| `BROWSED_MSGS` | `NUMBER` |  | Number of messages that have been browsed |
| `EXPIRED_MSGS` | `NUMBER` |  | Number of messages expired since `FIRST_ACTIVITY_TIME` |
| `DEQUEUED_MSG_LATENCY` | `NUMBER` |  | Last dequeued message latency (in seconds) |
| `LAST_ENQUEUE_TIME` | `TIMESTAMP(6)` |  | Timestamp of the last enqueued message |
| `LAST_DEQUEUE_TIME` | `TIMESTAMP(6)` |  | Timestamp of the last dequeued message |
| `ELAPSED_DEQUEUE_TIME` | `NUMBER` |  | Total time spent in dequeue (in hundredths of a second) |
| `DEQUEUE_CPU_TIME` | `NUMBER` |  | Total CPU time for dequeue (in hundredths of a second) |
| `DEQUEUE_TRANSACTIONS` | `NUMBER` |  | Number of dequeue transactions |
| `EXECUTION_COUNT` | `NUMBER` |  | Number of executions of the dequeue index cursor |
| `CON_DBID` | `NUMBER` |  | The database ID of the PDB for the sampled session |
| `CON_ID` | `NUMBER` |  | The ID of the container that `CON_DBID` identifies. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

" [V$PERSISTENT\_SUBSCRIBERS](V-PERSISTENT_SUBSCRIBERS.md) "