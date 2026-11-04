---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/V-ROWCACHE_SUBORDINATE.html
tags:
  - oracle
  - 12c
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
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |