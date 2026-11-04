---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-EXP_STATS.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.222 V$EXP\_STATS

`V$EXP_STATS` stores the expression tracking statistics of recently executed queries.

| Column | Datatype | Description |
| --- | --- | --- |
| `EXPID` | `NUMBER` | Expression ID of the current expression |
| `OBJNUM` | `NUMBER` | The object number contained in the expression |
| `DYNCOST` | `NUMBER` | Optimizer dynamic cost of evaluating the expression |
| `EVALCNT` | `NUMBER` | Number of times the expression has been evaluated |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |