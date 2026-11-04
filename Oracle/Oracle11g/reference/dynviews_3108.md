---
title: "V$TEMPSTAT"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_3108.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$TEMPSTAT` displays information about file read/write statistics.

| Column | Datatype | Description |
| --- | --- | --- |
| `FILE#` | `NUMBER` | Number of the file |
| `PHYRDS` | `NUMBER` | Number of physical reads done |
| `PHYWRTS` | `NUMBER` | Number of times DBWR is required to write |
| `PHYBLKRD` | `NUMBER` | Number of physical blocks read |
| `PHYBLKWRT` | `NUMBER` | Number of blocks written to disk, which may be the same as `PHYWRTS` if all writes are single blocks |
| `SINGLEBLKRDS` | `NUMBER` | Number of single block reads |
| `READTIM` | `NUMBER` | Time (in hundredths of a second) spent doing reads if the `TIMED_STATISTICS` parameter is `true`; `0` if `false` |
| `WRITETIM` | `NUMBER` | Time (in hundredths of a second) spent doing writes if the `TIMED_STATISTICS` parameter is `true`; `0` if `false` |
| `SINGLEBLKRDTIM` | `NUMBER` | Cumulative single block read time (in hundredths of a second) |
| `AVGIOTIM` | `NUMBER` | Average time (in hundredths of a second) spent on I/O, if the `TIMED_STATISTICS` parameter is `true`; `0` if `false` |
| `LSTIOTIM` | `NUMBER` | Time (in hundredths of a second) spent doing the last I/O, if the `TIMED_STATISTICS` parameter is `true`; `0` if `false` |
| `MINIOTIM` | `NUMBER` | Minimum time (in hundredths of a second) spent on a single I/O, if the `TIMED_STATISTICS` parameter is `true`; `0` if `false` |
| `MAXIORTM` | `NUMBER` | Maximum time (in hundredths of a second) spent doing a single read, if the `TIMED_STATISTICS` parameter is `true`; `0` if `false` |
| `MAXIOWTM` | `NUMBER` | Maximum time (in hundredths of a second) spent doing a single write, if the `TIMED_STATISTICS` parameter is `true`; `0` if `false` |