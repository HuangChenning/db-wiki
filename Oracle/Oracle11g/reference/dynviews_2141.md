---
title: "V$RESULT_CACHE_STATISTICS"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2141.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$RESULT_CACHE_STATISTICS` displays various Result Cache settings and usage statistics.

| Column | Datatype | Description |
| --- | --- | --- |
| `ID` | `NUMBER` | Statistic number |
| `NAME` | `VARCHAR2(128)` | Name of the statistic (see Table 8-6) |
| `VALUE` | `VARCHAR2(81)` | Value of the statistic |

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
| Find Copy Count <sup>Foot 1</sup> | Number of results copied directly out of the cache |

<sup>Footnote 1</sup> This statistic is available starting with Oracle Database 11g Release 2 (11.2.0.2).