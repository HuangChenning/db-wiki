---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-EQ_MESSAGE_CACHE.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.206 V$EQ\_MESSAGE\_CACHE

`V$EQ_MESSAGE_CACHE` provides performance statistics of the message cache for Transactional Event Queues (TEQs) at the event stream partition level in the instance.

| Column | Datatype | Description |
| --- | --- | --- |
| `QUEUE_ID` | `NUMBER` | Queue ID |
| `EVENT_STREAM_ID` | `NUMBER` | Event stream ID |
| `PRIORITY` | `NUMBER` | Priority of the event stream partition for dequeue, range `0` - `9` |
| `EVENT_STREAM_PARTITION_ID` | `NUMBER` | Event stream partition ID |
| `PARTITION_ID` | `NUMBER` | Queue partition ID |
| `MAX_MSGS` | `NUMBER` | Maximum number of messages for the event stream partition |
| `ENQUEUED_MSGS` | `NUMBER` | Number of messages enqueued for the event stream partition |
| `MSGS_MADE_EXPIRED` | `NUMBER` | Number of messages made expired |
| `CHUNK_SIZE` | `NUMBER` | The size of the memory chunk for storing messages |
| `NUM_CHUNKS` | `NUMBER` | Number of chunks for the event stream partition |
| `NUM_FREE_CHUNKS` | `NUMBER` | Number of free chunks for the event stream partition |
| `USED_MEMORY_SIZE` | `NUMBER` | Total estimated size of memory in use (in bytes) for the event stream partition |
| `STATE` | `VARCHAR2(13)` | Event stream partition state. Possible values:  - `CACHED` (in memory) - `UNCACHED` (on disk) - `UNCACHED_FREE` - `CACHED_FREE` - `UNKNOWN` |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

Note:

This view is available starting with Oracle Database 21c.

See Also:

[Oracle Database Advanced Queuing User's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADQUE0100) for more information about Oracle Transactional Event Queues and Advanced Queuing