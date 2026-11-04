---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-SERVICE_STATS.html
tags:
  - oracle
  - 21c
  - reference
---

## 10.9 V$SERVICE\_STATS

`V$SERVICE_STATS` displays a minimal set of performance statistics. These call rate statistics are used for making run-time routing decisions, for tracking service levels, and for per-instance diagnostics per call rate. The elapsed timing for each call provides a relative value across instances for how well a node is processing SQL calls issued under a service name.

When aggregation is enabled for the Service Name, then this view provides the timing and work done for calls issued for the whole service.

| Column | Datatype | Description |
| --- | --- | --- |
| `SERVICE_NAME_HASH` | `NUMBER` | Service name hash from `V$SERVICES` |
| `SERVICE_NAME` | `VARCHAR2(64)` | Service name from `V$SERVICES` |
| `STAT_ID` | `NUMBER` | Statistic identifier |
| `STAT_NAME` | `VARCHAR2(64)` | Derived statistic name from `V$STATNAME` and `V$SESS_TIME_MODEL` |
| `VALUE` | `NUMBER` | For statistics that measure time (such as the DB CPU, background elapsed time, or parse time elapsed statistics), this column displays a cumulative value in microseconds.  For other statistics that do not measure time (such as the db block changes, execute count, or logons cumulative statistics), this column displays the appropriate numeric value for the statistic. |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |