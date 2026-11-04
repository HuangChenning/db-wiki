---
title: DBA_RECOVERABLE_SCRIPT_BLOCKS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4197.htm
tags:
  - oracle
  - 11g
  - reference
---

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