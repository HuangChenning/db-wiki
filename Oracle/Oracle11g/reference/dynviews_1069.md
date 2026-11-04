---
title: "V$BH"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1069.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$BH` displays the status and number of pings for every buffer in the SGA. This is a Real Application Clusters view.

| Column | Datatype | Description |
| --- | --- | --- |
| `FILE#` | `NUMBER` | Datafile identifier number (to find the filename, query `DBA_DATA_FILES` or `V$DBFILE`) |
| `BLOCK#` | `NUMBER` | Block number |
| `CLASS#` | `NUMBER` | Class number |
| `STATUS` | `VARCHAR2(6)` | Status of the buffer: - `free` - Not currently in use - `xcur` - Exclusive - `scur` - Shared current - `cr` - Consistent read - `read` - Being read from disk - `mrec` - In media recovery mode - `irec` - In instance recovery mode |
| `XNC` | `NUMBER` | This column is obsolete. Its value is hard-coded to 0. |
| `FORCED_READS` | `NUMBER` | This column is obsolete. Its value is hard-coded to 0. |
| `FORCED_WRITES` | `NUMBER` | This column is obsolete. Its value is hard-coded to 0. |
| `LOCK_ELEMENT_ADDR` | `RAW(4 \| 8)` | Address of the lock element that contains the PCM lock that is covering the buffer. If more than one buffer has the same address, then these buffers are covered by the same PCM lock. |
| `LOCK_ELEMENT_NAME` | `NUMBER` | The address of the lock element that contains the PCM lock that is covering the buffer. If more than one buffer has the same address, then these buffers are covered by the same PCM lock. |
| `LOCK_ELEMENT_CLASS` | `NUMBER` | The address of the lock element that contains the PCM lock that is covering the buffer. If more than one buffer has the same address, then these buffers are covered by the same PCM lock. |
| `DIRTY` | `VARCHAR2(1)` | `Y` - block modified |
| `TEMP` | `VARCHAR2(1)` | `Y` - temporary block |
| `PING` | `VARCHAR2(1)` | `Y` - block pinged |
| `STALE` | `VARCHAR2(1)` | `Y` - block is stale |
| `DIRECT` | `VARCHAR2(1)` | `Y` - direct block |
| `NEW` | `VARCHAR2(1)` | Always set to `N`. This column is obsolete and maintained for backward compatibility. |
| `OBJD` | `NUMBER` | Database object number of the block that the buffer represents |
| `TS#` | `NUMBER` | Tablespace number of block |
| `LOBID` | `NUMBER` | If the buffer belongs to a SecureFiles object, the value in this column is the unique identifier for the SecureFiles object. For other buffer types, the value in this column is meaningless. |