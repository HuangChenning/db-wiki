---
title: "V$SERVICE_STATS"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_3008.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$SERVICE_STATS` displays a minimal set of performance statistics. These call rate statistics are used for making run-time routing decisions, for tracking service levels, and for per-instance diagnostics per call rate. The elapsed timing for each call provides a relative value across instances for how well a node is processing SQL calls issued under a service name.

When aggregation is enabled for the Service Name, then this view provides the timing and work done for calls issued for the whole service.

| Column | Datatype | Description |
| --- | --- | --- |
| `SERVICE_NAME_HASH` | `NUMBER` | Service name hash from `V$SERVICES` |
| `SERVICE_NAME` | `VARCHAR2(64)` | Service name from `V$SERVICES` |
| `STAT_ID` | `NUMBER` | Statistic identifier |
| `STAT_NAME` | `VARCHAR2(64)` | Derived statistic name from `V$STATNAME` and `V$SESS_TIME_MODEL` |
| `VALUE` | `NUMBER` | Cumulative value (in microseconds) |