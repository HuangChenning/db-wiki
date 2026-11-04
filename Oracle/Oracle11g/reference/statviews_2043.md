---
title: ALL_SCHEDULER_JOB_DESTS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2043.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_SCHEDULER_JOB_DESTS` displays information about the state of the jobs accessible to the current user at each of their destinations.

Related Views

- `DBA_SCHEDULER_JOB_DESTS` displays information about the state of all jobs in the database at each of their destinations.
- `USER_SCHEDULER_JOB_DESTS` displays information about the state of the jobs owned by the current user at each of their destinations. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` |  | Owner of the Scheduler job |
| `JOB_NAME` | `VARCHAR2(30)` |  | Name of the Scheduler job |
| `JOB_SUBNAME` | `VARCHAR2(31)` |  | Subname of the Scheduler job |
| `CREDENTIAL_OWNER` | `VARCHAR2(30)` |  | Owner of the credential used for the remote destination |
| `CREDENTIAL_NAME` | `VARCHAR2(30)` |  | Name of the credential used for the remote destination |
| `DESTINATION_OWNER` | `VARCHAR2(128)` |  | Owner of the destination object that points to the destination |
| `DESTINATION` | `VARCHAR2(128)` |  | Name of the destination object or the name of the destination itself |
| `JOB_DEST_ID` | `NUMBER` |  | Numerical ID assigned to the job at this destination |
| `ENABLED` | `VARCHAR2(5)` |  | Indicates whether the parent job is enabled (`TRUE`) or disabled (`FALSE`) |
| `REFS_ENABLED` | `VARCHAR2(5)` |  | Indicates whether this destination and its agent are enabled (`TRUE`) or disabled (`FALSE`) |
| `STATE` | `VARCHAR2(15)` |  | State of this job at this destination: - `DISABLED` - `RUNNING` - `CHAIN_STALLED` - `SCHEDULED` - `RETRY SCHEDULED` - `READY TO RUN` - `COMPLETED` - `BROKEN` - `FAILED` - `SUCCEEDED` - `REMOTE` - `STOPPED` |
| `NEXT_START_DATE` | `TIMESTAMP(6) WITH TIME ZONE` |  | Next start time of this job at this destination |
| `RUN_COUNT` | `NUMBER` |  | Number of times this job has run at this destination |
| `RETRY_COUNT` | `NUMBER` |  | Number of times this job has been retried at this destination |
| `FAILURE_COUNT` | `NUMBER` |  | Number of times this job has failed at this destination |
| `LAST_START_DATE` | `TIMESTAMP(6) WITH TIME ZONE` |  | Last time this job started at this destination |
| `LAST_END_DATE` | `TIMESTAMP(6) WITH TIME ZONE` |  | Last time this job ended at this destination |

See Also:

- ["DBA\_SCHEDULER\_JOB\_DESTS"](statviews_4247.md)
- ["USER\_SCHEDULER\_JOB\_DESTS"](statviews_5432.md)