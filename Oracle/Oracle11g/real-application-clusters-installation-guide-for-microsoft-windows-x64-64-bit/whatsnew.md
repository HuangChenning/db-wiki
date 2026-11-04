---
title: "What's New in Oracle Real Application Clusters Installation?"
book: Real Application Clusters Installation Guide for Microsoft Windows x64 (64-Bit)
doc_id: E48195-02
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/install.112/e48195/whatsnew.htm
tags:
  - oracle
  - 11g
  - real-application-clusters-installation-guide-for-microsoft-windows-x64-64-bit
---

This chapter describes new features as they pertain to the installation and configuration of Oracle Real Application Clusters (Oracle RAC). The topics are:

## New Features for Oracle RAC 11g Release 2 (11.2.0.4)

The following is a list of new features that are available starting with Oracle RAC 11g Release 2 (11.2.0.4):

### Windows Server 2012 and Windows Server 2012 R2 Support

Starting with Oracle Database 11g Release 2 (11.2.0.4), Oracle Database server, client, and Oracle RAC are supported on Windows Server 2012 (64-bit only) and Windows Server 2012 R2 (64-bit only).

Note:

Windows Database Bundle Patch 11.2.0.4.11 is required for Windows Server 2012 R2 support.

## New Features for Oracle RAC 11g Release 2 (11.2.0.3)

The following is a list of new features that are available starting with Oracle RAC 11g Release 2 (11.2.0.3):

### Oracle Database Quality of Service Management

The Database Quality of Service (QoS) Management Server allows system administrators to manage application service levels hosted in Oracle Database clusters by correlating accurate run-time performance and resource metrics and analyzing with an expert system to produce recommended resource adjustments to meet policy-based performance objectives.

See Also:

[Oracle Database Quality of Service Management User's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e24611/toc.htm)

## New Features for Oracle RAC 11g Release 2 (11.2.0.2)

The following new features are available starting with Oracle Database 11g Release 2 (11.2.0.2):

### New Software Updates Option

Use the Software Updates feature to dynamically download and apply software updates as part of the Oracle Database installation. You can also download the updates separately using the downloadUpdates option and later apply them during the installation by providing the location where the updates are present.

### Oracle Real Application Clusters One Node (Oracle RAC One Node)

Oracle RAC One Node is a single instance of Oracle RAC running on one node in a cluster. You can use Oracle RAC One Node to consolidate many databases onto a single cluster with minimal overhead, and still provide the high availability benefits of failover protection, online rolling patch application, and rolling upgrades for the operating system and for Oracle Clusterware. With Oracle RAC One Node you can standardize all Oracle Database deployments across your enterprise.

You can use Oracle Database and Oracle Grid Infrastructure configuration assistants, such as Oracle Database Configuration Assistant (DBCA) and RCONFIG, to configure Oracle RAC One Node databases.

Oracle RAC One Node is a single Oracle RAC database instance. You can use a planned online relocation to start a second Oracle RAC One Node instance temporarily on a new target node, so that you can migrate the current Oracle RAC One Node instance to this new target node. After the migration, the source node instance is shut down. Oracle RAC One Node databases can also fail over to another cluster node within its hosting server pool if their current node fails.

Oracle RAC One Node is not supported if you use a third-party clusterware software, such as Veritas, SFRAC, IBMPowerHA, or HP Serviceguard. Oracle Solaris Cluster is currently not supported.

Starting with Oracle Database 11g release 2 (11.2.0.2), Oracle RAC One Node is supported on all platforms where Oracle Real Application Clusters (Oracle RAC) is certified. Oracle RAC One Node supports Oracle Data Guard starting with Oracle Database 11g release 2 (11.2.0.2).

## New Features for Oracle RAC 11g Release 2 (11.2)

The following is a list of new features for Oracle RAC 11g release 2 (11.2):

- Oracle Automatic Storage Management and Oracle Clusterware Installation
- Oracle Automatic Storage Management Cluster File System (Oracle ACFS)
- Cluster Time Synchronization Service
- Oracle Database Configuration Assistant and Listeners
- Daylight Savings Time Upgrade of TIMESTAMP WITH TIMEZONE Data Type
- Oracle Enterprise Manager Database Control Provisioning
- Oracle Enterprise Manager and Oracle Clusterware Resource Management
- Oracle Enterprise Manager Patch Application
- Grid Plug and Play
- Improved Deployment, Deconfiguration, and Deinstallation
- SCAN for Simplified Client Access
- SRVCTL Command Enhancements for Patching
- Desktop Class and Server Class Installation Options
- Zero Downtime Patching for Oracle RAC
- Deinstallation Tool

### Oracle Automatic Storage Management and Oracle Clusterware Installation

With Oracle Grid Infrastructure 11g release 2 (11.2), Oracle Automatic Storage Management (Oracle ASM) and Oracle Clusterware are installed into a single home directory, which is referred to as the Grid Infrastructure home. Configuration assistants that start after the installer interview process configure Oracle ASM and Oracle Clusterware.

The installation of the combined products is called Oracle Grid Infrastructure. However, Oracle Clusterware and Oracle Automatic Storage Management remain separate products.

### Oracle Automatic Storage Management Cluster File System (Oracle ACFS)

Oracle Automatic Storage Management Cluster File System (Oracle ACFS) is a new multiplatform, scalable file system and storage management design that extends Oracle Automatic Storage Management (Oracle ASM) technology to support all application data. Oracle ACFS provides dynamic file system resizing, improved performance using the distribution, balancing, and striping technology across all available disks, and storage reliability through the Oracle ASM mirroring and parity protection.

Note:

For Oracle ASM 11g Release 2 (11.2.0.1), Oracle ACFS is supported on only:
- Windows Server 2003 64-bit
- Windows Server 2003 R2 64-bit

Starting with Oracle Database 11g Release 2 (11.2.0.2), Oracle ACFS is also supported on:

- Windows Server 2008, 64-bit
- Windows Server 2008 R2 64-bit

Starting with Oracle Database 11g Release 2 (11.2.0.4), Oracle ACFS is also supported on:

- Windows Server 2012, 64-bit
- Windows Server 2012 R2 64-bit

Oracle ASM Dynamic Volume Manager (Oracle ADVM) extends Oracle ASM by providing a disk driver interface to Oracle ASM storage allocated as Oracle ASM volume files. You can use Oracle ADVM to create virtual disks that contain file systems. File systems and other disk-based applications issue I/O requests to Oracle ADVM volume devices as they would to other storage devices on a vendor operating system. The file systems contained on Oracle ASM volumes can support files beyond Oracle database files, such as executable files, report files, trace files, alert logs, and other application data files.

### Cluster Time Synchronization Service

Cluster node times should be synchronized, particularly if the cluster is to be used for Oracle Real Application Clusters. With this release, Oracle Clusterware provides Cluster Time Synchronization Service (CTSS), which ensures that there is a synchronization service in the cluster. If neither Network Time Protocol (NTP) or Windows Time Service is not found during cluster configuration, then CTSS is configured to ensure time synchronization.

### Oracle Database Configuration Assistant and Listeners

With this release, Oracle Database Configuration Assistant (DBCA) no longer sets the value for `LOCAL_LISTENER`. When Oracle Clusterware starts the database resource, it updates the instance parameters. The `LOCAL_LISTENER` is set to the virtual IP endpoint of the local node listener address. You should not modify the setting for `LOCAL_LISTENER`. New installation instances register only with single client access name (SCAN) listeners as remote listeners. SCANs are virtual IP addresses assigned to the cluster, rather than to individual nodes, so cluster members can be added or removed without requiring updates of clients served by the cluster. Upgraded databases continue to register with all node listeners, and additionally with the SCAN listeners.

### Daylight Savings Time Upgrade of TIMESTAMP WITH TIMEZONE Data Type

When time zone files are updated to a new version, TIMESTAMP WITH TIMEZONE (TSTZ) data could become stale. In previous releases, database administrators ran the SQL script `utltzuv2.sql` to detect TSTZ data affected by the time zone version changes and then had to perform extensive manual procedures to update the TSTZ data.

With this release, TSTZ data is updated transparently with very minimal manual procedures using newly provided DBMS\_DST PL/SQL packages. In addition, there is no longer a need for clients to patch their time zone files.

See Also:

- [Oracle Database Upgrade Guide](https://docs.oracle.com/cd/E11882_01/server.112/e23633/upgrade.htm#UPGRD12399) for information about upgrading time zone files
- [Oracle Database Globalization Support Guide](https://docs.oracle.com/cd/E11882_01/server.112/e10729/ch4datetime.htm#NLSPG259) for information about how to upgrade the time zone file and TSTZ data
- [Oracle Call Interface Programmer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e10646/oci10new.htm#LNOCI16761) for information about performance effects of clients and servers operating with different versions of time zone files

### Oracle Enterprise Manager Database Control Provisioning

Oracle Enterprise Manager Database Control 11g provides the capability to provision automatically Oracle Grid Infrastructure and Oracle RAC installations on new nodes, and then extend the existing Oracle Grid Infrastructure and Oracle RAC database to these provisioned nodes. This provisioning procedure requires a successful Oracle RAC installation before you can use this feature.

See Also:

[Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41960/toc.htm) for information about this feature

### Oracle Enterprise Manager and Oracle Clusterware Resource Management

With this release, you can use Oracle Enterprise Manager Cluster home page to perform full administrative and monitoring support for both standalone database and Oracle RAC environments, using High Availability Application and Oracle Clusterware resource management. Such administrative tasks include creating and modifying server pools.

### Oracle Enterprise Manager Patch Application

With this release, you can apply patches to the Oracle RAC database using Oracle Enterprise Manager. A new Oracle Enterprise Manager feature, the Provisioning Advisor Console, enables you to customize, monitor, and deploy patch applications to nodes on the cluster.

### Grid Plug and Play

In the past, adding or removing servers in a cluster required extensive manual preparation. With this release, you can continue to configure server nodes manually, or you can use Grid Plug and Play to configure them dynamically as nodes are added or removed from the cluster.

Grid Plug and Play reduces the costs of installing, configuring, and managing server nodes by starting a Grid Naming Service (GNS) within the cluster to allow each node to perform the following tasks dynamically:

- Negotiate appropriate network identities for itself
- Acquire additional information it requires to operate from a configuration profile
- Configure or reconfigure itself using profile data, making host names and addresses resolvable on the network

Because servers perform these tasks dynamically, adding and removing nodes simply requires an administrator to connect the server to the cluster, and to allow the cluster to configure the node. Using Grid Plug and Play and best practice recommendations, you can add a node to the database cluster as part of the server restart, and remove a node from the cluster automatically when a server is turned off.

### Improved Deployment, Deconfiguration, and Deinstallation

Oracle configuration assistants ensure the success of recommended deployments, and prevent configuration issues.

Oracle configuration assistants provide the capability of deconfiguring and deinstalling Oracle Real Application Clusters, without requiring additional manual steps.

### SCAN for Simplified Client Access

With this release, the single client access name (SCAN) is the address to provide for all clients connecting to the cluster. SCAN is a domain name registered to at least one and up to three IP addresses, either in the domain name service (DNS) or the Grid Naming Service (GNS). SCAN eliminates the need to change clients when nodes are added to or removed from the cluster. Clients using SCAN can also access the cluster using Easy Connect Naming.

### SRVCTL Command Enhancements for Patching

With this release, you can use the Server Control Utility (SRVCTL) to shut down all Oracle software running within an Oracle home, in preparation for patching. Oracle Grid Infrastructure patching is automated across all nodes, and patches can be applied in a multinode, multipatch method.

### Desktop Class and Server Class Installation Options

In this release, there are two installation types: Desktop Class and Server Class.

The Desktop Class installation type is a simplified installation with a minimal number of manual configuration choices. The Desktop Class installation performs a full Oracle Database installation with a basic configuration.

The Server Class installation type allows for more advanced configuration options. Select this option when installing Oracle RAC, if you use Oracle Enterprise Manager Grid Control, or to configure database storage on Oracle ASM.

### Zero Downtime Patching for Oracle RAC

The Oracle patch utility, Opatch, can apply patches in a multinode, multipatch method, and does not start instances that have a nonrolling patch applied to it if other instances of the database do not have that patch. Opatch also detects if the database schema is an earlier patch level than the new patch, and it runs SQL statements to upgrade the database schema to the current patch level.

See Also:

[Oracle Universal Installer and OPatch User's Guide for Windows and UNIX](https://docs.oracle.com/cd/E11882_01/em.112/e12255/toc.htm)

### Deinstallation Tool

Oracle Universal Installer (OUI) no longer removes Oracle software. Use the new Deinstallation Tool (`deinstall.bat`) available on the installation media before installation, and in the Oracle home directory after installation. This tool can also be downloaded from Oracle Technology Network.

See Also:

[Chapter 8, "Removing Oracle Real Application Clusters Software"](rem_orcl.md) for more information

## New Features for Oracle RAC 11g Release 1 (11.1)

This section describes Oracle Database 11g release 1 features as they pertain to the installation and configuration of Oracle Real Application Clusters (Oracle RAC).

The topics in this section are:

- Changes in Installation Documentation
- Changes in the Installation Options
- New Components Available for Installation
- Enhancements and New Features for Installation

### Changes in Installation Documentation

With Oracle Database 11g release 1 (11.1), Oracle Clusterware can be installed or configured as an independent product. In addition, new documentation is provided for Oracle Database storage administration. For installation planning, note the documentation described in the following subsections.

#### Oracle Database 2 Day + Real Application Clusters Guide

This guide provides an overview and examples of the procedures to install and configure a two-node Oracle Clusterware and Oracle RAC environment.

#### Oracle Clusterware Installation Guide

This guide provides procedures either to install Oracle Clusterware as a standalone product, or to install Oracle Clusterware with either Oracle Database, or Oracle RAC. It contains system configuration instructions that require system administrator privileges.

#### Oracle Real Application Clusters Installation Guide

The guide that you are reading provides procedures to install Oracle RAC after you have successfully completed an Oracle Clusterware installation. It contains database configuration instructions for database administrators.

#### Oracle Database Storage Administrator's Guide

This guide provides information for database and storage administrators who administer and manage storage, or who configure and administer Oracle ASM.

#### Oracle Clusterware Administration and Deployment Guide

This is the administrator's reference for Oracle Clusterware. It contains information about administrative tasks, including those that involve changes to operating system configurations.

#### Oracle Real Application Clusters Administration and Deployment Guide

This is the administrator's reference for Oracle RAC. It contains information about administrative tasks. These tasks include database cloning, node addition and deletion, Oracle Cluster Registry (OCR) administration, use of Server Control (SRVCTL) and other database administration utilities.

### Changes in the Installation Options

The following are installation option changes for Oracle Database 11g release 1 (11.1):

- Oracle Application Express: This feature is installed with Oracle Database 11g. It was previously named HTML DB, and was available as a separate Companion CD component.
- Oracle Configuration Manager: Oracle Configuration Manager (OCM) is integrated with OUI. However, it is an optional component with database and client installations, and you must select Custom Installation to enable it. Oracle Configuration Manager, used in previous releases as customer configuration repository (CCR), is a tool that gathers and stores details relating to the configuration of the software stored in the Oracle ASM and Oracle Database home directories.
	See " "Oracle Configuration Manager for Improved Support" for further information.
- Oracle Data Mining: The Enterprise Edition installation type selects Oracle Data Mining option for installation by default.
- Oracle Database Vault: This feature is offered during installation. It is an optional component for database installation, available through Custom installation.
- Oracle SQL Developer: This feature is installed by default with template-based database installations, such as General Purpose, Transaction Processing, and Data Warehousing. It is also installed with database client Administrator, Run-Time, and Custom installations.
- Oracle Warehouse Builder: This information integration tool is now installed with both Standard and Enterprise Edition versions of Oracle Database. With Enterprise Edition, you can purchase additional extension processes. Installing Oracle Database also installs a previously seeded repository, OWBSYS, necessary for using Oracle Warehouse Builder.
- Oracle XML DB: Starting with Oracle Database 11g, Oracle XML DB is no longer an optional feature. It is installed and configured using Oracle Database Configuration Assistant (DBCA) for all database installations.

### New Components Available for Installation

The following are the new components available while installing Oracle Database 11g:

- Oracle Application Express: Starting with Oracle Database 11g, HTML DB is no longer available as a Companion CD component. Renamed Oracle Application Express, this component is installed with Oracle Database 11g.
	With Oracle Database 11g, Oracle Application Express replaces iSQL\*Plus.
- Oracle Configuration Manager: This feature is offered during custom installation. It was previously named Customer Configuration repository (CCR). It is an optional component for database and client installations. Oracle Configuration Manager gathers and stores details relating to the configuration of the software stored in Oracle Database home directories.
- Oracle SQL Developer: This feature is installed by default with template-based database installations, such as General Purpose, Transaction Processing, and Data Warehousing. It is also installed with database client Administrator, Run-Time, and Custom installations.
- Oracle Warehouse Builder: This feature is now included as an option in the Oracle Database installation.
- Oracle Real Application Testing: This feature is installed by default with the Enterprise Edition installation type of Oracle Database 11g.
	See Also:
	Oracle Database Performance Tuning Guide for more information about Oracle Real Application Testing

### Enhancements and New Features for Installation

The following are the enhancements and new features for Oracle Database 11g release 1 (11.1).

#### Automatic Diagnostic Repository

Automatic Diagnostic Repository (ADR) is a feature added to Oracle Database 11g. The main objective of this feature is to reduce the time required to resolve bugs. ADR is the layer of the Diagnostic Framework implemented in Oracle Database 11g that stores diagnostic data and also provides service APIs to access data. The default directory that stores the diagnostic data is `ORACLE_BASE\diag`.

Automatic Diagnostic Repository implements the following:

- Diagnostic data for all Oracle products which is written into an on-disk repository
- Interfaces that provide easy navigation of the repository and the capability to read and write data

For Oracle RAC installations, if you use a shared Oracle Database home, then ADR must be located on a shared storage location available to all the nodes.

Oracle Clusterware continues to place diagnostic data in the directory `CRS_home` `\log`, where `CRS_home` is the Oracle Clusterware home.

#### Oracle Automatic Storage Management Fast Mirror Resync

Oracle ASM fast mirror resync quickly resynchronizes Oracle ASM disks within a disk group after transient disk path failures if the disk drive media is not corrupted. Any failures that render a failure group temporarily unavailable are considered transient failures. Disk path malfunctions, such as cable disconnections, host bus adapter or controller failures, or disk power supply interruptions, can cause transient failures. The duration of a fast mirror resync depends on the duration of the outage. The duration of a resynchronization is typically much shorter than the amount of time required to completely rebuild an entire Oracle ASM disk group.

See Also:

Oracle Automatic Storage Management Administrator's Guide

#### Oracle ASM and Oracle RAC Deinstallation and Other Configuration Assistant Enhancements

Oracle Database Configuration Assistant (DBCA), Database Upgrade Assistant (DBUA), and Oracle Net Configuration Assistant (NETCA) have been improved. These improvements include the following:

##### DBCA

- Provides a command-line feature, `deleteASM`, that removes Oracle ASM instances.
- Provides the option to switch from a database configured for Oracle Enterprise Manager Database Control to Oracle Enterprise Manager Grid Control.

##### DBUA

- Includes an improved pre-upgrade script to provide space estimation, initialization parameters, statistics gathering, and new warnings. DBUA also provides upgrades from Oracle Database releases 9.0, 9.2, 10.1, and 10.2.
- Supports in-place patch set upgrades.
- Starts any services that were running before the upgrade.

#### New SYSASM Privilege for Oracle ASM Administration

This feature introduces a new SYSASM privilege that is specifically intended for performing Oracle ASM administration tasks. Using the SYSASM privilege instead of the SYSDBA privilege provides a clearer division of responsibility between Oracle ASM administration and database administration.

#### Oracle ASM Preferred Read Disk Groups

In previous releases, Oracle ASM used the disk with the primary copy of a mirrored extent as the preferred disk for data read operations. With this release, using the new initialization file parameter `asm_preferred_read_failure_groups`, you can specify disks located near a specific cluster node as the preferred disks from which that node obtains mirrored data. This option is presented in DBCA, or you can configure it after installation. This change facilitates faster processing of data with widely distributed shared storage systems or with extended clusters (clusters whose nodes are geographically dispersed), and improves disaster recovery preparedness.

#### Oracle Automatic Storage Management Rolling Migration

Rolling migration for Oracle ASM enables you to upgrade or patch Oracle ASM instances on clustered Oracle ASM nodes without affecting database availability. Rolling migration provides greater availability and a smoother migration of Oracle ASM software from one release to the next. This feature applies to Oracle ASM configurations that run on Oracle Database 11g release 1 (11.1) and later. In other words, you must have Oracle Database 11g release 1 (11.1) installed before you can perform rolling migrations.

Note:

You cannot change the owner of the Oracle ASM or Oracle Database home during an upgrade. You must use the same Oracle software owner that owns the existing Oracle ASM or Oracle Database home.

See Also:

Oracle Automatic Storage Management Administrator's Guide

#### Conversion of Single-Instance Oracle ASM to Clustered Oracle ASM

Using either Oracle Enterprise Manager Grid Control or the `rconfig` script, you can convert an existing Oracle ASM instance from a single-instance storage manager to a clustered storage manager. You can convert Oracle ASM release 11.1 instances directly, and convert releases prior to 11.1 by upgrading the instance to 11.1, and then performing the conversion.

#### Data Mining Schema Creation Option

In Oracle Database 11g, the data mining schema is created when you run the SQL script `catproc.sql` as the SYS user. Therefore, the data mining option is removed from the Database Features screen of DBCA.

#### Oracle Disk Manager Network File System Management

Oracle Disk Manager (ODM) can manage a network file system (NFS) on its own, without using the operating system kernel NFS driver. This is referred to as Direct NFS. Direct NFS implements the NFS version 3 protocol within the Oracle Database kernel. This change enables monitoring of NFS status using the ODM interface. The Oracle Database kernel driver tunes itself to obtain optimal use of available resources.

This feature provides the following:

- Ease of tuning, and diagnosability, by giving the Direct NFS client control over the I/O paths to the network file system, and avoiding the need to tune network performance at the operating system level.
- A highly stable, highly optimized NFS client for database operations.
- Use of the Oracle buffer cache, rather than the file system cache, for simpler tuning.
- A common, consistent NFS interface, capable for use across Linux, UNIX and Windows platforms.
- No requirement for additional configuration of NFS mounts.
	With operating system NFS drivers, NFS drives have to be mounted with the option `noac` (No Attribute Caching) to prevent the operating system NFS driver from optimizing the file system cache (by keeping file attributes locally). ODM automatically recognizes Oracle RAC instances, and performs appropriate operations for data files without requiring additional reconfiguration from users, system administrators, or DBAs.

#### Optimal Flexible Architecture (OFA) Simplified

With the development of stripe and mirror everything (SAME) architecture, and improved storage and throughput capacity for storage devices, the original OFA role of enhancing performance has shifted to a role of providing well-organized Oracle installations with separated software, configuration files, and data. This separation enhances security, and simplifies upgrading, cloning, and other administrative tasks.

Oracle Database 11g release 1 (11.1) incorporates several improvements to OFA to address this changed purpose.

As part of this shift in roles, the following features have been added:

- During Oracle RAC installation, you are prompted to accept the default, or select a location for the Oracle base directory, instead of the Oracle home directory. This change facilitates installation of multiple Oracle home directories in a common location, and separates software units for simplified administration. For this release, you are not required to use the Oracle base directory, but this may become a requirement in a future release.
- With this release, as part of the implementation of Automatic Diagnostic Repository (ADR), the following `admin` directories are changed:
	- `bdump` (location set by the `background_dump_dest` initialization parameter; storage of Oracle background process trace files)
		- `cdump` (location set by the `core_dump_dest` initialization parameter; storage of Oracle core dump files)
		- `udump` (location set by the `user_dump_dest` initialization parameter; storage of Oracle user SQL trace files)
	By default, the location of these trace and core files is in the `\diag` directory, which is in the path `ORACLE_BASE\diag`.
- The initialization parameters `background_dump_dest` and `user_dump_dest` are deprecated. They continue to be set, but you should not set these parameters manually.
- A new initialization parameter is introduced. `diagnostic_dest` contains the location of the ADR base directory, which is the directory under which one or more ADR homes are kept. Oracle documentation commonly refers to these homes as ADR homes. Each database instance has an ADR home, which is the root directory for several other directories that contain trace files, the alert log, health monitor reports, and dumps for critical errors. You can also view alert and trace files with the SQL statement `select name, value from v$diag_info`.
- The default fast recovery area (previously known as the Flash Recovery area) is moved from `ORACLE_HOME\..\flash_recovery_area` to `ORACLE_BASE\flash_recovery_area`.
- The default data file location is moved from `ORACLE_HOME\..\oradata` to `ORACLE_BASE\oradata`.
- A new utility, ADR Command Interpreter (ADRCI), is introduced. ADRCI facilitates reviewing alert log and trace files.

For Oracle RAC installations, Oracle requires that the fast recovery area and the data file location are on a location shared among all the nodes. Oracle Universal Installer (OUI) confirms that this is the case during installation. This change does not affect the location of trace files for Oracle Clusterware.

See Also:

Oracle Database Administrator's Guide for detailed information about these changes, and Oracle Database Utilities for information about viewing alert log and list trace files with ADRCI

#### Oracle Configuration Manager for Improved Support

During a custom installation, you are asked if you want to install Oracle Configuration Manager (OCM). OCM is an optional tool that enables you to associate your configuration information with your My Oracle Support account. This can facilitate handling of service requests by ensuring that server system information is readily available.

Configuring the OCM tool requires that you have the following information from your service agreement:

- Customer Support Identification (CSI) Number
- My Oracle Support user account name
- Country code

In addition, you are prompted for server proxy information if the host system does not have a direct connection to the Internet.

#### Support for Large Data Files

Large data file support is an automated feature that enables Oracle to support larger files on Oracle ASM more efficiently and to increase the maximum file size.

See Also:

Oracle Automatic Storage Management Administrator's Guide

#### Switching a Database from Database Control to Grid Control Configuration

In previous releases, Oracle Database Configuration Assistant (DBCA) contained the functionality to configure databases while creating them either with Database Control or with Grid Control, or to reconfigure databases after creation. However, to change the configuration from Database Control to Grid Control required significant work. With Oracle Database 11g, DBCA enables you to switch configuration of a database from Database Control to Grid Control by running the Oracle Enterprise Manager Configuration Plug-in.

#### New Features in Oracle Database 11g Release 11.1

Oracle Database 11g release 11.1 includes the following:

- ODP.NET configuration improvements:
	- Developers can now configure ODP.NET using configuration files, including application or web config, or `machine.config`.
		- The settings for specific versions of ODP.NET can be configured several ways for specific effects on precedence. For example, `machine.config` settings are.NET framework-wide settings that override the Windows registry values. The application or web config file settings are application-specific settings that override the `machine.config` settings and the Windows registry settings.
- Performance enhancements, such as the following:
	- Improved parameter context caching
		This release enhances the existing caching infrastructure to cache ODP.NET parameter contexts. This enhancement is independent of database version and it is available for all the supported database versions. This feature provides significant performance improvement for the applications that execute the same statement repeatedly.
		- Efficient large object (LOB) retrieval
		This release improves the performance of small-sized LOB retrieval by reducing the number of round-trips to the database. This enhancement is available only with Oracle 11g release 1 or later database releases.
		This enhancement is transparent to the developer. No code changes are needed to use this feature.

## Deprecated Features in Oracle Database 11g Release 2 (11.2)

The following are deprecated with Oracle Database 11g Release 2:

- Oracle Cluster File System (OCFS) for Windows
- Installing files on raw devices is no longer an option available during installation. You must use a shared file system, or use Oracle ASM If you are upgrading from a previous release and currently use raw devices, then your existing raw devices can continue to be used. After upgrade is complete, you can migrate to Oracle ASM or to a shared file system if you choose.

## Deprecated Features in Oracle Database 11g Release 1 (11.1)

The following components that were part of Oracle Database 10g release 2 (10.2) are not available for installation with Oracle Database 11g:

- iSQL\*Plus
- Oracle Workflow
- Data Mining Scoring Engine
- Oracle Enterprise Manager Java console

## Desupported Features in Oracle Database 11g Release 2 (11.2)

The following features are no longer supported with Oracle Database 11g Release 2 (11.2):

- The SYSDBA privilege of acting as administrator on the Oracle ASM instance is removed with this release.
- The `-cleanupOBase` flag of the deinstallation tool is desupported. There is no replacement for this flag.