---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-FALSE_PING.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.223 V$FALSE\_PING

`V$FALSE_PING` is deprecated. The information that was provided in this view is now provided in the `V$INSTANCE_CACHE_TRANSFER` and `V$SEGMENT_STATISTICS` views.

| Column | Datatype | Description |
| --- | --- | --- |
| `FILE#` | `NUMBER` | Data file identifier number (to find the file name, query `DBA_DATA_FILES` or `V$DBFILE`) |
| `BLOCK#` | `NUMBER` | Block number |
| `STATUS` | `VARCHAR2(10)` | Status of the block:  - `free` - Not currently in use - `xcur` - Exclusive - `scur` - Shared current - `cr` - Consistent read - `read` - Being read from disk - `mrec` - In media recovery mode - `irec` - In instance recovery mode |
| `XNC` | `NUMBER` | Number of PCM lock conversions from Exclusive mode due to contention with another instance. This column is obsolete and maintained for backward compatibility. |
| `FORCED_READS` | `NUMBER` | Number of times the block had to be reread from the cache because another instance has forced it out of this instance's cache by requesting the lock on the block in exclusive mode |
| `FORCED_WRITES` | `NUMBER` | Number of times GCS had to write this block to cache because this instance had used the block and another instance had requested the lock on the block in a conflicting mode |
| `NAME` | `VARCHAR2(128)` | Name of the database object containing the block |
| `PARTITION_NAME` | `VARCHAR2(128)` | NULL for nonpartitioned objects |
| `KIND` | `VARCHAR2(15)` | Type of database object |
| `OWNER#` | `NUMBER` | Owner number |
| `LOCK_ELEMENT_ADDR` | `RAW(4 \| 8)` | Address of the lock element that contains the PCM lock that is covering the buffer. If more than one buffer has the same address, then these buffers are covered by the same PCM lock. |
| `LOCK_ELEMENT_NAME` | `NUMBER` | Name of the lock that contains the PCM lock that is covering the buffer |
| `CLASS#` | `NUMBER` | Lock element class |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

- " [V$INSTANCE\_CACHE\_TRANSFER](V-INSTANCE_CACHE_TRANSFER.md) "
- " [V$SEGMENT\_STATISTICS](V-SEGMENT_STATISTICS.md) "