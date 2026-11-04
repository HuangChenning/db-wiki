---
title: "V$METRICNAME"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2066.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$METRICNAME` displays the mapping of the name of metrics to their metric ID.

| Column | Datatype | Description |
| --- | --- | --- |
| `GROUP_ID` | `NUMBER` | Metric group ID |
| `GROUP_NAME` | `VARCHAR2(64)` | Metric group name |
| `METRIC_ID` | `NUMBER` | Metric ID |
| `METRIC_NAME` | `VARCHAR2(64)` | Metric name |
| `METRIC_UNIT` | `VARCHAR2(64)` | Unit of measurement |