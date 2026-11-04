---
title: "V$SYSMETRIC_SUMMARY"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_3092.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$SYSMETRIC_SUMMARY` displays a summary of all system Metric values for the long-duration system metrics. The average, maximum value, minimum value, and the value of one standard deviation for the last hour are displayed for each metric item.

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