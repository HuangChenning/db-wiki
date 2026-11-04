---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-AQ_SERVER_POOL.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.33 V$AQ\_SERVER\_POOL

`V$AQ_SERVER_POOL` lists performance statistics for all the servers in the pool.

| Column | Datatype | Description |
| --- | --- | --- |
| `COORDINATOR_ID` | `NUMBER` | ID of the coordinator |
| `COORDINATOR_INSTANCE_ID` | `NUMBER` | Instance of the coordinator |
| `PROCESS_ID` | `VARCHAR2(24)` | Operating system process ID of the server |
| `PROCESS_NAME` | `VARCHAR2(48)` | Operating system process name of the server |
| `JOB_NAME` | `VARCHAR2(32)` | Name of the job handled |
| `POOL_STATE` | `VARCHAR2(20)` | State of the pool:  - `REMOTE` - `IDLE` - `ACTIVE` |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. The `CON_ID` value in this view is always 0. The rows pertain to the entire CDB or to the non-CDB. |

See Also:

[Oracle Database Advanced Queuing User's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADQUE0100) for more information about Oracle Database Advanced Queueing