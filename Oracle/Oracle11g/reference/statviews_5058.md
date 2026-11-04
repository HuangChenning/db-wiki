---
title: DBA_TABLESPACE_THRESHOLDS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5058.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_TABLESPACE_THRESHOLDS` describes space utilization threshold settings for all tablespaces in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `TABLESPACE_NAME` | `VARCHAR2(30)` |  | Tablespace name |
| `CONTENTS` | `VARCHAR2(9)` |  | Tablespace contents: |
| `EXTENT_MANAGEMENT` | `VARCHAR2(10)` |  | Indicates whether the extents in the tablespace are dictionary managed (`DICTIONARY`) or locally managed (`LOCAL`) |
| `THRESHOLD_TYPE` | `VARCHAR2(8)` |  | Source of the threshold: - `EXPLICIT` - `DEFAULT` - `NONE` |
| `METRICS_NAME` | `VARCHAR2(64)` |  | Name of the metric being monitored |
| `WARNING_OPERATOR` | `VARCHAR2(12)` |  | Relational operator for warning thresholds: - `GT` - `EQ` - `LT` - `LE` - `GE` - `CONTAINS` - `NE` - `DO NOT CHECK` - `DO_NOT_CHECK` |
| `WARNING_VALUE` | `VARCHAR2(256)` |  | Warning threshold value |
| `CRITICAL_OPERATOR` | `VARCHAR2(12)` |  | Relational operator for critical thresholds: - `GT` - `EQ` - `LT` - `LE` - `GE` - `CONTAINS` - `NE` - `DO NOT CHECK` - `DO_NOT_CHECK` |
| `CRITICAL_VALUE` | `VARCHAR2(256)` |  | Critical threshold value |