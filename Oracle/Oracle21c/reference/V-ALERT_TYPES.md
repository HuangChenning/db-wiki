---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-ALERT_TYPES.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.12 V$ALERT\_TYPES

`V$ALERT_TYPES` displays information about server alert types.

| Column | Datatype | Description |
| --- | --- | --- |
| `REASON_ID` | `NUMBER` | ID of the alert reason |
| `OBJECT_TYPE` | `VARCHAR2(64)` | Object type |
| `TYPE` | `VARCHAR2(9)` | Alert type:  - `Stateful` - `Stateless` |
| `GROUP_NAME` | `VARCHAR2(64)` | Group name |
| `SCOPE` | `VARCHAR2(8)` | Scope:  - `Database` - `Instance` |
| `INTERNAL_METRIC_CATEGORY` | `VARCHAR2(64)` | Internal metric category |
| `INTERNAL_METRIC_NAME` | `VARCHAR2(64)` | Internal metric name |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |