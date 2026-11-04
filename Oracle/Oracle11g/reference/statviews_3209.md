---
title: DBA_HIST_BUFFERED_SUBSCRIBERS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_3209.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_HIST_BUFFERED_SUBSCRIBERS` displays historical information about the subscribers for all buffered queues in the instance.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` | `NOT NULL` | Unique snapshot ID |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID for the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` | `NOT NULL` | Instance number for the snapshot |
| `QUEUE_SCHEMA` | `VARCHAR2(30)` | `NOT NULL` | Owner of the queue |
| `QUEUE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the queue |
| `SUBSCRIBER_ID` | `NUMBER` | `NOT NULL` | Internal subscriber number (for identification) |
| `SUBSCRIBER_NAME` | `VARCHAR2(30)` |  | Name of the subscriber |
| `SUBSCRIBER_ADDRESS` | `VARCHAR2(1024)` |  | Address of the subscribing agent |
| `SUBSCRIBER_TYPE` | `VARCHAR2(30)` |  | Type of subscriber: - `PROXY` - Proxy subscriber - `SUBSCRIBOR` |
| `STARTUP_TIME` | `DATE` | `NOT NULL` | Startup time of the instance |
| `LAST_BROWSED_SEQ` <sup>Foot 1</sup> | `NUMBER` |  | Sequence number of the most recently browsed message for the subscriber (comparable to the number of messages in the `V$STREAMS_APPLY_READER` view) |
| `LAST_BROWSED_NUM` <sup>Footref 1</sup> | `NUMBER` |  | Internal Message number for the most recently browsed message for the subscriber |
| `LAST_DEQUEUED_SEQ` <sup>Footref 1</sup> | `NUMBER` |  | Sequence number of the most recently dequeued message for the subscriber (comparable to the number of messages in the `V$STREAMS_APPLY_COORDINATOR` view) |
| `LAST_DEQUEUED_NUM` <sup>Footref 1</sup> | `NUMBER` |  | Internal Message number for the most recently dequeued message for the subscriber |
| `CURRENT_ENQ_SEQ` <sup>Footref 1</sup> | `NUMBER` |  | Current sequence number of the most recently enqueued message for the subscriber |
| `NUM_MSGS` | `NUMBER` |  | Total number of outstanding messages currently enqueued in the buffered queue for the subscriber (includes the count of the messages overflowed to disk) |
| `CNUM_MSGS` | `NUMBER` |  | Cumulative total number of messages enqueued for the subscriber since the creation of the buffered queue |
| `TOTAL_DEQUEUED_MSG` <sup>Footref 1</sup> | `NUMBER` |  | Total number of messages dequeued by the subscriber |
| `TOTAL_SPILLED_MSG` | `NUMBER` |  | Total number of spilled messages for the subscriber |
| `EXPIRED_MSGS` <sup>Footref 1</sup> | `NUMBER` |  | Number of expired messages |
| `MESSAGE_LAG` <sup>Footref 1</sup> | `NUMBER` |  | Message lag of the subscriber |
| `ELAPSED_DEQUEUE_TIME` <sup>Footref 1</sup> | `NUMBER` |  | Total time spent in dequeue (in hundredths of a second) |
| `DEQUEUE_CPU_TIME` <sup>Footref 1</sup> | `NUMBER` |  | Total CPU time for dequeue (in hundredths of a second) |
| `LAST_DEQUEUE_TIME` <sup>Footref 1</sup> | `TIMESTAMP(3)` |  | Last message dequeue time |
| `OLDEST_MSGID` <sup>Footref 1</sup> | `RAW(16)` |  | Message ID of the oldest message |
| `OLDEST_MSG_ENQTM` <sup>Footref 1</sup> | `TIMESTAMP(3)` |  | Enqueue time of the oldest message |

<sup>Footnote 1</sup> This column is available starting with Oracle Database 11g Release 2 (11.2.0.2).