---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-SGA_RESIZE_OPS.html
tags:
  - oracle
  - 21c
  - reference
---

## 10.35 V$SGA\_RESIZE\_OPS

This does not include in-progress operations. All sizes are expressed in bytes.

| Column | Datatype | Description |
| --- | --- | --- |
| `COMPONENT` | `VARCHAR2(64)` | Component name |
| `OPER_TYPE` | `VARCHAR2(13)` | Operation type:  - `STATIC` - `INITIALIZING` - `DISABLED` - `GROW` - `SHRINK` - `SHRINK_CANCEL` |
| `OPER_MODE` | `VARCHAR2(9)` | Operation mode:  - `MANUAL` - `DEFERRED` - `IMMEDIATE` |
| `PARAMETER` | `VARCHAR2(80)` | Name of the parameter for the resize operation |
| `INITIAL_SIZE` | `NUMBER` | Parameter value at the start of the operation |
| `TARGET_SIZE` | `NUMBER` | Requested value of the parameter after the resize |
| `FINAL_SIZE` | `NUMBER` | Real value of the parameter after the resize |
| `STATUS` | `VARCHAR2(9)` | Completion status of the operation:  - `INACTIVE` - `PENDING` - `COMPLETE` - `CANCELLED` - `ERROR` |
| `START_TIME` | `DATE` | Start time of the operation |
| `END_TIME` | `DATE` | End time of the operation |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |