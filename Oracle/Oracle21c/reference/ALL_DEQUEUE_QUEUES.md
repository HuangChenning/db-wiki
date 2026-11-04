---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_DEQUEUE_QUEUES.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.166 ALL\_DEQUEUE\_QUEUES

`ALL_DEQUEUE_QUEUES` describes all queues on which the current user has dequeue privileges. If the user has any Advanced Queuing system privileges, such as `DEQUEUE ANY QUEUE` or `MANAGE ANY QUEUE`, then this view describes all queues in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the queue |
| `NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the queue |
| `QUEUE_TABLE` | `VARCHAR2(128)` | `NOT NULL` | Name of the table in which the queue data resides |
| `QID` | `NUMBER` | `NOT NULL` | Object number of the queue |
| `QUEUE_TYPE` | `VARCHAR2(20)` |  | Type of the queue. Possible values:  - `EXCEPTION_QUEUE` - `NORMAL_QUEUE` |
| `MAX_RETRIES` | `NUMBER` |  | Maximum number of retries allowed when dequeuing from the queue |
| `RETRY_DELAY` | `NUMBER` |  | Time interval between retries |
| `ENQUEUE_ENABLED` | `VARCHAR2(7)` |  | Indicates whether the queue is enabled for enqueue (`  YES  `) or not (`  NO  `) |
| `DEQUEUE_ENABLED` | `VARCHAR2(7)` |  | Indicates whether the queue is enabled for dequeue (`  YES  `) or not (`  NO  `) |
| `RETENTION` | `VARCHAR2(40)` |  | Time interval that processed messages are retained in the queue, or `FOREVER` |
| `USER_COMMENT` | `VARCHAR2(50)` |  | User-specified comment |
| `NETWORK_NAME` | `VARCHAR2(512)` |  | Network name of the queue service |
| `SHARDED` | `VARCHAR2(5)` |  | `TRUE` if the queue is sharded, `FALSE` otherwise |
| `QUEUE_CATEGORY` <sup>Foot 1</sup> | `VARCHAR2(25)` |  | Queue category. Possible values:  - `Classic Queue` - `Sharded Queue` - `Transactional Event Queue` |
| `RECIPIENTS` <sup>Foot 1</sup> | `VARCHAR2(8)` |  | `SINGLE` or `MULTIPLE` recipients |

<sup>Footnote 1</sup> This column is available starting with Oracle Database 21c.