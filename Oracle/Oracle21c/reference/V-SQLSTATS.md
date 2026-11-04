---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-SQLSTATS.html
tags:
  - oracle
  - 21c
  - reference
---

## 10.76 V$SQLSTATS

`V$SQLSTATS` displays basic performance statistics for SQL cursors and contains one row per SQL statement (that is, one row per unique value of `SQL_ID`). The column definitions for columns in `V$SQLSTATS` are identical to those in the `V$SQL` and `V$SQLAREA` views. However, the `V$SQLSTATS` view differs from `V$SQL` and `V$SQLAREA` in that it is faster, more scalable, and has a greater data retention (the statistics may still appear in this view, even after the cursor has been aged out of the shared pool). Note that `V$SQLSTATS` contains a subset of columns that appear in `V$SQL` and `V$SQLAREA`.

| Column | Datatype | Description |
| --- | --- | --- |
| `SQL_TEXT` | `VARCHAR2(1000)` | First thousand characters of the SQL text for the current cursor |
| `SQL_FULLTEXT` | `CLOB` | Full text for the SQL statement exposed as a `CLOB` column. THe full text of a SQL statement can be retrieved using this column instead of joining with the `V$SQLTEXT` view. |
| `SQL_ID` | `VARCHAR2(13)` | SQL identifier of the parent cursor in the library cache |
| `LAST_ACTIVE_TIME` | `DATE` | Last time the statistics of a contributing cursor were updated |
| `LAST_ACTIVE_CHILD_ADDRESS` | `RAW(4 \| 8)` | Address of the contributing cursor that last updated these statistics |
| `PLAN_HASH_VALUE` | `NUMBER` | Numeric representation of the current SQL plan for this cursor. Comparing one `PLAN_HASH_VALUE` to another easily identifies whether or not two plans are the same (rather than comparing the two plans line by line). |
| `PARSE_CALLS` | `NUMBER` | Number of parse calls for all cursors with this SQL text and plan |
| `DISK_READS` | `NUMBER` | Number of disk reads for all cursors with this SQL text and plan |
| `DIRECT_WRITES` | `NUMBER` | Number of direct writes for all cursors with this SQL text and plan |
| `DIRECT_READS` | `NUMBER` | Number of direct reads for all cursors with this SQL text and plan |
| `BUFFER_GETS` | `NUMBER` | Number of buffer gets for all cursors with this SQL text and plan |
| `ROWS_PROCESSED` | `NUMBER` | Total number of rows the parsed SQL statement returns |
| `SERIALIZABLE_ABORTS` | `NUMBER` | Number of times the transaction failed to serialize, producing `ORA-08177` errors, per cursor |
| `FETCHES` | `NUMBER` | Number of fetches associated with the SQL statement |
| `EXECUTIONS` | `NUMBER` | Number of executions that took place on this object since it was brought into the library cache |
| `END_OF_FETCH_COUNT` | `NUMBER` | Number of times this cursor was fully executed since the cursor was brought into the library cache. The value of this statistic is not incremented when the cursor is partially executed, either because it failed during the execution or because only the first few rows produced by this cursor are fetched before the cursor is closed or re-executed. By definition, the value of the `END_OF_FETCH_COUNT` column should be less or equal to the value of the `EXECUTIONS` column. |
| `LOADS` | `NUMBER` | Number of times the object was either loaded or reloaded |
| `VERSION_COUNT` | `NUMBER` | number of cursors present in the cache with this SQL text and plan |
| `INVALIDATIONS` | `NUMBER` | Number of times this child cursor has been invalidated |
| `PX_SERVERS_EXECUTIONS` | `NUMBER` | Total number of executions performed by parallel execution servers (`0` when the statement has never been executed in parallel) |
| `CPU_TIME` | `NUMBER` | CPU time (in microseconds) used by this cursor for parsing, executing, and fetching |
| `ELAPSED_TIME` | `NUMBER` | Elapsed time (in microseconds) used by this cursor for parsing, executing, and fetching. If the cursor uses parallel execution, then `ELAPSED_TIME` is the cumulative time for the query coordinator, plus all parallel query worker processes. |
| `AVG_HARD_PARSE_TIME` | `NUMBER` | Average hard parse time (in microseconds) used by this cursor |
| `APPLICATION_WAIT_TIME` | `NUMBER` | Application wait time (in microseconds) |
| `CONCURRENCY_WAIT_TIME` | `NUMBER` | Concurrency wait time (in microseconds) |
| `CLUSTER_WAIT_TIME` | `NUMBER` | Cluster wait time (in microseconds). This value is specific to Oracle RAC. It shows the total time spent waiting for all waits that are categorized under the cluster class of wait events. The value is this column is an accumulated wait time spent waiting for Oracle RAC cluster resources. |
| `USER_IO_WAIT_TIME` | `NUMBER` | User I/O wait time (in microseconds) |
| `PLSQL_EXEC_TIME` | `NUMBER` | PL/SQL execution time (in microseconds) |
| `JAVA_EXEC_TIME` | `NUMBER` | Java execution time (in microseconds) |
| `SORTS` | `NUMBER` | Number of sorts that were done for the child cursor |
| `SHARABLE_MEM` | `NUMBER` | Total shared memory (in bytes) currently occupied by all cursors with this SQL text and plan |
| `TOTAL_SHARABLE_MEM` | `NUMBER` | Total shared memory (in bytes) occupied by all cursors with this SQL text and plan if they were to be fully loaded in the shared pool (that is, cursor size) |
| `TYPECHECK_MEM` | `NUMBER` | Typecheck memory |
| `IO_CELL_OFFLOAD_ELIGIBLE_BYTES` | `NUMBER` | Number of I/O bytes which can be filtered by the Exadata storage system  See Also: Oracle Exadata Storage Server Software documentation for more information |
| `IO_INTERCONNECT_BYTES` | `NUMBER` | Number of I/O bytes exchanged between Oracle Database and the storage system. Typically used for Cache Fusion or parallel queries. |
| `PHYSICAL_READ_REQUESTS` | `NUMBER` | Number of physical read I/O requests issued by the monitored SQL. The requests may not be disk reads. |
| `PHYSICAL_READ_BYTES` | `NUMBER` | Number of bytes read from disks by the monitored SQL |
| `PHYSICAL_WRITE_REQUESTS` | `NUMBER` | Number of physical write I/O requests issued by the monitored SQL |
| `PHYSICAL_WRITE_BYTES` | `NUMBER` | Number of bytes written to disks by the monitored SQL |
| `EXACT_MATCHING_SIGNATURE` | `NUMBER` | Signature used when the `CURSOR_SHARING` parameter is set to `EXACT` |
| `FORCE_MATCHING_SIGNATURE` | `NUMBER` | Signature used when the `CURSOR_SHARING` parameter is set to `FORCE` |
| `IO_CELL_UNCOMPRESSED_BYTES` | `NUMBER` | Number of uncompressed bytes (that is, size after decompression) that are offloaded to the Exadata cells  See Also: Oracle Exadata Storage Server Software documentation for more information |
| `IO_CELL_OFFLOAD_RETURNED_BYTES` | `NUMBER` | Number of bytes that are returned by Exadata cell through the regular I/O path  See Also: Oracle Exadata Storage Server Software documentation for more information |
| `DELTA_PARSE_CALLS` | `NUMBER` | Number of parse calls for the cursor since the last Automatic Workload Repository (AWR) snapshot  See Also: [Oracle Database Performance Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=TGDBA-GUID-9D3A3890-8E68-48C5-84D0-DB0A8D93C53A) for an introduction to AWR |
| `DELTA_DISK_READS` | `NUMBER` | Number of disk reads for the cursor since the last AWR snapshot |
| `DELTA_DIRECT_WRITES` | `NUMBER` | Number of direct writes for the cursor since the last AWR snapshot |
| `DELTA_DIRECT_READS` | `NUMBER` | Number of direct reads for the cursor since the last AWR snapshot |
| `DELTA_BUFFER_GETS` | `NUMBER` | Number of buffer gets for the cursor since the last AWR snapshot |
| `DELTA_ROWS_PROCESSED` | `NUMBER` | Number of rows returned by the cursor since the last AWR snapshot |
| `DELTA_FETCH_COUNT` | `NUMBER` | Number of fetches for the cursor since the last AWR snapshot |
| `DELTA_EXECUTION_COUNT` | `NUMBER` | Number of executions for the cursor since the last AWR snapshot |
| `DELTA_PX_SERVERS_EXECUTIONS` | `NUMBER` | Number of executions performed by parallel execution servers since the last AWR snapshot |
| `DELTA_END_OF_FETCH_COUNT` | `NUMBER` | Number of times the cursor was fully executed since the last AWR snapshot |
| `DELTA_CPU_TIME` | `NUMBER` | CPU time (in microseconds) for the cursor since the last AWR snapshot |
| `DELTA_ELAPSED_TIME` | `NUMBER` | Database time (in microseconds) for the cursor since the last AWR snapshot |
| `DELTA_APPLICATION_WAIT_TIME` | `NUMBER` | Time spent by the cursor (in microseconds) in the Application wait class since the last AWR snapshot |
| `DELTA_CONCURRENCY_TIME` | `NUMBER` | Time spent by the cursor (in microseconds) in the Concurrency wait class since the last AWR snapshot |
| `DELTA_CLUSTER_WAIT_TIME` | `NUMBER` | Time spent by the cursor (in microseconds) in the Cluster wait class since the last AWR snapshot |
| `DELTA_USER_IO_WAIT_TIME` | `NUMBER` | Time spent by the cursor (in microseconds) in the User I/O wait class since the last AWR snapshot |
| `DELTA_PLSQL_EXEC_TIME` | `NUMBER` | Time spent by the cursor (in microseconds) executing PL/SQL since the last AWR snapshot |
| `DELTA_JAVA_EXEC_TIME` | `NUMBER` | Time spent by the cursor (in microseconds) executing Java since the last AWR snapshot |
| `DELTA_SORTS` | `NUMBER` | Number of sorts for the cursor since the last AWR snapshot |
| `DELTA_LOADS` | `NUMBER` | Number of times the cursor was loaded since the last AWR snapshot |
| `DELTA_INVALIDATIONS` | `NUMBER` | Number of times the cursor was invalidated since the last AWR snapshot |
| `DELTA_PHYSICAL_READ_REQUESTS` | `NUMBER` | Number of physical read I/O requests for the cursor since the last AWR snapshot |
| `DELTA_PHYSICAL_READ_BYTES` | `NUMBER` | Number of bytes read from disk for the cursor since the last AWR snapshot |
| `DELTA_PHYSICAL_WRITE_REQUESTS` | `NUMBER` | Number of physical write I/O requests for the cursor since the last AWR snapshot |
| `DELTA_PHYSICAL_WRITE_BYTES` | `NUMBER` | Number of bytes written to disk for the cursor since the last AWR snapshot |
| `DELTA_IO_INTERCONNECT_BYTES` | `NUMBER` | Number of I/O bytes exchanged between the Oracle database and the storage system for the cursor since the last AWR snapshot |
| `DELTA_CELL_OFFLOAD_ELIG_BYTES` | `NUMBER` | Number of I/O bytes which can be filtered by the Exadata storage system for the cursor since the last AWR snapshot  See Also: Oracle Exadata Storage Server Software documentation for more information |
| `DELTA_CELL_UNCOMPRESSED_BYTES` | `NUMBER` | Number of uncompressed bytes that are offloaded to the Exadata cell for the cursor since the last AWR snapshot  See Also: Oracle Exadata Storage Server Software documentation for more information |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |
| `CON_DBID` | `NUMBER` | The database ID of the PDB |
| `OBSOLETE_COUNT` | `NUMBER` | Number of times that a parent cursor became obsolete |
| `AVOIDED_EXECUTIONS` | `NUMBER` | Number of executions attempted on this object, but prevented due to the SQL statement being in quarantine |
| `DELTA_AVOIDED_EXECUTIONS` | `NUMBER` | Number of executions attempted on this object, but prevented due to the SQL statement being in quarantine, since the last AWR snapshot |

See Also:

- " [V$SQL](V-SQL.md) "
- " [V$SQLAREA](V-SQLAREA.md) "