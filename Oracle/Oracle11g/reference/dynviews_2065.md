---
title: "V$METRIC_HISTORY"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2065.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$METRIC_HISTORY` displays all the available statistic values for the complete set of metrics captured by the AWR infrastructure.

| Column | Datatype | Description |
| --- | --- | --- |
| `BEGIN_TIME` | `DATE` | Begin time for the metric value |
| `END_TIME` | `DATE` | End time for the metric value |
| `INTSIZE_CSEC` | `NUMBER` | Size of the time period |
| `GROUP_ID` | `NUMBER` | Metric Group ID. Refer to the `V$METRICNAME` view for the name of the group. |
| `ENTITY_ID` | `NUMBER` | Entity ID for the metric in question. The value of the Entity ID depends upon the metric group. (See the table in the description of `V$METRIC` for an explanation of possible values.) |
| `ENTITY_SEQUENCE` | `NUMBER` | Entity Sequence number for the metric in question. The value of the Entity Sequence depends upon the metric group. (See the table in the description of `V$METRIC` for an explanation of possible values.) |
| `METRIC_ID` | `NUMBER` | Metric ID |
| `METRIC_NAME` | `VARCHAR2(64)` | Metric Name. This is the statistic that is captured for the entity. |
| `VALUE` | `NUMBER` | Value of the statistic between `BEGIN_TIME` and `END_TIME` |
| `METRIC_UNIT` | `VARCHAR2(64)` | Unit for the `VALUE` |