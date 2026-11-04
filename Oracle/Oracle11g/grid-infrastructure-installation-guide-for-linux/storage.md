---
title: Configuring Storage for Oracle Grid Infrastructure for a Cluster and Oracle RAC
book: Grid Infrastructure Installation Guide for Linux
doc_id: E41961-10
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/install.112/e41961/storage.htm
tags:
  - oracle
  - 11g
  - grid-infrastructure-installation-guide-for-linux
---

## 3 Configuring Storage for Oracle Grid Infrastructure for a Cluster and Oracle RAC

This chapter describes the storage configuration tasks that you must complete before you start the installer to install Oracle Clusterware and Oracle Automatic Storage Management (Oracle ASM), and that you must complete before adding an Oracle Real Application Clusters (Oracle RAC) installation to the cluster.

This chapter contains the following topics:

## 3.1 Reviewing Oracle Grid Infrastructure Storage Options

This section describes supported options for storing Oracle Grid Infrastructure for a cluster storage options. It contains the following sections:

- Overview of Oracle Clusterware and Oracle RAC Storage Options
- Oracle ACFS and Oracle ADVM Support
- General Information About Oracle ACFS
- General Storage Considerations for Oracle Grid Infrastructure and Oracle RAC
- Guidelines for Using Oracle ASM Disk Groups for Storage
- Using Logical Volume Managers with Oracle Grid Infrastructure and Oracle RAC
- Supported Storage Options
- After You Have Selected Disk Storage Options

See Also:

The Oracle Certification site on My Oracle Support for the most current information about certified storage options:
```
https://support.oracle.com
```

### 3.1.1 Overview of Oracle Clusterware and Oracle RAC Storage Options

There are two ways of storing Oracle Clusterware files:

- Oracle Automatic Storage Management (Oracle ASM): You can install Oracle Clusterware files (Oracle Cluster Registry and voting disk files) in Oracle ASM disk groups.
	Oracle ASM is the required database storage option for Typical installations, and for Standard Edition Oracle RAC installations. It is an integrated, high-performance database file system and disk manager for Oracle Clusterware and Oracle Database files. It performs striping and mirroring of database files automatically.
- A supported shared file system: Supported file systems include the following:
	- Network File System (NFS): Note that if you intend to use NFS for your data files, then you should create partitions large enough for the database files when you create partitions for Oracle Grid Infrastructure. NFS mounts differ for software binaries, Oracle Clusterware files, and database files.
		Note:
		Placing Oracle Grid Infrastructure for a cluster binaries on a cluster file system is not supported.
		You can no longer use OUI to install Oracle Clusterware or Oracle Database files on block or raw devices.
		See Also:
		My Oracle Support for supported file systems and NFS or NAS filers

### 3.1.2 Oracle ACFS and Oracle ADVM Support

Oracle Automatic Storage Management Cluster File System (Oracle ACFS) extends Oracle ASM technology to support of all of your application data in both single instance and cluster configurations. Oracle Automatic Storage Management Dynamic Volume Manager (Oracle ADVM) provides volume management services and a standard disk device driver interface to clients. Oracle Automatic Storage Management Cluster File System is layered on Oracle ASM through the Oracle Automatic Storage Management Dynamic Volume Manager interface.

Oracle ACFS and Oracle ADVM are supported on Oracle Linux 5 and Red Hat Enterprise Linux 5 for Linux x86 and Linux x86-64. Table 3-1 lists the releases, platforms and kernel versions that support Oracle ACFS and Oracle ADVM.

Table 3-1 Platforms that Support Oracle ACFS and Oracle ADVM

| Release | Platform/Operating system |  |
| --- | --- | --- |
| 11.2.x | Linux x86: Oracle Linux 5 and Red Hat Enterprise Linux 5 | 2.6.18, and later updates to 2.6.18 |
| 11.2.0.1 | Linux x86-64: Oracle Linux 5 and Red Hat Enterprise Linux 5 | 2.6.18, and later updates to 2.6.18 |
| 11.2.0.2 | Linux x86-64: Oracle Linux 5, Red Hat Enterprise Linux 5, SUSE Linux Enterprise Server 10 SP3 and later | 2.6.18, and later updates to 2.6.18 |
| 11.2.0.3 | Linux x86-64: Oracle Linux 5, Red Hat Enterprise Linux 5, SUSE Linux Enterprise Server 10 SP3 and later, SUSE Linux Enterprise Server 11 SP1 | 2.6.18, and later updates to 2.6.18  Oracle Unbreakable Enterprise Kernel 2.6.32-100.34.1 and later updates to 2.6.32-100 |
| 11.2.0.3 | Linux x86-64: Oracle Linux 6 (with Oracle Unbreakable Linux Kernel) | Oracle Unbreakable Enterprise kernel 2.6.32-100.34.1 and later updates to 2.6.32-100 |
| 11.2.0.3.3 (Oracle Grid Infrastructure PSU) | Linux x86-64: Red Hat Enterprise Linux 6, Oracle Linux with the Red Hat Compatible Kernel | 6.0, 6.1, 6.2 |
| 11.2.0.3.4 (Oracle Grid Infrastructure PSU) | Linux x86-64: Red Hat Enterprise Linux 6, Oracle Linux with the Red Hat Compatible Kernel | 6.3 and later |
| 11.2.0.3.7 (Oracle Grid Infrastructure PSU) | Linux x86-64: Oracle Linux 6 (with Oracle Unbreakable Enterprise Kernel), SUSE Linux Enterprise Server 11 SP2 | Oracle Unbreakable Enterprise Kernel 2.6.39-100 and later updates to 2.6.39-100 |
| 11.2.0.4 | Linux x86-64: SUSE Linux Enterprise Server 11 SP3 |  |

See Also:

- For current information on platforms and releases that support Oracle ACFS and Oracle ADVM refer to My Oracle Support Note 1369107.1:
	`https://support.oracle.com/CSP/main/article?cmd=show&type=NOT&id=1369107.1`
- For current Patch Set Update (PSU) release and support information refer to the PSU document on My Oracle Support.

Note:

Deployment of Security Enhanced Linux (SELinux) is not supported on Oracle ACFS file systems.

### 3.1.3 General Information About Oracle ACFS

Oracle Automatic Storage Management Cluster File System (Oracle ACFS) provides a general purpose file system. You can place Oracle Database binaries on this system, but you cannot place Oracle data files or Oracle Clusterware files on Oracle ACFS.

Note the following about Oracle ACFS:

- Oracle Restart does not support root-based Oracle Clusterware resources. For this reason, the following restrictions apply if you run Oracle ACFS on an Oracle Restart Configuration
	- You must manually load and unload Oracle ACFS drivers.
		- You must manually mount and unmount Oracle ACFS file systems, after the Oracle ASM instance is running
		- You can place Oracle ACFS database home file systems into the Oracle ACFS mount registry, along with other registered Oracle ACFS file systems.
- You cannot put Oracle Clusterware binaries and files on Oracle ACFS.
- You cannot put Oracle Database files on Oracle ACFS.
- You can put Oracle Database binaries and administrative files (for example, trace files) on Oracle ACFS.
- Oracle ACFS provides a general purpose file system for other files.

### 3.1.4 General Storage Considerations for Oracle Grid Infrastructure and Oracle RAC

For all installations, you must choose the storage option to use for Oracle Grid Infrastructure (Oracle Clusterware and Oracle ASM), and Oracle Real Application Clusters (Oracle RAC) databases. To enable automated backups during the installation, you must also choose the storage option to use for recovery files (the Fast Recovery Area). You do not have to use the same storage option for each file type.

#### 3.1.4.1 General Storage Considerations for Oracle Clusterware

Oracle Clusterware voting disks are used to monitor cluster node status, and Oracle Cluster Registry (OCR) files contain configuration information about the cluster. You can place voting disks and OCR files either in an Oracle ASM disk group, or on a cluster file system or shared network file system. Storage must be shared; any node that does not have access to an absolute majority of voting disks (more than half) will be restarted.

#### 3.1.4.2 General Storage Considerations for Oracle RAC

Use the following guidelines when choosing the storage options to use for each file type:

- You can choose any combination of the supported storage options for each file type provided that you satisfy all requirements listed for the chosen storage options.
- If you plan to install an Oracle RAC home on a shared OCFS2 location, then you must upgrade OCFS2 to at least version 1.4.1, which supports shared writable mmaps.
- Oracle recommends that you choose Oracle ASM as the storage option for database and recovery files.
- For Standard Edition Oracle RAC installations, Oracle ASM is the only supported storage option for database or recovery files.
- If you intend to use Oracle ASM with Oracle RAC, and you are configuring a new Oracle ASM instance, then your system must meet the following conditions:
	- All nodes on the cluster have Oracle Clusterware and Oracle ASM 11g release 2 (11.2) installed as part of an Oracle Grid Infrastructure for a cluster installation.
		- Any existing Oracle ASM instance on any node in the cluster is shut down.
