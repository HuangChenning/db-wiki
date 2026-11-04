---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-BUFFERED_PUBLISHERS.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.115 V$BUFFERED\_PUBLISHERS

`V$BUFFERED_PUBLISHERS` displays information about all buffered publishers in the instance.

There is one row per queue per sender. The values are reset to zero when the database (or instance in an Oracle RAC environment) restarts.

| Column | Datatype | Description |
| --- | --- | --- |
| `QUEUE_ID` | `NUMBER` | Identifier for the queue |
| `QUEUE_SCHEMA` | `VARCHAR2(128)` | Owner of the queue |
| `QUEUE_NAME` | `VARCHAR2(128)` | Name of the queue |
| `SENDER_NAME` | `VARCHAR2(128)` | Name of the agent enqueuing the message (the Streams name assigned for a capture process) |
| `SENDER_ADDRESS` | `VARCHAR2(1024)` | Queue name and database name of the source (last propagating) queue; database name is not specified if the source queue is in the local database |
| `SENDER_PROTOCOL` | `NUMBER` | Protocol used by the sender's address |
| `NUM_MSGS` | `NUMBER` | Current number of messages that have yet to be dequeued from the buffer queue |
| `CNUM_MSGS` | `NUMBER` | Cumulative total number of messages enqueued into the buffered queue since the database last started |
| `LAST_ENQUEUED_MSG` | `NUMBER` | Most recently enqueued message identifier |
| `UNBROWSED_MSGS` | `NUMBER` | Number of messages that have been enqueued but not browsed |
| `OVERSPILLED_MSGS` | `NUMBER` | Number of messages that have been spilled but not browsed |
| `MEMORY_USAGE` | `NUMBER` | Percentage of the Streams pool that is being used (or `0` if there is no Streams pool) |
| `ELAPSED_ENQUEUE_TIME` | `NUMBER` | Total time spent in enqueue (in hundredths of a second) |
| `ENQUEUE_CPU_TIME` | `NUMBER` | Total CPU time for enqueue (in hundredths of a second) |
| `LAST_ENQUEUE_TIME` | `TIMESTAMP(3) WITH TIME ZONE` | Last message enqueue time |
| `PUBLISHER_STATE` | `VARCHAR2(59)` | State of the publisher:  - `IN FLOW CONTROL: TOO MANY UNBROWSED MESSAGES` - `IN FLOW CONTROL: OVERSPILLED MESSAGES` - `IN FLOW CONTROL: INSUFFICIENT MEMORY AND UNBROWSED MESSAGES` - `PUBLISHING MESSAGES` - Normal |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |