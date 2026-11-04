---
title: "V$MEMORY_CURRENT_RESIZE_OPS"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2059.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$MEMORY_CURRENT_RESIZE_OPS` displays information about memory resize operations (both automatic and manual) which are currently in progress. An operation can be a grow or a shrink of a dynamic memory component. All sizes are expressed in bytes.

| Column | Datatype | Description |
| --- | --- | --- |
| `COMPONENT` | `VARCHAR2(64)` | Component name |
| `OPER_TYPE` | `VARCHAR2(13)` | Operation type: |
| `OPER_MODE` | `VARCHAR2(9)` | Operation mode: |
| `PARAMETER` | `VARCHAR2(80)` | Name of the parameter for the resize operation |
| `INITIAL_SIZE` | `NUMBER` | Parameter value at the start of the operation |
| `TARGET_SIZE` | `NUMBER` | Desired value of the parameter after the resize |
| `CURRENT_SIZE` | `NUMBER` | Current value of the parameter |
| `START_TIME` | `DATE` | Start time of the operation |
| `LAST_UPDATE_TIME` | `DATE` | Last time progress was made for the operation |