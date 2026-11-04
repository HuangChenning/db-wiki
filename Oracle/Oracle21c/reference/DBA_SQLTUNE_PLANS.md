---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_SQLTUNE_PLANS.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.381 DBA\_SQLTUNE\_PLANS

`DBA_SQLTUNE_PLANS` displays information about the execution plans generated for all SQL statements in the database during a SQL tuning session.

Related View

`USER_SQLTUNE_PLANS` displays information about the execution plans generated for the SQL statements owned by the current user during a SQL tuning session.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `TASK_ID` | `NUMBER(38)` | `NOT NULL` | Advisor task ID |
| `EXECUTION_NAME` | `VARCHAR2(128)` | `NOT NULL` | Advisor task execution |
| `OBJECT_ID` | `NUMBER(38)` | `NOT NULL` | Advisor object ID |
| `ATTRIBUTE` | `VARCHAR2(34)` |  | Text string identifying the type of the execution plan:  - `Original` - Original plan of the query - `Original with adjusted cost` - Same as `Original` but with adjusted cost - `Using SQL profile` - Plan with SQL profile applied - `Using new indices` - Plan with indexes applied |
| `STATEMENT_ID` | `VARCHAR2(30)` |  | Optional statement identifier specified in the `EXPLAIN PLAN` statement |
| `PLAN_HASH_VALUE` | `NUMBER` | `NOT NULL` | Numerical representation of the execution plan |
| `PLAN_ID` | `NUMBER` |  | Plan identifier |
| `TIMESTAMP` | `DATE` |  | Date and time when the `EXPLAIN PLAN` statement was issued |
| `REMARKS` | `VARCHAR2(4000)` |  | Place for comments that can be added to the steps of the execution plan |
| `OPERATION` | `VARCHAR2(30)` |  | Name of the operation performed at this step |
| `OPTIONS` | `VARCHAR2(255)` |  | Options used for the operation performed at this step |
| `OBJECT_NODE` | `VARCHAR2(128)` |  | Name of the database link used to reference the object |
| `OBJECT_OWNER` | `VARCHAR2(128)` |  | Owner of the object |
| `OBJECT_NAME` | `VARCHAR2(128)` |  | Name of the object |
| `OBJECT_ALIAS` | `VARCHAR2(261)` |  | Object alias |
| `OBJECT_INSTANCE` | `NUMBER(38)` |  | Numbered position of the object name in the original SQL statement |
| `OBJECT_TYPE` | `VARCHAR2(30)` |  | Descriptive modifier that further describes the type of object |
| `OPTIMIZER` | `VARCHAR2(255)` |  | Current mode of the optimizer |
| `SEARCH_COLUMNS` | `NUMBER` |  | Number of index columns with start and stop keys (that is, the number of columns with matching predicates) |
| `ID` | `NUMBER(38)` | `NOT NULL` | Identification number for this step in the execution plan |
| `PARENT_ID` | `NUMBER(38)` |  | ID of the next step that operates on the results of this step |
| `DEPTH` | `NUMBER(38)` |  | Depth |
| `POSITION` | `NUMBER(38)` |  | Order of processing for steps with the same parent ID |
| `COST` | `NUMBER(38)` |  | Cost of the current operation estimated by the cost-based optimizer (CBO) |
| `CARDINALITY` | `NUMBER(38)` |  | Number of rows returned by the current operation (estimated by the CBO) |
| `BYTES` | `NUMBER(38)` |  | Number of bytes returned by the current operation |
| `OTHER_TAG` | `VARCHAR2(255)` |  | Describes the function of the SQL text in the `OTHER` column. Values for `OTHER_TAG` are:  - `SERIAL` - SQL is the text of a locally-executed, serial query plan. Currently, SQL is not loaded in `OTHER` for this case. - `SERIAL_FROM_REMOTE` - SQL text shown in the `OTHER` column will be executed at a remote site - `PARALLEL_COMBINED_WITH_PARENT` - Parent of this operation is a DFO that performs both operations in the parallel execution plan - `PARALLEL_COMBINED_WITH_CHILD` - Child of this operation is a DFO that performs both operations in the parallel execution plan. - `PARALLEL_TO_SERIAL` - SQL text shown in the `OTHER` column is the top-level of the parallel plan. - `PARALLEL_TO_PARALLEL` - SQL text shown in the `OTHER` column is executed and output in parallel - `PARALLEL_FROM_SERIAL` - Operation consumes data from a serial operation and outputs it in parallel |
| `PARTITION_START` | `VARCHAR2(255)` |  | Start partition of a range of accessed partitions |
| `PARTITION_STOP` | `VARCHAR2(255)` |  | Stop partition of a range of accessed partitions |
| `PARTITION_ID` | `NUMBER(38)` |  | Step that has computed the pair of values of the `PARTITION_START` and `PARTITION_STOP` columns |
| `OTHER` | `LONG` |  | Information about parallel execution servers and parallel queries |
| `DISTRIBUTION` | `VARCHAR2(30)` |  | Distribution method |
| `CPU_COST` | `NUMBER(38)` |  | User-defined CPU cost |
| `IO_COST` | `NUMBER(38)` |  | User-defined I/O cost |
| `TEMP_SPACE` | `NUMBER(38)` |  | Temporary space usage of the operation (sort or hash-join) as estimated by the CBO |
| `ACCESS_PREDICATES` | `VARCHAR2(4000)` |  | Predicates used to locate rows in an access structure. For example, start or stop predicates for an index range scan. |
| `FILTER_PREDICATES` | `VARCHAR2(4000)` |  | Predicates used to filter rows before producing them |
| `PROJECTION` | `VARCHAR2(4000)` |  | Expressions produced by the operation |
| `TIME` | `NUMBER(38)` |  | Elapsed time (in seconds) of the operation as estimated by the CBO |
| `QBLOCK_NAME` | `VARCHAR2(128)` |  | Name of the query block |
| `OTHER_XML` | `CLOB` |  | Provides extra information specific to an execution step of the execution plan. The content of this column is structured using XML because it allows multiple pieces of information to be stored, including the following:  - Name of the schema against which the query was parsed - Release number of the Oracle Database that produced the explain plan - Hash value associated with the execution plan - Name (if any) of the outline or the SQL profile used to build the execution plan - Indication of whether or not dynamic statistics were used to produce the plan - The outline data, a set of optimizer hints that can be used to regenerate the same plan |

See Also:

" [USER\_SQLTUNE\_PLANS](USER_SQLTUNE_PLANS.md) "