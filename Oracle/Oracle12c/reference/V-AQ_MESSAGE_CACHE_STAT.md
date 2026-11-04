---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/V-AQ_MESSAGE_CACHE_STAT.html
tags:
  - oracle
  - 12c
  - reference
---

`V$AQ_MESSAGE_CACHE_STAT` displays statistics about memory management for sharded queues in the Streams pool within the System Global Area (SGA). Sharded queues use the Streams pool in units of subshards. Thus, columns of this view shows statistics at subshard level. This view shows statistics across all sharded queues.

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
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

Note:

This view is available starting with Oracle Database 12c Release 2 (12.2.0.1).