---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_RECOVERABLE_SCRIPT_HIST.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.268 DBA\_RECOVERABLE\_SCRIPT\_HIST

`DBA_RECOVERABLE_SCRIPT_HIST` displays details about executed or purged recoverable operations.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SCRIPT_ID` | `RAW(16)` |  | Unique id of the operation |
| `CREATION_TIME` | `DATE` |  | Time the operation was invoked |
| `INVOKING_PACKAGE_OWNER` | `VARCHAR2(128)` |  | Invoking package owner of the operation |
| `INVOKING_PACKAGE` | `VARCHAR2(128)` |  | Invoking package of the operation |
| `INVOKING_PROCEDURE` | `VARCHAR2(128)` |  | Invoking procedure of the operation |
| `INVOKING_USER` | `VARCHAR2(128)` |  | Script owner |
| `STATUS` | `VARCHAR2(8)` |  | state of the recoverable script: EXECUTED, PURGED |
| `TOTAL_BLOCKS` | `NUMBER` |  | total number of blocks for the recoverable script to be executed |
| `DONE_BLOCK_NUM` | `NUMBER` |  | last block so far executed |
| `SCRIPT_COMMENT` | `VARCHAR2(4000)` |  | comment for the recoverable script |