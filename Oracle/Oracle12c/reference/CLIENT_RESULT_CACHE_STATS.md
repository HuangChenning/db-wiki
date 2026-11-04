---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/CLIENT_RESULT_CACHE_STATS.html
tags:
  - oracle
  - 12c
  - reference
---

`CLIENT_RESULT_CACHE_STATS$` displays various Client Result Cache settings and usage statistics.

Statistics are stored as name, value pairs. For each client cache ID, there will be multiple rows for each statistic.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `CACHE_ID` | `NUMBER` | `NOT NULL` | Unique ID per client cache |
| `STAT_ID` | `NUMBER` | `NOT NULL` | Statistic ID |
| `NAME` | `VARCHAR2(128)` |  | Name of the statistic (see Table 3-1) |
| `VALUE` | `NUMBER` |  | Value of the statistic |

Table 3-1 CLIENT\_RESULT\_CACHE\_STATS$ Statistics

| Statistic Name | Description |
| --- | --- |
| Block Size | Size (in bytes) of each memory block in the result cache. |
| Block Count Max | Maximum number of blocks that can be allocated in the result cache based on the cache size configuration parameters on server and on client. |
| Block Count Current | Current number of blocks allocated by the client result cache. |
| Hash Bucket Count | Size of the hash table used for query matching. |
| Create Count Success | Number of cached result sets that did not get invalidated before caching all the rows of the result set. |
| Create Count Failure | Number of cached result sets that did not fetch all the rows in the result set. |
| Find Count | Number of cache hits. |
| Invalidation Count | Number of cached result sets that got invalidated due to database changes that could have affected the result set. |
| Delete Count Invalid | Number of cached result rests not invalidated whose memory was reclaimed by result cache. |
| Delete Count Valid | Number of invalidated cached result rests whose memory was reclaimed by result cache. |