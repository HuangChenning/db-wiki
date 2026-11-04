---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-AQ_SHARDED_SUBSCRIBER_STAT.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.34 V$AQ\_SHARDED\_SUBSCRIBER\_STAT

`V$AQ_SHARDED_SUBSCRIBER_STAT` displays basic statistical information about the subscribers of sharded queues. There is one row per queue per shard per subscriber.

Note:

AQ sharded queues are deprecated in Oracle Database 21c. Oracle recommends that you instead use Transactional Event Queues (TEQs) for higher throughput and better performance.

| Column | Datatype | Description |
| --- | --- | --- |
| `QUEUE_ID` | `NUMBER` | Queue identifier |
| `SUBSCRIBER_ID` | `NUMBER` | Subscriber identifier |
| `SHARD_ID` | `NUMBER` | Shard identifier |
| `PRIORITY` | `NUMBER` | Priority value of the shard |
| `MSG_SN` | `NUMBER` | Message serial number |
| `DEQUEUE_SUBSHARD` | `NUMBER` | Last known dequeue position in this shard |
| `ENQUEUED_MSGS` | `NUMBER` | Number of enqueued messages |
| `DEQUEUED_MSGS` | `NUMBER` | Number of dequeued messages |
| `ELAPSED_DEQUEUE_TIME` | `NUMBER` | Amount of time spent performing dequeues (in seconds) |
| `CPU_DEQUEUE_TIME` | `NUMBER` | Actual amount of CPU time spent performing dequeues (in seconds) |
| `DEQUEUE_RATE` | `NUMBER` | Number of messages dequeued per second |
| `DEQUEUE_POSITION` <sup>Foot 1</sup> | `RAW(16)` | Message ID at the dequeue position of the subscriber in this shard  A NULL value indicates that either the shard is empty or no dequeues have been done on this shard. |
| `TIME_SINCE_LAST_DEQUEUE` | `NUMBER` | Time since last dequeue activity (in seconds) |
| `ESTD_TIME_TO_DRAIN` | `NUMBER` | Estimated amount of time to drain the shard (in seconds) with current enqueue and dequeue rates. Null, if the enqueue rate is greater than the dequeue rate. |
| `ESTD_TIME_TO_DRAIN_NO_ENQ` | `NUMBER` | Estimated amount of time to drain the shard (in seconds) with no new enqueues |
| `MESSAGE_LATENCY_1` <sup>Foot 1</sup> | `NUMBER` | Message latency within the last 5 minutes (in milliseconds). Null if no message is consumed or it is delay dequeue. |
| `MESSAGE_LATENCY_2` <sup>Foot 1</sup> | `NUMBER` | Message latency within the last 1 hour (in milliseconds). Null if no message is consumed or it is delay dequeue. |
| `MESSAGE_LATENCY_3` <sup>Foot 1</sup> | `NUMBER` | Message latency within the last 5 hours (in milliseconds). Null if no message is consumed or it is delay dequeue. |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

<sup>Footnote 1</sup> This column is available starting with Oracle Database 21c.