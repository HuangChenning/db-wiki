---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/V-RESULT_CACHE_MEMORY.html
tags:
  - oracle
  - 12c
  - reference
---

`V$RESULT_CACHE_MEMORY` displays all the memory blocks and their status.

| Column | Datatype | Description |
| --- | --- | --- |
| `ID` | `NUMBER` | Unique block identifier (that is, the block number) |
| `CHUNK` | `NUMBER` | Chunk to which the block belongs (the upper 27 bits of the ID) |
| `OFFSET` | `NUMBER` | Offset of the block within its chunk (the lower 5 bits of the ID) |
| `FREE` | `VARCHAR2(3)` | Indicates whether the block is free (`YES`) or not (`NO`) |
| `OBJECT_ID` | `NUMBER` | Cache object to which the memory block belongs; NULL if the memory block is not allocated to a cache object (`FREE` = `YES`) |
| `POSITION` | `NUMBER` | Position of the block in the cached object; NULL if the memory block is not allocated to a cache object (`FREE` = `YES`) |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |