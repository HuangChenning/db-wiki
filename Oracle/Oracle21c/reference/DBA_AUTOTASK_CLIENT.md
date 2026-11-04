---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_AUTOTASK_CLIENT.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.193 DBA\_AUTOTASK\_CLIENT

`DBA_AUTOTASK_CLIENT` displays statistical data for each automated maintenance task over 7-day and 30-day periods.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `CLIENT_NAME` | `VARCHAR2(64)` |  | Name of the client |
| `STATUS` | `VARCHAR2(8)` |  | Job status:  - `ENABLED` - `DISABLED` |
| `CONSUMER_GROUP` | `VARCHAR2(128)` |  | Consumer group used for normal priority jobs for this client |
| `CLIENT_TAG` | `VARCHAR2(2)` |  | Tag used to identify jobs for this client |
| `PRIORITY_OVERRIDE` | `VARCHAR2(7)` |  | User-specified priority at which the task executes:  - `URGENT` - `HIGH` - `MEDIUM` - `LOW` |
| `ATTRIBUTES` | `VARCHAR2(4000)` |  | Attributes of the client |
| `WINDOW_GROUP` | `VARCHAR2(64)` |  | Window group used to schedule jobs |
| `SERVICE_NAME` | `VARCHAR2(64)` |  | Name of the service on which jobs will execute for the client |
| `RESOURCE_PERCENTAGE` | `NUMBER` |  | Percentage of maintenance resources for high priority maintenance tasks for this client |
| `USE_RESOURCE_ESTIMATES` | `VARCHAR2(5)` |  | Indicates whether resource estimates are used for this client (`TRUE`) or not (`FALSE`) |
| `MEAN_JOB_DURATION` | `INTERVAL DAY(9) TO SECOND(9)` |  | Average elapsed time for a job for this client (in seconds) |
| `MEAN_JOB_CPU` | `INTERVAL DAY(9) TO SECOND(9)` |  | Average CPU time for a job submitted by this client (in seconds) |
| `MEAN_JOB_ATTEMPTS` | `NUMBER` |  | Average number of attempts it takes to complete a task |
| `MEAN_INCOMING_TASKS_7_DAYS` | `NUMBER` |  | Average number of incoming tasks at the Maintenance Window Start over the last 7 days |
| `MEAN_INCOMING_TASKS_30_DAYS` | `NUMBER` |  | Average number of incoming tasks at the Maintenance Window Start over the last 30 days |
| `TOTAL_CPU_LAST_7_DAYS` | `INTERVAL DAY(9) TO SECOND(9)` |  | Cumulative CPU time used by the jobs for this client over the last 7 days (in seconds) |
| `TOTAL_CPU_LAST_30_DAYS` | `INTERVAL DAY(9) TO SECOND(9)` |  | Cumulative CPU time used by the jobs for this client over the last 30 days (in seconds) |
| `MAX_DURATION_LAST_7_DAYS` | `INTERVAL DAY(3) TO SECOND(0)` |  | Maximum elapsed time for a job over the last 7 days (in seconds) |
| `MAX_DURATION_LAST_30_DAYS` | `INTERVAL DAY(3) TO SECOND(0)` |  | Maximum elapsed time for a job over the last 30 days (in seconds) |
| `WINDOW_DURATION_LAST_7_DAYS` | `INTERVAL DAY(9) TO SECOND(9)` |  | Total time during which the client was active during the last 7 days |
| `WINDOW_DURATION_LAST_30_DAYS` | `INTERVAL DAY(9) TO SECOND(9)` |  | Total time during which the client was active during the last 30 days |
| `LAST_CHANGE` | `TIMESTAMP(6) WITH TIME ZONE` |  | Timestamp of last configuration change for the client |