---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-AQ_CROSS_INSTANCE_JOBS.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.19 V$AQ\_CROSS\_INSTANCE\_JOBS

`V$AQ_CROSS_INSTANCE_JOBS` describes each of the cross process jobs.

Each job serves to forward messages for a shard from a source instance to a destination instance for a set of subscribers of a sharded queue.

Note:

AQ sharded queues are deprecated in Oracle Database 21c. Oracle recommends that you instead use Transactional Event Queues (TEQs) for higher throughput and better performance.

| Column | Datatype | Description |
| --- | --- | --- |
| `JOB_ID` | `NUMBER` | Job ID within this coordinator |
| `SCHEMA_NAME` | `VARCHAR2(128)` | Source schema of the job |
| `QUEUE_NAME` | `VARCHAR2(128)` | Source queue name of the cross job |
| `SHARD_ID` | `NUMBER` | Source shard ID |
| `START_SUBSHARD_ID` | `NUMBER` | Start subshard ID of the job |
| `DESTINATION_INSTANCE_ID` | `NUMBER` | Destination instance of the cross job |
| `COORDINATOR_ID` | `NUMBER` | Index of the coordinator serving the job |
| `DEST_SERVER_PROCESS_ID` | `NUMBER` | Process ID of the destination server |
| `JOB_STATE` | `VARCHAR2(28)` | State of the job:  - `REQUESTED` - `RUNNING` - `STOPPED` - `PAUSED` - `CRASHED` - `INACTIVE` |
| `FLOW_CONTROL` | `NUMBER` | Indicates whether the job is flow controlled:  - `0` - The job is not flow controlled - `1` - The job is flow controlled |
| `MSGS_SENT` | `NUMBER` | Messages sent during the job |
| `BYTES_SENT` | `NUMBER` | Bytes sent during the job |
| `ACK_LATENCY` | `NUMBER` | Latency for receiving ACK for the job |
| `JOB_TYPE` | `VARCHAR2(26)` | Cross instance job type. Values:  - `CROSS_STREAM` 	: This job type is responsible for forwarding a shard from its owner instance to a destination dequeue instance for all subscribers performing dequeue from that shard at the destination dequeue instance. - `DEQUEUE_AFFINITY_TO_REMOTE`: This job type is responsible for switching a subscriber's dequeue affinity from a shard's owner instance to a remote dequeue instance. - `DEQUEUE_AFFINITY_TO_LOCAL`: This job type is responsible for switching back a subscriber's dequeue affinity from a remote dequeue instance to a shard's owner instance. |
| `PRIORITY0_CROSS_LWM` | `NUMBER` | Last priority 0 subshard received at `DESTINATION_INSTANCE_ID` |
| `PRIORITY1_CROSS_LWM` | `NUMBER` | Last priority 1 subshard received at `DESTINATION_INSTANCE_ID` |
| `PRIORITY2_CROSS_LWM` | `NUMBER` | Last priority 2 subshard received at `DESTINATION_INSTANCE_ID` |
| `PRIORITY3_CROSS_LWM` | `NUMBER` | Last priority 3 subshard received at `DESTINATION_INSTANCE_ID` |
| `PRIORITY4_CROSS_LWM` | `NUMBER` | Last priority 4 subshard received at `DESTINATION_INSTANCE_ID` |
| `PRIORITY5_CROSS_LWM` | `NUMBER` | Last priority 5 subshard received at `DESTINATION_INSTANCE_ID` |
| `PRIORITY6_CROSS_LWM` | `NUMBER` | Last priority 6 subshard received at `DESTINATION_INSTANCE_ID` |
| `PRIORITY7_CROSS_LWM` | `NUMBER` | Last priority 7 subshard received at `DESTINATION_INSTANCE_ID` |
| `PRIORITY8_CROSS_LWM` | `NUMBER` | Last priority 8 subshard received at `DESTINATION_INSTANCE_ID` |
| `PRIORITY9_CROSS_LWM` | `NUMBER` | Last priority 9 subshard received at `DESTINATION_INSTANCE_ID` |
| `JOB_START_TIME` | `TIMESTAMP(3) WITH TIME ZONE` | Start time of this job |
| `SUBSCRIBER_ID` | `NUMBER` | Subscriber ID whose affinity is being switched for the `DEQUEUE_AFFINITY_TO_REMOTE` and `DEQUEUE_AFFINITY_TO_LOCAL` job types |
| `SUBSCRIBER_NAME` | `VARCHAR2(512)` | Subscriber name whose affinity is being switched for the `DEQUEUE_AFFINITY_TO_REMOTE` and `DEQUEUE_AFFINITY_TO_LOCAL` job types. This column is `NULL` for the `CROSS_STREAM` job type. |
| `OWNER_INSTANCE_ID` | `NUMBER` | Owner instance of the shard |
| `QUEUE_ID` | `NUMBER` | Queue ID |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

[Oracle Database Advanced Queuing User's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADQUE0100) for more information about Oracle Database Advanced Queueing