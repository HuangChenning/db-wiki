---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/PLAN_TABLE.html
tags:
  - oracle
  - 21c
  - reference
---

## 7.218 PLAN\_TABLE

`PLAN_TABLE` is automatically created as a global temporary table to hold the output of an `EXPLAIN PLAN` statement for all users.

`PLAN_TABLE` is the default sample output table into which the `EXPLAIN PLAN` statement inserts rows describing execution plans.

While a `PLAN_TABLE` table is automatically set up for each user, you can use the SQL script `utlxplan.sql` to manually create a local `PLAN_TABLE` in your schema.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `STATEMENT_ID` | `VARCHAR2(30)` |  | Value of the optional `STATEMENT_ID` parameter specified in the `EXPLAIN PLAN` statement |
| `PLAN_ID` | `NUMBER` |  | Unique identifier of a plan in the database |
| `TIMESTAMP` | `DATE` |  | Date and time when the `EXPLAIN PLAN` statement was generated |
| `REMARKS` | `VARCHAR2(4000)` |  | Any comment (of up to 4000 bytes) you want to associate with each step of the explained plan. This column is used to indicate whether an outline or SQL Profile was used for the query.  If you need to add or change a remark on any row of the `PLAN_TABLE`, then use the `UPDATE` statement to modify the rows of the `PLAN_TABLE`. |
| `OPERATION` | `VARCHAR2(30)` |  | Name of the internal operation performed in this step. In the first row generated for a statement, the column contains one of the following values:  - `DELETE STATEMENT` - `INSERT STATEMENT` - `SELECT STATEMENT` - `UPDATE STATEMENT` |
| `OPTIONS` | `VARCHAR2(255)` |  | A variation on the operation described in the `OPERATION` column |
| `OBJECT_NODE` | `VARCHAR2(128)` |  | Name of the database link used to reference the object (a table name or view name). For local queries using parallel execution, this column describes the order in which output from operations is consumed. |
| `OBJECT_OWNER` | `VARCHAR2(128)` |  | Owner of the table or index |
| `OBJECT_NAME` | `VARCHAR2(128)` |  | Name of the table or index |
| `OBJECT_ALIAS` | `VARCHAR2(261)` |  | Unique alias of a table or view in a SQL statement. For indexes, it is the object alias of the underlying table. |
| `OBJECT_INSTANCE` | `NUMBER(38)` |  | Number corresponding to the ordinal position of the object as it appears in the original statement. The numbering proceeds from left to right, outer to inner with respect to the original statement text. View expansion results in unpredictable numbers. |
| `OBJECT_TYPE` | `VARCHAR2(30)` |  | Modifier that provides descriptive information about the object; for example, `NON-UNIQUE` for indexes |
| `OPTIMIZER` | `VARCHAR2(255)` |  | Current mode of the optimizer |
| `SEARCH_COLUMNS` | `NUMBER` |  | Not currently used |
| `ID` | `NUMBER(38)` |  | A number assigned to each step in the execution plan |
| `PARENT_ID` | `NUMBER(38)` |  | ID of the next execution step that operates on the output of the `ID` step |
| `DEPTH` | `NUMBER(38)` |  | Depth of the operation in the row source tree that the plan represents. The value can be used for indenting the rows in a plan table report. |
| `POSITION` | `NUMBER(38)` |  | For the first row of output, this indicates the optimizer's estimated cost of executing the statement. For the other rows, it indicates the position relative to the other children of the same parent. |
| `COST` | `NUMBER(38)` |  | Cost of the operation as estimated by the optimizer's query approach. Cost is not determined for table access operations. The value of this column does not have any particular unit of measurement; it is merely a weighted value used to compare costs of execution plans. The value of this column is a function of the `CPU_COST` and `IO_COST` columns. |
| `CARDINALITY` | `NUMBER(38)` |  | Estimate by the query optimization approach of the number of rows accessed by the operation |
| `BYTES` | `NUMBER(38)` |  | Estimate by the query optimization approach of the number of bytes accessed by the operation |
| `OTHER_TAG` | `VARCHAR2(255)` |  | Describes the contents of the `OTHER` column:  - `SERIAL` - Serial execution. Currently, SQL is not loaded in the `OTHER` column for this case. - `SERIAL_FROM_REMOTE` - Serial execution at a remote site. - `PARALLEL_FROM_SERIAL` - Serial execution. Output of step is partitioned or broadcast to parallel execution servers. - `PARALLEL_TO_SERIAL` - Parallel execution. Output of step is returned to serial query coordinator (QC) process. - `PARALLEL_TO_PARALLEL` - Parallel execution. Output of step is repartitioned to second set of parallel execution servers. - `PARALLEL_COMBINED_WITH_PARENT` - Parallel execution; Output of step goes to next step in same parallel process. No interprocess communication to parent. - `PARALLEL_COMBINED_WITH_CHILD` - Parallel execution. Input of step comes from prior step in same parallel process. No interprocess communication from child. |
| `PARTITION_START` | `VARCHAR2(255)` |  | Start partition of a range of accessed partitions:  - `number` - Start partition has been identified by the SQL compiler, and its partition number is given by `number` - `KEY` - Start partition will be identified at run time from partitioning key values - `ROW` `LOCATION` - Start partition (same as the stop partition) will be computed at run time from the location of each record being retrieved. The record location is obtained from a user-specified `ROWID` or from a global index. - `INVALID` - Range of accessed partitions is empty |
| `PARTITION_STOP` | `VARCHAR2(255)` |  | Stop partition of a range of accessed partitions:  - `number` - Stop partition has been identified by the SQL compiler, and its partition number is given by `number` - `KEY` - Stop partition will be identified at run time from partitioning key values - `ROW` `LOCATION` - Stop partition (same as the start partition) will be computed at run time from the location of each record being retrieved. The record location is obtained from a user-specified `ROWID` or from a global index. - `INVALID` - Range of accessed partitions is empty |
| `PARTITION_ID` | `NUMBER(38)` |  | Step that has computed the pair of values of the `PARTITION_START` and `PARTITION_STOP` columns |
| `OTHER` | `LONG` |  | Other information that is specific to the execution step that a user might find useful (see the `OTHER_TAG` column) |
| `OTHER_XML` | `CLOB` |  | Provides extra information specific to an execution step of the execution plan. The content of this column is structured using XML since multiple pieces of information can be stored there. This includes:  - Name of the schema against which the query was parsed - Release number of the Oracle Database that produced the explain plan - Hash value associated with the execution plan - Name (if any) of the outline or the SQL profile used to build the execution plan - Indication of whether or not dynamic statistics were used to produce the plan - The outline data, a set of optimizer hints that can be used to regenerate the same plan |
| `DISTRIBUTION` | `VARCHAR2(30)` |  | Method used to distribute rows from producer query servers to consumer query servers |
| `CPU_COST` | `NUMBER(38)` |  | CPU cost of the operation as estimated by the query optimizer's approach. The value of this column is proportional to the number of machine cycles required for the operation. For statements that use the rule-based approach, this column is NULL. |
| `IO_COST` | `NUMBER(38)` |  | I/O cost of the operation as estimated by the query optimizer's approach. The value of this column is proportional to the number of data blocks read by the operation. For statements that use the rule-based approach, this column is NULL. |
| `TEMP_SPACE` | `NUMBER(38)` |  | Temporary space (in bytes) used by the operation as estimated by the query optimizer's approach. For statements that use the rule-based approach, or for operations that do not use any temporary space, this column is NULL. |
| `ACCESS_PREDICATES` | `VARCHAR2(4000)` |  | Predicates used to locate rows in an access structure. For example, start or stop predicates for an index range scan. |
| `FILTER_PREDICATES` | `VARCHAR2(4000)` |  | Predicates used to filter rows before producing them |
| `PROJECTION` | `VARCHAR2(4000)` |  | Expressions produced by the operation |
| `TIME` | `NUMBER(38)` |  | Elapsed time (in seconds) of the operation as estimated by query optimization. For statements that use the rule-based approach, this column is NULL. |
| `QBLOCK_NAME` | `VARCHAR2(128)` |  | Name of the query block (either system-generated or defined by the user with the `QB_NAME` hint) |