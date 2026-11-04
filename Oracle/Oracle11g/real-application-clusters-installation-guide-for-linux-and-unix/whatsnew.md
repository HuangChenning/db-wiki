---
title: "What's New in Oracle Real Application Clusters Installation?"
book: Real Application Clusters Installation Guide for Linux and UNIX
doc_id: E41962-05
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/install.112/e41962/whatsnew.htm
tags:
  - oracle
  - 11g
  - real-application-clusters-installation-guide-for-linux-and-unix
---

This section describes new features as they pertain to the installation and configuration of Oracle Real Application Clusters (Oracle RAC). The topics in this section are:

## New Features for Release 2 (11.2.0.4)

The following is a list of new features for Release 2 (11.2.0.4):

### Cluster and Oracle RAC Diagnosability Tools Enhancements

Starting with Oracle Grid Infrastructure 11g Release 2 (11.2.0.4), the Trace File Analyzer and Collector is installed automatically with Oracle Grid Infrastructure installation. The Trace File Analyzer and Collector is a diagnostic collection utility to simplify diagnostic data collection on Oracle Clusterware, Oracle Grid Infrastructure, and Oracle RAC systems.

Note:

The Trace File Analyzer and Collector is available starting with Oracle Grid Infrastructure 11g Release 2 (11.2.0.4).

See Also:

[Oracle Clusterware Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41959/troubleshoot.htm#CWADD92407) for information about using Trace File Analyzer and Collector

### Oracle Database Health Checks and Best Practice Recommendation

Oracle RAC Configuration Audit tool (RACcheck) is available with Oracle Grid Infrastructure 11g Release 2 (11.2.0.4) for assessment of single instance and Oracle RAC database installations for known configuration issues, best practices, regular health checks, and pre- and post upgrade best practices.

Note:

The Oracle RAC Configuration Audit tool is available starting with Oracle Grid Infrastructure 11g Release 2 (11.2.0.4).

See Also:

[Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41960/racchk.htm#RACAD8365)

## Desupported Options for Release 2 (11.2.0.4)

The following features are no longer supported with Oracle Grid Infrastructure 11g Release 2 (11.2.0.4):

### Block and Raw Devices Not Supported with OUI

With this release, OUI no longer supports installation of Oracle Clusterware files on block or raw devices. Install Oracle Clusterware files either on Oracle Automatic Storage Management disk groups, or in a supported shared file system.

### Deprecation of -cleanupOBase

The `-cleanupOBase` flag of the deinstallation tool is deprecated in this release. There is no replacement for this flag.

## New Features for Release 2 (11.2.0.3)

Starting with Oracle Database 11g Release 2 (11.2.0.3) you can enter the Proxy Realm information when providing the details for downloading software updates. The proxy realm identifies the security database used for authentication. If you do not have a proxy realm, then you do not have to provide an entry for the Proxy Username, Proxy Password, and Proxy Realm fields. It is case-sensitive.

This proxy realm is for software updates download only.

## New Features for Release 2 (11.2.0.2)

The following is a list of new features for Release 2 (11.2.0.2):

### Enhanced Patch Set Installation

Starting with the release of the 11.2.0.2 patch set for Oracle Database 11g Release 2, Oracle Database patch sets are full installations of the Oracle Database software. Note the following changes with the new patch set packaging:

- Direct upgrades from previous releases (11.x, 10.x) to the most recent patch set are supported.
- Out-of-place patch set upgrades, in which you install the patch set into a new, separate Oracle home, are the best practices recommendation. In-place upgrades are supported, but not recommended.
- New installations consist of installing the most recent patch set, rather than installing a base release and then upgrading to a patch release.

See Also:

My Oracle Support note 1189783.1, "Important Changes to Oracle Database Patch Sets Starting With 11.2.0.2", available from the following URL:

`https://support.oracle.com`

### New Software Updates Option

Use the Software Updates feature to dynamically download and apply software updates as part of the Oracle Database installation. You can also download the updates separately using the downloadUpdates option and later apply them during the installation by providing the location where the updates are present.

### Oracle Real Application Clusters One Node (Oracle RAC One Node)

Oracle RAC One Node is a single instance of Oracle RAC running on one node in a cluster. You can use Oracle RAC One Node to consolidate many databases onto a single cluster with minimal overhead, and still provide the high availability benefits of failover protection, online rolling patch application, as well as rolling upgrades for the operating system and for Oracle Clusterware. With Oracle RAC One Node you can standardize all Oracle Database deployments across your enterprise.

You can use Oracle Database and Oracle Grid Infrastructure configuration assistants, such as Oracle Database Configuration Assistant (DBCA) and RCONFIG, to configure Oracle RAC One Node databases.

Oracle RAC One Node is a single Oracle RAC database instance. You can use a planned online relocation to start a second Oracle RAC One Node instance temporarily on a new target node, so that you can migrate the current Oracle RAC One Node instance to this new target node. After the migration, the source node instance is shut down. Oracle RAC One Node databases can also fail over to another cluster node within its hosting server pool if their current node fails.

Oracle RAC One Node is not supported if you use a third-party clusterware software, such as Veritas, SFRAC, IBMPowerHA, or HP Serviceguard. Sun Solaris Cluster is not supported at this time.

With Oracle Database release 2 (11.2.0.2), Oracle RAC One Node is supported on all platforms where Oracle Real Application Clusters (Oracle RAC) is certified.

### Redundant Interconnect Usage

In previous releases, to make use of redundant networks for the interconnect, bonding, trunking, teaming, or similar technology was required. Oracle Grid Infrastructure and Oracle RAC can now make use of redundant network interconnects, without the use of other network technology, to enhance optimal communication in the cluster. This functionality is available starting with Oracle Database 11g Release 2 (11.2.0.2).

Redundant Interconnect Usage enables load-balancing and high availability across multiple (up to four) private networks (also known as interconnects).

## New Features for Release 2 (11.2)

The following is a list of new features for Release 2 (11.2)

### Oracle Automatic Storage Management and Oracle Clusterware Installation

With Oracle Clusterware 11g release 2 (11.2), Oracle Automatic Storage Management (Oracle ASM) is part of the Oracle Grid Infrastructure installation. In an Oracle Clusterware and Oracle RAC installation, Oracle ASM is installed in the Oracle Clusterware home. In addition, Oracle ASM can be configured to require separate administrative privileges, so that membership in OSDBA may no longer provide administrator access to both the database and the storage tiers.

### Oracle Automatic Storage Management Cluster File System (ACFS)

Oracle Automatic Storage Management Cluster File System (Oracle ACFS) is a new multi-platform, scalable file system and storage management design that extends Oracle Automatic Storage Management (Oracle ASM) technology to support all application data. Oracle ACFS provides dynamic file system resizing, and improved performance using the distribution, balancing and striping technology across all available storage, and provides storage reliability through Oracle ASM's mirroring and parity protection.

Oracle ACFS is available for Linux. It is not available for UNIX platforms at the time of this release.

### Cluster Verification Utility Fixup Scripts and Grid Infrastructure Checks

Cluster Verification Utility (CVU) has the following new features:

- CVU can generate shell scripts (Fixup scripts) that perform the system configuration that is required for a successful installation, in addition to identifying system issues that can cause installation failures.
- CVU provides additional checks to address install, configuration and operational issues.
- CVU is automatically called by OUI to verify prerequisites, and will prompt you to create fixup scripts to correct many system configuration issues that prevent installation.

### Database Agent and Listeners

DBCA no longer sets the value for LOCAL\_LISTENER. When Oracle Clusterware starts the database resource, it updates the instance parameters. The LOCAL\_LISTENER is set to the virtual IP endpoint of the local node listener address. You should not modify the setting for LOCAL\_LISTENER. New installation instances only register with Single Client Access Name (SCAN) listeners as remote listeners. SCANs are virtual IP addresses assigned to the cluster, rather than to individual nodes, so cluster members can be added or removed without requiring updates of clients served by the cluster. Upgraded databases will continue to register with all node listeners, and additionally with the SCAN listeners.

### Daylight Savings Time Upgrade of Timestamp with Timezone Data Type

When time zone version files are updated due to Daylight Saving Time changes, TIMESTAMP WITH TIMEZONE (TSTZ) data could become stale. In previous releases, database administrators ran the SQL script `utltzuv2.sql` to detect TSTZ data affected by the time zone version changes and then had to carry out extensive manual procedures to update the TSTZ data.

TSTZ data is updated transparently with very minimal manual procedures using newly provided DBMS\_DST PL/SQL packages. In addition, there is no longer a need for clients to patch their time zone data files.

See Also:

[Oracle Database Upgrade Guide](https://docs.oracle.com/cd/E11882_01/server.112/e23633/toc.htm) for information about preparing to upgrade Timestamp with Time Zone data, [Oracle Database Globalization Support Guide](https://docs.oracle.com/cd/E11882_01/server.112/e10729/toc.htm) for information about how to upgrade the Time Zone file and Timestamp with Time Zone data, and [Oracle Call Interface Programmer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e10646/toc.htm) for information about performance effects of clients and servers operating with different versions of Time Zone files

### Enterprise Manager Database Control Provisioning

Database Control 11g provides the capability to automatically provision Oracle Clusterware and Oracle RAC installations on new nodes, and then extend the existing Oracle Clusterware and Oracle RAC database to these provisioned nodes. This provisioning procedure requires a successful Oracle RAC installation before you can use this feature.

See Also:

[Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41960/toc.htm) for information about this feature

### Enterprise Manager Clusterware Resource Management

You can use Enterprise Manager Cluster Home page to perform full administrative and monitoring support for High Availability Application and Oracle Clusterware resource management. Such administrative tasks include creating and modifying server pools.

### Grid Plug and Play

In the past, adding or removing servers in a cluster required extensive manual preparation. Grid Plug and Play reduces the costs of installing, configuring, and managing server nodes by using a grid naming service within the cluster to enable each node to perform the following tasks dynamically:

- Negotiating appropriate network identities for itself
- Acquiring additional information it needs to operate from a configuration profile
- Configuring or reconfiguring itself using profile data, making hostnames and addresses resolvable on the network

As servers perform these tasks dynamically, adding and removing nodes simply requires an administrator to connect the server to the cluster, and to enable the cluster to configure the node. Using Grid Plug and Play, and using best practices recommendations, adding a node to the database cluster is part of the normal server restart, and removing a node from the cluster occurs automatically when a server is turned off.

### Improved Deployment, Deconfiguration and Deinstallation

Oracle configuration assistants provide additional guidance to ensure recommended deployment, and to prevent configuration issues. In addition, configuration assistants validate configurations, and provide scripts to fix issues, which you can choose to use, or reject. If you accept the fix scripts, then configuration issues will be fixed automatically.

Oracle configuration assistants provide the capability of deconfiguring and deinstalling Oracle Real Application Clusters, without requiring additional manual steps.

### SCAN Addresses for Simplified Client Access

The Single Client Access Name (SCAN) is the address to provide for all clients connecting to the cluster. The SCAN is a domain name registered to three IP addresses, either in the domain name service (DNS) or the Grid Naming Service (GNS). SCANs eliminate the need to change clients when nodes are added to or removed from the cluster. Clients using SCANs can also access the cluster using Easy Connect.

### Zero Downtime Patching for Oracle RAC

Opatch now can apply patches in multi-node, multi-patch fashion, and will not start up instances that have a non-rolling patch applied to it, if other instances of the database do not have that patch. Opatch also detects if the database schema is an earlier patch level than the new patch, and it runs SQL commands to bring the schema up to the new patch level.

See Also:

[Oracle Universal Installer and OPatch User's Guide for Windows and UNIX](https://docs.oracle.com/cd/E11882_01/em.112/e12255/oui7_opatch.htm#OUICG305)

### Deprecated Options with Oracle RAC 11g Release 2 (11.2)

Note the following changes with this release:

- Installing files on raw devices is no longer an option available during installation. You must use a shared file system, or use Oracle Automatic Storage Management. If you are upgrading from a previous release and currently use raw devices, then your existing raw devices can continue to be used. After upgrade is complete, you can migrate to Oracle ASM or to a shared file system if you choose.
- The SYSDBA privilege of acting as administrator on the Oracle ASM instance is removed with this release, unless the operating system OSDBA group for the database is the same group that is designated as the OSASM group for Oracle Automatic Storage Management.
- If separate Oracle ASM access privileges are enabled, and database administrators are not members of the OSASM group, then database administrators must be a member of the OSDBA for Oracle ASM group to be able to access Oracle ASM files You can designate the OSDBA group for the Oracle RAC database as the OSDBA group for the Oracle ASM instance.

## New Features for Release 1(11.1)

The following is a list of new features for Oracle RAC 11g release 1 (11.1):

Note:

Some features in this list have been superseded by changes in the 11.2 release, particularly those listed for Oracle ASM.

### Changes in Installation Documentation

With Oracle Database 11g release 1, Oracle Clusterware can be installed or configured as an independent product, and additional documentation is provided on storage administration. For installation planning, note the following documentation:

#### Oracle Database 2 Day + Real Application Clusters Guide

This book provides an overview and examples of the procedures to install and configure a two-node Oracle Clusterware and Oracle RAC environment.

#### Oracle Grid Infrastructure Installation Guide

This platform-specific book provides procedures either to install Oracle Clusterware as a standalone product, or to install Oracle Clusterware with either Oracle Database, or Oracle RAC. It contains system configuration instructions that require system administrator privileges.

#### Oracle Real Application Clusters Installation Guide

This book (the guide that you are reading) provides procedures to install Oracle RAC after you have completed successfully an Oracle Clusterware installation. It contains database configuration instructions for database administrators.

#### Oracle Database Storage Administrator's Guide

This book provides information for database and storage administrators who administer and manage storage, or who configure and administer Oracle Automatic Storage Management (Oracle ASM).

#### Oracle Clusterware Administration and Deployment Guide

This is the administrator's reference for Oracle Clusterware. It contains information about administrative tasks, including those that involve changes to operating system configurations, and cloning Oracle Clusterware.

#### Oracle Real Application Clusters Administration and Deployment Guide

This is the administrator's reference for Oracle RAC. It contains information about administrative tasks. These tasks include database cloning, node addition and deletion, Oracle Cluster Registry (OCR) administration, use of SRVCTL and other database administration utilities, and tuning changes to operating system configurations.

### Changes in the Install Options

The following are installation option changes for Oracle Database 11g:

- Oracle Application Express: This feature is installed with Oracle Database 11g. It was previously named HTML DB, and was available as a separate Companion CD component.
- Oracle Configuration Manager: Oracle Configuration Manager (OCM) is integrated with Oracle Universal Installer. However, it is an optional component with database and client installations. Oracle Configuration Manager, used in previous releases as Customer Configuration Repository (CCR), is a tool that gathers and stores details relating to the configuration of the software stored in the Oracle ASM and database Oracle home directories.
- Oracle Data Mining: The Enterprise Edition installation type selects Oracle Database Mining option by default. In Oracle Database 11g, the Data Mining metadata is created with `SYS` metadata when you select the Create Database option.
- Oracle Database: This feature is integrated with Oracle Universal Installer. However, it is an optional component for database installation.
- Oracle SQL Developer: This feature is installed by default with template-based database installations, such as General Purpose, Transaction Processing, and Data Warehousing. It is also installed with database client Administrator, Runtime, and Advanced installations.
- Oracle Warehouse Builder: This information integration tool is now installed with both Standard and Enterprise Edition versions of the Oracle Database. With Enterprise Edition, you can purchase additional extension processes. Installing the Oracle Database also installs a pre-seeded repository, `OWBSYS`, necessary for using Oracle Warehouse Builder.
- Oracle Ultra Search: Starting with Oracle Database 11g, Oracle Ultra Search is integrated with Oracle Database. In the previous releases, this product was available as a Companion CD component.
- Oracle XML DB: Starting with Oracle Database 11g, Oracle XML DB is no longer an optional feature. It is installed and configured using Database Configuration Assistant for all database installations.

### New Components Available for Installation

The following are the new components available while installing Oracle Database 11g:

- Oracle Application Express: Starting Oracle Database 11g, HTML DB is no longer available as a Companion CD component. Renamed as Oracle Application Express, this component is installed with Oracle Database 11g.
	With Oracle Database 11g, Oracle Application Express replaces iSQL\*Plus.
	See Also:
	[Oracle Application Express User's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e11947/toc.htm) for more information about Oracle Application Express
- Oracle Configuration Manager: This feature is offered during Advanced installation. It was previously named Customer Configuration repository (CCR). It is an optional component for database and client installations. Oracle Configuration Manager gathers and stores details relating to the configuration of the software stored in database Oracle home directories.
- Oracle Database Vault: This feature is an optional component for database installation.
	See Also:
	[Oracle Database Vault Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e23090/toc.htm) for more information about Oracle Database
- Oracle Real Application Testing: This feature is installed by default with the Enterprise Edition installation type of Oracle Database 11g.
	See Also:
	[Oracle Database Real Application Testing User's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41481/rat_intro.htm#RATUG101) for more information about Oracle Real Application Testing
- Oracle SQL Developer: This feature is installed by default with template-based database installations, such as General Purpose, Transaction Processing, and Data Warehousing. It is also installed with database client Administrator, Runtime, and Advanced installations.
	See Also:
	[Oracle SQL Developer User's Guide](https://docs.oracle.com/cd/E11882_01/doc.112/e12152/intro.htm#RPTUG10000) for more information about Oracle SQL Developer
- Oracle Warehouse Builder: This feature is now included as an option in the Database installation.
	Note:
	With Standard Edition and Enterprise Edition versions of Oracle Database 11g release 2 (11.2), Oracle Warehouse Builder with basic features is installed. However, with Enterprise Edition, you can purchase options that extend Oracle Warehouse Builder.
	See Also:
	[Oracle Warehouse Builder Sources and Targets Guide](https://docs.oracle.com/cd/E11882_01/owb.112/e10582/toc.htm) for more information about Oracle Warehouse Builder

### Enhancements and New Features for Installation

The following is a list of enhancements and new features for Oracle Database 11g release 2 (11.2):

#### Automatic Diagnostic Repository

The Automatic Diagnostic Repository is a feature added to Oracle Database 11g. The main objective of this feature is to reduce the time required to resolve bugs. Automatic Diagnostic Repository is the layer of the Diagnostic Framework implemented in Oracle Database 11g that stores diagnostic data and also provides service APIs to access data. The default directory that stores the diagnostic data is `$ORACLE_BASE/diag`.

The Automatic Diagnostic Repository implements the following:

- Diagnostic data for all Oracle products is written into an on-disk repository.
- Interfaces that provide easy navigation of the repository, and the capability to read and write data

For Oracle RAC installations, if you use a shared Oracle Database home, then the Automatic Data Repository must be located on a shared storage location that is available to all the nodes.

Oracle Clusterware continues to store diagnostic data in the directory `Grid_home` `/log`, where `Grid_home` is the Oracle Clusterware home.

#### Oracle Automatic Storage Management Fast Mirror Resync

Oracle ASM fast mirror resync quickly resynchronizes Oracle ASM disks within a disk group after transient disk path failures as long as the disk drive media is not corrupted. Any failures that render a failure group temporarily unavailable are considered transient failures. Disk path malfunctions, such as cable disconnections, host bus adapter or controller failures, or disk power supply interruptions, can cause transient failures. The duration of a fast mirror resync depends on the duration of the outage. The duration of a resynchronization is typically much shorter than the amount of time required to completely rebuild an entire Oracle ASM disk group.

See Also:

[Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e18951/toc.htm)

#### Oracle ASM, Deinstallation, and Other Configuration Assistant Enhancements

ASM Configuration Assistant (ASMCA) is a new configuration tool that can run from the Oracle Grid Infrastructure for a cluster home. ASMCA configures ASM instances, diskgroups, volumes, and file systems. ASMCA is run during installation, and can be used as an administration configuration tool, like DBCA.

Database Configuration Assistant (DBCA), Database Upgrade Assistant (DBUA), and Oracle Net Configuration Assistant (NETCA) have been improved. These improvements include the following:

##### DBCA

DBCA is enhanced with the following feature:

- Provides the option to switch from a database configured for Oracle Enterprise Manager Database Control to Oracle Enterprise Manager Grid Control.

##### DBUA

DBUA is enhanced with the following features:

- Includes an improved pre-upgrade script to provide space estimation, initialization parameters, statistics gathering, and new warnings. DBUA also provides upgrades from Oracle Database releases 9.0, 9.2, 10.1, and 10.2.
- Update for Oracle Database 11g release 11.2: Also provides upgrades for 11.1.
	Only out-of-place upgrades are supported.
- Starts any services running prior to upgrades

##### Deinstallation Tool

Includes a deinstallation tool (`deinstall`), which is available in the installation media before installation, and is available in Oracle home directories after installation. It is located in the path $ORACLE\_HOME/deinstall. The script stops Oracle software, and removes Oracle software and configuration files on the operating system.

#### New SYSASM Privilege and OSASM group for Oracle ASM Administration

This feature introduces a new `SYSASM` privilege that is specifically intended for performing Oracle ASM administration tasks. Using the `SYSASM` privilege instead of the `SYSDBA` privilege provides a clearer division of responsibility between Oracle ASM administration and database administration.

OSASM is a new operating system group that is used exclusively for Oracle ASM. Members of the OSASM group can connect as SYSASM using operating system authentication and have full access to Oracle ASM.

#### Oracle ASM Preferred Read Disk Groups

In previous releases, Oracle ASM used the disk with the primary copy of a mirrored extent as the preferred disk for data reads. With this release, using the new initialization file parameter `asm_preferred_read_failure_groups`, you can specify disks located near a specific cluster node as the preferred disks from which that node obtains mirrored data. This option is presented in Database Configuration Assistant (DBCA), and can be configured after installation. This change facilitates faster processing of data with widely distributed shared storage systems or with extended clusters (clusters whose nodes are geographically dispersed), and improves disaster recovery preparedness.

#### Oracle Automatic Storage Management Rolling Migration

Rolling migration for Oracle ASM enables you to upgrade or patch Oracle ASM instances on clustered Oracle ASM nodes without affecting database availability. Rolling migration provides greater availability and more graceful migration of Oracle ASM software from one release to the next. This feature applies to Oracle ASM configurations that run on Oracle Database 11g release 1 (11.1) and later. In other words, you must already have Oracle Database 11g release 1 (11.1) installed before you can perform rolling migrations.

Note:

You cannot change the owner of the Oracle ASM or Oracle Database home during an upgrade. You must use the same Oracle software owner that owns the existing Oracle ASM or Oracle Database home.

See Also:

[Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e18951/toc.htm)

#### Data Mining Schema Creation Option

In Oracle Database 11g, the data mining schema is created when you run the SQL script `catproc.sql` as the SYS user. Therefore, the data mining option is removed from the Database Features screen of Database Configuration Assistant.

#### Oracle Disk Manager Network File System Management

Oracle Disk Manager (ODM) can manage network file systems (NFS) on its own, without using the operating system kernel NFS driver. This is referred to as Direct NFS. Direct NFS implements NFS version 3 protocol within the Oracle Database kernel. This change enables monitoring of NFS status using the ODM interface. The Oracle Database kernel driver tunes itself to obtain optimal use of available resources.

This feature provides the following:

- Ease of tuning, and diagnosability, by providing the Oracle kernel control over the input-output paths to Network File Server, and avoiding the need to tune network performance at the operating system level.
- A highly stable, highly optimized NFS client for database operations.
- Use of the Oracle network file system layer for user tasks, reserving the operating system kernel network file system layer for network communication.
- Use of the Oracle buffer cache, rather than the file system cache, for simpler tuning.
- A common, consistent NFS interface, capable for use across Linux, UNIX and Windows platforms.
- Oracle RAC aware NFS performance. With operating system NFS drivers, even though NFS is a shared file system, NFS drives have to be mounted with the option `noac` (NO Attribute Caching) to prevent the operating system NFS driver from optimizing the filesystem cache by storing file attributes locally. ODM NFS automatically recognizes Oracle RAC instances, and performs appropriate operations for datafiles without requiring additional reconfiguration from users, system administrators, or DBAs. If you store the Oracle Clusterware voting disks or Oracle Cluster Registry (OCR) files on NFS, then you must continue to require mounting voting disks with the `noac` option.

#### Optimal Flexible Architecture (OFA) Simplified

With the development of Stripe and Mirror Everything architecture (SAME), and improved storage and throughput capacity for storage devices, the original OFA mission to enhance performance has shifted to its role of providing well-organized Oracle installations with separated software, configuration files and data. This separation enhances security, and simplifies upgrade, cloning, and other administrative tasks.

Oracle Database 11g release 2 (11.2) incorporates several changes to OFA to address this changed purpose.

As part of this change:

- During Oracle RAC installation, you are prompted to accept the default, or select a location for the Oracle base directory, instead of the Oracle home directory. This change facilitates installation of more than one Oracle home directory in a common location, and separates software units for simplified administration.
- With this release, as part of the implementation of Automatic Diagnostic Repository (ADR), the following `admin` directories are changed:
	- `bdump` (location set by the `background_dump_dest` initialization parameter; storage of Oracle background process trace files)
		- `cdump` (location set by the `core_dump_dest` initialization parameter; storage of Oracle core dump files)
		- `udump` (location set by the `user_dump_dest` initialization parameter; storage of Oracle user SQL trace files)
	By default, the location of these trace and core files is in the `/diag` directory, which is in the path `$ORACLE_BASE/diag`.
- The initialization parameters `BACKGROUND_DUMP_DEST` and `USER_DUMP_DEST` are deprecated. They continue to be set, but you should not set these parameters manually.
- A new initialization parameter is introduced. `DIAGNOSTIC_DEST` contains the location of "ADR base", which is the base directory under which one or more Automatic Database Repository homes are kept. Oracle documentation commonly refers to these homes as ADR homes. Each database instance has an ADR home, which is the root directory for a number of other directories that contain trace files, the alert log, health monitor reports, and dumps for critical errors. You can also view alert and trace files with the SQL statement `select name, value from v$diag_info`.
- The default Fast Recovery Area (formerly known as Flash Recovery Area) is moved from `$ORACLE_HOME/../recovery_area` to `$ORACLE_BASE/recovery_area`.
- The default data file location is moved from `$ORACLE_HOME/../oradata` to `$ORACLE_BASE/oradata`.
- A new utility, The ADR Command Interpreter (ADRCI), is introduced. The ADRCI facilitates reviewing alert log and trace files.

For Oracle RAC installations, Oracle requires that the Fast Recovery Area and the data file location are on a location shared among all the nodes. The Oracle Universal Installer confirms that this is the case during installation.

This change does not affect the location of trace files for Oracle Clusterware.

See Also:

[Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/toc.htm) for detailed information about these changes, and [Oracle Database Utilities](https://docs.oracle.com/cd/E11882_01/server.112/e22490/toc.htm) for information about viewing alert log and list trace files with ADRCI

#### Oracle Configuration Manager for Improved Support

During installation, you are asked if you want to install Oracle Configuration Manager (OCM). OCM is an optional tool that enables you to associate your configuration information with your My Oracle Support account (formerly OracleMetalink). This can facilitate handling of service requests by ensuring that server system information is readily available.

Configuring the OCM tool requires that you have the following information from your service agreement:

- My Oracle Support e-mail address/username
- Password

In addition, you are prompted for server proxy information, if the host system does not have a direct connection to the Internet.

#### Support for Large Data Files

Large data file support is an automated feature that enables Oracle to support larger files on Oracle ASM more efficiently, and to increase the maximum file size.

See Also:

[Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e18951/toc.htm)

#### Switching a Database from Database Control to Grid Control Configuration

In previous releases, Database Configuration Assistant contains the functionality to configure databases while creating them either with Database Control or with Grid Control, or to reconfigure databases after creation. However, if you want to change the configuration from Database to Grid control, this requires significant work. With Oracle Database 11g, Database Configuration Assistant enables you to switch configuration of a database from Database Control to Grid Control by running the Oracle Enterprise Manager Configuration Plug-in.

### Deprecated Components in Oracle Database 11g Release 1 (11.1)

The following components that were part of Oracle Database 10g release 2 (10.2) are not available for installation with Oracle Database 11g:

- iSQL\*Plus
- Oracle Workflow
- Data Mining Scoring Engine
- Oracle Enterprise Manager Java console