---
title: "V$THRESHOLD_TYPES"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_3110.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$THRESHOLD_TYPES` displays information about threshold types.

| Column | Datatype | Description |
| --- | --- | --- |
| `METRICS_ID` | `NUMBER` | Metrics ID |
| `METRICS_GROUP_ID` | `NUMBER` | Metrics group ID |
| `OPERATOR_MASK` | `NUMBER` | Operator mask |
| `OBJECT_TYPE` | `VARCHAR2(64)` | Object type: - `SYSTEM` - `FILE` - `SERVICE` - `EVENT_CLASS` - `TABLESPACE` - `SESSION` |
| `ALERT_REASON_ID` | `NUMBER` | ID of the alert reason |
| `METRIC_VALUE_TYPE` | `NUMBER` | Metric value type |