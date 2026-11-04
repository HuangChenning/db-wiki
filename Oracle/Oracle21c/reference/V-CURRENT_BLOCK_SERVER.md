---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-CURRENT_BLOCK_SERVER.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.152 V$CURRENT\_BLOCK\_SERVER

`V$CURRENT_BLOCK_SERVER` displays statistics on the Global Cache Service processes (LMS) used in cache fusion.

| Column | Datatype | Description |
| --- | --- | --- |
| `PIN0` | `NUMBER` | Pins taking less than 100 microseconds |
| `PIN1` | `NUMBER` | Pins taking 100 microseconds to 1 millisecond |
| `PIN10` | `NUMBER` | Pins taking 1 to 10 milliseconds |
| `PIN100` | `NUMBER` | Pins taking 10 to 100 milliseconds |
| `PIN1000` | `NUMBER` | Pins taking 100 to 1000 milliseconds |
| `PIN10000` | `NUMBER` | Pins taking 1000 to 10000 milliseconds |
| `FLUSH0` | `NUMBER` | Flushes taking less than 100 microseconds |
| `FLUSH1` | `NUMBER` | Flushes taking 100 microseconds to 1 millisecond |
| `FLUSH10` | `NUMBER` | Flushes taking 1 to 10 milliseconds |
| `FLUSH100` | `NUMBER` | Flushes taking 10 to 100 milliseconds |
| `FLUSH1000` | `NUMBER` | Flushes taking 100 to 1000 milliseconds |
| `FLUSH10000` | `NUMBER` | Flushes taking 1000 to 10000 milliseconds |
| `WRITE1` <sup>Foot 1</sup> | `NUMBER` | Writes taking less than 1 millisecond |
| `WRITE10` <sup>Foot 1</sup> | `NUMBER` | Writes taking 1 to 10 milliseconds |
| `WRITE100` <sup>Foot 1</sup> | `NUMBER` | Writes taking 10 to 100 milliseconds |
| `WRITE1000` <sup>Foot 1</sup> | `NUMBER` | Writes taking 100 to 1000 milliseconds |
| `WRITE10000` <sup>Foot 1</sup> | `NUMBER` | Writes taking 1000 to 10000 milliseconds |
| `CLEANDC` | `NUMBER` | Reserved for internal use |
| `RCVDC` | `NUMBER` | Number of lock down-converts to S (shared) caused by instance recovery |
| `QUEUEDC` | `NUMBER` | Number of queued lock down-converts to NULL |
| `EVICTDC` | `NUMBER` | Number of lock down-converts to NULL caused by an SGA shrink |
| `WRITEDC` | `NUMBER` | Number of dirty blocks in read-mostly objects which were written and the X (exclusive) lock down-converted to S (shared) locks |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

<sup>Footnote 1</sup>

This column is deprecated in Oracle Database 12c Release 2 (12.2.0.1) and may be removed in a future release.