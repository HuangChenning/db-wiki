---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_HIST_BUFFER_POOL_STAT.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.380 DBA\_HIST\_BUFFER\_POOL\_STAT

`DBA_HIST_BUFFER_POOL_STAT` displays historical statistics about all buffer pools available for the instance.

This view contains snapshots of `V$BUFFER_POOL_STATISTICS`.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` | `NOT NULL` | Unique snapshot ID |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID for the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` | `NOT NULL` | Instance number for the snapshot |
| `ID` | `NUMBER` | `NOT NULL` | Buffer pool identifier number |
| `NAME` | `VARCHAR2(20)` |  | Name of the buffer pool |
| `BLOCK_SIZE` | `NUMBER` |  | Block Size |
| `SET_MSIZE` | `NUMBER` |  | Buffer pool maximum set size |
| `CNUM_REPL` | `NUMBER` |  | Number of buffers on the replacement list |
| `CNUM_WRITE` | `NUMBER` |  | Number of buffers on the write list |
| `CNUM_SET` | `NUMBER` |  | Number of buffers in the set |
| `BUF_GOT` | `NUMBER` |  | Number of buffers gotten by the set |
| `SUM_WRITE` | `NUMBER` |  | Number of buffers written by the set |
| `SUM_SCAN` | `NUMBER` |  | Number of buffers scanned in the set |
| `FREE_BUFFER_WAIT` | `NUMBER` |  | Free buffer wait statistic |
| `WRITE_COMPLETE_WAIT` | `NUMBER` |  | Write complete wait statistic |
| `BUFFER_BUSY_WAIT` | `NUMBER` |  | Buffer busy wait statistic |
| `FREE_BUFFER_INSPECTED` | `NUMBER` |  | Free buffer inspected statistic |
| `DIRTY_BUFFERS_INSPECTED` | `NUMBER` |  | Dirty buffers inspected statistic |
| `DB_BLOCK_CHANGE` | `NUMBER` |  | Database blocks changed statistic |
| `DB_BLOCK_GETS` | `NUMBER` |  | Database blocks gotten statistic |
| `CONSISTENT_GETS` | `NUMBER` |  | Consistent gets statistic |
| `PHYSICAL_READS` | `NUMBER` |  | Physical reads statistic |
| `PHYSICAL_WRITES` | `NUMBER` |  | Physical writes statistic |
| `CON_DBID` | `NUMBER` |  | The database ID of the PDB for the sampled session |
| `CON_ID` | `NUMBER` |  | The ID of the container that `CON_DBID` identifies. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

" [V$BUFFER\_POOL\_STATISTICS](V-BUFFER_POOL_STATISTICS.md) "