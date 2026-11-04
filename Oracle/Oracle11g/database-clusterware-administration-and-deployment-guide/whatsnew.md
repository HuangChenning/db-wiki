---
title: "What's New in Oracle Clusterware Administration and Deployment?"
book: Database Clusterware Administration and Deployment Guide
doc_id: E41959-04
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/rac.112/e41959/whatsnew.htm
tags:
  - oracle
  - 11g
  - database-clusterware-administration-and-deployment-guide
---

This chapter lists new features in Oracle Clusterware for Oracle Database 11g release 2 (11.2) and 11g release 2 (11.2.0.1).

## Oracle Database 11g Release 2 (11.2.0.4) New Features in Oracle Clusterware

This section describes the Oracle Database 11g release 2 (11.2.0.4) features for Oracle Clusterware administration and deployment.

- Oracle RAC Configuration Audit Tool
	The Oracle Real Application Clusters (Oracle RAC) Configuration Audit Tool (RACcheck) assesses single instance and Oracle RAC database installations for known configuration issues, best practices, regular health checks, and pre- and post-upgrade best practices.
	See Also:
	[Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41960/racchk.htm#RACAD8365) for more information
- Oracle Trace File Analyzer Collector
	The Oracle Trace File Analyzer (TFA) Collector is a diagnostic collection utility to simplify diagnostic data collection for Oracle Clusterware, Oracle Grid Infrastructure, and Oracle Real Application Clusters (Oracle RAC) systems.
	See Also:
	["Oracle Trace File Analyzer Collector"](troubleshoot.md)

## Oracle Database 11g Release 2 (11.2) New Features in Oracle Clusterware

This section describes administration and deployment features for Oracle Clusterware starting with Oracle Database 11g release 2 (11.2).

See Also:

[Oracle Database New Features Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41360/toc.htm) for a complete description of the features in Oracle Database 11g release 2 (11.2)

- Oracle Real Application Clusters One Node (Oracle RAC One Node)
	Oracle Real Application Clusters One Node (Oracle RAC One Node) provides enhanced high availability for single-instance databases, protecting them from both planned and unplanned downtime. Oracle RAC One Node provides the following:
	- Always-on single-instance database services
		- Better consolidation for database servers
		- Enhanced server virtualization
		- Lower cost development and test platform for full Oracle RAC
	In addition, Oracle RAC One Node facilitates the consolidation of database storage, standardizes your database environment, and, when necessary, enables you to upgrade to a full, multinode Oracle RAC database without downtime or disruption.
	Use online database relocation to migrate an Oracle RAC One Node database from one node to another while maintaining service availability.
	This feature includes enhancements to the Server Control Utility (SRVCTL) for both Oracle RAC One Node and online database relocation.
	See Also:
	[Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41960/onenode.htm#RACAD7894) for more information about Oracle RAC One Node
- Configuration Wizard for the Oracle Grid Infrastructure Software
	This Configuration Wizard enables you to configure the Oracle Grid Infrastructure software after performing a software-only installation. You no longer have to manually edit the `config_params` configuration file as this wizard takes you through the process, step by step.
	See Also:
	["Configuring Oracle Grid Infrastructure"](admin.md) for more information
- Cluster Health Monitor (CHM)
	The Cluster Health Monitor (CHM) gathers operating system metrics in real time and stores them in its repository for later analysis to determine the root cause of many Oracle Clusterware and Oracle RAC issues with the assistance of Oracle Support. It also works together with Oracle Database Quality of Service Management (Oracle Database QoS Management) by providing metrics to detect memory over-commitment on a node. With this information, Oracle Database QoS Management can take action to relieve the stress and preserve existing workloads.
	See Also:
	- ["Cluster Health Monitor"](troubleshoot.md) for more information
	- [Oracle Database Quality of Service Management User's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e24611/toc.htm) for more information about Oracle Database QoS Management
- Enhancements to SRVCTL for Grid Infrastructure Management
	Enhancements to the Server Control utility (SRVCTL) simplify the management of various new Oracle Grid Infrastructure and Oracle RAC resources.
	See Also:
	[Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41960/srvctladmin.htm#RACAD005) for more information about SRVCTL
- Redundant Interconnect Usage
	In previous releases, to make use of redundant networks for the interconnect, bonding, trunking, teaming, or similar technology was required. Oracle Grid Infrastructure and Oracle RAC can now make use of redundant network interconnects, without the use of other network technology, to enhance optimal communication in the cluster.
	Redundant Interconnect Usage enables load-balancing and high availability across multiple (up to four) private networks (also known as interconnects).
	See Also:
	["Redundant Interconnect Usage"](admin.md) for more information
- Oracle Database Quality of Service Management Server
	The Oracle Database Quality of Service Management server allows system administrators to manage application service levels hosted in Oracle Database clusters by correlating accurate run-time performance and resource metrics and analyzing with an expert system to produce recommended resource adjustments to meet policy-based performance objectives.
	See Also:
	[Oracle Database Quality of Service Management User's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e24611/toc.htm) for more information

## Oracle Database 11g Release 2 (11.2.0.1) New Features in Oracle Clusterware

This section describes administration and deployment features for Oracle Clusterware starting with Oracle Database 11g Release 2 (11.2.0.1).

- Oracle Restart
	Oracle Restart provides automatic restart of Oracle Database and listeners.
	For standalone servers, Oracle Restart monitors and automatically restarts Oracle processes, such as [Oracle Automatic Storage Management (Oracle ASM)](glossary.md), Oracle Database, and listeners, on the server. Oracle Restart and Oracle ASM provide the Grid Infrastructure for a standalone server.
	See Also:
	[Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/restart.htm#ADMIN12708) for more information about Oracle Restart
- Improved Oracle Clusterware resource modeling
	Oracle Clusterware can manage different types of applications and processes, including third-party applications. You can create dependencies among the applications and processes and manage them as one entity.
	Oracle Clusterware uses different entities to manage your applications and processes, including resources, resource types, servers, and server pools. In addition to revised application programming interfaces (APIs), Oracle has created a new set of APIs to manage these entities.
	See Also:
	- ["Policy-Based Cluster and Capacity Management"](admin.md) for more information about servers and server pools
	- ["Oracle Clusterware Resources and Agents"](crschp.md) for more information about resources and resource types
	- [Appendix F, "Oracle Clusterware C Application Program Interfaces"](crs_api.md) for more information about APIs
- Policy-based cluster and capacity management
	Server capacity management is improved through logical separation of a [cluster](glossary.md) into [server pool](glossary.md) s. You can determine where and how resources run in the cluster using a [cardinality](glossary.md) -based approach. Subsequently, nodes become anonymous, eliminating the need to identify the nodes when placing resources on them.
	Server pools are assigned various levels of importance. When a failure occurs, Oracle Clusterware efficiently reallocates and reassigns capacity for applications to another, less important server pool within the cluster based on user-defined policies. This feature enables faster resource failover and dynamic capacity assignment.
	Clusters can host resources (defined as applications and databases) in server pools, which are isolated with respect to their resource consumption by the user-defined policies. For example, you can choose to run all human resources applications, accounting applications, and email applications in separate server pools.
	See Also:
	["Policy-Based Cluster and Capacity Management"](admin.md) for more information
- Role-separated management
	Role-separated management enables multiple applications and databases to share the same cluster and hardware resources, but ensures that different administration groups do not interfere with each other.
	See Also:
	["Role-Separated Management"](admin.md) for more information
- Cluster time synchronization service
	Cluster time synchronization service synchronizes the system time on all nodes in a cluster when vendor time synchronization software (such as NTP on UNIX and Window Time Service) is not installed. Synchronized system time across the cluster is a prerequisite to successfully run an Oracle cluster, improving the reliability of the entire Oracle cluster environment.
	See Also:
	["Cluster Time Management"](admin.md) for more information
- Oracle Cluster Registry and voting disks can be stored using Oracle Automatic Storage Management
	OCR and voting disks can be stored in Oracle Automatic Storage Management (Oracle ASM). The Oracle ASM partnership and status table (PST) is replicated on multiple disks and is extended to store OCR. Consequently, OCR can tolerate the loss of the same number of disks as are in the underlying [disk group](glossary.md) and be relocated in response to disk failures.
	Oracle ASM reserves several blocks at a fixed location on every Oracle ASM disk for storing the voting disk. Should the disk holding the voting disk fail, Oracle ASM selects another disk on which to store this data.
	Storing OCR and the voting disk on Oracle ASM eliminates the need for third-party cluster volume managers and eliminates the complexity of managing disk partitions for OCR and voting disks in Oracle Clusterware installations.
	Note:
	The `dd` commands used to back up and recover voting disks in previous versions of Oracle Clusterware are not supported in Oracle Clusterware 11g release 2 (11.2).
	See Also:
	[Chapter 3, "Managing Oracle Cluster Registry and Voting Disks"](votocr.md) for more information about OCR and voting disks
- Oracle Automatic Storage Management Cluster File System
	The Oracle Automatic Storage Management Cluster File System (Oracle ACFS) extends Oracle ASM by providing a robust, general purpose extent-based and journaling file system for files other than Oracle database files. Oracle ACFS provides support for files such as Oracle binaries, report files, trace files, alert logs, and other application data files. With the addition of Oracle ACFS, Oracle ASM becomes a complete storage management solution for both Oracle database and non-database files.
	Additionally, Oracle ACFS
	- Supports large files with 64-bit file and file system data structure sizes leading to exabyte-capable file and file system capacities.
		- Uses extent-based storage allocation for improved performance.
		- Uses a log-based metadata transaction engine for file system integrity and fast recovery.
		- Can be exported to remote clients through industry standard protocols such as Network File System and Common Internet File System.
	Oracle ACFS eliminates the need for third-party cluster file system solutions, while streamlining, automating, and simplifying all file type management in both a single node and Oracle Real Application Clusters (Oracle RAC) and Grid computing environments.
	Oracle ACFS supports dynamic file system expansion and contraction without downtime. It is also highly available, leveraging the Oracle ASM mirroring and striping features in addition to hardware RAID functionality.
	See Also:
	[Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e18951/toc.htm) for more information about Oracle ACFS
- Oracle Clusterware out-of-place upgrade
	You can install a new version of Oracle Clusterware into a separate home. Installing Oracle Clusterware in a separate home before the upgrade reduces planned outage time required for cluster upgrades, which assists in meeting availability service level agreements. After the Oracle Clusterware software is installed, you can then upgrade the cluster by stopping the previous version of the Oracle Clusterware software and starting the new version node by node (known as a rolling upgrade).
	See Also:
	[Oracle Grid Infrastructure Installation Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=GINST) for more information about out-of-place upgrades
- Enhanced Cluster Verification Utility
	Enhancements to the Cluster Verification Utility (CVU) include the following checks on the cluster:
	- Before and after node addition
		- After node deletion
		- Before and after storage addition
		- Before and after storage deletion
		- After network modification
		- Oracle ASM integrity
	In addition to command-line commands, these checks are done through the Oracle Universal Installer, Database Configuration Assistant, and Oracle Enterprise Manager. These enhancements facilitate implementation and configuration of cluster environments and provide assistance in diagnosing problems in a cluster environment, improving configuration and installation.
	See Also:
	- [Appendix A, "Cluster Verification Utility Reference"](cvu.md) for more information about CVU commands
	- [Oracle Grid Infrastructure Installation Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=GINST) for more information about CVU checks done during installation
- Enhanced Integration of Cluster Verification Utility and Oracle Universal Installer
	This feature fully integrates the CVU with Oracle Universal Installer so that multi-node checks are done automatically. This ensures that any problems with cluster setup are detected and corrected before installing Oracle software.
	The CVU validates cluster components and verifies the cluster readiness at different stages of Oracle RAC deployment, such as installation of Oracle Clusterware and Oracle RAC databases, and configuration of Oracle RAC databases. It also helps validate the successful completion of a specific stage of Oracle RAC deployment.
	See Also:
	[Oracle Grid Infrastructure Installation Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=GINST) for more information about CVU checks done during installation
- Grid Plug and Play
	Grid Plug and Play enables you to move your data center toward a dynamic Grid Infrastructure. This enables you to consolidate applications and lower the costs of managing applications, while providing a highly available environment that can easily scale when the workload requires. There are many modifications in Oracle RAC 11g release 2 (11.2) to support the easy addition of servers in a cluster and therefore a more dynamic grid.
	In the past, adding or removing servers in a cluster required extensive manual preparation. With this release, Grid Plug and Play reduces the costs of installing, configuring, and managing server nodes by automating the following tasks:
	- Adding an Oracle RAC database instance
		- Negotiating appropriate network identities for itself
		- Acquiring additional information it needs to operate from a configuration profile
		- Configuring or reconfiguring itself using profile data, making host names and addresses resolvable on the network
	Additionally, the number of steps necessary to add and remove nodes is reduced.
	Oracle Enterprise Manager immediately reflects Grid Plug and Play-enabled changes.
- Oracle Enterprise Manager support for Oracle ACFS
	This feature provides a comprehensive management solution that extends Oracle ASM technology to support general purpose files not directly supported by ASM, and in both single-instance Oracle Database and Oracle Clusterware configurations. It also enhances existing Oracle Enterprise Manager support for Oracle ASM, and adds new features to support the Oracle ASM Dynamic Volume Manager (ADVM) and Oracle ASM Cluster File System technology (ACFS).
	Oracle Automatic Storage Management Cluster File System (Oracle ACFS) is a scalable file system and storage management design that extends Oracle ASM technology. It supports all application data in both single host and cluster configurations and leverages existing Oracle ASM functionality to achieve the following:
	- Dynamic file system resizing
		- Maximized performance through Oracle ASM's automatic distribution
		- Balancing and striping of the file system across all available disks
		- Storage reliability through Oracle ASM's mirroring and parity protection
	Oracle ACFS provides a multiplatform storage management solution to access clusterwide, non-database customer files.
	See Also:
	[Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e18951/asmfs_em.htm#OSTMG40000) for more information about Oracle ACFS
- Oracle Enterprise Manager-based Oracle Clusterware resource management
	You can use Oracle Enterprise Manager to manage Oracle Clusterware resources. You can create and configure resources in Oracle Clusterware and also monitor and manage resources after they are deployed in the cluster.
	See Also:
	["Adding Resources Using Oracle Enterprise Manager"](crschp.md)
- Zero downtime for patching Oracle Clusterware
	Patching Oracle Clusterware and Oracle RAC can be completed without taking the entire cluster down. This also allows for out-of-place upgrades to the cluster software and Oracle Database, reducing the planned maintenance downtime required in an Oracle RAC environment.
- Improvements to provisioning of Oracle Clusterware and Oracle RAC
	This feature offers a simplified solution for provisioning Oracle RAC systems. Oracle Enterprise Manager Database Control enables you to extend Oracle RAC clusters by automating the provisioning tasks on the new nodes.