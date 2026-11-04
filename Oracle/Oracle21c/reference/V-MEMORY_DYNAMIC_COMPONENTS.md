---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-MEMORY_DYNAMIC_COMPONENTS.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.77 V$MEMORY\_DYNAMIC\_COMPONENTS

`V$MEMORY_DYNAMIC_COMPONENTS` displays information about the dynamic SGA components.

This view summarizes information based on all completed SGA resize operations since instance startup. All sizes are expressed in bytes.

| Column | Datatype | Description |
| --- | --- | --- |
| `COMPONENT` | `VARCHAR2(64)` | Component name |
| `CURRENT_SIZE` | `NUMBER` | Current size of the component |
| `MIN_SIZE` | `NUMBER` | Minimum size of the component since instance startup |
| `MAX_SIZE` | `NUMBER` | Maximum size of the component since instance startup |
| `USER_SPECIFIED_SIZE` | `NUMBER` | Value of the user parameter for the component |
| `OPER_COUNT` | `NUMBER` | Number of operations since instance startup |
| `LAST_OPER_TYPE` | `VARCHAR2(13)` | Last completed operation for the component:  - `STATIC` - `INITIALIZING` - `DISABLED` - `GROW` - `SHRINK` - `SHRINK_CANCEL` |
| `LAST_OPER_MODE` | `VARCHAR2(9)` | Mode of the last completed operation:  - `MANUAL` - `DEFERRED` - `IMMEDIATE` |
| `LAST_OPER_TIME` | `DATE` | Start time of the last completed operation |
| `GRANULE_SIZE` | `NUMBER` | Granularity of the `GROW` or `SHRINK` operation |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |