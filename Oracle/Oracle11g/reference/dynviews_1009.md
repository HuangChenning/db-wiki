---
title: "V$ALERT_TYPES"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1009.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$ALERT_TYPES` displays information about server alert types.

| Column | Datatype | Description |
| --- | --- | --- |
| `REASON_ID` | `NUMBER` | ID of the alert reason |
| `OBJECT_TYPE` | `VARCHAR2(64)` | Object type |
| `TYPE` | `VARCHAR2(9)` | Alert type: - `Stateful` - `Stateless` |
| `GROUP_NAME` | `VARCHAR2(64)` | Group name |
| `SCOPE` | `VARCHAR2(8)` | Scope: - `Database` - `Instance` |
| `INTERNAL_METRIC_CATEGORY` | `VARCHAR2(64)` | Internal metric category |
| `INTERNAL_METRIC_NAME` | `VARCHAR2(64)` | Internal metric name |