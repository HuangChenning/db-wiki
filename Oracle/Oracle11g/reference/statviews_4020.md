---
title: DBA_HIST_PERSISTENT_QUEUES
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4020.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_HIST_PERSISTENT_QUEUES` displays STREAMS AQ persistent queues historical statistics information. This view contains snapshots of `V$PERSISTENT_QUEUES`.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` | `NOT NULL` | Unique snapshot ID |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID for the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` | `NOT NULL` | Instance number for the snapshot |
| `QUEUE_SCHEMA` | `VARCHAR2(30)` | `NOT NULL` | Owner of the queue |
| `QUEUE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the queue |
| `QUEUE_ID` | `NUMBER` | `NOT NULL` | Identifier for the queue |
| `FIRST_ACTIVITY_TIME` | `TIMESTAMP(6)` |  | First queue activity time since database startup |
| `ENQUEUED_MSGS` | `NUMBER` |  | Number of messages enqueued |
| `DEQUEUED_MSGS` | `NUMBER` |  | Number of messages dequeued  Note: This column will not be incremented until all the subscribers of the message have dequeued the message and its retention time has elapsed. |
| `BROWSED_MSGS` <sup>Foot 1</sup> | `NUMBER` |  | Number of messages that have been browsed |
| `ELAPSED_ENQUEUE_TIME` | `NUMBER` |  | Total time (in hundredths of a second) spent doing enqueue |
| `ELAPSED_DEQUEUE_TIME` | `NUMBER` |  | Total time (in hundredths of a second) spent doing dequeue |
| `ENQUEUE_CPU_TIME` <sup>Footref 1</sup> | `NUMBER` |  | Total CPU time for enqueue (in hundredths of a second) |
| `DEQUEUE_CPU_TIME` <sup>Footref 1</sup> | `NUMBER` |  | Total CPU time for dequeue (in hundredths of a second) |
| `AVG_MSG_AGE` <sup>Footref 1</sup> | `NUMBER` |  | Average age of messages in the queue |
| `DEQUEUED_MSG_LATENCY` <sup>Footref 1</sup> | `NUMBER` |  | Last dequeued message latency (in seconds) |
| `ELAPSED_TRANSFORMATION_TIME` | `NUMBER` |  | Total time (in hundredths of a second) spent doing transformation |
| `ELAPSED_RULE_EVALUATION_TIME` | `NUMBER` |  | Total time (in hundredths of a second) spent doing rule evaluation |
| `ENQUEUED_EXPIRY_MSGS` | `NUMBER` |  | Number of messages enqueued with expiry |
| `ENQUEUED_DELAY_MSGS` | `NUMBER` |  | Number of messages enqueued with delay |
| `MSGS_MADE_EXPIRED` | `NUMBER` |  | Number of messages expired by time manager |
| `MSGS_MADE_READY` | `NUMBER` |  | Number of messages made ready by time manager |
| `LAST_ENQUEUE_TIME` | `TIMESTAMP(6)` |  | Last message enqueue time |
| `LAST_DEQUEUE_TIME` | `TIMESTAMP(6)` |  | Last message dequeue time |
| `LAST_TM_EXPIRY_TIME` | `TIMESTAMP(6)` |  | Last time message was expired by time manager |
| `LAST_TM_READY_TIME` | `TIMESTAMP(6)` |  | Last time message was made ready by time manager |
| `ENQUEUE_TRANSACTIONS` <sup>Footref 1</sup> | `NUMBER` |  | Number of enqueue transactions |
| `DEQUEUE_TRANSACTIONS` <sup>Footref 1</sup> | `NUMBER` |  | Number of dequeue transactions |
| `EXECUTION_COUNT` <sup>Footref 1</sup> | `NUMBER` |  | Number of executions of the dequeue cursor |

<sup>Footnote 1</sup> This column is available starting with Oracle Database 11g Release 2 (11.2.0.2).