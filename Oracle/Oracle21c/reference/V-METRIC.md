---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-METRIC.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.80 V$METRIC

`V$METRIC` displays the most recent statistic values for the complete set of metrics captured by the Automatic Workload Repository (AWR) infrastructure.

| Column | Datatype | Description |
| --- | --- | --- |
| `BEGIN_TIME` | `DATE` | Begin time of the interval |
| `END_TIME` | `DATE` | End time of the interval |
| `INTSIZE_CSEC` | `NUMBER` | Interval size (in hundredths of a second) |
| `GROUP_ID` | `NUMBER` | Metric Group ID. Refer to the `V$METRICNAME` view for the name of the group. |
| `ENTITY_ID` | `NUMBER` | Entity ID for the metric in question. The value of the Entity ID depends upon the metric group. (See the following table for an explanation of possible values.) |
| `ENTITY_SEQUENCE` | `NUMBER` | Entity Sequence number for the metric in question. The value of the Entity Sequence depends upon the metric group. (See the following table for an explanation of possible values.) |
| `METRIC_ID` | `NUMBER` | Metric ID |
| `METRIC_NAME` | `VARCHAR2(64)` | Metric Name. This is the statistic that is captured for the entity. |
| `VALUE` | `NUMBER` | Value of the statistic between `BEGIN_TIME` and `END_TIME` |
| `METRIC_UNIT` | `VARCHAR2(64)` | Unit for the `VALUE` |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

The following table describes what the `ENTITY_ID` and `ENTITY_SEQUENCE` are for each metric group:

| GID | Group NAME | Entity ID | Entity Sequence |
| --- | --- | --- | --- |
| 0 | Event Metrics | Event# | N/A |
| 1 | Event Class Metrics | Wait Class ID | N/A |
| 2 | System Metrics Long Duration | N/A | N/A |
| 3 | System Metrics Short Duration | N/A | N/A |
| 4 | Session Metrics Long Duration | Session ID | Serial# |
| 5 | Session Metrics Short Duration | Session ID | Serial# |
| 6 | Service Metrics | N/A | Service Hash |
| 7 | File Metrics Long Duration | File# | Creation Change# |
| 9 | Tablespace Metrics Long Duration | Tablespace# | N/A |
| 10 | Service Metrics (Short) | N/A | Service Hash |