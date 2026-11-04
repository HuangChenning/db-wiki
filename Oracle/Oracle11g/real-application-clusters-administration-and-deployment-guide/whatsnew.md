---
title: "What's New in Oracle RAC Administration and Deployment?"
book: Real Application Clusters Administration and Deployment Guide
doc_id: E41960-04
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/rac.112/e41960/whatsnew.htm
tags:
  - oracle
  - 11g
  - real-application-clusters-administration-and-deployment-guide
---

This section describes the new administration and deployment features for Oracle Real Application Clusters (Oracle RAC) for Oracle Database 11g release 2 (11.2.0.4), 11g release 2 (11.2.0.2), and 11g release 2 (11.2.0.1).

## Oracle Database 11g Release 2 (11.2.0.4) New Features in Oracle RAC

This section describes the Oracle Database 11g release 2 (11.2.0.4) features for Oracle RAC administration and deployment.

- Oracle RAC Configuration Audit Tool
	The Oracle RAC Configuration Audit Tool (RACcheck) assesses single instance and Oracle RAC database installations for known configuration issues, best practices, regular health checks, and pre- and post-upgrade best practices.
	See Also:
	[Appendix D, "Oracle RAC Configuration Audit Tool"](racchk.md)
- Oracle Trace File Analyzer Collector
	The Oracle Trace File Analyzer (TFA) Collector is a diagnostic collection utility to simplify diagnostic data collection for Oracle Clusterware, Oracle Grid Infrastructure, and Oracle RAC systems.
	See Also:
	[Oracle Clusterware Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41959/ocrsyntax.htm#CWADD92047)

## Oracle Database 11g Release 2 (11.2.0.2) New Features in Oracle RAC

This section describes the Oracle Database 11g release 2 (11.2.0.2) features for Oracle RAC administration and deployment.

- Oracle RAC One Node
	Oracle Real Application Clusters One Node (Oracle RAC One Node) provides enhanced high availability for noncluster databases, protecting them from both planned and unplanned downtime. Oracle RAC One Node provides the following:
	- Always-on noncluster database services
		- Better consolidation for database servers
		- Enhanced server virtualization
		- Lower cost development and test platform for full Oracle RAC
	In addition, Oracle RAC One Node facilitates the consolidation of database storage, standardizes your database environment, and, when necessary, enables you to upgrade to a full, multinode Oracle RAC database without downtime or disruption.
	Online database relocation is a tool you can use to relocate an Oracle RAC One Node database from one node to another while maintaining service availability.
	This feature includes enhancements to the Server Control Utility (SRVCTL) for both Oracle RAC One Node and online database relocation.
	This feature also includes enhancements to the Database Configuration Assistant (DBCA) to enable you to use the tool to add an Oracle RAC One Node database.
- Edition-Based Redefinition
	You can specify an edition attribute for a database service using SRVCTL. When you specify an edition attribute for a service, all subsequent connections that specify the service use this edition as the initial session edition.
	Specifying an edition as a service attribute can help to manage resource usage. For example, services associated with an edition can be placed on a separate instance in an Oracle RAC environment, and the Oracle Database Resource Manager can manage resources used by different editions by associating resource plans with the corresponding services.
	See Also:
	- [Oracle Database Advanced Application Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e41502/whatsnew.htm#ADFNS110) for more information about edition-based redefinition
	- [Appendix A, "Server Control Utility Reference"](srvctladmin.md) for more information about enhancements to the `srvctl add service` and `srvctl modify service` commands
- Enhancements to SRVCTL for Grid Infrastructure Management
	Enhancements to SRVCTL simplify the management of various new Oracle Grid Infrastructure and Oracle RAC resources.
	See Also:
	- [Appendix A, "Server Control Utility Reference"](srvctladmin.md) for more information about these additional commands
	- [Oracle Clusterware Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41959/cvu.htm#CWADD1100) for more information about the Cluster Verification Utility
- Oracle Database Quality of Service Management Server
	The Oracle Database Quality of Service Management server allows system administrators to manage application service levels hosted in Oracle Database clusters by correlating accurate runtime performance and resource metrics and analyzing with an expert system to produce recommended resource adjustments to meet policy-based performance objectives.
	See Also:
	[Oracle Database Quality of Service Management User's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e24611/toc.htm) for more information

## Oracle Database 11g Release 2 (11.2.0.1) New Features in Oracle RAC

This section describes the Oracle Database 11g release 2 (11.2.0.1) features for Oracle RAC administration and deployment.

- Grid Plug and Play
	Grid Plug and Play reduces per-node configuration data and the need for explicit add and delete nodes steps, where possible. This allows a system administrator to take a template system image and run it on a node to be added with no further configuration. This removes many manual operations, reduces the opportunity for errors, and encourages configurations that can be changed more easily. Removal of the per-node configuration makes the nodes easier to replace because it is not required that they contain individual states that must be managed.
	Grid Plug and Play also introduces simplified instance addition. When your databases are backed with [Oracle Managed Files](rac_glossary.md) and Oracle Automatic Storage Management (Oracle ASM), recovery threads and undo tablespaces are automatically created for an instance that you add explicitly with the `srvctl add instance` command, or implicitly when a policy-managed database brings up a new instance.
	All tools and utilities such as DBCA, the Oracle Net Configuration Assistant (NETCA), and SRVCTL have been updated to support Grid Plug and Play. Oracle Enterprise Manager, the graphical interface for managing Oracle RAC, provides management and monitoring for the Grid Plug and Play environment.
	Grid Plug and Play reduces the cost of installing, configuring, and managing database nodes by making their per-node state disposable. Nodes can easily be replaced with regenerated state.
	See Also:
	[Oracle Real Application Clusters Installation Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=GINST) for more information about Grid Plug and Play
- Policy-based cluster and capacity management
	Oracle Clusterware allocates and reassigns capacity based on policies you define, enabling faster resource failover and dynamic capacity assignment using policy-based management.
	Policy-based cluster and capacity management allows the efficient allocation of different types of applications in the cluster. Various applications can be hosted on a shared infrastructure, being isolated regarding their resource consumption by policies and, therefore, behave as if they were deployed in single-system environments. Policy-managed Oracle RAC databases use policy-based cluster management to provide the required resources for the workloads the database supports.
	See Also:
	[Oracle Clusterware Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41959/admin.htm#CWADD91100) for more information
- Role-separated management
	Role-separated management for Oracle Clusterware allows certain administrative tasks to be delegated to different people, representing different roles in the company. It is based on the idea of an administrator role, called CRS Administrator, that can create server pools and grant administrative tasks on a per resource basis. For example, if two databases are placed into the same cluster, the CRS Administrator can manage both databases in the cluster. But, the CRS Administrator can also decide to grant different administrative privileges to each DBA responsible for each one of those databases.
	Role-separated management enables multiple applications and databases to share the same cluster and hardware resources, but ensures that different administration groups do not interfere with each other.
	See Also:
	[Oracle Clusterware Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41959/admin.htm#CWADD91105) for more information
- Improved Cluster Resource Modeling
	Oracle Clusterware can manage different types of applications and processes. You can create dependencies among the applications and processes and manage them as a single entity.
	See Also:
	[Oracle Clusterware Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41959/admin.htm#CWADD91100) for more information
- Oracle Enterprise Manager-based Oracle Clusterware resource management
	You can use Oracle Enterprise Manager to manage Oracle Clusterware resources. You can create and configure resources in Oracle Clusterware and also monitor and manage resources after they are deployed in the cluster.
	See Also:
	[Oracle Clusterware Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41959/crschp.htm#CWADD91297) for more information
- Oracle Cluster Registry performance enhancements
	Improvements in the way Oracle Clusterware accesses Oracle Cluster Registry (OCR) speed up relocation of services when a node fails. Oracle Clusterware now supports up to five copies of OCR for improved availability of the cluster and OCR can now be stored in Oracle ASM.
	The tools to manage OCR have changed to support the new management options. Consistent storage management automation provides improved performance in Oracle Clusterware and Oracle RAC environments, and easier management of the cluster.
	See Also:
	[Oracle Clusterware Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41959/votocr.htm#CWADD90963) for more information
- SRVCTL support for noncluster database
	Server Control Utility (SRVCTL) commands have been enhanced to manage the configuration in a standalone server using Oracle Restart. The new SRVCTL functionality enables you to register a noncluster database that can be managed by Oracle Clusterware. Once registered, Oracle Clusterware can start, stop, monitor, and restart the database instance.
	The new SRVCTL functionality simplifies management of Oracle Database through a consistent interface that can be used from the console or scripted. An improved management interface makes it easy to provide higher availability for noncluster databases that run on a server that is part of a cluster.
	See Also:
	- [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/toc.htm) for more information about using SRVCTL commands on a noncluster database
	- [Appendix A, "Server Control Utility Reference"](srvctladmin.md) for a list of SRVCTL commands
- Enhanced Cluster Verification Utility
	New Cluster Verification Utility (CVU) functionality checks certain storage types and configurations. Also, more consideration is given to user-specific settings.
	In addition to command-line commands, these checks are done through the Oracle Universal Installer, DBCA, and Oracle Enterprise Manager. These enhancements facilitate implementation and configuration of cluster environments and provide assistance in diagnosing problems in a cluster environment, improving configuration and installation.
	See Also:
	[Oracle Clusterware Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41959/cvu.htm#CWADD1100) for more information about CVU commands
- Oracle Enterprise Manager support for Grid Plug and Play
	You can use Oracle Enterprise Manager:
	- To support the Grid Plug and Play environment
		- To administer dynamic configuration use
		- To manage Grid Plug and Play profiles and targets, such as hosts, clusters, and Oracle RAC databases and Oracle RAC database instances
	Additionally, Oracle Enterprise Manager supports other Oracle RAC administration tasks, including:
	- Monitoring
		- Startup
		- Shutdown
		- Backup and recovery
		- Tablespace management
		- Node addition
- Oracle Enterprise Manager provisioning for Oracle Clusterware and Oracle RAC
	The Oracle Enterprise Manager provisioning framework has been updated to reflect the changes to the installation and configuration of Oracle Clusterware and Oracle RAC. You can achieve easier implementation and management of a clustered database environment using the Oracle Enterprise Manager provisioning framework.
- Zero downtime for patching Oracle RAC
	Patching Oracle Clusterware and Oracle RAC can be completed without taking the entire cluster down. This also allows for out-of-place upgrades to the cluster software and Oracle Database, reducing the planned maintenance downtime required in an Oracle RAC environment.
- Integrated support for application failover in an Oracle Data Guard configuration
	Applications connected to a primary database transparently failover to a new primary database when Oracle Data Guard changes roles. Clients integrated with Fast Application Notification (FAN) can achieve fast failover between primary and standby databases, in addition to fast failover within the cluster. Services have an attribute with which you can associate the service with a database role, such as `PHYSICAL_STANDBY`, so that the service is only active when the database is mounted in the associated role.
	See Also:
	- [Oracle Data Guard Broker](https://docs.oracle.com/cd/E11882_01/server.112/e40771/sofo.htm#DGBKR3425) for more information
	- [Chapter 5, "Introduction to Automatic Workload Management"](hafeats.md)
- Oracle ASM Dynamic Volume Manager
	The Oracle ASM Dynamic Volume Manager is a kernel-loadable device driver that provides a standard device driver interface to clients, such as the Oracle Automatic Storage Management Cluster File System (Oracle ACFS). Oracle ASM Dynamic Volume Manager is the primary I/O interface for Oracle ACFS to perform I/O and build a file system using Oracle Automatic Storage Management (Oracle ASM) as a volume manager. Oracle ASM Dynamic Volume Manager is loaded upon Oracle ASM startup, is cluster aware, and communicates with Oracle ASM for extent map information, extent rebalancing, and I/O failures.
	Oracle ASM Dynamic Volume Manager provides a standard I/O interface allowing general-purpose file systems to leverage the full functionality of Oracle ASM as a volume manager. Files not directly supported by Oracle ASM, such as Oracle binaries, can now reside on ACFS on Oracle ASM volumes. This eliminates the need for third-party file systems or volume managers to host general-purpose files.
	See Also:
	[Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e18951/asmfilesystem.htm#OSTMG32000) for more information
- Oracle Enterprise Manager support for Oracle Automatic Storage Management Cluster File System
	Oracle Enterprise Manager provides a comprehensive management solution that extends Oracle ASM technology to support all customer application data files, both database and non-database, and in both single-host and cluster configurations. It also enhances existing Oracle Enterprise Manager support for Oracle ASM, and adds features to support the Oracle ASM Dynamic Volume Manager (ADVM) and Oracle ASM Cluster File System (ACFS) technology.
	Oracle Enterprise Manager provides a graphical user interface that makes it easier to manage the environment, whether it is a standalone server or a cluster deployment of Oracle ASM. The centralized console provides a consistent interface for managing volumes, database files, file systems, and the Oracle Database.
	See Also:
	[Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e18951/asmfs_em.htm#OSTMG40000) for more information
- Oracle Automatic Storage Management Cluster File System
	The Oracle Automatic Storage Management Cluster File System (Oracle ACFS) provides a robust, modern, general purpose file system for files beyond the Oracle database files. Oracle ACFS also provides support for files such as Oracle binaries, report files, trace files, alert logs, and other application data files. With the addition of Oracle ACFS, Oracle ASM becomes a complete storage management solution for both Oracle database and non-database files.
	Additionally, Oracle ACFS
	- Supports large files with 64-bit file and file system data structure sizes leading to exabyte-capable file and file system capacities
		- Uses extent-based storage allocation for improved performance
		- Uses a log-based metadata transaction engine for file system integrity and fast recovery
		- Can be exported to remote clients through industry standard protocols such as NFS and CIFS
	Oracle ACFS complements and leverages Oracle ASM and provides a general purpose journaling file system for storing and managing non-Oracle database files. This eliminates the need for third-party cluster file system solutions, while streamlining, automating, and simplifying all file type management in both single node and Oracle RAC and Grid computing environments.
	Oracle ACFS supports dynamic file system expansion and contraction without any downtime and is also highly available, leveraging the Oracle ASM mirroring and striping features in addition to hardware RAID functionality.
	See Also:
	[Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e18951/asmfilesystem.htm#OSTMG31000) for more information about Oracle ACFS
- Automatic Storage Management file access control
	This feature implements access control on Oracle ASM files on UNIX platforms to isolate itself and different database instances from each other and prevent unauthorized access. The feature includes SQL statements to grant, modify, and deny file permissions.
	This feature enables multiple database instances to store their Oracle ASM files in the same disk group and enables consolidation of multiple databases, securely, to prevent database instances from accessing or overwriting files belonging to other database instances.
	See Also:
	- [Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e18951/asmdiskgrps.htm#OSTMG02660) for more information
	- ["Oracle Automatic Storage Management with Oracle RAC"](storage.md)
- Universal Connection Pool
	Universal Connection Pool (UCP) is a Java connection pool that replaces the deprecated JDBC Implicit Connection Cache with Oracle Database 11g (11.1.0.7). UCP is integrated with Oracle RAC to provide the following benefits:
	- A single UCP can be leveraged by any Oracle component or user.
		- Eliminates redundant connection pools from several Oracle Components, such as AOL/J, ADF Business Components, and TopLink.
		- Provides consistent connection pool behavior for an Oracle component or product. For example, the connection pool sizes can be configured to provide consistent connection management behavior for an application.
		- Provides JMX interfaces for the UCP Manager, which delivers a consistent management interface to manage the connection pool.
		- UCP adapters can provide standards compliance for a specific connection type being pooled.
		- Supports connection pooling for Oracle and non-Oracle connections.
		- Supports pooling for any type of connections, including JDBC or JCA connections.
	See Also:
	[Oracle Database 2 Day + Real Application Clusters Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e17264/toc.htm) for more information about configuring JDBC clients
- Expose high availability events through a Java API
	You can access fast application notification (FAN) events with a simplified JAVA API if you are not using the Oracle connection pool features.
	See Also:
	["Fast Application Notification"](hafeats.md) for more information about FAN events
- SRVCTL enhancements to support Grid Plug and Play
	This feature includes enhancements to the server control utility (SRVCTL) for the Grid Plug and Play feature.
	See Also:
	[Appendix A, "Server Control Utility Reference"](srvctladmin.md) for a list of SRVCTL commands