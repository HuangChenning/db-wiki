---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-METRIC_HISTORY.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.82 V$METRIC\_HISTORY

`V$METRIC_HISTORY` displays all the available statistic values for the complete set of metrics captured by the Automatic Workload Repository (AWR) infrastructure.

| Column | Datatype | Description |
| --- | --- | --- |
| `BEGIN_TIME` | `DATE` | Begin time of the interval |
| `END_TIME` | `DATE` | End time of the interval |
| `INTSIZE_CSEC` | `NUMBER` | Interval size (in hundredths of a second) |
| `GROUP_ID` | `NUMBER` | Metric Group ID. Refer to the `V$METRICNAME` view for the name of the group. |
| `ENTITY_ID` | `NUMBER` | Entity ID for the metric in question. The value of the Entity ID depends upon the metric group. (See the table in the description of `V$METRIC` for an explanation of possible values.) |
| `ENTITY_SEQUENCE` | `NUMBER` | Entity Sequence number for the metric in question. The value of the Entity Sequence depends upon the metric group. (See the table in the description of `V$METRIC` for an explanation of possible values.) |
| `METRIC_ID` | `NUMBER` | Metric ID |
| `METRIC_NAME` | `VARCHAR2(64)` | Metric Name. This is the statistic that is captured for the entity. |
| `VALUE` | `NUMBER` | Value of the statistic between `BEGIN_TIME` and `END_TIME` |
| `METRIC_UNIT` | `VARCHAR2(64)` | Unit for the `VALUE` |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |