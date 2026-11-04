---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/DBA_HIST_STAT_NAME.html
tags:
  - oracle
  - 19c
  - reference
---

## 5.68 DBA\_HIST\_STAT\_NAME

`DBA_HIST_STAT_NAME` displays decoded statistic names for the statistics captured in the Workload Repository.

This includes OLAP statisitics and OLAP timed events. This view captures information from `V$STATNAME` and is used with `DBA_HIST_SYSSTAT` and `DBA_HIST_SYS_TIME_MODEL`.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID |
| `STAT_ID` | `NUMBER` | `NOT NULL` | Statistic identifier |
| `STAT_NAME` | `VARCHAR2(64)` | `NOT NULL` | Statistic name |
| `CON_DBID` | `NUMBER` |  | The database ID of the PDB for the sampled session |
| `CON_ID` | `NUMBER` |  | The ID of the container that `CON_DBID` identifies. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |