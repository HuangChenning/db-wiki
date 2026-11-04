---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_SR_OBJ_ALL.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.387 DBA\_SR\_OBJ\_ALL

`DBA_SR_OBJ_ALL` provides information on the objects registered for synchronous refresh for current and defunct groups.

To see information on the objects registered for synchronous refresh for only the current groups, use the `DBA_SR_OBJ` view.

Related View

`USER_SR_OBJ_ALL` provides information on the objects registered for synchronous refresh for current and defunct groups for the current user. Its columns are the same as those in `DBA_SR_OBJ_ALL`.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the synchronous refresh object |
| `NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the synchronous refresh object |
| `TYPE` | `VARCHAR2(5)` |  | Type of synchronous refresh object:  - `MVIEW` - `TABLE` |
| `GROUP_ID` | `NUMBER` | `NOT NULL` | Group ID of the synchronous refresh group to which this object belongs |
| `CURRENT_GROUP` | `VARCHAR2(1)` |  | Indicates whether the record is for a current group:  - `Y` - Yes - `N` - No |
| `STAGING_LOG_NAME` | `VARCHAR2(128)` |  | Name of the staging log for tables. This column has a value of NULL for materialized views. |

See Also:

" [USER\_SR\_OBJ\_ALL](USER_SR_OBJ_ALL.md) "