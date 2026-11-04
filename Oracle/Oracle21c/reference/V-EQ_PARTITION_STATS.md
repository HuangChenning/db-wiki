---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-EQ_PARTITION_STATS.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.211 V$EQ\_PARTITION\_STATS

`V$EQ_PARTITION_STATS` displays usage statistics for the Transactional Event Queue (TEQ) queue partition cache and the dequeue log partition cache.

| Column | Datatype | Description |
| --- | --- | --- |
| `INST_ID` | `NUMBER` | Current instance ID |
| `QUEUE_ID` | `NUMBER` | Queue ID |
| `QUEUE_TABLE_ID` | `NUMBER` | Queue table object ID |
| `QUEUE_SCHEMA` | `VARCHAR2(128)` | Queue schema name |
| `QUEUE_NAME` | `VARCHAR2(128)` | Queue name |
| `PT_TUNED_SIZ_QT` | `NUMBER` | Current tuned size of the queue partition cache, expressed in number of partition cache elements |
| `PT_CACHED_PTNS_QT` | `NUMBER` | Current number of cached partitions in the queue partition cache |
| `PT_OVER_CACHED_PTNS_QT` | `NUMBER` | Current number of over-cached partitions in the queue partition cache, that is, the number of cached partitions whose partition cache elements exceed the current tuned size of the queue partition cache |
| `PT_TOTAL_UPTUNE_QT` | `NUMBER` | Total amount of space added to the queue partition cache due to tune-ups, since the cache was initialized, expressed in number of partition cache elements |
| `PT_NO_OF_UPTUNES_QT` | `NUMBER` | Total number of times a tune-up was triggered on the queue partition cache, since the cache was initialized |
| `PT_TOTAL_DOWNTUNE_QT` | `NUMBER` | Total amount of space removed from the queue partition cache due to tune-downs, since the cache was initialized, expressed in number of partition cache elements |
| `PT_NO_OF_DOWNTUNES_QT` | `NUMBER` | Total number of times a tune-down was triggered on the queue partition cache, since the cache was initialized |
| `PT_CACHE_MISS_QT` | `NUMBER` | Total number of cache misses during partition lookups on the queue partition cache |
| `PT_CACHE_HIT_QT` | `NUMBER` | Total number of cache hits during partition lookups on the queue partition cache |
| `PT_TOTAL_CACH_GET_QT` | `NUMBER` | Total number of successful fetches from the queue partition cache |
| `PT_TOTAL_CACH_PUT_QT` | `NUMBER` | Total number of caching operations that occurred on the queue partition cache |
| `PT_UNBOUNDINGS_QT` | `NUMBER` | Total number of times queue partitions were unbounded |
| `PT_TUNED_SIZ_DQ` | `NUMBER` | Current tuned size of the dequeue log partition cache, expressed in number of partition cache elements |
| `PT_CACHED_PTNS_DQ` | `NUMBER` | Current number of cached partitions in the dequeue log partition cache |
| `PT_OVER_CACHED_PTNS_DQ` | `NUMBER` | Current number of over-cached partitions in the dequeue log partition cache, that is, the number of cached dequeue log partitions whose partition cache elements exceed the current tuned size of the dequeue log partition cache |
| `PT_TOTAL_UPTUNE_DQ` | `NUMBER` | Total amount of space added to the dequeue log partition cache due to tune-ups, since the cache was initialized, expressed in number of partition cache elements |
| `PT_NO_OF_UPTUNES_DQ` | `NUMBER` | Total number of times a tune-up was triggered on the dequeue log partition cache, since the cache was initialized |
| `PT_TOTAL_DOWNTUNE_DQ` | `NUMBER` | Total amount of space removed from the dequeue log partition cache due to tune-downs, since the cache was initialized, expressed in number of partition cache elements |
| `PT_NO_OF_DOWNTUNES_DQ` | `NUMBER` | Total number of times a tune-down was triggered on the dequeue log partition cache, since the cache was initialized |
| `PT_CACHE_MISS_DQ` | `NUMBER` | Total number of cache misses during partition lookups on the dequeue log partition cache |
| `PT_CACHE_HIT_DQ` | `NUMBER` | Total number of cache hits during partition lookups on the dequeue log partition cache |
| `PT_TOTAL_CACH_GET_DQ` | `NUMBER` | Total number of successful fetches from the dequeue log partition cache |
| `PT_TOTAL_CACH_PUT_DQ` | `NUMBER` | Total number of caching operations that occurred on the dequeue log partition cache |
| `PT_UNBOUNDINGS_DQ` | `NUMBER` | Total number of times dequeue log partitions were unbounded |
| `ADD_PARTITION_FG_QT` | `NUMBER` | Total number of queue partitions created inline during foreground AQ enqueue operations |
| `ADD_PARTITION_BG_QT` | `NUMBER` | Total number of queue partitions created asynchronously by the AQ partitioning background process |
| `ADD_PARTITION_FG_DQLOG` | `NUMBER` | Total number of dequeue log partitions created inline during foreground AQ dequeue operations |
| `ADD_PARTITION_BG_DQLOG` | `NUMBER` | Total number of dequeue log partitions created asynchronously by the AQ partitioning background process |
| `TRUNC_PARTITION_QT` | `NUMBER` | Total number of truncated and recycled queue partitions |
| `TRUNC_PARTITION_DQLOG` | `NUMBER` | Total number of truncated and recycled dequeue log partitions |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

Note:

This view is available starting with Oracle Database 21c.

See Also:

[Oracle Database Advanced Queuing User's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADQUE0100) for more information about Oracle Transactional Event Queues and Advanced Queuing