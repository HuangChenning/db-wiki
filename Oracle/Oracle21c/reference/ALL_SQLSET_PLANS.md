---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_SQLSET_PLANS.html
tags:
  - oracle
  - 21c
  - reference
---

## 4.83 ALL\_SQLSET\_PLANS

`ALL_SQLSET_PLANS` describes captured plans for statements in the SQL tuning sets accessible to the current user.

Related Views

- `DBA_SQLSET_PLANS` describes captured plans in the SQL tuning sets in the database.
- `USER_SQLSET_PLANS` describes captured plans for statements in the SQL tuning sets owned by the current user. This view does not display the `SQLSET_OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SQLSET_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of SQL tuning set for the statement |
| `SQLSET_OWNER` | `VARCHAR2(128)` |  | User name of SQL tuning set owner |
| `SQLSET_ID` | `NUMBER` | `NOT NULL` | ID of SQL tuning set for the statement |
| `CON_DBID` | `NUMBER` | `NOT NULL` | The database ID of the PDB |
| `SQL_ID` | `VARCHAR2(13)` | `NOT NULL` | SQL identifier of the parent cursor in the library cache |
| `FORCE_MATCHING_SIGNATURE` | `NUMBER` | `NOT NULL` | The signature used when the `CURSOR_SHARING` parameter is set to `FORCE` |
| `PLAN_HASH_VALUE` | `NUMBER` | `NOT NULL` | Numerical representation of the SQL plan for the cursor. Comparing one `PLAN_HASH_VALUE` to another easily identifies whether or not two plans are the same (rather than comparing the two plans line-by-line). |
| `SQL_SEQ` | `NUMBER` | `NOT NULL` | SQL sequence |
| `STATEMENT_ID` | `VARCHAR2(128)` |  | Statement ID |
| `PLAN_ID` | `NUMBER` |  | Plan ID |
| `TIMESTAMP` | `DATE` |  | Date and time timestamp |
| `REMARKS` | `VARCHAR2(4000)` |  | Remarks |
| `OPERATION` | `VARCHAR2(128)` |  | Name of the internal operation performed in this step (for example, `TABLE ACCESS`) |
| `OPTIONS` | `VARCHAR2(255)` |  | A variation on the operation described in the `OPERATION` column (for example, `FULL`) |
| `OBJECT_NODE` | `VARCHAR2(128)` |  | Name of the database link used to reference the object (a table name or view name). For local queries that use parallel execution, this column describes the order in which output from operations is consumed. |
| `OBJECT_OWNER` | `VARCHAR2(128)` |  | Name of the user who owns the schema containing the table or index |
| `OBJECT_NAME` | `VARCHAR2(128)` |  | Name of the table or index |
| `OBJECT_ALIAS` | `VARCHAR2(261)` |  | Alias for the object |
| `OBJECT_INSTANCE` | `NUMBER(38)` |  | Instance number for the object |
| `OBJECT_TYPE` | `VARCHAR2(128)` |  | Type of the object |
| `OPTIMIZER` | `VARCHAR2(255)` |  | Current mode of the optimizer for the first row in the plan (statement line), for example, `CHOOSE`. When the operation is a database access (for example, `TABLE ACCESS`), this column indicates whether or not the object is analyzed. |
| `SEARCH_COLUMNS` | `NUMBER` |  | Number of index columns with start and stop keys (that is, the number of columns with matching predicates) |
| `ID` | `NUMBER(38)` | `NOT NULL` | A number assigned to each step in the execution plan |
| `PARENT_ID` | `NUMBER(38)` |  | ID of the next execution step that operates on the output of the current step |
| `DEPTH` | `NUMBER(38)` |  | Depth (or level) of the operation in the tree. It is not necessary to issue a `CONNECT BY` statement to get the level information, which is generally used to indent the rows from the `PLAN_TABLE` table. The root operation (statement) is level 0. |
| `POSITION` | `NUMBER(38)` |  | Order of processing for all operations that have the same `PARENT_ID`. |
| `COST` | `NUMBER(38)` |  | Cost of the operation as estimated by the optimizer's cost-based approach. For statements that use the rule-based approach, this column is NULL. |
| `CARDINALITY` | `NUMBER(38)` |  | Estimate, made by the cost-based optimizer, of the number of rows produced by the operation |
| `BYTES` | `NUMBER(38)` |  | Estimate, made by the cost-based optimizer, of the number of bytes produced by the operation |
| `OTHER_TAG` | `VARCHAR2(255)` |  | Describes the contents of the `OTHER` column. For information about values, see [Oracle Database SQL Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=TGSQL271). |
| `PARTITION_START` | `VARCHAR2(255)` |  | Start partition of a range of accessed partitions |
| `PARTITION_STOP` | `VARCHAR2(255)` |  | Stop partition of a range of accessed partitions |
| `PARTITION_ID` | `NUMBER(38)` |  | Step that computes the pair of values of the `PARTITION_START` and `PARTITION_STOP` columns |
| `OTHER` | `LONG` |  | Other information specific to the execution step that users may find useful. For information about values, see [Oracle Database SQL Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=TGSQL271). |
| `DISTRIBUTION` | `VARCHAR2(128)` |  | Stores the method used to distribute rows from producer query servers to consumer query servers |
| `CPU_COST` | `NUMBER(38)` |  | CPU cost of the operation as estimated by the optimizer's cost-based approach. For statements that use the rule-based approach, this column is NULL. |
| `IO_COST` | `NUMBER(38)` |  | I/O cost of the operation as estimated by the optimizer's cost-based approach. For statements that use the rule-based approach, this column is NULL. |
| `TEMP_SPACE` | `NUMBER(38)` |  | Temporary space usage of the operation (sort or hash join) as estimated by the optimizer's cost-based approach. For statements that use the rule-based approach, this column is NULL. |
| `ACCESS_PREDICATES` | `VARCHAR2(4000)` |  | Predicates used to locate rows in an access structure. For example, start or stop predicates for an index range scan. |
| `FILTER_PREDICATES` | `VARCHAR2(4000)` |  | Predicates used to filter rows before producing them |
| `PROJECTION` | `VARCHAR2(4000)` |  | Expressions produced by the operation |
| `TIME` | `NUMBER(38)` |  | Elapsed time (in seconds) of the operation as estimated by the optimizer's cost-based approach. For statements that use the rule-based approach, this column is NULL. |
| `QBLOCK_NAME` | `VARCHAR2(128)` |  | Name of the query block |
| `OTHER_XML` | `CLOB` |  | Provides extra information specific to an execution step of the execution plan. The content of this column is structured using XML since multiple pieces of information can be stored there. This includes:  - Name of the schema against which the query was parsed - Release number of the Oracle Database that produced the explain plan - Hash value associated with the execution plan - Name (if any) of the outline or the SQL profile used to build the execution plan - Indication of whether or not dynamic statistics were used to produce the plan - The outline data, a set of optimizer hints that can be used to regenerate the same plan  For further information about values, see [Oracle Database SQL Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=TGSQL271). |
| `EXECUTIONS` | `NUMBER` |  | Number of times the plan has been executed |
| `STARTS` | `NUMBER` |  | Number of times this operation has been started, accumulated over the past executions |
| `OUTPUT_ROWS` | `NUMBER` |  | Number of rows produced by the row source, accumulated over the past executions |
| `CR_BUFFER_GETS` | `NUMBER` |  | Number of buffers received in consistent mode, accumulated over the past executions. Buffers are usually retrieved in consistent mode for queries. |
| `CU_BUFFER_GETS` | `NUMBER` |  | Number of buffers retrieved in current mode, accumulated over the past executions. Buffers are retrieved in current mode for statements such as `INSERT`, `UPDATE`, and `DELETE`. |
| `DISK_READS` | `NUMBER` |  | Number of physical disk reads performed by the operation, accumulated over the past executions |
| `DISK_WRITES` | `NUMBER` |  | Number of physical disk writes performed by the operation, accumulated over the past executions |
| `ELAPSED_TIME` | `NUMBER` |  | Elapsed time (in microseconds) corresponding to this operation, accumulated over the past executions |
| `LAST_STARTS` | `NUMBER` |  | Number of times this operation has been started, during the last execution |
| `LAST_OUTPUT_ROWS` | `NUMBER` |  | Number of rows produced by the row source, during the last execution |
| `LAST_CR_BUFFER_GETS` | `NUMBER` |  | Number of buffers retrieved in consistent mode, during the last execution. Buffers are usually retrieved in consistent mode for queries. |
| `LAST_CU_BUFFER_GETS` | `NUMBER` |  | Number of buffers retrieved in current mode, during the last execution. Buffers are retrieved in current mode for statements such as `INSERT`, `UPDATE`, and `DELETE`. |
| `LAST_DISK_READS` | `NUMBER` |  | Number of physical disk reads performed by the operation, during the last execution |
| `LAST_DISK_WRITES` | `NUMBER` |  | Number of physical disk writes performed by the operation, during the last execution |
| `LAST_ELAPSED_TIME` | `NUMBER` |  | Elapsed time (in microseconds) corresponding to this operation, during the last execution |
| `POLICY` | `VARCHAR2(10)` |  | Sizing policy for this work area:  - `MANUAL` - `AUTO` |
| `ESTIMATED_OPTIMAL_SIZE` | `NUMBER` |  | Estimated size (in KB) required by this work area to execute the operation completely in memory (optimal execution). This is either derived from optimizer statistics or from previous executions. |
| `ESTIMATED_ONEPASS_SIZE` | `NUMBER` |  | Estimated size (in KB) required by this work area to execute the operation in a single pass. This is either derived from optimizer statistics or from previous executions. |
| `LAST_MEMORY_USED` | `NUMBER` |  | Memory size (in KB) used by this work area during the last execution of the cursor |
| `LAST_EXECUTION` | `VARCHAR2(10)` |  | Indicates whether this work area ran using `OPTIMAL`, `ONE` `PASS`, or under `ONE` `PASS` memory requirement (`MULTI` - `PASS`), during the last execution of the cursor |
| `LAST_DEGREE` | `NUMBER` |  | Degree of parallelism used, during the last execution of the cursor |
| `TOTAL_EXECUTIONS` | `NUMBER` |  | Number of times this work area was active |
| `OPTIMAL_EXECUTIONS` | `NUMBER` |  | Number of times this work area ran in optimal mode |
| `ONEPASS_EXECUTIONS` | `NUMBER` |  | Number of times this work area ran in one pass mode |
| `MULTIPASSES_EXECUTIONS` | `NUMBER` |  | Number of times this work area ran below the one pass memory requirement |
| `ACTIVE_TIME` | `NUMBER` |  | Average time this work area is active (in hundredths of a second) |
| `MAX_TEMPSEG_SIZE` | `NUMBER` |  | Maximum temporary segment size (in bytes) created by an instantiation of this work area. This column is null if this work area has never spilled to disk. |
| `LAST_TEMPSEG_SIZE` | `NUMBER` |  | Temporary segment size (in bytes) created in the last instantiation of this work area. This column is null if the last instantiation of this work area did not spill to disk. |

See Also:

- " [DBA\_SQLSET\_PLANS](DBA_SQLSET_PLANS.md) "
- " [USER\_SQLSET\_PLANS](USER_SQLSET_PLANS.md) "