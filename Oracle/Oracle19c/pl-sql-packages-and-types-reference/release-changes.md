---
title: Changes in This Release for Oracle Database PL/SQL Packages and Types Reference
book: PL/SQL Packages and Types Reference
doc_id: E96430-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/arpls/release-changes.html
tags:
  - oracle
  - 19c
  - pl-sql-packages-and-types-reference
---

This preface contains:

- Changes in Oracle Database Release 19c, Version 19.1

### Changes in Oracle Database Release 19c, Version 19.1

The following are changes in *Oracle Database PL/SQL Packages and Types Reference* for Oracle Database release 19c, version 19.1.

See [*Oracle Database New Features Guide*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=NEWFT) for a complete list of new features in this release.

### New Features

This section lists the major new features in Oracle Database release 19c *PL/SQL Packages and Types Reference*.

The following features are new in Oracle Database release 19c, version 19.1:

- `ANYTYPE TYPE`
	The `GETANYTYPEFROMPERSISTENT` function replaces `GETPERISTENT` static function.
	See [GETANYTYPEFROMPERSISTENT Function](ANYTYPE-TYPE.md)
- `DBMS_ADDM`
	Automatic Database Diagnostic Monitor (ADDM) support for pluggable databases (PDBs). You can now use ADDM to analyze AWR data in PDBs for identifying and resolving performance related issues. Two new parameters, `CDB_TYPE_OVERRIDE` and `READ_ONLY_TYPE_OVERRIDE` added to the following subprograms to the `DBMS_ADDM` package:
	- `ANALYZE_DB` Procedure
		- `ANALYZE_INST` Procedure
		- `ANALYZE_PARTIAL` Procedure
		- `COMPARE_CAPTURE_REPL AY_REPORT` Function
		- `COMPARE_DATABASES` Function
		- `COMPARE_INSTANCES` Function
		- `COMPARE_REPLAY_REPLA Y_REPORT` Function
		- `REAL_TIME_ADDM_REPORT` Function
- `DBMS_AUTO_INDEX`
	The new package `DBMS_AUTO_INDEX` provides an interface for configuring auto indexes and generating reports containing the details of the executed automatic indexing operations in a database.
	See “ [DBMS\_AUTO\_INDEX](DBMS_AUTO_INDEX.md) ”
- `DBMS_CREDENTIAL`
	You can also use the DBMS\_CREDENTIAL.CREATE\_CREDENTIAL procedure to manage the credentials for cloud object storage. The credential parameter of `impdb` specifies the name of a credential object that contains the user name and password required to access an object store bucket. You can also specify a default credential using the database property `DEFAULT_CREDENTIAL`.
- `DBMS_HADOOP`
	Oracle Database now supports hybrid partitioned tables. A hybrid partitioned table is a partitioned table in which some partitions reside in the database and some partitions reside outside the database in external files, such as operating system files or Hadoop Distributed File System (HDFS) files.
	A new procedure `CREATE_HYBRID_PARTNED_TABLE` is added to the `DBMS_HADOOP` package.
- `DBMS_INMEMORY_ADMIN`
	A new function `POPULATE_WAIT` is added to `DBMS_INMEMORY_ADMIN` package. This function ensures that the specified In-Memory objects have been populated before allowing application access.
- `DBMS_MEMOPTIMIZE`
	The following new subprograms are added to the `DBMS_MEMOPTIMIZE` package as part of the Memoptimized Rowstore fast ingest feature:
	- `GET_APPLY_HWM_SEQID`
		- `GET_WRITE_HWM_SEQID`
		- `WRITE_END`
	See “ [DBMS\_MEMOPTIMIZE](DBMS_MEMOPTIMIZE.md) ”

`DBMS_MEMOPTIMIZE_ADMIN`

The new package `DBMS_MEMOPTIMIZE_ADMIN` provides an interface for flushing the Memoptimized Rowstore data buffered in the large pool to disk.

See “ [DBMS\_MEMOPTIMIZE\_ADMIN](DBMS_MEMOPTIMIZE_ADMIN.md) ”

- `DBMS_METADATA`
	The following new transform parameters which are used by the metadata layer of datapump are added to the `DBMS_METADATA.SET_TRANSFORM_PARAM` procedure:
	- `OMIT_ENCRYPTION_CLAUSE`
		- `DWCS_CVT_IOTS`
		- `DWCS_CVT_CONSTRAINTS`
		- `CONSTRAINT_USE_DEFAULT_INDEXES`
		- `CONSTRAINT_NAME_FROM_INDEXES`
