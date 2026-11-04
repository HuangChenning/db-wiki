---
title: "What's New in the SQL Language Reference?"
book: SQL Language Reference
doc_id: E41084-04
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e41084/wnsql.htm
tags:
  - oracle
  - 11g
  - sql-language-reference
---

This section describes new features of Oracle Database 11g and provides pointers to additional information.

For information on features that were new in earlier versions of Oracle Database, refer to the documentation for the earlier release.

## Oracle Database 11g Release 2 (11.2.0.4) New Features in the SQL Language Reference

The following are new features in this release:

- You can now instruct the database to optimize the storage of data in history tables. See the [\[NO\] OPTIMIZE DATA](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_5010.htm#BGEBGFCA) clause of `CREATE` `FLASHBACK` `ARCHIVE` and the [\[NO\] OPTIMIZE DATA](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_1008.htm#BGEDBAEF) clause of `ALTER` `FLASHBACK` `ARCHIVE`.
- The function [SYS\_CONTEXT](functions184.md) enables you to query a new built-in namespace, `SYS_SESSION_ROLES`, which allows you to determine if a specified role is currently enabled for the session.
- The new system privilege `EXEMPT` `REDACTION` `POLICY` allows you to bypass any existing Oracle Data Redaction policies. See [Table 18-1](statements_9013.md).

## Oracle Database 11g Release 2 (11.2.0.2) New Features in the SQL Language Reference

The following top-level SQL statements are enhanced in this release:

- `CREATE` `TABLE` and `ALTER` `TABLE` now support the clause [deferred\_segment\_creation](statements_7002.md) for partitions and subpartitions. This lets you postpone creation of a segment until the first row of data is inserted into the partition or subpartition.
- `TRUNCATE` `TABLE` has a new clause [DROP ALL STORAGE](statements_10007.md) that lets you deallocate all segments for a table. `ALTER` `TABLE` has a new clause [DROP ALL STORAGE](statements_3001.md) that lets you deallocate all segments for a partition or subpartition.

## Oracle Database 11g Release 2 (11.2.0.1) New Features in the SQL Language Reference

Structural Changes in the SQL Language Reference

A number of sections of this book that were made up primarily of PL/SQL were moved to [Oracle Database PL/SQL Language Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e25519/toc.htm) in Oracle Database 11g Release 1. Refer to "Structural Changes in the SQL Language Reference" for details on this migration of material.

New Features in the SQL Language Reference

The following top-level SQL statements are new or enhanced in this release:

- A new top-level SQL statement [ALTER DATABASE LINK](statements_1005.md) lets you update the fixed user password in a database link when the password of a connection or authentication user has changed.
- The `ALTER` `DISKGROUP` statement has the following changes:
	- A new [disk\_region\_clause](statements_1007.md) lets you determine the Intelligent Data Placement attribute of the disk group file.
		- New [diskgroup\_volume\_clauses](statements_1007.md) let you manipulate logical Oracle ASM Dynamic Volume Manager (Oracle ADVM) volumes corresponding to physical volume devices.
		- Several new clauses let you control access to Oracle ASM files: [usergroup\_clauses](statements_1007.md), [user\_clauses](statements_1007.md), [file\_permissions\_clause](statements_1007.md), and [file\_owner\_clause](statements_1007.md).
- `AUDIT` and `NOAUDIT` contain a new clause [ALL STATEMENTS](statements_4007.md) that lets you enable and disable auditing of all top-level SQL statements executed. In `AUDIT` only, a new clause [IN SESSION CURRENT](statements_4007.md) allows you to limit auditing to the current session.
- `CREATE` `DISKGROUP` and `ALTER` `DISKGROUP` have the following changes:
	- A new clause [QUORUM | REGULAR](statements_5008.md) let you designate a disk or failure group as a quorum disk or failure group, which can contain the voting file for Cluster Synchronization Services (CSS).
- Two new statements, [CREATE EDITION](statements_5009.md) and [DROP EDITION](statements_8014.md), let you use editions. An edition makes it possible to have two or more versions of the same editionable objects in the database.
- [CREATE INDEXTYPE](statements_5013.md) and [ALTER INDEXTYPE](statements_1011.md) have a new clause `WITH` `SYSTEM` `MANAGED` `STORAGE` `TABLES`. This clause makes it possible to create domain indexes in both range- and list-partitioned tables.
- `ALTER` `SESSION` contains a new clause [SYNC WITH PRIMARY](statements_2013.md) that lets you synchronize the physical standby database with the primary database. A new session parameter [STANDBY\_MAX\_DATA\_DELAY](statements_2013.md) lets you specify a session-specific apply lag tolerance for queries to a physical standby database that is in real-time query mode.
- `CREATE` `MATERIALIZED` `VIEW` `LOG` has a new clause [COMMIT SCN](statements_6003.md) that instructs the database to use commit SCN data instead of timestamps to refresh the materialized view, which improves the speed of the refresh.
- `CREATE` `MATERIALIZED` `VIEW` `LOG` and `ALTER` `MATERIALIZED` `VIEW` `LOG` have a new clause [mv\_log\_purge\_clause](statements_6003.md) that lets you specify the purge time for the materialized view log.
- `CREATE` `TABLE` and `ALTER` `TABLE` are enhanced in the following ways:
	- A new clause [deferred\_segment\_creation](statements_7002.md) lets you postpone creation of the table segment until the first row of data is inserted into the table. This clause is also applicable to materialized views.
		- The clause [table\_compression](statements_7002.md) has new syntax and terminology. Use `COMPRESS` `FOR` `OLTP` to specify OLTP table compression. (In earlier releases, the syntax was `COMPRESS` `FOR` `ALL` `OPERATIONS`.) Use `COMPRESS` `BASIC` to specify basic table compression. (In earlier releases, the syntax was `COMPRESS` `FOR` `DIRECT_LOAD` `OPERATIONS` and this type of compression was called DSS table compression.)
		- A new [RESULT\_CACHE Clause](statements_7002.md) lets you specify whether the results of queries that name the table are considered for result caching.
		- The [nested\_table\_col\_properties](statements_7002.md) provides a `LOCAL` keyword to equipartition a nested table with partitioned base table. This is the default behavior in this release. The default in earlier releases was not to equipartition the nested table with the partitioned base table. Now you must specify the `GLOBAL` keyword to store an unpartitioned nested table with a partitioned base table.
- The `CREATE` `VIEW` has a new keyword [EDITIONING](statements_8004.md) that lets you create an editioning view.
- The statement [GRANT](statements_9013.md) has a new `EXECUTE` object privilege on directory objects. The `ORACLE_LOADER` access driver for external tables references this privilege when deciding whether to execute a preprocessor program.

The following built-in functions are new or enhanced in this release:

- For a specified measure, the function [LISTAGG](functions089.md) orders data within each group specified in an `ORDER` `BY` clause and then concatenates the values of the measure column.
- A new [NTH\_VALUE](functions114.md) function returns the value of a measure in a specified row of a window of data.
- Three new functions are useful when you are changing the time zone data file for your database: [ORA\_DST\_AFFECTED](functions121.md), [ORA\_DST\_CONVERT](functions122.md), and [ORA\_DST\_ERROR](functions123.md).

The following miscellaneous features are new or enhanced in this release:

- Hints, which were introduced in Oracle7, are now superseded by several Oracle tools, including the SQL Tuning Advisor, SQL plan management, and SQL Performance Analyzer. See ["Hints"](sql_elements006.md) for more information.
- Beginning with Oracle Database 11g Release 2 (11.2.0.1), the `PARALLEL`, `PARALLEL_INDEX`, `NO_PARALLEL`, and `NO_PARALLEL_INDEX` hints are statement-level hints and supersede the earlier object-level hints. See ["Note on Parallel Hints"](sql_elements006.md).
- A new [APPEND\_VALUES Hint](sql_elements006.md) lets you use direct-path `INSERT` with the `VALUES` clause.
- When specifying a redo log file, you can use the new keyword [BLOCKSIZE Clause](clauses004.md) to override the operating system-dependent sector size.
- The [LOB\_compression\_clause](statements_7002.md) now has a new `LOW` setting, which results in significantly higher decompression and compression speeds, at the cost of a slightly lower compression ratio.
- The [subquery\_factoring\_clause](statements_10002.md) now supports recursive subquery factoring (recursive WITH), which lets you query hierarchical data. This feature is more powerful than `CONNECT` `BY` in that it provides depth-first search and breadth-first search, and supports multiple recursive branches. A new [search\_clause](statements_10002.md) and [cycle\_clause](statements_10002.md) let you specify an ordering for the rows and mark cycles in the recursion.

## Oracle Database 11g Release 1 New Features in the SQL Language Reference

Structural Changes in the SQL Language Reference

A number of SQL statements are constructed almost entirely of PL/SQL elements. Those statements continue to appear in this reference, but the bulk of their syntax and semantics has been moved to [Oracle Database PL/SQL Language Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e25519/toc.htm). The following table contains links to both the abbreviated SQL syntax and semantics in this book and to the full syntax and semantics in Oracle Database PL/SQL Language Reference.

| Abbreviated SQL Section | Full Syntax and Semantics |
| --- | --- |
| [CREATE FUNCTION](statements_5011.md) | [CREATE FUNCTION](https://docs.oracle.com/cd/E11882_01/appdev.112/e25519/create_function.htm#LNPLS01370) |
| [CREATE PACKAGE](statements_6006.md) | [CREATE PACKAGE](https://docs.oracle.com/cd/E11882_01/appdev.112/e25519/create_package.htm#LNPLS01371) |
| [CREATE PACKAGE BODY](statements_6007.md) | [CREATE PACKAGE BODY](https://docs.oracle.com/cd/E11882_01/appdev.112/e25519/create_package_body.htm#LNPLS01372) |
| [CREATE PROCEDURE](statements_6009.md) | [CREATE PROCEDURE](https://docs.oracle.com/cd/E11882_01/appdev.112/e25519/create_procedure.htm#LNPLS01373) |
| [CREATE TRIGGER](statements_7004.md) | [CREATE TRIGGER](https://docs.oracle.com/cd/E11882_01/appdev.112/e25519/create_trigger.htm#LNPLS01374) |
| [CREATE TYPE](statements_8001.md) | [CREATE TYPE](https://docs.oracle.com/cd/E11882_01/appdev.112/e25519/create_type.htm#LNPLS01375) |
| [CREATE TYPE BODY](statements_8002.md) | [CREATE TYPE BODY](https://docs.oracle.com/cd/E11882_01/appdev.112/e25519/create_type_body.htm#LNPLS01376) |
| [ALTER FUNCTION](statements_1009.md) | [ALTER FUNCTION](https://docs.oracle.com/cd/E11882_01/appdev.112/e25519/alter_function.htm#LNPLS99999) |
| [ALTER PACKAGE](statements_2006.md) | [ALTER PACKAGE](https://docs.oracle.com/cd/E11882_01/appdev.112/e25519/alter_package.htm#LNPLS99998) |
| [ALTER PROCEDURE](statements_2007.md) | [ALTER PROCEDURE](https://docs.oracle.com/cd/E11882_01/appdev.112/e25519/alter_procedure.htm#LNPLS99997) |
| [ALTER TRIGGER](statements_4001.md) | [ALTER TRIGGER](https://docs.oracle.com/cd/E11882_01/appdev.112/e25519/alter_trigger.htm#LNPLS99996) |
| [ALTER TYPE](statements_4002.md) | [ALTER TYPE](https://docs.oracle.com/cd/E11882_01/appdev.112/e25519/alter_type.htm#LNPLS99995) |

New Features in the SQL Language Reference

The following top-level SQL statements are new or enhanced in this release:

- [ALTER DATABASE](statements_1004.md) has been enhanced as follows:
	- The clause [managed\_standby\_recovery](statements_1004.md) has been greatly simplified. A number of subclauses have been deprecated as the database now handles much of the recovery process automatically.
		- The [supplemental\_db\_logging](statements_1004.md) contains new syntax that lets you enable or disable supplemental logging of PL/SQL calls.
		- The [standby\_database\_clauses](statements_1004.md) have new syntax that lets you convert a physical standby database into a snapshot standby database or convert a snapshot standby database into a physical standby database.
		- The clause [managed\_standby\_recovery](statements_1004.md) has new `KEEP` `IDENTITY` syntax that lets you use the rolling upgrade feature provided by a logical standby and also revert to the original configuration of a primary database and a physical standby.
- [ALTER DISKGROUP](statements_1007.md) has been enhanced as follows:
	- The [check\_diskgroup\_clause](statements_1007.md) has simplified syntax for checking the consistency of disk groups, disks, and files in an Oracle ASM environment.
		- The clause [diskgroup\_availability](statements_1007.md) offers new options when mounting a disk group.
		- New clauses [disk\_offline\_clause](statements_1007.md) and [disk\_online\_clause](statements_1007.md) let you take a disk offline for repair and then bring it back online.
- [ALTER INDEX](statements_1010.md) has been enhanced as follows:
	- A new `MIGRATE` parameter lets you migrate a domain index from user-managed storage tables to system-managed storage tables.
		- A new `INVISIBLE` parameter lets you modify an index so that it is invisible to the optimizer.
		- The ["PARAMETERS Clause"](statements_1010.md) now lets you rebuild an XMLIndex index as well as a domain index.
- [ALTER SYSTEM](statements_2014.md) has been enhanced as follows:
	- New syntax lets you kill a session on another instance in an Oracle Real Application Clusters (Oracle RAC) environment.
		- New [rolling\_migration\_clauses](statements_2014.md) let you prepare an Oracle ASM cluster for migration and return it to normal operation after all nodes have migrated to the same software version.
- [ALTER TABLE](statements_3001.md) has been enhanced as follows:
	- The behavior of the [add\_column\_clause](statements_3001.md) when you specify a `DEFAULT` value has been enhanced for improved performance.
		- The syntax for [READ ONLY | READ WRITE](statements_3001.md) lets you put a table into read-only mode, to prevent DDL or DML changes during table maintenance, and then back into read/write mode.
		- The clause [add\_table\_partition](statements_3001.md) has expanded syntax to let you add a system partition.
		- The [flashback\_archive\_clause](statements_3001.md) lets you enable or disable historical tracking for the table.
		- The [add\_column\_clause](statements_3001.md) now lets you add a virtual column to a table.
		- A new clause [alter\_interval\_partitioning](statements_3001.md) lets you convert a range-partitioned table to an interval\_partitioned table.
		- A new [dependent\_tables\_clause](statements_3001.md) lets you instruct the database to cascade various partition maintenance operations on a table to reference-partitioned child tables.
- [ALTER TABLESPACE](statements_3002.md) has new syntax that lets you shrink the space taken by a temporary tablespace or an individual temp file.
- [ASSOCIATE STATISTICS](statements_4006.md) has syntax that lets you specify that the database should manage storage of statistics collected on a system-managed domain index.
- [AUDIT](statements_4007.md) has new syntax that lets you audit various activities on data mining models.
- [CALL](statements_4008.md) now permits positional, named, and mixed notation in the argument to the routine being called, if the routine takes any arguments.
- [COMMENT](statements_4009.md) has a new `MINING` `MODEL` clause lets you provide descriptive comments for a data mining model.
- [CREATE DISKGROUP](statements_5008.md) and [ALTER DISKGROUP](statements_1007.md) have new syntax that lets you set various attributes of a disk group.
- The new statements [CREATE FLASHBACK ARCHIVE](statements_5010.md), [ALTER FLASHBACK ARCHIVE](statements_1008.md), and [DROP FLASHBACK ARCHIVE](statements_8015.md) let you create, modify, and drop flashback data archives, which in turn let you track historical changes to tables.
- [CREATE INDEX](statements_5012.md) has been enhanced as follows:
	- A new [local\_domain\_index\_clause](statements_5012.md) lets you create a locally partitioned domain index.
		- The [index\_attributes](statements_5012.md) have been modified to let you create an index that is invisible to the optimizer.
		- A new [XMLIndex\_clause](statements_5012.md) lets you create an XMLIndex index for XML data.
- [CREATE INDEXTYPE](statements_5013.md) and [ALTER INDEXTYPE](statements_1011.md) let you specify that domain indexes built on the subject indextypes can be range partitioned, and will have their storage tables and partition maintenance operations managed by the database.
- [CREATE PFILE](statements_6008.md) has new syntax that lets you create a parameter file from current system-wide parameter settings.
- [CREATE RESTORE POINT](statements_6011.md) has new syntax that lets you create a restore point for a specified datetime or SCN in the past, and to preserve a flashback database.
- [CREATE SPFILE](statements_6016.md) has new syntax that lets you create a system parameter file from current system-wide parameter settings.
- [CREATE TABLE](statements_7002.md) has been enhanced as follows:
	- The [flashback\_archive\_clause](statements_7002.md) lets you create the table with tracking of historical changes enabled
		- The clause [system\_partitioning](statements_7002.md) lets you partition the table `BY` `SYSTEM`
		- A new [virtual\_column\_definition](statements_7002.md) lets you create a virtual column.
		- New syntax for XML storage lets you store XML data in binary XML format.
		- A new clause [reference\_partitioning](statements_7002.md) lets you partition a table by reference to another partitioned table.
		- The [LOB\_parameters](statements_7002.md) now include a `SECUREFILE` parameter, which lets you specify a new storage for LOBs that is faster, more efficient, and allows for new features such as LOB compression, encryption, and deduplication.
		- A new [LOB\_compression\_clause](statements_7002.md) lets you enable or disable server-side LOB compression for LOBs using SecureFiles storage.
		- A new [LOB\_deduplicate\_clause](statements_7002.md) lets you coalesce duplicate data into a single shared repository, reducing storage consumption and simplifying storage management for LOBs using SecureFiles storage.
		- The [LOB\_parameters](statements_7002.md) now include `ENCRYPT` and `DECRYPT` clauses to enable and disable encryption of LOB columns for LOBs using SecureFiles storage.
- [CREATE TABLESPACE](statements_7003.md) has new syntax which, along with a new `ENCRYPT` keyword in the [storage\_clause](clauses009.md), lets you encrypt an entire tablespace.
- [DROP DISKGROUP](statements_8013.md) has a new `FORCE` keyword that lets you drop a disk group that can no longer be mounted by an Oracle ASM instance.
- [GRANT](statements_9013.md) contains several new system and object privileges that enable the grantee to work with data mining models.
- [LOCK TABLE](statements_9015.md) has new syntax that lets you specify the maximum number of seconds the statement should wait to obtain a DML lock on the table.
- [MERGE](statements_9016.md) now supports operations on tables with domain indexes.
- [SELECT](statements_10002.md) has new `PIVOT` syntax that lets you rotate rows into columns. A new `UNPIVOT` operation lets you query data to rotate columns into rows.

The following SQL built-in functions have been added or enhanced:

- [CUBE\_TABLE](functions042.md) is a new built-in function that extracts data from a cube or dimension and returns it in the two-dimensional format of a relational table.
- [INSERTXMLAFTER](functions078.md) let you add one or more nodes of any kind immediately after a target node that is not an attribute node.
- [REGEXP\_INSTR](functions148.md) and [REGEXP\_SUBSTR](functions150.md) now have an optional `subexpr` parameter that lets you target a particular substring of the regular expression being evaluated.
- [REGEXP\_COUNT](functions147.md) is a new built-in function that counts the number of occurrences of a specified regular expression pattern in a source string.
- [PREDICTION](functions132.md), [PREDICTION\_COST](functions134.md), and [PREDICTION\_SET](functions137.md) have been enhanced. New syntax let you specify that the stored cost matrix should be used only if it is available, or to specify a cost matrix inline.
- [PREDICTION\_BOUNDS](functions133.md) is a new function that returns the lower and upper confidence bounds for a prediction.
- [XMLCAST](functions236.md) and [XMLEXISTS](functions243.md) are two new functions that let you cast XML data to SQL scalar data types and determine whether an XQuery expression returns a nonempty XQuery sequence, respectively.
- [XMLDIFF](functions241.md) and [XMLPATCH](functions247.md) are two new functions that provide SQL interfaces to the corresponding XMLDiff and XMLPatch C APIs. They let you compare two XMLType documents and use the diff file to patch an XMLType document.

The following miscellaneous changes have been made:

- In earlier releases, one form of expression in [Chapter 6, "Expressions"](expressions.md) was the variable expression. This form has been renamed to placeholder expression for consistency with other books in the documentation set. See ["Placeholder Expressions"](expressions012.md).
- In earlier releases, the `TRUNCATE` statement was presented as a single statement with separate syntactic branches for `TABLE` and `CLUSTER`. That command has now been divided into [TRUNCATE CLUSTER](statements_10006.md) and [TRUNCATE TABLE](statements_10007.md) for consistency with other top-level SQL statements. No actual syntax or semantic changes have occurred.
- Two new hints, ["RESULT\_CACHE Hint"](sql_elements006.md) and ["NO\_RESULT\_CACHE Hint"](sql_elements006.md), let you override settings of the `RESULT_CACHE_MODE` initialization parameter.
- ["Function Expressions"](expressions008.md) now permit positional, named, and mixed notation in the argument to a user-defined function being used as an expression.
- The `index_partition_description` syntax of [ALTER TABLE](statements_3001.md) and [ALTER INDEX](statements_1010.md) now lets you specify parameters for a partition of a domain index.
- A new object type object type is supported with Oracle Multimedia. See [Media Types](sql_elements001.md)