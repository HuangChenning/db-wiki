---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-EQ_NONDUR_SUBSCRIBER_LWM.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.210 V$EQ\_NONDUR\_SUBSCRIBER\_LWM

`V$EQ_NONDUR_SUBSCRIBER_LWM` projects the low watermarks (LWMs) of non-durable subscribers in a Transactional Event Queue (TEQ). The LWM of a non-durable subscriber is a combination of event stream, priority, and LWM (event queue partition).

| Column | Datatype | Description |
| --- | --- | --- |
| `QUEUE_ID` | `NUMBER` | Queue ID |
| `SUBSCRIBER_ID` | `NUMBER` | ID of the non-durable subscriber |
| `EVENT_STREAM_ID` | `NUMBER` | Event stream ID |
| `PRIORITY` | `NUMBER` | Priority of the event stream |
| `LWM` | `NUMBER` | Lower watermark (in an event stream partition) of the non-durable subscriber |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

Note:

This view is available starting with Oracle Database 21c.

See Also:

[Oracle Database Advanced Queuing User's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADQUE0100) for more information about Oracle Transactional Event Queues and Advanced Queuing