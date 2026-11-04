---
title: DBA_HIST_OPTIMIZER_ENV
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4014.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_HIST_OPTIMIZER_ENV` displays the optimizer environments that have been captured in the Workload Repository. This view is used with the `DBA_HIST_SQLSTAT` view.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID |
| `OPTIMIZER_ENV_HASH_VALUE` | `NUMBER` | `NOT NULL` | Hash value for the optimizer environment |
| `OPTIMIZER_ENV` | `RAW(623)` |  | Optimizer environment |