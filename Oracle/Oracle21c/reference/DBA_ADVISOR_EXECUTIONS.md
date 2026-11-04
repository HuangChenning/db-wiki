---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_ADVISOR_EXECUTIONS.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.27 DBA\_ADVISOR\_EXECUTIONS

`DBA_ADVISOR_EXECUTIONS` displays metadata information for task executions.

For example, the SQL Performance Analyzer creates a minimum of three executions to perform a change impact analysis on a SQL workload. The first one collects performance data for the version of the workload before the change, the second one collects data for the version of the workload after the change, and the third one performs impact analysis. All of these executions belong to the same task and are grouped into this view. Similarly, the automatic SQL tuning task, `SYS_AUTO_SQL_TUNING_TASK`, creates a new execution for each tuning run.

Related View

`USER_ADVISOR_EXECUTIONS` displays metadata information for task executions owned by the current user.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` |  | Owner of the task |
| `TASK_ID` | `NUMBER` | `NOT NULL` | Unique identifier of the task |
| `TASK_NAME` | `VARCHAR2(128)` |  | Name of the task |
| `EXECUTION_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the task execution with which this entry (row) is associated |
| `EXECUTION_ID` | `NUMBER` | `NOT NULL` | Execution ID |
| `DESCRIPTION` | `VARCHAR2(256)` |  | User-supplied description of the task |
| `EXECUTION_TYPE` | `VARCHAR2(128)` |  | Type of the last execution (optional for single-execution tasks) |
| `EXECUTION_TYPE#` | `NUMBER` |  | Reserved for internal use |
| `EXECUTION_START` | `DATE` |  | Execution start date and time |
| `EXECUTION_LAST_MODIFIED` | `DATE` | `NOT NULL` | Last modified date and time for the execution |
| `EXECUTION_END` | `DATE` |  | Execution end date and time |
| `ADVISOR_NAME` | `VARCHAR2(128)` |  | Advisor associated with the task |
| `REQUESTED_DOP` | `NUMBER` |  | The degree of parallelism (DOP) value requested by the user (through the `TEST_EXECUTE_DOP` parameter). It can be any value greater or equal to zero. |
| `ACTUAL_DOP` | `NUMBER` |  | The actual degree of parallelism (DOP) with which the execution finished. If the requested DOP is greater than than what is available on the system, the `ACTUAL_DOP` value can be lower than the `REQUESTED_DOP` value. |
| `CONCURRENT_EXECUTION` | `VARCHAR2(3)` |  | Indicates whether concurrency was used for this execution (`YES`) or not (`NO`) |
| `ADVISOR_ID` | `NUMBER` | `NOT NULL` | Unique identifier for the advisor |
| `STATUS` | `VARCHAR2(11)` |  | Current operational status of the task:  - `EXECUTING` - `COMPLETED` - `INTERRUPTED` - `CANCELLED` - `FATAL ERROR` |
| `STATUS#` | `NUMBER` | `NOT NULL` | Reserved for internal use |
| `STATUS_MESSAGE` | `VARCHAR2(4000)` |  | Informational message provided by the advisor regarding the status |
| `ERROR_MESSAGE` | `VARCHAR2(4000)` |  | Informational message or an error message indicating the current operation or condition |

See Also:

" [USER\_ADVISOR\_EXECUTIONS](USER_ADVISOR_EXECUTIONS.md) "