---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/V-RESULT_CACHE_STATISTICS.html
tags:
  - oracle
  - 12c
  - reference
---

`V$RESULT_CACHE_STATISTICS` displays various Result Cache settings and usage statistics.

| Column | Datatype | Description |
| --- | --- | --- |
| `ID` | `NUMBER` | Statistic number |
| `NAME` | `VARCHAR2(128)` | Name of the statistic (see Table 8-6) |
| `VALUE` | `VARCHAR2(81)` | Value of the statistic |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

Table 8-6 V$RESULT\_CACHE\_STATISTICS Statistics

| Statistic Name | Description |
| --- | --- |
| Block Size (Bytes) | Size of each memory block |
| Block Count Maximum | Maximum number of memory blocks allowed |
| Block Count Current | Number of memory blocks currently allocated |
| Result Size Maximum (Blocks) | Maximum number of blocks allowed for a single result |
| Create Count Success | Number of cache results successfully created |
| Create Count Failure | Number of cache results that failed to create |
| Find Count | Number of cached results that were successfully found |
| Invalidation Count | Total number of invalidations |
| Delete Count Invalid | Number of invalid cached results deleted |
| Delete Count Valid | Number of valid cached results deleted |
| Hash Chain Length | Average length of items in the hash chain |
| Find Copy Count | Number of results copied directly out of the cache |