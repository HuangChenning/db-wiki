---
title: DBA_HIST_INST_CACHE_TRANSFER
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_3228.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_HIST_INST_CACHE_TRANSFER` displays the historical statistics on the cache blocks transferred among instances. This view contains snapshots of `V$INSTANCE_CACHE_TRANSFER`.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` |  | Unique snapshot ID |
| `DBID` | `NUMBER` |  | Database ID for the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` |  | Instance number for the snapshot |
| `INSTANCE` | `NUMBER` |  | Instance from which the blocks are transferred |
| `CLASS` | `VARCHAR2(18)` |  | Class of the cache block |
| `CR_BLOCK` | `NUMBER` |  | CR block transfers not affected by remote processing delays |
| `CR_BUSY` | `NUMBER` |  | Current block transfers affected by remote contention |
| `CR_CONGESTED` | `NUMBER` |  | CR block transfers affected by remote system load |
| `CURRENT_BLOCK` | `NUMBER` |  | Current block transfers not affected by remote processing delays |
| `CURRENT_BUSY` | `NUMBER` |  | Current block transfers affected by remote contention |
| `CURRENT_CONGESTED` | `NUMBER` |  | Current block transfers affected by remote system load |
| `LOST` | `NUMBER` |  | The number of blocks that were sent by a particular instance but that never arrived in this instance |
| `CR_2HOP` | `NUMBER` |  | The count of CR blocks which were received by this instance from a particular instance after a 2-way round-trip |
| `CR_3HOP` | `NUMBER` |  | The count of CR blocks which were received by this instance from a particular instance after a 3-way round-trip |
| `CURRENT_2HOP` | `NUMBER` |  | The count of current blocks which were received by this instance from a particular instance after a 2-way roundtrip |
| `CURRENT_3HOP` | `NUMBER` |  | The count of current blocks which were received by this instance from a particular instance after a 3-way roundtrip |
| `CR_BLOCK_TIME` | `NUMBER` |  | Total time waited for CR blocks from a particular instance (includes the other times) |
| `CR_BUSY_TIME` | `NUMBER` |  | The time waited for CR blocks which were received by this instance from a particular instance and which were delayed by a log flushed on the sending instance |
| `CR_CONGESTED_TIME` | `NUMBER` |  | The time waited for CR blocks which were received by this instance from a particular instance and which were delayed because LMS was busy |
| `CURRENT_BLOCK_TIME` | `NUMBER` |  | Total time waited for CR blocks from a particular instance (includes the other times) |
| `CURRENT_BUSY_TIME` | `NUMBER` |  | The time waited for current blocks which were received by this instance from a particular instance and which were delayed by a log flushed on the sending instance |
| `CURRENT_CONGESTED_TIME` | `NUMBER` |  | The time waited for current blocks which were received by this instance from a particular instance and which were delayed because LMS was busy |
| `LOST_TIME` | `NUMBER` |  | The time waited for blocks that were sent by a particular instance but that never arrived in this instance |
| `CR_2HOP_TIME` | `NUMBER` |  | The time waited for CR blocks which were received by this instance from a particular instance after a 2-way round-trip |
| `CR_3HOP_TIME` | `NUMBER` |  | The time waited for CR blocks which were received by this instance from a particular instance after a 3-way round-trip |
| `CURRENT_2HOP_TIME` | `NUMBER` |  | The time waited for current blocks which were received by this instance from a particular instance after a 2-way roundtrip |
| `CURRENT_3HOP_TIME` | `NUMBER` |  | The time waited for current blocks which were received by this instance from a particular instance after a 3-way roundtrip |