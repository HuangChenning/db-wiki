---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-ENQUEUE_STAT.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.201 V$ENQUEUE\_STAT

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
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |