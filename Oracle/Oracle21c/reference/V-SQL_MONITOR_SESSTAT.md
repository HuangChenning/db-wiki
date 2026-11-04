---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-SQL_MONITOR_SESSTAT.html
tags:
  - oracle
  - 21c
  - reference
---

## 10.56 V$SQL\_MONITOR\_SESSTAT

`V$SQL_MONITOR_SESSTAT` displays information about statistics that are exposed in `V$SESSTAT`.

| Column | Datatype | Description |
| --- | --- | --- |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |
| `KEY` | `NUMBER` | Artificial join key to efficiently join with other database operation views |
| `STATISTIC#` | `NUMBER` | Statistic number |
| `VALUE` | `NUMBER` | Value associated with the statistic |

See Also:

" [V$SESSTAT](V-SESSTAT.md) "