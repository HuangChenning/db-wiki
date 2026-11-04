---
title: ALL_SCHEDULER_RUNNING_JOBS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2053.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_SCHEDULER_RUNNING_JOBS` displays information about the running Scheduler jobs accessible to the current user.

Related Views

- `DBA_SCHEDULER_RUNNING_JOBS` displays information about all running Scheduler jobs in the database.
- `USER_SCHEDULER_RUNNING_JOBS` displays information about the running Scheduler jobs owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` |  | Owner of the running Scheduler job |
| `JOB_NAME` | `VARCHAR2(30)` |  | Name of the running Scheduler job |
| `JOB_SUBNAME` | `VARCHAR2(30)` |  | Subname of the running Scheduler job (for a job running a chain step) |
| `JOB_STYLE` | `VARCHAR2(11)` |  | Job style: - `REGULAR` - `LIGHTWEIGHT` |
| `DETACHED` | `VARCHAR2(5)` |  | Indicates whether the detached attribute is set for the job (`TRUE`) or not (`FALSE`). If the detached attribute is set, then the job will remain running even after the job action has completed. |
| `SESSION_ID` | `NUMBER` |  | Identifier of the session running the Scheduler job |
| `SLAVE_PROCESS_ID` | `NUMBER` |  | Process number of the slave process running the Scheduler job |
| `SLAVE_OS_PROCESS_ID` | `VARCHAR2(12)` |  | Process number of the operating system slave process running the scheduler job |
| `RUNNING_INSTANCE` | `NUMBER` |  | Database instance number of the slave process running the Scheduler job |
| `RESOURCE_CONSUMER_GROUP` | `VARCHAR2(32)` |  | Resource consumer group of the session in which the Scheduler job is running |
| `ELAPSED_TIME` | `INTERVAL DAY(3) TO SECOND(2)` |  | Elapsed time since the Scheduler job was started |
| `CPU_USED` | `INTERVAL DAY(3) TO SECOND(2)` |  | CPU time consumed by the running Scheduler job, if available |
| `DESTINATION_OWNER` | `VARCHAR2(128)` |  | Owner of the destination object (if used), else NULL |
| `DESTINATION` | `VARCHAR2(128)` |  | Destination that this job is running on |
| `CREDENTIAL_OWNER` | `VARCHAR2(30)` |  | Owner of the login credential used for this running job, if any |
| `CREDENTIAL_NAME` | `VARCHAR2(30)` |  | Name of the login credential used for this running job, if any |
| `LOG_ID` <sup>Foot 1</sup> | `NUMBER` |  | Log ID used for this running job. This column maps to the `LOG_ID` column of the `*_SCHEDULER_JOB_LOG` and `*_SCHEDULER_JOB_RUN_DETAILS` views. |

<sup>Footnote 1</sup> This column is available starting with Oracle Database 11g Release 2 (11.2.0.2).

See Also:

- ["DBA\_SCHEDULER\_RUNNING\_JOBS"](statviews_4258.md)
- ["USER\_SCHEDULER\_RUNNING\_JOBS"](statviews_5441.md)