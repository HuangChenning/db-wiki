---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_ANALYTIC_VIEW_AGGR_FNS_AE.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.15 ALL\_ANALYTIC\_VIEW\_AGGR\_FNS\_AE

`ALL_ANALYTIC_VIEW_AGGR_FNS_AE` describes the aggregation functions of the analytic views (across all editions) accessible to the current user.

Related Views

- `DBA_ANALYTIC_VIEW_AGGR_FNS_AE` describes the aggregation functions of all analytic views (across all editions) in the database.
- `USER_ANALYTIC_VIEW_AGGR_FNS_AE` describes the aggregation functions of the analytic views (across all editions) owned by the current user. This view does not display the `OWNER` or `ORIGIN_CON_ID` columns.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the analytic view |
| `ANALYTIC_VIEW_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the analytic view |
| `AGGR_GROUP_NAME` | `VARCHAR2(128)` | `NOT NULL` | Aggregation group name of the analytic view aggregation function |
| `FUNCTION_NAME` | `VARCHAR2(128)` |  | Name of the analytic view aggregation function |
| `DEPTH` | `NUMBER` | `NOT NULL` | Depth of the inner aggregation function |
| `IS_DISTINCT` | `VARCHAR2(1)` |  | Column that indicates if the function uses the distinct modifier |
| `ORIGIN_CON_ID` | `NUMBER` |  | The ID of the container where the data originates. Possible values include:  - `0`: This value is used for rows in non-CDBs. This value is not used for CDBs. - n: This value is used for rows containing data that originate in the container with container ID n (n = 1 if the row originates in root). |
| `EDITION_NAME` | `VARCHAR2(128)` |  | Name of the application edition where the analytic view is defined |

Note:

This view is available starting with Oracle Database 21c, Release Update 21.5.

See Also:

- " [DBA\_ANALYTIC\_VIEW\_AGGR\_FNS\_AE](DBA_ANALYTIC_VIEW_AGGR_FNS_AE.md) "
- " [USER\_ANALYTIC\_VIEW\_AGGR\_FNS\_AE](USER_ANALYTIC_VIEW_AGGR_FNS_AE.md) "