---
title: "What's New in Oracle Database Administrator's Guide?"
book: "Administrator's Guide"
doc_id: E25494-07
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e25494/whatsnew.htm
tags:
  - oracle
  - 11g
  - administrators-guide
---

This section describes new features of Oracle Database 11g Release 2 that are documented in this guide, and provides pointers to additional information.

This section contains the following topics:

## Oracle Database 11g Release 2 (11.2.0.3) New Features in the Administrator's Guide

- Copy-on-write cloning of a database with CloneDB
	When cloning a database with CloneDB, Oracle Database can create the files in a CloneDB database based on copy-on-write technology, so that only the blocks that are modified in the CloneDB database require additional storage on disk.
	See ["Cloning a Database with CloneDB"](create.md).
- Hybrid Columnar Compression
	Hybrid Columnar Compression offers higher compression levels for direct path loaded data. This new compression capability is recommended for data that is not updated frequently. You can specify Hybrid Columnar Compression at the partition, table, and tablespace level. You can also specify the desired level of compression to achieve the proper trade-off between disk usage and CPU overhead. You can use the compression advisor to help you determine the proper compression levels for your application.
	See ["Consider Using Table Compression"](tables.md).

## Oracle Database 11g Release 2 (11.2.0.2) New Features in the Administrator's Guide

- Deferred segment creation for partitioned objects
	- Deferred segment creation now applies to partitioned objects as well as nonpartitioned objects.
		See ["Understand Deferred Segment Creation"](tables.md).
		- You can drop segments from empty tables that were migrated from previous releases, using the `DBMS_SPACE_ADMIN.DROP_EMPTY_SEGMENTS` procedure.
		See ["Dropping Unused Object Storage"](schema.md).
		- The `DROP` `ALL` `STORAGE` clause of the `TRUNCATE` statement enables you to deallocate segments for a table.
		See ["Using TRUNCATE"](general.md).
		- You can materialize segments for tables, partitions, and dependent objects for which segment creation was deferred, using the `DBMS_SPACE_ADMIN.MATERIALIZE_DEFERRED_SEGMENTS` procedure.
		See ["Materializing Segments"](tables.md).
- New default first extent size for partitioned tables improves performance
	The default size of the first extent of any new segment for a partitioned table is now 8 MB instead of 64 KB. This helps improve performance of inserts and queries on partitioned tables. Although partitioned tables will start with a larger initial size, once sufficient data is inserted, the space consumption will be the same as in previous releases. You can override this default by setting the `INITIAL` size in the storage clause for the table. This new default only applies to table partitions and LOB partitions.
- New initialization parameter to improve the performance of `NOLOGGING` direct-path inserts
	You can now significantly improve the performance of unrecoverable direct path inserts by disabling the periodic update of the control files. You do so by setting the new initialization parameter `DB_UNRECOVERABLE_SCN_TRACKING` to `FALSE`. However, if you perform an unrecoverable direct path insert with these control file updates disabled, you will no longer be able to accurately query the database to determine if any data files are currently unrecoverable.
	See ["Direct-Path INSERT without Logging"](tables.md)
- Improved e-mail notification capabilities in Oracle Scheduler
	Oracle Scheduler e-mail notification preferences now include options to specify authentication and SSL or TLS protocols for the designated SMTP Server.
	See ["Setting Scheduler Preferences"](schedadmin.md).
- Edition attributes of database services
	You can set the edition attribute of a database service when you create the service, or you can modify an existing database service to set its edition attribute.
	See ["Setting the Edition Attribute of a Database Service"](general.md).
- Enhancements to Oracle Database Resource Manager
	- You can optimize the performance of parallel statements by limiting the parallel statement activity per consumer group, prioritizing parallel statements in the parallel statement queue, and limiting the wait time for parallel statement in the parallel statement queue.
		Parallel statement queuing enables efficient management of parallel statements when the database does not have sufficient resources to run a statement at the specified degree of parallelism. A submitted parallel statement is added to the parallel statement queue if the resources required to run the statement exceed the parallel statement activity limit specified for the database or the consumer group to which the parallel statement is assigned. Parallel statement queuing can also manage multiple parallel statement workloads according to the priorities and resource allocations specified by a resource plan.
		- You can track CPU utilization using per-minute metrics for each resource plan. You can also monitor resource utilization for consumer groups, even if Resource Manager is not enabled, thus allowing you to view the potential effect of Resource Manager.
		See ["V$RSRCMGRMETRIC"](dbrm.md).

## Oracle Database 11g Release 2 (11.2.0.1) New Features in the Administrator's Guide

- Oracle Restart improves database availability by automatically restarting the database after a failure.
	If you configure Oracle Restart, then the database, the listener, the Oracle Automatic Storage Management instance, and other Oracle components can be automatically restarted after a hardware or software failure or after a restart of the database host computer.
	See [Chapter 4, "Configuring Automatic Restart of an Oracle Database"](restart.md).
