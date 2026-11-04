---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_HIST_SQL_PLAN.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.60 DBA\_HIST\_SQL\_PLAN

`DBA_HIST_SQL_PLAN` displays the execution plan information for each child cursor in the workload repository.

This view captures information from `V$SQL_PLAN` and is used with the `DBA_HIST_SQLSTAT` view.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID |
| `SQL_ID` | `VARCHAR2(13)` | `NOT NULL` | SQL identifier of the parent cursor in the library cache |
| `PLAN_HASH_VALUE` | `NUMBER` | `NOT NULL` | Numerical representation of the SQL plan for the cursor. Comparing one `PLAN_HASH_VALUE` to another easily identifies whether or not two plans are the same (rather than comparing the two plans line by line). |
| `ID` | `NUMBER` | `NOT NULL` | A number assigned to each step in the execution plan |
| `OPERATION` | `VARCHAR2(30)` |  | Name of the internal operation performed in this step (for example, `TABLE ACCESS`) |
| `OPTIONS` | `VARCHAR2(30)` |  | A variation on the operation described in the `OPERATION` column (for example, `FULL`) |
| `OBJECT_NODE` | `VARCHAR2(128)` |  | Name of the database link used to reference the object (a table name or view name). For local queries that use parallel execution, this column describes the order in which output from operations is consumed. |
| `OBJECT#` | `NUMBER` |  | Object number of the table or the index |
| `OBJECT_OWNER` | `VARCHAR2(128)` |  | Name of the user who owns the schema containing the table or index |
| `OBJECT_NAME` | `VARCHAR2(128)` |  | Name of the table or index |
| `OBJECT_ALIAS` | `VARCHAR2(261)` |  | Alias for the object |
| `OBJECT_TYPE` | `VARCHAR2(20)` |  | Type of the object |
| `OPTIMIZER` | `VARCHAR2(20)` |  | Current mode of the optimizer for the first row in the plan (statement line), for example, `ALL_ROWS`. When the operation is a database access (for example, `TABLE ACCESS`), this column indicates whether or not the object is analyzed. |
| `PARENT_ID` | `NUMBER` |  | ID of the next execution step that operates on the output of the current step |
| `DEPTH` | `NUMBER` |  | Depth (or level) of the operation in the tree. It is not necessary to issue a `CONNECT BY` statement to get the level information, which is generally used to indent the rows from the `PLAN_TABLE` table. The root operation (statement) is level 0. |
| `POSITION` | `NUMBER` |  | Order of processing for all operations that have the same `PARENT_ID` |
| `SEARCH_COLUMNS` | `NUMBER` |  | Number of index columns with start and stop keys (that is, the number of columns with matching predicates) |
| `COST` | `NUMBER` |  | Cost of the operation as estimated by the optimizer's cost-based approach. For statements that use the rule-based approach, this column is null. |
| `CARDINALITY` | `NUMBER` |  | Estimate, by the cost-based optimizer, of the number of rows produced by the operation |
| `BYTES` | `NUMBER` |  | Estimate, by the cost-based optimizer, of the number of bytes produced by the operation |
| `OTHER_TAG` | `VARCHAR2(35)` |  | Describes the contents of the `OTHER` column. See `EXPLAIN PLAN` for values. |
| `PARTITION_START` | `VARCHAR2(64)` |  | Start partition of a range of accessed partitions |
| `PARTITION_STOP` | `VARCHAR2(64)` |  | Stop partition of a range of accessed partitions |
| `PARTITION_ID` | `NUMBER` |  | Step that computes the pair of values of the `PARTITION_START` and `PARTITION_STOP` columns |
| `OTHER` | `VARCHAR2(4000)` |  | Other information specific to the execution step that users may find useful. See `EXPLAIN PLAN` for values. |
| `DISTRIBUTION` | `VARCHAR2(20)` |  | Stores the method used to distribute rows from producer query servers to consumer query servers |
| `CPU_COST` | `NUMBER` |  | CPU cost of the operation as estimated by the optimizer's cost-based approach. For statements that use the rule-based approach, this column is null. |
| `IO_COST` | `NUMBER` |  | I/O cost of the operation as estimated by the optimizer's cost-based approach. For statements that use the rule-based approach, this column is null. |
| `TEMP_SPACE` | `NUMBER` |  | Temporary space usage of the operation (sort or hash-join) as estimated by the optimizer's cost-based approach. For statements that use the rule-based approach, this column is null. |
| `ACCESS_PREDICATES` | `VARCHAR2(4000)` |  | Predicates used to locate rows in an access structure. For example, start or stop predicates for an index range scan. |
| `FILTER_PREDICATES` | `VARCHAR2(4000)` |  | Predicates used to filter rows before producing them |
| `PROJECTION` | `VARCHAR2(4000)` |  | Expressions produced by the operation |
| `TIME` | `NUMBER` |  | Elapsed time (in seconds) of the operation as estimated by the optimizer's cost-based approach. For statements that use the rule-based approach, this column is null. |
| `QBLOCK_NAME` | `VARCHAR2(128)` |  | Name of the query block |
| `REMARKS` | `VARCHAR2(4000)` |  | Remarks |
| `TIMESTAMP` | `DATE` |  | Timestamp for when the plan was produced |
| `OTHER_XML` | `CLOB` |  | Provides extra information specific to an execution step of the execution plan. The content of this column is structured using XML because it allows multiple pieces of information to be stored, including the following:  - Name of the schema against which the query was parsed - Release number of the Oracle Database that produced the explain plan - Hash value associated with the execution plan - Name (if any) of the outline or the SQL profile used to build the execution plan - Indication of whether or not dynamic statistics were used to produce the plan - The outline data, a set of optimizer hints that can be used to regenerate the same plan |
| `CON_DBID` | `NUMBER` |  | The database ID of the PDB for the sampled session |
| `CON_ID` | `NUMBER` |  | The ID of the container that `CON_DBID` identifies. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

- " [V$SQL\_PLAN](V-SQL_PLAN.md) "
- " [DBA\_HIST\_SQLSTAT](DBA_HIST_SQLSTAT.md) "