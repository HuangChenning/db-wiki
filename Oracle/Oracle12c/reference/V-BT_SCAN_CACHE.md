---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/V-BT_SCAN_CACHE.html
tags:
  - oracle
  - 12c
  - reference
---

`V$BT_SCAN_CACHE` shows the parameters and status of the big table cache section.

| Column | Datatype | Description |
| --- | --- | --- |
| `BT_CACHE_ALLOC` | `NUMBER` | Current ratio of the big table cache section to the buffer cache |
| `BT_CACHE_TARGET` | `NUMBER` | Target ratio of the big table cache section to the buffer cache |
| `OBJECT_COUNT` | `NUMBER` | Number of objects tracked by the big table cache section |
| `MEMORY_BUF_ALLOC` | `NUMBER` | Number of memory buffers allocated by the big table cache section to objects |
| `MIN_CACHED_TEMP` | `NUMBER` | Minimum temperature of any object that is allowed to be cached by the big table cache section |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

" [DB\_BIG\_TABLE\_CACHE\_PERCENT\_TARGET](DB_BIG_TABLE_CACHE_PERCENT_TARGET.md) " for more information about enabling the big table cache