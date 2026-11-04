---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_THRESHOLDS.html
tags:
  - oracle
  - 21c
  - reference
---

## 7.53 DBA\_THRESHOLDS

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `METRICS_NAME` | `VARCHAR2(64)` |  | Metrics name |
| `WARNING_OPERATOR` | `VARCHAR2(12)` |  | Relational operator for warning thresholds:  - `GT` - `EQ` - `LT` - `LE` - `GE` - `CONTAINS` - `NE` - `DO NOT CHECK` - `DO_NOT_CHECK` |
| `WARNING_VALUE` | `VARCHAR2(256)` |  | Warning threshold value |
| `CRITICAL_OPERATOR` | `VARCHAR2(12)` |  | Relational operator for critical thresholds:  - `GT` - `EQ` - `LT` - `LE` - `GE` - `CONTAINS` - `NE` - `DO NOT CHECK` - `DO_NOT_CHECK` |
| `CRITICAL_VALUE` | `VARCHAR2(256)` |  | Critical threshold value |
| `OBSERVATION_PERIOD` | `NUMBER` |  | Observation period length (in minutes) |
| `CONSECUTIVE_OCCURRENCES` | `NUMBER` |  | Number of occurrences before an alert is issued |
| `INSTANCE_NAME` | `VARCHAR2(16)` |  | Instance name; NULL for database-wide alerts |
| `OBJECT_TYPE` | `VARCHAR2(64)` |  | Object type:  - `SYSTEM` - `SERVICE` - `EVENT_CLASS` - `TABLESPACE` - `FILE` |
| `OBJECT_NAME` | `VARCHAR2(513)` |  | Name of the object for which the threshold is set |
| `STATUS` | `VARCHAR2(7)` |  | Indicates whether the threshold is applicable on a valid object (`VALID`) or not (`INVALID`)  Thresholds for non-tablespace metrics can only be set in `ROOT` and apply to a CDB as a whole. Any pre-existing non-tablespace thresholds that may exist in a PDB have a status of `INVALID` in the `DBA_THRESHOLDS` view. You can remove these threshold settings using the `DBMS_SERVER_ALERT.SET_THRESHOLD` API.  See [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ARPLS68004) for more information about the `DBMS_SERVER_ALERT.SET_THRESHOLD` API. |