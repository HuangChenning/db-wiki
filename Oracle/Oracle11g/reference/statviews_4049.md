---
title: DBA_HIST_SQL_WORKAREA_HSTGRM
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4049.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_HIST_SQL_WORKAREA_HSTGRM` displays the historical cumulative work area execution statistics (cumulated since instance startup) for different work area groups. This view contains snapshots of `V$SQL_WORKAREA_HISTOGRAM`.

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