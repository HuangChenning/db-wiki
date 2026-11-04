---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-PERSISTENT_SUBSCRIBERS.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.118 V$PERSISTENT\_SUBSCRIBERS

`V$PERSISTENT_SUBSCRIBERS` displays information about all active subscribers of the persistent queues in the database.

There is one row per instance per queue per subscriber. The rows are deleted when the database (or instance in an Oracle RAC environment) restarts.

Note:

This view does not display information about sharded queues. For information about sharded queues, refer to the " [V$AQ\_SHARDED\_SUBSCRIBER\_STAT](V-AQ_SHARDED_SUBSCRIBER_STAT.md) " view.

| Column | Datatype | Description |
| --- | --- | --- |
| `QUEUE_ID` | `NUMBER` | Identifier for the queue |
| `QUEUE_SCHEMA` | `VARCHAR2(128)` | Owner of the queue |
| `QUEUE_NAME` | `VARCHAR2(128)` | Name of the queue |
| `SUBSCRIBER_ID` | `NUMBER` | Internal subscriber number |
| `SUBSCRIBER_NAME` | `VARCHAR2(512)` | Name of the subscriber |
| `SUBSCRIBER_ADDRESS` | `VARCHAR2(1024)` | Address of the subscribing agent |
| `PROTOCOL` | `NUMBER` | Protocol of the subscribing agent |
| `SUBSCRIBER_TYPE` | `VARCHAR2(128)` | Type of the subscriber:  - `PROXY` - Propagation subscriber - `SUBSCRIBER` - Normal subscriber - `RECIPIENT` - Recipient |
| `FIRST_ACTIVITY_TIME` | `TIMESTAMP(6)` | First subscriber activity time since database startup |
| `ENQUEUED_MSGS` | `NUMBER` | Number of messages enqueued since `FIRST_ACTIVITY_TIME` |
| `DEQUEUED_MSGS` | `NUMBER` | Number of messages dequeued since `FIRST_ACTIVITY_TIME` |
| `AVG_MSG_AGE` | `NUMBER` | Average age of messages in the queue |
| `BROWSED_MSGS` | `NUMBER` | Number of messages that have been browsed |
| `EXPIRED_MSGS` | `NUMBER` | Number of messages expired since `FIRST_ACTIVITY_TIME` |
| `DEQUEUED_MSG_LATENCY` | `NUMBER` | Last dequeued message latency (in seconds) |
| `LAST_ENQUEUE_TIME` | `TIMESTAMP(6)` | Timestamp of the last enqueued message |
| `LAST_DEQUEUE_TIME` | `TIMESTAMP(6)` | Timestamp of the last dequeued message |
| `ELAPSED_DEQUEUE_TIME` | `NUMBER` | Total time spent in dequeue (in hundredths of a second) |
| `DEQUEUE_CPU_TIME` | `NUMBER` | Total CPU time for dequeue (in hundredths of a second) |
| `DEQUEUE_TRANSACTIONS` | `NUMBER` | Number of dequeue transactions |
| `EXECUTION_COUNT` | `NUMBER` | Number of executions of the dequeue index cursor |
| `DEQUEUE_MEMORY_LOCKS` | `NUMBER` | Number of dequeue transactions that obtained memory locks |
| `DEQUEUE_DISK_LOCKS` | `NUMBER` | Number of dequeue transactions that obtained disk locks |
| `DEQUEUE_DISK_DELETES` | `NUMBER` | Number of dequeue transactions that deleted index-organized table entries |
| `OLDEST_MSGID` | `RAW(16)` | Message ID of the oldest message |
| `OLDEST_MSG_ENQTM` | `TIMESTAMP(6)` | Enqueue time of the oldest message |
| `PARENT_SUBSCRIBER_ID` | `NUMBER` | Subscriber ID of the parent durable subscriber |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |