---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-RSRC_PDB.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.192 V$RSRC\_PDB

`V$RSRC_PDB` displays data related to currently active resource consumer groups by pluggable database (PDB).

When the `STATISTICS_LEVEL` is set to `TYPICAL` or `ALL`, this view contains information about CPU utilization and wait times even when no Resource Manager plan is set or when the Resource Manager plan does not monitor CPU or session resources.

Statistics in `V$RSRC_PDB` are reset when a multitenant container database (CDB) changes its resource plan. They are not impacted by PDB resource plan changes.

`V$RSRC_PDB` covers the same time period for all PDBs. This view is specifically designed for comparing statistics across different PDBs.

Since `V$RSRC_PDB` does not contain information at the consumer group level, it is not useful for comparing consumer groups inside a PDB.

| Column | Datatype | Description |
| --- | --- | --- |
| `PDB_NAME` | `VARCHAR2(32)` | PDB name |
| `CPU_WAIT_TIME` | `NUMBER` | Cumulative amount of time that sessions waited for CPU because of resource management. This does not include waits due to latch or enqueue contention, I/O waits, and so on. When CPU resources are not being actively managed, this value is set to zero. |
| `CPU_WAITS` | `NUMBER` | Cumulative number of times all sessions in the consumer group had to wait for CPU because of resource management. This does not include waits due to latch or enqueue contention, I/O waits, and so on. When CPU resources are not being actively managed, this value is set to zero. |
| `CONSUMED_CPU_TIME` | `NUMBER` | Cumulative amount of CPU time consumed by all sessions in the consumer group (in milliseconds) |
| `YIELDS` | `NUMBER` | Cumulative number of times that sessions in the consumer group had to yield CPU to other sessions because of quantum expiration. When CPU resources are not being actively managed, this value is set to zero. |
| `IO_SERVICE_TIME` | `NUMBER` | Cumulative I/O wait time (in milliseconds) |
| `IO_SERVICE_WAITS` | `NUMBER` | Total number of wait requests |
| `SMALL_READ_MEGABYTES` | `NUMBER` | Number of single block megabytes read |
| `SMALL_WRITE_MEGABYTES` | `NUMBER` | Number of single block megabytes written |
| `LARGE_READ_MEGABYTES` | `NUMBER` | Number of multiblock megabytes read |
| `LARGE_WRITE_MEGABYTES` | `NUMBER` | Number of multiblock megabytes written |
| `SMALL_READ_REQUESTS` | `NUMBER` | Number of single block read requests |
| `SMALL_WRITE_REQUESTS` | `NUMBER` | Number of single block write requests |
| `LARGE_READ_REQUESTS` | `NUMBER` | Number of multiblock read requests |
| `LARGE_WRITE_REQUESTS` | `NUMBER` | Number of multiblock write requests |
| `PQS_COMPLETED` | `NUMBER` | Total number of completed parallel statements in the consumer group |
| `PQ_SERVERS_USED` | `NUMBER` | Total number of parallel servers used by completed parallel statements in the consumer group |
| `PQS_QUEUED` | `NUMBER` | Number of times that sessions in the consumer group were queued when trying to run parallel statements |
| `PQ_ACTIVE_TIME` | `NUMBER` | Cumulative sum of the parallel active times for all completed parallel statements in the consumer group (in milliseconds) |
| `PQ_QUEUED_TIME` | `NUMBER` | Total amount of time that sessions in the consumer group were queued when trying to run parallel statements (in milliseconds) |
| `PQ_QUEUE_TIME_OUTS` | `NUMBER` | Number of times that parallel statements from sessions in the consumer group timed out because their queue time exceeded the Resource Manager plan's `PARALLEL_QUEUE_TIMEOUT` limit |
| `CURRENT_PQS_ACTIVE` | `NUMBER` | Number of active parallel statements in the consumer group. This value does not include parallel statements that are never queued, such as GV$ queries. |
| `CURRENT_PQ_SERVERS_ACTIVE` | `NUMBER` | Number of active parallel servers in the consumer group. This value does not include servers running parallel statements that are never queued, such as GV$ queries. |
| `CURRENT_PQS_QUEUED` | `NUMBER` | Number of sessions in the consumer group that are waiting in the parallel statement queue trying to run parallel statements |
| `SGA_BYTES` | `NUMBER` | The current SGA usage by this PDB in bytes |
| `BUFFER_CACHE_BYTES` | `NUMBER` | The current usage of buffer cache by this PDB in bytes |
| `SHARED_POOL_BYTES` | `NUMBER` | The current usage of shared pool by this PDB in bytes |
| `PGA_BYTES` | `NUMBER` | The current usage of PGA by this PDB in bytes |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

" [V$RSRC\_CONSUMER\_GROUP](V-RSRC_CONSUMER_GROUP.md) "