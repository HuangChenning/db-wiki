---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_QUEUE_SUBSCRIBERS.html
tags:
  - oracle
  - 21c
  - reference
---

## 4.21 ALL\_QUEUE\_SUBSCRIBERS

`ALL_QUEUE_SUBSCRIBERS` displays the list of subscribers that the current user has privilege to dequeue from.

Related Views

- `DBA_QUEUE_SUBSCRIBERS` displays the list of subscribers on all queues in the database.
- `USER_QUEUE_SUBSCRIBERS` displays the list of subscribers on queues that are under the current user's schema. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the queue |
| `QUEUE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the queue |
| `QUEUE_TABLE` | `VARCHAR2(128)` | `NOT NULL` | Name of the queue table on which the queue is defined |
| `CONSUMER_NAME` | `VARCHAR2(512)` |  | Name of the subscriber |
| `ADDRESS` | `VARCHAR2(1024)` |  | Address of the subscriber |
| `PROTOCOL` | `NUMBER` |  | Protocol of the subscriber |
| `TRANSFORMATION` | `VARCHAR2(61)` |  | Transformation for the subscriber |
| `RULE` | `CLOB` |  | Rule condition for the subscriber |
| `DELIVERY_MODE` | `VARCHAR2(22)` |  | Message delivery mode for the subscriber:  - `PERSISTENT` - `BUFFERED` - `PERSISTENT_OR_BUFFERED` |
| `IF_NONDURABLE_SUBSCRIBER` | `VARCHAR2(3)` |  | Indicates whether the subscriber is a non-durable subscriber (`YES`) or not (`NO`) |
| `QUEUE_TO_QUEUE` | `VARCHAR2(5)` |  | Indicates whether the subscriber is a queue-to-queue subscriber (`TRUE`) or not (`FALSE`) |
| `SUBSCRIBER_ID` | `NUMBER` |  | ID of the subscriber |
| `POS_BITMAP` | `NUMBER` |  | Position of the subscriber in the bitmap |

See Also:

- " [DBA\_QUEUE\_SUBSCRIBERS](DBA_QUEUE_SUBSCRIBERS.md) "
- " [USER\_QUEUE\_SUBSCRIBERS](USER_QUEUE_SUBSCRIBERS.md) "