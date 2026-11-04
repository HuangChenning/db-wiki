---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-AQ_MESSAGE_CACHE_STAT.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.26 V$AQ\_MESSAGE\_CACHE\_STAT

`V$AQ_MESSAGE_CACHE_STAT` displays statistics about memory management for sharded queues in the Streams pool within the System Global Area (SGA). Sharded queues use the Streams pool in units of subshards. Thus, columns of this view shows statistics at subshard level. This view shows statistics across all sharded queues.

Note:

AQ sharded queues are deprecated in Oracle Database 21c. Oracle recommends that you instead use Transactional Event Queues (TEQs) for higher throughput and better performance.

| Column | Datatype | Description |
| --- | --- | --- |
| `NUM_EVICTED` | `NUMBER` | Number of evicted subshards across all sharded queues |
| `NUM_PREFETCHED` | `NUMBER` | Number of subshards pre-fetched by AQ background process |
| `NUM_UNEVICTION` | `NUMBER` | Number of subshards un-evicted by foreground process (like dequeue process) |
| `NUM_UNCACHED` | `NUMBER` | Number of subshards stored as uncached |
| `NUM_TRACKED` | `NUMBER` | Number of subshards which are actively tracking dequeue rates |
| `NUM_CACHED` | `NUMBER` | Number of subshards stored as cached |
| `MAX_SUBSH_SIZE` | `NUMBER` | Maximum subshard size seen till now, in terms of number of messages per subshard |
| `MIN_SUBSH_SIZE` | `NUMBER` | Minimum subshard size seen till now, in terms of number of messages per subshard |
| `MEAN_SUBSH_SIZE` | `NUMBER` | Mean subshard size seen till now, in terms of number of messages per subshard |
| `AVG_EVICTION_RATE` | `NUMBER` | Average number subshards evicted per second |
| `AVG_LOAD_RATE` | `NUMBER` | Average number of subshards pre-fetched or un-evicted per second |
| `AVG_EVICTION_TIME` | `NUMBER` | Average time taken to evict one subshard (in milliseconds) |
| `AVG_LOAD_TIME` | `NUMBER` | Average time taken to un-evict one subshard (in milliseconds) |
| `AVG_MISS_RATIO` | `NUMBER` | Average ratio of number of foreground un-evictions versus background pre-fetch |
| `AVG_THRASH_RATIO` | `NUMBER` | Average ratio of number of subshard pre-fetched by background without dequeue attempt versus total number of subshards prefetched |
| `MANDATORY_AFF_SWITCH_ATTEMPTS` | `NUMBER` | An affinity switch is a change in dequeue instance for a shard-subscriber pair. A mandatory affinity switch is when there are local enqueues in the queue at the instance but no local dequeues present, so the dequeue affinity is switched to another instance for that shard-subscriber pair. This column shows the number of times mandatory affinity switches were attempted across all instances. Populated at the smallest instance id only. |
| `OPTIONAL_AFF_SWITCH_ATTEMPTS` | `NUMBER` | Optional affinity switches are affinity switches that are not mandatory. Optional affinity switches are done for global load balancing across the Oracle Real Application Clusters (Oracle RAC) database. This column shows the number of times optional affinity switches were attempted across all instances. Populated at the smallest instance id only. |
| `MIN_EVICT_PERCENT` | `NUMBER` | Percentage of `streams_pool` memory beyond which sharded queue subshard eviction is triggered |
| `LAST_AVG_CACHED_HORIZON` | `NUMBER` | Last average number of cached subshards seen in sharded queue memory manager horizon |
| `LAST_AVG_MEMORY_HORIZON` | `NUMBER` | Last average memory of cached subshards seen in sharded queue memory manager horizon |
| `LAST_AVG_SUBSHARD_HORIZON` | `NUMBER` | Last average number of subshards seen in sharded queue memory manager horizon |
| `LAST_LEEWAY_SHIFT` | `NUMBER` | Internal leeway for memory threshold |
| `AVG_OPTTIME_DRIFT` | `NUMBER` | Average drift of opt\_time for all subshards. A drift is defined as a difference between opt\_time as set on a subshard and the actual time at which subshard is first dequeueed after prefetch/uneviction. |
| `NUM_THRESHOLD_DRIFT` | `NUMBER` | Number of times drift value has gone over threshold time. A typical threshold time can be horizon\_time/2. |
| `MAX_OPT_TIME_DRIFT` | `NUMBER` | Maximum drift till now |
| `MIN_OPT_TIME_DRIFT` | `NUMBER` | Minimum drift till now |
| `AVG_OPT_TIME_ERROR` | `NUMBER` | An opt\_time error occurs when a cached subshard is unevicted by a foreground process (instead of being prefetched by the aq background). Thus, opt\_time error is the difference between the actual opt\_time set for a sharded queue subshard and the absolute time at which foreground unevicts the same subshard. This column represents average time of this error. |
| `MAX_OPT_TIME_ERROR` | `NUMBER` | Maximum opt\_time error |
| `MIN_OPT_TIME_ERROR` | `NUMBER` | Minimum opt\_time error |
| `NUM_FG_RELOADED` | `NUMBER` | Number of subshards reloaded from disk into message cache by foreground processes |
| `NUM_PRERELOADED` | `NUMBER` | Number of subshards reloaded from disk into message cache in advance by background processes |
| `AVG_RELOAD_TIME` | `NUMBER` | Average time to reload a subshard from disk into message cache (in milliseconds) |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |