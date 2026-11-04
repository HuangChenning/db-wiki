---
title: ALL_DEQUEUE_QUEUES
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1070.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_DEQUEUE_QUEUES` describes all queues on which the current user has dequeue privileges. If the user has any Advanced Queuing system privileges, such as `DEQUEUE ANY QUEUE` or `MANAGE ANY QUEUE`, then this view describes all queues in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the queue |
| `NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the queue |
| `QUEUE_TABLE` | `VARCHAR2(30)` | `NOT NULL` | Name of the table in which the queue data resides |
| `QID` | `NUMBER` | `NOT NULL` | Object number of the queue |
| `QUEUE_TYPE` | `VARCHAR2(20)` |  | Type of the queue: - `EXCEPTION_QUEUE` - `NORMAL_QUEUE` |
| `MAX_RETRIES` | `NUMBER` |  | Maximum number of retries allowed when dequeuing from the queue |
| `RETRY_DELAY` | `NUMBER` |  | Time interval between retries |
| `ENQUEUE_ENABLED` | `VARCHAR2(7)` |  | Indicates whether the queue is enabled for enqueue ( `YES` ) or not ( `NO` ) |
| `DEQUEUE_ENABLED` | `VARCHAR2(7)` |  | Indicates whether the queue is enabled for dequeue ( `YES` ) or not ( `NO` ) |
| `RETENTION` | `VARCHAR2(40)` |  | Time interval that processed messages are retained in the queue, or `FOREVER` |
| `USER_COMMENT` | `VARCHAR2(50)` |  | User-specified comment |
| `NETWORK_NAME` | `VARCHAR2(512)` |  | Network name of the queue service |