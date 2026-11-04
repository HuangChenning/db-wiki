---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-AQ_JOB_COORDINATOR.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.23 V$AQ\_JOB\_COORDINATOR

`V$AQ_JOB_COORDINATOR` lists performance statistics per coordinator, for every AQ coordinator controlled by the Oracle Database Advanced Queueing primary coordinator.

| Column | Datatype | Description |
| --- | --- | --- |
| `COORDINATOR_ID` | `NUMBER` | ID of the coordinator |
| `PROCESS_ID` | `VARCHAR2(24)` | Operating system process ID of the coordinator |
| `PROCESS_NAME` | `VARCHAR2(48)` | Operating system process name of the coordinator |
| `JOB_NAME` | `VARCHAR2(32)` | Name of the job handled |
| `JOB_TYPE` | `NUMBER` | Type of job handled |
| `SERVER_COUNT` | `NUMBER` | Number of servers active |
| `MAX_SERVER_COUNT` | `NUMBER` | Maximum server fanout achieved |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. The `CON_ID` value in this view is always 0. The rows pertain to the entire CDB or to the non-CDB. |

See Also:

[Oracle Database Advanced Queuing User's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADQUE0100) for more information about Oracle Database Advanced Queueing