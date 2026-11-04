---
title: DBA_HIST_PERSISTENT_SUBS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4021.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_HIST_PERSISTENT_SUBS` displays STREAMS AQ persistent queue subscribers historical statistics information. This view contains snapshots of `V$PERSISTENT_SUBSCRIBERS`.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` | `NOT NULL` | Unique snapshot ID |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID for the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` | `NOT NULL` | Instance number for the snapshot |
| `QUEUE_SCHEMA` | `VARCHAR2(30)` | `NOT NULL` | Owner of the queue |
| `QUEUE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the queue |
| `SUBSCRIBER_ID` | `NUMBER` | `NOT NULL` | Internal subscriber number |
| `SUBSCRIBER_NAME` | `VARCHAR2(30)` |  | Name of the subscriber |
| `SUBSCRIBER_ADDRESS` | `VARCHAR2(1024)` |  | Address of the subscribing agent |
| `SUBSCRIBER_TYPE` | `VARCHAR2(30)` |  | Type of the subscriber: - `PROXY` - Propagation subscriber - `SUBSCRIBER` - Normal subscriber - `RECIPIENT` - Recipient |
| `FIRST_ACTIVITY_TIME` | `TIMESTAMP(6)` |  | First subscriber activity time since database startup |
| `ENQUEUED_MSGS` | `NUMBER` |  | Number of messages enqueued since `FIRST_ACTIVITY_TIME` |
| `DEQUEUED_MSGS` | `NUMBER` |  | Number of messages dequeued since `FIRST_ACTIVITY_TIME` |
| `AVG_MSG_AGE` <sup>Foot 1</sup> | `NUMBER` |  | Average age of messages in the queue |
| `BROWSED_MSGS` <sup>Footref 1</sup> | `NUMBER` |  | Number of messages that have been browsed |
| `EXPIRED_MSGS` | `NUMBER` |  | Number of messages expired since `FIRST_ACTIVITY_TIME` |
| `DEQUEUED_MSG_LATENCY` | `NUMBER` |  | Last dequeued message latency (in seconds) |
| `LAST_ENQUEUE_TIME` | `TIMESTAMP(6)` |  | Timestamp of the last enqueued message |
| `LAST_DEQUEUE_TIME` | `TIMESTAMP(6)` |  | Timestamp of the last dequeued message |
| `ELAPSED_DEQUEUE_TIME` <sup>Footref 1</sup> | `NUMBER` |  | Total time spent in dequeue (in hundredths of a second) |
| `DEQUEUE_CPU_TIME` <sup>Footref 1</sup> | `NUMBER` |  | Total CPU time for dequeue (in hundredths of a second) |
| `DEQUEUE_TRANSACTIONS` <sup>Footref 1</sup> | `NUMBER` |  | Number of dequeue transactions |
| `EXECUTION_COUNT` <sup>Footref 1</sup> | `NUMBER` |  | Number of executions of the dequeue index cursor |

<sup>Footnote 1</sup> This column is available starting with Oracle Database 11g Release 2 (11.2.0.2).