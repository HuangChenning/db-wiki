---
title: "V$PQ_SLAVE"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2098.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$PQ_SLAVE` lists statistics for each of the active parallel execution servers on an instance.

| Column | Datatype | Description |
| --- | --- | --- |
| `SLAVE_NAME` | `VARCHAR2(4)` | Name of the parallel execution server |
| `STATUS` | `VARCHAR2(4)` | Current status of the parallel execution server: |
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