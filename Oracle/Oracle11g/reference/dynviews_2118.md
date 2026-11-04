---
title: "V$QMON_SERVER_STATS"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2118.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$QMON_SERVER_STATS` displays information and statistics about the active queue monitor server processes. There is one row per live queue monitor server process. The rows are deleted when the database (or instance in an Oracle RAC environment) restarts.

| Column | Datatype | Description |
| --- | --- | --- |
| `QMNC_PID` | `VARCHAR2(24)` | Process ID of the Queue Monitor Coordinator for this server |
| `SERVER_PID` | `VARCHAR2(24)` | Process ID of the server |
| `SERVER_NAME` | `VARCHAR2(48)` | Name of the server |
| `STATUS` | `VARCHAR2(40)` | Current state of the server: - `UNUSED` - `RUNNING` - `IDLE WAIT` - `EXITING` - `NOT ACTIVE` |
| `SERVER_START_TIME` | `TIMESTAMP(3) WITH TIME ZONE` | Start time of the server |
| `TASK_NAME` | `VARCHAR2(32)` | Current executing task |
| `TASK_NUMBER` | `NUMBER` | Unique task number of the running task |
| `TASK_START_TIME` | `TIMESTAMP(3) WITH TIME ZONE` | Start time of the running task |
| `LAST_WAIT_TIME` | `TIMESTAMP(3) WITH TIME ZONE` | Time when the server last waited |
| `MAX_LATENCY` | `NUMBER` | Maximum task latency for this server (in seconds) |
| `MIN_LATENCY` | `NUMBER` | Minimum task latency for this server (in seconds) |
| `TOTAL_LATENCY` | `NUMBER` | Cumulative task latency for this server (in seconds) |
| `NUM_TASKS` | `NUMBER` | Number of tasks processed by the server |
| `LAST_FAILURE` | `VARCHAR2(32)` | Last failure encountered by the server |
| `LAST_FAILURE_TIME` | `TIMESTAMP(3) WITH TIME ZONE` | Last failure time |
| `LAST_FAILURE_TASK` | `VARCHAR2(32)` | Task being run at the time of the last failure |
| `LAST_FAILURE_TASKNUM` | `NUMBER` | Unique task number of the failed task |