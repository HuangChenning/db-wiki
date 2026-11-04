---
title: DBA_HIST_MEMORY_RESIZE_OPS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4009.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_HIST_MEMORY_RESIZE_OPS` displays memory resize operations history. This view contains snapshots of `V$MEMORY_RESIZE_OPS`.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` | `NOT NULL` | Unique snapshot ID |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID for the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` | `NOT NULL` | Instance number for the snapshot |
| `COMPONENT` | `VARCHAR2(64)` | `NOT NULL` | Component name |
| `OPER_TYPE` | `VARCHAR2(13)` | `NOT NULL` | Operation type: |
| `START_TIME` | `DATE` | `NOT NULL` | Start time of the operation |
| `END_TIME` | `DATE` | `NOT NULL` | End time of the operation |
| `TARGET_SIZE` | `NUMBER` | `NOT NULL` | Requested value of the parameter after the resize |
| `OPER_MODE` | `VARCHAR2(9)` |  | Operation mode: |
| `PARAMETER` | `VARCHAR2(80)` |  | Name of the parameter for the resize operation |
| `INITIAL_SIZE` | `NUMBER` |  | Parameter value at the start of the operation |
| `FINAL_SIZE` | `NUMBER` |  | Real value of the parameter after the resize |
| `STATUS` | `VARCHAR2(9)` |  | Completion status of the operation: |