---
title: "V$PERSISTENT_PUBLISHERS"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2090.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$PERSISTENT_PUBLISHERS` displays information about all active publishers of the persistent queues in the database. There is one row per instance per queue per publisher. The rows are deleted when the database (or instance in an Oracle RAC environment) restarts.

| Column | Datatype | Description |
| --- | --- | --- |
| `QUEUE_ID` | `NUMBER` | Identifier for the queue |
| `QUEUE_SCHEMA` | `VARCHAR2(30)` | Owner of the queue |
| `QUEUE_NAME` | `VARCHAR2(30)` | Name of the queue |
| `PUBLISHER_NAME` | `VARCHAR2(30)` | Name of the agent enqueuing the message |
| `PUBLISHER_ADDRESS` | `VARCHAR2(1024)` | Address of the publisher agent |
| `PROTOCOL` | `NUMBER` | Protocol used by the publisher's address |
| `ENQUEUED_MSGS` | `NUMBER` | Number of messages that have been enqueued |
| `ELAPSED_ENQUEUE_TIME` | `NUMBER` | Total time spent doing enqueue (in hundredths of a second) |
| `ENQUEUE_CPU_TIME` | `NUMBER` | Total CPU time for enqueue (in hundredths of a second) |
| `LAST_ENQUEUE_TIME` | `TIMESTAMP(6)` | Last enqueue message timestamp |
| `ENQUEUE_TRANSACTIONS` | `NUMBER` | Number of enqueue transactions |