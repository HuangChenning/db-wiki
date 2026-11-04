---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_ANALYTIC_VIEWS_AE.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.61 ALL\_ANALYTIC\_VIEWS\_AE

`ALL_ANALYTIC_VIEWS_AE` describes the analytic views (across all editions) accessible to the current user.

Related Views

- `DBA_ANALYTIC_VIEWS_AE` describes all analytic views (across all editions) in the database.
- `USER_ANALYTIC_VIEWS_AE` describes the analytic views (across all editions) owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the analytic view |
| `ANALYTIC_VIEW_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the analytic view |
| `TABLE_OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the fact table or view on which the analytic view is defined |
| `TABLE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the fact table or view on which the analytic view is defined |
| `TABLE_ALIAS` | `VARCHAR2(128)` |  | Alias of the fact table or view on which the analytic view is defined; the default is `TABLE_NAME` |
| `IS_REMOTE` | `VARCHAR2(1)` |  | Indicates whether the source is a remote table. The values are:  - `Y` - Remote table - `N` - Local table |
| `DEFAULT_AGGR` | `VARCHAR2(128)` |  | Default aggregation of the analytic view |
| `DEFAULT_AGGR_GROUP_NAME` | `VARCHAR2(128)` | `NOT NULL` | Always `DEFAULT_AGGREGATION$` at present |
| `DEFAULT_MEASURE` | `VARCHAR2(128)` |  | Name of the default measure of the analytic view |
| `COMPILE_STATE` | `VARCHAR2(7)` |  | Compile status of the analytic view:  - `VALID` - `INVALID` |
| `DYN_ALL_CACHE` | `VARCHAR2(1)` |  | The value of this column is always `N` |
| `QUERY_TRANSFORM_ENABLED` | `VARCHAR2(1)` |  | Indicates whether query transformation is enabled for the analytic view (`Y`) or not (`N`) |
| `QUERY_TRANSFORM_RELY` | `VARCHAR2(1)` |  | Indicates whether the `RELY` option is specified for the query transformation (`Y`) or not (`N`) |
| `ORIGIN_CON_ID` | `NUMBER` |  | The ID of the container where the data originates. Possible values include:  - `0`: This value is used for rows in non-CDBs. This value is not used for CDBs. - n: This value is used for rows containing data that originate in the container with container ID n (n = 1 if the row originates in root). |
| `EDITION_NAME` | `VARCHAR2(128)` |  | Name of the application edition where the analytic view is defined |

Note:

This view is available starting with Oracle Database 21c, Release Update 21.5.

See Also:

- " [DBA\_ANALYTIC\_VIEWS\_AE](DBA_ANALYTIC_VIEWS_AE.md) "
- " [USER\_ANALYTIC\_VIEWS\_AE](USER_ANALYTIC_VIEWS_AE.md) "