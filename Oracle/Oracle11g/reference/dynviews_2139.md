---
title: "V$RESULT_CACHE_MEMORY"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2139.htm
tags:
  - oracle
  - 11g
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