---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-RESULT_CACHE_MEMORY.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.171 V$RESULT\_CACHE\_MEMORY

`V$RESULT_CACHE_MEMORY` displays all the memory blocks and their status.

| Column | Datatype | Description |
| --- | --- | --- |
| `ID` | `NUMBER` | Unique block identifier (that is, the block number) |
| `CHUNK` | `NUMBER` | Chunk to which the block belongs, relative to the subcache in which the memory object resides (the upper 27 bits of the ID) |
| `OFFSET` | `NUMBER` | Offset of the block within its chunk, relative to the subcache in which the memory object resides (the lower 5 bits of the ID) |
| `SUBCACHE_ID` <sup>Foot 1</sup> | `NUMBER` | Subcache ID |
| `FREE` | `VARCHAR2(3)` | Indicates whether the block is free (`YES`) or not (`NO`) |
| `OBJECT_ID` | `NUMBER` | Cache object to which the memory block belongs; NULL if the memory block is not allocated to a cache object (`FREE` = `YES`) |
| `POSITION` | `NUMBER` | Position of the block in the cached object; NULL if the memory block is not allocated to a cache object (`FREE` = `YES`) |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

<sup>Footnote 1</sup> This column is available starting with Oracle Database 21c.