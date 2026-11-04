---
title: User-Managed Local Domain Indexes
book: "Data Cartridge Developer's Guide"
doc_id: E10765-02
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e10765/user_man_idx_apnd.htm
tags:
  - oracle
  - 11g
  - data-cartridge-developers-guide
---

## A User-Managed Local Domain Indexes

The user-managed approach for partitioning domain indexes has been the only method available until Oracle Database 11g Release 1, when system-managed partitioning was introduced. The user-managed approach has three significant limitations:

- Because the extensible indexing framework does not store information about the domain index related objects in the kernel, you must maintain tables and partitions by invoking user-supplied routines.
- Because the kernel does not support equipartitioned tables, each partition has to have a set of tables and dependent schema objects, which must be managed programmatically in the user-managed indexing code.
	As the number of partitions increases, the proliferation of domain index storage objects can become an obstacle to efficient operation. To use a table that contains images and has 1,000 partitions, an indexing schema that creates 64 bitmap indexes on its storage table (after it is extended to support local domain indexes) would need create and manage 1,000 domain index storage tables and 64,000 bitmap indexes.
- During DML and query processing with local domain indexes, you would need a separate set of cursors for each partition; this is required because each partition has its own set of tables. As a consequence, applications that use a large number of partitions and require access to several partitions simultaneously must compile new SQL cursors at run-time, which impacts performance.

Oracle recommends that you use the system-managed approach, as described in [Chapter 8, "Building Domain Indexes"](dom_idx.md).

Oracle plans to deprecate the user-managed approach in a future release. Information provided in this appendix documents the specific differences between the user-managed and system managed processes and APIs.

## Comparing User-Managed and System-Managed Domain Indexes

An alternative approach would be to use system-managed domain indexes. It addresses these limitations and has the following benefits:

- Because the kernel performs many more maintenance tasks on behalf of the user, there is no need for programmatic support for table and partition maintenance operations. These operations can be implemented by taking actions in the server and by using a very minimal set of interface routines. The cartridge code can then be relatively unaware of partition issues.
- The number of objects that must be managed to support local partitioned domain indexes is identical to the number for non-partitioned domain indexes. For local partitioned indexes, the domain index storage tables are equipartitioned with respect to the base tables; therefore, the number of domain index storage tables does not increase with an increase in the number of partitions.
- A single set of query and DML statements can now access and manipulate the system-partitioned storage tables, facilitating cursor sharing and enhancing performance.

## Truncating Domain Indexes

There is no explicit statement for truncating a domain index. However, when the corresponding table is truncated, your indextype's truncate method is invoked. For example:

```
TRUNCATE TABLE MyEmployees;
```

truncates `ResumeTextIndex` by calling your ODCIIndexTruncate() method.

## Creating Indextypes

Use the following syntax to create indextypes for the user-managed domain indexes.

```
CREATE INDEXTYPE TextIndexType
FOR Contains (VARCHAR2, VARCHAR2)
USING TextIndexMethods;
```

## Using Domain Indexes for the Indextype

In order for the indextype to be able to use local domain indexes, the methods have to be declared when the indextype is created:

```
CREATE INDEXTYPE TextIndexType
  FOR Contains (VARCHAR2, VARCHAR2)
  USING TextIndexMethods
  WITH LOCAL RANGE PARTITION;
```

## Partitioning Domain Indexes

The user-managed approach uses the methods ODCIIndexMergePartition() and ODCIIndexSplitPartition() to support local domain indexes.

## APIs for User-Managed Domain Indexes

The following methods are used only in the user-managed implementation of domain indexes.

### ODCIIndexTruncate()

This is an index definition method. When a user issues a `TRUNCATE` statement against a table that contains a column or object type attribute indexed by your indextype, Oracle calls your ODCIIndexTruncate() method. This method should leave the domain index empty.

Syntax

```
FUNCTION ODCIIndexTruncate(
   ia ODCIIndexInfo, 
   env ODCIEnv) 
RETURN NUMBER
```

| Parameter | Description |
| --- | --- |
| ``` ia ``` | Contains information about the indexed column |
| ``` env ``` | The environment handle passed to the routine |

Returns

`ODCIConst.Success` on success, or `ODCIConst.Error` on error, or `ODCIConst.Warning`.

While truncating a local domain index, the first N+1 calls can return `ODCIConst.ErrContinue` too.

Usage Notes

