---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-SQL_MONITOR.html
tags:
  - oracle
  - 21c
  - reference
---

## 10.55 V$SQL\_MONITOR

`V$SQL_MONITOR` displays SQL statements whose execution have been (or are being) monitored by Oracle.

This view contains global, high-level information about simple and composite database operations.

Oracle Database monitors simple database operations, which are top SQL statements and PL/SQL subprograms, when any of the following conditions is true:

- The operations run in parallel.
- The operations have consumed at least 5 seconds of CPU or I/O time in a single execution.
- Tracking for the operations is forced by the /\*+ MONITOR \*/ hint.

For simple database operations, monitoring statistics are not cumulative over several executions. In this case, one entry in `V$SQL_MONITOR` is dedicated to a single execution of a SQL statement. If the database monitors two executions of the same SQL statement, then each execution has a separate entry in `V$SQL_MONITOR`.

For simple database operations, `V$SQL_MONITOR` has one entry for the parallel execution coordinator process and one entry for each parallel execution server process. Each entry has corresponding entries in `V$SQL_PLAN_MONITOR`. Because the processes allocated for the parallel execution of a SQL statement are cooperating for the same execution, these entries share the same execution key (the combination of `SQL_ID`, `SQL_EXEC_START`, and `SQL_EXEC_ID`).

Oracle Database monitors composite database operations when either of the following conditions is true:

- A database operation was started with `DBMS_SQL_MONITOR.BEGIN_OPERATION` and the operation has consumed at least 5 seconds of CPU or I/O time.
- Tracking for the operation is forced by setting `FORCE_TRACKING` to `Y` in `DBMS_SQL_MONITOR.BEGIN_OPERATION`.

For composite database operations, each row contains an operation whose statistics are accumulated over the SQL statements and PL/SQL subprograms that run in the same session as part of the operation.

The ` V$SQL_MONITOR` view contains a subset of the statistics available in `V$SQL`. However, unlike `V$SQL`, monitoring statistics are not cumulative over several executions. Instead, one entry in `V$SQL_MONITOR` is dedicated to a single execution of a SQL statement. If the database monitors two executions of the same SQL statement, then each execution has a separate entry in `V$SQL_MONITOR`.

The primary key is the combination of the columns `SQL_ID`, `SQL_EXEC_START`, and `SQL_EXEC_ID`.

`V$SQL_MONITOR` has one entry for the parallel execution coordinator process, and one entry for each parallel execution server process. Each entry has corresponding entries in `V$SQL_PLAN_MONITOR`. Because the processes allocated for the parallel execution of a SQL statement are cooperating for the same execution, these entries share the same execution key (the composite `SQL_ID`, `SQL_EXEC_START`, and `SQL_EXEC_ID`). You can aggregate the execution key to determine the overall statistics for a parallel execution.

When the SQL statement being monitored is executing, statistics in `V$SQL_MONITOR` are generally refreshed in near real time, once every second. Once the execution ends, monitoring information is not deleted immediately. Instead, it is kept in `V$SQL_MONITOR` for at least one minute. The entry will eventually be deleted to reclaim its space as new statements are monitored.

