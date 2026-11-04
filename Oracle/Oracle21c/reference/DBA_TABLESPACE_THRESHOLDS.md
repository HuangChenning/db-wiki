---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_TABLESPACE_THRESHOLDS.html
tags:
  - oracle
  - 21c
  - reference
---

## 7.48 DBA\_TABLESPACE\_THRESHOLDS

`DBA_TABLESPACE_THRESHOLDS` describes space utilization threshold settings for all tablespaces in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `TABLESPACE_NAME` | `VARCHAR2(30)` |  | Tablespace name |
| `CONTENTS` | `VARCHAR2(9)` |  | Tablespace contents:  - `UNDO` - `PERMANENT` - `TEMPORARY` |
| `EXTENT_MANAGEMENT` | `VARCHAR2(10)` |  | Indicates whether the extents in the tablespace are dictionary managed (`DICTIONARY`) or locally managed (`LOCAL`) |
| `THRESHOLD_TYPE` | `VARCHAR2(8)` |  | Indicates whether the threshold value is derived from a `DEFAULT` threshold or an `EXPLICIT` threshold |
| `METRICS_NAME` | `VARCHAR2(64)` |  | Name of the metric for which the threshold is set |
| `WARNING_OPERATOR` | `VARCHAR2(12)` |  | Relational operator for warning thresholds:  - `GT` - `EQ` - `LT` - `LE` - `GE` - `CONTAINS` - `NE` - `DO_NOT_CHECK` |
| `WARNING_VALUE` | `VARCHAR2(256)` |  | Warning threshold value |
| `CRITICAL_OPERATOR` | `VARCHAR2(12)` |  | Relational operator for critical thresholds:  - `GT` - `EQ` - `LT` - `LE` - `GE` - `CONTAINS` - `NE` - `DO_NOT_CHECK` |
| `CRITICAL_VALUE` | `VARCHAR2(256)` |  | Critical threshold value |