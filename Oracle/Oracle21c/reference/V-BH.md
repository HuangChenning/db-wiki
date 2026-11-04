---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-BH.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.108 V$BH

`V$BH` displays the status and number of pings for every buffer in the SGA. This is an Oracle Real Application Clusters view.

| Column | Datatype | Description |
| --- | --- | --- |
| `FILE#` | `NUMBER` | Data file identifier number (to find the file name, query `DBA_DATA_FILES` or `V$DBFILE`) |
| `BLOCK#` | `NUMBER` | Block number |
| `CLASS#` | `NUMBER` | Class number |
| `STATUS` | `VARCHAR2(10)` | Status of the buffer:  - `cr` - Consistent read - `flashcur` - A current flash cache buffer - `flashfree` - A free flash cache buffer - `free` - Not currently in use - `irec` - In instance recovery mode - `mrec` - In media recovery mode - `pi` - A past image in RAC mode - `pmemfree` - A free PMEM buffer - `pmemcr` - pmemcr - A consistent-read/previous version of a PMEM buffer - `pmemcur` - A current PMEM buffer - `read` - Being read from disk - `scur` - Shared current - `securefile` - A secured file buffer - `xcur` - Exclusive |
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
| `NEW` | `CHAR(1)` | Always set to `N`. This column is obsolete and maintained for backward compatibility. |
| `OBJD` | `NUMBER` | Database object number of the block that the buffer represents |
| `TS#` | `NUMBER` | Tablespace number of block |
| `LOBID` | `NUMBER` | If the buffer belongs to a SecureFiles object, the value in this column is the unique identifier for the SecureFiles object. For other buffer types, the value in this column is meaningless. |
| `CACHEHINT` | `NUMBER` | Numeric representation of the values in the `FLASH_CACHE` and `CELL_FLASH_CACHE` columns. See the descriptions and possible values for the `FLASH_CACHE` and `CELL_FLASH_CACHE` columns in this view. |
| `FLASH_CACHE` | `VARCHAR2(7)` | Database Smart Flash Cache hint to be used for segment blocks:  - DEFAULT - KEEP - NONE  Solaris and Oracle Linux functionality only. |
| `CELL_FLASH_CACHE` | `VARCHAR2(7)` | Cell flash cache hint to be used for segment blocks:  - DEFAULT - KEEP - NONE  See Also: Oracle Exadata Storage Server Software documentation for more information |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |