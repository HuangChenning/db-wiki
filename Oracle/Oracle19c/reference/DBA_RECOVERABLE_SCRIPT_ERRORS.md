---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/DBA_RECOVERABLE_SCRIPT_ERRORS.html
tags:
  - oracle
  - 19c
  - reference
---

## 5.265 DBA\_RECOVERABLE\_SCRIPT\_ERRORS

`DBA_RECOVERABLE_SCRIPT_ERRORS` provides details about errors that occurred during script execution.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SCRIPT_ID` | `RAW(16)` |  | Global unique ID of the recoverable script |
| `BLOCK_NUM` | `NUMBER` |  | The `n` th block that failed |
| `ERROR_NUMBER` | `NUMBER` |  | Number of the error encountered while executing the block |
| `ERROR_MESSAGE` | `VARCHAR2(4000)` |  | Error message encountered while executing the block |
| `ERROR_CREATION_TIME` | `DATE` |  | Time that the error was created |