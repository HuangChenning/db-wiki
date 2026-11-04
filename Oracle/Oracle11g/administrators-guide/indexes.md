---
title: Managing Indexes
book: "Administrator's Guide"
doc_id: E25494-07
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e25494/indexes.htm
tags:
  - oracle
  - 11g
  - administrators-guide
---

## 21 Managing Indexes

In this chapter:

## About Indexes

Indexes are optional structures associated with tables and clusters that allow SQL queries to execute more quickly against a table. Just as the index in this manual helps you locate information faster than if there were no index, an Oracle Database index provides a faster access path to table data. You can use indexes without rewriting any queries. Your results are the same, but you see them more quickly.

Oracle Database provides several indexing schemes that provide complementary performance functionality. These are:

- B-tree indexes: the default and the most common
- B-tree cluster indexes: defined specifically for cluster
- Hash cluster indexes: defined specifically for a hash cluster
- Global and local indexes: relate to partitioned tables and indexes
- Reverse key indexes: most useful for Oracle Real Application Clusters applications
- Bitmap indexes: compact; work best for columns with a small set of values
- Function-based indexes: contain the precomputed value of a function/expression
- Domain indexes: specific to an application or cartridge.

Indexes are logically and physically independent of the data in the associated table. Being independent structures, they require storage space. You can create or drop an index without affecting the base tables, database applications, or other indexes. The database automatically maintains indexes when you insert, update, and delete rows of the associated table. If you drop an index, all applications continue to work. However, access to previously indexed data might be slower.

See Also:

