---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-PQ_SLAVE.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.126 V$PQ\_SLAVE

`V$PQ_SLAVE` lists statistics for each of the active parallel execution servers on an instance.

| Column | Datatype | Description |
| --- | --- | --- |
| `SLAVE_NAME` | `VARCHAR2(4)` | Name of the parallel execution server |
| `STATUS` | `VARCHAR2(4)` | Current status of the parallel execution server:  - `BUSY` - `IDLE` |
| `SESSIONS` | `NUMBER` | Number of sessions that have used this parallel execution server |
| `IDLE_TIME_CUR` | `NUMBER` | Amount of time spent idle while processing statements in the current session |
| `BUSY_TIME_CUR` | `NUMBER` | Amount of time spent busy while processing statements in the current session |
| `CPU_SECS_CUR` | `NUMBER` | Amount of CPU time spent on the current session |
| `MSGS_SENT_CUR` | `NUMBER` | Number of messages sent while processing statements for the current session |
| `MSGS_RCVD_CUR` | `NUMBER` | Number of messages received while processing statements for the current session |
| `IDLE_TIME_TOTAL` | `NUMBER` | Total amount of time this query server has been idle |
| `BUSY_TIME_TOTAL` | `NUMBER` | Total amount of time this query server has been active |
| `CPU_SECS_TOTAL` | `NUMBER` | Total amount of CPU time this query server has used to process statements |
| `MSGS_SENT_TOTAL` | `NUMBER` | Total number of messages this query server has sent |
| `MSGS_RCVD_TOTAL` | `NUMBER` | Total number of messages this query server has received |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |