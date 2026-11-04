---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/V-PERSISTENT_QUEUES.html
tags:
  - oracle
  - 12c
  - reference
---

`V$PERSISTENT_QUEUES` displays information about all active persistent queues in the database since the queues' first activity time. There is one row per queue. The rows are deleted when the database (or instance in an Oracle RAC environment) restarts.

| Column | Datatype | Description |
| --- | --- | --- |
| `QUEUE_ID` | `NUMBER` | Identifier for the queue |
| `QUEUE_TABLE_ID` | `NUMBER` | Queue table identifier |
| `QUEUE_SCHEMA` | `VARCHAR2(128)` | Owner of the queue |
| `QUEUE_NAME` | `VARCHAR2(128)` | Name of the queue |
| `FIRST_ACTIVITY_TIME` | `TIMESTAMP(6)` | First queue activity time since database startup |
| `ENQUEUED_MSGS` | `NUMBER` | Number of messages enqueued |
| `DEQUEUED_MSGS` | `NUMBER` | Number of messages dequeued  Note: This column will not be incremented until all the subscribers of the message have dequeued the message and its retention time has elapsed. |
| `BROWSED_MSGS` | `NUMBER` | Number of messages that have been browsed |
| `ELAPSED_ENQUEUE_TIME` | `NUMBER` | Total time (in hundredths of a second) spent doing enqueue |
| `ELAPSED_DEQUEUE_TIME` | `NUMBER` | Total time (in hundredths of a second) spent doing dequeue |
| `ENQUEUE_CPU_TIME` | `NUMBER` | Total CPU time for enqueue (in hundredths of a second) |
| `DEQUEUE_CPU_TIME` | `NUMBER` | Total CPU time for dequeue (in hundredths of a second) |
| `AVG_MSG_AGE` | `NUMBER` | Average age of messages in the queue |
| `DEQUEUED_MSG_LATENCY` | `NUMBER` | Last dequeued message latency (in seconds) |
| `ELAPSED_TRANSFORMATION_TIME` | `NUMBER` | Total time (in hundredths of a second) spent doing transformation |
| `ELAPSED_RULE_EVALUATION_TIME` | `NUMBER` | Total time (in hundredths of a second) spent doing rule evaluation |
| `ENQUEUED_EXPIRY_MSGS` | `NUMBER` | Number of messages enqueued with expiry |
| `ENQUEUED_DELAY_MSGS` | `NUMBER` | Number of messages enqueued with delay |
| `MSGS_MADE_EXPIRED` | `NUMBER` | Number of messages expired by time manager |
| `MSGS_MADE_READY` | `NUMBER` | Number of messages made ready by time manager |
| `LAST_ENQUEUE_TIME` | `TIMESTAMP(6)` | Last message enqueue time |
| `LAST_DEQUEUE_TIME` | `TIMESTAMP(6)` | Last message dequeue time |
| `LAST_TM_EXPIRY_TIME` | `TIMESTAMP(6)` | Last time message was expired by time manager |
| `LAST_TM_READY_TIME` | `TIMESTAMP(6)` | Last time message was made ready by time manager |
| `ENQUEUE_TRANSACTIONS` | `NUMBER` | Number of enqueue transactions |
| `DEQUEUE_TRANSACTIONS` | `NUMBER` | Number of dequeue transactions |
| `EXECUTION_COUNT` | `NUMBER` | Number of executions of the dequeue cursor |
| `OLDEST_MSGID` | `RAW(16)` | Message ID of the oldest message in the queue |
| `OLDEST_MSG_ENQTM` | `TIMESTAMP(6)` | Enqueue time of the oldest message in the queue |
| `MANDATORY_AFF_SWITCHES_OUT` | `NUMBER` | An affinity switch is a change in dequeue instance for a shard-subscriber pair. A mandatory affinity switch is when there are local enqueues in the queue at the instance but no local dequeues present, so the dequeue affinity is switched to another instance for that shard-subscriber pair. This column shows the number of times mandatory affinity switches were needed from this instance to another for this queue.  This column is available starting with Oracle Database 12c Release 2 (12.2.0.1). |
| `OPTIONAL_AFF_SWITCHES_OUT` | `NUMBER` | Optional affinity switches are affinity switches that are not mandatory. Optional affinity switches are done for global load balancing across the Oracle Real Application Clusters (Oracle RAC) database. This column shows the number of times optional affinity switches were needed from this instance to another for this queue.  This column is available starting with Oracle Database 12c Release 2 (12.2.0.1). |
| `AFF_SWITCHES_BACK_IN` | `NUMBER` | The number of times dequeue affinities have come back from other instances to this instance. (`MANDATORY_AFF_SWITCHES_OUT` + `OPTIONAL_AFF_SWITCHES_OUT` - `AFF_SWITCHES_BACK_IN`) is the number of cross instance affinities present across all shard-subscriber pair for shards owned by this instance for this queue.  This column is available starting with Oracle Database 12c Release 2 (12.2.0.1). |
| `CROSS_STREAM_JOBS` | `NUMBER` | The number of times a shard is being forwarded to another instance due to cross instance dequeues for this queue  This column is available starting with Oracle Database 12c Release 2 (12.2.0.1). |
| `RESTORE_BITMAP_JOBS` | `NUMBER` | The number of times subscribers used existing shard forwarding to have cross instance dequeues for this queue  This column is available starting with Oracle Database 12c Release 2 (12.2.0.1). |
| `SHADOW_AFF_SWITCHES_IN` | `NUMBER` | The number of affinity switches for this queue where this instance is the dequeue instance for a shard-subscriber pair where the shard is being enqueued at another instance  This column is available starting with Oracle Database 12c Release 2 (12.2.0.1). |
| `SHADOW_AFF_SWITCHES_OUT` | `NUMBER` | The number of affinity switches for this queue where shadow affinity is switched back to source instance of the shard. (`SHADOW_AFF_SWITCHES_IN` - `SHADOW_AFF_SWITCHES_OUT`) is the number of dequeue affinities which are performing cross instance dequeues from non-local shards.  This column is available starting with Oracle Database 12c Release 2 (12.2.0.1). |
| `SHADOW_SHARDS_RECEIVED` | `NUMBER` | The number of times a shard is being forwarded from another instance to this instance due to cross instance dequeues for this queue  This column is available starting with Oracle Database 12c Release 2 (12.2.0.1). |
| `SHADOW_SHARDS_FREED` | `NUMBER` | The number of times a forwarded shard to this instance was stopped due to removal of cross instance dequeues for this queue  This column is available starting with Oracle Database 12c Release 2 (12.2.0.1). |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

Note:

This view does not display accurate information about sharded queues.