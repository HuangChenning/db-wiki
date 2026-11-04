---
title: "V$ENQUEUE_STATISTICS"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1128.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$ENQUEUE_STATISTICS` displays statistics on the number of enqueue (lock) requests for each type of lock. `V$ENQUEUE_STATISTICS` encompasses `V$ENQUEUE_STAT` and gives more detailed information (several rows for same enqueues with different reasons).

| Column | Datatype | Description |
| --- | --- | --- |
| `EQ_NAME` | `VARCHAR2(64)` | Name of the enqueue request |
| `EQ_TYPE` | `VARCHAR2(2)` | Type of enqueue requested |
| `REQ_REASON` | `VARCHAR2(64)` | Reason for the enqueue request |
| `TOTAL_REQ#` | `NUMBER` | Total number of enqueue requests or enqueue conversions for this type of enqueue |
| `TOTAL_WAIT#` | `NUMBER` | Total number of times an enqueue request or conversion resulted in a wait |
| `SUCC_REQ#` | `NUMBER` | Number of times an enqueue request or conversion was granted |
| `FAILED_REQ#` | `NUMBER` | Number of times an enqueue request or conversion failed |
| `CUM_WAIT_TIME` | `NUMBER` | Total amount of time (in milliseconds) spent waiting for the enqueue or enqueue conversion |
| `REQ_DESCRIPTION` | `VARCHAR2(4000)` | Description of the enqueue request |
| `EVENT#` | `NUMBER` | Event number |