---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_SR_OBJ_STATUS_ALL.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.389 DBA\_SR\_OBJ\_STATUS\_ALL

`DBA_SR_OBJ_STATUS_ALL` provides information on the status of objects registered for synchronous refresh.

The view contains information on the status of the objects of both the current and past runs of both current and defunct groups. Therefore, this view can be used to examine the history of synchronous refresh operations. The current run of a group is the most recent run of a group; a current group is a currently valid group, which is capable of being refreshed. A group becomes defunct when it is unregistered for any reason, either explicitly by the user or implicitly as a side-effect when the user registers materialized views related to the materialized views in the group.

To see information on the status of refresh operations for the most recent runs of only the current groups, use the `DBA_SR_OBJ_STATUS` view.

Related View

`USER_SR_OBJ_STATUS_ALL` provides information on the status of objects registered for synchronous refresh in the database which are owned by the current user. Its columns are the same as those in `DBA_SR_OBJ_STATUS_ALL`.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the synchronous refresh object |
| `NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the synchronous refresh object |
| `TYPE` | `VARCHAR2(5)` |  | Type of synchronous refresh object:  - `MVIEW` - `TABLE` |
| `GROUP_ID` | `NUMBER` | `NOT NULL` | Group ID of the synchronous refresh group to which this object belongs |
| `STATUS` | `VARCHAR2(13)` |  | Status of the synchronous refresh object:  - `NOT PROCESSED` - `COMPLETE` - `ABORT` |
| `CURRENT_RUN` | `VARCHAR2(1)` |  | Indicates whether the record is for the most recent refresh operation on the group:  - `Y` - Yes - `N` - No |
| `CURRENT_GROUP` | `VARCHAR2(1)` |  | Indicates whether the record is for a current group:  - `Y` - Yes - `N` - No |
| `ERROR_NUMBER` | `NUMBER` |  | Error number of the run (if any) |
| `ERROR_MESSAGE` | `VARCHAR2(4000)` |  | Error message of the run (if any) |
| `LAST_MODIFIED_TIME` | `DATE` |  | Last modification time of the synchronous refresh object |

See Also:

" [USER\_SR\_OBJ\_STATUS\_ALL](USER_SR_OBJ_STATUS_ALL.md) "