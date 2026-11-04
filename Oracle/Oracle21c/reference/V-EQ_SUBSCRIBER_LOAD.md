---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-EQ_SUBSCRIBER_LOAD.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.213 V$EQ\_SUBSCRIBER\_LOAD

`V$EQ_SUBSCRIBER_LOAD` describes the load of all subscribers of Transactional Event Queue (TEQ) event streams in terms of latency at every instance in an Oracle RAC environment.

Latency denotes the predicted amount of time (in seconds) required from the current time to drain all the messages for that subscriber at each respective instance. The latency calculation considers past enqueue/dequeue rates and future enqueue/dequeue rates based on history.

| Column | Datatype | Description |
| --- | --- | --- |
| `QUEUE_ID` | `NUMBER` | Queue ID |
| `QUEUE_SCHEMA` | `VARCHAR2(128)` | Queue schema |
| `QUEUE_NAME` | `VARCHAR2(128)` | Queue name |
| `SUBSCRIBER_ID` | `NUMBER` | Subscriber ID |
| `SUBSCRIBER_NAME` | `VARCHAR2(128)` | Subscriber name |
| `LATENCY_STATE` | `VARCHAR2(8)` | Latency state. Possible values:  - `FINITE` - The subscriber will be able to dequeue all the messages in a finite amount of time - `INFINITE` - The subscriber's dequeue rate may not catch up to the enqueue rate - `UNKNOWN` - Latency is not yet known |
| `LATENCY` | `NUMBER` | Latency (in seconds). Valid only when `LATENCY_STATE` is `FINITE`. |
| `DEQUEUE_REQUESTS` | `NUMBER` | Approximate number of dequeue requests noted recently |
| `ACTIVE_EVENT_STREAM_ID` | `NUMBER` | Number of event streams that have messages for this subscriber |
| `ACTIVE_LISTENER` | `VARCHAR2(5)` | Indicates whether the subscriber is actively listening at this instance for messages (`TRUE`) or not (`FALSE`) |
| `DEQUEUE_SESSIONS` | `NUMBER` | Displays the number of active dequeue sessions for this subscriber |
| `FLAGS` | `NUMBER` | For internal use only |
| `MANDATORY_AFF_SWITCHES` | `NUMBER` | An affinity switch is a change in the dequeue instance for an event stream-subscriber pair. A mandatory affinity switch is when there are local enqueues in the queue at the instance but no local dequeues present, so the dequeue affinity is switched to another instance for that event stream-subscriber pair. This column shows the number of times mandatory affinity switches were needed from this instance to another for this subscriber. |
| `OPTIONAL_AFF_SWITCHES` | `NUMBER` | Optional affinity switches are affinity switches that are not mandatory. Optional affinity switches are done for global load balancing across the Oracle Real Application Clusters (Oracle RAC) database. This column shows the number of times optional affinity switches were needed from this instance to another for this subscriber. |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

Note:

This view is available starting with Oracle Database 21c.

See Also:

[Oracle Database Advanced Queuing User's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADQUE0100) for more information about Oracle Transactional Event Queues and Advanced Queuing