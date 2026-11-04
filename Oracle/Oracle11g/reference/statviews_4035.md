---
title: DBA_HIST_SERVICE_STAT
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4035.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_HIST_SERVICE_STAT` displays the history of important service statistics tracked by the Workload Repository. The call rate statistics in this view can be used for making run-time routing decisions, for tracking service levels, and for per-instance diagnostics per call rate.

The elapsed timing for each call provides a relative value across instances for how well a node is processing SQL calls issued under a service name. When aggregation is enabled for the service name, this view provides historical data on the timing and work done for calls issued for the whole service. This view contains information from `V$SERVICE_STATS`.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` |  | Unique snapshot ID |
| `DBID` | `NUMBER` |  | Database ID for the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` |  | Instance number for the snapshot |
| `SERVICE_NAME_HASH` | `NUMBER` |  | Hash of the service name |
| `SERVICE_NAME` | `VARCHAR2(64)` |  | Name of the service |
| `STAT_ID` | `NUMBER` |  | Statistic identifier |
| `STAT_NAME` | `VARCHAR2(64)` |  | Statistic name |
| `VALUE` | `NUMBER` |  | Value of the statistic |