---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-SCHEDULER_RUNNING_JOBS.html
tags:
  - oracle
  - 21c
  - reference
---

## 10.1 V$SCHEDULER\_RUNNING\_JOBS

`V$SCHEDULER_RUNNING_JOBS` displays information about running Scheduler jobs.

| Column | Datatype | Description |
| --- | --- | --- |
| `SESSION_ID` | `NUMBER` | Identifier of the session running the Scheduler job |
| `SESSION_SERIAL_NUM` | `NUMBER` | Session serial number |
| `JOB_ID` | `NUMBER` | ID of the running Scheduler job |
| `PADDR` | `RAW(4 \| 8)` | Process address |
| `OS_PROCESS_ID` | `VARCHAR2(12)` | Operating system process ID |
| `SESSION_STAT_CPU` | `INTERVAL DAY(2) TO SECOND(3)` | CPU statistics for the session |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire multitenant container database (CDB). This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |