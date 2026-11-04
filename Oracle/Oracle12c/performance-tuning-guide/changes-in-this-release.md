---
title: Database Performance Tuning Guide
book: Database Performance Tuning Guide
doc_id: E85600-04
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/tgdba/changes-in-this-release.html
tags:
  - oracle
  - 12c
  - performance-tuning-guide
---

This preface contains:

### Changes in Oracle Database 12c Release 2 (12.2.0.1)

The following are changes in Oracle Database Performance Tuning Guide for Oracle Database 12c Release 2 (12.2.0.1).

#### New Features

The following features are new in this release:

- Per-process PGA limits
	A runaway query consuming excessive amount of PGA memory can create a serious performance problem in Oracle Database. In a multitenant container database (CDB), this type of query can affect the performance of all the pluggable databases (PDBs). To prevent this issue, you can now specify an absolute limit for the amount of PGA memory that can be used by each session in a particular consumer group.
	See " [Sizing the Program Global Area Using the Resource Manager](tuning-program-global-area.md) "
- Prespawned server processes
	Oracle Database now prespawns pools of server processes when dedicated broker connection mode is enabled or threaded execution mode is enabled. This feature improves the client connection performance in these modes of database operation.
	See " [Improved Client Connection Performance Due to Prespawned Processes](configuring-database-for-performance.md) "
- Automatic Workload Repository (AWR) support for multitenant environment
	You can now capture Automatic Workload Repository (AWR) data for the PDBs in a multitenant environment. This feature enables performance tuning of PDBs in a multitenant environment.
	See " [Managing Automatic Workload Repository in a Multitenant Environment](gathering-database-statistics.md) "
- Automatic Workload Repository (AWR) support for Oracle Active Data Guard standby databases
	You can now capture Automatic Workload Repository (AWR) data for Oracle Active Data Guard standby databases. This feature enables performance tuning of Oracle Active Data Guard standby databases.
	See " [Managing Automatic Workload Repository in Active Data Guard Standby Databases](gathering-database-statistics.md) "
- Direct NFS Client performance improvement features - Parallel NFS and Direct NFS Dispatcher
	Parallel NFS is an optional feature of Oracle Direct NFS Client that is introduced in NFS version 4.1. This feature enables highly scalable distributed NAS storage for better I/O performance.
	The Direct NFS dispatcher feature consolidates the number of TCP connections that are created from a database instance to an NFS server. In large database deployments, using Direct NFS dispatcher improves scalability and network performance.
	See " [Improving I/O Performance Using Direct NFS Client](managing-operating-system-resources.md) "
- Service-oriented buffer cache access optimization
	Cluster-managed services allocate workloads across various Oracle Real Application Clusters (Oracle RAC) database instances. These services also access data from the Oracle RAC database instances and provide it to the applications requesting the data. The Service-oriented Buffer Cache Access Optimization feature allows Oracle RAC to cache service-specific data that is frequently accessed by each of these services, thus improving the data access time for the services. This data-dependent caching also leads to more consistent response times when accessing data across Oracle RAC database instances. This feature is permanently enabled in Oracle RAC.

### Changes in Oracle Database 12c Release 1 (12.1.0.2)

The following are changes in Oracle Database Performance Tuning Guide for Oracle Database 12c Release 1 (12.1.0.2).

#### New Features

The following features are new in this release:

- In-Memory Column Store
	The In-Memory Column Store (IM column store) is an optional area of the SGA that stores copies of tables, partitions, and other database objects in a columnar format that is optimized for rapid scans. IM column store accelerates database performance of analytics, data warehousing, and online transaction processing (OLTP) applications.
	See " [Using the In-Memory Column Store to Improve Query Performance](tuning-system-global-area.md) ".
- Manageability support for In-Memory Column Store
	SQL Monitor report, ASH report, and AWR report now show statistics for various in-memory operations.
- Force full database caching mode
	Force full database caching mode enables you to cache the entire database in memory, which may provide substantial performance improvements when performing full table scans or accessing LOBs.
	See " [Configuring the Database Caching Mode](tuning-database-buffer-cache.md) ".

### Changes in Oracle Database 12c Release 1 (12.1.0.1)

The following are changes in Oracle Database Performance Tuning Guide for Oracle Database 12c Release 1 (12.1.0.1).

#### New Features

The following features are new in this release:

- Real-Time ADDM
	Real-Time ADDM helps you to analyze and resolve problems in unresponsive or hung databases without having to restart the database.
	See " [Real-Time ADDM Analysis](automatic-performance-diagnostics.md) ".
- Limiting the size of the Program Global Area (PGA)
	The `PGA_AGGREGATE_LIMIT` initialization parameter enables you to specify a hard limit on PGA memory usage. Oracle Database ensures that the PGA size does not exceed this limit by terminating sessions or processes that are consuming the most PGA memory.
	See " [Limiting the Size of the Program Global Area](tuning-program-global-area.md) ".

#### Other Changes

The following are additional changes in the release:

- New books
	Oracle Database Performance Tuning Guide is undergoing a major rewrite for this release. As a result, the book structure has undergone significant changes. This book now contains only tuning topics that pertain to the database itself. All SQL-related tuning topics are moved to Oracle Database SQL Tuning Guide.