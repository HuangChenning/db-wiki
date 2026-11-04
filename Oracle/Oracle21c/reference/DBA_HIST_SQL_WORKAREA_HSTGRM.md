---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_HIST_SQL_WORKAREA_HSTGRM.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.62 DBA\_HIST\_SQL\_WORKAREA\_HSTGRM

`DBA_HIST_SQL_WORKAREA_HSTGRM` displays the historical cumulative work area execution statistics (cumulated since instance startup) for different work area groups.

This view contains snapshots of `V$SQL_WORKAREA_HISTOGRAM`.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` | `NOT NULL` | Unique snapshot ID |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID for the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` | `NOT NULL` | Instance number for the snapshot |
| `LOW_OPTIMAL_SIZE` | `NUMBER` | `NOT NULL` | Lower bound for the optimal memory requirement of work areas included in the row (in bytes) |
| `HIGH_OPTIMAL_SIZE` | `NUMBER` | `NOT NULL` | Upper bound for the optimal memory requirement of work areas included in the row (in bytes) |
| `OPTIMAL_EXECUTIONS` | `NUMBER` |  | Number of work areas with an optimal memory requirement comprised between `LOW_OPTIMAL_SIZE` and `HIGH_OPTIMAL_SIZE` which have been executed in optimal mode since instance startup |
| `ONEPASS_EXECUTIONS` | `NUMBER` |  | Number of work areas with an optimal memory requirement comprised between `LOW_OPTIMAL_SIZE` and `HIGH_OPTIMAL_SIZE` which have been executed in one-pass mode since instance startup |
| `MULTIPASSES_EXECUTIONS` | `NUMBER` |  | Number of work areas with an optimal memory requirement comprised between `LOW_OPTIMAL_SIZE` and `HIGH_OPTIMAL_SIZE` which have been executed in multi-pass mode since instance startup |
| `TOTAL_EXECUTIONS` | `NUMBER` |  | Sum of `OPTIMAL_EXECUTIONS`, `ONEPASS_EXECUTIONS`, and `MULTIPASSES_EXECUTIONS` |
| `CON_DBID` | `NUMBER` |  | The database ID of the PDB for the sampled session |
| `CON_ID` | `NUMBER` |  | The ID of the container that `CON_DBID` identifies. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |