---
title: ALL_SCHEDULER_JOB_RUN_DETAILS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2045.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_SCHEDULER_JOB_RUN_DETAILS` displays log run details for the Scheduler jobs accessible to the current user.

Related Views

- `DBA_SCHEDULER_JOB_RUN_DETAILS` displays log run details for all Scheduler jobs in the database.
- `USER_SCHEDULER_JOB_RUN_DETAILS` displays log run details for the Scheduler jobs owned by the current user.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `LOG_ID` | `NUMBER` |  | Unique identifier of the log entry (foreign key of the `*_SCHEDULER_JOB_LOG` views) |
| `LOG_DATE` | `TIMESTAMP(6) WITH TIME ZONE` |  | Date of the log entry |
| `OWNER` | `VARCHAR2(30)` |  | Owner of the Scheduler job |
| `JOB_NAME` | `VARCHAR2(65)` |  | Name of the Scheduler job |
| `JOB_SUBNAME` | `VARCHAR2(65)` |  | Subname of the Scheduler job (for a chain step job) |
| `STATUS` | `VARCHAR2(30)` |  | Status of the job run |
| `ERROR#` | `NUMBER` |  | Error number in the case of an error |
| `REQ_START_DATE` | `TIMESTAMP(6) WITH TIME ZONE` |  | Requested start date of the job run |
| `ACTUAL_START_DATE` | `TIMESTAMP(6) WITH TIME ZONE` |  | Actual date on which the job was run |
| `RUN_DURATION` | `INTERVAL DAY(3) TO SECOND(0)` |  | Duration of the job run |
| `INSTANCE_ID` | `NUMBER` |  | Identifier of the instance on which the job was run |
| `SESSION_ID` | `VARCHAR2(30)` |  | Session identifier of the job run |
| `SLAVE_PID` | `VARCHAR2(30)` |  | Process identifier of the slave on which the job was run |
| `CPU_USED` | `INTERVAL DAY(3) TO SECOND(2)` |  | Amount of CPU used for the job run |
| `CREDENTIAL_OWNER` | `VARCHAR2(65)` |  | Owner of the credential used for this remote job run |
| `CREDENTIAL_NAME` | `VARCHAR2(65)` |  | Name of the credential used for this remote job run |
| `DESTINATION_OWNER` | `VARCHAR2(128)` |  | Owner of the destination object used in this remote job run; NULL if no object used |
| `DESTINATION` | `VARCHAR2(128)` |  | Destination for a remote job operation |
| `ADDITIONAL_INFO` | `VARCHAR2(4000)` |  | Additional information on the job run, if applicable |