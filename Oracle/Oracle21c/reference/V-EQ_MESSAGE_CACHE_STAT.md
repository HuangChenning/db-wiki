---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-EQ_MESSAGE_CACHE_STAT.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.208 V$EQ\_MESSAGE\_CACHE\_STAT

`V$EQ_MESSAGE_CACHE_STAT` displays statistics about memory management for Transactional Event Queues (TEQs) in the Streams pool within the System Global Area (SGA). TEQs use the Streams pool in units of event queue partitions. Thus, columns of this view shows statistics at the event queue partition level. This view shows statistics across all TEQs.

| Column | Datatype | Description |
| --- | --- | --- |
| `NUM_EVICTED` | `NUMBER` | Number of evicted event queue partitions across all TEQs |
| `NUM_PREFETCHED` | `NUMBER` | Number of event queue partitions pre-fetched by an AQ background process |
| `NUM_UNEVICTION` | `NUMBER` | Number of event queue partitions unevicted by a foreground process, such as the dequeue process |
| `NUM_UNCACHED` | `NUMBER` | Number of event queue partitions stored as uncached |
| `NUM_TRACKED` | `NUMBER` | Number of event queue partitions which are actively tracking dequeue rates |
| `NUM_CACHED` | `NUMBER` | Number of event queue partitions stored as cached |
| `MAX_SUBSH_SIZE` | `NUMBER` | Maximum event queue partition size seen till now, in terms of number of messages per event queue partition |
| `MIN_SUBSH_SIZE` | `NUMBER` | Minimum event queue partition size seen till now, in terms of number of messages per event queue partition |
| `MEAN_SUBSH_SIZE` | `NUMBER` | Mean event queue partition size seen till now, in terms of number of messages per event queue partition |
| `AVG_EVICTION_RATE` | `NUMBER` | Average number of event queue partitions evicted per second |
| `AVG_LOAD_RATE` | `NUMBER` | Average number of event queue partitions pre-fetched or unevicted per second |
| `AVG_EVICTION_TIME` | `NUMBER` | Average time taken to evict one event queue partition (in milliseconds) |
| `AVG_LOAD_TIME` | `NUMBER` | Average time taken to un-evict one event queue partition (in milliseconds) |
| `AVG_MISS_RATIO` | `NUMBER` | Average ratio of number of foreground un-evictions versus background pre-fetch |
| `AVG_THRASH_RATIO` | `NUMBER` | Average ratio of number of event queue partitions pre-fetched by background without dequeue attempt versus total number of event queue partitions prefetched |
| `MANDATORY_AFF_SWITCH_ATTEMPTS` | `NUMBER` | An affinity switch is a change in dequeue instance for a TEQ-subscriber pair. A mandatory affinity switch is when there are local enqueues in the queue at the instance but no local dequeues present, so the dequeue affinity is switched to another instance for that TEQ-subscriber pair. This column shows the number of times mandatory affinity switches were attempted across all instances. Populated at the smallest instance ID only. |
| `OPTIONAL_AFF_SWITCH_ATTEMPTS` | `NUMBER` | Optional affinity switches are affinity switches that are not mandatory. Optional affinity switches are done for global load balancing across the Oracle Real Application Clusters (Oracle RAC) database. This column shows the number of times optional affinity switches were attempted across all instances. Populated at the smallest instance ID only. |
| `MIN_EVICT_PERCENT` | `NUMBER` | Percentage of `streams_pool` memory beyond which event queue partition eviction is triggered |
| `LAST_AVG_CACHED_HORIZON` | `NUMBER` | Last average number of cached event queue partitions seen in TEQ memory manager horizon |
| `LAST_AVG_MEMORY_HORIZON` | `NUMBER` | Last average memory of cached event queue partitions seen in TEQ memory manager horizon |
| `LAST_AVG_SUBSHARD_HORIZON` | `NUMBER` | Last average number of event queue partitions seen in TEQ memory manager horizon |
| `LAST_LEEWAY_SHIFT` | `NUMBER` | Internal leeway for memory threshold |
| `AVG_OPTTIME_DRIFT` | `NUMBER` | Average drift of opt\_time for all event queue partitions. A drift is defined as a difference between opt\_time as set on an event queue partition and the actual time at which an event queue partition is first dequeueed after prefetch/uneviction. |
| `NUM_THRESHOLD_DRIFT` | `NUMBER` | Number of times drift value has gone over threshold time. A typical threshold time can be horizon\_time/2. |
| `MAX_OPT_TIME_DRIFT` | `NUMBER` | Maximum drift until now |
| `MIN_OPT_TIME_DRIFT` | `NUMBER` | Minimum drift until now |
| `AVG_OPT_TIME_ERROR` | `NUMBER` | An opt\_time error occurs when a cached event queue partition is unevicted by a foreground process (instead of being prefetched by the AQ background). Thus, opt\_time error is the difference between the actual opt\_time set for an event queue partition and the absolute time at which foreground unevicts the same event queue partition. This column represents the average time of this error. |
| `MAX_OPT_TIME_ERROR` | `NUMBER` | Maximum opt\_time error |
| `MIN_OPT_TIME_ERROR` | `NUMBER` | Minimum opt\_time error |
| `NUM_FG_RELOADED` | `NUMBER` | Number of event stream partitions reloaded from disk into message cache by foreground processes |
| `NUM_PRERELOADED` | `NUMBER` | Number of event stream partitions reloaded from disk into message cache in advance by background processes |
| `AVG_RELOAD_TIME` | `NUMBER` | Average time to reload an event stream partition from disk into message cache (in milliseconds) |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

Note:

This view is available starting with Oracle Database 21c.

See Also:

[Oracle Database Advanced Queuing User's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADQUE0100) for more information about Oracle Transactional Event Queues and Advanced Queuing