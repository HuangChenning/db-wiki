---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-QMON_SERVER_STATS.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.149 V$QMON\_SERVER\_STATS

There is one row per live queue monitor server process. The rows are deleted when the database (or instance in an Oracle RAC environment) restarts.

| Column | Datatype | Description |
| --- | --- | --- |
| `QMNC_PID` | `VARCHAR2(24)` | Non-sharded queue primary process ID |
| `SERVER_PID` | `VARCHAR2(24)` | Process ID of the server |
| `SERVER_NAME` | `VARCHAR2(48)` | Name of the server |
| `STATUS` | `VARCHAR2(40)` | Current state of the server:  - `UNUSED` - `RUNNING` - `IDLE WAIT` - `EXITING` - `NOT ACTIVE` |
| `SERVER_START_TIME` | `TIMESTAMP(3) WITH TIME ZONE` | Start time of the server |
| `TASK_NAME` | `VARCHAR2(32)` | Current executing task |
| `TASK_NUMBER` | `NUMBER` | Unique task number of the running task |
| `TASK_START_TIME` | `TIMESTAMP(3) WITH TIME ZONE` | Start time of the running task |
| `LAST_WAIT_TIME` | `TIMESTAMP(3) WITH TIME ZONE` | Time when the server last waited |
| `MAX_LATENCY` | `NUMBER` | Maximum task latency for this server (in seconds) |
| `MIN_LATENCY` | `NUMBER` | Minimum task latency for this server (in seconds) |
| `TOTAL_LATENCY` | `NUMBER` | Cumulative task latency for this server (in seconds) |
| `NUM_TASKS` | `NUMBER` | Number of tasks processed by the server |
| `LAST_FAILURE` | `VARCHAR2(128)` | Last failure encountered by the server |
| `LAST_FAILURE_TIME` | `TIMESTAMP(3) WITH TIME ZONE` | Last failure time |
| `LAST_FAILURE_TASK` | `VARCHAR2(32)` | Task being run at the time of the last failure |
| `LAST_FAILURE_TASKNUM` | `NUMBER` | Unique task number of the failed task |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. The `CON_ID` value in this view is always 0. The rows pertain to the entire CDB or to the non-CDB. |