- `DBMS_MVIEW`
	Oracle Database now supports hybrid partitioned tables. A hybrid partitioned table is a partitioned table in which some partitions reside in the database and some partitions reside outside the database in external files, such as operating system files or Hadoop Distributed File System (HDFS) files.
	A new parameter, `SKIP_EXT_DATA`, is added to the `DBMS_MVIEW.REFRESH` procedure.

`DBMS_SQLQ`

The new package `DBMS_SQLQ` provides an interface for configuring quarantine thresholds for SQL statements and their execution plans. The SQL statements that cross the quarantine thresholds are quarantined and are not allowed to run again in a database.

See “ [DBMS\_SQLQ](DBMS_SQLQ.md) ”

- `DBMS_SQLDIAG` New SQL Repair Advisor function `DBMS_SQLDIAG.SQL_DIAGNOSE_AND_REPAIR`
	The new SQL Repair Advisor function `DBMS_SQLDIAG.SQL_DIAGNOSE_AND_REPAIR` creates a diagnostic task, executes it, and accepts SQL patch recommendation for a SQL statement that is generating a critical error. This function helps users to diagnose and fix problems.
- `DBMS_SODA`
	DBMS\_SODA is a PL/SQL package implementing Simple Oracle Document Access (SODA) which allows you to use the Oracle Database as a NoSQL document store. Additional functions and features are added in this release.
- `DBMS_STATS`
	A new boolean parameter `REALTIME_STATS` is added to `GET_TABLE_STATS` and `GET_COLUMN_STATS` procedures.
- `DBMS_XPLAN`
	New `COMPARE_PLANS` function added to the `DBMS_XPLAN` package. This function compares each plan in a list with a reference plan and returns the report.
- Key-based Messaging
	The following new parameters are added to the `GET_QUEUE_PARAMETER`, `SET_QUEUE_PARAMETER`, and `UNSET_QUEUE_PARAMETER` procedures of the `DBMS_AQADM` package as part of the Key-based messaging feature:
	- Sharded queue parameters
		- `SHARD_NUM`
				- `KEY_BASED_ENQUEUE`
				- `STICKY_DEQUEUE`
		- Key-based parameters
		- `AQ$KEY_TO_SHARD_MAP`
				- `AQ$GET_KEY_SHARD_INST`
	See “ [DBMS\_AQADM](DBMS_AQADM.md) ”

**Changes in Oracle Database Release 19c, Version 19.9**

The following features are new in Oracle Database release 19c, version 19.9:

- Support for `DBMS_CRYPTO` Asymmetric Key Operations
	Starting with this release, the `DBMS_CRYPTO` PL/SQL package supports asymmetric key operations, in addition to the existing support for symmetric key operations. To implement the support for asymmetric key operations, the following procedures have been added to the `DBMS_CRYPTO` package:
	- `PKENCRYPT`
		- `PKDECRYPT`
		- `SIGN`
		- `VERIFY`
	See [DBMS\_CRYPTO](DBMS_CRYPTO.md).

**Changes in Oracle Database Release 19c, Version 19.10**

The following features are new in Oracle Database release 19c, version 19.10:

- `DBMS_CLOUD`
	The `DBMS_CLOUD` package provides a comprehensive support for working with data in Object Storage.
- Blockchain tables are append-only tables in which only insert operations are allowed. Deleting rows is either prohibited or restricted based on time. Rows in a blockchain table are made tamper-resistant by special sequencing & chaining algorithms. Users can verify that rows have not been tampered. A hash value that is part of the row metadata is used to chain and validate rows. Blockchain tables enable you to implement a centralized ledger model where all participants in the blockchain network have access to the same tamper-resistant ledger. The following new packages are available in this release:
	- `DBMS_BLOCKCHAIN_TABLE`
		- `DBMS_USER_CERTS`
- `DBMS_LOGMNR` subprograms `ADD_LOGFILE Procedure` and `START_LOGMNR Procedure` modified to support per-PDB Capture for Oracle Autonomous Database.

**Changes in Oracle Database Release 19c, Version 19.11**

The following features are new in Oracle Database release 19c, version 19.11:

- `DBMS_IMMUTABLE_TABLE`
	Immutable tables are `read-only` tables that protect data against unauthorized modification. They also prevent against accidental data modifications that may be caused by human errors. The `DBMS_IMMUTABLE_TABLE` package allows you to delete the expired rows in an immutable table.