| Column | Datatype | Description |
| --- | --- | --- |
| `KEY` | `NUMBER` | Artificial join key to efficiently join `V$SQL_MONITOR` with its corresponding plan level monitoring statistics stored in `V$SQL_PLAN_MONITOR` |
| `REPORT_ID` | `NUMBER` | Unique ID of the XML report stored in Automatic Workload Repository (AWR) for this monitored entity |
| `STATUS` | `VARCHAR2(19)` | SQL execution status:  - `QUEUED` - SQL statement is queued - `EXECUTING` - SQL statement is still executing - `DONE (ERROR)` - Execution terminated with an error - `DONE (FIRST N ROWS)` - Execution terminated by the application before all rows were fetched - `DONE (ALL ROWS)` - Execution terminated and all rows were fetched - `DONE` - Execution terminated (parallel execution) |
| `USER#` | `NUMBER` | User ID of the database user who issued the SQL being monitored |
| `USERNAME` | `VARCHAR2(128)` | User name of the database user who issued the SQL being monitored |
| `MODULE` | `VARCHAR2(64)` | Name of the executing module when sampled, as set by the `DBMS_APPLICATION_INFO.SET_MODULE` procedure |
| `ACTION` | `VARCHAR2(64)` | Name of the executing action when sampled, as set by the `DBMS_APPLICATION_INFO.SET_ACTION` procedure |
| `SERVICE_NAME` | `VARCHAR2(64)` | Service name of the user session |
| `CLIENT_IDENTIFIER` | `VARCHAR2(64)` | Client identifier from the user session |
| `CLIENT_INFO` | `VARCHAR2(64)` | Client information for the user session |
| `PROGRAM` | `VARCHAR2(84)` | Name of the operating system program that issued the monitored SQL |
| `PLSQL_ENTRY_OBJECT_ID` | `NUMBER` | Object ID of the top-most PL/SQL subprogram on the stack; NULL if there is no PL/SQL subprogram on the stack |
| `PLSQL_ENTRY_SUBPROGRAM_ID` | `NUMBER` | Subprogram ID of the top-most PL/SQL subprogram on the stack; NULL if there is no PL/SQL subprogram on the stack |
| `PLSQL_OBJECT_ID` | `NUMBER` | Object ID of the currently executing PL/SQL subprogram; NULL if executing SQL |
| `PLSQL_SUBPROGRAM_ID` | `NUMBER` | Subprogram ID of the currently executing PL/SQL object; NULL if executing SQL |
| `FIRST_REFRESH_TIME` | `DATE` | Time when monitoring of the SQL statement started, generally a few seconds after execution start time |
| `LAST_REFRESH_TIME` | `DATE` | Time when statistics in `V$SQL_MONITOR` were last updated for the SQL statement. Statistics are generally refreshed every second when the statement executes. |
| `REFRESH_COUNT` | `NUMBER` | Number of times `V$SQL_MONITOR` statistics have been refreshed (generally once every second when the SQL statement executes) |
| `DBOP_EXEC_ID` | `NUMBER` | Database operation execution identifier for the current execution. If the type is SQL, the `DBOP_EXEC_ID` will be `NULL`. |
| `DBOP_NAME` | `VARCHAR2(30)` | Database operation name. If the type is SQL, the `DBOP_NAME` will be `NULL`. |
| `SID` | `NUMBER` | Session identifier executing (or having executed) the SQL statement being monitored |
| `PROCESS_NAME` | `VARCHAR2(5)` | Process name identifier executing (or having executed)the statement; `ora` if the process is foreground, else the background process name (for example, `p001` for PX server p001) |
| `SQL_ID` | `VARCHAR2(13)` | SQL identifier of the statement being monitored |
| `SQL_TEXT` | `VARCHAR2(2000)` | Up to the first 2000 characters of the text of the SQL being monitored |
| `IS_FULL_SQLTEXT` | `VARCHAR2(1)` | Indicates whether the `SQL_TEXT` column has the entire SQL text (`Y`) or not (`N`) |
| `SQL_EXEC_START` | `DATE` | Time when the execution started |
| `SQL_EXEC_ID` | `NUMBER` | Execution identifier. Together, the three columns `SQL_ID`, `SQL_EXEC_START`, and `SQL_EXEC_ID` represent the execution key. The execution key is used to uniquely identify one execution of the SQL statement. |
| `SQL_PLAN_HASH_VALUE` | `NUMBER` | SQL plan hash value |
| `SQL_FULL_PLAN_HASH_VALUE` | `NUMBER` | Numeric representation of the complete SQL plan for this cursor. Comparing one `SQL_FULL_PLAN_HASH_VALUE` to another easily identifies whether or not two plans are the same (rather than comparing the two plans line by line). Note that the `SQL_FULL_PLAN_HASH_VALUE` cannot be compared across databases releases. It is not backward compatible. |
| `EXACT_MATCHING_SIGNATURE` | `NUMBER` | Signature calculated on the normalized SQL text. The normalization includes the removal of white space and the uppercasing of all non-literal strings. |
| `FORCE_MATCHING_SIGNATURE` | `NUMBER` | Same as `EXACT_MATCHING_SIGNATURE` but literals in the SQL text are replaced by binds |
| `SQL_CHILD_ADDRESS` | `RAW(4 \| 8)` | Address of the child cursor (can be used with `SQL_ID` to join with `V$SQL`) |
| `SESSION_SERIAL#` | `NUMBER` | Session serial number executing the statement being monitored |
| `PX_IS_CROSS_INSTANCE` | `VARCHAR2(1)` | Indicates whether the SQL statement ran parallel across multiple instances (`Y`) or not (`N`) |
| `PX_MAXDOP` | `NUMBER` | Maximum degree of parallelism for any plan operation executed on behalf of the monitored SQL |
| `PX_MAXDOP_INSTANCES` | `NUMBER` | Number of database instances touched at the maximum degree of parallelism |
| `PX_SERVERS_REQUESTED` | `NUMBER` | Total number of parallel execution servers requested to execute the monitored SQL |
| `PX_SERVERS_ALLOCATED` | `NUMBER` | Actual number of parallel execution servers allocated to execute the query |
| `PX_SERVER#` | `NUMBER` | Logical parallel execution server process number executing (or having executed) the statement being monitored; NULL if this monitoring entry is not associated with an execution server. This is a logical number within the parallel server set (see `SERVER#` in `V$PX_SESSION`). |
| `PX_SERVER_GROUP` | `NUMBER` | Logical parallel execution server group number to which `PX_SERVER#` belongs (see `SERVER_GROUP` in `V$PX_SESSION`); NULL if this monitoring entry is not associated with a parallel execution server. This value is generally `1` unless the SQL statement has one or more parallel sub-queries. |
| `PX_SERVER_SET` | `NUMBER` | Number (`1` or `2`) of the logical set of parallel execution servers to which `PX_SERVER#` belongs (see `SERVER_SET` in `V$PX_SESSION`); NULL if this monitoring entry is not associated with a parallel execution server |
| `PX_QCINST_ID` | `NUMBER` | Instance identifier where the parallel execution coordinator runs; NULL if `PX_SERVER#` is NULL |
| `PX_QCSID` | `NUMBER` | Session identifier for the parallel execution coordinator; NULL if `PX_SERVER#` is NULL |
| `ERROR_NUMBER` | `VARCHAR2(40)` | Error number encountered in case a SQL fails to execute successfully (for example, 932 in case of ORA-00932) |
| `ERROR_FACILITY` | `VARCHAR2(4)` | Error facility in case a SQL fails to execute successfully (for example, ORA in case of ORA-00932) |
| `ERROR_MESSAGE` | `VARCHAR2(256)` | Detailed error message displayed corresponding to the error number and error facility when a SQL fails to execute successfully |
| `BINDS_XML` | `CLOB` | Information about bind variables used with the SQL, such as name, position, value, data type, and so on (stored in XML format) |
| `OTHER_XML` | `CLOB` | Additional information about SQL execution stored in XML format |
| `ELAPSED_TIME` | `NUMBER` | Elapsed time (in microseconds); updated as the statement executes |
| `QUEUING_TIME` | `NUMBER` | Duration of time (in microseconds) spent by SQL in the statement queue |
| `CPU_TIME` | `NUMBER` | CPU time (in microseconds); updated as the statement executes |
| `FETCHES` | `NUMBER` | Number of fetches associated with the SQL statement; updated as the statement executes |
| `BUFFER_GETS` | `NUMBER` | Number of buffer get operations; updated as the statement executes |
| `DISK_READS` | `NUMBER` | Number of disk reads; updated as the statement executes |
| `DIRECT_WRITES` | `NUMBER` | Number of direct writes; updated as the statement executes |
| `IO_INTERCONNECT_BYTES` | `NUMBER` | Number of I/O bytes exchanged between Oracle Database and the storage system |
| `PHYSICAL_READ_REQUESTS` | `NUMBER` | Number of physical read I/O requests issued by the monitored SQL |
| `PHYSICAL_READ_BYTES` | `NUMBER` | Number of bytes read from disks by the monitored SQL |
| `PHYSICAL_WRITE_REQUESTS` | `NUMBER` | Number of physical write I/O requests issued by the monitored SQL |
| `PHYSICAL_WRITE_BYTES` | `NUMBER` | Number of bytes written to disks by the monitored SQL |
| `APPLICATION_WAIT_TIME` | `NUMBER` | Application wait time (in microseconds); updated as the statement executes |
| `CONCURRENCY_WAIT_TIME` | `NUMBER` | Concurrency wait time (in microseconds); updated as the statement executes |
| `CLUSTER_WAIT_TIME` | `NUMBER` | Cluster wait time (in microseconds); updated as the statement executes |
| `USER_IO_WAIT_TIME` | `NUMBER` | User I/O Wait Time (in microseconds); updated as the statement executes |
| `PLSQL_EXEC_TIME` | `NUMBER` | PL/SQL execution time (in microseconds); updated as the statement executes |
| `JAVA_EXEC_TIME` | `NUMBER` | Java execution time (in microseconds); updated as the statement executes |
| `RM_LAST_ACTION` | `VARCHAR2(48)` | The most recent action that was taken on this SQL operation by Resource Manager. Its value is one of the following:  - `CANCEL_SQL` - `KILL_SESSION` - `LOG_ONLY` - `SWITCH TO <CG NAME>`  For the last value, \<CG NAME> is the name of the consumer group that the SQL operation was switched to. If the Resource Plan has since been changed then \<CG NAME> is the ID of the consumer group. |
| `RM_LAST_ACTION_REASON` | `VARCHAR2(128)` | The reason for the most recent action that was taken on this SQL operation by Resource Manager. Its value is one of the following:  - `SWITCH_CPU_TIME` - `SWITCH_IO_REQS` - `SWITCH_IO_MBS` - `SWITCH_ELAPSED_TIME` - `SWITCH_IO_LOGICAL` |
| `RM_LAST_ACTION_TIME` | `DATE` | The time of the most recent action that was taken on this SQL operation by Resource Manager |
| `RM_CONSUMER_GROUP` | `VARCHAR2(128)` | The current consumer group for this SQL operation |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |
| `CON_NAME` | `VARCHAR2(128)` | Container name of the object. The value of this column is NULL in non-CDBs. |
| `ECID` | `VARCHAR2(64)` | Execution context identifier (sent by Application Server) |
| `IS_ADAPTIVE_PLAN` | `VARCHAR2(1)` | Indicates whether the statistics are from an adaptive plan (Y) or not (N). |
| `IS_FINAL_PLAN` | `VARCHAR2(1)` | Indicates whether the statistics are from the final plan (Y) or not (N). |
| `IN_DBOP_NAME` | `VARCHAR2(30)` | If the SQL that is monitored was executed by a session that was also monitored by a database operation (DBOP), then this column specifies the name of that DBOP |
| `IN_DBOP_EXEC_ID` | `NUMBER` | If the SQL that is monitored was executed by a session that was also monitored by a database operation (DBOP), then this column specifies the execution ID of that DBO |
| `IO_CELL_UNCOMPRESSED_BYTES` | `NUMBER` | Number of uncompressed bytes (that is, size after decompression) that are offloaded to the Exadata cells  See Also: Oracle Exadata Storage Server Software documentation for more information |
| `IO_CELL_OFFLOAD_ELIGIBLE_BYTES` | `NUMBER` | Number of I/O bytes which can be filtered by the Exadata storage system  See Also: Oracle Exadata Storage Server Software documentation for more information |
| `IO_CELL_OFFLOAD_RETURNED_BYTES` | `NUMBER` | Number of filtered bytes returned by Exadata cells (that is, the number of bytes returned after processing has been offloaded on the Exadata cells)  See Also: Oracle Exadata Storage Server Software documentation for more information |
| `CURRENT_USER#` | `NUMBER` | Unique number identifying the current user |
| `CURRENT_USERNAME` | `VARCHAR2(128)` | Username for the current user |

See Also:

- " [V$SQL\_PLAN\_MONITOR](V-SQL_PLAN_MONITOR.md) "
- " [V$ALL\_SQL\_MONITOR](V-ALL_SQL_MONITOR.md) "
- [Oracle Database SQL Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=TGSQL-GUID-C941CE9D-97E1-42F8-91ED-4949B2B710BF) for more information about monitoring database operations
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ARPLS65239) for more information about the `DBMS_APPLICATION_INFO.SET_MODULE` procedure
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ARPLS65235) for more information about the `DBMS_APPLICATION_INFO.SET_ACTION` procedure