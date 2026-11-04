---
title: "V$ENQUEUE_STAT"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1127.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$ENQUEUE_STAT` displays statistics on the number of enqueue (lock) requests for each type of lock.

| Column | Datatype | Description |
| --- | --- | --- |
| `INST_ID` | `NUMBER` | ID of the instance |
| `EQ_TYPE` | `VARCHAR2(2)` | Type of enqueue requested |
| `TOTAL_REQ#` | `NUMBER` | Total number of enqueue requests or enqueue conversions for this type of enqueue |
| `TOTAL_WAIT#` | `NUMBER` | Total number of times an enqueue request or conversion resulted in a wait |
| `SUCC_REQ#` | `NUMBER` | Number of times an enqueue request or conversion was granted |
| `FAILED_REQ#` | `NUMBER` | Number of times an enqueue request or conversion failed |
| `CUM_WAIT_TIME` | `NUMBER` | Total amount of time (in milliseconds) spent waiting for the enqueue or enqueue conversion |