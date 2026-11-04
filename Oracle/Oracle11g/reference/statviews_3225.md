---
title: DBA_HIST_FILESTATXS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_3225.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_HIST_FILESTATXS` displays information about file read/write statistics. This view contains snapshots of `V$FILESTAT`.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` |  | Unique snapshot ID |
| `DBID` | `NUMBER` |  | Database ID for the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` |  | Instance number for the snapshot |
| `FILE#` | `NUMBER` |  | File identification number |
| `CREATION_CHANGE#` | `NUMBER` |  | Change number at which the datafile was created |
| `FILENAME` | `VARCHAR2(513)` |  | Name of the datafile |
| `TS#` | `NUMBER` |  | Tablespace number |
| `TSNAME` | `VARCHAR2(30)` |  | Name of the tablespace |
| `BLOCK_SIZE` | `NUMBER` |  | Block size of the datafile |
| `PHYRDS` | `NUMBER` |  | Number of physical reads done |
| `PHYWRTS` | `NUMBER` |  | Number of times DBWR is required to write |
| `SINGLEBLKRDS` | `NUMBER` |  | Number of single block reads |
| `READTIM` | `NUMBER` |  | Time (in hundredths of a second) spent doing reads if the `TIMED_STATISTICS` parameter is `true`; `0` if `TIMED_STATISTICS` is `false` |
| `WRITETIM` | `NUMBER` |  | Time (in hundredths of a second) spent doing writes if the `TIMED_STATISTICS` parameter is `true`; `0` if `TIMED_STATISTICS` is `false` |
| `SINGLEBLKRDTIM` | `NUMBER` |  | Cumulative single block read time (in hundredths of a second) |
| `PHYBLKRD` | `NUMBER` |  | Number of physical blocks read |
| `PHYBLKWRT` | `NUMBER` |  | Number of blocks written to disk, which may be the same as `PHYWRTS` if all writes are single blocks |
| `WAIT_COUNT` | `NUMBER` |  | Shows the number of waits at the file level for contended buffers. This value includes the individual wait events that are included in the buffer busy waits wait event.  See Also: ["buffer busy waits"](waitevents003.md) |
| `TIME` | `NUMBER` |  | Time spent waiting for the wait events in the `WAIT_COUNT` column |