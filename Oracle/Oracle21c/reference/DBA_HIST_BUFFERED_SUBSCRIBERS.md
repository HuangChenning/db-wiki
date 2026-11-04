---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_HIST_BUFFERED_SUBSCRIBERS.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.382 DBA\_HIST\_BUFFERED\_SUBSCRIBERS

`DBA_HIST_BUFFERED_SUBSCRIBERS` displays historical information about the subscribers for all buffered queues in the instance.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` | `NOT NULL` | Unique snapshot ID |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID for the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` | `NOT NULL` | Instance number for the snapshot |
| `QUEUE_SCHEMA` | `VARCHAR2(128)` | `NOT NULL` | Owner of the queue |
| `QUEUE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the queue |
| `SUBSCRIBER_ID` | `NUMBER` | `NOT NULL` | Internal subscriber number (for identification) |
| `SUBSCRIBER_NAME` | `VARCHAR2(128)` |  | Name of the subscriber |
| `SUBSCRIBER_ADDRESS` | `VARCHAR2(1024)` |  | Address of the subscribing agent |
| `SUBSCRIBER_TYPE` | `VARCHAR2(128)` |  | Type of subscriber:  - `PROXY` - Proxy subscriber - `SUBSCRIBOR` |
| `STARTUP_TIME` | `DATE` | `NOT NULL` | Startup time of the instance |
| `LAST_BROWSED_SEQ` | `NUMBER` |  | Sequence number of the most recently browsed message for the subscriber (comparable to the number of messages in the `V$STREAMS_APPLY_READER` view) |
| `LAST_BROWSED_NUM` | `NUMBER` |  | Internal Message number for the most recently browsed message for the subscriber |
| `LAST_DEQUEUED_SEQ` | `NUMBER` |  | Sequence number of the most recently dequeued message for the subscriber (comparable to the number of messages in the `V$STREAMS_APPLY_COORDINATOR` view) |
| `LAST_DEQUEUED_NUM` | `NUMBER` |  | Internal Message number for the most recently dequeued message for the subscriber |
| `CURRENT_ENQ_SEQ` | `NUMBER` |  | Current sequence number of the most recently enqueued message for the subscriber |
| `NUM_MSGS` | `NUMBER` |  | Total number of outstanding messages currently enqueued in the buffered queue for the subscriber (includes the count of the messages overflowed to disk) |
| `CNUM_MSGS` | `NUMBER` |  | Cumulative total number of messages enqueued for the subscriber since the creation of the buffered queue |
| `TOTAL_DEQUEUED_MSG` | `NUMBER` |  | Total number of messages dequeued by the subscriber |
| `TOTAL_SPILLED_MSG` | `NUMBER` |  | Total number of spilled messages for the subscriber |
| `EXPIRED_MSGS` | `NUMBER` |  | Number of expired messages |
| `MESSAGE_LAG` | `NUMBER` |  | Message lag of the subscriber |
| `ELAPSED_DEQUEUE_TIME` | `NUMBER` |  | Total time spent in dequeue (in hundredths of a second) |
| `DEQUEUE_CPU_TIME` | `NUMBER` |  | Total CPU time for dequeue (in hundredths of a second) |
| `LAST_DEQUEUE_TIME` | `TIMESTAMP(3)` |  | Last message dequeue time |
| `OLDEST_MSGID` | `RAW(16)` |  | Message ID of the oldest message |
| `OLDEST_MSG_ENQTM` | `TIMESTAMP(3)` |  | Enqueue time of the oldest message |
| `CON_DBID` | `NUMBER` |  | The database ID of the PDB for the sampled session |
| `CON_ID` | `NUMBER` |  | The ID of the container that `CON_DBID` identifies. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |