---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-BT_SCAN_OBJ_TEMPS.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.112 V$BT\_SCAN\_OBJ\_TEMPS

`V$BT_SCAN_OBJ_TEMPS` shows the active objects currently tracked by the big table cache.

| Column | Datatype | Description |
| --- | --- | --- |
| `TS#` | `NUMBER` | Tablespace number |
| `DATAOBJ#` | `NUMBER` | Data object number (objd) |
| `SIZE_IN_BLKS` | `NUMBER` | Size of the object being scanned on this instance, in blocks |
| `TEMPERATURE` | `NUMBER` | Temperature of this object |
| `POLICY` | `VARCHAR2(10)` | Caching policy of this object. Possible values:  - `MEM_ONLY`: This object will be fully cached in memory. - `MEM_PART`: This object will be partially cached in memory and some portion will remain on disk and will not be cached. - `DISK`: this object will not be cached in memory or flash for the scan at all. - `INVALID`: The caching policy is not valid. |
| `CACHED_IN_MEM` | `NUMBER` | The number of blocks that are cached/allocated in memory for this object |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

" [DB\_BIG\_TABLE\_CACHE\_PERCENT\_TARGET](DB_BIG_TABLE_CACHE_PERCENT_TARGET.md) " for more information about enabling the big table cache