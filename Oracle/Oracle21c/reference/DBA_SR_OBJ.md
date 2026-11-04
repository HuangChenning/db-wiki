---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_SR_OBJ.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.386 DBA\_SR\_OBJ

`DBA_SR_OBJ` provides information on the objects registered for synchronous refresh for current groups.

Related View

`USER_SR_OBJ` provides information on the objects registered for synchronous refresh for current groups for the current user. Its columns are the same as those in `DBA_SR_OBJ`.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the synchronous refresh object |
| `NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the synchronous refresh object |
| `TYPE` | `VARCHAR2(5)` |  | Type of synchronous refresh object:  - `MVIEW` - `TABLE` |
| `GROUP_ID` | `NUMBER` | `NOT NULL` | Group ID of the synchronous refresh group to which this object belongs |
| `STAGING_LOG_NAME` | `VARCHAR2(128)` |  | Name of the staging log for tables. This column has a value of NULL for materialized views. |

See Also:

" [USER\_SR\_OBJ](USER_SR_OBJ.md) "