- New subprograms are added to `DBMS_SODA` and `SODA Types`.
- A new procedure, `ACCHK_VIEWS`, is added to the `DBMS_APP_CONT_ADMIN` package. This procedure is available for the 19c release only.

### Deprecated Features

List of deprecated features in Oracle Database release 19c version 19.1 *PL/SQL Packages and Types Reference*.

`DBMS_SESSION.IS_ROLE_ENABLED` function is deprecated.

Use `DBMS_SESSION.CURRENT_IS_ROLE_ENABLED` or `DBMS_SESSION.SESSION_IS_ROLE_ENABLED` function instead.

Starting with Oracle Database 19c, customer use of the `SERVICE_NAMES` parameter is deprecated. It can be desupported in a future release.

The use of the `SERVICE_NAMES` parameter is no longer actively supported. It must not be used for high availability (HA) deployments. It is not supported to use service names parameter for any HA operations. This restriction includes FAN, load balancing, `FAILOVER_TYPE`, `FAILOVER_RESTORE`, `SESSION_STATE_CONSISTENCY`, and any other uses.

To manage your services, Oracle recommends that you use the `SRVCTL` or `GDSCTL` command line utilities, or the `DBMS_SERVICE` package.

### Desupported Features

This section lists the desupported features in Oracle Database release 19c version 19.1 *PL/SQL Packages and Types Reference*.

The following features are desupported in this release:

- The ability to create flat file dictionary dumps of pluggable databases (PDBs) is desupported in Oracle Database 19c.
	In previous releases, using a flat file dictionary was one means of mining the redo logs for the changes associated with a specific PDB whose data dictionary was contained within the flat file. This feature is now desupported. With Oracle Database 19c and later releases, Oracle recommends that you call `DBMS_LOGMNR.START_LOGMNR`, and supply the system change number (SCN) or time range that you want to mine. The SCN or time range options of `START_LOGMNR` are enhanced to support mining of individual PDBs.
- Desupport of `CONTINUOUS_MINE` option
	The `continuous_mine` option for the `DBMS_LOGMNR.START_LOGMNR` package is desupported in Oracle Database 19c, and is no longer available. The `CONTINUOUS_MINE` functionality of the `LogMiner` package is obsolete. It was deprecated in Oracle Database 12c Release 2 (12.2). There is no replacement functionality.
	Desupport of `Oracle Streams`
	Starting in Oracle Database 19c, the Oracle Streams feature is desupported. Use Oracle GoldenGate to replace all replication features of Oracle Streams.
- `Oracle Multimedia`
	Starting in Oracle Database 19c, the Oracle Multimedia feature is desupported. Use Oracle SecureFiles with open source or third-party products for metadata extraction and for image processing and conversion instead of Oracle Multimedia.
	**See Also:** For more information, see [*Oracle Database Upgrade Guide*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=UPGRD-GUID-FA024F34-A61A-4C4B-AA60-C123A9191A16)
- MAX\_CONNECTIONS attribute of LOG\_ARCHIVE\_DEST\_n Desupported
	The MAX\_CONNECTIONS attribute of the LOG\_ARCHIVE\_DEST\_n parameters for Oracle Data Guard Redo Transport is obsolete. It is desupported in Oracle Database 19c.
	The MAX\_CONNECTIONS attribute can interfere with the new Redo Transport Streaming mechanism introduced in Oracle Database 11g, and increase the time necessary to resolve gaps. To prevent these types of errors, Oracle has desupported and removed this attribute.
- `Desupport of Extended Datatype Support (EDS)`
	The Extended Datatype Support (EDS) feature is desupported in Oracle Database 19c. All Data types that the EDS feature supported are now supported natively by both Logical Standby and Oracle GoldenGate.
	The Extended Datatype Support (EDS) feature provides a mechanism for logical standbys to support certain Oracle data types that lack native redo-based support. For example, EDS was used to replicate tables with a SDO\_GEOMETRY column. However, starting with Oracle Database 12c Release 2 (12.2), there are no EDS-supported Oracle data types that are not supported natively, either by Logical standby, or by Oracle GoldenGate. This feature is desupported with Oracle Database 19c (19.1).
- The initialization parameter `O7_DICTIONARY_ACCESSIBILITY` is desupported in Oracle Database 19c.
	The `O7_DICTIONARY_ACCESSIBILITY` parameter controlled restrictions on System Privileges from accessing `SYS` owned objects. It was retained to enable certain backward compatibility for earlier release applications. Desupporting obsolete features enables Oracle to focus on security across all features and functionality. Oracle recommends that you manage system privileges in accordance with standard security best practices.