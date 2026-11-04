---
title: ALL_QUEUE_SUBSCRIBERS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2017.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_QUEUE_SUBSCRIBERS` displays the list of subscribers that the current user has privilege to dequeue from.

Related Views

- `DBA_QUEUE_SUBSCRIBERS` displays the list of subscribers on all queues in the database.
- `USER_QUEUE_SUBSCRIBERS` displays the list of subscribers on queues that are under the current user's schema. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the queue |
| `QUEUE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the queue |
| `QUEUE_TABLE` | `VARCHAR2(30)` | `NOT NULL` | Name of the queue table on which the queue is defined |
| `CONSUMER_NAME` | `VARCHAR2(30)` |  | Name of the subscriber |
| `ADDRESS` | `VARCHAR2(1024)` |  | Address of the subscriber |
| `PROTOCOL` | `NUMBER` |  | Protocol of the subscriber |
| `TRANSFORMATION` | `VARCHAR2(61)` |  | Transformation for the subscriber |
| `RULE` | `CLOB` |  | Rule condition for the subscriber |
| `DELIVERY_MODE` | `VARCHAR2(22)` |  | Message delivery mode for the subscriber: |
| `IF_NONDURABLE_SUBSCRIBER` | `VARCHAR2(24)` |  | Indicates whether the subscriber is a non-durable subscriber (`YES`) or not (`NO`) |
| `QUEUE_TO_QUEUE` | `VARCHAR2(5)` |  | Indicates whether the subscriber is a queue-to-queue subscriber (`TRUE`) or not (`FALSE`) |