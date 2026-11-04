---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-EQ_CROSS_INSTANCE_JOBS.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.204 V$EQ\_CROSS\_INSTANCE\_JOBS

`V$EQ_CROSS_INSTANCE_JOBS` describes Transactional Event Queue (TEQ) cross-instance jobs.

Each job forwards messages for an event stream from a source instance to a destination instance for a set of subscribers of a TEQ.

| Column | Datatype | Description |
| --- | --- | --- |
| `JOB_ID` | `NUMBER` | Job ID within this coordinator |
| `SCHEMA_NAME` | `VARCHAR2(128)` | Source schema of the job |
| `QUEUE_NAME` | `VARCHAR2(128)` | Source queue name of the job |
| `EVENT_STREAM_ID` | `NUMBER` | Source event stream ID |
| `START_EVENT_STREAM_PARTITION_ID` | `NUMBER` | Start event stream partition ID of the job |
| `DESTINATION_INSTANCE_ID` | `NUMBER` | Destination instance of the job |
| `COORDINATOR_ID` | `NUMBER` | Index of the coordinator serving the job |
| `DEST_SERVER_PROCESS_ID` | `NUMBER` | Process ID of the destination server |
| `JOB_STATE` | `VARCHAR2(28)` | State of the job. Possible values:  - `REQUESTED` - `RUNNING` - `STOPPED` - `PAUSED` - `CRASHED` - `INACTIVE` |
| `FLOW_CONTROL` | `NUMBER` | Indicates whether the job is flow controlled. Possible values:  - `0` - The job is not flow controlled - `1` - The job is flow controlled |
| `MSGS_SENT` | `NUMBER` | Number of messages sent during the job |
| `BYTES_SENT` | `NUMBER` | Number of bytes sent during the job |
| `ACK_LATENCY` | `NUMBER` | Latency for receiving ACK for the job |
| `JOB_TYPE` | `VARCHAR2(26)` | Job type. Possible values:  - `CROSS_STREAM`: This job type is responsible for forwarding an event stream from its owner instance to a destination dequeue instance for all subscribers performing dequeue from that event stream at the destination dequeue instance. - `DEQUEUE_AFFINITY_TO_REMOTE`: This job type is responsible for switching a subscriber's dequeue affinity from an event stream's owner instance to a remote dequeue instance. - `DEQUEUE_AFFINITY_TO_LOCAL`: This job type is responsible for switching back a subscriber's dequeue affinity from a remote dequeue instance to an event stream's owner instance. |
| `PRIORITY0_CROSS_LWM` | `NUMBER` | ID of last priority 0 event stream partition received at `DESTINATION_INSTANCE_ID` |
| `PRIORITY1_CROSS_LWM` | `NUMBER` | ID of last priority 1 event stream partition received at `DESTINATION_INSTANCE_ID` |
| `PRIORITY2_CROSS_LWM` | `NUMBER` | ID of last priority 2 event stream partition received at `DESTINATION_INSTANCE_ID` |
| `PRIORITY3_CROSS_LWM` | `NUMBER` | ID of last priority 3 event stream partition received at `DESTINATION_INSTANCE_ID` |
| `PRIORITY4_CROSS_LWM` | `NUMBER` | ID of last priority 4 event stream partition received at `DESTINATION_INSTANCE_ID` |
| `PRIORITY5_CROSS_LWM` | `NUMBER` | ID of last priority 5 event stream partition received at `DESTINATION_INSTANCE_ID` |
| `PRIORITY6_CROSS_LWM` | `NUMBER` | ID of last priority 6 event stream partition received at `DESTINATION_INSTANCE_ID` |
| `PRIORITY7_CROSS_LWM` | `NUMBER` | ID of last priority 7 event stream partition received at `DESTINATION_INSTANCE_ID` |
| `PRIORITY8_CROSS_LWM` | `NUMBER` | ID of last priority 8 event stream partition received at `DESTINATION_INSTANCE_ID` |
| `PRIORITY9_CROSS_LWM` | `NUMBER` | ID of last priority 9 event stream partition received at `DESTINATION_INSTANCE_ID` |
| `JOB_START_TIME` | `TIMESTAMP(3) WITH TIME ZONE` | Start time of this job |
| `SUBSCRIBER_ID` | `NUMBER` | ID of the subscriber whose affinity is being switched for the `DEQUEUE_AFFINITY_TO_REMOTE` and `DEQUEUE_AFFINITY_TO_LOCAL` job types |
| `SUBSCRIBER_NAME` | `VARCHAR2(512)` | Name of subscriber whose affinity is being switched for the `DEQUEUE_AFFINITY_TO_REMOTE` and `DEQUEUE_AFFINITY_TO_LOCAL` job types.  This column is NULL for the `CROSS_STREAM` job type. |
| `OWNER_INSTANCE_ID` | `NUMBER` | ID of the instance that owns the event stream |
| `QUEUE_ID` | `NUMBER` | Queue ID |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

Note:

This view is available starting with Oracle Database 21c.

See Also:

[Oracle Database Advanced Queuing User's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADQUE0100) for more information about Oracle Transactional Event Queues and Advanced Queuing