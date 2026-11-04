---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_ADVISOR_PARAMETERS.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.35 DBA\_ADVISOR\_PARAMETERS

`DBA_ADVISOR_PARAMETERS` displays all task parameters and their current values in the database.

This data is accessible by all tasks.

Related View

`USER_ADVISOR_PARAMETERS` displays the task parameters and their current values for the tasks owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` |  | Owner of the task or workload object |
| `TASK_ID` | `NUMBER` | `NOT NULL` | Unique identifier number of the task or workload object |
| `TASK_NAME` | `VARCHAR2(128)` |  | Name of the task or workload object |
| `PARAMETER_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the parameter |
| `PARAMETER_VALUE` | `VARCHAR2(4000)` | `NOT NULL` | Value of the parameter. Numeric parameter values are converted to a string equivalent.  Possible keywords as values:  - `ALL` - `UNLIMITED` - `UNUSED` |
| `PARAMETER_TYPE` | `VARCHAR2(10)` |  | Datatype of the parameter:  - `NUMBER` - Numeric value - `STRING` - String value. If the string contains special characters, then it will be enclosed in single quotes. - `STRINGLIST` - Comma-separated list of string elements. If a string element contains a comma or other special characters, then the element will be enclosed in single quotes. - `TABLE` - Single table reference. A reference will contain a schema name, followed by an optional table name. 	If the table name is omitted or is the character `%`, then the table name is interpreted as a wildcard. SQL quoted identifiers are supported. - `TABLELIST` - List of one or more comma-separated table references. A reference will contain schema name, followed by an optional table name. 	If the table name is omitted or is the character `%`, then the table name is interpreted as a wildcard. SQL quoted identifiers are supported. |
| `IS_DEFAULT` | `VARCHAR2(1)` |  | Indicates whether the parameter value is set to the advisor's default value (`Y`) or not (`N`) |
| `IS_OUTPUT` | `VARCHAR2(1)` |  | Indicates whether the task execution process sets the parameter value (`Y`) or not (`N`) |
| `IS_MODIFIABLE_ANYTIME` | `VARCHAR2(1)` |  | Indicates whether the parameter value can be modified when the task is not in its initial state (`Y`) or not (`N`) |
| `DESCRIPTION` | `VARCHAR2(4000)` |  | Optional description of the parameter |
| `EXECUTION_TYPE` | `VARCHAR2(128)` |  | For advisors supporting multiple executions, the type of execution this parameter pertains to |

See Also:

" [USER\_ADVISOR\_PARAMETERS](USER_ADVISOR_PARAMETERS.md) "