---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-SQL_MONITOR_STATNAME.html
tags:
  - oracle
  - 21c
  - reference
---

## 10.57 V$SQL\_MONITOR\_STATNAME

`V$SQL_MONITOR_STATNAME` provides information about the plan line statistics exposed in `V$SQL_PLAN_MONITOR`. A plan line statistic is identified by its group ID (column `GROUP_ID`) and its ID (column `ID`).

| Column | Datatype | Description |
| --- | --- | --- |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |
| `ID` | `NUMBER` | Plan line statistic ID |
| `GROUP_ID` | `NUMBER` | Plan line statistic group ID |
| `NAME` | `VARCHAR2(40)` | Short name for the statistic |
| `DESCRIPTION` | `VARCHAR2(200)` | Short description for the statistic |
| `TYPE` | `NUMBER` | Reserved for internal use |
| `FLAGS` | `NUMBER` | Reserved for internal use |

See Also:

" [V$SQL\_PLAN\_MONITOR](V-SQL_PLAN_MONITOR.md) "