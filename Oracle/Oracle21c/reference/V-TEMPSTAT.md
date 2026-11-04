---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-TEMPSTAT.html
tags:
  - oracle
  - 21c
  - reference
---

## 10.113 V$TEMPSTAT

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
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |