---
title: "V$PERSISTENT_SUBSCRIBERS"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2093.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$PERSISTENT_SUBSCRIBERS` displays information about all active subscribers of the persistent queues in the database. There is one row per instance per queue per subscriber. The rows are deleted when the database (or instance in an Oracle RAC environment) restarts.

| Column | Datatype | Description |
| --- | --- | --- |
| `QUEUE_ID` | `NUMBER` | Identifier for the queue |
| `QUEUE_SCHEMA` | `VARCHAR2(30)` | Owner of the queue |
| `QUEUE_NAME` | `VARCHAR2(30)` | Name of the queue |
| `SUBSCRIBER_ID` | `NUMBER` | Internal subscriber number |
| `SUBSCRIBER_NAME` | `VARCHAR2(30)` | Name of the subscriber |
| `SUBSCRIBER_ADDRESS` | `VARCHAR2(1024)` | Address of the subscribing agent |
| `PROTOCOL` | `NUMBER` | Protocol of the subscribing agent |
| `SUBSCRIBER_TYPE` | `VARCHAR2(30)` | Type of the subscriber: - `PROXY` - Propagation subscriber - `SUBSCRIBER` - Normal subscriber - `RECIPIENT` - Recipient |
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
| `DEQUEUE_MEMORY_LOCKS` <sup>Foot 1</sup> | `NUMBER` | Number of dequeue transactions that obtained memory locks |
| `DEQUEUE_DISK_LOCKS` <sup>Footref 1</sup> | `NUMBER` | Number of dequeue transactions that obtained disk locks |
| `DEQUEUE_DISK_DELETES` <sup>Footref 1</sup> | `NUMBER` | Number of dequeue transactions that deleted index-organized table entries |
| `OLDEST_MSGID` <sup>Footref 1</sup> | `RAW(16)` | Message ID of the oldest message |
| `OLDEST_MSG_ENQTM` <sup>Footref 1</sup> | `TIMESTAMP(6)` | Enqueue time of the oldest message |

<sup>Footnote 1</sup> This column is available starting with Oracle Database 11g Release 2 (11.2.0.2).