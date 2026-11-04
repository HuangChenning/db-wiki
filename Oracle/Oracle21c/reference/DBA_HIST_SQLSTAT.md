---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_HIST_SQLSTAT.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.65 DBA\_HIST\_SQLSTAT

`DBA_HIST_SQLSTAT` displays historical information about SQL statistics.

This view captures the top SQL statements based on a set of criteria and captures the statistics information from `V$SQL`. The total value is the value of the statistics since instance startup. The delta value is the value of the statistics from the `BEGIN_INTERVAL_TIME` to the `END_INTERVAL_TIME` in the `DBA_HIST_SNAPSHOT` view.

This view is used with the `DBA_HIST_OPTIMIZER_ENV`, `DBA_HIST_SQLTEXT`, and `DBA_HIST_SQL_PLAN` views to provide a complete picture of historical SQL statistics.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` | `NOT NULL` | Unique snapshot ID |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID for the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` | `NOT NULL` | Instance number for the snapshot |
| `SQL_ID` | `VARCHAR2(13)` | `NOT NULL` | SQL identifier of the parent cursor in the library cache |
| `PLAN_HASH_VALUE` | `NUMBER` | `NOT NULL` | Numerical representation of the SQL plan for the cursor. Comparing one `PLAN_HASH_VALUE` to another easily identifies whether or not two plans are the same (rather than comparing the two plans line by line). |
| `OPTIMIZER_COST` | `NUMBER` |  | Cost of the query given by the optimizer |
| `OPTIMIZER_MODE` | `VARCHAR2(10)` |  | Mode under which the SQL statement is executed |
| `OPTIMIZER_ENV_HASH_VALUE` | `NUMBER` |  | Hash Value for the optimizer environment |
| `SHARABLE_MEM` | `NUMBER` |  | Amount of shared memory used by the child cursor (in bytes) |
| `LOADED_VERSIONS` | `NUMBER` |  | Indicates whether the context heap is loaded (`1`) or not (`0`) |
| `VERSION_COUNT` | `NUMBER` |  | Number of children associated with the cursor |
| `MODULE` | `VARCHAR2(64)` |  | Contains the name of the module that was executing at the time that the SQL statement was first parsed, which is set by calling `DBMS_APPLICATION_INFO.SET_MODULE` |
| `ACTION` | `VARCHAR2(64)` |  | Contains the name of the action that was executing at the time that the SQL statement was first parsed, which is set by calling `DBMS_APPLICATION_INFO.SET_ACTION` |
| `SQL_PROFILE` | `VARCHAR2(64)` |  | Name of the applied SQL Profile |
| `FORCE_MATCHING_SIGNATURE` | `NUMBER` |  | The signature used when the `CURSOR_SHARING` parameter is set to `FORCE` |
| `PARSING_SCHEMA_ID` | `NUMBER` |  | Schema ID that was used to originally build the child cursor |
| `PARSING_SCHEMA_NAME` | `VARCHAR2(128)` |  | Schema name that was used to originally build the child cursor |
| `PARSING_USER_ID` | `NUMBER` |  | User ID that was used to originally build the child cursor |
| `FETCHES_TOTAL` | `NUMBER` |  | Cumulative number of fetches associated with the SQL statement |
| `FETCHES_DELTA` | `NUMBER` |  | Delta number of fetches associated with the SQL statement |
| `END_OF_FETCH_COUNT_TOTAL` | `NUMBER` |  | Cumulative number of times this cursor was fully executed since the cursor was brought into the library cache. The value of this statistic is not incremented when the cursor is partially executed, either because it failed during the execution or because only the first few rows produced by this cursor are fetched before the cursor is closed or re-executed. By definition, the value of the `END_OF_FETCH_COUNT` column should be less or equal to the value of the `EXECUTIONS` column. |
| `END_OF_FETCH_COUNT_DELTA` | `NUMBER` |  | Delta number of times this cursor was fully executed since the cursor was brought into the library cache. The value of this statistic is not incremented when the cursor is partially executed, either because it failed during the execution or because only the first few rows produced by this cursor are fetched before the cursor is closed or re-executed. |
| `SORTS_TOTAL` | `NUMBER` |  | Cumulative number of sorts that were done for this child cursor |
| `SORTS_DELTA` | `NUMBER` |  | Delta number of sorts that were done for this child cursor |
| `EXECUTIONS_TOTAL` | `NUMBER` |  | Cumulative number of executions that took place on this object since it was brought into the library cache |
| `EXECUTIONS_DELTA` | `NUMBER` |  | Delta number of executions that took place on this object since it was brought into the library cache |
| `PX_SERVERS_EXECS_TOTAL` | `NUMBER` |  | Cumulative number of PX server executions |
| `PX_SERVERS_EXECS_DELTA` | `NUMBER` |  | Delta number of PX server executions |
| `LOADS_TOTAL` | `NUMBER` |  | Cumulative number of times the object was either loaded or reloaded |
| `LOADS_DELTA` | `NUMBER` |  | Delta number of times the object was either loaded or reloaded |
| `INVALIDATIONS_TOTAL` | `NUMBER` |  | Cumulative number of times this child cursor has been invalidated |
| `INVALIDATIONS_DELTA` | `NUMBER` |  | Delta number of times this child cursor has been invalidated |
| `PARSE_CALLS_TOTAL` | `NUMBER` |  | Cumulative number of parse calls for this child cursor |
| `PARSE_CALLS_DELTA` | `NUMBER` |  | Delta number of parse calls for this child cursor |
| `DISK_READS_TOTAL` | `NUMBER` |  | Cumulative number of disk reads for this child cursor |
| `DISK_READS_DELTA` | `NUMBER` |  | Delta number of disk reads for this child cursor |
| `BUFFER_GETS_TOTAL` | `NUMBER` |  | Cumulative number of buffer gets for this child cursor |
| `BUFFER_GETS_DELTA` | `NUMBER` |  | Delta number of buffer gets for this child cursor |
| `ROWS_PROCESSED_TOTAL` | `NUMBER` |  | Cumulative number of rows the parsed SQL statement returns |
| `ROWS_PROCESSED_DELTA` | `NUMBER` |  | Delta number of rows the parsed SQL statement returns |
| `CPU_TIME_TOTAL` | `NUMBER` |  | Cumulative value of CPU time (in microseconds) used by this cursor for parsing/executing/fetching |
| `CPU_TIME_DELTA` | `NUMBER` |  | Delta value of CPU time (in microseconds) used by this cursor for parsing/executing/fetching |
| `ELAPSED_TIME_TOTAL` | `NUMBER` |  | Cumulative value of elapsed time (in microseconds) used by this cursor for parsing/executing/fetching. If the cursor uses parallel execution, then `ELAPSED_TIME_TOTAL` is the cumulative time for the query coordinator, plus all parallel query worker processes. |
| `ELAPSED_TIME_DELTA` | `NUMBER` |  | Delta value of elapsed time (in microseconds) used by this cursor for parsing/executing/fetching |
| `IOWAIT_TOTAL` | `NUMBER` |  | Cumulative value of user I/O wait time (in microseconds) |
| `IOWAIT_DELTA` | `NUMBER` |  | Delta value of user I/O wait time (in microseconds) |
| `CLWAIT_TOTAL` | `NUMBER` |  | Cumulative value of cluster wait time (in microseconds) |
| `CLWAIT_DELTA` | `NUMBER` |  | Delta value of cluster wait time (in microseconds) |
| `APWAIT_TOTAL` | `NUMBER` |  | Cumulative value of application wait time (in microseconds) |
| `APWAIT_DELTA` | `NUMBER` |  | Delta value of application wait time (in microseconds) |
| `CCWAIT_TOTAL` | `NUMBER` |  | Cumulative value of concurrency wait time (in microseconds) |
| `CCWAIT_DELTA` | `NUMBER` |  | Delta value of concurrency wait time (in microseconds) |
| `DIRECT_WRITES_TOTAL` | `NUMBER` |  | Cumulative value of direct writes |
| `DIRECT_WRITES_DELTA` | `NUMBER` |  | Delta value of direct writes |
| `PLSEXEC_TIME_TOTAL` | `NUMBER` |  | Cumulative value of PL/SQL Execution Time (in microseconds) |
| `PLSEXEC_TIME_DELTA` | `NUMBER` |  | Delta value of PL/SQL Execution Time (in microseconds) |
| `JAVEXEC_TIME_TOTAL` | `NUMBER` |  | Cumulative value of Java Execution Time (in microseconds) |
| `JAVEXEC_TIME_DELTA` | `NUMBER` |  | Delta value of Java Execution Time (in microseconds) |
| `IO_OFFLOAD_ELIG_BYTES_TOTAL` | `NUMBER` |  | Cumulative value of number of I/O bytes which can be filtered by the Exadata storage system  See Also: Oracle Exadata Storage Server Software documentation for more information |
| `IO_OFFLOAD_ELIG_BYTES_DELTA` | `NUMBER` |  | Delta value of number of I/O bytes which can be filtered by the Exadata storage system  See Also: Oracle Exadata Storage Server Software documentation for more information |
| `IO_INTERCONNECT_BYTES_TOTAL` | `NUMBER` |  | Cumulative value of number of I/O bytes exchanged between Oracle Database and the storage system |
| `IO_INTERCONNECT_BYTES_DELTA` | `NUMBER` |  | Delta value of number of I/O bytes exchanged between Oracle Database and the storage system |
| `PHYSICAL_READ_REQUESTS_TOTAL` | `NUMBER` |  | Cumulative value of number of physical read I/O requests issued by the monitored SQL |
| `PHYSICAL_READ_REQUESTS_DELTA` | `NUMBER` |  | Delta value of number of physical read I/O requests issued by the monitored SQL |
| `PHYSICAL_READ_BYTES_TOTAL` | `NUMBER` |  | Cumulative value of number of bytes read from disks by the monitored SQL |
| `PHYSICAL_READ_BYTES_DELTA` | `NUMBER` |  | Delta value of number of bytes read from disks by the monitored SQL |
| `PHYSICAL_WRITE_REQUESTS_TOTAL` | `NUMBER` |  | Cumulative value of number of physical write I/O requests issued by the monitored SQL |
| `PHYSICAL_WRITE_REQUESTS_DELTA` | `NUMBER` |  | Delta value of number of physical write I/O requests issued by the monitored SQL |
| `PHYSICAL_WRITE_BYTES_TOTAL` | `NUMBER` |  | Cumulative value of number of bytes written to disks by the monitored SQL |
| `PHYSICAL_WRITE_BYTES_DELTA` | `NUMBER` |  | Delta value of number of bytes written to disks by the monitored SQL |
| `OPTIMIZED_PHYSICAL_READS_TOTAL` | `NUMBER` |  | Cumulative value of number of physical reads from the Database Smart Flash Cache or the Exadata Smart Flash Cache by the monitored SQL |
| `OPTIMIZED_PHYSICAL_READS_DELTA` | `NUMBER` |  | Delta value of number of physical reads from the Database Smart Flash Cache or the Exadata Smart Flash Cache by the monitored SQL |
| `CELL_UNCOMPRESSED_BYTES_TOTAL` | `NUMBER` |  | Cumulative value of number of uncompressed bytes (that is, size after decompression) that are offloaded to the Exadata cells  See Also: Oracle Exadata Storage Server Software documentation for more information |
| `CELL_UNCOMPRESSED_BYTES_DELTA` | `NUMBER` |  | Delta value of number of uncompressed bytes (that is, size after decompression) that are offloaded to the Exadata cells  See Also: Oracle Exadata Storage Server Software documentation for more information |
| `IO_OFFLOAD_RETURN_BYTES_TOTAL` | `NUMBER` |  | Cumulative value of number of bytes that are returned by the Exadata cell for smart scan only (that is, not including bytes for other database I/O)  See Also: Oracle Exadata Storage Server Software documentation for more information |
| `IO_OFFLOAD_RETURN_BYTES_DELTA` | `NUMBER` |  | Delta value of number of bytes that are returned by the Exadata cell for smart scan only (that is, not including bytes for other database I/O)  See Also: Oracle Exadata Storage Server Software documentation for more information |
| `BIND_DATA` | `RAW(2000)` |  | Bind data |
| `FLAG` | `NUMBER` |  | Reserved for internal use |
| `OBSOLETE_COUNT` | `NUMBER` |  | Number of times that a parent cursor became obsolete |
| `CON_DBID` | `NUMBER` |  | The database ID of the PDB for the sampled session |
| `CON_ID` | `NUMBER` |  | The ID of the container that `CON_DBID` identifies. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |