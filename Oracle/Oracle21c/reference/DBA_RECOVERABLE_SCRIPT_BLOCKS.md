---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_RECOVERABLE_SCRIPT_BLOCKS.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.266 DBA\_RECOVERABLE\_SCRIPT\_BLOCKS

`DBA_RECOVERABLE_SCRIPT_BLOCKS` provides details about recoverable script blocks.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SCRIPT_ID` | `RAW(16)` |  | Global unique ID of the recoverable script to which this block belongs |
| `BLOCK_NUM` | `NUMBER` |  | The `n` th block in the recoverable script to be executed |
| `FORWARD_BLOCK` | `CLOB` |  | Forward block to be executed |
| `FORWARD_BLOCK_DBLINK` | `VARCHAR2(128)` |  | Database where the forward block is executed |
| `UNDO_BLOCK` | `CLOB` |  | Block to roll back the forward operation |
| `UNDO_BLOCK_DBLINK` | `VARCHAR2(128)` |  | Database where the undo block is executed |
| `STATUS` | `VARCHAR2(12)` |  | Status of the block execution: GENERATING, NOT EXECUTED, EXECUTING, EXECUTED, or ERROR |
| `BLOCK_COMMENT` | `VARCHAR2(4000)` |  | Comment for the block |