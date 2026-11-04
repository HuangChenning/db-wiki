---
title: DBA_HIST_METRIC_NAME
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4011.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_HIST_METRIC_NAME` describes attributes of the set of RDBMS metrics. This view contains a snapshot of `V$METRICNAME`.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID |
| `GROUP_ID` | `NUMBER` | `NOT NULL` | Metric Group ID |
| `GROUP_NAME` | `VARCHAR2(64)` |  | Metric group name |
| `METRIC_ID` | `NUMBER` | `NOT NULL` | Metric ID |
| `METRIC_NAME` | `VARCHAR2(64)` | `NOT NULL` | Metric name |
| `METRIC_UNIT` | `VARCHAR2(64)` | `NOT NULL` | Unit of measurement |