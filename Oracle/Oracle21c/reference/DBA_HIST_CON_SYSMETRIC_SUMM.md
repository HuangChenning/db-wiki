---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_HIST_CON_SYSMETRIC_SUMM.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.390 DBA\_HIST\_CON\_SYSMETRIC\_SUMM

`DBA_HIST_CON_SYSMETRIC_SUMM` displays a history of statistical summary of all metric values in the system metrics long duration (60–second) group. This view contains snapshots of `V$CON_SYSMETRIC_SUMMARY`.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` |  | Unique snapshot ID |
| `DBID` | `NUMBER` |  | Database ID for the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` |  | Instance number for the snapshot |
| `BEGIN_TIME` | `DATE` |  | Begin time of the interval |
| `END_TIME` | `DATE` |  | End time of the interval |
| `INTSIZE` | `NUMBER` |  | Interval size (in hundredths of a second) |
| `GROUP_ID` | `NUMBER` |  | Group ID |
| `METRIC_ID` | `NUMBER` |  | Metric ID |
| `METRIC_NAME` | `VARCHAR2(64)` |  | Metric name |
| `METRIC_UNIT` | `VARCHAR2(64)` |  | Unit of measurement |
| `NUM_INTERVAL` | `NUMBER` |  | Number of intervals observed |
| `MINVAL` | `NUMBER` |  | Minimum value observed |
| `MAXVAL` | `NUMBER` |  | Maximum value observed |
| `AVERAGE` | `NUMBER` |  | Average over the period |
| `STANDARD_DEVIATION` | `NUMBER` |  | One standard deviation |
| `SUM_SQUARES` | `NUMBER` |  | Sum of the squared deviations from the mean |
| `CON_DBID` | `NUMBER` |  | The database ID of the PDB for the sampled session |
| `CON_ID` | `NUMBER` |  | The ID of the container that `CON_DBID` identifies. Possible values include:  - When queried from a non-CDB, the statistics for that instance are returned, and the `CON_ID` value is `0`. - When queried from the root of a CDB, the statistics in every container are returned, and the `CON_ID` value indicates the container to which the statistics belong. - When queried from a PDB, statistics from that PDB are returned, and the `CON_ID` value is the container ID for that PDB. |