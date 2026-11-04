---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-AQ_MESSAGE_CACHE_ADVICE.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.25 V$AQ\_MESSAGE\_CACHE\_ADVICE

`V$AQ_MESSAGE_CACHE_ADVICE` shows simulated metrics for a range of potential message cache sizes. This view assists in cache sizing by providing information in the form of metrics as described below.

Note:

AQ sharded queues are deprecated in Oracle Database 21c. Oracle recommends that you instead use Transactional Event Queues (TEQs) for higher throughput and better performance.

| Column | Datatype | Description |
| --- | --- | --- |
| `SIZE_FOR_ESTIMATE` | `NUMBER` | Cache size for simulation (in megabytes) |
| `SIZE_FACTOR` | `NUMBER` | Size factor with respect to the current cache size |
| `ESTD_SIZE_TYPE` | `VARCHAR2(9)` | Possible values:  - `MINIMUM`: This cache size is required to have all dequeues in-memory (no uncached). - `PREFERRED`: This is the smallest message cache size required to eliminate 80% of unevictions that occur with a message cache size of `MINIMUM` for subscribers who keep up, that is, subscribers whose dequeue rate matches the enqueue rate. - `MAXIMUM`: This cache size is required to have zero evictions. - `NULL`: This is the value in all other cases. |
| `ESTD_CACHED_SUBSHARDS` | `NUMBER` | Estimated number of cached subshards for this size |
| `ESTD_UNCACHED_SUBSHARDS` | `NUMBER` | Estimated number of uncached subshards for this size |
| `ESTD_EVICTIONS` | `NUMBER` | Estimated number of subshards evicted for this size |
| `ESTD_EVICTION_RATE` | `NUMBER` | Estimated number of subshards getting evicted per minute |
| `ESTD_FG_UNEVICTIONS` | `NUMBER` | Estimated number of subshards unevicted by foreground processes |
| `ESTD_FG_UNEVICTION_RATE` | `NUMBER` | Estimated number of subshards getting unevicted by foreground processes |
| `ESTD_BG_UNEVICTIONS` | `NUMBER` | Estimated number of subshards unevicted by background processes |
| `ESTD_BG_UNEVICTION_RATE` | `NUMBER` | Estimated number of subshards getting unevicted by background processes |
| `ESTD_BG_PROCESSES` | `NUMBER` | Estimated number of background processes required for this size |
| `TOTAL_ENQUEUE_RATE` | `NUMBER` | Simulated number of messages being enqueued per second |
| `TOTAL_DEQUEUE_RATE` | `NUMBER` | Simulated number of messages being dequeued per second |
| `AVG_SUBSHARD_SIZE` | `NUMBER` | Simulated average number of messages per cached subshard |
| `AVG_SUBSHARD_MEMORY` | `NUMBER` | Simulated average memory per cached subshard (in megabytes) |
| `AVG_EVICTION_TIME` | `NUMBER` | Simulated average time to evict a cached subshard (in milliseconds) |
| `AVG_UNEVICTION_TIME` | `NUMBER` | Simulated average time to unevict a cached subshard (in milliseconds) |
| `FLAGS` | `NUMBER` | Reserved for internal use |
| `SIMULATION_TIME` | `NUMBER` | Amount of time that was simulated for (in minutes) |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |