---
title: ALL_QUEUES
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2019.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_QUEUES` describes all queues on which the current user has enqueue or dequeue privileges. If the user has any Advanced Queuing system privileges, like `MANAGE ANY QUEUE`, `ENQUEUE ANY QUEUE` or `DEQUEUE ANY QUEUE`, then this view describes all queues in the database.

Related Views

- `DBA_QUEUES` describes all queues in the database.
- `USER_QUEUES` describes the operational characteristics of every queue owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the queue |
| `NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the queue |
| `QUEUE_TABLE` | `VARCHAR2(30)` | `NOT NULL` | Name of the table the queue data resides in |
| `QID` | `NUMBER` | `NOT NULL` | Object number of the queue |
| `QUEUE_TYPE` | `VARCHAR2(20)` |  | Type of the queue: - `EXCEPTION_QUEUE` - `NON_PERSISTENT_QUEUE` - `NORMAL_QUEUE` |
| `MAX_RETRIES` | `NUMBER` |  | Maximum number of retries allowed when dequeuing from the queue |
| `RETRY_DELAY` | `NUMBER` |  | Time interval between retries |
| `ENQUEUE_ENABLED` | `VARCHAR2(7)` |  | Indicates whether the queue is enabled for enqueue (`YES`) or not (`NO`) |
| `DEQUEUE_ENABLED` | `VARCHAR2(7)` |  | Indicates whether the queue is enabled for dequeue (`YES`) or not (`NO`) |
| `RETENTION` | `VARCHAR2(40)` |  | Time interval (in seconds) processed messages are retained in the queue, or `FOREVER` |
| `USER_COMMENT` | `VARCHAR2(50)` |  | User specified comment |
| `NETWORK_NAME` | `VARCHAR2(512)` |  | Network name |

See Also:

[Oracle Streams Advanced Queuing User's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e11013/toc.htm) for more information about these views and Advanced Queuing