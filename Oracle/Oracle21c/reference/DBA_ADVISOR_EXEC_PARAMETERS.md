---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_ADVISOR_EXEC_PARAMETERS.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.25 DBA\_ADVISOR\_EXEC\_PARAMETERS

`DBA_ADVISOR_EXEC_PARAMETERS` displays the parameter values used for past executions of tasks.

It is more useful for advisors supporting multiple executions, such as SQL Performance Analyzer, where a parameter can have different values for different executions.

Related View

`USER_ADVISOR_EXEC_PARAMETERS` displays the parameter values used for past executions of tasks owned by the current user.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` |  | Owner of the task |
| `TASK_ID` | `NUMBER` | `NOT NULL` | Unique identifier of the task |
| `TASK_NAME` | `VARCHAR2(128)` |  | Name of the task |
| `EXECUTION_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the task execution with which this entry (row) is associated |
| `EXECUTION_TYPE` | `VARCHAR2(128)` |  | Type of the last execution. This information is optional for single-execution tasks. |
| `PARAMETER_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the parameter |
| `PARAMETER_VALUE` | `VARCHAR2(4000)` |  | Value of the parameter. Numeric parameter values are converted to a string equivalent. |
| `PARAMETER_TYPE` | `VARCHAR2(10)` |  | Datatype of the parameter (see `DBA_ADVISOR_PARAMETERS`) |
| `IS_DEFAULT` | `VARCHAR2(1)` |  | Indicates whether the parameter value is set to the advisor's default value (`Y`) or not (`N`) |
| `IS_OUTPUT` | `VARCHAR2(1)` |  | Indicates whether the task execution process sets the parameter value (`Y`) or not (`N`) |
| `IS_MODIFIABLE_ANYTIME` | `VARCHAR2(1)` |  | Indicates whether the parameter value can be modified when the task is not in its initial state (`Y`) or not (`N`) |
| `DESCRIPTION` | `VARCHAR2(4000)` |  | Optional description of the parameter |
| `PARAMETER_FLAGS` | `NUMBER` | `NOT NULL` | Reserved for internal use |
| `PARAMETER_TYPE#` | `NUMBER` | `NOT NULL` | Reserved for internal use |

See Also:

" [USER\_ADVISOR\_EXEC\_PARAMETERS](USER_ADVISOR_EXEC_PARAMETERS.md) "