---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-AW_CALC.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.78 V$AW\_CALC

`V$AW_CALC` reports on the effectiveness of various caches used by Oracle OLAP during dynamic aggregation.

| Column | Datatype | Description |
| --- | --- | --- |
| `SESSION_ID` | `NUMBER` | A unique numeric identifier for the session. |
| `AGGREGATE_CACHE_HITS` | `NUMBER` | The number of times a dimension member is found in the aggregate cache (a hit).  The number of hits for run-time aggregation can be increased by fetching data across the dense dimension |
| `AGGREGATE_CACHE_MISSES` | `NUMBER` | The number of times a dimension member is not found in the aggregate cache and must be read from disk (a miss). |
| `SESSION_CACHE_HITS` | `NUMBER` | The number of times the data is found in the session cache (a hit). |
| `SESSION_CACHE_MISSES` | `NUMBER` | The number of times the data is not found in the session cache (a miss). |
| `POOL_HITS` | `NUMBER` | The number of times the data is found in a page in the OLAP page pool (a hit). |
| `POOL_MISSES` | `NUMBER` | The number of times the data is not found in the OLAP page pool (a miss). |
| `POOL_NEW_PAGES` | `NUMBER` | The number of newly created pages in the OLAP page pool that have not yet been written to the workspace LOB. |
| `POOL_RECLAIMED_PAGES` | `NUMBER` | The number of previously unused pages that have been recycled with new data. |
| `CACHE_WRITES` | `NUMBER` | The number of times the data from the OLAP page pool has been written to the database cache. |
| `POOL_SIZE` | `NUMBER` | The number of kilobytes in the OLAP page pool. |
| `CURR_DML_COMMAND` | `VARCHAR2(64)` | The command currently being executed. |
| `PREV_DML_COMMAND` | `VARCHAR2(64)` | The command most recently completed. |
| `AGGR_FUNC_LOGICAL_NA` | `NUMBER` | The number of times the aggregation engine returns a logical NA because the AGGINDEX option is on and the composite tuple does not exist. |
| `AGGR_FUNC_PRECOMPUTE` | `NUMBER` | The number of times the aggregation engine finds a value in a position that it was called to calculate. |
| `AGGR_FUNC_CALCS` | `NUMBER` | The number of times the aggregation engine calculates a parent value based on the values of its children. |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |