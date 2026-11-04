---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/V-AQ_REMOTE_DEQUEUE_AFFINITY.html
tags:
  - oracle
  - 12c
  - reference
---

`V$AQ_REMOTE_DEQUEUE_AFFINITY` lists the dequeue affinity instance of the subscribers not dequeuing locally from the shard's owner instance. Cross instance message forwarding is used for these subscribers.

| Column | Datatype | Description |
| --- | --- | --- |
| `QUEUE_ID` | `NUMBER` | Queue ID |
| `SHARD_ID` | `NUMBER` | Shard ID which is being forwarded from SOURCE\_INSTANCE to INST\_ID for the subscriber |
| `SOURCE_INSTANCE_ID` | `NUMBER` | Owner instance ID from where the shard is being forwarded |
| `SUBSCRIBER_ID` | `NUMBER` | Subscriber ID |
| `QUEUE_SCHEMA` | `VARCHAR2(128)` | Queue schema name |
| `QUEUE_NAME` | `VARCHAR2(128)` | Queue name |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

Note:

This view is available starting with Oracle Database 12c Release 2 (12.2.0.1).