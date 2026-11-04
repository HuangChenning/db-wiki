---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-CACHE_LOCK.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.119 V$CACHE\_LOCK

`V$CACHE_LOCK` is deprecated. The information that was provided in this view is now provided in the `V$INSTANCE_CACHE_TRANSFER` and `V$SEGMENT_STATISTICS` views.

| Column | Datatype | Description |
| --- | --- | --- |
| `FILE#` | `NUMBER` | Data file identifier number (to find file name, query `DBA_DATA_FILES` or `V$DBFILE`) |
| `BLOCK#` | `NUMBER` | Block number |
| `STATUS` | `VARCHAR2(10)` | Status of the block:  - `free` - Not currently in use - `xcur` - Exclusive - `scur` - Shared current - `cr` - Consistent read - `read` - Being read from disk - `mrec` - In media recovery mode - `irec` - In instance recovery mode |
| `XNC` | `NUMBER` | Number of parallel cache management (PCM) lock conversions due to contention with another instance |
| `FORCED_READS` | `NUMBER` | Number of times the block had to be reread from the cache because another instance has forced it out of this instance's cache by requesting the lock on the block in exclusive mode |
| `FORCED_WRITES` | `NUMBER` | Number of times GCS had to write this block to cache because this instance had used the block and another instance had requested the lock on the block in a conflicting mode |
| `NAME` | `VARCHAR2(128)` | Name of the database object containing the block |
| `KIND` | `VARCHAR2(15)` | Type of database object:  - `1` - Index - `2` - Table - `3` - Cluster - `4` - View - `5` - Synonym - `6` - Sequence - `7` - Procedure - `8` - Function - `9` - Package - `10` - Nonexistent - `11` - Package body - `12` - Trigger - `13` - Type - `14` - Type body - `19` - Table partition - `20` - Index partition - `21` - LOB - `22` - Library - `Null` - Unknown |
| `OWNER#` | `NUMBER` | Owner number |
| `LOCK_ELEMENT_ADDR` | `RAW(4 \| 8)` | Address of the lock element that contains the PCM lock that is covering the buffer. If more than one buffer has the same address, then these buffers are covered by the same PCM lock. |
| `LOCK_ELEMENT_NAME` | `NUMBER` | Address of the lock element that contains the PCM lock that is covering the buffer. If more than one buffer has the same address, then these buffers are covered by the same PCM lock. |
| `INDX` | `NUMBER` | Platform-specific lock manager identifier |
| `CLASS` | `NUMBER` | Platform-specific lock manager identifier |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |