---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_RECOVERABLE_SCRIPT.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.265 DBA\_RECOVERABLE\_SCRIPT

`DBA_RECOVERABLE_SCRIPT` provides details about recoverable operations.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SCRIPT_ID` | `RAW(16)` |  | Unique ID of the operation |
| `CREATION_TIME` | `DATE` |  | Time the operation was invoked |
| `INVOKING_PACKAGE_OWNER` | `VARCHAR2(128)` |  | Invoking package owner of the operation |
| `INVOKING_PACKAGE` | `VARCHAR2(128)` |  | Invoking package of the operation |
| `INVOKING_PROCEDURE` | `VARCHAR2(128)` |  | Invoking procedure of the operation |
| `INVOKING_USER` | `VARCHAR2(128)` |  | Script owner |
| `STATUS` | `VARCHAR2(12)` |  | State of the recoverable script: GENERATING, NOT EXECUTED, EXECUTING, EXECUTED, or ERROR |
| `TOTAL_BLOCKS` | `NUMBER` |  | Total number of blocks for the recoverable script to be executed |
| `DONE_BLOCK_NUM` | `NUMBER` |  | Last block executed, thus far |
| `SCRIPT_COMMENT` | `VARCHAR2(4000)` |  | Comment for the recoverable script |