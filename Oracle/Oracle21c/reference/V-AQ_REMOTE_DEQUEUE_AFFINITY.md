---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-AQ_REMOTE_DEQUEUE_AFFINITY.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.32 V$AQ\_REMOTE\_DEQUEUE\_AFFINITY

`V$AQ_REMOTE_DEQUEUE_AFFINITY` lists the dequeue affinity instance of the subscribers not dequeuing locally from the shard's owner instance. Cross instance message forwarding is used for these subscribers.

Note:

AQ sharded queues are deprecated in Oracle Database 21c. Oracle recommends that you instead use Transactional Event Queues (TEQs) for higher throughput and better performance.

| Column | Datatype | Description |
| --- | --- | --- |
| `QUEUE_ID` | `NUMBER` | Queue ID |
| `SHARD_ID` | `NUMBER` | Shard ID which is being forwarded from SOURCE\_INSTANCE to INST\_ID for the subscriber |
| `SOURCE_INSTANCE_ID` | `NUMBER` | Owner instance ID from where the shard is being forwarded |
| `SUBSCRIBER_ID` | `NUMBER` | Subscriber ID |
| `QUEUE_SCHEMA` | `VARCHAR2(128)` | Queue schema name |
| `QUEUE_NAME` | `VARCHAR2(128)` | Queue name |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |