---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_SR_GRP_STATUS.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.384 DBA\_SR\_GRP\_STATUS

`DBA_SR_GRP_STATUS` provides information on the current refresh operations for the current synchronous refresh groups in the database. It has the same columns as the `DBA_SR_GRP_STATUS_ALL` view.

Refresh operations are controlled using the `DBMS_SYNC_REFRESH` package.

Related View

`USER_SR_GRP_STATUS` provides information on the current refresh operations for the current synchronous refresh groups in the database which are owned by the current user. Its columns are the same as those in `DBA_SR_GRP_STATUS`.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the refresh operation, which is the user who launched the operation |
| `GROUP_ID` | `NUMBER` | `NOT NULL` | Group ID of the synchronous refresh group |
| `OPERATION` | `VARCHAR2(7)` |  | The phase of the refresh operation performed:  - `PREPARE` - `EXECUTE` |
| `STATUS` | `VARCHAR2(10)` |  | The status of the refresh operation:  - `RUNNING` - `NOT PROCESSED` - `COMPLETE` - `ERROR-SOFT` - `ERROR-HARD` - `ABORT` - `PARTIAL` |
| `NUM_TBLS` | `NUMBER` | `NOT NULL` | The number of tables in the synchronous refresh group |
| `NUM_MVS` | `NUMBER` | `NOT NULL` | The number of materialized views in the synchronous refresh group |
| `BASE_TBLS_REFR_STATUS` | `VARCHAR2(13)` |  | Indicates the refresh status of base tables in the synchronous refresh group. The possible values are:  - `NOT PROCESSED` - `COMPLETE` - `ABORT` |
| `NUM_MVS_COMPLETED` | `NUMBER` |  | The number of materialized views which have completed refresh in the synchronous refresh group |
| `NUM_MVS_ABORTED` | `NUMBER` |  | The number of materialized views which have terminated refresh in the synchronous refresh group |
| `ERROR_NUMBER` | `NUMBER` |  | Error number of the run (if any) |
| `ERROR_MESSAGE` | `VARCHAR2(4000)` |  | Error message of the run (if any) |
| `PREPARE_START_TIME` | `DATE` |  | Time that the `PREPARE_REFRESH` phase of the run started |
| `PREPARE_END_TIME` | `DATE` |  | Time that the `PREPARE_REFRESH` phase of the run ended |
| `EXECUTE_START_TIME` | `DATE` |  | Time that the `EXECUTE_REFRESH` phase of the run started |
| `EXECUTE_END_TIME` | `DATE` |  | Time that the `EXECUTE_REFRESH` phase of the run ended |

See Also:

- " [USER\_SR\_GRP\_STATUS](USER_SR_GRP_STATUS.md) "
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ARPLS73623) for more information about the `DBMS_SYNC_REFRESH` package