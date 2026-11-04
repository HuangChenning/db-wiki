---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_ADVISOR_TASKS.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.50 DBA\_ADVISOR\_TASKS

`DBA_ADVISOR_TASKS` displays information about all tasks in the database.

The view contains one row for each task. Each task has a name that is unique to the owner. Task names are just informational and no uniqueness is enforced within any other namespace.

Related View

`USER_ADVISOR_TASKS` displays information about the tasks owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` |  | Owner of the task |
| `TASK_ID` | `NUMBER` | `NOT NULL` | Unique identifier of the task |
| `TASK_NAME` | `VARCHAR2(128)` |  | Name of the task |
| `DESCRIPTION` | `VARCHAR2(256)` |  | User-supplied description of the task |
| `ADVISOR_NAME` | `VARCHAR2(128)` |  | Advisor associated with the task |
| `CREATED` | `DATE` | `NOT NULL` | Creation date of the task |
| `LAST_MODIFIED` | `DATE` | `NOT NULL` | Date on which the task was last modified |
| `PARENT_TASK_ID` | `NUMBER` |  | Identifier of the parent task (if the task was created because of the recommendation of another task) |
| `PARENT_RXEC_ID` | `NUMBER` |  | Identifier of the recommendation within the parent task that resulted in the creation of the task |
| `LAST_EXECUTION` | `VARCHAR2(128)` |  | Name of the current or last task execution |
| `EXECUTION_TYPE` | `VARCHAR2(128)` |  | Type of the last execution. This information is optional for single-execution tasks. |
| `EXECUTION_TYPE#` | `NUMBER` |  | Reserved for internal use |
| `EXECUTION_DESCRIPTION` | `VARCHAR2(256)` |  | Optional description of the last execution |
| `EXECUTION_START` | `DATE` |  | Execution start date and time of the task |
| `EXECUTION_END` | `DATE` |  | Execution end date and time of the task |
| `STATUS` | `VARCHAR2(11)` |  | Current operational status of the task:  - `INITIAL` - Initial state of the task; no recommendations are present - `EXECUTING` - Task is currently running - `INTERRUPTED` - Task analysis was interrupted by the user. Recommendation data, if present, can be viewed and reported at this time. - `COMPLETED` - Task successfully completed the analysis operation. Recommendation data can be viewed and reported. - `ERROR` - An error occurred during the analysis operation. Recommendations, if present, can be viewed and reported at this time. |
| `STATUS_MESSAGE` | `VARCHAR2(4000)` |  | Informational message provided by the advisor regarding the status |
| `PCT_COMPLETION_TIME` | `NUMBER` |  | Percent completion, in terms of time, of the task when it is executing |
| `PROGRESS_METRIC` | `NUMBER` |  | Metric that measures the progress of the task in terms of quality. Each advisor may have its own metric. |
| `METRIC_UNITS` | `VARCHAR2(64)` |  | Unit of the metric used to measure progress |
| `ACTIVITY_COUNTER` | `NUMBER` |  | Counter that is updated frequently by the advisor, denoting that useful work is being performed |
| `RECOMMENDATION_COUNT` | `NUMBER` |  | Number of recommendations produced |
| `ERROR_MESSAGE` | `VARCHAR2(4000)` |  | Informational message or an error message indicating the current operation or condition |
| `SOURCE` | `VARCHAR2(128)` |  | Optional name that identifies the creator of the task |
| `HOW_CREATED` | `VARCHAR2(30)` |  | Optional task or template on which the object was based |
| `READ_ONLY` | `VARCHAR2(5)` |  | Indicates whether the task is read-only (`TRUE`) or not (`FALSE`) |
| `SYSTEM_TASK` | `VARCHAR2(5)` |  | Indicates whether the task is a system task (`TRUE`) or not (`FALSE`). The automatic SQL tuning task, `SYS_AUTO_SQL_TUNING_TASK`, is one example of a system task. |
| `ADVISOR_ID` | `NUMBER` | `NOT NULL` | Unique identifier for the advisor |
| `STATUS#` | `NUMBER` |  | Reserved for internal use |

See Also:

" [USER\_ADVISOR\_TASKS](USER_ADVISOR_TASKS.md) "