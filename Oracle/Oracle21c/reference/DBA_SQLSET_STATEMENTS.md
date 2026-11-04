---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_SQLSET_STATEMENTS.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.379 DBA\_SQLSET\_STATEMENTS

`DBA_SQLSET_STATEMENTS` displays information about the SQL statements, along with their statistics, that form all SQL tuning sets in the database. Its columns, except for `PARSING_SCHEMA_ID`, are the same as those in `ALL_SQLSET_STATEMENTS`.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SQLSET_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the SQL tuning set for the statement |
| `SQLSET_OWNER` | `VARCHAR2(128)` |  | User name of the SQL tuning set owner |
| `SQLSET_ID` | `NUMBER` | `NOT NULL` | ID of the SQL tuning set for the statement |
| `CON_DBID` | `NUMBER` | `NOT NULL` | The database ID of the PDB |
| `SQL_ID` | `VARCHAR2(13)` | `NOT NULL` | SQL identifier of the parent cursor in the library cache |
| `FORCE_MATCHING_SIGNATURE` | `NUMBER` | `NOT NULL` | The signature used when the `CURSOR_SHARING` parameter is set to `FORCE` |
| `SQL_TEXT` | `CLOB` |  | Full text for the SQL statement exposed as a CLOB column. |
| `PARSING_SCHEMA_NAME` | `VARCHAR2(128)` |  | Name of the user in whose schema the statement was parsed |
| `PARSING_SCHEMA_ID` | `NUMBER` |  | ID of the schema in which the statement was parsed |
| `PLAN_HASH_VALUE` | `NUMBER` | `NOT NULL` | Hash value for the plan corresponding to statistics in this record |
| `BIND_DATA` | `RAW(2000)` |  | Bind data |
| `BINDS_CAPTURED` | `CHAR(1)` |  | Binds captured |
| `MODULE` | `VARCHAR2(64)` |  | Contains the name of the module that was executing at the time that the SQL statement was first parsed, which is set by calling `DBMS_APPLICATION_INFO.SET_MODULE` |
| `ACTION` | `VARCHAR2(64)` |  | Contains the name of the action that was executing at the time that the SQL statement was first parsed, which is set by calling `DBMS_APPLICATION_INFO.SET_ACTION` |
| `ELAPSED_TIME` | `NUMBER` |  | Elapsed time (in microseconds) used by this cursor for parsing, executing, and fetching |
| `CPU_TIME` | `NUMBER` |  | CPU time (in microseconds) used by this cursor for parsing, executing, and fetching |
| `BUFFER_GETS` | `NUMBER` |  | Number of buffer gets for this child cursor |
| `DISK_READS` | `NUMBER` |  | Number of disk reads for this child cursor |
| `DIRECT_WRITES` | `NUMBER` |  | Number of direct writes for this child cursor |
| `ROWS_PROCESSED` | `NUMBER` |  | Total number of rows that the parsed SQL statement returns |
| `FETCHES` | `NUMBER` |  | Number of fetches associated with the SQL statement |
| `EXECUTIONS` | `NUMBER` |  | Number of executions that took place on this object since it was brought into the library cache |
| `END_OF_FETCH_COUNT` | `NUMBER` |  | Number of times this cursor was fully executed since the cursor was brought into the library cache. The value of this statistic in not incremented when the cursor is partially executed, either because it failed during the execution or because only the first few rows produced by this cursor are fetched before the cursor is closed or re-executed. By definition, the value of the `END_OF_FETCH_COUNT` column should be less than, or equal to, the value of the `EXECUTIONS` column. |
| `OPTIMIZER_COST` | `NUMBER` |  | Cost of this query, given by the optimizer |
| `OPTIMIZER_ENV` | `RAW(2000)` |  | Optimizer environment |
| `PRIORITY` | `NUMBER` |  | User-defined priority |
| `COMMAND_TYPE` | `NUMBER` |  | Oracle command type definition |
| `FIRST_LOAD_TIME` | `VARCHAR2(19)` |  | Timestamp of the parent creation time |
| `STAT_PERIOD` | `NUMBER` |  | Period of time (in seconds) during which the statistics of the SQL statement were collected |
| `ACTIVE_STAT_PERIOD` | `NUMBER` |  | Effective period of time (in seconds) during which the SQL statement was active |
| `OTHER` | `CLOB` |  | Client data, specified by the user, for this statement |
| `PLAN_TIMESTAMP` | `DATE` |  | Timestamp for the plan corresponding to the statistics in this record |
| `SQL_SEQ` | `NUMBER` | `NOT NULL` | SQL sequence |
| `LAST_EXEC_START_TIME` | `VARCHAR2(19)` |  | For SQLs captured from the cursor cache, this is the time when the most recent execution of this SQL started |

See Also:

- " [ALL\_SQLSET\_STATEMENTS](ALL_SQLSET_STATEMENTS.md) "
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ARPLS65239) for more information about the `DBMS_APPLICATION_INFO.SET_MODULE` procedure
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ARPLS65235) for more information about the `DBMS_APPLICATION_INFO.SET_ACTION` procedure