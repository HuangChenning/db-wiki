---
title: "V$MEMORY_RESIZE_OPS"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2061.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$MEMORY_RESIZE_OPS` displays information about the last 800 completed memory resize operations (both automatic and manual). This does not include in-progress operations. All sizes are expressed in bytes.

| Column | Datatype | Description |
| --- | --- | --- |
| `COMPONENT` | `VARCHAR2(64)` | Component name |
| `OPER_TYPE` | `VARCHAR2(13)` | Operation type: |
| `OPER_MODE` | `VARCHAR2(9)` | Operation mode: |
| `PARAMETER` | `VARCHAR2(80)` | Name of the parameter for the resize operation |
| `INITIAL_SIZE` | `NUMBER` | Parameter value at the start of the operation |
| `TARGET_SIZE` | `NUMBER` | Requested value of the parameter after the resize |
| `FINAL_SIZE` | `NUMBER` | Real value of the parameter after the resize |
| `STATUS` | `VARCHAR2(9)` | Completion status of the operation: |
| `START_TIME` | `DATE` | Start time of the operation |
| `END_TIME` | `DATE` | End time of the operation |