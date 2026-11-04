---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/V-EXP_STATS.html
tags:
  - oracle
  - 12c
  - reference
---

`V$EXP_STATS` stores the expression tracking statistics of recently executed queries.

| Column | Datatype | Description |
| --- | --- | --- |
| `EXPID` | `NUMBER` | Expression ID of the current expression |
| `OBJNUM` | `NUMBER` | The object number contained in the expression |
| `DYNCOST` | `NUMBER` | Optimizer dynamic cost of evaluating the expression |
| `EVALCNT` | `NUMBER` | Number of times the expression has been evaluated |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

Note:

This view is available starting with Oracle Database 12c Release 2 (12.2.0.1).