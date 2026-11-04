---
title: Using Indexes and Clusters
book: Performance Tuning Guide
doc_id: E41573-04
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e41573/data_acc.htm
tags:
  - oracle
  - 11g
  - performance-tuning-guide
---

## 14 Using Indexes and Clusters

This chapter provides an overview of data access methods using indexes and clusters that can enhance or degrade performance.

The chapter contains the following sections:

## 14.1 Understanding Index Performance

This section describes the following:

- Tuning the Logical Structure
- Index Tuning using the SQLAccess Advisor
- Choosing Columns and Expressions to Index
- Choosing Composite Indexes
- Writing Statements That Use Indexes
- Writing Statements That Avoid Using Indexes
- Re-creating Indexes
- Using Nonunique Indexes to Enforce Uniqueness
- Using Enabled Novalidated Constraints

### 14.1.1 Tuning the Logical Structure

Although query optimization helps avoid the use of nonselective indexes within query execution, the SQL engine must continue to maintain all indexes defined against a table, regardless of whether queries make use of them. Index maintenance can present a significant CPU and I/O resource demand in any write-intensive application. In other words, do not build indexes unless necessary.

To maintain optimal performance, drop indexes that an application is not using. You can find indexes that are not being used by using the `ALTER` `INDEX` `MONITORING` `USAGE` functionality over a period that is representative of your workload. This monitoring feature records whether an index has been used. If you find that an index has not been used, then drop it. Make sure you are monitoring a representative workload to avoid dropping an index which is used, but not by the workload you sampled.

Also, indexes within an application sometimes have uses that are not immediately apparent from a survey of statement execution plans. An example of this is a foreign key index on a parent table, which prevents share locks from being taken out on a child table.

If you are deciding whether to create new indexes to tune statements, then you can also use the `EXPLAIN` `PLAN` statement to determine whether the optimizer chooses to use these indexes when the application is run. If you create new indexes to tune a statement that is currently parsed, then Oracle Database invalidates the statement.

When the statement is next parsed, the optimizer automatically chooses a new execution plan that could potentially use the new index. If you create new indexes on a remote database to tune a distributed statement, then the optimizer considers these indexes when the statement is next parsed.

Note that creating an index to tune one statement can affect the optimizer's choice of execution plans for other statements. For example, if you create an index to be used by one statement, then the optimizer can choose to use that index for other statements in the application as well. For this reason, reexamine the application's performance and execution plans, and rerun the SQL trace facility after you have tuned those statements that you initially identified for tuning.

See Also:

- [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/toc.htm) for syntax and semantics of the `ALTER` `INDEX` `MONITORING` `USAGE` statement
- [Oracle Database Advanced Application Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e41502/toc.htm) to learn about foreign keys

### 14.1.2 Index Tuning using the SQLAccess Advisor

SQL Access Advisor is an alternative to manually determining which indexes are required. This advisor recommends a set of indexes when invoked from Oracle Enterprise Manager or run through the `DBMS_ADVISOR` package APIs. SQL Access Advisor either recommends using a workload or it generates a hypothetical workload for a specified schema.

Various workload sources are available, such as the current contents of the SQL cache, a user-defined set of SQL statements, or a SQL tuning set. Given a workload, SQL Access Advisor generates a set of recommendations from which you can select the indexes to be implemented. An implementation script is provided that can be executed manually or automatically through Oracle Enterprise Manager.

See Also:

["Overview of SQL Access Advisor"](advisor.md)

### 14.1.3 Choosing Columns and Expressions to Index

A key is a column or expression on which you can build an index. Follow these guidelines for choosing keys to index:

- Consider indexing keys that appear frequently in `WHERE` clauses.
- Consider indexing keys that frequently join tables in SQL statements. For more information on optimizing joins, see the "Using Hash Clusters for Performance".
- Choose index keys that have high selectivity. The selectivity of an index is the percentage of rows in a table having the same value for the indexed key. An index's selectivity is optimal if few rows have the same value.
	Note:
	Oracle Database automatically creates indexes, or uses existing indexes, on the keys and expressions of unique and primary keys that you define with integrity constraints.
	Indexing low selectivity columns can be helpful when the data distribution is skewed so that one or two values occur much less often than other values.
- Do not use standard B-tree indexes on keys or expressions with few distinct values. Such keys or expressions usually have poor selectivity and therefore do not optimize performance unless the frequently selected key values appear less frequently than the other key values. You can use bitmap indexes effectively in such cases, unless the index is modified frequently, as in a high concurrency OLTP application.
- Do not index frequently modified columns. `UPDATE` statements that modify indexed columns and `INSERT` and `DELETE` statements that modify indexed tables take longer than if there were no index. Such SQL statements must modify data in indexes and data in tables. They also create additional undo and redo.
- Do not index keys that appear only in `WHERE` clauses with functions or operators. A `WHERE` clause that uses a function, other than `MIN` or `MAX`, or an operator with an indexed key does not make available the access path that uses the index except with function-based indexes.
- Consider indexing foreign keys of referential integrity constraints in cases in which a large number of concurrent `INSERT`, `UPDATE`, and `DELETE` statements access the parent and child tables. Such an index allows `UPDATE` s and `DELETE` s on the parent table without share locking the child table.
- When choosing to index a key, consider whether the performance gain for queries is worth the performance loss for `INSERT` s, `UPDATE` s, and `DELETE` s and the use of the space required to store the index. You might want to experiment by comparing the processing times of the SQL statements with and without indexes. You can measure processing time with the SQL trace facility.
	See Also:
	[Oracle Database Advanced Application Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e41502/toc.htm) for more information on the effects of foreign keys on locking

### 14.1.4 Choosing Composite Indexes

A composite index contains multiple key columns. Composite indexes can provide additional advantages over single-column indexes:

- Improved selectivity
	Sometimes you can combine two or more columns or expressions, each with poor selectivity, to form a composite index with higher selectivity.
- Reduced I/O
	If all columns selected by a query are in a composite index, then Oracle Database can return these values from the index without accessing the table.

A SQL statement can use an access path involving a composite index when the statement contains constructs that use a leading portion of the index.

Note:

This is no longer the case with index skip scans. See ["Index Skip Scans"](optimops.md).

A leading portion of an index is a set of one or more columns that were specified first and consecutively in the list of columns in the `CREATE` `INDEX` statement that created the index. Consider this `CREATE` `INDEX` statement:

```
CREATE INDEX comp_ind 
ON table1(x, y, z);
```
- `x`, `xy`, and `xyz` combinations of columns are leading portions of the index
- `yz`, `y`, and `z` combinations of columns are not leading portions of the index

#### 14.1.4.1 Choosing Keys for Composite Indexes

Follow these guidelines for choosing keys for composite indexes:

- Consider creating a composite index on keys that appear together frequently in `WHERE` clause conditions combined with `AND` operators, especially if their combined selectivity is better than the selectivity of either key individually.
- If several queries select the same set of keys based on one or more key values, then consider creating a composite index containing all of these keys.

Of course, consider the guidelines associated with the general performance advantages and trade-offs of indexes described in the previous sections.

#### 14.1.4.2 Ordering Keys for Composite Indexes

Follow these guidelines for ordering keys in composite indexes:

- Create the index so the keys used in `WHERE` clauses make up a leading portion.
- If some keys appear in `WHERE` clauses more frequently, then create the index so that the more frequently selected keys make up a leading portion to allow the statements that use only these keys to use the index.
- If all keys appear in `WHERE` clauses equally often but the data is physically ordered on one of the keys, then place this key first in the composite index.

### 14.1.5 Writing Statements That Use Indexes

Even after you create an index, the optimizer cannot use an access path that uses the index simply because the index exists. The optimizer can choose such an access path for a SQL statement only if it contains a construct that makes the access path available. To allow the query optimizer the option of using an index access path, ensure that the statement contains a construct that makes such an access path available.

### 14.1.6 Writing Statements That Avoid Using Indexes

In some cases, you might want to prevent a SQL statement from using an access path that uses an existing index. You may want to take this approach if you know that the index is not very selective and a full table scan would be more efficient. If the statement contains a construct that makes such an index access path available, then you can force the optimizer to use a full table scan through one of the following methods:

