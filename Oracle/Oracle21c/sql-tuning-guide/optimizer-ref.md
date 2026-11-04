---
title: SQL Tuning Guide
book: SQL Tuning Guide
doc_id: F31828-11
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/tgsql/optimizer-ref.html
tags:
  - oracle
  - 21c
  - sql-tuning-guide
---

### 7.1 PLAN\_TABLE Columns

`PLAN_TABLE` is populated by the `EXPLAIN PLAN` statement.

The following table describes the columns in `PLAN_TABLE`.

Table 7-1 PLAN\_TABLE Columns

| Column | Type | Description |
| --- | --- | --- |
| `STATEMENT_ID` | `VARCHAR2(30)` | Value of the optional `STATEMENT_ID` parameter specified in the `EXPLAIN` `PLAN` statement. |
| `PLAN_ID` | `NUMBER` | Unique identifier of a plan in the database. |
| `TIMESTAMP` | `DATE ` | Date and time when the `EXPLAIN` `PLAN` statement was generated. |
| `REMARKS` | `VARCHAR2(80)` | Any comment (of up to 80 bytes) you want to associate with each step of the explained plan. This column indicates whether the database used an outline or SQL profile for the query.  If you need to add or change a remark on any row of the `PLAN_TABLE`, then use the `UPDATE` statement to modify the rows of the `PLAN_TABLE`. |
| `OPERATION` | `VARCHAR2(30)` | Name of the internal operation performed in this step. In the first row generated for a statement, the column contains one of the following values:  - `DELETE STATEMENT` - `INSERT STATEMENT` - `SELECT STATEMENT` - `UPDATE STATEMENT`  See " OPERATION and OPTION Columns of PLAN\_TABLE " for more information about values for this column. |
| `OPTIONS ` | `VARCHAR2(225) ` | A variation on the operation that the `OPERATION` column describes.  See " OPERATION and OPTION Columns of PLAN\_TABLE " for more information about values for this column. |
| `OBJECT_NODE ` | `VARCHAR2(128) ` | Name of the database link used to reference the object (a table name or view name). For local queries using parallel execution, this column describes the order in which the database consumes output from operations. |
| `OBJECT_OWNER ` | `VARCHAR2(30) ` | Name of the user who owns the schema containing the table or index. |
| `OBJECT_NAME ` | `VARCHAR2(30) ` | Name of the table or index. |
| `OBJECT_ALIAS` | `VARCHAR2(65) ` | Unique alias of a table or view in a SQL statement. For indexes, it is the object alias of the underlying table. |
| `OBJECT_INSTANCE ` | `NUMERIC ` | Number corresponding to the ordinal position of the object as it appears in the original statement. The numbering proceeds from left to right, outer to inner for the original statement text. View expansion results in unpredictable numbers. |
| `OBJECT_TYPE ` | `VARCHAR2(30) ` | Modifier that provides descriptive information about the object; for example, `NONUNIQUE` for indexes. |
| `OPTIMIZER ` | `VARCHAR2(255) ` | Current mode of the optimizer. |
| `SEARCH_COLUMNS ` | `NUMBERIC ` | Not currently used. |
| `ID ` | `NUMERIC ` | A number assigned to each step in the execution plan. |
| `PARENT_ID ` | `NUMERIC ` | The ID of the next execution step that operates on the output of the `ID` step. |
| `DEPTH` | `NUMERIC` | Depth of the operation in the row source tree that the plan represents. You can use this value to indent the rows in a plan table report. |
| `POSITION ` | `NUMERIC ` | For the first row of output, this indicates the estimated cost of executing the statement. For the other rows, it indicates the position relative to the other children of the same parent. |
| `COST ` | `NUMERIC ` | Cost of the operation as estimated by the optimizer. Cost is not determined for table access operations. The value of this column does not have any particular unit of measurement; it is a weighted value used to compare costs of execution plans. The value of this column is a function of the `CPU_COST` and `IO_COST` columns. |
| `CARDINALITY ` | `NUMERIC ` | Estimate by the query optimization approach of the number of rows that the operation accessed. |
| `BYTES ` | `NUMERIC ` | Estimate by the query optimization approach of the number of bytes that the operation accessed. |
| `OTHER_TAG ` | `VARCHAR2(255) ` | Describes the contents of the `OTHER` column. Values are:  - `SERIAL` (blank): Serial execution. Currently, SQL is not loaded in the `OTHER` column for this case. - `SERIAL_FROM_REMOTE` ` (S -> R)`: Serial execution at a remote site. - `PARALLEL_FROM_SERIAL (S -> P)`: Serial execution. Output of step is partitioned or broadcast to parallel execution servers. - `PARALLEL_TO_SERIAL (P -> S)`: Parallel execution. Output of step is returned to serial QC process. - `PARALLEL_TO_PARALLEL (P -> P)`: Parallel execution. Output of step is repartitioned to second set of parallel execution servers. - `PARALLEL_COMBINED_WITH_PARENT (PWP)`: Parallel execution; Output of step goes to next step in same parallel process. No interprocess communication to parent. - `PARALLEL_COMBINED_WITH_CHILD (PWC)`: Parallel execution. Input of step comes from prior step in same parallel process. No interprocess communication from child. |
| `PARTITION_START ` | `VARCHAR2(255) ` | Start partition of a range of accessed partitions. It can take one of the following values:  n indicates that the start partition has been identified by the SQL compiler, and its partition number is given by n.  `KEY` indicates that the start partition is identified at run time from partitioning key values.  `ROW LOCATION` indicates that the database computes the start partition (same as the stop partition) at run time from the location of each retrieved record. The record location is obtained by a user-specified ROWID or from a global index.  `INVALID` indicates that the range of accessed partitions is empty. |
| `PARTITION_STOP ` | `VARCHAR2(255) ` | Stop partition of a range of accessed partitions. It can take one of the following values:  n indicates that the stop partition has been identified by the SQL compiler, and its partition number is given by n.  `KEY` indicates that the stop partition is identified at run time from partitioning key values.  `ROW LOCATION` indicates that the database computes the stop partition (same as the start partition) at run time from the location of each retrieved record. The record location is obtained by a user or from a global index.  `INVALID` indicates that the range of accessed partitions is empty. |
| `PARTITION_ID ` | `NUMERIC ` | Step that has computed the pair of values of the `PARTITION_START` and `PARTITION_STOP` columns. |
| `OTHER ` | `LONG ` | Other information that is specific to the execution step that a user might find useful. See the `OTHER_TAG` column. |
| `DISTRIBUTION ` | `VARCHAR2(30) ` | Method used to distribute rows from producer query servers to consumer query servers.  See " DISTRIBUTION Column of PLAN\_TABLE " for more information about the possible values for this column. For more information about consumer and producer query servers, see [Oracle Database VLDB and Partitioning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/tgsql&id=GUID-1C6BC851-DE4A-4651-9813-3E70023C8264). |
| `CPU_COST ` | `NUMERIC ` | CPU cost of the operation as estimated by the optimizer. The value of this column is proportional to the number of machine cycles required for the operation. For statements that use the rule-based approach, this column is null. |
| `IO_COST ` | `NUMERIC ` | I/O cost of the operation as estimated by the optimizer. The value of this column is proportional to the number of data blocks read by the operation. For statements that use the rule-based approach, this column is null. |
| `TEMP_SPACE ` | `NUMERIC ` | Temporary space, in bytes, used by the operation as estimated by the optimizer. For statements that use the rule-based approach, or for operations that do not use any temporary space, this column is null. |
| `ACCESS_PREDICATES` | `VARCHAR2(4000)` | Predicates used to locate rows in an access structure. For example, start or stop predicates for an index range scan. |
| `FILTER_PREDICATES` | `VARCHAR2(4000)` | Predicates used to filter rows before producing them. |
| `PROJECTION` | `VARCHAR2(4000)` | Expressions produced by the operation. |
| `TIME` | `NUMBER(20,2)` | Elapsed time in seconds of the operation as estimated by query optimization. For statements that use the rule-based approach, this column is null. |
| `QBLOCK_NAME` | `VARCHAR2(30)` | Name of the query block, either system-generated or defined by the user with the `QB_NAME` hint. |

" OPERATION and OPTION Columns of PLAN\_TABLE " lists each combination of `OPERATION` and `OPTIONS` produced by the `EXPLAIN PLAN` statement and its meaning within an execution plan.

See Also:

[Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/tgsql&id=REFRN29510) for more information about `PLAN_TABLE`

### 7.2 OPERATION and OPTION Columns of PLAN\_TABLE

This table lists each combination of the `OPERATION` and `OPTIONS` columns of `PLAN_TABLE` and their meaning within an execution plan.

Table 7-2 OPERATION and OPTIONS Values Produced by EXPLAIN PLAN

| Operation | Option | Description |
| --- | --- | --- |
| `AND-EQUAL` |  | Operation accepting multiple sets of rowids, returning the intersection of the sets, eliminating duplicates. Used for the single-column indexes access path. |
| `BITMAP` | `CONVERSION ` | `TO ROWIDS` converts bitmap representations to actual rowids that you can use to access the table.  `FROM ROWIDS` converts the rowids to a bitmap representation.  `COUNT` returns the number of rowids if the actual values are not needed. |
| `BITMAP` | `INDEX ` | `SINGLE VALUE` looks up the bitmap for a single key value in the index.  `RANGE SCAN` retrieves bitmaps for a key value range.  `FULL SCAN` performs a full scan of a bitmap index if there is no start or stop key. |
| `BITMAP ` | `MERGE ` | Merges several bitmaps resulting from a range scan into one bitmap. |
| `BITMAP ` | `MINUS ` | Subtracts bits of one bitmap from another. Row source is used for negated predicates. This option is usable only if there are non-negated predicates yielding a bitmap from which the subtraction can take place. |
| `BITMAP ` | `OR ` | Computes the bitwise `OR` of two bitmaps. |
| `BITMAP ` | `AND ` | Computes the bitwise `AND` of two bitmaps. |
| `BITMAP ` | `KEY ITERATION ` | Takes each row from a table row source and finds the corresponding bitmap from a bitmap index. This set of bitmaps are then merged into one bitmap in a following `BITMAP` `MERGE` operation. |
| `CONNECT BY ` |  | Retrieves rows in hierarchical order for a query containing a `CONNECT BY` clause. |
| `CONCATENATION ` |  | Operation accepting multiple sets of rows returning the union-all of the sets. |
| `COUNT` |  | Operation counting the number of rows selected from a table. |
| `COUNT` | `STOPKEY` | Count operation where the number of rows returned is limited by the `ROWNUM` expression in the `WHERE` clause. |
| `CUBE JOIN` |  | Joins a table or view on the left and a cube on the right.  See [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/tgsql&id=SQLRF55589) to learn about the `NO_USE_CUBE` and `USE_CUBE` hints. |
| `CUBE JOIN` | `ANTI` | Uses an antijoin for a table or view on the left and a cube on the right. |
| `CUBE JOIN` | `ANTI SNA` | Uses an antijoin (single-sided null aware) for a table or view on the left and a cube on the right. The join column on the right (cube side) is `NOT NULL`. |
| `CUBE JOIN` | `OUTER` | Uses an outer join for a table or view on the left and a cube on the right. |
| `CUBE JOIN` | `RIGHT SEMI` | Uses a right semijoin for a table or view on the left and a cube on the right. |
| `CUBE SCAN` |  | Uses inner joins for all cube access. |
| `CUBE SCAN` | `PARTIAL OUTER` | Uses an outer join for at least one dimension, and inner joins for the other dimensions. |
| `CUBE SCAN` | `OUTER` | Uses outer joins for all cube access. |
| `DOMAIN INDEX ` |  | Retrieval of one or more rowids from a domain index. The options column contain information supplied by a user-defined domain index cost function, if any. |
| `FILTER ` |  | Operation accepting a set of rows, eliminates some of them, and returns the rest. |
| `FIRST ROW ` |  | Retrieval of only the first row selected by a query. |
| `FOR UPDATE ` |  | Operation retrieving and locking the rows selected by a query containing a `FOR` `UPDATE` clause. |
| `HASH` | `GROUP BY` | Operation hashing a set of rows into groups for a query with a `GROUP` `BY` clause. |
| `HASH` | `GROUP BY PIVOT` | Operation hashing a set of rows into groups for a query with a `GROUP` `BY` clause. The `PIVOT` option indicates a pivot-specific optimization for the `HASH GROUP BY` operator. |
| `HASH JOIN `  (These are join operations.) |  | Operation joining two sets of rows and returning the result. This join method is useful for joining large data sets of data (DSS, Batch). The join condition is an efficient way of accessing the second table.  Query optimizer uses the smaller of the two tables/data sources to build a hash table on the join key in memory. Then it scans the larger table, probing the hash table to find the joined rows. |
| `HASH JOIN ` | `ANTI ` | Hash (left) antijoin |
| `HASH JOIN ` | `SEMI ` | Hash (left) semijoin |
| `HASH JOIN ` | `RIGHT ANTI ` | Hash right antijoin |
| `HASH JOIN ` | `RIGHT SEMI ` | Hash right semijoin |
| `HASH JOIN ` | `OUTER ` | Hash (left) outer join |
| `HASH JOIN ` | `RIGHT OUTER ` | Hash right outer join |
| `INDEX `  (These are access methods.) | `UNIQUE SCAN ` | Retrieval of a single rowid from an index. |
| `INDEX` | `RANGE SCAN ` | Retrieval of one or more rowids from an index. Indexed values are scanned in ascending order. |
| `INDEX` | `RANGE SCAN DESCENDING ` | Retrieval of one or more rowids from an index. Indexed values are scanned in descending order. |
| `INDEX` | `FULL SCAN ` | Retrieval of all rowids from an index when there is no start or stop key. Indexed values are scanned in ascending order. |
| `INDEX` | `FULL SCAN DESCENDING ` | Retrieval of all rowids from an index when there is no start or stop key. Indexed values are scanned in descending order. |
| `INDEX ` | `FAST FULL SCAN ` | Retrieval of all rowids (and column values) using multiblock reads. No sorting order can be defined. Compares to a full table scan on only the indexed columns. Only available with the cost based optimizer. |
| `INDEX ` | `SKIP SCAN ` | Retrieval of rowids from a concatenated index without using the leading column(s) in the index. Only available with the cost based optimizer. |
| `INLIST ITERATOR ` |  | Iterates over the next operation in the plan for each value in the `IN` -list predicate. |
| `INTERSECTION ` |  | Operation accepting two sets of rows and returning the intersection of the sets, eliminating duplicates. |
| `MERGE JOIN `  (These are join operations.) |  | Operation accepting two sets of rows, each sorted by a value, combining each row from one set with the matching rows from the other, and returning the result. |
| `MERGE JOIN ` | `OUTER ` | Merge join operation to perform an outer join statement. |
| `MERGE JOIN ` | `ANTI ` | Merge antijoin. |
| `MERGE JOIN ` | `SEMI ` | Merge semijoin. |
| `MERGE JOIN ` | `CARTESIAN ` | Can result from 1 or more of the tables not having any join conditions to any other tables in the statement. Can occur even with a join and it may not be flagged as `CARTESIAN` in the plan. |
| `CONNECT BY ` |  | Retrieval of rows in hierarchical order for a query containing a `CONNECT` `BY` clause. |
| `MAT_VIEW REWRITE ACCESS `  (These are access methods.) | `FULL` | Retrieval of all rows from a materialized view. |
| `MAT_VIEW REWRITE ACCESS ` | `SAMPLE ` | Retrieval of sampled rows from a materialized view. |
| `MAT_VIEW REWRITE ACCESS ` | `CLUSTER ` | Retrieval of rows from a materialized view based on a value of an indexed cluster key. |
| `MAT_VIEW REWRITE ACCESS` | `HASH ` | Retrieval of rows from materialized view based on hash cluster key value. |
| `MAT_VIEW REWRITE ACCESS` | `BY ROWID RANGE ` | Retrieval of rows from a materialized view based on a rowid range. |
| `MAT_VIEW REWRITE ACCESS` | `SAMPLE BY ROWID RANGE ` | Retrieval of sampled rows from a materialized view based on a rowid range. |
| `MAT_VIEW REWRITE ACCESS` | `BY USER ROWID ` | If the materialized view rows are located using user-supplied rowids. |
| `MAT_VIEW REWRITE ACCESS ` | `BY INDEX ROWID ` | If the materialized view is nonpartitioned and rows are located using indexes. |
| `MAT_VIEW REWRITE ACCESS ` | `BY GLOBAL INDEX ROWID ` | If the materialized view is partitioned and rows are located using only global indexes. |
| `MAT_VIEW REWRITE ACCESS ` | `BY LOCAL INDEX ROWID ` | If the materialized view is partitioned and rows are located using one or more local indexes and possibly some global indexes.  Partition Boundaries:  The partition boundaries might have been computed by:  A previous `PARTITION` step, in which case the `PARTITION_START` and `PARTITION_STOP` column values replicate the values present in the `PARTITION` step, and the `PARTITION_ID` contains the ID of the `PARTITION` step. Possible values for `PARTITION_START` and `PARTITION_STOP` are `NUMBER` (n), `KEY`, and `INVALID`.  The `MAT_VIEW REWRITE ACCESS` or `INDEX` step itself, in which case the `PARTITION_ID` contains the `ID` of the step. Possible values for `PARTITION_START` and `PARTITION_STOP` are `NUMBER` (n), `KEY`, `ROW` `REMOVE_LOCATION` (`MAT_VIEW REWRITE` `ACCESS` only), and `INVALID`. |
| `MINUS` |  | Operation accepting two sets of rows and returning rows appearing in the first set but not in the second, eliminating duplicates. |
| `NESTED LOOPS`  (These are join operations.) |  | Operation accepting two sets of rows, an outer set and an inner set. Oracle Database compares each row of the outer set with each row of the inner set, returning rows that satisfy a condition. This join method is useful for joining small subsets of data (OLTP). The join condition is an efficient way of accessing the second table. |
| `NESTED LOOPS ` | `OUTER` | Nested loops operation to perform an outer join statement. |
| `PARTITION` |  | Iterates over the next operation in the plan for each partition in the range given by the `PARTITION_START` and `PARTITION_STOP` columns. `PARTITION` describes partition boundaries applicable to a single partitioned object (table or index) or to a set of equipartitioned objects (a partitioned table and its local indexes). The partition boundaries are provided by the values of `PARTITION_START` and `PARTITION_STOP` of the `PARTITION`. Refer to [Table 6-2](generating-and-displaying-execution-plans.md) for valid values of partition start and stop. |
| `PARTITION` | `SINGLE` | Access one partition. |
| `PARTITION` | `ITERATOR` | Access many partitions (a subset). |
| `PARTITION` | `ALL` | Access all partitions. |
| `PARTITION` | `INLIST` | Similar to iterator, but based on an `IN` -list predicate. |
| `PARTITION` | `INVALID` | Indicates that the partition set to be accessed is empty. |
| `POLYMORPHIC TABLE FUNCTION` |  | Indicates the row source for a polymorphic table function, which is a table function whose return type is determined by its arguments. |
| `PX` `ITERATOR` | `BLOCK`, `CHUNK` | Implements the division of an object into block or chunk ranges among a set of parallel execution servers. |
| `PX` `COORDINATOR` |  | Implements the Query Coordinator which controls, schedules, and executes the parallel plan below it using parallel execution servers. It also represents a serialization point, as the end of the part of the plan executed in parallel and always has a `PX SEND QC` operation below it. |
| `PX` `PARTITION` |  | Same semantics as the regular `PARTITION` operation except that it appears in a parallel plan. |
| `PX` `RECEIVE` |  | Shows the consumer/receiver parallel execution node reading repartitioned data from a send/producer (QC or parallel execution server) executing on a PX SEND node. This information was formerly displayed into the `DISTRIBUTION` column. See Table 7-1. |
| `PX` `SEND` | `QC` `(RANDOM), HASH`, `RANGE` | Implements the distribution method taking place between two sets of parallel execution servers. Shows the boundary between two sets and how data is repartitioned on the send/producer side (QC or side. This information was formerly displayed into the `DISTRIBUTION` column. See Table 7-1. |
| `REMOTE` |  | Retrieval of data from a remote database. |
| `SEQUENCE` |  | Operation involving accessing values of a sequence. |
| `SORT` | `AGGREGATE` | Retrieval of a single row after applying a group function to a set of selected rows. In this case, the database “sorts” a single row. |
| `SORT` | `UNIQUE` | Operation sorting a set of rows to eliminate duplicates. |
| `SORT` | `GROUP` `BY` | Operation sorting a set of rows into groups for a query with a `GROUP` `BY` clause. |
| `SORT` | `GROUP BY PIVOT` | Operation sorting a set of rows into groups for a query with a `GROUP` `BY` clause. The `PIVOT` option indicates a pivot-specific optimization for the `SORT GROUP BY` operator. |
| `SORT ` | `JOIN ` | Operation sorting a set of rows before a merge-join. |
| `SORT ` | `ORDER BY ` | Operation sorting a set of rows for a query with an `ORDER` `BY` clause. |
| `TABLE ACCESS `  (These are access methods.) | `FULL ` | Retrieval of all rows from a table.  `INMEMORY FULL` indicates a scan of the In-Memory column store (IM column store). The absence of `INMEMORY` indicates a scan of the row store.  `INMEMORY FULL (HYBRID)` indicates a hybrid In-Memory scan. In this case, the query is divided into two parts, with one part scanning the IM column store to perform filters, and the other part scanning the row store to project the filtered query results. |
| `TABLE ACCESS ` | `SAMPLE ` | Retrieval of sampled rows from a table. |
| `TABLE ACCESS ` | `CLUSTER ` | Retrieval of rows from a table based on a value of an indexed cluster key. |
| `TABLE ACCESS ` | `HASH ` | Retrieval of rows from table based on hash cluster key value. |
| `TABLE ACCESS ` | `BY ROWID RANGE ` | Retrieval of rows from a table based on a rowid range. |
| `TABLE ACCESS ` | `SAMPLE BY ROWID RANGE ` | Retrieval of sampled rows from a table based on a rowid range. |
| `TABLE ACCESS` | `BY USER ROWID ` | If the table rows are located using user-supplied rowids. |
| `TABLE ACCESS ` | `BY INDEX ROWID ` | If the table is nonpartitioned and rows are located using index(es). |
| `TABLE ACCESS ` | `BY GLOBAL INDEX ROWID ` | If the table is partitioned and rows are located using only global indexes. |
| `TABLE ACCESS ` | `BY LOCAL INDEX ROWID ` | If the table is partitioned and rows are located using one or more local indexes and possibly some global indexes.  Partition Boundaries:  The partition boundaries might have been computed by:  A previous `PARTITION` step, in which case the `PARTITION_START` and `PARTITION_STOP` column values replicate the values present in the `PARTITION` step, and the `PARTITION_ID` contains the ID of the `PARTITION` step. Possible values for `PARTITION_START` and `PARTITION_STOP` are `NUMBER` (n), `KEY`, and `INVALID`.  The `TABLE` `ACCESS` or `INDEX` step itself, in which case the `PARTITION_ID` contains the `ID` of the step. Possible values for `PARTITION_START` and `PARTITION_STOP` are `NUMBER` (n), `KEY`, `ROW` `REMOVE_LOCATION` (`TABLE` `ACCESS` only), and `INVALID`. |
| `TRANSPOSE` |  | Operation evaluating a `PIVOT` operation by transposing the results of `GROUP BY` to produce the final pivoted data. |
| `UNION ` |  | Operation accepting two sets of rows and returns the union of the sets, eliminating duplicates. |
| `UNPIVOT ` |  | Operation that rotates data from columns into rows. |
| `VIEW ` |  | Operation performing a view's query and then returning the resulting rows to another operation. |

### 7.3 DISTRIBUTION Column of PLAN\_TABLE

The `DISTRIBUTION` column indicates the method used to distribute rows from producer query servers to consumer query servers.

Table 7-3 Values of DISTRIBUTION Column of the PLAN\_TABLE

| DISTRIBUTION Text | Description |
| --- | --- |
| `PARTITION (ROWID)` | Maps rows to query servers based on the partitioning of a table or index using the rowid of the row to `UPDATE` / `DELETE`. |
| `PARTITION (KEY)` | Maps rows to query servers based on the partitioning of a table or index using a set of columns. Used for partial partition-wise join, `PARALLEL INSERT`, `CREATE TABLE AS SELECT` of a partitioned table, and `CREATE PARTITIONED GLOBAL INDEX`. |
| `HASH` | Maps rows to query servers using a hash function on the join key. Used for `PARALLEL JOIN` or `PARALLEL GROUP BY`. |
| `RANGE` | Maps rows to query servers using ranges of the sort key. Used when the statement contains an `ORDER BY` clause. |
| `ROUND-ROBIN` | Randomly maps rows to query servers. |
| `BROADCAST` | Broadcasts the rows of the entire table to each query server. Used for a parallel join when one table is very small compared to the other. |
| `QC (ORDER)` | The QC consumes the input in order, from the first to the last query server. Used when the statement contains an `ORDER BY` clause. |
| `QC (RANDOM)` | The QC consumes the input randomly. Used when the statement does not have an `ORDER BY` clause. |