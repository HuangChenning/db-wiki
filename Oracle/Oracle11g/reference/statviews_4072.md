---
title: DBA_HIST_WR_CONTROL
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4072.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_HIST_WR_CONTROL` displays the control information for the Workload Repository.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID |
| `SNAP_INTERVAL` | `INTERVAL DAY(5) TO SECOND(1)` | `NOT NULL` | Snapshot interval; how often to automatically take snapshots |
| `RETENTION` | `INTERVAL DAY(5) TO SECOND(1)` | `NOT NULL` | Retention setting for the snapshots; amount of time to keep the snapshots |
| `TOPNSQL` | `VARCHAR2(10)` |  | The number of Top SQL flushed for each SQL criteria (elapsed time, CPU time, parse calls, shareable memory, version count) |