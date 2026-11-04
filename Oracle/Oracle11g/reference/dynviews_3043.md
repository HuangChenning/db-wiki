---
title: "V$SQL"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_3043.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$SQL` lists statistics on shared SQL areas without the `GROUP BY` clause and contains one row for each child of the original SQL text entered. Statistics displayed in `V$SQL` are normally updated at the end of query execution. However, for long running queries, they are updated every 5 seconds. This makes it easy to see the impact of long running SQL statements while they are still in progress.

| Column | Datatype | Description |
| --- | --- | --- |
| `SQL_TEXT` | `VARCHAR2(1000)` | First thousand characters of the SQL text for the current cursor |
| `SQL_FULLTEXT` | `CLOB` | Full text for the SQL statement exposed as a `CLOB` column. The full text of a SQL statement can be retrieved using this column instead of joining with the `V$SQLTEXT` dynamic performance view. |
| `SQL_ID` | `VARCHAR2(13)` | SQL identifier of the parent cursor in the library cache |
| `SHARABLE_MEM` | `NUMBER` | Amount of shared memory used by the child cursor (in bytes) |
| `PERSISTENT_MEM` | `NUMBER` | Fixed amount of memory used for the lifetime of the child cursor (in bytes) |
| `RUNTIME_MEM` | `NUMBER` | Fixed amount of memory required during the execution of the child cursor |
| `SORTS` | `NUMBER` | Number of sorts that were done for the child cursor |
| `LOADED_VERSIONS` | `NUMBER` | Indicates whether the context heap is loaded (`1`) or not (`0`) |
| `OPEN_VERSIONS` | `NUMBER` | Indicates whether the child cursor is locked (`1`) or not (`0`) |
| `USERS_OPENING` | `NUMBER` | Number of users that have any of the child cursors open |
| `FETCHES` | `NUMBER` | Number of fetches associated with the SQL statement |
| `EXECUTIONS` | `NUMBER` | Number of executions that took place on this object since it was brought into the library cache |
| `PX_SERVERS_EXECUTIONS` | `NUMBER` | Total number of executions performed by parallel execution servers (`0` when the statement has never been executed in parallel) |
| `END_OF_FETCH_COUNT` | `NUMBER` | Number of times this cursor was fully executed since the cursor was brought into the library cache. The value of this statistic is not incremented when the cursor is partially executed, either because it failed during the execution or because only the first few rows produced by this cursor are fetched before the cursor is closed or re-executed. By definition, the value of the `END_OF_FETCH_COUNT` column should be less or equal to the value of the `EXECUTIONS` column. |
| `USERS_EXECUTING` | `NUMBER` | Number of users executing the statement |
| `LOADS` | `NUMBER` | Number of times the object was either loaded or reloaded |
| `FIRST_LOAD_TIME` | `VARCHAR2(19)` | Timestamp of the parent creation time |
| `INVALIDATIONS` | `NUMBER` | Number of times this child cursor has been invalidated |
| `PARSE_CALLS` | `NUMBER` | Number of parse calls for this child cursor |
| `DISK_READS` | `NUMBER` | Number of disk reads for this child cursor |
| `DIRECT_WRITES` | `NUMBER` | Number of direct writes for this child cursor |
| `BUFFER_GETS` | `NUMBER` | Number of buffer gets for this child cursor |
| `APPLICATION_WAIT_TIME` | `NUMBER` | Application wait time (in microseconds) |
| `CONCURRENCY_WAIT_TIME` | `NUMBER` | Concurrency wait time (in microseconds) |
| `CLUSTER_WAIT_TIME` | `NUMBER` | Cluster wait time (in microseconds) |
| `USER_IO_WAIT_TIME` | `NUMBER` | User I/O Wait Time (in microseconds) |
| `PLSQL_EXEC_TIME` | `NUMBER` | PL/SQL execution time (in microseconds) |
| `JAVA_EXEC_TIME` | `NUMBER` | Java execution time (in microseconds) |
| `ROWS_PROCESSED` | `NUMBER` | Total number of rows the parsed SQL statement returns |
| `COMMAND_TYPE` | `NUMBER` | Oracle command type definition |
| `OPTIMIZER_MODE` | `VARCHAR2(10)` | Mode under which the SQL statement was executed |
| `OPTIMIZER_COST` | `NUMBER` | Cost of this query given by the optimizer |
| `OPTIMIZER_ENV` | `RAW(2000)` | Optimizer environment |
| `OPTIMIZER_ENV_HASH_VALUE` | `NUMBER` | Hash value for the optimizer environment |
| `PARSING_USER_ID` | `NUMBER` | User ID of the user who originally built this child cursor |
| `PARSING_SCHEMA_ID` | `NUMBER` | Schema ID that was used to originally build this child cursor |
| `PARSING_SCHEMA_NAME` | `VARCHAR2(30)` | Schema name that was used to originally build this child cursor |
| `KEPT_VERSIONS` | `NUMBER` | Indicates whether this child cursor has been marked to be kept pinned in the cache using the `DBMS_SHARED_POOL` package |
| `ADDRESS` | `RAW(4 \| 8)` | Address of the handle to the parent for this cursor |
| `TYPE_CHK_HEAP` | `RAW(4)` | Descriptor of the type check heap for this child cursor |
| `HASH_VALUE` | `NUMBER` | Hash value of the parent statement in the library cache |
| `OLD_HASH_VALUE` | `NUMBER` | Old SQL hash value |
| `PLAN_HASH_VALUE` | `NUMBER` | Numeric representation of the SQL plan for this cursor. Comparing one `PLAN_HASH_VALUE` to another easily identifies whether or not two plans are the same (rather than comparing the two plans line by line). |
| `CHILD_NUMBER` | `NUMBER` | Number of this child cursor |
| `SERVICE` | `VARCHAR2(64)` | Service name |
| `SERVICE_HASH` | `NUMBER` | Hash value for the name listed in the `SERVICE` column |
| `MODULE` | `VARCHAR2(64)` | Contains the name of the module that was executing at the time that the SQL statement was first parsed, which is set by calling `DBMS_APPLICATION_INFO.SET_MODULE` |
| `MODULE_HASH` | `NUMBER` | Hash value of the module listed in the `MODULE` column |
| `ACTION` | `VARCHAR2(64)` | Contains the name of the action that was executing at the time that the SQL statement was first parsed, which is set by calling `DBMS_APPLICATION_INFO.SET_ACTION` |
| `ACTION_HASH` | `NUMBER` | Hash value of the action listed in the `ACTION` column |
| `SERIALIZABLE_ABORTS` | `NUMBER` | Number of times the transaction failed to serialize, producing `ORA-08177` errors, per cursor |
| `OUTLINE_CATEGORY` | `VARCHAR2(64)` | If an outline was applied during construction of the cursor, then this column displays the category of that outline. Otherwise the column is left blank. |
| `CPU_TIME` | `NUMBER` | CPU time (in microseconds) used by this cursor for parsing, executing, and fetching |
| `ELAPSED_TIME` | `NUMBER` | Elapsed time (in microseconds) used by this cursor for parsing, executing, and fetching. If the cursor uses parallel execution, then `ELAPSED_TIME` is the cumulative time for the query coordinator, plus all parallel query slave processes. |
| `OUTLINE_SID` | `NUMBER` | Outline session identifier |
| `CHILD_ADDRESS` | `RAW(4 \| 8)` | Address of the child cursor |
| `SQLTYPE` | `NUMBER` | Denotes the version of the SQL language used for this statement |
| `REMOTE` | `VARCHAR2(1)` | Indicates whether the cursor is remote mapped (`Y`) or not (`N`) |
| `OBJECT_STATUS` | `VARCHAR2(19)` | Status of the cursor: - `VALID` - Valid, authorized without errors - `VALID_AUTH_ERROR` - Valid, authorized with authorization errors - `VALID_COMPILE_ERROR` - Valid, authorized with compilation errors - `VALID_UNAUTH` - Valid, unauthorized - `INVALID_UNAUTH` - Invalid, unauthorized - `INVALID` - Invalid, unauthorized but keep the timestamp |
| `LITERAL_HASH_VALUE` | `NUMBER` | Hash value of the literals which are replaced with system-generated bind variables and are to be matched, when `CURSOR_SHARING` is used. This is not the hash value for the SQL statement. If `CURSOR_SHARING` is not used, then the value is `0`. |
| `LAST_LOAD_TIME` | `VARCHAR2(19)` | Time at which the query plan was loaded into the library cache |
| `IS_OBSOLETE` | `VARCHAR2(1)` | Indicates whether the cursor has become obsolete (`Y`) or not (`N`). This can happen if the number of child cursors is too large. |
| `IS_BIND_SENSITIVE` | `VARCHAR2(1)` | Indicates whether the cursor is bind sensitive (`Y`) or not (`N`). A query is considered bind-sensitive if the optimizer peeked at one of its bind variable values when computing predicate selectivities and where a change in a bind variable value may cause the optimizer to generate a different plan. |
| `IS_BIND_AWARE` | `VARCHAR2(1)` | Indicates whether the cursor is bind aware (`Y`) or not (`N`). A query is considered bind-aware if it has been marked to use extended cursor sharing. The query would already have been marked as bind-sensitive. |
| `IS_SHAREABLE` | `VARCHAR2(1)` | Indicates whether the cursor can be shared (`Y`) or not (`N`) |
| `CHILD_LATCH` | `NUMBER` | Child latch number that is protecting the cursor. This column is obsolete and maintained for backward compatibility. |
| `SQL_PROFILE` | `VARCHAR2(64)` | SQL profile used for this statement, if any |
| `SQL_PATCH` | `VARCHAR2(30)` | SQL patch used for this statement, if any |
| `SQL_PLAN_BASELINE` | `VARCHAR2(30)` | SQL plan baseline used for this statement, if any |
| `PROGRAM_ID` | `NUMBER` | Program identifier |
| `PROGRAM_LINE#` | `NUMBER` | Program line number |
| `EXACT_MATCHING_SIGNATURE` | `NUMBER` | Signature calculated on the normalized SQL text. The normalization includes the removal of white space and the uppercasing of all non-literal strings. |
| `FORCE_MATCHING_SIGNATURE` | `NUMBER` | Signature used when the `CURSOR_SHARING` parameter is set to `FORCE` |
| `LAST_ACTIVE_TIME` | `DATE` | TIme at which the query plan was last active |
| `BIND_DATA` | `RAW(2000)` | Bind data |
| `TYPECHECK_MEM` | `NUMBER` | Typecheck memory |
| `IO_CELL_OFFLOAD_ELIGIBLE_BYTES` | `NUMBER` | Number of I/O bytes which can be filtered by the Exadata storage system  See Also: Oracle Exadata Storage Server Software documentation for more information |
| `IO_INTERCONNECT_BYTES` | `NUMBER` | Number of I/O bytes exchanged between Oracle Database and the storage system |
| `PHYSICAL_READ_REQUESTS` | `NUMBER` | Number of physical read I/O requests issued by the monitored SQL |
| `PHYSICAL_READ_BYTES` | `NUMBER` | Number of bytes read from disks by the monitored SQL |
| `PHYSICAL_WRITE_REQUESTS` | `NUMBER` | Number of physical write I/O requests issued by the monitored SQL |
| `PHYSICAL_WRITE_BYTES` | `NUMBER` | Number of bytes written to disks by the monitored SQL |
| `OPTIMIZED_PHY_READ_REQUESTS` | `NUMBER` | Number of physical read I/O requests from Database Smart Flash Cache issued by the monitored SQL |
| `LOCKED_TOTAL` | `NUMBER` | Total number of times the child cursor has been locked |
| `PINNED_TOTAL` | `NUMBER` | Total number of times the child cursor has been pinned |
| `IO_CELL_UNCOMPRESSED_BYTES` | `NUMBER` | Number of uncompressed bytes (that is, size after decompression) that are offloaded to the Exadata cells  See Also: Oracle Exadata Storage Server Software documentation for more information |
| `IO_CELL_OFFLOAD_RETURNED_BYTES` | `NUMBER` | Number of bytes that are returned by Exadata cell through the regular I/O path  See Also: Oracle Exadata Storage Server Software documentation for more information |