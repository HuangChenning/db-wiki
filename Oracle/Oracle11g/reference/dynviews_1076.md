---
title: "V$BUFFERED_SUBSCRIBERS"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1076.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$BUFFERED_SUBSCRIBERS` displays information about the subscribers for all buffered queues in the instance. There is one row per subscriber per queue.

| Column | Datatype | Description |
| --- | --- | --- |
| `QUEUE_ID` | `NUMBER` | Identifier for the queue |
| `QUEUE_SCHEMA` | `VARCHAR2(30)` | Owner of the queue |
| `QUEUE_NAME` | `VARCHAR2(30)` | Name of the queue |
| `SUBSCRIBER_ID` | `NUMBER` | Internal subscriber number (for identification) |
| `SUBSCRIBER_NAME` | `VARCHAR2(30)` | Name of the subscriber (comparable to the Streams name for the Streams process) |
| `SUBSCRIBER_ADDRESS` | `VARCHAR2(1024)` | Address of the subscribing agent |
| `PROTOCOL` | `NUMBER` | Protocol of the subscribing agent |
| `SUBSCRIBER_TYPE` | `VARCHAR2(30)` | Type of the subscriber: - `PROXY` - Proxy subscriber - `SUBSCRIBER` |
| `STARTUP_TIME` | `DATE` | Startup time |
| `LAST_BROWSED_SEQ` | `NUMBER` | Sequence number of the most recently browsed message for the subscriber (comparable to the number of messages in the `V$STREAMS_APPLY_READER` view) |
| `LAST_BROWSED_NUM` | `NUMBER` | Internal Message number for the most recently browsed message for the subscriber |
| `LAST_DEQUEUED_SEQ` | `NUMBER` | Sequence number of the most recently dequeued message for the subscriber (comparable to the number of messages in the `V$STREAMS_APPLY_COORDINATOR` view) |
| `LAST_DEQUEUED_NUM` | `NUMBER` | Internal Message number for the most recently dequeued message for the subscriber |
| `CURRENT_ENQ_SEQ` | `NUMBER` | Current sequence number of the most recently enqueued message for the subscriber |
| `NUM_MSGS` | `NUMBER` | Total number of outstanding messages currently enqueued in the buffered queue for the subscriber (includes the count of the messages overflowed to disk) |
| `CNUM_MSGS` | `NUMBER` | Cumulative total number of messages enqueued for the subscriber since the database last started |
| `TOTAL_DEQUEUED_MSG` | `NUMBER` | Total number of messages dequeued by the subscriber |
| `TOTAL_SPILLED_MSG` | `NUMBER` | Total number of spilled messages for the subscriber |
| `EXPIRED_MSGS` | `NUMBER` | Number of expired messages |
| `MESSAGE_LAG` | `NUMBER` | Message lag of the subscriber |
| `ELAPSED_DEQUEUE_TIME` | `NUMBER` | Total time spent in dequeue (in hundredths of a second) |
| `DEQUEUE_CPU_TIME` | `NUMBER` | Total CPU time for dequeue (in hundredths of a second) |
| `AVG_MSG_AGE` <sup>Foot 1</sup> | `NUMBER` | Average age of messages currently enqueued in the buffered queue for the subscriber |
| `LAST_DEQUEUE_TIME` | `TIMESTAMP(3) WITH TIME ZONE` | Last message dequeue time |
| `OLDEST_MSGID` | `RAW(16)` | Message ID of the oldest message |
| `OLDEST_MSG_ENQTM` | `TIMESTAMP(3)` | Enqueue time of the oldest message |

<sup>Footnote 1</sup> This column is available starting with Oracle Database 11g Release 2 (11.2.0.2).