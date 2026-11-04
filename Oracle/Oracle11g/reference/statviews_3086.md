---
title: DBA_AUTOTASK_CLIENT_JOB
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_3086.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_AUTOTASK_CLIENT_JOB` displays information about currently running Scheduler jobs created for automated maintenance tasks. It provides information about some objects targeted by those jobs, as well as some additional statistics from previous instantiations of the same task. Some of this additional data is taken from generic Scheduler views.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `CLIENT_NAME` | `VARCHAR2(64)` |  | Name of the client |
| `JOB_NAME` | `VARCHAR2(65)` |  | Name of the job |
| `JOB_SCHEDULER_STATUS` | `VARCHAR2(15)` |  | Job status: - `DISABLED` - `RETRY SCHEDULED` - `SCHEDULED` - `RUNNING` - `COMPLETED` - `BROKEN` - `FAILED` - `REMOTE` - `SUCCEEDED` - `CHAIN_STALLED` |
| `TASK_NAME` | `VARCHAR2(64)` |  | Name of the task being performed |
| `TASK_TARGET_TYPE` | `VARCHAR2(64)` |  | Type of the target being processed |
| `TASK_TARGET_NAME` | `VARCHAR2(513)` | `NOT NULL` | Name of the target |
| `TASK_PRIORITY` | `VARCHAR2(7)` |  | Priority of the task: |
| `TASK_OPERATION` | `VARCHAR2(64)` |  | Operation performed on the object |