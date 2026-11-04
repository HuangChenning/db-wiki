---
title: "V$SQL_PLAN_MONITOR"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_3055.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$SQL_PLAN_MONITOR` displays plan level monitoring statistics for each SQL statement found in `V$SQL_MONITOR`. Each row in `V$SQL_PLAN_MONITOR` corresponds to an operation of the execution plan being monitored. As with `V$SQL_MONITOR`, statistics exposed in `V$SQL_PLAN_MONITOR` are generally updated every second when the statement executes. These statistics are recycled on the same basis as `V$SQL_MONITOR`.

To eliminate the overhead of SQL plan monitoring, statistics collected for each operation of the plan don't record timing information such as elapsed time, CPU time, or I/O time. Instead, this timing information can be estimated quite accurately by joining `V$SQL_PLAN_MONITOR` with `V$ACTIVE_SESSION_HISTORY` on `SQL_ID`, `SQL_EXEC_START`, `SQL_EXEC_ID`, and `SQL_PLAN_LINE_ID` (simply named `PLAN_LINE_ID` in `V$SQL_PLAN_MONITOR`). The result of that join is a sample of the activity performed by each operation in the plan, from which an estimate of CPU time and wait time can be derived. This can be achieved by breaking statement level monitoring time statistics found in `V$SQL_MONITOR` in proportion to the number of samples found in `V$ACTIVE_SESSION_HISTORY` for the corresponding activity type.

| Column | Datatype | Description |
| --- | --- | --- |
| `KEY` | `NUMBER` | Foreign key to efficiently join `V$SQL_PLAN_MONITOR` with `V$SQL_MONITOR` (see `V$SQL_MONITOR`) |
| `STATUS` | `VARCHAR2(19)` | SQL execution status: - `EXECUTING` - SQL statement is still executing - `DONE (ERROR)` - Execution terminated with an error - `DONE (FIRST N ROWS)` - Execution terminated by the application before all rows were fetched - `DONE (ALL ROWS)` - Execution terminated and all rows were fetched - `DONE` - Execution terminated (parallel execution) |
| `FIRST_REFRESH_TIME` | `DATE` | Time when monitoring of the SQL statement started |
| `LAST_REFRESH_TIME` | `DATE` | Time when statistics were last updated for the SQL statement |
| `FIRST_CHANGE_TIME` | `DATE` | First time a row was produced by this operation |
| `LAST_CHANGE_TIME` | `DATE` | Last time a row was produced by this operation |
| `REFRESH_COUNT` | `NUMBER` | Number of times statistics have been refreshed |
| `SID` | `NUMBER` | Session identifier executing (or having executed) the SQL statement being monitored |
| `PROCESS_NAME` | `VARCHAR2(5)` | Process name identifier |
| `SQL_ID` | `VARCHAR2(13)` | SQL identifier |
| `SQL_EXEC_START` | `DATE` | Time when the execution started |
| `SQL_EXEC_ID` | `NUMBER` | Execution identifier |
| `SQL_PLAN_HASH_VALUE` | `NUMBER` | SQL plan hash value |
| `SQL_CHILD_ADDRESS` | `RAW(4 \| 8)` | Address of the child cursor |
| `PLAN_PARENT_ID` | `NUMBER` | ID of the next execution step that operates on the output of the current step |
| `PLAN_LINE_ID` | `NUMBER` | Plan line number for the entry |
| `PLAN_OPERATION` | `VARCHAR2(30)` | Plan operation name (from `V$SQL_PLAN`) |
| `PLAN_OPTIONS` | `VARCHAR2(30)` | Plan option name (from `V$SQL_PLAN`) |
| `PLAN_OBJECT_OWNER` | `VARCHAR2(30)` | Name of the user who owns the schema containing the table or index |
| `PLAN_OBJECT_NAME` | `VARCHAR2(30)` | Name of the table or index |
| `PLAN_OBJECT_TYPE` | `VARCHAR2(20)` | Type of the object |
| `PLAN_DEPTH` | `NUMBER` | Depth (or level) of the operation in the tree. It is not necessary to issue a `CONNECT BY` statement to get the level information, which is generally used to indent the rows from the `PLAN_TABLE` table. The root operation (statement) is level 0. |
| `PLAN_POSITION` | `NUMBER` | Order of processing for all operations that have the same `PARENT_ID` |
| `PLAN_COST` | `NUMBER` | Cost of the operation as estimated by the optimizer's cost-based approach. For statements that use the rule-based approach, this column is NULL. |
| `PLAN_CARDINALITY` | `NUMBER` | Estimate, by the cost-based optimizer, of the number of rows produced by the operation |
| `PLAN_BYTES` | `NUMBER` | Estimate, by the cost-based optimizer, of the number of bytes produced by the operation |
| `PLAN_TIME` | `NUMBER` | Elapsed time (in seconds) of the operation as estimated by the optimizer's cost-based approach. For statements that use the rule-based approach, this column is NULL. |
| `PLAN_PARTITION_START` | `VARCHAR2(64)` | Start partition of a range of accessed partitions |
| `PLAN_PARTITION_STOP` | `VARCHAR2(64)` | Stop partition of a range of accessed partitions |
| `PLAN_CPU_COST` | `NUMBER` | CPU cost of the operation as estimated by the optimizer's cost-based approach. For statements that use the rule-based approach, this column is NULL. |
| `PLAN_IO_COST` | `NUMBER` | I/O cost of the operation as estimated by the optimizer's cost-based approach. For statements that use the rule-based approach, this column is NULL. |
| `PLAN_TEMP_SPACE` | `NUMBER` | Temporary space usage of the operation (sort or hash-join) as estimated by the optimizer's cost-based approach. For statements that use the rule-based approach, this column is NULL. |
| `STARTS` | `NUMBER` | Number of times this operation was executed. For example, an operation is executed multiple times when it is on the right side of a nested-loop join (once for each row of the left input of that nested-loop join). |
| `OUTPUT_ROWS` | `NUMBER` | Number of rows produced by this operation since the execution started. This number is cumulated for all executions of this operation. Divide by the value of the `STARTS` column to compute the average number of rows per execution of the operation. Note that the value in the `STARTS` column is equal to or higher than the value in the `OUTPUT_ROWS` column. The value will usually be equal, but depending on internal optimizations a higher value may be seen. |
| `IO_INTERCONNECT_BYTES` | `NUMBER` | Number of I/O bytes exchanged between Oracle Database and the storage system. Maintained only after Oracle starts to monitor the execution. |
| `PHYSICAL_READ_REQUESTS` | `NUMBER` | Number of physical read I/O requests issued by the monitored SQL. Maintained only after Oracle starts to monitor the execution. |
| `PHYSICAL_READ_BYTES` | `NUMBER` | Number of bytes read from disks by the monitored SQL. Maintained only after Oracle starts to monitor the execution. |
| `PHYSICAL_WRITE_REQUESTS` | `NUMBER` | Number of physical write I/O requests issued by the monitored SQL. Maintained only after Oracle starts to monitor the execution. |
| `PHYSICAL_WRITE_BYTES` | `NUMBER` | Number of bytes written to disks by the monitored SQL. Maintained only after Oracle starts to monitor the execution. |
| `WORKAREA_MEM` | `NUMBER` | Amount of memory (in bytes) used by the operation when the query is executing; NULL if the execution is done. This applies only to operations using a work area, such as sort, hash-join, group-by, and so on. |
| `WORKAREA_MAX_MEM` | `NUMBER` | Maximum value (in bytes) for `WORKAREA_MEM`; NULL if the operation is not using a work area. When the execution is finished, this value will hold the maximum amount of memory consumed by this operation during the execution of the statement. |
| `WORKAREA_TEMPSEG` | `NUMBER` | Amount of temporary space (in bytes) used by the operation when the query is executing; NULL if the operation has not spilled to disk or if the execution is finished |
| `WORKAREA_MAX_TEMPSEG` | `NUMBER` | Maximum value (in bytes) for `WORKAREA_TEMPSEG`; NULL if this operation never spilled to disk. When the execution is done, this value will hold the maximum amount of temporary space consumed by this operation during the entire execution. |