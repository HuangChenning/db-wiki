---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-GES_RESOURCE.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.259 V$GES\_RESOURCE

`V$GES_RESOURCE` is an Oracle Real Application Clusters view. It displays information of all resources currently known to the lock manager.

| Column | Datatype | Description |
| --- | --- | --- |
| `RESP` | `RAW(4 \| 8)` | Resource pointer |
| `RESOURCE_NAME` | `VARCHAR2(30)` | Resource name in hexadecimal for the lock |
| `ON_CONVERT_Q` | `NUMBER` | `1` if on convert queue, `0` otherwise |
| `ON_GRANT_Q` | `NUMBER` | `1` if on granted queue, `0` otherwise |
| `PERSISTENT_RES` | `NUMBER` | `1` if it is a persistent resource, `0` otherwise |
| `MASTER_NODE` | `NUMBER` | Primary node ID |
| `NEXT_CVT_LEVEL` | `VARCHAR2(9)` | Next lock level to convert on global convert queue |
| `VALUE_BLK_STATE` | `VARCHAR2(32)` | State of the value block |
| `VALUE_BLK` | `VARCHAR2(64)` | First 64 bytes of the value block |
| `CACHE_LEVEL` | `NUMBER` | Level at which the resource is cached (`0`, `1`, or `2`; `255` if not on cache) |
| `PDBSCOPE` | `NUMBER` | Indicates whether an enqueue is PDB-scoped (`1`) or not (`0`) |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |