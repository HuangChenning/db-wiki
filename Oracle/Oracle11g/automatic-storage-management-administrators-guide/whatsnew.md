---
title: "What's New in Oracle Automatic Storage Management?"
book: "Automatic Storage Management Administrator's Guide"
doc_id: E18951-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e18951/whatsnew.htm
tags:
  - oracle
  - 11g
  - automatic-storage-management-administrators-guide
---

This chapter describes the new features for Oracle Automatic Storage Management (Oracle ASM).

This chapter contains the following topics:

See Also:

[Oracle Database New Features Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41360/toc.htm) for a complete description of the new features in Oracle Database 11g release 2 (11.2)

## Oracle Automatic Storage Management 11g Release 2 (11.2.0.3) New Features

Note:

This functionality is available starting with Oracle Automatic Storage Management 11g Release 2 (11.2.0.3).

This section describes the Oracle Automatic Storage Management (Oracle ASM) 11g release 2 (11.2.0.3) new features:

- Read-write Oracle ACFS snapshots
	This feature supports read-write snapshots on Oracle ACFS file systems. For information about Oracle ACFS snapshots, refer to ["About Oracle ACFS Snapshots"](asmfilesystem.md).
	The `acfsutil` `snap` commands support read-write snapshots. For information about these commands, refer to ["Oracle ACFS Command-Line Utilities for Multiple Environments"](asmfs_util010.md).
- Support for Oracle ACFS Security and Encryption on Windows
	This feature supports Oracle ACFS Security and Encryption on Windows platforms. For information about security and encryption functionality, refer to ["Oracle ACFS Security"](asmfilesystem.md) and ["Oracle ACFS Encryption"](asmfilesystem.md).
- Support for Oracle ACFS Replication and Tagging on Windows
	This feature supports Oracle ACFS Replication and Tagging on Windows platforms. For information about replication and tagging functionality, refer to ["Oracle ACFS Replication"](asmfilesystem.md) and ["Oracle ACFS Tagging"](asmfilesystem.md).
- Support for additional file types
	Oracle ACFS supports, without snapshots, RMAN backups, archive logs, and Data Pump dumpsets. For more information, refer to ["Overview of Oracle ACFS"](asmfilesystem.md).

## Oracle Automatic Storage Management 11g Release 2 (11.2.0.2) New Features

Note:

This functionality is available starting with Oracle Automatic Storage Management 11g Release 2 (11.2.0.2). For release 2 (11.2.0.2), Oracle ACFS encryption, replication, security, and tagging are available on Linux.

This section describes the Oracle Automatic Storage Management (Oracle ASM) 11g release 2 (11.2.0.2) new features:

- Oracle ACFS security
	The Oracle ACFS security feature provides realm-based security for Oracle ACFS file systems.
	Oracle ACFS security enables you to create realms to specify security policies for users and groups to determine access on file system objects. The Oracle ACFS security feature provides a finer-grained access control on top of the access control provided by the operating system.
	Oracle ACFS security can use the encryption feature to protect the contents of realm-secured files stored in Oracle ACFS file systems.
	Note:
	Oracle ACFS security is not supported if the file system has been replicated with Oracle ACFS replication.
	For more information, refer to ["Oracle ACFS Security"](asmfilesystem.md), ["Securing Oracle ACFS File Systems"](asmfs_util001.md), and ["Oracle ACFS Command-Line Tools for Security"](asmfs_util008.md).
- Oracle ACFS encryption
	The Oracle ACFS encryption feature enables you to encrypt data stored on disk (data-at-rest).
	Oracle ACFS encryption protects data in an Oracle ACFS file system in encrypted format to prevent unauthorized use of data in the case of data loss or theft.
	Note:
	Encryption is not supported if the file system has been replicated with Oracle ACFS replication.
	For more information, refer to ["Oracle ACFS Encryption"](asmfilesystem.md), ["Encrypting Oracle ACFS File Systems"](asmfs_util001.md), and ["Oracle ACFS Command-Line Tools for Encryption"](asmfs_util009.md).
- Oracle ACFS replication
	This feature enables replication of Oracle ACFS file systems across the network to a remote site, providing disaster recovery capability for the file system.
	This release of the feature supports only one standby file system for each primary file system.
	Note:
	- Oracle ACFS replication is not supported if the file system has been encrypted with Oracle ACFS encryption.
	- Oracle ACFS replication is not supported if the file system has been prepared for Oracle ACFS security.
	For more information, refer to ["Oracle ACFS Replication"](asmfilesystem.md), ["Replicating Oracle ACFS File Systems"](asmfs_util001.md), and ["Oracle ACFS Command-Line Tools for Replication"](asmfs_util007.md).
- Oracle ACFS tagging
	This feature provides a method for relating a group of files based on a common naming attribute assigned to these files called a tag name. Oracle ACFS Replication can use this tagging feature to select specific files with a unique tag name for replication to a different remote cluster site. This tagging option reduces the need to replicate an entire Oracle ACFS file system.
	For more information, refer to ["Oracle ACFS Tagging"](asmfilesystem.md), ["Tagging Oracle ACFS File Systems"](asmfs_util001.md), and ["Oracle ACFS Command-Line Tools for Tagging"](asmfs_util006.md).
- New configuration wizard for cluster configuration outside of software installation
	This feature provides a wizard to configure an Oracle Grid Infrastructure environment after the installation has completed and has been tested.
	For more information, refer to ["Configuring Oracle Grid Infrastructure with the Configuration Wizard"](asminst.md).
- Oracle ACFS functionality on the Solaris operating system
	This feature provides Oracle ACFS functionality on the Solaris operating system.
	For more information, refer to ["Oracle ACFS Command-line Tools for the Solaris Environment"](asmfs_util003.md).
- Oracle ACFS functionality on the AIX operating system
	This feature provides Oracle ACFS functionality on the AIX operating system.
	For more information, refer to ["Oracle ACFS Command-line Tools for the AIX Environment"](asmfs_util004.md).
- Oracle ASM Configuration Assistant enhancements
	These enhancements to ASMCA provide support for Oracle ACFS file system security and encryption.
	For more information, refer to ["Managing Security and Encryption for Oracle ACFS File Systems with Oracle ASM Configuration Assistant"](asmca.md).

## Oracle Automatic Storage Management 11g Release 2 (11.2.0.1) New Features

This section describes the Oracle Automatic Storage Management (Oracle ASM) 11g release 2 (11.2.0.1) new features:

- Oracle Automatic Storage Management Cluster File System (Oracle ACFS)
	Oracle Automatic Storage Management Cluster File System (Oracle ACFS) is a new multi-platform, scalable file system, and storage management design that extends Oracle ASM technology to support all of your application data in both single host and cluster configurations. Additionally, Oracle ACFS provides snapshot functionality for a point-in-time copy of an Oracle ACFS system.
	For more information, see ["Overview of Oracle ACFS"](asmfilesystem.md).
- Oracle ASM Dynamic Volume Manager
	Oracle ASM Dynamic Volume Manager (Oracle ADVM) provides volume management services and a standard disk device driver interface to clients. File systems and other disk-based applications send I/O requests to Oracle ADVM volume devices as they would to other storage devices on a vendor operating system.
	Oracle Automatic Storage Management Cluster File System (Oracle ACFS) is layered on Oracle ASM through the Oracle ADVM interface. With the addition of Oracle ADVM, Oracle ASM becomes a complete storage solution for both database and non-database file needs.
	For more information, see ["Overview of Oracle ASM Dynamic Volume Manager"](asmfilesystem.md).
- Oracle Automatic Storage Management Cluster File System Snapshots
	An Oracle ACFS Snapshot is a point-in-time copy of a file system that can provide up to 63 snapshot images. Oracle ACFS Snapshot performs fast creation of persistent Oracle ACFS images at a specific point in time with very low overhead leveraging the Copy-on-Write (COW) technology.
	Even as the file system changes, the snapshot does not, giving you the ability to view the file system as it was at the time the snapshot was created. Initially, snapshots are read-only, which preserves the point in time they captured.
	For more information, see ["About Oracle ACFS Snapshots"](asmfilesystem.md).
- Oracle ASM Configuration Assistant (ASMCA)
	Oracle ASM Configuration Assistant provides a GUI interface for installing and configuring Oracle ASM instances, disk groups, volumes, and file systems.
	In addition, the ASMCA command-line interface provides functionality for installing and configuring Oracle ASM instances, disk groups, volumes, and file systems in a non-GUI utility.
	For more information about using Oracle ASM Configuration Assistant, see [Chapter 11, "Oracle ASM Configuration Assistant"](asmca.md).
- ASMCMD Enhancements
	This feature extends Oracle ASM Command Line Utility (ASMCMD) to provide full functionality, so that any operation that can be performed with SQL commands can be performed with ASMCMD. The added functionality includes the following areas:
	- Disk, failure group, and disk group operations
		- Disk group attribute operations
		- Oracle ASM File Access Control user and group operations
		- Template operations
		- Oracle ASM instance operations
		- File operations
		- Oracle ASM volume operations
	Changes were also made to standardize ASMCMD command-line and command options.
	For more information about ASMCMD commands, see ["Types of ASMCMD Commands"](asm_util001.md).
- Intelligent Data Placement
	The Intelligent Data Placement feature enables you to specify disk regions on Oracle ASM disks to ensure that frequently accessed data is placed on the outermost (hot) tracks which provide higher performance.
	For more information, see ["Intelligent Data Placement"](asmdiskgrps.md).
