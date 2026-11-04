---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/V-AQ_SHARDED_SUBSCRIBER_STAT.html
tags:
  - oracle
  - 12c
  - reference
---

`V$AQ_SHARDED_SUBSCRIBER_STAT` displays basic statistical information about the subscribers of sharded queues. There is one row per queue per shard per subscriber.

| Column | Datatype | Description |
| --- | --- | --- |
| `QUEUE_ID` | `NUMBER` | Queue identifier |
| `SUBSCRIBER_ID` | `NUMBER` | Subscriber identifier |
| `SHARD_ID` | `NUMBER` | Shard identifier |
| `PRIORITY` | `NUMBER` | Priority value of the shard |
| `DEQUEUE_SUBSHARD` | `NUMBER` | Last known dequeue position in this shard |
| `ENQUEUED_MSGS` | `NUMBER` | Number of enqueued messages |
| `DEQUEUED_MSGS` | `NUMBER` | Number of dequeued messages |
| `ELAPSED_DEQUEUE_TIME` | `NUMBER` | Amount of time spent performing dequeues (in seconds) |
| `CPU_DEQUEUE_TIME` | `NUMBER` | Actual amount of CPU time spent performing dequeues (in seconds) |
| `DEQUEUE_RATE` | `NUMBER` | Number of messages dequeued per second |
| `TIME_SINCE_LAST_DEQUEUE` | `NUMBER` | Time since last dequeue activity (in seconds) |
| `ESTD_TIME_TO_DRAIN` | `NUMBER` | Estimated amount of time to drain the shard (in seconds) with current enqueue and dequeue rates. Null, if the enqueue rate is greater than the dequeue rate. |
| `ESTD_TIME_TO_DRAIN_NO_ENQ` | `NUMBER` | Estimated amount of time to drain the shard (in seconds) with no new enqueues |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

Note:

This view is available starting with Oracle Database 12c Release 2 (12.2.0.1).