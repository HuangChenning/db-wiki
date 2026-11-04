---
title: DBA_RECOVERABLE_SCRIPT_HIST
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4199.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_RECOVERABLE_SCRIPT_HIST` displays details about executed or purged recoverable operations.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SCRIPT_ID` | `RAW(16)` |  | Unique id of the operation |
| `CREATION_TIME` | `DATE` |  | Time the operation was invoked |
| `INVOKING_PACKAGE_OWNER` | `VARCHAR2(30)` |  | Invoking package owner of the operation |
| `INVOKING_PACKAGE` | `VARCHAR2(30)` |  | Invoking package of the operation |
| `INVOKING_PROCEDURE` | `VARCHAR2(30)` |  | Invoking procedure of the operation |
| `INVOKING_USER` | `VARCHAR2(30)` |  | Script owner |
| `STATUS` | `VARCHAR2(8)` |  | state of the recoverable script: EXECUTED, PURGED |
| `TOTAL_BLOCKS` | `NUMBER` |  | total number of blocks for the recoverable script to be executed |
| `DONE_BLOCK_NUM` | `NUMBER` |  | last block so far executed |
| `SCRIPT_COMMENT` | `VARCHAR2(4000)` |  | comment for the recoverable script |