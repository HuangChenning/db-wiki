---
title: ALL_SQLSET_STATEMENTS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2074.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_SQLSET_STATEMENTS` displays information about the SQL statements, along with their statistics, that form all SQL tuning sets accessible to the current user.

Related Views

- `DBA_SQLSET_STATEMENTS` displays information about the SQL statements, along with their statistics, that form all SQL tuning sets in the database. This view does not display the `SQL_SEQ` column.
- `USER_SQLSET_STATEMENTS` displays information about the SQL statements, along with their statistics, that form the SQL tuning sets owned by the current user. This view does not display the `SQLSET_OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SQLSET_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the SQL tuning set for the statement |
| `SQLSET_ID` | `NUMBER` | `NOT NULL` | ID of the SQL tuning set for the statement |
| `SQLSET_OWNER` | `VARCHAR2(30)` |  | User name of the SQL tuning set owner |
| `SQL_ID` | `VARCHAR2(13)` | `NOT NULL` | SQL identifier of the parent cursor in the library cache |
| `FORCE_MATCHING_SIGNATURE` | `NUMBER` | `NOT NULL` | The signature used when the `CURSOR_SHARING` parameter is set to `FORCE` |
| `SQL_TEXT` | `CLOB` |  | Full text for the SQL statement exposed as a CLOB column. |
| `PLAN_HASH_VALUE` | `NUMBER` | `NOT NULL` | Hash value for the plan corresponding to statistics in this record |
| `PARSING_SCHEMA_NAME` | `VARCHAR2(30)` |  | Name of the user in whose schema the statement was parsed |
| `BIND_DATA` | `RAW(2000)` |  | Bind data |
| `BINDS_CAPTURED` | `CHAR(1)` |  | Binds captured |
| `MODULE` <sup>Foot 1</sup> | `VARCHAR2(48)` |  | Contains the name of the module that was executing at the time that the SQL statement was first parsed, which is set by calling `DBMS_APPLICATION_INFO.SET_MODULE` |
| `ACTION` <sup>Footref 1</sup> | `VARCHAR2(32)` |  | Contains the name of the action that was executing at the time that the SQL statement was first parsed, which is set by calling `DBMS_APPLICATION_INFO.SET_ACTION` |
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
| `OPTIMIZER_ENV` | `RAW(1000)` |  | Optimizer environment |
| `PRIORITY` | `NUMBER` |  | User-defined priority |
| `COMMAND_TYPE` | `NUMBER` |  | Oracle command type definition |
| `FIRST_LOAD_TIME` | `VARCHAR2(19)` |  | Timestamp of the parent creation time |
| `STAT_PERIOD` | `NUMBER` |  | Period of time (in seconds) during which the statistics of the SQL statement were collected |
| `ACTIVE_STAT_PERIOD` | `NUMBER` |  | Effective period of time (in seconds) during which the SQL statement was active |
| `OTHER` | `CLOB` |  | Client data, specified by the user, for this statement |
| `PLAN_TIMESTAMP` | `DATE` |  | Timestamp for the plan corresponding to the statistics in this record |
| `SQL_SEQ` | `NUMBER` | `NOT NULL` | SQL sequence |

<sup>Footnote 1</sup> The datatype of this column is `VARCHAR2(64)` starting with Oracle Database 11g Release 2 (11.2.0.2).