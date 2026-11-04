---
title: DBA_HIST_BUFFERED_QUEUES
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_3208.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_HIST_BUFFERED_QUEUES` displays historical information about all buffered queues available for the instance.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` | `NOT NULL` | Unique snapshot ID |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID for the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` | `NOT NULL` | Instance number for the snapshot |
| `QUEUE_SCHEMA` | `VARCHAR2(30)` | `NOT NULL` | Owner of the queue |
| `QUEUE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the queue |
| `STARTUP_TIME` | `DATE` | `NOT NULL` | Startup time of the instance |
| `QUEUE_ID` | `NUMBER` | `NOT NULL` | ID of the queue |
| `NUM_MSGS` | `NUMBER` |  | Total number of outstanding messages currently enqueued in the buffered queue for the subscriber (includes the count of the messages overflowed to disk) |
| `SPILL_MSGS` | `NUMBER` |  | Current number of overflow messages spilled to disk from the buffered queue |
| `CNUM_MSGS` | `NUMBER` |  | Cumulative total number of messages enqueued into the buffered queue since the buffered queue was created. |
| `CSPILL_MSGS` | `NUMBER` |  | Cumulative total number of overflow messages spilled to disk from the buffered queue since the buffered queue was created |
| `EXPIRED_MSGS` <sup>Foot 1</sup> | `NUMBER` |  | Number of expired messages |
| `OLDEST_MSGID` <sup>Footref 1</sup> | `RAW(16)` |  | Message ID of the oldest message |
| `OLDEST_MSG_ENQTM` <sup>Footref 1</sup> | `TIMESTAMP(3)` |  | Enqueue time of the oldest message |
| `QUEUE_STATE` <sup>Footref 1</sup> | `VARCHAR2(25)` |  | Indicates whether the queue is in recovery mode (`QUEUE` `IS` `IN` `RECOVERY` `MODE`) or not (`NORMAL`) |
| `ELAPSED_ENQUEUE_TIME` <sup>Footref 1</sup> | `NUMBER` |  | Total time spent in enqueue (in hundredths of a second) |
| `ELAPSED_DEQUEUE_TIME` <sup>Footref 1</sup> | `NUMBER` |  | Total time spent in dequeue (in hundredths of a second) |
| `ELAPSED_TRANSFORMATION_TIME` <sup>Footref 1</sup> | `NUMBER` |  | Total time for evaluating transformations (in hundredths of a second) |
| `ELAPSED_RULE_EVALUATION_TIME` <sup>Footref 1</sup> | `NUMBER` |  | Total time for rule evaluations (in hundredths of a second) |
| `ENQUEUE_CPU_TIME` <sup>Footref 1</sup> | `NUMBER` |  | Total CPU time for enqueue (in hundredths of a second) |
| `DEQUEUE_CPU_TIME` <sup>Footref 1</sup> | `NUMBER` |  | Total CPU time for dequeue (in hundredths of a second) |
| `LAST_ENQUEUE_TIME` <sup>Footref 1</sup> | `TIMESTAMP(3)` |  | Last message enqueue time |
| `LAST_DEQUEUE_TIME` <sup>Footref 1</sup> | `TIMESTAMP(3)` |  | Last message dequeue time |

<sup>Footnote 1</sup> This column is available starting with Oracle Database 11g Release 2 (11.2.0.2).