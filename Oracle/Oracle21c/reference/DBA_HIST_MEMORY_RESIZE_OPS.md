---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_HIST_MEMORY_RESIZE_OPS.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.9 DBA\_HIST\_MEMORY\_RESIZE\_OPS

This view contains snapshots of `V$MEMORY_RESIZE_OPS`.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` | `NOT NULL` | Unique snapshot ID |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID for the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` | `NOT NULL` | Instance number for the snapshot |
| `COMPONENT` | `VARCHAR2(64)` | `NOT NULL` | Component name |
| `OPER_TYPE` | `VARCHAR2(13)` | `NOT NULL` | Operation type:  - `STATIC` - `INITIALIZING` - `DISABLED` - `GROW` - `SHRINK` - `SHRINK_CANCEL` |
| `START_TIME` | `DATE` | `NOT NULL` | Start time of the operation |
| `END_TIME` | `DATE` | `NOT NULL` | End time of the operation |
| `TARGET_SIZE` | `NUMBER` | `NOT NULL` | Requested value of the parameter after the resize |
| `OPER_MODE` | `VARCHAR2(9)` |  | Operation mode:  - `MANUAL` - `DEFERRED` - `IMMEDIATE` |
| `PARAMETER` | `VARCHAR2(80)` |  | Name of the parameter for the resize operation |
| `INITIAL_SIZE` | `NUMBER` |  | Parameter value at the start of the operation |
| `FINAL_SIZE` | `NUMBER` |  | Real value of the parameter after the resize |
| `STATUS` | `VARCHAR2(9)` |  | Completion status of the operation:  - `INACTIVE` - `PENDING` - `COMPLETE` - `CANCELLED` - `ERROR` |
| `CON_DBID` | `NUMBER` |  | The database ID of the PDB for the sampled session |
| `CON_ID` | `NUMBER` |  | The ID of the container that `CON_DBID` identifies. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

" [V$MEMORY\_RESIZE\_OPS](V-MEMORY_RESIZE_OPS.md) "