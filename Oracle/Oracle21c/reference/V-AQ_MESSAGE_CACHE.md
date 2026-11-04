---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-AQ_MESSAGE_CACHE.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.24 V$AQ\_MESSAGE\_CACHE

`V$AQ_MESSAGE_CACHE` provides performance statistics of the message cache for sharded queues at the subshard level in the instance.

Note:

AQ sharded queues are deprecated in Oracle Database 21c. Oracle recommends that you instead use Transactional Event Queues (TEQs) for higher throughput and better performance.

| Column | Datatype | Description |
| --- | --- | --- |
| `QUEUE_ID` | `NUMBER` | Queue ID |
| `SHARD_ID` | `NUMBER` | Shard ID |
| `PRIORITY` | `NUMBER` | Priority of the subshard for dequeue, range `0-9` |
| `SUBSHARD_ID` | `NUMBER` | Subshard ID in the shard |
| `PARTITION_ID` | `NUMBER` | Partition id for the particular subshard |
| `MAX_MSGS` | `NUMBER` | Maximum number of messages of subshard |
| `ENQUEUED_MSGS` | `NUMBER` | Number of messages enqueued for the subshard |
| `MSGS_MADE_EXPIRED` | `NUMBER` | Number of messages made expired |
| `CHUNK_SIZE` | `NUMBER` | The size of the memory chunk for storing messages |
| `NUM_CHUNKS` | `NUMBER` | Number of chunks for the subshard |
| `NUM_FREE_CHUNKS` | `NUMBER` | Number of free chunks for the subshard |
| `USED_MEMORY_SIZE` | `NUMBER` | Total estimated size of memory in use (in bytes) for the subshard |
| `STATE` | `VARCHAR2(13)` | Subshard state. Possible values:  - `CACHED` (in memory) - `UNCACHED` (on disk) - `UNCACHED_FREE` - `CACHED_FREE` - `UNKNOWN` |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

[Oracle Database Advanced Queuing User's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADQUE0100) for more information about Oracle Database Advanced Queueing