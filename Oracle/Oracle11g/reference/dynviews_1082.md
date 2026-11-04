---
title: "V$CLIENT_STATS"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1082.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$CLIENT_STATS` displays measures for all sessions that are active for the client identifier per instance. The statistics available in this view are a subset of those available in `V$SESSTAT` and `V$SESS_TIME_MODEL`.

| Column | Datatype | Description |
| --- | --- | --- |
| `CLIENT_IDENTIFIER` | `VARCHAR2(64)` | Client identifier |
| `STAT_ID` | `NUMBER` | Statistic identifier |
| `STAT_NAME` | `VARCHAR2(64)` | Derived statistic name from `V$STATNAME` and `V$SESS_TIME_MODEL` |
| `VALUE` | `NUMBER` | Cumulative value (in microseconds) |