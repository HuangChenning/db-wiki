---
title: Extensible Indexing Interface
book: "Data Cartridge Developer's Guide"
doc_id: E10765-02
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e10765/ext_idx_ref.htm
tags:
  - oracle
  - 11g
  - data-cartridge-developers-guide
---

## 20 Extensible Indexing Interface

This chapter describes Oracle Data Cartridge Interface extensible indexing interfaces. This chapter contains this topic:

- Extensible Indexing - System-Defined Interface Routines

## Extensible Indexing - System-Defined Interface Routines

Table 20-1 summarizes the extensible indexing routines.

Caution:

These routines are invoked by Oracle at the appropriate times based on SQL statements executed by the end user. Do not invoke these routines directly as this may result in corruption of index data.

Table 20-1 Summary of System-Defined Extensible Indexing Interface Routines

| Routine | Description |
| --- | --- |
| ODCIGetInterfaces() | Invoked when an `INDEXTYPE` is created by a `CREATE` `INDEXTYPE...` statement or is altered. |
| ODCIIndexAlter() | Invoked when a domain index or a domain index partition is altered using an `ALTER INDEX`, an `ALTER INDEX PARTITION`, a `TRUNCATE TABLE`, a `RENAME TABLE`, an `ALTER TABLE RENAME COLUMN`, or an `ALTER TABLE [ADD\|TRUNCATE\|SPLIT\|MERGE] PARTITION` statement. |
| ODCIIndexClose() | Invoked to end the processing of an operator. |
| ODCIIndexCreate() | Invoked when a domain index is created by a `CREATE INDEX...INDEXTYPE IS...PARAMETERS...` statement issued by the user. |
| ODCIIndexDelete() | Invoked when a row is deleted from a table that has a domain index defined on one or more of its columns. |
| ODCIIndexDrop() | Invoked when a domain index is dropped explicitly using a `DROP` `INDEX` statement, or implicitly through a `DROP` `TABLE` or `DROP` `USER` statement. |
| ODCIIndexExchangePartition() | Invoked when an `ALTER TABLE EXCHANGE PARTITION...INCLUDING INDEXES` is issued on a partitioned table on which a local domain index is defined. |
| ODCIIndexFetch() | Invoked repeatedly to retrieve the rows satisfying the operator predicate. |
| ODCIIndexGetMetadata() | Returns a series of strings of PL/SQL code that comprise the non-dictionary metadata associated with the index. |
| ODCIIndexInsert() | Invoked when a row or a set of rows is inserted into a table that has a domain index defined on one or more of its columns. |
| ODCIIndexStart() | Invoked to start the evaluation of an operator on an indexed column. |
| ODCIIndexUpdate() | Invoked when a row is updated in a table and the updated column has a domain index defined on. |
| ODCIIndexUpdPartMetadata() | Invoked during partition maintenance operations. Patches the indextype metadata tables to correctly reflect the partition maintenance operation. |
| ODCIIndexUtilCleanup() | Cleans up temporary states created by ODCIIndexUtilGetTableNames(). |
| ODCIIndexUtilGetTableNames() | IDetermines if the secondary tables storing the index data should be transported. |

### ODCIGetInterfaces()

Invoked when an `INDEXTYPE` is created by a `CREATE` `INDEXTYPE...` statement or is altered.

Syntax

```
FUNCTION ODCIGetInterfaces(
   ifclist OUT ODCIObjectList)
RETURN NUMBER
```

| Parameter | Description |
| --- | --- |
| ``` ifclist ``` | Contains information about the interfaces it supports |

Returns

`ODCIConst.Success` on success or `ODCIConst.Error` on error

Usage Notes

This function should be implemented as a static type method.

This function must return `SYS.ODCIINDEX2` in the `ODCIObjectList` if the indextype uses the second version of the `ODCIIndex` interface, which was implemented in the current version of the Oracle Database and is described in this book.

### ODCIIndexAlter()

Invoked when a domain index or a domain index partition is altered using one of the following methods:

- `ALTER INDEX`
- `ALTER INDEX PARTITION`
- `TRUNCATE TABLE` `table_name`
- `RENAME TABLE`
- `ALTER TABLE...[ADD|TRUNCATE|SPLIT|MERGE]...PARTITION`
- `ALTER TABLE RENAME`
- `ALTER TABLE RENAME COLUMN`

To populate the index partitions when creating local domain indexes, this method is invoked for each partition of the base table.

Syntax

```
STATIC FUNCTION ODCIIndexAlter(
   ia ODCIIndexInfo, 
   parms IN OUT VARCHAR2, 
   alter_option NUMBER, 
   env ODCIEnv) 
RETURN NUMBER
```

