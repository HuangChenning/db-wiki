---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-EQ_REMOTE_DEQUEUE_AFFINITY.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.212 V$EQ\_REMOTE\_DEQUEUE\_AFFINITY

`V$EQ_REMOTE_DEQUEUE_AFFINITY` lists the for Transactional Event Queue (TEQ) dequeue affinity instance of the subscribers not dequeuing locally from the event streams's owner instance. Cross-instance message forwarding is used for these subscribers.

| Column | Datatype | Description |
| --- | --- | --- |
| `QUEUE_ID` | `NUMBER` | Queue ID |
| `EVENT_STREAM_ID` | `NUMBER` | Event stream ID, which is being forwarded from `SOURCE_INSTANCE` to `INST_ID` for the subscriber |
| `SOURCE_INSTANCE_ID` | `NUMBER` | Owner instance ID from which the event stream is being forwarded |
| `SUBSCRIBER_ID` | `NUMBER` | Subscriber ID |
| `QUEUE_SCHEMA` | `VARCHAR2(128)` | Owner of the queue |
| `QUEUE_NAME` | `VARCHAR2(128)` | Queue name |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

Note:

This view is available starting with Oracle Database 21c.

See Also:

[Oracle Database Advanced Queuing User's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADQUE0100) for more information about Oracle Transactional Event Queues and Advanced Queuing