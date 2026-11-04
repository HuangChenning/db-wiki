---
title: "V$SCHEDULER_RUNNING_JOBS"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_3001.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$SCHEDULER_RUNNING_JOBS` displays information about running Scheduler jobs.

| Column | Datatype | Description |
| --- | --- | --- |
| `SESSION_ID` | `NUMBER` | Identifier of the session running the Scheduler job |
| `SESSION_SERIAL_NUM` | `NUMBER` | Session serial number |
| `JOB_ID` | `NUMBER` | ID of the running Scheduler job |
| `PADDR` | `RAW(4 \| 8)` | Process address |
| `OS_PROCESS_ID` | `VARCHAR2(12)` | Operating system process ID |
| `SESSION_STAT_CPU` | `INTERVAL DAY(2) TO SECOND(3)` | CPU statistics for the session |