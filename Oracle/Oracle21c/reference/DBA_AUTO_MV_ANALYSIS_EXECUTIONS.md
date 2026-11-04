---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_AUTO_MV_ANALYSIS_EXECUTIONS.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.180 DBA\_AUTO\_MV\_ANALYSIS\_EXECUTIONS

`DBA_AUTO_MV_ANALYSIS_EXECUTIONS` displays information about analysis and tuning executions associated with automatic materialized views.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` |  | Owner of the task |
| `TASK_ID` | `NUMBER` | `NOT NULL` | Unique identifier of the task |
| `TASK_NAME` | `VARCHAR2(128)` |  | Name of the task  The value of this column is always `SYS_AUTO_MV_TASK`. |
| `EXECUTION_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the task execution with which this entry (row) is associated |
| `EXECUTION_ID` | `NUMBER` | `NOT NULL` | Execution ID |
| `DESCRIPTION` | `VARCHAR2(256)` |  | User-supplied description of the task |
| `EXECUTION_TYPE` | `VARCHAR2(128)` |  | Type of the last execution (optional for single-execution tasks) |
| `EXECUTION_TYPE#` | `NUMBER` |  | Reserved for internal use |
| `EXECUTION_START` | `DATE` |  | Execution start date and time |
| `EXECUTION_LAST_MODIFIED` | `DATE` | `NOT NULL` | Last modified date and time for the execution |
| `EXECUTION_END` | `DATE` |  | Execution end date and time |
| `REQUESTED_DOP` | `NUMBER` |  | The degree of parallelism (DOP) value requested by the user (through the `TEST_EXECUTE_DOP` parameter). It can be any value greater or equal to zero. |
| `ACTUAL_DOP` | `NUMBER` |  | The actual degree of parallelism (DOP) with which the execution finished. If the requested DOP is greater than than what is available on the system, the `ACTUAL_DOP` value can be lower than the `REQUESTED_DOP` value. |
| `CONCURRENT_EXECUTION` | `VARCHAR2(3)` |  | Indicates whether concurrency was used for this execution (`YES`) or not (`NO`) |
| `ADVISOR_NAME` | `VARCHAR2(128)` |  | Advisor associated with the task |
| `ADVISOR_ID` | `NUMBER` | `NOT NULL` | Unique identifier for the advisor |
| `STATUS` | `VARCHAR2(11)` |  | Current operational status of the task:  - `EXECUTING` - `COMPLETED` - `INTERRUPTED` - `CANCELLED` - `FATAL ERROR` |
| `STATUS#` | `NUMBER` | `NOT NULL` | Reserved for internal use |
| `STATUS_MESSAGE` | `VARCHAR2(4000)` |  | Informational message provided by the advisor regarding the status |
| `ERROR_MESSAGE` | `VARCHAR2(4000)` |  | Informational message or an error message indicating the current operation or condition |

Note:

This view is available starting with Oracle Database 21c.