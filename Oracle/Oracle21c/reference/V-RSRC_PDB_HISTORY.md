---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-RSRC_PDB_HISTORY.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.193 V$RSRC\_PDB\_HISTORY

`V$RSRC_PDB_HISTORY` displays a history of consumer group statistics for each entry in `V$RSRC_PDB` that has a non-NULL plan by pluggable database (PDB).

When the `STATISTICS_LEVEL` is set to `TYPICAL` or `ALL`, this view contains information about CPU utilization and wait times even when no Resource Manager plan is set or when the Resource Manager plan does not monitor CPU or session resources.

A new window is created in `V$RSRC_PDB_HISTORY` when a multitenant container database (CDB) changes its resource plan. The plan windows for the CDB are not impacted by a PDB resource plan change.

`V$RSRC_PDB_HISTORY` covers the same time period for all PDBs. This view is specifically designed for comparing statistics across different PDBs.

Since `V$RSRC_PDB_HISTORY` does not contain information at the consumer group level, it is not useful for comparing consumer groups inside a PDB.

| Column | Datatype | Description |
| --- | --- | --- |
| `SEQUENCE#` | `NUMBER` | A sequential counter that uniquely describes the `V$RSRC_PDB` entry to which these consumer group statistics apply. When the instance is restarted, this value is reset to zero. |
| `PDB_NAME` | `VARCHAR2(32)` | PBD name |
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
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

" [V$RSRC\_CONS\_GROUP\_HISTORY](V-RSRC_CONS_GROUP_HISTORY.md) "