| Parameter | Description |
| --- | --- |
| ``` ia ``` | Contains information about the index and the indexed column |
| ``` parms (IN) ``` | Parameter string - With `ALTER` `INDEX` `PARAMETERS` or `ALTER` `INDEX` `REBUILD`, contains the user specified parameter string - With `ALTER` `INDEX` `RENAME`, contains the new name of the domain index - With `ALTER TABLE RENAME COLUMN`, contains the new domain-indexed column name - With `ALTER TABLE RENAME or RENAME TABLE`, contains the new table name |
| ``` parms (OUT) ``` | Parameter string  Valid only with `ALTER` `INDEX` `PARAMETERS` or `ALTER` `INDEX` `REBUILD`; contains the resultant string to be stored in system catalogs |
| ``` alter_option ``` | Specifies one of the following options: - `AlterIndexNone` if `ALTER INDEX [PARTITION] PARAMETERS` - `AlterIndexRename` if `ALTER INDEX RENAME [PARTITION]` - `AlterIndexRebuild` if `ALTER INDEX REBUILD [PARTITION] [PARAMETERS]` - `AlterIndexRenameCol` if `ALTER TABLE RENAME COLUMN` - `AlterIndexRenameTab` if `ALTER TABLE RENAME` or `RENAME TABLE` - `AlterIndexUpdBlockRefs` if `ALTER TABLE UPDATE BLOCK REFERENCES` - `AlterIndexMigrate` if `ALTER INDEX COMPILE` when the domain index is user-managed, but its indextype is system-managed |
| ``` env ``` | The environment handle passed to the routine |

Returns

`ODCIConst.Success` on success, `ODCIConst.Error` on error, or `ODCIConst.Warning` otherwise. When invoked to rebuild local index partitions, may also return `ODCIConst.ErrContinue`.

Usage Notes

- This function should be implemented as a static type method.
- An `ALTER` `INDEX` statement can be invoked for domain indexes in multiple ways.
	```
	ALTER INDEX index_name
	PARAMETERS (parms);
	```
	or
	```
	ALTER INDEX index_name
	REBUILD PARAMETERS (parms);
	```
	The precise behavior in these two cases is defined by the implementation. One possibility is that the first statement would merely reorganize the index based on the parameters while the second would rebuild it from scratch.
- The maximum length of the input parameters string is 1000 characters. The `OUT` value of the `parms` argument can be set to resultant parameters string to be stored in the system catalogs.
- The `ALTER` `INDEX` statement can also be used to rename a domain index in the following way:
	```
	ALTER INDEX index_name
	RENAME TO new_index_name
	```
- When the name of the table on which a domain index is created changes, ODCIIndexAlter() is invoked with `alter_option=AlterIndexRenameTab`, and `new_table_name` is passed to the `parms` argument:
	```
	ALTER TABLE table_name 
	RENAME new_table_name
	```
	or
	```
	RENAME table_name 
	TO new_table_name
	```
- When the name of the column on which a domain index is created changes, ODCIIndexAlter() is invoked with `alter_option=AlterIndexRenameCol`, and `new_column_name` is passed to the `parms` argument:
	```
	ALTER TABLE table_name 
	RENAME COLUMN column_name 
	TO new_column_name
	```
- If the `PARALLEL` clause is omitted, then the domain index or local domain index partition is rebuilt sequentially.
- If the `PARALLEL` clause is specified, the parallel degree is passed to the ODCIIndexAlter() invocation in the `IndexParaDegree` attribute of `ODCIIndexInfo`, and the `Parallel` bit of the `IndexInfoFlags` attribute is set. The parallel degree is determined as follows:
	- If `PARALLEL DEGREE` deg is specified, deg is passed.
		- If only `PARALLEL` is specified, then a constant is passed to indicate that the default degree of parallelism was specified.
- If the `ODCIIndexAlter` routine returns with the `ODCIConst`.`Success`, the index is valid and usable. If the ODCIIndexAlter() routine returns with `ODCIConst`.`Warning`, the index is valid and usable but a warning message is returned to the user. If ODCIIndexAlter() returns with an error (or exception), the domain index is marked `FAILED`.
- When the ODCIIndexAlter() routine is being executed, the domain index is marked `LOADING`.
- Every SQL statement executed by ODCIIndexAlter() is treated as an independent operation. The changes made by ODCIIndexCreate() are not guaranteed to be atomic.
- The `AlterIndexUpdBlockRefs` alter option applies only to domain indexes on index-organized tables. When the end user executes an `ALTER INDEX` `domain_index` `UPDATE BLOCK REFERENCES`, ODCIIndexAlter() is called with the `AlterIndexUpdBlockRefs` bit set to give the cartridge developer the opportunity to update guesses as to the block locations of rows, stored in logical rowids.
- The `AlterIndexMigrate` alter options applies only to migration of user-managed domain indexes to system-managed domain indexes. When the user-managed domain index is marked `INVALID`, but its indextype is system-managed, you must make an `ALTER INDEX` `domain_index` `COMPILE` call to re-validate the domain index. This calls the ODCIIndexAlter() method with `alter_option=AlterIndexMigrate`, to allow an opportunity to migrate the domain index to the system-managed approach.

### ODCIIndexClose()

Invoked to end the processing of an operator.

Syntax

```
FUNCTION ODCIIndexClose(
   self IN impltype, 
   env ODCIEnv) 
RETURN NUMBER
```

