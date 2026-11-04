---
title: SQL Language Reference
book: SQL Language Reference
doc_id: E83703-08
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/sqlrf/Changes-in-This-Release-for-Oracle-Database-SQL-Language-Reference.html
tags:
  - oracle
  - 12c
  - sql-language-reference
---

This preface contains:

### Changes in Oracle Database 12c Release 2 (12.2.0.1)

The following are changes in Oracle Database SQL Language Reference for Oracle Database 12c Release 2 (12.2.0.1).

#### New Features

The following features are new in this release:

Long Identifiers

The maximum length for most database object names has increased from 30 bytes to 128 bytes.

See [Database Object Naming Rules](Database-Object-Names-and-Qualifiers.md).

Data-Bound Collation and Case-Insensitive Databases

Data-bound collation allows you to declare character comparison rules at the column level. The collation declared for a column is automatically applied to all collation-sensitive SQL operations that reference the column. This enables applications to consistently apply language-specific comparison rules to the exact data that requires these rules. Data-bound collation also allows you to declare a case-insensitive collation for a table or a schema, so that all columns in a table or schema can be compared in a case-insensitive manner. This enables you to create a case-insensitive database.

See [Data-Bound Collation](Data-Type-Comparison-Rules.md).

Features that Introduce New SQL Statements

The following features introduce new SQL statements:

- Analytic views are metadata objects that provide a fast and efficient way to create and store analytic queries of data in existing database tables and views. With analytic views you can easily create complex analytic queries on large amounts of hierarchical and dimensional data. Attribute dimensions, hierarchies, and analytic views are new database schema objects.
	See the following new statements:
	- [CREATE ANALYTIC VIEW](CREATE-ANALYTIC-VIEW.md)
		- [CREATE ATTRIBUTE DIMENSION](CREATE-ATTRIBUTE-DIMENSION.md)
		- [CREATE HIERARCHY](CREATE-HIERARCHY.md)
		- [ALTER ANALYTIC VIEW](ALTER-ANALYTIC-VIEW.md)
		- [ALTER ATTRIBUTE DIMENSION](ALTER-ATTRIBUTE-DIMENSION.md)
		- [ALTER HIERARCHY](ALTER-HIERARCHY.md)
		- [DROP ANALYTIC VIEW](DROP-ANALYTIC-VIEW.md)
		- [DROP ATTRIBUTE DIMENSION](DROP-ATTRIBUTE-DIMENSION.md)
		- [DROP HIERARCHY](DROP-HIERARCHY.md)
- Join groups allow you to optimize join queries for table columns that are populated in the In-Memory Column Store.
	See the following new statements:
	- [CREATE INMEMORY JOIN GROUP](CREATE-INMEMORY-JOIN-GROUP.md)
		- [ALTER INMEMORY JOIN GROUP](ALTER-INMEMORY-JOIN-GROUP.md)
		- [DROP INMEMORY JOIN GROUP](DROP-INMEMORY-JOIN-GROUP.md)
- Oracle Sharding supports distribution and replication of data across a pool of discrete Oracle databases that share no hardware or software.
	See the following new statements:
	- [CREATE TABLESPACE SET](CREATE-TABLESPACE-SET.md)
		- [ALTER TABLESPACE SET](ALTER-TABLESPACE-SET.md)
		- [DROP TABLESPACE SET](DROP-TABLESPACE-SET.md)
	See the new clauses [SHARDED](CREATE-TABLE.md) and [DUPLICATED](CREATE-TABLE.md) of `CREATE` `TABLE`.
- You can use PDB lockdown profiles in a multitenant container database (CDB) to restrict user operations in PDBs.
	See the following new statements:
	- [CREATE LOCKDOWN PROFILE](CREATE-LOCKDOWN-PROFILE.md)
		- [ALTER LOCKDOWN PROFILE](ALTER-LOCKDOWN-PROFILE.md)
		- [DROP LOCKDOWN PROFILE](DROP-LOCKDOWN-PROFILE.md)

ADMINISTER KEY MANAGEMENT Enhancements

- You can instruct the database to force a keystore open for certain operations.
	See [Notes on the FORCE KEYSTORE Clause](ADMINISTER-KEY-MANAGEMENT.md).
- You can use keystore passwords stored in an external store.
	See the new clause `EXTERNAL` `STORE` in [Notes on Specifying Keystore Passwords](ADMINISTER-KEY-MANAGEMENT.md).
- You can specify an encryption algorithm for a master key.
	See the new clause `USING` `ALGORITHM` of [set\_key](ADMINISTER-KEY-MANAGEMENT.md) and [create\_key](ADMINISTER-KEY-MANAGEMENT.md).

ALTER SESSION Enhancement

- When you switch to a different container in a CDB, you can specify the service you would like to use in the new container.
	See the new clause [SERVICE](ALTER-SESSION.md).

AUDIT and NOAUDIT (Unified Auditing) Enhancements

- You can enable or disable unified audit policies for users who have been directly granted specific roles.
	See the new clauses [by\_users\_with\_roles](AUDIT-Unified-Auditing.md) of `AUDIT` and `NOAUDIT`.

CREATE DATABASE and ALTER DATABASE Enhancements

