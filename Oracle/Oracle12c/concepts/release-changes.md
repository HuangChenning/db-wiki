---
title: Database Concepts
book: Database Concepts
doc_id: E85769-04
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/cncpt/release-changes.html
tags:
  - oracle
  - 12c
  - concepts
---

This preface contains:

### Changes in Oracle Database 12c Release 2 (12.2.0.1)

Oracle Database Concepts for Oracle Database 12c Release 2 (12.2.0.1) has the following changes.

#### New Features

The following major features are new in this release:

- Oracle Database Sharding
	Oracle Sharding is a scalability and availability feature for suitable OLTP applications in which data is horizontally partitioned across discrete Oracle databases, called shards, which share no hardware or software. An application sees the collection of shards as a single logical Oracle database. Sharding provides linear scalability with fault isolation, automation of many lifecycle management tasks, excellent runtime performance, and the many advantages that come using an Oracle database as a shard (such as SQL and JSON support).
	See " [Oracle Sharding Architecture](oracle-sharding-architecture.md) ".
- Multitenant enhancements
	- Application containers
		An application container consists of an application root and one or more application PDBs. The container stores data for a specific application, which contains common data and metadata. You can upgrade or patch the application once in the application root, and then synchronize the application PDBs with the root.
		See " [About Application Containers](overview-of-the-multitenant-architecture.md) ", " [Overview of Common and Local Objects in a CDB](overview-of-the-multitenant-architecture.md) ", and " [Overview of Applications in an Application Container](overview-of-the-multitenant-architecture.md) ".
		- PDB creation and relocation enhancements
		These enhancements include:
		- You can relocate a PDB from one CDB to another with minimal down time (see " [Creation of a PDB by Relocating](introduction-to-the-multitenant-architecture.md) ").
				- During a PDB clone operation, the source PDB no longer needs to be in read-only mode (see " [Creation of a PDB by Cloning a PDB or a Non-CDB](introduction-to-the-multitenant-architecture.md) ").
				- You can create a proxy PDB, which references a PDB in a different CDB and provides fully functional access to the referenced PDB (" [Proxy PDBs](overview-of-the-multitenant-architecture.md) ").
		- Flashback PDB and PDB restore points
		You can use `FLASHBACK PLUGGABLE DATABASE` command to rewind a PDB to any SCN without affecting other PDBs in a CDB. You can also create a restore point specific for a PDB, and rewind the PDB to this restore point without affecting other PDB.
		See " [Overview of Flashback PDB in a CDB](overview-of-the-multitenant-architecture.md) ".
		- PDB lockdown profiles
		A PDB lockdown profile is a security mechanism to restrict operations that are available to users connected to a specified PDB. For example, a CDB administrator might create a lockdown profile to restrict networking access such as `UTL_HTTP` and `UTL_SMTP`, or local user access to objects in a common schema.
		See " [Overview of PDB Lockdown Profiles](overview-of-the-multitenant-architecture.md) ".
		- Performance manageability enhancements
		You can configure PDB parameters to guarantee or limit SGA memory, PGA memory, sessions, CPU, and I/O rates for each PDB. You can also configure performance profiles to configure Oracle Database Resource Manager resource plans for a large number of PDBs.
		See " [Benefits of the Multitenant Architecture for Manageability](introduction-to-the-multitenant-architecture.md) ".
- Compression enhancements
	- Advanced index compression enhancements
		Advanced high compression (`COMPRESS ADVANCED HIGH`) offers higher ratios than index compression offered in previous releases.
		See " [Advanced Index Compression](indexes-and-index-organized-tables.md) ".
		- Hybrid Columnar Compression (HCC) extended to conventional inserts
		Conventional inserts into heap-organized tables can use Hybrid Columnar Compression. Thus, the compression benefits now extends to `SQL INSERT SELECT` statements without the `APPEND` hint, and array inserts from programmatic interfaces such as PL/SQL and the Oracle Call Interface (OCI).
		See " [DML and Hybrid Columnar Compression](tables-and-table-clusters.md) ".
- Partitioning enhancements
	- You can partition external tables on virtual or non-virtual columns. Thus, you can take advantage of performance improvements provided by partition pruning and partition-wise joins. Oracle Database also provides the `ORACLE_HDFS` driver for the extraction of data stored in a Hadoop Distributed File System (HDFS), and the `ORACLE_HIVE` driver for access to data stored in an Apache Hive database.
		See " [Overview of External Tables](tables-and-table-clusters.md) ".
		- List partitioning is expanded to allow multiple partition key columns.
		See " [List Partitioning](partitions-views-and-other-schema-objects.md) ".
- Unstructured data enhancements
	- JSON enhancements
		Oracle Database extends support for storing and querying JSON documents in the database by enabling you to generate JSON documents from relational data using SQL and manipulate JSON documents as PL/SQL objects. Also, the IM column store now loads an efficient binary representation of JSON columns.
		See " [Overview of JSON in Oracle Database](concepts-for-database-developers.md) ".
		- Oracle Multimedia PL/SQL API
		Oracle Multimedia provides a PL/SQL API for multimedia functionality such as image thumbnail creation, image watermarking, and metadata extraction for multimedia data stored in BLOBs and BFILEs.
		See " [Overview of Oracle Multimedia](concepts-for-database-developers.md) ".
