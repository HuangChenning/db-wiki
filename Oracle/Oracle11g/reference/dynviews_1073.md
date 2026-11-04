---
title: "V$BUFFER_POOL_STATISTICS"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1073.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$BUFFER_POOL_STATISTICS` displays statistics about all buffer pools available for the instance.

| Column | Datatype | Description |
| --- | --- | --- |
| `ID` | `NUMBER` | Buffer pool identifier number |
| `NAME` | `VARCHAR2(20)` | Name of the buffer pool |
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

See Also:

["DB\_CACHE\_SIZE"](initparams052.md)