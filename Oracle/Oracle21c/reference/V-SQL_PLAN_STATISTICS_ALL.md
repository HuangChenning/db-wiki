---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-SQL_PLAN_STATISTICS_ALL.html
tags:
  - oracle
  - 21c
  - reference
---

## 10.62 V$SQL\_PLAN\_STATISTICS\_ALL

This view concatenates information in `V$SQL_PLAN` with execution statistics from `V$SQL_PLAN_STATISTICS` and `V$SQL_WORKAREA`.

| Column | Datatype | Description |
| --- | --- | --- |
| `ADDRESS` | `RAW(4 \| 8)` | Address of the handle to the parent for this cursor |
| `HASH_VALUE` | `NUMBER` | Hash value of the parent statement in the library cache. The two columns `ADDRESS` and `HASH_VALUE` can be used to join with `V$SQLAREA` to add the cursor-specific information. |
| `SQL_ID` | `VARCHAR2(13)` | SQL identifier of the parent statement in the library cache |
| `PLAN_HASH_VALUE` | `NUMBER` | Numerical representation of the current SQL plan for this cursor. Comparing one `PLAN_HASH_VALUE` to another easily identifies whether or not two plans are the same (rather than comparing the two plans line by line) |
| `FULL_PLAN_HASH_VALUE` | `NUMBER` | Numeric representation of the complete SQL plan for this cursor. Comparing one `FULL_PLAN_HASH_VALUE` to another easily identifies whether or not two plans are the same (rather than comparing the two plans line by line). Note that the `FULL_PLAN_HASH_VALUE` cannot be compared across databases releases. It is not backward compatible. |
| `CHILD_ADDRESS` | `RAW(4 \| 8)` | Address of the child cursor |
| `CHILD_NUMBER` | `NUMBER` | Number of the child cursor that uses this execution plan. The columns `ADDRESS`, `HASH_VALUE`, and `CHILD_NUMBER` can be used to join with `V$SQL` to add the child cursor-specific information. |
| `TIMESTAMP` | `DATE` | Date and time when the execution plan was generated |
| `OPERATION` | `VARCHAR2(120)` | Name of the internal operation performed in this step (for example, `TABLE ACCESS`) |
| `OPTIONS` | `VARCHAR2(120)` | A variation on the operation described in the `OPERATION` column (for example, `FULL`) |
| `OBJECT_NODE` | `VARCHAR2(160)` | Name of the database link used to reference the object (a table name or view name). For local queries that use parallel execution, this column describes the order in which output from operations is consumed. |
| `OBJECT#` | `NUMBER` | Object number of the table or the index |
| `OBJECT_OWNER` | `VARCHAR2(128)` | Name of the user who owns the schema containing the table or index |
| `OBJECT_NAME` | `VARCHAR2(128)` | Name of the table or index |
| `OBJECT_ALIAS` | `VARCHAR2(261)` | Alias for the object |
| `OBJECT_TYPE` | `VARCHAR2(80)` | Type of the object |
| `OPTIMIZER` | `VARCHAR2(80)` | Current mode of the optimizer for the first row in the plan (statement line), for example, `CHOOSE`. When the operation is a database access (for example, `TABLE ACCESS`), this column indicates whether or not the object is analyzed. |
| `ID` | `NUMBER` | A number assigned to each step in the execution plan |
| `PARENT_ID` | `NUMBER` | ID of the next execution step that operates on the output of the current step |
| `DEPTH` | `NUMBER` | Depth (or level) of the operation in the tree. It is not necessary to issue a `CONNECT BY` statement to get the level information, which is generally used to indent the rows from the `PLAN_TABLE` table. The root operation (statement) is level 0. |
| `POSITION` | `NUMBER` | Order of processing for all operations that have the same `PARENT_ID` |
| `SEARCH_COLUMNS` | `NUMBER` | Number of index columns with start and stop keys (that is, the number of columns with matching predicates) |
| `COST` | `NUMBER` | Cost of the operation as estimated by the optimizer's cost-based approach. For statements that use the rule-based approach, this column is null. |
| `CARDINALITY` | `NUMBER` | Estimate, by the cost-based optimizer, of the number of rows produced by the operation |
| `BYTES` | `NUMBER` | Estimate, by the cost-based optimizer, of the number of bytes produced by the operation |
| `OTHER_TAG` | `VARCHAR2(140)` | Describes the contents of the `OTHER` column. See `EXPLAIN PLAN` for values. |
| `PARTITION_START` | `VARCHAR2(256)` | Start partition of a range of accessed partitions |
| `PARTITION_STOP` | `VARCHAR2(256)` | Stop partition of a range of accessed partitions |
| `PARTITION_ID` | `NUMBER` | Step that computes the pair of values of the `PARTITION_START` and `PARTITION_STOP` columns |
| `OTHER` | `VARCHAR2(4000)` | Other information specific to the execution step that users may find useful. See `EXPLAIN PLAN` for values. |
| `DISTRIBUTION` | `VARCHAR2(80)` | Stores the method used to distribute rows from producer query servers to consumer query servers |
| `CPU_COST` | `NUMBER` | CPU cost of the operation as estimated by the optimizer's cost-based approach. For statements that use the rule-based approach, this column is null. |
| `IO_COST` | `NUMBER` | I/O cost of the operation as estimated by the optimizer's cost-based approach. For statements that use the rule-based approach, this column is null. |
| `TEMP_SPACE` | `NUMBER` | Temporary space usage of the operation (sort or hash-join) as estimated by the optimizer's cost-based approach. For statements that use the rule-based approach, this column is null. |
| `ACCESS_PREDICATES` | `VARCHAR2(4000)` | Predicates used to locate rows in an access structure. For example, start or stop predicates for an index range scan. |
| `FILTER_PREDICATES` | `VARCHAR2(4000)` | Predicates used to filter rows before producing them |
| `PROJECTION` | `VARCHAR2(4000)` | Expressions produced by the operation |
| `TIME` | `NUMBER` | Elapsed time (in seconds) of the operation as estimated by the optimizer's cost-based approach. For statements that use the rule-based approach, this column is null. |
| `QBLOCK_NAME` | `VARCHAR2(128)` | Name of the query block |
| `REMARKS` | `VARCHAR2(4000)` | Remarks |
| `OTHER_XML` | `CLOB` | Provides extra information specific to an execution step of the execution plan. The content of this column is structured using XML since multiple pieces of information can be stored there. This includes:  - Name of the schema against which the query was parsed - Release number of the Oracle Database that produced the explain plan - Hash value associated with the execution plan - Name (if any) of the outline or the SQL profile used to build the execution plan - Indication of whether or not dynamic statistics were used to produce the plan - The outline data, a set of optimizer hints that can be used to regenerate the same plan - Additional data that describes the relationship between rows in the plan table and subplans of adaptive plans. Note that in Oracle Database 12c, there will be extra rows in the plan table and `V$SQL_PLAN`. |
| `EXECUTIONS` | `NUMBER` | Number of times this cursor has been executed |
| `LAST_STARTS` | `NUMBER` | Number of times this operation has been started, during the last execution |
| `STARTS` | `NUMBER` | Number of times this operation has been started, accumulated over the past executions |
| `LAST_OUTPUT_ROWS` | `NUMBER` | Number of rows produced by the row source, during the last execution |
| `OUTPUT_ROWS` | `NUMBER` | Number of rows produced by the row source, accumulated over the past executions |
| `LAST_CR_BUFFER_GETS` | `NUMBER` | Number of buffers retrieved in consistent mode, during the last execution. Buffers are usually retrieved in consistent mode for queries. |
| `CR_BUFFER_GETS` | `NUMBER` | Number of buffers retrieved in consistent mode, accumulated over the past executions. Buffers are usually retrieved in consistent mode for queries. |
| `LAST_CU_BUFFER_GETS` | `NUMBER` | Number of buffers retrieved in current mode, during the last execution. Buffers are retrieved in current mode for statements such as `INSERT`, `UPDATE`, and `DELETE`. |
| `CU_BUFFER_GETS` | `NUMBER` | Number of buffers retrieved in current mode, accumulated over the past executions. Buffers are retrieved in current mode for statements such as `INSERT`, `UPDATE`, and `DELETE`. |
| `LAST_DISK_READS` | `NUMBER` | Number of physical disk reads performed by the operation, during the last execution |
| `DISK_READS` | `NUMBER` | Number of physical disk reads performed by the operation, accumulated over the past executions |
| `LAST_DISK_WRITES` | `NUMBER` | Number of physical disk writes performed by the operation, during the last execution |
| `DISK_WRITES` | `NUMBER` | Number of physical disk writes performed by the operation, accumulated over the past executions |
| `LAST_ELAPSED_TIME` | `NUMBER` | Elapsed time (in microseconds) corresponding to this operation, during the last execution |
| `ELAPSED_TIME` | `NUMBER` | Elapsed time (in microseconds) corresponding to this operation, accumulated over the past executions |
| `POLICY` | `VARCHAR2(40)` | Sizing policy for this work area:  - `MANUAL` - `AUTO` |
| `ESTIMATED_OPTIMAL_SIZE` | `NUMBER` | Estimated size (in KB) required by this work area to execute the operation completely in memory (optimal execution). This is either derived from optimizer statistics or from previous executions. |
| `ESTIMATED_ONEPASS_SIZE` | `NUMBER` | Estimated size (in KB) required by this work area to execute the operation in a single pass. This is either derived from optimizer statistics or from previous executions. |
| `LAST_MEMORY_USED` | `NUMBER` | Memory size (in KB) used by this work area during the last execution of the cursor |
| `LAST_EXECUTION` | `VARCHAR2(40)` | Indicates whether this work area ran using `OPTIMAL`, `ONE PASS`, or under `ONE PASS` memory requirement (`MULTI-PASS`), during the last execution of the cursor |
| `LAST_DEGREE` | `NUMBER` | Degree of parallelism used, during the last execution of the cursor |
| `TOTAL_EXECUTIONS` | `NUMBER` | Number of times this work area was active |
| `OPTIMAL_EXECUTIONS` | `NUMBER` | Number of times this work area ran in optimal mode |
| `ONEPASS_EXECUTIONS` | `NUMBER` | Number of times this work area ran in one pass mode |
| `MULTIPASSES_EXECUTIONS` | `NUMBER` | Number of times this work area ran below the one pass memory requirement |
| `ACTIVE_TIME` | `NUMBER` | Average time this work area is active (in hundredths of a second) |
| `MAX_TEMPSEG_SIZE` | `NUMBER` | Maximum temporary segment size (in bytes) created by an instantiation of this work area. This column is null if this work area has never spilled to disk. |
| `LAST_TEMPSEG_SIZE` | `NUMBER` | Temporary segment size (in bytes) created in the last instantiation of this work area. This column is null if the last instantiation of this work area did not spill to disk. |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |
| `CON_DBID` | `NUMBER` | The database ID of the PDB |

See Also:

- " [V$SQL\_PLAN\_STATISTICS](V-SQL_PLAN_STATISTICS.md) "
- " [V$SQL\_WORKAREA](V-SQL_WORKAREA.md) "