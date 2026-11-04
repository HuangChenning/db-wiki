---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/V-AQ_NONDUR_SUBSCRIBER_LWM.html
tags:
  - oracle
  - 19c
  - reference
---

## 7.27 V$AQ\_NONDUR\_SUBSCRIBER\_LWM

`V$AQ_NONDUR_SUBSCRIBER_LWM` projects the low watermarks (LWMs) of non-durable subscribers in a sharded queue. The LWM of a non-durable subscriber is a combination of shard, priority and LWM (subshard).

| Column | Datatype | Description |
| --- | --- | --- |
| `QUEUE_ID` | `NUMBER` | Queue ID |
| `SUBSCRIBER_ID` | `NUMBER` | ID of the non-durable subscriber |
| `SHARD_ID` | `NUMBER` | Shard ID |
| `PRIORITY` | `NUMBER` | Priority of the shard |
| `LWM` | `NUMBER` | Lower watermark (in a subshard) of the non-durable subscriber |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

[Oracle Database Advanced Queuing User's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/refrn&id=ADQUE0100) for more information about Oracle Database Advanced Queueing