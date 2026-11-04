---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-BUFFER_POOL_STATISTICS.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.114 V$BUFFER\_POOL\_STATISTICS

`V$BUFFER_POOL_STATISTICS` displays statistics about all buffer pools available for the instance.

| Column | Datatype | Description |
| --- | --- | --- |
| `ID` | `NUMBER` | Buffer pool identifier number |
| `NAME` | `VARCHAR2(20)` | Name of the buffer pool |
| `BLOCK_SIZE` | `NUMBER` | Block size (in bytes) for buffers in this pool. Possible values: the standard block size, the power of 2 nonstandard block sizes, `2048`, `4096`, `8192`, `16384`, `32768`. |
| `SET_MSIZE` | `NUMBER` | Buffer pool maximum set size |
| `CNUM_REPL` | `NUMBER` | Number of buffers on replacement list |
| `CNUM_WRITE` | `NUMBER` | Number of buffers on write list |
| `CNUM_SET` | `NUMBER` | Number of buffers in set |
| `BUF_GOT` | `NUMBER` | Number of buffers gotten by the set |
| `SUM_WRITE` | `NUMBER` | Number of buffers written by the set |
| `SUM_SCAN` | `NUMBER` | Number of buffers scanned in the set |
| `FREE_BUFFER_WAIT` | `NUMBER` | Free buffer wait statistic |
| `WRITE_COMPLETE_WAIT` | `NUMBER` | Write complete wait statistic |
| `BUFFER_BUSY_WAIT` | `NUMBER` | Buffer busy wait statistic |
| `FREE_BUFFER_INSPECTED` | `NUMBER` | Free buffer inspected statistic |
| `DIRTY_BUFFERS_INSPECTED` | `NUMBER` | Dirty buffers inspected statistic |
| `DB_BLOCK_CHANGE` | `NUMBER` | Database blocks changed statistic |
| `DB_BLOCK_GETS` | `NUMBER` | Database blocks gotten statistic |
| `CONSISTENT_GETS` | `NUMBER` | Consistent gets statistic |
| `PHYSICAL_READS` | `NUMBER` | Physical reads statistic |
| `PHYSICAL_WRITES` | `NUMBER` | Physical writes statistic |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

" [DB\_CACHE\_SIZE](DB_CACHE_SIZE.md) "