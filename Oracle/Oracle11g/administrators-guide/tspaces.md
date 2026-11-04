---
title: Managing Tablespaces
book: "Administrator's Guide"
doc_id: E25494-07
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e25494/tspaces.htm
tags:
  - oracle
  - 11g
  - administrators-guide
---

## 14 Managing Tablespaces

In this chapter:

See Also:

- [Oracle Database Concepts](https://docs.oracle.com/cd/E11882_01/server.112/e40540/logical.htm#CNCPT402) for a complete discussion of database structure, space management, tablespaces, and data files
- [Chapter 17, "Using Oracle Managed Files"](omf.md) for information about creating data files and temp files that are both created and managed by the Oracle Database server

## Guidelines for Managing Tablespaces

A tablespace is a database storage unit that groups related logical structures together. The database data files are stored in tablespaces. Before working with tablespaces of an Oracle Database, familiarize yourself with the guidelines provided in the following sections:

- Using Multiple Tablespaces
- Assigning Tablespace Quotas to Users

### Using Multiple Tablespaces

Using multiple tablespaces allows you more flexibility in performing database operations. When a database has multiple tablespaces, you can:

- Separate user data from data dictionary data to reduce I/O contention.
- Separate data of one application from the data of another to prevent multiple applications from being affected if a tablespace must be taken offline.
- Store the data files of different tablespaces on different disk drives to reduce I/O contention.
- Take individual tablespaces offline while others remain online, providing better overall availability.
- Optimizing tablespace use by reserving a tablespace for a particular type of database use, such as high update activity, read-only activity, or temporary segment storage.
- Back up individual tablespaces.

Some operating systems set a limit on the number of files that can be open simultaneously. Such limits can affect the number of tablespaces that can be simultaneously online. To avoid exceeding your operating system limit, plan your tablespaces efficiently. Create only enough tablespaces to fulfill your needs, and create these tablespaces with as few files as possible. If you must increase the size of a tablespace, then add one or two large data files, or create data files with autoextension enabled, rather than creating many small data files.

Review your data in light of these factors and decide how many tablespaces you need for your database design.

### Assigning Tablespace Quotas to Users

Grant to users who will be creating tables, clusters, materialized views, indexes, and other objects the privilege to create the object and a quota (space allowance or limit) in the tablespace intended to hold the object segment.

Note:

For PL/SQL objects such as packages, procedures, and functions, users only need the privileges to create the objects. No explicit tablespace quota is required to create these PL/SQL objects.

See Also:

[Oracle Database Security Guide](https://docs.oracle.com/cd/E11882_01/network.112/e36292/users.htm#DBSEG002) for information about creating users and assigning tablespace quotas.

## Creating Tablespaces

Before you can create a tablespace, you must create a database to contain it. The primary tablespace in any database is the `SYSTEM` tablespace, which contains information basic to the functioning of the database server, such as the data dictionary and the system rollback segment. The `SYSTEM` tablespace is the first tablespace created at database creation. It is managed as any other tablespace, but requires a higher level of privilege and is restricted in some ways. For example, you cannot rename or drop the `SYSTEM` tablespace or take it offline.

The `SYSAUX` tablespace, which acts as an auxiliary tablespace to the `SYSTEM` tablespace, is also always created when you create a database. It contains the schemas used by various Oracle products and features, so that those products do not require their own tablespaces. As for the `SYSTEM` tablespace, management of the `SYSAUX` tablespace requires a higher level of security and you cannot rename or drop it. The management of the `SYSAUX` tablespace is discussed separately in "Managing the SYSAUX Tablespace".

The steps for creating tablespaces vary by operating system, but the first step is always to use your operating system to create a directory structure in which your data files will be allocated. On most operating systems, you specify the size and fully specified filenames of data files when you create a new tablespace or alter an existing tablespace by adding data files. Whether you are creating a new tablespace or modifying an existing one, the database automatically allocates and formats the data files as specified.

To create a new tablespace, use the SQL statement `CREATE TABLESPACE` or `CREATE TEMPORARY TABLESPACE`. You must have the `CREATE TABLESPACE` system privilege to create a tablespace. Later, you can use the `ALTER TABLESPACE` or `ALTER DATABASE` statements to alter the tablespace. You must have the `ALTER TABLESPACE` or `ALTER DATABASE` system privilege, correspondingly.

You can also use the `CREATE UNDO TABLESPACE` statement to create a special type of tablespace called an undo tablespace, which is specifically designed to contain undo records. These are records generated by the database that are used to roll back, or undo, changes to the database for recovery, read consistency, or as requested by a `ROLLBACK` statement. Creating and managing undo tablespaces is the subject of [Chapter 16, "Managing Undo"](undo.md).

The creation and maintenance of permanent and temporary tablespaces are discussed in the following sections:

- Locally Managed Tablespaces
- Bigfile Tablespaces
- Compressed Tablespaces
- Encrypted Tablespaces
- Temporary Tablespaces
- Multiple Temporary Tablespaces: Using Tablespace Groups
	See Also:
	- [Chapter 2, "Creating and Configuring an Oracle Database"](create.md) and your Oracle Database installation documentation for your operating system for information about tablespaces that are created at database creation
	- [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/toc.htm) for more information about the syntax and semantics of the `CREATE TABLESPACE`, `CREATE TEMPORARY TABLESPACE`, `ALTER TABLESPACE`, and `ALTER DATABASE` statements.
	- ["Specifying Database Block Sizes"](create.md) for information about initialization parameters necessary to create tablespaces with nonstandard block sizes

### Locally Managed Tablespaces

Locally managed tablespaces track all extent information in the tablespace itself by using bitmaps, resulting in the following benefits:

- Fast, concurrent space operations. Space allocations and deallocations modify locally managed resources (bitmaps stored in header files).
- Enhanced performance
- Readable standby databases are allowed, because locally managed temporary tablespaces do not generate any undo or redo.
- Space allocation is simplified, because when the `AUTOALLOCATE` clause is specified, the database automatically selects the appropriate extent size.
- User reliance on the data dictionary is reduced, because the necessary information is stored in file headers and bitmap blocks.
- Coalescing free extents is unnecessary for locally managed tablespaces.

All tablespaces, including the `SYSTEM` tablespace, can be locally managed.

The `DBMS_SPACE_ADMIN` package provides maintenance procedures for locally managed tablespaces.

See Also:

- ["Creating a Locally Managed SYSTEM Tablespace"](create.md), "Migrating the SYSTEM Tablespace to a Locally Managed Tablespace", and "Diagnosing and Repairing Locally Managed Tablespace Problems"
- "Bigfile Tablespaces" for information about creating another type of locally managed tablespace that contains only a single data file or temp file.
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/d_spadmn.htm#ARPLS057) for information on the `DBMS_SPACE_ADMIN` package

#### Creating a Locally Managed Tablespace

Create a locally managed tablespace by specifying `LOCAL` in the `EXTENT MANAGEMENT` clause of the `CREATE TABLESPACE` statement. This is the default for new permanent tablespaces, but you must specify the `EXTENT` `MANAGEMENT` `LOCAL` clause to specify either the `AUTOALLOCATE` clause or the `UNIFORM` clause. You can have the database manage extents for you automatically with the `AUTOALLOCATE` clause (the default), or you can specify that the tablespace is managed with uniform extents of a specific size (`UNIFORM`).

If you expect the tablespace to contain objects of varying sizes requiring many extents with different extent sizes, then `AUTOALLOCATE` is the best choice. `AUTOALLOCATE` is also a good choice if it is not important for you to have a lot of control over space allocation and deallocation, because it simplifies tablespace management. Some space may be wasted with this setting, but the benefit of having Oracle Database manage your space most likely outweighs this drawback.

If you want exact control over unused space, and you can predict exactly the space to be allocated for an object or objects and the number and size of extents, then `UNIFORM` is a good choice. This setting ensures that you will never have unusable space in your tablespace.

When you do not explicitly specify the type of extent management, Oracle Database determines extent management as follows:

- If the `CREATE TABLESPACE` statement omits the `DEFAULT` storage clause, then the database creates a locally managed autoallocated tablespace.
- If the `CREATE TABLESPACE` statement includes a `DEFAULT` storage clause, then the database considers the following:
	- If you specified the `MINIMUM EXTENT` clause, the database evaluates whether the values of `MINIMUM EXTENT`, `INITIAL`, and `NEXT` are equal and the value of `PCTINCREASE` is 0. If so, the database creates a locally managed uniform tablespace with extent size = `INITIAL`. If the `MINIMUM EXTENT`, `INITIAL`, and `NEXT` parameters are not equal, or if `PCTINCREASE` is not 0, the database ignores any extent storage parameters you may specify and creates a locally managed, autoallocated tablespace.
		- If you did not specify `MINIMUM EXTENT` clause, the database evaluates only whether the storage values of `INITIAL` and `NEXT` are equal and `PCTINCREASE` is 0. If so, the tablespace is locally managed and uniform. Otherwise, the tablespace is locally managed and autoallocated.

The following statement creates a locally managed tablespace named `lmtbsb` and specifies `AUTOALLOCATE`:

```
CREATE TABLESPACE lmtbsb DATAFILE '/u02/oracle/data/lmtbsb01.dbf' SIZE 50M
    EXTENT MANAGEMENT LOCAL AUTOALLOCATE;
```

`AUTOALLOCATE` causes the tablespace to be system managed with a minimum extent size of 64K.

The alternative to `AUTOALLOCATE` is `UNIFORM`. which specifies that the tablespace is managed with extents of uniform size. You can specify that size in the `SIZE` clause of `UNIFORM`. If you omit `SIZE`, then the default size is 1M.

The following example creates a tablespace with uniform 128K extents. (In a database with 2K blocks, each extent would be equivalent to 64 database blocks). Each 128K extent is represented by a bit in the extent bitmap for this file.

```
CREATE TABLESPACE lmtbsb DATAFILE '/u02/oracle/data/lmtbsb01.dbf' SIZE 50M
    EXTENT MANAGEMENT LOCAL UNIFORM SIZE 128K;
```

You cannot specify the `DEFAULT` storage clause, `MINIMUM EXTENT`, or `TEMPORARY` when you explicitly specify `EXTENT MANAGEMENT LOCAL`. To create a temporary locally managed tablespace, use the `CREATE TEMPORARY TABLESPACE` statement.

Note:

When you allocate a data file for a locally managed tablespace, you should allow space for metadata used for space management (the extent bitmap or space header segment) which are part of user space. For example, if you specify the `UNIFORM` clause in the extent management clause but you omit the `SIZE` parameter, then the default extent size is 1MB. In that case, the size specified for the data file must be larger (at least one block plus space for the bitmap) than 1MB.

#### Specifying Segment Space Management in Locally Managed Tablespaces

In a locally managed tablespace, there are two methods that Oracle Database can use to manage segment space: automatic and manual. Manual segment space management uses linked lists called "freelists" to manage free space in the segment, while automatic segment space management uses bitmaps. Automatic segment space management is the more efficient method, and is the default for all new permanent, locally managed tablespaces.

Automatic segment space management delivers better space utilization than manual segment space management. It is also self-tuning, in that it scales with increasing number of users or instances. In an Oracle Real Application Clusters environment, automatic segment space management allows for a dynamic affinity of space to instances. In addition, for many standard workloads, application performance with automatic segment space management is better than the performance of a well-tuned application using manual segment space management.

Although automatic segment space management is the default for all new permanent, locally managed tablespaces, you can explicitly enable it with the `SEGMENT SPACE MANAGEMENT AUTO` clause.

The following statement creates tablespace `lmtbsb` with automatic segment space management:

```
CREATE TABLESPACE lmtbsb DATAFILE '/u02/oracle/data/lmtbsb01.dbf' SIZE 50M
    EXTENT MANAGEMENT LOCAL 
    SEGMENT SPACE MANAGEMENT AUTO;
```

The `SEGMENT SPACE MANAGEMENT MANUAL` clause disables automatic segment space management.

The segment space management that you specify at tablespace creation time applies to all segments subsequently created in the tablespace. You cannot change the segment space management mode of a tablespace.

Notes:

- If you set extent management to `LOCAL` `UNIFORM`, then you must ensure that each extent contains at least 5 database blocks.
- If you set extent management to `LOCAL` `AUTOALLOCATE`, and if the database block size is 16K or greater, then Oracle manages segment space by creating extents with a minimum size of 5 blocks rounded up to 64K.
- You cannot specify automatic segment space management for the `SYSTEM` tablespace.

Locally managed tablespaces using automatic segment space management can be created as single-file or bigfile tablespaces, as described in "Bigfile Tablespaces".

### Bigfile Tablespaces

A bigfile tablespace is a tablespace with a single, but potentially very large (up to 4G blocks) data file. Traditional smallfile tablespaces, in contrast, can contain multiple data files, but the files cannot be as large. The benefits of bigfile tablespaces are the following:

- A bigfile tablespace with 8K blocks can contain a 32 terabyte data file. A bigfile tablespace with 32K blocks can contain a 128 terabyte data file. The maximum number of data files in an Oracle Database is limited (usually to 64K files). Therefore, bigfile tablespaces can significantly enhance the storage capacity of an Oracle Database.
- Bigfile tablespaces can reduce the number of data files needed for a database. An additional benefit is that the `DB_FILES` initialization parameter and `MAXDATAFILES` parameter of the `CREATE DATABASE` and `CREATE CONTROLFILE` statements can be adjusted to reduce the amount of SGA space required for data file information and the size of the control file.
- Bigfile tablespaces simplify database management by providing data file transparency. SQL syntax for the `ALTER` `TABLESPACE` statement lets you perform operations on tablespaces, rather than the underlying individual data files.

Bigfile tablespaces are supported only for locally managed tablespaces with automatic segment space management, with three exceptions: locally managed undo tablespaces, temporary tablespaces, and the `SYSTEM` tablespace.

Notes:

- Bigfile tablespaces are intended to be used with Automatic Storage Management (Oracle ASM) or other logical volume managers that supports striping or RAID, and dynamically extensible logical volumes.
- Avoid creating bigfile tablespaces on a system that does not support striping because of negative implications for parallel query execution and RMAN backup parallelization.
- Using bigfile tablespaces on platforms that do not support large file sizes is not recommended and can limit tablespace capacity. See your operating system specific documentation for information about maximum supported file sizes.

#### Creating a Bigfile Tablespace

To create a bigfile tablespace, specify the `BIGFILE` keyword of the `CREATE` `TABLESPACE` statement (`CREATE` `BIGFILE` `TABLESPACE`...). Oracle Database automatically creates a locally managed tablespace with automatic segment space management. You can, but need not, specify `EXTENT` `MANAGEMENT` `LOCAL` and `SEGMENT` `SPACE` `MANAGEMENT` `AUTO` in this statement. However, the database returns an error if you specify `EXTENT` `MANAGEMENT` `DICTIONARY` or `SEGMENT` `SPACE` `MANAGEMENT` `MANUAL`. The remaining syntax of the statement is the same as for the `CREATE TABLESPACE` statement, but you can only specify one data file. For example:

```
CREATE BIGFILE TABLESPACE bigtbs 
    DATAFILE '/u02/oracle/data/bigtbs01.dbf' SIZE 50G
...
```

You can specify `SIZE` in kilobytes (K), megabytes (M), gigabytes (G), or terabytes (T).

If the default tablespace type was set to `BIGFILE` at database creation, you need not specify the keyword `BIGFILE` in the `CREATE TABLESPACE` statement. A bigfile tablespace is created by default.

If the default tablespace type was set to `BIGFILE` at database creation, but you want to create a traditional (smallfile) tablespace, then specify a `CREATE` `SMALLFILE` `TABLESPACE` statement to override the default tablespace type for the tablespace that you are creating.

See Also:

["Supporting Bigfile Tablespaces During Database Creation"](create.md)

#### Identifying a Bigfile Tablespace

The following views contain a `BIGFILE` column that identifies a tablespace as a bigfile tablespace:

- `DBA_TABLESPACES`
- `USER_TABLESPACES`
- `V$TABLESPACE`

You can also identify a bigfile tablespace by the relative file number of its single data file. That number is 1024 on most platforms, but 4096 on OS/390.

### Compressed Tablespaces

You can specify that all tables created in a tablespace are compressed by default. You specify the type of table compression using the `DEFAULT` keyword, followed by one of the compression type clauses used when creating a table.

The following statement indicates that all tables created in the tablespace are to use OLTP compression, unless otherwise specified:

```
CREATE TABLESPACE ... DEFAULT COMPRESS FOR OLTP ... ;
```

You can override the default tablespace compression specification when you create a table in that tablespace.

See Also:

- ["Consider Using Table Compression"](tables.md) for information about the various types of table compression
- [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_7003.htm#SQLRF01403) for the exact syntax to use when creating a tablespace with a default compression type

### Encrypted Tablespaces

You can encrypt any permanent tablespace to protect sensitive data. Tablespace encryption is completely transparent to your applications, so no application modification is necessary. Encrypted tablespaces primarily protect your data from unauthorized access by means other than through the database. For example, when encrypted tablespaces are written to backup media for travel from one Oracle database to another or for travel to an off-site facility for storage, they remain encrypted. Also, encrypted tablespaces protect data from users who try to circumvent the security features of the database and access database files directly through the operating system file system.

Tablespace encryption does not address all security issues. It does not, for example, provide access control from within the database. Any user who is granted privileges on objects stored in an encrypted tablespace can access those objects without providing any kind of additional password or key.

When you encrypt a tablespace, all tablespace blocks are encrypted. All segment types are supported for encryption, including tables, clusters, indexes, LOBs (`BASICFILE` and `SECUREFILE`), table and index partitions, and so on.

Note:

There is no need to use LOB encryption on `SECUREFILE` LOBs stored in an encrypted tablespace.

To maximize security, data from an encrypted tablespace is automatically encrypted when written to the undo tablespace, to the redo logs, and to any temporary tablespace. There is no need to explicitly create encrypted undo or temporary tablespaces, and in fact, you cannot specify encryption for those tablespace types.

For partitioned tables and indexes that have different partitions in different tablespaces, it is permitted to use both encrypted and non-encrypted tablespaces in the same table or index.

Tablespace encryption uses the transparent data encryption feature of Oracle Database, which requires that you create an Oracle wallet to store the master encryption key for the database. The wallet must be open before you can create the encrypted tablespace and before you can store or retrieve encrypted data. When you open the wallet, it is available to all session, and it remains open until you explicitly close it or until the database is shut down.

To encrypt a tablespace, you must open the database with the `COMPATIBLE` initialization parameter set to 11.1.0 or higher. The default setting for `COMPATIBLE` for a new Oracle Database 11g Release 2 installation is 11.2.0. Any user who can create a tablespace can create an encrypted tablespace.

Transparent data encryption supports industry-standard encryption algorithms, including the following Advanced Encryption Standard (AES) and Triple Data Encryption Standard (3DES) algorithms:

- AES256
- AES192
- AES128
- 3DES168

The encryption key length is implied by the algorithm name. For example, the AES128 algorithm uses 128-bit keys. You specify the algorithm to use when you create the tablespace, and different tablespaces can use different algorithms. Although longer key lengths theoretically provide greater security, there is a trade-off in CPU overhead. If you do not specify the algorithm in your `CREATE` `TABLESPACE` statement, AES128 is the default. There is no disk space overhead for encrypting a tablespace.

Examples

The following statement creates an encrypted tablespace with the default encryption algorithm:

```
CREATE TABLESPACE securespace
DATAFILE '/u01/app/oracle/oradata/orcl/secure01.dbf' SIZE 100M
ENCRYPTION
DEFAULT STORAGE(ENCRYPT);
```

The following statement creates the same tablespace with the AES256 algorithm:

```
CREATE TABLESPACE securespace
DATAFILE '/u01/app/oracle/oradata/orcl/secure01.dbf' SIZE 100M
ENCRYPTION USING 'AES256'
DEFAULT STORAGE(ENCRYPT);
```

Restrictions

The following are restrictions for encrypted tablespaces:

- You cannot encrypt an existing tablespace with an `ALTER` `TABLESPACE` statement. However, you can use Data Pump or SQL statements such as `CREATE` `TABLE` `AS` `SELECT` or `ALTER` `TABLE` `MOVE` to move existing table data into an encrypted tablespace.
- Encrypted tablespaces are subject to restrictions when transporting to another database. See "Limitations on Transportable Tablespace Use".
- When recovering a database with encrypted tablespaces (for example after a `SHUTDOWN` `ABORT` or a catastrophic error that brings down the database instance), you must open the Oracle wallet after database mount and before database open, so the recovery process can decrypt data blocks and redo.

In addition, see [Oracle Database Advanced Security Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e40393/asotrans.htm#ASOAG9518) for general restrictions for transparent data encryption.

Querying Tablespace Encryption Information

The `DBA_TABLESPACES` and `USER_TABLESPACES` data dictionary views include a column named `ENCRYPTED`. This column contains `YES` for encrypted tablespaces.

The view `V$ENCRYPTED_TABLESPACES` lists all currently encrypted tablespaces. The following query displays the name and encryption algorithm of encrypted tablespaces:

```
SELECT t.name, e.encryptionalg algorithm 
FROM  v$tablespace t, v$encrypted_tablespaces e
WHERE t.ts# = e.ts#;
 
NAME                           ALGORITHM 
------------------------------ --------- 
SECURESPACE                    AES256
```

See Also:

- [Oracle Database 2 Day + Security Guide](https://docs.oracle.com/cd/E11882_01/server.112/e10575/tdpsg_securing_data.htm#TDPSG40043) for more information about transparent data encryption and for instructions for creating and opening wallets
- ["Consider Encrypting Columns That Contain Sensitive Data"](tables.md) for an alternative to encrypting an entire tablespace
- [Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41960/design.htm#RACAD510) for information on using an Oracle wallet in an Oracle Real Application Clusters environment
- [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_7003.htm#SQLRF01403) for information about the `CREATE` `TABLESPACE` statement

### Temporary Tablespaces

A temporary tablespace contains transient data that persists only for the duration of the session. Temporary tablespaces can improve the concurrency of multiple sort operations that do not fit in memory and can improve the efficiency of space management operations during sorts.

Temporary tablespaces are used to store the following:

- Intermediate sort results
- Temporary tables and temporary indexes
- Temporary LOBs
- Temporary B-trees

Within a temporary tablespace, all sort operations for a particular instance share a single sort segment, and sort segments exist for every instance that performs sort operations that require temporary space. A sort segment is created by the first statement after startup that uses the temporary tablespace for sorting, and is released only at shutdown.

By default, a single temporary tablespace named `TEMP` is created for each new Oracle Database installation. You can create additional temporary tablespaces with the `CREATE` `TABLESPACE` statement. You can assign a temporary tablespace to each database user with the `CREATE USER` or `ALTER USER` statement. A single temporary tablespace can be shared by multiple users.

You cannot explicitly create objects in a temporary tablespace.

Note:

The exception to the preceding statement is a temporary table. When you create a temporary table, its rows are stored in your default temporary tablespace, unless you create the table in a new temporary tablespace. See ["Creating a Temporary Table"](tables.md) for more information.

Default Temporary Tablespace

Users who are not explicitly assigned a temporary tablespace use the database default temporary tablespace, which for new installations is `TEMP`. You can change the default temporary tablespace for the database with the following command:

```
ALTER DATABASE DEFAULT TEMPORARY TABLESPACE tablespace_name;
```

To determine the current default temporary tablespace for the database, run the following query:

```
SELECT PROPERTY_NAME, PROPERTY_VALUE FROM DATABASE_PROPERTIES WHERE
   PROPERTY_NAME='DEFAULT_TEMP_TABLESPACE';

PROPERTY_NAME              PROPERTY_VALUE
-------------------------- ------------------------------
DEFAULT_TEMP_TABLESPACE    TEMP
```

Space Allocation in a Temporary Tablespace

You can view the allocation and deallocation of space in a temporary tablespace sort segment using the `V$SORT_SEGMENT` view. The `V$TEMPSEG_USAGE` view identifies the current sort users in those segments.

When a sort operation that uses temporary space completes, allocated extents in the sort segment are not deallocated; they are just marked as free and available for reuse. The `DBA_TEMP_FREE_SPACE` view displays the total allocated and free space in each temporary tablespace. See "Viewing Space Usage for Temporary Tablespaces" for more information. You can manually shrink a locally managed temporary tablespace that has a large amount of unused space. See "Shrinking a Locally Managed Temporary Tablespace" for details.

See Also:

- [Oracle Database Security Guide](https://docs.oracle.com/cd/E11882_01/network.112/e36292/users.htm#DBSEG002) for information about creating users and assigning temporary tablespaces
- [Oracle Database Concepts](https://docs.oracle.com/cd/E11882_01/server.112/e40540/logical.htm#CNCPT1092) for more information about the default temporary tablespace
- [Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/toc.htm) for more information about the `V$SORT_SEGMENT`, `V$TEMPSEG_USAGE`, and `DBA_TEMP_FREE_SPACE` views
- [Oracle Database Performance Tuning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41573/memory.htm#PFGRF01401) for a discussion on tuning sorts

#### Creating a Locally Managed Temporary Tablespace

Because space management is much simpler and more efficient in locally managed tablespaces, they are ideally suited for temporary tablespaces. Locally managed temporary tablespaces use temp files, which do not modify data outside of the temporary tablespace or generate any redo for temporary tablespace data. Because of this, they enable you to perform on-disk sorting operations in a read-only or standby database.

You also use different views for viewing information about temp files than you would for data files. The `V$TEMPFILE` and `DBA_TEMP_FILES` views are analogous to the `V$DATAFILE` and `DBA_DATA_FILES` views.

To create a locally managed temporary tablespace, you use the `CREATE TEMPORARY TABLESPACE` statement, which requires that you have the `CREATE TABLESPACE` system privilege.

The following statement creates a temporary tablespace in which each extent is 16M. Each 16M extent (which is the equivalent of 8000 blocks when the standard block size is 2K) is represented by a bit in the bitmap for the file.

```
CREATE TEMPORARY TABLESPACE lmtemp TEMPFILE '/u02/oracle/data/lmtemp01.dbf' 
     SIZE 20M REUSE
     EXTENT MANAGEMENT LOCAL UNIFORM SIZE 16M;
```

The extent management clause is optional for temporary tablespaces because all temporary tablespaces are created with locally managed extents of a uniform size. The default for `SIZE` is 1M. To specify another value for `SIZE`, you can do so as shown in the preceding statement.

Note:

On some operating systems, the database does not allocate space for the temp file until the temp file blocks are actually accessed. This delay in space allocation results in faster creation and resizing of temp files, but it requires that sufficient disk space is available when the temp files are later used. See your operating system documentation to determine whether the database allocates temp file space in this way on your system.

#### Creating a Bigfile Temporary Tablespace

Just as for regular tablespaces, you can create single-file (bigfile) temporary tablespaces. Use the `CREATE BIGFILE TEMPORARY TABLESPACE` statement to create a single-temp file tablespace. See the sections "Creating a Bigfile Tablespace" and "Altering a Bigfile Tablespace" for information about bigfile tablespaces, but consider that you are creating temporary tablespaces that use temp files instead of data files.

#### Viewing Space Usage for Temporary Tablespaces

The `DBA_TEMP_FREE_SPACE` dictionary view contains information about space usage for each temporary tablespace. The information includes the space allocated and the free space. You can query this view for these statistics using the following command.

```
SELECT * from DBA_TEMP_FREE_SPACE;
 
TABLESPACE_NAME                     TABLESPACE_SIZE ALLOCATED_SPACE FREE_SPACE
----------------------------------- --------------- --------------- ----------
TEMP                                250609664       250609664       249561088
```

### Multiple Temporary Tablespaces: Using Tablespace Groups

A tablespace group enables a user to consume temporary space from multiple tablespaces. Using a tablespace group, rather than a single temporary tablespace, can alleviate problems caused where one tablespace is inadequate to hold the results of a sort, particularly on a table that has many partitions. A tablespace group enables parallel execution servers in a single parallel operation to use multiple temporary tablespaces.

A tablespace group has the following characteristics:

- It contains at least one tablespace. There is no explicit limit on the maximum number of tablespaces that are contained in a group.
- It shares the namespace of tablespaces, so its name cannot be the same as any tablespace.
- You can specify a tablespace group name wherever a tablespace name would appear when you assign a default temporary tablespace for the database or a temporary tablespace for a user.

You do not explicitly create a tablespace group. Rather, it is created implicitly when you assign the first temporary tablespace to the group. The group is deleted when the last temporary tablespace it contains is removed from it.

The view `DBA_TABLESPACE_GROUPS` lists tablespace groups and their member tablespaces.

See Also:

[Oracle Database Security Guide](https://docs.oracle.com/cd/E11882_01/network.112/e36292/users.htm#DBSEG10240) for more information about assigning a temporary tablespace or tablespace group to a user

#### Creating a Tablespace Group

You create a tablespace group implicitly when you include the `TABLESPACE GROUP` clause in the `CREATE TEMPORARY TABLESPACE` or `ALTER TABLESPACE` statement and the specified tablespace group does not currently exist.

For example, if neither `group1` nor `group2` exists, then the following statements create those groups, each of which has only the specified tablespace as a member:

```
CREATE TEMPORARY TABLESPACE lmtemp2 TEMPFILE '/u02/oracle/data/lmtemp201.dbf'
     SIZE 50M
     TABLESPACE GROUP group1;

ALTER TABLESPACE lmtemp TABLESPACE GROUP group2;
```

#### Changing Members of a Tablespace Group

You can add a tablespace to an existing tablespace group by specifying the existing group name in the `TABLESPACE GROUP` clause of the `CREATE TEMPORARY TABLESPACE` or `ALTER TABLESPACE` statement.

The following statement adds a tablespace to an existing group. It creates and adds tablespace `lmtemp3` to `group1`, so that `group1` contains tablespaces `lmtemp2` and `lmtemp3`.

```
CREATE TEMPORARY TABLESPACE lmtemp3 TEMPFILE '/u02/oracle/data/lmtemp301.dbf'
     SIZE 25M
     TABLESPACE GROUP group1;
```

The following statement also adds a tablespace to an existing group, but in this case because tablespace `lmtemp2` already belongs to `group1`, it is in effect moved from `group1` to `group2`:

```
ALTER TABLESPACE lmtemp2 TABLESPACE GROUP group2;
```

Now `group2` contains both `lmtemp` and `lmtemp2`, while `group1` consists of only `tmtemp3`.

You can remove a tablespace from a group as shown in the following statement:

```
ALTER TABLESPACE lmtemp3 TABLESPACE GROUP '';
```

Tablespace `lmtemp3` no longer belongs to any group. Further, since there are no longer any members of `group1`, this results in the implicit deletion of `group1`.

#### Assigning a Tablespace Group as the Default Temporary Tablespace

Use the `ALTER DATABASE...DEFAULT` `TEMPORARY` `TABLESPACE` statement to assign a tablespace group as the default temporary tablespace for the database. For example:

```
ALTER DATABASE DEFAULT TEMPORARY TABLESPACE group2;
```

Any user who has not explicitly been assigned a temporary tablespace will now use tablespaces `lmtemp` and `lmtemp2`.

If a tablespace group is specified as the default temporary tablespace, you cannot drop any of its member tablespaces. You must first remove the tablespace from the tablespace group. Likewise, you cannot drop a single temporary tablespace as long as it is the default temporary tablespace.

## Specifying Nonstandard Block Sizes for Tablespaces

You can create tablespaces with block sizes different from the standard database block size, which is specified by the `DB_BLOCK_SIZE` initialization parameter. This feature lets you transport tablespaces with unlike block sizes between databases.

Use the `BLOCKSIZE` clause of the `CREATE TABLESPACE` statement to create a tablespace with a block size different from the database standard block size. In order for the `BLOCKSIZE` clause to succeed, you must have already set the `DB_CACHE_SIZE` and at least one `DB_nK_CACHE_SIZE` initialization parameter. Further, and the integer you specify in the `BLOCKSIZE` clause must correspond with the setting of one `DB_nK_CACHE_SIZE` parameter setting. Although redundant, specifying a `BLOCKSIZE` equal to the standard block size, as specified by the `DB_BLOCK_SIZE` initialization parameter, is allowed.

The following statement creates tablespace `lmtbsb`, but specifies a block size that differs from the standard database block size (as specified by the `DB_BLOCK_SIZE` initialization parameter):

```
CREATE TABLESPACE lmtbsb DATAFILE '/u02/oracle/data/lmtbsb01.dbf' SIZE 50M
    EXTENT MANAGEMENT LOCAL UNIFORM SIZE 128K
    BLOCKSIZE 8K;
```

See Also:

- ["Specifying Database Block Sizes"](create.md)
- ["Setting the Buffer Cache Initialization Parameters"](memory.md) for information about the `DB_CACHE_SIZE` and `DB_nK_CACHE_SIZE` parameter settings
- "Transporting Tablespaces Between Databases"

## Controlling the Writing of Redo Records

For some database operations, you can control whether the database generates redo records. Without redo, no media recovery is possible. However, suppressing redo generation can improve performance, and may be appropriate for easily recoverable operations. An example of such an operation is a `CREATE TABLE...AS SELECT` statement, which can be repeated in case of database or instance failure.

Specify the `NOLOGGING` clause in the `CREATE TABLESPACE` statement to suppress redo when these operations are performed for objects within the tablespace. If you do not include this clause, or if you specify `LOGGING` instead, then the database generates redo when changes are made to objects in the tablespace. Redo is never generated for temporary segments or in temporary tablespaces, regardless of the logging attribute.

The logging attribute specified at the tablespace level is the default attribute for objects created within the tablespace. You can override this default logging attribute by specifying `LOGGING` or `NOLOGGING` at the schema object level--for example, in a `CREATE TABLE` statement.

If you have a standby database, `NOLOGGING` mode causes problems with the availability and accuracy of the standby database. To overcome this problem, you can specify `FORCE LOGGING` mode. When you include the `FORCE LOGGING` clause in the `CREATE TABLESPACE` statement, you force the generation of redo records for all operations that make changes to objects in a tablespace. This overrides any specification made at the object level.

If you transport a tablespace that is in `FORCE LOGGING` mode to another database, the new tablespace will not maintain the `FORCE LOGGING` mode.

See Also:

- [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/clauses005.htm#SQLRF30009) for information about operations that can be done in `NOLOGGING` mode
- ["Specifying FORCE LOGGING Mode"](create.md) for more information about `FORCE LOGGING` mode and for information about the effects of the `FORCE LOGGING` clause used with the `CREATE DATABASE` statement

## Altering Tablespace Availability

You can take an online tablespace offline so that it is temporarily unavailable for general use. The rest of the database remains open and available for users to access data. Conversely, you can bring an offline tablespace online to make the schema objects within the tablespace available to database users. The database must be open to alter the availability of a tablespace.

To alter the availability of a tablespace, use the `ALTER TABLESPACE` statement. You must have the `ALTER TABLESPACE` or `MANAGE TABLESPACE` system privilege.

See Also:

["Altering Data File Availability"](dfiles.md) for information about altering the availability of individual data files within a tablespace

### Taking Tablespaces Offline

You may want to take a tablespace offline for any of the following reasons:

- To make a portion of the database unavailable while allowing normal access to the remainder of the database
- To perform an offline tablespace backup (even though a tablespace can be backed up while online and in use)
- To make an application and its group of tables temporarily unavailable while updating or maintaining the application
- To rename or relocate tablespace data files
	See ["Renaming and Relocating Data Files"](dfiles.md) for details.

When a tablespace is taken offline, the database takes all the associated files offline.

You cannot take the following tablespaces offline:

- `SYSTEM`
- The undo tablespace
- Temporary tablespaces

Before taking a tablespace offline, consider altering the tablespace allocation of any users who have been assigned the tablespace as a default tablespace. Doing so is advisable because those users will not be able to access objects in the tablespace while it is offline.

You can specify any of the following parameters as part of the `ALTER TABLESPACE...OFFLINE` statement:

| Clause | Description |
| --- | --- |
| `NORMAL` | A tablespace can be taken offline normally if no error conditions exist for any of the data files of the tablespace. No data file in the tablespace can be currently offline as the result of a write error. When you specify `OFFLINE NORMAL`, the database takes a checkpoint for all data files of the tablespace as it takes them offline. `NORMAL` is the default. |
| `TEMPORARY` | A tablespace can be taken offline temporarily, even if there are error conditions for one or more files of the tablespace. When you specify `OFFLINE TEMPORARY`, the database takes offline the data files that are not already offline, checkpointing them as it does so.  If no files are offline, but you use the temporary clause, media recovery is not required to bring the tablespace back online. However, if one or more files of the tablespace are offline because of write errors, and you take the tablespace offline temporarily, the tablespace requires recovery before you can bring it back online. |
| `IMMEDIATE` | A tablespace can be taken offline immediately, without the database taking a checkpoint on any of the data files. When you specify `OFFLINE IMMEDIATE`, media recovery for the tablespace is required before the tablespace can be brought online. You cannot take a tablespace offline immediately if the database is running in `NOARCHIVELOG` mode. |

Caution:

If you must take a tablespace offline, use the `NORMAL` clause (the default) if possible. This setting guarantees that the tablespace will not require recovery to come back online, even if after incomplete recovery you reset the redo log sequence using an `ALTER DATABASE OPEN RESETLOGS` statement.

Specify `TEMPORARY` only when you cannot take the tablespace offline normally. In this case, only the files taken offline because of errors need to be recovered before the tablespace can be brought online. Specify `IMMEDIATE` only after trying both the normal and temporary settings.

The following example takes the `users` tablespace offline normally:

```
ALTER TABLESPACE users OFFLINE NORMAL;
```

### Bringing Tablespaces Online

You can bring any tablespace in an Oracle Database online whenever the database is open. A tablespace is normally online so that the data contained within it is available to database users.

If a tablespace to be brought online was not taken offline "cleanly" (that is, using the `NORMAL` clause of the `ALTER TABLESPACE OFFLINE` statement), you must first perform media recovery on the tablespace before bringing it online. Otherwise, the database returns an error and the tablespace remains offline.

See Also:

[Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/cd/E11882_01/backup.112/e10642/toc.htm) for information about performing media recovery

The following statement brings the `users` tablespace online:

```
ALTER TABLESPACE users ONLINE;
```

## Using Read-Only Tablespaces

Making a tablespace read-only prevents write operations on the data files in the tablespace. The primary purpose of read-only tablespaces is to eliminate the need to perform backup and recovery of large, static portions of a database. Read-only tablespaces also provide a way to protecting historical data so that users cannot modify it. Making a tablespace read-only prevents updates on all tables in the tablespace, regardless of a user's update privilege level.

Note:

Making a tablespace read-only cannot in itself be used to satisfy archiving or data publishing requirements, because the tablespace can only be brought online in the database in which it was created. However, you can meet such requirements by using the transportable tablespace feature, as described in "Transporting Tablespaces Between Databases".

You can drop items, such as tables or indexes, from a read-only tablespace, but you cannot create or alter objects in a read-only tablespace. You can execute statements that update the file description in the data dictionary, such as `ALTER TABLE...ADD` or `ALTER TABLE...MODIFY`, but you will not be able to use the new description until the tablespace is made read/write.

Read-only tablespaces can be transported to other databases. And, since read-only tablespaces can never be updated, they can reside on CD-ROM or WORM (Write Once-Read Many) devices.

The following topics are discussed in this section:

- Making a Tablespace Read-Only
- Making a Read-Only Tablespace Writable
- Creating a Read-Only Tablespace on a WORM Device
- Delaying the Opening of Data Files in Read-Only Tablespaces
	See Also:
	"Transporting Tablespaces Between Databases"

### Making a Tablespace Read-Only

All tablespaces are initially created as read/write. Use the `READ ONLY` clause in the `ALTER TABLESPACE` statement to change a tablespace to read-only. You must have the `ALTER TABLESPACE` or `MANAGE TABLESPACE` system privilege.

Before you can make a tablespace read-only, the following conditions must be met.

- The tablespace must be online. This is necessary to ensure that there is no undo information that must be applied to the tablespace.
- The tablespace cannot be the active undo tablespace or `SYSTEM` tablespace.
- The tablespace must not currently be involved in an online backup, because the end of a backup updates the header file of all data files in the tablespace.
- The tablespace cannot be a temporary tablespace.

For better performance while accessing data in a read-only tablespace, you can issue a query that accesses all of the blocks of the tables in the tablespace just before making it read-only. A simple query, such as `SELECT COUNT (*)`, executed against each table ensures that the data blocks in the tablespace can be subsequently accessed most efficiently. This eliminates the need for the database to check the status of the transactions that most recently modified the blocks.

The following statement makes the `flights` tablespace read-only:

```
ALTER TABLESPACE flights READ ONLY;
```

You can issue the `ALTER TABLESPACE...READ ONLY` statement while the database is processing transactions. After the statement is issued, the tablespace is put into a transitional read-only mode, and the `ALTER` command waits for existing transactions to complete by committing or by rolling back. No further DML operations are allowed to the tablespace, and if a DML statement attempts further changes, then an error is returned.

The `ALTER TABLESPACE...READ ONLY` statement waits for the following transactions to either commit or roll back before returning: transactions that have pending or uncommitted changes to the tablespace and that were started before you issued the statement. If a transaction started before the statement remains active, but rolls back to a savepoint, rolling back its changes to the tablespace, then the statement no longer waits for this active transaction.

If you find it is taking a long time for the `ALTER TABLESPACE` statement to complete, then you can identify the transactions that are preventing the read-only state from taking effect. You can then notify the owners of those transactions and decide whether to terminate the transactions, if necessary.

The following example identifies the transaction entry for the `ALTER TABLESPACE...READ ONLY` statement and displays its session address (`saddr`):

```
SELECT SQL_TEXT, SADDR 
    FROM V$SQLAREA,V$SESSION
    WHERE V$SQLAREA.ADDRESS = V$SESSION.SQL_ADDRESS    
        AND SQL_TEXT LIKE 'alter tablespace%'; 

SQL_TEXT                                 SADDR   
---------------------------------------- --------
alter tablespace tbs1 read only          80034AF0
```

The start SCN of each active transaction is stored in the `V$TRANSACTION` view. Displaying this view sorted by ascending start SCN lists the transactions in execution order. From the preceding example, you already know the session address of the transaction entry for the read-only statement, and you can now locate it in the `V$TRANSACTION` view. All transactions with smaller start SCN, which indicates an earlier execution, can potentially hold up the quiesce and subsequent read-only state of the tablespace.

```
SELECT SES_ADDR, START_SCNB 
    FROM V$TRANSACTION
    ORDER BY START_SCNB;

SES_ADDR START_SCNB
-------- ----------
800352A0       3621   --> waiting on this txn
80035A50       3623   --> waiting on this txn
80034AF0       3628   --> this is the ALTER TABLESPACE statement
80037910       3629   --> don't care about this txn
```

You can now find the owners of the blocking transactions.

```
SELECT T.SES_ADDR, S.USERNAME, S.MACHINE
   FROM V$SESSION S, V$TRANSACTION T
   WHERE T.SES_ADDR = S.SADDR
   ORDER BY T.SES_ADDR

SES_ADDR USERNAME             MACHINE
-------- -------------------- --------------------
800352A0 DAVIDB               DAVIDBLAP             --> Contact this user
80035A50 MIKEL                LAB61                 --> Contact this user
80034AF0 DBA01                STEVEFLAP           
80037910 NICKD                NICKDLAP
```

After making the tablespace read-only, it is advisable to back it up immediately. As long as the tablespace remains read-only, no further backups of the tablespace are necessary, because no changes can be made to it.

See Also:

[Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/cd/E11882_01/backup.112/e10642/toc.htm)

### Making a Read-Only Tablespace Writable

Use the `READ WRITE` keywords in the `ALTER TABLESPACE` statement to change a tablespace to allow write operations. You must have the `ALTER TABLESPACE` or `MANAGE TABLESPACE` system privilege.

A prerequisite to making the tablespace read/write is that all of the data files in the tablespace, as well as the tablespace itself, must be online. Use the `DATAFILE...ONLINE` clause of the `ALTER DATABASE` statement to bring a data file online. The `V$DATAFILE` view lists the current status of data files.

The following statement makes the `flights` tablespace writable:

```
ALTER TABLESPACE flights READ WRITE;
```

Making a read-only tablespace writable updates the control file entry for the data files, so that you can use the read-only version of the data files as a starting point for recovery.

### Creating a Read-Only Tablespace on a WORM Device

Follow these steps to create a read-only tablespace on a CD-ROM or WORM (Write Once-Read Many) device.

1. Create a writable tablespace on another device. Create the objects that belong in the tablespace and insert your data.
2. Alter the tablespace to make it read-only.
3. Copy the data files of the tablespace onto the WORM device. Use operating system commands to copy the files.
4. Take the tablespace offline.
5. Rename the data files to coincide with the names of the data files you copied onto your WORM device. Use `ALTER TABLESPACE` with the `RENAME DATAFILE` clause. Renaming the data files changes their names in the control file.
6. Bring the tablespace back online.

### Delaying the Opening of Data Files in Read-Only Tablespaces

When substantial portions of a very large database are stored in read-only tablespaces that are located on slow-access devices or hierarchical storage, you should consider setting the `READ_ONLY_OPEN_DELAYED` initialization parameter to `TRUE`. This speeds certain operations, primarily opening the database, by causing data files in read-only tablespaces to be accessed for the first time only when an attempt is made to read data stored within them.

Setting `READ_ONLY_OPEN_DELAYED=TRUE` has the following side-effects:

- A missing or bad read-only file is not detected at open time. It is only discovered when there is an attempt to access it.
- `ALTER SYSTEM CHECK DATAFILES` does not check read-only files.
- `ALTER TABLESPACE...ONLINE` and `ALTER DATABASE` `DATAFILE...ONLINE` do not check read-only files. They are checked only upon the first access.
- `V$RECOVER_FILE`, `V$BACKUP`, and `V$DATAFILE_HEADER` do not access read-only files. Read-only files are indicated in the results list with the error " `DELAYED OPEN` ", with zeroes for the values of other columns.
- `V$DATAFILE` does not access read-only files. Read-only files have a size of "0" listed.
- `V$RECOVERY_LOG` does not access read-only files. Logs they could need for recovery are not added to the list.
- `ALTER DATABASE NOARCHIVELOG` does not access read-only files.It proceeds even if there is a read-only file that requires recovery.
	Notes:
	- `RECOVER DATABASE` and `ALTER DATABASE OPEN RESETLOGS` continue to access all read-only data files regardless of the parameter value. To avoid accessing read-only files for these operations, take those files offline.
	- If a backup control file is used, the read-only status of some files may be inaccurate. This can cause some of these operations to return unexpected results. Care should be taken in this situation.

## Altering and Maintaining Tablespaces

This section covers various subjects that relate to altering and maintaining tablespaces.

This section covers the following topics:

- Increasing the Size of a Tablespace
- Altering a Locally Managed Tablespace
- Altering a Bigfile Tablespace
- Altering a Locally Managed Temporary Tablespace
- Shrinking a Locally Managed Temporary Tablespace

### Increasing the Size of a Tablespace

You can increase the size of a tablespace by either increasing the size of a data file in the tablespace or adding one. See ["Changing Data File Size"](dfiles.md) and ["Creating Data Files and Adding Data Files to a Tablespace"](dfiles.md) for more information.

Additionally, you can enable automatic file extension (`AUTOEXTEND`) to data files and bigfile tablespaces. See ["Enabling and Disabling Automatic Extension for a Data File"](dfiles.md).

### Altering a Locally Managed Tablespace

You cannot alter a locally managed tablespace to a locally managed temporary tablespace, nor can you change its method of segment space management. Coalescing free extents is unnecessary for locally managed tablespaces. However, you can use the `ALTER TABLESPACE` statement on locally managed tablespaces for some operations, including the following:

- Adding a data file. For example:
	```
	ALTER TABLESPACE lmtbsb
	   ADD DATAFILE '/u02/oracle/data/lmtbsb02.dbf' SIZE 1M;
	```
- Altering tablespace availability (`ONLINE` / `OFFLINE`). See "Altering Tablespace Availability".
- Making a tablespace read-only or read/write. See "Using Read-Only Tablespaces".
- Renaming a data file, or enabling or disabling the autoextension of the size of a data file in the tablespace. See [Chapter 15, "Managing Data Files and Temp Files"](dfiles.md).

### Altering a Bigfile Tablespace

Two clauses of the `ALTER TABLESPACE` statement support data file transparency when you are using bigfile tablespaces:

- `RESIZE`: The `RESIZE` clause lets you resize the single data file in a bigfile tablespace to an absolute size, without referring to the data file. For example:
	```
	ALTER TABLESPACE bigtbs RESIZE 80G;
	```
- `AUTOEXTEND` (used outside of the `ADD` `DATAFILE` clause):
	With a bigfile tablespace, you can use the `AUTOEXTEND` clause outside of the `ADD` `DATAFILE` clause. For example:
	```
	ALTER TABLESPACE bigtbs AUTOEXTEND ON NEXT 20G;
	```

An error is raised if you specify an `ADD` `DATAFILE` clause for a bigfile tablespace.

### Altering a Locally Managed Temporary Tablespace

Note:

You cannot use the `ALTER TABLESPACE` statement, with the `TEMPORARY` keyword, to change a locally managed permanent tablespace into a locally managed temporary tablespace. You must use the `CREATE TEMPORARY TABLESPACE` statement to create a locally managed temporary tablespace.

You can use `ALTER TABLESPACE` to add a temp file, take a temp file offline, or bring a temp file online, as illustrated in the following examples:

```
ALTER TABLESPACE lmtemp
   ADD TEMPFILE '/u02/oracle/data/lmtemp02.dbf' SIZE 18M REUSE;

ALTER TABLESPACE lmtemp TEMPFILE OFFLINE;
ALTER TABLESPACE lmtemp TEMPFILE ONLINE;
```

Note:

You cannot take a temporary tablespace offline. Instead, you take its temp file offline. The view `V$TEMPFILE` displays online status for a temp file.

The `ALTER DATABASE` statement can be used to alter temp files.

The following statements take offline and bring online temp files. They behave identically to the last two `ALTER` `TABLESPACE` statements in the previous example.

```
ALTER DATABASE TEMPFILE '/u02/oracle/data/lmtemp02.dbf' OFFLINE;
ALTER DATABASE TEMPFILE '/u02/oracle/data/lmtemp02.dbf' ONLINE;
```

The following statement resizes a temp file:

```
ALTER DATABASE TEMPFILE '/u02/oracle/data/lmtemp02.dbf' RESIZE 18M;
```

The following statement drops a temp file and deletes its operating system file:

```
ALTER DATABASE TEMPFILE '/u02/oracle/data/lmtemp02.dbf' DROP
    INCLUDING DATAFILES;
```

The tablespace to which this temp file belonged remains. A message is written to the alert log for the temp file that was deleted. If an operating system error prevents the deletion of the file, the statement still succeeds, but a message describing the error is written to the alert log.

It is also possible to use the `ALTER DATABASE` statement to enable or disable the automatic extension of an existing temp file, and to rename a temp file. See [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_1004.htm#SQLRF00802) for the required syntax.

Note:

To rename a temp file, you take the temp file offline, use operating system commands to rename or relocate the temp file, and then use the `ALTER` `DATABASE` `RENAME` `FILE` command to update the database control files.

### Shrinking a Locally Managed Temporary Tablespace

Large sort operations performed by the database may result in a temporary tablespace growing and occupying a considerable amount of disk space. After the sort operation completes, the extra space is not released; it is just marked as free and available for reuse. Therefore, a single large sort operation might result in a large amount of allocated temporary space that remains unused after the sort operation is complete. For this reason, the database enables you to shrink locally managed temporary tablespaces and release unused space.

You use the `SHRINK SPACE` clause of the `ALTER TABLESPACE` statement to shrink a temporary tablespace, or the `SHRINK TEMPFILE` clause of the `ALTER TABLESPACE` statement to shrink a specific temp file of a temporary tablespace. Shrinking frees as much space as possible while maintaining the other attributes of the tablespace or temp file. The optional `KEEP` clause defines a minimum size for the tablespace or temp file.

Shrinking is an online operation, which means that user sessions can continue to allocate sort extents if needed, and already-running queries are not affected.

The following example shrinks the locally managed temporary tablespace `lmtmp1` while ensuring a minimum size of 20M.

```
ALTER TABLESPACE lmtemp1 SHRINK SPACE KEEP 20M;
```

The following example shrinks the temp file `lmtemp02.dbf` of the locally managed temporary tablespace `lmtmp2`. Because the `KEEP` clause is omitted, the database attempts to shrink the temp file to the minimum possible size.

```
ALTER TABLESPACE lmtemp2 SHRINK TEMPFILE '/u02/oracle/data/lmtemp02.dbf';
```

## Renaming Tablespaces

Using the `RENAME TO` clause of the `ALTER TABLESPACE`, you can rename a permanent or temporary tablespace. For example, the following statement renames the `users` tablespace:

```
ALTER TABLESPACE users RENAME TO usersts;
```

When you rename a tablespace the database updates all references to the tablespace name in the data dictionary, control file, and (online) data file headers. The database does not change the tablespace ID so if this tablespace were, for example, the default tablespace for a user, then the renamed tablespace would show as the default tablespace for the user in the `DBA_USERS` view.

The following affect the operation of this statement:

- The `COMPATIBLE` parameter must be set to 10.0.0 or higher.
- If the tablespace being renamed is the `SYSTEM` tablespace or the `SYSAUX` tablespace, then it will not be renamed and an error is raised.
- If any data file in the tablespace is offline, or if the tablespace is offline, then the tablespace is not renamed and an error is raised.
- If the tablespace is read only, then data file headers are not updated. This should not be regarded as corruption; instead, it causes a message to be written to the alert log indicating that data file headers have not been renamed. The data dictionary and control file are updated.
- If the tablespace is the default temporary tablespace, then the corresponding entry in the database properties table is updated and the `DATABASE_PROPERTIES` view shows the new name.
- If the tablespace is an undo tablespace and if the following conditions are met, then the tablespace name is changed to the new tablespace name in the server parameter file (`SPFILE`).
	- The server parameter file was used to start up the database.
		- The tablespace name is specified as the `UNDO_TABLESPACE` for any instance.
	If a traditional initialization parameter file (`PFILE`) is being used then a message is written to the alert log stating that the initialization parameter file must be manually changed.

## Dropping Tablespaces

You can drop a tablespace and its contents (the segments contained in the tablespace) from the database if the tablespace and its contents are no longer required. You must have the `DROP` `TABLESPACE` system privilege to drop a tablespace.

Caution:

Once a tablespace has been dropped, the data in the tablespace is not recoverable. Therefore, ensure that all data contained in a tablespace to be dropped will not be required in the future. Also, immediately before and after dropping a tablespace from a database, back up the database completely. This is strongly recommended so that you can recover the database if you mistakenly drop a tablespace, or if the database experiences a problem in the future after the tablespace has been dropped.

When you drop a tablespace, the file pointers in the control file of the associated database are removed. You can optionally direct Oracle Database to delete the operating system files (data files) that constituted the dropped tablespace. If you do not direct the database to delete the data files at the same time that it deletes the tablespace, you must later use the appropriate commands of your operating system to delete them.

You cannot drop a tablespace that contains any active segments. For example, if a table in the tablespace is currently being used or the tablespace contains undo data needed to roll back uncommitted transactions, you cannot drop the tablespace. The tablespace can be online or offline, but it is best to take the tablespace offline before dropping it.

To drop a tablespace, use the `DROP TABLESPACE` statement. The following statement drops the `users` tablespace, including the segments in the tablespace:

```
DROP TABLESPACE users INCLUDING CONTENTS;
```

If the tablespace is empty (does not contain any tables, views, or other structures), you do not need to specify the `INCLUDING CONTENTS` clause. Use the `CASCADE CONSTRAINTS` clause to drop all referential integrity constraints from tables outside the tablespace that refer to primary and unique keys of tables inside the tablespace.

To delete the data files associated with a tablespace at the same time that the tablespace is dropped, use the `INCLUDING CONTENTS AND DATAFILES` clause. The following statement drops the `users` tablespace and its associated data files:

```
DROP TABLESPACE users INCLUDING CONTENTS AND DATAFILES;
```

A message is written to the alert log for each data file that is deleted. If an operating system error prevents the deletion of a file, the `DROP TABLESPACE` statement still succeeds, but a message describing the error is written to the alert log.

See Also:

["Dropping Data Files"](dfiles.md)

## Managing the SYSAUX Tablespace

The `SYSAUX` tablespace was installed as an auxiliary tablespace to the `SYSTEM` tablespace when you created your database. Some database components that formerly created and used separate tablespaces now occupy the `SYSAUX` tablespace.

If the `SYSAUX` tablespace becomes unavailable, core database functionality will remain operational. The database features that use the `SYSAUX` tablespace could fail, or function with limited capability.

### Monitoring Occupants of the SYSAUX Tablespace

The list of registered occupants of the `SYSAUX` tablespace are discussed in ["About the SYSAUX Tablespace"](create.md). These components can use the `SYSAUX` tablespace, and their installation provides the means of establishing their occupancy of the `SYSAUX` tablespace.

You can monitor the occupants of the `SYSAUX` tablespace using the `V$SYSAUX_OCCUPANTS` view. This view lists the following information about the occupants of the `SYSAUX` tablespace:

- Name of the occupant
- Occupant description
- Schema name
- Move procedure
- Current space usage

View information is maintained by the occupants.

See Also:

[Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_3089.htm#REFRN30271) for a detailed description of the `V$SYSAUX_OCCUPANTS` view

### Moving Occupants Out Of or Into the SYSAUX Tablespace

You will have an option at component install time to specify that you do not want the component to reside in `SYSAUX`. Also, if you later decide that the component should be relocated to a designated tablespace, you can use the move procedure for that component, as specified in the `V$SYSAUX_OCCUPANTS` view, to perform the move.

The move procedure also lets you move a component from another tablespace into the `SYSAUX` tablespace.

### Controlling the Size of the SYSAUX Tablespace

The `SYSAUX` tablespace is occupied by several database components, and its total size is governed by the space consumed by those components. The space consumed by the components, in turn, depends on which features or functionality are being used and on the nature of the database workload.

The largest portion of the `SYSAUX` tablespace is occupied by the Automatic Workload Repository (AWR). The space consumed by the AWR is determined by several factors, including the number of active sessions in the system at any given time, the snapshot interval, and the historical data retention period. A typical system with an average of 10 concurrent active sessions may require approximately 200 to 300 MB of space for its AWR data.

The following table provides guidelines on sizing the `SYSAUX` tablespace based on the system configuration and expected load.

| Parameter/Recommendation | Small | Medium | Large |
| --- | --- | --- | --- |
| Number of CPUs | 2 | 8 | 32 |
| Number of concurrently active sessions | 10 | 20 | 100 |
| Number of user objects: tables and indexes | 500 | 5,000 | 50,000 |
| Estimated `SYSAUX` size at steady state with default configuration | 500 MB | 2 GB | 5 GB |

You can control the size of the AWR by changing the snapshot interval and historical data retention period. For more information on managing the AWR snapshot interval and retention period, see [Oracle Database Performance Tuning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41573/autostat.htm#PFGRF02601).

Another major occupant of the `SYSAUX` tablespace is the embedded Oracle Enterprise Manager repository. This repository is used by Oracle Enterprise Manager Database Control to store its metadata. The size of this repository depends on database activity and on configuration-related information stored in the repository.

Other database components in the `SYSAUX` tablespace will grow in size only if their associated features (for example, Oracle Text and Oracle Streams) are in use. If the features are not used, then these components do not have any significant effect on the size of the `SYSAUX` tablespace.

## Diagnosing and Repairing Locally Managed Tablespace Problems

Oracle Database includes the `DBMS_SPACE_ADMIN` package, which is a collection of aids for diagnosing and repairing problems in locally managed tablespaces.

DBMS\_SPACE\_ADMIN Package Procedures

The following table lists the `DBMS_SPACE_ADMIN` package procedures. See [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/d_spadmn.htm#ARPLS057) for details on each procedure.

| Procedure | Description |
| --- | --- |
| `ASSM_SEGMENT_VERIFY` | Verifies the integrity of segments created in tablespaces that have automatic segment space management enabled. Outputs a dump file named `sid` `_ora_` `process_id`.`trc` to the location that corresponds to the `Diag` `Trace` entry in the `V$DIAG_INFO` view.  Use `SEGMENT_VERIFY` for tablespaces with manual segment space management. |
| `ASSM_TABLESPACE_VERIFY` | Verifies the integrity of tablespaces that have automatic segment space management enabled. Outputs a dump file named `sid` `_ora_` `process_id`.`trc` to the location that corresponds to the `Diag` `Trace` entry in the `V$DIAG_INFO` view.  Use `TABLESPACE_VERIFY` for tablespaces with manual segment space management. |
| `DROP_EMPTY_SEGMENTS` | Drops segments from empty tables or table partitions and dependent objects |
| `MATERIALIZE_DEFERRED_SEGMENTS` | Materializes segments for tables and table partitions with deferred segment creation and their dependent objects. |
| `SEGMENT_CORRUPT` | Marks the segment corrupt or valid so that appropriate error recovery can be done |
| `SEGMENT_DROP_CORRUPT` | Drops a segment currently marked corrupt (without reclaiming space) |
| `SEGMENT_DUMP` | Dumps the segment header and bitmap blocks of a specific segment to a dump file named `sid` `_ora_` `process_id`.`trc` in the location that corresponds to the `Diag` `Trace` entry in the `V$DIAG_INFO` view. Provides an option to select a slightly abbreviated dump, which includes segment header and includes bitmap block summaries, without percent-free states of each block. |
| `SEGMENT_VERIFY` | Verifies the consistency of the extent map of the segment |
| `TABLESPACE_FIX_BITMAPS` | Marks the appropriate DBA range (extent) as free or used in bitmap |
| `TABLESPACE_FIX_SEGMENT_STATES` | Fixes the state of the segments in a tablespace in which migration was stopped |
| `TABLESPACE_MIGRATE_FROM_LOCAL` | Migrates a locally managed tablespace to dictionary-managed tablespace |
| `TABLESPACE_MIGRATE_TO_LOCAL` | Migrates a dictionary-managed tablespace to a locally managed tablespace |
| `TABLESPACE_REBUILD_BITMAPS` | Rebuilds the appropriate bitmaps |
| `TABLESPACE_REBUILD_QUOTAS` | Rebuilds quotas for a specific tablespace |
| `TABLESPACE_RELOCATE_BITMAPS` | Relocates the bitmaps to the specified destination |
| `TABLESPACE_VERIFY` | Verifies that the bitmaps and extent maps for the segments in the tablespace are synchronized |

The following scenarios describe typical situations in which you can use the `DBMS_SPACE_ADMIN` package to diagnose and resolve problems.

Note:

Some of these procedures can result in lost and unrecoverable data if not used properly. You should work with Oracle Support Services if you have doubts about these procedures.

See Also:

- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/d_spadmn.htm#ARPLS057) for details about the `DBMS_SPACE_ADMIN` package
- ["Viewing ADR Locations with the V$DIAG\_INFO View"](diag.md)

### Scenario 1: Fixing Bitmap When Allocated Blocks are Marked Free (No Overlap)

The `TABLESPACE_VERIFY` procedure discovers that a segment has allocated blocks that are marked free in the bitmap, but no overlap between segments is reported.

In this scenario, perform the following tasks:

1. Call the `SEGMENT_DUMP` procedure to dump the ranges that the administrator allocated to the segment.
2. For each range, call the `TABLESPACE_FIX_BITMAPS` procedure with the `TABLESPACE_EXTENT_MAKE_USED` option to mark the space as used.
3. Call `TABLESPACE_REBUILD_QUOTAS` to rebuild quotas.

### Scenario 2: Dropping a Corrupted Segment

You cannot drop a segment because the bitmap has segment blocks marked "free". The system has automatically marked the segment corrupted.

In this scenario, perform the following tasks:

1. Call the `SEGMENT_VERIFY` procedure with the `SEGMENT_VERIFY_EXTENTS_GLOBAL` option. If no overlaps are reported, then proceed with steps 2 through 5.
2. Call the `SEGMENT_DUMP` procedure to dump the DBA ranges allocated to the segment.
3. For each range, call `TABLESPACE_FIX_BITMAPS` with the `TABLESPACE_EXTENT_MAKE_FREE` option to mark the space as free.
4. Call `SEGMENT_DROP_CORRUPT` to drop the `SEG$` entry.
5. Call `TABLESPACE_REBUILD_QUOTAS` to rebuild quotas.

### Scenario 3: Fixing Bitmap Where Overlap is Reported

The `TABLESPACE_VERIFY` procedure reports some overlapping. Some of the real data must be sacrificed based on previous internal errors.

After choosing the object to be sacrificed, in this case say, table `t1`, perform the following tasks:

1. Make a list of all objects that `t1` overlaps.
2. Drop table `t1`. If necessary, follow up by calling the `SEGMENT_DROP_CORRUPT` procedure.
3. Call the `SEGMENT_VERIFY` procedure on all objects that `t1` overlapped. If necessary, call the `TABLESPACE_FIX_BITMAPS` procedure to mark appropriate bitmap blocks as used.
4. Rerun the `TABLESPACE_VERIFY` procedure to verify that the problem is resolved.

### Scenario 4: Correcting Media Corruption of Bitmap Blocks

A set of bitmap blocks has media corruption.

In this scenario, perform the following tasks:

1. Call the `TABLESPACE_REBUILD_BITMAPS` procedure, either on all bitmap blocks, or on a single block if only one is corrupt.
2. Call the `TABLESPACE_REBUILD_QUOTAS` procedure to rebuild quotas.
3. Call the `TABLESPACE_VERIFY` procedure to verify that the bitmaps are consistent.

### Scenario 5: Migrating from a Dictionary-Managed to a Locally Managed Tablespace

Use the `TABLESPACE_MIGRATE_TO_LOCAL` procedure to migrate a dictionary-managed tablespace to a locally managed tablespace. This operation is done online, but space management operations are blocked until the migration has been completed. Therefore, you can read or modify data while the migration is in progress, but if you are loading a large amount of data that requires the allocation of additional extents, then the operation may be blocked.

Assume that the database block size is 2K and the existing extent sizes in tablespace `tbs_1` are 10, 50, and 10,000 blocks (used, used, and free). The `MINIMUM EXTENT` value is 20K (10 blocks). Allow the system to choose the bitmap allocation unit. The value of 10 blocks is chosen, because it is the highest common denominator and does not exceed `MINIMUM EXTENT`.

The statement to convert `tbs_1` to a locally managed tablespace is as follows:

```
EXEC DBMS_SPACE_ADMIN.TABLESPACE_MIGRATE_TO_LOCAL ('tbs_1');
```

If you choose to specify an allocation unit size, it must be a factor of the unit size calculated by the system.

## Migrating the SYSTEM Tablespace to a Locally Managed Tablespace

Use the `DBMS_SPACE_ADMIN.TABLESPACE_MIGRATE_TO_LOCAL` procedure to migrate the `SYSTEM` tablespace from dictionary-managed to locally managed.

Before performing the migration the following conditions must be met:

- The database has a default temporary tablespace that is not `SYSTEM.`
- There are no rollback segments in the dictionary-managed tablespace.
- There is at least one online rollback segment in a locally managed tablespace, or if using automatic undo management, an undo tablespace is online.
- All tablespaces other than the tablespace containing the undo space (that is, the tablespace containing the rollback segment or the undo tablespace) are in read-only mode.
- The `SYSAUX` tablespace is offline.
- The system is in restricted mode.
- There is a cold backup of the database.

All of these conditions, except for the cold backup, are enforced by the `TABLESPACE_MIGRATE_TO_LOCAL` procedure.

The following statement performs the migration:

```
SQL> EXECUTE DBMS_SPACE_ADMIN.TABLESPACE_MIGRATE_TO_LOCAL('SYSTEM');
```

Note:

After the `SYSTEM` tablespace is migrated to locally managed, any dictionary-managed tablespaces in the database cannot be made read/write. If you want to use the dictionary-managed tablespaces in read/write mode, then Oracle recommends that you first migrate these tablespaces to locally managed before migrating the `SYSTEM` tablespace.

## Transporting Tablespaces Between Databases

This section describes how to transport tablespaces between databases, and contains the following topics:

- Introduction to Transportable Tablespaces
- About Transporting Tablespaces Across Platforms
- Limitations on Transportable Tablespace Use
- Compatibility Considerations for Transportable Tablespaces
- Transporting Tablespaces Between Databases: A Procedure and Example
- Using Transportable Tablespaces: Scenarios

Note:

You must be using the Enterprise Edition of Oracle Database Release 8i or later to generate a transportable tablespace set. However, you can use any edition of Oracle Database 8i or later to import a transportable tablespace set into an Oracle database on the same platform. To import a transportable tablespace set into an Oracle database on a different platform, both databases must have compatibility set to at least 10.0.0. See "Compatibility Considerations for Transportable Tablespaces" for a discussion of database compatibility for transporting tablespaces across release levels.

### Introduction to Transportable Tablespaces

You can use the Transportable Tablespaces feature to copy a set of tablespaces from one Oracle Database to another.

Note:

This method for transporting tablespaces requires that you place the tablespaces to be transported in read-only mode until you complete the transporting process. If this is undesirable, you can use the Transportable Tablespaces from Backup feature, described in [Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/cd/E11882_01/backup.112/e10642/rcmttbsb.htm#BRADV05141).

The tablespaces being transported can be either dictionary managed or locally managed. Starting with Oracle9i, the transported tablespaces are not required to be of the same block size as the destination database standard block size.

Moving data using transportable tablespaces is much faster than performing either an export/import or unload/load of the same data. This is because the data files containing all of the actual data are just copied to the destination location, and you use Data Pump to transfer only the metadata of the tablespace objects to the new database.

Note:

Beginning with Oracle Database 11g Release 1, you must use Data Pump for transportable tablespaces. The only circumstance under which you can use the original import and export utilities, IMP and EXP, is for a backward migration of XMLType data to a database version 10g Release 2 or earlier. See [Oracle Database Utilities](https://docs.oracle.com/cd/E11882_01/server.112/e22490/toc.htm) for more information on these utilities and to [Oracle XML DB Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e23094/toc.htm) for more information on XMLTypes.

The transportable tablespace feature is useful in several scenarios, including:

- Exporting and importing partitions in data warehousing tables
- Publishing structured data on CDs
- Copying multiple read-only versions of a tablespace on multiple databases
- Archiving historical data
- Performing tablespace point-in-time-recovery (TSPITR)

These scenarios are discussed in "Using Transportable Tablespaces: Scenarios".

There are two ways to transport a tablespace:

- Manually, following the steps described in this section. This involves issuing commands to SQL\*Plus, RMAN, and Data Pump.
- Using the Transport Tablespaces Wizard in Enterprise Manager
	To run the Transport Tablespaces Wizard:
	1. Log in to Enterprise Manager with a user that has the `EXP_FULL_DATABASE` role.
		2. At the top of the Database Home page, click Data Movement to view the Data Movement page.
		3. Under Move Database Files, click Transport Tablespaces.

See Also:

[Oracle Database Data Warehousing Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25554/transport.htm#DWHSG8301) for information about using transportable tablespaces in a data warehousing environment

### About Transporting Tablespaces Across Platforms

Starting with Oracle Database Release 10g, you can transport tablespaces across platforms. This functionality can be used to:

- Allow a database to be migrated from one platform to another
- Provide an easier and more efficient means for content providers to publish structured data and distribute it to customers running Oracle Database on different platforms
- Simplify the distribution of data from a data warehouse environment to data marts, which are often running on smaller platforms
- Enable the sharing of read-only tablespaces between Oracle Database installations on different operating systems or platforms, assuming that your storage system is accessible from those platforms and the platforms all have the same endianness, as described in the sections that follow.

Many, but not all, platforms are supported for cross-platform tablespace transport. You can query the `V$TRANSPORTABLE_PLATFORM` view to see the platforms that are supported, and to determine each platform's endian format (byte ordering). The following query displays the platforms that support cross-platform tablespace transport:

```
SQL> COLUMN PLATFORM_NAME FORMAT A36
SQL> SELECT * FROM V$TRANSPORTABLE_PLATFORM ORDER BY PLATFORM_NAME;

PLATFORM_ID PLATFORM_NAME                        ENDIAN_FORMAT
----------- ------------------------------------ --------------
          6 AIX-Based Systems (64-bit)           Big
         16 Apple Mac OS                         Big
         19 HP IA Open VMS                       Little
         15 HP Open VMS                          Little
          5 HP Tru64 UNIX                        Little
          3 HP-UX (64-bit)                       Big
          4 HP-UX IA (64-bit)                    Big
         18 IBM Power Based Linux                Big
          9 IBM zSeries Based Linux              Big
         10 Linux IA (32-bit)                    Little
         11 Linux IA (64-bit)                    Little
         13 Linux x86 64-bit                     Little
          7 Microsoft Windows IA (32-bit)        Little
          8 Microsoft Windows IA (64-bit)        Little
         12 Microsoft Windows x86 64-bit         Little
         17 Solaris Operating System (x86)       Little
         20 Solaris Operating System (x86-64)    Little
          1 Solaris[tm] OE (32-bit)              Big
          2 Solaris[tm] OE (64-bit)              Big
 
19 rows selected.
```

If the source platform and the destination platform are of different endianness, then an additional step must be done on either the source or destination platform to convert the tablespace being transported to the destination format. If they are of the same endianness, then no conversion is necessary and tablespaces can be transported as if they were on the same platform.

Before a tablespace can be transported to a different platform, the data file header must identify the platform to which it belongs. In an Oracle Database with compatibility set to 10.0.0 or later, you can accomplish this by making the data file read/write at least once.

### Limitations on Transportable Tablespace Use

Be aware of the following limitations as you plan to transport tablespaces:

- The source and the destination databases must use compatible database character sets. That is, one of the following must be true:
	- The database character sets of the source and the target databases are the same.
		- The source database character set is a strict (binary) subset of the target database character set, and the following three conditions are true:
		- The source database is in version 10.1.0.3 or higher.
				- The tablespaces to be transported contain no table columns with character length semantics or the maximum character width is the same in both the source and target database character sets.
				- The tablespaces to be transported contain no columns with the `CLOB` data type, or the source and the target database character sets are both single-byte or both multibyte.
		- The source database character set is a strict (binary) subset of the target database character set, and the following two conditions are true:
		- The source database is in a version lower than 10.1.0.3.
				- The maximum character width is the same in the source and target database character sets.
- The source and the target databases must use compatible national character sets. Specifically, one of the following must be true:
	- The national character sets of the source and target databases are the same.
		- The source database is in version 10.1.0.3 or higher and the tablespaces to be transported contain no columns with `NCHAR`, `NVARCHAR2`, or `NCLOB` data type.
	Note:
	The subset-superset relationship between character sets recognized by Oracle Database is documented in the [Oracle Database Globalization Support Guide](https://docs.oracle.com/cd/E11882_01/server.112/e10729/applocaledata.htm#NLSPG584).
- You cannot transport a tablespace to a destination database that contains a tablespace of the same name. However, before the transport operation, you can rename either the tablespace to be transported or the destination tablespace.
- Objects with underlying objects (such as materialized views) or contained objects (such as partitioned tables) are not transportable unless all of the underlying or contained objects are in the tablespace set.
- Encrypted tablespaces have the following the limitations:
	- Before transporting an encrypted tablespace, you must copy the Oracle wallet manually to the destination database, unless the master encryption key is stored in a Hardware Security Module (HSM) device instead of an Oracle wallet. When copying the wallet, the wallet password remains the same in the destination database. However, it is recommended that you change the password on the destination database so that each database has its own wallet password. See [Oracle Database Advanced Security Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e40393/toc.htm) for information about HSM devices, about determining the location of the Oracle wallet, and about changing the wallet password with Oracle Wallet Manager.
		- You cannot transport an encrypted tablespace to a database that already has an Oracle wallet for transparent data encryption. In this case, you must use Oracle Data Pump to export the tablespace's schema objects and then import them to the destination database. You can optionally take advantage of Oracle Data Pump features that enable you to maintain encryption for the data while it is being exported and imported. See [Oracle Database Utilities](https://docs.oracle.com/cd/E11882_01/server.112/e22490/dp_export.htm#SUTIL200) for more information.
		- You cannot transport an encrypted tablespace to a platform with different endianness.
- Tablespaces that do not use block encryption but that contain tables with encrypted columns cannot be transported. You must use Oracle Data Pump to export and import the tablespace's schema objects. You can take advantage of Oracle Data Pump features that enable you to maintain encryption for the data while it is being exported and imported. See [Oracle Database Utilities](https://docs.oracle.com/cd/E11882_01/server.112/e22490/dp_export.htm#SUTIL200) for more information.
- Beginning with Oracle Database 10g Release 2, you can transport tablespaces that contain XMLTypes. Beginning with Oracle Database 11g Release 1, you must use only Data Pump to export and import the tablespace metadata for tablespaces that contain XMLTypes.
	The following query returns a list of tablespaces that contain XMLTypes:
	```
	select distinct p.tablespace_name from dba_tablespaces p, 
	  dba_xml_tables x, dba_users u, all_all_tables t where
	  t.table_name=x.table_name and t.tablespace_name=p.tablespace_name
	  and x.owner=u.username
	```
	See [Oracle XML DB Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e23094/toc.htm) for information on XMLTypes.
	Transporting tablespaces with XMLTypes has the following limitations:
	- The destination database must have XML DB installed.
		- Schemas referenced by XMLType tables cannot be the XML DB standard schemas.
		- Schemas referenced by XMLType tables cannot have cyclic dependencies.
		- XMLType tables with row level security are not supported, because they cannot be exported or imported.
		- If the schema for a transported XMLType table is not present in the destination database, it is imported and registered. If the schema already exists in the destination database, an error is returned unless the `ignore=y` option is set.
		- If an XMLType table uses a schema that is dependent on another schema, the schema that is depended on is not exported. The import succeeds only if that schema is already in the destination database.

Additional limitations include the following:

SYSTEM Tablespace Objects You cannot transport the SYSTEM tablespace or objects owned by the user SYS. Some examples of such objects are PL/SQL, Java classes, callouts, views, synonyms, users, privileges, dimensions, directories, and sequences.

Opaque Types Types whose interpretation is application-specific and opaque to the database (such as `RAW`, `BFILE`, and the AnyTypes) can be transported, but they are not converted as part of the cross-platform transport operation. Their actual structure is known only to the application, so the application must address any endianness issues after these types are moved to the new platform. Types and objects that use these opaque types, either directly or indirectly, are also subject to this limitation.

Floating-Point Numbers `BINARY_FLOAT` and `BINARY_DOUBLE` types are transportable using Data Pump.

### Compatibility Considerations for Transportable Tablespaces

When you create a transportable tablespace set, Oracle Database computes the lowest compatibility level at which the destination database must run. This is referred to as the compatibility level of the transportable set. Beginning with Oracle Database 11g, a tablespace can always be transported to a database with the same or higher compatibility setting, whether the destination database is on the same or a different platform. The database signals an error if the compatibility level of the transportable set is higher than the compatibility level of the destination database.

The following table shows the minimum compatibility requirements of the source and destination tablespace in various scenarios. The source and destination database need not have the same compatibility setting.

Table 14-1 Minimum Compatibility Requirements

<table><thead><tr><th rowspan="2">Transport Scenario</th><th colspan="2">Minimum Compatibility Setting</th></tr><tr><th headers="r1c1-t44 r1c1-t44">Source Database</th><th headers="r1c1-t44 r2c1-t44 r1c2-t44">Destination Database</th></tr></thead><tbody><tr><td headers="r1c1-t44 r2c1-t44"><p>Databases on the same platform</p></td><td headers="r3c1-t44 r1c2-t44 r2c2-t44"><p>8.0</p></td><td headers="r3c1-t44 r1c2-t44"><p>8.0</p></td></tr><tr><td headers="r1c1-t44 r2c1-t44"><p>Tablespace with different database block size than the destination database</p></td><td headers="r4c1-t44 r1c2-t44 r2c2-t44"><p>9.0</p></td><td headers="r4c1-t44 r1c2-t44"><p>9.0</p></td></tr><tr><td headers="r1c1-t44 r2c1-t44"><p>Databases on different platforms</p></td><td headers="r5c1-t44 r1c2-t44 r2c2-t44"><p>10.0</p></td><td headers="r5c1-t44 r1c2-t44"><p>10.0</p></td></tr></tbody></table>

### Transporting Tablespaces Between Databases: A Procedure and Example

The following list of tasks summarizes the process of transporting a tablespace. Details for each task are provided in the subsequent example.

Note:

This method of generating a transportable tablespace requires that you temporarily make the tablespace read-only. If this is undesirable, you can use the alternate method known as transportable tablespace from backup. See [Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/cd/E11882_01/backup.112/e10642/rcmttbsb.htm#BRADV05141) for details.

1. For cross-platform transport, check the endian format of both platforms by querying the `V$TRANSPORTABLE_PLATFORM` view.
	Ignore this task if you are transporting your tablespace set to the same platform.
2. Pick a self-contained set of tablespaces.
3. At the source database, place the set of tablespaces in read-only mode and generate a transportable tablespace set.
	A transportable tablespace set (or transportable set) consists of data files for the set of tablespaces being transported and an export file containing structural information (metadata) for the set of tablespaces. You use Data Pump to perform the export.
	If you are transporting the tablespace set to a platform with different endianness from the source platform, you must convert the tablespace set to the endianness of the destination platform. You can perform a source-side conversion at this step in the procedure, or you can perform a destination-side conversion as part of Task 4.
4. Transport the tablespace set.
	Copy the data files and the export file to a place that is accessible to the destination database.
	If you transported the tablespace set to a platform with different endianness from the source platform, and you have not performed a source-side conversion to the endianness of the destination platform, perform a destination-side conversion now.
5. (Optional) Restore tablespaces to read/write mode.
6. At the destination database, import the tablespace set.
	Invoke the Data Pump utility to import the metadata for the tablespace set.

Example

These tasks for transporting a tablespace are illustrated more fully in the example that follows, where it is assumed the following data files and tablespaces exist:

| Tablespace | Data File |
| --- | --- |
| `sales_1` | /u01/app/oracle/oradata/salesdb/sales\_101.dbf |
| `sales_2` | /u01/app/oracle/oradata/salesdb/sales\_201.dbf |

#### Task 1: Determine if Platforms are Supported and Determine Endianness

This task is only necessary if you are transporting the tablespace set to a platform different from the source platform.

If you are transporting the tablespace set to a platform different from the source platform, then determine if cross-platform tablespace transport is supported for both the source and destination platforms, and determine the endianness of each platform. If both platforms have the same endianness, no conversion is necessary. Otherwise you must do a conversion of the tablespace set either at the source or destination database.

If you are transporting `sales_1` and `sales_2` to a different platform, you can execute the following query on each platform. If the query returns a row, the platform supports cross-platform tablespace transport.

```
SELECT d.PLATFORM_NAME, ENDIAN_FORMAT
     FROM V$TRANSPORTABLE_PLATFORM tp, V$DATABASE d
     WHERE tp.PLATFORM_NAME = d.PLATFORM_NAME;
```

The following is the query result from the source platform:

```
PLATFORM_NAME                      ENDIAN_FORMAT
---------------------------------- --------------
Solaris[tm] OE (32-bit)            Big
```

The following is the result from the destination platform:

```
PLATFORM_NAME                      ENDIAN_FORMAT
---------------------------------- --------------
Microsoft Windows IA (32-bit)      Little
```

You can see that the endian formats are different and thus a conversion is necessary for transporting the tablespace set.

#### Task 2: Pick a Self-Contained Set of Tablespaces

There may be logical or physical dependencies between objects in the transportable set and those outside of the set. You can only transport a set of tablespaces that is self-contained. In this context "self-contained" means that there are no references from inside the set of tablespaces pointing outside of the tablespaces. Some examples of self contained tablespace violations are:

- An index inside the set of tablespaces is for a table outside of the set of tablespaces.
	Note:
	It is not a violation if a corresponding index for a table is outside of the set of tablespaces.
- A partitioned table is partially contained in the set of tablespaces.
	The tablespace set you want to copy must contain either all partitions of a partitioned table, or none of the partitions of a partitioned table. To transport a subset of a partition table, you must exchange the partitions into tables.
	See [Oracle Database VLDB and Partitioning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25523/part_admin002.htm#VLDBG1156) for information about exchanging partitions.
- A referential integrity constraint points to a table across a set boundary.
	When transporting a set of tablespaces, you can choose to include referential integrity constraints. However, doing so can affect whether a set of tablespaces is self-contained. If you decide not to transport constraints, then the constraints are not considered as pointers.
- A table inside the set of tablespaces contains a `LOB` column that points to `LOB` s outside the set of tablespaces.
- An XML DB schema (\*.xsd) that was registered by user A imports a global schema that was registered by user B, and the following is true: the default tablespace for user A is tablespace A, the default tablespace for user B is tablespace B, and only tablespace A is included in the set of tablespaces.

To determine whether a set of tablespaces is self-contained, you can invoke the `TRANSPORT_SET_CHECK` procedure in the Oracle supplied package `DBMS_TTS`. You must have been granted the `EXECUTE_CATALOG_ROLE` role (initially signed to `SYS`) to execute this procedure.

When you invoke the `DBMS_TTS` package, you specify the list of tablespaces in the transportable set to be checked for self containment. You can optionally specify if constraints must be included. For strict or full containment, you must additionally set the `TTS_FULL_CHECK` parameter to `TRUE`.

The strict or full containment check is for cases that require capturing not only references going outside the transportable set, but also those coming into the set. Tablespace Point-in-Time Recovery (TSPITR) is one such case where dependent objects must be fully contained or fully outside the transportable set.

For example, it is a violation to perform TSPITR on a tablespace containing a table `t` but not its index `i` because the index and data will be inconsistent after the transport. A full containment check ensures that there are no dependencies going outside or coming into the transportable set. See the example for TSPITR in the [Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/cd/E11882_01/backup.112/e10642/rcmtspit.htm#BRADV89796).

Note:

The default for transportable tablespaces is to check for self containment rather than full containment.

The following statement can be used to determine whether tablespaces `sales_1` and `sales_2` are self-contained, with referential integrity constraints taken into consideration (indicated by `TRUE`).

```
EXECUTE DBMS_TTS.TRANSPORT_SET_CHECK('sales_1,sales_2', TRUE);
```

After invoking this PL/SQL package, you can see all violations by selecting from the `TRANSPORT_SET_VIOLATIONS` view. If the set of tablespaces is self-contained, this view is empty. The following example illustrates a case where there are two violations: a foreign key constraint, `dept_fk`, across the tablespace set boundary, and a partitioned table, `jim.sales`, that is partially contained in the tablespace set.

```
SQL> SELECT * FROM TRANSPORT_SET_VIOLATIONS;

VIOLATIONS
---------------------------------------------------------------------------
Constraint DEPT_FK between table JIM.EMP in tablespace SALES_1 and table
JIM.DEPT in tablespace OTHER
Partitioned table JIM.SALES is partially contained in the transportable set
```

These violations must be resolved before `sales_1` and `sales_2` are transportable. As noted in the next task, one choice for bypassing the integrity constraint violation is to not export the integrity constraints.

See Also:

- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/d_tts.htm#ARPLS063) for more information about the `DBMS_TTS` package
- [Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/cd/E11882_01/backup.112/e10642/rcmtspit.htm#BRADV89796) for information specific to using the `DBMS_TTS` package for TSPITR

#### Task 3: Generate a Transportable Tablespace Set

After ensuring you have a self-contained set of tablespaces that you want to transport, generate a transportable tablespace set by completing the following steps:

1. Start SQL\*Plus and connect to the database as an administrator or as a user who has either the `ALTER` `TABLESPACE` or `MANAGE` `TABLESPACE` system privilege.
	See ["Connecting to the Database with SQL\*Plus"](dba.md) for instructions.
2. Make all tablespaces in the set read-only.
	```
	SQL> ALTER TABLESPACE sales_1 READ ONLY;
	Tablespace altered.
	SQL> ALTER TABLESPACE sales_2 READ ONLY;
	Tablespace altered.
	```
3. Invoke the Data Pump export utility as user `system` and specify the tablespaces in the transportable set.
	```
	SQL> HOST
	$ expdp system dumpfile=expdat.dmp directory=data_pump_dir 
	        transport_tablespaces=sales_1,sales_2 logfile=tts_export.log
	Password: password
	```
	You must always specify `TRANSPORT_TABLESPACES`, which determines the mode of the export operation. In this example:
	- The `DUMPFILE` parameter specifies the name of the structural information export file to be created, `expdat.dmp`.
		- The `DIRECTORY` parameter specifies the directory object that points to the operating system or Oracle Automatic Storage Management location of the dump file. You must create the `DIRECTORY` object before invoking Data Pump, and you must grant the `READ` and `WRITE` object privileges on the directory to `PUBLIC`. See [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_5007.htm#SQLRF01207) for information on the `CREATE` `DIRECTORY` command.
		Note:
		The directory object `DATA_PUMP_DIR` is automatically created when you install Oracle Database. Read and write access to this directory is automatically granted to the `DBA` role, and thus to users `SYS` and `SYSTEM`. If the `DIRECTORY` parameter is omitted, `DATA_PUMP_DIR` is used as the default directory.
		- The `LOGFILE` parameter specifies the file name of the log file to be written by the export utility. The log file is written to the same directory as the dump file.
		- `EXPDP` prompts for the password for the `system` account if you do not specify it on the command line.
		- Triggers and indexes are included in the export operation by default.
	To perform a transport tablespace operation with a strict containment check, use the `TRANSPORT_FULL_CHECK` parameter, as shown in the following example:
	```
	expdp system dumpfile=expdat.dmp directory=data_pump_dir
	      transport_tablespaces=sales_1,sales_2 transport_full_check=y
	      logfile=tts_export.log
	```
	In this case, the Data Pump export utility verifies that there are no dependencies between the objects inside the transportable set and objects outside the transportable set. If the tablespace set being transported is not self-contained, then the export fails and indicates that the transportable set is not self-contained. You must then return to Task 2 to resolve all violations.
	Notes:
	The Data Pump utility is used to export only data dictionary structural information (metadata) for the tablespaces. No actual data is unloaded, so this operation goes relatively quickly even for large tablespace sets.
4. Check the log file for errors, and take note of the dump file and data files that you must transport to the destination database. `EXPDP` outputs the names and paths of these files in messages like these:
	```
	******************************************************************************
	Dump file set for SYSTEM.SYS_EXPORT_TRANSPORTABLE_01 is:
	  /u01/app/oracle/admin/salesdb/dpdump/expdat.dmp
	******************************************************************************
	Datafiles required for transportable tablespace SALES_1:
	  /u01/app/oracle/oradata/salesdb/sales_101.dbf
	Datafiles required for transportable tablespace SALES_2:
	  /u01/app/oracle/oradata/salesdb/sales_201.dbf
	```
5. When finished, exit back to SQL\*Plus:
	```
	$ EXIT
	```
	See Also:
	[Oracle Database Utilities](https://docs.oracle.com/cd/E11882_01/server.112/e22490/dp_export.htm#SUTIL200) for information about using the Data Pump utility

If `sales_1` and `sales_2` are being transported to a different platform, and the endianness of the platforms is different, and if you want to convert before transporting the tablespace set, then convert the data files composing the `sales_1` and `sales_2` tablespaces:

1. From SQL\*Plus, return to the host system:
	```
	SQL> HOST
	```
2. Start RMAN and connect to the source database:
	```
	$ RMAN TARGET /
	Recovery Manager: Release 11.2.0.0.1 
	Copyright (c) 1982, 2007, Oracle.  All rights reserved.
	connected to target database: salesdb (DBID=3295731590)
	```
3. Use the RMAN `CONVERT` `TABLESPACE` command to convert the data files into a temporary location on the source platform.
	In this example, assume that the temporary location, directory `/tmp`, has already been created. The converted data files are assigned names by the system.
	```
	RMAN> CONVERT TABLESPACE sales_1,sales_2 
	2> TO PLATFORM 'Microsoft Windows IA (32-bit)'
	3> FORMAT '/tmp/%U';
	Starting conversion at source at 30-SEP-08
	using channel ORA_DISK_1
	channel ORA_DISK_1: starting datafile conversion
	input datafile file number=00007 name=/u01/app/oracle/oradata/salesdb/sales_101.dbf
	converted datafile=/tmp/data_D-SALESDB_I-1192614013_TS-SALES_1_FNO-7_03jru08s
	channel ORA_DISK_1: datafile conversion complete, elapsed time: 00:00:45
	channel ORA_DISK_1: starting datafile conversion
	input datafile file number=00008 name=/u01/app/oracle/oradata/salesdb/sales_201.dbf
	converted datafile=/tmp/data_D-SALESDB_I-1192614013_TS-SALES_2_FNO-8_04jru0aa
	channel ORA_DISK_1: datafile conversion complete, elapsed time: 00:00:25
	Finished conversion at source at 30-SEP-08
	```
	See Also:
	[Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta012.htm#RCMRF192) for a description of the RMAN `CONVERT` command
4. Exit Recovery Manager:
	```
	RMAN> exit
	Recovery Manager complete.
	```

#### Task 4: Transport the Tablespace Set

Complete the following steps:

1. Transport both the data files and the export (dump) file of the tablespaces to a place that is accessible to the destination database. To accomplish this, do one of the following:
	- If no endianness conversion of the tablespace set is needed, or if you already converted the tablespace set:
		1. Transport the dump file to the directory pointed to by the `DATA_PUMP_DIR` directory object, or to any other directory of your choosing.
			Run the following query to determine the location of `DATA_PUMP_DIR`:
			```
			SELECT * FROM DBA_DIRECTORIES WHERE DIRECTORY_NAME = 'DATA_PUMP_DIR';
			OWNER      DIRECTORY_NAME   DIRECTORY_PATH
			---------- ---------------- -----------------------------------
			SYS        DATA_PUMP_DIR    C:\app\orauser\admin\orawin\dpdump\
			```
				2. Transport the data files to the location of the existing data files of the destination database.
			On the UNIX and Linux platforms, this location is typically /u01/app/oracle/oradata/SID/ or +DISKGROUP/SID/datafile/.
			Note:
			If you converted the data files, obtain the new names and locations of the data files from the `CONVERT` `TABLESPACE` command output, as shown in Step 3 of Task 3: Generate a Transportable Tablespace Set.
		- If you intend to perform endianness conversion after transporting to the destination host:
		1. Transport the dump file to the directory pointed to by the `DATA_PUMP_DIR` directory object, or to any other directory of your choosing.
				2. Transport the data files to a temporary location on the destination host (for example, /tmp or C:\\TEMP). During conversion, you can move the converted data files to the location of the existing data files of the destination database.
	Tip:
	If both the source and destination are file systems, you can transport using:
	- Any facility for copying flat files (for example, an operating system copy utility or ftp)
	- The `DBMS_FILE_TRANSFER` package
	- RMAN
	- Any facility for publishing on CDs
	If either the source or destination is an Oracle Automatic Storage Management (Oracle ASM) disk group, you can use:
	- ftp to or from the `/sys/asm` virtual folder in the XML DB repository
		See [Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e18951/asmfiles.htm#OSTMG10001) for more information.
	- The `DBMS_FILE_TRANSFER` package
	- RMAN
	Caution:
	Exercise caution when using the UNIX `dd` utility to copy raw-device files between databases. The `dd` utility can be used to copy an entire source raw-device file, or it can be invoked with options that instruct it to copy only a specific range of blocks from the source raw-device file.
	It is difficult to ascertain actual data file size for a raw-device file because of hidden control information that is stored as part of the data file. Thus, it is advisable when using the `dd` utility to specify copying the entire source raw-device file contents.
2. If you are transporting the tablespace set to a platform with endianness that is different from the source platform, and you have not yet converted the tablespace set, do so now with RMAN.
	The following example places the converted data files into C:\\app\\orauser\\oradata\\orawin\\, which is the location of the existing data files for the destination database:
	```
	C:\>RMAN TARGET /
	 
	Recovery Manager: Release 11.2.0.0.1 
	 
	Copyright (c) 1982, 2007, Oracle.  All rights reserved.
	connected to target database: ORAWIN (DBID=3462152886)
	RMAN> CONVERT DATAFILE 
	2>'C:\Temp\sales_101.dbf',
	3>'C:\Temp\sales_201.dbf'
	4>TO PLATFORM="Microsoft Windows IA (32-bit)"
	5>FROM PLATFORM="Solaris[tm] OE (32-bit)"
	6>DB_FILE_NAME_CONVERT=
	7>'C:\Temp\', 'C:\app\orauser\oradata\orawin\'
	8> PARALLELISM=4;
	```
	You identify the data files by filename, not by tablespace name. Until the tablespace metadata is imported, the destination instance has no way of knowing the desired tablespace names.
	If the source location, the target location, or both do not use Oracle Automatic Storage Management (Oracle ASM), then the source and target platforms are optional. RMAN determines the source platform by examining the data file, and the target platform defaults to the platform of the host running the conversion.
	If both the source and target locations use Oracle ASM, then you must specify the source and target platforms in the `DB_FILE_NAME_CONVERT` clause.

See Also:

["Copying Files Using the Database Server"](dfiles.md) for information about using the `DBMS_FILE_TRANSFER` package to copy the files that are being transported and their metadata

#### Task 5: (Optional) Restore Tablespaces to Read/Write Mode

Make the transported tablespaces read/write again at the source database, as follows:

```
ALTER TABLESPACE sales_1 READ WRITE;
ALTER TABLESPACE sales_2 READ WRITE;
```

You can postpone this task to first ensure that the import process succeeds.

#### Task 6: Import the Tablespace Set

Note:

If you are transporting a tablespace of a different block size than the standard block size of the database receiving the tablespace set, then you must first have a `DB_` `n` `K_CACHE_SIZE` initialization parameter entry in the receiving database parameter file.

For example, if you are transporting a tablespace with an 8K block size into a database with a 4K standard block size, then you must include a `DB_8K_CACHE_SIZE` initialization parameter entry in the parameter file. If it is not already included in the parameter file, this parameter can be set using the `ALTER SYSTEM SET` statement.

See [Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams046.htm#REFRN10027) for information about specifying values for the `DB_` `n` `K_CACHE_SIZE` initialization parameter.

Any privileged user can perform this task. To import a tablespace set, complete the following steps:

1. Import the tablespace metadata using the Data Pump Import utility, `impdp`:
	```
	impdp system dumpfile=expdat.dmp directory=data_pump_dir
	   TRANSPORT_DATAFILES=
	   c:\app\orauser\oradata\orawin\sales_101.dbf,
	   c:\app\orauser\oradata\orawin\sales_201.dbf
	   remap_schema=sales1:crm1  remap_schema=sales2:crm2
	   logfile=tts_import.log
	Password: password
	```
	In this example we specify the following:
	- The `DUMPFILE` parameter specifies the exported file containing the metadata for the tablespaces to be imported.
		- The `DIRECTORY` parameter specifies the directory object that identifies the location of the dump file.
		- The `TRANSPORT_DATAFILES` parameter identifies all of the data files containing the tablespaces to be imported.
		- The `REMAP_SCHEMA` parameter changes the ownership of database objects. If you do not specify `REMAP_SCHEMA`, all database objects (such as tables and indexes) are created in the same user schema as in the source database, and those users must already exist in the destination database. If they do not exist, then the import utility returns an error. In this example, objects in the tablespace set owned by `sales1` in the source database will be owned by `crm1` in the destination database after the tablespace set is imported. Similarly, objects owned by `sales2` in the source database will be owned by `crm2` in the destination database. In this case, the destination database is not required to have users `sales1` and `sales2`, but must have users `crm1` and `crm2`.
		- The `LOGFILE` parameter specifies the file name of the log file to be written by the import utility. The log file is written to the directory from which the dump file is read.
	After this statement executes successfully, all tablespaces in the set being copied remain in read-only mode. Check the import log file to ensure that no error has occurred.
	When dealing with a large number of data files, specifying the list of data file names in the statement line can be a laborious process. It can even exceed the statement line limit. In this situation, you can use an import parameter file. For example, you can invoke the Data Pump import utility as follows:
	```
	impdp system parfile='par.f'
	```
	where the parameter file, `par.f` contains the following:
	```
	DUMPFILE=expdat.dmp 
	DIRECTORY=data_pump_dir
	TRANSPORT_DATAFILES=
	C:\app\orauser\oradata\orawin\sales_101.dbf,
	C:\app\orauser\oradata\orawin\sales_201.dbf
	REMAP_SCHEMA=sales1:crm1  REMAP_SCHEMA=sales2:crm2
	LOGFILE=tts_import.log
	```
	See Also:
	[Oracle Database Utilities](https://docs.oracle.com/cd/E11882_01/server.112/e22490/toc.htm) for information about using the import utility
2. If required, put the tablespaces into read/write mode on the destination database.

### Using Transportable Tablespaces: Scenarios

The following sections describe some uses for transportable tablespaces:

- Transporting and Attaching Partitions for Data Warehousing
- Publishing Structured Data on CDs
- Mounting the Same Tablespace Read-Only on Multiple Databases
- Archiving Historical Data Using Transportable Tablespaces
- Using Transportable Tablespaces to Perform TSPITR

#### Transporting and Attaching Partitions for Data Warehousing

Typical enterprise data warehouses contain one or more large fact tables. These fact tables can be partitioned by date, making the enterprise data warehouse a historical database. You can build indexes to speed up star queries. Oracle recommends that you build local indexes for such historically partitioned tables to avoid rebuilding global indexes every time you drop the oldest partition from the historical database.

Suppose every month you would like to load one month of data into the data warehouse. There is a large fact table in the data warehouse called `sales`, which has the following columns:

```
CREATE TABLE sales (invoice_no NUMBER,
   sale_year  INT NOT NULL,
   sale_month INT NOT NULL,
   sale_day   INT NOT NULL)
   PARTITION BY RANGE (sale_year, sale_month, sale_day)
     (partition jan98 VALUES LESS THAN (1998, 2, 1),
      partition feb98 VALUES LESS THAN (1998, 3, 1),
      partition mar98 VALUES LESS THAN (1998, 4, 1),
      partition apr98 VALUES LESS THAN (1998, 5, 1),
      partition may98 VALUES LESS THAN (1998, 6, 1),
      partition jun98 VALUES LESS THAN (1998, 7, 1));
```

You create a local non-prefixed index:

```
CREATE INDEX sales_index ON sales(invoice_no) LOCAL;
```

Initially, all partitions are empty, and are in the same default tablespace. Each month, you want to create one partition and attach it to the partitioned `sales` table.

Suppose it is July 1998, and you would like to load the July sales data into the partitioned table. In a staging database, you create a new tablespace, `ts_jul`. You also create a table, `jul_sales`, in that tablespace with the same column types as the `sales` table. You can create the table `jul_sales` using the `CREATE` `TABLE`... `AS` `SELECT` statement. After creating and populating `jul_sales`, you can also create an index, `jul_sale_index`, for the table, indexing the same column as the local index in the `sales` table. After building the index, transport the tablespace `ts_jul` to the data warehouse.

In the data warehouse, add a partition to the `sales` table for the July sales data. This also creates another partition for the local non-prefixed index:

```
ALTER TABLE sales ADD PARTITION jul98 VALUES LESS THAN (1998, 8, 1);
```

Attach the transported table `jul_sales` to the table `sales` by exchanging it with the new partition:

```
ALTER TABLE sales EXCHANGE PARTITION jul98 WITH TABLE jul_sales 
   INCLUDING INDEXES
   WITHOUT VALIDATION;
```

This statement places the July sales data into the new partition `jul98`, attaching the new data to the partitioned table. This statement also converts the index `jul_sale_index` into a partition of the local index for the `sales` table. This statement should return immediately, because it only operates on the structural information and it simply switches database pointers. If you know that the data in the new partition does not overlap with data in previous partitions, you are advised to specify the `WITHOUT VALIDATION` clause. Otherwise, the statement goes through all the new data in the new partition in an attempt to validate the range of that partition.

If all partitions of the `sales` table came from the same staging database (the staging database is never destroyed), the exchange statement always succeeds. In general, however, if data in a partitioned table comes from different databases, the exchange operation might fail. For example, if the `jan98` partition of `sales` did not come from the same staging database, the preceding exchange operation can fail, returning the following error:

```
ORA-19728: data object number conflict between table JUL_SALES and partition JAN98 in table SALES
```

To resolve this conflict, move the offending partition by issuing the following statement:

```
ALTER TABLE sales MOVE PARTITION jan98;
```

Then retry the exchange operation.

After the exchange succeeds, you can safely drop `jul_sales` and `jul_sale_index` (both are now empty). Thus you have successfully loaded the July sales data into your data warehouse.

#### Publishing Structured Data on CDs

Transportable tablespaces provide a way to publish structured data on CDs. A data provider can load a tablespace with data to be published, generate the transportable set, and copy the transportable set to a CD. This CD can then be distributed.

When customers receive this CD, they can add the CD contents to an existing database without having to copy the data files from the CD to disk storage. For example, suppose on a Windows NT system D: drive is the CD drive. You can import a transportable set with data file `catalog.f` and export file `expdat.dmp` as follows:

```
IMPDP system/password DUMPFILE=expdat.dmp DIRECTORY=dpump_dir
   TRANSPORT_DATAFILES='D:\catalog.f'
```

You can remove the CD while the database is still up. Subsequent queries to the tablespace return an error indicating that the database cannot open the data files on the CD. However, operations to other parts of the database are not affected. Placing the CD back into the drive makes the tablespace readable again.

Removing the CD is the same as removing the data files of a read-only tablespace. If you shut down and restart the database, the database indicates that it cannot find the removed data file and does not open the database (unless you set the initialization parameter `READ_ONLY_OPEN_DELAYED` to `TRUE`). When `READ_ONLY_OPEN_DELAYED` is set to `TRUE`, the database reads the file only when someone queries the transported tablespace. Thus, when transporting a tablespace from a CD, you should always set the `READ_ONLY_OPEN_DELAYED` initialization parameter to `TRUE`, unless the CD is permanently attached to the database.

#### Mounting the Same Tablespace Read-Only on Multiple Databases

You can use transportable tablespaces to mount a tablespace read-only on multiple databases. In this way, separate databases can share the same data on disk instead of duplicating data on separate disks. The tablespace data files must be accessible by all databases. To avoid database corruption, the tablespace must remain read-only in all the databases mounting the tablespace.

The following are two scenarios for mounting the same tablespace read-only on multiple databases:

- The tablespace originates in a database that is separate from the databases that will share the tablespace.
	You generate a transportable set in the source database, put the transportable set onto a disk that is accessible to all databases, and then import the metadata into each database on which you want to mount the tablespace.
- The tablespace already belongs to one of the databases that will share the tablespace.
	It is assumed that the data files are already on a shared disk. In the database where the tablespace already exists, you make the tablespace read-only, generate the transportable set, and then import the tablespace into the other databases, leaving the data files in the same location on the shared disk.

You can make a disk accessible by multiple computers in several ways. You can use either a cluster file system or raw disk. You can also use network file system (NFS), but be aware that if a user queries the shared tablespace while NFS is down, the database will hang until the NFS operation times out.

Later, you can drop the read-only tablespace in some of the databases. Doing so does not modify the data files for the tablespace. Thus, the drop operation does not corrupt the tablespace. Do not make the tablespace read/write unless only one database is mounting the tablespace.

#### Archiving Historical Data Using Transportable Tablespaces

Since a transportable tablespace set is a self-contained set of files that can be imported into any Oracle Database, you can archive old/historical data in an enterprise data warehouse using the transportable tablespace procedures described in this chapter.

See Also:

[Oracle Database Data Warehousing Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25554/transport.htm#DWHSG8301) for more details

#### Using Transportable Tablespaces to Perform TSPITR

You can use transportable tablespaces to perform tablespace point-in-time recovery (TSPITR).

See Also:

[Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/cd/E11882_01/backup.112/e10642/rcmtspit.htm#BRADV009) for information about how to perform TSPITR using transportable tablespaces

### Moving Databases Across Platforms Using Transportable Tablespaces

You can use the transportable tablespace feature to migrate a database to a different platform by creating a new database on the destination platform and performing a transport of all the user tablespaces. See [Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/cd/E11882_01/backup.112/e10642/rcmxplat.htm#BRADV05432) for more information.

You cannot transport the `SYSTEM` tablespace. Therefore, objects such as sequences, PL/SQL packages, and other objects that depend on the `SYSTEM` tablespace are not transported. You must either create these objects manually on the destination database, or use Data Pump to transport the objects that are not moved by transportable tablespace.

## Tablespace Data Dictionary Views

The following data dictionary and dynamic performance views provide useful information about the tablespaces of a database.

| View | Description |
| --- | --- |
| `V$TABLESPACE` | Name and number of all tablespaces from the control file. |
| `V$ENCRYPTED_TABLESPACES` | Name and encryption algorithm of all encrypted tablespaces. |
| `DBA_TABLESPACES`, `USER_TABLESPACES` | Descriptions of all (or user accessible) tablespaces. |
| `DBA_TABLESPACE_GROUPS` | Displays the tablespace groups and the tablespaces that belong to them. |
| `DBA_SEGMENTS`, `USER_SEGMENTS` | Information about segments within all (or user accessible) tablespaces. |
| `DBA_EXTENTS`, `USER_EXTENTS` | Information about data extents within all (or user accessible) tablespaces. |
| `DBA_FREE_SPACE`, `USER_FREE_SPACE` | Information about free extents within all (or user accessible) tablespaces. |
| `DBA_TEMP_FREE_SPACE` | Displays the total allocated and free space in each temporary tablespace. |
| `V$DATAFILE` | Information about all data files, including tablespace number of owning tablespace. |
| `V$TEMPFILE` | Information about all temp files, including tablespace number of owning tablespace. |
| `DBA_DATA_FILES` | Shows files (data files) belonging to tablespaces. |
| `DBA_TEMP_FILES` | Shows files (temp files) belonging to temporary tablespaces. |
| `V$TEMP_EXTENT_MAP` | Information for all extents in all locally managed temporary tablespaces. |
| `V$TEMP_EXTENT_POOL` | For locally managed temporary tablespaces: the state of temporary space cached and used for by each instance. |
| `V$TEMP_SPACE_HEADER` | Shows space used/free for each temp file. |
| `DBA_USERS` | Default and temporary tablespaces for all users. |
| `DBA_TS_QUOTAS` | Lists tablespace quotas for all users. |
| `V$SORT_SEGMENT` | Information about every sort segment in a given instance. The view is only updated when the tablespace is of the `TEMPORARY` type. |
| `V$TEMPSEG_USAGE` | Describes temporary (sort) segment usage by user for temporary or permanent tablespaces. |

The following are just a few examples of using some of these views.

See Also:

[Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/toc.htm) for complete description of these views

### Example 1: Listing Tablespaces and Default Storage Parameters

To list the names and default storage parameters of all tablespaces in a database, use the following query on the `DBA_TABLESPACES` view:

```
SELECT TABLESPACE_NAME "TABLESPACE",
   INITIAL_EXTENT "INITIAL_EXT",
   NEXT_EXTENT "NEXT_EXT",
   MIN_EXTENTS "MIN_EXT",
   MAX_EXTENTS "MAX_EXT",
   PCT_INCREASE
   FROM DBA_TABLESPACES;

TABLESPACE  INITIAL_EXT  NEXT_EXT  MIN_EXT   MAX_EXT    PCT_INCREASE  
----------  -----------  --------  -------   -------    ------------ 
RBS             1048576   1048576        2        40               0
SYSTEM           106496    106496        1        99               1
TEMP             106496    106496        1        99               0
TESTTBS           57344     16384        2        10               1
USERS             57344     57344        1        99               1
```

### Example 2: Listing the Data Files and Associated Tablespaces of a Database

To list the names, sizes, and associated tablespaces of a database, enter the following query on the `DBA_DATA_FILES` view:

```
SELECT  FILE_NAME, BLOCKS, TABLESPACE_NAME
   FROM DBA_DATA_FILES;

FILE_NAME                                      BLOCKS  TABLESPACE_NAME
------------                               ----------  -------------------
/U02/ORACLE/IDDB3/DBF/RBS01.DBF                  1536  RBS
/U02/ORACLE/IDDB3/DBF/SYSTEM01.DBF               6586  SYSTEM
/U02/ORACLE/IDDB3/DBF/TEMP01.DBF                 6400  TEMP
/U02/ORACLE/IDDB3/DBF/TESTTBS01.DBF              6400  TESTTBS
/U02/ORACLE/IDDB3/DBF/USERS01.DBF                 384  USERS
```

### Example 3: Displaying Statistics for Free Space (Extents) of Each Tablespace

To produce statistics about free extents and coalescing activity for each tablespace in the database, enter the following query:

```
SELECT TABLESPACE_NAME "TABLESPACE", FILE_ID,
   COUNT(*)    "PIECES",
   MAX(blocks) "MAXIMUM",
   MIN(blocks) "MINIMUM",
   AVG(blocks) "AVERAGE",
   SUM(blocks) "TOTAL"
   FROM DBA_FREE_SPACE
GROUP BY TABLESPACE_NAME, FILE_ID;

TABLESPACE    FILE_ID  PIECES   MAXIMUM    MINIMUM  AVERAGE    TOTAL
----------    -------  ------   -------    -------  -------   ------
RBS                 2       1       955        955      955      955
SYSTEM              1       1       119        119      119      119
TEMP                4       1      6399       6399     6399     6399
TESTTBS             5       5      6364          3     1278     6390
USERS               3       1       363        363      363      363
```

`PIECES` shows the number of free space extents in the tablespace file, `MAXIMUM` and `MINIMUM` show the largest and smallest contiguous area of space in database blocks, `AVERAGE` shows the average size in blocks of a free space extent, and `TOTAL` shows the amount of free space in each tablespace file in blocks. This query is useful when you are going to create a new object or you know that a segment is about to extend, and you want to ensure that there is enough space in the containing tablespace.