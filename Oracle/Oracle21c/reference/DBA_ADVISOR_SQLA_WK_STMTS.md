---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_ADVISOR_SQLA_WK_STMTS.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.41 DBA\_ADVISOR\_SQLA\_WK\_STMTS

`DBA_ADVISOR_SQLA_WK_STMTS` displays information about all workload objects in the database after an Access Advisor analysis operation.

Related View

`USER_ADVISOR_SQLA_WK_STMTS` displays information about the workload objects owned by the current user after an Access Advisor analysis operation. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` |  | Owner of the task |
| `TASK_NAME` | `VARCHAR2(128)` |  | Name of the task |
| `TASK_ID` | `NUMBER` | `NOT NULL` | Unique identifier of the task |
| `SQLSET_ID` | `NUMBER` |  | ID of the SQL tuning set for the statement |
| `SQLSET_NAME` | `VARCHAR2(128)` |  | Name of the SQL tuning set for the statement |
| `WORKLOAD_NAME` | `VARCHAR2(128)` |  | Name of the workload |
| `SQL_ID` | `VARCHAR(13)` | `NOT NULL` | Generated identifier of the statement |
| `SQL_SEQ` | `NUMBER` | `NOT NULL` | SQL sequence |
| `PLAN_HASH_VALUE` | `NUMBER` | `NOT NULL` | Numerical representation of the SQL plan for the cursor. Comparing one `PLAN_HASH_VALUE` to another easily identifies whether or not two plans are the same (rather than comparing the two plans line-by-line). |
| `PARSING_SCHEMA_NAME` | `VARCHAR2(128)` |  | Schema name that was used to originally build this child cursor |
| `USERNAME` | `VARCHAR2(128)` |  | Name of the user executing the statement |
| `MODULE` | `VARCHAR2(64)` |  | Name of the module issuing the statement |
| `ACTION` | `VARCHAR2(64)` |  | Module action for the statement |
| `CPU_TIME` | `NUMBER` |  | Total CPU count (in seconds) of the executing statement |
| `BUFFER_GETS` | `NUMBER` |  | Total number of buffer gets for the statement |
| `DISK_READS` | `NUMBER` |  | Total disk-read I/O count for the statement |
| `ELAPSED_TIME` | `NUMBER` |  | Total elapsed time (in seconds) of the executing statement |
| `ROWS_PROCESSED` | `NUMBER` |  | Total number of rows processed by the statement |
| `EXECUTIONS` | `NUMBER` |  | Total number of times the statement was executed |
| `FIRST_LOAD_TIME` | `DATE` |  | Load time of parent cursor |
| `LAST_EXECUTION_DATE` | `DATE` |  | Date on which the statement was last executed |
| `PRIORITY` | `NUMBER` |  | Business importance of the statement:  - `1` - High - `2` - Medium - `3` - Low |
| `COMMAND_TYPE` | `NUMBER` |  | Type of the command |
| `STAT_PERIOD` | `NUMBER` |  | Unused |
| `ACTIVE_STAT_PERIOD` | `NUMBER` |  | Effective period of time (in seconds) during which the SQL statement was active |
| `SQL_TEXT` | `CLOB` |  | Text of the SQL statement |
| `PRECOST` | `NUMBER` |  | Cost of executing the statement in the workload prior to the recommendations |
| `POSTCOST` | `NUMBER` |  | Cost of executing the statement in the workload after the recommendations |
| `IMPORTANCE` | `NUMBER` |  | Advisor-calculated importance value |
| `REC_ID` | `NUMBER` |  | Associated recommendation identifier |
| `VALIDATED` | `NUMBER` |  | Indicates whether the statement is valid for analysis:  - `0` - Statement will not be analyzed by the `EXECUTE_TASK` procedure. Typically, the statement references one or more tables that do not have valid statistics. To correct this problem, ensure that the tables have valid statistics and execute the `RESET_SQLWKLD` procedure on the current workload. - `1` - Statement is eligible for analysis by the `EXECUTE_TASK` procedure |

See Also:

" [USER\_ADVISOR\_SQLA\_WK\_STMTS](USER_ADVISOR_SQLA_WK_STMTS.md) "