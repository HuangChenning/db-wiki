---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_HIST_BUFFERED_QUEUES.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.381 DBA\_HIST\_BUFFERED\_QUEUES

`DBA_HIST_BUFFERED_QUEUES` displays historical information about all buffered queues available for the instance.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` | `NOT NULL` | Unique snapshot ID |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID for the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` | `NOT NULL` | Instance number for the snapshot |
| `QUEUE_SCHEMA` | `VARCHAR2(128)` | `NOT NULL` | Owner of the queue |
| `QUEUE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the queue |
| `STARTUP_TIME` | `DATE` | `NOT NULL` | Startup time of the instance |
| `QUEUE_ID` | `NUMBER` | `NOT NULL` | ID of the queue |
| `NUM_MSGS` | `NUMBER` |  | Total number of outstanding messages currently enqueued in the buffered queue for the subscriber (includes the count of the messages overflowed to disk) |
| `SPILL_MSGS` | `NUMBER` |  | Current number of overflow messages spilled to disk from the buffered queue |
| `CNUM_MSGS` | `NUMBER` |  | Cumulative total number of messages enqueued into the buffered queue since the buffered queue was created. |
| `CSPILL_MSGS` | `NUMBER` |  | Cumulative total number of overflow messages spilled to disk from the buffered queue since the buffered queue was created |
| `EXPIRED_MSGS` | `NUMBER` |  | Number of expired messages |
| `OLDEST_MSGID` | `RAW(16)` |  | Message ID of the oldest message |
| `OLDEST_MSG_ENQTM` | `TIMESTAMP(3)` |  | Enqueue time of the oldest message |
| `QUEUE_STATE` | `VARCHAR2(25)` |  | Indicates whether the queue is in recovery mode (`QUEUE` `IS` `IN` `RECOVERY` `MODE`) or not (`NORMAL`) |
| `ELAPSED_ENQUEUE_TIME` | `NUMBER` |  | Total time spent in enqueue (in hundredths of a second) |
| `ELAPSED_DEQUEUE_TIME` | `NUMBER` |  | Total time spent in dequeue (in hundredths of a second) |
| `ELAPSED_TRANSFORMATION_TIME` | `NUMBER` |  | Total time for evaluating transformations (in hundredths of a second) |
| `ELAPSED_RULE_EVALUATION_TIME` | `NUMBER` |  | Total time for rule evaluations (in hundredths of a second) |
| `ENQUEUE_CPU_TIME` | `NUMBER` |  | Total CPU time for enqueue (in hundredths of a second) |
| `DEQUEUE_CPU_TIME` | `NUMBER` |  | Total CPU time for dequeue (in hundredths of a second) |
| `LAST_ENQUEUE_TIME` | `TIMESTAMP(3)` |  | Last message enqueue time |
| `LAST_DEQUEUE_TIME` | `TIMESTAMP(3)` |  | Last message dequeue time |
| `CON_DBID` | `NUMBER` |  | The database ID of the PDB for the sampled session |
| `CON_ID` | `NUMBER` |  | The ID of the container that `CON_DBID` identifies. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |