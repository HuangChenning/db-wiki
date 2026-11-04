---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-SQLAREA.html
tags:
  - oracle
  - 21c
  - reference
---

## 10.71 V$SQLAREA

`V$SQLAREA` displays statistics on shared SQL areas and contains one row per SQL string. It provides statistics on SQL statements that are in memory, parsed, and ready for execution.

| Column | Datatype | Description |
| --- | --- | --- |
| `SQL_TEXT` | `VARCHAR2(1000)` | First thousand characters of the SQL text for the current cursor |
| `SQL_FULLTEXT` | `CLOB` | All characters of the SQL text for the current cursor |
| `SQL_ID` | `VARCHAR2(13)` | SQL identifier of the parent cursor in the library cache |
| `SHARABLE_MEM` | `NUMBER` | Amount of shared memory used by a cursor. If multiple child cursors exist, then the sum of all shared memory used by all child cursors. |
| `PERSISTENT_MEM` | `NUMBER` | Fixed amount of memory used for the lifetime of an open cursor. If multiple child cursors exist, then the fixed sum of memory used for the lifetime of all the child cursors. |
| `RUNTIME_MEM` | `NUMBER` | Fixed amount of memory required during execution of a cursor. If multiple child cursors exist, then the fixed sum of all memory required during execution of all the child cursors. |
| `SORTS` | `NUMBER` | Sum of the number of sorts that were done for all the child cursors |
| `VERSION_COUNT` | `NUMBER` | Number of child cursors that are present in the cache under this parent |
| `LOADED_VERSIONS` | `NUMBER` | Number of child cursors that are present in the cache and have their context heap loaded |
| `OPEN_VERSIONS` | `NUMBER` | Number of child cursors that are currently open under this current parent |
| `USERS_OPENING` | `NUMBER` | Number of users that have any of the child cursors open |
| `FETCHES` | `NUMBER` | Number of fetches associated with the SQL statement |
| `EXECUTIONS` | `NUMBER` | Total number of executions, totalled over all the child cursors |
| `PX_SERVERS_EXECUTIONS` | `NUMBER` | Total number of executions performed by parallel execution servers (`0` when the statement has never been executed in parallel) |
| `END_OF_FETCH_COUNT` | `NUMBER` | Number of times this cursor was fully executed since the cursor was brought into the library cache. The value of this statistic is not incremented when the cursor is partially executed, either because it failed during the execution or because only the first few rows produced by this cursor are fetched before the cursor is closed or re-executed. By definition, the value of the `END_OF_FETCH_COUNT` column should be less or equal to the value of the `EXECUTIONS` column. |
| `USERS_EXECUTING` | `NUMBER` | Total number of users executing the statement over all child cursors |
| `LOADS` | `NUMBER` | Number of times the object was loaded or reloaded |
| `FIRST_LOAD_TIME` | `VARCHAR2(76)` | Timestamp of the parent creation time |
| `INVALIDATIONS` | `NUMBER` | Total number of invalidations over all the child cursors |
| `PARSE_CALLS` | `NUMBER` | Sum of all parse calls to all the child cursors under this parent |
| `DISK_READS` | `NUMBER` | Sum of the number of disk reads over all child cursors |
| `DIRECT_WRITES` | `NUMBER` | Sum of the number of direct writes over all child cursors |
| `DIRECT_READS` | `NUMBER` | Sum of the number of direct reads over all child cursors |
| `BUFFER_GETS` | `NUMBER` | Sum of buffer gets over all child cursors |
| `APPLICATION_WAIT_TIME` | `NUMBER` | Application wait time (in microseconds) |
| `CONCURRENCY_WAIT_TIME` | `NUMBER` | Concurrency wait time (in microseconds) |
| `CLUSTER_WAIT_TIME` | `NUMBER` | Cluster wait time (in microseconds) |
| `USER_IO_WAIT_TIME` | `NUMBER` | User I/O Wait Time (in microseconds) |
| `PLSQL_EXEC_TIME` | `NUMBER` | PL/SQL execution time (in microseconds) |
| `JAVA_EXEC_TIME` | `NUMBER` | Java execution time (in microseconds) |
| `ROWS_PROCESSED` | `NUMBER` | Total number of rows processed on behalf of this SQL statement |
| `COMMAND_TYPE` | `NUMBER` | Oracle command type definition |
| `OPTIMIZER_MODE` | `VARCHAR2(10)` | Mode under which the SQL statement was executed |
| `OPTIMIZER_COST` | `NUMBER` | Cost of this query given by the optimizer |
| `OPTIMIZER_ENV` | `RAW(2000)` | Optimizer environment |
| `OPTIMIZER_ENV_HASH_VALUE` | `NUMBER` | Hash value for the optimizer environment |
| `PARSING_USER_ID` | `NUMBER` | User ID of the user that has parsed the very first cursor under this parent |
| `PARSING_SCHEMA_ID` | `NUMBER` | Schema ID that was used to parse this child cursor |
| `PARSING_SCHEMA_NAME` | `VARCHAR2(128)` | Schema name that was used to parse this child cursor |
| `KEPT_VERSIONS` | `NUMBER` | Number of child cursors that have been marked to be kept using the `DBMS_SHARED_POOL` package |
| `ADDRESS` | `RAW(4 \| 8)` | Address of the handle to the parent for this cursor |
| `HASH_VALUE` | `NUMBER` | Hash value of the parent statement in the library cache |
| `OLD_HASH_VALUE` | `NUMBER` | Old SQL hash value |
| `PLAN_HASH_VALUE` | `NUMBER` | Numeric representation of the current SQL plan for this cursor. Comparing one `PLAN_HASH_VALUE` to another easily identifies whether or not two plans are the same (rather than comparing the two plans line by line). |
| `FULL_PLAN_HASH_VALUE` | `NUMBER` | Numeric representation of the complete SQL plan for this cursor. Comparing one `FULL_PLAN_HASH_VALUE` to another easily identifies whether or not two plans are the same (rather than comparing the two plans line by line). Note that the `FULL_PLAN_HASH_VALUE` cannot be compared across databases releases. It is not backward compatible. |
| `MODULE` | `VARCHAR2(64)` | Contains the name of the module that was executing when the SQL statement was first parsed as set by calling `DBMS_APPLICATION_INFO.SET_MODULE` |
| `MODULE_HASH` | `NUMBER` | Hash value of the module that is named in the `MODULE` column |
| `ACTION` | `VARCHAR2(64)` | Contains the name of the action that was executing when the SQL statement was first parsed as set by calling `DBMS_APPLICATION_INFO.SET_ACTION` |
| `ACTION_HASH` | `NUMBER` | Hash value of the action that is named in the `ACTION` column |
| `SERIALIZABLE_ABORTS` | `NUMBER` | Number of times the transaction failed to serialize, producing `ORA-08177` errors, totalled over all the child cursors |
| `OUTLINE_CATEGORY` | `VARCHAR2(64)` | If an outline was applied during construction of the cursor, then this column displays the category of that outline. Otherwise the column is left blank. |
| `CPU_TIME` | `NUMBER` | CPU time (in microseconds) used by this cursor for parsing, executing, and fetching |
| `ELAPSED_TIME` | `NUMBER` | Elapsed time (in microseconds) used by this cursor for parsing, executing, and fetching. If the cursor uses parallel execution, then `ELAPSED_TIME` is the cumulative time for the query coordinator, plus all parallel query worker processes. |
| `OUTLINE_SID` | `VARCHAR2(40)` | Outline session identifier |
| `LAST_ACTIVE_CHILD_ADDRESS` | `RAW(4 \| 8)` | Address (identifier) of the child cursor that was the last to be active in the group (that is, the child cursor on behalf of which statistics in `V$SQL` were updated) |
| `REMOTE` | `VARCHAR2(1)` | Indicates whether the cursor is remote mapped (`Y`) or not (`N`) |
| `OBJECT_STATUS` | `VARCHAR2(19)` | Status of the cursor:  - `VALID` - Valid, authorized without errors - `VALID_AUTH_ERROR` - Valid, authorized with authorization errors - `VALID_COMPILE_ERROR` - Valid, authorized with compilation errors - `VALID_UNAUTH` - Valid, unauthorized - `INVALID_UNAUTH` - Invalid, unauthorized - `INVALID` - Invalid, unauthorized but keep the timestamp |
| `LITERAL_HASH_VALUE` | `NUMBER` | Hash value of the literals which are replaced with system-generated bind variables and are to be matched, when `CURSOR_SHARING` is used. This is not the hash value for the SQL statement. If `CURSOR_SHARING` is not used, then the value is `0`. |
| `LAST_LOAD_TIME` | `DATE` | Time at which the query plan was loaded into the library cache |
| `IS_OBSOLETE` | `VARCHAR2(1)` | Indicates whether the cursor has become obsolete (`Y`) or not (`N`). This can happen if the number of child cursors is too large. |
| `IS_BIND_SENSITIVE` | `VARCHAR2(1)` | Indicates whether the cursor is bind sensitive (`Y`) or not (`N`). A query is considered bind-sensitive if the optimizer peeked at one of its bind variable values when computing predicate selectivities and where a change in a bind variable value may cause the optimizer to generate a different plan. |
| `IS_BIND_AWARE` | `VARCHAR2(1)` | Indicates whether the cursor is bind aware (`Y`) or not (`N`). A query is considered bind-aware if it has been marked to use extended cursor sharing. The query would already have been marked as bind-sensitive. |
| `CHILD_LATCH` | `NUMBER` | Child latch number that is protecting the cursor. This column is obsolete and maintained for backward compatibility. |
| `SQL_PROFILE` | `VARCHAR2(64)` | SQL profile used for this statement, if any |
| `SQL_PATCH` | `VARCHAR2(128)` | SQL patch used for this statement, if any |
| `SQL_PLAN_BASELINE` | `VARCHAR2(128)` | SQL plan baseline used for this statement, if any |
| `PROGRAM_ID` | `NUMBER` | Program identifier |
| `PROGRAM_LINE#` | `NUMBER` | Program line number |
| `EXACT_MATCHING_SIGNATURE` | `NUMBER` | Signature used when the `CURSOR_SHARING` parameter is set to `EXACT` |
| `FORCE_MATCHING_SIGNATURE` | `NUMBER` | Signature used when the `CURSOR_SHARING` parameter is set to `FORCE` |
| `LAST_ACTIVE_TIME` | `DATE` | Time at which the query plan was last active |
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
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |
| `IS_REOPTIMIZABLE` | `VARCHAR2(1)` | This column shows whether the next execution matching this child cursor will trigger a reoptimization. The values are:  - `Y`: If the next execution will trigger a reoptimization - `R`: If the child cursor contains reoptimization information, but will not trigger reoptimization because the cursor was compiled in reporting mode - `N`: If the child cursor has no reoptimization information |
| `IS_RESOLVED_ADAPTIVE_PLAN` | `VARCHAR2(1)` | This column shows whether all of the adaptive parts of a plan have been resolved to the final plan. Once the plan is resolved, the plan hash value and the plan displayed by `DBMS_XPLAN` will not change through the end of execution. The values for this column are:  - `NULL`: If the plan is not adaptive - `Y`: If the plan is fully resolved - `N`: If the plan is not yet fully resolved  See Also: [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ARPLS378) for more information about the `DBMS_XPLAN` package |

See Also:

- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ARPLS055) for more information about the `DBMS_SHARED_POOL` package
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ARPLS65239) for more information about the `DBMS_APPLICATION_INFO.SET_MODULE` procedure
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ARPLS65235) for more information about the `DBMS_APPLICATION_INFO.SET_ACTION` procedure
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ARPLS378) for more information about the `DBMS_XPLAN` package