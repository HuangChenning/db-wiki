---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-INMEMORY_AREA.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.6 V$INMEMORY\_AREA

`V$INMEMORY_AREA` contains information on the space allocation inside the In-Memory area.

The In-Memory area is sub-divided into two pools: a 1MB pool used to store the actual column formatted data populated into memory, and a 64K pool used to store metadata about the objects that are populated into the In-Memory Column Store (IM column store). The amount of available memory in each pool is visible in the `V$INMEMORY_AREA` view. The relative size of the two pools is determined by internal heuristics. The majority of the In-Memory area memory is allocated to the 1MB pool.

| Column | Datatype | Description |
| --- | --- | --- |
| `POOL` | `VARCHAR2(26)` | Name of the pools in the In-Memory area |
| `ALLOC_BYTES` | `NUMBER` | Total amount of memory allocated to this pool |
| `USED_BYTES` | `NUMBER` | Amount of memory currently used in this pool |
| `POPULATE_STATUS` | `VARCHAR2(26)` | Shows the status of the IM column store, for example, whether it is currently being populated or if it is done |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire multitenant container database (CDB). This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |