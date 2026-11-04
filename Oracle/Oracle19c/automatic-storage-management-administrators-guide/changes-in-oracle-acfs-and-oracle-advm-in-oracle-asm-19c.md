---
title: "Oracle Automatic Storage Management Administrator's Guide"
book: "Oracle Automatic Storage Management Administrator's Guide"
doc_id: F34287-08
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/ostmg/changes-in-this-release-for-oracle-automatic-storage-management-administrators-guide/changes-in-oracle-acfs-and-oracle-advm-in-oracle-asm-19c.html
tags:
  - oracle
  - 19c
  - automatic-storage-management-administrators-guide
---

## Changes in Oracle ACFS and Oracle ADVM in Oracle ASM 19c

The following are changes to Oracle Automatic Storage Management Cluster File System (Oracle ACFS) and Oracle ASM Dynamic Volume Manager (Oracle ADVM) in Oracle Automatic Storage Management release 19c.

## New Features

These are new features for Oracle ACFS 19c.

- Enhancements for Oracle ACFS `acfsutil` commands and views, providing more detailed output for diagnosis and analysis.
	Enhancements to Oracle ACFS `acfsutil` commands and views include:
	- Display open Oracle ACFS files at any given time using the `acfsutil` `info` `ftrace` command
		- Display lock contention statistics for cluster wide diagnostics using the `acfsutil` `lockstats` command
		- Perform a faster scan on relevant metadata only, rather than the entire collection, using the `acfsutil` `meta` command with the `-g` option
		- Display information for diagnosing Oracle ACFS metadata using the `acfsutil` `info` `file` command with the `-m` option
		- Shrinking an Oracle ACFS file system is supported in AIX environments using the `acfsutil` `size` command
		- Updated Oracle ACFS views ( `V$ASM_FILESYSTEM`, `V$ASM_ACFSSNAPSHOTS`, `V$ASM_ACFSAUTORESIZE` ) reflect content from prior releases
- Support for running the Oracle ACFS `fsck` command online (Linux)
	You can conduct an online analysis of the file system without any forced downtime and can perform checks of the Oracle ACFS file system without requiring a dismount of the file system (unmount). Running `fsck` online is supported only on Linux.
	See also
	- [Oracle ACFS Command-Line Tools for Linux Environments](managing-oracle-acfs-with-command-line-tools.md)
- Oracle ACFS Replication Improvements
	Oracle ACFS replication improvements enable more flexibility and capabilities for replication commands. These improvements include:
	- Oracle ACFS `acfsutil` `repl` commands, except `acfsutil` `repl` `info` `-c` `-u`, can now be invoked as an Oracle ASM user that is not root.
		- Oracle ACFS `acfsutil` `repl` `terminate` `standby` now has remote terminate capabilities with a new `remote` keyword to the standby termination command:
		`acfsutil` `repl` `terminate` `standby` `remote` *standby-location*
		The new `remote` keyword causes the standby to terminate replication processing on the primary location before terminating replication on the standby location.

## Deprecated Features

These are the deprecated features for Oracle ACFS 19c.

- Deprecation of Oracle ACFS Replication Version 1
	Starting with Oracle ACFS 19c (19.3), Oracle ACFS replication protocol version 1 is deprecated. Replication protocol version 1 has been replaced with snapshot-based replication version 2, introduced in Oracle ACFS 12c Release 2 (12.2.0.1).
	See also
	- [Oracle ACFS Replication](introducing-oracle-acfs-and-oracle-advm.md) for an overview of Oracle ACFS snapshot-based replication
	- [Configuring Oracle ACFS Snapshot-Based Replication](configuring-oracle-acfs-snapshot-based-replication.md) for information about converting an existing Oracle ACFS replication protocol version 1 environment to snapshot-based replication
- Deprecation of Oracle ACFS Encryption on Solaris and Windows
	Starting with Oracle ACFS 19c (19.3), Oracle ACFS encryption is deprecated on Solaris and Microsoft Windows operating systems.
	Oracle ACFS Encryption on Oracle Solaris and Microsoft Windows is based on RSA technology. Retirement of RSA technology has been announced. Oracle ACFS Encryption continues to be supported on Linux, and is unaffected by this deprecation, because Linux uses an alternative technology.
- Deprecation of Oracle ACFS on Windows
	Starting with Oracle ACFS 19c (19.5), Oracle ACFS is deprecated on Microsoft Windows.
	Deprecating certain clustering features with limited adoption allows Oracle to focus on improving core scaling, availability, and manageability across all features and functionality. Oracle ACFS file systems on Microsoft Windows are deprecated, and can be desupported in a future release. Depending on the use case, to replace current Oracle ACFS file systems, Oracle recommends that you move to Oracle Automatic Storage Management (Oracle ASM), Oracle Database File System (DBFS), or Microsoft Windows shares.
- Deprecation of Oracle ACFS Security (Vault) and Oracle ACFS Auditing
	Starting with Oracle ACFS 19c (19.5), Oracle ACFS Security (Vault) and ACFS Auditing are deprecated.
	Deprecating certain clustering features with limited adoption enables Oracle to focus on improving core scaling, availability, and manageability across all features and functionality. Oracle ACFS Security (Vault) and Oracle ACFS Auditing are deprecated, and can be desupported in a future release.
- Deprecation of Oracle ACFS on Member Clusters (ACFS Remote)
	Starting with Oracle ACFS 19c (19.5), Oracle ACFS on Member Clusters (ACFS Remote) is deprecated.
	Oracle Oracle ACFS on Member Clusters (ACFS Remote) is deprecated, and can be removed in a future release. Deprecating certain clustering features with limited adoption enables Oracle to focus on improving core scaling, availability, and manageability across all features and functionality.
- Deprecation of Cluster Domain - Member Clusters
	Starting with Oracle Grid Infrastructure 19c (19.5), Member Clusters, which are part of the Oracle Cluster Domain architecture, are deprecated.
	Oracle Member Clusters are deprecated, and can be desupported in a future release. Deprecating certain clustering features with limited adoption allows Oracle to focus on improving core scaling, availability, and manageability across all features and functionality. Oracle Cluster Domains consist of a Domain Services Cluster (DSC) and Member Clusters. The deprecation of Member Clusters affects the clustering used with the DSC, but not its ability to host services for other production clusters. Oracle recommends that customers align their next software or hardware upgrade with the transition off Cluster Domain - Member Clusters.