- Raw or block devices are supported only when upgrading an existing installation using the partitions already configured. On new installations, using raw or block device partitions is not supported by Oracle Automatic Storage Management Configuration Assistant (ASMCA) or Oracle Universal Installer (OUI), but is supported by the software if you perform manual configuration.
	See Also:
	[Oracle Database Upgrade Guide](https://docs.oracle.com/cd/E11882_01/server.112/e23633/toc.htm) for information about how to prepare for upgrading an existing database
- If you do not have a storage option that provides external file redundancy, then you must configure at least three voting disk areas to provide voting disk redundancy.

### 3.1.5 Guidelines for Using Oracle ASM Disk Groups for Storage

During Oracle Grid Infrastructure installation, you can create one disk group. After the Oracle Grid Infrastructure installation, you can create additional disk groups using ASMCA, SQL\*Plus, or ASMCMD. Note that with Oracle Database 11g release 2 (11.2) and later releases, Oracle Database Configuration Assistant (DBCA) does not have the functionality to create disk groups for Oracle ASM.

If you install Oracle Database or Oracle RAC after you install Oracle Grid Infrastructure, then you can either use the same disk group for database files, OCR, and voting disk files, or you can use different disk groups. If you create multiple disk groups before installing Oracle RAC or before creating a database, then you can decide to do one of the following:

- Place the data files in the same disk group as the Oracle Clusterware files.
- Use the same Oracle ASM disk group for data files and recovery files.
- Use different disk groups for each file type.

If you create only one disk group for storage, then the OCR and voting disk files, database files, and recovery files are contained in the one disk group. If you create multiple disk groups for storage, then you can choose to place files in different disk groups.

Note:

The Oracle ASM instance that manages the existing disk group should be running in the Grid home.

See Also:

[Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e18951/toc.htm) for information about creating disk groups

### 3.1.6 Using Logical Volume Managers with Oracle Grid Infrastructure and Oracle RAC

Oracle Grid Infrastructure and Oracle RAC only support cluster-aware volume managers. This means, the volume manager that you want to use comes with a certain vendor cluster solution. To confirm that a volume manager you want to use is supported, look under the Certifications tab on My Oracle Support whether the associated cluster solution is certified for Oracle RAC. My Oracle Support is available at the following URL:

```
https://support.oracle.com
```

### 3.1.7 Supported Storage Options

The following table shows the storage options supported for storing Oracle Clusterware and Oracle RAC files.

Note:

For information about OCFS2, refer to the following Web site:
```
http://oss.oracle.com/projects/ocfs2/
```

If you plan to install an Oracle RAC home on a shared OCFS2 location, then you must upgrade OCFS2 to at least version 1.4.1, which supports shared writable `mmaps`.

For OCFS2 certification status, and for other cluster file system support, refer to the Certify page on My Oracle Support.

Table 3-2 Supported Storage Options for Oracle Clusterware and Oracle RAC

| Storage Option | OCR and Voting Disk Files | Oracle Clusterware binaries | Oracle RAC binaries | Oracle Database Files | Oracle Recovery Files |
| --- | --- | --- | --- | --- | --- |
| Oracle Automatic Storage Management (Oracle ASM)  Note: Loopback devices are not supported for use with Oracle ASM | Yes | No | No | Yes | Yes |
| Oracle Automatic Storage Management Cluster File System (Oracle ACFS) | No | No | Yes | No | No |
| Local file system | No | Yes | Yes | No | No |
| NFS file system on a certified NAS filer  Note: Direct NFS Client does not support Oracle Clusterware files. | Yes | Yes | Yes | Yes | Yes |
| Shared disk partitions (block devices or raw devices) | Not supported by OUI or ASMCA, but supported by the software. They can be added or removed after installation. | No | No | Not supported by OUI or ASMCA, but supported by the software. They can be added or removed after installation. | No |

Use the following guidelines when choosing storage options:

- You can choose any combination of the supported storage options for each file type provided that you satisfy all requirements listed for the chosen storage options.
- You can use Oracle ASM 11g release 2 (11.2) and later to store Oracle Clusterware files. You cannot use prior Oracle ASM releases to do this.
- If you do not have a storage option that provides external file redundancy, then you must configure at least three voting disk locations and at least three Oracle Cluster Registry locations to provide redundancy.

### 3.1.8 After You Have Selected Disk Storage Options

When you have determined your disk storage options, configure shared storage:

- To use a file system, refer to Shared File System Storage Configuration.
- To use Oracle Automatic Storage Management, refer to "Using Disk Groups with Oracle Database Files on Oracle ASM"

## 3.2 Shared File System Storage Configuration

The installer does not suggest a default location for the Oracle Cluster Registry (OCR) or the Oracle Clusterware voting disk. If you choose to create these files on a file system, then review the following sections to complete storage requirements for Oracle Clusterware files:

- Requirements for Using a Shared File System
- Deciding to Use a Cluster File System for Oracle Clusterware Files
- Deciding to Use Direct NFS Client for Data Files
- Deciding to Use NFS for Data Files
- Configuring Storage NFS Mount and Buffer Size Parameters
- Checking NFS Mount and Buffer Size Parameters for Oracle Clusterware
- Checking NFS Mount and Buffer Size Parameters for Oracle RAC
- Enabling Direct NFS Client Oracle Disk Manager Control of NFS
- Enabling Hybrid Columnar Compression on Direct NFS Client
- Creating Directories for Oracle Clusterware Files on Shared File Systems
- Creating Directories for Oracle Database Files on Shared File Systems
- Disabling Direct NFS Client Oracle Disk Management Control of NFS

Note:

The OCR is a file that contains the configuration information and status of the cluster. The installer automatically initializes the OCR during the Oracle Clusterware installation. Database Configuration Assistant uses the OCR for storing the configurations for the cluster databases that it creates.

### 3.2.1 Requirements for Using a Shared File System

To use a shared file system for Oracle Clusterware, Oracle ASM, and Oracle RAC, the file system must comply with the following requirements:

- To use an NFS file system, it must be on a supported NAS device. Log in to My Oracle Support at the following URL, and click the Certification tab to find the most current information about supported NAS devices:
	`https://support.oracle.com`
- If you choose to place your Oracle Cluster Registry (OCR) files on a shared file system, then Oracle recommends that one of the following is true:
	- The disks used for the file system are on a highly available storage device, (for example, a RAID device).
		- At least two file systems are mounted, and use the features of Oracle Clusterware 11g release 2 (11.2) to provide redundancy for the OCR.
- If you choose to place your database files on a shared file system, then one of the following should be true:
	- The disks used for the file system are on a highly available storage device, (for example, a RAID device).
		- The file systems consist of at least two independent file systems, with the database files on one file system, and the recovery files on a different file system.
- The user account with which you perform the installation (`oracle` or `grid`) must have write permissions to create the files in the path that you specify.

Note:

Upgrading from Oracle9i release 2 using the raw device or shared file for the OCR that you used for the SRVM configuration repository is not supported.

If you are upgrading Oracle Clusterware, and your existing cluster uses 100 MB OCR and 20 MB voting disk partitions, then you must extend these partitions to at least 300 MB. Oracle recommends that you do not use partitions, but instead place OCR and voting disks in disk groups marked as QUORUM disk groups.

All storage products must be supported by both your server and storage vendors.

Use Table 3-3 and Table 3-4 to determine the minimum size for shared file systems:

Table 3-3 Oracle Clusterware Shared File System Volume Size Requirements

| File Types Stored | Number of Volumes | Volume Size |
| --- | --- | --- |
| Voting disks with external redundancy | 3 | At least 300 MB for each voting disk volume. |
| Oracle Cluster Registry (OCR) with external redundancy | 1 | At least 300 MB for each OCR volume |
| Oracle Clusterware files (OCR and voting disks) with redundancy provided by Oracle software. | 1 | At least 300 MB for each OCR volume  At least 300 MB for each voting disk volume |

Table 3-4 Oracle RAC Shared File System Volume Size Requirements

| File Types Stored | Number of Volumes | Volume Size |
| --- | --- | --- |
| Oracle Database files | 1 | At least 1.5 GB for each volume |
| Recovery files  Note: Recovery files must be on a different volume than database files | 1 | At least 2 GB for each volume |

In Table 3-3 and Table 3-4, the total required volume size is cumulative. For example, to store all Oracle Clusterware files on the shared file system with normal redundancy, you should have at least 2 GB of storage available over a minimum of three volumes (three separate volume locations for the OCR and two OCR mirrors, and one voting disk on each volume). You should have a minimum of three physical disks, each at least 500 MB, to ensure that voting disks and OCR files are on separate physical disks. If you add Oracle RAC using one volume for database files and one volume for recovery files, then you should have at least 3.5 GB available storage over two volumes, and at least 5.5 GB available total for all volumes.

Note:

If you create partitions on shared partitions with `fdisk` by specifying a device size, such as `+300M`, the actual device created may be smaller than the size requested, based on the cylinder geometry of the disk. This is due to current fdisk restrictions. Oracle recommends that you partition the entire disk that you allocate for use by Oracle ASM.

### 3.2.2 Deciding to Use a Cluster File System for Oracle Clusterware Files

For new installations, Oracle recommends that you use Oracle Automatic Storage Management (Oracle ASM) to store voting disk and OCR files. For Linux x86 (32-bit) and x86-64 (64-bit) platforms, Oracle provides a cluster file system, OCFS2. However, Oracle does not recommend using OCFS2 for Oracle Clusterware files.

### 3.2.3 Deciding to Use Direct NFS Client for Data Files

Direct NFS Client is an alternative to using kernel-managed NFS. This section contains the following information about Direct NFS Client:

- About Direct NFS Client Storage
- Using the oranfstab File with Direct NFS Client
- Mounting NFS Storage Devices with Direct NFS Client
- Specifying Network Paths with the oranfstab File

#### 3.2.3.1 About Direct NFS Client Storage

With Oracle Database 11g release 2 (11.2), instead of using the operating system kernel NFS client, you can configure Oracle Database to access NFS V3 servers directly using an Oracle internal Direct NFS Client.

To enable Oracle Database to use Direct NFS Client, the NFS file systems must be mounted and available over regular NFS mounts before you start installation. Direct NFS Client manages settings after installation. You should still set the kernel mount options as a backup, but for normal operation, Direct NFS Client will manage NFS mounts.

Refer to your vendor documentation to complete NFS configuration and mounting.

Some NFS file servers require NFS clients to connect using reserved ports. If your filer is running with reserved port checking, then you must disable it for Direct NFS Client to operate. To disable reserved port checking, consult your NFS file server documentation.

For NFS servers that restrict port range, you can use the `insecure` option to enable clients other than `root` to connect to the NFS server. Alternatively, you can disable Direct NFS Client as described in Section 3.2.12, "Disabling Direct NFS Client Oracle Disk Management Control of NFS".

Note:

Use NFS servers supported for Oracle RAC. Refer to the following URL for support information:

`https://support.oracle.com`

#### 3.2.3.2 Using the oranfstab File with Direct NFS Client

If you use Direct NFS Client, then you can choose to use a new file specific for Oracle data file management, `oranfstab`, to specify additional options specific for Oracle Database to Direct NFS Client. For example, you can use `oranfstab` to specify additional paths for a mount point. You can add the `oranfstab` file either to `/etc` or to `$ORACLE_HOME/dbs`.

With shared Oracle homes, when the `oranfstab` file is placed in `$ORACLE_HOME/dbs`, the entries in the file are specific to a single database. In this case, all nodes running an Oracle RAC database use the same `$ORACLE_HOME/dbs/oranfstab` file. In non-shared Oracle RAC installs, `oranfstab` must be replicated on all nodes.

When the `oranfstab` file is placed in `/etc`, then it is globally available to all Oracle databases, and can contain mount points used by all Oracle databases running on nodes in the cluster, including standalone databases. However, on Oracle RAC systems, if the `oranfstab` file is placed in `/etc`, then you must replicate the file `/etc/oranfstab` file on all nodes, and keep each `/etc/oranfstab` file synchronized on all nodes, just as you must with the `/etc/fstab` file.

See Also:

Section 3.2.5, "Configuring Storage NFS Mount and Buffer Size Parameters" for information about configuring `/etc/fstab`

In all cases, mount points must be mounted by the kernel NFS system, even when they are being served using Direct NFS Client.

Caution:

Direct NFS Client will not serve an NFS server with write size values (`wtmax`) less than 32768.

#### 3.2.3.3 Mounting NFS Storage Devices with Direct NFS Client

Direct NFS Client determines mount point settings to NFS storage devices based on the configurations in `/etc/mtab`, which are changed with configuring the `/etc/fstab` file.

Direct NFS Client searches for mount entries in the following order:

1. `$ORACLE_HOME/dbs/oranfstab`
2. `/etc/oranfstab`
3. `/etc/mtab`

Direct NFS Client uses the first matching entry found.

Oracle Database is not shipped with Direct NFS Client enabled by default. To enable Direct NFS Client, complete the following steps:

1. Change the directory to `$ORACLE_HOME/rdbms/lib`.
2. Enter the following command:
	```
	make -f ins_rdbms.mk dnfs_on
	```

Note:

You can have only one active Direct NFS Client implementation for each instance. Using Direct NFS Client on an instance will prevent another Direct NFS Client implementation.

If Oracle Database uses Direct NFS Client mount points configured using `oranfstab`, then it first verifies kernel NFS mounts by cross-checking entries in `oranfstab` with operating system NFS mount points. If a mismatch exists, then Direct NFS logs an informational message, and does not operate.

If Oracle Database cannot open an NFS server using Direct NFS Client, then Oracle Database uses the platform operating system kernel NFS client. In this case, the kernel NFS mount options must be set up as defined in "Checking NFS Mount and Buffer Size Parameters for Oracle RAC". Additionally, an informational message is logged into the Oracle alert and trace files indicating that Direct NFS Client could not connect to an NFS server.

Section 3.1.7, "Supported Storage Options" lists the file types that are supported by Direct NFS.

The Oracle files resident on the NFS server that are served by the Direct NFS Client are also accessible through the operating system kernel NFS client.

See Also:

[Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/toc.htm) for guidelines to follow regarding managing Oracle database data files created with Direct NFS Client or kernel NFS

#### 3.2.3.4 Specifying Network Paths with the oranfstab File

Direct NFS Client can use up to four network paths defined in the `oranfstab` file for an NFS server. Direct NFS Client performs load balancing across all specified paths. If a specified path fails, then Direct NFS Client reissues I/O commands over any remaining paths.

Use the following SQL\*Plus views for managing Direct NFS Client in a cluster environment:

- gv$dnfs\_servers: Shows a table of servers accessed using Direct NFS Client.
- gv$dnfs\_files: Shows a table of files currently open using Direct NFS Client.
- gv$dnfs\_channels: Shows a table of open network paths (or channels) to servers for which Direct NFS Client is providing files.
- gv$dnfs\_stats: Shows a table of performance statistics for Direct NFS Client.

Note:

Use `v$` views for single instances, and `gv$` views for Oracle Clusterware and Oracle RAC storage.

### 3.2.4 Deciding to Use NFS for Data Files

Network-attached storage (NAS) systems use NFS to access data. You can store data files on a supported NFS system.

NFS file systems must be mounted and available over NFS mounts before you start installation. Refer to your vendor documentation to complete NFS configuration and mounting.

Be aware that the performance of Oracle software and databases stored on NAS devices depends on the performance of the network connection between the Oracle server and the NAS device.

For this reason, Oracle recommends that you connect the server to the NAS device using a private dedicated network connection, which should be Gigabit Ethernet or better.

### 3.2.5 Configuring Storage NFS Mount and Buffer Size Parameters

If you are using NFS for the Grid home or Oracle RAC home, then you must set up the NFS mounts on the storage so that they allow `root` on the clients mounting to the storage to be considered `root` instead of being mapped to an anonymous user, and allow `root` on the client server to create files on the NFS filesystem that are owned by `root`.

On NFS, you can obtain `root` access for clients writing to the storage by enabling `no_root_squash` on the server side. For example, to set up Oracle Clusterware file storage in the path `/vol/grid`, with nodes node1, node 2, and node3 in the domain `mycluster.example.com`, add a line similar to the following to the `/etc/exports` file:

```
/vol/grid/ node1.mycluster.example.com(rw,no_root_squash)
node2.mycluster.example.com(rw,no_root_squash) node3.mycluster.example.com
(rw,no_root_squash)
```

If the domain or DNS is secure so that no unauthorized system can obtain an IP address on it, then you can grant `root` access by domain, rather than specifying particular cluster member nodes:

For example:

```
/vol/grid/ *.mycluster.example.com(rw,no_root_squash)
```

Oracle recommends that you use a secure DNS or domain, and grant `root` access to cluster member nodes using the domain, as using this syntax allows you to add or remove nodes without the need to reconfigure the NFS server.

If you use Grid Naming Service (GNS), then the subdomain allocated for resolution by GNS within the cluster is a secure domain. Any server without a correctly signed Grid Plug and Play (GPnP) profile cannot join the cluster, so an unauthorized system cannot obtain or use names inside the GNS subdomain.

Caution:

Granting `root` access by domain can be used to obtain unauthorized access to systems. System administrators should refer to their operating system documentation for the risks associated with using `no_root_squash`.

After changing `/etc/exports`, reload the file system mount using the following command:

```
# /usr/sbin/exportfs -avr
```

### 3.2.6 Checking NFS Mount and Buffer Size Parameters for Oracle Clusterware

On the cluster member nodes, you must set the values for the NFS buffer size parameters `rsize` and `wsize` to 32768.

The NFS client-side mount options for binaries are:

```
rw,bg,hard,nointr,tcp,vers=3,timeo=600,rsize=32768,wsize=32768,actimeo=0
```

Note:

The `intr` and `nointr` mount options are deprecated with Oracle Linux re deprecated in Oracle Unbreakable Enterprise Linux and Oracle Linux kernels, 2.6.32 and later.

If you have Oracle Grid Infrastructure binaries on an NFS mount, then you must include the `suid` option.

The NFS client-side mount options for Oracle Clusterware files (OCR and voting disk files) are:

```
rw,bg,hard,nointr,rsize=32768,wsize=32768,tcp,noac,vers=3,timeo=600,actimeo=0
```

Update the `/etc/fstab` file on each node with an entry containing the NFS mount options for your platform. For example, if your platform is x86-64, and you are creating a mount point for Oracle Clusterware files, then update the `/etc/fstab` files with an entry similar to the following:

```
nfs_server:/vol/grid  /u02/oracle/cwfiles nfs \
rw,bg,hard,nointr,tcp,vers=3,timeo=600,actimeo=0,rsize=32768,wsize=32768 0 0
```

Note that mount point options are different for Oracle software binaries, Oracle Clusterware files (OCR and voting disks), and data files.

To create a mount point for binaries only, provide an entry similar to the following for a binaries mount point:

```
nfs_server:/vol/bin /u02/oracle/grid nfs \
rw,bg,hard,nointr,rsize=32768,wsize=32768,tcp,vers=3,timeo=600,actimeo=0,suid
```

See Also:

My Oracle Support bulletin 359515.1, "Mount Options for Oracle Files When Used with NAS Devices" for the most current information about mount options, available from the following URL:

`https://support.oracle.com`

Note:

Refer to your storage vendor documentation for additional information about mount options.

### 3.2.7 Checking NFS Mount and Buffer Size Parameters for Oracle RAC

If you use NFS mounts, then you must mount NFS volumes used for storing database files with special mount options on each node that has an Oracle RAC instance. When mounting an NFS file system, Oracle recommends that you use the same mount point options that your NAS vendor used when certifying the device. Refer to your device documentation or contact your vendor for information about recommended mount-point options.

Update the `/etc/fstab` file on each node with an entry similar to the following:

```
nfs_server:/vol/DATA/oradata  /u02/oradata     nfs\   
rw,bg,hard,nointr,tcp,vers=3,timeo=600,actimeo=0,rsize=32768,wsize=32768 0 0
```

The mandatory mount options comprise the minimum set of mount options that you must use while mounting the NFS volumes. These mount options are essential to protect the integrity of the data and to prevent any database corruption. Failure to use these mount options may result in the generation of file access errors. Refer to your operating system or NAS device documentation for more information about the specific options supported on your platform.

See Also:

My Oracle Support note 359515.1 for updated NAS mount option information, available at the following URL:
```
https://support.oracle.com
```

### 3.2.8 Enabling Direct NFS Client Oracle Disk Manager Control of NFS

Complete the following procedure to enable Direct NFS Client:

1. Create an `oranfstab` file with the following attributes for each NFS server to be accessed using Direct NFS Client:
	- Server: The NFS server name.
		- Local: Up to four paths on the database host, specified by IP address or by name, as displayed using the `ifconfig` command run on the database host.
		- Path: Up to four network paths to the NFS server, specified either by IP address, or by name, as displayed using the `ifconfig` command on the NFS server.
		- Export: The exported path from the NFS server.
		- Mount: The corresponding local mount point for the exported volume.
		- Mnt\_timeout: Specifies (in seconds) the time Direct NFS Client should wait for a successful mount before timing out. This parameter is optional. The default timeout is 10 minutes (`600`).
		- Dontroute: Specifies that outgoing messages should not be routed by the operating system, but instead sent using the IP address to which they are bound. Note that this POSIX option sometimes does not work on Linux systems with multiple paths in the same subnet.
		- management: Enables Direct NFS Client to use the management interface for SNMP queries. You can use this parameter if SNMP is running on separate management interfaces on the NFS server. The default value is the server parameter value.
		- community: Specifies the community string for use in SNMP queries. Default value is public.
	The examples that follow show three possible NFS server entries in `oranfstab`. A single `oranfstab` can have multiple NFS server entries.
	Example 3-1 Using Local and Path NFS Server Entries
	The following example uses both local and path. Since they are in different subnets, we do not have to specify `dontroute`.
	```
	server: MyDataServer1
	local: 192.0.2.0
	path: 192.0.2.1
	local: 192.0.100.0
	path: 192.0.100.1
	export: /vol/oradata1 mount: /mnt/oradata1
	community: private
	```
	Example 3-2 Using Local and Path in the Same Subnet, with dontroute
	The following example shows local and path in the same subnet. `dontroute` is specified in this case:
	```
	server: MyDataServer2
	local: 192.0.2.0
	path: 192.0.2.128
	local: 192.0.2.1
	path: 192.0.2.129
	dontroute
	export: /vol/oradata2 mount: /mnt/oradata2
	management: 192.0.10.128
	```
	Example 3-3 Using Names in Place of IP Addresses, with Multiple Exports
	```
	server: MyDataServer3
	local: LocalPath1
	path: NfsPath1
	local: LocalPath2
	path: NfsPath2
	local: LocalPath3
	path: NfsPath3
	local: LocalPath4
	path: NfsPath4
	dontroute
	export: /vol/oradata3 mount: /mnt/oradata3
	export: /vol/oradata4 mount: /mnt/oradata4
	export: /vol/oradata5 mount: /mnt/oradata5
	export: /vol/oradata6 mount: /mnt/oradata6
	```
2. By default, Direct NFS Client is installed in a disabled state. To enable Direct NFS Client, complete the following steps on each node. If you use a shared Grid home for the cluster, then complete the following steps in the shared Grid home:
	1. Log in as the Oracle Grid Infrastructure installation owner.
		2. Change directory to `Grid_home` `/rdbms/lib`.
		3. Enter the following commands:
		```
		$ make -f ins_rdbms.mk dnfs_on
		```

### 3.2.9 Enabling Hybrid Columnar Compression on Direct NFS Client

To enable Hybrid Columnar Compression (HCC) on Direct NFS Client, perform the following steps:

1. Ensure that SNMP is enabled on the ZFS Storage Server. For example:
	```
	$ snmpget -v1 -c public server_name .1.3.6.1.4.1.42.2.225.1.4.2.0
	SNMPv2-SMI::enterprises.42.2.225.1.4.2.0 = STRING: "Sun Storage 7410"
	```
2. If SNMP is enabled on an interface other than the NFS server, then configure `oranfstab` using the `management` parameter.
3. If SNMP is configured using a community string other than public, then configure `oranfstab` file using the community parameter.
4. Ensure that `libnetsnmp.so` is installed by checking if `snmpget` is available.

### 3.2.10 Creating Directories for Oracle Clusterware Files on Shared File Systems

Use the following instructions to create directories for Oracle Clusterware files. You can also configure shared file systems for the Oracle Database and recovery files.

Note:

For both NFS and OCFS2 storage, you must complete this procedure only if you want to place the Oracle Clusterware files on a separate file system from the Oracle base directory.

To create directories for the Oracle Clusterware files on separate file systems from the Oracle base directory, follow these steps:

1. If necessary, configure the shared file systems to use and mount them on each node.
	Note:
	The mount point that you use for the file system must be identical on each node. Ensure that the file systems are configured to mount automatically when a node restarts.
2. Use the `df` command to determine the free disk space on each mounted file system.
3. From the display, identify the file systems to use. Choose a file system with a minimum of 600 MB of free disk space (one OCR and one voting disk, with external redundancy).
	If you are using the same file system for multiple file types, then add the disk space requirements for each type to determine the total disk space requirement.
4. Note the names of the mount point directories for the file systems that you identified.
5. If the user performing installation (typically, `grid` or `oracle`) has permissions to create directories on the storage location where you plan to install Oracle Clusterware files, then OUI creates the Oracle Clusterware file directory.
	If the user performing installation does not have write access, then you must create these directories manually using commands similar to the following to create the recommended subdirectories in each of the mount point directories and set the appropriate owner, group, and permissions on the directory. For example, where the user is `oracle`, and the Oracle Clusterware file storage area is `cluster`:
	```
	# mkdir /mount_point/cluster
	# chown oracle:oinstall /mount_point/cluster
	# chmod 775 /mount_point/cluster
	```
	Note:
	After installation, directories in the installation path for the OCR files should be owned by `root`, and not writable by any account other than `root`.

When you have completed creating a subdirectory in the mount point directory, and set the appropriate owner, group, and permissions, you have completed OCFS2 or NFS configuration for Oracle Grid Infrastructure.

### 3.2.11 Creating Directories for Oracle Database Files on Shared File Systems

Use the following instructions to create directories for shared file systems for Oracle Database and recovery files (for example, for an Oracle RAC database).

1. If necessary, configure the shared file systems and mount them on each node.
	Note:
	The mount point that you use for the file system must be identical on each node. Ensure that the file systems are configured to mount automatically when a node restarts.
2. Use the `df -h` command to determine the free disk space on each mounted file system.
3. From the display, identify the file systems:
	| File Type | File System Requirements |
	| --- | --- |
	| Database files | Choose either: - A single file system with at least 1.5 GB of free disk space. - Two or more file systems with at least 1.5 GB of free disk space in total. |
	| Recovery files | Choose a file system with at least 2 GB of free disk space. |
	If you are using the same file system for multiple file types, then add the disk space requirements for each type to determine the total disk space requirement.
4. Note the names of the mount point directories for the file systems that you identified.
5. If the user performing installation (typically, `oracle`) has permissions to create directories on the disks where you plan to install Oracle Database, then DBCA creates the Oracle Database file directory, and the Recovery file directory.
	If the user performing installation does not have write access, then you must create these directories manually using commands similar to the following to create the recommended subdirectories in each of the mount point directories and set the appropriate owner, group, and permissions on them:
	- Database file directory:
		```
		# mkdir /mount_point/oradata
		# chown oracle:oinstall /mount_point/oradata
		# chmod 775 /mount_point/oradata
		```
	- Recovery file directory (Fast Recovery Area):
		```
		# mkdir /mount_point/recovery_area
		# chown oracle:oinstall /mount_point/recovery_area
		# chmod 775 /mount_point/recovery_area
		```

By making members of the `oinstall` group owners of these directories, this permits them to be read by multiple Oracle homes, including those with different OSDBA groups.

When you have completed creating subdirectories in each of the mount point directories, and set the appropriate owner, group, and permissions, you have completed OCFS2 or NFS configuration for Oracle Database shared storage.

### 3.2.12 Disabling Direct NFS Client Oracle Disk Management Control of NFS

Complete the following steps to disable the Direct NFS Client:

1. Log in as the Oracle Grid Infrastructure installation owner, and disable the Direct NFS Client using the following commands, where `Grid_home` is the path to the Oracle Grid Infrastructure home:
	```
	$ cd Grid_home/rdbms/lib
	$ make -f ins_rdbms.mk dnfs_off
	```
	Enter these commands on each node in the cluster, or on the shared Grid home if you are using a shared home for the Oracle Grid Infrastructure installation.
2. Remove the `oranfstab` file.

Note:

If you remove an NFS path that Oracle Database is using, then you must restart the database for the change to be effective.

## 3.3 Oracle Automatic Storage Management Storage Configuration

Review the following sections to configure storage for Oracle Automatic Storage Management:

- Configuring Storage for Oracle Automatic Storage Management
- Using Disk Groups with Oracle Database Files on Oracle ASM
- Configuring Oracle Automatic Storage Management Cluster File System
- Upgrading Existing Oracle ASM Instances

### 3.3.1 Configuring Storage for Oracle Automatic Storage Management

This section describes how to configure storage for use with Oracle Automatic Storage Management.

- Identifying Storage Requirements for Oracle Automatic Storage Management
- Creating Files on a NAS Device for Use with Oracle ASM
- Using an Existing Oracle ASM Disk Group
- Configuring Disks for Oracle ASM with ASMLIB
- Configuring ASMLIB for Multipath Disks
- Configuring Disk Devices Manually for Oracle ASM

#### 3.3.1.1 Identifying Storage Requirements for Oracle Automatic Storage Management

To identify the storage requirements for using Oracle ASM, you must determine how many devices and the amount of free disk space that you require. To complete this task, follow these steps:

1. Determine whether you want to use Oracle ASM for Oracle Clusterware files (OCR and voting disks), Oracle Database files, recovery files, or all files except for Oracle Clusterware or Oracle Database binaries. Oracle Database files include data files, control files, redo log files, the server parameter file, and the password file.
	Note:
	You do not have to use the same storage mechanism for Oracle Clusterware, Oracle Database files and recovery files. You can use a shared file system for one file type and Oracle ASM for the other.
	If you choose to enable automated backups and you do not have a shared file system available, then you must choose Oracle ASM for recovery file storage.
	If you enable automated backups during the installation, then you can select Oracle ASM as the storage mechanism for recovery files by specifying an Oracle Automatic Storage Management disk group for the Fast Recovery Area. If you select a noninteractive installation mode, then by default it creates one disk group and stores the OCR and voting disk files there. If you want to have any other disk groups for use in a subsequent database install, then you can choose interactive mode, or run ASMCA (or a command line tool) to create the appropriate disk groups before starting the database install.
2. Choose the Oracle ASM redundancy level to use for the Oracle ASM disk group.
	The redundancy level that you choose for the Oracle ASM disk group determines how Oracle ASM mirrors files in the disk group and determines the number of disks and amount of free disk space that you require, as follows:
	- External redundancy
		An external redundancy disk group requires a minimum of one disk device. The effective disk space in an external redundancy disk group is the sum of the disk space in all of its devices.
		For Oracle Clusterware files, External redundancy disk groups provide 1 voting disk file, and 1 OCR, with no copies. You must use an external technology to provide mirroring for high availability.
		Because Oracle ASM does not mirror data in an external redundancy disk group, Oracle recommends that you use external redundancy with storage devices such as RAID, or other similar devices that provide their own data protection mechanisms.
		- Normal redundancy
		In a normal redundancy disk group, to increase performance and reliability, Oracle ASM by default uses two-way mirroring. A normal redundancy disk group requires a minimum of two disk devices (or two failure groups). The effective disk space in a normal redundancy disk group is half the sum of the disk space in all of its devices.
		For Oracle Clusterware files, Normal redundancy disk groups provide 3 voting disk files, 1 OCR and 2 copies (one primary and one secondary mirror). With normal redundancy, the cluster can survive the loss of one failure group.
		For most installations, Oracle recommends that you select normal redundancy.
		- High redundancy
		In a high redundancy disk group, Oracle ASM uses three-way mirroring to increase performance and provide the highest level of reliability. A high redundancy disk group requires a minimum of three disk devices (or three failure groups). The effective disk space in a high redundancy disk group is one-third the sum of the disk space in all of its devices.
		For Oracle Clusterware files, High redundancy disk groups provide 5 voting disk files, 1 OCR and 3 copies (one primary and two secondary mirrors). With high redundancy, the cluster can survive the loss of two failure groups.
		While high redundancy disk groups do provide a high level of data protection, you should consider the greater cost of additional storage devices before deciding to select high redundancy disk groups.
3. Determine the total amount of disk space that you require for Oracle Clusterware files, and for the database files and recovery files.
	Use Table 3-5 and Table 3-6 to determine the minimum number of disks and the minimum disk space requirements for installing Oracle Clusterware files, and installing the starter database, where you have voting disks in a separate disk group:
	Table 3-5 Total Oracle Clusterware Storage Space Required by Redundancy Type
	| Redundancy Level | Minimum Number of Disks | Oracle Cluster Registry (OCR) Files | Voting Disk Files | Both File Types |
	| --- | --- | --- | --- | --- |
	| External | 1 | 300 MB | 300 MB | 600 MB |
	| Normal | 3 | 600 MB | 900 MB | 1.5 GB <sup>Foot 1</sup> |
	| High | 5 | 900 MB | 1.5 GB | 2.4 GB |
	<sup>Footnote 1</sup> If you create a disk group during installation, then it must be at least 2 GB.
	Note:
	If the voting disk files are in a disk group, be aware that disk groups with Oracle Clusterware files (OCR and voting disk files) have a higher minimum number of failure groups than other disk groups.
	If you create a disk group as part of the installation in order to install the OCR and voting disk files, then the installer requires that you create these files on a disk group with at least 2 GB of available space.
	A quorum failure group is a special type of failure group and disks in these failure groups do not contain user data. A quorum failure group is not considered when determining redundancy requirements in respect to storing user data. However, a quorum failure group counts when mounting a disk group.
	Table 3-6 Total Oracle Database Storage Space Required by Redundancy Type
	| Redundancy Level | Minimum Number of Disks | Database Files | Recovery Files | Both File Types |
	| --- | --- | --- | --- | --- |
	| External | 1 | 1.5 GB | 3 GB | 4.5 GB |
	| Normal | 2 | 3 GB | 6 GB | 9 GB |
	| High | 3 | 4.5 GB | 9 GB | 13.5 GB |
4. Determine an allocation unit size. Every Oracle ASM disk is divided into allocation units (AU). An allocation unit is the fundamental unit of allocation within a disk group. You can select the AU Size value from 1, 2, 4, 8, 16, 32 or 64 MB, depending on the specific disk group compatibility level. The default value is set to 1 MB.
5. For Oracle Clusterware installations, you must also add additional disk space for the Oracle ASM metadata. You can use the following formula to calculate the disk space requirements (in MB) for OCR and voting disk files, and the Oracle ASM metadata:
	total = \[2 \* ausize \* disks\] + \[redundancy \* (ausize \* (nodes \* (clients + 1) + 30) + (64 \* nodes) + 533)\]
	Where:
	- redundancy = Number of mirrors: external = 1, normal = 2, high = 3.
		- ausize = Metadata AU size in megabytes (default is 1 MB)
		- nodes = Number of nodes in cluster.
		- clients - Number of database instances for each node.
		- disks - Number of disks in disk group.
	For example, for a four-node Oracle RAC installation, using three disks in a normal redundancy disk group, you require an additional 1684 MB of space:
	\[2 \* 1 \* 3\] + \[2 \* (1 \* (4 \* (4 + 1)+ 30)+ (64 \* 4)+ 533)\] = 1684 MB
	To ensure high availability of Oracle Clusterware files on Oracle ASM, for a normal redundancy disk group, as a general rule for most installations, you must have at least 2 GB of disk space for Oracle Clusterware files in three separate failure groups, with at least three physical disks. To ensure that the effective disk space to create Oracle Clusterware files is 2 GB, best practice suggests that you ensure at least 2.1 GB of capacity for each disk, with a total capacity of at least 6.3 GB for three disks.
6. Optionally, identify failure groups for the Oracle ASM disk group devices.
	If you intend to use a normal or high redundancy disk group, then you can further protect your database against hardware failure by associating a set of disk devices in a custom failure group. By default, each device comprises its own failure group. However, if two disk devices in a normal redundancy disk group are attached to the same SCSI controller, then the disk group becomes unavailable if the controller fails. The controller in this example is a single point of failure.
	To protect against failures of this type, you could use two SCSI controllers, each with two disks, and define a failure group for the disks attached to each controller. This configuration would enable the disk group to tolerate the failure of one SCSI controller.
	Note:
	Define custom failure groups after installation, using the GUI tool ASMCA, the command line tool `asmcmd`, or SQL commands.
	If you define custom failure groups, then for failure groups containing database files only, you must specify a minimum of two failure groups for normal redundancy disk groups and three failure groups for high redundancy disk groups.
	For failure groups containing database files and clusterware files, including voting disks, you must specify a minimum of three failure groups for normal redundancy disk groups, and five failure groups for high redundancy disk groups.
	Disk groups containing voting files must have at least 3 failure groups for normal redundancy or at least 5 failure groups for high redundancy. Otherwise, the minimum is 2 and 3 respectively. The minimum number of failure groups applies whether or not they are custom failure groups.
7. If you are sure that a suitable disk group does not exist on the system, then install or identify appropriate disk devices to add to a new disk group. Use the following guidelines when identifying appropriate disk devices:
	- All of the devices in an Oracle ASM disk group should be the same size and have the same performance characteristics.
		- Do not specify multiple partitions on a single physical disk as a disk group device. Each disk group device should be on a separate physical disk.
		- Although you can specify a logical volume as a device in an Oracle ASM disk group, Oracle does not recommend their use because it adds a layer of complexity that is unnecessary with Oracle ASM. In addition, Oracle RAC requires a cluster logical volume manager in case you decide to use a logical volume with Oracle ASM and Oracle RAC.
		Oracle recommends that if you choose to use a logical volume manager, then use the logical volume manager to represent a single LUN without striping or mirroring, so that you can minimize the impact of the additional storage layer.

#### 3.3.1.2 Creating Files on a NAS Device for Use with Oracle ASM

If you have a certified NAS storage device, then you can create zero-padded files in an NFS mounted directory and use those files as disk devices in an Oracle ASM disk group.

To create these files, follow these steps:

1. If necessary, create an exported directory for the disk group files on the NAS device.
	Refer to the NAS device documentation for more information about completing this step.
2. Switch user to `root`.
3. Create a mount point directory on the local system. For example:
	```
	# mkdir -p /mnt/oracleasm
	```
4. To ensure that the NFS file system is mounted when the system restarts, add an entry for the file system in the mount file `/etc/fstab`.
	See Also:
	My Oracle Support note 359515.1 for updated NAS mount option information, available at the following URL:
	```
	https://support.oracle.com
	```
	For more information about editing the mount file for the operating system, refer to the `man` pages. For more information about recommended mount options, refer to the section "Checking NFS Mount and Buffer Size Parameters for Oracle RAC".
5. Enter a command similar to the following to mount the NFS file system on the local system:
	```
	# mount /mnt/oracleasm
	```
6. Choose a name for the disk group to create. For example: `sales1`.
7. Create a directory for the files on the NFS file system, using the disk group name as the directory name. For example:
	```
	# mkdir /mnt/oracleasm/nfsdg
	```
8. Use commands similar to the following to create the required number of zero-padded files in this directory:
	```
	# dd if=/dev/zero
	of=/mnt/oracleasm/nfsdg/disk1 bs=1024k 
	count=1000 oflag=direct
	```
	This example creates 1 GB files on the NFS file system. You must create one, two, or three files respectively to create an external, normal, or high redundancy disk group.
9. Enter commands similar to the following to change the owner, group, and permissions on the directory and files that you created, where the installation owner is `grid`, and the OSASM group is `asmadmin`:
	```
	# chown -R grid:asmadmin /mnt/oracleasm
	# chmod -R 660 /mnt/oracleasm
	```
10. If you plan to install Oracle RAC or a standalone Oracle Database, then during installation, edit the Oracle ASM disk discovery string to specify a regular expression that matches the file names you created. For example:
	```
	/mnt/oracleasm/sales1/
	```
	Note:
	During installation, disk paths mounted on Oracle ASM and registered on ASMLIB with the string ORCL:\* are listed as default database storage candidate disks.

#### 3.3.1.3 Using an Existing Oracle ASM Disk Group

Select from the following choices to store either database or recovery files in an existing Oracle ASM disk group, depending on installation method:

- If you select an installation method that runs Database Configuration Assistant in interactive mode, then you can decide whether you want to create a disk group, or to use an existing one.
	The same choice is available to you if you use Database Configuration Assistant after the installation to create a database.
- If you select an installation method that runs Database Configuration Assistant in noninteractive mode, then you must choose an existing disk group for the new database; you cannot create a disk group. However, you can add disk devices to an existing disk group if it has insufficient free space for your requirements.

Note:

The Oracle Automatic Storage Management instance that manages the existing disk group can be running in a different Oracle home directory.

To determine if an existing Oracle Automatic Storage Management disk group exists, or to determine if there is sufficient disk space in a disk group, you can use the Oracle ASM command line tool (`asmcmd`), Oracle Enterprise Manager Grid Control or Database Control. Alternatively, you can use the following procedure:

1. View the contents of the `oratab` file to determine if an Oracle Automatic Storage Management instance is configured on the system:
	```
	$ more /etc/oratab
	```
	If an Oracle Automatic Storage Management instance is configured on the system, then the `oratab` file should contain a line similar to the following:
	```
	+ASM2:oracle_home_path
	```
	In this example, `+ASM2` is the system identifier (SID) of the Oracle Automatic Storage Management instance, with the node number appended, and `oracle_home_path` is the Oracle home directory where it is installed. By convention, the SID for an Oracle Automatic Storage Management instance begins with a plus sign.
2. Set the `ORACLE_SID` and `ORACLE_HOME` environment variables to specify the appropriate values for the Oracle Automatic Storage Management instance.
3. Connect to the Oracle Automatic Storage Management instance and start the instance if necessary:
	```
	$ $ORACLE_HOME/bin/asmcmd
	ASMCMD> startup
	```
4. Enter one of the following commands to view the existing disk groups, their redundancy level, and the amount of free disk space in each one:
	```
	ASMCMD> lsdg
	```
	or:
	```
	$ORACLE_HOME/bin/asmcmd -p lsdg
	```
5. From the output, identify a disk group with the appropriate redundancy level and note the free space that it contains.
6. If necessary, install or identify the additional disk devices required to meet the storage requirements listed in the previous section.
	Note:
	If you are adding devices to an existing disk group, then Oracle recommends that you use devices that have the same size and performance characteristics as the existing devices in that disk group.

#### 3.3.1.4 Configuring Disks for Oracle ASM with ASMLIB

The Oracle Automatic Storage Management (Oracle ASM) library driver (ASMLIB) simplifies the configuration and management of the disk devices by eliminating the need to rebind disk devices used with Oracle ASM each time the system is restarted.

Without ASMLIB Linux 2.6 kernel and later, block device paths do not maintain permissions and path persistence unless you create a `permissions` or `rules` file on each cluster member node; block device paths that were `/dev/sda` can appear as `/dev/sdb` after a system restart. Adding new disks requires you to modify the `udev` file to provide permissions and path persistence for the new disk.

With ASMLIB, you define the range of disks you want to have made available as Oracle ASM disks. ASMLIB maintains permissions and disk labels that are persistent on the storage device, so that label is available even after an operating system upgrade. You can update storage paths on all cluster member nodes by running one `oracleasm` command on each node.

If you intend to use Oracle ASM on block devices for database storage for Linux, then Oracle recommends that you install the ASMLIB driver and associated utilities, and use them to configure the disks for Oracle ASM.

Caution:

On IBM: Linux on System z servers, due to a block size compatibility issue, you cannot use ASMLIB with SCSI storage devices and Fibre Channel Protocol (FCP) for Oracle Grid Infrastructure release 11.2.0.1 and later.

Workaround: use block device directly (for example, using paths similar to `/dev/mapper/mpatha_part1`), or use DASD disks.

See Also:

My Oracle Support notes How to Manually Configure Disk Storage devices for use with Oracle ASM 11.2 on IBM: Linux on System z under SLES (Doc ID 1350008.1) and How to Manually Configure Disk Storage devices for use with Oracle ASM 11.2 on IBM: Linux on System z under Red Hat 5 (Doc ID 1351746.1), available at the following URL:

`https://support.oracle.com`

To use the Oracle Automatic Storage Management library driver (ASMLIB) to configure Oracle ASM devices, complete the following tasks.

- Installing and Configuring the Oracle ASM Library Driver Software
- Configuring Disk Devices to Use Oracle ASM Library Driver on x86 Systems
- Configuring Disk Devices to Use ASM Library Driver on IBM: Linux on System z
- Administering the Oracle ASM Library Driver and Disks

Note:

To create a database during the installation using the Oracle ASM library driver, you must choose an installation method that runs ASMCA in interactive mode. You must also change the default disk discovery string to `ORCL:*.`

##### 3.3.1.4.1 Installing and Configuring the Oracle ASM Library Driver Software

ASMLIB is already included with Unbreakable Enterprise Kernel packages, and with SUSE 11. If you are a member of the Unbreakable Linux Network, then you can install the ASMLIB rpms by subscribing to the Oracle Software for Enterprise Linux channel, and using `up2date` to retrieve the most current package for your system and kernel. For additional information, refer to the following URL:

```
http://www.oracle.com/technetwork/topics/linux/asmlib/index-101839.html
```

To install and configure the ASMLIB driver software manually, follow these steps:

1. Enter the following command to determine the kernel version and architecture of the system:
	```
	# uname -rm
	```
2. Download the required ASMLIB packages from the Oracle Technology Network (OTN) Web site:
	```
	http://www.oracle.com/technetwork/server-storage/linux/downloads/index-088143.html
	```
	Note:
	You must install `oracleasm-support` package version 2.0.1 or later to use ASMLIB on Red Hat Enterprise Linux 5 Advanced Server. ASMLIB is already included with SUSE distributions.
	Tip:
	My Oracle Support note 1089399.1 for information about ASMLIB support with Red Hat distributions:
	`https://support.oracle.com/CSP/main/article?cmd=show&type=NOT&id=1089399.1`
	You must install the following packages, where `version` is the version of the ASMLIB driver, `arch` is the system architecture, and `kernel` is the version of the kernel that you are using:
	```
	oracleasm-support-version.arch.rpm
	oracleasm-kernel-version.arch.rpm
	oracleasmlib-version.arch.rpm
	```
3. Switch user to the `root` user:
	```
	$ su -
	```
4. Enter a command similar to the following to install the packages:
	```
	# rpm -ivh oracleasm-support-version.arch.rpm \
	           oracleasm-kernel-version.arch.rpm \
	           oracleasmlib-version.arch.rpm
	```
	For example, if you are using the Red Hat Enterprise Linux 5 AS kernel on an AMD64 system, then enter a command similar to the following:
	```
	# rpm -ivh oracleasm-support-2.1.3-1.el5.x86_64.rpm \
	     oracleasm-2.6.18-194.26.1.el5xen-2.0.5-1.el5.x86_64.rpm \
	     oracleasmlib-2.0.4-1.el5.x86_64.rpm
	```
5. Enter the following command to run the `oracleasm` initialization script with the `configure` option:
	```
	# /usr/sbin/oracleasm configure -i
	```
	Note:
	The `oracleasm` command in `/usr/sbin` is the command you should use. The `/etc/init.d` path is not deprecated, but the `oracleasm` binary in that path is now used typically for internal commands.
6. Enter the following information in response to the prompts that the script displays:
	| Prompt | Suggested Response |
	| --- | --- |
	| Default user to own the driver interface: | Standard groups and users configuration: Specify the Oracle software owner user (for example, `oracle`)  Job role separation groups and users configuration: Specify the Grid Infrastructure software owner (for example, `grid`) |
	| Default group to own the driver interface: | Standard groups and users configuration: Specify the OSDBA group for the database (for example, `dba`).  Job role separation groups and users configuration: Specify the OSASM group for storage administration (for example, `asmadmin`). |
	| Start Oracle ASM Library driver on boot (y/n): | Enter `y` to start the Oracle Automatic Storage Management library driver when the system starts. |
	| Scan for Oracle ASM disks on boot (y/n) | Enter `y` to scan for Oracle ASM disks when the system starts. |
	The script completes the following tasks:
	- Creates the `/etc/sysconfig/oracleasm` configuration file
		- Creates the `/dev/oracleasm` mount point
		- Mounts the ASMLIB driver file system
		Note:
		The ASMLIB driver file system is not a regular file system. It is used only by the Oracle ASM library to communicate with the Oracle ASM driver.
7. Enter the following command to load the `oracleasm` kernel module:
	```
	# /usr/sbin/oracleasm init
	```
8. Repeat this procedure on all nodes in the cluster where you want to install Oracle RAC.

##### 3.3.1.4.2 Configuring Disk Devices to Use Oracle ASM Library Driver on x86 Systems

To configure the disk devices to use in an Oracle ASM disk group, follow these steps:

1. If you intend to use IDE, SCSI, or RAID devices in the Oracle ASM disk group, then follow these steps:
	1. If necessary, install or configure the shared disk devices that you intend to use for the disk group and restart the system.
		2. To identify the device name for the disks to use, enter the following command:
		```
		# /sbin/fdisk -l
		```
		Depending on the type of disk, the device name can vary:
		| Disk Type | Device Name Format | Description |
		| --- | --- | --- |
		| IDE disk | ``` /dev/hdxn ``` | In this example, `x` is a letter that identifies the IDE disk and `n` is the partition number. For example, `/dev/hda` is the first disk on the first IDE bus. |
		| SCSI disk | ``` /dev/sdxn ``` | In this example, `x` is a letter that identifies the SCSI disk and `n` is the partition number. For example, `/dev/sda` is the first disk on the first SCSI bus. |
		| RAID disk | ``` /dev/rd/cxdypz /dev/ida/cxdypz ``` | Depending on the RAID controller, RAID devices can have different device names. In the examples shown, `x` is a number that identifies the controller, `y` is a number that identifies the disk, and `z` is a number that identifies the partition. For example, `/dev/ida/c0d1` is the second logical drive on the first controller. |
		To include devices in a disk group, you can specify either whole-drive device names or partition device names.
		Note:
		Oracle recommends that you create a single whole-disk partition on each disk.
		3. Use either `fdisk` or `parted` to create a single whole-disk partition on the disk devices.
2. Enter a command similar to the following to mark a disk as an Oracle ASM disk:
	```
	# /usr/sbin/oracleasm createdisk DISK1 /dev/sdb1
	```
	In this example, `DISK1` is the name you assign to the disk.
	Note:
	The disk names that you specify can contain uppercase letters, numbers, and the underscore character. They must start with an uppercase letter.
	If you are using a multi-pathing disk driver with Oracle ASM, then make sure that you specify the correct logical device name for the disk.
3. To make the disk available on the other nodes in the cluster, enter the following command as `root` on each node:
	```
	# /usr/sbin/oracleasm scandisks
	```
	This command identifies shared disks attached to the node that are marked as Oracle ASM disks.

##### 3.3.1.4.3 Configuring Disk Devices to Use ASM Library Driver on IBM: Linux on System z

1. If you formatted the DASD with the compatible disk layout, then enter a command similar to the following to create a single whole-disk partition on the device:
	```
	# /sbin/fdasd -a /dev/dasdxxxx
	```
2. Enter a command similar to the following to mark a disk as an ASM disk:
	```
	# /etc/init.d/oracleasm createdisk DISK1 /dev/dasdxxxx
	```
	In this example, `DISK1` is a name that you want to assign to the disk.
	Note:
	The disk names that you specify can contain uppercase letters, numbers, and the underscore character. They must start with an uppercase letter.
	If you are using a multi-pathing disk driver with ASM, then make sure that you specify the correct logical device name for the disk.
3. To make the disk available on the other cluster nodes, enter the following command as root on each node:
	```
	# /etc/init.d/oracleasm scandisks
	```
	This command identifies shared disks attached to the node that are marked as ASM disks.

##### 3.3.1.4.4 Administering the Oracle ASM Library Driver and Disks

To administer the Oracle Automatic Storage Management library driver (ASMLIB) and disks, use the `oracleasm` initialization script with different options, as described in Table 3-7.

Table 3-7 ORACLEASM Script Options

| Option | Description |
| --- | --- |
| ``` configure ``` | Use the `configure` option to reconfigure the Oracle Automatic Storage Management library driver, if necessary:  ``` # /usr/sbin/oracleasm configure -i ```  To see command options, enter `oracleasm configure` without the `-i` flag. |
| ``` enable disable ``` | Use the `disable` and `enable` options to change the actions of the Oracle Automatic Storage Management library driver when the system starts. The `enable` option causes the Oracle Automatic Storage Management library driver to load when the system starts:  ``` # /usr/sbin/oracleasm enable ``` |
| ``` start stop restart ``` | Use the `start`, `stop`, and `restart` options to load or unload the Oracle Automatic Storage Management library driver without restarting the system:  ``` # /usr/sbin/oracleasm restart ``` |
| ``` createdisk ``` | Use the `createdisk` option to mark a disk device for use with the Oracle Automatic Storage Management library driver and give it a name:  ``` # /usr/sbin/oracleasm createdisk DISKNAME devicename ``` |
| ``` deletedisk ``` | Use the `deletedisk` option to unmark a named disk device:  ``` # /usr/sbin/oracleasm deletedisk DISKNAME ```  Caution: Do not use this command to unmark disks that are being used by an Oracle Automatic Storage Management disk group. You must delete the disk from the Oracle Automatic Storage Management disk group before you unmark it. |
| ``` querydisk ``` | Use the `querydisk` option to determine if a disk device or disk name is being used by the Oracle Automatic Storage Management library driver:  ``` # /usr/sbin/oracleasm querydisk {DISKNAME \| devicename} ``` |
| ``` listdisks ``` | Use the `listdisks` option to list the disk names of marked Oracle Automatic Storage Management library driver disks:  ``` # /usr/sbin/oracleasm listdisks ``` |
| ``` scandisks ``` | Use the `scandisks` option to enable cluster nodes to identify which shared disks have been marked as Oracle Automatic Storage Management library driver disks on another node:  ``` # /usr/sbin/oracleasm scandisks ``` |

#### 3.3.1.5 Configuring ASMLIB for Multipath Disks

Additional configuration is required to use the Oracle Automatic Storage Management library Driver (ASMLIB) with third party vendor multipath disks.

See Also:

My Oracle Support site for updates to supported storage options:
```
https://support.oracle.com
```

##### 3.3.1.5.1 About Using Oracle ASM with Multipath Disks

Oracle ASM requires that each disk is uniquely identified. If the same disk appears under multiple paths, then it causes errors. In a multipath disk configuration, the same disk can appear three times:

1. The initial path to the disk
2. The second path to the disk
3. The multipath disk access point.

For example: If you have one local disk, `/dev/sda`, and one disk attached with external storage, then your server shows two connections, or paths, to that external storage. The Linux SCSI driver shows both paths. They appear as `/dev/sdb` and `/dev/sdc`. The system may access either `/dev/sdb` or `/dev/sdc`, but the access is to the same disk.

If you enable multipathing, then you have a multipath disk (for example, `/dev/multipatha`), which can access both `/dev/sdb` and `/dev sdc`; any I/O to `multipatha` can use either the `sdb` or `sdc` path. If a system is using the `/dev/sdb` path, and that cable is unplugged, then the system shows an error. But the multipath disk will switch from the `/dev/sdb` path to the `/dev/sdc` path.

Most system software is unaware of multipath configurations. They can use any paths (`sdb`, `sdc` or `multipatha`). ASMLIB also is unaware of multipath configurations.

By default, ASMLIB recognizes the first disk path that Linux reports to it, but because it imprints an identity on that disk, it recognizes that disk only under one path. Depending on your storage driver, it may recognize the multipath disk, or it may recognize one of the single disk paths.

Instead of relying on the default, you should configure Oracle ASM to recognize the multipath disk.

##### 3.3.1.5.2 Disk Scan Ordering

The ASMLIB configuration file is located in the path `/etc/sysconfig/oracleasm`. It contains all the startup configuration you specified with the command `/etc/init.d/oracleasm configure`. That command cannot configure scan ordering.

The configuration file contains many configuration variables. The `ORACLEASM_SCANORDER` variable specifies disks to be scanned first. The `ORACLEASM_SCANEXCLUDE` variable specifies the disks that are to be ignored.

Configure values for `ORACLEASM_SCANORDER` using space-delimited prefix strings. A prefix string is the common string associated with a type of disk. For example, if you use the prefix string `sd`, then this string matches all SCSI devices, including `/dev/sda`, `/dev/sdb`, `/dev/sdc` and so on. Note that these are not globs. They do not use wild cards. They are simple prefixes. Also note that the path is not a part of the prefix. For example, the `/dev/` path is not part of the prefix for SCSI disks that are in the path `/dev/sd` \*.

For Oracle Linux and Red Hat Enterprise Linux version 5, when scanning, the kernel sees the devices as `/dev/mapper/` `XXX` entries. By default, the 2.6 kernel device file naming scheme `udev` creates the `/dev/mapper/` `XXX` names for human readability. Any configuration using `ORACLEASM_SCANORDER` should use the `/dev/mapper/` `XXX` entries.

##### 3.3.1.5.3 Configuring Disk Scan Ordering to Select Multipath Disks

To configure ASMLIB to select multipath disks first, complete the following procedure:

1. Using a text editor, open the ASMLIB configuration file `/etc/sysconfig/oracleasm`.
2. Edit the ORACLEASM\_SCANORDER variable to provide the prefix path of the multipath disks. For example, if the multipath disks use the prefix `multipath` (`/dev/mapper/multipatha`, `/dev/mapper/multipathb` and so on), and the multipath disks mount SCSI disks, then provide a prefix path similar to the following:
	```
	ORACLEASM_SCANORDER="multipath sd"
	```
3. Save the file.

When you have completed this procedure, then when ASMLIB scans disks, it first scans all disks with the prefix string multipath, and labels these disks as Oracle ASM disks using the `/dev/mapper/multipath` `X` value. It then scans all disks with the prefix string `sd`. However, because ASMLIB recognizes that these disks have already been labeled with the `/dev/mapper/multipath` string values, it ignores these disks. After scanning for the prefix strings `multipath` and `sd`, Oracle ASM then scans for any other disks that do not match the scan order.

In the example in step 2, the key word multipath is actually the alias for multipath devices configured in `/etc/multipath.conf` under the `multipaths` section. For example:

```
multipaths {
       multipath {
               wwid                    3600508b4000156d700012000000b0000
               alias                   multipath
               ...
       }
       multipath {
               ...
               alias                   mympath
               ...
       }
       ...
}
```

The default device name is in the format /dev/mapper/mpath\* (or a similar path).

##### 3.3.1.5.4 Configuring Disk Order Scan to Exclude Single Path Disks

To configure ASMLIB to exclude particular single path disks, complete the following procedure:

1. Using a text editor, open the ASMLIB configuration file `/etc/sysconfig/oracleasm`.
2. Edit the `ORACLEASM_SCANEXCLUDE` variable to provide the prefix path of the single path disks. For example, if you want to exclude the single path disks `/dev sdb` and `/dev/sdc`, then provide a prefix path similar to the following:
	```
	ORACLEASM_SCANEXCLUDE="sdb sdc"
	```
3. Save the file.

When you have completed this procedure, then when ASMLIB scans disks, it scans all disks except for the disks with the `sdb` and `sdc` prefixes, so that it ignores `/dev/sdb` and `/dev/sdc`. It does not ignore other SCSI disks, nor multipath disks. If you have a multipath disk (for example, `/dev/multipatha`), which accesses both `/dev/sdb` and `/dev sdc`, but you have configured ASMLIB to ignore `sdb` and `sdc`, then ASMLIB ignores these disks and instead marks only the multipath disk as an Oracle ASM disk.

#### 3.3.1.6 Configuring Disk Devices Manually for Oracle ASM

By default, the 2.6 kernel device file naming scheme `udev` dynamically creates device file names when the server is started, and assigns ownership of them to `root`. If `udev` applies default settings, then it changes device file names and owners for voting disks or Oracle Cluster Registry partitions, corrupting them when the server is restarted. For example, a voting disk on a device named `/dev/sdd` owned by the user `grid` may be on a device named `/dev/sdf` owned by `root` after restarting the server.If you use ASMLIB, then you do not need to ensure permissions and device path persistency in `udev`.

If you do not use ASMLIB, then you must create a custom rules file. When `udev` is started, it sequentially carries out rules (configuration directives) defined in rules files. These files are in the path `/etc/udev/rules.d/`. Rules files are read in lexical order. For example, rules in the file `10-wacom.rules` are parsed and carried out before rules in the rules file `90-ib.rules`.

When specifying the device information in the UDEV rules file, ensure that the OWNER, GROUP and MODE are specified before any other characteristics in the order shown. For example, if you want to include the characteristic ACTION on the UDEV line, then specify ACTION after OWNER, GROUP, and MODE.

Where rules files describe the same devices, on the supported Linux kernel versions, the last file read is the one that is applied.

To configure a permissions file for disk devices, complete the following tasks:

1. To obtain information about existing block devices, run the command `scsi_id` (`/sbin/scsi_id`) on storage devices from one cluster node to obtain their unique device identifiers. When running the `scsi_id` command with the `-s` argument, the device path and name passed should be that relative to the `sysfs` directory `/sys` (for example, `/block/device`) when referring to `/sys/block/device`. For example:
	```
	# /sbin/scsi_id -g -s /block/sdb/sdb1
	360a98000686f6959684a453333524174
	 
	# /sbin/scsi_id -g -s /block/sde/sde1
	360a98000686f6959684a453333524179
	```
	Record the unique SCSI identifiers of clusterware devices, so you can provide them when required.
	Note:
	The command `scsi_id` should return the same device identifier value for a given device, regardless of which node the command is run from.
2. Configure SCSI devices as trusted devices (white listed), by editing the `/etc/scsi_id.config` file and adding `options=-g` to the file. For example:
	```
	# cat > /etc/scsi_id.config
	vendor="ATA",options=-p 0x80
	options=-g
	```
3. Using a text editor, create a UDEV rules file for the Oracle ASM devices, setting permissions to 0660 for the installation owner and the group whose members are administrators of the Oracle Grid Infrastructure software. For example, using the installation owner `grid` and using a role-based group configuration, with the OSASM group `asmadmin`:
	```
	# vi /etc/udev/rules.d/99-oracle-asmdevices.rules
	KERNEL=="sd?1", BUS=="scsi", PROGRAM=="/sbin/scsi_id",
	RESULT=="14f70656e66696c00000000", OWNER="grid", GROUP="asmadmin", MODE="0660"
	KERNEL=="sd?2", BUS=="scsi", PROGRAM=="/sbin/scsi_id",
	RESULT=="14f70656e66696c00000001", OWNER="grid", GROUP="asmadmin", MODE="0660"
	KERNEL=="sd?3", BUS=="scsi", PROGRAM=="/sbin/scsi_id",
	RESULT=="14f70656e66696c00000002", OWNER="grid", GROUP="asmadmin", MODE="0660"
	```
4. Copy the `rules.d` file to all other nodes on the cluster. For example:
	```
	# scp 99-oracle-asmdevices.rules root@node2:/etc/udev/rules.d/99-oracle-asmdevices.rules
	```
5. Load updated block device partition tables on all member nodes of the cluster, using `/sbin/partprobe` `devicename`. You must do this as `root`.
6. Run the command `udevtest` (`/sbin/udevtest`) to test the UDEV rules configuration you have created. The output should indicate that the block devices are available and the rules are applied as expected. For example:
	```
	# udevtest /block/sdb/sdb1
	main: looking at device '/block/sdb/sdb1' from subsystem 'block'
	udev_rules_get_name: add symlink
	'disk/by-id/scsi-360a98000686f6959684a453333524174-part1'
	udev_rules_get_name: add symlink
	'disk/by-path/ip-192.168.1.1:3260-iscsi-iqn.1992-08.com.netapp:sn.887085-part1'
	udev_node_mknod: preserve file '/dev/.tmp-8-17', because it has correct dev_t
	run_program: '/lib/udev/vol_id --export /dev/.tmp-8-17'
	run_program: '/lib/udev/vol_id' returned with status 4
	run_program: '/sbin/scsi_id'
	run_program: '/sbin/scsi_id' (stdout) '360a98000686f6959684a453333524174'
	run_program: '/sbin/scsi_id' returned with status 0
	udev_rules_get_name: rule applied, 'sdb1' becomes 'ocr1'
	udev_device_event: device '/block/sdb/sdb1' validate currently present symlinks
	udev_node_add: creating device node '/dev/ocr1', major = '8', minor = '17', 
	mode = '0640', uid = '0', gid = '500'
	udev_node_add: creating symlink
	'/dev/disk/by-id/scsi-360a98000686f6959684a453333524174-part1' to '../../ocr1'
	udev_node_add: creating symlink
	'/dev/disk/by-path/ip-192.168.1.1:3260-iscsi-iqn.1992-08.com.netapp:sn.84187085
	-part1' to '../../ocr1'
	main: run: 'socket:/org/kernel/udev/monitor'
	main: run: '/lib/udev/udev_run_devd'
	main: run: 'socket:/org/freedesktop/hal/udev_event'
	main: run: '/sbin/pam_console_apply /dev/ocr1
	/dev/disk/by-id/scsi-360a98000686f6959684a453333524174-part1
	/dev/disk/by-path/ip-192.168.1.1:3260-iscsi-iqn.1992-08.com.netapp:sn.84187085-
	part1'
	```
	In the example output, note that applying the rules renames OCR device `/dev/sdb1` to `/dev/ocr1`.
7. Enter the command to restart the UDEV service.
	On Asianux, Oracle Linux 5, and RHEL5, the commands are:
	```
	# /sbin/udevcontrol reload_rules
	# /sbin/start_udev
	```
	On SUSE 10 and 11, the command is:
	```
	# /etc/init.d boot.udev restart
	```

### 3.3.2 Using Disk Groups with Oracle Database Files on Oracle ASM

Review the following sections to configure Oracle Automatic Storage Management (Oracle ASM) storage for Oracle Clusterware and Oracle Database Files:

- Identifying and Using Existing Oracle Database Diskgroups on Oracle ASM
- Creating Diskgroups for Oracle Database Data Files

#### 3.3.2.1 Identifying and Using Existing Oracle Database Diskgroups on Oracle ASM

The following section describes how to identify existing disk groups and determine the free disk space that they contain.

- Optionally, identify failure groups for the Oracle ASM disk group devices.
	If you intend to use a normal or high redundancy disk group, then you can further protect your database against hardware failure by associating a set of disk devices in a custom failure group. By default, each device comprises its own failure group. However, if two disk devices in a normal redundancy disk group are attached to the same SCSI controller, then the disk group becomes unavailable if the controller fails. The controller in this example is a single point of failure.
	To protect against failures of this type, you could use two SCSI controllers, each with two disks, and define a failure group for the disks attached to each controller. This configuration would enable the disk group to tolerate the failure of one SCSI controller.
	Note:
	If you define custom failure groups, then you must specify a minimum of two failure groups for normal redundancy and three failure groups for high redundancy.

#### 3.3.2.2 Creating Diskgroups for Oracle Database Data Files

If you are sure that a suitable disk group does not exist on the system, then install or identify appropriate disk devices to add to a new disk group. Use the following guidelines when identifying appropriate disk devices:

- All of the devices in an Oracle ASM disk group should be the same size and have the same performance characteristics.
- Do not specify multiple partitions on a single physical disk as a disk group device. Oracle ASM expects each disk group device to be on a separate physical disk.
- Although you can specify a logical volume as a device in an Oracle ASM disk group, Oracle does not recommend their use because it adds a layer of complexity that is unnecessary with Oracle ASM. In addition, Oracle RAC requires a cluster logical volume manager in case you decide to use a logical volume with Oracle ASM and Oracle RAC.

### 3.3.3 Configuring Oracle Automatic Storage Management Cluster File System

Oracle ACFS is installed as part of an Oracle Grid Infrastructure installation (Oracle Clusterware and Oracle Automatic Storage Management) for 11g release 2 (11.2).

You can also create a General Purpose File System configuration of ACFS using ASMCA.

See Also:

Section 3.1.3, "General Information About Oracle ACFS" for supported deployment options

To configure Oracle ACFS for an Oracle Database home for an Oracle RAC database:

1. Install Oracle Grid Infrastructure for a cluster (Oracle Clusterware and Oracle Automatic Storage Management)
2. Change directory to the Oracle Grid Infrastructure home. For example:
	```
	$ cd /u01/app/11.2.0/grid
	```
3. Ensure that the Oracle Grid Infrastructure installation owner has read and write permissions on the storage mountpoint you want to use. For example, if you want to use the mountpoint `/u02/acfsmounts/`:
	```
	$ ls -l /u02/acfsmounts
	```
4. Start Oracle ASM Configuration Assistant as the grid installation owner. For example:
	```
	./asmca
	```
5. The Configure ASM: ASM Disk Groups page shows you the Oracle ASM disk group you created during installation. Click the ASM Cluster File Systems tab.
6. On the ASM Cluster File Systems page, right-click the Data disk, then select Create ACFS for Database Home.
7. In the Create ACFS Hosted Database Home window, enter the following information:
	- Database Home ADVM Volume Device Name: Enter the name of the database home. The name must be unique in your enterprise. For example: `dbase_01`
		- Database Home Mountpoint: Enter the directory path for the mount point. For example: `/u02/acfsmounts/dbase_01`
		Make a note of this mount point for future reference.
		- Database Home Size (GB): Enter in gigabytes the size you want the database home to be.
		- Database Home Owner Name: Enter the name of the Oracle Database installation owner you plan to use to install the database. For example: `oracle` 1
		- Database Home Owner Group: Enter the OSDBA group whose members you plan to provide when you install the database. Members of this group are given operating system authentication for the SYSDBA privileges on the database. For example: `dba1`
		- Click OK when you have completed your entries.
8. Run the script generated by Oracle ASM Configuration Assistant as a privileged user (`root`). On an Oracle Clusterware environment, the script registers the ACFS as a resource managed by Oracle Clusterware. Registering ACFS as a resource helps Oracle Clusterware to mount the ACFS automatically in proper order when ACFS is used for an Oracle RAC database Home.
9. During Oracle RAC installation, ensure that you or the DBA who installs Oracle RAC selects for the Oracle home the mount point you provided in the Database Home Mountpoint field (in the preceding example, `/u02/acfsmounts/dbase_01`).

See Also:

[Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e18951/toc.htm) for more information about configuring and managing your storage with Oracle ACFS

### 3.3.4 Upgrading Existing Oracle ASM Instances

If you have an Oracle ASM installation from a prior release installed on your server, or in an existing Oracle Clusterware installation, then you can use Oracle Automatic Storage Management Configuration Assistant (ASMCA, located in the path `Grid_home` `/bin`) to upgrade the existing Oracle ASM instance to 11g release 2 (11.2), and subsequently configure failure groups, Oracle ASM volumes and Oracle Automatic Storage Management Cluster File System (Oracle ACFS).

Note:

You must first shut down all database instances and applications on the node with the existing Oracle ASM instance before upgrading it.

During installation, if you are upgrading from an Oracle ASM release prior to 11.2, and you chose to use Oracle ASM and ASMCA detects that there is a prior Oracle ASM version installed in another Oracle ASM home, then after installing the Oracle ASM 11g release 2 (11.2) binaries, you can start ASMCA to upgrade the existing Oracle ASM instance. You can then choose to configure an Oracle ACFS deployment by creating Oracle ASM volumes and using the upgraded Oracle ASM to create the Oracle ACFS.

If you are upgrading from Oracle ASM 11g release 2 (11.2.0.1) or later, then Oracle ASM is always upgraded with Oracle Grid Infrastructure as part of the rolling upgrade, and ASMCA is started by the root scripts during upgrade. ASMCA cannot perform a separate upgrade of Oracle ASM from release 11.2.0.1 to 11.2.0.2.

On an existing Oracle Clusterware or Oracle RAC installation, if the prior version of Oracle ASM instances on all nodes is 11g release 1, then you are provided with the option to perform a rolling upgrade of Oracle ASM instances. If the prior version of Oracle ASM instances on an Oracle RAC installation are from a release prior to 11g release 1, then rolling upgrades cannot be performed. Oracle ASM on all nodes will be upgraded to 11g release 2 (11.2).

## 3.4 Desupport of Block and Raw Devices

With the release of Oracle Database and Oracle RAC 11g release 2 (11.2), using Database Configuration Assistant or the installer to store Oracle Clusterware or Oracle Database files on block or raw devices is not supported.

If you intend to upgrade an existing Oracle RAC database, or an Oracle RAC database with Oracle ASM instances, then you can use an existing raw or block device partition, and perform a rolling upgrade of your existing installation. Performing a new installation using block or raw devices is not allowed.

Alternatively, on IBM: Linux on System z block devices, you can use the `-d ldl` option to format the DASD using the Linux disk layout if you require only a single partition (for example, if you want to create a partition for ASM file management). If you use this disk layout, then the partition device name for the DASD is `/dev/dasd` `xxxx` `1`.

## 3.5 Configuring Raw Logical Volumes on IBM: Linux on System z

On IBM: Linux on System z, you can use raw logical volume manager (LVM) volumes for Oracle Clusterware and Automatic Storage Management files. You can create the required raw logical volumes in a volume group on either direct access storage devices (DASDs) or on SCSI devices. To configure the required raw logical volumes, follow these steps:

Note:

You do not have to format FBA-type DASDs in Linux. The device name for the single whole-disk partition for FBA-type DASDs is `/dev/dasd` `xxxx` `1`.

1. If necessary, install or configure the shared DASDs that you intend to use for the disk group and restart the system.
2. Enter the following command to identify the DASDs configured on the system:
	```
	# more /proc/dasd/devices
	```
	The output from this command contains lines similar to the following:
	```
	0302(ECKD) at ( 94: 48) is dasdm : active at blocksize: 4096, 540000 blocks, 2109 MB
	```
	These lines display the following information for each DASD:
	- The device number (`0302)`
		- The device type (`ECKD` or `FBA`)
		- The Linux device major and minor numbers (`94: 48`)
		- The Linux device file name (`dasdm`)
		In general, DASDs have device names in the form `dasd` `xxxx`, where `xxxx` is between one and four letters that identify the device.
		- The block size and size of the device
3. From the display, identify the devices that you want to use.
	If the devices displayed are FBA-type DASDs, then you do not have to configure them. You can proceed to bind them for Oracle Database files.
	If you want to use ECKD-type DASDs, then enter a command similar to the following to format the DASD, if it is not already formatted:
	```
	# /sbin/dasdfmt -b 4096 -f /dev/dasdxxxx
	```
	Caution:
	Formatting a DASD destroys all existing data on the device. Make sure that:
	- You specify the correct DASD device name
	- The DASD does not contain existing data that you want to preserve
	This command formats the DASD with a block size of 4 KB and the compatible disk layout (default), which enables you to create up to three partitions on the DASD.
4. If you intend to create raw logical volumes on SCSI devices, then proceed to step 5.
	If you intend to create raw logical volumes on DASDs, and you formatted the DASD with the compatible disk layout, then determine how you want to create partitions.
	To create a single whole-disk partition on the device (for example, if you want to create a partition on an entire raw logical volume for database files), enter a command similar to the following:
	```
	# /sbin/fdasd -a /dev/dasdxxxx
	```
	This command creates one partition across the entire disk. You are then ready to mark devices as physical volumes. Proceed to Step 6.
	To create up to three partitions on the device (for example, if you want to create partitions for individual tablespaces), enter a command similar to the following:
	```
	# /sbin/fdasd /dev/dasdxxxx
	```
	Use the following guidelines when creating partitions:
	- Use the `p` command to list the partition table of the device.
		- Use the `n` command to create a new partition.
		- After you have created the required partitions on this device, use the `w` command to write the modified partition table to the device.
		- See the `fdasd` man page for more information about creating partitions.
	The partitions on a DASD have device names similar to the following, where `n` is the partition number, between 1 and 3:
	```
	/dev/dasdxxxxn
	```
	When you have completed creating partitions, you are then ready to mark devices as physical volumes. Proceed to Step 6.
5. If you intend to use SCSI devices in the volume group, then follow these steps:
	1. If necessary, install or configure the shared disk devices that you intend to use for the volume group and restart the system.
		2. To identify the device name for the disks that you want to use, enter the following command:
		```
		# /sbin/fdisk -l
		```
		SCSI devices have device names similar to the following:
		```
		/dev/sdxn
		```
		In this example, `x` is a letter that identifies the SCSI disk and `n` is the partition number. For example, `/dev/sda` is the first disk on the first SCSI bus.
		3. If necessary, use `fdisk` to create partitions on the devices that you want to use.
		4. Use the `t` command in `fdisk` to change the system ID for the partitions that you want to use to `0x8e`.
6. Enter a command similar to the following to mark each device that you want to use in the volume group as a physical volume:
	For SCSI devices:
	```
	# pvcreate /dev/sda1 /dev/sdb1
	```
	For DASD devices:
	```
	# pvcreate /dev/dasda1 /dev/dasdb1
	```
7. To create a volume group named `oracle_vg` using the devices that you marked, enter a command similar to the following:
	For SCSI devices:
	```
	# vgcreate oracle_vg /dev/sda1 /dev/sdb1
	```
	For DASD devices:
	```
	# vgcreate oracle_vg /dev/dasda1 /dev/dasdb1
	```
8. To create the required logical volumes in the volume group that you created, enter commands similar to the following:
	```
	# lvcreate -L size -n lv_name vg_name
	```
	In this example:
	- `size` is the size of the logical volume, for example `500M`
		- `lv_name` is the name of the logical volume, for example `orcl_system_raw_500m`
		- `vg_name` is the name of the volume group, for example `oracle_vg`
	For example, to create a 500 MB logical volume for the SYSTEM tablespace for a database named `rac` in the `oracle_vg` volume group, enter the following command:
	```
	# lvcreate -L 500M -n rac_system_raw_500m oracle_vg
	```
	Note:
	These commands create a device name similar to the following for each logical volume:
	```
	/dev/vg_name/lv_name
	```
9. On the other cluster nodes, enter the following commands to scan all volume groups and make them active:
	```
	# vgscan
	# vgchange -a y
	```