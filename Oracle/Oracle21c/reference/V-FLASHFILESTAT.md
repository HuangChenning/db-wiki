---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-FLASHFILESTAT.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.239 V$FLASHFILESTAT

`V$FLASHFILESTAT` displays statistics about Database Smart Flash Cache.

By taking snapshots of `SINGLEBLKRDS` and `SINGLEBLKRDTIM_MICRO`, you can easily calculate the average latency of all the flash files in a given time period

| Column | Datatype | Description |
| --- | --- | --- |
| `FLASHFILE#` | `NUMBER` | The file number of the flash file |
| `NAME` | `VARCHAR2(513)` | Name and path of the flash file |
| `BYTES` | `NUMBER` | Size of the flash file, in bytes |
| `ENABLED` | `NUMBER` | Indicates whether this flash file is enabled or not |
| `SINGLEBLKRDS` | `NUMBER` | Number of reads to the flash file |
| `SINGLEBLKRDTIM_MICRO` | `NUMBER` | Cumulative latency of reading blocks from this particular flash file/device, in microseconds |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

[Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADMIN13391) for more information about configuring Database Smart Flash Cache