- You can specify a local temporary tablespace for your database.
	See the clause [default\_temp\_tablespace](CREATE-DATABASE.md) of `CREATE` `DATABASE` and the [DEFAULT \[LOCAL\] TEMPORARY TABLESPACE Clause](https://docs.oracle.com/en/database/oracle/oracle-database/12.2/sqlrf/ALTER-DATABASE.html#GUID-8069872F-E680-4511-ADD8-A4E30AF67986__BGBEIJJD) of `ALTER` `DATABASE`.
- You can specify local undo mode or shared undo mode for a CDB.
	See the new [undo\_mode\_clause](CREATE-DATABASE.md) of `CREATE` `DATABASE` and [undo\_mode\_clause](ALTER-DATABASE.md) of `ALTER` `DATABASE`.
- For Oracle Real Application Clusters (Oracle RAC) or Oracle RAC One Node databases, you can control the number of instances on a physical standby that Redo Apply uses.
	See the new clause [USING INSTANCES](ALTER-DATABASE.md) of `ALTER` `DATABASE`.
- You can perform offline encryption or decryption of a data file using Transparent Data Encryption (TDE).
	See the new clauses [ENCRYPT | DECRYPT](ALTER-DATABASE.md) of `ALTER` `DATABASE`.

CREATE DIRECTORY Enhancement

- You can create directories that are application common objects. Application common objects can be shared by application PDBs in an application container.
	See the new clause [SHARING](CREATE-DIRECTORY.md) of `CREATE` `DIRECTORY`.

CREATE DISKGROUP and ALTER DISKGROUP Enhancements

- You can create Oracle ASM flex disk groups, which support quota groups and file groups. Flex disk groups enable you to define a quota limit for the files of a group of databases within a disk group.
	See:
	- The new `FLEX` keyword in the [REDUNDANCY Clause](CREATE-DISKGROUP.md) of `CREATE` `DISKGROUP`.
		- The new [quotagroup\_clauses](ALTER-DISKGROUP.md) of `ALTER` `DISKGROUP`.
		- The new [filegroup\_clauses](ALTER-DISKGROUP.md) of `ALTER` `DISKGROUP`.
- You can pause, restart, and change the power of active disk group rebalance operations. You can also specify which phases of a rebalance operation to perform.
	See the [rebalance\_diskgroup\_clause](ALTER-DISKGROUP.md) of `ALTER` `DISKGROUP`.
- The following new Oracle ASM disk group attributes are listed in [Table 13-2](CREATE-DISKGROUP.md):
	- `LOGICAL_SECTOR_SIZE` allows you to set the logical sector size of a disk group.
		- `PREFERRED_READ.ENABLED` allows you to specify whether preferred read functionality is enabled for a disk group in an Oracle extended cluster.

CREATE INDEX, ALTER INDEX, and DROP INDEX Enhancements

- You can specify whether to invalidate dependent cursors while creating an index, rebuilding an index, marking an index `UNUSABLE`, or dropping an index.
	See the new clause `{` `DEFERRED` `|` `IMMEDIATE` `}` `INVALIDATION` of [`CREATE` `INDEX`](CREATE-INDEX.md), [`ALTER` `INDEX`](ALTER-TABLE.md), and [`DROP` `INDEX`](DROP-INDEX.md).
- Advanced index compression provides a `HIGH` compression level.
	See the new `HIGH` keyword of the clause [advanced\_index\_compression](CREATE-INDEX.md) of `CREATE` `INDEX`.

CREATE JAVA Enhancement

- You can create Java schema objects that are application common objects. Application common objects can be shared by application PDBs in an application container.
	See the new clause [SHARING](CREATE-JAVA.md) of `CREATE` `JAVA`.

CREATE MATERIALIZED VIEW and ALTER MATERIALIZED VIEW Enhancements

- A real-time materialized view provides fresh data to user queries even when the materialized view is not in sync with its base tables due to data changes.
	See the new clause `{` `ENABLE` `|` `DISABLE` `}` `ON` `QUERY` `COMPUTATION` of [`CREATE` `MATERIALIZED` `VIEW`](CREATE-MATERIALIZED-VIEW.md) and [`ALTER` `MATERIALIZED` `VIEW`](ALTER-MATERIALIZED-VIEW.md).
- The `ON` `STATEMENT` refresh mode causes an automatic refresh to occur every time a DML operation is performed on any of a materialized view's base tables.
	See the new [ON STATEMENT Clause](CREATE-MATERIALIZED-VIEW.md) of `CREATE` `MATERIALIZED` `VIEW`.

CREATE PLUGGABLE DATABASE and ALTER PLUGGABLE DATABASE Enhancements

- An application container is a component of a CDB that stores data for one or more applications. It consists of an application root, an optional application seed, and application PDBs.
	See the new clauses [AS APPLICATION CONTAINER](CREATE-PLUGGABLE-DATABASE.md) and [AS SEED](CREATE-PLUGGABLE-DATABASE.md) of `CREATE` `PLUGGABLE` `DATABASE`.
- You can perform the following operations in an application container:
	- Install, patch, upgrade, and uninstall applications
		- Register application versions and patch numbers
		- Keep applications in sync between the application root and application PDBs
	See the new [application\_clauses](ALTER-PLUGGABLE-DATABASE.md) of `ALTER` `PLUGGABLE` `DATABASE`.
- You can create a refreshable PDB when cloning a PDB. Changes in the source PDB can be propagated to the refreshable PDB, either manually or automatically.
	See the new [pdb\_refresh\_mode\_clause](CREATE-PLUGGABLE-DATABASE.md) of `CREATE` `PLUGGABLE` `DATABASE` and the new clauses [REFRESH](ALTER-PLUGGABLE-DATABASE.md) and [pdb\_refresh\_mode\_clause](ALTER-PLUGGABLE-DATABASE.md) of `ALTER` `PLUGGABLE` `DATABASE`.
- A proxy PDB references a PDB in a different CDB and provides fully functional access to the referenced PDB.
	See the new clauses [AS PROXY FROM](CREATE-PLUGGABLE-DATABASE.md) and [HOST and PORT](CREATE-PLUGGABLE-DATABASE.md) of `CREATE` `PLUGGABLE` `DATABASE`.
- You can relocate a PDB from one CDB to another.
	See the new clause [RELOCATE](CREATE-PLUGGABLE-DATABASE.md) of `CREATE` `PLUGGABLE` `DATABASE`.
- When cloning a PDB, you can instruct the database to clone a tablespace using storage snapshots or clone the data model definition of a tablespace, but not the tablespace's data.
	See the new clauses [{ SNAPSHOT COPY | NO DATA }](CREATE-PLUGGABLE-DATABASE.md) of `CREATE` `PLUGGABLE` `DATABASE`.
- When plugging in a PDB, you can instruct the database to copy or move tablespace files to a new location.
	See the new clauses [{ COPY | MOVE | NOCOPY }](CREATE-PLUGGABLE-DATABASE.md) of `CREATE` `PLUGGABLE` `DATABASE`.
- In earlier releases, you could specify a permanent default tablespace only when creating a PDB from seed. You can now also specify a permanent default tablespace when cloning a PDB or plugging in a PDB.
	See the clause [default\_tablespace](CREATE-PLUGGABLE-DATABASE.md) of `CREATE` `PLUGGABLE` `DATABASE`.
- You can use parallel execution servers to copy a new PDB's data files to a new location. This may result in faster creation of the PDB.
	See the new [parallel\_pdb\_creation\_clause](CREATE-PLUGGABLE-DATABASE.md) of `CREATE` `PLUGGABLE` `DATABASE`.

CREATE PROFILE and ALTER PROFILE Enhancements

- In profiles, you can specify the permitted number of consecutive days of no logins after which an account will be locked.
	See the new [INACTIVE\_ACCOUNT\_TIME](CREATE-PROFILE.md) setting of `CREATE` `PROFILE` and `ALTER` `PROFILE`.

CREATE RESTORE POINT Enhancement

- You can create restore points for a PDB.
	See the new clauses [CLEAN](CREATE-RESTORE-POINT.md) and [FOR PLUGGABLE DATABASE](CREATE-RESTORE-POINT.md) of `CREATE` `RESTORE` `POINT`.

CREATE SEQUENCE Enhancement

- You can create sequences that are application common objects. Application common objects can be shared by application PDBs in an application container.
	See the new clause [SHARING](CREATE-SEQUENCE.md) of `CREATE` `SEQUENCE`.

CREATE SYNONYM Enhancement

- You can create synonyms that are application common objects. Application common objects can be shared by application PDBs in an application container.
	See the new clause [SHARING](CREATE-SYNONYM.md) of `CREATE` `SYNONYM`.

CREATE TABLE and ALTER TABLE Enhancements

- You can create partitioned external tables.
	See the [external\_table\_clause](CREATE-TABLE.md) of `CREATE` `TABLE` and the clause [alter\_external\_table](ALTER-TABLE.md) of `ALTER` `TABLE`.
- You can specify constraints on external tables.
	See [External Table Constraints](constraint.md).
- You can specify up to 16 partitioning key columns for list-partitioned tables, and up to 16 subpartitioning key columns for composite-partitioned tables that use list subpartitioning. In earlier releases, you could specify only one partitioning or subpartitioning key column.
	See the [list\_values\_clause](CREATE-TABLE.md) of `CREATE` `TABLE` and `ALTER` `TABLE`.
- You can create an automatic list-partitioned table. This type of table enables the database to create additional list partitions on demand.
	See the new clauses [AUTOMATIC](CREATE-TABLE.md) of `CREATE` `TABLE` and [alter\_automatic\_partitioning](ALTER-TABLE.md) of `ALTER` `TABLE`.
- You can change a nonpartitioned table to a partitioned table.
	See the new clause [modify\_to\_partitioned](ALTER-TABLE.md) of `ALTER` `TABLE`.
- You can create a table that matches the structure of an existing partitioned table. The two tables are then eligible for exchanging partitions and subpartitions.
	See the new clause [FOR EXCHANGE WITH TABLE](CREATE-TABLE.md) of `CREATE` `TABLE`.
- You can specify which rows to preserve during the following operations: moving, splitting, or merging table partitions or subpartitions; moving a table; or converting a nonpartitioned table to a partitioned table.
	See the new clause [filter\_condition](ALTER-TABLE.md) of `ALTER` `TABLE`.
- You can specify read-only mode for a table, partition, or subpartition.
	See the new [read\_only\_clause](CREATE-TABLE.md) of `CREATE` `TABLE` and `ALTER` `TABLE`.
- DML operations on a table are allowed while splitting its partitions and subpartitions.
	See the new `ONLINE` keyword of the clauses [split\_table\_partition](ALTER-TABLE.md) and [split\_table\_subpartition](ALTER-TABLE.md) of `ALTER` `TABLE`.
- Nonpartitioned tables can be moved as an online operation without blocking any concurrent DML operations. A table move operation now also supports automatic index maintenance as part of the move.
	See the [move\_table\_clause](ALTER-TABLE.md) of `ALTER` `TABLE`.
- You can specify whether to invalidate dependent cursors while performing table partition maintenance operations.
	See the new clause [{ DEFERRED | IMMEDIATE } INVALIDATION](ALTER-TABLE.md) of `ALTER` `TABLE`.
- You can create tables that are application common objects. Application common objects can be shared by application PDBs in an application container.
	See the new clause [SHARING](CREATE-TABLE.md) of `CREATE` `TABLE`.
- Table column encryption supports the following additional algorithms: `ARIA192`, `ARIA256`, `GOST256`, and `SEED128`.
	See the clause [encryption\_spec](CREATE-TABLE.md) of `CREATE` `TABLE` and `ALTER` `TABLE`.
- When specifying default In-Memory Column Store (IM column store) settings for a table, you can specify the Oracle RAC or Oracle Active Data Guard instances in which the table is eligible to be populated in the IM column store.
	See the new clause [FOR SERVICE](CREATE-TABLE.md) of `CREATE` `TABLE` and `ALTER` `TABLE`.
- You can create Automatic Data Optimization policies that enable, disable, or recompress tables in the IM column store.
	See the new clause [ilm\_inmemory\_policy](ALTER-TABLE.md) of `CREATE` `TABLE` and `ALTER` `TABLE`.
- Automatic Data Optimization compression policies support an additional compression method: `COLUMN` `STORE` `COMPRESS` `FOR` `QUERY`.
	See the clause [ilm\_compression\_policy](ALTER-TABLE.md) of `CREATE` `TABLE` and `ALTER` `TABLE`.

CREATE TABLESPACE and ALTER TABLESPACE Enhancements

- Tablespace encryption enhancements: You can encrypt both offline and online tablespaces. You can encrypt undo tablespaces, temporary tablespaces, and the `SYSTEM` and `SYSAUX` tablespaces. Tablespace encryption supports the following additional algorithms: `ARIA192`, `ARIA256`, `GOST256`, and `SEED128`.
	See the new [tablespace\_encryption\_clause](CREATE-TABLESPACE.md) of `CREATE` `TABLESPACE` and the new clause [alter\_tablespace\_encryption](ALTER-TABLESPACE.md) of `ALTER` `TABLESPACE`.
- You can create local temporary tablespaces, which are useful for Oracle Real Application Clusters and Oracle Flex Clusters. They store a separate, nonshared temp file for each database instance, which can improve I/O performance.
	See the new `LOCAL` `TEMPORARY` `TABLESPACE` clause of the [temporary\_tablespace\_clause](CREATE-TABLESPACE.md) of `CREATE` `TABLESPACE`.
- You can specify a default index compression method for a tablespace.
	See the new clause [default\_index\_compression](CREATE-TABLESPACE.md) of `CREATE` `TABLESPACE` and the clause [default\_tablespace\_params](ALTER-TABLESPACE.md) of `ALTER` `TABLESPACE`.
- In earlier releases of Oracle Database, you could specify a default table compression method for a tablespace. You can still do this in Oracle Database 12c Release 2 (12.2), however, the syntax now includes the `TABLE` keyword to differentiate it from the new default index compression syntax.
	See the new clause [default\_table\_compression](CREATE-TABLESPACE.md) of `CREATE` `TABLESPACE` and the clause [default\_tablespace\_params](ALTER-TABLESPACE.md) of `ALTER` `TABLESPACE`.

CREATE USER and ALTER USER Enhancements

- You can assign a local temporary tablespace to a user.
	See the new `LOCAL` keyword for the `TEMPORARY` `TABLESPACE` clause of [`CREATE` `USER`](CREATE-USER.md) and [`ALTER` `USER`](ALTER-USER.md).

CREATE VIEW Enhancement

- You can create views that are application common objects. Application common objects can be shared by application PDBs in an application container.
	See the new clause [SHARING](CREATE-VIEW.md) of `CREATE` `VIEW`.

FLASHBACK DATABASE Enhancement

- You can flash back a PDB.
	See the new clause [PLUGGABLE](FLASHBACK-DATABASE.md) of `FLASHBACK` `DATABASE`.

SELECT Enhancement

- The `query_table_expression` clause of the `FROM` clause of the `SELECT` statement now accepts a hierarchy or an analytic view in a subquery.
	See the clause [query\_table\_expression](SELECT.md) of `SELECT`.

New Operator

- The new `COLLATE` operator determines the collation for an expression. This operator enables you to override the collation that the database would have derived for the expression using standard collation derivation rules.
	See [COLLATE Operator](COLLATE-Operator.md).

New or Enhanced Expressions

- The new calculated measure expression defines a calculated measure in an analytic view.
	See [Calculated Measure Expressions](Calculated-Measure-Expressions.md).
- JSON object access expressions have been enhanced to let you access specific elements of a JSON array.
	See the clause `array_step` of [JSON Object Access Expressions](JSON-Object-Access-Expressions.md).

Enhanced Condition

- The `JSON_EXISTS` condition now lets you pass values to the path expression.
	See the new clause [JSON\_passing\_clause](SQL-JSON-Conditions.md) of `JSON_EXISTS`.

New or Enhanced Functions

- Approximate Query Processing Functions
	The following new functions return approximate results with negligible deviation from the exact result:
	- [APPROX\_MEDIAN](APPROX_MEDIAN.md) takes a numeric or datetime value and returns an approximate median value.
		- [APPROX\_PERCENTILE](APPROX_PERCENTILE.md) takes a percentile value and a sort specification, and returns the value that would fall into that percentile value with respect to the sort specification.
	The following new functions support materialized view-based summary aggregation strategies for approximate distinct value counts:
	- [APPROX\_COUNT\_DISTINCT\_DETAIL](APPROX_COUNT_DISTINCT_DETAIL.md) calculates information about the approximate number of rows that contain a distinct value for an expression and returns a `BLOB` value, called a detail, which contains that information in a special format.
		- [APPROX\_COUNT\_DISTINCT\_AGG](APPROX_COUNT_DISTINCT_AGG.md) takes as its input a column of details containing information about approximate distinct value counts, and enables you to perform aggregations of those counts.
		- [TO\_APPROX\_COUNT\_DISTINCT](TO_APPROX_COUNT_DISTINCT.md) takes as its input a detail containing information about an approximate distinct value count, and converts it to a `NUMBER` value.
	The following new functions support materialized view-based summary aggregation strategies for approximate percentile values:
	- [APPROX\_PERCENTILE\_DETAIL](APPROX_PERCENTILE_DETAIL.md) calculates approximate percentile information for the values and returns a `BLOB` value, called a detail, which contains that information in a special format.
		- [APPROX\_PERCENTILE\_AGG](APPROX_PERCENTILE_AGG.md) takes as its input a column of details containing approximate percentile information, and enables you to perform aggregations of that information.
		- [TO\_APPROX\_PERCENTILE](TO_APPROX_PERCENTILE.md) takes as its input a detail containing approximate percentile information, a percentile value, and a sort specification, and returns an approximate value that would fall into that percentile value with respect to the sort specification.
- Collation Functions
	The following new functions return information about collation settings:
	- [COLLATION](COLLATION.md) returns the name of the derived collation for an expression.
		- [NLS\_COLLATION\_ID](NLS_COLLATION_ID.md) takes as its argument a collation name and returns the corresponding collation ID number.
		- [NLS\_COLLATION\_NAME](NLS_COLLATION_NAME.md) takes as its argument a collation ID number and returns the corresponding collation name.
- Conversion Functions
	The following conversion functions now allow you to specify a value to be returned if a conversion error occurs:
	- [CAST](CAST.md) - In addition, this function now lets you to specify a format model and NLS parameters to be applied for the conversion.
		- [TO\_BINARY\_DOUBLE](TO_BINARY_DOUBLE.md)
		- [TO\_BINARY\_FLOAT](TO_BINARY_FLOAT.md)
		- [TO\_DATE](TO_DATE.md)
		- [TO\_DSINTERVAL](TO_DSINTERVAL.md)
		- [TO\_NUMBER](TO_NUMBER.md)
		- [TO\_TIMESTAMP](TO_TIMESTAMP.md)
		- [TO\_TIMESTAMP\_TZ](TO_TIMESTAMP_TZ.md)
		- [TO\_YMINTERVAL](TO_YMINTERVAL.md)
	The following new function lets you determine whether an expression can be converted to a specified data type:
	- [VALIDATE\_CONVERSION](VALIDATE_CONVERSION.md)
	The following new functions allow additional data types to be converted to `BLOB`, character, and `CLOB` values:
	- [TO\_BLOB (bfile)](TO_BLOB-bfile.md) converts a `BFILE` value to a `BLOB` value.
		- [TO\_CHAR (bfile|blob)](TO_CHAR-bfile-blob.md) converts `BFILE` or `BLOB` data to the database character set.
		- [TO\_CLOB (bfile|blob)](TO_CLOB-bfile-blob.md) converts `BFILE` or `BLOB` data to the database character set and returns the data as a `CLOB` value.
- Data Mining Functions
	The data mining functions are enhanced so they can be applied to models built using the native algorithms of Oracle, as well as those built using R through the extensibility mechanism of Oracle Advanced Analytics. See [Data Mining Functions](Single-Row-Functions.md).
	The following are new data mining functions:
	- [FEATURE\_COMPARE](FEATURE_COMPARE.md) uses a Feature Extraction model to compare two different documents.
		- [ORA\_DM\_PARTITION\_NAME](ORA_DM_PARTITION_NAME.md) returns the name of the partition associated with the input row.
	The syntax of the following functions is enhanced so that the functions can use the `GROUPING` hint when scoring a partitioned model:
	- [CLUSTER\_DETAILS](CLUSTER_DETAILS.md)
		- [CLUSTER\_DISTANCE](CLUSTER_DISTANCE.md)
		- [CLUSTER\_ID](CLUSTER_ID.md)
		- [CLUSTER\_PROBABILITY](CLUSTER_PROBABILITY.md)
		- [CLUSTER\_SET](CLUSTER_SET.md)
		- [FEATURE\_COMPARE](FEATURE_COMPARE.md)
		- [FEATURE\_DETAILS](FEATURE_DETAILS.md)
		- [FEATURE\_ID](FEATURE_ID.md)
		- [FEATURE\_SET](FEATURE_SET.md)
		- [FEATURE\_VALUE](FEATURE_VALUE.md)
		- [ORA\_DM\_PARTITION\_NAME](ORA_DM_PARTITION_NAME.md)
		- [PREDICTION](PREDICTION.md)
		- [PREDICTION\_BOUNDS](PREDICTION_BOUNDS.md)
		- [PREDICTION\_COST](PREDICTION_COST.md)
		- [PREDICTION\_DETAILS](PREDICTION_DETAILS.md)
		- [PREDICTION\_PROBABILITY](PREDICTION_PROBABILITY.md)
		- [PREDICTION\_SET](PREDICTION_SET.md)
- JSON Functions
	The following new functions enable you to query and generate JavaScript Object Notation (JSON) data:
	- [JSON\_ARRAY](JSON_ARRAY.md) takes as its input one or more SQL expressions, converts each expression to a JSON value, and returns a JSON array that contains those JSON values.
		- [JSON\_ARRAYAGG](JSON_ARRAYAGG.md) takes as its input a column of SQL expressions, converts each expression to a JSON value, and returns a single JSON array that contains those JSON values.
		- [JSON\_DATAGUIDE](JSON_DATAGUIDE.md) takes as its input a table column of JSON data. Each row in the column is referred to as a JSON document. For each JSON document in the column, this function returns a `CLOB` value that contains a flat data guide for that JSON document.
		- [JSON\_OBJECT](JSON_OBJECT.md) takes as its input one or more property key-value pairs, and returns a JSON object that contains an object member for each of those key-value pairs.
		- [JSON\_OBJECTAGG](JSON_OBJECTAGG.md) takes as its input a property key-value pair, constructs an object member for each key-value pair, and returns a single JSON object that contains those object members.
	The following JSON functions have been enhanced to let you specify a return value when no match is found:
	- [JSON\_QUERY](JSON_QUERY.md)
		- [JSON\_VALUE](JSON_VALUE.md)
- LISTAGG Function
	- [LISTAGG](LISTAGG.md) now allows you to control how the function behaves when the return value exceeds the maximum length of the return data type.

New or Enhanced Privileges

The following are new or enhanced system privileges and object privileges:

- The following system privileges, which are listed in [Table 18-1](GRANT.md), have been enhanced:
	- `CREATE` `JOB` and `CREATE` `ANY` `JOB` now allow you to manage resource objects and incompatibility resource objects.
- The following new system privileges are listed in [Table 18-1](GRANT.md):
	- These system privileges allow the creation and management of analytic views:
		`CREATE` `ANALYTIC` `VIEW`, `CREATE` `ANY` `ANALYTIC` `VIEW`, `ALTER` `ANY` `ANALYTIC` `VIEW`, `DROP` `ANY` `ANALYTIC` `VIEW`
		`CREATE` `ATTRIBUTE` `DIMENSION`, `CREATE` `ANY` `ATTRIBUTE` `DIMENSION`, `ALTER` `ANY` `ATTRIBUTE` `DIMENSION`, `DROP` `ANY` `ATTRIBUTE` `DIMENSION`
		`CREATE` `HIERARCHY`, `CREATE` `ANY` `HIERARCHY`, `ALTER` `ANY` `HIERARCHY`, and `DROP` `ANY` `HIERARCHY`
		- `CREATE` `LOCKDOWN` `PROFILE`, `ALTER` `LOCKDOWN` `PROFILE`, and `DROP` `LOCKDOWN` `PROFILE` allow you to manage PDB lockdown profiles.
		- `INHERIT` `ANY` `REMOTE` `PRIVILEGES` allows you to execute definer's rights procedures or functions that contain current user database links.
		- `USE` `ANY` `JOB` `RESOURCE` allows you to associate any schedule resource object with any program or job in the grantee’s schema.
- The following new object privileges are listed in [Table 18-2](GRANT.md):
	- `INHERIT` `REMOTE` `PRIVILEGES` can be granted on a user to users and roles. It allows the user on whom this privilege is granted to execute definer's rights procedures or functions that contain current user database links and are owned by the grantee.
		- The `USE` privilege can be granted on job scheduler objects. It allows you to associate the specified scheduler resource object with programs and jobs.

New Hints

The following are new hints:

- The [CONTAINERS Hint](Comments.md) lets you pass a hint to the query of each PDB in a CDB or application container during a `SELECT`... `containers_clause`... query.
- The [FRESH\_MV Hint](Comments.md) is part of the new real-time materialized view feature. This hint allows you to fetch up-to-date data from a stale real-time materialized view.
- The [GROUPING Hint](Comments.md) applies to data mining scoring functions when scoring partitioned models.
- The [USE\_BAND Hint](Comments.md) and [NO\_USE\_BAND Hint](Comments.md) allow you to use or exclude band joins in a query. Band joins are new for this release. For more information, see [Band Joins](Joins.md).

#### Deprecated Features

The following features are deprecated in this release, and may be desupported in a future release:

- The Oracle Multimedia support for object types that comply with the first edition of the ISO/IEC 13249-5:2001 SQLMM Part5:StillImage standard (commonly referred to as the SQL/MM Still Image standard) is deprecated.
	See [Oracle Multimedia Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/sqlrf&id=AIVUG-GUID-96044E20-7005-4C46-852D-43D0B2D3A125) for more information.
- The [XMLROOT](XMLROOT.md) function is deprecated. It is still supported for backward compatibility. However, Oracle recommends that you instead use the SQL/XML function `XMLSERIALIZE` with a version number.
	See [Oracle XML DB Developer's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/sqlrf&id=ADXDB-GUID-55FE9CED-5B25-4DA2-9F9E-921DF8276EB8) for more information on the `XMLSERIALIZE` function.

#### Desupported Features

Some features previously described in this document are desupported in Oracle Database 12c Release 2 (12.2). See [Oracle Database Upgrade Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/sqlrf&id=UPGRD60000) for a list of desupported features.

### Changes in Oracle Database 12c Release 1 (12.1.0.2)

The following are changes in Oracle Database SQL Language Reference for Oracle Database 12c Release 1 (12.1.0.2).

#### New Features

The following features are new in this release:

- The In-Memory Column Store (IM column store) is an optional, static SGA pool that stores copies of tables and partitions in a special columnar format optimized for rapid scans.
	See the [inmemory\_table\_clause](CREATE-TABLE.md) of `CREATE` `TABLE`, the [inmemory\_clause](CREATE-TABLESPACE.md) of `CREATE` `TABLESPACE`, and the [inmemory\_table\_clause](CREATE-MATERIALIZED-VIEW.md) of `CREATE` `MATERIALIZED` `VIEW`
	See the following hints:
	- [INMEMORY Hint](Comments.md)
		- [NO\_INMEMORY Hint](Comments.md)
		- [INMEMORY\_PRUNING Hint](Comments.md)
		- [NO\_INMEMORY\_PRUNING Hint](Comments.md)
- Oracle Database now supports JavaScript Object Notation (JSON).
	See the following conditions:
	- [IS JSON Condition](SQL-JSON-Conditions.md)
		- [JSON\_EXISTS Condition](SQL-JSON-Conditions.md)
		- [JSON\_TEXTCONTAINS Condition](SQL-JSON-Conditions.md)
	See the following functions:
	- [JSON\_QUERY](JSON_QUERY.md)
		- [JSON\_TABLE](JSON_TABLE.md)
		- [JSON\_VALUE](JSON_VALUE.md)
	See " [JSON Object Access Expressions](JSON-Object-Access-Expressions.md) "
- Attribute clustering lets you cluster table data in close physical proximity based on the content of specified columns.
	See the [attribute\_clustering\_clause](CREATE-TABLE.md) of `CREATE` `TABLE` and the [attribute\_clustering\_clause](ALTER-TABLE.md) of `ALTER` `TABLE`
	See the following hints:
	- [CLUSTERING Hint](Comments.md)
		- [NO\_CLUSTERING Hint](Comments.md)
- Zone maps let you reduce the I/O and CPU costs of table scans by tracking the sets of contiguous data blocks, or zones, in which certain column values are stored. You can use zone maps with or without attribute clustering.
	See the statements [CREATE MATERIALIZED ZONEMAP](CREATE-MATERIALIZED-ZONEMAP.md), [ALTER MATERIALIZED ZONEMAP](ALTER-MATERIALIZED-ZONEMAP.md), and [DROP MATERIALIZED ZONEMAP](DROP-MATERIALIZED-ZONEMAP.md), and the [zonemap\_clause](CREATE-TABLE.md) of `CREATE` `TABLE`
	See the [NO\_ZONEMAP Hint](Comments.md) and the function [SYS\_OP\_ZONE\_ID](SYS_OP_ZONE_ID.md)
- You can now create range-partitioned hash clusters.
	See the [cluster\_range\_partitions](CREATE-CLUSTER.md) clause of `CREATE` `CLUSTER` and the [allocate\_extent\_clause](ALTER-CLUSTER.md) of `ALTER` `CLUSTER`
- The new function `APPROX_COUNT_DISTINCT` returns the approximate number of distinct values for a column. This function is an alternative to the `COUNT` function. It processes large amounts of data significantly faster than `COUNT`, with negligible deviation from the exact result.
	See [APPROX\_COUNT\_DISTINCT](APPROX_COUNT_DISTINCT.md)
- A new type of index compression called advanced index compression lets you improve compression ratios significantly while still providing efficient access to indexes.
	See the [advanced\_index\_compression](CREATE-INDEX.md) clause of `CREATE` `INDEX`
- For tables compressed with Hybrid Columnar Compression, you can now control whether row-level locking is used during DML operations.
	See the [\[NO\] ROW LEVEL LOCKING](https://docs.oracle.com/en/database/oracle/oracle-database/12.2/sqlrf/CREATE-TABLE.html#GUID-F9CE0CC3-13AE-4744-A43C-EAC7A71AAAB6__CEGEFDAC) clause of `CREATE` `TABLE`
- The database now supports force full database caching mode, which allows you to designate the entire database, including NOCACHE LOBs, as eligible for caching in the buffer cache.
	See the [\[NO\] FORCE FULL DATABASE CACHING](https://docs.oracle.com/en/database/oracle/oracle-database/12.2/sqlrf/ALTER-DATABASE.html#GUID-8069872F-E680-4511-ADD8-A4E30AF67986__BGBCFJGI) clause of `ALTER` `DATABASE`
- When you grant a database role to a user who is responsible for CBAC grants, you can now specify `WITH` `DELEGATE` `OPTION` in the `GRANT` statement to prevent giving the grantee additional privileges on the role. `WITH` `DELEGATE` `OPTION` is an alternative to `WITH` `ADMIN` `OPTION`. It enables a role to be granted to program units, but it does not permit the granting of the role to other principals or the administration of the role itself.
	See the [WITH DELEGATE OPTION](GRANT.md) clause of `GRANT`
- The new `READ` object privilege and `READ` `ANY` `TABLE` system privilege allow users to query tables, materialized views, views, and their synonyms.
	The `READ` object privilege is an alternative to the `SELECT` object privilege. In addition to querying objects, the `SELECT` object privilege allows users lock rows of a table with the `LOCK` `TABLE` and `SELECT`... `FOR` `UPDATE` statements. The `READ` object privilege only allows users to query objects. See [Table 18-2](GRANT.md) for more information.
	The `READ` `ANY` `TABLE` system privilege is an alternative to the `SELECT` `ANY` `TABLE` system privilege. In addition to querying objects, the `SELECT` `ANY` `TABLE` privilege allows users to lock rows of a table with the `SELECT`... `FOR` `UPDATE` statement. The `READ` `ANY` `TABLE` privilege only allows users to query objects. See [Table 18-1](GRANT.md) for more information.

### Changes in Oracle Database 12c Release 1 (12.1.0.1)

The following are changes in Oracle Database SQL Language Reference for Oracle Database 12c Release 1 (12.1.0.1).

#### New Features

The following features are new in this release:

Features that Introduce New SQL Statements

The following features introduce new SQL statements:

- The multitenant architecture offers the capability that enables an Oracle database to function as a multitenant container database (CDB). A CDB is an Oracle database that includes one or more pluggable databases (PDBs). A PDB is a portable collection of schemas, schema objects, and nonschema objects that appears to an Oracle client as a non-CDB. You can unplug a PDB from a CDB and plug it into a different CDB.
	See the following new statements:
	- [CREATE PLUGGABLE DATABASE](CREATE-PLUGGABLE-DATABASE.md)
		- [ALTER PLUGGABLE DATABASE](ALTER-PLUGGABLE-DATABASE.md)
		- [DROP PLUGGABLE DATABASE](DROP-PLUGGABLE-DATABASE.md)
- Unified auditing provides a full set of enhanced auditing features. It enables you to create named unified audit policies, enable or disable unified audit policies, apply users to or exclude users from policies, and set whether an audit record is created if the audited behavior fails, succeeds, or both. It also enables you to capture application context values in audit records.
	See the following new statements:
	- [CREATE AUDIT POLICY (Unified Auditing)](CREATE-AUDIT-POLICY-Unified-Auditing.md)
		- [ALTER AUDIT POLICY (Unified Auditing)](ALTER-AUDIT-POLICY-Unified-Auditing.md)
		- [DROP AUDIT POLICY (Unified Auditing)](DROP-AUDIT-POLICY-Unified-Auditing.md)
		- [AUDIT (Unified Auditing)](AUDIT-Unified-Auditing.md)
		- [NOAUDIT (Unified Auditing)](NOAUDIT-Unified-Auditing.md)
- A new unified key management interface for Transparent Data Encryption (TDE) eases key administration tasks, provides for better compliance and tracking, and improves separation of duty between the database administrator and security administrator.
	See the new [ADMINISTER KEY MANAGEMENT](ADMINISTER-KEY-MANAGEMENT.md) statement.

ALTER DATABASE Enhancements

The following features provide enhancements to the `ALTER` `DATABASE` statement:

- Storage Snapshot Optimization enables you to use a third-party storage snapshot of the database taken without backup mode for all types of recovery operations, including point-in-time recovery. The `ALTER` `DATABASE` statement has been enhanced with the new `SNAPSHOT` `TIME` clause to enable you to recover the database using such a storage snapshot.
	See the new `SNAPSHOT` `TIME` clause of the `ALTER` `DATABASE` [full\_database\_recovery](ALTER-DATABASE.md) clause.
- Move an online data file to a new location while the database is open and accessing the data file.
	See the new [move\_datafile\_clause](ALTER-DATABASE.md) of `ALTER` `DATABASE`.
- Create a control file for a Data Guard far sync instance.
	See the enhanced [controlfile\_clauses](ALTER-DATABASE.md) of `ALTER` `DATABASE`.
- Performing switchovers and failovers to a physical standby database is simplified.
	See the new `ALTER` `DATABASE` clauses [switchover\_clause](ALTER-DATABASE.md) and [failover\_clause](ALTER-DATABASE.md).
- Real-time apply is now enabled by default during Redo Apply on a physical standby database. You can disable real-time apply by specifying `USING` `ARCHIVED` `LOGFILE`.
	See the enhanced [managed\_standby\_recovery](ALTER-DATABASE.md) clause of `ALTER` `DATABASE`.

ALTER SYSTEM Enhancements

The following features provide enhancements to the `ALTER` `SYSTEM` statement:

- Relocate a client to the least loaded Oracle ASM instance.
	See the new [RELOCATE CLIENT](ALTER-SYSTEM.md) clause of `ALTER` `SYSTEM`.
- Apply one-off patches released for Oracle ASM in a rolling manner.
	See the new [rolling\_patch\_clauses](ALTER-SYSTEM.md) of `ALTER` `SYSTEM`.

AUDIT and NOAUDIT (Traditional Auditing) Enhancements

The following feature provides enhancements to the `AUDIT` and `NOAUDIT` statements for traditional auditing:

- Audit operations on a SQL translation profile.
	See the new clause [ON SQL TRANSLATION PROFILE](AUDIT-Traditional-Auditing.md) of `AUDIT`.

CREATE DISKGROUP and ALTER DISKGROUP Enhancements

The following features provide enhancements to the `CREATE` `DISKGROUP` statement, `ALTER` `DISKGROUP` statement, or both:

- Check logical data corruptions and repair them automatically in normal and high redundancy Oracle ASM disks groups.
	See the new [scrub\_clause](ALTER-DISKGROUP.md) of `ALTER` `DISKGROUP`.
- Replace a user in an Oracle ASM disk group.
	See the enhanced [user\_clauses](ALTER-DISKGROUP.md) of `ALTER` `DISKGROUP`.
- Change the permissions, owner, and user group of an Oracle ASM disk group file while it is open.
	See the enhanced `ALTER` `DISKGROUP` clauses [file\_permissions\_clause](ALTER-DISKGROUP.md) and the [file\_owner\_clause](ALTER-DISKGROUP.md).
- Replace one or more disks in an Oracle ASM disk group with a single operation.
	See the new [replace\_disk\_clause](ALTER-DISKGROUP.md) of `ALTER` `DISKGROUP`.
- Rename a disk in an Oracle ASM disk group.
	See the new [rename\_disk\_clause](ALTER-DISKGROUP.md) of `ALTER` `DISKGROUP`.
- The following are new Oracle ASM disk group attributes:
	- `CONTENT`.`CHECK` allows you to enable or disable content checking when performing data copy operations for rebalancing a disk group.
		- `FAILGROUP_REPAIR_TIME` allows you to specify a default repair time for the failure groups in the disk group.
		- `PHYS_META_REPLICATED` allows you to track the replication status of a disk group.
		- `THIN_PROVISIONED` allows you to enable or disable the functionality to discard unused storage space after a disk group rebalance is completed.
	See [Table 13-2](CREATE-DISKGROUP.md).

CREATE FLASHBACK ARCHIVE and ALTER FLASHBACK ARCHIVE Enhancements

The following feature provides enhancements to the `CREATE` `FLASHBACK` `ARCHIVE` and `ALTER` `FLASHBACK` `ARCHIVE` statements:

- Instruct the database to optimize the storage of data in history tables.
	See the new clause [\[NO\] OPTIMIZE DATA](https://docs.oracle.com/en/database/oracle/oracle-database/12.2/sqlrf/CREATE-FLASHBACK-ARCHIVE.html#GUID-9E821EC5-8350-4729-85FE-2188EBB4139B__BGEIBJJB) of `CREATE` `FLASHBACK` `ARCHIVE` and the new clause [\[NO\] OPTIMIZE DATA](https://docs.oracle.com/en/database/oracle/oracle-database/12.2/sqlrf/ALTER-FLASHBACK-ARCHIVE.html#GUID-285814C9-06ED-4BDB-BB19-E2BA6505C850__BGEDFAJC) of `ALTER` `FLASHBACK` `ARCHVE`.

CREATE INDEX and ALTER INDEX Enhancements

The following features provide enhancements to the `CREATE` `INDEX` statement, `ALTER` `INDEX` statement, or both:

- Create partial indexes on a subset of the partitions of a table.
	See the new [partial\_index\_clause](CREATE-INDEX.md) of `CREATE` `INDEX`.
- Remove orphaned index entries for records that were previously dropped or truncated by a table partition maintenance operation.
	See the new keyword [CLEANUP](ALTER-INDEX.md) of `ALTER` `INDEX`... `COALESCE` and the new keyword [CLEANUP](ALTER-INDEX.md) of `ALTER` `INDEX`... `MODIFY` `PARTITION`... `COALESCE`.
- Create multiple indexes on the same set of columns, column expressions, or both if the indexes are of different types, use different partitioning, or have different uniqueness properties.
	See the [index\_expr](CREATE-INDEX.md) clause of `CREATE` `INDEX`.

CREATE INDEXTYPE and ALTER INDEXTYPE Enhancements

The following feature provides enhancements to the `CREATE` `INDEXTYPE` and `ALTER` `INDEXTYPE` statements:

- Create domain indexes on hash- and interval-partitioned tables.
	See [CREATE INDEXTYPE](CREATE-INDEXTYPE.md) and [ALTER INDEXTYPE](ALTER-INDEXTYPE.md).

CREATE MATERIALIZED VIEW and ALTER MATERIALIZED VIEW Enhancements

The following feature provides enhancements to the `CREATE` `MATERIALIZED` `VIEW` and `ALTER` `MATERIALIZED` `VIEW` statements:

- Materialized views, which are noneditioned objects, can depend on editioned objects.
	See:
	- The new clauses [evaluation\_edition\_clause](CREATE-MATERIALIZED-VIEW.md) and [unusable\_editions\_clause](CREATE-MATERIALIZED-VIEW.md) of `CREATE` `MATERIALIZED` `VIEW`
		- The new clauses [evaluation\_edition\_clause](ALTER-MATERIALIZED-VIEW.md) and [unusable\_editions\_clause](ALTER-MATERIALIZED-VIEW.md) of `ALTER` `MATERIALIZEED` `VIEW`

CREATE MATERIALIZED VIEW LOG and ALTER MATERIALIZED VIEW LOG Enhancements

The following feature provides enhancements to the `CREATE` `MATERIALIZED` `VIEW` `LOG` and `ALTER` `MATERIALIZED` `VIEW` `LOG` statements:

- Specify the refresh method for which a materialized view log will be used. You can specify synchronous refresh, which is introduced in Oracle Database 12c, or fast refresh, which is also available in earlier releases.
	See:
	- The new [for\_refresh\_clause](CREATE-MATERIALIZED-VIEW-LOG.md) of `CREATE` `MATERIALIZED` `VIEW` `LOG`
		- The new [for\_refresh\_clause](ALTER-MATERIALIZED-VIEW-LOG.md) of `ALTER` `MATERIALIZED` `VIEW` `LOG`

CREATE SEQUENCE and ALTER SEQUENCE Enhancements

The following features provide enhancements to the `CREATE` `SEQUENCE` and `ALTER` `SEQUENCE` statements:

- Control whether the sequence pseudocolumn `NEXTVAL` retains its original value during replay for Application Continuity.
	See:
	- The new clauses [KEEP](CREATE-SEQUENCE.md) and [NOKEEP](CREATE-SEQUENCE.md) of `CREATE` `SEQUENCE`
		- The new clauses `KEEP` and `NOKEEP` of [ALTER SEQUENCE](ALTER-SEQUENCE.md)
- Create a session sequence, which is a special type of sequence that is specifically designed to be used with global temporary tables that have session visibility.
	See:
	- The new clauses [SESSION](CREATE-SEQUENCE.md) and [GLOBAL](CREATE-SEQUENCE.md) of `CREATE` `SEQUENCE`
		- The new clauses `SESSION` and `GLOBAL` of [ALTER SEQUENCE](ALTER-SEQUENCE.md)

CREATE TABLE and ALTER TABLE Enhancements

The following features provide enhancements to the `CREATE` `TABLE` statement, `ALTER` `TABLE` statement, or both:

- The maximum size for the `VARCHAR2`, `NVARCHAR2`, and `RAW` data types is increased to 32767 bytes.
	See " [Extended Data Types](Data-Types.md) ".
- Temporal Validity support enables you to associate a valid time dimension with a table. You can use Oracle Flashback Query to retrieve rows from that table based on whether they are considered valid as of a specified time or during a specified time period.
	See:
	- The new `CREATE` `TABLE` clause [period\_definition](CREATE-TABLE.md)
		- The new `ALTER` `TABLE` clauses [add\_period\_clause](ALTER-TABLE.md) and [drop\_period\_clause](ALTER-TABLE.md)
		- The enhanced `SELECT` [flashback\_query\_clause](SELECT.md)
- Virtual columns, which are noneditioned objects, can depend on editioned objects.
	See:
	- The new clauses [evaluation\_edition\_clause](CREATE-TABLE.md) and [unusable\_editions\_clause](CREATE-TABLE.md) of `CREATE` `TABLE`
		- The new clause [modify\_virtcol\_properties](ALTER-TABLE.md) of `ALTER` `TABLE`
- Performance has been improved when you specify a `DEFAULT` value for a nullable column.
	See the [DEFAULT](ALTER-TABLE.md) clause of `ALTER` `TABLE`.
- Specify a default column value that includes the sequence pseudocolumns `CURRVAL` and `NEXTVAL`.
	See:
	- The [DEFAULT](CREATE-TABLE.md) clause of `CREATE` `TABLE`
		- The [DEFAULT](ALTER-TABLE.md) clause of `ALTER` `TABLE`
- The `DEFAULT` clause has the new clause `ON` `NULL`, which instructs the database to assign a specified default column value when an `INSERT` statement attempts to assign a value that evaluates to NULL.
	See:
	- The [ON NULL](CREATE-TABLE.md) clause of `CREATE` `TABLE`
		- The [ON NULL](ALTER-TABLE.md) clause of `ALTER` `TABLE`
- Specify an identity column, which is assigned an increasing or decreasing integer value from a sequence generator.
	See:
	- The new clauses [identity\_clause](CREATE-TABLE.md) of `CREATE` `TABLE` and [identity\_options](CREATE-TABLE.md) of `CREATE` `TABLE`
		- The new clauses [identity\_clause](ALTER-TABLE.md) of `ALTER` `TABLE` and [identity\_options](ALTER-TABLE.md) of `ALTER` `TABLE`
- Hide and unhide columns in tables.
	See:
	- The new clauses [VISIBLE | INVISIBLE](CREATE-TABLE.md) of `CREATE` `TABLE`
		- The new clauses [VISIBLE | INVISIBLE](CREATE-TABLE.md) of `CREATE` `TABLE` for virtual columns
		- The new clause [modify\_col\_visibility](ALTER-TABLE.md) of `ALTER` `TABLE`
- Recursively cascade a truncate operation to child tables.
	See the new keyword [CASCADE](ALTER-TABLE.md) of the clause `truncate_partition_subpart` of `ALTER` `TABLE`.
- Recursively cascade an exchange operation to child tables.
	See the new keyword [CASCADE](ALTER-TABLE.md) of the clause `exchange_partition_subpart` of `ALTER` `TABLE`.
- Store `XMLType` data, and abstract data types that contain attributes of type `XMLType`, `CLOB`, `BLOB`, or `NCLOB`, in an `ANYDATA` column.
	See the new clause [modify\_opaque\_type](ALTER-TABLE.md) of `ALTER` `TABLE`.
- Enable a table for row archival for In-Database Archiving.
	See the new [ROW ARCHIVAL](CREATE-TABLE.md) clause of `CREATE` `TABLE`.
- Manage policies for Automatic Data Optimization.
	See the new [ilm\_clause](CREATE-TABLE.md) of `CREATE` `TABLE` and the new [ilm\_clause](ALTER-TABLE.md) of `ALTER` `TABLE`.
- Create a reference-partitioned child table whose parent is an interval-partitioned table.
	See the enhanced clause [reference\_partitioning](CREATE-TABLE.md) of `CREATE` `TABLE`.
- Specify multiple table partitions or table subpartitions for the following `ALTER` `TABLE` operations:
	- Add one or more range, list, or system partitions to a table. See [add\_table\_partition](ALTER-TABLE.md).
		- Add one or more range subpartitions to a partition. See [add\_range\_subpartition](ALTER-TABLE.md).
		- Add one or more list subpartitions to a partition. See [add\_list\_subpartition](ALTER-TABLE.md).
		- Split one range or list partition into two or more partitions. See [split\_table\_partition](ALTER-TABLE.md).
		- Split one range or list subpartition into two or more subpartitions. See [split\_table\_subpartition](ALTER-TABLE.md).
		- Merge two or more range, list, or system partitions into one new partition. See [merge\_table\_partitions](ALTER-TABLE.md).
		- Merge two or more range or list subpartitions into one new subpartition. See [merge\_table\_subpartitions](ALTER-TABLE.md).
		- Truncate one or more partitions or subpartitions. See [truncate\_partition\_subpart](ALTER-TABLE.md).
		- Drop one or more partitions. See [drop\_table\_partition](ALTER-TABLE.md).
		- Drop one or more subpartitions. See [drop\_table\_subpartition](ALTER-TABLE.md).
- In earlier releases, the following DDL operations required a DML-blocking lock. You can use the new `ONLINE` keyword to allow the execution of DML statements during the following DDL operations:
	- Dropping an index (using `DROP` `INDEX`... [ONLINE](DROP-INDEX.md)...)
		- Marking an index as `UNUSABLE` (using `ALTER` `INDEX`... `UNUSABLE` [ONLINE](ALTER-INDEX.md))
		- Marking a column as `UNUSED` (using `ALTER` `TABLE`... `SET` `UNUSED`... [ONLINE](ALTER-TABLE.md)...)
		- Dropping a constraint (using `ALTER` `TABLE`... `DROP`... [ONLINE](ALTER-TABLE.md)...)
		- Moving a table partition (using `ALTER` `TABLE`... `MOVE` `PARTITION`... [ONLINE](ALTER-TABLE.md))
		- Moving a table subpartition (using `ALTER` `TABLE`... `MOVE` `SUBPARTITION`... [ONLINE](ALTER-TABLE.md))

CREATE VIEW Enhancements

The following features provide enhancements to the `CREATE` `VIEW` statement:

- Hide and unhide columns in views.
	See the new clause [VISIBLE | INVISIBLE](CREATE-VIEW.md) of `CREATE` `VIEW`.
- Specify whether functions referenced in the view are executed using the view invoker's rights or the view definer's rights.
	See the new clause [BEQUEATH](CREATE-VIEW.md) of `CREATE` `VIEW`.

GRANT and REVOKE Enhancements

The following features provide enhancements to the `GRANT` and `REVOKE` statements:

- Grant object privileges on a user to users and roles.
	See:
	- The new clause [ON USER](GRANT.md) of `GRANT`
		- The new clause [ON USER](REVOKE.md) of `REVOKE`
- Grant object privileges on a SQL translation profile to users and roles.
	See:
	- The new clause [ON SQL TRANSLATION PROFILE](GRANT.md) of `GRANT`
		- The new clause [ON SQL TRANSLATION PROFILE](REVOKE.md) of `REVOKE`
- Grant code based access control (CBAC) roles to program units.
	See:
	- The new clause [grant\_roles\_to\_programs](GRANT.md) of `GRANT`
		- The new clause [revoke\_roles\_from\_programs](REVOKE.md) of `REVOKE`

SELECT Enhancements

The following features provide enhancements to the `SELECT` statement:

- Pattern matching enables you to recognize patterns found across multiple rows in a table.
	See the new [row\_pattern\_clause](SELECT.md) of `SELECT`.
- Perform top-N queries by specifying an offset, and the number of rows or percentage of rows to return.
	See the new [row\_limiting\_clause](SELECT.md) of `SELECT`.
- In a query that performs outer joins of more than two pairs of tables, a single table can now be the null-generated table for multiple tables.
	See " [Outer Joins](Joins.md) ".
- Perform a variation of an ANSI `CROSS` `JOIN` or an ANSI `LEFT` `OUTER` `JOIN` with left correlation support. You can specify a table reference or collection expression on the right side of the join clause.
	See the new [cross\_outer\_apply\_clause](SELECT.md) of `SELECT`.
- Specify a lateral inline view in a query expression.
	See the new keyword [LATERAL](SELECT.md) of `SELECT`.
- Declare and define PL/SQL functions and procedures in the `WITH` clause of a query. You can then reference the PL/SQL functions in the query and its subqueries.
	See the new clause [plsql\_declarations](SELECT.md) on `SELECT`.

TRUNCATE TABLE Enhancements

The following feature provides enhancements to the `TRUNCATE` `TABLE` statement:

- Recursively truncate child tables.
	See the new clause [CASCADE](TRUNCATE-TABLE.md) of `TRUNCATE` `TABLE`.

New or Enhanced Functions

The following are new or enhanced functions:

- [CLUSTER\_DETAILS](CLUSTER_DETAILS.md) is a new function that predicts cluster membership for each row. It can use a pre-defined clustering model or perform dynamic clustering. The function returns an XML string that describes the predicted cluster or a specified cluster.
- [CLUSTER\_DISTANCE](CLUSTER_DISTANCE.md) is a new function that predicts cluster membership for each row. It can use a pre-defined clustering model or perform dynamic clustering. The function returns the raw distance between each row and the centroid of either the predicted cluster or a specified.
- [CLUSTER\_ID](CLUSTER_ID.md) has been enhanced so that it can either use a pre-defined clustering model or perform dynamic clustering.
- [CLUSTER\_PROBABILITY](CLUSTER_PROBABILITY.md) has been enhanced so that it can either use a pre-defined clustering model or perform dynamic clustering. The data type of the return value has been changed from `NUMBER` to `BINARY_DOUBLE`.
- [CLUSTER\_SET](CLUSTER_SET.md) has been enhanced so that it can either use a pre-defined clustering model or perform dynamic clustering. The data type of the returned probability has been changed from `NUMBER` to `BINARY_DOUBLE`
- [FEATURE\_DETAILS](FEATURE_DETAILS.md) is a new function that predicts feature matches for each row. It can use a pre-defined feature extraction model or perform dynamic feature extraction. The function returns an XML string that describes the predicted feature or a specified feature.
- [FEATURE\_ID](FEATURE_ID.md) has been enhanced so that it can either use a pre-defined feature extraction model or perform dynamic feature extraction.
- [FEATURE\_SET](FEATURE_SET.md) has been enhanced so that it can either use a pre-defined feature extraction model or perform dynamic feature extraction. The data type of the returned probability has been changed from `NUMBER` to `BINARY_DOUBLE`.
- [FEATURE\_VALUE](FEATURE_VALUE.md) has been enhanced so that it can either use a pre-defined feature extraction model or perform dynamic feature extraction. The data type of the return value has been changed from `NUMBER` to `BINARY_DOUBLE`.
- [ORA\_INVOKING\_USER](ORA_INVOKING_USER.md) is a new function that returns the name of the database user who invoked the current statement or view. This function takes into account the `BEQUEATH` property of intervening views referenced in the statement.
- [ORA\_INVOKING\_USERID](ORA_INVOKING_USERID.md) is a new function that returns the identifier of the database user who invoked the current statement or view. This function takes into account the `BEQUEATH` property of intervening views referenced in the statement.
- [PREDICTION](PREDICTION.md) has been enhanced so that it can either use a pre-defined predictive model or perform dynamic prediction.
- [PREDICTION\_BOUNDS](PREDICTION_BOUNDS.md) now returns the upper and lower bounds of the prediction as the `BINARY_DOUBLE` data type. It previously returned these values as the `NUMBER` data type.
- [PREDICTION\_COST](PREDICTION_COST.md) has been enhanced so that it can either use a pre-defined predictive model or perform dynamic prediction. The data type of the returned cost has been changed from `NUMBER` to `BINARY_DOUBLE`.
- [PREDICTION\_DETAILS](PREDICTION_DETAILS.md) has been enhanced so that it can either use a pre-defined predictive model or perform dynamic prediction.
- [PREDICTION\_PROBABILITY](PREDICTION_PROBABILITY.md) has been enhanced so that it can either use a pre-defined predictive model or perform dynamic prediction. The data type of the returned probability has been changed from `NUMBER` to `BINARY_DOUBLE`.
- [PREDICTION\_SET](PREDICTION_SET.md) has been enhanced so that it can either use a pre-defined predictive model or perform dynamic prediction. The data type of the returned probability has been changed from `NUMBER` to `BINARY_DOUBLE`.
- [STANDARD\_HASH](STANDARD_HASH.md) is a new function that computes a hash value for a given expression using one of several standardized hash algorithms.
- [SYS\_CONTEXT](SYS_CONTEXT.md) enables you to query a new built-in namespace, `SYS_SESSION_ROLES`, which allows you to determine if a specified role is currently enabled for the session.

New or Enhanced Privileges

The following are new or enhanced system privileges and object privileges:

- The behavior has changed for the following system privilege, which is listed in [Table 18-1](GRANT.md):
	- `SELECT` `ANY` `DICTIONARY` now does not allow you to query the following objects in the `SYS` schema: `DEFAULT_PWD$`, `ENC$`, `LINK$`, `USER$`, `USER_HISTORY$`, and `XS$VERIFIERS`.
- The following new system privileges are listed in [Table 18-1](GRANT.md):
	- `CREATE` `SQL` `TRANSLATION` `PROFILE`, `CREATE` `ANY` `SQL` `TRANSLATION` `PROFILE`, `ALTER` `ANY` `SQL` `TRANSLATION` `PROFILE`, `USE` `ANY` `SQL` `TRANSLATION` `PROFILE`, and `DROP` `ANY` `SQL` `TRANSLATION` `PROFILE` allow you to manage SQL translation profiles.
		- `EXEMPT` `REDACTION` `POLICY` allows you to bypass any existing Oracle Data Redaction policies.
		- `INHERIT` `ANY` `PRIVILEGES` allows you to execute invoker's rights procedures with the privileges of the invoker.
		- `KEEP` `DATE` `TIME` allows the `SYSDATE` and `SYSTIMESTAMP` functions to return their original values during replay for Application Continuity.
		- `KEEP` `SYSGUID` allows the `SYS_GUID` function to return its original value during replay for Application Continuity.
		- `LOGMINING` allows you to perform LogMiner operations in a multitenant container database (CDB).
		- `PURGE` `DBA_RECYCLEBIN` allows you to remove all objects from the system-wide recycle bin.
		- `SYSBACKUP` allows you to perform backup and recovery tasks.
		- `SYSDG` allows you to manage Oracle Data Guard.
		- `SYSKM` allows you to perform encryption key management.
		- `TRANSLATE` `ANY` `SQL` allows you to translate SQL for any user.
- The following new object privileges are listed in [Table 18-2](GRANT.md):
	- The `ALTER` and `USE` privileges authorize operations on SQL translation profiles.
		- `INHERIT` `PRIVILEGES` is a new type of object privilege that can be granted on a user to users and roles. It allows invoker's rights procedures owned by the grantee to be executed with the privileges of the invoker when the invoker is the user on whom this privilege is granted.
		- `KEEP` `SEQUENCE` allows the sequence pseudocolumn `NEXTVAL` to retain its original value during replay for Application Continuity.
		- `TRANSLATE` `SQL` is a new type of object privilege that can be granted on a user to users and roles. It allows the grantee to translate SQL through the grantee's SQL translation profile for the user on whom this privilege is granted.

New Hints

The following are new hints:

- The [GATHER\_OPTIMIZER\_STATISTICS Hint](Comments.md) and [NO\_GATHER\_OPTIMIZER\_STATISTICS Hint](Comments.md) allow you to enable and disable statistics gathering during bulk loads.
- The [PQ\_CONCURRENT\_UNION Hint](Comments.md) and [NO\_PQ\_CONCURRENT\_UNION Hint](Comments.md) allow you to enable and disable concurrent processing of `UNION` and `UNION` `ALL` operations.
- The [PQ\_FILTER Hint](Comments.md) allows you to instruct the optimizer on how to process rows when filtering correlated subqueries.
- The [PQ\_SKEW Hint](Comments.md) and [NO\_PQ\_SKEW Hint](Comments.md) allow you to advise the optimizer of whether the distribution of the values of the join keys for a parallel join is skewed.
- The [USE\_CUBE Hint](Comments.md) and [NO\_USE\_CUBE Hint](Comments.md) allow you to specify whether to use or exclude cube joins.

#### Deprecated Features

The following features are deprecated in this release, and may be desupported in a future release:

- Stored outlines are deprecated. They are still supported for backward compatibility. However, Oracle recommends that you use SQL plan management instead. SQL plan management creates SQL plan baselines, which offer superior SQL performance stability compared with stored outlines.
	See [Oracle Database SQL Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/sqlrf&id=TGSQL615) for more information about SQL plan management.
- The use of PKI encryption with Transparent Data Encryption is deprecated. To configure Transparent Data Encryption, use the [ADMINISTER KEY MANAGEMENT](ADMINISTER-KEY-MANAGEMENT.md) statement.
	See [Oracle Database Advanced Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/sqlrf&id=ASOAG600) for more information.

#### Desupported Features

Some features previously described in this document are desupported in Oracle Database 12c Release 1 (12.1). See [Oracle Database Upgrade Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/sqlrf&id=UPGRD60000) for a list of desupported features.