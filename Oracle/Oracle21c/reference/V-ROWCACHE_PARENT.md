---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-ROWCACHE_PARENT.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.187 V$ROWCACHE\_PARENT

There is one row per lock owner, and one waiter for each object. This row shows the mode held or requested. For objects with no owners or waiters, a single row is displayed.

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
| `TXN` | `RAW(4 \| 8)` | Transaction currently locking the object |
| `SADDR` | `RAW(4 \| 8)` | Address of the session |
| `INST_LOCK_REQUEST` | `NUMBER` | Mode in which instance lock is being requested. This column is only relevant for Real Application Clusters. |
| `INST_LOCK_RELEASE` | `NUMBER` | Whether the instance lock needs to be released. This column is only relevant for Real Application Clusters. |
| `INST_LOCK_TYPE` | `VARCHAR2(2)` | Type of instance lock. This column is only relevant for Real Application Clusters. |
| `INST_LOCK_ID1` | `RAW(4)` | ID associated with the instance lock. This column is only relevant for Real Application Clusters. |
| `INST_LOCK_ID2` | `RAW(4)` | ID associated with the instance lock. This column is only relevant for Real Application Clusters. |
| `KEY` | `RAW(100)` | Contents of the key. This column is only relevant for Real Application Clusters. |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |