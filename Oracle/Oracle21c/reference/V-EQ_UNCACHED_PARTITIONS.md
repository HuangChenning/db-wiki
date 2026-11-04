---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-EQ_UNCACHED_PARTITIONS.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.215 V$EQ\_UNCACHED\_PARTITIONS

`V$EQ_UNCACHED_PARTITIONS` describes all uncached Transactional Event Queue (TEQ) event stream partitions.

| Column | Datatype | Description |
| --- | --- | --- |
| `QUEUE_ID` | `NUMBER` | Queue ID |
| `EVENT_STREAM_ID` | `NUMBER` | Event stream ID |
| `PRIORITY` | `NUMBER` | Priority of the event stream partition |
| `EVENT_STREAM_PARTITION_ID` | `NUMBER` | Event stream partition ID |
| `OPT_STATE` | `VARCHAR2(19)` | Current message cache optimizer state of the event stream partition. Possible values:  - `EMPTY` - `READY` - `EVICTION_PROGRESS` - `EVICTED` - `UNEVICTION_PROGRESS` - `PREFETCH_PROGRESS` - `NEED_RELOAD` - `RELOAD_PROGRESS` - `NA`: Error in the message cache optimizer state of the event stream partition |
| `OPT_TIME` | `TIMESTAMP(3) WITH TIME ZONE` | The predicted absolute time when the event stream partition could be accessed in future |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

Note:

This view is available starting with Oracle Database 21c.

See Also:

[Oracle Database Advanced Queuing User's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADQUE0100) for more information about Oracle Transactional Event Queues and Advanced Queuing