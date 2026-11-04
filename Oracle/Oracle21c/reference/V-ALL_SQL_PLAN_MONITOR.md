---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-ALL_SQL_PLAN_MONITOR.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.15 V$ALL\_SQL\_PLAN\_MONITOR

`V$ALL_SQL_PLAN_MONITOR` displays plan level monitoring statistics for each SQL statement found in `V$ALL_SQL_MONITOR`.

Note:

`V$ALL_SQL_PLAN_MONITOR` allows application developers to view statistics about their own SQL statements. It is similar to the `V$SQL_PLAN_MONITOR` view, with the following exception:

- When queried by a user with the `SYSDBA` privilege, the `V$ALL_SQL_PLAN_MONITOR` view displays the same data as the `V$SQL_PLAN_MONITOR` view.
- When queried by any other user, the `V$ALL_SQL_PLAN_MONITOR` view displays data only about SQL statements that were executed in sessions owned by that user.

See also " [V$SQL\_PLAN\_MONITOR](V-SQL_PLAN_MONITOR.md) "

| Column | Datatype | Description |
| --- | --- | --- |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |
| `KEY` | `NUMBER` | Foreign key to efficiently join `V$ALL_SQL_PLAN_MONITOR` with `V$ALL_SQL_MONITOR` (see `V$ALL_SQL_MONITOR`) |
| `STATUS` | `VARCHAR2(19)` | SQL execution status:  - `EXECUTING` - SQL statement is still executing - `DONE (ERROR)` - Execution terminated with an error - `DONE (FIRST N ROWS)` - Execution terminated by the application before all rows were fetched - `DONE (ALL ROWS)` - Execution terminated and all rows were fetched - `DONE` - Execution terminated (parallel execution) |
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
| `SQL_CHILD_ADDRESS` | `RAW(8)` | Address of the child cursor |
| `PLAN_PARENT_ID` | `NUMBER` | ID of the next execution step that operates on the output of the current step |
| `PLAN_LINE_ID` | `NUMBER` | Plan line number for the entry |
| `PLAN_OPERATION` | `VARCHAR2(30)` | Plan operation name (from `V$SQL_PLAN`) |
| `PLAN_OPTIONS` | `VARCHAR2(30)` | Plan option name (from `V$SQL_PLAN`) |
| `PLAN_OBJECT_OWNER` | `VARCHAR2(128)` | Name of the user who owns the schema containing the table or index |
| `PLAN_OBJECT_NAME` | `VARCHAR2(128)` | Name of the table or index |
| `PLAN_OBJECT_TYPE` | `VARCHAR2(80)` | Type of the object |
| `PLAN_DEPTH` | `NUMBER` | Depth (or level) of the operation in the tree. It is not necessary to issue a `CONNECT BY` statement to get the level information, which is generally used to indent the rows from the `PLAN_TABLE` table. The root operation (statement) is level 0. |
| `PLAN_POSITION` | `NUMBER` | Order of processing for all operations that have the same `PARENT_ID` |
| `PLAN_COST` | `NUMBER` | Cost of the operation as estimated by the optimizer's cost-based approach. For statements that use the rule-based approach, this column is NULL. |
| `PLAN_CARDINALITY` | `NUMBER` | Estimate, by the cost-based optimizer, of the number of rows produced by the operation |
| `PLAN_BYTES` | `NUMBER` | Estimate, by the cost-based optimizer, of the number of bytes produced by the operation |
| `PLAN_TIME` | `NUMBER` | Elapsed time (in seconds) of the operation as estimated by the optimizer's cost-based approach. For statements that use the rule-based approach, this column is NULL. |
| `PLAN_PARTITION_START` | `VARCHAR2(256)` | Start partition of a range of accessed partitions |
| `PLAN_PARTITION_STOP` | `VARCHAR2(256)` | Stop partition of a range of accessed partitions |
| `PLAN_CPU_COST` | `NUMBER` | CPU cost of the operation as estimated by the optimizer's cost-based approach. For statements that use the rule-based approach, this column is NULL. |
| `PLAN_IO_COST` | `NUMBER` | I/O cost of the operation as estimated by the optimizer's cost-based approach. For statements that use the rule-based approach, this column is NULL. |
| `PLAN_TEMP_SPACE` | `NUMBER` | Temporary space usage of the operation (sort or hash-join) as estimated by the optimizer's cost-based approach. For statements that use the rule-based approach, this column is NULL. |
| `STARTS` | `NUMBER` | Number of times this operation was executed. For example, an operation is executed multiple times when it is on the right side of a nested-loop join (once for each row of the left input of that nested-loop join). |
| `OUTPUT_ROWS` | `NUMBER` | Number of rows produced by this operation since the execution started. This number is cumulated for all executions of this operation. Divide by the value of the STARTS column to compute the average number of rows per execution of the operation. Note that the value in the `STARTS` column is equal to or higher than the value in the `OUTPUT_ROWS` column. The value will usually be equal, but depending on internal optimizations a higher value may be seen. |
| `IO_INTERCONNECT_BYTES` | `NUMBER` | Number of I/O bytes exchanged between Oracle Database and the storage system. Maintained only after Oracle starts to monitor the execution. |
| `PHYSICAL_READ_REQUESTS` | `NUMBER` | Number of physical read I/O requests issued by the monitored SQL. Maintained only after Oracle starts to monitor the execution. |
| `PHYSICAL_READ_BYTES` | `NUMBER` | Number of bytes read from disks by the monitored SQL. Maintained only after Oracle starts to monitor the execution. |
| `PHYSICAL_WRITE_REQUESTS` | `NUMBER` | Number of physical write I/O requests issued by the monitored SQL. Maintained only after Oracle starts to monitor the execution. |
| `PHYSICAL_WRITE_BYTES` | `NUMBER` | Number of bytes written to disks by the monitored SQL. Maintained only after Oracle starts to monitor the execution. |
| `WORKAREA_MEM` | `NUMBER` | Amount of memory (in bytes) used by the operation when the query is executing; NULL if the execution is done. This applies only to operations using a work area, such as sort, hash-join, group-by, and so on. |
| `WORKAREA_MAX_MEM` | `NUMBER` | Maximum value (in bytes) for `WORKAREA_MEM`; NULL if the operation is not using a work area. When the execution is finished, this value will hold the maximum amount of memory consumed by this operation during the execution of the statement. |
| `WORKAREA_TEMPSEG` | `NUMBER` | Amount of temporary space (in bytes) used by the operation when the query is executing; NULL if the operation has not spilled to disk or if the execution is finished |
| `WORKAREA_MAX_TEMPSEG` | `NUMBER` | Maximum value (in bytes) for `WORKAREA_TEMPSEG`; NULL if this operation never spilled to disk. When the execution is done, this value will hold the maximum amount of temporary space consumed by this operation during the entire execution. |
| `OTHERSTAT_GROUP_ID` | `NUMBER` | Plan line statistic group identifier (see `GROUP_ID` column in `V$SQL_MONITOR_STATNAME`) |
| `OTHERSTAT_1_ID` | `NUMBER` | Statistic identifier (see `ID` column in `V$SQL_MONITOR_STATNAME`) for statistic number 1 of that plan line |
| `OTHERSTAT_1_TYPE` | `NUMBER` | Reserved for internal use |
| `OTHERSTAT_1_VALUE` | `NUMBER` | Value of statistic number 1 of that plan line |
| `OTHERSTAT_2_ID` | `NUMBER` | Statistic identifier (see `ID` column in `V$SQL_MONITOR_STATNAME`) for statistic number 2 of that plan line |
| `OTHERSTAT_2_TYPE` | `NUMBER` | Reserved for internal use |
| `OTHERSTAT_2_VALUE` | `NUMBER` | Value of statistic number 2 of that plan line |
| `OTHERSTAT_3_ID` | `NUMBER` | Statistic identifier (see `ID` column in `V$SQL_MONITOR_STATNAME`) for statistic number 3 of that plan line |
| `OTHERSTAT_3_TYPE` | `NUMBER` | Reserved for internal use |
| `OTHERSTAT_3_VALUE` | `NUMBER` | Value of statistic number 3 of that plan line |
| `OTHERSTAT_4_ID` | `NUMBER` | Statistic identifier (see `ID` column in `V$SQL_MONITOR_STATNAME`) for statistic number 4 of that plan line |
| `OTHERSTAT_4_TYPE` | `NUMBER` | Reserved for internal use |
| `OTHERSTAT_4_VALUE` | `NUMBER` | Value of statistic number 4 of that plan line |
| `OTHERSTAT_5_ID` | `NUMBER` | Statistic identifier (see `ID` column in `V$SQL_MONITOR_STATNAME`) for statistic number 5 of that plan line |
| `OTHERSTAT_5_TYPE` | `NUMBER` | Reserved for internal use |
| `OTHERSTAT_5_VALUE` | `NUMBER` | Value of statistic number 5 of that plan line |
| `OTHERSTAT_6_ID` | `NUMBER` | Statistic identifier (see `ID` column in `V$SQL_MONITOR_STATNAME`) for statistic number 6 of that plan line |
| `OTHERSTAT_6_TYPE` | `NUMBER` | Reserved for internal use |
| `OTHERSTAT_6_VALUE` | `NUMBER` | Value of statistic number 6 of that plan line |
| `OTHERSTAT_7_ID` | `NUMBER` | Statistic identifier (see `ID` column in `V$SQL_MONITOR_STATNAME`) for statistic number 7 of that plan line |
| `OTHERSTAT_7_TYPE` | `NUMBER` | Reserved for internal use |
| `OTHERSTAT_7_VALUE` | `NUMBER` | Value of statistic number 7 of that plan line |
| `OTHERSTAT_8_ID` | `NUMBER` | Statistic identifier (see `ID` column in `V$SQL_MONITOR_STATNAME`) for statistic number 8 of that plan line |
| `OTHERSTAT_8_TYPE` | `NUMBER` | Reserved for internal use |
| `OTHERSTAT_8_VALUE` | `NUMBER` | Value of statistic number 8 of that plan line |
| `OTHERSTAT_9_ID` | `NUMBER` | Statistic identifier (see `ID` column in `V$SQL_MONITOR_STATNAME`) for statistic number 9 of that plan line |
| `OTHERSTAT_9_TYPE` | `NUMBER` | Reserved for internal use |
| `OTHERSTAT_9_VALUE` | `NUMBER` | Value of statistic number 9 of that plan line |
| `OTHERSTAT_10_ID` | `NUMBER` | Statistic identifier (see `ID` column in `V$SQL_MONITOR_STATNAME`) for statistic number 10 of that plan line |
| `OTHERSTAT_10_TYPE` | `NUMBER` | Reserved for internal use |
| `OTHERSTAT_10_VALUE` | `NUMBER` | Value of statistic number 10 of that plan line |
| `OTHERSTAT_11_ID` | `NUMBER` | Statistic identifier (see `ID` column in `V$SQL_MONITOR_STATNAME`) for statistic number 11 of that plan line |
| `OTHERSTAT_11_TYPE` | `NUMBER` | Reserved for internal use |
| `OTHERSTAT_11_VALUE` | `NUMBER` | Value of statistic number 11 of that plan line |
| `OTHERSTAT_12_ID` | `NUMBER` | Statistic identifier (see `ID` column in `V$SQL_MONITOR_STATNAME`) for statistic number 12 of that plan line |
| `OTHERSTAT_12_TYPE` | `NUMBER` | Reserved for internal use |
| `OTHERSTAT_12_VALUE` | `NUMBER` | Value of statistic number 12 of that plan line |
| `OTHERSTAT_13_ID` | `NUMBER` | Statistic identifier (see `ID` column in `V$SQL_MONITOR_STATNAME`) for statistic number 13 of that plan line |
| `OTHERSTAT_13_TYPE` | `NUMBER` | Reserved for internal use |
| `OTHERSTAT_13_VALUE` | `NUMBER` | Value of statistic number 13 of that plan line |
| `OTHERSTAT_14_ID` | `NUMBER` | Statistic identifier (see `ID` column in `V$SQL_MONITOR_STATNAME`) for statistic number 14 of that plan line |
| `OTHERSTAT_14_TYPE` | `NUMBER` | Reserved for internal use |
| `OTHERSTAT_14_VALUE` | `NUMBER` | Value of statistic number 14 of that plan line |
| `OTHERSTAT_15_ID` | `NUMBER` | Statistic identifier (see `ID` column in `V$SQL_MONITOR_STATNAME`) for statistic number 15 of that plan line |
| `OTHERSTAT_15_TYPE` | `NUMBER` | Reserved for internal use |
| `OTHERSTAT_15_VALUE` | `NUMBER` | Value of statistic number 15 of that plan line |
| `OTHERSTAT_16_ID` | `NUMBER` | Statistic identifier (see `ID` column in `V$SQL_MONITOR_STATNAME`) for statistic number 16 of that plan line |
| `OTHERSTAT_16_TYPE` | `NUMBER` | Reserved for internal use |
| `OTHERSTAT_16_VALUE` | `NUMBER` | Value of statistic number 16 of that plan line |
| `OTHERSTAT_17_ID` | `NUMBER` | Statistic identifier (see `ID` column in `V$SQL_MONITOR_STATNAME`) for statistic number 17 of that plan line |
| `OTHERSTAT_17_TYPE` | `NUMBER` | Reserved for internal use |
| `OTHERSTAT_17_VALUE` | `NUMBER` | Value of statistic number 17 of that plan line |
| `OTHERSTAT_18_ID` | `NUMBER` | Statistic identifier (see `ID` column in `V$SQL_MONITOR_STATNAME`) for statistic number 18 of that plan line |
| `OTHERSTAT_18_TYPE` | `NUMBER` | Reserved for internal use |
| `OTHERSTAT_18_VALUE` | `NUMBER` | Value of statistic number 18 of that plan line |
| `OTHERSTAT_19_ID` | `NUMBER` | Statistic identifier (see `ID` column in `V$SQL_MONITOR_STATNAME`) for statistic number 19 of that plan line |
| `OTHERSTAT_19_TYPE` | `NUMBER` | Reserved for internal use |
| `OTHERSTAT_19_VALUE` | `NUMBER` | Value of statistic number 19 of that plan line |
| `OTHERSTAT_20_ID` | `NUMBER` | Statistic identifier (see `ID` column in `V$SQL_MONITOR_STATNAME`) for statistic number 20 of that plan line |
| `OTHERSTAT_20_TYPE` | `NUMBER` | Reserved for internal use |
| `OTHERSTAT_20_VALUE` | `NUMBER` | Value of statistic number 20 of that plan line |
| `OTHERSTAT_21_ID` | `NUMBER` | Statistic identifier (see `ID` column in `V$SQL_MONITOR_STATNAME`) for statistic number 21 of that plan line |
| `OTHERSTAT_21_TYPE` | `NUMBER` | Reserved for internal use |
| `OTHERSTAT_21_VALUE` | `NUMBER` | Value of statistic number 21 of that plan line |
| `OTHERSTAT_22_ID` | `NUMBER` | Statistic identifier (see `ID` column in `V$SQL_MONITOR_STATNAME`) for statistic number 22 of that plan line |
| `OTHERSTAT_22_TYPE` | `NUMBER` | Reserved for internal use |
| `OTHERSTAT_22_VALUE` | `NUMBER` | Value of statistic number 22 of that plan line |
| `OTHERSTAT_23_ID` | `NUMBER` | Statistic identifier (see `ID` column in `V$SQL_MONITOR_STATNAME`) for statistic number 23 of that plan line |
| `OTHERSTAT_23_TYPE` | `NUMBER` | Reserved for internal use |
| `OTHERSTAT_23_VALUE` | `NUMBER` | Value of statistic number 23 of that plan line |
| `OTHERSTAT_24_ID` | `NUMBER` | Statistic identifier (see `ID` column in `V$SQL_MONITOR_STATNAME`) for statistic number 24 of that plan line |
| `OTHERSTAT_24_TYPE` | `NUMBER` | Reserved for internal use |
| `OTHERSTAT_24_VALUE` | `NUMBER` | Value of statistic number 24 of that plan line |
| `OTHERSTAT_25_ID` | `NUMBER` | Statistic identifier (see `ID` column in `V$SQL_MONITOR_STATNAME`) for statistic number 25 of that plan line |
| `OTHERSTAT_25_TYPE` | `NUMBER` | Reserved for internal use |
| `OTHERSTAT_25_VALUE` | `NUMBER` | Value of statistic number 25 of that plan line |
| `OTHERSTAT_26_ID` | `NUMBER` | Statistic identifier (see `ID` column in `V$SQL_MONITOR_STATNAME`) for statistic number 26 of that plan line |
| `OTHERSTAT_26_TYPE` | `NUMBER` | Reserved for internal use |
| `OTHERSTAT_26_VALUE` | `NUMBER` | Value of statistic number 26 of that plan line |
| `OTHERSTAT_27_ID` | `NUMBER` | Statistic identifier (see `ID` column in `V$SQL_MONITOR_STATNAME`) for statistic number 27 of that plan line |
| `OTHERSTAT_27_TYPE` | `NUMBER` | Reserved for internal use |
| `OTHERSTAT_27_VALUE` | `NUMBER` | Value of statistic number 27 of that plan line |
| `OTHERSTAT_28_ID` | `NUMBER` | Statistic identifier (see `ID` column in `V$SQL_MONITOR_STATNAME`) for statistic number 28 of that plan line |
| `OTHERSTAT_28_TYPE` | `NUMBER` | Reserved for internal use |
| `OTHERSTAT_28_VALUE` | `NUMBER` | Value of statistic number 28 of that plan line |
| `OTHERSTAT_29_ID` | `NUMBER` | Statistic identifier (see `ID` column in `V$SQL_MONITOR_STATNAME`) for statistic number 29 of that plan line |
| `OTHERSTAT_29_TYPE` | `NUMBER` | Reserved for internal use |
| `OTHERSTAT_29_VALUE` | `NUMBER` | Value of statistic number 29 of that plan line |
| `OTHERSTAT_30_ID` | `NUMBER` | Statistic identifier (see `ID` column in `V$SQL_MONITOR_STATNAME`) for statistic number 30 of that plan line |
| `OTHERSTAT_30_TYPE` | `NUMBER` | Reserved for internal use |
| `OTHERSTAT_30_VALUE` | `NUMBER` | Value of statistic number 30 of that plan line |
| `OTHER_XML` | `CLOB` | Provides extra information specific to an execution step of the execution plan. The content of this column is structured using XML because it allows multiple pieces of information to be stored, including the following:  - Name of the schema against which the query was parsed - Release number of the Oracle Database that produced the explain plan - Hash value associated with the execution plan - Name (if any) of the outline or the SQL profile used to build the execution plan - Indication of whether or not dynamic statistics were used to produce the plan - The outline data, a set of optimizer hints that can be used to regenerate the same plan |
| `PLAN_OPERATION_INACTIVE` | `NUMBER` | Indicates whether this plan operation was part of the final resolved plan |