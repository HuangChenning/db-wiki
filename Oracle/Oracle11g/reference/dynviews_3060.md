---
title: "V$SQL_SHARED_MEMORY"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_3060.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$SQL_SHARED_MEMORY` displays information about the cursor shared memory snapshot. Each SQL statement stored in the shared pool has one or more child objects associated with it. Each child object has a number of parts, one of which is the context heap, which holds, among other things, the query plan.

| Column | Datatype | Description |
| --- | --- | --- |
| `SQL_TEXT` | `VARCHAR2(1000)` | SQL text of the shared cursor child object for which this row is displaying information |
| `SQL_FULLTEXT` | `CLOB` | Full text for the SQL statement exposed as a `CLOB` column. The full text of a SQL statement can be retrieved using this column instead of joining with the `V$SQLTEXT` dynamic performance view. |
| `HASH_VALUE` | `NUMBER` | Hash value of the above SQL text in the shared pool |
| `SQL_ID` | `VARCHAR2(13)` | SQL identifier of the above SQL text in the shared pool |
| `HEAP_DESC` | `RAW(4 \| 8)` | Address of the descriptor for the context heap of the child cursor described in this row |
| `STRUCTURE` | `VARCHAR2(16)` | If the memory chunk described in this row was allocated using a comment of the form "X: Y", then this is the "X" part of the comment |
| `FUNCTION` | `VARCHAR2(16)` | Similar to the `STRUCTURE` column, this is the "Y" field of the comment |
| `CHUNK_COM` | `VARCHAR2(16)` | Whole comment field that was supplied when this memory chunk was allocated |
| `CHUNK_PTR` | `RAW(4 \| 8)` | Starting address of the allocated memory chunk |
| `CHUNK_SIZE` | `NUMBER` | Amount of memory allocated for this chunk |
| `ALLOC_CLASS` | `VARCHAR2(8)` | Class of memory that this chunk of memory belongs to. It will usually be either `FREEABLE` or `PERMANENT`. |
| `CHUNK_TYPE` | `NUMBER` | An index into a table of callback functions that tell the server how to re-create this chunk of memory should it need to be removed from the shared pool based on an LRU algorithm |
| `SUBHEAP_DESC` | `RAW(4 \| 8)` | If the parent heap of this context heap is itself a subheap, then this is the address of the descriptor of the parent heap |