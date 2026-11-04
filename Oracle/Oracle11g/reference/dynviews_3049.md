---
title: "V$SQL_CS_STATISTICS"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_3049.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$SQL_CS_STATISTICS` contains the raw execution statistics used by the monitoring component of adaptive cursor sharing. A sample of the executions is monitored. This view exposes which executions were sampled, and what the statistics were for those executions. The statistics are cumulative for each distinct set of bind values.

| Column | Datatype | Description |
| --- | --- | --- |
| `ADDRESS` | `RAW(4)` | Address of the handle to the parent for this cursor |
| `HASH_VALUE` | `NUMBER` | Hash value of the parent statement in the library cache |
| `SQL_ID` | `VARCHAR2(13)` | SQL identifier of the parent cursor in the library cache |
| `CHILD_NUMBER` | `NUMBER` | Number of the child cursor being monitored |
| `BIND_SET_HASH_VALUE` | `NUMBER` | Hash of the values of the binds |
| `PEEKED` | `VARCHAR2(1)` | Indicates if this is the bind set used to build the cursor (Y) or not (N) |
| `EXECUTIONS` | `NUMBER` | Number of times this bind set has been executed and monitored |
| `ROWS_PROCESSED` | `NUMBER` | Cumulative number of rows processed by all row sources in the plan over all monitored executions with this bind set |
| `BUFFER_GETS` | `NUMBER` | Cumulative number of buffer gets over all monitored executions with this bind set |
| `CPU_TIME` | `NUMBER` | Cumulative CPU time (in microseconds) used by this cursor for monitored executions with this bind set |