- Edition-based redefinition enables application developers and DBAs to upgrade an application with little or no application down time.
	A new database construct called an edition provides a privacy mechanism for installing new code and for making data changes so that the running production application does not see the changes. When all the required changes have been made in private, they can be made available to users. In support of edition-based redefinition, a new kind of view called an editioning view and a new kind of trigger called a crossedition trigger are introduced.
	See ["Managing Editions"](general.md).
- Database Smart Flash Cache
	Database Smart Flash Cache is an optional memory component that you can add if your database is running on Solaris or Oracle Linux. It is an extension of the SGA-resident buffer cache, providing a level 2 cache for database blocks. It can improve response time and overall throughput.
	See ["Memory Architecture Overview"](memory.md).
- The Automatic Segment Advisor can now return a recommendation to use OLTP compression for a table.
	See ["Reclaiming Wasted Space"](schema.md).
- Deferred segment creation
	When creating a nonpartitioned heap-organized table in a locally managed tablespace, table segment creation is deferred until the first row is inserted.
	See ["Understand Deferred Segment Creation"](tables.md).
- Oracle Database File System
	The Oracle Database File System creates a standard file system interface on top of files and directories that are stored in database tables.
	See [Oracle Database SecureFiles and Large Objects Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e18294/adlob_fs.htm#ADLOB45943) for complete information.
- Oracle Scheduler enhancements
	- Remote database jobs—You can now create a job that runs stored procedures and anonymous PL/SQL blocks on another database instance on the same host or on a remote host. The target database can be any release of Oracle Database.
		See ["Database Jobs"](schedover.md).
		- Multiple-destination jobs—You can now run a job on multiple locations, and control and monitor all instances of the job from one central database. You do so by specifying multiple destinations when you create the job. A destination can be the local host or local database; a remote host (for remote external jobs); or a remote database (for remote database jobs).
		See ["Multiple-Destination Jobs"](schedover.md)
		- File watchers—A new Scheduler object called a file watcher simplifies the task of configuring the Scheduler to start a job upon the arrival of a file on the local or a remote system.
		See ["Starting a Job When a File Arrives on a System"](scheduse.md).
		- E-mail notifications—You can configure the Scheduler to automatically send an e-mail notification to one or more recipients when a specified job state event occurs. You can now receive an e-mail when a job completes, if it fails or is disabled, if it exceeds its allotted run time, and so on.
		See ["Monitoring Job State with E-mail Notifications"](scheduse.md).
- Database Resource Manager Enhancements
	- Instance caging
		Oracle Database now provides a method for managing CPU allocations on a multi-CPU server running multiple database instances. Instance caging limits the maximum number of CPUs that any one database instance can use. If an instance then becomes CPU-bound, the Resource Manager begins allocating CPU based on the current resource plan. Thus, instance caging and the Resource Manager work together to support desired levels of service across multiple instances.
		See ["Managing Multiple Database Instances on a Single Server"](dbrm.md).
		- New `MAX_UTILIZATION_LIMIT` attribute of resource plan directives enables you to impose an absolute upper limit on CPU utilization for a resource consumer group. This absolute limit overrides any automatic redistribution of CPU within a plan.
		- New `ORACLE_FUNCTION` consumer group mapping rule type, and new predefined mapping rules for Data Pump and RMAN.
		Sessions performing a data load with Data Pump or performing backup or copy operations with RMAN are now automatically mapped to predefined consumer groups.
		See ["Predefined Consumer Group Mapping Rules"](dbrm.md).
		- New sample resource plans and resource consumer groups to support data warehousing operations with Oracle Exadata
		See ["Predefined Resource Plans and Consumer Groups"](dbrm.md).
- New SQL command syntax for specifying table compression for direct load operations only or for all (OLTP) operations.
	See ["Consider Using Table Compression"](tables.md).
- The Flash Recovery Area is renamed to Fast Recovery Area.
- External tables can be preprocessed by user-supplied preprocessor programs.
	By using a preprocessing program, users can use data from a file that is not in a format supported by the access driver. For example, a user may want to access data stored in a compressed format. Specifying a decompression program for the `ORACLE_LOADER` access driver allows the data to be decompressed as the access driver processes the data.
	See ["Preprocessing External Tables"](tables.md).
- Archive logging now supports up to 30 standby databases.
- IP version 6 is now supported.
	Oracle Database components and utilities now support Internet Protocol version 6 (IPv6) addresses, which are 128 bits in length. You can now specify an IPv6 address with the easy connect method in SQL\*Plus.
	See ["Connecting to the Database with SQL\*Plus"](dba.md).
- Redo logs can now be stored on disk drives with a sector size of 4K bytes without performance degradation.
	A new redo log file block size of 4K bytes enables online redo logs to be stored on newer high-capacity disks with a 4K byte sectors size without incurring performance degradation. The new block size ensures that log file writes are sector-aligned.
	See ["Planning the Block Size of Redo Log Files"](onlineredo.md).
- The Enterprise Manager Support Workbench, a component of the fault diagnosability infrastructure, now supports investigating, reporting, and resolving critical errors in Oracle Automatic Storage Management instances.
	See [Chapter 9, "Managing Diagnostic Data"](diag.md).