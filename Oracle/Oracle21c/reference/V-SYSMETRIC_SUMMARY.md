---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-SYSMETRIC_SUMMARY.html
tags:
  - oracle
  - 21c
  - reference
---

## 10.97 V$SYSMETRIC\_SUMMARY

The average, maximum value, minimum value, and the value of one standard deviation for the last hour are displayed for each metric item.

| Column | Datatype | Description |
| --- | --- | --- |
| `BEGIN_TIME` | `DATE` | Begin time of the interval |
| `END_TIME` | `DATE` | End time of the interval |
| `INTSIZE_CSEC` | `NUMBER` | Interval size (in hundredths of a second) |
| `GROUP_ID` | `NUMBER` | Metric group ID |
| `METRIC_ID` | `NUMBER` | Metric ID |
| `METRIC_NAME` | `VARCHAR2(64)` | Metric name |
| `NUM_INTERVAL` | `NUMBER` | Number of intervals observed |
| `MAXVAL` | `NUMBER` | Maximum value observed |
| `MINVAL` | `NUMBER` | Minimum value observed |
| `AVERAGE` | `NUMBER` | Average value over the period |
| `STANDARD_DEVIATION` | `NUMBER` | One standard deviation |
| `METRIC_UNIT` | `VARCHAR2(64)` | Metric unit description |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - n: Where n is the applicable container ID for the rows containing data |