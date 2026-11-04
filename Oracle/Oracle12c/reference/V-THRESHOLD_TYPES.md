---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/V-THRESHOLD_TYPES.html
tags:
  - oracle
  - 12c
  - reference
---

| Column | Datatype | Description |
| --- | --- | --- |
| `METRICS_ID` | `NUMBER` | Metrics ID |
| `METRICS_GROUP_ID` | `NUMBER` | Metrics group ID |
| `OPERATOR_MASK` | `NUMBER` | Operator mask |
| `OBJECT_TYPE` | `VARCHAR2(64)` | Object type:  - `SYSTEM` - `FILE` - `SERVICE` - `EVENT_CLASS` - `TABLESPACE` - `SESSION` |
| `ALERT_REASON_ID` | `NUMBER` | ID of the alert reason |
| `METRIC_VALUE_TYPE` | `NUMBER` | Metric value type |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |