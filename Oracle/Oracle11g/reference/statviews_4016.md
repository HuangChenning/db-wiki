---
title: DBA_HIST_OSSTAT_NAME
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4016.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_HIST_OSSTAT_NAME` displays the names of the operating system statistics. This view is used with `DBA_HIST_OSSTAT`.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID |
| `STAT_ID` | `NUMBER` | `NOT NULL` | Statistic ID |
| `STAT_NAME` | `VARCHAR2(64)` | `NOT NULL` | Statistic name |