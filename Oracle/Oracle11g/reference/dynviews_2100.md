---
title: "V$PQ_TQSTAT"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2100.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$PQ_TQSTAT` contains statistics on parallel execution operations. The statistics are compiled after the query completes and only remain for the duration of the session. It displays the number of rows processed through each parallel execution server at each stage of the execution tree. This view can help determine skew problems in a query's execution. (Note that for PDML, information from `V$PQ_TQSTAT` is available only after a commit or rollback operation.)

| Column | Datatype | Description |
| --- | --- | --- |
| `DFO_NUMBER` | `NUMBER` | Data flow operator (DFO) tree number to differentiate queries |
| `TQ_ID` | `NUMBER` | Table queue ID within the query, which represents the connection between two DFO nodes in the query execution tree |
| `SERVER_TYPE` | `VARCHAR2(10)` | The role in table queue - producer/consumer/ranger |
| `NUM_ROWS` | `NUMBER` | The number of rows produced/consumed |
| `BYTES` | `NUMBER` | The number of bytes produced/consumed |
| `OPEN_TIME` | `NUMBER` | Time (seconds) the table queue remained open |
| `AVG_LATENCY` | `NUMBER` | Time (minutes) for a message to be dequeued after it enters the queue |
| `WAITS` | `NUMBER` | The number of waits encountered during dequeue |
| `TIMEOUTS` | `NUMBER` | The number of timeouts when waiting for a message |
| `PROCESS` | `VARCHAR2(10)` | Process ID |
| `INSTANCE` | `NUMBER` | Instance ID |