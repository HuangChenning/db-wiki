---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_QUEUES.html
tags:
  - oracle
  - 21c
  - reference
---

## 4.23 ALL\_QUEUES

If the user has any Advanced Queuing system privileges, like `MANAGE ANY QUEUE`, `ENQUEUE ANY QUEUE` or `DEQUEUE ANY QUEUE`, then this view describes all queues in the database.

Related Views

- `DBA_QUEUES` describes all queues in the database.
- `USER_QUEUES` describes the operational characteristics of every queue owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the queue |
| `NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the queue |
| `QUEUE_TABLE` | `VARCHAR2(128)` | `NOT NULL` | Name of the table the queue data resides in |
| `QID` | `NUMBER` | `NOT NULL` | Object number of the queue |
| `QUEUE_TYPE` | `VARCHAR2(20)` |  | Type of the queue. Possible values:  - `EXCEPTION_QUEUE` - `NON_PERSISTENT_QUEUE` - `NORMAL_QUEUE` |
| `MAX_RETRIES` | `NUMBER` |  | Maximum number of retries allowed when dequeuing from the queue |
| `RETRY_DELAY` | `NUMBER` |  | Time interval between retries |
| `ENQUEUE_ENABLED` | `VARCHAR2(7)` |  | Indicates whether the queue is enabled for enqueue (`YES`) or not (`NO`) |
| `DEQUEUE_ENABLED` | `VARCHAR2(7)` |  | Indicates whether the queue is enabled for dequeue (`YES`) or not (`NO`) |
| `RETENTION` | `VARCHAR2(40)` |  | Time interval (in seconds) processed messages are retained in the queue, or ` FOREVER` |
| `USER_COMMENT` | `VARCHAR2(50)` |  | User specified comment |
| `NETWORK_NAME` | `VARCHAR2(512)` |  | Network name |
| `SHARDED` | `VARCHAR2(5)` |  | `TRUE` if queue is sharded, `FALSE` otherwise |
| `QUEUE_CATEGORY` <sup>Foot 1</sup> | `VARCHAR2(25)` |  | Queue category. Possible values:  - `Classic Queue` - `Sharded Queue` - `Transactional Event Queue` |
| `RECIPIENTS` <sup>Foot 1</sup> | `VARCHAR2(8)` |  | `SINGLE` or `MULTIPLE` recipients |

<sup>Footnote 1</sup> This column is available starting with Oracle Database 21c.

See Also:

- " [DBA\_QUEUES](DBA_QUEUES.md) "
- " [USER\_QUEUES](USER_QUEUES.md) "
- [Oracle Database Advanced Queuing User's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADQUE0100) for more information Advanced Queuing