- Specifying the Sector Size for Disk Drives
	Oracle ASM provides the capability to specify a sector size of 512 bytes or 4096 kilobytes with the `SECTOR_SIZE` disk group attribute when creating disk groups. Oracle ASM provides support for 4 KB sector disk drives without a performance penalty.
	For information about setting the sector size for disk drives, see ["Specifying the Sector Size for Drives"](asmdiskgrps.md).
	See Also:
	[Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_5008.htm#SQLRF01114) for information about the disk group attributes and the [`CREATE DISKGROUP`](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_5008.htm#SQLRF01114) SQL statement
- Disk Group Rename
	The `renamedg` tool enables you to change the name of a cloned disk group.
	For information about renaming disk groups with `renamedg`, see ["Renaming Disks Groups"](asmdiskgrps.md).
- Oracle ASM File Access Control
	Oracle ASM on Linux and UNIX platforms implements access control on its files to isolate different database instances from each other and prevent accidental access that could lead to the corruption of data files. Oracle ASM implements new SQL statements and ASMCMD commands to grant, modify, and deny file permissions. The new security model and syntax is consistent with those that have been implemented for the objects represented in an Oracle database.
	This feature enables multiple database instances to store their Oracle ASM files in the same disk group and be able to consolidate multiple databases while preventing an unauthorized database instance from accessing and overwriting files of a different instance.
	For more information about Oracle ASM File Access Control, see ["Managing Oracle ASM File Access Control for Disk Groups"](asmdiskgrps.md), ["Managing Oracle ASM File Access Control with Oracle Enterprise Manager"](asm_em.md), and ["ASMCMD File Access Control Commands"](asm_util006.md).
- Oracle Cluster Registry (OCR) and Voting Files stored in Oracle ASM
	This feature enables storage of Oracle Cluster Registry (OCR) and the voting file in Oracle ASM disk groups. This functionality enables Oracle ASM to provide a unified storage solution, storing all the data for the clusterware and the database, without the need for third-party volume managers or cluster file systems.
	For more information, see ["Oracle Cluster Registry and Voting Files in Oracle ASM Disk Groups"](asmdiskgrps.md).
	See Also:
	[Oracle Clusterware Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41959/admin.htm#CWADD838) for information about administering voting files and Oracle Cluster Registry (OCR)
- Oracle Restart
	Oracle Restart enables the startup and automatic restart of single-instance Oracle Database through the Cluster Ready Services (CRS) component of Oracle Clusterware on a single server. This provides higher availability and automated management of single-instance Oracle Database and Oracle ASM instances.
	For more information, see ["Using Oracle Restart"](asminst.md).
	See Also:
	- [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/restart.htm#ADMIN12721) for information about configuring and administering Oracle Restart
	- [Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41960/srvctladmin.htm#RACAD005) for information about automatically restarting single-instance databases residing on an Oracle RAC node
- Oracle Enterprise Manager Support of Oracle ACFS
	Oracle Enterprise Manager has enhanced Oracle ASM support to enable you to manage Oracle Automatic Storage Management Cluster File System (Oracle ACFS) technology and Oracle ASM Dynamic Volume Manager. These features operate as a comprehensive management solution to extend Oracle ASM technology to support all your application data files in database and non-database and in both single host and cluster configurations.
	Oracle Enterprise Manager supports the following:
	- Create, modify, and delete Oracle ACFS
		- Monitor space usage and performance features of Oracle ACFS
		- Support Oracle ASM Dynamic Volume Manager features as required by Oracle ACFS
	For more information about using Oracle Enterprise Manager to administer Oracle ASM, see [Chapter 10, "Administering Oracle ACFS with Oracle Enterprise Manager"](asmfs_em.md).
- Oracle Enterprise Manager Database Control Enhancements for Improved Oracle ASM Manageability
	Oracle Enterprise Manager has been enhanced to manage Oracle ASM features, such as Oracle ASM File Access Control, OCR and voting files in Oracle ASM, disk resync, Oracle ASM rolling migrations, disk regions, and Oracle ASM manageability and infrastructure.
	For more information about using Oracle Enterprise Manager to administer Oracle ASM, see [Chapter 9, "Administering Oracle ASM with Oracle Enterprise Manager"](asm_em.md).
- Oracle Enterprise Manager Oracle ASM Support Workbench
	Oracle Enterprise Manager Oracle ASM Support Workbench has been enhanced to help diagnose and package incidents to Oracle Support Services for Oracle ASM instances. This feature extends the benefit of Oracle Enterprise Manager Support Workbench to Oracle ASM by helping you package all necessary diagnostic data for incidents.
	For more information about using Oracle Enterprise Manager to administer Oracle ASM, see ["Oracle ASM Support Workbench"](asm_em.md).
	See Also:
	- [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/diag.htm#ADMIN12299) for information about viewing problems with Oracle Enterprise Manager Support Workbench
	- [Oracle Database 2 Day DBA](https://docs.oracle.com/cd/E11882_01/server.112/e10897/problems.htm#ADMQS12115) for information about accessing Oracle Enterprise Manager Support Workbench home page and viewing problems using Oracle Enterprise Manager Support Workbench

## Oracle Automatic Storage Management 11g Release 1 (11.1) New Features

This section describes the Oracle Automatic Storage Management (Oracle ASM) 11g release 1 (11.1) new features:

- This book is new for Oracle Database 11g release 1 (11.1) and it is the primary information source for Oracle Automatic Storage Management features.
- Oracle ASM Fast Mirror Resync
	Oracle ASM fast mirror resync quickly resynchronizes Oracle ASM disks within a disk group after transient disk path failures if the disk drive media is not corrupted. Any failures that render a failure group temporarily unavailable are considered transient failures. Disk path malfunctions, such as cable disconnections, host bus adapter or controller failures, or disk power supply interruptions, can cause transient failures.
	For more information about Oracle ASM fast mirror resync, see ["Oracle ASM Fast Mirror Resync"](asmdiskgrps.md).
- Oracle ASM Rolling Upgrade
	You can now place an Oracle ASM Cluster in rolling upgrade mode, which enables you to operate with mixed Oracle ASM versions starting with Oracle Database 11g release 1 (11.1) and later. Consequently, Oracle ASM nodes can be independently upgraded or patched without affecting database availability.
	For more information about Oracle ASM rolling upgrade, see ["Using Oracle ASM Rolling Upgrade"](asminst.md).
- New SYSASM Privilege and OSASM operating system group for Oracle ASM Administration
	This feature introduces a new SYSASM privilege that is specifically intended for performing Oracle ASM administration tasks. Using the SYSASM privilege instead of the SYSDBA privilege provides a clearer division of responsibility between Oracle ASM administration and database administration.
	OSASM is a new operating system group that is used exclusively for Oracle ASM. Members of the OSASM group can connect as `SYSASM` using operating system authentication and have full access to Oracle ASM.
	For more information about the SYSASM privilege, see ["Authentication for Accessing Oracle ASM Instances"](asminst.md).
- Oracle ASM Scalability and Performance Enhancements
	Oracle ASM file extent management has been enhanced to improve performance and to use significantly less system global area (SGA) memory to store file extents. When Oracle ASM files increase in size, the size of each new extent also increases automatically so that fewer extent pointers are required to describe the file. This feature improves performance when accessing Oracle ASM files that are 20 GB and larger, up to 128 TB. Very large databases (VLDBs) often require these large file sizes.
	For more information about scalability and performance enhancements, see ["Extents"](asmcon.md).
- Oracle ASM Command Line Utility (ASMCMD) Commands and Options
	ASMCMD has the following new commands: `lsdsk`, `md_backup`, `md_restore` and `remap`. In addition, you can use new options for the `ls` and `lsdg` commands.
	For more information about new and enhanced ASMCMD commands, ["Types of ASMCMD Commands"](asm_util001.md).
- Enhancements to SQL statements to manage Oracle ASM disk groups
	The `ALTER` `DISKGROUP`, `CREATE` `DISKGROUP`, and `DROP` `DISKGROUP` SQL statements have been enhanced with additional syntax options, including:
	- Syntax that sets various attributes of a disk group
		- Syntax for checking the consistency of disk groups, disks, and files in an Oracle ASM environment
		- Syntax options when mounting a disk group.
		- Syntax that takes a disk offline for repair and then brings it back online.
		- Syntax that drops a disk group that can no longer be mounted by an Oracle ASM instance.
	For more information about administering disk groups with the `ALTER` `DISKGROUP`, `CREATE` `DISKGROUP`, and `DROP` `DISKGROUP` SQL statements, see [Chapter 4, "Administering Oracle ASM Disk Groups"](asmdiskgrps.md).
	See Also:
	[Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_5008.htm#SQLRF01114) for information about the disk group attributes and the [`CREATE DISKGROUP`](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_5008.htm#SQLRF01114) SQL statement
- New Attributes for Disk Group Compatibility
	To enable the new Oracle ASM features, you can use two new disk group compatibility attributes, `COMPATIBLE.RDBMS` and `COMPATIBLE.ASM`. These attributes specify the minimum software version that is required to use disk groups for the database and for Oracle ASM respectively. This feature enables heterogeneous environments with disk groups from both Oracle Database 10g and Oracle Database 11g.
	For more information about disk group compatibility, see ["Disk Group Compatibility"](asmdiskgrps.md).
- Oracle ASM Preferred Read Failure Groups
	This feature is useful in extended clusters where remote nodes have asymmetric access with respect to performance. The feature enables more efficient use of network resources by eliminating the use of the network to perform read operations.
	Oracle ASM in Oracle Database 10g always reads the primary copy of a mirrored extent set. In Oracle Database 11g, when you configure Oracle ASM failure groups it might be more efficient for a node to read from a failure group that is closest to the node, even if it is a secondary extent. You can configure your database to read from a particular failure group extent by configuring preferred read failure groups.
	For more information about preferred read failure groups, see ["Preferred Read Failure Groups"](asmdiskgrps.md).
- Oracle ASM Fast Rebalance
	Rebalance operations that occur while a disk group is in `RESTRICTED` mode eliminate the lock and unlock extent map messaging between Oracle ASM instances in Oracle RAC environments, improving overall rebalance throughput.
	For more information about Oracle ASM fast rebalance, see ["About Restricted Mode"](asminst.md).