---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_SR_OBJ_STATUS.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.388 DBA\_SR\_OBJ\_STATUS

`DBA_SR_OBJ_STATUS` provides information on the status of objects registered for synchronous refresh for the current refresh operations for the current synchronous refresh groups in the database.

To see information on the status of objects registered for synchronous refresh, use the `DBA_SR_OBJ_STATUS_ALL` view.

Related View

`USER_SR_OBJ_STATUS` provides information on the status of objects registered for synchronous refresh for the current refresh operations for the current synchronous refresh groups in the database which are owned by the current user. Its columns are the same as those in `DBA_SR_OBJ_STATUS`.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the synchronous refresh object |
| `NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the synchronous refresh object |
| `TYPE` | `VARCHAR2(5)` |  | Type of synchronous refresh object:  - `MVIEW` - `TABLE` |
| `GROUP_ID` | `NUMBER` | `NOT NULL` | Group ID of the synchronous refresh group to which this object belongs |
| `STATUS` | `VARCHAR2(13)` |  | Status of the synchronous refresh object:  - `NOT PROCESSED` - `COMPLETE` - `ABORT` |
| `ERROR_NUMBER` | `NUMBER` |  | Error number of the run (if any) |
| `ERROR_MESSAGE` | `VARCHAR2(4000)` |  | Error message of the run (if any) |
| `LAST_MODIFIED_TIME` | `DATE` |  | Last modification time of the synchronous refresh object |

See Also:

" [USER\_SR\_OBJ\_STATUS](USER_SR_OBJ_STATUS.md) "