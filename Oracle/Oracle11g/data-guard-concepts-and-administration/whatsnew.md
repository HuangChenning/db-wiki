---
title: "What's New in Oracle Data Guard?"
book: Data Guard Concepts and Administration
doc_id: E41134-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e41134/whatsnew.htm
tags:
  - oracle
  - 11g
  - data-guard-concepts-and-administration
---

The features and enhancements described in this preface were added to Oracle Data Guard in Oracle Database 11g.

## Oracle Database 11g Release 2 (11.2.0.3) New Features in Oracle Data Guard

The following new features are specific to SQL Apply in Oracle Data Guard 11g Release 2 (11.2.0.3):

- Support for `XMLType` data stored as binary XML
- Support for `XMLType` data stored in object-relational format

Support for both these storage formats requires that the primary database be running Oracle Database 11g Release 2 (11.2.0.3) or higher with a redo compatibility setting of 11.2.0.3 or higher. See ["Datatype Considerations"](data_support.md) for more information about supported data types.

## New Features in Oracle Data Guard 11.2

The following sections describe the new features and enhancements that were added in Oracle Data Guard 11g Release 2 (11.2):

New 11.2 Features Common to Redo Apply and SQL Apply

- As of Oracle Database 11g Release 2 (11.2.0.2), Oracle Data Guard is fully integrated with Oracle Real Application Clusters One Node (Oracle RAC One Node).
- A Data Guard configuration can now consist of a primary database and up to 30 standby databases.
- The `FAL_CLIENT` database initialization parameter is no longer required.
- The default archive destination used by the Oracle Automatic Storage Management (Oracle ASM) feature and the fast recovery area feature has changed from `LOG_ARCHIVE_DEST_10` to `LOG_ARCHIVE_DEST_1`.
- Redo transport compression is no longer limited to compressing redo data only when a redo gap is being resolved. When compression is enabled for a destination, all redo data sent to that destination is compressed.
- The new `ALTER SYSTEM FLUSH REDO` SQL statement can be used at failover time to flush unsent redo from a mounted primary database to a standby database, thereby allowing a zero data loss failover to be performed even if the primary database is not running in a zero data loss data protection mode. See [Section 8.2.2](role_management.md) for more information.

New 11.2 Features Specific to Redo Apply

- You can configure apply lag tolerance in a real-time query environment by using the new `STANDBY_MAX_DATA_DELAY` parameter.
- You can use the new `ALTER SESSION SYNC WITH PRIMARY` SQL statement to ensure that a suitably configured physical standby database is synchronized with the primary database as of the time the statement is issued.
- The `V$DATAGUARD_STATS` view has been enhanced to a greater degree of accuracy in many of its columns, including apply lag and transport lag.
- You can view a histogram of apply lag values on the physical standby. To do so, query the new `V$STANDBY_EVENT_HISTOGRAM` view.
- A corrupted data block in a primary database can be automatically replaced with an uncorrupted copy of that block from a physical standby database that is operating in real-time query mode. A corrupted block in a physical standby database can also be automatically replaced with an uncorrupted copy of the block from the primary database.

See Also:

[Section 9.2, "Opening a Physical Standby Database"](manage_ps.md) for more information about each of these features

New 11.2 Features Specific to SQL Apply

- Logical standby databases support tables with basic table compression, OLTP table compression, and Hybrid Columnar Compression.
	See Also:
	- [Oracle Database Concepts](https://docs.oracle.com/cd/E11882_01/server.112/e40540/tablecls.htm#CNCPT89198) for more information about Hybrid Columnar Compression
- Logical standby and the LogMiner utility support tables with SecureFiles LOB columns. Compression and encryption operations on SecureFiles LOB columns are also supported. (De-duplication operations and fragment-based operations are not supported.)
- Changes made in the context of XA global transactions on an Oracle RAC primary database are replicated on a logical standby database.
- Online redefinition performed at the primary database using the `DBMS_REDEFINITION` PL/SQL package is transparently replicated on a logical standby database.
- Logical Standby supports the use of editions at the primary database, including the use of edition-based redefinition to upgrade applications with minimal downtime.
	See Also:
	- [Oracle Database Advanced Application Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e41502/adfns_editions.htm#ADFNS020) for information about edition-based redefinition
- Logical standby databases support Streams Capture. This allows you to offload processing from the primary database in one-way information propagation configurations and make the logical standby the hub that propagates information to multiple databases. Streams Capture can also propagate changes that are local to the logical standby database.

## New Features in Oracle Data Guard 11.1

The following sections describe the new features and enhancements that were added in Oracle Data Guard 11g Release 1 (11.1):

- New 11.1 Features Common to Redo Apply and SQL Apply
- New 11.1 Features Specific to Redo Apply
- New 11.1 Features Specific to SQL Apply

New 11.1 Features Common to Redo Apply and SQL Apply

- Compression of redo traffic over the network in a Data Guard configuration
	This feature improves redo transport performance when resolving redo gaps by compressing redo before it is transmitted over the network.
	See Also:
	["COMPRESSION"](log_arch_dest_param.md) attribute
- Redo transport response time histogram
	The `V$REDO_DEST_RESP_HISTOGRAM` dynamic performance view contains a histogram of response times for each `SYNC` redo transport destination. The data in this view can be used to assist in the determination of an appropriate value for the `LOG_ARCHIVE_DEST_` `n` NET\_TIMEOUT attribute.
	See Also:
	["NET\_TIMEOUT"](log_arch_dest_param.md) attribute
- Faster role transitions
- Strong authentication for redo transport network sessions
	Redo transport network sessions can now be authenticated using SSL. This provides strong authentication and makes the use of remote login password files optional in a Data Guard configuration.
- Simplified Data Guard management interface
	The SQL statements and initialization parameters used to manage a Data Guard configuration have been simplified through the deprecation of redundant SQL clauses and initialization parameters.
	See Also:
	- [Chapter 16, "SQL Statements Relevant to Data Guard"](sql_stmts.md) for information about which statements have had clauses deprecated
	- [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/toc.htm) for information about deprecated clauses relevant to the SQL statements discussed in [Chapter 16](sql_stmts.md)
	- [Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams125.htm#REFRN10086) for information about deprecated attributes of the `LOG_ARCHIVE_DEST_` n parameter
- Enhancements around `DB_UNIQUE_NAME`
	You can now find the `DB_UNIQUE_NAME` of the primary database from the standby database by querying the new `PRIMARY_DB_UNIQUE_NAME` column in the `V$DATABASE` view. Also, Oracle Data Guard release 11g ensures each database's `DB_UNIQUE_NAME` is different. After upgrading to 11g, any databases with the same `DB_UNIQUE_NAME` will not be able to communicate with each other.
- Use of physical standby database for rolling upgrades
	A physical standby database can now take advantage of the rolling upgrade feature provided by a logical standby. Through the use of the new `KEEP IDENTITY` clause option to the SQL `ALTER DATABASE RECOVER TO LOGICAL STANDBY` statement, a physical standby database can be temporarily converted into a logical standby database for the rolling upgrade, and then reverted back to the original configuration of a primary database and a physical standby database when the upgrade is done.
	See Also:
	[Chapter 12, "Using SQL Apply to Upgrade the Oracle Database"](rollup.md)
- Heterogeneous Data Guard Configuration
	This feature allows a mix of Linux and Windows primary and standby databases in the same Data Guard configuration.

New 11.1 Features Specific to Redo Apply

- Real-time query capability of physical standby
	This feature makes it possible to query a physical standby database while Redo Apply is active.
	See Also:
	[Section 9.2, "Opening a Physical Standby Database"](manage_ps.md) for more information about how an open physical standby database can continue to receive and apply redo data from a primary database
- Snapshot standby
	A snapshot standby database is new type of updatable standby database that provides full data protection for a primary database.
	See Also:
	[Section 9.7, "Managing a Snapshot Standby Database"](manage_ps.md)
- Lost-write detection using a physical standby
	A "lost write" is a serious form of data corruption that can adversely impact a database. It occurs when an I/O subsystem acknowledges the completion of a block write in the database, while in fact the write did not occur in the persistent storage. This feature allows a physical standby database to detect lost writes to a primary or physical standby database.
	See Also:
	[Section 13.6, "Recovering From Lost-Write Errors on a Primary Database"](scenarios.md) for an example of lost-write recovery, and [Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/cd/E11882_01/backup.112/e10642/rcmconfa.htm#BRADV89476) for information about enabling lost-write detection
- Improved Integration with RMAN
	A number of enhancements in RMAN help to simplify backup and recovery operations across all primary and physical standby databases, when using a catalog. Also, you can use the RMAN `DUPLICATE` command to create a physical standby database over the network without a need for pre-existing database backups.

New 11.1 Features Specific to SQL Apply

- Support for additional object datatypes and PL/SQL packages
	- XML stored as `CLOB`
		- `DBMS_RLS` (row-level security or Virtual Private Database)
		- `DBMS_FGA`
	See Also:
	[Appendix C, "Data Type and DDL Support on a Logical Standby Database"](data_support.md)
- Support Transparent Data Encryption (TDE)
	Data Guard SQL Apply can be used to provide data protection for the primary database with Transparent Data Encryption enabled. This allows a logical standby database to provide data protection for applications with advanced security requirements.
- Dynamic setting of Data Guard SQL Apply parameters
	You can now configure specific SQL Apply parameters without requiring SQL Apply to be restarted. Using the `DBMS_LOGSTDBY.APPLY_SET` package, you can dynamically set initialization parameters, thus improving the manageability, uptime, and automation of a logical standby configuration.
	In addition, the `APPLY_SET` and `APPLY_UNSET` subprograms include two new parameters: `LOG_AUTO_DEL_RETENTION_TARGET` and `EVENT_LOG_DEST`.
	See Also:
	`DBMS_LOGSTDBY` PL/SQL package in the [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/toc.htm)
- Enhanced Oracle RAC switchover support for logical standby databases
	When switching over to a logical standby database where either the primary database or the standby database is using Oracle RAC, the `SWITCHOVER` command can be used without having to shut down any instance, either at the primary or at the logical standby database.
- Enhanced DDL handling in Oracle Data Guard SQL Apply
	SQL Apply will execute parallel DDLs in parallel (based on availability of parallel servers).
- Use of the PL/SQL DBMS\_SCHEDULER package to create Scheduler jobs on a standby database
	Scheduler Jobs can be created on a standby database using the PL/SQL `DBMS_SCHEDULER` package and can be associated with an appropriate database role so that they run when intended (for example, when the database is the primary, standby, or both).