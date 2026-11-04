---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_ADVISOR_LOG.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.32 DBA\_ADVISOR\_LOG

`DBA_ADVISOR_LOG` displays information about the current state of all tasks in the database, as well as execution-specific data such as progress monitoring and completion status.

The view contains one row for each task.

Related View

`USER_ADVISOR_LOG` displays information about the current state of the tasks owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` |  | Owner of the task |
| `TASK_ID` | `NUMBER` | `NOT NULL` | Identifier of the task |
| `TASK_NAME` | `VARCHAR2(128)` |  | Name of the task |
| `EXECUTION_START` | `DATE` |  | Execution start date and time of the task |
| `EXECUTION_END` | `DATE` |  | Execution end date and time of the task |
| `STATUS` | `VARCHAR2(11)` |  | Current operational status of the task:  - `INITIAL` - Initial state of the task; no recommendations are present - `EXECUTING` - Task is currently running - `COMPLETED` - Task successfully completed the analysis operation. Recommendation data can be viewed and reported. - `INTERRUPTED` - Task analysis was interrupted by the user. Recommendation data, if present, can be viewed and reported at this time. - `CANCELLED` - `FATAL ERROR` - An irrecoverable error occurred during the analysis operation. All recommendation data is unusable. |
| `STATUS_MESSAGE` | `VARCHAR2(4000)` |  | Informational message provided by the advisor regarding the status |
| `PCT_COMPLETION_TIME` | `NUMBER` |  | Percent completion, in terms of time, of the task when it is executing |
| `PROGRESS_METRIC` | `NUMBER` |  | Metric that measures the progress of the task in terms of quality. Each advisor could have its own metric. |
| `METRIC_UNITS` | `VARCHAR2(64)` |  | Unit of the metric used to measure progress |
| `ACTIVITY_COUNTER` | `NUMBER` |  | Counter that is updated frequently by the advisor, denoting that useful work is being performed |
| `RECOMMENDATION_COUNT` | `NUMBER` |  | Number of recommendations produced |
| `ERROR_MESSAGE` | `VARCHAR2(4000)` |  | Informational message or an error message indicating the current operation or condition |

See Also:

" [USER\_ADVISOR\_LOG](USER_ADVISOR_LOG.md) "