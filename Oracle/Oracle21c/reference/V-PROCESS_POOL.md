---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-PROCESS_POOL.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.132 V$PROCESS\_POOL

| Column | Datatype | Description |
| --- | --- | --- |
| `POOL_NAME` | `VARCHAR2(512)` | Pool name |
| `ENABLED` | `VARCHAR2(5)` | Indicates whether the pool is active (`TRUE`) or not (`FALSE`) |
| `MIN_COUNT` | `NUMBER` | The default or configured minimum value |
| `BATCH_COUNT` | `NUMBER` | The default or configured batch count |
| `INIT_COUNT` | `NUMBER` | The default or configured initial count |
| `CUR_COUNT` | `NUMBER` | The number of spawned processes available in this pool |
| `MAX_COUNT` | `NUMBER` | When `INIT_COUNT` is set, `MAX_COUNT` shows the number of processes yet to be spawned. Note that the current process count (`CUR_COUNT`) cannot reach `INIT_COUNT` in cases where processes are consumed during the spawn. |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This row is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |