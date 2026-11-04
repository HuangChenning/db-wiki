---
title: DBA_HIST_STAT_NAME
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4054.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_HIST_STAT_NAME` displays decoded statistic names for the statistics captured in the Workload Repository. This view captures information from `V$STATNAME` and used with `DBA_HIST_SYSSTAT` and `DBA_HIST_SYS_TIME_MODEL`.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID |
| `STAT_ID` | `NUMBER` | `NOT NULL` | Statistic identifier |
| `STAT_NAME` | `VARCHAR2(64)` | `NOT NULL` | Statistic name |