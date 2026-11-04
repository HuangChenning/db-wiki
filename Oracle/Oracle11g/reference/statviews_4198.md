---
title: DBA_RECOVERABLE_SCRIPT_ERRORS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4198.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_RECOVERABLE_SCRIPT_ERRORS` provides details about errors that occurred during script execution.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SCRIPT_ID` | `RAW(16)` |  | Global unique ID of the recoverable script |
| `BLOCK_NUM` | `NUMBER` |  | The `n` th block that failed |
| `ERROR_NUMBER` | `NUMBER` |  | Number of the error encountered while executing the block |
| `ERROR_MESSAGE` | `VARCHAR2(4000)` |  | Error message encountered while executing the block |
| `ERROR_CREATION_TIME` | `DATE` |  | Time that the error was created |