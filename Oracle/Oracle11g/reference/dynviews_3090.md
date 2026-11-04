---
title: "V$SYSMETRIC"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_3090.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$SYSMETRIC` displays the system metric values captured for the most current time interval for both the long duration (60-second) and short duration (15-second) system metrics.

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