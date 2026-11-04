---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-RESULT_CACHE_STATISTICS.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.173 V$RESULT\_CACHE\_STATISTICS

`V$RESULT_CACHE_STATISTICS` displays various result cache settings and usage statistics.

| Column | Datatype | Description |
| --- | --- | --- |
| `ID` | `NUMBER` | Statistic number |
| `NAME` | `VARCHAR2(128)` | Name of the statistic (see Table 9-6) |
| `VALUE` | `VARCHAR2(81)` | Value of the statistic |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

Table 9-6 V$RESULT\_CACHE\_STATISTICS and V$RESULT\_SUBCACHE\_STATISTICS Statistics

| Statistic Name | Description |
| --- | --- |
| Block Count Current | Number of memory blocks currently allocated |
| Block Count Maximum | Maximum number of memory blocks allowed |
| Block Size (Bytes) | Size of each memory block |
| Create Count Failure | Number of cache results that failed to create |
| Create Count Success | Number of cache results successfully created |
| Delete Count Invalid | Number of invalid cached results deleted |
| Delete Count Valid | Number of valid cached results deleted |
| Find Copy Count | Number of results copied directly out of the cache |
| Find Count | Number of cached results that were successfully found |
| Global Load Rate | Rate at which cached results were fetched from remote instances (in bytes per 10 milliseconds) |
| Global Prune By Self Count | Number of times this instance did not provide a cached result to a remote instance because this instance deemed it inefficient to do so |
| Global Prune Count | Number of times this instance did not fetch a cached result from a remote instance because it was deemed inefficient to do so |
| Hash Chain Length | Average length of items in the hash chain |
| Invalidation Count | Total number of invalidations |
| Result Size Maximum (Blocks) | Maximum number of blocks allowed for a single result |
| Subcache Count | Number of subcaches in the result cache |

See Also:

" [V$RESULT\_SUBCACHE\_STATISTICS](V-RESULT_SUBCACHE_STATISTICS.md) "