- Local temporary tablespaces
	You can create local, nonshared temporary tablespaces. When many read-only instances access a single database, local temporary tablespaces can improve performance for queries that involve sorts, hash aggregations, and joins.
	Note:
	In previous releases, the term temporary tablespace referred to what is now called a shared temporary tablespace.
	See " [Temporary Tablespaces](logical-storage-structures.md) ".
- Application Continuity enhancements
	Application Continuity for planned outages enables applications to continue operations for database sessions that can be reliably drained or migrated. An application-independent infrastructure enables continuity of service from an application perspective, masking planned outages relating to the database.
	See " [Application Continuity for Planned Maintenance](transactions.md) ".
- Real-Time database operation monitoring enhancements
	You can start and stop a database operation from any session in the database by specifying the session identifier and serial number for a particular session.
	See " [Database Operations](process-architecture.md) ".
- Instance architecture enhancements
	- Support for read/write and read-only instances in the same database
		Both read/write and read-only instances can open the same database. Read-only instances improve scalability of parallel queries for data warehousing workloads. For example, in an `INSERT ... SELECT` statement, the read/write and read-only instances process the `SELECT`, whereas only the read/write instances process the `INSERT`.
		See " [Read/Write and Read-Only Instances](oracle-database-instance.md) ".
		- Pre-Spawned processes
		You can pre-create a pool of server processes by using the `DBMS_PROCESS` PL/SQL package. The new Process Manager (PMAN) background process monitors the pool of pre-created processes, which wait to be associated with a client request. When a connection requires a server process, the database can eliminate some of the steps in process creation.
		See " [How Oracle Database Creates Server Processes](process-architecture.md) ".
		- Process Monitor (PMON) process group
		Duties that belonged exclusively to PMON now belong to the PMON process group, which includes PMON, Cleanup Main Process (CLMN), and Cleanup Helper Processes (CLnn). The PMON process group is responsible for the monitoring and cleanup of other processes.
		See " [Process Monitor Process (PMON) Group](process-architecture.md) ".
		- Database resource quarantine
		In some cases, process cleanup itself can encounter errors, which can result in the termination of process monitor (PMON) or the database instance. In some circumstances, by allowing certain database resources to be quarantined, the database instance can avoid termination.
		See " [Database Resource Quarantine](process-architecture.md) ".
- Optimizer Statistics Advisor
	This built-in diagnostic software analyzes how you are currently gathering statistics, the effectiveness of existing statistics gathering jobs, and the quality of the gathered statistics. Optimizer Statistics Advisor maintains rules, which embody Oracle best practices based on the current feature set. In this way, the advisor always provides the most up-to-date recommendations for statistics gathering.
	See " [Optimizer Statistics Advisor](concepts-for-database-administrators.md) ".

### Changes in Oracle Database 12c Release 1 (12.1.0.2)

Oracle Database Concepts for Oracle Database 12c Release 1 (12.1.0.2) has the following changes.

#### New Features

The following features are new in this release:

- In-Memory Column Store
	The In-Memory Column Store (IM column store) is an optional area in the SGA that stores whole tables, table partitions, and individual columns in a compressed columnar format. The database uses special techniques, including SIMD vector processing, to scan columnar data rapidly. The IM column store is a supplement to rather than a replacement for the database buffer cache.
	See " [In-Memory Area](memory-architecture.md) ".
- Automatic Big Table Caching
	This optional, configurable portion of the database buffer cache uses an algorithm for large tables based on object type and temperature. In single-instance and Oracle RAC databases, parallel queries can use the big table cache when the `DB_BIG_TABLE_CACHE_PERCENT_TARGET` initialization parameter is set to a nonzero value, and `PARALLEL_DEGREE_POLICY` is set to `auto` or `adaptive`. In a single-instance configuration only, serial queries can use the big table cache when `DB_BIG_TABLE_CACHE_PERCENT_TARGET` is set.
	See " [Buffer I/O](memory-architecture.md) ", and " [Buffer Pools](memory-architecture.md) ".

### Changes in Oracle Database 12c Release 1 (12.1.0.1)

Oracle Database Concepts for Oracle Database 12c Release 1 (12.1.0.1) has the following changes.

#### New Features

The following features are new in this release:

- Multitenant architecture
	The [multitenant architecture](glossary.md) capability enables an Oracle database to function as a [multitenant container database (CDB)](glossary.md). A CDB includes zero, one, or many customer-created pluggable databases (PDBs). A [PDB](glossary.md) is a portable collection of schemas, schema objects, and nonschema objects that appears to an Oracle Net client as a [non-CDB](glossary.md). You can unplug a PDB from a CDB and plug it into a different CDB.
	See " [Introduction to the Multitenant Architecture](introduction-to-the-multitenant-architecture.md) ".
- Multiprocess and multithreaded Oracle Database
	Starting with this release, Oracle Database may use operating system threads to allow resource sharing and reduce resource consumption.
	See " [Multiprocess and Multithreaded Oracle Database Systems](process-architecture.md) ".