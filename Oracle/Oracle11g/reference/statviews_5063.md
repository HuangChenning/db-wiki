---
title: DBA_THRESHOLDS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5063.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_THRESHOLDS` describes all thresholds.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `METRICS_NAME` | `VARCHAR2(64)` |  | Metrics name |
| `WARNING_OPERATOR` | `VARCHAR2(12)` |  | Relational operator for warning thresholds: - `GT` - `EQ` - `LT` - `LE` - `GE` - `CONTAINS` - `NE` - `DO NOT CHECK` - `DO_NOT_CHECK` |
| `WARNING_VALUE` | `VARCHAR2(256)` |  | Warning threshold value |
| `CRITICAL_OPERATOR` | `VARCHAR2(12)` |  | Relational operator for critical thresholds: - `GT` - `EQ` - `LT` - `LE` - `GE` - `CONTAINS` - `NE` - `DO NOT CHECK` - `DO_NOT_CHECK` |
| `CRITICAL_VALUE` | `VARCHAR2(256)` |  | Critical threshold value |
| `OBSERVATION_PERIOD` | `NUMBER` |  | Observation period length (in minutes) |
| `CONSECUTIVE_OCCURRENCES` | `NUMBER` |  | Number of occurrences before an alert is issued |
| `INSTANCE_NAME` | `VARCHAR2(16)` |  | Instance name; NULL for database-wide alerts |
| `OBJECT_TYPE` | `VARCHAR2(64)` |  | Object type: |
| `OBJECT_NAME` | `VARCHAR2(513)` |  | Name of the object for which the threshold is set |
| `STATUS` | `VARCHAR2(7)` |  | Indicates whether the threshold is applicable on a valid object (`VALID`) or not (`INVALID`) |