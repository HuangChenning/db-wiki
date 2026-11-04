---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-EQ_NONDUR_SUBSCRIBER.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.209 V$EQ\_NONDUR\_SUBSCRIBER

`V$EQ_NONDUR_SUBSCRIBER` provides information about the non-durable subscriptions on Transactional Event Queues (TEQs).

| Column | Datatype | Description |
| --- | --- | --- |
| `QUEUE_ID` | `NUMBER` | Queue ID |
| `SUBSCRIBER_ID` | `NUMBER` | ID of the non-durable subscriber |
| `SUBSCRIBER_NAME` | `VARCHAR2(128)` | Subscriber name |
| `RULE_CONDITION` | `VARCHAR2(4000)` | Rule condition of the subscriber |
| `TRANSFORMATION_OWNER` | `VARCHAR2(128)` | Owner of the transformation (for JMS queues) |
| `TRANSFORMATION_NAME` | `VARCHAR2(128)` | Name of the transformation (for JMS queues) |
| `CREATION_TIME` | `TIMESTAMP(1) WITH TIME ZONE` | Non-durable subscriber creation time |
| `FLAGS` | `NUMBER` | Property of the subscriber. Possible values:  - `0x0001` – Persistent subscriber - `0x0002` – Buffered subscriber - `0x0004` – JMS subscriber - `0x0008` – Rule-based subscriber - `0x0010` – Subscriber has transformation - `0x0020` – Notification-only non-durable subscriber 	subscriber |
| `SUBSCRIBER_TYPE` | `NUMBER` | Type of subscriber. Possible values:  - `1` – JMS non-durable subscriber - `2` – Service layer dummy non-durable subscriber - `3` – Notification-only non-durable subscriber |
| `BITPOS` | `NUMBER` | Position of subscriber in subscriber bitmap |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

Note:

This view is available starting with Oracle Database 21c.

See Also:

[Oracle Database Advanced Queuing User's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADQUE0100) for more information about Oracle Transactional Event Queues and Advanced Queuing