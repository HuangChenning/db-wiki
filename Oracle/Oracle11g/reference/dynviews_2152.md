---
title: "V$ROLLSTAT"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2152.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$ROLLSTAT` contains rollback segment statistics.

| Column | Datatype | Description |
| --- | --- | --- |
| `USN` | `NUMBER` | Rollback segment number |
| `LATCH` | `NUMBER` | Latch for the rollback segment |
| `EXTENTS` | `NUMBER` | Number of extents in the rollback segment |
| `RSSIZE` | `NUMBER` | Size (in bytes) of the rollback segment. This value differs by the number of bytes in one database block from the value of the `BYTES` column of the `*_SEGMENTS` view.  See Also: [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/toc.htm) |
| `WRITES` | `NUMBER` | Number of bytes written to the rollback segment |
| `XACTS` | `NUMBER` | Number of active transactions |
| `GETS` | `NUMBER` | Number of header gets |
| `WAITS` | `NUMBER` | Number of header waits |
| `OPTSIZE` | `NUMBER` | Optimal size of the rollback segment |
| `HWMSIZE` | `NUMBER` | High watermark of the rollback segment size |
| `SHRINKS` | `NUMBER` | Number of times the size of a rollback segment decreases |
| `WRAPS` | `NUMBER` | Number of times rollback segment is wrapped |
| `EXTENDS` | `NUMBER` | Number of times rollback segment size is extended |
| `AVESHRINK` | `NUMBER` | Average shrink size |
| `AVEACTIVE` | `NUMBER` | Current size of active extents, averaged over time. |
| `STATUS` | `VARCHAR2(15)` | Rollback segment status: |
| `CUREXT` | `NUMBER` | Current extent |
| `CURBLK` | `NUMBER` | Current block |