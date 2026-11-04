---
title: Configuring Oracle GoldenGate
book: High Availability Best Practices
doc_id: E10803-06
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e10803/config_gg.htm
tags:
  - oracle
  - 11g
  - high-availability-best-practices
---

## 10 Configuring Oracle GoldenGate

Oracle GoldenGate delivers low-impact, real-time data acquisition, distribution, and delivery across both homogeneous and heterogeneous systems. Oracle GoldenGate enables cost-effective and low-impact real-time data integration and continuous availability solutions across a wide variety of use cases. Oracle GoldenGate offers close integration with Oracle technologies and applications, support for additional heterogeneous systems, and improved performance.

This chapter contains the following topics:

## 10.1 Oracle GoldenGate Overview

Oracle GoldenGate captures primary database changes by reading redo records from a source database online redo log file, transforming those records into a platform independent trail file format, and transmitting the trail file to a target database(s). Oracle GoldenGate maintains a logical replica by converting the trail file into SQL and applying SQL to a target database. A target database is open read/write while synchronization occurs. Additional Oracle GoldenGate information can be found at

`http://www.oracle.com/us/products/middleware/data-integration/goldengate/index.html`

Oracle GoldenGate is ideally used where its flexibility can address advanced requirements not addressed by other MAA features. Oracle GoldenGate is an important element in the MAA architecture, useful for the following purposes:

