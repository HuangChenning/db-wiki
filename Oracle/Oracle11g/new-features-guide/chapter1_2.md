---
title: Oracle Database 11g Release 2 (11.2.0.2) New Features
book: New Features Guide
doc_id: E41360-06
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e41360/chapter1_2.htm
tags:
  - oracle
  - 11g
  - new-features-guide
---

## 3 Oracle Database 11g Release 2 (11.2.0.2) New Features

This chapter contains descriptions of all of the features that are new to Oracle Database 11g Release 2 (11.2.0.2).

## 3.1 General

The following sections describe the new features for Oracle Database 11g Release 2 (11.2.0.2).

### 3.1.1 General

The following sections provide information on new features for 11.2.0.2.

#### 3.1.1.1 Control File Updates Can Be Disabled During NOLOGGING Operations

Parameter `DB_UNRECOVERABLE_SCN_TRACKING = [ TRUE | FALSE ]` can be used to turn off control file writes to update fields that track the highest unrecoverable SCN and Time during a `NOLOGGING` direct path operation.

Performance of the `NOLOGGING` load operation could be limited by the control file write I/O.

#### 3.1.1.2 New Package for Configuring Automatic SQL Tuning

A new PL/SQL package, `DBMS_AUTO_SQLTUNE`, has been introduced to provide more restrictive access to the Automatic SQL Tuning feature.

With this package, access to Automatic SQL Tuning can be restricted to DBAs so that only they can change its configuration settings that effect run-time behavior of the query optimizer, such as enabling or disabling automatic SQL profile creation.

See Also:

[Oracle Database Performance Tuning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41573/toc.htm) for details

#### 3.1.1.3 Enhanced Security for DBMS\_SCHEDULER E-Mail Notification

Encryption and authentication have been added to the Oracle Scheduler's e-mail notification feature.

E-mail notification on job failures was added in 11.2.0.1, but it did not support those e-mail servers that require either encryption or authentication. This feature adds this support in 11.2.0.2.

See Also:

[Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/toc.htm) for details

#### 3.1.1.4 Enhanced TRUNCATE Functionality

While truncating a table or partition, you can now specify whether or not to keep any segments. Truncating a table or partition with the new extended syntax removes all segments and does not use any space until new data is inserted.

All allocated space in a database can now be reclaimed by truncating tables or partitions with the new extended syntax, optimizing the space foot print of any application.

See Also:

[Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/toc.htm) for details

#### 3.1.1.5 Support for In-Place Upgrade of Clients

Both in-place and out-of-place upgrades are supported for client installations.

You now have the option of doing in-place client upgrades reducing the need for extra storage and simplifying the installation process.

See Also:

[Oracle Database Client Installation Guide for Linux](https://docs.oracle.com/cd/E11882_01/install.112/e24322/toc.htm) for details

#### 3.1.1.6 Maintenance Package for Segment Creation on Demand

Customers can manage the space allocation of any application through extended functionality of the `DBMS_SPACE_ADMIN` package. This package can be used to remove the segments for all empty tables in a database, a user schema, or for specific tables. This package also provides the opposite functionality to materialize all segments for empty tables or partitions with deferred segment creation

The explicit management of deferred segment creation enables you to take advantage of this functionality at any given point in time, even after table or partition creation. This is especially useful for systems that were upgraded in-place and makes a re-creation of all empty objects unnecessary.

See Also:

[Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/toc.htm) for details

#### 3.1.1.7 Maximum CPU Utilization Limit

Resource Manager provides a new directive called `MAX_UTILIZATION_LIMIT` that allows you to place a hard limit on the amount of CPU utilized by a consumer group.

The `MAX_UTILIZATION_LIMIT` directive is useful for limiting the CPU utilization of low priority workloads. This directive is also useful for providing more consistent performance for the workload in a consumer group, and it helps to build systems where end users experience consistent response times for each database operation.

See Also:

[Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/toc.htm) for details

#### 3.1.1.8 Name Matching

This feature provides an efficient method for matching proper names (and words) that take a query as input and returns a ranked list of matches. The new operator `NDATA` is introduced for this functionality.

In today's multicultural society, a person accustomed to the spelling rules of one demographic may have difficulty applying those same rules to a name originating from a different culture.

Name matching provides a solution to match proper names that might differ in spelling due to orthographic variation.

See Also:

[Oracle Text Reference](https://docs.oracle.com/cd/E11882_01/text.112/e24436/toc.htm) for details

#### 3.1.1.9 Named Entity Extraction

Entity extraction is the recognition of entity names (people and organizations), places, temporal expressions, and types of numerical expressions such as currencies and measures.

The goal of entity extraction is to identify instances of a particular pre-specified class of entities in textual documents.

The benefit is to produce a "structured" view of a document that can later be used for text or data mining and more comprehensive intelligence analysis.

See Also:

[Oracle Text Reference](https://docs.oracle.com/cd/E11882_01/text.112/e24436/toc.htm) for details

#### 3.1.1.10 Default Size of First Extent of Any New Segment for a Partitioned Table Has Changed

The default size of the first extent of any new segment for a partitioned table is now 8 MB instead of 64 K.

The goal is to improve I/O performance. However, under certain circumstances, loading a table will take significantly more disk space.

See Also:

[Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/tables.htm#ADMIN11635) for details

#### 3.1.1.11 Parallel Statement Queuing

Parallel Statement Queuing ensures all statements run on a system get the appropriate parallel resources to perform well by allowing you to ensure that a system is neither overwhelmed nor starved for parallel server processes. Queuing can be implemented per resource group and allows for both prioritization of statements and the above mentioned management of a parallel workload. Parallel Statement Queuing works in conjunction with Automatic Degree of Parallelism.

Data Warehouses are evolving into systems that support both operational environments and the more classic strategic data warehouse workloads. These mixed workloads require active workload management. One of these resources that should be managed as part of the workload management process is the use of Parallel Server Processes. Parallel server resources are allocated by Automatic Degree of Parallelism (DOP). Statement queuing is then used to ensure that each statement can run with the optimal DOP within the system limits. Allowing each statement to run with the optimal DOP allows a system to:

- Perform well overall and avoid large wait times on system resources.
- Utilize all resources in an optimal manner without trashing the system in peak times or due to runaway queries.
- Balance overall performance to be much more predictable.
- Allocate appropriate resources based on policies, not based on user abuse.

See Also:

[Oracle Database VLDB and Partitioning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25523/parallel002.htm#VLDBG14020) for details

#### 3.1.1.12 PMML Import

This release adds support for importing external data mining models (linear and binary logistic regression) using the Data Mining Group Predictive Model Markup Language (PMML) standard. The imported models become native Oracle Data Mining (ODM) models capable of Oracle Exadata offload.

If you use an external data mining product to generate models, you could encounter difficulty when deploying those models into their production databases. The current process of deploying such models is expensive, error prone, and non-performant. This feature streamlines the movement of external models into production Oracle systems and leverages optimized performance of the ODM option.

See Also:

[Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/d_datmin.htm#ARPLS72987) for details

#### 3.1.1.13 Result Set Interface

The client interface `CTX_QUERY.RESULT_SET` runs a query and generates a result set. The components of the result set are:

- Documents.
- Support order by `SDATA`.
- A total estimated count of number of matching documents.
- A count, broken down by metadata value, of matching documents in each category.

A page of search results consist of many disparate elements (for example, metadata of the first few documents, snippet, total hit counts, and so on). Instead of accessing the database to construct bits of the search results, it would be useful to have a clean result set mechanism. The result set interface is able to produce the various kinds of data needed for a page of search results all at once, improving performance by sharing overhead. The result set interface can also return data views which are difficult to express in SQL, such as top `n` by category queries.

See Also:

[Oracle Text Application Developer's Guide](https://docs.oracle.com/cd/E11882_01/text.112/e24435/toc.htm) for details

#### 3.1.1.14 Segment Creation On Demand for Partitioned Tables

The initial segment creation for partitioned tables and indexes can be deferred until data is first inserted into an object. Individual partitions will not be physically created before data is inserted for the first time.

Several prepackaged applications are delivered with large schemas containing many partitioned tables and indexes. With deferred segment creation for partitioned tables, empty database objects do not consume any space, reducing the installation footprint and speeding up the installation.

See Also:

[Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/toc.htm) for details

#### 3.1.1.15 Simplification of XML and XQuery Interfaces

This feature extends the XQuery 1.0 standard's operator `fn:doc` and `fn:collection` to allow direct access to collections of XML documents stored in the database.

Direct access to XML content in tables and views is provided by extending `fn:doc` and `fn:collection` to support DBUri-style paths through the pseudo protocol `xdb://`.

Simplification of Oracle XML and XQuery interfaces provides standard mechanisms, allows building of portable XML applications that are easier to maintain, and deprecates redundant or unused functionality.

See Also:

[Oracle XML DB Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e23094/xdb_xquery.htm#ADXDB1700) for details

#### 3.1.1.16 SMTP Authentication

Starting with this release, you can configure the `UTL_SMTP` PL/SQL package for use on both Transport Layer Security (TLS) and Secure Sockets Layer (SSL) servers."

This allows the package to be used to send to SMTP servers that require authentication to combat spam.

See Also:

[Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/toc.htm) for details

#### 3.1.1.17 SMTP Encryption

`UTL_SMTP` is extended in this release to provide Secure Sockets Layer (SSL) and Transport Layer Security (TLS) support.

This allows the package to be used to send to SMTP servers using SSL and TLS to ensure channel integrity.

See Also:

[Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/toc.htm) for details

#### 3.1.1.18 SPA Support for Active Data Guard Environment

If you are using Oracle Active Data Guard physical standby database, you already have full dataset or clone or both of the production environment that can be leveraged for testing with SQL Performance Analyzer (SPA). Using remote test execution SPA trial method, you can connect to a physical standby database in read-only mode and use it for testing. The physical standby database continues to be in read-only and standby mode (changes are being applied) during SPA testing. The SPA analysis and reports are available from the remote database that is orchestrating the SPA trials. The orchestrating database (SPA system) can be the primary database or any remote database running Oracle Database 11g and higher releases.

This feature allows customers to leverage existing Active Data Guard physical standby databases for SQL Performance Analyzer Testing.

See Also:

[Oracle Database Testing Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41481/toc.htm) for details

#### 3.1.1.19 The EDITION Attribute of a Database Service

The `EDITION` attribute of a database service specifies the initial session edition for a session that is started using that service. If the program that creates a new session does not specify the initial session, then the edition name specified by the service is used. If the service does not specify the edition name, then the initial session edition is the database default edition.

When an edition-based redefinition exercise is implemented to support hot rollover, some clients to the database will want to use the pre-upgrade edition and others will want to use the post-upgrade edition. In this scenario, the database default edition is insufficient because, by definition, it denotes a single edition. The `EDITION` attribute of a database service provides a way to allow the client to specify the edition it wants using environment data rather than by changing the client code.

See Also:

[Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/toc.htm) for details

#### 3.1.1.20 Using Binary XML with SecureFiles as the XMLType Default Storage

In this release, the default storage model has changed for XMLType from `STORE AS CLOB` to `STORE AS SECURE FILE BINARY XML`. This affects the storage used when an explicit `STORE AS` clause is not supplied when creating an XMLType table or column. Not specifying a `STORE AS CLAUSE` indicates that it is left to the database to determine what the optimal storage model should be.

Prior to database release 11.2.0.2, the default storage model was `STORE AS BASICFILE CLOB`. In 11.2.0.2, the default is changed to `STORE AS SECUREFILE BINARY XML`.

This change requires the installation of the XDB feature in order to work correctly. Customers that choose not to install the XDB feature must explicitly add `STORE AS CLOB` to any DLL statements that create XMLType table or columns to avoid DDL errors. Note that the use of XMLType without having the XDB installed is not a supported configuration as of 11.1.0.1.

No data migration takes place when databases are upgraded to 11.2.0.2.

Binary XML with SecureFiles provides efficient storage, retrieval, and DML capabilities for semi-structured and unstructured XML data. Changing the default storage for XMLType to binary XML with SecureFiles helps customers to adopt best practices.

See Also:

[Oracle XML DB Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e23094/whatsnew.htm#ADXDB5975) for details

#### 3.1.1.21 JDBC 4.0 SQLXML

This feature implements the JDBC 4.0 specification of the `SQLXML` interface for managing the XML data type in the database.

This feature allows Java applications using JDBC-Thin or JDBC-OCI to manage the XML data type in the database, using the standard `SQLXML` type (`java.sql.SQLXML`).

See Also:

[Oracle Database JDBC Developer's Guide](https://docs.oracle.com/cd/E11882_01/java.112/e16548/toc.htm) for details

#### 3.1.1.22 ID Key LCRs in XStream

ID key LCRs enable an XStream client application to process changes to rows that include unsupported data types. ID key LCRs do not contain all of the columns for a row change. Instead, they contain the rowid of the changed row, a group of key columns to identify the row in the table, and the data for the scalar columns of the table that are supported by XStream Out. ID key LCRs do not contain columns for unsupported data types.

This feature enables XStream users to capture database changes that cannot be supported using Oracle Streams.

See Also:

[Oracle Database XStream Guide](https://docs.oracle.com/cd/E11882_01/server.112/e16545/xstrm_cncpt.htm#XSTRM72577) for details

### 3.1.2 ACFS Improvements

The following sections provide information on ACFS improvements for 11.2.0.2.

#### 3.1.2.1 ACFS, ADVM and Snapshots on Solaris and AIX

Oracle ACFS, Oracle ASM Dynamic Volume Manager (Oracle ADVM) and Snapshots were delivered in Oracle Database 11g Release 2 (11.2.0.1) on Windows NT and Linux platforms.

Oracle Database 11g Release 2 (11.2.0.2) now provides a general purpose cluster file system which leverages the capabilities of Oracle ASM on Solaris and AIX platforms.

See Also:

[Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e18951/asmfs_util003.htm#OSTMG92400) for details

#### 3.1.2.2 Oracle ACFS Replication

The Oracle Automatic Storage Management Cluster File System (Oracle ACFS) Replication feature supports asynchronous replication of an ACFS file system from a primary to standby site.

The Oracle ACFS Replication feature allows you to replicate ACFS file systems across the network to another (possibly distant) site. This provides a disaster recovery capability for the file system. This feature can be used in conjunction with Oracle Data Guard to replicate all Oracle data.

See Also:

[Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e18951/asmfilesystem.htm#OSTMG34600) for details

#### 3.1.2.3 Oracle ACFS Security and Encryption Features

Oracle ASM Cluster File System (Oracle ACFS) security feature provides realm-based security for Oracle ACFS.

Oracle ACFS encryption feature enables data stored on disk (data-at-rest) to be encrypted.

Oracle ACFS security feature provides the ability to create realms to specify security policies for users or groups for accessing file system objects. The Oracle ACFS security feature provides a finer-grained access control on top of the access control provided by the operating system.

Oracle ACFS encryption feature provides the ability to keep data in an Oracle ACFS file system in encrypted format to prevent unauthorized use of data in the case of data loss or theft.

See Also:

[Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e18951/asmfilesystem.htm#OSTMG34500) for details

#### 3.1.2.4 Oracle ACFS Tagging

The Oracle ACFS Tagging feature provides a method for relating a group of files based on a common naming attribute assigned to these files called a tag name.

You can use this feature alone or in conjunction with other features. For example, in conjunction with Oracle ACFS Replication, you can select specific files that you would like to replicate to a different remote cluster site by assigning a unique tag name to them. You would then instruct Oracle ACFS Replication to replicate files based upon this tag name. By using tagging in this respect, the need to replicate entire Oracle ACFS file systems is reduced.

See Also:

[Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e18951/asmfilesystem.htm#OSTMG34700) for details

### 3.1.3 Quality of Service (QoS) Management

A new Quality of Service (QoS) Management Server enables run time management of service levels for hosted database applications on a shared infrastructure by cluster administrators. The goal is to present an easy-to-use, policy-driven management system that ensures meeting service levels if sufficient resources are available and when they are not, allocates resources to the most business critical workloads not meeting their service levels at the expense of the less critical ones.

The following sections describe Quality of Service Management Server features.

#### 3.1.3.1 Database QoS Management Server

The Database Quality of Service (QoS) Management Server allows system administrators to manage application service levels hosted in Oracle Database clusters by correlating accurate run-time performance and resource metrics and analyzing with an expert system to produce recommended resource adjustments to meet policy-based performance objectives.

The Database QoS Management Server enables the pooling of resources to help ensure that, when sufficient resources are available, performance and availability objectives are met, even under demand surges. Managing resource allocations to match performance objectives using a set of predefined policies, the Database QoS Management Server greatly reduces system administrator and DBA time and expertise. By continuously monitoring the system performance based on real demand, it quickly identifies bottlenecks and potential problems that can be corrected before an actual outage occurs. This system cuts time to resolve service level violations as it provides detailed metrics and bottleneck identification along with recommendations for resolution. The end result is the stakeholders trust to share resources thus reducing capital and operational expenses.

See Also:

[Oracle Database Quality of Service Management User's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e24611/apqos_intro.htm#APQOS109) for details

#### 3.1.3.2 Database Quality of Service (QoS) Management Support

To support the Database Quality of Service (QoS) Management Server, the Oracle Database Resource Manager and metrics have been enhanced to support fine-grained performance metrics and now have the ability to manage workloads by user-defined performance classes.

By supporting the Database QoS Management Server, applications sharing a single database or multiple databases within a cluster can be managed discretely to monitor and maintain their service levels. This consolidation reduces hardware, software and management costs while maintaining business objectives.

See Also:

[Oracle Database Quality of Service Management User's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e24611/apqos_intro.htm#APQOS111) for details

#### 3.1.3.3 Enterprise Manager QoS Management Integration

The administration of the Database Quality of Service (QoS) Management Server is integrated into the new Cluster Administration section of Enterprise Manager. This is designed as a task-based interface to create policy sets using a wizard, manage application service levels using a dashboard, and monitor performance through historical graphs, logs and alerts.

This feature provides full task-based integration into Enterprise Manager, simplifying the administration tasks necessary to manage database application service levels using the Database QoS Management Server. It both reduces task and troubleshooting time as well as the level of training required thus reducing costs while maintaining application availability.

See Also:

[Oracle Database Quality of Service Management User's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e24611/apqos_admin.htm#APQOS159) for details

#### 3.1.3.4 Server Memory Stress Protection for Oracle Clusters

When QoS Management is enabled and managing an Oracle Clusterware server pool, it receives a metrics stream from the Cluster Health Monitor that provides real-time memory data including the amount available, in use, and swapped to disk for each server. Should a node be determined to be under memory stress, the CRS-managed database services are stopped on that node preventing new connections from being created thereby protecting existing sessions. Once the memory stress is relieved (for example, by either existing sessions closing or user intervention), the services are restarted automatically and the listener begins sending opening connections on that server.

Enterprise database servers can run out of available memory due to too many sessions or runaway workloads. This can result in failed transactions or, in extreme cases, a reboot of the server and loss of a valuable resource. Oracle Database QoS Management detects memory pressure in real-time and prevents the addition of new sessions from exhausting available memory thus protecting existing workloads and the availability of the server. This adds a new resource protection capability in managing Service Levels for Oracle RAC database-hosted applications.

### 3.1.4 Database Replay

The following sections provide information on new Database Replay features for 11.2.0.2.

#### 3.1.4.1 Database Replay SQL Performance Analyzer (SPA) Integration

This feature allows you to perform SQL Tuning Set (STS) capture and workload capture or replay at the same time in a single process. STS is automatically exported when the AWR data for the capture or replay is exported into the specified directory object. By integrating SPA and Database Replay, you can analyze SQL-centric issues in the workload more easily than if they were to do this manually in separate steps. An SPA report can be generated at the end of workload replay to facilitate SQL-centric analysis. Oracle RAC is not yet supported.

Integration of SPA and Database Replay features provides the ability to perform SQL Tuning Set and workload capture or replay in one process and at the same time. As a result, an SPA report is available to help with SQL-centric analysis when workload replay is done.

See Also:

[Oracle Database Testing Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41481/toc.htm) for details

#### 3.1.4.2 Database Replay Timeout Function

During workload replay, it is sometimes possible that due to an execution plan, system change or otherwise, a replay call may hang or take a long time. You can specify a replay timeout parameter. If the call exceeds the timeout, that particular call is aborted. This is useful with workloads when one or a few calls result in the workload replay to run too long or hang. Aborting these will still provide a useful workload replay.

Database Replay timeout functionality provides the ability to control how long a long running or runaway replay call will take. Without this functionality, a replay call may take a long time or hang depending on the situation.

See Also:

[Oracle Database Testing Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41481/toc.htm) for details

#### 3.1.4.3 Database Replay Workload Analyzer

Database Replay Workload Analyzer is a tool that analyzes a captured workload and provides an assessment of how reliably it can be replayed. It highlights any potential problems that might be encountered during replay by outlining the parts that cannot be replayed accurately due to insufficient data, errors during capture, and usage of features that are unsupported by Database Replay.

This feature tells you, at the time of capture, whether the specific workload captured is something that can be relied upon for future testing.

See Also:

[Oracle Database Testing Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41481/toc.htm) for details

### 3.1.5 Management

The following sections provide information on new management features for 11.2.0.2.

#### 3.1.5.1 DBCA Support for Creating an Oracle RAC One Node Database

Support has been added in this release to Oracle Database Configuration Assistant (DBCA) to create an Oracle Real Application Clusters One Node (Oracle RAC One Node) database as part of the database creation process.

Oracle RAC One Node is a new option to the Oracle Enterprise Edition introduced with the Oracle Database 11.2.0.1. Oracle DBCA now recognizes Oracle RAC One Node databases and provides the required configuration options to ease the management of Oracle RAC One Node.

See Also:

[Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41960/onenode.htm#RACAD7894) for details

#### 3.1.5.2 Option of Downloading Latest Updates During Installation

This feature allows the installer to download mandatory patches for itself as well as for the base product at installation time so that they do not need to be applied later. It also helps resolve installation issues at the middle of a release without either recutting the media or deferring the bug fix to a later release.

Currently, when there is a bug in the base installation, you have to wait until the next release before it can be fixed. This feature helps resolve installation issues at the middle of a release without either recutting the media or deferring the bug fix to a later release. The feature also applies mandatory patches for the base product, thereby creating more certified installations out-of-box.

See Also:

[Oracle Database Installation Guide for Linux](https://docs.oracle.com/cd/E11882_01/install.112/e47689/toc.htm) for details

#### 3.1.5.3 Oracle ASM Configuration Assistant Support for Out-of-Place Upgrades

Oracle Grid Infrastructure for a Cluster 11g Release 2 supports out-of-place upgrades. The Oracle ASM Configuration Assistant (ASMCA) now fully supports out-of-place upgrades to this new release.

The graphical user interface (GUI) provides a simple interactive method for upgrading environments to this new release. To allow scripting, the assistant also provides an on-interactive method (silent) mode, which addresses various deployment scenarios used by customers.

See Also:

[Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e18951/asminst.htm#OSTMG53000) for details

#### 3.1.5.4 Oracle Database Upgrade Assistant Support for Out-of-Place Upgrades

Oracle Grid Infrastructure for a Cluster 11g Release 2 supports out-of-place upgrades. The Database Upgrade Assistant (DBUA) now fully supports out-of-place upgrades to this new release.

The graphical user interface (GUI) provides a simple interactive method for upgrading environments to this new release. To allow scripting, the assistant also provides an on-interactive method (silent) mode, which addresses various deployment scenarios used by customers.

See Also:

[Oracle Database Upgrade Guide](https://docs.oracle.com/cd/E11882_01/server.112/e23633/upgrade.htm#UPGRD12387) for details

#### 3.1.5.5 Oracle Enterprise Manager DB Control Support for Oracle RAC One Node

Oracle Enterprise Manager DB Control provides support for Oracle RAC One Node databases.

Oracle RAC One Node is a new option to the Oracle Enterprise Edition introduced with the Oracle Database 11.2.0.1. Oracle Enterprise Manager DB Control now recognizes Oracle RAC One Node databases and provides the required configuration options in an easy-to-use graphical user interface (GUI), which simplifies the management of Oracle RAC One Node beyond the scope of the command-line tools that are already available.

#### 3.1.5.6 Online Relocation of an Oracle RAC One Node Database

Oracle RAC One Node allows the online relocation of an Oracle RAC One Node database from one server to another. The migration period can be customized up to 12 hours.

Oracle RAC One Node allows the online relocation of an Oracle RAC One Node database from one server to another, which provides increased availability for applications based on an Oracle Database. You can now move a database for workload balancing as well as for performing planned maintenance on the server, on the operating system, or when applying patches to the Oracle software in a rolling fashion.

See Also:

[Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41960/onenode.htm#RACAD7894) for details

#### 3.1.5.7 SRVCTL-Based Management of Oracle RAC One Node Databases

Oracle RAC One Node is a new option to the Oracle Database Enterprise Edition. Oracle RAC One Node represents an Oracle RAC database that runs only one active database instance which can be managed using `SRVCTL` as any other Oracle RAC database.

Using `SRVCTL` simplifies and optimizes the management of Oracle RAC One Node databases.

See Also:

[Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41960/toc.htm) for details

#### 3.1.5.8 CRSCTL Command Enhancements

The `CRSCTL` command set has been enhancement to enable the management of various new Oracle Grid Infrastructure for a Cluster resources.

Using these new commands simplifies the management of Oracle Grid Infrastructure for a Cluster.

See Also:

[Oracle Clusterware Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41959/toc.htm) for details

#### 3.1.5.9 SRVCTL Command Enhancements

The `SRVCTL` command set has been enhancement to enable the management of various new Oracle Grid Infrastructure for a Cluster and Oracle RAC resources.

Using these new commands simplifies the management of Oracle RAC and Oracle Grid Infrastructure for a Cluster.

See Also:

[Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41960/toc.htm) for details

#### 3.1.5.10 Enhanced XStream Manageability

To increase the manageability of XStream, new process parameters are added to provide capabilities such as process memory control, changes to sequences, and the ability to exclude changes performed by specific users or transactions. Repositioning within the stream by either `SCN` or `TIME` is available. In addition, new views specific to XStream are provided such as `V$XSTREAM_OUTBOUND_SERVER` and `V$XSTREAM_TRANSACTION`, and existing views have been extended to provide additional information such as the client status or memory utilization of a process.

These enhancements give the XStream user more control over and visibility into XStream processing.

See Also:

[Oracle Database XStream Guide](https://docs.oracle.com/cd/E11882_01/server.112/e16545/toc.htm) for details

#### 3.1.5.11 Columnar Compression Support in Supplemental Logging and XStream

Columnar compression is now supported with Oracle Streams and XStream.

This feature enables logical replication of tables compressed using Hybrid Columnar Compression.

See Also:

[Oracle Streams Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e17069/ap_restrictions.htm#STRMS1191) for details

#### 3.1.5.12 Standalone Configuration Wizard for Post-Installation Cluster Configuration

The installation of Oracle Grid Infrastructure for a Cluster with Oracle Database 11g Release 2 includes a software-only option. This wizard assists the administrator with completing the cluster configuration independently of the software installation.

The configuration wizard provides an easy-to-use interface to configure the cluster independently of the software installation. Post-installation configuration of the software at the customer site is a standing requirement.

Customers that need to be able to mass deploy Oracle Grid Infrastructure for a Cluster or that need to support remote installations benefit from this feature.

See Also:

[Oracle Clusterware Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41959/admin.htm#CWADD92094) for details

#### 3.1.5.13 Redundant Interconnect Usage

Oracle RAC requires a dedicated network connection between the servers of the Oracle RAC cluster. The dedicated network connection, called interconnect, is crucial for the communication in the cluster. Using redundant network connections for load balancing and for failure protection is recommended. While in previous releases, technologies like bonding or trunking had to be used to make use of redundant networks for the interconnect, Oracle Grid Infrastructure for a Cluster and Oracle RAC now provide a native way of using redundant network interfaces in order to ensure optimal communication in the cluster.

Using redundant interconnects optimizes the stability, reliability, and scalability of an Oracle RAC cluster.

See Also:

[Oracle Grid Infrastructure Installation Guide for Linux](https://docs.oracle.com/cd/E11882_01/install.112/e41961/toc.htm) for details