---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_SR_STLOG_EXCEPTIONS.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.391 DBA\_SR\_STLOG\_EXCEPTIONS

`DBA_SR_STLOG_EXCEPTIONS` provides information on the exceptions in the staging logs for the tables processed by `DBMS_SYNC_REFRESH`.`PREPARE_STAGING_LOG`.

Related View

`USER_SR_STLOG_EXCEPTIONS` provides information on the exceptions in the staging logs for the tables belonging to the current user processed by `DBMS_SYNC_REFRESH`.`PREPARE_STAGING_LOG`. Its columns are the same as those in `DBA_SR_STLOG_EXCEPTIONS`.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the base table registered for synchronous refresh |
| `TABLE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the base table registered for synchronous refresh |
| `STAGING_LOG_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the staging log for tables. This column has a value of NULL for materialized views. |
| `BAD_ROWID` | `ROWID` | `NOT NULL` | Row ID of the staging log row causing the exception for the synchronous refresh |
| `ERROR_NUMBER` | `NUMBER` |  | Error number of the exception for the synchronous refresh |
| `ERROR_MESSAGE` | `VARCHAR2(4000)` |  | Error message associated with the `ERROR_NUMBER` for the synchronous refresh |

See Also:

- " [USER\_SR\_STLOG\_EXCEPTIONS](USER_SR_STLOG_EXCEPTIONS.md) "
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ARPLS73623) for more information about the `DBMS_SYNC_REFRESH` package