---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-PQ_TQSTAT.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.128 V$PQ\_TQSTAT

The statistics are compiled after the query completes and only remain for the duration of the session. It displays the number of rows processed through each parallel execution server at each stage of the execution tree. This view can help determine skew problems in a query's execution. (Note that for PDML, information from `V$PQ_TQSTAT` is available only after a commit or rollback operation.)

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
| `PROCESS` | `VARCHAR2(6)` | Process ID |
| `INSTANCE` | `NUMBER` | Instance ID |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |