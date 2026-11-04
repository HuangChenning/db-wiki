---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-SQL_CS_STATISTICS.html
tags:
  - oracle
  - 21c
  - reference
---

## 10.52 V$SQL\_CS\_STATISTICS

A sample of the executions is monitored. This view exposes which executions were sampled, and what the statistics were for those executions. The statistics are cumulative for each distinct set of bind values.

| Column | Datatype | Description |
| --- | --- | --- |
| `ADDRESS` | `RAW(4 \| 8)` | Address of the handle to the parent for this cursor |
| `HASH_VALUE` | `NUMBER` | Hash value of the parent statement in the library cache |
| `SQL_ID` | `VARCHAR2(13)` | SQL identifier of the parent cursor in the library cache |
| `CHILD_NUMBER` | `NUMBER` | Number of the child cursor being monitored |
| `BIND_SET_HASH_VALUE` | `NUMBER` | Hash of the values of the binds |
| `PEEKED` | `VARCHAR2(1)` | Indicates if this is the bind set used to build the cursor (Y) or not (N) |
| `EXECUTIONS` | `NUMBER` | Number of times this bind set has been executed and monitored |
| `ROWS_PROCESSED` | `NUMBER` | Cumulative number of rows processed by all row sources in the plan over all monitored executions with this bind set |
| `BUFFER_GETS` | `NUMBER` | Cumulative number of buffer gets over all monitored executions with this bind set |
| `CPU_TIME` | `NUMBER` | Cumulative CPU time (in microseconds) used by this cursor for monitored executions with this bind set |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |