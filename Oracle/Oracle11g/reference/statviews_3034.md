---
title: DBA_ADVISOR_SQLSTATS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_3034.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_ADVISOR_SQLSTATS` displays execution statistics for the test-execution of different SQL plans during the advisor analysis.

Related View

`USER_ADVISOR_SQLSTATS` displays execution statistics owned by the current user for the test-execution of different SQL plans during the advisor analysis.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `TASK_NAME` | `VARCHAR2(30)` |  | Advisor task name in which the SQL statement was executed (see `DBA_ADVISOR_TASKS`) |
| `TASK_ID` | `NUMBER(38)` | `NOT NULL` | Advisor task ID in which the SQL statement was executed (see `DBA_ADVISOR_TASKS`) |
| `EXECUTION_NAME` | `VARCHAR2(30)` | `NOT NULL` | Advisor task execution in which the SQL statement was executed (see `DBA_ADVISOR_EXECUTIONS`) |
| `EXECUTION_TYPE` | `VARCHAR2(30)` |  | Type of the advisor task execution in which the SQL statement was executed (see `DBA_ADVISOR_EXECUTIONS`) |
| `OBJECT_ID` | `NUMBER(38)` | `NOT NULL` | Advisor object ID identifying the relevant SQL statement (see `DBA_ADVISOR_OBJECTS`) |
| `PLAN_ID` | `NUMBER` | `NOT NULL` | Plan ID number generated to uniquely identify a plan for a particular SQL statement (foreign key to `DBA_ADVISOR_SQLPLANS`) |
| `SQL_ID` | `VARCHAR2(13)` | `NOT NULL` | Identifier for the SQL statement executed |
| `PLAN_HASH_VALUE` | `NUMBER` | `NOT NULL` | Hash value of the SQL execution plan |
| `ATTR1` | `NUMBER` |  | Reserved for internal use |
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
| `OTHER` | `CLOB` |  | Reserved for future use |
| `TESTEXEC_TOTAL_EXECS` | `NUMBER` |  | Total number of executions during test execute |
| `IO_INTERCONNECT_BYTES` | `NUMBER` |  | Number of I/O bytes exchanged between Oracle Database and the storage system |
| `TESTEXEC_FIRST_EXEC_IGNORED` | `VARCHAR2(1)` |  | Indicates whether the first execution in test execute is ignored (`Y`) or not (`N`) |