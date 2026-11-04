---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-EQ_MESSAGE_CACHE_ADVICE.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.207 V$EQ\_MESSAGE\_CACHE\_ADVICE

`V$EQ_MESSAGE_CACHE_ADVICE` shows simulated metrics for a range of potential message cache sizes for Transactional Event Queues (TEQs). This view assists in cache sizing by providing information in the form of metrics as described below.

| Column | Datatype | Description |
| --- | --- | --- |
| `SIZE_FOR_ESTIMATE` | `NUMBER` | Cache size for simulation (in megabytes) |
| `SIZE_FACTOR` | `NUMBER` | Size factor with respect to the current cache size |
| `ESTD_SIZE_TYPE` | `VARCHAR2(9)` | Possible values:  - `MINIMUM`: This cache size is required to have all dequeues in-memory (no uncached). - `CURRENT`: This is the current size of the message cache. - `MAXIMUM`: This cache size is required to have zero evictions. - `NULL`: This is the value in all other cases. |
| `ESTD_CACHED_PARTITIONS` | `NUMBER` | Estimated number of cached event stream partitions for this size |
| `ESTD_UNCACHED_PARTITIONS` | `NUMBER` | Estimated number of uncached event stream partitions for this size |
| `ESTD_EVICTIONS` | `NUMBER` | Estimated number of event stream partitions evicted for this size |
| `ESTD_EVICTION_RATE` | `NUMBER` | Estimated number of event stream partitions getting evicted per minute |
| `ESTD_FG_UNEVICTIONS` | `NUMBER` | Estimated number of event stream partitions unevicted by foreground processes |
| `ESTD_FG_UNEVICTION_RATE` | `NUMBER` | Estimated number of event stream partitions getting unevicted by foreground processes |
| `ESTD_BG_UNEVICTIONS` | `NUMBER` | Estimated number of event stream partitions unevicted by background processes |
| `ESTD_BG_UNEVICTION_RATE` | `NUMBER` | Estimated number of event stream partitions getting unevicted by background processes |
| `ESTD_BG_PROCESSES` | `NUMBER` | Estimated number of background processes required for this size |
| `TOTAL_ENQUEUE_RATE` | `NUMBER` | Simulated number of messages being enqueued per second |
| `TOTAL_DEQUEUE_RATE` | `NUMBER` | Simulated number of messages being dequeued per second |
| `AVG_PARTITION_SIZE` | `NUMBER` | Simulated average number of messages per cached event stream partitions |
| `AVG_PARTITION_MEMORY` | `NUMBER` | Simulated average memory per cached event stream partition (in megabytes) |
| `AVG_EVICTION_TIME` | `NUMBER` | Simulated average time to evict a cached event stream partition (in milliseconds) |
| `AVG_UNEVICTION_TIME` | `NUMBER` | Simulated average time to unevict a cached event stream partition (in milliseconds) |
| `FLAGS` | `NUMBER` | Reserved for internal use |
| `SIMULATION_TIME` | `NUMBER` | Amount of time that was simulated for (in minutes) |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

Note:

This view is available starting with Oracle Database 21c.

See Also:

[Oracle Database Advanced Queuing User's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADQUE0100) for more information about Oracle Transactional Event Queues and Advanced Queuing