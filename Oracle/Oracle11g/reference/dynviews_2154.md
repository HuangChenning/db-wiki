---
title: "V$ROWCACHE_PARENT"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2154.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$ROWCACHE_PARENT` displays information for parent objects in the data dictionary. There is one row per lock owner, and one waiter for each object. This row shows the mode held or requested. For objects with no owners or waiters, a single row is displayed.

| Column | Datatype | Description |
| --- | --- | --- |
| `INDX` | `NUMBER` | Index of the row |
| `HASH` | `NUMBER` | Hash value |
| `ADDRESS` | `RAW(4 \| 8)` | Address of the parent object |
| `CACHE#` | `NUMBER` | Parent cache ID |
| `CACHE_NAME` | `VARCHAR2(64)` | Parent cache name |
| `EXISTENT` | `VARCHAR2(1)` | Indicates whether the object is an existing object |
| `LOCK_MODE` | `NUMBER` | Mode the lock is held in |
| `LOCK_REQUEST` | `NUMBER` | Mode the lock is requested in |
| `TXN` | `RAW(4)` | Transaction currently locking the object |
| `SADDR` | `RAW(4 \| 8)` | Address of the session |
| `INST_LOCK_REQUEST` | `NUMBER` | Mode in which instance lock is being requested. This column is only relevant for Real Application Clusters. |
| `INST_LOCK_RELEASE` | `NUMBER` | Whether the instance lock needs to be released. This column is only relevant for Real Application Clusters. |
| `INST_LOCK_TYPE` | `VARCHAR2(2)` | Type of instance lock. This column is only relevant for Real Application Clusters. |
| `INST_LOCK_ID1` | `RAW(4)` | ID associated with the instance lock. This column is only relevant for Real Application Clusters. |
| `INST_LOCK_ID2` | `RAW(4)` | ID associated with the instance lock. This column is only relevant for Real Application Clusters. |
| `KEY` | `RAW(100)` | Contents of the key. This column is only relevant for Real Application Clusters. |