---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_HIST_SYSMETRIC_SUMMARY.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.73 DBA\_HIST\_SYSMETRIC\_SUMMARY

`DBA_HIST_SYSMETRIC_SUMMARY` displays a history of statistical summary of all metric values in the System Metrics Long Duration group.

This view contains snapshots of `V$SYSMETRIC_SUMMARY`.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` | `NOT NULL` | Unique snapshot ID |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID for the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` | `NOT NULL` | Instance number for the snapshot |
| `BEGIN_TIME` | `DATE` | `NOT NULL` | Begin time of the interval |
| `END_TIME` | `DATE` | `NOT NULL` | End time of the interval |
| `INTSIZE` | `NUMBER` | `NOT NULL` | Interval size (in hundredths of a second) |
| `GROUP_ID` | `NUMBER` | `NOT NULL` | Group ID |
| `METRIC_ID` | `NUMBER` | `NOT NULL` | Metric ID |
| `METRIC_NAME` | `VARCHAR2(64)` | `NOT NULL` | Metric name |
| `METRIC_UNIT` | `VARCHAR2(64)` | `NOT NULL` | Unit of measurement |
| `NUM_INTERVAL` | `NUMBER` | `NOT NULL` | Number of intervals observed |
| `MINVAL` | `NUMBER` | `NOT NULL` | Minimum value observed |
| `MAXVAL` | `NUMBER` | `NOT NULL` | Maximum value observed |
| `AVERAGE` | `NUMBER` | `NOT NULL` | Average over the period |
| `STANDARD_DEVIATION` | `NUMBER` | `NOT NULL` | One standard deviation |
| `SUM_SQUARES` | `NUMBER` |  | Sum of the squared deviations from the mean |
| `CON_DBID` | `NUMBER` |  | The database ID of the PDB for the sampled session |
| `CON_ID` | `NUMBER` |  | The ID of the container that `CON_DBID` identifies. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |