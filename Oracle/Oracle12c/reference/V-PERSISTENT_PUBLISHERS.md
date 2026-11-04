---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/V-PERSISTENT_PUBLISHERS.html
tags:
  - oracle
  - 12c
  - reference
---

There is one row per instance per queue per publisher. The rows are deleted when the database (or instance in an Oracle RAC environment) restarts.

| Column | Datatype | Description |
| --- | --- | --- |
| `QUEUE_ID` | `NUMBER` | Identifier for the queue |
| `QUEUE_SCHEMA` | `VARCHAR2(128)` | Owner of the queue |
| `QUEUE_NAME` | `VARCHAR2(128)` | Name of the queue |
| `PUBLISHER_NAME` | `VARCHAR2(128)` | Name of the agent enqueuing the message |
| `PUBLISHER_ADDRESS` | `VARCHAR2(1024)` | Address of the publisher agent |
| `PROTOCOL` | `NUMBER` | Protocol used by the publisher's address |
| `ENQUEUED_MSGS` | `NUMBER` | Number of messages that have been enqueued |
| `ELAPSED_ENQUEUE_TIME` | `NUMBER` | Total time spent doing enqueue (in hundredths of a second) |
| `ENQUEUE_CPU_TIME` | `NUMBER` | Total CPU time for enqueue (in hundredths of a second) |
| `LAST_ENQUEUE_TIME` | `TIMESTAMP(6)` | Last enqueue message timestamp |
| `ENQUEUE_TRANSACTIONS` | `NUMBER` | Number of enqueue transactions |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |