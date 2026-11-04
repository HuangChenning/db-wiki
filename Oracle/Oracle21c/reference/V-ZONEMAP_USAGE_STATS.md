---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-ZONEMAP_USAGE_STATS.html
tags:
  - oracle
  - 21c
  - reference
---

## 10.146 V$ZONEMAP\_USAGE\_STATS

| Column | Datatype | Description |
| --- | --- | --- |
| `ZONEMAP` | `VARCHAR2(257)` | Name of the zone map in the form of owner.name |
| `PRUNING_TYPE` | `VARCHAR2(11)` | Type of data pruning performed using the zone map |
| `EXECUTIONS` | `NUMBER` | Number of executions, including parallel worker executions |
| `BASE_COUNT` | `NUMBER` | Base count accumulated over number of executions |
| `PRUNED_COUNT` | `NUMBER` | Pruned count accumulated over number of executions |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

The ratio (`PRUNED_COUNT / BASE_COUNT`) shows the fraction of data pruned by the zone map.