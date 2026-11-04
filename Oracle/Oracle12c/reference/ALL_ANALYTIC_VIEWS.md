---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/ALL_ANALYTIC_VIEWS.html
tags:
  - oracle
  - 12c
  - reference
---

`ALL_ANALYTIC_VIEWS` describes the analytic views accessible to the current user.

Related Views

- `DBA_ANALYTIC_VIEWS` describes all analytic views in the database.
- `USER_ANALYTIC_VIEWS` describes the analytic views owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the analytic view |
| `ANALYTIC_VIEW_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the analytic view |
| `TABLE_OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the fact table or view on which the analytic view is defined |
| `TABLE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the fact table or view on which the analytic view is defined |
| `TABLE_ALIAS` | `VARCHAR2(128)` |  | Alias of the fact table or view on which the analytic view is defined; the default is `TABLE_NAME` |
| `DEFAULT_AGGR` | `VARCHAR2(128)` |  | Default aggregation of the analytic view |
| `DEFAULT_MEASURE` | `VARCHAR2(128)` |  | Name of the default measure of the analytic view |
| `COMPILE_STATE` | `VARCHAR2(7)` |  | Compile status of the analytic view:  - `VALID` - `INVALID` |
| `ORIGIN_CON_ID` | `NUMBER` |  | The ID of the container where the data originates. Possible values include:  - `0`: This value is used for rows in non-CDBs. This value is not used for CDBs. - n: This value is used for rows containing data that originate in the container with container ID n (n = 1 if the row originates in root). |

Note:

This view is available starting with Oracle Database 12c Release 2 (12.2.0.1).

See Also:

- " [DBA\_ANALYTIC\_VIEWS](DBA_ANALYTIC_VIEWS.md) "
- " [USER\_ANALYTIC\_VIEWS](USER_ANALYTIC_VIEWS.md) "