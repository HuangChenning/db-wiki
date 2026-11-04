---
title: "Administrator's Guide"
book: "Advanced Cluster File System Administrator's Guide"
doc_id: F30297-04
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/acfsg/intro-acfs-advm.html
tags:
  - oracle
  - 21c
  - advanced-cluster-file-system-administrators-guide
---

Oracle ASM Cluster File System (Oracle ACFS) and Oracle ASM Dynamic Volume Manager (Oracle ADVM) provide key components of storage management.

This chapter describes the components of Oracle Advanced Cluster File System (Oracle ACFS) and Oracle ASM Dynamic Volume Manager (Oracle ADVM).

This chapter provides concepts and an overview of Oracle ACFS and Oracle ADVM features with the following topics:

- Changes in Oracle ACFS and Oracle ADVM in Oracle Database 21c
- [Overview of Oracle ACFS](overview-acfs-advm.md)
- [Understanding Oracle ACFS Concepts](understand-acfs-concepts.md)
- [Understanding Oracle ACFS Administration](understand-acfs-admin.md)
- [Overview of Oracle ASM Dynamic Volume Manager](overview-advm.md)

See Also:

- [Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/acfsg&id=OSTMG-GUID-BC612D35-5399-4A35-843E-CF76E3D3CDB5) for information about Oracle Automatic Storage Management (Oracle ASM)
- [Oracle ACFS Features Enabled by Compatibility Attribute Settings](understand-acfs-admin.md) for information about Oracle ACFS features and disk group attribute settings
- [Managing Oracle ACFS and Oracle ADVM With ASMCA](manage-acfs-advm-asmca.md) for information about using Oracle ASM Configuration Assistant to administer Oracle ACFS
- [Managing Oracle ADVM with ASMCMD](manage-advm-asmcmd.md) for information about volume management commands
- [Managing Oracle ACFS with Command-Line Tools](manage-acfs-advm-commands.md) for information about Oracle ACFS operating system utilities
- [Using Views to Display Oracle ACFS Information](views-acfs-advm-info.md) for information about using views to obtain Oracle ACFS information
- [Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/acfsg&id=OSTMG-GUID-17B6982D-DC71-40D2-BB9B-A6C659DD187E) for information about the `ALTER` `DISKGROUP` `ADD` `VOLUME` SQL statement to administer volumes

### Changes in Oracle ACFS and Oracle ADVM in Oracle Database 21c

The following are changes to Oracle Advanced Cluster File System (Oracle ACFS) and Oracle ASM Dynamic Volume Manager (Oracle ADVM) in Oracle Database 21c.

- New Features
- Desupported Features

See Also:

- [Oracle Database Licensing Information User Manual](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/acfsg&id=DBLIC) to determine whether a feature is available on your edition of Oracle Database
- [Oracle Database New Features Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/acfsg&id=NEWFT) for a complete description of the new features in this release
- [Oracle Database Upgrade Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/acfsg&id=UPGRD) for a complete description of the deprecated and desupported features in this release

Note:

In Oracle Automatic Storage Management (Oracle ASM) 21c, information about Oracle ASM is documented in the [Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/acfsg&id=OSTMG-GUID-BC612D35-5399-4A35-843E-CF76E3D3CDB5).

New Features

These are new features for Oracle ACFS 21c.

- Oracle ACFS File Based Snapshots
	Oracle ACFS file based snapshots provides the ability to create snapshots of individual Oracle ACFS files in a space efficient manner on Linux.
	See Also:
	- [acfsutil fshare create](acfs-commands-utilities.md)
	- [About Oracle ACFS Snapshots](understand-acfs-concepts.md) for an overview of Oracle ACFS snapshots
- Oracle ACFS Replication Unplanned Failover
	Oracle ACFS replication failover provides unplanned failover where the standby location assumes the role of the primary in case of failure.
	See Also:
	- [acfsutil repl failover](acfs-commands-replication.md)
	- [Oracle ACFS Replication](understand-acfs-admin.md) for an overview of Oracle ACFS replication
- Oracle ACFS Automatic Shrinking
	Oracle ACFS automatic shrinking automatically shrinks an Oracle ACFS file system based on policy, providing there is enough free storage available in the volume.
	See Also:
	- [acfsutil size](acfs-commands-utilities.md)
- Oracle ACFS Mixed Sector Support
	Oracle ACFS mixed sector support enables the Linux primary and accelerator volumes of an Oracle ACFS file system to use a mix of different logical sector sizes, such as 512-bytes and 4096 bytes.
	See Also:
	- [mkfs](acfs-commands-linux.md) for information about creating an accelerator volume
	- [Oracle ACFS Accelerator Volume](understand-acfs-admin.md) for an overview of accelerator volumes

Desupported Features

These are desupported features for Oracle ACFS 21c.

- Desupport of Oracle ACFS Replication Version 1
	Starting with Oracle ACFS 21c, Oracle ACFS replication protocol version 1 is desupported. Replication protocol version 1 has been replaced with snapshot-based replication version 2, introduced in Oracle ACFS 12c Release 2 (12.2.0.1).
- Desupport of Oracle ACFS Encryption on Solaris and Windows
	Starting with Oracle ACFS 21c, Oracle ACFS encryption is desupported on Solaris and Microsoft Windows operating systems.
- Desupport of Oracle ACFS Security (Vault) and ACFS Auditing
	Starting with Oracle ACFS 21c, Oracle ACFS Security (Vault) and ACFS Auditing are desupported.
- Desupport of Oracle ACFS on Microsoft Windows
	Starting with Oracle ACFS 21c, Oracle ACFS is desupported on Windows.
- Desupport of Oracle ACFS Remote
	Starting with Oracle ACFS 21c, Oracle ACFS on Member Clusters (ACFS Remote) is desupported.
- Desupport of Cluster Domain - Member Clusters
	Starting with Oracle Grid Infrastructure 21c, Member Clusters, which are part of the Oracle Cluster Domain architecture, are desupported.