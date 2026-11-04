---
title: "V$QMON_COORDINATOR_STATS"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2117.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$QMON_COORDINATOR_STATS` displays information and statistics about the Queue Monitor Coordinator process (QMNC). There is one row per instance. The rows are deleted when the database (or instance in an Oracle RAC environment) restarts.

| Column | Datatype | Description |
| --- | --- | --- |
| `QMNC_PID` | `VARCHAR2(24)` | Queue Monitor Coordinator process ID |
| `STATUS` | `VARCHAR2(24)` | Current status of the coordinator: |
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