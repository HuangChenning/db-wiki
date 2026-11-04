---
title: "V$SQL_MONITOR"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_3052.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$SQL_MONITOR` displays SQL statements whose execution have been (or are being) monitored by Oracle. An entry is created in `V$SQL_MONITOR` every time the execution of a SQL statement is being monitored. SQL monitoring is automatically started when a SQL statement runs parallel or when it has consumed at least 5 seconds of CPU or I/O time.

When the SQL statement being monitored is executing, statistics in `V$SQL_MONITOR` are generally refreshed in near real time, once every second. Once the execution ends, monitoring information is not deleted immediately. Instead, it is kept in `V$SQL_MONITOR` for at least one minute. The entry will eventually be deleted to reclaim its space as new statements are monitored.

| Column | Datatype | Description |
| --- | --- | --- |
| `KEY` | `NUMBER` | Artificial join key to efficiently join `V$SQL_MONITOR` with its corresponding plan level monitoring statistics stored in `V$SQL_PLAN_MONITOR` |
| `STATUS` | `VARCHAR2(19)` | SQL execution status: - `QUEUED` - SQL statement is queued - `EXECUTING` - SQL statement is still executing - `DONE (ERROR)` - Execution terminated with an error - `DONE (FIRST N ROWS)` - Execution terminated by the application before all rows were fetched - `DONE (ALL ROWS)` - Execution terminated and all rows were fetched - `DONE` - Execution terminated (parallel execution) |
| `USER#` | `NUMBER` | User ID of the database user who issued the SQL being monitored |
| `USERNAME` | `VARCHAR2(30)` | User name of the database user who issued the SQL being monitored |
| `MODULE` <sup>Foot 1</sup> | `VARCHAR2(64)` | Name of the executing module when sampled, as set by the `DBMS_APPLICATION_INFO.SET_MODULE` procedure |
| `ACTION` <sup>Footref 1</sup> | `VARCHAR2(64)` | Name of the executing action when sampled, as set by the `DBMS_APPLICATION_INFO.SET_ACTION` procedure |
| `SERVICE_NAME` | `VARCHAR2(64)` | Service name of the user session |
| `CLIENT_IDENTIFIER` | `VARCHAR2(64)` | Client identifier from the user session |
| `CLIENT_INFO` | `VARCHAR2(64)` | Client information for the user session |
| `PROGRAM` | `VARCHAR2(48)` | Name of the OS program that issued the monitored SQL |
| `PLSQL_ENTRY_OBJECT_ID` | `NUMBER` | Object ID of the top-most PL/SQL subprogram on the stack; NULL if there is no PL/SQL subprogram on the stack |
| `PLSQL_ENTRY_SUBPROGRAM_ID` | `NUMBER` | Subprogram ID of the top-most PL/SQL subprogram on the stack; NULL if there is no PL/SQL subprogram on the stack |
| `PLSQL_OBJECT_ID` | `NUMBER` | Object ID of the currently executing PL/SQL subprogram; NULL if executing SQL |
| `PLSQL_SUBPROGRAM_ID` | `NUMBER` | Subprogram ID of the currently executing PL/SQL object; NULL if executing SQL |
| `FIRST_REFRESH_TIME` | `DATE` | Time when monitoring of the SQL statement started, generally a few seconds after execution start time |
| `LAST_REFRESH_TIME` | `DATE` | Time when statistics in `V$SQL_MONITOR` were last updated for the SQL statement. Statistics are generally refreshed every second when the statement executes. |
| `REFRESH_COUNT` | `NUMBER` | Number of times `V$SQL_MONITOR` statistics have been refreshed (generally once every second when the SQL statement executes) |
| `SID` | `NUMBER` | Session identifier executing (or having executed) the SQL statement being monitored |
| `PROCESS_NAME` | `VARCHAR2(5)` | Process name identifier executing (or having executed)the statement; `ora` if the process is foreground, else the background process name (for example, `p001` for PX server p001) |
| `SQL_ID` | `VARCHAR2(13)` | SQL identifier of the statement being monitored |
| `SQL_TEXT` | `VARCHAR2(2000)` | Up to the first 2000 characters of the text of the SQL being monitored |
| `IS_FULL_SQLTEXT` | `VARCHAR2(1)` | Indicates whether the `SQL_TEXT` column has the entire SQL text (`Y`) or not (`N`) |
| `SQL_EXEC_START` | `DATE` | Time when the execution started |
| `SQL_EXEC_ID` | `NUMBER` | Execution identifier. Together, the three columns `SQL_ID`, `SQL_EXEC_START`, and `SQL_EXEC_ID` represent the execution key. The execution key is used to uniquely identify one execution of the SQL statement. |
| `SQL_PLAN_HASH_VALUE` | `NUMBER` | SQL Plan hash value |
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
| `RM_LAST_ACTION` <sup>Foot 2</sup> | `VARCHAR2(48)` | The most recent action that was taken on this SQL operation by Resource Manager. Its value is one of the following: - `CANCEL_SQL` - `KILL_SESSION` - `LOG_ONLY` - `SWITCH TO <CG NAME>`  For the last value, `<CG NAME>` is the name of the consumer group that the SQL operation was switched to. If the Resource Plan has since been changed then `<CG NAME>` is the ID of the consumer group. |
| `RM_LAST_ACTION_REASON` <sup>Footref 2</sup> | `VARCHAR2(30)` | The reason for the most recent action that was taken on this SQL operation by Resource Manager. Its value is one of the following: |
| `RM_LAST_ACTION_TIME` <sup>Footref 2</sup> | `DATE` | The time of the most recent action that was taken on this SQL operation by Resource Manager |
| `RM_CONSUMER_GROUP` <sup>Footref 2</sup> | `VARCHAR2(30)` | The current consumer group for this SQL operation |

<sup>Footnote 1</sup> The datatype of this column is `VARCHAR2(64)` starting with Oracle Database 11g Release 2 (11.2.0.2).

<sup>Footnote 2</sup> This column is available starting with Oracle Database 11g Release 2 (11.2.0.4)