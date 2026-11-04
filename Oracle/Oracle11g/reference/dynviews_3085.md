---
title: "V$SUBCACHE"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_3085.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$SUBCACHE` displays information about the subordinate caches currently loaded into library cache memory. The view walks through the library cache, printing out a row for each loaded subordinate cache per library cache object.

| Column | Datatype | Description |
| --- | --- | --- |
| `OWNER_NAME` | `VARCHAR2(64)` | Owner of the object containing these cache entries |
| `NAME` | `VARCHAR2(1000)` | Object Name |
| `TYPE` | `NUMBER` | Object Type |
| `HEAP_NUM` | `NUMBER` | Heap number containing this subordinate cache |
| `CACHE_ID` | `NUMBER` | Subordinate cache ID |
| `CACHE_CNT` | `NUMBER` | Number of entries for this cache in this object |
| `HEAP_SZ` | `NUMBER` | Amount of extent space allocated to this heap |
| `HEAP_ALOC` | `NUMBER` | Amount of extent space allocated from this heap |
| `HEAP_USED` | `NUMBER` | Amount of space utilized in this heap |