- Use the `NO_INDEX` hint to give the query optimizer maximum flexibility while disallowing the use of a certain index.
- Use the `FULL` hint to instruct the optimizer to choose a full table scan instead of an index scan.
- Use the `INDEX` or `INDEX_COMBINE` hints to instruct the optimizer to use one index or a set of listed indexes instead of another.
	See Also:
	[Chapter 19, "Using Optimizer Hints"](hintsref.md) for more information on the `NO_INDEX`, `FULL`, `INDEX`, and `INDEX_COMBINE` and hints

Parallel execution uses indexes effectively. It does not perform parallel index range scans, but it does perform parallel index lookups for parallel nested loop join execution. If an index is very selective (there are few rows for each index entry), then it might be better to use sequential index lookup rather than parallel table scan.

### 14.1.7 Re-creating Indexes

You might want to re-create an index to compact it and minimize fragmented space, or to change the index's storage characteristics. When creating a new index that is a subset of an existing index or when rebuilding an existing index with new storage characteristics, Oracle Database might use the existing index instead of the base table to improve the performance of the index build.

However, in some cases using the base table instead of the existing index is beneficial. Consider an index on a table on which a lot of DML has been performed. Because of the DML, the size of the index can increase to the point where each block is only 50% full, or even less. If the index refers to most of the columns in the table, then the index could actually be larger than the table. In this case, it is faster to use the base table rather than the index to re-create the index.

Use the `ALTER` `INDEX`... `REBUILD` statement to reorganize or compact an existing index or to change its storage characteristics. The `REBUILD` statement uses the existing index as the basis for the new one. All index storage statements are supported, such as `STORAGE` (for extent allocation), `TABLESPACE` (to move the index to a new tablespace), and `INITRANS` (to change the initial number of entries).

Usually, `ALTER` `INDEX`... `REBUILD` is faster than dropping and re-creating an index, because this statement uses the fast full scan feature. It reads all the index blocks using multiblock I/O, then discards the branch blocks. A further advantage of this approach is that the old index is still available for queries while the rebuild is in progress.

See Also:

[Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_1.htm#SQLRF008) for more information about the `CREATE` `INDEX` and `ALTER` `INDEX` statements and restrictions on rebuilding indexes

### 14.1.8 Compacting Indexes

You can coalesce leaf blocks of an index by using the `ALTER` `INDEX` statement with the `COALESCE` option. This option lets you combine leaf levels of an index to free blocks for reuse. You can also rebuild the index online.

See Also:

[Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/toc.htm) and [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/toc.htm) for more information about the syntax for this statement

### 14.1.9 Using Nonunique Indexes to Enforce Uniqueness

You can use an existing nonunique index on a table to enforce uniqueness, either for `UNIQUE` constraints or the unique aspect of a `PRIMARY` `KEY` constraint. The advantage of this approach is that the index remains available and valid when the constraint is disabled. Therefore, enabling a disabled `UNIQUE` or `PRIMARY` `KEY` constraint does not require rebuilding the unique index associated with the constraint. This can yield significant time savings on enable operations for large tables.

Using a nonunique index to enforce uniqueness also lets you eliminate redundant indexes. You do not need a unique index on a primary key column if that column is included as the prefix of a composite index. You can use the existing index to enable and enforce the constraint. You also save significant space by not duplicating the index. However, if the existing index is partitioned, then the partitioning key of the index must also be a subset of the `UNIQUE` key; otherwise, Oracle Database creates an additional unique index to enforce the constraint.

### 14.1.10 Using Enabled Novalidated Constraints

An enabled novalidated constraint behaves similarly to an enabled validated constraint for new data. Placing a constraint in the enabled novalidated state signifies that any new data entered into the table must conform to the constraint. Existing data is not checked. By placing a constraint in the enabled novalidated state, you enable the constraint without locking the table.

If you change a constraint from disabled to enabled, then the table must be locked. No new DML, queries, or DDL can occur, because no mechanism can ensure that operations on the table conform to the constraint during the enable operation. The enabled novalidated state prevents users from performing operations on the table that violate the constraint.

The database can validate an enabled novalidated constraint with a parallel, consistent-read query of the table to determine whether any data violates the constraint. The database performs no locking, so the enable operation does not block readers or writers. In addition, the database can validate enabled novalidated constraints in parallel. The database can validate multiple constraints at the same time and check the validity of each constraint using parallel query.

Use the following approach to create tables with constraints and indexes:

1. Create the tables with the constraints. `NOT` `NULL` constraints can be unnamed and should be created enabled and validated. You should name all other constraints (`CHECK`, `UNIQUE`, `PRIMARY` `KEY`, and `FOREIGN` `KEY`) and create them disabled.
	Note:
	By default, constraints are created in the `ENABLED` state.
2. Load old data into the tables.
3. Create all indexes, including indexes needed for constraints.
4. Enable novalidate all constraints. Do this to primary keys before foreign keys.
5. Allow users to query and modify data.
6. With a separate `ALTER` `TABLE` statement for each constraint, validate all constraints. Do this to primary keys before foreign keys. For example,
	```
	CREATE TABLE t (a NUMBER CONSTRAINT apk PRIMARY KEY DISABLE,
	b NUMBER NOT NULL);
	CREATE TABLE x (c NUMBER CONSTRAINT afk REFERENCES t DISABLE);
	```

Now load data into table `t`.

```
CREATE UNIQUE INDEX tai ON t (a); 
CREATE INDEX tci ON x (c); 
ALTER TABLE t MODIFY CONSTRAINT apk ENABLE NOVALIDATE;
ALTER TABLE x MODIFY CONSTRAINT afk ENABLE NOVALIDATE;
```

At this point, users can start performing `INSERT`, `UPDATE`, `DELETE`, and `SELECT` operations on table `t`.

```
ALTER TABLE t ENABLE CONSTRAINT apk;
ALTER TABLE x ENABLE CONSTRAINT afk;
```

Now the constraints are enabled and validated.

See Also:

[Oracle Database Concepts](https://docs.oracle.com/cd/E11882_01/server.112/e40540/datainte.htm#CNCPT021) for a complete discussion of integrity constraints

## 14.2 Using Function-based Indexes for Performance

A function-based index includes columns that are either transformed by a function, such as the `UPPER` function, or included in an expression, such as `col1` + `col2`. With a function-based index, you can store computation-intensive expressions in the index.

Defining a function-based index on the transformed column or expression allows that data to be returned using the index when that function or expression is used in a `WHERE` clause or an `ORDER` `BY` clause. This allows Oracle Database to bypass computing the value of the expression when processing `SELECT` and `DELETE` statements. Therefore, a function-based index can be beneficial when frequently-executed SQL statements include transformed columns, or columns in expressions, in a `WHERE` or `ORDER` `BY` clause.

Oracle Database treats descending indexes as function-based indexes. The columns marked `DESC` are sorted in descending order.

For example, function-based indexes defined with the `UPPER` (`column_name`) or `LOWER` (`column_name`) keywords allow case-insensitive searches. The index created in the following statement:

```
CREATE INDEX uppercase_idx ON employees (UPPER(last_name));
```

facilitates processing queries such as:

```
SELECT * FROM employees
    WHERE UPPER(last_name) = 'MARKSON';
```

See Also:

- [Oracle Database Advanced Application Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e41502/toc.htm) and [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/toc.htm) for more information on using function-based indexes
- [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_5.htm#SQLRF012) for more information on the `CREATE` `INDEX` statement

## 14.3 Using Partitioned Indexes for Performance

Similar to partitioned tables, partitioned indexes improve manageability, availability, performance, and scalability. They can either be partitioned independently (global indexes) or automatically linked to a table's partitioning method (local indexes).

Oracle Database supports both range and hash partitioned global indexes. In a range partitioned global index, each index partition contains values defined by a partition bound. In a hash partitioned global index, each partition contains values determined by the Oracle Database hash function.

The hash method can improve performance of indexes where a small number leaf blocks in the index have high contention in multiuser OLTP environment. In some OLTP applications, index insertions happen only at the right edge of the index. This situation could occur when the index is defined on monotonically increasing columns. In such situations, the right edge of the index becomes a hotspot because of contention for index pages, buffers, latches for update, and additional index maintenance activity, which results in performance degradation.

With hash partitioned global indexes index entries are hashed to different partitions based on partitioning key and the number of partitions. This spreads out contention over number of defined partitions, resulting in increased throughput. Hash-partitioned global indexes would benefit TPC-H refresh functions that are executed as massive PDMLs into huge fact tables because contention for buffer latches would be spread out over multiple partitions.

With hash partitioning, an index entry is mapped to a particular index partition based on the hash value generated by Oracle Database. The syntax to create hash-partitioned global index is very similar to hash-partitioned table. Queries involving equality and `IN` predicates on index partitioning key can efficiently use global hash partitioned index to answer queries quickly.

See Also:

[Oracle Database Concepts](https://docs.oracle.com/cd/E11882_01/server.112/e40540/tablecls.htm#CNCPT010) and [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/tables.htm#ADMIN01506) for more information on global indexes tables

## 14.4 Using Index-Organized Tables for Performance

An index-organized table differs from an ordinary table in that the data for the table is held in its associated index. Changes to the table data, such as adding new rows, updating rows, or deleting rows, result only in updating the index. Because data rows are stored in the index, index-organized tables provide faster key-based access to table data for queries that involve exact match or range search or both.

A parent/child relationship is an example of a situation that may warrant an index-organized table. For example, a members table has a child table containing phone numbers. Phone numbers for a member are changed and added over time. In a heap-organized table, rows are inserted in data blocks where they fit. However, when you query the members table, you always retrieve the phone numbers from the child table. To make the retrieval more efficient, you can store the phone numbers in an index-organized table so that phone records for a given member are inserted near each other in the data blocks.

In some circumstances, an index-organized table may provide a performance advantage over a heap-organized table. For example, if a query requires fewer blocks in the cache, then the database uses the buffer cache more efficiently. If fewer distinct blocks are needed for a query, then a single physical I/O may retrieve all necessary data, requiring a smaller amount of I/O for each query.

Global hash-partitioned indexes are supported for index-organized tables and can provide performance benefits in a multiuser OLTP environment. Index-organized tables are useful when you must store related pieces of data together or physically store data in a specific order.

See Also:

[Oracle Database Concepts](https://docs.oracle.com/cd/E11882_01/server.112/e40540/tablecls.htm#CNCPT010) and [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/tables.htm#ADMIN01506) for more information on index-organized tables

## 14.5 Using Bitmap Indexes for Performance

Bitmap indexes can substantially improve performance of queries that have all of the following characteristics:

- The `WHERE` clause contains multiple predicates on low- or medium-cardinality columns.
- The individual predicates on these low- or medium-cardinality columns select a large number of rows.
- The bitmap indexes used in the queries have been created on some or all of these low- or medium-cardinality columns.
- The tables in the queries contain many rows.

You can use multiple bitmap indexes to evaluate the conditions on a single table. Bitmap indexes are thus highly advantageous for complex ad hoc queries that contain lengthy `WHERE` clauses. Bitmap indexes can also provide optimal performance for aggregate queries and for optimizing joins in star schemas.

See Also:

[Oracle Database Concepts](https://docs.oracle.com/cd/E11882_01/server.112/e40540/tablecls.htm#CNCPT010) and [Oracle Database Data Warehousing Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25554/indexes.htm#DWHSG006) for more information on bitmap indexing

## 14.6 Using Bitmap Join Indexes for Performance

In addition to a bitmap index on a single table, you can create a bitmap join index, which is a bitmap index for the join of two or more tables. A bitmap join index is a space-saving way to reduce the volume of data that must be joined by performing restrictions in advance. For each value in a column of a table, a bitmap join index stores the rowids of corresponding rows in another table. In a data warehousing environment, the join condition is an equi-inner join between the primary key column(s) of the dimension tables and the foreign key column(s) in the fact table.

Bitmap join indexes are much more efficient in storage than materialized join views, an alternative for materializing joins in advance. Materialized join views do not compress the rowids of the fact tables.

See Also:

[Oracle Database Data Warehousing Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25554/indexes.htm#DWHSG006) for examples and restrictions of bitmap join indexes

## 14.7 Using Domain Indexes for Performance

Domain indexes are built using the indexing logic supplied by a user-defined indextype. An indextype provides an efficient mechanism to access data that satisfy certain operator predicates. Typically, the user-defined indextype is part of an Oracle Database option, like the Spatial option. For example, the `SpatialIndextype` allows efficient search and retrieval of spatial data that overlap a given bounding box.

The cartridge determines the parameters you can specify in creating and maintaining the domain index. Similarly, the performance and storage characteristics of the domain index are presented in the specific cartridge documentation.

Refer to the appropriate cartridge documentation for information such as the following:

- What data types can be indexed?
- What indextypes are provided?
- What operators does the indextype support?
- How can the domain index be created and maintained?
- How do we efficiently use the operator in queries?
- What are the performance characteristics?
	Note:
	You can also create index types with the `CREATE` `INDEXTYPE` statement.
	See Also:
	[Oracle Spatial Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e11830/toc.htm) for information about the `SpatialIndextype`

## 14.8 Using Table Clusters for Performance

A table cluster is a group of one or more tables that are physically stored together because they share common columns and usually appear together in SQL statements. Because the database physically stores related rows together, disk access time improves. To create a cluster, use the `CREATE` `CLUSTER` statement.

See Also:

[Oracle Database Concepts](https://docs.oracle.com/cd/E11882_01/server.112/e40540/toc.htm) for more information on clusters

Follow these guidelines when deciding whether to cluster tables:

- Cluster tables that are accessed frequently by the application in join statements.
- Do not cluster tables if the application joins them only occasionally or modifies their common column values frequently. Modifying a row's cluster key value takes longer than modifying the value in an unclustered table, because Oracle Database might need to migrate the modified row to another block to maintain the cluster.
- Do not cluster tables if the application often performs full table scans of only one of the tables. A full table scan of a clustered table can take longer than a full table scan of an unclustered table. Oracle Database is likely to read more blocks because the tables are stored together.
- Cluster master-detail tables if you often select a master record and then the corresponding detail records. Detail records are stored in the same data block(s) as the master record, so they are likely still to be in memory when you select them, requiring Oracle Database to perform less I/O.
- Store a detail table alone in a cluster if you often select many detail records of the same master. This measure improves the performance of queries that select detail records of the same master, but does not decrease the performance of a full table scan on the master table. An alternative is to use an index organized table.
- Do not cluster tables if the data from all tables with the same cluster key value exceeds more than one or two data blocks. To access a row in a clustered table, Oracle Database reads all blocks containing rows with that value. If these rows take up multiple blocks, then accessing a single row could require more reads than accessing the same row in an unclustered table.
- Do not cluster tables when the number of rows for each cluster key value varies significantly. This causes waste of space for the low cardinality key value; it causes collisions for the high cardinality key values. Collisions degrade performance.

Consider the benefits and drawbacks of clusters for the application. For example, you might decide that the performance gain for join statements outweighs the performance loss for statements that modify cluster key values. You might want to experiment and compare processing times with the tables both clustered and stored separately.

See Also:

[Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/toc.htm) for more information on creating clusters

## 14.9 Using Hash Clusters for Performance

Hash clusters group table data by applying a hash function to each row's cluster key value. All rows with the same cluster key value are stored together on disk. Consider the benefits and drawbacks of hash clusters for the application. You might want to experiment and compare processing times with a particular table in a hash cluster and alone with an index.

Follow these guidelines for choosing when to use hash clusters:

- Use hash clusters to store tables accessed frequently by SQL statements with `WHERE` clauses, if the `WHERE` clauses contain equality conditions that use the same column or combination of columns. Designate this column or combination of columns as the cluster key.
- Store a table in a hash cluster if you can determine how much space is required to hold all rows with a given cluster key value, including rows to be inserted immediately and rows to be inserted in the future.
- Use sorted hash clusters, where rows corresponding to each value of the hash function are sorted on a specific columns in ascending order, when the database can improve response time on operations with this sorted clustered data.
- Do not store a table in a hash cluster if the application often performs full table scans and if you must allocate a great deal of space to the hash cluster in anticipation of the table growing. Such full table scans must read all blocks allocated to the hash cluster, even though some blocks might contain few rows. Storing the table alone reduces the number of blocks read by full table scans.
- Do not store a table in a hash cluster if the application frequently modifies the cluster key values. Modifying a row's cluster key value can take longer than modifying the value in an unclustered table, because Oracle Database might need to migrate the modified row to another block to maintain the cluster.

Storing a single table in a hash cluster can be useful, regardless of whether the table is joined frequently with other tables, as long as hashing is appropriate for the table based on the considerations in this list.

See Also:

- [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/hash.htm#ADMIN019) to learn how to manage hash clusters
- [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_5001.htm#SQLRF01201) to learn about the `CREATE` `CLUSTER` statement