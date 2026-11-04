---
title: DBA_RECOVERABLE_SCRIPT
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4196.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_RECOVERABLE_SCRIPT` provides details about recoverable operations.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SCRIPT_ID` | `RAW(16)` |  | Unique ID of the operation |
| `CREATION_TIME` | `DATE` |  | Time the operation was invoked |
| `INVOKING_PACKAGE_OWNER` | `VARCHAR2(30)` |  | Invoking package owner of the operation |
| `INVOKING_PACKAGE` | `VARCHAR2(30)` |  | Invoking package of the operation |
| `INVOKING_PROCEDURE` | `VARCHAR2(30)` |  | Invoking procedure of the operation |
| `INVOKING_USER` | `VARCHAR2(30)` |  | Script owner |
| `STATUS` | `VARCHAR2(12)` |  | State of the recoverable script: GENERATING, NOT EXECUTED, EXECUTING, EXECUTED, or ERROR |
| `TOTAL_BLOCKS` | `NUMBER` |  | Total number of blocks for the recoverable script to be executed |
| `DONE_BLOCK_NUM` | `NUMBER` |  | Last block executed, thus far |
| `SCRIPT_COMMENT` | `VARCHAR2(4000)` |  | Comment for the recoverable script |