---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_HIST_OPTIMIZER_ENV.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.14 DBA\_HIST\_OPTIMIZER\_ENV

`DBA_HIST_OPTIMIZER_ENV` displays the optimizer environments that have been captured in the Workload Repository.

This view is used with the `DBA_HIST_SQLSTAT` view.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID |
| `OPTIMIZER_ENV_HASH_VALUE` | `NUMBER` | `NOT NULL` | Hash value for the optimizer environment |
| `OPTIMIZER_ENV` | `RAW(2000)` |  | Optimizer environment |
| `CON_DBID` | `NUMBER` |  | The database ID of the PDB for the sampled session |
| `CON_ID` | `NUMBER` |  | The ID of the container that `CON_DBID` identifies. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

" [DBA\_HIST\_SQLSTAT](DBA_HIST_SQLSTAT.md) "