- [Oracle Database Concepts](https://docs.oracle.com/cd/E11882_01/server.112/e40540/indexiot.htm#CNCPT811) for an overview of indexes
- [Chapter 19, "Managing Space for Schema Objects"](schema.md)

## Guidelines for Managing Indexes

This section discusses guidelines for managing indexes and contains the following topics:

- Create Indexes After Inserting Table Data
- Index the Correct Tables and Columns
- Order Index Columns for Performance
- Limit the Number of Indexes for Each Table
- Drop Indexes That Are No Longer Required
- Indexes and Deferred Segment Creation
- Estimate Index Size and Set Storage Parameters
- Specify the Tablespace for Each Index
- Consider Parallelizing Index Creation
- Consider Creating Indexes with NOLOGGING
- Understand When to Use Unusable or Invisible Indexes
- Consider Costs and Benefits of Coalescing or Rebuilding Indexes
- Consider Cost Before Disabling or Dropping Constraints
	See Also:
	- [Oracle Database Concepts](https://docs.oracle.com/cd/E11882_01/server.112/e40540/indexiot.htm#CNCPT811) for conceptual information about indexes and indexing, including descriptions of the various indexing schemes offered by Oracle
	- [Oracle Database Performance Tuning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41573/data_acc.htm#PFGRF94788) and [Oracle Database Data Warehousing Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25554/indexes.htm#DWHSG006) for information about bitmap indexes
	- [Oracle Database Data Cartridge Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e10765/dom_idx.htm#ADDCI290) for information about defining domain-specific operators and indexing schemes and integrating them into the Oracle Database server

### Create Indexes After Inserting Table Data

Data is often inserted or loaded into a table using either the SQL\*Loader or an import utility. It is more efficient to create an index for a table after inserting or loading the data. If you create one or more indexes before loading data, the database then must update every index as each row is inserted.

Creating an index on a table that already has data requires sort space. Some sort space comes from memory allocated for the index creator. The amount for each user is determined by the initialization parameter `SORT_AREA_SIZE`. The database also swaps sort information to and from temporary segments that are only allocated during the index creation in the user's temporary tablespace.

Under certain conditions, data can be loaded into a table with SQL\*Loader direct-path load and an index can be created as data is loaded.

See Also:

[Oracle Database Utilities](https://docs.oracle.com/cd/E11882_01/server.112/e22490/ldr_modes.htm#SUTIL009) for information about using SQL\*Loader for direct-path load

### Index the Correct Tables and Columns

Use the following guidelines for determining when to create an index:

- Create an index if you frequently want to retrieve less than 15% of the rows in a large table. The percentage varies greatly according to the relative speed of a table scan and how the row data is distributed in relation to the index key. The faster the table scan, the lower the percentage; the more clustered the row data, the higher the percentage.
- To improve performance on joins of multiple tables, index columns used for joins.
	Note:
	Primary and unique keys automatically have indexes, but you might want to create an index on a foreign key.
- Small tables do not require indexes. If a query is taking too long, then the table might have grown from small to large.

Columns That Are Suitable for Indexing

Some columns are strong candidates for indexing. Columns with one or more of the following characteristics are candidates for indexing:

- Values are relatively unique in the column.
- There is a wide range of values (good for regular indexes).
- There is a small range of values (good for bitmap indexes).
- The column contains many nulls, but queries often select all rows having a value. In this case, use the following phrase:
	```
	WHERE COL_X > -9.99 * power(10,125)
	```
	Using the preceding phrase is preferable to:
	```
	WHERE COL_X IS NOT NULL
	```
	This is because the first uses an index on `COL_X` (assuming that `COL_X` is a numeric column).

Columns That Are Not Suitable for Indexing

Columns with the following characteristics are less suitable for indexing:

- There are many nulls in the column and you do not search on the not null values.

`LONG` and `LONG` `RAW` columns cannot be indexed.

Virtual Columns

You can create unique or non-unique indexes on virtual columns. A table index defined on a virtual column is equivalent to a function-based index on the table.

See Also:

"Creating a Function-Based Index"

### Order Index Columns for Performance

The order of columns in the `CREATE` `INDEX` statement can affect query performance. In general, specify the most frequently used columns first.

If you create a single index across columns to speed up queries that access, for example, `col1`, `col2`, and `col3`; then queries that access just `col1`, or that access just `col1` and `col2`, are also speeded up. But a query that accessed just `col2`, just `col3`, or just `col2` and `col3` does not use the index.

Note:

In some cases, such as when the leading column has very low cardinality, the database may use a skip scan of this type of index. See [Oracle Database Concepts](https://docs.oracle.com/cd/E11882_01/server.112/e40540/indexiot.htm#CNCPT88842) for more information about index skip scan.

### Limit the Number of Indexes for Each Table

A table can have any number of indexes. However, the more indexes there are, the more overhead is incurred as the table is modified. Specifically, when rows are inserted or deleted, all indexes on the table must be updated as well. Also, when a column is updated, all indexes that contain the column must be updated.

Thus, there is a trade-off between the speed of retrieving data from a table and the speed of updating the table. For example, if a table is primarily read-only, having more indexes can be useful; but if a table is heavily updated, having fewer indexes could be preferable.

### Drop Indexes That Are No Longer Required

Consider dropping an index if:

- It does not speed up queries. The table could be very small, or there could be many rows in the table but very few index entries.
- The queries in your applications do not use the index.
- The index must be dropped before being rebuilt.
	See Also:
	"Monitoring Index Usage"

### Indexes and Deferred Segment Creation

Index segment creation is deferred when the associated table defers segment creation. This is because index segment creation reflects the behavior of the table it is associated with.

See Also:

["Understand Deferred Segment Creation"](tables.md) for further information

### Estimate Index Size and Set Storage Parameters

Estimating the size of an index before creating one can facilitate better disk space planning and management. You can use the combined estimated size of indexes, along with estimates for tables, the undo tablespace, and redo log files, to determine the amount of disk space that is required to hold an intended database. From these estimates, you can make correct hardware purchases and other decisions.

Use the estimated size of an individual index to better manage the disk space that the index uses. When an index is created, you can set appropriate storage parameters and improve I/O performance of applications that use the index. For example, assume that you estimate the maximum size of an index before creating it. If you then set the storage parameters when you create the index, fewer extents are allocated for the table data segment, and all of the index data is stored in a relatively contiguous section of disk space. This decreases the time necessary for disk I/O operations involving this index.

The maximum size of a single index entry is approximately one-half the data block size.

Storage parameters of an index segment created for the index used to enforce a primary key or unique key constraint can be set in either of the following ways:

- In the `ENABLE`... `USING` `INDEX` clause of the `CREATE` `TABLE` or `ALTER` `TABLE` statement
- In the `STORAGE` clause of the `ALTER` `INDEX` statement

### Specify the Tablespace for Each Index

Indexes can be created in any tablespace. An index can be created in the same or different tablespace as the table it indexes. If you use the same tablespace for a table and its index, it can be more convenient to perform database maintenance (such as tablespace or file backup) or to ensure application availability. All the related data is always online together.

Using different tablespaces (on different disks) for a table and its index produces better performance than storing the table and index in the same tablespace. Disk contention is reduced. But, if you use different tablespaces for a table and its index and one tablespace is offline (containing either data or index), then the statements referencing that table are not guaranteed to work.

### Consider Parallelizing Index Creation

You can parallelize index creation, much the same as you can parallelize table creation. Because multiple processes work together to create the index, the database can create the index more quickly than if a single server process created the index sequentially.

When creating an index in parallel, storage parameters are used separately by each query server process. Therefore, an index created with an `INITIAL` value of 5M and a parallel degree of 12 consumes at least 60M of storage during index creation.

See Also:

[Oracle Database VLDB and Partitioning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25523/parallel.htm#VLDBG010) for information about using parallel execution

### Consider Creating Indexes with NOLOGGING

You can create an index and generate minimal redo log records by specifying `NOLOGGING` in the `CREATE INDEX` statement.

Note:

Because indexes created using `NOLOGGING` are not archived, perform a backup after you create the index.

Creating an index with `NOLOGGING` has the following benefits:

- Space is saved in the redo log files.
- The time it takes to create the index is decreased.
- Performance improves for parallel creation of large indexes.

In general, the relative performance improvement is greater for larger indexes created without `LOGGING` than for smaller ones. Creating small indexes without `LOGGING` has little effect on the time it takes to create an index. However, for larger indexes the performance improvement can be significant, especially when you are also parallelizing the index creation.

### Understand When to Use Unusable or Invisible Indexes

Use unusable or invisible indexes when you want to improve the performance of bulk loads, test the effects of removing an index before dropping it, or otherwise suspend the use of an index by the optimizer.

Unusable indexes

An unusable index is ignored by the optimizer and is not maintained by DML. One reason to make an index unusable is to improve bulk load performance. (Bulk loads go more quickly if the database does not need to maintain indexes when inserting rows.) Instead of dropping the index and later re-creating it, which requires you to recall the exact parameters of the `CREATE` `INDEX` statement, you can make the index unusable, and then rebuild it.

You can create an index in the unusable state, or you can mark an existing index or index partition unusable. In some cases the database may mark an index unusable, such as when a failure occurs while building the index. When one partition of a partitioned index is marked unusable, the other partitions of the index remain valid.

An unusable index or index partition must be rebuilt, or dropped and re-created, before it can be used. Truncating a table makes an unusable index valid.

Beginning with Oracle Database 11g Release 2, when you make an existing index unusable, its index segment is dropped.

The functionality of unusable indexes depends on the setting of the `SKIP_UNUSABLE_INDEXES` initialization parameter. When `SKIP_UNUSABLE_INDEXES` is `TRUE` (the default), then:

- DML statements against the table proceed, but unusable indexes are not maintained.
- DML statements terminate with an error if there are any unusable indexes that are used to enforce the `UNIQUE` constraint.
- For nonpartitioned indexes, the optimizer does not consider any unusable indexes when creating an access plan for `SELECT` statements. The only exception is when an index is explicitly specified with the `INDEX()` hint.
- For a partitioned index where one or more of the partitions are unusable, the optimizer does not consider the index if it cannot determine at query compilation time if any of the index partitions can be pruned. This is true for both partitioned and nonpartitioned tables. The only exception is when an index is explicitly specified with the `INDEX()` hint.

When `SKIP_UNUSABLE_INDEXES` is `FALSE`, then:

- If any unusable indexes or index partitions are present, any DML statements that would cause those indexes or index partitions to be updated are terminated with an error.
- For `SELECT` statements, if an unusable index or unusable index partition is present but the optimizer does not choose to use it for the access plan, the statement proceeds. However, if the optimizer does choose to use the unusable index or unusable index partition, the statement terminates with an error.

Invisible Indexes

Beginning with Oracle Database 11g Release 1, you can create invisible indexes or make an existing index invisible. An invisible index is ignored by the optimizer unless you explicitly set the `OPTIMIZER_USE_INVISIBLE_INDEXES` initialization parameter to `TRUE` at the session or system level. Unlike unusable indexes, an invisible index is maintained during DML statements. Although you can make a partitioned index invisible, you cannot make an individual index partition invisible while leaving the other partitions visible.Using invisible indexes, you can do the following:

- Test the removal of an index before dropping it.
- Use temporary index structures for certain operations or modules of an application without affecting the overall application.

### Consider Costs and Benefits of Coalescing or Rebuilding Indexes

Improper sizing or increased growth can produce index fragmentation. To eliminate or reduce fragmentation, you can rebuild or coalesce the index. But before you perform either task weigh the costs and benefits of each option and choose the one that works best for your situation. Table 21-1 is a comparison of the costs and benefits associated with rebuilding and coalescing indexes.

Table 21-1 Costs and Benefits of Coalescing or Rebuilding Indexes

| Rebuild Index | Coalesce Index |
| --- | --- |
| Quickly moves index to another tablespace | Cannot move index to another tablespace |
| Higher costs: requires more disk space | Lower costs: does not require more disk space |
| Creates new tree, shrinks height if applicable | Coalesces leaf blocks within same branch of tree |
| Enables you to quickly change storage and tablespace parameters without having to drop the original index. | Quickly frees up index leaf blocks for use. |

In situations where you have B-tree index leaf blocks that can be freed up for reuse, you can merge those leaf blocks using the following statement:

```
ALTER INDEX vmoore COALESCE;
```

Figure 21-1 illustrates the effect of an `ALTER INDEX COALESCE` on the index `vmoore`. Before performing the operation, the first two leaf blocks are 50% full. Therefore, you have an opportunity to reduce fragmentation and completely fill the first block, while freeing up the second.

Figure 21-1 Coalescing Indexes

![Figure 21-1 Coalescing Indexes](img/admin026.gif)

> This is a text description of admin026.gif. It shows a B-tree index before and after coalescing. In the "before" image, there are two index blocks, each of which is half full. The "after" image shows that these two index blocks have been combined into one full index block.
>
> End of image description.
  

### Consider Cost Before Disabling or Dropping Constraints

Because unique and primary keys have associated indexes, you should factor in the cost of dropping and creating indexes when considering whether to disable or drop a `UNIQUE` or `PRIMARY KEY` constraint. If the associated index for a `UNIQUE` key or `PRIMARY KEY` constraint is extremely large, you can save time by leaving the constraint enabled rather than dropping and re-creating the large index. You also have the option of explicitly specifying that you want to keep or drop the index when dropping or disabling a `UNIQUE` or `PRIMARY KEY` constraint.

See Also:

["Managing Integrity Constraints"](general.md)

## Creating Indexes

This section describes how to create indexes.

Note:

These operations also collect index statistics.

To create an index in your own schema, at least one of the following conditions must be true:

- The table or cluster to be indexed is in your own schema.
- You have `INDEX` privilege on the table to be indexed.
- You have `CREATE ANY INDEX` system privilege.

To create an index in another schema, all of the following conditions must be true:

- You have `CREATE ANY INDEX` system privilege.
- The owner of the other schema has a quota for the tablespaces to contain the index or index partitions, or `UNLIMITED TABLESPACE` system privilege.

This section contains the following topics:

- Creating an Index Explicitly
- Creating a Unique Index Explicitly
- Creating an Index Associated with a Constraint
- Creating a Large Index
- Creating an Index Online
- Creating a Function-Based Index
- Creating a Key-Compressed Index
- Creating an Unusable Index
- Creating an Invisible Index

### Creating an Index Explicitly

You can create indexes explicitly (outside of integrity constraints) using the SQL statement `CREATE INDEX`. The following statement creates an index named `emp_ename` for the `ename` column of the `emp` table:

```
CREATE INDEX emp_ename ON emp(ename)
      TABLESPACE users
      STORAGE (INITIAL 20K
      NEXT 20k);
```

Notice that several storage settings and a tablespace are explicitly specified for the index. If you do not specify storage options (such as `INITIAL` and `NEXT`) for an index, the default storage options of the default or specified tablespace are automatically used.

See Also:

[Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_5012.htm#SQLRF01209) for syntax and restrictions on the use of the `CREATE INDEX` statement

### Creating a Unique Index Explicitly

Indexes can be unique or non-unique. Unique indexes guarantee that no two rows of a table have duplicate values in the key column (or columns). Non-unique indexes do not impose this restriction on the column values.

Use the `CREATE UNIQUE INDEX` statement to create a unique index. The following example creates a unique index:

```
CREATE UNIQUE INDEX dept_unique_index ON dept (dname)
      TABLESPACE indx;
```

Alternatively, you can define `UNIQUE` integrity constraints on the desired columns. The database enforces `UNIQUE` integrity constraints by automatically defining a unique index on the unique key. This is discussed in the following section. However, it is advisable that any index that exists for query performance, including unique indexes, be created explicitly.

See Also:

[Oracle Database Performance Tuning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41573/data_acc.htm#PFGRF004) for more information about creating an index for performance

### Creating an Index Associated with a Constraint

Oracle Database enforces a `UNIQUE` key or `PRIMARY KEY` integrity constraint on a table by creating a unique index on the unique key or primary key. This index is automatically created by the database when the constraint is enabled. No action is required by you when you issue the `CREATE TABLE` or `ALTER TABLE` statement to create the index, but you can optionally specify a `USING INDEX` clause to exercise control over its creation. This includes both when a constraint is defined and enabled, and when a defined but disabled constraint is enabled.

To enable a `UNIQUE` or `PRIMARY KEY` constraint, thus creating an associated index, the owner of the table must have a quota for the tablespace intended to contain the index, or the `UNLIMITED TABLESPACE` system privilege. The index associated with a constraint always takes the name of the constraint, unless you optionally specify otherwise.

Note:

An efficient procedure for enabling a constraint that can make use of parallelism is described in ["Efficient Use of Integrity Constraints: A Procedure"](general.md).

#### Specifying Storage Options for an Index Associated with a Constraint

You can set the storage options for the indexes associated with `UNIQUE` and `PRIMARY KEY` constraints using the `USING INDEX` clause. The following `CREATE TABLE` statement enables a `PRIMARY KEY` constraint and specifies the storage options of the associated index:

```
CREATE TABLE emp (
     empno NUMBER(5) PRIMARY KEY, age INTEGER)
     ENABLE PRIMARY KEY USING INDEX
     TABLESPACE users;
```

#### Specifying the Index Associated with a Constraint

If you require more explicit control over the indexes associated with `UNIQUE` and `PRIMARY KEY` constraints, the database lets you:

- Specify an existing index that the database is to use to enforce the constraint
- Specify a `CREATE` `INDEX` statement that the database is to use to create the index and enforce the constraint

These options are specified using the `USING` `INDEX` clause. The following statements present some examples.

Example 1:

```
CREATE TABLE a (
     a1 INT PRIMARY KEY USING INDEX (create index ai on a (a1)));
```

Example 2:

```
CREATE TABLE b(
     b1 INT, 
     b2 INT, 
     CONSTRAINT bu1 UNIQUE (b1, b2) 
                    USING INDEX (create unique index bi on b(b1, b2)),
     CONSTRAINT bu2 UNIQUE (b2, b1) USING INDEX bi);
```

Example 3:

```
CREATE TABLE c(c1 INT, c2 INT);
CREATE INDEX ci ON c (c1, c2);
ALTER TABLE c ADD CONSTRAINT cpk PRIMARY KEY (c1) USING INDEX ci;
```

If a single statement creates an index with one constraint and also uses that index for another constraint, the system will attempt to rearrange the clauses to create the index before reusing it.

See Also:

["Managing Integrity Constraints"](general.md)

### Creating a Large Index

When creating an extremely large index, consider allocating a larger temporary tablespace for the index creation using the following procedure:

1. Create a new temporary tablespace using the `CREATE TABLESPACE` or `CREATE TEMPORARY TABLESPACE` statement.
2. Use the `TEMPORARY TABLESPACE` option of the `ALTER USER` statement to make this your new temporary tablespace.
3. Create the index using the `CREATE INDEX` statement.
4. Drop this tablespace using the `DROP TABLESPACE` statement. Then use the `ALTER USER` statement to reset your temporary tablespace to your original temporary tablespace.

Using this procedure can avoid the problem of expanding your usual, and usually shared, temporary tablespace to an unreasonably large size that might affect future performance.

### Creating an Index Online

You can create and rebuild indexes online. Therefore, you can update base tables at the same time you are building or rebuilding indexes on that table. You can perform DML operations while the index build is taking place, but DDL operations are not allowed. Parallel execution is not supported when creating or rebuilding an index online.

The following statements illustrate online index build operations:

```
CREATE INDEX emp_name ON emp (mgr, emp1, emp2, emp3) ONLINE;
```

Note:

Keep in mind that the time that it takes on online index build to complete is proportional to the size of the table and the number of concurrently executing DML statements. Therefore, it is best to start online index builds when DML activity is low.

See Also:

"Rebuilding an Existing Index"

### Creating a Function-Based Index

Function-based indexes facilitate queries that qualify a value returned by a function or expression. The value of the function or expression is precomputed and stored in the index.

In addition to the prerequisites for creating a conventional index, if the index is based on user-defined functions, then those functions must be marked `DETERMINISTIC`. Also, you just have the `EXECUTE` object privilege on any user-defined function(s) used in the function-based index if those functions are owned by another user.

Note:

`CREATE INDEX` stores the timestamp of the most recent function used in the function-based index. This timestamp is updated when the index is validated. When performing tablespace point-in-time recovery of a function-based index, if the timestamp on the most recent function used in the index is newer than the timestamp stored in the index, then the index is marked invalid. You must use the `ANALYZE INDEX...VALIDATE STRUCTURE` statement to validate this index.

To illustrate a function-based index, consider the following statement that defines a function-based index (`area_index`) defined on the function `area(geo)`:

```
CREATE INDEX area_index ON rivers (area(geo));
```

In the following SQL statement, when `area(geo)` is referenced in the `WHERE` clause, the optimizer considers using the index `area_index`.

```
SELECT id, geo, area(geo), desc
     FROM rivers     
     WHERE Area(geo) >5000;
```

Table owners should have `EXECUTE` privileges on the functions used in function-based indexes.

Because a function-based index depends upon any function it is using, it can be invalidated when a function changes. If the function is valid, you can use an `ALTER INDEX...ENABLE` statement to enable a function-based index that has been disabled. The `ALTER INDEX...DISABLE` statement lets you disable the use of a function-based index. Consider doing this if you are working on the body of the function.

Note:

An alternative to creating a function-based index is to add a virtual column to the target table and index the virtual column. See ["About Tables"](tables.md) for more information.

See Also:

- [Oracle Database Concepts](https://docs.oracle.com/cd/E11882_01/server.112/e40540/indexiot.htm#CNCPT1161) for more information about function-based indexes
- [Oracle Database Advanced Application Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e41502/adfns_indexes.htm#ADFNS00505) for information about using function-based indexes in applications and examples of their use

### Creating a Key-Compressed Index

Creating an index using key compression enables you to eliminate repeated occurrences of key column prefix values.

Key compression breaks an index key into a prefix and a suffix entry. Compression is achieved by sharing the prefix entries among all the suffix entries in an index block. This sharing can lead to huge savings in space, allowing you to store more keys for each index block while improving performance.

Key compression can be useful in the following situations:

- You have a non-unique index where `ROWID` is appended to make the key unique. If you use key compression here, the duplicate key is stored as a prefix entry on the index block without the `ROWID`. The remaining rows become suffix entries consisting of only the `ROWID`.
- You have a unique multicolumn index.

You enable key compression using the `COMPRESS` clause. The prefix length (as the number of key columns) can also be specified to identify how the key columns are broken into a prefix and suffix entry. For example, the following statement compresses duplicate occurrences of a key in the index leaf block:

```
CREATE INDEX  emp_ename ON emp(ename)
   TABLESPACE users
   COMPRESS 1;
```

The `COMPRESS` clause can also be specified during rebuild. For example, during rebuild you can disable compression as follows:

```
ALTER INDEX emp_ename REBUILD NOCOMPRESS;
```

See Also:

[Oracle Database Concepts](https://docs.oracle.com/cd/E11882_01/server.112/e40540/indexiot.htm#CNCPT1177) for a more detailed discussion of key compression

### Creating an Unusable Index

When you create an index in the `UNUSABLE` state, it is ignored by the optimizer and is not maintained by DML. An unusable index must be rebuilt, or dropped and re-created, before it can be used.

If the index is partitioned, then all index partitions are marked `UNUSABLE`.

Beginning with Oracle Database 11g Release 2, the database does not create an index segment when creating an unusable index.

The following procedure illustrates how to create unusable indexes and query the database for details about the index.

To create an unusable index:

1. If necessary, create the table to be indexed.
	For example, create a hash-partitioned table called `hr.employees_part` as follows:
	```
	sh@PROD> CONNECT hr
	Enter password: **
	Connected.
	hr@PROD> CREATE TABLE employees_part
	  2    PARTITION BY HASH (employee_id) PARTITIONS 2
	  3    AS SELECT * FROM employees;
	 
	Table created.
	hr@PROD> SELECT COUNT(*) FROM employees_part;
	 
	  COUNT(*)
	----------
	       107
	```
2. Create an index with the keyword `UNUSABLE`.
	The following example creates a locally partitioned index on `employees_part`, naming the index partitions `p1_i_emp_ename` and `p2_i_emp_ename`, and making `p1_i_emp_ename` unusable:
	```
	hr@PROD> CREATE INDEX i_emp_ename ON employees_part (employee_id)
	  2    LOCAL (PARTITION p1_i_emp_ename UNUSABLE, PARTITION p2_i_emp_ename);
	 
	Index created.
	```
3. Optionally, verify that the index is unusable by querying the data dictionary.
	The following example queries the status of index `i_emp_ename` and its two partitions, showing that only partition `p2_i_emp_ename` is unusable:
	```
	hr@PROD> SELECT INDEX_NAME AS "INDEX OR PARTITION NAME", STATUS
	  2  FROM   USER_INDEXES
	  3  WHERE  INDEX_NAME = 'I_EMP_ENAME'
	  4  UNION ALL
	  5  SELECT PARTITION_NAME AS "INDEX OR PARTITION NAME", STATUS
	  6  FROM   USER_IND_PARTITIONS
	  7  WHERE  PARTITION_NAME LIKE '%I_EMP_ENAME%';
	 
	INDEX OR PARTITION NAME        STATUS
	------------------------------ --------
	I_EMP_ENAME                    N/A
	P1_I_EMP_ENAME                 UNUSABLE
	P2_I_EMP_ENAME                 USABLE
	```
4. Optionally, query the data dictionary to determine whether storage exists for the partitions.
	For example, the following query shows that only index partition `p2_i_emp_ename` occupies a segment. Because you created `p1_i_emp_ename` as unusable, the database did not allocate a segment for it.
	```
	hr@PROD> COL PARTITION_NAME FORMAT a14
	hr@PROD> COL SEG_CREATED FORMAT a11
	hr@PROD> SELECT p.PARTITION_NAME, p.STATUS AS "PART_STATUS",
	  2         p.SEGMENT_CREATED AS "SEG_CREATED",   
	  3  FROM   USER_IND_PARTITIONS p, USER_SEGMENTS s
	  4  WHERE  s.SEGMENT_NAME = 'I_EMP_ENAME';
	 
	PARTITION_NAME PART_STA SEG_CREATED 
	-------------- -------- ----------- 
	P2_I_EMP_ENAME USABLE   YES       
	P1_I_EMP_ENAME UNUSABLE NO
	```

See Also:

- "Understand When to Use Unusable or Invisible Indexes"
- "Making an Index Unusable"
- [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_5012.htm#SQLRF54038) for more information on creating unusable indexes, including restrictions.

### Creating an Invisible Index

An invisible index is an index that is ignored by the optimizer unless you explicitly set the `OPTIMIZER_USE_INVISIBLE_INDEXES` initialization parameter to `TRUE` at the session or system level.

To create an invisible index:

- Use the `CREATE INDEX` statement with the `INVISIBLE` keyword.
	The following statement creates an invisible index named `emp_ename` for the `ename` column of the `emp` table:
	```
	CREATE INDEX emp_ename ON emp(ename)
	      TABLESPACE users
	      STORAGE (INITIAL 20K
	      NEXT 20k)
	      INVISIBLE;
	```

See Also:

- "Understand When to Use Unusable or Invisible Indexes"
- "Making an Index Invisible"
- [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_5012.htm#SQLRF01209) for more information on creating invisible indexes

## Altering Indexes

To alter an index, your schema must contain the index or you must have the `ALTER ANY INDEX` system privilege. With the `ALTER INDEX` statement, you can:

- Rebuild or coalesce an existing index
- Deallocate unused space or allocate a new extent
- Specify parallel execution (or not) and alter the degree of parallelism
- Alter storage parameters or physical attributes
- Specify `LOGGING` or `NOLOGGING`
- Enable or disable key compression
- Mark the index unusable
- Make the index invisible
- Rename the index
- Start or stop the monitoring of index usage

You cannot alter index column structure.

More detailed discussions of some of these operations are contained in the following sections:

- Altering Storage Characteristics of an Index
- Rebuilding an Existing Index
- Making an Index Unusable
- Making an Index Invisible
- Monitoring Index Usage

See Also:

- [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_1010.htm#SQLRF00805) for details on the `ALTER` `INDEX` statement

### Altering Storage Characteristics of an Index

Alter the storage parameters of any index, including those created by the database to enforce primary and unique key integrity constraints, using the `ALTER INDEX` statement. For example, the following statement alters the `emp_ename` index:

```
ALTER INDEX emp_ename
     STORAGE (NEXT 40);
```

The parameters `INITIAL` and `MINEXTENTS` cannot be altered. All new settings for the other storage parameters affect only extents subsequently allocated for the index.

For indexes that implement integrity constraints, you can adjust storage parameters by issuing an `ALTER TABLE` statement that includes the `USING INDEX` subclause of the `ENABLE` clause. For example, the following statement changes the storage options of the index created on table `emp` to enforce the primary key constraint:

```
ALTER TABLE emp
     ENABLE PRIMARY KEY USING INDEX;
```

See Also:

[Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_1010.htm#SQLRF00805) for syntax and restrictions on the use of the `ALTER INDEX` statement

### Rebuilding an Existing Index

Before rebuilding an existing index, compare the costs and benefits associated with rebuilding to those associated with coalescing indexes as described in Table 21-1.

When you rebuild an index, you use an existing index as the data source. Creating an index in this manner enables you to change storage characteristics or move to a new tablespace. Rebuilding an index based on an existing data source removes intra-block fragmentation. Compared to dropping the index and using the `CREATE INDEX` statement, rebuilding an existing index offers better performance.

The following statement rebuilds the existing index `emp_name`:

```
ALTER INDEX emp_name REBUILD;
```

The `REBUILD` clause must immediately follow the index name, and precede any other options. It cannot be used with the `DEALLOCATE UNUSED` clause.

You have the option of rebuilding the index online. Rebuilding online enables you to update base tables at the same time that you are rebuilding. The following statement rebuilds the `emp_name` index online:

```
ALTER INDEX emp_name REBUILD ONLINE;
```

To rebuild an index in a different user's schema online, the following additional system privileges are required:

- `CREATE ANY TABLE`
- `CREATE ANY INDEX`

Note:

Online index rebuilding has stricter limitations on the maximum key length that can be handled, compared to other methods of rebuilding an index. If an ORA-1450 (maximum key length exceeded) error occurs when rebuilding online, try rebuilding offline, coalescing, or dropping and re-creating the index.

If you do not have the space required to rebuild an index, you can choose instead to coalesce the index. Coalescing an index is an online operation.

See Also:

- "Creating an Index Online"
- "Monitoring Space Use of Indexes"

### Making an Index Unusable

When you make an index unusable, it is ignored by the optimizer and is not maintained by DML. When you make one partition of a partitioned index unusable, the other partitions of the index remain valid.

You must rebuild or drop and re-create an unusable index or index partition before using it.

The following procedure illustrates how to make an index and index partition unusable, and how to query the object status.

To make an index unusable:

1. Query the data dictionary to determine whether an existing index or index partition is usable or unusable.
	For example, issue the following query (output truncated to save space):
	```
	hr@PROD> SELECT INDEX_NAME AS "INDEX OR PART NAME", STATUS, SEGMENT_CREATED
	  2  FROM   USER_INDEXES
	  3  UNION ALL
	  4  SELECT PARTITION_NAME AS "INDEX OR PART NAME", STATUS, SEGMENT_CREATED
	  5  FROM   USER_IND_PARTITIONS;
	 
	INDEX OR PART NAME             STATUS   SEG
	------------------------------ -------- ---
	I_EMP_ENAME                    N/A      N/A
	JHIST_EMP_ID_ST_DATE_PK        VALID    YES
	JHIST_JOB_IX                   VALID    YES
	JHIST_EMPLOYEE_IX              VALID    YES
	JHIST_DEPARTMENT_IX            VALID    YES
	EMP_EMAIL_UK                   VALID    NO
	.
	.
	.
	COUNTRY_C_ID_PK                VALID    YES
	REG_ID_PK                      VALID    YES
	P2_I_EMP_ENAME                 USABLE   YES
	P1_I_EMP_ENAME                 UNUSABLE NO
	 
	22 rows selected.
	```
	The preceding output shows that only index partition `p1_i_emp_ename` is unusable.
2. Make an index or index partition unusable by specifying the `UNUSABLE` keyword.
	The following example makes index `emp_email_uk` unusable:
	```
	hr@PROD> ALTER INDEX emp_email_uk UNUSABLE;
	 
	Index altered.
	```
	The following example makes index partition `p2_i_emp_ename` unusable:
	```
	hr@PROD> ALTER INDEX i_emp_ename MODIFY PARTITION p2_i_emp_ename UNUSABLE;
	 
	Index altered.
	```
3. Optionally, query the data dictionary to verify the status change.
	For example, issue the following query (output truncated to save space):
	```
	hr@PROD> SELECT INDEX_NAME AS "INDEX OR PARTITION NAME", STATUS, 
	  2  SEGMENT_CREATED
	  3  FROM   USER_INDEXES
	  4  UNION ALL
	  5  SELECT PARTITION_NAME AS "INDEX OR PARTITION NAME", STATUS, 
	  6  SEGMENT_CREATED
	  7  FROM   USER_IND_PARTITIONS;
	 
	INDEX OR PARTITION NAME        STATUS   SEG
	------------------------------ -------- ---
	I_EMP_ENAME                    N/A      N/A
	JHIST_EMP_ID_ST_DATE_PK        VALID    YES
	JHIST_JOB_IX                   VALID    YES
	JHIST_EMPLOYEE_IX              VALID    YES
	JHIST_DEPARTMENT_IX            VALID    YES
	EMP_EMAIL_UK                   UNUSABLE NO
	.
	.
	.
	COUNTRY_C_ID_PK                VALID    YES
	REG_ID_PK                      VALID    YES
	P2_I_EMP_ENAME                 UNUSABLE NO
	P1_I_EMP_ENAME                 UNUSABLE NO
	 
	22 rows selected.
	```
	A query of space consumed by the `i_emp_ename` and `emp_email_uk` segments shows that the segments no longer exist:
	```
	hr@PROD> SELECT SEGMENT_NAME, BYTES
	  2  FROM   USER_SEGMENTS
	  3  WHERE  SEGMENT_NAME IN ('I_EMP_ENAME', 'EMP_EMAIL_UK');
	 
	no rows selected
	```

See Also:

- "Understand When to Use Unusable or Invisible Indexes"
- "Creating an Unusable Index"
- [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_5012.htm#SQLRF54038) for more information about the `UNUSABLE` keyword, including restrictions

### Making an Index Invisible

An invisible index is ignored by the optimizer unless you explicitly set the `OPTIMIZER_USE_INVISIBLE_INDEXES` initialization parameter to `TRUE` at the session or system level. Making an index invisible is an alternative to making it unusable or dropping it. You cannot make an individual index partition invisible. Attempting to do so produces an error.

To make an index invisible:

- Submit the following SQL statement:
	```
	ALTER INDEX index INVISIBLE;
	```

To make an invisible index visible again:

- Submit the following SQL statement:
	```
	ALTER INDEX index VISIBLE;
	```

To determine whether an index is visible or invisible:

- Query the dictionary views `USER_INDEXES`, `ALL_INDEXES`, or `DBA_INDEXES`.
	For example, to determine if the index `ind1` is invisible, issue the following query:
	```
	SELECT INDEX_NAME, VISIBILITY FROM USER_INDEXES
	   WHERE INDEX_NAME = 'IND1';
	INDEX_NAME   VISIBILITY
	----------   ----------
	IND1         VISIBLE
	```

### Renaming an Index

To rename an index, issue this statement:

```
ALTER INDEX index_name RENAME TO new_name;
```

### Monitoring Index Usage

Oracle Database provides a means of monitoring indexes to determine whether they are being used. If an index is not being used, then it can be dropped, eliminating unnecessary statement overhead.

To start monitoring the usage of an index, issue this statement:

```
ALTER INDEX index MONITORING USAGE;
```

Later, issue the following statement to stop the monitoring:

```
ALTER INDEX index NOMONITORING USAGE;
```

The view `V$OBJECT_USAGE` can be queried for the index being monitored to see if the index has been used. The view contains a `USED` column whose value is `YES` or `NO`, depending upon if the index has been used within the time period being monitored. The view also contains the start and stop times of the monitoring period, and a `MONITORING` column (`YES` / `NO`) to indicate if usage monitoring is currently active.

Each time that you specify `MONITORING USAGE`, the `V$OBJECT_USAGE` view is reset for the specified index. The previous usage information is cleared or reset, and a new start time is recorded. When you specify `NOMONITORING USAGE`, no further monitoring is performed, and the end time is recorded for the monitoring period. Until the next `ALTER INDEX...MONITORING USAGE` statement is issued, the view information is left unchanged.

## Monitoring Space Use of Indexes

If key values in an index are inserted, updated, and deleted frequently, the index can lose its acquired space efficiency over time. Monitor index efficiency of space usage at regular intervals by first analyzing the index structure, using the `ANALYZE INDEX...VALIDATE STRUCTURE` statement, and then querying the `INDEX_STATS` view:

```
SELECT PCT_USED FROM INDEX_STATS WHERE NAME = 'index';
```

The percentage of index space usage varies according to how often index keys are inserted, updated, or deleted. Develop a history of average efficiency of space usage for an index by performing the following sequence of operations several times:

- Analyzing statistics
- Validating the index
- Checking `PCT_USED`
- Dropping and rebuilding (or coalescing) the index

When you find that index space usage drops below its average, you can condense the index space by dropping the index and rebuilding it, or coalescing it.

See Also:

["Analyzing Tables, Indexes, and Clusters"](general.md)

## Dropping Indexes

To drop an index, the index must be contained in your schema, or you must have the `DROP ANY INDEX` system privilege.

Some reasons for dropping an index include:

- The index is no longer required.
- The index is not providing anticipated performance improvements for queries issued against the associated table. For example, the table might be very small, or there might be many rows in the table but very few index entries.
- Applications do not use the index to query the data.
- The index has become invalid and must be dropped before being rebuilt.
- The index has become too fragmented and must be dropped before being rebuilt.

When you drop an index, all extents of the index segment are returned to the containing tablespace and become available for other objects in the tablespace.

How you drop an index depends on whether you created the index explicitly with a `CREATE INDEX` statement, or implicitly by defining a key constraint on a table. If you created the index explicitly with the `CREATE INDEX` statement, then you can drop the index with the `DROP INDEX` statement. The following statement drops the `emp_ename` index:

```
DROP INDEX emp_ename;
```

You cannot drop only the index associated with an enabled `UNIQUE` key or `PRIMARY KEY` constraint. To drop a constraints associated index, you must disable or drop the constraint itself.

Note:

If a table is dropped, all associated indexes are dropped automatically.

See Also:

- [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_8017.htm#SQLRF01510) for syntax and restrictions on the use of the `DROP INDEX` statement
- ["Managing Integrity Constraints"](general.md)
- "Making an Index Invisible" for an alternative to dropping indexes

## Indexes Data Dictionary Views

The following views display information about indexes:

| View | Description |
| --- | --- |
| `DBA_INDEXES`  `ALL_INDEXES`  `USER_INDEXES` | `DBA` view describes indexes on all tables in the database. `ALL` view describes indexes on all tables accessible to the user. `USER` view is restricted to indexes owned by the user. Some columns in these views contain statistics that are generated by the `DBMS_STATS` package or `ANALYZE` statement. |
| `DBA_IND_COLUMNS`  `ALL_IND_COLUMNS`  `USER_IND_COLUMNS` | These views describe the columns of indexes on tables. Some columns in these views contain statistics that are generated by the `DBMS_STATS` package or `ANALYZE` statement. |
| `DBA_IND_EXPRESSIONS`  `ALL_IND_EXPRESSIONS`  `USER_IND_EXPRESSIONS` | These views describe the expressions of function-based indexes on tables. |
| `DBA_IND_PARTITIONS`  `ALL_IND_PARTITIONS`  `USER_IND_PARTITIONS` | These views display, for each index partition, the partition-level partitioning information, the storage parameters for the partition, and various partition statistics that are generated by the `DBMS_STATS` package. |
| `DBA_IND_STATISTICS`  `ALL_IND_STATISTICS`  `USER_IND_STATISTICS` | These views contain optimizer statistics for indexes. |
| `INDEX_STATS` | Stores information from the last `ANALYZE INDEX...VALIDATE STRUCTURE` statement. |
| `INDEX_HISTOGRAM` | Stores information from the last `ANALYZE INDEX...VALIDATE STRUCTURE` statement. |
| `V$OBJECT_USAGE` | Contains index usage information produced by the `ALTER INDEX...MONITORING USAGE` functionality. |

See Also:

[Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/toc.htm) for a complete description of these views