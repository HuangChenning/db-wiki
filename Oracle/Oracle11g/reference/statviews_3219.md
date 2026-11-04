---
title: DBA_HIST_DLM_MISC
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_3219.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_HIST_DLM_MISC` displays miscellaneous Oracle Real Application Clusters (Oracle RAC) statistics. This view contains snapshots of `V$DLM_MISC`.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` |  | Unique snapshot ID |
| `DBID` | `NUMBER` |  | Database ID for the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` |  | Instance number for the snapshot |
| `STATISTIC#` | `NUMBER` |  | Statistic number |
| `NAME` | `VARCHAR2(38)` |  | Statistic name |
| `VALUE` | `NUMBER` |  | Statistic value |