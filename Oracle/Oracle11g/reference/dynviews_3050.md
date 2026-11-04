---
title: "V$SQL_CURSOR"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_3050.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$SQL_CURSOR` displays debugging information for each cursor associated with the session querying this view.

| Column | Datatype | Description |
| --- | --- | --- |
| `CURNO` | `NUMBER` | Cursor number |
| `FLAG` | `NUMBER` | Flags set in the cursor |
| `STATUS` | `VARCHAR2(9)` | Status of the cursor; that is, what state the cursor is in |
| `PARENT_HANDLE` | `RAW(4 \| 8)` | Pointer to the parent cursor handle |
| `PARENT_LOCK` | `RAW(4 \| 8)` | Pointer to the parent cursor lock |
| `CHILD_LOCK` | `RAW(4 \| 8)` | Pointer to the child cursor lock |
| `CHILD_PIN` | `RAW(4 \| 8)` | Pointer to the child cursor pin |
| `PERS_HEAP_MEM` | `NUMBER` | Total amount of memory allocated from persistent heap for this cursor |
| `WORK_HEAP_MEM` | `NUMBER` | Total amount of memory allocated from the work heap for this cursor |
| `BIND_VARS` | `NUMBER` | Total number of bind positions in the query currently parsed into this cursor |
| `DEFINE_VARS` | `NUMBER` | Total number of define variables in the query currently parsed into this cursor |
| `BIND_MEM_LOC` | `VARCHAR2(64)` | Which memory heap the bind variables are stored in: either the UGA or the CGA |
| `INST_FLAG` | `VARCHAR2(64)` | Instantiation object flags |
| `INST_FLAG2` | `VARCHAR2(64)` | Instantiation object flags (continued) |