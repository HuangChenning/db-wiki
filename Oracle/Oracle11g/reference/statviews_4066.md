---
title: DBA_HIST_TEMPSTATXS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4066.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_HIST_TEMPSTATXS` displays information about temporary file read/write statistics. This view contains snapshots of `V$TEMPSTAT`.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` | `NOT NULL` | Unique snapshot ID |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID for the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` | `NOT NULL` | Instance number for the snapshot |
| `FILE#` | `NUMBER` | `NOT NULL` | File identification number |
| `CREATION_CHANGE#` | `NUMBER` | `NOT NULL` | Change number at which the tempfile was created |
| `FILENAME` | `VARCHAR2(513)` | `NOT NULL` | Name of the tempfile |
| `TS#` | `NUMBER` | `NOT NULL` | Tablespace number |
| `TSNAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the tablespace |
| `BLOCK_SIZE` | `NUMBER` |  | Block size of the tempfile |
| `PHYRDS` | `NUMBER` |  | Number of physical reads done |
| `PHYWRTS` | `NUMBER` |  | Number of times DBWR is required to write |
| `SINGLEBLKRDS` | `NUMBER` |  | Number of single block reads |
| `READTIM` | `NUMBER` |  | Time (in hundredths of a second) spent doing reads if the `TIMED_STATISTICS` parameter is `true`; `0` if `false` |
| `WRITETIM` | `NUMBER` |  | Time (in hundredths of a second) spent doing writes if the `TIMED_STATISTICS` parameter is `true`; `0` if `false` |
| `SINGLEBLKRDTIM` | `NUMBER` |  | Cumulative single block read time (in hundredths of a second) |
| `PHYBLKRD` | `NUMBER` |  | Number of physical blocks read |
| `PHYBLKWRT` | `NUMBER` |  | Number of blocks written to disk, which may be the same as `PHYWRTS` if all writes are single blocks |
| `WAIT_COUNT` | `NUMBER` |  | Shows the number of waits at the file level for contended buffers. This value includes the individual wait events that are included in the buffer busy waits wait event.  See Also: ["buffer busy waits"](waitevents003.md) |
| `TIME` | `NUMBER` |  | Time spent waiting for the wait events in the `WAIT_COUNT` column |