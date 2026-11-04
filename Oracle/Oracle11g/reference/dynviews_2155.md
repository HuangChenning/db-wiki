---
title: "V$ROWCACHE_SUBORDINATE"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2155.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$ROWCACHE_SUBORDINATE` displays information for subordinate objects in the data dictionary.

| Column | Datatype | Description |
| --- | --- | --- |
| `INDX` | `NUMBER` | The index |
| `HASH` | `NUMBER` | The hash value |
| `ADDRESS` | `RAW(4 \| 8)` | Address of the subordinate object |
| `CACHE#` | `NUMBER` | The parent cache ID |
| `SUBCACHE#` | `NUMBER` | The subcache ID |
| `SUBCACHE_NAME` | `VARCHAR2(64)` | The subcache name |
| `EXISTENT` | `VARCHAR2(1)` | Whether the object is an existing object |
| `PARENT` | `RAW(4 \| 8)` | Address of the parent object |
| `KEY` | `RAW(100)` | The contents of the key |