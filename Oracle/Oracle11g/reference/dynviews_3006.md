---
title: "V$SERV_MOD_ACT_STATS"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_3006.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$SERV_MOD_ACT_STATS` displays the same set of performance statistics as `V$SERVICE_STATS` except for a specific combination of service/module/action names.

When aggregation is enabled for the service name, module, and action name, then this view provides the timing and work done for calls issued for the business transaction.

| Column | Datatype | Description |
| --- | --- | --- |
| `AGGREGATION_TYPE` | `VARCHAR2(21)` | Aggregation statistic type: - `SERVICE_MODULE` - Action value is NULL and the entry is an aggregate for all actions within a given module - `SERVICE_MODULE_ACTION` - Action value is NULL only for an empty action, and the aggregation is on the level of service/module/action |
| `SERVICE_NAME` | `VARCHAR2(64)` | Service name from `V$SERVICES` |
| `MODULE` <sup>Foot 1</sup> | `VARCHAR2(49)` | Module name from `DBA_ENABLED_AGGREGATIONS` |
| `ACTION` <sup>Footref 1</sup> | `VARCHAR2(33)` | Action name from `DBA_ENABLED_AGGREGATIONS` |
| `STAT_ID` | `NUMBER` | Statistic identifier |
| `STAT_NAME` | `VARCHAR2(64)` | Derived statistic name from `V$STATNAME` and `V$SESS_TIME_MODEL` |
| `VALUE` | `NUMBER` | Cumulative value (in microseconds) |

<sup>Footnote 1</sup> The datatype of this column is `VARCHAR2(65)` starting with Oracle Database 11g Release 2 (11.2.0.2).