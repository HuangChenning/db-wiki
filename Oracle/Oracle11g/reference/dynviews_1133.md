---
title: "V$FALSE_PING"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1133.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$FALSE_PING` is deprecated. The information that was provided in this view is now provided in the `V$INSTANCE_CACHE_TRANSFER` and `V$SEGMENT_STATISTICS` views.

| Column | Datatype | Description |
| --- | --- | --- |
| `FILE#` | `NUMBER` | Datafile identifier number (to find the filename, query `DBA_DATA_FILES` or `V$DBFILE`) |
| `BLOCK#` | `NUMBER` | Block number |
| `STATUS` | `VARCHAR2(6)` | Status of the block: - `free` - Not currently in use - `xcur` - Exclusive - `scur` - Shared current - `cr` - Consistent read - `read` - Being read from disk - `mrec` - In media recovery mode - `irec` - In instance recovery mode |
| `XNC` | `NUMBER` | Number of PCM lock conversions from Exclusive mode due to contention with another instance. This column is obsolete and maintained for backward compatibility. |
| `FORCED_READS` | `NUMBER` | Number of times the block had to be reread from the cache because another instance has forced it out of this instance's cache by requesting the lock on the block in exclusive mode |
| `FORCED_WRITES` | `NUMBER` | Number of times GCS had to write this block to cache because this instance had used the block and another instance had requested the lock on the block in a conflicting mode |
| `NAME` | `VARCHAR2(30)` | Name of the database object containing the block |
| `PARTITION_NAME` | `VARCHAR2(30)` | NULL for non-partitioned objects |
| `KIND` | `VARCHAR2(15)` | Type of database object |
| `OWNER#` | `NUMBER` | Owner number |
| `LOCK_ELEMENT_ADDR` | `RAW(4 \| 8)` | Address of the lock element that contains the PCM lock that is covering the buffer. If more than one buffer has the same address, then these buffers are covered by the same PCM lock. |
| `LOCK_ELEMENT_NAME` | `NUMBER` | Name of the lock that contains the PCM lock that is covering the buffer |
| `LOCK_ELEMENT_CLASS` | `NUMBER` | Lock element class |