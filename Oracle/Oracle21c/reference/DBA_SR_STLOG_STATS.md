---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_SR_STLOG_STATS.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.392 DBA\_SR\_STLOG\_STATS

`DBA_SR_STLOG_STATS` provides information on the statistics in the staging logs for the tables processed by `DBMS_SYNC_REFRESH.PREPARE_STAGING_LOG`.

These three statistics columns in the staging log are filled in `PREPARE_STAGING_LOG`:

- The number of inserts (`NUM_INSERTS`)
- The number of deletes (`NUM_DELETES`)
- The number of updates (`NUM_UPDATES`)

After the data in the staging logs of a synchronous refresh group have been processed by `PREPARE_REFRESH` and `EXECUTE_REFRESH`, the statistics columns for the tables in the group are cleared and appear as `NULL`.

Related View

`USER_SR_STLOG_STATS` provides information on the statistics in the staging logs for the tables belonging to the current user processed by `DBMS_SYNC_REFRESH.PREPARE_STAGING_LOG`.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the base table registered for synchronous refresh |
| `TABLE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the table |
| `STAGING_LOG_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the staging log for tables. NULL for materialized views |
| `NUM_INSERTS` | `NUMBER` | `NOT NULL` | The number of inserts in the staging log |
| `NUM_DELETES` | `NUMBER` | `NOT NULL` | The number of deletes in the staging log |
| `NUM_UPDATES` | `NUMBER` | `NOT NULL` | The number of updates in the staging log |
| `PSL_MODE` | `VARCHAR2(33)` |  | The mode specified by the user in running `DBMS_SYNC_REFRESH.PREPARE_STAGING_LOG`. Possible values:  - `DELETE_TRUSTED` - `DELETE_TRUSTED and UPDATE_TRUSTED` - `ENFORCED` - `INSERT_TRUSTED` - `INSERT_TRUSTED and DELETE_TRUSTED` - `TRUSTED` - `UPDATE_TRUSTED` - `UPDATE_TRUSTED and INSERT_TRUSTED` |

See Also:

- " [USER\_SR\_STLOG\_STATS](USER_SR_STLOG_STATS.md) "
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ARPLS73623) for more information about the `DBMS_SYNC_REFRESH` package