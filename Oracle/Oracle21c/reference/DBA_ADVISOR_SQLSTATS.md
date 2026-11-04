---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_ADVISOR_SQLSTATS.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.43 DBA\_ADVISOR\_SQLSTATS

`DBA_ADVISOR_SQLSTATS` displays execution statistics for the test-execution of different SQL plans during the advisor analysis.

Related View

`USER_ADVISOR_SQLSTATS` displays execution statistics owned by the current user for the test-execution of different SQL plans during the advisor analysis.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `TASK_NAME` | `VARCHAR2(128)` |  | Advisor task name in which the SQL statement was executed (see `DBA_ADVISOR_TASKS`) |
| `TASK_ID` | `NUMBER(38)` | `NOT NULL` | Advisor task ID in which the SQL statement was executed (see `DBA_ADVISOR_TASKS`) |
| `EXECUTION_NAME` | `VARCHAR2(128)` | `NOT NULL` | Advisor task execution in which the SQL statement was executed (see `DBA_ADVISOR_EXECUTIONS`) |
| `EXECUTION_TYPE` | `VARCHAR2(128)` |  | Type of the advisor task execution in which the SQL statement was executed (see `DBA_ADVISOR_EXECUTIONS`) |
| `OBJECT_ID` | `NUMBER(38)` | `NOT NULL` | Advisor object ID identifying the relevant SQL statement (see `DBA_ADVISOR_OBJECTS`) |
| `PLAN_ID` | `NUMBER` | `NOT NULL` | Plan ID number generated to uniquely identify a plan for a particular SQL statement (foreign key to `DBA_ADVISOR_SQLPLANS`) |
| `SQL_ID` | `VARCHAR2(13)` | `NOT NULL` | Identifier for the SQL statement executed |
| `PLAN_HASH_VALUE` | `NUMBER` | `NOT NULL` | Hash value of the SQL execution plan |
| `ATTR1` | `NUMBER` |  | For internal use only |
| `CON_DBID` | `NUMBER` |  | The database ID of the pluggable database (PDB) |
| `PARSE_TIME` | `NUMBER` |  | Parse time (in microseconds) measured for the SQL |
| `ELAPSED_TIME` | `NUMBER` |  | Elapsed time (in microseconds) to execute the SQL and fetch all of its rows, after parsing |
| `CPU_TIME` | `NUMBER` |  | CPU time (in microseconds) to execute the SQL and fetch all of its rows, after parsing |
| `USER_IO_TIME` | `NUMBER` |  | I/O time (in microseconds) to execute the SQL and fetch all of its rows, after parsing |
| `BUFFER_GETS` | `NUMBER` |  | Number of buffer gets measured for executing the SQL and fetching all of its rows |
| `DISK_READS` | `NUMBER` |  | Number of disk reads measured for executing the SQL and fetching all of its rows |
| `DIRECT_WRITES` | `NUMBER` |  | Number of direct writes measured for executing the SQL and fetching all of its rows |
| `PHYSICAL_READ_REQUESTS` | `NUMBER` |  | Number of physical read I/O requests issued by the monitored SQL |
| `PHYSICAL_WRITE_REQUESTS` | `NUMBER` |  | Number of physical write I/O requests issued by the monitored SQL |
| `PHYSICAL_READ_BYTES` | `NUMBER` |  | Number of bytes read from disks by the monitored SQL |
| `PHYSICAL_WRITE_BYTES` | `NUMBER` |  | Number of bytes written to disks by the monitored SQL |
| `ROWS_PROCESSED` | `NUMBER` |  | Number of rows returned by the SQL execution |
| `FETCHES` | `NUMBER` |  | Number of fetches for the SQL execution |
| `EXECUTIONS` | `NUMBER` |  | Execution count for the SQL. This column will always have a value of `1` or `0`. |
| `END_OF_FETCH_COUNT` | `NUMBER` |  | Indicates whether the SQL was executed to end-of-fetch (`1`) or not (`0`) |
| `OPTIMIZER_COST` | `NUMBER` |  | Optimizer cost for the execution plan |
| `OTHER` | `CLOB` |  | For internal use only |
| `TESTEXEC_TOTAL_EXECS` | `NUMBER` |  | Total number of executions during test execute |
| `IO_INTERCONNECT_BYTES` | `NUMBER` |  | Number of I/O bytes exchanged between Oracle Database and the storage system |
| `TESTEXEC_FIRST_EXEC_IGNORED` | `VARCHAR2(1)` |  | Indicates whether the first execution in test execute is ignored (`Y`) or not (`N`) |
| `CON_DBID` | `NUMBER` |  | The database ID of the PDB |
| `ATTR2` | `NUMBER` |  | For internal use only |
| `ATTR3` | `NUMBER` |  | For internal use only |
| `CACHED_GETS` | `NUMBER` |  | The total of the db block gets from cache statistic and the consistent gets from cache statistic |
| `DIRECT_GETS` | `NUMBER` |  | The total of the db block gets direct statistic and the consistent gets direct statistic |
| `EXECUTIONS_ORIGINAL` | `NUMBER` |  | Number of original executions from the SQL tuning set, independent of trial executions |
| `OBJECT_FLAGS` | `NUMBER` |  | Value of the flags from the execution of the SQL, such as timeout or error |

See Also:

- " [USER\_ADVISOR\_SQLSTATS](USER_ADVISOR_SQLSTATS.md) "
- " [Statistics Descriptions](statistics-descriptions-2.md) " for more information about statistics