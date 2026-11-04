---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-INSTANCE_CACHE_TRANSFER.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.9 V$INSTANCE\_CACHE\_TRANSFER

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
| `CR_RDMA` <sup>Foot 1</sup> | `NUMBER` | The count of CR Blocks which were directly read from a remote instance via RDMA |
| `CR_RDMA_TIME`  <sup>Foot 1</sup> | `NUMBER` | Total time waited to directly read CR blocks from a remote instance via RDMA (in centiseconds) |
| `CR_BUSY` | `NUMBER` | CR Block transfers affected by remote contention |
| `CR_BUSY_TIME` | `NUMBER` | The time waited for CR blocks which were received by this instance from a particular instance and which were delayed by a log flushed on the sending instance |
| `CR_CONGESTED` | `NUMBER` | CR Block transfers affected by remote system load |
| `CR_CONGESTED_TIME` | `NUMBER` | The time waited for CR blocks which were received by this instance from a particular instance and which were delayed because LMS was busy |
| `CURRENT_BLOCK` | `NUMBER` | Current block transfers not affected by remote processing delays |
| `CURRENT_BLOCK_TIME` | `NUMBER` | Total time waited for current blocks from a particular instance (includes the other times |
| `CURRENT_2HOP` | `NUMBER` | The count of current blocks which were received by this instance from a particular instance after a 2-way round-trip |
| `CURRENT_2HOP_TIME` | `NUMBER` | The time waited for current blocks which were received by this instance from a particular instance after a 2-way round-trip |
| `CURRENT_3HOP` | `NUMBER` | The count of current blocks which were received by this instance from a particular instance after a 3-way round-trip |
| `CURRENT_3HOP_TIME` | `NUMBER` | The time waited for current blocks which were received by this instance from a particular instance after a 3-way round-trip |
| `CURRENT_RDMA` <sup>Foot 1</sup> | `NUMBER` | The count of current blocks which were directly read from a remote instance via RDMA |
| `CURRENT_RDMA_TIME` <sup>Foot 1</sup> | `NUMBER` | Total time waited to directly read current blocks from a remote instance via RDMA (in centiseconds) |
| `CURRENT_BUSY` | `NUMBER` | Current block transfers affected by remote contention |
| `CURRENT_BUSY_TIME` | `NUMBER` | The time waited for current blocks which were received by this instance from a particular instance and which were delayed by a log flushed on the sending instance |
| `CURRENT_CONGESTED` | `NUMBER` | Current block transfers affected by remote system load |
| `CURRENT_CONGESTED_TIME` | `NUMBER` | The time waited for current blocks which were received by this instance from a particular instance and which were delayed because LMS was busy |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

<sup>Footnote 1</sup> This column is available starting with Oracle Database 21c.