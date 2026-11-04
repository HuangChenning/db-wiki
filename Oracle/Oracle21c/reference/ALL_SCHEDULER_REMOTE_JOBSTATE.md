---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_SCHEDULER_REMOTE_JOBSTATE.html
tags:
  - oracle
  - 21c
  - reference
---

## 4.59 ALL\_SCHEDULER\_REMOTE\_JOBSTATE

`ALL_SCHEDULER_REMOTE_JOBSTATE` displays information about the state of the jobs accessible to the current user at remote databases.

Related Views

- `DBA_SCHEDULER_REMOTE_JOBSTATE` displays information about the state of all jobs at remote databases.
- `USER_SCHEDULER_REMOTE_JOBSTATE` displays information about the state of the jobs owned by the current user at remote databases. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the Scheduler job |
| `JOB_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the Scheduler job |
| `DESTINATION` | `VARCHAR2(512)` | `NOT NULL` | Name of the job destination |
| `STATE` | `VARCHAR2(15)` |  | State of the job at the destination:  - `DISABLED` - `RETRY SCHEDULED` - `SCHEDULED` - `RUNNING` - `COMPLETED` - `BROKEN` - `FAILED` - `SUCCEEDED` - `STOPPED` |
| `NEXT_START_DATE` | `TIMESTAMP(6) WITH TIME ZONE` |  | Next start date of the job at the destination |
| `RUN_COUNT` | `NUMBER` |  | Run count of the job at the destination |
| `FAILURE_COUNT` | `NUMBER` |  | Failure count of the job at the destination |
| `RETRY_COUNT` | `NUMBER` |  | Retry count of the job at the destination |
| `LAST_START_DATE` | `TIMESTAMP(6) WITH TIME ZONE` |  | Last start date of the job at the destination |
| `LAST_END_DATE` | `TIMESTAMP(6) WITH TIME ZONE` |  | Last end date of the job at the destination |

See Also:

- " [DBA\_SCHEDULER\_REMOTE\_JOBSTATE](DBA_SCHEDULER_REMOTE_JOBSTATE.md) "
- " [USER\_SCHEDULER\_REMOTE\_JOBSTATE](USER_SCHEDULER_REMOTE_JOBSTATE.md) "