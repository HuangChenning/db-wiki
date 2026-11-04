---
title: DBA_HIST_OSSTAT
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4015.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_HIST_OSSTAT` displays historical operating system statistics. This view contains snapshots of `V$OSSTAT`.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` |  | Unique snapshot ID |
| `DBID` | `NUMBER` |  | Database ID for the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` |  | Instance number for the snapshot |
| `STAT_ID` | `NUMBER` |  | Statistic ID |
| `STAT_NAME` | `VARCHAR2(64)` |  | Statistic name |
| `VALUE` | `NUMBER` |  | Statistic value |