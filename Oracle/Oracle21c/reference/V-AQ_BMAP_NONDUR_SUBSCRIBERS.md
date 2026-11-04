---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-AQ_BMAP_NONDUR_SUBSCRIBERS.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.18 V$AQ\_BMAP\_NONDUR\_SUBSCRIBERS

`V$AQ_BMAP_NONDUR_SUBSCRIBERS` can be used to get the available bit positions. The view is queried to get the free bit position during creation of a non-durable subscriber.

| Column | Datatype | Description |
| --- | --- | --- |
| `QUEUE_ID` | `NUMBER` | Queue ID |
| `USED_POS` | `RAW(128)` | Stream of bits to identify used and available bit positions |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

[Oracle Database Advanced Queuing User's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADQUE0100) for more information about Oracle Database Advanced Queueing