- Active-Active multi-master configurations used for data availability and to scale performance. An important consideration for such configurations is the ability to manage update conflicts either by avoiding them or by implementing a process for conflict detection and resolution.
- Offload operational reporting when read/write access to the reporting instance is required.
- Near zero downtime (one-way replication) or zero downtime (bi-directional replication) for planned maintenance tasks, including:
	- Database upgrades
		- Application upgrades that modify back-end database objects (requires the user to implement transformations to map old and new versions.
		- Database consolidation
		- Database and platform migrations

### 10.1.1 Oracle GoldenGate and Oracle Streams

Oracle GoldenGate is a direct replacement for Oracle Streams in the Oracle MAA Architecture. Oracle GoldenGate replaces Oracle Streams because it offers similar advanced replication capabilities in an all-Oracle environment combined with extensive support for replication across heterogeneous database management systems. Oracle GoldenGate offers customers the opportunity to simplify their environment by standardizing on a single horizontal replication technology for all platforms. Oracle recommends that customers consider Oracle GoldenGate when implementing new replication projects to benefit from Oracle's ongoing investment in this technology.

Oracle Streams users can continue to expand existing Streams implementations with the confidence that Oracle will protect their investment through continued support of the Streams product. For more information about Oracle Streams, see the Oracle Streams area at:

`http://www.oracle.com/technetwork/database/focus-areas/data-integration/index.html`

### 10.1.2 Oracle GoldenGate and Oracle RAC

Oracle GoldenGate active-active replication can be used for both High Availability and to scale performance by balancing workload across multiple synchronized replicas of an Oracle Database. Using Oracle GoldenGate for this purpose requires:

- Redundant copies of the Oracle database
- Supplemental database logging
- Replication overhead from capture and apply processes on each database
- Conflict detection and resolution
- Client notification/redirection in the event of a database outage
- Meeting all prerequisites for logical replication

In contrast, Oracle RAC provides High Availability and scalable performance by balancing workload across multiple servers having shared access to a single copy of the Oracle database. Oracle RAC includes integrated methods of client notification and redirection and has no additional processing or prerequisites required by logical replication. For these reasons Oracle RAC is the preferred method for implementing High Availability and scaling performance for the Oracle Database. Oracle GoldenGate is often used with Oracle RAC for maintenance or migrations, or as a method for distributing subsets of a source database across remote geographic locations to provide local read/write access or to create a local read/write replica for offloading reporting applications (when such applications require read/write access to the database).

### 10.1.3 Oracle GoldenGate and Oracle Data Guard/Oracle Active Data Guard

Oracle GoldenGate is Oracle's strategic logical replication product. Oracle Data Guard is Oracle's strategic physical replication product focused on data protection and data availability, and is the standard MAA recommendation for such purposes because of the advantages it offers over logical replication. Oracle Data Guard is also commonly used in place of storage-remote mirroring or host-based mirroring solutions for disaster protection. Oracle Data Guard also minimizes planned downtime by supporting database rolling upgrades, select migrations (for example, Windows to Linux), data center moves, and other types of planned maintenance. Oracle Active Data Guard, an extension to Oracle Data Guard, is the simplest, fastest, most efficient method of maintaining a synchronized physical replica of a source database open read-only for offloading read-only workload and backups. For a detailed discussion of Data Guard advantages for data protection, see the Product Technical Brief, "Oracle Active Data Guard and Oracle GoldenGate" available from the GoldenGate link at

`http://www.oracle.com/technetwork/database/features/availability/index.html`

Oracle GoldenGate is often used in Data Guard configurations in a complementary manner. A Data Guard physical standby provides data protection and availability while Oracle GoldenGate capture processes are configured at either the primary database, or at the standby database (using ALO mode), to distribute data to one or more target databases, either Oracle or non-Oracle, to address advanced replication requirements. Oracle GoldenGate can also be used in place of Oracle Data Guard for requirements where its advantages outweigh Oracle Data Guard's specialized capabilities for data protection, high availability, and disaster recovery, and when all prerequisites for logical replication can be met. Such use-cases include:

- When read/write access to the target database is required, either to implement multi-master replication, or to offload packaged reporting applications that require read/write access to the target database
- For planned maintenance or migrations in heterogeneous environments not supported by Oracle Data Guard
- For additional flexibility during planned maintenance to replicate downward from a new Oracle Database or application version to the previous version, for fast switchback should unforeseen problems be encountered
- To maintain availability through application upgrades that modify back-end database objects

### 10.1.4 Oracle GoldenGate and Edition-Based Redefinition

Edition-based redefinition is a capability implemented entirely within Oracle Database that enables database objects that implement the back end of an application to be patched or upgraded without interrupting the availability of the application. Edition-based redefinition enables customers to implement application upgrades online with zero database downtime. Edition-based redefinition requires Oracle Database 11g Release 2, and it requires application changes; an application must be made editionable to upgrade online.

Oracle GoldenGate can also be used for online application upgrades. The application itself does not need to be modified to implement an upgrade, but the administrator must have sufficient knowledge of the differences between old and new versions of the application to implement mapping between versions using Oracle GoldenGate. User control over the application, and user preference for the second major distinction between these technologies determines which approach makes the most sense to achieve a zero downtime application upgrade.

The second major difference between these technologies is that edition-based redefinition uses only the single database that ordinarily supports the application. Oracle GoldenGate uses a second synchronized database to execute the upgrade.

- Using edition-based redefinition, the old version of the application is in the old edition and the new version of the application is in the new edition - both within the same database; the edition is the isolation mechanism. Data that is represented the same in the old and the new versions of the application is represented only once in table columns used by both versions; only data that is represented differently in the two application versions must exist twice. Synchronization is needed, therefore, only for that typically small proportion of the total data that differs between the two versions. Because a cross edition trigger fires within a transaction, potential conflicts between the old and the new representations are prevented before they can be committed, and there is no need for conflict-resolution.
- Using Oracle GoldenGate, the old version of the application runs on the original database and the new version of the application runs on a second database; the second database is the isolation mechanism. All data - both that which is represented the same in the old and the new versions of the application and that which is represented differently in the two application versions must exist twice. Synchronization is needed, therefore, for all the data. The synchronization is implemented using code that intervenes in the replay mechanism for the SQL that is constructed by mining the redo logs. It is, therefore, non-transactional; and conflicts between the old and the new representations cannot be prevented. Rather, conflict-resolution must be implemented as an explicit, post-processing step.

## 10.2 Oracle GoldenGate Configuration Best Practices

There are several best practices for configuring GoldenGate Extract, Data pump and Replicat for optimal performance and High Availability to reduce increased latencies caused by downtime of GoldenGate processes, including the following:

- Use of a Clustered File System
- Improved ASM Log File Read API
- Replicat Commit Behavior
- Oracle Clusterware Configuration
- Additional Oracle GoldenGate Best Practices

### 10.2.1 Use of a Clustered File System

Using a clustered file system is fundamental to the continuing availability of Oracle GoldenGate checkpoint and trail files in the event of a node failure. Ensuring the availability of the checkpoint files is essential to ensure that, after a failure occurs, the Extract process can continue mining from the last known archived redo log file position and Replicat processes can start applying from the same trail file position before a failure occurred. Using Oracle Database Filesystem (DBFS) or Oracle Automatic Storage Management Cluster File System (Oracle ACFS) allows a surviving database or ASM instance to be the source of an Extract process or destination for the Replicat processes.

Best practices for configuring DBFS or Oracle ACFS for use with Oracle GoldenGate are described in each of the following references.

Note:

The best practices provided in the following documents apply to all supported Oracle GoldenGate platforms, including Oracle Exadata Database Machine.

See:

- See "DBFS Configuration Best Practices for use with Oracle GoldenGate" in My Oracle Support Note 1319042.1 at
	`https://support.oracle.com/CSP/main/article?cmd=show&type=NOT&id=1319042.1`
- Product Technical Brief, "Oracle GoldenGate on Sun Oracle Database Machine" from the GoldenGate link at
	`http://www.oracle.com/technetwork/database/features/availability/index.html`

### 10.2.2 Improved ASM Log File Read API

Oracle GoldenGate 11g introduces a new optimized method of reading log files stored in Oracle ASM. This new method uses the database server to access the redo and archived redo log files, instead of connecting directly to the Oracle ASM instance. The database must contain the libraries with the API modules. The libraries are currently included with Oracle Database release 10.2.0.5 and 11.2.0.2. For information for accessing the API modules for other releases, see "Optimized Access for Oracle GoldenGate to Redo Log Files in ASM - for Oracle Database Releases other than 10.2.0.5 and 11.2.0.2" in My Oracle Support Note 1333171.1 at

`https://support.oracle.com/CSP/main/article?cmd=show&type=NOT&id=1333171.1`

See Also:

Oracle GoldenGate Windows and UNIX Reference Guide (v11.1.1.1) for more information about extract `TRANLOGOPTIONS` `DBLOGREADER` parameter

### 10.2.3 Replicat Commit Behavior

If you are using Oracle GoldenGate version 11.1.1 or lower it is recommended that you set the Replicat commit behavior to `COMMIT` `NOWAIT`. The Replicat processes does not wait at each commit when applying transactions, increasing throughput performance. This should only be considered when using a checkpoint table due to protection of recovery data during a checkpoint.

If using Oracle Database 11g Release 1 (11.1) or an earlier release, set the Replicat parameter file to `COMMIT` `NOWAIT` as follows:

Set the Replicat parameter file to `COMMIT` `NOWAIT` as follows:

```
SQLEXEC "ALTER SESSION SET COMMIT_WRITE='NOWAIT'";
```

For Oracle Database 11g Release 2 (11.2) and newer Oracle Database releases, set the Replicat parameter file to `COMMIT` `NOWAIT` as follows:

```
SQLEXEC "ALTER SESSION SET COMMIT_WAIT='NOWAIT'";
```

Starting in GoldenGate v11.1.1.1 `COMMIT` `NOWAIT` is the default behavior when using a checkpoint table.

### 10.2.4 Oracle Clusterware Configuration

Running Oracle GoldenGate within an Oracle RAC environment provides the ability to reduce downtime due to server failure. Oracle Clusterware can be configured such that, if a node fails, the Oracle GoldenGate processes automatically start on a surviving node. This way the Extract can continue mining the redo logs or the Replicat can continue applying from the last recorded checkpoint.

Note:

If you are using an Oracle GoldenGate Data pump process (release v11.1.1 or earlier) to transfer the trail files from a source host on the database machine using DBFS (this applies to the Exadata Database Machine and to non-Exadata configurations), see "Oracle GoldenGate Best Practices: Oracle GoldenGate high availability using Oracle Clusterware" in My Oracle Support Note 1313703.1 at

`https://support.oracle.com/CSP/main/article?cmd=show&type=NOT&id=1313703.1`

See Also:

For more detailed instructions to configure Oracle Clusterware with GoldenGate, see the product technical brief, "Oracle GoldenGate High Availability using Oracle Clusterware" from the GoldenGate link at

`http://www.oracle.com/technetwork/database/features/availability/index.html`

### 10.2.5 Additional Oracle GoldenGate Best Practices

Oracle GoldenGate configuration best practices continue to evolve with enhanced Oracle integration. For updates and information about best practices for all components, visit the MAA website at

`http://www.oracle.com/goto/maa`

Current best practices include:

- See "Oracle GoldenGate database Schema Profile check script for Oracle Database" in My Oracle Support Note 1296168.1 at
	`https://support.oracle.com/CSP/main/article?cmd=show&type=NOT&id=1296168.1`
- See "Oracle GoldenGate database Complete Database Profile check script (All Schemas)" in My Oracle Support Note 1298562.1 at
	`https://support.oracle.com/CSP/main/article?cmd=show&type=NOT&id=1298562.1`
- The product technical briefs:
	- Zero-Downtime Database Upgrades Using Oracle GoldenGate
		- Best Practices for Conflict Detection and Resolution in Active-Active Database Configurations Using Oracle GoldenGate
	available from the GoldenGate link at
	`http://www.oracle.com/technetwork/database/features/availability/index.html`

## 10.3 Oracle GoldenGate Operational Best Practices

See the following documents for more information about Oracle GoldenGate management and operational Best Practices:

- Oracle GoldenGate For Windows and UNIX Administrator's Guide
- Oracle GoldenGate For Windows and UNIX Troubleshooting and Tuning Guide
- See "Oracle GoldenGate - Heartbeat process to monitor lag and performance in GoldenGate" in My Oracle Support Note 1299679.1 at
	`https://support.oracle.com/CSP/main/article?cmd=show&type=NOT&id=1299679.1`
- See, "Oracle GoldenGate Best Practices: Oracle GoldenGate Veridata" in My Oracle Support Note 1312092.1 at
	`https://support.oracle.com/CSP/main/article?cmd=show&type=NOT&id=1312092.1`