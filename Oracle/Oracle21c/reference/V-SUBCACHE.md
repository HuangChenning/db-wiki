---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-SUBCACHE.html
tags:
  - oracle
  - 21c
  - reference
---

## 10.90 V$SUBCACHE

The view walks through the library cache, printing out a row for each loaded subordinate cache per library cache object.

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
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |