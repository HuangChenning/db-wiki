---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-SQL_CURSOR.html
tags:
  - oracle
  - 21c
  - reference
---

## 10.53 V$SQL\_CURSOR

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
| `CHILD_HANDLE` | `RAW(4 \| 8)` | Pointer to the child cursor handle |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |