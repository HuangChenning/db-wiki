---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_MVREF_CHANGE_STATS.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.198 DBA\_MVREF\_CHANGE\_STATS

`DBA_MVREF_CHANGE_STATS` displays the change data load information on the base tables associated with a refresh run for all the materialized views for the database.

Related View

`USER_MVREF_CHANGE_STATS` displays the change data load information on the master tables associated with a refresh run for all the materialized views in the database that are accessible to the current user.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `TBL_OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the master table for the materialized view |
| `TBL_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the master table for the materialized view |
| `MV_OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the materialized view |
| `MV_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the materialized view |
| `REFRESH_ID` | `NUMBER` | `NOT NULL` | The refresh ID of the refresh run |
| `NUM_ROWS_INS` | `NUMBER` |  | The number of inserts in the materialized view log of the table (applicable only if the table has a materialized view log) |
| `NUM_ROWS_UPD` | `NUMBER` |  | The number of updates in the materialized view log of the table (applicable only if the table has a materialized view log) |
| `NUM_ROWS_DEL` | `NUMBER` |  | The number of deletes in the materialized view log of the table (applicable only if the table has a materialized view log) |
| `NUM_ROWS_DL_INS` | `NUMBER` |  | The number of direct load inserts on the table |
| `PMOPS_OCCURRED` | `CHAR(1)` |  | Indicates whether a partition-maintenance operation (PMOP) occurred. Possible values:  - `Y` - `N` - `NULL`: Indicates an unknown value |
| `PMOP_DETAILS` | `VARCHAR2(4000)` |  | Details of the PMOPs in the following format:  - `TRUNCATE (low_bound, high_bound)` - `EXECHANGE (low_bound, high_bound)` |
| `NUM_ROWS` | `NUMBER` |  | The number of rows in the table at the start of the refresh operation |

See Also:

" [USER\_MVREF\_CHANGE\_STATS](USER_MVREF_CHANGE_STATS.md) "