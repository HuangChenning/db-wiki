---
title: DBA_HIST_STREAMS_APPLY_SUM
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4055.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_HIST_STREAMS_APPLY_SUM` displays information about each apply process and its activities. This view contains a snapshot of `V$STREAMS_APPLY_COORDINATOR`, `V$STREAMS_APPLY_READER`, and `V$STREAMS_APPLY_SERVER`. This view is intended for use with Automatic Workload Repository (AWR).

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` | `NOT NULL` | Unique snapshot ID |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID for the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` | `NOT NULL` | Instance number for the snapshot |
| `APPLY_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the apply process |
| `STARTUP_TIME` | `DATE` | `NOT NULL` | Time that the apply process was last started |
| `READER_TOTAL_MESSAGES_DEQUEUED` | `NUMBER` |  | Total number of messages dequeued since the apply process was last started |
| `READER_LAG` | `NUMBER` |  | For captured messages, the delay (in seconds) between the creation of the last message and it being received by the apply process. For user enqueued messages, the delay between the message being enqueued in the local database and being received by the apply process. |
| `COORD_TOTAL_RECEIVED` | `NUMBER` |  | Total number of transactions received by the coordinator process since the apply process was last started |
| `COORD_TOTAL_APPLIED` | `NUMBER` |  | Total number of transactions applied by the apply process since the apply process was last started |
| `COORD_TOTAL_ROLLBACKS` | `NUMBER` |  | Number of transactions which were rolled back due to unexpected contention |
| `COORD_TOTAL_WAIT_DEPS` | `NUMBER` |  | Number of times since the apply process was last started that an apply server waited to apply a logical change record (LCR) in a transaction until another apply server applied a transaction because of a dependency between the transactions |
| `COORD_TOTAL_WAIT_CMTS` | `NUMBER` |  | Number of times since the apply process was last started that an apply server waited to commit a transaction until another apply server committed a transaction to serialize commits |
| `COORD_LWM_LAG` | `NUMBER` |  | For captured messages, the delay (in seconds) between the creation of the message corresponding to the low watermark and it being applied by the apply process. For user enqueued messages, the delay between the message being enqueued in the local database and being applied by the apply process. |
| `SERVER_TOTAL_MESSAGES_APPLIED` | `NUMBER` |  | Total number of messages applied by all the apply servers since the apply process was last started |
| `SERVER_ELAPSED_DEQUEUE_TIME` | `NUMBER` |  | Time elapsed (in hundredths of a second) dequeuing messages by all the apply servers since the apply process was last started |
| `SERVER_ELAPSED_APPLY_TIME` | `NUMBER` |  | Time elapsed (in hundredths of a second) applying messages by all the apply servers since the apply process was last started |