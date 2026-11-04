---
title: "V$BUFFERED_QUEUES"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1075.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$BUFFERED_QUEUES` displays information about all buffered queues in the instance. There is one row per queue.

| Column | Datatype | Description |
| --- | --- | --- |
| `QUEUE_ID` | `NUMBER` | Identifier for the queue |
| `QUEUE_SCHEMA` | `VARCHAR2(30)` | Owner of the queue |
| `QUEUE_NAME` | `VARCHAR2(30)` | Name of the queue |
| `STARTUP_TIME` | `DATE` | Startup time |
| `NUM_MSGS` | `NUMBER` | Total number of messages currently in the buffered queue |
| `SPILL_MSGS` | `NUMBER` | Current number of overflow messages spilled to disk from the buffered queue |
| `CNUM_MSGS` | `NUMBER` | Cumulative total number of messages enqueued into the buffered queue since the database last started |
| `CSPILL_MSGS` | `NUMBER` | Cumulative total number of overflow messages spilled to disk from the buffered queue since the database last started |
| `EXPIRED_MSGS` | `NUMBER` | Number of expired messages |
| `OLDEST_MSGID` | `RAW(16)` | Message ID of the oldest message |
| `OLDEST_MSG_ENQTM` | `TIMESTAMP(3)` | Enqueue time of the oldest message |
| `QUEUE_STATE` | `VARCHAR2(25)` | Indicates whether the queue is in recovery mode (`QUEUE IS IN RECOVERY MODE`) or not (`NORMAL`) |
| `ELAPSED_ENQUEUE_TIME` | `NUMBER` | Total time spent in enqueue (in hundredths of a second) |
| `ELAPSED_DEQUEUE_TIME` | `NUMBER` | Total time spent in dequeue (in hundredths of a second) |
| `ELAPSED_TRANSFORMATION_TIME` | `NUMBER` | Total time for evaluating transformations (in hundredths of a second) |
| `ELAPSED_RULE_EVALUATION_TIME` | `NUMBER` | Total time for rule evaluations (in hundredths of a second) |
| `ENQUEUE_CPU_TIME` | `NUMBER` | Total CPU time for enqueue (in hundredths of a second) |
| `DEQUEUE_CPU_TIME` | `NUMBER` | Total CPU time for dequeue (in hundredths of a second) |
| `AVG_MSG_AGE` <sup>Foot 1</sup> | `NUMBER` | Average age of messages in the queue |
| `LAST_ENQUEUE_TIME` | `TIMESTAMP(3) WITH TIME ZONE` | Last message enqueue time |
| `LAST_DEQUEUE_TIME` | `TIMESTAMP(3) WITH TIME ZONE` | Last message dequeue time |
| `QUEUE_SIZE` <sup>Footref 1</sup> | `NUMBER` | Size of queue, which is the total number of bytes allocated for all messages and metadata |

<sup>Footnote 1</sup> This column is available starting with Oracle Database 11g Release 2 (11.2.0.2).