---
title: "V$INSTANCE_CACHE_TRANSFER"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2003.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$INSTANCE_CACHE_TRANSFER` displays statistics for the cache blocks transferred among instances.

Oracle keeps multiple versions of data buffered in the buffer cache. The current buffer (or block), `CURRENT_BLOCK`, is the most up-to-date copy, containing all recent modifications. A consistent read buffer (or block), `CR_BLOCK`, contains the version of the data at a particular time prior to the current buffer. It is read-consistent (that is, all the data shown in that buffer are consistent for the start time of a query).

Therefore, for the same data block there can be multiple copies in the buffer cache: one current copy, and one or more consistent read copies with data consistent as of different snapshot times.

| Column | Datatype | Description |
| --- | --- | --- |
| `INSTANCE` | `NUMBER` | Instance from which the blocks are transferred |
| `CLASS` | `VARCHAR2(18)` | Class of the cache block |
| `LOST` | `NUMBER` | The number of blocks that were sent by a particular instance but that never arrived in this instance |
| `LOST_TIME` | `NUMBER` | The time waited for blocks that were sent by a particular instance but that never arrived in this instance |
| `CR_BLOCK` | `NUMBER` | CR Block transfers not affected by remote processing delays |
| `CR_BLOCK_TIME` | `NUMBER` | Total time waited for CR blocks from a particular instance (includes the other times) |
| `CR_2HOP` | `NUMBER` | The count of CR blocks which were received by this instance from a particular instance after a 2-way round-trip |
| `CR_2HOP_TIME` | `NUMBER` | The time waited for CR blocks which were received by this instance from a particular instance after a 2-way round-trip |
| `CR_3HOP` | `NUMBER` | The count of CR blocks which were received by this instance from a particular instance after a 3-way round-trip |
| `CR_3HOP_TIME` | `NUMBER` | The time waited for CR blocks which were received by this instance from a particular instance after a 3-way round-trip |
| `CR_BUSY` | `NUMBER` | CR Block transfers affected by remote contention |
| `CR_BUSY_TIME` | `NUMBER` | The time waited for CR blocks which were received by this instance from a particular instance and which were delayed by a log flushed on the sending instance |
| `CR_CONGESTED` | `NUMBER` | CR Block transfers affected by remote system load |
| `CR_CONGESTED_TIME` | `NUMBER` | The time waited for CR blocks which were received by this instance from a particular instance and which were delayed because LMS was busy |
| `CURRENT_BLOCK` | `NUMBER` | Current block transfers not affected by remote processing delays |
| `CURRENT_BLOCK_TIME` | `NUMBER` | Total time waited for current blocks from a particular instance (includes the other times |
| `CURRENT_2HOP` | `NUMBER` | The count of current blocks which were received by this instance from a particular instance after a 2-way roundtrip |
| `CURRENT_2HOP_TIME` | `NUMBER` | The time waited for current blocks which were received by this instance from a particular instance after a 2-way roundtrip |
| `CURRENT_3HOP` | `NUMBER` | The count of current blocks which were received by this instance from a particular instance after a 3-way roundtrip |
| `CURRENT_3HOP_TIME` | `NUMBER` | The time waited for current blocks which were received by this instance from a particular instance after a 3-way roundtrip |
| `CURRENT_BUSY` | `NUMBER` | Current block transfers affected by remote contention |
| `CURRENT_BUSY_TIME` | `NUMBER` | The time waited for current blocks which were received by this instance from a particular instance and which were delayed by a log flushed on the sending instance |
| `CURRENT_CONGESTED` | `NUMBER` | Current block transfers affected by remote system load |
| `CURRENT_CONGESTED_TIME` | `NUMBER` | The time waited for current blocks which were received by this instance from a particular instance and which were delayed because LMS was busy |