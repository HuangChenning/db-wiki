---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/V-CON_SYSMETRIC_HISTORY.html
tags:
  - oracle
  - 12c
  - reference
---

`V$CON_SYSMETRIC_HISTORY` displays all PDB long duration (60-second with 1 hour history) system metric values available in the database.

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

Note:

This view is available starting with Oracle Database 12c Release 2 (12.2.0.1).