| Parameter | Description |
| --- | --- |
| ``` self(IN) ``` | Is the value of the context returned by the previous invocation of ODCIIndexFetch() |
| ``` env ``` | The environment handle passed to the routine |

Returns

- `ODCIConst.Success` on success
- `ODCIConst.Error` on error

Usage Notes

The index implementor can perform any appropriate actions to finish up the processing of an domain index scan, such as freeing memory and other resources.

### ODCIIndexCreate()

Invoked when a domain index is created by a `CREATE INDEX...INDEXTYPE IS...PARAMETERS...` statement issued by the user. The domain index can be either a non-partitioned index or a local partitioned domain index. The local partitioned domain index can be created in either a system- or a user-managed scheme.

Syntax

```
FUNCTION ODCIIndexCreate(
   ia ODCIIndexInfo, 
   parms VARCHAR2, 
   env ODCIEnv)
RETURN NUMBER
```

| Parameter | Description |
| --- | --- |
| ``` ia ``` | Contains information about the index and the indexed column |
| ``` parms ``` | The `PARAMETERS` string passed in not interpreted by Oracle. The maximum size of the parameter string is `1,000` characters. |
| ``` env ``` | The environment handle passed to the routine |

Returns

`ODCIConst.Success`, `ODCIConst.Error`, `ODCIConst.Warning`, `ODCIConst.ErrContinue` if the method is invoked at the partition level for creation of a local partitioned index, to continue to the next partition even in case of an error, or `ODCIConst.Fatal` to signify that all dictionary entries for the index are cleaned up and that the `CREATE INDEX` operation is rolled back. Returning this status code assumes that the cartridge code has not created any objects (or cleaned up any objects created).

Usage Notes

- This function should be implemented as a `STATIC` type method.
- Creates objects (such as tables) to store the index data, generate the index data, and store the data in the index data tables.
- This procedure should handle creation of indexes on both empty and non-empty tables. If the base table is not empty, the procedure can scan the entire table and generate index data.
- When the ODCIIndexCreate() routine is running, the domain index is marked `LOADING`.
- Every SQL statement executed by ODCIIndexCreate() is treated as an independent operation. The changes made by ODCIIndexCreate() are not guaranteed to be atomic.
- To create a non-partitioned domain index, the ODCIIndexCreate() method is invoked, and the only valid return codes are `ODCIConst.Success`, `ODCIConst.Warning`, `ODCIConst.Error`, or `ODCIConst.Fatal`. If the operation returns `ODCIConst.Fatal`, the `CREATE INDEX` statement is rolled back by the server.
- In a non-partitioned domain index, the `IndexPartition`, `TablePartition` name, and the `callProperty` should be `NULL`.
- For a non-partitioned domain index, the parallel degree is passed to the ODCIIndexCreate() invocation in the `IndexParaDegree` attribute of `ODCIIndexInfo`, and the `Parallel` bit of the `IndexInfoFlags` is set. The parallel degree is determined as follows:
	- If `PARALLEL DEGREE` `deg` is specified, `deg` is passed.
		- If only `PARALLEL` is specified, then a constant indicating that the default degree of parallelism was specified, is passed.
		- If the `PARALLEL` clause is omitted entirely, the operation is performed sequentially.
- If the ODCIIndexCreate() routine returns with the `ODCIConst`.`Success`, the index is valid and usable. If the ODCIIndexCreate() routine returns with `ODCIConst`.`Warning`, the index is valid and usable but a warning message is returned to the user. If the ODCIIndexCreate() routine returns with an `ODCIConst`.`Error` (or exception), the domain index is marked `FAILED.`
- The only operations permitted on `FAILED` domain indexes is `DROP` `INDEX`, `TRUNCATE` `TABLE` or `ALTER` `INDEX` `REBUILD`.
- If a domain index is created on an column of object type which contains a `REF` attribute, do not dereference the `REF` s while building your index. Dereferencing a `REF` fetches data from a different table instance. If the data in the other table is modified, the domain index becomes incorrect. Note that the user is not notified.
- The ODCIIndexCreate() method is invoked twice for the creation of system managed local domain indexes and the only valid return codes are `ODCIConst.Success`, `ODCIConst.Warning` or `ODCIConst.Error`. `ODCIConst.Fatal` can be returned by the first call and results in the `CREATE INDEX` statement being rolled back by the server. The number of partitions is passed in as an argument `ODCIIndexInfo.IndexPartitionTotal`. The first call should create all the index storage tables. All the index storage tables should preferably be system partitioned to get the benefits of local domain indexes. Also:
	- These tables must have the same number of partitions as the base table
		- The users should generate the create table statement with both object and partition level attributes
- Note that the object level create routine only passes in the object level parameter string. However, to construct the storage attributes for all the partitions, it needs the partition level parameter strings. The cartridge indexing code must obtain them by querying the `*_ind_partitions` views on the dictionary tables. The system partitioned tables should not be populated in this phase. The user should wait for the subsequent calls ODCIIndexAlter() to populate the partitions. Also, it is recommended that the users should derive the names of the storage tables and its partitions from the index name and the index partition names. In this case, the user should fetch the index partition names from the `*_ind_partitions` view and construct the partition names for the storage table.
- In the second ODCIIndexCreate() call, the user can create domain index storage table dependent objects, such as indexes, constraints, and triggers. These can be created as before by directly using the SQL callbacks. However, for system partitioned storage tables, the following types of indexes are disallowed:
	- non-partitioned index
		- globally partitioned index
- Sequence numbers and synonyms can be created using callbacks and they are assumed to be partition-independent. The set of objects created for non-partitioned domain index is identical to that of a local partitioned index and these objects are not impacted when a table or partition maintenance operation is done. It is the users responsibility to drop these objects when the index is dropped.
- Other (transient) objects needed for temporary use can be created using callbacks as before. It is the responsibility of user-supplied code to drop them by the end of the create call.
- Temporary tables can be created for holding intermediate data. The server does not perform maintenance operations on these tables.
- External Objects, such as files, can be created for temporary use.
- All the tables left after the invocation of ODCIIndexCreate() or ODCIIndexAlter() are supposed to be system-managed, and the server takes appropriate actions on them during drop, truncate, or the partition maintenance operations.
- Since this routine handles multiple things, such as creation of a non-partitioned index or creation of a local index, you must take special care to code it appropriately.

### ODCIIndexDelete()

Invoked when a row is deleted from a table that has a domain index defined on one or more of its columns.

Syntax

```
FUNCTION ODCIIndexDelete(
   ia ODCIIndexInfo, 
   rid VARCHAR2, 
   oldval icoltype, 
   env ODCIEnv) 
RETURN NUMBER
```

| Parameter | Description |
| --- | --- |
| ``` ia ``` | Contains information about the index and the indexed column |
| ``` rid ``` | The row identifier of the deleted row |
| ``` oldval ``` | The value of the indexed column in the deleted row. The data type is identical to that of the indexed column. |
| ``` env ``` | The environment handle passed to the routine |

Returns

`ODCIConst.Success` on success, or `ODCIConst.Error` on error.

Usage Notes

- This function should be implemented as a `STATIC` type method.
- This method should delete index data corresponding to the deleted row from the appropriate tables or files storing index data.
- Note that the index partition object identifier `ODCIIndexInfo.IndexPartitionIden` and the base table partition physical identifier `ODCIIndexInfo.IndexCols(1).TablePartitionIden` is passed in for local domain index. The indextype must use the new DML syntax using the partition number and the provided `SYS_OP_DOBJTOPNUM` function to delete data from the storage system partitioned table:
	```
	DELETE FROM SP PARTITION (
	   SYS_OP_DOBJTOPNUM(
	       base_table_name,
	      :tab_physical_partid))
	   VALUES(…) 
	   WHERE rowid = :rowid;
	```

### ODCIIndexDrop()

The ODCIIndexDrop() procedure is invoked when a domain index is dropped explicitly using a `DROP` `INDEX` statement, or implicitly through a `DROP` `TABLE` or `DROP` `USER` statement.

Syntax

```
FUNCTION ODCIIndexDrop(
   ia ODCIIndexInfo, 
   env ODCIEnv) 
RETURN NUMBER
```

| Parameter | Description |
| --- | --- |
| ``` ia ``` | Contains information about the index and the indexed column |
| ``` env ``` | The environment handle passed to the routine |

Returns

`ODCIConst.Success` on success, or `ODCIConst.Error` on error, or `ODCIConst.Warning`.

Usage Notes

- This method should be implemented as a static type method.
- This method should drop the tables storing the domain index data.
- For both a non-partitioned domain index and system managed local domain index, the ODCIIndexDrop() method is invoked only one time. The user need not drop the index storage tables if the system-managed approach is used. This is done automatically by the kernel after the call is completed.
- Since it is possible that the domain index is marked `FAILED` (due to abnormal termination of some DDL routine), the ODCIIndexDrop() routine should be capable of cleaning up partially created domain indexes. When the ODCIIndexDrop() routine is being executed, the domain index is marked `LOADING`.
- Note that if the ODCIIndexDrop() routine returns with an `ODCIConst.Error` or exception, the `DROP` `INDEX` statement fails and the index is marked `FAILED`. In that case, there is no mechanism to get rid of the domain index except by using the `FORCE` option. If the ODCIIndexDrop() routine returns with `ODCIConst`.`Warning` in the case of an explicit `DROP` `INDEX` statement, the operation succeeds but a warning message is returned to the user.
- Every SQL statement executed by ODCIIndexDrop() is treated as an independent operation. The changes made by ODCIIndexDrop() are not guaranteed to be atomic.
- For both a non-partitioned domain index and system managed local domain index, the ODCIIndexDrop() method is invoked only one time. With the system-managed approach, the index storage tables don't have to be dropped. This is done automatically by the kernel after the call is completed.

### ODCIIndexExchangePartition()

This method is invoked when an `ALTER TABLE EXCHANGE PARTITION...INCLUDING INDEXES` command is issued on a partitioned table that has a defined local domain index.

Syntax

```
FUNCTION ODCIIndexExchangePartition( 
   ia ODCIIndexInfo, 
   ia1 ODCIIndexInfo, 
   env ODCIEnv) 
RETURN NUMBER
```

| Parameter | Description |
| --- | --- |
| ia | Contains information about the domain index partition to exchange. |
| ia1 | Contains information about the non-partitioned domain index. |
| env | The environment handle passed to the routine |

Returns

`ODCIConst.Success` on success, or `ODCIConst.Error` on error, or `ODCIConst.Warning`.

Usage Notes

- The function should be implemented as a `STATIC` type method.
- This method should handle both converting a partition of a domain index into a non-partitioned domain index and converting a non-partitioned index to a partition of a partitioned domain index.

### ODCIIndexFetch()

This procedure is invoked repeatedly to retrieve the rows satisfying the operator predicate.

Syntax

```
FUNCTION ODCIIndexFetch(
   self IN [OUT] impltype, 
   nrows IN NUMBER, 
   rids OUT ODCIRidList, 
   env ODCIEnv) 
RETURN NUMBER
```

| Parameter | Description |
| --- | --- |
| ``` self(IN) ``` | Is the value of the context returned by the previous call (to `ODCIIndexFetch` or to ODCIIndexStart() if this is the first time fetch is being called for this operator instance |
| ``` self(OUT) ``` | The context that is passed to the next query-time call. Note that this parameter does not have to be defined as `OUT` if the value is not modified in this routine. |
| ``` nrows ``` | Is the maximum number of result rows that can be returned to Oracle in this call |
| ``` rids ``` | Is the array of row identifiers for the result rows being returned by this call |
| ``` env ``` | The environment handle passed to the routine |

Returns

`ODCIConst.Success` on success, or `ODCIConst.Error` on error.

Usage Notes

- ODCIIndexFetch() returns rows satisfying the operator predicate. That is, it returns the row identifiers of all the rows for which the operator return value falls within the specified bounds.
- Each call to ODCIIndexFetch() can return a maximum of nrows number of rows. The value of nrows passed in is decided by Oracle based on some internal factors. However, the ODCIIndexFetch() routine can return lesser than nrows number of rows. The row identifiers are returned through the output `rids` array. A `NULL` `ROWID` (as an element of the `rids` array) indicates that all satisfying rows have been returned.
	Assume that there are `3000` rows which satisfy the operator predicate, and that the value of `nrows` `= 2000`. The first invocation of ODCIIndexFetch() can return the first `2000` rows. The second invocation can return a `rid` list consisting of the remaining `1000` rows followed by a `NULL` element. The `NULL` value in `rid` list indicates that all satisfying rows have now been returned.
- If the context value is changed within this call, the new value is passed in to subsequent query-time calls.

### ODCIIndexGetMetadata()

Returns a series of strings of PL/SQL code that comprise the non-dictionary metadata associated with the index in `ia`. The routine can pass whatever information is required at import time. For example, policy, version, preferences, and so on. This method is optional unless implementation-specific metadata is required.

Syntax

```
FUNCTION ODCIIndexGetMetadata(
   ia IN ODCIIndexInfo, 
   version IN VARCHAR2, 
   new_block OUT PLS_INTEGER,
   env ODCIEnv) 
RETURN VARCHAR2;
```

| Parameter | Description |
| --- | --- |
| ``` ia ``` | Specifies the index on which export is currently working |
| ``` version ``` | Version of export making the call in the form `11.2.0.1.00` |
| ``` new_block ``` | Non-zero (`TRUE`): Returned string starts a new PL/SQL block. Export terminates the current block (if any) with `END`; and open a new block with `BEGIN` before writing strings to the dump file. The routine is called again.  `0` (`FALSE`): Returned string continues current block. Export writes only the returned string to the dump file then calls the routine again. |
| ``` env ``` | The environment handle passed to the routine |

Returns

- A null-terminated string containing a piece of an opaque block of PL/SQL code
- A zero-length string indicates no more data; export stops calling the routine

Usage Notes

- This function should be implemented as a static type method.
- The routine is called repeatedly until the return string length is 0. If an index has no metadata to be exported using PL/SQL, it should return an empty string upon first call.
- This routine can be used to build one or more blocks of anonymous PL/SQL code for execution by import. Each returned block is invoked independently by import. That is, if a block fails for any reason at import time, subsequent blocks are still invoked. Therefore any dependent code should be incorporated within a single block. The size of an individual block of PL/SQL code is limited only by the size of import's read buffer controlled by its `BUFFER` parameter.
- The execution of these PL/SQL blocks at import time is considered part of the associated domain index's creation. Therefore, their execution is dependent upon the successful import of the index's underlying base table and user's setting of import's `INDEXES=Y/N` parameter, as is the creation of the index.
- The routine should not pass back the `BEGIN` / `END` strings that open and close the individual blocks of PL/SQL code; export adds these to mark the individual units of execution.
- The parameter `version` is the version number of the currently executing export client. Since export and import can be used to downgrade a database to the previous functional point release, it also represents the minimum server version you can expect to find at import time; it may be higher, but never lower.
- The cartridge developer can use this information to determine what version of information should be written to the dump file. For example, assume the current server version is `11.2.0.1.0`, but the export version handed in is `11.1.0.1.0`. If a cartridge's metadata changed formats these version, it would know to write the data to the dump file in 11.1 format, anticipating an import into an 11.2 system.
- The data contained within the strings handed back to export must be completely platform-independent. That is, they should contain no binary information that may reflect the endian nature of the export platform, which may be different from the import platform. Binary information may be passed as hex strings and converted through `RAWTOHEX` and `HEXTORAW`.
- The strings are translated from the export server to export client character set and are written to the dump file as such. At import time, they are translated from export client character set to import client character set, then from import client char set to import server character set when handed over the UPI interface.
- Specifying a target schema in the execution of any of the PL/SQL blocks must be avoided because it frequently causes an error if you use import's `FROMUSER` -> `TOUSER` schema replication feature. For example, a procedure prototype such as:
	```
	PROCEDURE AQ_CREATE ( schema IN VARCHAR2, que_name IN VARCHAR2) ...
	```
	should be avoided becuase it fails if you have remapped schema A to schema B on import. You can assume at import time that you are connected to the target schema.
- Export dump files from a particular version must be importable into all future versions. This means that all PL/SQL routines invoked within the anonymous PL/SQL blocks written to the dump file must be supported for all time. You may wish to encode some version information to assist with detecting when conversion may be required.
- Export operates in a read-only transaction if its parameter `CONSISTENT=Y`. In this case, no writes are allowed from the export session. Therefore, this method must not write any database state.
- You can attempt to import the same dump file multiple times, especially when using import's `IGNORE=Y` parameter. Therefore, this method must produce PL/SQL code that is idempotent, or at least deterministic when executed multiple times.
- Case on database object names must be preserved; that is, objects named ' `Foo` ' and ' `FOO` ' are distinct objects. Database object names should be enclosed within double quotes ("") to preserve case.

Error Handling

Any unrecoverable error should raise an exception allowing it to propagate back to `get_domain_index_metadata` and thence back to export. This causes export to terminate the creation of the current index's DDL in the dump file and to move on to the next index.

At import time, failure of the execution of any metadata PL/SQL block causes the associated index not to be created under the assumption that the metadata creation is an integral part of the index creation.

### ODCIIndexInsert()

Invoked when a row or a set of rows is inserted into a table that has a domain index defined on one or more of its columns.

| Syntax | Description |
| --- | --- |
| ``` FUNCTION ODCIIndexInsert(    ia ODCIIndexInfo,     rid VARCHAR2,     newval icoltype,     env ODCIEnv)  RETURN NUMBER ``` | Inserts a single row |
| ``` FUNCTION ODCIIndexInsert(    ia ODCIIndexInfo,    ridlist ODCIRidList,    newvallist varray_of_column_type,    env ODCIEnv)  RETURN NUMBER ``` | Inserts a set of rows |

| Parameter | Description |
| --- | --- |
| ``` ia ``` | Contains information about the index and the indexed column |
| ``` rid ``` | The row identifier of the new row in the table |
| ``` newval ``` | The value of the indexed column in the inserted row |
| ``` ridlist ``` | A varray (maximum size `32767`) containing the list of rowids for the rows being inserted into the base table |
| ``` newvallist ``` | A varray (maximum size `32767`) containing the list of values being inserted into the indexed column in the base table; these entries have a one-to-one correspondence with the entries in `ridlist` |
| ``` env ``` | The environment handle passed to the routine |

Returns

`ODCIConst``.Success` on success, or `ODCIConst.Error` on error.

Usage Notes

- This function should be implemented as a `STATIC` type method.
- This method should insert index data corresponding to the row or set of rows passed in into the appropriate tables or files storing index data. A `NULL` value in `ridlist` indicates the end of the varray.
- If the indextype is defined `WITH ARRAY DML`, a batch of rows can be inserted into the table. In this case, ODCIIndexInsert() is invoked using the second of the two syntax synopses. Otherwise, the single-row syntax is used.
- Note that the index partition object identifier `ODCIIndexInfo.IndexPartitionIden` and the base table partition physical identifier `ODCIIndexInfo.IndexCols(1).TablePartitionIden` is passed in for local domain index. The indextype must use the new DML syntax using the partition number and the provided `SYS_OP_DOBJTOPNUM` function to insert into the storage system partitioned table:
	```
	INSERT INTO SP PARTITION (
	   SYS_OP_DOBJTOPNUM(
	      base_table_name, 
	      :tab_physical_partid))
	VALUES(…);
	```

### ODCIIndexStart()

Invoked to start the evaluation of an operator on an indexed column.

Syntax

```
FUNCTION ODCIIndexStart(
   sctx IN OUT <impltype>, 
   ia ODCIIndexInfo, 
   pi ODCIPredInfo, 
   qi ODCIQueryInfo, 
   strt <opbndtype>, 
   stop <opbndtype>, 
   <valargs>, 
   env ODCIEnv)
RETURN NUMBER
```

| Parameter | Description |
| --- | --- |
| ``` sctx(IN) ``` | The value of the scan context returned by some previous related query-time call (such as the corresponding ancillary operator, if invoked before the primary operator); `NULL` otherwise |
| ``` sctx(OUT) ``` | The context that is passed to the next query-time call; the next query-time call is to ODCIIndexFetch() |
| ``` ia ``` | Contains information about the index and the indexed column |
| ``` pi ``` | Contains information about the operator predicate |
| ``` qi ``` | Contains query information (hints plus list of ancillary operators referenced) |
| ``` strt ``` | The start value of the bounds on the operator return value. The data type is identical to that of the operator's return value |
| ``` stop ``` | The stop value of the bounds on the operator return value. The data type is identical to that of the operator's return value. |
| ``` valargs ``` | The value arguments of the operator invocation. The number and data types of these arguments are identical to those of the value arguments to the operator. |
| ``` env ``` | The environment handle passed to the routine |

Returns

`ODCIConst``.Success` on success, or `ODCIConst.Error` on error.

Usage Notes

- The function should be implemented as a static method.
- ODCIIndexStart() is invoked to begin the evaluation of an operator on an indexed column. In particular, the following conditions hold:
	- The first argument to the operator is a column which has a domain index defined on it.
		- The indextype of the domain index (specified in `ODCIIndexInfo` parameter) supports the current operator.
		- All other arguments to the operator are value arguments (literals) which are passed in through the `<valargs>` parameters.
- The ODCIIndexStart() method should initialize the index scan as needed (using the operator-related information in the `pi` argument) and prepare for the subsequent invocations of ODCIIndexFetch().
- The `strt` and `stop` parameters, with the `bndflg` value in `ODCIPredInfo` parameter, specify the range of values within which the operator return value should lie.
- Bounds for operator return values are specified as follows:
	- If the predicate to be evaluated is of the form `op` `LIKE` `val`, the `ODCIIndexPrefixMatch` flag is set. In this case, the start key contains the value `<val>` and the stop key value is irrelevant.
		- If the predicate to be evaluated is of the form `op` = `val`, the `ODCIIndexExactMatch` flag is set. In this case, the start key contains the value `<val>` and the stop key value is irrelevant.
		- If the predicate to be evaluated is of the form `op` > `val`, `startkey` contains the value `<val>` and stop key value is set to `NULL`. If the predicate is of the form `op` >= `<val>`, the flag `ODCIIndexIncludeStart` is also set.
		- If the predicate to be evaluated is of the form `op` `< val`, stop key contains the value \<val> and the start key value is set to `NULL`. If the predicate is of the form `op` `<= val`, the flag `ODCIIndexIncludeStop` is also set.
- A context value can be returned to Oracle (through the `SELF` argument) which is then passed back to the next query-time call. The next call is to ODCIIndexFetch() if the evaluation continues, or to ODCIIndexStart() if the evaluation is restarted. The context value can be used to store the entire evaluation state or just a handle to the memory containing the state.
- Note that if the same indextype supports multiple operators with different signatures, multiple ODCIIndexStart() methods must be implemented, one for each distinct combination of value argument data types. For example, if an indextype supports three operators:
	1. `op1(number, number)`
		2. `op1(varchar2, varchar2)`
		3. `op2(number, number)`
	two `ODCIIndexStart` routines must be implemented:
	- `ODCIIndexStart(...., NUMBER)` — handles cases (1) and (3) which has a `NUMBER` value argumen `t`
		- `ODCIIndexStart(...., VARCHAR2)` — handles case (2) which has a `VARCHAR2` value argument
- The query information in `qi` parameter can be used to optimize the domain index scan, if possible. The query information includes hints that have been specified for the query and the list of relevant ancillary operators referenced in the query block.
- The index partition object identifier `ODCIIndexInfo.IndexPartitionIden` and the base table partition physical identifier `ODCIIndexInfo.IndexCols(1).TablePartitionIden` is passed in for local domain index. The indextype must use the new SQL syntax using the partition number and the provided `SYS_OP_DOBJTOPNUM` function to query the corresponding partition of the storage system partitioned table:
	```
	SELECT FROM SP PARTITION(
	   SYS_OP_DOBJTOPNUM(
	   base_table_name, 
	   :tab_physical_partid)) 
	WHERE ...;
	```

### ODCIIndexUpdate()

Invoked when a row is updated in a table that has a defined domain index on one or more of its columns.

Syntax

```
FUNCTION ODCIIndexUpdate( 
   ia ODCIIndexInfo, 
   rid VARCHAR2, 
   oldval icoltype, 
   newval icoltype, 
   env ODCIEnv)
RETURN NUMBER
```

| Parameter | Description |
| --- | --- |
| ``` ia ``` | Contains information about the index and the indexed column |
| ``` rid ``` | The row identifier of the updated row |
| ``` oldval ``` | The value of the indexed column before the update. The data type is identical to that of the indexed column. |
| ``` newval ``` | The value of the indexed column after the update. The data type is identical to that of the indexed column. |
| ``` env ``` | The environment handle passed to the routine |

Returns

`ODCIConst.Success` on success, or `ODCIConst.Error` on error.

Usage Notes

- The function should be implemented as a `static` type method.
- This method should update the tables or files storing the index data for the updated row.
- In addition to a SQL `UPDATE` statement, a LOB value can be updated through a variety of `WRITE` interfaces (see [Oracle Database SecureFiles and Large Objects Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e18294/toc.htm)). If a domain index is defined on a `LOB` column or an object type containing a `LOB` attribute, the `ODCIIndexUpdate` routine is called when a LOB locator is implicitly or explicitly closed after one or more write operations.
- The index partition object identifier, `ODCIIndexInfo.IndexPartitionIden`, and the base table partition physical identifier, `ODCIIndexInfo.IndexCols(1).TablePartitionIden`, is passed in for local domain indexes. The indextype must use the new DML syntax with the partition number, and the provided `DATAOBJ_TO_PARTITION()` function to update data in the storage system partitioned table:
	```
	UPDATE SP PARTITION 
	   (DATAOBJ_TO_PARTITION(
	      base_table_name, :tab_physical_partid)) 
	   VALUES(…) SET val = :newval WHERE rowid + :rowid;
	```

### ODCIIndexUpdPartMetadata()

Invoked during partition maintenance operations. Patches the indextype metadata tables to correctly reflect the partition maintenance operation.

Syntax

```
FUNCTION ODCIIndexUpdPartMetadata(
   ia ODCIIndexInfo,
   palist ODCIPartInfoList,
   env ODCIEnv)
```

| Parameter | Description |
| --- | --- |
| ``` ia ``` | The information about the domain index; does not contain partition-specific information |
| ``` palist ``` | The information about the dropped or added partitions |
| ``` env ``` | The environment handle |

Usage Notes

- This method should be implemented as a `STATIC` type method.
- When an indextype is specified with the `SYSTEM MANAGED` approach, this method is invoked on the local domain index of this indextype during partition management operations.
- SQL DDLs are not allowed in this method.
- The indextype should update its metadata mapping specific to the partitions, if any.
- The `palist` argument contains a list of partitions that should be dropped or added. For example, if the base table operation is `ALTER TABLE SPLIT PARTITTION P1 INTO P11 AND P12`, then the `palist` would have information about `3` partitions: `P1` (drop), `P11` (add) and `P12` (add), along with their index partition names and index partition object identifiers.
- If the ODCIIndexUpdPartMetadata() call raises or returns an error, then the partition management operation on the base table is rolled back.

### ODCIIndexUtilCleanup()

Cleans up temporary states created by ODCIIndexUtilGetTableNames(). See ODCIIndexUtilGetTableNames() for further information.

Syntax

```
FUNCTION ODCIIndexUtilCleanup (
   context  PLS_INTEGER)
```

| Parameter | Description |
| --- | --- |
| ``` context ``` | The number created by ODCIIndexUtilGetTableNames() that uniquely identifies state information for a particular index. |

Usage Notes

- The procedure should be implemented as a static type method.
- ODCIIndexUtilCleanup() deletes any temporary state associated with the parameter context.
- Exceptions raised by ODCIIndexUtilCleanup() are ignored by its caller.

### ODCIIndexUtilGetTableNames()

Determines if the secondary tables of the domain index should be exported/imported. By default, secondary objects of the domain are not imported or exported. However, if this interface and ODCIIndexUtilCleanup() are present, the system invokes them.

If this interface is implemented, your application can also invoke it for transportable tablespace operations.

Syntax

```
FUNCTION ODCIIndexUtilGetTableNames(
   ia sys.odciindexinfo, 
   read_only PLS_INTEGER, 
   version varchar2, 
   context OUT PLS_INTEGER)
RETURN BOOLEAN
```

| Parameter | Description |
| --- | --- |
| ``` ia ``` | Contains information about the index and the indexed column |
| ``` read_only ``` | Specify 1 if the encompassing transaction is read-only, meaning no writes allowed. Otherwise 0. |
| ``` version ``` | Version of export making the call. |
| ``` context ``` | A unique number that is used by ODCIIndexUtilCleanup() to facilitate the clean up of any state held open between ODCIIndexUtilGetTableNames() and ODCIIndexUtilCleanup() |

Returns

`TRUE` if the domain indexes' secondary tables should be exported/imported. Otherwise, the function returns `FALSE`.

Usage Notes

- This function should be implemented as a static type method.
- This function should return `TRUE` or `FALSE` based on whether the secondary tables should be exported/imported.
- This function should return `TRUE` or `FALSE` based on whether the secondary tables should be transported. Secondary objects other than tables do not participate in transportable tablespaces. They must be recreated on the import side when the ODCIIndexCreate() method is invoked with the `ODCI_INDEX_TRANS_TBLSPC` bit set in the `ODCIIndexInfo.IndexInfoFlags`.