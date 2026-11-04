---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-QMON_COORDINATOR_STATS.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.148 V$QMON\_COORDINATOR\_STATS

There is one row per instance. The rows are deleted when the database (or instance in an Oracle RAC environment) restarts.

| Column | Datatype | Description |
| --- | --- | --- |
| `QMNC_PID` | `VARCHAR2(24)` | Non-sharded queue primary process ID |
| `STATUS` | `VARCHAR2(24)` | Current status of the coordinator:  - `DEAD` - `INITIALIZING` - `RUNNING TASK COORDINATOR` - `WAITING` - `ADDING SERVER` |
| `NUM_SERVERS` | `NUMBER` | Number of QMON servers currently running |
| `LAST_SERVER_START_TIME` | `TIMESTAMP(3) WITH TIME ZONE` | Last server startup time |
| `LAST_SERVER_PID` | `VARCHAR2(24)` | Process ID of the last server process (Qnnn) created |
| `NEXT_WAKEUP_TIME` | `TIMESTAMP(3) WITH TIME ZONE` | Next wakeup time of the coordinator |
| `NEXT_READY_TIME` | `TIMESTAMP(3) WITH TIME ZONE` | Ready time of the first delayed task |
| `NEXT_EXPIRY_TIME` | `TIMESTAMP(3) WITH TIME ZONE` | Expiry time of the next ready task |
| `LAST_WAIT_TIME` | `TIMESTAMP(3) WITH TIME ZONE` | Time when the coordinator went to sleep |
| `LAST_FAILURE` | `VARCHAR2(32)` | Last failure encountered |
| `LAST_FAILURE_TIME` | `TIMESTAMP(3) WITH TIME ZONE` | Last failure time |
| `MAX_TASK_LATENCY` | `VARCHAR2(40)` | Maximum task latency across all the servers (in seconds) |
| `MIN_TASK_LATENCY` | `VARCHAR2(40)` | Minimum task latency across all the servers (in seconds) |
| `TOTAL_TASK_LATENCY` | `NUMBER` | Cumulative latency across all the tasks (in seconds) |
| `TOTAL_TASKS_EXECUTED` | `NUMBER` | Cumulative number of tasks serviced by all the servers |
| `MAX_SERVERS` | `NUMBER` | Maximum number of servers present at any point of time |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. The `CON_ID` value in this view is always 0. The rows pertain to the entire CDB or to the non-CDB. |