- This function should be implemented as a static type method.
- After this function executes, the domain index should be empty (corresponding to the empty base table).
- While the ODCIIndexTruncate() routine is being executed, the domain index is marked `LOADING`. If the ODCIIndexTruncate() routine returns with an `ODCIConst`.`Error` (or exception), the domain index is marked `FAILED`. The only operation permitted on `FAILED` domain indexes is `DROP` `INDEX`, `TRUNCATE` `TABLE` or `ALTER` `INDEX` `REBUILD`. If ODCIIndexTruncate() returns with `ODCIConst`.`Warning`, the operation succeeds but a warning message is returned to the user.
- Every SQL statement executed by ODCIIndexTruncate() is treated as an independent operation. The changes made by ODCIIndexTruncate() are not guaranteed to be atomic.
- This method is invoked for truncating a non-partitioned index, truncating a local domain index, and also for truncating a single index partition during `ALTER TABLE TRUNCATE PARTITION`.
	For truncating a non-partitioned index, the ODCIIndexTruncate() is invoked with the `IndexPartition`, `TablePartition` and `callProperty` set to `NULL`.
	For truncating a local domain index, the routine is invoked N+2 times, where N is the number of partitions.
	For truncating a single index partition during `ALTER TABLE TRUNCATE PARTITION`, this routine is invoked with the `IndexPartition` and the `TablePartition` filled in and the `callProperty` set to `NULL`.

### ODCIIndexMergePartition()

Invoked when a `ALTER TABLE MERGE PARTITION` is issued on range partitioned table on which a domain index is defined.

Syntax

```
FUNCTION ODCIIndexMergePartition(
   ia ODCIIndexInfo, 
   part_name1 ODCIPartInfo, 
   part_name2 ODCIPartInfo, 
   parms VARCHAR2, 
   env ODCIEnv) 
RETURN NUMBER
```

| Parameter | Description |
| --- | --- |
| ``` ia ``` | Contains index and table partition name for one of the partitions to be merged |
| ``` part_name1 ``` | Contains index and table partition name for the second partition to be merged |
| ``` part_name2 ``` | Holds index and table partition name for the new merged partition |
| ``` parms ``` | Contains the parameter string for the resultant merged partition, essentially the default parameter string associated with the index. |
| ``` env ``` | The environment handle passed to the routine |

Returns

`ODCIConst.Success` on success, or `ODCIConst.Error` on error, or `ODCIConst.Warning`.

Usage Notes

- The function should be implemented as a static type method.
- You should create a new table representing the resultant merged partition and populate it with data from the merged partitions. Then drop the tables corresponding to the merged index partitions.
- The newly created partition should pick the default parameter string associated with the index level. Resulting local index partitions are marked `UNUSABLE`; you should not attempt to populate the data in the new partition until after an `ALTER INDEX REBUILD PARTITION` call.
- The old table and the dictionary entries for the old index partitions are deleted before the call to ODCIIndexMergePartition(), so the cartridge code for this routine should not rely on the existence of this data in the views.

### ODCIIndexSplitPartition()

Invoked when an `ALTER TABLE SPLIT PARTITION` is invoked on a partitioned table where a domain index is defined.

Syntax

```
FUNCTION ODCIIndexSplitPartition(
   ia ODCIIndexInfo, 
   part_name1 ODCIPartInfo, 
   part_name2 ODCIPartInfo, 
   parms VARCHAR2, 
   env ODCIEnv) 
RETURN NUMBER
```

| Parameter | Description |
| --- | --- |
| ``` ia ``` | Contains the information about the partition to be split |
| ``` part_name1 ``` | Holds the index and table partition names for one of the new partitions |
| ``` part_name2 ``` | Holds the index and table partition names for the other new partition |
| ``` parms ``` | Contains the parameter string for the new partitions, the string associated with the index partition that is being split. |
| ``` env ``` | The environment handle passed to the routine |

Returns

`ODCIConst.Success` on success, or `ODCIConst.Error` on error, or `ODCIConst.Warning`.

Usage Notes

- The function should be implemented as a static type method.
- You must to drop the metadata corresponding to the partition that is split, and create metadata for the two newly created partitions.
- The new tables should pick up the default parameter string associated with the split partition.
- The index data corresponding to these partitions need not be computed since the indexes are marked `UNUSABLE`. The indexes can be built after an `ALTER INDEX REBUILD PARTITION` call makes the indexes usable again.
- The old table and the old index partition's dictionary entries are deleted before the call to ODCIIndexSplitPartition(), so the cartridge code for this routine should not rely on the existence of this data in the views.