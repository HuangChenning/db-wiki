---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-SYSMETRIC_HISTORY.html
tags:
  - oracle
  - 21c
  - reference
---

## 10.96 V$SYSMETRIC\_HISTORY

Both long duration (60-second with 1 hour history) and short duration (15-second with one-interval only) metrics are displayed by this view.

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
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - n: Where n is the applicable container ID for the rows containing data |