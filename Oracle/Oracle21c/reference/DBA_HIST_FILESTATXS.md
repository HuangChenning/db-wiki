---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_HIST_FILESTATXS.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.405 DBA\_HIST\_FILESTATXS

`DBA_HIST_FILESTATXS` displays information about file read/write statistics.

This view contains snapshots of `V$FILESTAT`.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` | `NOT NULL` | Unique snapshot ID |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID for the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` | `NOT NULL` | Instance number for the snapshot |
| `FILE#` | `NUMBER` | `NOT NULL` | File identification number |
| `CREATION_CHANGE#` | `NUMBER` | `NOT NULL` | Change number at which the data file was created |
| `FILENAME` | `VARCHAR2(513)` | `NOT NULL` | Name of the data file |
| `TS#` | `NUMBER` | `NOT NULL` | Tablespace number |
| `TSNAME` | `VARCHAR2(30)` |  | Name of the tablespace |
| `BLOCK_SIZE` | `NUMBER` |  | Block size of the data file |
| `PHYRDS` | `NUMBER` |  | Number of physical reads done |
| `PHYWRTS` | `NUMBER` |  | Number of times DBWR is required to write |
| `SINGLEBLKRDS` | `NUMBER` |  | Number of single block reads |
| `READTIM` | `NUMBER` |  | Time (in hundredths of a second) spent doing reads if the `TIMED_STATISTICS` parameter is `true`; `0` if `TIMED_STATISTICS` is `false` |
| `WRITETIM` | `NUMBER` |  | Time (in hundredths of a second) spent doing writes if the `TIMED_STATISTICS` parameter is `true`; `0` if `TIMED_STATISTICS` is `false` |
| `SINGLEBLKRDTIM` | `NUMBER` |  | Cumulative single block read time (in hundredths of a second) |
| `PHYBLKRD` | `NUMBER` |  | Number of physical blocks read |
| `PHYBLKWRT` | `NUMBER` |  | Number of blocks written to disk, which may be the same as `PHYWRTS` if all writes are single blocks |
| `WAIT_COUNT` | `NUMBER` |  | Shows the number of waits at the file level for contended buffers. This value includes the individual wait events that are included in the buffer busy waits wait event.  See Also: " [buffer busy waits](descriptions-of-wait-events.md) " |
| `TIME` | `NUMBER` |  | Time spent waiting for the wait events in the `WAIT_COUNT` column |
| `OPTIMIZED_PHYBLKRD` | `NUMBER` |  | Number of physical reads from Database Smart Flash Cache blocks |
| `CON_DBID` | `NUMBER` |  | The database ID of the PDB for the sampled session |
| `CON_ID` | `NUMBER` |  | The ID of the container that `CON_DBID` identifies. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

" [V$FILESTAT](V-FILESTAT.md) "