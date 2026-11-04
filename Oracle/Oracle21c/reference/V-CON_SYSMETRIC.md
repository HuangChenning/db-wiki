---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-CON_SYSMETRIC.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.132 V$CON\_SYSMETRIC

`V$CON_SYSMETRIC` displays the system metric values captured for the most current time interval for the PDB long duration (60-second) system metrics.

| Column | Datatype | Description |
| --- | --- | --- |
| `BEGIN_TIME` | `DATE` | Begin time of the interval |
| `END_TIME` | `DATE` | End time of the interval |
| `INTSIZE_CSEC` | `NUMBER` | Interval size (in hundredths of a second) |
| `GROUP_ID` | `NUMBER` | Metric group ID |
| `METRIC_ID` | `NUMBER` | Metric ID |
| `METRIC_NAME` | `VARCHAR2(64)` | Metric name |
| `VALUE` | `NUMBER` | Metric value |
| `METRIC_UNIT` | `VARCHAR2(64)` | Metric unit description |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - When queried from a non-CDB, the statistics for that instance are returned, and the `CON_ID` value is `0`. - When queried from the root of a CDB, the statistics for every container are returned, and the `CON_ID` value indicates the container to which the statistics belong. - When queried from a PDB, statistics from that PDB are returned, and the `CON_ID` value is the container ID for that PDB. |