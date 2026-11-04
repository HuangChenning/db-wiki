---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-MEMORY_CURRENT_RESIZE_OPS.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.76 V$MEMORY\_CURRENT\_RESIZE\_OPS

`V$MEMORY_CURRENT_RESIZE_OPS` displays information about memory resize operations (both automatic and manual) which are currently in progress.

An operation can be a grow or a shrink of a dynamic memory component. All sizes are expressed in bytes.

| Column | Datatype | Description |
| --- | --- | --- |
| `COMPONENT` | `VARCHAR2(64)` | Component name |
| `OPER_TYPE` | `VARCHAR2(13)` | Operation type:  - `STATIC` - `INITIALIZING` - `DISABLED` - `GROW` - `SHRINK` - `SHRINK_CANCEL` |
| `OPER_MODE` | `VARCHAR2(9)` | Operation mode:  - `MANUAL` - `DEFERRED` - `IMMEDIATE` |
| `PARAMETER` | `VARCHAR2(80)` | Name of the parameter for the resize operation |
| `INITIAL_SIZE` | `NUMBER` | Parameter value at the start of the operation |
| `TARGET_SIZE` | `NUMBER` | Desired value of the parameter after the resize |
| `CURRENT_SIZE` | `NUMBER` | Current value of the parameter |
| `START_TIME` | `DATE` | Start time of the operation |
| `LAST_UPDATE_TIME` | `DATE` | Last time progress was made for the operation |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |