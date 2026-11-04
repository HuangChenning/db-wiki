---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-AQ.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.16 V$AQ

`V$AQ` displays statistics for the queues in the database.

| Column | Datatype | Description |
| --- | --- | --- |
| `QID` | `NUMBER` | Unique queue identifier |
| `WAITING` | `NUMBER` | Number of messages in the queue in the state ' `WAITING` ' |
| `READY` | `NUMBER` | Number of messages in the queue in the state ' `READY` ' |
| `EXPIRED` | `NUMBER` | Number of messages in the queue the state ' `EXPIRED` ' |
| `AVERAGE_MSG_AGE` | `NUMBER` | Average age of the messages in the queue' |
| `TOTAL_WAIT` | `NUMBER` | Total wait time of all ' `READY` ' messages in the queue |
| `AVERAGE_WAIT` | `NUMBER` | Average wait time of ' `READY` ' messages in the queue |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

[Oracle Database Advanced Queuing User's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADQUE0100) for more information about Oracle Database Advanced Queueing