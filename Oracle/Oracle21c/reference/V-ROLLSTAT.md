---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-ROLLSTAT.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.185 V$ROLLSTAT

| Column | Datatype | Description |
| --- | --- | --- |
| `USN` | `NUMBER` | Rollback segment number |
| `LATCH` | `NUMBER` | Latch for the rollback segment |
| `EXTENTS` | `NUMBER` | Number of extents in the rollback segment |
| `RSSIZE` | `NUMBER` | Size (in bytes) of the rollback segment. This value differs by the number of bytes in one database block from the value of the `BYTES` column of the `*_SEGMENTS` view.  See Also: [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADMIN11462) for more information about space management for rollback segments |
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
| `STATUS` | `VARCHAR2(15)` | Rollback segment status:  - `ONLINE` - `PENDING OFFLINE` - `OFFLINE` - `FULL` |
| `CUREXT` | `NUMBER` | Current extent |
| `CURBLK` | `NUMBER` | Current block |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |