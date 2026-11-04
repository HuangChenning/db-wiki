---
title: "V$DB_CACHE_ADVICE"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1106.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$DB_CACHE_ADVICE` contains rows that predict the number of physical reads for the cache size corresponding to each row. The rows also compute a "physical read factor," which is the ratio of the number of estimated reads to the number of reads actually performed by the real buffer cache during the measurement interval.

See Also:

["DB\_CACHE\_ADVICE"](initparams051.md)

| Column | Datatype | Description |
| --- | --- | --- |
| `ID` | `NUMBER` | Buffer pool identifier (ranges from 1 to 8) |
| `NAME` | `VARCHAR2(20)` | Buffer pool name |
| `BLOCK_SIZE` | `NUMBER` | Block size in bytes for buffers in this pool. Possible values: the standard block size, the power of 2 non-standard block sizes, `2048`, `4096`, `8192`, `16384`, `32768`. |
| `ADVICE_STATUS` | `VARCHAR2(3)` | Status of the advisory. `ON` indicates it is currently running; `OFF` indicates it is disabled (in this case the estimates are historical and calculated when last enabled). |
| `SIZE_FOR_ESTIMATE` | `NUMBER` | Cache size for prediction (in megabytes) |
| `SIZE_FACTOR` | `NUMBER` | Size factor with respect to the current cache size |
| `BUFFERS_FOR_ESTIMATE` | `NUMBER` | Cache size for prediction (in terms of buffers) |
| `ESTD_PHYSICAL_READ_FACTOR` | `NUMBER` | Physical read factor for this cache size, which is the ratio of the number of estimated physical reads to the number of reads in the real cache. If there are no physical reads in the real cache, the value of this column is null. |
| `ESTD_PHYSICAL_READS` | `NUMBER` | Estimated number of physical reads for this cache size |
| `ESTD_PHYSICAL_READ_TIME` | `NUMBER` | Estimated disk read time (in seconds) |
| `ESTD_PCT_OF_DB_TIME_FOR_READS` | `NUMBER` | Estimated disk time as a percentage of the total time |
| `ESTD_CLUSTER_READS` | `NUMBER` | Estimated total number of blocks foreground processes read from the global cache (Real Application Clusters only) |
| `ESTD_CLUSTER_READ_TIME` | `NUMBER` | Estimated total amount of time, in seconds, foreground processes read from global cache (Real Application Clusters only) |