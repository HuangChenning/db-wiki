---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_HIST_INST_CACHE_TRANSFER.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.410 DBA\_HIST\_INST\_CACHE\_TRANSFER

`DBA_HIST_INST_CACHE_TRANSFER` displays the historical statistics on the cache blocks transferred among instances.

This view contains snapshots of `V$INSTANCE_CACHE_TRANSFER`.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` | `NOT NULL` | Unique snapshot ID |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID for the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` | `NOT NULL` | Instance number for the snapshot |
| `INSTANCE` | `NUMBER` | `NOT NULL` | Instance from which the blocks are transferred |
| `CLASS` | `VARCHAR2(18)` | `NOT NULL` | Class of the cache block |
| `CR_BLOCK` | `NUMBER` |  | CR block transfers not affected by remote processing delays |
| `CR_BUSY` | `NUMBER` |  | Current block transfers affected by remote contention |
| `CR_CONGESTED` | `NUMBER` |  | CR block transfers affected by remote system load |
| `CURRENT_BLOCK` | `NUMBER` |  | Current block transfers not affected by remote processing delays |
| `CURRENT_BUSY` | `NUMBER` |  | Current block transfers affected by remote contention |
| `CURRENT_CONGESTED` | `NUMBER` |  | Current block transfers affected by remote system load |
| `LOST` | `NUMBER` |  | The number of blocks that were sent by a particular instance but that never arrived in this instance |
| `CR_2HOP` | `NUMBER` |  | The count of CR blocks which were received by this instance from a particular instance after a 2-way round-trip |
| `CR_3HOP` | `NUMBER` |  | The count of CR blocks which were received by this instance from a particular instance after a 3-way round-trip |
| `CR_RDMA` <sup>Foot 1</sup> | `NUMBER` |  | The count of CR Blocks which were directly read from a remote instance via RDMA |
| `CURRENT_2HOP` | `NUMBER` |  | The count of current blocks which were received by this instance from a particular instance after a 2-way round-trip |
| `CURRENT_3HOP` | `NUMBER` |  | The count of current blocks which were received by this instance from a particular instance after a 3-way round-trip |
| `CURRENT_RDMA` <sup>Foot 1</sup> | `NUMBER` |  | The count of current blocks which were directly read from a remote instance via RDMA |
| `CR_BLOCK_TIME` | `NUMBER` |  | Total time waited for CR blocks from a particular instance (includes the other times) |
| `CR_BUSY_TIME` | `NUMBER` |  | The time waited for CR blocks which were received by this instance from a particular instance and which were delayed by a log flushed on the sending instance |
| `CR_CONGESTED_TIME` | `NUMBER` |  | The time waited for CR blocks which were received by this instance from a particular instance and which were delayed because LMS was busy |
| `CURRENT_BLOCK_TIME` | `NUMBER` |  | Total time waited for CR blocks from a particular instance (includes the other times) |
| `CURRENT_BUSY_TIME` | `NUMBER` |  | The time waited for current blocks which were received by this instance from a particular instance and which were delayed by a log flushed on the sending instance |
| `CURRENT_CONGESTED_TIME` | `NUMBER` |  | The time waited for current blocks which were received by this instance from a particular instance and which were delayed because LMS was busy |
| `LOST_TIME` | `NUMBER` |  | The time waited for blocks that were sent by a particular instance but that never arrived in this instance |
| `CR_2HOP_TIME` | `NUMBER` |  | The time waited for CR blocks which were received by this instance from a particular instance after a 2-way round-trip |
| `CR_3HOP_TIME` | `NUMBER` |  | The time waited for CR blocks which were received by this instance from a particular instance after a 3-way round-trip |
| `CR_RDMA_TIME` <sup>Foot 1</sup> | `NUMBER` |  | Total time waited to directly read CR blocks from a remote instance via RDMA (in centiseconds) |
| `CURRENT_2HOP_TIME` | `NUMBER` |  | The time waited for current blocks which were received by this instance from a particular instance after a 2-way round-trip |
| `CURRENT_3HOP_TIME` | `NUMBER` |  | The time waited for current blocks which were received by this instance from a particular instance after a 3-way round-trip |
| `CURRENT_RDMA_TIME` <sup>Foot 1</sup> | `NUMBER` |  | Total time waited to directly read current blocks from a remote instance via RDMA (in centiseconds) |
| `CON_DBID` | `NUMBER` |  | The database ID of the PDB for the sampled session |
| `CON_ID` | `NUMBER` |  | The ID of the container that `CON_DBID` identifies. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

<sup>Footnote 1</sup> This column is available starting with Oracle Database 21c.

See Also:

" [V$INSTANCE\_CACHE\_TRANSFER](V-INSTANCE_CACHE_TRANSFER.md) "