---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-DB_CACHE_ADVICE.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.164 V$DB\_CACHE\_ADVICE

`V$DB_CACHE_ADVICE` contains rows that predict the number of physical reads for the cache size corresponding to each row.

The rows also compute a "physical read factor," which is the ratio of the number of estimated reads to the number of reads actually performed by the real buffer cache during the measurement interval.

See Also:

" [DB\_CACHE\_ADVICE](DB_CACHE_ADVICE.md) "

| Column | Datatype | Description |
| --- | --- | --- |
| `ID` | `NUMBER` | Buffer pool identifier (ranges from 1 to 8) |
| `NAME` | `VARCHAR2(20)` | Buffer pool name |
| `BLOCK_SIZE` | `NUMBER` | Block size in bytes for buffers in this pool. Possible values: the standard block size, the power of 2 nonstandard block sizes, `2048`, `4096`, `8192`, `16384`, `32768`. |
| `ADVICE_STATUS` | `VARCHAR2(3)` | Status of the advisory. `ON` indicates it is currently running; `OFF` indicates it is disabled (in this case the estimates are historical and calculated when last enabled). |
| `SIZE_FOR_ESTIMATE` | `NUMBER` | Cache size for prediction (in megabytes) |
| `SIZE_FACTOR` | `NUMBER` | Size factor with respect to the current cache size |
| `BUFFERS_FOR_ESTIMATE` | `NUMBER` | Cache size for prediction (in terms of buffers) |
| `ESTD_PHYSICAL_READ_FACTOR` | `NUMBER` | Physical read factor for this cache size, which is the ratio of the number of estimated physical reads to the number of reads in the real cache. If there are no physical reads in the real cache, the value of this column is null. |
| `ESTD_PHYSICAL_READS` | `NUMBER` | Estimated number of physical reads for this cache size |
| `ESTD_PHYSICAL_READ_TIME` | `NUMBER` | Estimated disk read time (in seconds) |
| `ESTD_PCT_OF_DB_TIME_FOR_READS` | `NUMBER` | Estimated disk time as a percentage of the total time |
| `ESTD_CLUSTER_READS` | `NUMBER` | Estimated total number of blocks foreground processes read from the global cache (Oracle Real Application Clusters only) |
| `ESTD_CLUSTER_READ_TIME` | `NUMBER` | Estimated total amount of time, in seconds, foreground processes read from global cache (Oracle Real Application Clusters only) |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |