---
title: Managing Tables
book: "Administrator's Guide"
doc_id: E25494-07
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e25494/tables.htm
tags:
  - oracle
  - 11g
  - administrators-guide
---

## 20 Managing Tables

In this chapter:

## About Tables

Tables are the basic unit of data storage in an Oracle Database. Data is stored in rows and columns. You define a table with a table name, such as `employees`, and a set of columns. You give each column a column name, such as `employee_id`, `last_name`, and `job_id`; a data type, such as `VARCHAR2`, `DATE`, or `NUMBER`; and a width. The width can be predetermined by the data type, as in `DATE`. If columns are of the `NUMBER` data type, define precision and scale instead of width. A row is a collection of column information corresponding to a single record.

You can specify rules for each column of a table. These rules are called integrity constraints. One example is a `NOT NULL` integrity constraint. This constraint forces the column to contain a value in every row.

You can invoke transparent data encryption to encrypt data before storing it. If users attempt to circumvent the database access control mechanisms by looking inside Oracle data files directly with operating system tools, encryption prevents these users from viewing sensitive data.

Tables can also include virtual columns. A virtual column is like any other table column, except that its value is derived by evaluating an expression. The expression can include columns from the same table, constants, SQL functions, and user-defined PL/SQL functions. You cannot explicitly write to a virtual column.

Some column types, such as `LOB` s, varrays, and nested tables, are stored in their own segments. `LOB` s and varrays are stored in `LOB` segments, while nested tables are stored in storage tables. You can specify a `STORAGE` clause for these segments that will override storage parameters specified at the table level.

After you create a table, you insert rows of data using SQL statements or using an Oracle bulk load utility. Table data can then be queried, deleted, or updated using SQL.

See Also:

- [Oracle Database Concepts](https://docs.oracle.com/cd/E11882_01/server.112/e40540/tablecls.htm#CNCPT211) for an overview of tables
- [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/sql_elements001.htm#SQLRF0021) for descriptions of Oracle Database data types
- [Chapter 19, "Managing Space for Schema Objects"](schema.md) for guidelines for managing space for tables
- [Chapter 18, "Managing Schema Objects"](general.md) for information on additional aspects of managing tables, such as specifying integrity constraints and analyzing tables
- [Oracle Database Advanced Security Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e40393/asotrans.htm#ASOAG600) for a discussion of transparent data encryption

## Guidelines for Managing Tables

This section describes guidelines to follow when managing tables. Following these guidelines can make the management of your tables easier and can improve performance when creating the table, as well as when loading, updating, and querying the table data.

The following topics are discussed:

- Design Tables Before Creating Them
- Specify the Type of Table to Create
- Specify the Location of Each Table
- Consider Parallelizing Table Creation
- Consider Using NOLOGGING When Creating Tables
- Consider Using Table Compression
- Consider Encrypting Columns That Contain Sensitive Data
- Understand Deferred Segment Creation
- Estimate Table Size and Plan Accordingly
- Restrictions to Consider When Creating Tables

### Design Tables Before Creating Them

Usually, the application developer is responsible for designing the elements of an application, including the tables. Database administrators are responsible for establishing the attributes of the underlying tablespace that will hold the application tables. Either the DBA or the applications developer, or both working jointly, can be responsible for the actual creation of the tables, depending upon the practices for a site.

Working with the application developer, consider the following guidelines when designing tables:

- Use descriptive names for tables, columns, indexes, and clusters.
- Be consistent in abbreviations and in the use of singular and plural forms of table names and columns.
- Document the meaning of each table and its columns with the `COMMENT` command.
- Normalize each table.
- Select the appropriate data type for each column.
- Consider whether your applications would benefit from adding one or more virtual columns to some tables.
- Define columns that allow nulls last, to conserve storage space.
- Cluster tables whenever appropriate, to conserve storage space and optimize performance of SQL statements.

Before creating a table, you should also determine whether to use integrity constraints. Integrity constraints can be defined on the columns of a table to enforce the business rules of your database automatically.

### Specify the Type of Table to Create

Here are the types of tables that you can create:

| Type of Table | Description |
| --- | --- |
| Ordinary (heap-organized) table | This is the basic, general purpose type of table which is the primary subject of this chapter. Its data is stored as an unordered collection (heap). |
| Clustered table | A clustered table is a table that is part of a cluster. A cluster is a group of tables that share the same data blocks because they share common columns and are often used together.  Clusters and clustered tables are discussed in [Chapter 22, "Managing Clusters"](clustrs.md). |
| Index-organized table | Unlike an ordinary (heap-organized) table, data for an index-organized table is stored in a B-tree index structure in a primary key sorted manner. Besides storing the primary key column values of an index-organized table row, each index entry in the B-tree stores the nonkey column values as well.  Index-organized tables are discussed in "Managing Index-Organized Tables". |
| Partitioned table | Partitioned tables enable your data to be broken down into smaller, more manageable pieces called partitions, or even subpartitions. Each partition can have separate physical attributes, such as compression enabled or disabled, type of compression, physical storage settings, and tablespace, thus providing a structure that can be better tuned for availability and performance. In addition, each partition can be managed individually, which can simplify and reduce the time required for backup and administration.  Partitioned tables are discussed in [Oracle Database VLDB and Partitioning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25523/toc.htm). |

### Specify the Location of Each Table

It is advisable to specify the `TABLESPACE` clause in a `CREATE TABLE` statement to identify the tablespace that is to store the new table. For partitioned tables, you can optionally identify the tablespace that is to store each partition. Ensure that you have the appropriate privileges and quota on any tablespaces that you use. If you do not specify a tablespace in a `CREATE TABLE` statement, the table is created in your default tablespace.

When specifying the tablespace to contain a new table, ensure that you understand implications of your selection. By properly specifying a tablespace during the creation of each table, you can increase the performance of the database system and decrease the time needed for database administration.

The following situations illustrate how not specifying a tablespace, or specifying an inappropriate one, can affect performance:

- If users' objects are created in the `SYSTEM` tablespace, the performance of the database can suffer, since both data dictionary objects and user objects must contend for the same data files. Users' objects should not be stored in the `SYSTEM` tablespace. To avoid this, ensure that all users are assigned default tablespaces when they are created in the database.
- If application-associated tables are arbitrarily stored in various tablespaces, the time necessary to complete administrative operations (such as backup and recovery) for the data of that application can be increased.

### Consider Parallelizing Table Creation

You can use parallel execution when creating tables using a subquery (`AS SELECT`) in the `CREATE TABLE` statement. Because multiple processes work together to create the table, performance of the table creation operation is improved.

Parallelizing table creation is discussed in the section "Parallelizing Table Creation".

### Consider Using NOLOGGING When Creating Tables

To create a table most efficiently use the `NOLOGGING` clause in the `CREATE TABLE...AS SELECT` statement. The `NOLOGGING` clause causes minimal redo information to be generated during the table creation. This has the following benefits:

- Space is saved in the redo log files.
- The time it takes to create the table is decreased.
- Performance improves for parallel creation of large tables.

The `NOLOGGING` clause also specifies that subsequent direct loads using SQL\*Loader and direct load `INSERT` operations are not logged. Subsequent DML statements (`UPDATE`, `DELETE`, and conventional path insert) are unaffected by the `NOLOGGING` attribute of the table and generate redo.

If you cannot afford to lose the table after you have created it (for example, you will no longer have access to the data used to create the table) you should take a backup immediately after the table is created. In some situations, such as for tables that are created for temporary use, this precaution may not be necessary.

In general, the relative performance improvement of specifying `NOLOGGING` is greater for larger tables than for smaller tables. For small tables, `NOLOGGING` has little effect on the time it takes to create a table. However, for larger tables the performance improvement can be significant, especially when also parallelizing the table creation.

### Consider Using Table Compression

As your database grows in size, consider using table compression. Compression saves disk space, reduces memory use in the database buffer cache, and can significantly speed query execution during reads. Compression has a cost in CPU overhead for data loading and DML. However, this cost might be offset by reduced I/O requirements.

Table compression is completely transparent to applications. It is useful in decision support systems (DSS), online transaction processing (OLTP) systems, and archival systems.

You can specify compression for a tablespace, a table, or a partition. If specified at the tablespace level, then all tables created in that tablespace are compressed by default.

Compression can occur while data is being inserted, updated, or bulk loaded into a table. Operations that permit compression include:

- Single-row or array inserts and updates
- The following direct-path `INSERT` methods:
	- Direct path SQL\*Loader
		- `CREATE` `TABLE` `AS` `SELECT` statements
		- Parallel `INSERT` statements
		- `INSERT` statements with an `APPEND` or `APPEND_VALUES` hint

Oracle Database supports several methods of table compression. They are summarized in Table 20-1.

Table 20-1 Table Compression Methods

| Table Compression Method | Compression Level | CPU Overhead | Applications | Notes |
| --- | --- | --- | --- | --- |
| Basic compression | High | Minimal | DSS | None. |
| OLTP compression | High | Minimal | OLTP, DSS | None. |
| Warehouse compression (Hybrid Columnar Compression) | Higher | Higher | DSS | The compression level and CPU overhead depend on compression level specified (LOW or HIGH). |
| Archive compression (Hybrid Columnar Compression) | Highest | Highest | Archiving | The compression level and CPU overhead depend on compression level specified (LOW or HIGH). |

When you use basic compression, warehouse compression, or archive compression, compression only occurs when data is bulk loaded into a table.

When you use OLTP compression, compression occurs while data is being inserted, updated, or bulk loaded into a table. Operations that permit compression include:

- Single-row or array inserts and updates
	Inserts and updates are not compressed immediately. When updating an already compressed block, any columns that are not updated usually remain compressed. Updated columns are stored in an uncompressed format similar to any uncompressed block. The updated values are re-compressed when the block reaches a database-controlled threshold. Inserted data is also compressed when the data in the block reaches a database-controlled threshold.
- The following direct-path `INSERT` methods:
	- Direct path SQL\*Loader
		- `CREATE` `TABLE` `AS` `SELECT` statements
		- Parallel `INSERT` statements
		- `INSERT` statements with an `APPEND` or `APPEND_VALUES` hint

Basic compression compresses data inserted by direct path load only and supports limited data types and SQL operations. OLTP compression is intended for OLTP applications and compresses data manipulated by any SQL operation.

Warehouse compression and archive compression achieve the highest compression levels because they use Hybrid Columnar Compression technology. Hybrid Columnar Compression technology uses a modified form of columnar storage instead of row-major storage. This enables the database to store similar data together, which improves the effectiveness of compression algorithms. For data that is updated, Hybrid Columnar Compression uses more CPU and moves the updated rows to row format so that future updates are faster. Because of this optimization, you should use it only for data that is updated infrequently.

The higher compression levels of Hybrid Columnar Compression are achieved only with data that is direct-path inserted. Conventional inserts and updates are supported, but cause rows to be moved from columnar to row format, and reduce the compression level.

Regardless of the compression method, `DELETE` operations on a compressed block are identical to `DELETE` operations on a non-compressed block. Any space obtained on a data block, caused by SQL `DELETE` operations, is reused by subsequent SQL `INSERT` operations. With Hybrid Columnar Compression technology, when all the rows in a compression unit are deleted, the space in the compression unit is available for reuse.

Table 20-2 lists characteristics of each table compression method.

Table 20-2 Table Compression Characteristics

| Table Compression Method | CREATE/ALTER TABLE Syntax | Direct-Path INSERT | Notes |
| --- | --- | --- | --- |
| Basic compression | `COMPRESS [BASIC]` | Rows are compressed with basic compression. | `COMPRESS` and `COMPRESS` `BASIC` are equivalent.  Rows inserted without using direct-path insert and updated rows are uncompressed. |
| OLTP compression | `COMPRESS FOR OLTP` | Rows are compressed with OLTP compression. | Rows inserted without using direct-path insert and updated rows are compressed using OLTP compression. |
| Warehouse compression (Hybrid Columnar Compression) | `COMPRESS FOR QUERY [LOW\|HIGH]` | Rows are compressed with warehouse compression. | This compression method can result in high CPU overhead.  Updated rows and rows inserted without using direct-path insert are stored in row format instead of column format, and thus have a lower compression level. |
| Archive compression (Hybrid Columnar Compression) | `COMPRESS FOR ARCHIVE [LOW\|HIGH]` | Rows are compressed with archive compression. | This compression method can result in high CPU overhead.  Updated rows and rows inserted without using direct-path insert are stored in row format instead of column format, and thus have a lower compression level. |

You specify table compression with the `COMPRESS` clause of the `CREATE` `TABLE` statement. You can enable compression for an existing table by using these clauses in an `ALTER` `TABLE` statement. In this case, only data that is inserted or updated after compression is enabled is compressed. Similarly, you can disable table compression for an existing compressed table with the `ALTER` `TABLE`...`NOCOMPRESS` statement. In this case, all data that was already compressed remains compressed, and new data is inserted uncompressed.

The `COMPRESS` `FOR` `QUERY` `HIGH` option is the default data warehouse compression mode. It provides good compression and performance when using Hybrid Columnar Compression on Exadata storage. The `COMPRESS` `FOR` `QUERY` `LOW` option should be used in environments where load performance is critical. It loads faster than data compressed with the `COMPRESS` `FOR` `QUERY` `HIGH` option.

The `COMPRESS FOR ARCHIVE LOW` option is the default archive compression mode. It provides a high compression level and is ideal for infrequently-accessed data. The `COMPRESS FOR ARCHIVE HIGH` option should be used for data that is rarely accessed.

A compression advisor, provided by the `DBMS_COMPRESSION` package, helps you determine the expected compression level for a particular table with a particular compression method.

Note:

Hybrid Columnar Compression is dependent on the underlying storage system. See [Oracle Database Licensing Information](https://docs.oracle.com/cd/E11882_01/license.112/e47877/editions.htm#DBLIC2152) for more information.

See Also:

- [Oracle Database Concepts](https://docs.oracle.com/cd/E11882_01/server.112/e40540/tablecls.htm#CNCPT1132) for an overview of table compression
- ["Compressed Tablespaces"](tspaces.md)

#### Examples Related to Table Compression

The following examples are related to table compression:

- Example 20-1, "Creating a Table with OLTP Table Compression"
- Example 20-2, "Creating a Table with Basic Table Compression"
- Example 20-3, "Using Direct-Path Insert to Insert Rows Into a Table"
- Example 20-4, "Creating a Table with Warehouse Compression"
- Example 20-5, "Creating a Table with Archive Compression"

Example 20-1 Creating a Table with OLTP Table Compression

The following example enables OLTP table compression on the table `orders`:

```
CREATE TABLE orders  ...  COMPRESS FOR OLTP;
```

Data for the `orders` table is compressed during both direct-path `INSERT` and conventional DML.

Example 20-2 Creating a Table with Basic Table Compression

The following statements, which are equivalent, enable basic table compression on the `sales_history` table, which is a fact table in a data warehouse:

```
CREATE TABLE sales_history  ...  COMPRESS BASIC;

CREATE TABLE sales_history  ...  COMPRESS;
```

Frequent queries are run against this table, but no DML is expected.

Example 20-3 Using Direct-Path Insert to Insert Rows Into a Table

This example demonstrates using the `APPEND` hint to insert rows into the `sales_history` table using direct-path `INSERT`.

```
INSERT /*+ APPEND */ INTO sales_history SELECT * FROM sales WHERE cust_id=8890;
COMMIT;
```

Example 20-4 Creating a Table with Warehouse Compression

This example enables Hybrid Columnar Compression on the table `sales_history`:

```
CREATE TABLE sales_history  ...  COMPRESS FOR QUERY;
```

The table is created with the default `COMPRESS FOR QUERY HIGH` option. This option provides a higher level of compression than basic or OLTP compression. It works well when load performance is critical, frequent queries are run against this table, and no DML is expected.

Example 20-5 Creating a Table with Archive Compression

The following example enables Hybrid Columnar Compression on the table `sales_history`:

```
CREATE TABLE sales_history  ...  COMPRESS FOR ARCHIVE;
```

The table is created with the default `COMPRESS FOR ARCHIVE LOW` option. This option provides the highest level of compression and works well for infrequently-accessed data.

#### Compression and Partitioned Tables

A table can have both compressed and uncompressed partitions, and different partitions can use different compression methods. If the compression settings for a table and one of its partitions do not match, then the partition setting has precedence for the partition.

To change the compression method for a partition, do one of the following:

- To change the compression method for new data only, use `ALTER` `TABLE`... `MODIFY` `PARTITION`... `COMPRESS`...
- To change the compression method for both new and existing data, use either `ALTER` `TABLE`... `MOVE` `PARTITION`... `COMPRESS`... or online table redefinition.

#### Determining If a Table Is Compressed

In the `*_TABLES` data dictionary views, compressed tables have `ENABLED` in the `COMPRESSION` column. For partitioned tables, this column is null, and the `COMPRESSION` column of the `*_TAB_PARTITIONS` views indicates the partitions that are compressed. In addition, the `COMPRESS_FOR` column indicates the compression method in use for the table or partition.

```
SQL> SELECT table_name, compression, compress_for FROM user_tables;
 
TABLE_NAME       COMPRESSION   COMPRESS_FOR
---------------- ------------  -----------------
T1               DISABLED
T2               ENABLED       BASIC
T3               ENABLED       OLTP
T4               ENABLED       QUERY HIGH
T5               ENABLED       ARCHIVE LOW
```
```
SQL> SELECT table_name, partition_name, compression, compress_for
  FROM user_tab_partitions;

TABLE_NAME  PARTITION_NAME   COMPRESSION   COMPRESS_FOR
----------- ---------------- -----------   ------------------------------
SALES       Q4_2004          ENABLED       ARCHIVE HIGH
  ...
SALES       Q3_2008          ENABLED       QUERY HIGH
SALES       Q4_2008          ENABLED       QUERY HIGH
SALES       Q1_2009          ENABLED       OLTP
SALES       Q2_2009          ENABLED       OLTP
```

#### Determining Which Rows Are Compressed

When Hybrid Columnar Compression tables are updated, the rows change to a lower level of compression, such as from warehouse compression (`QUERY` `HIGH`) to OLTP compression or no compression. To determine the compression level of a row, use the `GET_COMPRESSION_TYPE` function in the `DBMS_COMPRESSION` package.

For example, the following query returns the compression type for a row in the `hr.employees` table:

```
SELECT DECODE(DBMS_COMPRESSION.GET_COMPRESSION_TYPE(
                 ownname => 'HR', 
                 tabname => 'EMPLOYEES', 
                 row_id  => 'AAAVEIAAGAAAABTAAD'), 
   1,  'No Compression',
   2,  'Basic or OLTP Compression', 
   4,  'Hybrid Columnar Compression for Query High',
   8,  'Hybrid Columnar Compression for Query Low',
   16, 'Hybrid Columnar Compression for Archive High',
   32, 'Hybrid Columnar Compression for Archive Low',
   'Unknown Compression Type') compression_type
FROM DUAL;
```

By sampling the table rows, you can determine the percentage of rows that are no longer at the higher compression level. You can use `ALTER TABLE` or `MOVE PARTITION` to specify a higher compression level. For example, if 10 percent of the rows are no longer at the highest compression level, then you might alter the table or move the partition to specify a higher compression level.

See Also:

[Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/d_compress.htm#ARPLS65610) for additional information about `GET_COMPRESSION_TYPE`

#### Changing the Compression Level

You can change the compression level for a partition, table, or tablespace. For example, suppose a company uses warehouse compression for its sales data, but sales data older than six months is rarely accessed. If the sales data is stored in a table that is partitioned based on the age of the data, then the compression level for the older data can be changed to archive compression to free disk space.

If a table is partitioned, then the `DBMS_REDEFINITION` package can change the compression level of the table. This package performs online redefinition of a table by creating a temporary copy of the table that holds the table data while it is being redefined. The table being redefined remains available for queries and DML statements during the redefinition. The amount of free space for online table redefinition depends on the relative compression level of the existing table and the new table. Ensure you have enough hard disk space on your system before using the `DBMS_REDEFINITION` package.

If a table is not partitioned, then you can use the `ALTER TABLE...MOVE...COMPRESS FOR...` statement to change the compression level. The `ALTER TABLE...MOVE` statement does not permit DML statements against the table while the command is running.

To change the compression level for a partition, use the `ALTER TABLE...MODIFY PARTITION` statement. To change the compression level for a tablespace, use the `ALTER TABLESPACE` statement.

See Also:

- "Moving a Table to a New Segment or Tablespace" for additional information about the `ALTER TABLE` command
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/d_redefi.htm#ARPLS042) for additional information about the `DBMS_REDEFINITION` package

#### Adding and Dropping Columns in Compressed Tables

The following restrictions apply when adding columns to compressed tables:

- Basic compression—You cannot specify a default value for an added column.
- OLTP compression—If a default value is specified for an added column, then the column must be `NOT` `NULL`. Added nullable columns with default values are not supported.

The following restrictions apply when dropping columns in compressed tables:

- Basic compression—Dropping a column is not supported.
- OLTP compression— `DROP` `COLUMN` is supported, but internally the database sets the column `UNUSED` to avoid long-running decompression and recompression operations.

#### Exporting and Importing Hybrid Columnar Compression Tables

Hybrid Columnar Compression tables can be imported using the `impdp` command of the Data Pump Import utility. By default, the `impdp` command preserves the table properties, and the imported table is a Hybrid Columnar Compression table. On tablespaces not supporting Hybrid Columnar Compression, the `impdp` command fails with an error. The tables can also be exported using the `expdp` command.

You can import the Hybrid Columnar Compression table as an uncompressed table using the `TRANSFORM:SEGMENT_ATTRIBUTES=n` option clause of the `impdp` command.

An uncompressed or OLTP-compressed table can be converted to Hybrid Columnar Compression format during import. To convert a non-Hybrid Columnar Compression table to a Hybrid Columnar Compression table, do the following:

1. Specify default compression for the tablespace using the `ALTER TABLESPACE ... SET DEFAULT COMPRESS` command.
2. Override the `SEGMENT_ATTRIBUTES` option of the imported table during import.

See Also:

- [Oracle Database Utilities](https://docs.oracle.com/cd/E11882_01/server.112/e22490/dp_import.htm#SUTIL300) for additional information about the Data Pump Import utility
- [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_3002.htm#SQLRF01002) for additional information about the `ALTER TABLESPACE` command

#### Restoring a Hybrid Columnar Compression Table

There may be times when a Hybrid Columnar Compression table must be restored from a backup. The table can be restored to a system that supports Hybrid Columnar Compression, or to a system that does not support Hybrid Columnar Compression. When restoring a table with Hybrid Columnar Compression to a system that supports Hybrid Columnar Compression, restore the file using Oracle Recovery Manager (RMAN) as usual.

When a Hybrid Columnar Compression table is restored to a system that does not support Hybrid Columnar Compression, you must convert the table from Hybrid Columnar Compression to OLTP compression or an uncompressed format. To restore the table, do the following:

1. Ensure there is sufficient storage in environment to hold the data in uncompressed or OLTP compression format.
2. Use RMAN to restore the Hybrid Columnar Compression tablespace.
3. Complete one of the following actions to convert the table from Hybrid Columnar Compression to OLTP compression or an uncompressed format:
	- Use the following statement to change the data compression from Hybrid Columnar Compression to `COMPRESS FOR OLTP`:
		```
		ALTER TABLE table_name
		 MOVE COMPRESS FOR OLTP;
		```
		- Use the following statement to change the data compression from Hybrid Columnar Compression to `NOCOMPRESS`:
		```
		ALTER TABLE table_name
		 MOVE NOCOMPRESS;
		```
		- Use the following statement to change each partition to `NOCOMPRESS`:
		```
		ALTER TABLE table_name
		 MOVE PARTITION partition_name
		 NOCOMPRESS;
		```
		Change each partition separately.
		- Use the following statement to move the data to `NOCOMPRESS` in parallel:
		```
		ALTER TABLE table_name
		 MOVE NOCOMPRESS PARALLEL;
		```

See ALso:

- [Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/cd/E11882_01/backup.112/e10642/rcmquick.htm#BRADV89346) for additional information about RMAN
- [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_3001.htm#SQLRF01001) for additional information about the `ALTER TABLE` command

#### Notes and Other Restrictions for Compressed Tables

The following are notes and restrictions related to compressed tables:

- Online segment shrink is not supported for compressed tables.
- The table compression methods described in this section do not apply to SecureFiles large objects (LOBs). SecureFiles LOBs have their own compression methods. See [Oracle Database SecureFiles and Large Objects Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e18294/adlob_smart.htm#ADLOB4444) for more information.
- Compression technology uses CPU. Ensure that you have enough available CPU to handle the additional load.
- Tables created with basic compression have the `PCT_FREE` parameter automatically set to `0` unless you specify otherwise.

#### Packing Compressed Tables

If you use conventional DML on a table compressed with basic compression or Hybrid Columnar Compression, then all inserted and updated rows are stored uncompressed or in a less-compressed format. To "pack" the compressed table so that these rows are compressed, use an `ALTER` `TABLE` `MOVE` statement. This operation takes an exclusive lock on the table, and therefore prevents any updates and loads until it completes. If this is not acceptable, then you can use online table redefinition.

See Also:

- [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/toc.htm) for more details on the `CREATE` `TABLE`...`COMPRESS`, `ALTER` `TABLE`...`COMPRESS`, and `ALTER` `TABLE`...`MOVE` statements, including restrictions
- [Oracle Database VLDB and Partitioning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25523/toc.htm) for more information on table partitioning
- "Improving INSERT Performance with Direct-Path INSERT"
- "Redefining Tables Online"

### Consider Encrypting Columns That Contain Sensitive Data

You can encrypt individual table columns that contain sensitive data. Examples of sensitive data include social security numbers, credit card numbers, and medical records. Column encryption is transparent to your applications, with some restrictions.

Although encryption is not meant to solve all security problems, it does protect your data from users who try to circumvent the security features of the database and access database files directly through the operating system file system.

Column encryption uses the transparent data encryption feature of Oracle Database, which requires that you create an Oracle wallet to store the master encryption key for the database. The wallet must be open before you can create a table with encrypted columns and before you can store or retrieve encrypted data. When you open the wallet, it is available to all sessions, and it remains open until you explicitly close it or until the database is shut down.

Transparent data encryption supports industry-standard encryption algorithms, including the following Advanced Encryption Standard (AES) and Triple Data Encryption Standard (3DES) algorithms:

- AES256
- AES192
- AES128
- 3DES168

You choose the algorithm to use when you create the table. All encrypted columns in the table use the same algorithm. The default is AES192. The encryption key length is implied by the algorithm name. For example, the AES128 algorithm uses 128-bit keys.

If you plan on encrypting many columns in one or more tables, you may want to consider encrypting an entire tablespace instead and storing these tables in that tablespace. Tablespace encryption, which also uses the transparent data encryption feature but encrypts at the physical block level, can perform better than encrypting many columns. Another reason to encrypt at the tablespace level is to address the following limitations of column encryption:

- If the `COMPATIBLE` initialization parameter set to 10.2.0, which is the minimum setting to enable transparent data encryption, data from encrypted columns that is involved in a sort or hash-join and that must be written to a temporary tablespace is written in clear text, and thus exposed to attacks. You must set `COMPATIBLE` to 11.1.0 or higher to ensure that encrypted data written to a temporary tablespace remains encrypted. Note that as long as `COMPATIBLE` is set to 10.2.0 or higher, data from encrypted columns remains encrypted when written to the undo tablespace or the redo log.
- Certain data types, such as object data types, are not supported for column encryption.
- You cannot use the transportable tablespace feature for a tablespace that includes tables with encrypted columns.
- Other restrictions, which are detailed in [Oracle Database Advanced Security Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e40393/asotrans.htm#ASOAG9518).

See Also:

- ["Encrypted Tablespaces"](tspaces.md)
- "Example: Creating a Table"
- [Oracle Database Advanced Security Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e40393/asotrans.htm#ASOAG600) for more information about transparent data encryption and for instructions for creating and opening wallets
- [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_7002.htm#SQLRF01402) for information about the `CREATE` `TABLE` statement
- [Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41960/design.htm#RACAD510) for information on using an Oracle wallet in an Oracle Real Application Clusters environment
- ["Transporting Tablespaces Between Databases"](tspaces.md)

### Understand Deferred Segment Creation

Beginning with Oracle Database 11g Release 2, when you create heap-organized tables in a locally managed tablespace, the database defers table segment creation until the first row is inserted.

In addition, segment creation is deferred for any LOB columns of the table, any indexes created implicitly as part of table creation, and any indexes subsequently explicitly created on the table.

Note:

In Release 11.2.0.1, deferred segment creation is not supported for partitioned tables. This restriction is removed in release 11.2.0.2 and later.

The advantages of this space allocation method are the following:

- It saves a significant amount of disk space in applications that create hundreds or thousands of tables upon installation, many of which might never be populated.
- It reduces application installation time.

There is a small performance penalty when the first row is inserted, because the new segment must be created at that time.

To enable deferred segment creation, compatibility must be set to '11.2.0' or higher.

The new clauses for the `CREATE` `TABLE` statement are:

- `SEGMENT` `CREATION` `DEFERRED`
- `SEGMENT` `CREATION` `IMMEDIATE`

These clauses override the default setting of the `DEFERRED_SEGMENT_CREATION` initialization parameter, `TRUE`, which defers segment creation. To disable deferred segment creation, set this parameter to `FALSE`.

Note that when you create a table with deferred segment creation, the new table appears in the `*_TABLES` views, but no entry for it appears in the `*_SEGMENTS` views until you insert the first row.

You can verify deferred segment creation by viewing the `SEGMENT_CREATED` column in `*_TABLES`, `*_INDEXES`, and `*_LOBS` views for nonpartitioned tables, and in `*_TAB_PARTITIONS`, `*_IND_PARTITIONS,` and `*_LOB_PARTITIONS` views for partitioned tables.

Note:

With this new allocation method, it is essential that you do proper capacity planning so that the database has enough disk space to handle segment creation when tables are populated. See ["Capacity Planning for Database Objects"](schema.md).

The following example creates two tables to demonstrate deferred segment creation. The first table uses the `SEGMENT` `CREATION` `DEFERRED` clause. No segments are created for it initially. The second table uses the `SEGMENT` `CREATION` `IMMEDIATE` clause and, therefore, segments are created for it immediately.

```
CREATE TABLE part_time_employees (
    empno NUMBER(8),
    name VARCHAR2(30),
    hourly_rate NUMBER (7,2)
    )   
    SEGMENT CREATION DEFERRED;
 
CREATE TABLE hourly_employees (
    empno NUMBER(8),
    name VARCHAR2(30),
    hourly_rate NUMBER (7,2)
    ) 
   SEGMENT CREATION IMMEDIATE
   PARTITION BY RANGE(empno)
    (PARTITION empno_to_100 VALUES LESS THAN (100),
    PARTITION empno_to_200 VALUES LESS THAN (200));
```

The following query against `USER_SEGMENTS` returns two rows for `HOURLY_EMPLOYEES`, one for each partition, but returns no rows for `PART_TIME_EMPLOYEES because` segment creation for that table was deferred.

```
SELECT segment_name, partition_name FROM user_segments;
 
SEGMENT_NAME         PARTITION_NAME                                
-------------------- ------------------------------                             
HOURLY_EMPLOYEES     EMPNO_TO_100                       
HOURLY_EMPLOYEES     EMPNO_TO_200
```

The `USER_TABLES` view shows that `PART_TIME_EMPLOYEES` has no segments:

```
SELECT table_name, segment_created FROM user_tables;
```
```
TABLE_NAME                     SEGMENT_CREATED
------------------------------ ----------------------------------------
PART_TIME_EMPLOYEES            NO
HOURLY_EMPLOYEES               N/A
```

For the `HOURLY_EMPLOYEES` table, which is partitioned, the `segment_created` column is `N/A` because the `USER_TABLES` view does not provide that information for partitioned tables. It is available from the `USER_TAB_PARTITIONS` view, shown below.

```
SELECT table_name, segment_created, partition_name
 FROM user_tab_partitions;

TABLE_NAME           SEGMENT_CREATED      PARTITION_NAME
-------------------- -------------------- ------------------------------
HOURLY_EMPLOYEES     YES                  EMPNO_TO_100
HOURLY_EMPLOYEES     YES                  EMPNO_TO_200
```

The following statements add employees to these tables.

```
INSERT INTO hourly_employees VALUES (99, 'FRose', 20.00);
INSERT INTO hourly_employees VALUES (150, 'LRose', 25.00);
 
INSERT INTO part_time_employees VALUES (50, 'KReilly', 10.00);
```

Repeating the same `SELECT` statements as before shows that `PART_TIME_EMPLOYEES` now has a segment, due to the insertion of row data. `HOURLY_EMPLOYEES` remains as before.

```
SELECT segment_name, partition_name FROM user_segments;
 
SEGMENT_NAME         PARTITION_NAME
-------------------- ------------------------------
PART_TIME_EMPLOYEES
HOURLY_EMPLOYEES     EMPNO_TO_100
HOURLY_EMPLOYEES     EMPNO_TO_200
```
```
SELECT table_name, segment_created FROM user_tables;
 
TABLE_NAME           SEGMENT_CREATED
-------------------- --------------------
PART_TIME_EMPLOYEES  YES
HOURLY_EMPLOYEES     N/A
```

The `USER_TAB_PARTITIONS` view does not change.

See Also:

[Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_7002.htm#SQLRF54479) for notes and restrictions on deferred segment creation

### Materializing Segments

Beginning with Oracle Database 11g release 2 (11.2.0.2), the `DBMS_SPACE_ADMIN` package includes the `MATERIALIZE_DEFERRED_SEGMENTS()` procedure, which enables you to materialize segments for tables, table partitions, and dependent objects created with deferred segment creation enabled.

You can add segments as needed, rather than starting with more than you need and using database resources unnecessarily.

The following example materializes segments for the `EMPLOYEES` table in the `HR` schema.

```
BEGIN
  DBMS_SPACE_ADMIN.MATERIALIZE_DEFERRED_SEGMENTS(
    schema_name  => 'HR',
    table_name   => 'EMPLOYEES');
END;
```

See Also:

[Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/d_spadmn.htm#ARPLS73095) for details about this procedure

### Estimate Table Size and Plan Accordingly

Estimate the sizes of tables before creating them. Preferably, do this as part of database planning. Knowing the sizes, and uses, for database tables is an important part of database planning.

You can use the combined estimated size of tables, along with estimates for indexes, undo space, and redo log files, to determine the amount of disk space that is required to hold an intended database. From these estimates, you can make correct hardware purchases.

You can use the estimated size and growth rate of an individual table to better determine the attributes of a tablespace and its underlying data files that are best suited for the table. This can enable you to more easily manage the table disk space and improve I/O performance of applications that use the table.

See Also:

["Capacity Planning for Database Objects"](schema.md)

### Restrictions to Consider When Creating Tables

Here are some restrictions that may affect your table planning and usage:

- Tables containing object types cannot be imported into a pre-Oracle8 database.
- You cannot merge an exported table into a preexisting table having the same name in a different schema.
- You cannot move types and extent tables to a different schema when the original data still exists in the database.
- Oracle Database has a limit on the total number of columns that a table (or attributes that an object type) can have. See [Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/limits.htm#REFRN004) for this limit.
	Further, when you create a table that contains user-defined type data, the database maps columns of user-defined type to relational columns for storing the user-defined type data. This causes additional relational columns to be created. This results in "hidden" relational columns that are not visible in a `DESCRIBE` table statement and are not returned by a `SELECT *` statement. Therefore, when you create an object table, or a relational table with columns of `REF`, varray, nested table, or object type, be aware that the total number of columns that the database actually creates for the table can be more than those you specify.
	See Also:
	[Oracle Database Object-Relational Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e11822/toc.htm) for more information about user-defined types

## Creating Tables

To create a new table in your schema, you must have the `CREATE TABLE` system privilege. To create a table in another user's schema, you must have the `CREATE ANY TABLE` system privilege. Additionally, the owner of the table must have a quota for the tablespace that contains the table, or the `UNLIMITED TABLESPACE` system privilege.

Create tables using the SQL statement `CREATE TABLE`.

This section contains the following topics:

- Example: Creating a Table
- Creating a Temporary Table
- Parallelizing Table Creation
	See Also:
	[Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/toc.htm) for exact syntax of the `CREATE TABLE` and other SQL statements discussed in this chapter

### Example: Creating a Table

When you issue the following statement, you create a table named `admin_emp` in the `hr` schema and store it in the `admin_tbs` tablespace:

```
CREATE TABLE hr.admin_emp (
         empno      NUMBER(5) PRIMARY KEY,
         ename      VARCHAR2(15) NOT NULL,
         ssn        NUMBER(9) ENCRYPT USING 'AES256',
         job        VARCHAR2(10),
         mgr        NUMBER(5),
         hiredate   DATE DEFAULT (sysdate),
         photo      BLOB,
         sal        NUMBER(7,2),
         hrly_rate  NUMBER(7,2) GENERATED ALWAYS AS (sal/2080),
         comm       NUMBER(7,2),
         deptno     NUMBER(3) NOT NULL
                     CONSTRAINT admin_dept_fkey REFERENCES hr.departments
                     (department_id))
   TABLESPACE admin_tbs
   STORAGE ( INITIAL 50K);

COMMENT ON TABLE hr.admin_emp IS 'Enhanced employee table';
```

Note the following about this example:

- Integrity constraints are defined on several columns of the table.
- The `STORAGE` clause specifies the size of the first extent. See [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/clauses009.htm#SQLRF30013) for details on this clause.
- Encryption is defined on one column (`ssn`), through the transparent data encryption feature of Oracle Database. The Oracle Wallet must therefore be open for this `CREATE` `TABLE` statement to succeed.
- The `photo` column is of data type `BLOB`, which is a member of the set of data types called large objects (LOBs). LOBs are used to store semi-structured data (such as an XML tree) and unstructured data (such as the stream of bits in a color image).
- One column is defined as a virtual column (`hrly_rate`). This column computes the employee's hourly rate as the yearly salary divided by 2,080. See [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_7002.htm#SQLRF54465) for a discussion of rules for virtual columns.
- A `COMMENT` statement is used to store a comment for the table. You query the `*_TAB_COMMENTS` data dictionary views to retrieve such comments. See [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_4009.htm#SQLRF01109) for more information.

See Also:

- [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/sql_elements001.htm#SQLRF0021) for a description of the data types that you can specify for table columns
- ["Managing Integrity Constraints"](general.md)
- [Oracle Database Advanced Security Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e40393/asotrans.htm#ASOAG600) for information about transparent data encryption and the Oracle Wallet
- [Oracle Database SecureFiles and Large Objects Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e18294/toc.htm) for more information about LOBs.

### Creating a Temporary Table

Temporary tables are useful in applications where a result set is to be buffered (temporarily persisted), perhaps because it is constructed by running multiple DML operations. For example, consider the following:

A Web-based airlines reservations application allows a customer to create several optional itineraries. Each itinerary is represented by a row in a temporary table. The application updates the rows to reflect changes in the itineraries. When the customer decides which itinerary she wants to use, the application moves the row for that itinerary to a persistent table.

During the session, the itinerary data is private. At the end of the session, the optional itineraries are dropped.

The definition of a temporary table is visible to all sessions, but the data in a temporary table is visible only to the session that inserts the data into the table.

Use the `CREATE GLOBAL TEMPORARY TABLE` statement to create a temporary table. The `ON COMMIT` clause indicates if the data in the table is transaction-specific (the default) or session-specific, the implications of which are as follows:

| ON COMMIT Setting | Implications |
| --- | --- |
| `DELETE ROWS` | This creates a temporary table that is transaction specific. A session becomes bound to the temporary table with a transactions first insert into the table. The binding goes away at the end of the transaction. The database truncates the table (delete all rows) after each commit. |
| `PRESERVE ROWS` | This creates a temporary table that is session specific. A session gets bound to the temporary table with the first insert into the table in the session. This binding goes away at the end of the session or by issuing a `TRUNCATE` of the table in the session. The database truncates the table when you terminate the session. |

This statement creates a temporary table that is transaction specific:

```
CREATE GLOBAL TEMPORARY TABLE admin_work_area
        (startdate DATE,
         enddate DATE,
         class CHAR(20))
      ON COMMIT DELETE ROWS;
```

Indexes can be created on temporary tables. They are also temporary and the data in the index has the same session or transaction scope as the data in the underlying table.

By default, rows in a temporary table are stored in the default temporary tablespace of the user who creates it. However, you can assign a temporary table to another tablespace upon creation of the temporary table by using the `TABLESPACE` clause of `CREATE GLOBAL TEMPORARY TABLE`. You can use this feature to conserve space used by temporary tables. For example, if you must perform many small temporary table operations and the default temporary tablespace is configured for sort operations and thus uses a large extent size, these small operations will consume lots of unnecessary disk space. In this case it is better to allocate a second temporary tablespace with a smaller extent size.

The following two statements create a temporary tablespace with a 64 KB extent size, and then a new temporary table in that tablespace.

```
CREATE TEMPORARY TABLESPACE tbs_t1 
    TEMPFILE 'tbs_t1.f' SIZE 50m REUSE AUTOEXTEND ON
    MAXSIZE UNLIMITED
    EXTENT MANAGEMENT LOCAL UNIFORM SIZE 64K;

CREATE GLOBAL TEMPORARY TABLE admin_work_area
        (startdate DATE,
         enddate DATE,
         class CHAR(20))
      ON COMMIT DELETE ROWS
      TABLESPACE tbs_t1;
```

See Also:

["Temporary Tablespaces"](tspaces.md)

Unlike permanent tables, temporary tables and their indexes do not automatically allocate a segment when they are created. Instead, segments are allocated when the first `INSERT` (or `CREATE` `TABLE` `AS` `SELECT`) is performed. Therefore, if a `SELECT`, `UPDATE`, or `DELETE` is performed before the first `INSERT`, then the table appears to be empty.

DDL operations (except `TRUNCATE`) are allowed on an existing temporary table only if no session is currently bound to that temporary table.

If you rollback a transaction, the data you entered is lost, although the table definition persists.

A transaction-specific temporary table allows only one transaction at a time. If there are several autonomous transactions in a single transaction scope, each autonomous transaction can use the table only as soon as the previous one commits.

Because the data in a temporary table is, by definition, temporary, backup and recovery of temporary table data is not available in the event of a system failure. To prepare for such a failure, you should develop alternative methods for preserving temporary table data.

### Parallelizing Table Creation

When you specify the `AS SELECT` clause to create a table and populate it with data from another table, you can use parallel execution. The `CREATE TABLE...AS SELECT` statement contains two parts: a `CREATE` part (DDL) and a `SELECT` part (query). Oracle Database can parallelize both parts of the statement. The `CREATE` part is parallelized if one of the following is true:

- A `PARALLEL` clause is included in the `CREATE TABLE...AS SELECT` statement
- An `ALTER SESSION FORCE PARALLEL DDL` statement is specified

The query part is parallelized if all of the following are true:

- The query includes a parallel hint specification (`PARALLEL` or `PARALLEL_INDEX`) or the `CREATE` part includes the `PARALLEL` clause or the schema objects referred to in the query have a `PARALLEL` declaration associated with them.
- At least one of the tables specified in the query requires either a full table scan or an index range scan spanning multiple partitions.

If you parallelize the creation of a table, that table then has a parallel declaration (the `PARALLEL` clause) associated with it. Any subsequent DML or queries on the table, for which parallelization is possible, will attempt to use parallel execution.

The following simple statement parallelizes the creation of a table and stores the result in a compressed format, using table compression:

```
CREATE TABLE hr.admin_emp_dept
     PARALLEL COMPRESS
     AS SELECT * FROM hr.employees
     WHERE department_id = 10;
```

In this case, the `PARALLEL` clause tells the database to select an optimum number of parallel execution servers when creating the table.

See Also:

- [Oracle Database VLDB and Partitioning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25523/parallel.htm#VLDBG010) for detailed information on using parallel execution
- ["Managing Processes for Parallel SQL Execution"](manproc.md)

## Loading Tables

This section describes techniques for loading data into tables. In contains the following topics:

- Methods for Loading Tables
- Improving INSERT Performance with Direct-Path INSERT
- Using Conventional Inserts to Load Tables
- Avoiding Bulk INSERT Failures with DML Error Logging

Note:

Beginning with release 11.2.0.2 of Oracle Database, the default size of the first extent of any new segment for a partitioned table is 8 MB instead of 64 KB. This helps improve performance of inserts and queries on partitioned tables. Although partitioned tables will start with a larger initial size, once sufficient data is inserted, the space consumption will be the same as in previous releases. You can override this default by setting the `INITIAL` size in the storage clause for the table. This new default only applies to table partitions and LOB partitions.

### Methods for Loading Tables

There are several means of inserting or initially loading data into your tables. Most commonly used are the following:

| Method | Description |
| --- | --- |
| SQL\*Loader | This Oracle utility program loads data from external files into tables of an Oracle Database.  For information about SQL\*Loader, see [Oracle Database Utilities](https://docs.oracle.com/cd/E11882_01/server.112/e22490/ldr_concepts.htm#SUTIL003). |
| [`CREATE TABLE`... `AS SELECT`](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_7002.htm#SQLRF01402) statement (CTAS) | Using this SQL statement you can create a table and populate it with data selected from another existing table, including an external table. |
| [`INSERT`](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_9014.htm#SQLRF01604) statement | The `INSERT` statement enables you to add rows to a table, either by specifying the column values or by specifying a subquery that selects data from another existing table, including an external table.  One form of the `INSERT` statement enables direct-path `INSERT`, which can improve performance, and is useful for bulk loading. See "Improving INSERT Performance with Direct-Path INSERT".  If you are inserting a lot of data and want to avoid statement termination and rollback if an error is encountered, you can insert with DML error logging. See "Avoiding Bulk INSERT Failures with DML Error Logging". |
| [`MERGE`](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_9016.htm#SQLRF01606) statement | The `MERGE` statement enables you to insert rows into or update rows of a table, by selecting rows from another existing table. If a row in the new data corresponds to an item that already exists in the table, then an `UPDATE` is performed, else an `INSERT` is performed. |

See [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/toc.htm) for details on the `CREATE TABLE`... `AS SELECT`, `INSERT`, and `MERGE` statements.

Note:

Only a few details and examples of inserting data into tables are included in this book. Oracle documentation specific to data warehousing and application development provide more extensive information about inserting and manipulating data in tables. See:
- [Oracle Database Data Warehousing Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25554/part4.htm#DWHSG8270)
- [Oracle Database SecureFiles and Large Objects Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e18294/adlob_managing.htm#ADLOB45151)

See Also:

"Managing External Tables"

### Improving INSERT Performance with Direct-Path INSERT

When loading large amounts of data, you can improve load performance by using direct-path `INSERT`.

This section contains:

- About Direct-Path INSERT
- How Direct-Path INSERT Works
- Loading Data with Direct-Path INSERT
- Specifying the Logging Mode for Direct-Path INSERT
- Additional Considerations for Direct-Path INSERT

#### About Direct-Path INSERT

Oracle Database inserts data into a table in one of two ways:

- During conventional INSERT operations, the database reuses free space in the table, interleaving newly inserted data with existing data. During such operations, the database also maintains referential integrity constraints.
- During direct-path INSERT operations, the database appends the inserted data after existing data in the table. Data is written directly into data files, bypassing the buffer cache. Free space in the table is not reused, and referential integrity constraints are ignored. Direct-path `INSERT` can perform significantly better than conventional insert.

The database can insert data either in serial mode, where one process executes the statement, or in parallel mode, where multiple processes work together simultaneously to run a single SQL statement. The latter is referred to as parallel execution.

The following are benefits of direct-path `INSERT`:

- During direct-path `INSERT`, you can disable the logging of redo and undo entries to reduce load time. Conventional insert operations, in contrast, must always log such entries, because those operations reuse free space and maintain referential integrity.
- Direct-path `INSERT` operations ensure atomicity of the transaction, even when run in parallel mode. Atomicity cannot be guaranteed during parallel direct-path loads (using SQL\*Loader).

When performing parallel direct-path loads, one notable difference between SQL\*Loader and `INSERT` statements is the following: If errors occur during parallel direct-path loads with SQL\*Loader, the load completes, but some indexes could be marked `UNUSABLE` at the end of the load. Parallel direct-path `INSERT`, in contrast, rolls back the statement if errors occur during index update.

Note:

A conventional `INSERT` operation checks for violations of `NOT` `NULL` constraints during the insert. Therefore, if a `NOT` `NULL` constraint is violated for a conventional `INSERT` operation, then the error is returned during the insert. A direct-path `INSERT` operation checks for violations of `NOT` `NULL` constraints before the insert. Therefore, if a `NOT` `NULL` constraint is violated for a direct-path `INSERT` operation, then the error is returned before the insert.

#### How Direct-Path INSERT Works

You can use direct-path `INSERT` on both partitioned and nonpartitioned tables.

##### Serial Direct-Path INSERT into Partitioned or Nonpartitioned Tables

The single process inserts data beyond the current high water mark of the table segment or of each partition segment. (The high-water mark is the level at which blocks have never been formatted to receive data.) When a `COMMIT` runs, the high-water mark is updated to the new value, making the data visible to users.

##### Parallel Direct-Path INSERT into Partitioned Tables

This situation is analogous to serial direct-path `INSERT`. Each parallel execution server is assigned one or more partitions, with no more than one process working on a single partition. Each parallel execution server inserts data beyond the current high-water mark of its assigned partition segment(s). When a `COMMIT` runs, the high-water mark of each partition segment is updated to its new value, making the data visible to users.

##### Parallel Direct-Path INSERT into Nonpartitioned Tables

Each parallel execution server allocates a new temporary segment and inserts data into that temporary segment. When a `COMMIT` runs, the parallel execution coordinator merges the new temporary segments into the primary table segment, where it is visible to users.

#### Loading Data with Direct-Path INSERT

You can load data with direct-path `INSERT` by using direct-path `INSERT` SQL statements, inserting data in parallel mode, or by using the Oracle SQL\*Loader utility in direct-path mode. A direct-path `INSERT` can be done in either serial or parallel mode.

##### Serial Mode Inserts with SQL Statements

You can activate direct-path `INSERT` in serial mode with SQL in the following ways:

- If you are performing an `INSERT` with a subquery, specify the `APPEND` hint in each `INSERT` statement, either immediately after the `INSERT` keyword, or immediately after the `SELECT` keyword in the subquery of the `INSERT` statement.
- If you are performing an `INSERT` with the `VALUES` clause, specify the `APPEND_VALUES` hint in each `INSERT` statement immediately after the `INSERT` keyword. Direct-path `INSERT` with the `VALUES` clause is best used when there are hundreds of thousands or millions of rows to load. The typical usage scenario is for array inserts using OCI. Another usage scenario might be inserts in a `FORALL` statement in PL/SQL.

If you specify the `APPEND` hint (as opposed to the `APPEND_VALUES` hint) in an `INSERT` statement with a `VALUES` clause, the `APPEND` hint is ignored and a conventional insert is performed.

The following is an example of using the `APPEND` hint to perform a direct-path `INSERT`:

```
INSERT /*+ APPEND */ INTO sales_hist SELECT * FROM sales WHERE cust_id=8890;
```

The following PL/SQL code fragment is an example of using the `APPEND_VALUES` hint:

```
FORALL i IN 1..numrecords
  INSERT /*+ APPEND_VALUES */ INTO orderdata 
  VALUES(ordernum(i), custid(i), orderdate(i),shipmode(i), paymentid(i));
COMMIT;
```

##### Parallel Mode Inserts with SQL Statements

When you are inserting in parallel mode, direct-path `INSERT` is the default. However, you can insert in parallel mode using conventional `INSERT` by using the `NOAPPEND` `PARALLEL` hint.

To run in parallel DML mode, the following requirements must be met:

- You must have Oracle Enterprise Edition installed.
- You must enable parallel DML in your session. To do this, submit the following statement:
	```
	ALTER SESSION { ENABLE | FORCE } PARALLEL DML;
	```
- You must meet at least one of the following requirements:
	- Specify the parallel attribute for the target table, either at create time or subsequently
		- Specify the `PARALLEL` hint for each insert operation
		- Set the database initialization parameter `PARALLEL_DEGREE_POLICY` to `AUTO`

To disable direct-path `INSERT`, specify the `NOAPPEND` hint in each `INSERT` statement. Doing so overrides parallel DML mode.

Note:

You cannot query or modify data inserted using direct-path `INSERT` immediately after the insert is complete. If you attempt to do so, an ORA-12838 error is generated. You must first issue a `COMMIT` statement before attempting to read or modify the newly-inserted data.

See Also:

- "Using Conventional Inserts to Load Tables"
- [Oracle Database Performance Tuning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41573/hintsref.htm#PFGRF005) for more information on using hints
- [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_9014.htm#SQLRF01604) for more information on the subquery syntax of `INSERT` statements and for additional restrictions on using direct-path `INSERT`

#### Specifying the Logging Mode for Direct-Path INSERT

Direct-path `INSERT` lets you choose whether to log redo and undo information during the insert operation.

- You can specify logging mode for a table, partition, index, or `LOB` storage at create time (in a `CREATE` statement) or subsequently (in an `ALTER` statement).
- If you do not specify either `LOGGING` or `NOLOGGING` at these times:
	- The logging attribute of a partition defaults to the logging attribute of its table.
		- The logging attribute of a table or index defaults to the logging attribute of the tablespace in which it resides.
		- The logging attribute of `LOB` storage defaults to `LOGGING` if you specify `CACHE` for `LOB` storage. If you do not specify `CACHE`, then the logging attributes defaults to that of the tablespace in which the `LOB` values resides.
- You set the logging attribute of a tablespace in a `CREATE` `TABLESPACE` or `ALTER` `TABLESPACE` statements.
	Note:
	If the database or tablespace is in `FORCE` `LOGGING` mode, then direct path `INSERT` always logs, regardless of the logging setting.

##### Direct-Path INSERT with Logging

In this mode, Oracle Database performs full redo logging for instance and media recovery. If the database is in `ARCHIVELOG` mode, then you can archive redo logs to tape. If the database is in `NOARCHIVELOG` mode, then you can recover instance crashes but not disk failures.

##### Direct-Path INSERT without Logging

In this mode, Oracle Database inserts data without redo or undo logging. Instead, the database logs a small number of block range invalidation redo records and periodically updates the control file with information about the most recent direct write.

Direct-path `INSERT` without logging improves performance. However, if you subsequently must perform media recovery, the invalidation redo records mark a range of blocks as logically corrupt, because no redo data was logged for them. Therefore, it is important that you back up the data after such an insert operation.

Beginning with release 11.2.0.2 of Oracle Database, you can significantly improve the performance of unrecoverable direct path inserts by disabling the periodic update of the control files. You do so by setting the initialization parameter `DB_UNRECOVERABLE_SCN_TRACKING` to `FALSE`. However, if you perform an unrecoverable direct path insert with these control file updates disabled, you will no longer be able to accurately query the database to determine if any data files are currently unrecoverable.

See Also:

- [Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/cd/E11882_01/backup.112/e10642/rcmreprt.htm#BRADV89598) for more information about unrecoverable data files
- The section "Determining If a Backup Is Required After Unrecoverable Operations" in [Oracle Data Guard Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e41134/scenarios.htm#SBYDB4896)

#### Additional Considerations for Direct-Path INSERT

The following are some additional considerations when using direct-path `INSERT`.

##### Compressed Tables

If a table is created with the basic compression, then you must use direct-path `INSERT` to compress table data as it is loaded. If a table is created with OLTP, warehouse, or archive compression, then best compression ratios are achieved with direct-path `INSERT`.

See "Consider Using Table Compression" for more information.

##### Index Maintenance with Direct-Path INSERT

Oracle Database performs index maintenance at the end of direct-path `INSERT` operations on tables (partitioned or nonpartitioned) that have indexes. This index maintenance is performed by the parallel execution servers for parallel direct-path `INSERT` or by the single process for serial direct-path `INSERT`. You can avoid the performance impact of index maintenance by making the index unusable before the `INSERT` operation and then rebuilding it afterward.

See Also:

["Making an Index Unusable"](indexes.md)

##### Space Considerations with Direct-Path INSERT

Direct-path `INSERT` requires more space than conventional-path `INSERT`.

All serial direct-path `INSERT` operations, as well as parallel direct-path `INSERT` into partitioned tables, insert data above the high-water mark of the affected segment. This requires some additional space.

Parallel direct-path `INSERT` into nonpartitioned tables requires even more space, because it creates a temporary segment for each degree of parallelism. If the nonpartitioned table is not in a locally managed tablespace in automatic segment-space management mode, you can modify the values of the `NEXT` and `PCTINCREASE` storage parameter and `MINIMUM` `EXTENT` tablespace parameter to provide sufficient (but not excess) storage for the temporary segments. Choose values for these parameters so that:

- The size of each extent is not too small (no less than 1 MB). This setting affects the total number of extents in the object.
- The size of each extent is not so large that the parallel `INSERT` results in wasted space on segments that are larger than necessary.

After the direct-path `INSERT` operation is complete, you can reset these parameters to settings more appropriate for serial operations.

##### Locking Considerations with Direct-Path INSERT

During direct-path `INSERT`, the database obtains exclusive locks on the table (or on all partitions of a partitioned table). As a result, users cannot perform any concurrent insert, update, or delete operations on the table, and concurrent index creation and build operations are not permitted. Concurrent queries, however, are supported, but the query will return only the information before the insert operation.

### Using Conventional Inserts to Load Tables

During conventional INSERT operations, the database reuses free space in the table, interleaving newly inserted data with existing data. During such operations, the database also maintains referential integrity constraints. Unlike direct-path `INSERT` operations, conventional `INSERT` operations do not require an exclusive lock on the table.

Several other restrictions apply to direct-path `INSERT` operations that do not apply to conventional `INSERT` operations. See [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_9014.htm#SQLRF55049) for information about these restrictions.

You can perform a conventional `INSERT` operation in serial mode or in parallel mode using the `NOAPPEND` hint.

The following is an example of using the `NOAPPEND` hint to perform a conventional `INSERT` in serial mode:

```
INSERT /*+ NOAPPEND */ INTO sales_hist SELECT * FROM sales WHERE cust_id=8890;
```

The following is an example of using the `NOAPPEND` hint to perform a conventional `INSERT` in parallel mode:

```
INSERT /*+ NOAPPEND PARALLEL */ INTO sales_hist
   SELECT * FROM sales;
```

To run in parallel DML mode, the following requirements must be met:

- You must have Oracle Enterprise Edition installed.
- You must enable parallel DML in your session. To do this, submit the following statement:
	```
	ALTER SESSION { ENABLE | FORCE } PARALLEL DML;
	```
- You must meet at least one of the following requirements:
	- Specify the parallel attribute for the target table, either at create time or subsequently
		- Specify the `PARALLEL` hint for each insert operation
		- Set the database initialization parameter `PARALLEL_DEGREE_POLICY` to `AUTO`

### Avoiding Bulk INSERT Failures with DML Error Logging

When you load a table using an `INSERT` statement with subquery, if an error occurs, the statement is terminated and rolled back in its entirety. This can be wasteful of time and system resources. For such `INSERT` statements, you can avoid this situation by using the DML error logging feature.

To use DML error logging, you add a statement clause that specifies the name of an error logging table into which the database records errors encountered during DML operations. When you add this error logging clause to the `INSERT` statement, certain types of errors no longer terminate and roll back the statement. Instead, each error is logged and the statement continues. You then take corrective action on the erroneous rows at a later time.

DML error logging works with `INSERT`, `UPDATE`, `MERGE`, and `DELETE` statements. This section focuses on `INSERT` statements.

To insert data with DML error logging:

1. Create an error logging table. (Optional)
	You can create the table manually or use the `DBMS_ERRLOG` package to automatically create it for you. See "Creating an Error Logging Table" for details.
2. Execute an `INSERT` statement and include an error logging clause. This clause:
	- Optionally references the error logging table that you created. If you do not provide an error logging table name, the database logs to an error logging table with a default name. The default error logging table name is `ERR$_` followed by the first 25 characters of the name of the table that is being inserted into.
		- Optionally includes a tag (a numeric or string literal in parentheses) that gets added to the error log to help identify the statement that caused the errors. If the tag is omitted, a `NULL` value is used.
		- Optionally includes a `REJECT LIMIT` subclause.
		This subclause indicates the maximum number of errors that can be encountered before the `INSERT` statement terminates and rolls back. You can also specify `UNLIMITED`. The default reject limit is zero, which means that upon encountering the first error, the error is logged and the statement rolls back. For parallel DML operations, the reject limit is applied to each parallel server.
	Note:
	If the statement exceeds the reject limit and rolls back, the error logging table retains the log entries recorded so far.
	See [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_9014.htm#SQLRF55061) for error logging clause syntax information.
3. Query the error logging table and take corrective action for the rows that generated errors.
	See "Error Logging Table Format", later in this section, for details on the error logging table structure.

Example The following statement inserts rows into the `DW_EMPL` table and logs errors to the `ERR_EMPL` table. The tag ' `daily_load` ' is copied to each log entry. The statement terminates and rolls back if the number of errors exceeds 25.

```
INSERT INTO dw_empl
  SELECT employee_id, first_name, last_name, hire_date, salary, department_id 
  FROM employees
  WHERE hire_date > sysdate - 7
  LOG ERRORS INTO err_empl ('daily_load') REJECT LIMIT 25
```

For more examples, see [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_9014.htm#SQLRF55104) and [Oracle Database Data Warehousing Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25554/transform.htm#DWHSG8337).

#### Error Logging Table Format

The error logging table consists of two parts:

- A mandatory set of columns that describe the error. For example, one column contains the Oracle error number.
	Table 20-3 lists these error description columns.
- An optional set of columns that contain data from the row that caused the error. The column names match the column names from the table being inserted into (the "DML table").
	The number of columns in this part of the error logging table can be zero, one, or more, up to the number of columns in the DML table. If a column exists in the error logging table that has the same name as a column in the DML table, the corresponding data from the offending row being inserted is written to this error logging table column. If a DML table column does not have a corresponding column in the error logging table, the column is not logged. If the error logging table contains a column with a name that does not match a DML table column, the column is ignored.
	Because type conversion errors are one type of error that might occur, the data types of the optional columns in the error logging table must be types that can capture any value without data loss or conversion errors. (If the optional log columns were of the same types as the DML table columns, capturing the problematic data into the log could suffer the same data conversion problem that caused the error.) The database makes a best effort to log a meaningful value for data that causes conversion errors. If a value cannot be derived, `NULL` is logged for the column. An error on insertion into the error logging table causes the statement to terminate.
	Table 20-4 lists the recommended error logging table column data types to use for each data type from the DML table. These recommended data types are used when you create the error logging table automatically with the `DBMS_ERRLOG` package.

Table 20-3 Mandatory Error Description Columns

| Column Name | Data Type | Description |
| --- | --- | --- |
| `ORA_ERR_NUMBER$` | `NUMBER` | Oracle error number |
| `ORA_ERR_MESG$` | `VARCHAR2(2000)` | Oracle error message text |
| `ORA_ERR_ROWID$` | `ROWID` | Rowid of the row in error (for update and delete) |
| `ORA_ERR_OPTYP$` | `VARCHAR2(2)` | Type of operation: insert (`I`), update (`U`), delete (`D`)  Note: Errors from the update clause and insert clause of a `MERGE` operation are distinguished by the `U` and `I` values. |
| `ORA_ERR_TAG$` | `VARCHAR2(2000)` | Value of the tag supplied by the user in the error logging clause |

Table 20-4 Error Logging Table Column Data Types

| DML Table Column Type | Error Logging Table Column Type | Notes |
| --- | --- | --- |
| `NUMBER` | `VARCHAR2(4000)` | Able to log conversion errors |
| `CHAR/VARCHAR2(n)` | `VARCHAR2(4000)` | Logs any value without information loss |
| `NCHAR/NVARCHAR2(n)` | `NVARCHAR2(4000)` | Logs any value without information loss |
| `DATE/TIMESTAMP` | `VARCHAR2(4000)` | Logs any value without information loss. Converts to character format with the default date/time format mask |
| `RAW` | `RAW(2000)` | Logs any value without information loss |
| `ROWID` | `UROWID` | Logs any rowid type |
| `LONG/LOB` |  | Not supported |
| User-defined types |  | Not supported |

#### Creating an Error Logging Table

You can create an error logging table manually, or you can use a PL/SQL package to automatically create one for you.

##### Creating an Error Logging Table Automatically

You use the `DBMS_ERRLOG` package to automatically create an error logging table. The `CREATE_ERROR_LOG` procedure creates an error logging table with all of the mandatory error description columns plus all of the columns from the named DML table, and performs the data type mappings shown in Table 20-4.

The following statement creates the error logging table used in the previous example.

```
EXECUTE DBMS_ERRLOG.CREATE_ERROR_LOG('DW_EMPL', 'ERR_EMPL');
```

See [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/d_errlog.htm#ARPLS680) for details on `DBMS_ERRLOG`.

##### Creating an Error Logging Table Manually

You use standard DDL to manually create the error logging table. See "Error Logging Table Format" for table structure requirements. You must include all mandatory error description columns. They can be in any order, but must be the first columns in the table.

#### Error Logging Restrictions and Caveats

Oracle Database logs the following errors during DML operations:

- Column values that are too large
- Constraint violations (`NOT` `NULL`, unique, referential, and check constraints)
- Errors raised during trigger execution
- Errors resulting from type conversion between a column in a subquery and the corresponding column of the table
- Partition mapping errors
- Certain `MERGE` operation errors (`ORA-30926`: Unable to get a stable set of rows for MERGE operation.)

Some errors are not logged, and cause the DML operation to terminate and roll back. For a list of these errors and for other DML logging restrictions, see the discussion of the `error_logging_clause` in the `INSERT` section of [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_9014.htm#SQLRF55101).

##### Space Considerations

Ensure that you consider space requirements before using DML error logging. You require available space not only for the table being inserted into, but also for the error logging table.

##### Security

The user who issues the `INSERT` statement with DML error logging must have `INSERT` privileges on the error logging table.

See Also:

[Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_9014.htm#SQLRF55101) and [Oracle Database Data Warehousing Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25554/transform.htm#DWHSG8337) for DML error logging examples.

## Automatically Collecting Statistics on Tables

The PL/SQL package DBMS\_STATS lets you generate and manage statistics for cost-based optimization. You can use this package to gather, modify, view, export, import, and delete statistics. You can also use this package to identify or name statistics that have been gathered.

Formerly, you enabled `DBMS_STATS` to automatically gather statistics for a table by specifying the `MONITORING` keyword in the `CREATE` (or `ALTER`) `TABLE` statement. Starting with Oracle Database 11g, the `MONITORING` and `NOMONITORING` keywords have been deprecated and statistics are collected automatically. If you do specify these keywords, they are ignored.

Monitoring tracks the approximate number of `INSERT`, `UPDATE`, and `DELETE` operations for the table since the last time statistics were gathered. Information about how many rows are affected is maintained in the SGA, until periodically (about every three hours) SMON incorporates the data into the data dictionary. This data dictionary information is made visible through the `DBA_TAB_MODIFICATIONS,ALL_TAB_MODIFICATIONS`, or `USER_TAB_MODIFICATIONS` views. The database uses these views to identify tables with stale statistics.

The default for the STATISTICS\_LEVEL initialization parameter is `TYPICAL`, which enables automatic statistics collection. Automatic statistics collection and the `DBMS_STATS` package enable the optimizer to generate accurate execution plans. Setting the `STATISTICS_LEVEL` initialization parameter to `BASIC` disables the collection of many of the important statistics required by Oracle Database features and functionality. To disable monitoring of all tables, set the `STATISTICS_LEVEL` initialization parameter to `BASIC`. Automatic statistics collection and the `DBMS_STATS` package enable the optimizer to generate accurate execution plans.

See Also:

- [Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams254.htm#REFRN10214) for detailed information on the `STATISTICS_LEVEL` initialization parameter
- [Oracle Database Performance Tuning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41573/stats.htm#PFGRF003) for information on managing optimizer statistics
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/d_stats.htm#ARPLS059) for information about using the `DBMS_STATS` package
- ["About Automated Maintenance Tasks"](tasks.md) for information on using the Scheduler to collect statistics automatically

## Altering Tables

You alter a table using the `ALTER TABLE` statement. To alter a table, the table must be contained in your schema, or you must have either the `ALTER` object privilege for the table or the `ALTER ANY TABLE` system privilege.

Many of the usages of the `ALTER TABLE` statement are presented in the following sections:

- Reasons for Using the ALTER TABLE Statement
- Altering Physical Attributes of a Table
- Moving a Table to a New Segment or Tablespace
- Manually Allocating Storage for a Table
- Modifying an Existing Column Definition
- Adding Table Columns
- Renaming Table Columns
- Dropping Table Columns
- Placing a Table in Read-Only Mode

Caution:

Before altering a table, familiarize yourself with the consequences of doing so. The [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_3001.htm#SQLRF01001) lists many of these consequences in the descriptions of the `ALTER TABLE` clauses.

If a view, materialized view, trigger, domain index, function-based index, check constraint, function, procedure of package depends on a base table, the alteration of the base table or its columns can affect the dependent object. See ["Managing Object Dependencies"](general.md) for information about how the database manages dependencies.

### Reasons for Using the ALTER TABLE Statement

You can use the ALTER TABLE statement to perform any of the following actions that affect a table:

- Modify physical characteristics (`INITRANS` or storage parameters)
- Move the table to a new segment or tablespace
- Explicitly allocate an extent or deallocate unused space
- Add, drop, or rename columns, or modify an existing column definition (data type, length, default value, `NOT NULL` integrity constraint, column expression (for virtual columns), and encryption properties.)
- Modify the logging attributes of the table
- Modify the `CACHE` / `NOCACHE` attributes
- Add, modify or drop integrity constraints associated with the table
- Enable or disable integrity constraints or triggers associated with the table
- Modify the degree of parallelism for the table
- Rename a table
- Put a table in read-only mode and return it to read/write mode
- Add or modify index-organized table characteristics
- Alter the characteristics of an external table
- Add or modify `LOB` columns
- Add or modify object type, nested table, or varray columns

Many of these operations are discussed in succeeding sections.

### Altering Physical Attributes of a Table

When altering the transaction entry setting `INITRANS` of a table, note that a new setting for `INITRANS` applies only to data blocks subsequently allocated for the table.

The storage parameters `INITIAL` and `MINEXTENTS` cannot be altered. All new settings for the other storage parameters (for example, `NEXT`, `PCTINCREASE`) affect only extents subsequently allocated for the table. The size of the next extent allocated is determined by the current values of `NEXT` and `PCTINCREASE`, and is not based on previous values of these parameters.

See Also:

The discussions of the physical attributes clause and the storage clause in [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/clauses.htm#SQLRF021)

### Moving a Table to a New Segment or Tablespace

The `ALTER TABLE...MOVE` statement enables you to relocate data of a nonpartitioned table or of a partition of a partitioned table into a new segment, and optionally into a different tablespace for which you have quota. This statement also lets you modify any of the storage attributes of the table or partition, including those which cannot be modified using `ALTER TABLE`. You can also use the `ALTER TABLE...MOVE` statement with a `COMPRESS` clause to store the new segment using table compression.

One important reason to move a table to a new tablespace (with a new data file) is to eliminate the possibility that old versions of column data—versions left on now unused portions of the disk due to segment shrink, reorganization, or previous table moves—could be viewed by bypassing the access controls of the database (for example with an operating system utility). This is especially important with columns that you intend to modify by adding transparent data encryption.

Note:

The `ALTER TABLE...MOVE` statement does not permit DML against the table while the statement is executing. To leave the table available for DML while moving it, see "Redefining Tables Online".

The following statement moves the `hr.admin_emp` table to a new segment and tablespace, specifying new storage parameters:

```
ALTER TABLE hr.admin_emp MOVE
      STORAGE ( INITIAL 20K
                NEXT 40K
                MINEXTENTS 2
                MAXEXTENTS 20
                PCTINCREASE 0 )
  TABLESPACE hr_tbs;
```

Moving a table changes the rowids of the rows in the table. This causes indexes on the table to be marked `UNUSABLE`, and DML accessing the table using these indexes will receive an ORA-01502 error. The indexes on the table must be dropped or rebuilt. Likewise, any statistics for the table become invalid and new statistics should be collected after moving the table.

If the table includes `LOB` column(s), this statement can be used to move the table along with `LOB` data and `LOB` index segments (associated with this table) which the user explicitly specifies. If not specified, the default is to not move the `LOB` data and `LOB` index segments.

See Also:

"Consider Encrypting Columns That Contain Sensitive Data" for more information on transparent data encryption

### Manually Allocating Storage for a Table

Oracle Database dynamically allocates additional extents for the data segment of a table, as required. However, perhaps you want to allocate an additional extent for a table explicitly. For example, in an Oracle Real Application Clusters environment, an extent of a table can be allocated explicitly for a specific instance.

A new extent can be allocated for a table using the `ALTER TABLE...ALLOCATE EXTENT` clause.

You can also explicitly deallocate unused space using the `DEALLOCATE UNUSED` clause of `ALTER TABLE`. This is described in ["Reclaiming Wasted Space"](schema.md).

### Modifying an Existing Column Definition

Use the `ALTER TABLE...MODIFY` statement to modify an existing column definition. You can modify column data type, default value, column constraint, column expression (for virtual columns) and column encryption.

You can increase the length of an existing column, or decrease it, if all existing data satisfies the new length. You can change a column from byte semantics to `CHAR` semantics or vice versa. You must set the initialization parameter `BLANK_TRIMMING=TRUE` to decrease the length of a non-empty `CHAR` column.

If you are modifying a table to increase the length of a column of data type `CHAR`, realize that this can be a time consuming operation and can require substantial additional storage, especially if the table contains many rows. This is because the `CHAR` value in each row must be blank-padded to satisfy the new column length.

See Also:

[Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_3001.htm#SQLRF01001) for additional information about modifying table columns and additional restrictions

### Adding Table Columns

To add a column to an existing table, use the `ALTER TABLE...ADD` statement.

The following statement alters the `hr.admin_emp` table to add a new column named `bonus`:

```
ALTER TABLE hr.admin_emp
      ADD (bonus NUMBER (7,2));
```

If a new column is added to a table, the column is initially `NULL` unless you specify the `DEFAULT` clause. When you specify a default value, the database immediately updates each row with the default value. Note that this can take some time, and that during the update, there is an exclusive DML lock on the table. For some types of tables (for example, tables without LOB columns), if you specify both a `NOT` `NULL` constraint and a default value, the database can optimize the column add operation and greatly reduce the amount of time that the table is locked for DML.

You can add a column with a `NOT` `NULL` constraint only if the table does not contain any rows, or you specify a default value.

See Also:

[Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_3001.htm#SQLRF01001) for additional rules and restrictions for adding table columns

#### Adding a Column to a Compressed Table

If you enable basic compression on a table, you can add columns only if you do not specify default values.

If you enable OLTP compression on a table, you can add columns to that table with or without default values. If a default value is specified, the column must be `NOT` `NULL`.

See Also:

"Consider Using Table Compression"

#### Adding a Virtual Column

If the new column is a virtual column, its value is determined by its column expression. (Note that a virtual column's value is calculated only when it is queried.)

See Also:

- [Oracle Database Concepts](https://docs.oracle.com/cd/E11882_01/server.112/e40540/tablecls.htm#CNCPT89199)
- "Example: Creating a Table" for an example of a virtual column

### Renaming Table Columns

Oracle Database lets you rename existing columns in a table. Use the `RENAME COLUMN` clause of the `ALTER TABLE` statement to rename a column. The new name must not conflict with the name of any existing column in the table. No other clauses are allowed with the `RENAME COLUMN` clause.

The following statement renames the `comm` column of the `hr.admin_emp` table.

```
ALTER TABLE hr.admin_emp
      RENAME COLUMN comm TO commission;
```

As noted earlier, altering a table column can invalidate dependent objects. However, when you rename a column, the database updates associated data dictionary tables to ensure that function-based indexes and check constraints remain valid.

Oracle Database also lets you rename column constraints. This is discussed in ["Renaming Constraints"](general.md).

Note:

The `RENAME TO` clause of `ALTER TABLE` appears similar in syntax to the `RENAME COLUMN` clause, but is used for renaming the table itself.

### Dropping Table Columns

You can drop columns that are no longer needed from a table, including an index-organized table. This provides a convenient means to free space in a database, and avoids your having to export/import data then re-create indexes and constraints.

You cannot drop all columns from a table, nor can you drop columns from a table owned by `SYS`. Any attempt to do so results in an error.

See Also:

[Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_3001.htm#SQLRF01001) for information about additional restrictions and options for dropping columns from a table

#### Removing Columns from Tables

When you issue an `ALTER TABLE...DROP COLUMN` statement, the column descriptor and the data associated with the target column are removed from each row in the table. You can drop multiple columns with one statement.

The following statements are examples of dropping columns from the `hr.admin_emp` table. The first statement drops only the `sal` column:

```
ALTER TABLE hr.admin_emp DROP COLUMN sal;
```

The next statement drops both the `bonus` and `comm` columns:

```
ALTER TABLE hr.admin_emp DROP (bonus, commission);
```

#### Marking Columns Unused

If you are concerned about the length of time it could take to drop column data from all of the rows in a large table, you can use the `ALTER TABLE...SET UNUSED` statement. This statement marks one or more columns as unused, but does not actually remove the target column data or restore the disk space occupied by these columns. However, a column that is marked as unused is not displayed in queries or data dictionary views, and its name is removed so that a new column can reuse that name. In most cases, constraints, indexes, and statistics defined on the column are also removed. The exception is that any internal indexes for LOB columns that are marked unused are not removed.

To mark the `hiredate` and `mgr` columns as unused, execute the following statement:

```
ALTER TABLE hr.admin_emp SET UNUSED (hiredate, mgr);
```

You can later remove columns that are marked as unused by issuing an `ALTER TABLE...DROP UNUSED COLUMNS` statement. Unused columns are also removed from the target table whenever an explicit drop of any particular column or columns of the table is issued.

The data dictionary views `USER_UNUSED_COL_TABS`, `ALL_UNUSED_COL_TABS`, or `DBA_UNUSED_COL_TABS` can be used to list all tables containing unused columns. The `COUNT` field shows the number of unused columns in the table.

```
SELECT * FROM DBA_UNUSED_COL_TABS;

OWNER                       TABLE_NAME                  COUNT
--------------------------- --------------------------- -----
HR                          ADMIN_EMP                       2
```

For external tables, the `SET` `UNUSED` statement is transparently converted into an `ALTER` `TABLE` `DROP` `COLUMN` statement. Because external tables consist of metadata only in the database, the `DROP` `COLUMN` statement performs equivalently to the `SET` `UNUSED` statement.

#### Removing Unused Columns

The `ALTER TABLE...DROP UNUSED COLUMNS` statement is the only action allowed on unused columns. It physically removes unused columns from the table and reclaims disk space.

In the `ALTER TABLE` statement that follows, the optional clause `CHECKPOINT` is specified. This clause causes a checkpoint to be applied after processing the specified number of rows, in this case 250. Checkpointing cuts down on the amount of undo logs accumulated during the drop column operation to avoid a potential exhaustion of undo space.

```
ALTER TABLE hr.admin_emp DROP UNUSED COLUMNS CHECKPOINT 250;
```

#### Dropping Columns in Compressed Tables

If you enable OLTP compression on a table, you can drop table columns. If you enable basic compression only, you cannot drop columns.

See Also:

"Consider Using Table Compression"

### Placing a Table in Read-Only Mode

You can place a table in read-only mode with the `ALTER` `TABLE`...`READ` `ONLY` statement, and return it to read/write mode with the `ALTER` `TABLE`...`READ` `WRITE` statement. An example of a table for which read-only mode makes sense is a configuration table. If your application contains configuration tables that are not modified after installation and that must not be modified by users, your application installation scripts can place these tables in read-only mode.

To place a table in read-only mode, you must have the `ALTER` `TABLE` privilege on the table or the `ALTER` `ANY` `TABLE` privilege. In addition, the `COMPATIBLE` initialization parameter must be set to 11.1.0 or greater.

The following example places the `SALES` table in read-only mode:

```
ALTER TABLE SALES READ ONLY;
```

The following example returns the table to read/write mode:

```
ALTER TABLE SALES READ WRITE;
```

When a table is in read-only mode, operations that attempt to modify table data are disallowed. The following operations are not permitted on a read-only table:

- All DML operations on the table or any of its partitions
- `TRUNCATE` `TABLE`
- `SELECT` `FOR` `UPDATE`
- `ALTER` `TABLE` `ADD` / `MODIFY` / `RENAME` / `DROP` `COLUMN`
- `ALTER` `TABLE` `SET` `COLUMN` `UNUSED`
- `ALTER` `TABLE` `DROP` / `TRUNCATE` / `EXCHANGE` `(``SUB``)` `PARTITION`
- `ALTER` `TABLE` `UPGRADE` `INCLUDING` `DATA` or `ALTER` `TYPE` `CASCADE` `INCLUDING` `TABLE` `DATA` for a type with read-only table dependents
- Online redefinition
- `FLASHBACK` `TABLE`

The following operations are permitted on a read-only table:

- `SELECT`
- `CREATE` / `ALTER` / `DROP` `INDEX`
- `ALTER` `TABLE` `ADD` / `MODIFY` / `DROP` / `ENABLE` / `DISABLE` `CONSTRAINT`
- `ALTER` `TABLE` for physical property changes
- `ALTER` `TABLE` `DROP` `UNUSED` `COLUMNS`
- `ALTER` `TABLE` `ADD` / `COALESCE` / `MERGE` / `MODIFY` / `MOVE` / `RENAME` / `SPLIT` `(SUB)PARTITION`
- `ALTER` `TABLE` `MOVE`
- `ALTER` `TABLE` `ENABLE` `ROW` `MOVEMENT` and `ALTER` `TABLE` `SHRINK`
- `RENAME` `TABLE` and `ALTER` `TABLE` `RENAME` `TO`
- `DROP` `TABLE`
- `ALTER` `TABLE` `DEALLOCATE` `UNUSED`
- `ALTER` `TABLE` `ADD` / `DROP` `SUPPLEMENTAL` `LOG`

See Also:

[Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_3001.htm#SQLRF01001) for more information about the `ALTER` `TABLE` statement

## Redefining Tables Online

In any database system, it is occasionally necessary to modify the logical or physical structure of a table to:

- Improve the performance of queries or DML
- Accommodate application changes
- Manage storage

Oracle Database provides a mechanism to make table structure modifications without significantly affecting the availability of the table. The mechanism is called online table redefinition. Redefining tables online provides a substantial increase in availability compared to traditional methods of redefining tables.

When a table is redefined online, it is accessible to both queries and DML during much of the redefinition process. Typically, the table is locked in the exclusive mode only during a very small window that is independent of the size of the table and complexity of the redefinition, and that is completely transparent to users. However, if there are many concurrent DML operations during redefinition, then a longer wait might be necessary before the table can be locked. Due to the wait, more changes are committed to the original table, which increases the refresh time and the amount of time that the table is locked.

Online table redefinition requires an amount of free space that is approximately equivalent to the space used by the table being redefined. More space may be required if new columns are added.

You can perform online table redefinition with the Enterprise Manager Reorganize Objects wizard or with the `DBMS_REDEFINITION` package.

Note:

To invoke the Reorganize Objects wizard:
1. On the Tables page of Enterprise Manager, click in the Select column to select the table to redefine.
2. In the Actions list, select Reorganize.
3. Click Go.

This section describes online redefinition with the `DBMS_REDEFINITION` package. It contains the following topics:

- Features of Online Table Redefinition
- Performing Online Redefinition with DBMS\_REDEFINITION
- Results of the Redefinition Process
- Performing Intermediate Synchronization
- Aborting Online Table Redefinition and Cleaning Up After Errors
- Restrictions for Online Redefinition of Tables
- Online Redefinition of a Single Partition
- Online Table Redefinition Examples
- Privileges Required for the DBMS\_REDEFINITION Package

See Also:

[Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/d_redefi.htm#ARPLS042) for a description of the `DBMS_REDEFINITION` package

### Features of Online Table Redefinition

Online table redefinition enables you to:

- Modify the storage parameters of a table or cluster
- Move a table or cluster to a different tablespace
	Note:
	If it is not important to keep a table available for DML when moving it to another tablespace, you can use the simpler `ALTER` `TABLE` `MOVE` command. See "Moving a Table to a New Segment or Tablespace".
- Add, modify, or drop one or more columns in a table or cluster
- Add or drop partitioning support (non-clustered tables only)
- Change partition structure
- Change physical properties of a single table partition, including moving it to a different tablespace in the same schema
- Change physical properties of a materialized view log or an Oracle Streams Advanced Queuing queue table
- Add support for parallel queries
- Re-create a table or cluster to reduce fragmentation
	Note:
	In many cases, online segment shrink is an easier way to reduce fragmentation. See ["Reclaiming Wasted Space"](schema.md).
- Change the organization of a normal table (heap organized) to an index-organized table, or do the reverse.
- Convert a relational table into a table with object columns, or do the reverse.
- Convert an object table into a relational table or a table with object columns, or do the reverse.

### Performing Online Redefinition with DBMS\_REDEFINITION

You use the `DBMS_REDEFINITION` package to perform online redefinition of a table. See [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/d_redefi.htm#ARPLS042) for package details.

To redefine a table online:

1. Choose the redefinition method: by key or by rowid
	By key—Select a primary key or pseudo-primary key to use for the redefinition. Pseudo-primary keys are unique keys with all component columns having `NOT NULL` constraints. For this method, the versions of the tables before and after redefinition should have the same primary key columns. This is the preferred and default method of redefinition.
	By rowid—Use this method if no key is available. In this method, a hidden column named `M_ROW$$` is added to the post-redefined version of the table. It is recommended that this column be dropped or marked as unused after the redefinition is complete. If `COMPATIBLE` is set to 10.2.0 or higher, the final phase of redefinition automatically sets this column unused. You can then use the `ALTER` `TABLE`... `DROP` `UNUSED` `COLUMNS` statement to drop it.
	You cannot use this method on index-organized tables.
2. Verify that the table can be redefined online by invoking the `CAN_REDEF_TABLE` procedure. If the table is not a candidate for online redefinition, then this procedure raises an error indicating why the table cannot be redefined online.
3. Create an empty interim table (in the same schema as the table to be redefined) with all of the desired logical and physical attributes. If columns are to be dropped, do not include them in the definition of the interim table. If a column is to be added, then add the column definition to the interim table. If a column is to be modified, create it in the interim table with the properties that you want.
	It is not necessary to create the interim table with all the indexes, constraints, grants, and triggers of the table being redefined, because these will be defined in step [^1] when you copy dependent objects.
4. If redefining a partitioned table with the rowid method, enable row movement on the interim table.
	```
	ALTER TABLE ... ENABLE ROW MOVEMENT;
	```
5. (Optional) If you are redefining a large table and want to improve the performance of the next step by running it in parallel, issue the following statements:
	```
	ALTER SESSION FORCE PARALLEL DML PARALLEL degree-of-parallelism;
	ALTER SESSION FORCE PARALLEL QUERY PARALLEL degree-of-parallelism;
	```
6. Start the redefinition process by calling `START_REDEF_TABLE`, providing the following:
	- The schema and table name of the table to be redefined
		- The interim table name
		- A column mapping string that maps the columns of table to be redefined to the columns of the interim table
		See "Constructing a Column Mapping String" for details.
		- The redefinition method
		Package constants are provided for specifying the redefinition method. `DBMS_REDEFINITION.CONS_USE_PK` is used to indicate that the redefinition should be done using primary keys or pseudo-primary keys. `DBMS_REDEFINITION.CONS_USE_ROWID` is use to indicate that the redefinition should be done using rowids. If this argument is omitted, the default method of redefinition (`CONS_USE_PK`) is assumed.
		- Optionally, the columns to be used in ordering rows
		- If redefining only a single partition of a partitioned table, the partition name
	Because this process involves copying data, it may take a while. The table being redefined remains available for queries and DML during the entire process.
	Note:
	- You can query the `DBA_REDEFINITION_OBJECTS` view to list the objects currently involved in online redefinition.
	- If `START_REDEF_TABLE` fails for any reason, you must call `ABORT_REDEF_TABLE`, otherwise subsequent attempts to redefine the table will fail.
7. Copy dependent objects (such as triggers, indexes, materialized view logs, grants, and constraints) and statistics from the table being redefined to the interim table, using one of the following two methods. Method 1 is the preferred method because it is more automatic, but there may be times that you would choose to use method 2. Method 1 also enables you to copy table statistics to the interim table.
	- Method 1: Automatically Creating Dependent Objects
		Use the `COPY_TABLE_DEPENDENTS` procedure to automatically create dependent objects on the interim table. This procedure also registers the dependent objects. Registering the dependent objects enables the identities of these objects and their copied counterparts to be automatically swapped later as part of the redefinition completion process. The result is that when the redefinition is completed, the names of the dependent objects will be the same as the names of the original dependent objects.
		For more information, see "Creating Dependent Objects Automatically".
		- Method 2: Manually Creating Dependent Objects
		You can manually create dependent objects on the interim table and then register them. For more information, see "Creating Dependent Objects Manually".
		Note:
		In Oracle Database Release 9i, you were required to manually create the triggers, indexes, grants, and constraints on the interim table, and there may still be situations where you want to or must do so. In such cases, any referential constraints involving the interim table (that is, the interim table is either a parent or a child table of the referential constraint) must be created disabled. When online redefinition completes, the referential constraint is automatically enabled. In addition, until the redefinition process is either completed or aborted, any trigger defined on the interim table does not execute.
8. Execute the `FINISH_REDEF_TABLE` procedure to complete the redefinition of the table. During this procedure, the original table is locked in exclusive mode for a very short time, independent of the amount of data in the original table. However, `FINISH_REDEF_TABLE` will wait for all pending DML to commit before completing the redefinition.
9. If you used rowids for the redefinition and your `COMPATIBLE` initialization parameter is set to 10.1.0 or lower, drop or set `UNUSED` the hidden column `M_ROW$$` that is now in the redefined table.
	```
	ALTER TABLE table_name SET UNUSED (M_ROW$$);
	```
	If `COMPATIBLE` is 10.2.0 or higher, this hidden column is automatically set `UNUSED` when redefinition completes. You can then drop the column with the `ALTER` `TABLE`... `DROP` `UNUSED` `COLUMNS` statement.
10. Wait for any long-running queries against the interim table to complete, and then drop the interim table.
	If you drop the interim table while there are active queries running against it, you may encounter an `ORA-08103` error ("object no longer exists").

See Also:

"Online Table Redefinition Examples"

#### Constructing a Column Mapping String

The column mapping string that you pass as an argument to `START_REDEF_TABLE` contains a comma-delimited list of column mapping pairs, where each pair has the following syntax:

```
[expression]  column_name
```

The `column_name` term indicates a column in the interim table. The optional `expression` can include columns from the table being redefined, constants, operators, function or method calls, and so on, in accordance with the rules for expressions in a SQL `SELECT` statement. However, only simple deterministic subexpressions—that is, subexpressions whose results do not vary between one evaluation and the next—plus sequences and `SYSDATE` can be used. No subqueries are permitted. In the simplest case, the expression consists of just a column name from the table being redefined.

If an expression is present, its value is placed in the designated interim table column during redefinition. If the expression is omitted, it is assumed that both the table being redefined and the interim table have a column named `column_name`, and the value of that column in the table being redefined is placed in the same column in the interim table.

For example, if the `override` column in the table being redefined is to be renamed to `override_commission`, and every override commission is to be raised by 2%, the correct column mapping pair is:

```
override*1.02  override_commission
```

If you supply ' `*` ' or `NULL` as the column mapping string, it is assumed that all the columns (with their names unchanged) are to be included in the interim table. Otherwise, only those columns specified explicitly in the string are considered. The order of the column mapping pairs is unimportant.

For examples of column mapping strings, see "Online Table Redefinition Examples".

Data Conversions When mapping columns, you can convert data types, with some restrictions.

If you provide ' `*` ' or `NULL` as the column mapping string, only the implicit conversions permitted by SQL are supported. For example, you can convert from `CHAR` to `VARCHAR2`, from `INTEGER` to `NUMBER`, and so on.

To perform other data type conversions, including converting from one object type to another or one collection type to another, you must provide a column mapping pair with an expression that performs the conversion. The expression can include the `CAST` function, built-in functions like `TO_NUMBER`, conversion functions that you create, and so on.

#### Creating Dependent Objects Automatically

You use the `COPY_TABLE_DEPENDENTS` procedure to automatically create dependent objects on the interim table.

You can discover if errors occurred while copying dependent objects by checking the `num_errors` output argument. If the `ignore_errors` argument is set to `TRUE`, the `COPY_TABLE_DEPENDENTS` procedure continues copying dependent objects even if an error is encountered when creating an object. You can view these errors by querying the `DBA_REDEFINITION_ERRORS` view.

Reasons for errors include:

- A lack of system resources
- A change in the logical structure of the table that would require recoding the dependent object.
	See Example 3 in "Online Table Redefinition Examples" for a discussion of this type of error.

If `ignore_errors` is set to `FALSE`, the `COPY_TABLE_DEPENDENTS` procedure stops copying objects as soon as any error is encountered.

After you correct any errors you can again attempt to copy the dependent objects by reexecuting the `COPY_TABLE_DEPENDENTS` procedure. Optionally you can create the objects manually and then register them as explained in "Creating Dependent Objects Manually". The `COPY_TABLE_DEPENDENTS` procedure can be used multiple times as necessary. If an object has already been successfully copied, it is not copied again.

#### Creating Dependent Objects Manually

If you manually create dependent objects on the interim table with SQL\*Plus or Enterprise Manager, you must then use the `REGISTER_DEPENDENT_OBJECT` procedure to register the dependent objects. Registering dependent objects enables the redefinition completion process to restore dependent object names to what they were before redefinition.

You would also use the `REGISTER_DEPENDENT_OBJECT` procedure if the `COPY_TABLE_DEPENDENTS` procedure failed to copy a dependent object and manual intervention is required.

You can query the `DBA_REDEFINITION_OBJECTS` view to determine which dependent objects are registered. This view shows dependent objects that were registered explicitly with the `REGISTER_DEPENDENT_OBJECT` procedure or implicitly with the `COPY_TABLE_DEPENDENTS` procedure. Only current information is shown in the view.

The `UNREGISTER_DEPENDENT_OBJECT` procedure can be used to unregister a dependent object on the table being redefined and on the interim table.

Note:

Manually created dependent objects do not have to be identical to their corresponding original dependent objects. For example, when manually creating a materialized view log on the interim table, you can log different columns. In addition, the interim table can have more or fewer dependent objects.

### Results of the Redefinition Process

The following are the end results of the redefinition process:

- The original table is redefined with the columns, indexes, constraints, grants, triggers, and statistics of the interim table.
- Dependent objects that were registered, either explicitly using `REGISTER_DEPENDENT_OBJECT` or implicitly using `COPY_TABLE_DEPENDENTS`, are renamed automatically so that dependent object names on the redefined table are the same as before redefinition.
	Note:
	If no registration is done or no automatic copying is done, then you must manually rename the dependent objects.
- The referential constraints involving the interim table now involve the redefined table and are enabled.
- Any indexes, triggers, materialized view logs, grants, and constraints defined on the original table (prior to redefinition) are transferred to the interim table and are dropped when the user drops the interim table. Any referential constraints involving the original table before the redefinition now involve the interim table and are disabled.
- Some PL/SQL objects, views, synonyms, and other table-dependent objects may become invalidated. Only those objects that depend on elements of the table that were changed are invalidated. For example, if a PL/SQL procedure queries only columns of the redefined table that were unchanged by the redefinition, the procedure remains valid. See ["Managing Object Dependencies"](general.md) for more information about schema object dependencies.

### Performing Intermediate Synchronization

After the redefinition process has been started by calling `START_REDEF_TABLE` and before `FINISH_REDEF_TABLE` has been called, a large number of DML statements might have been executed on the original table. If you know that this is the case, it is recommended that you periodically synchronize the interim table with the original table. This is done by calling the `SYNC_INTERIM_TABLE` procedure. Calling this procedure reduces the time taken by `FINISH_REDEF_TABLE` to complete the redefinition process. There is no limit to the number of times that you can call `SYNC_INTERIM_TABLE`.

The small amount of time that the original table is locked during `FINISH_REDEF_TABLE` is independent of whether `SYNC_INTERIM_TABLE` has been called.

### Aborting Online Table Redefinition and Cleaning Up After Errors

In the event that an error is raised during the redefinition process, or if you choose to terminate the redefinition process, call `ABORT_REDEF_TABLE`. This procedure drops temporary logs and tables associated with the redefinition process. After this procedure is called, you can drop the interim table and its dependent objects.

If the online redefinition process must be restarted, if you do not first call `ABORT_REDEF_TABLE`, subsequent attempts to redefine the table will fail.

### Restrictions for Online Redefinition of Tables

The following restrictions apply to the online redefinition of tables:

- If the table is to be redefined using primary key or pseudo-primary keys (unique keys or constraints with all component columns having not null constraints), then the post-redefinition table must have the same primary key or pseudo-primary key columns. If the table is to be redefined using rowids, then the table must not be an index-organized table.
- After redefining a table that has a materialized view log, the subsequent refresh of any dependent materialized view must be a complete refresh.
- Tables that are replicated in an n-way master configuration can be redefined, but horizontal subsetting (subset of rows in the table), vertical subsetting (subset of columns in the table), and column transformations are not allowed.
- The overflow table of an index-organized table cannot be redefined online independently.
- Tables with fine-grained access control (row-level security) cannot be redefined online.
- Tables for which Flashback Data Archive is enabled cannot be redefined online. You cannot enable Flashback Data Archive for the interim table.
- Tables with `BFILE` columns cannot be redefined online.
- Tables with `LONG` columns can be redefined online, but those columns must be converted to `CLOBS`. Also, `LONG RAW` columns must be converted to `BLOBS`. Tables with `LOB` columns are acceptable.
- On a system with sufficient resources for parallel execution, and in the case where the interim table is not partitioned, redefinition of a `LONG` column to a `LOB` column can be executed in parallel, provided that:
	- The segment used to store the `LOB` column in the interim table belongs to a locally managed tablespace with Automatic Segment Space Management (ASSM) enabled.
		- There is a simple mapping from one `LONG` column to one `LOB` column, and the interim table has only one `LOB` column.
	In the case where the interim table is partitioned, the normal methods for parallel execution for partitioning apply.
- Tables in the `SYS` and `SYSTEM` schema cannot be redefined online.
- Temporary tables cannot be redefined.
- A subset of rows in the table cannot be redefined.
- Only simple deterministic expressions, sequences, and `SYSDATE` can be used when mapping the columns in the interim table to those of the original table. For example, subqueries are not allowed.
- If new columns are being added as part of the redefinition and there are no column mappings for these columns, then they must not be declared `NOT` `NULL` until the redefinition is complete.
- There cannot be any referential constraints between the table being redefined and the interim table.
- Table redefinition cannot be done `NOLOGGING`.
- For materialized view logs and queue tables, online redefinition is restricted to changes in physical properties. No horizontal or vertical subsetting is permitted, nor are any column transformations. The only valid value for the column mapping string is `NULL`.
- You cannot perform online redefinition on a table that is partitioned if the table includes one or more nested tables.
- You can convert a `VARRAY` to a nested table with the `CAST` operator in the column mapping. However, you cannot convert a nested table to a `VARRAY`.
- When the columns in the `col_mapping` parameter of the `DBMS_REDEFINITION.START_REDEF_TABLE` procedure include a sequence, the `orderby_cols` parameter must be `NULL`.
- Online redefinition cannot run on multiple tables concurrently in separate `DBMS_REDEFINITION` sessions if the tables are related by reference partitioning.
	See [Oracle Database VLDB and Partitioning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25523/part_admin001.htm#VLDBG1093) for more information about reference partitioning.
- Online redefinition of an object table or `XMLType` table can cause a dangling `REF` in other tables if those other tables have a `REF` column that references the redefined table.
	See [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/sql_elements001.htm#SQLRF51006) for more information about dangling `REF` s.

### Online Redefinition of a Single Partition

Beginning with Oracle Database 10g Release 2, you can redefine online a single partition of a table. This is useful if, for example, you want to move a partition to a different tablespace and keep the partition available for DML during the operation.

Another use for this capability is redefining an entire table, but doing it one partition at a time to reduce resource requirements. For example, to move a very large table to a different tablespace, you can move it one partition at a time to minimize the free space and undo space required to complete the move.

Redefining a single partition differs from redefining a table in the following ways:

- There is no need to copy dependent objects. It is not valid to use the `COPY_TABLE_DEPENDENTS` procedure when redefining a single partition.
- You must manually create any local indexes on the interim table.
- The column mapping string for `START_REDEF_TABLE` must be `NULL`.
- When using the by-rowid method, the final phase of redefinition drops the hidden column `M_ROW$$` instead of setting it unused.

Note:

If it is not important to keep a partition available for DML when moving it to another tablespace, you can use the simpler `ALTER` `TABLE`...`MOVE` `PARTITION` statement.

See also:

- The section "Moving Partitions" in [Oracle Database VLDB and Partitioning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25523/part_admin002.htm#VLDBG1193)
- [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_3001.htm#SQLRF01001) for details on the `ALTER` `TABLE`...`MOVE` `PARTITION` statement

#### Rules for Online Redefinition of a Single Partition

The underlying mechanism for redefinition of a single partition is the exchange partition capability of the database (`ALTER` `TABLE`...`EXCHANGE` `PARTITION`). Rules and restrictions for online redefinition of a single partition are therefore governed by this mechanism. Here are some general restrictions:

- No logical changes (such as adding or dropping a column) are permitted.
- No changes to the partitioning method (such as changing from range partitioning to hash partitioning) are permitted.

Here are the rules for defining the interim table:

- If the partition being redefined is a range, hash, or list partition, the interim table must be nonpartitioned.
- If the partition being redefined is a range partition of a composite range-hash partitioned table, the interim table must be a hash partitioned table. In addition, the partitioning key of the interim table must be identical to the subpartitioning key of the range-hash partitioned table, and the number of partitions in the interim table must be identical to the number of subpartitions in the range partition being redefined.
- If the partition being redefined is a hash partition that uses the rowid redefinition method, then row movement must be enabled on the interim table before redefinition starts.
- If the partition being redefined is a range partition of a composite range-list partitioned table, the interim table must be a list partitioned table. In addition, the partitioning key of the interim table must be identical to the subpartitioning key of the range-list partitioned table, and the values lists of the interim table's list partitions must exactly match the values lists of the list subpartitions in the range partition being redefined.
- If you define the interim table as compressed, then you must use the by-key method of redefinition, not the by-rowid method.

These additional rules apply if the table being redefined is a partitioned index-organized table:

- The interim table must also be index-organized.
- The original and interim tables must have primary keys on the same columns, in the same order.
- If key compression is enabled, it must be enabled for both the original and interim tables, with the same prefix length.
- Both the original and interim tables must have overflow segments, or neither can have them. Likewise for mapping tables.
- Both the original and interim tables must have identical storage attributes for any LOB columns.

See Also:

The section "Exchanging Partitions" in [Oracle Database VLDB and Partitioning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25523/part_admin002.htm#VLDBG1156)

### Online Table Redefinition Examples

For the following examples, see [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/d_redefi.htm#ARPLS042) for descriptions of all `DBMS_REDEFINITION` subprograms.

| Example | Description |
| --- | --- |
| Example 1 | Redefines a table by adding new columns and adding partitioning. |
| Example 2 | Demonstrates redefinition with object data types. |
| Example 3 | Demonstrates redefinition with manually registered dependent objects. |
| Example 4 | Redefines a single table partition, moving it to a different tablespace. |

Example 1

This example illustrates online redefinition of the previously created table `hr.admin_emp`, which at this point only contains columns: `empno`, `ename`, `job`, `deptno`. The table is redefined as follows:

- New columns `mgr`, `hiredate`, `sal`, and `bonus` are added. (These existed in the original table but were dropped in previous examples.)
- The new column `bonus` is initialized to 0
- The column `deptno` has its value increased by 10.
- The redefined table is partitioned by range on `empno`.

The steps in this redefinition are illustrated below.

1. Verify that the table is a candidate for online redefinition. In this case you specify that the redefinition is to be done using primary keys or pseudo-primary keys.
	```
	BEGIN
	  DBMS_REDEFINITION.CAN_REDEF_TABLE('hr','admin_emp',
	      DBMS_REDEFINITION.CONS_USE_PK);
	END;
	/
	```
2. Create an interim table `hr.int_admin_emp`.
	```
	CREATE TABLE hr.int_admin_emp
	        (empno      NUMBER(5) PRIMARY KEY,
	         ename      VARCHAR2(15) NOT NULL,
	         job        VARCHAR2(10),
	         mgr        NUMBER(5),
	         hiredate   DATE DEFAULT (sysdate),
	         sal        NUMBER(7,2),
	         deptno     NUMBER(3) NOT NULL,
	         bonus      NUMBER (7,2) DEFAULT(1000))
	     PARTITION BY RANGE(empno)
	       (PARTITION emp1000 VALUES LESS THAN (1000) TABLESPACE admin_tbs,
	        PARTITION emp2000 VALUES LESS THAN (2000) TABLESPACE admin_tbs2);
	```
3. Start the redefinition process.
	```
	BEGIN
	  DBMS_REDEFINITION.START_REDEF_TABLE('hr', 'admin_emp','int_admin_emp',
	       'empno empno, ename ename, job job, deptno+10 deptno, 0 bonus',
	        dbms_redefinition.cons_use_pk);
	END;
	/
	```
4. Copy dependent objects. (Automatically create any triggers, indexes, materialized view logs, grants, and constraints on `hr.int_admin_emp`.)
	```
	DECLARE
	num_errors PLS_INTEGER;
	BEGIN
	  DBMS_REDEFINITION.COPY_TABLE_DEPENDENTS('hr', 'admin_emp','int_admin_emp',
	   DBMS_REDEFINITION.CONS_ORIG_PARAMS, TRUE, TRUE, TRUE, TRUE, num_errors);
	END;
	/
	```
	Note that the `ignore_errors` argument is set to `TRUE` for this call. The reason is that the interim table was created with a primary key constraint, and when `COPY_TABLE_DEPENDENTS` attempts to copy the primary key constraint and index from the original table, errors occurs. You can ignore these errors, but you must run the query shown in the next step to see if there are other errors.
5. Query the `DBA_REDEFINITION_ERRORS` view to check for errors.
	```
	SQL> select object_name, base_table_name, ddl_txt from
	         DBA_REDEFINITION_ERRORS;
	 
	OBJECT_NAME   BASE_TABLE_NAME  DDL_TXT
	------------- ---------------- ------------------------------
	SYS_C005836   ADMIN_EMP        CREATE UNIQUE INDEX "HR"."TMP$
	                               $_SYS_C0058360" ON "HR"."INT_A
	                               DMIN_EMP" ("EMPNO")
	 
	SYS_C005836   ADMIN_EMP        ALTER TABLE "HR"."INT_ADMIN_EM
	                               P" ADD CONSTRAINT "TMP$$_SYS_C
	                               0058360" PRIMARY KEY
	```
	These errors are caused by the existing primary key constraint on the interim table and can be ignored. Note that with this approach, the names of the primary key constraint and index on the post-redefined table are changed. An alternate approach, one that avoids errors and name changes, would be to define the interim table without a primary key constraint. In this case, the primary key constraint and index are copied from the original table.
	Note:
	The best approach is to define the interim table with a primary key constraint, use `REGISTER_DEPENDENT_OBJECT` to register the primary key constraint and index, and then copy the remaining dependent objects with `COPY_TABLE_DEPENDENTS`. This approach avoids errors and ensures that the redefined table always has a primary key and that the dependent object names do not change.
6. Optionally, synchronize the interim table `hr.int_admin_emp`.
	```
	BEGIN 
	  DBMS_REDEFINITION.SYNC_INTERIM_TABLE('hr', 'admin_emp', 'int_admin_emp');
	END;
	/
	```
7. Complete the redefinition.
	```
	BEGIN
	  DBMS_REDEFINITION.FINISH_REDEF_TABLE('hr', 'admin_emp', 'int_admin_emp');
	END;
	/
	```
	The table `hr.admin_emp` is locked in the exclusive mode only for a small window toward the end of this step. After this call the table `hr.admin_emp` is redefined such that it has all the attributes of the `hr.int_admin_emp` table.
8. Wait for any long-running queries against the interim table to complete, and then drop the interim table.

Example 2

This example redefines a table to change columns into object attributes. The redefined table gets a new column that is an object type.

The original table, named `CUSTOMER`, is defined as follows:

```
Name         Type          
------------ ------------- 
CID          NUMBER            <- Primary key
NAME         VARCHAR2(30)  
STREET       VARCHAR2(100) 
CITY         VARCHAR2(30)  
STATE        VARCHAR2(2)   
ZIP          NUMBER(5)
```

The type definition for the new object is:

```
CREATE TYPE ADDR_T AS OBJECT (  
   street VARCHAR2(100),        
   city VARCHAR2(30),           
   state VARCHAR2(2),           
   zip NUMBER(5, 0) );
```

Here are the steps for this redefinition:

1. Verify that the table is a candidate for online redefinition. Specify that the redefinition is to be done using primary keys or pseudo-primary keys.
	```
	BEGIN
	  DBMS_REDEFINITION.CAN_REDEF_TABLE('STEVE','CUSTOMER',
	        DBMS_REDEFINITION.CONS_USE_PK);
	END;
	/
	```
2. Create the interim table `int_customer`.
	```
	CREATE TABLE INT_CUSTOMER(
	  CID NUMBER,
	  NAME  VARCHAR2(30),          
	  ADDR  ADDR_T);
	```
	Note that no primary key is defined on the interim table. When dependent objects are copied in step [^2], the primary key constraint and index are copied.
3. Because `CUSTOMER` is a very large table, specify parallel operations for the next step.
	```
	alter session force parallel dml parallel 4;
	alter session force parallel query parallel 4;
	```
4. Start the redefinition process using primary keys.
	```
	BEGIN
	  DBMS_REDEFINITION.START_REDEF_TABLE(
	   uname       => 'STEVE',
	   orig_table  => 'CUSTOMER',
	   int_table   => 'INT_CUSTOMER',
	   col_mapping => 'cid cid,  name name,
	      addr_t(street, city, state, zip) addr');
	END;
	/
	```
	Note that `addr_t(street, city, state, zip)` is a call to the object constructor.
5. Copy dependent objects.
	```
	DECLARE
	num_errors PLS_INTEGER;
	BEGIN
	  DBMS_REDEFINITION.COPY_TABLE_DEPENDENTS(
	   'STEVE','CUSTOMER','INT_CUSTOMER',DBMS_REDEFINITION.CONS_ORIG_PARAMS,
	    TRUE, TRUE, TRUE, FALSE, num_errors, TRUE);
	END;
	/
	```
	Note that for this call, the final argument indicates that table statistics are to be copied to the interim table.
6. Optionally synchronize the interim table.
	```
	BEGIN 
	  DBMS_REDEFINITION.SYNC_INTERIM_TABLE('STEVE', 'CUSTOMER', 'INT_CUSTOMER');
	END;
	/
	```
7. Complete the redefinition.
	```
	BEGIN
	  DBMS_REDEFINITION.FINISH_REDEF_TABLE('STEVE', 'CUSTOMER', 'INT_CUSTOMER');
	END;
	/
	```
8. Wait for any long-running queries against the interim table to complete, and then drop the interim table.

Example 3

This example addresses the situation where a dependent object must be manually created and registered.

Consider the case where a table `T1` has a column named `C1`, and where this column becomes `C2` after the redefinition. Assume that there is an index `Index1` on `C1`. In this case, `COPY_TABLE_DEPENDENTS` tries to create an index on the interim table corresponding to `Index1`, and tries to create it on a column `C1`, which does not exist on the interim table. This results in an error. You must therefore manually create the index on column `C2` and register it. Here are the steps:

1. Create the interim table `INT_T1` and create an index `Int_Index1` on column `C2`.
2. Ensure that `T1` is a candidate for online redefinition with `CAN_REDEF_TABLE`, and then begin the redefinition process with `START_REDEF_TABLE`.
3. Register the original (`Index1`) and interim (`Int_Index1`) dependent objects.
	```
	BEGIN
	 DBMS_REDEFINITION.REGISTER_DEPENDENT_OBJECT(
	   uname         => 'STEVE',
	   orig_table    => 'T1',
	   int_table     => 'INT_T1',
	   dep_type      => DBMS_REDEFINITION.CONS_INDEX,
	   dep_owner     => 'STEVE',
	   dep_orig_name => 'Index1',
	   dep_int_name  => 'Int_Index1');
	END;
	/
	```
4. Use `COPY_TABLE_DEPENDENTS` to copy the remaining dependent objects.
5. Optionally synchronize the interim table.
6. Complete the redefinition and drop the interim table.

Example 4

This example demonstrates redefining a single partition. It moves the oldest partition of a range-partitioned sales table to a tablespace named `TBS_LOW_FREQ`. The table containing the partition to be redefined is defined as follows:

```
CREATE TABLE salestable
(s_productid NUMBER,
s_saledate DATE,
s_custid NUMBER,
s_totalprice NUMBER)
TABLESPACE users
PARTITION BY RANGE(s_saledate)
(PARTITION sal03q1 VALUES LESS THAN (TO_DATE('01-APR-2003', 'DD-MON-YYYY')),
PARTITION sal03q2 VALUES LESS THAN (TO_DATE('01-JUL-2003', 'DD-MON-YYYY')),
PARTITION sal03q3 VALUES LESS THAN (TO_DATE('01-OCT-2003', 'DD-MON-YYYY')),
PARTITION sal03q4 VALUES LESS THAN (TO_DATE('01-JAN-2004', 'DD-MON-YYYY')));
```

The table has a local partitioned index that is defined as follows:

```
CREATE INDEX sales_index ON salestable 
   (s_saledate, s_productid, s_custid) LOCAL;
```

Here are the steps. In the following procedure calls, note the extra argument: partition name (`part_name`).

1. Ensure that `salestable` is a candidate for redefinition.
	```
	BEGIN
	  DBMS_REDEFINITION.CAN_REDEF_TABLE(
	   uname        => 'STEVE',
	   tname        => 'SALESTABLE',
	   options_flag => DBMS_REDEFINITION.CONS_USE_ROWID,
	   part_name    => 'sal03q1');
	END;
	/
	```
2. Create the interim table in the `TBS_LOW_FREQ` tablespace. Because this is a redefinition of a range partition, the interim table is nonpartitioned.
	```
	CREATE TABLE int_salestable
	(s_productid NUMBER,
	s_saledate DATE,
	s_custid NUMBER,
	s_totalprice NUMBER)
	TABLESPACE tbs_low_freq;
	```
3. Start the redefinition process using rowid.
	```
	BEGIN
	  DBMS_REDEFINITION.START_REDEF_TABLE(
	   uname        => 'STEVE',
	   orig_table   => 'salestable',
	   int_table    => 'int_salestable',
	   col_mapping  => NULL,
	   options_flag => DBMS_REDEFINITION.CONS_USE_ROWID,
	   part_name    => 'sal03q1');
	END;
	/
	```
4. Manually create any local indexes on the interim table.
	```
	CREATE INDEX int_sales_index ON int_salestable 
	(s_saledate, s_productid, s_custid)
	TABLESPACE tbs_low_freq;
	```
5. Optionally synchronize the interim table.
	```
	BEGIN 
	  DBMS_REDEFINITION.SYNC_INTERIM_TABLE(
	   uname      => 'STEVE', 
	   orig_table => 'salestable', 
	   int_table  => 'int_salestable',
	   part_name  => 'sal03q1');
	END;
	/
	```
6. Complete the redefinition.
	```
	BEGIN 
	  DBMS_REDEFINITION.FINISH_REDEF_TABLE(
	   uname      => 'STEVE', 
	   orig_table => 'salestable', 
	   int_table  => 'int_salestable',
	   part_name  => 'sal03q1');
	END;
	/
	```
7. Wait for any long-running queries against the interim table to complete, and then drop the interim table.

The following query shows that the oldest partition has been moved to the new tablespace:

```
select partition_name, tablespace_name from user_tab_partitions
 where table_name = 'SALESTABLE';
 
PARTITION_NAME                 TABLESPACE_NAME
------------------------------ ------------------------------
SAL03Q1                        TBS_LOW_FREQ
SAL03Q2                        USERS
SAL03Q3                        USERS
SAL03Q4                        USERS
 
4 rows selected.
```

### Privileges Required for the DBMS\_REDEFINITION Package

Execute privileges on the `DBMS_REDEFINITION` package are required to run subprograms in the package. Execute privileges on the `DBMS_REDEFINITION` package are granted to `EXECUTE_CATALOG_ROLE`.

In addition, for a user to redefine a table in the user's schema using the package, the user must be granted the following privileges:

- `CREATE` `TABLE`
- `CREATE` `MATERIALIZED` `VIEW`

The `CREATE TRIGGER` privilege is also required to execute the `COPY_TABLE_DEPENDENTS` procedure.

For a user to redefine a table in other schemas using the package, the user must be granted the following privileges:

- `CREATE` `ANY` `TABLE`
- `ALTER` `ANY` `TABLE`
- `DROP` `ANY` `TABLE`
- `LOCK` `ANY TABLE`
- `SELECT` `ANY` `TABLE`

The following additional privileges are required to execute `COPY_TABLE_DEPENDENTS` on tables in other schemas:

- `CREATE` `ANY` `TRIGGER`
- `CREATE` `ANY` `INDEX`

## Researching and Reversing Erroneous Table Changes

To enable you to research and reverse erroneous changes to tables, Oracle Database provides a a group of features that you can use to view past states of database objects or to return database objects to a previous state without using point-in-time media recovery. These features are known as Oracle Flashback features, and are described in [Oracle Database Advanced Application Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e41502/adfns_flashback.htm#ADFNS1008).

To research an erroneous change, you can use multiple Oracle Flashback queries to view row data at specific points in time. A more efficient approach would be to use Oracle Flashback Version Query to view all changes to a row over a period of time. With this feature, you append a `VERSIONS` clause to a `SELECT` statement that specifies a system change number (SCN) or timestamp range between which you want to view changes to row values. The query also can return associated metadata, such as the transaction responsible for the change.

After you identify an erroneous transaction, you can use Oracle Flashback Transaction Query to identify other changes that were made by the transaction. You can then use Oracle Flashback Transaction to reverse the erroneous transaction. (Note that Oracle Flashback Transaction must also reverse all dependent transactions—subsequent transactions involving the same rows as the erroneous transaction.) You also have the option of using Oracle Flashback Table, described in "Recovering Tables Using Oracle Flashback Table".

Note:

You must be using automatic undo management to use Oracle Flashback features. See ["Introduction to Automatic Undo Management"](undo.md).

See Also:

[Oracle Database Advanced Application Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e41502/adfns_flashback.htm#ADFNS1008) for information about Oracle Flashback features.

## Recovering Tables Using Oracle Flashback Table

Oracle Flashback Table enables you to restore a table to its state as of a previous point in time. It provides a fast, online solution for recovering a table that has been accidentally modified or deleted by a user or application. In many cases, Oracle Flashback Table eliminates the need for you to perform more complicated point-in-time recovery operations.

Oracle Flashback Table:

- Restores all data in a specified table to a previous point in time described by a timestamp or SCN.
- Performs the restore operation online.
- Automatically maintains all of the table attributes, such as indexes, triggers, and constraints that are necessary for an application to function with the flashed-back table.
- Maintains any remote state in a distributed environment. For example, all of the table modifications required by replication if a replicated table is flashed back.
- Maintains data integrity as specified by constraints. Tables are flashed back provided none of the table constraints are violated. This includes any referential integrity constraints specified between a table included in the `FLASHBACK TABLE` statement and another table that is not included in the `FLASHBACK TABLE` statement.
- Even after a flashback operation, the data in the original table is not lost. You can later revert to the original state.

Note:

You must be using automatic undo management to use Oracle Flashback Table. See ["Introduction to Automatic Undo Management"](undo.md).

See Also:

[Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/cd/E11882_01/backup.112/e10642/rcmflash.htm#BRADV81517) for more information about the `FLASHBACK TABLE` statement.

## Dropping Tables

To drop a table that you no longer need, use the `DROP TABLE` statement. The table must be contained in your schema or you must have the `DROP ANY TABLE` system privilege.

Caution:

Before dropping a table, familiarize yourself with the consequences of doing so:
- Dropping a table removes the table definition from the data dictionary. All rows of the table are no longer accessible.
- All indexes and triggers associated with a table are dropped.
- All views and PL/SQL program units dependent on a dropped table remain, yet become invalid (not usable). See ["Managing Object Dependencies"](general.md) for information about how the database manages dependencies.
- All synonyms for a dropped table remain, but return an error when used.
- All extents allocated for a table that is dropped are returned to the free space of the tablespace and can be used by any other object requiring new extents or new objects. All rows corresponding to a clustered table are deleted from the blocks of the cluster. Clustered tables are the subject of [Chapter 22, "Managing Clusters"](clustrs.md).

The following statement drops the `hr.int_admin_emp` table:

```
DROP TABLE hr.int_admin_emp;
```

If the table to be dropped contains any primary or unique keys referenced by foreign keys of other tables and you intend to drop the `FOREIGN KEY` constraints of the child tables, then include the `CASCADE` clause in the `DROP TABLE` statement, as shown below:

```
DROP TABLE hr.admin_emp CASCADE CONSTRAINTS;
```

When you drop a table, normally the database does not immediately release the space associated with the table. Rather, the database renames the table and places it in a recycle bin, where it can later be recovered with the `FLASHBACK` `TABLE` statement if you find that you dropped the table in error. If you should want to immediately release the space associated with the table at the time you issue the `DROP TABLE` statement, include the `PURGE` clause as shown in the following statement:

```
DROP TABLE hr.admin_emp PURGE;
```

Perhaps instead of dropping a table, you want to truncate it. The `TRUNCATE` statement provides a fast, efficient method for deleting all rows from a table, but it does not affect any structures associated with the table being truncated (column definitions, constraints, triggers, and so forth) or authorizations. The `TRUNCATE` statement is discussed in ["Truncating Tables and Clusters"](general.md).

## Using Flashback Drop and Managing the Recycle Bin

When you drop a table, the database does not immediately remove the space associated with the table. The database renames the table and places it and any associated objects in a recycle bin, where, in case the table was dropped in error, it can be recovered at a later time. This feature is called Flashback Drop, and the `FLASHBACK` `TABLE` statement is used to restore the table. Before discussing the use of the `FLASHBACK` `TABLE` statement for this purpose, it is important to understand how the recycle bin works, and how you manage its contents.

This section contains the following topics:

- What Is the Recycle Bin?
- Viewing and Querying Objects in the Recycle Bin
- Purging Objects in the Recycle Bin
- Restoring Tables from the Recycle Bin

### What Is the Recycle Bin?

The recycle bin is actually a data dictionary table containing information about dropped objects. Dropped tables and any associated objects such as indexes, constraints, nested tables, and the likes are not removed and still occupy space. They continue to count against user space quotas, until specifically purged from the recycle bin or the unlikely situation where they must be purged by the database because of tablespace space constraints.

Each user can be thought of as having his own recycle bin, because, unless a user has the `SYSDBA` privilege, the only objects that the user has access to in the recycle bin are those that the user owns. A user can view his objects in the recycle bin using the following statement:

```
SELECT * FROM RECYCLEBIN;
```

When you drop a tablespace including its contents, the objects in the tablespace are not placed in the recycle bin and the database purges any entries in the recycle bin for objects located in the tablespace. The database also purges any recycle bin entries for objects in a tablespace when you drop the tablespace, not including contents, and the tablespace is otherwise empty. Likewise:

- When you drop a user, any objects belonging to the user are not placed in the recycle bin and any objects in the recycle bin are purged.
- When you drop a cluster, its member tables are not placed in the recycle bin and any former member tables in the recycle bin are purged.
- When you drop a type, any dependent objects such as subtypes are not placed in the recycle bin and any former dependent objects in the recycle bin are purged.

Object Naming in the Recycle Bin

When a dropped table is moved to the recycle bin, the table and its associated objects are given system-generated names. This is necessary to avoid name conflicts that may arise if multiple tables have the same name. This could occur under the following circumstances:

- A user drops a table, re-creates it with the same name, then drops it again.
- Two users have tables with the same name, and both users drop their tables.

The renaming convention is as follows:

```
BIN$unique_id
$version
```

where:

- `unique_id` is a 26-character globally unique identifier for this object, which makes the recycle bin name unique across all databases
- `version` is a version number assigned by the database

### Enabling and Disabling the Recycle Bin

When the recycle bin is enabled, dropped tables and their dependent objects are placed in the recycle bin. When the recycle bin is disabled, dropped tables and their dependent objects are not placed in the recycle bin; they are just dropped, and you must use other means to recover them (such as recovering from backup).

Disabling the recycle bin does not purge or otherwise affect objects already in the recycle bin. The recycle bin is enabled by default.

You enable and disable the recycle bin by changing the `recyclebin` initialization parameter. This parameter is not dynamic, so a database restart is required when you change it with an `ALTER` `SYSTEM` statement.

To disable the recycle bin:

1. Issue one of the following statements:
	```
	ALTER SESSION SET recyclebin = OFF;
	ALTER SYSTEM SET recyclebin = OFF SCOPE = SPFILE;
	```
2. If you used `ALTER` `SYSTEM`, restart the database.

To enable the recycle bin:

1. Issue one of the following statements:
	```
	ALTER SESSION SET recyclebin = ON;
	ALTER SYSTEM SET recyclebin = ON SCOPE = SPFILE;
	```
2. If you used `ALTER` `SYSTEM`, restart the database.

See Also:

- ["About Initialization Parameters and Initialization Parameter Files"](create.md) for more information on initialization parameters
- ["Changing Initialization Parameter Values"](create.md) for a description of dynamic and static initialization parameters

### Viewing and Querying Objects in the Recycle Bin

Oracle Database provides two views for obtaining information about objects in the recycle bin:

| View | Description |
| --- | --- |
| `USER_RECYCLEBIN` | This view can be used by users to see their own dropped objects in the recycle bin. It has a synonym `RECYCLEBIN`, for ease of use. |
| `DBA_RECYCLEBIN` | This view gives administrators visibility to all dropped objects in the recycle bin |

One use for these views is to identify the name that the database has assigned to a dropped object, as shown in the following example:

```
SELECT object_name, original_name FROM dba_recyclebin
   WHERE owner = 'HR';

OBJECT_NAME                    ORIGINAL_NAME
------------------------------ --------------------------------
BIN$yrMKlZaLMhfgNAgAIMenRA==$0 EMPLOYEES
```

You can also view the contents of the recycle bin using the SQL\*Plus command `SHOW RECYCLEBIN`.

```
SQL> show recyclebin

ORIGINAL NAME    RECYCLEBIN NAME                OBJECT TYPE  DROP TIME
---------------- ------------------------------ ------------ -------------------
EMPLOYEES        BIN$yrMKlZaVMhfgNAgAIMenRA==$0 TABLE        2003-10-27:14:00:19
```

You can query objects that are in the recycle bin, just as you can query other objects. However, you must specify the name of the object as it is identified in the recycle bin. For example:

```
SELECT * FROM "BIN$yrMKlZaVMhfgNAgAIMenRA==$0";
```

### Purging Objects in the Recycle Bin

If you decide that you are never going to restore an item from the recycle bin, you can use the `PURGE` statement to remove the items and their associated objects from the recycle bin and release their storage space. You need the same privileges as if you were dropping the item.

When you use the `PURGE` statement to purge a table, you can use the name that the table is known by in the recycle bin or the original name of the table. The recycle bin name can be obtained from either the `DBA_` or `USER_RECYCLEBIN` view as shown in "Viewing and Querying Objects in the Recycle Bin". The following hypothetical example purges the table `hr.int_admin_emp`, which was renamed to `BIN$jsleilx392mk2=293$0` when it was placed in the recycle bin:

```
PURGE TABLE "BIN$jsleilx392mk2=293$0";
```

You can achieve the same result with the following statement:

```
PURGE TABLE int_admin_emp;
```

You can use the `PURGE` statement to purge all the objects in the recycle bin that are from a specified tablespace or only the tablespace objects belonging to a specified user, as shown in the following examples:

```
PURGE TABLESPACE example;
PURGE TABLESPACE example USER oe;
```

Users can purge the recycle bin of their own objects, and release space for objects, by using the following statement:

```
PURGE RECYCLEBIN;
```

If you have the `SYSDBA` privilege, then you can purge the entire recycle bin by specifying `DBA_RECYCLEBIN`, instead of `RECYCLEBIN` in the previous statement.

You can also use the `PURGE` statement to purge an index from the recycle bin or to purge from the recycle bin all objects in a specified tablespace.

See Also:

[Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_9018.htm#SQLRF01803) for more information on the `PURGE` statement

### Restoring Tables from the Recycle Bin

Use the `FLASHBACK` `TABLE`... `TO` `BEFORE` `DROP` statement to recover objects from the recycle bin. You can specify either the name of the table in the recycle bin or the original table name. An optional `RENAME TO` clause lets you rename the table as you recover it. The recycle bin name can be obtained from either the `DBA_` or `USER_RECYCLEBIN` view as shown in "Viewing and Querying Objects in the Recycle Bin". To use the `FLASHBACK` `TABLE`... `TO` `BEFORE` `DROP` statement, you need the same privileges required to drop the table.

The following example restores `int_admin_emp` table and assigns to it a new name:

```
FLASHBACK TABLE int_admin_emp TO BEFORE DROP 
   RENAME TO int2_admin_emp;
```

The system-generated recycle bin name is very useful if you have dropped a table multiple times. For example, suppose you have three versions of the `int2_admin_emp` table in the recycle bin and you want to recover the second version. You can do this by issuing two `FLASHBACK TABLE` statements, or you can query the recycle bin and then flashback to the appropriate system-generated name, as shown in the following example. Including the create time in the query can help you verify that you are restoring the correct table.

```
SELECT object_name, original_name, createtime FROM recyclebin;    

OBJECT_NAME                    ORIGINAL_NAME   CREATETIME
------------------------------ --------------- -------------------
BIN$yrMKlZaLMhfgNAgAIMenRA==$0 INT2_ADMIN_EMP  2006-02-05:21:05:52
BIN$yrMKlZaVMhfgNAgAIMenRA==$0 INT2_ADMIN_EMP  2006-02-05:21:25:13
BIN$yrMKlZaQMhfgNAgAIMenRA==$0 INT2_ADMIN_EMP  2006-02-05:22:05:53

FLASHBACK TABLE "BIN$yrMKlZaVMhfgNAgAIMenRA==$0" TO BEFORE DROP;
```

Restoring Dependent Objects

When you restore a table from the recycle bin, dependent objects such as indexes do not get their original names back; they retain their system-generated recycle bin names. You must manually rename dependent objects to restore their original names. If you plan to manually restore original names for dependent objects, ensure that you make note of each dependent object's system-generated recycle bin name before you restore the table.

The following is an example of restoring the original names of some of the indexes of the dropped table `JOB_HISTORY`, from the `HR` sample schema. The example assumes that you are logged in as the `HR` user.

1. After dropping `JOB_HISTORY` and before restoring it from the recycle bin, run the following query:
	```
	SELECT OBJECT_NAME, ORIGINAL_NAME, TYPE FROM RECYCLEBIN;
	OBJECT_NAME                    ORIGINAL_NAME             TYPE
	------------------------------ ------------------------- --------
	BIN$DBo9UChtZSbgQFeMiAdCcQ==$0 JHIST_JOB_IX              INDEX
	BIN$DBo9UChuZSbgQFeMiAdCcQ==$0 JHIST_EMPLOYEE_IX         INDEX
	BIN$DBo9UChvZSbgQFeMiAdCcQ==$0 JHIST_DEPARTMENT_IX       INDEX
	BIN$DBo9UChwZSbgQFeMiAdCcQ==$0 JHIST_EMP_ID_ST_DATE_PK   INDEX
	BIN$DBo9UChxZSbgQFeMiAdCcQ==$0 JOB_HISTORY               TABLE
	```
2. Restore the table with the following command:
	```
	FLASHBACK TABLE JOB_HISTORY TO BEFORE DROP;
	```
3. Run the following query to verify that all `JOB_HISTORY` indexes retained their system-generated recycle bin names:
	```
	SELECT INDEX_NAME FROM USER_INDEXES WHERE TABLE_NAME = 'JOB_HISTORY';
	 
	INDEX_NAME
	------------------------------
	BIN$DBo9UChwZSbgQFeMiAdCcQ==$0
	BIN$DBo9UChtZSbgQFeMiAdCcQ==$0
	BIN$DBo9UChuZSbgQFeMiAdCcQ==$0
	BIN$DBo9UChvZSbgQFeMiAdCcQ==$0
	```
4. Restore the original names of the first two indexes as follows:
	```
	ALTER INDEX "BIN$DBo9UChtZSbgQFeMiAdCcQ==$0" RENAME TO JHIST_JOB_IX;
	ALTER INDEX "BIN$DBo9UChuZSbgQFeMiAdCcQ==$0" RENAME TO JHIST_EMPLOYEE_IX;
	```
	Note that double quotes are required around the system-generated names.

## Managing Index-Organized Tables

This section describes aspects of managing index-organized tables, and contains the following topics:

- What Are Index-Organized Tables?
- Creating Index-Organized Tables
- Maintaining Index-Organized Tables
- Creating Secondary Indexes on Index-Organized Tables
- Analyzing Index-Organized Tables
- Using the ORDER BY Clause with Index-Organized Tables
- Converting Index-Organized Tables to Regular Tables

### What Are Index-Organized Tables?

An index-organized table has a storage organization that is a variant of a primary B-tree. Unlike an ordinary (heap-organized) table whose data is stored as an unordered collection (heap), data for an index-organized table is stored in a B-tree index structure in a primary key sorted manner. Each leaf block in the index structure stores both the key and nonkey columns.

The structure of an index-organized table provides the following benefits:

- Fast random access on the primary key because an index-only scan is sufficient. And, because there is no separate table storage area, changes to the table data (such as adding new rows, updating rows, or deleting rows) result only in updating the index structure.
- Fast range access on the primary key because the rows are clustered in primary key order.
- Lower storage requirements because duplication of primary keys is avoided. They are not stored both in the index and underlying table, as is true with heap-organized tables.

Index-organized tables have full table functionality. They support features such as constraints, triggers, LOB and object columns, partitioning, parallel operations, online reorganization, and replication. And, they offer these additional features:

- Key compression
- Overflow storage area and specific column placement
- Secondary indexes, including bitmap indexes.

Index-organized tables are ideal for OLTP applications, which require fast primary key access and high availability. For example, queries and DML on an orders table used in electronic order processing are predominantly based on primary key access, and heavy volume of concurrent DML can cause row chaining and inefficient space usage in indexes, resulting in a frequent need to reorganize. Because an index-organized table can be reorganized online and without invalidating its secondary indexes, the window of unavailability is greatly reduced or eliminated.

Index-organized tables are suitable for modeling application-specific index structures. For example, content-based information retrieval applications containing text, image and audio data require inverted indexes that can be effectively modeled using index-organized tables. A fundamental component of an internet search engine is an inverted index that can be modeled using index-organized tables.

These are but a few of the applications for index-organized tables.

See Also:

- [Oracle Database Concepts](https://docs.oracle.com/cd/E11882_01/server.112/e40540/indexiot.htm#CNCPT911) for a more thorough description of index-organized tables
- [Oracle Database VLDB and Partitioning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25523/part_admin001.htm#VLDBG1112) for information about partitioning index-organized tables

### Creating Index-Organized Tables

You use the `CREATE TABLE` statement to create index-organized tables, but you must provide additional information:

- An `ORGANIZATION INDEX` qualifier, which indicates that this is an index-organized table
- A primary key, specified through a column constraint clause (for a single column primary key) or a table constraint clause (for a multiple-column primary key).

Optionally, you can specify the following:

- An `OVERFLOW` clause, which preserves dense clustering of the B-tree index by enabling the storage of some of the nonkey columns in a separate overflow data segment.
- A `PCTTHRESHOLD` value, which, when an overflow segment is being used, defines the maximum size of the portion of the row that is stored in the index block, as a percentage of block size. Rows columns that would cause the row size to exceed this maximum are stored in the overflow segment. The row is broken at a column boundary into two pieces, a head piece and tail piece. The head piece fits in the specified threshold and is stored along with the key in the index leaf block. The tail piece is stored in the overflow area as one or more row pieces. Thus, the index entry contains the key value, the nonkey column values that fit the specified threshold, and a pointer to the rest of the row.
- An `INCLUDING` clause, which can be used to specify the nonkey columns that are to be stored in the index block with the primary key.

#### Example: Creating an Index-Organized Table

The following statement creates an index-organized table:

```
CREATE TABLE admin_docindex(
        token char(20), 
        doc_id NUMBER,
        token_frequency NUMBER,
        token_offsets VARCHAR2(2000),
        CONSTRAINT pk_admin_docindex PRIMARY KEY (token, doc_id))
    ORGANIZATION INDEX 
    TABLESPACE admin_tbs
    PCTTHRESHOLD 20
    OVERFLOW TABLESPACE admin_tbs2;
```

This example creates an index-organized table named `admin_docindex`, with a primary key composed of the columns `token` and `doc_id`. The `OVERFLOW` and `PCTTHRESHOLD` clauses specify that if the length of a row exceeds 20% of the index block size, then the column that exceeded that threshold and all columns after it are moved to the overflow segment. The overflow segment is stored in the `admin_tbs2` tablespace.

See Also:

[Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_7002.htm#SQLRF01402) for more information about the syntax to create an index-organized table

#### Restrictions for Index-Organized Tables

The following are restrictions on creating index-organized tables.

- The maximum number of columns is 1000.
- The maximum number of columns in the index portion of a row is 255, including both key and nonkey columns. If more than 255 columns are required, you must use an overflow segment.
- The maximum number of columns that you can include in the primary key is 32.
- `PCTTHRESHOLD` must be in the range of 1–50. The default is 50.
- All key columns must fit within the specified threshold.
- If the maximum size of a row exceeds 50% of the index block size and you do not specify an overflow segment, the `CREATE` `TABLE` statement fails.
- Index-organized tables cannot have virtual columns.

#### Creating Index-Organized Tables that Contain Object Types

Index-organized tables can store object types. The following example creates object type `admin_typ`, then creates an index-organized table containing a column of object type `admin_typ`:

```
CREATE OR REPLACE TYPE admin_typ AS OBJECT
    (col1 NUMBER, col2 VARCHAR2(6));
CREATE TABLE admin_iot (c1 NUMBER primary key, c2 admin_typ)
    ORGANIZATION INDEX;
```

You can also create an index-organized table of object types. For example:

```
CREATE TABLE admin_iot2 OF admin_typ (col1 PRIMARY KEY)
    ORGANIZATION INDEX;
```

Another example, that follows, shows that index-organized tables store nested tables efficiently. For a nested table column, the database internally creates a storage table to hold all the nested table rows.

```
CREATE TYPE project_t AS OBJECT(pno NUMBER, pname VARCHAR2(80));
/
CREATE TYPE project_set AS TABLE OF project_t;
/
CREATE TABLE proj_tab (eno NUMBER, projects PROJECT_SET)
    NESTED TABLE projects STORE AS emp_project_tab
                ((PRIMARY KEY(nested_table_id, pno)) 
    ORGANIZATION INDEX)
    RETURN AS LOCATOR;
```

The rows belonging to a single nested table instance are identified by a `nested_table_id` column. If an ordinary table is used to store nested table columns, the nested table rows typically get de-clustered. But when you use an index-organized table, the nested table rows can be clustered based on the `nested_table_id` column.

See Also:

- [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_7002.htm#SQLRF01402) for details of the syntax used for creating index-organized tables
- [Oracle Database VLDB and Partitioning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25523/part_admin001.htm#VLDBG1112) for information about creating partitioned index-organized tables
- [Oracle Database Object-Relational Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e11822/toc.htm) for information about object types

#### Choosing and Monitoring a Threshold Value

Choose a threshold value that can accommodate your key columns, as well as the first few nonkey columns (if they are frequently accessed).

After choosing a threshold value, you can monitor tables to verify that the value you specified is appropriate. You can use the `ANALYZE` `TABLE`... `LIST` `CHAINED` `ROWS` statement to determine the number and identity of rows exceeding the threshold value.

See Also:

- ["Listing Chained Rows of Tables and Clusters"](general.md) for more information about chained rows
- [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_4005.htm#SQLRF01105) for syntax of the `ANALYZE` statement

#### Using the INCLUDING Clause

In addition to specifying `PCTTHRESHOLD`, you can use the `INCLUDING` clause to control which nonkey columns are stored with the key columns. The database accommodates all nonkey columns up to and including the column specified in the `INCLUDING` clause in the index leaf block, provided it does not exceed the specified threshold. All nonkey columns beyond the column specified in the `INCLUDING` clause are stored in the overflow segment. If the `INCLUDING` and `PCTTHRESHOLD` clauses conflict, `PCTTHRESHOLD` takes precedence.

Note:

Oracle Database moves all primary key columns of an indexed-organized table to the beginning of the table (in their key order) to provide efficient primary key–based access. As an example:
```
CREATE TABLE admin_iot4(a INT, b INT, c INT, d INT, 
                primary key(c,b))
    ORGANIZATION INDEX;
```

The stored column order is: `c b a d` (instead of: `a b c d`). The last primary key column is `b`, based on the stored column order. The `INCLUDING` column can be the last primary key column (`b` in this example), or any nonkey column (that is, any column after `b` in the stored column order).

The following `CREATE TABLE` statement is similar to the one shown earlier in "Example: Creating an Index-Organized Table" but is modified to create an index-organized table where the `token_offsets` column value is always stored in the overflow area:

```
CREATE TABLE admin_docindex2(
        token CHAR(20), 
        doc_id NUMBER,
        token_frequency NUMBER,
        token_offsets VARCHAR2(2000),
        CONSTRAINT pk_admin_docindex2 PRIMARY KEY (token, doc_id))
    ORGANIZATION INDEX 
    TABLESPACE admin_tbs
    PCTTHRESHOLD 20
    INCLUDING token_frequency
    OVERFLOW TABLESPACE admin_tbs2;
```

Here, only nonkey columns prior to `token_offsets` (in this case a single column only) are stored with the key column values in the index leaf block.

#### Parallelizing Index-Organized Table Creation

The `CREATE TABLE...AS SELECT` statement enables you to create an index-organized table and load data from an existing table into it. By including the `PARALLEL` clause, the load can be done in parallel.

The following statement creates an index-organized table in parallel by selecting rows from the conventional table `hr.jobs`:

```
CREATE TABLE admin_iot3(i PRIMARY KEY, j, k, l) 
     ORGANIZATION INDEX 
     PARALLEL
     AS SELECT * FROM hr.jobs;
```

This statement provides an alternative to parallel bulk-load using SQL\*Loader.

#### Using Key Compression

Creating an index-organized table using key compression enables you to eliminate repeated occurrences of key column prefix values.

Key compression breaks an index key into a prefix and a suffix entry. Compression is achieved by sharing the prefix entries among all the suffix entries in an index block. This sharing can lead to huge savings in space, allowing you to store more keys in each index block while improving performance.

You can enable key compression using the `COMPRESS` clause while:

- Creating an index-organized table
- Moving an index-organized table

You can also specify the prefix length (as the number of key columns), which identifies how the key columns are broken into a prefix and suffix entry.

```
CREATE TABLE admin_iot5(i INT, j INT, k INT, l INT, PRIMARY KEY (i, j, k)) 
    ORGANIZATION INDEX COMPRESS;
```

The preceding statement is equivalent to the following statement:

```
CREATE TABLE admin_iot6(i INT, j INT, k INT, l INT, PRIMARY KEY(i, j, k)) 
    ORGANIZATION INDEX COMPRESS 2;
```

For the list of values (1,2,3), (1,2,4), (1,2,7), (1,3,5), (1,3,4), (1,4,4) the repeated occurrences of (1,2), (1,3) are compressed away.

You can also override the default prefix length used for compression as follows:

```
CREATE TABLE admin_iot7(i INT, j INT, k INT, l INT, PRIMARY KEY (i, j, k)) 
    ORGANIZATION INDEX COMPRESS 1;
```

For the list of values (1,2,3), (1,2,4), (1,2,7), (1,3,5), (1,3,4), (1,4,4), the repeated occurrences of 1 are compressed away.

You can disable compression as follows:

```
ALTER TABLE admin_iot5 MOVE NOCOMPRESS;
```

One application of key compression is in a time-series application that uses a set of time-stamped rows belonging to a single item, such as a stock price. Index-organized tables are attractive for such applications because of the ability to cluster rows based on the primary key. By defining an index-organized table with primary key (stock symbol, time stamp), you can store and manipulate time-series data efficiently. You can achieve more storage savings by compressing repeated occurrences of the item identifier (for example, the stock symbol) in a time series by using an index-organized table with key compression.

See Also:

[Oracle Database Concepts](https://docs.oracle.com/cd/E11882_01/server.112/e40540/indexiot.htm#CNCPT1177) for more information about key compression

### Maintaining Index-Organized Tables

Index-organized tables differ from ordinary tables only in physical organization. Logically, they are manipulated in the same manner as ordinary tables. You can specify an index-organized table just as you would specify a regular table in `INSERT`, `SELECT`, `DELETE`, and `UPDATE` statements.

#### Altering Index-Organized Tables

All of the alter options available for ordinary tables are available for index-organized tables. This includes `ADD`, `MODIFY`, and `DROP` `COLUMNS` and `CONSTRAINTS`. However, the primary key constraint for an index-organized table cannot be dropped, deferred, or disabled

You can use the `ALTER TABLE` statement to modify physical and storage attributes for both primary key index and overflow data segments. All the attributes specified prior to the `OVERFLOW` keyword are applicable to the primary key index segment. All attributes specified after the `OVERFLOW` key word are applicable to the overflow data segment. For example, you can set the `INITRANS` of the primary key index segment to 4 and the overflow of the data segment `INITRANS` to 6 as follows:

```
ALTER TABLE admin_docindex INITRANS 4 OVERFLOW INITRANS 6;
```

You can also alter `PCTTHRESHOLD` and `INCLUDING` column values. A new setting is used to break the row into head and overflow tail pieces during subsequent operations. For example, the `PCTHRESHOLD` and `INCLUDING` column values can be altered for the `admin_docindex` table as follows:

```
ALTER TABLE admin_docindex PCTTHRESHOLD 15 INCLUDING doc_id;
```

By setting the `INCLUDING` column to `doc_id`, all the columns that follow `token_frequency` and `token_offsets`, are stored in the overflow data segment.

For index-organized tables created without an overflow data segment, you can add an overflow data segment by using the `ADD OVERFLOW` clause. For example, you can add an overflow segment to table `admin_iot3` as follows:

```
ALTER TABLE admin_iot3 ADD OVERFLOW TABLESPACE admin_tbs2;
```

#### Moving (Rebuilding) Index-Organized Tables

Because index-organized tables are primarily stored in a B-tree index, you can encounter fragmentation as a consequence of incremental updates. However, you can use the `ALTER TABLE...MOVE` statement to rebuild the index and reduce this fragmentation.

The following statement rebuilds the index-organized table `admin_docindex`:

```
ALTER TABLE admin_docindex MOVE;
```

You can rebuild index-organized tables online using the `ONLINE` keyword. The overflow data segment, if present, is rebuilt when the `OVERFLOW` keyword is specified. For example, to rebuild the `admin_docindex` table but not the overflow data segment, perform a move online as follows:

```
ALTER TABLE admin_docindex MOVE ONLINE;
```

To rebuild the `admin_docindex` table along with its overflow data segment perform the move operation as shown in the following statement. This statement also illustrates moving both the table and overflow data segment to new tablespaces.

```
ALTER TABLE admin_docindex MOVE TABLESPACE admin_tbs2 
    OVERFLOW TABLESPACE admin_tbs3;
```

In this last statement, an index-organized table with a LOB column (CLOB) is created. Later, the table is moved with the `LOB` index and data segment being rebuilt and moved to a new tablespace.

```
CREATE TABLE admin_iot_lob
   (c1 number (6) primary key,
    admin_lob CLOB)
   ORGANIZATION INDEX
   LOB (admin_lob) STORE AS (TABLESPACE admin_tbs2);
.
.
.
ALTER TABLE admin_iot_lob MOVE LOB (admin_lob) STORE AS (TABLESPACE admin_tbs3);
```

See Also:

[Oracle Database SecureFiles and Large Objects Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e18294/adlob_tables.htm#ADLOB45315) for information about LOBs in index-organized tables

### Creating Secondary Indexes on Index-Organized Tables

You can create secondary indexes on an index-organized tables to provide multiple access paths. Secondary indexes on index-organized tables differ from indexes on ordinary tables in two ways:

- They store logical rowids instead of physical rowids. This is necessary because the inherent movability of rows in a B-tree index results in the rows having no permanent physical addresses. If the physical location of a row changes, its logical rowid remains valid. One effect of this is that a table maintenance operation, such as `ALTER TABLE`... `MOVE`, does not make the secondary index unusable.
- The logical rowid also includes a physical guess which identifies the database block address at which the row is likely to be found. If the physical guess is correct, a secondary index scan would incur a single additional I/O once the secondary key is found. The performance would be similar to that of a secondary index-scan on an ordinary table.

Unique and non-unique secondary indexes, function-based secondary indexes, and bitmap indexes are supported as secondary indexes on index-organized tables.

#### Syntax for Creating the Secondary Index

The following statement shows the creation of a secondary index on the `docindex` index-organized table where `doc_id` and `token` are the key columns:

```
CREATE INDEX Doc_id_index on Docindex(Doc_id, Token);
```

This secondary index allows the database to efficiently process a query, such as the following, the involves a predicate on `doc_id`:

```
SELECT Token FROM Docindex WHERE Doc_id = 1;
```

#### Maintaining Physical Guesses in Logical Rowids

A logical rowid can include a guess, which identifies the block location of a row at the time the guess is made. Instead of doing a full key search, the database uses the guess to search the block directly. However, as new rows are inserted, guesses can become stale. The indexes are still usable through the primary key-component of the logical rowid, but access to rows is slower.

Collect index statistics with the `DBMS_STATS` package to monitor the staleness of guesses. The database checks whether the existing guesses are still valid and records the percentage of rows with valid guesses in the data dictionary. This statistic is stored in the `PCT_DIRECT_ACCESS` column of the `DBA_INDEXES` view (and related views).

To obtain fresh guesses, you can rebuild the secondary index. Note that rebuilding a secondary index on an index-organized table involves reading the base table, unlike rebuilding an index on an ordinary table. A quicker, more light weight means of fixing the guesses is to use the `ALTER` `INDEX`... `UPDATE` `BLOCK` `REFERENCES` statement. This statement is performed online, while DML is still allowed on the underlying index-organized table.

After you rebuild a secondary index, or otherwise update the block references in the guesses, collect index statistics again.

#### Bitmap Indexes

Bitmap indexes on index-organized tables are supported, provided the index-organized table is created with a mapping table. This is done by specifying the `MAPPING` `TABLE` clause in the `CREATE` `TABLE` statement that you use to create the index-organized table, or in an `ALTER` `TABLE` statement to add the mapping table later.

See Also:

[Oracle Database Concepts](https://docs.oracle.com/cd/E11882_01/server.112/e40540/indexiot.htm#CNCPT88857) for a description of mapping tables

### Analyzing Index-Organized Tables

Just like ordinary tables, index-organized tables are analyzed using the `DBMS_STATS` package, or the `ANALYZE` statement.

#### Collecting Optimizer Statistics for Index-Organized Tables

To collect optimizer statistics, use the `DBMS_STATS` package.

For example, the following statement gathers statistics for the index-organized `countries` table in the `hr` schema:

```
EXECUTE DBMS_STATS.GATHER_TABLE_STATS ('HR','COUNTRIES');
```

The `DBMS_STATS` package analyzes both the primary key index segment and the overflow data segment, and computes logical as well as physical statistics for the table.

- The logical statistics can be queried using `USER_TABLES`, `ALL_TABLES` or `DBA_TABLES`.
- You can query the physical statistics of the primary key index segment using `USER_INDEXES`, `ALL_INDEXES` or `DBA_INDEXES` (and using the primary key index name). For example, you can obtain the primary key index segment physical statistics for the table `admin_docindex` as follows:
	```
	SELECT LAST_ANALYZED, BLEVEL,LEAF_BLOCKS, DISTINCT_KEYS 
	   FROM DBA_INDEXES WHERE INDEX_NAME= 'PK_ADMIN_DOCINDEX';
	```
- You can query the physical statistics for the overflow data segment using the `USER_TABLES`, `ALL_TABLES` or `DBA_TABLES`. You can identify the overflow entry by searching for `IOT_TYPE = 'IOT_OVERFLOW'`. For example, you can obtain overflow data segment physical attributes associated with the `admin_docindex` table as follows:
	```
	SELECT LAST_ANALYZED, NUM_ROWS, BLOCKS, EMPTY_BLOCKS 
	   FROM DBA_TABLES WHERE IOT_TYPE='IOT_OVERFLOW' 
	          and IOT_NAME= 'ADMIN_DOCINDEX';
	```
	See Also:
	- [Oracle Database Performance Tuning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41573/stats.htm#PFGRF003) for more information about collecting optimizer statistics
	- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/d_stats.htm#ARPLS059) for more information about of the `DBMS_STATS` package

#### Validating the Structure of Index-Organized Tables

Use the `ANALYZE` statement to validate the structure of your index-organized table or to list any chained rows. These operations are discussed in the following sections located elsewhere in this book:

- ["Validating Tables, Indexes, Clusters, and Materialized Views"](general.md)
- ["Listing Chained Rows of Tables and Clusters"](general.md)
	Note:
	There are special considerations when listing chained rows for index-organized tables. These are discussed in the [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_4005.htm#SQLRF01105).

### Using the ORDER BY Clause with Index-Organized Tables

If an `ORDER BY` clause only references the primary key column or a prefix of it, then the optimizer avoids the sorting overhead, as the rows are returned sorted on the primary key columns.

The following queries avoid sorting overhead because the data is already sorted on the primary key:

```
SELECT * FROM admin_docindex2 ORDER BY token, doc_id;
SELECT * FROM admin_docindex2 ORDER BY token;
```

If, however, you have an `ORDER BY` clause on a suffix of the primary key column or non-primary-key columns, additional sorting is required (assuming no other secondary indexes are defined).

```
SELECT * FROM admin_docindex2 ORDER BY doc_id;
SELECT * FROM admin_docindex2 ORDER BY token_frequency;
```

### Converting Index-Organized Tables to Regular Tables

You can convert index-organized tables to regular (heap organized) tables using the Oracle import or export utilities, or the `CREATE TABLE...AS SELECT` statement.

To convert an index-organized table to a regular table:

- Export the index-organized table data using conventional path.
- Create a regular table definition with the same definition.
- Import the index-organized table data, making sure `IGNORE=y` (ensures that object exists error is ignored).
	Note:
	Before converting an index-organized table to a regular table, be aware that index-organized tables cannot be exported using pre-Oracle8 versions of the Export utility.
	See Also:
	[Oracle Database Utilities](https://docs.oracle.com/cd/E11882_01/server.112/e22490/toc.htm) for more details about using the original `IMP` and `EXP` utilities and the Data Pump import and export utilities

## Managing External Tables

This section contains:

- About External Tables
- Creating External Tables
- Altering External Tables
- Preprocessing External Tables
- Dropping External Tables
- System and Object Privileges for External Tables

### About External Tables

Oracle Database allows you read-only access to data in external tables. External tables are defined as tables that do not reside in the database, and can be in any format for which an access driver is provided. By providing the database with metadata describing an external table, the database is able to expose the data in the external table as if it were data residing in a regular database table. The external data can be queried directly and in parallel using SQL.

You can, for example, select, join, or sort external table data. You can also create views and synonyms for external tables. However, no DML operations (`UPDATE`, `INSERT`, or `DELETE`) are possible, and no indexes can be created, on external tables.

External tables provide a framework to unload the result of an arbitrary `SELECT` statement into a platform-independent Oracle-proprietary format that can be used by Oracle Data Pump. External tables provide a valuable means for performing basic extraction, transformation, and loading (ETL) tasks that are common for data warehousing.

The means of defining the metadata for external tables is through the `CREATE TABLE...ORGANIZATION EXTERNAL` statement. This external table definition can be thought of as a view that allows running any SQL query against external data without requiring that the external data first be loaded into the database. An access driver is the actual mechanism used to read the external data in the table. When you use external tables to unload data, the metadata is automatically created based on the data types in the `SELECT` statement.

Oracle Database provides two access drivers for external tables. The default access driver is `ORACLE_LOADER`, which allows the reading of data from external files using the Oracle loader technology. The `ORACLE_LOADER` access driver provides data mapping capabilities which are a subset of the control file syntax of SQL\*Loader utility. The second access driver, `ORACLE_DATAPUMP`, lets you unload data—that is, read data from the database and insert it into an external table, represented by one or more external files—and then reload it into an Oracle Database.

Note:

The `ANALYZE` statement is not supported for gathering statistics for external tables. Use the `DBMS_STATS` package instead.

See Also:

- [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_7002.htm#SQLRF54503) for restrictions that apply to external tables
- [Oracle Database Utilities](https://docs.oracle.com/cd/E11882_01/server.112/e22490/et_concepts.htm#SUTIL011) for information about access drivers
- [Oracle Database Data Warehousing Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25554/transform.htm#DWHSG8312) for information about using external tables for ETL in a data warehousing environment
- [Oracle Database Performance Tuning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41573/stats.htm#PFGRF003) for information about using the `DBMS_STATS` package

External Table Restrictions

The following are restrictions on external tables:

- The `ANALYZE` statement is not supported for gathering statistics for external tables. Use the `DBMS_STATS` package instead.
- Virtual columns are not supported

See Also:

- [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_7002.htm#SQLRF54503) for restrictions that apply to external tables
- [Oracle Database Utilities](https://docs.oracle.com/cd/E11882_01/server.112/e22490/et_concepts.htm#SUTIL011) for information about access drivers
- [Oracle Database Data Warehousing Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25554/transform.htm#DWHSG8312) for information about using external tables for ETL in a data warehousing environment
- [Oracle Database Performance Tuning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41573/stats.htm#PFGRF003) for information about using the `DBMS_STATS` package

### Creating External Tables

You create external tables using the `CREATE` `TABLE` statement with an `ORGANIZATION` `EXTERNAL` clause. This statement creates only metadata in the data dictionary.

Note:

External tables cannot have virtual columns.

The following example creates an external table and then uploads the data to a database table. Alternatively, you can unload data through the external table framework by specifying the `AS` `subquery` clause of the `CREATE TABLE` statement. External table data pump unload can use only the `ORACLE_DATAPUMP` access driver.

EXAMPLE: Creating an External Table and Loading Data

In this example, the data for the external table resides in the two text files `empxt1.dat` and `empxt2.dat`.

The file `empxt1.dat` contains the following sample data:

```
360,Jane,Janus,ST_CLERK,121,17-MAY-2001,3000,0,50,jjanus
361,Mark,Jasper,SA_REP,145,17-MAY-2001,8000,.1,80,mjasper
362,Brenda,Starr,AD_ASST,200,17-MAY-2001,5500,0,10,bstarr
363,Alex,Alda,AC_MGR,145,17-MAY-2001,9000,.15,80,aalda
```

The file `empxt2.dat` contains the following sample data:

```
401,Jesse,Cromwell,HR_REP,203,17-MAY-2001,7000,0,40,jcromwel
402,Abby,Applegate,IT_PROG,103,17-MAY-2001,9000,.2,60,aapplega
403,Carol,Cousins,AD_VP,100,17-MAY-2001,27000,.3,90,ccousins
404,John,Richardson,AC_ACCOUNT,205,17-MAY-2001,5000,0,110,jrichard
```

The following SQL statements create an external table named `admin_ext_employees` in the `hr` schema and load data from the external table into the `hr.employees` table.

```
CONNECT  /  AS SYSDBA;
-- Set up directories and grant access to hr 
CREATE OR REPLACE DIRECTORY admin_dat_dir
    AS '/flatfiles/data'; 
CREATE OR REPLACE DIRECTORY admin_log_dir 
    AS '/flatfiles/log'; 
CREATE OR REPLACE DIRECTORY admin_bad_dir 
    AS '/flatfiles/bad'; 
GRANT READ ON DIRECTORY admin_dat_dir TO hr; 
GRANT WRITE ON DIRECTORY admin_log_dir TO hr; 
GRANT WRITE ON DIRECTORY admin_bad_dir TO hr;
-- hr connects. Provide the user password (hr) when prompted.
CONNECT hr
-- create the external table
CREATE TABLE admin_ext_employees
                   (employee_id       NUMBER(4), 
                    first_name        VARCHAR2(20),
                    last_name         VARCHAR2(25), 
                    job_id            VARCHAR2(10),
                    manager_id        NUMBER(4),
                    hire_date         DATE,
                    salary            NUMBER(8,2),
                    commission_pct    NUMBER(2,2),
                    department_id     NUMBER(4),
                    email             VARCHAR2(25) 
                   ) 
     ORGANIZATION EXTERNAL 
     ( 
       TYPE ORACLE_LOADER 
       DEFAULT DIRECTORY admin_dat_dir 
       ACCESS PARAMETERS 
       ( 
         records delimited by newline 
         badfile admin_bad_dir:'empxt%a_%p.bad' 
         logfile admin_log_dir:'empxt%a_%p.log' 
         fields terminated by ',' 
         missing field values are null 
         ( employee_id, first_name, last_name, job_id, manager_id, 
           hire_date char date_format date mask "dd-mon-yyyy", 
           salary, commission_pct, department_id, email 
         ) 
       ) 
       LOCATION ('empxt1.dat', 'empxt2.dat') 
     ) 
     PARALLEL 
     REJECT LIMIT UNLIMITED; 
-- enable parallel for loading (good if lots of data to load)
ALTER SESSION ENABLE PARALLEL DML;
-- load the data in hr employees table
INSERT INTO employees (employee_id, first_name, last_name, job_id, manager_id,
                       hire_date, salary, commission_pct, department_id, email) 
            SELECT * FROM admin_ext_employees;
```

The following paragraphs contain descriptive information about this example.

The first few statements in this example create the directory objects for the operating system directories that contain the data sources, and for the bad record and log files specified in the access parameters. You must also grant `READ` or `WRITE` directory object privileges, as appropriate.

Note:

When creating a directory object or BFILEs, ensure that the following conditions are met:
- The operating system file must not be a symbolic or hard link.
- The operating system directory path named in the Oracle Database directory object must be an existing OS directory path.
- The operating system directory path named in the directory object should not contain any symbolic links in its components.

The `TYPE` specification indicates the access driver of the external table. The access driver is the API that interprets the external data for the database. If you omit the `TYPE` specification, `ORACLE_LOADER` is the default access driver. You must specify the `ORACLE_DATAPUMP` access driver if you specify the `AS` `subquery` clause to unload data from one Oracle Database and reload it into the same or a different Oracle Database.

The access parameters, specified in the `ACCESS PARAMETERS` clause, are opaque to the database. These access parameters are defined by the access driver, and are provided to the access driver by the database when the external table is accessed. See [Oracle Database Utilities](https://docs.oracle.com/cd/E11882_01/server.112/e22490/et_params.htm#SUTIL012) for a description of the `ORACLE_LOADER` access parameters.

The `PARALLEL` clause enables parallel query on the data sources. The granule of parallelism is by default a data source, but parallel access within a data source is implemented whenever possible. For example, if `PARALLEL=3` were specified, then multiple parallel execution servers could be working on a data source. But, parallel access within a data source is provided by the access driver only if all of the following conditions are met:

- The media allows random positioning within a data source
- It is possible to find a record boundary from a random position
- The data files are large enough to make it worthwhile to break up into multiple chunks
	Note:
	Specifying a `PARALLEL` clause is of value only when dealing with large amounts of data. Otherwise, it is not advisable to specify a `PARALLEL` clause, and doing so can be detrimental.

The `REJECT` `LIMIT` clause specifies that there is no limit on the number of errors that can occur during a query of the external data. For parallel access, the `REJECT` `LIMIT` applies to each parallel execution server independently. For example, if a `REJECT` `LIMIT` of 10 is specified, then each parallel query process can allow up to 10 rejections. Therefore, with a parallel degree of two and a `REJECT` `LIMIT` of 10, the statement might fail with between 10 and 20 rejections. If one parallel server processes all 10 rejections, then the limit is reached, and the statement is terminated. However, one parallel execution server could process nine rejections and another parallel execution server could process nine rejections and the statement will succeed with 18 rejections. Hence, the only precisely enforced values for `REJECT` `LIMIT` on parallel query are `0` and `UNLIMITED`.

In this example, the `INSERT` `INTO` `TABLE` statement generates a dataflow from the external data source to the Oracle Database SQL engine where data is processed. As data is parsed by the access driver from the external table sources and provided to the external table interface, the external data is converted from its external representation to its Oracle Database internal data type.

See Also:

[Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_7002.htm#SQLRF01402) provides details of the syntax of the `CREATE TABLE` statement for creating external tables and specifies restrictions on the use of clauses

### Altering External Tables

You can use any of the `ALTER TABLE` clauses shown in Table 20-5 to change the characteristics of an external table. No other clauses are permitted.

Table 20-5 ALTER TABLE Clauses for External Tables

| ALTER TABLE Clause | Description | Example |
| --- | --- | --- |
| `REJECT LIMIT` | Changes the reject limit. The default value is `0`. | ``` ALTER TABLE admin_ext_employees    REJECT LIMIT 100; ``` |
| `PROJECT` `COLUMN` | Determines how the access driver validates rows in subsequent queries:  - `PROJECT` `COLUMN` `REFERENCED`: the access driver processes only the columns in the select list of the query. This setting may not provide a consistent set of rows when querying a different column list from the same external table. - `PROJECT` `COLUMN` `ALL`: the access driver processes all of the columns defined on the external table. This setting always provides a consistent set of rows when querying an external table. This is the default. | ``` ALTER TABLE admin_ext_employees    PROJECT COLUMN REFERENCED;  ALTER TABLE admin_ext_employees    PROJECT COLUMN ALL; ``` |
| `DEFAULT DIRECTORY` | Changes the default directory specification | ``` ALTER TABLE admin_ext_employees      DEFAULT DIRECTORY admin_dat2_dir; ``` |

### Preprocessing External Tables

Caution:

There are security implications to consider when using the `PREPROCESSOR` clause. See [Oracle Database Security Guide](https://docs.oracle.com/cd/E11882_01/network.112/e36292/guidelines.htm#DBSEG10007) for more information.

External tables can be preprocessed by user-supplied preprocessor programs. By using a preprocessing program, users can use data from a file that is not in a format supported by the driver. For example, a user may want to access data stored in a compressed format. Specifying a decompression program for the `ORACLE_LOADER` access driver allows the data to be decompressed as the access driver processes the data.

To use the preprocessing feature, you must specify the `PREPROCESSOR` clause in the access parameters of the `ORACLE_LOADER` access driver. The preprocessor must be a directory object, and the user accessing the external table must have `EXECUTE` privileges for the directory object. The following example includes the `PREPROCESSOR` clause and specifies the directory and preprocessor program.

```
CREATE TABLE sales_transactions_ext
(PROD_ID NUMBER,
 CUST_ID NUMBER,
 TIME_ID DATE,
 CHANNEL_ID CHAR,
 PROMO_ID NUMBER,
 QUANTITY_SOLD NUMBER,
 AMOUNT_SOLD NUMBER(10,2),
 UNIT_COST NUMBER(10,2),
 UNIT_PRICE NUMBER(10,2))
ORGANIZATION external
(TYPE oracle_loader
 DEFAULT DIRECTORY data_file_dir
 ACCESS PARAMETERS
  (RECORDS DELIMITED BY NEWLINE
   CHARACTERSET AL32UTF8
   PREPROCESSOR exec_file_dir:'zcat'

   BADFILE log_file_dir:'sh_sales.bad_xt'
   LOGFILE log_file_dir:'sh_sales.log_xt'
   FIELDS TERMINATED BY "|" LDRTRIM
  ( PROD_ID,
    CUST_ID,
    TIME_ID,
    CHANNEL_ID,
    PROMO_ID,
    QUANTITY_SOLD,
    AMOUNT_SOLD,
    UNIT_COST,
    UNIT_PRICE))
 location ('sh_sales.dat.gz')
)REJECT LIMIT UNLIMITED;
```

The `PREPROCESSOR` clause is not available for databases that use Oracle Database Vault.

See Also:

- [Oracle Database Utilities](https://docs.oracle.com/cd/E11882_01/server.112/e22490/et_params.htm#SUTIL1385) provides information more information about the `PREPROCESSOR` clause
- [Oracle Database Security Guide](https://docs.oracle.com/cd/E11882_01/network.112/e36292/guidelines.htm#DBSEG10007) for more information about the security implications of the `PREPROCESSOR` clause

### Dropping External Tables

For an external table, the `DROP` `TABLE` statement removes only the table metadata in the database. It has no affect on the actual data, which resides outside of the database.

### System and Object Privileges for External Tables

System and object privileges for external tables are a subset of those for regular table. Only the following system privileges are applicable to external tables:

- `CREATE` `ANY` `TABLE`
- `ALTER` `ANY` `TABLE`
- `DROP` `ANY` `TABLE`
- `SELECT` `ANY` `TABLE`

Only the following object privileges are applicable to external tables:

- `ALTER`
- `SELECT`

However, object privileges associated with a directory are:

- `READ`
- `WRITE`

For external tables, `READ` privileges are required on directory objects that contain data sources, while `WRITE` privileges are required for directory objects containing bad, log, or discard files.

## Tables Data Dictionary Views

The following views allow you to access information about tables.

| View | Description |
| --- | --- |
| `DBA_TABLES`  `ALL_TABLES`  `USER_TABLES` | `DBA` view describes all relational tables in the database. `ALL` view describes all tables accessible to the user. `USER` view is restricted to tables owned by the user. Some columns in these views contain statistics that are generated by the `DBMS_STATS` package or `ANALYZE` statement. |
| `DBA_TAB_COLUMNS`  `ALL_TAB_COLUMNS`  `USER_TAB_COLUMNS` | These views describe the columns of tables, views, and clusters in the database. Some columns in these views contain statistics that are generated by the `DBMS_STATS` package or `ANALYZE` statement. |
| `DBA_ALL_TABLES`  `ALL_ALL_TABLES`  `USER_ALL_TABLES` | These views describe all relational and object tables in the database. Object tables are not specifically discussed in this book. |
| `DBA_TAB_COMMENTS`  `ALL_TAB_COMMENTS`  `USER_TAB_COMMENTS` | These views display comments for tables and views. Comments are entered using the `COMMENT` statement. |
| `DBA_COL_COMMENTS`  `ALL_COL_COMMENTS`  `USER_COL_COMMENTS` | These views display comments for table and view columns. Comments are entered using the `COMMENT` statement. |
| `DBA_EXTERNAL_TABLES`  `ALL_EXTERNAL_TABLES`  `USER_EXTERNAL_TABLES` | These views list the specific attributes of external tables in the database. |
| `DBA_EXTERNAL_LOCATIONS`  `ALL_EXTERNAL_LOCATIONS`  `USER_EXTERNAL_LOCATIONS` | These views list the data sources for external tables. |
| `DBA_TAB_HISTOGRAMS`  `ALL_TAB_HISTOGRAMS`  `USER_TAB_HISTOGRAMS` | These views describe histograms on tables and views. |
| `DBA_TAB_STATISTICS`  `ALL_TAB_STATISTICS`  `USER_TAB_STATISTICS` | These views contain optimizer statistics for tables. |
| `DBA_TAB_COL_STATISTICS`  `ALL_TAB_COL_STATISTICS`  `USER_TAB_COL_STATISTICS` | These views provide column statistics and histogram information extracted from the related `TAB_COLUMNS` views. |
| `DBA_TAB_MODIFICATIONS`  `ALL_TAB_MODIFICATIONS`  `USER_TAB_MODIFICATIONS` | These views describe tables that have been modified since the last time table statistics were gathered on them. They are not populated immediately, but after a time lapse (usually 3 hours). |
| `DBA_ENCRYPTED_COLUMNS`  `USER_ENCRYPTED_COLUMNS`  `ALL_ENCRYPTED_COLUMNS` | These views list table columns that are encrypted, and for each column, lists the encryption algorithm in use. |
| `DBA_UNUSED_COL_TABS`  `ALL_UNUSED_COL_TABS`  `USER_UNUSED_COL_TABS` | These views list tables with unused columns, as marked by the `ALTER TABLE ... SET UNUSED` statement. |
| `DBA_PARTIAL_DROP_TABS`  `ALL_PARTIAL_DROP_TABS`  `USER_PARTIAL_DROP_TABS` | These views list tables that have partially completed `DROP COLUMN` operations. These operations could be incomplete because the operation was interrupted by the user or a system failure. |

Example: Displaying Column Information

Column information, such as name, data type, length, precision, scale, and default data values can be listed using one of the views ending with the `_COLUMNS` suffix. For example, the following query lists all of the default column values for the `emp` and `dept` tables:

```
SELECT TABLE_NAME, COLUMN_NAME, DATA_TYPE, DATA_LENGTH, LAST_ANALYZED
    FROM DBA_TAB_COLUMNS
    WHERE OWNER = 'HR'
    ORDER BY TABLE_NAME;
```

The following is the output from the query:

```
TABLE_NAME           COLUMN_NAME          DATA_TYPE   DATA_LENGTH LAST_ANALYZED
-------------------- -------------------- ---------- ------------ -------------
COUNTRIES            COUNTRY_ID           CHAR                  2 05-FEB-03
COUNTRIES            COUNTRY_NAME         VARCHAR2             40 05-FEB-03
COUNTRIES            REGION_ID            NUMBER               22 05-FEB-03
DEPARTMENTS          DEPARTMENT_ID        NUMBER               22 05-FEB-03
DEPARTMENTS          DEPARTMENT_NAME      VARCHAR2             30 05-FEB-03
DEPARTMENTS          MANAGER_ID           NUMBER               22 05-FEB-03
DEPARTMENTS          LOCATION_ID          NUMBER               22 05-FEB-03
EMPLOYEES            EMPLOYEE_ID          NUMBER               22 05-FEB-03
EMPLOYEES            FIRST_NAME           VARCHAR2             20 05-FEB-03
EMPLOYEES            LAST_NAME            VARCHAR2             25 05-FEB-03
EMPLOYEES            EMAIL                VARCHAR2             25 05-FEB-03
.
.
.
LOCATIONS            COUNTRY_ID           CHAR                  2 05-FEB-03
REGIONS              REGION_ID            NUMBER               22 05-FEB-03
REGIONS              REGION_NAME          VARCHAR2             25 05-FEB-03

51 rows selected.
```

See Also:

- [Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/toc.htm) for complete descriptions of these views
- [Oracle Database Object-Relational Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e11822/adobjint.htm#ADOBJ7034) for information about object tables
- [Oracle Database Performance Tuning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41573/stats.htm#PFGRF003) for information about histograms and generating statistics for tables
- ["Analyzing Tables, Indexes, and Clusters"](general.md)

[^1]: Copy dependent objects (such as triggers, indexes, materialized view logs, grants, and constraints) and statistics from the table being redefined to the interim table, using one of the following two methods. Method 1 is the preferred method because it is more automatic, but there may be times that you would choose to use method 2. Method 1 also enables you to copy table statistics to the interim table.

- Method 1: Automatically Creating Dependent Objects
	Use the `COPY_TABLE_DEPENDENTS` procedure to automatically create dependent objects on the interim table. This procedure also registers the dependent objects. Registering the dependent objects enables the identities of these objects and their copied counterparts to be automatically swapped later as part of the redefinition completion process. The result is that when the redefinition is completed, the names of the dependent objects will be the same as the names of the original dependent objects.
	For more information, see "Creating Dependent Objects Automatically".
- Method 2: Manually Creating Dependent Objects
	You can manually create dependent objects on the interim table and then register them. For more information, see "Creating Dependent Objects Manually".
	Note:
	In Oracle Database Release 9i, you were required to manually create the triggers, indexes, grants, and constraints on the interim table, and there may still be situations where you want to or must do so. In such cases, any referential constraints involving the interim table (that is, the interim table is either a parent or a child table of the referential constraint) must be created disabled. When online redefinition completes, the referential constraint is automatically enabled. In addition, until the redefinition process is either completed or aborted, any trigger defined on the interim table does not execute.

[^undefined]: Execute the `FINISH_REDEF_TABLE` procedure to complete the redefinition of the table. During this procedure, the original table is locked in exclusive mode for a very short time, independent of the amount of data in the original table. However, `FINISH_REDEF_TABLE` will wait for all pending DML to commit before completing the redefinition.

[^undefined]: If you used rowids for the redefinition and your `COMPATIBLE` initialization parameter is set to 10.1.0 or lower, drop or set `UNUSED` the hidden column `M_ROW$$` that is now in the redefined table.

```
ALTER TABLE table_name SET UNUSED (M_ROW$$);
```

If `COMPATIBLE` is 10.2.0 or higher, this hidden column is automatically set `UNUSED` when redefinition completes. You can then drop the column with the `ALTER` `TABLE`... `DROP` `UNUSED` `COLUMNS` statement.

[^undefined]: Wait for any long-running queries against the interim table to complete, and then drop the interim table.

If you drop the interim table while there are active queries running against it, you may encounter an `ORA-08103` error ("object no longer exists").

[^2]: Copy dependent objects.

```
DECLARE
num_errors PLS_INTEGER;
BEGIN
  DBMS_REDEFINITION.COPY_TABLE_DEPENDENTS(
   'STEVE','CUSTOMER','INT_CUSTOMER',DBMS_REDEFINITION.CONS_ORIG_PARAMS,
    TRUE, TRUE, TRUE, FALSE, num_errors, TRUE);
END;
/
```

Note that for this call, the final argument indicates that table statistics are to be copied to the interim table.

[^undefined]: Optionally synchronize the interim table.

```
BEGIN 
  DBMS_REDEFINITION.SYNC_INTERIM_TABLE('STEVE', 'CUSTOMER', 'INT_CUSTOMER');
END;
/
```

[^undefined]: Complete the redefinition.

```
BEGIN
  DBMS_REDEFINITION.FINISH_REDEF_TABLE('STEVE', 'CUSTOMER', 'INT_CUSTOMER');
END;
/
```

[^undefined]: Wait for any long-running queries against the interim table to complete, and then drop the interim table.