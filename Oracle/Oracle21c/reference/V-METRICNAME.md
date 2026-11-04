---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-METRICNAME.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.83 V$METRICNAME

`V$METRICNAME` displays the mapping of the name of metrics to their metric ID.

| Column | Datatype | Description |
| --- | --- | --- |
| `GROUP_ID` | `NUMBER` | Metric group ID |
| `GROUP_NAME` | `VARCHAR2(64)` | Metric group name |
| `METRIC_ID` | `NUMBER` | Metric ID |
| `METRIC_NAME` | `VARCHAR2(64)` | Metric name |
| `METRIC_UNIT` | `VARCHAR2(64)` | Unit of measurement |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |