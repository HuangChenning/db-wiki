---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_ADVISOR_SQLW_STMTS.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.46 DBA\_ADVISOR\_SQLW\_STMTS

`DBA_ADVISOR_SQLW_STMTS` displays rows that correspond to all statements in the workload.

All columns are guaranteed to be non-null.

Related View

`USER_ADVISOR_SQLW_STMTS` displays rows that correspond to the statements in the workload owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` |  | Owner of the workload object |
| `WORKLOAD_ID` | `NUMBER` | `NOT NULL` | Unique identifier number of the workload object |
| `WORKLOAD_NAME` | `VARCHAR2(128)` |  | Name of the workload |
| `SQL_ID` | `NUMBER` | `NOT NULL` | Generated identifier of the statement |
| `HASH_VALUE` | `NUMBER` |  | Hash value for the parent statement in the cache |
| `USERNAME` | `VARCHAR2(128)` |  | Name of the user executing the statement |
| `MODULE` | `VARCHAR2(64)` |  | Name of the module issuing the statement |
| `ACTION` | `VARCHAR2(64)` |  | Module action for the statement |
| `CPU_TIME` | `NUMBER` |  | Total CPU count (in seconds) of the executing statement |
| `BUFFER_GETS` | `NUMBER` |  | Total number of buffer gets for the statement |
| `DISK_READS` | `NUMBER` |  | Total disk-read I/O count for the statement |
| `ELAPSED_TIME` | `NUMBER` |  | Total elapsed time (in seconds) of the executing statement |
| `ROWS_PROCESSED` | `NUMBER` |  | Total number of rows processed by the statement |
| `EXECUTIONS` | `NUMBER` |  | Total number of times the statement was executed |
| `OPTIMIZER_COST` | `NUMBER` |  | Cost of executing the statement in the workload prior to the recommendations |
| `LAST_EXECUTION_DATE` | `DATE` |  | Date on which the statement was last executed |
| `PRIORITY` | `NUMBER` |  | Priority of the statement:  - `1` - High - `2` - Medium - `3` - Low |
| `COMMAND_TYPE` | `NUMBER` |  | Type of the command |
| `STAT_PERIOD` | `NUMBER` |  | Unused |
| `SQL_TEXT` | `CLOB` |  | Text of the SQL statement |
| `VALID` | `NUMBER` |  | Indicates whether the statement is valid for analysis:  - `0` - Statement will not be analyzed by the `EXECUTE_TASK` procedure. Typically, the statement references one or more tables that do not have valid statistics. To correct this problem, ensure that the tables have valid statistics and execute the `RESET_SQLWKLD` procedure on the current workload. - `1` - Statement is eligible for analysis by the `EXECUTE_TASK` procedure. |

See Also:

" [USER\_ADVISOR\_SQLW\_STMTS](USER_ADVISOR_SQLW_STMTS.md) "