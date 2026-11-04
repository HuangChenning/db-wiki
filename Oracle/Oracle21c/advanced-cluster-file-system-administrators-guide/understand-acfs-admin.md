---
title: "Administrator's Guide"
book: "Advanced Cluster File System Administrator's Guide"
doc_id: F30297-04
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/acfsg/understand-acfs-admin.html
tags:
  - oracle
  - 21c
  - advanced-cluster-file-system-administrators-guide
---

This section describes Oracle ACFS administration and contains the following topics:

### Oracle ACFS and File Access and Administration Security

Oracle ACFS supports traditional Unix-style file access control classes (user, group, other) for Linux environments.

Most Oracle ACFS administrative actions are performed by users with either root or Oracle ASM administration privileges for Linux environments. General Oracle ACFS information for file systems can be accessed by any system user.

In support of Oracle ACFS administration, Oracle recommends that the Oracle ASM administrator role is given to a root privileged user, as many common Oracle ACFS file system management tasks including mount, umount, fsck, driver load, and driver unload are root privileged operations. Other privileged Oracle ACFS file system operations that do not require root privileges can be performed by the Oracle ASM administrator. If the Oracle ASM administrator role is not given to a root privileged user, access to Oracle ACFS file systems can be restricted with the `norootsuid` and `nodev` mount options.

See Also:

- Oracle ACFS Encryption for information about Oracle ACFS encryption
- [Managing Oracle ACFS with Command-Line Tools](manage-acfs-advm-commands.md) for information about administering Oracle ACFS
- [Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/acfsg&id=OSTMG-GUID-7396FD18-628B-4026-AA55-79C6D6205EAE) for information about Oracle ASM privileges

### Oracle ACFS and Grid Infrastructure Installation

Oracle Grid Infrastructure includes Oracle Clusterware, Oracle ASM, Oracle ACFS, Oracle ADVM, and driver resources software components, which are installed into the Grid Infrastructure home using the Oracle Universal Installation (OUI) tool.

### Oracle ACFS Configuration

After a Grid Infrastructure installation and with an operational Oracle Clusterware, you can use Oracle ASM Configuration Assistant (ASMCA) to start the Oracle ASM instance and create Oracle ASM disk groups, Oracle ADVM volumes, and Oracle ACFS file systems. Alternatively, Oracle ASM disk groups and Oracle ADVM volumes can be created using SQL\*Plus and ASMCMD command line tools. File systems can be created using operating system command-line tools.

Oracle ACFS file systems are configured with Oracle ADVM based operating system storage devices that are created automatically following the creation of an Oracle ADVM dynamic volume file. After a volume file and its associated volume device file are created, a file system can be created and bound to that operating system storage device. Following creation, an Oracle ACFS file system can be mounted, after which it is accessible to authorized users and applications executing file and file system operations.

See Also:

- [Basic Steps to Manage Oracle ACFS Systems](steps-manage-acfs.md) for an example of the specific actions required to create a file system
- [ASMCA GUI Tool for Managing Oracle ACFS and Oracle ADVM](manage-acfs-advm-asmca.md) for information about managing Oracle ACFS file systems with ASMCA
- [Managing Oracle ACFS with Command-Line Tools](manage-acfs-advm-commands.md) for information about using Oracle ACFS commands to create a file system
- Oracle Clusterware Resources and Oracle ACFS Administration for information about configuring Oracle Clusterware resources for use with the database

### Oracle ACFS Features Enabled by Compatibility Attribute Settings

This topic describes the Oracle ACFS features enabled by valid combinations of the disk group compatibility attribute settings.

The following list applies to Oracle ACFS features enabled by disk group compatibility attribute settings.

- The value of `COMPATIBLE.ASM` must always be greater than or equal to the value of `COMPATIBLE.RDBMS` and `COMPATIBLE.ADVM`.
- Starting with Oracle Grid Infrastructure 12.2.0.1 software, the minimum setting for `COMPATIBLE.ASM` is `11.2.0.2`.
- A value of not applicable (n/a) means that the setting of the attribute has no effect on the feature.
- Oracle ACFS features not explicitly listed in the following table do not require advancing the disk group compatibility attribute settings.
- Oracle ACFS features explicitly identified by an operating system in the following table are available on that operating system starting with the associated disk group attribute settings.
- If encryption is configured for the first time on Oracle ASM 11g Release 2 (11.2.0.3) on Linux or if encryption parameters must be changed or a new volume encryption key must be created following a software upgrade to Oracle ASM 11g Release 2 (11.2.0.3) on Linux, then the disk group compatibility attributes for `ASM` and `ADVM` must be set to `11.2.0.3` or higher.
- Using replication or encryption with database files on Oracle ACFS is not supported.
- Oracle ACFS on Oracle Exadata storage is supported starting with Oracle Grid Infrastructure 12.1.0.2 on Linux.

The following table describes the Oracle ACFS features enabled by valid combinations of the disk group compatibility attribute settings.

Table 1-1 Oracle ACFS features enabled by disk group compatibility attribute settings

| Disk Group Features Enabled | COMPATIBLE.ASM | COMPATIBLE.RDBMS | COMPATIBLE.ADVM |
| --- | --- | --- | --- |
| Volumes in disk groups | \>= 11.2 | n/a | \>= 11.2 |
| Encryption, replication, security, tagging (Linux systems) | \>= 11.2.0.2 | n/a | \>= 11.2.0.2 |
| Read-only snapshots | \>= 11.2.0.2 | n/a | \>= 11.2.0.2 |
| Read-write snapshots | \>= 11.2.0.3 | n/a | \>= 11.2.0.3 |
| Unlimited file system expansion | \>= 11.2.0.4 | n/a | \>= 11.2.0.4 |
| Performance and scalability improvements in `ls` and `find` | \>= 11.2.0.4 | n/a | \>= 11.2.0.4 |
| Storing database files in Oracle ACFS for Oracle RAC configurations. | \>= 12.1 | n/a | \>= 12.1 |
| Encryption, replication, security, tagging (Solaris systems) | \>= 12.1 | n/a | \>= 12.1 |
| Replication and tagging (AIX systems) | \>= 12.1 | n/a | \>= 12.1 |
| Creation from an existing snapshot and conversion of a snapshot | \>= 12.1 | n/a | \>= 12.1 |
| Support for 1023 snapshots | \>= 12.1 | n/a | \>= 12.1.0.2 |
| Storing database files in Oracle ACFS for Oracle Restart configurations | \>= 12.2 | n/a | \>= 12.2 |
| Accelerator volume for Oracle ACFS file system | \>= 12.2 | n/a | \>= 12.2 |
| Metadata storage on accelerator volume for Oracle ACFS file system | \>=12.2, or >=12.1.0.2 on Oracle Data Appliance (ODA) | n/a | \>=12.2, or >=12.1.0.2 on Oracle Data Appliance (ODA) |
| Logical sector size of the Oracle ADVM volume | \>= 12.2 | n/a | \>= 12.2 |
| Oracle ACFS support for 4 K sectors | \>=12.2 | n/a | \>=12.2 |
| Oracle ACFS automatic resize | \>=12.2, or >=12.1.0.2 on Oracle Data Appliance (ODA) | n/a | \>=12.2, or >=12.1.0.2 on Oracle Data Appliance (ODA) |
| Oracle ACFS sparse files | \>=12.2, or >=12.1.0.2 on Oracle Data Appliance (ODA) | n/a | \>=12.2, or >=12.1.0.2 on Oracle Data Appliance (ODA) |
| Oracle ACFS compression | \>=12.2 | n/a | \>=12.2 |
| Oracle ACFS snapshot quotas | \>= 12.2 | n/a | \>= 12.2 |
| Oracle ACFS snapshot duplication | \>= 12.2 | n/a | \>= 12.2 |
| Oracle ACFS snapshot remastering | \>= 12.2 | n/a | \>= 12.2 |
| Space usage information by individual Oracle ACFS snapshots | \>= 12.2 | n/a | \>= 12.2 |
| Oracle ACFS snaphot-based replication | \>=12.2 | n/a | \>=12.2 |
| Oracle ACFS Defragger | \>=12.2 | n/a | \>=12.2 |
| Oracle ADVM volume on a flex disk group | \>=12.2 | \>=12.2 | \>=12.2 |
| Oracle ACFS replication role reversal or unplanned failover | \>=18.0 | n/a | \>=18.0 |
| Reducing the size of an Oracle ACFS file system | \>=18.0 | n/a | \>=18.0 |
| Oracle ACFS snapshot links | \>=18.0 | n/a | \>=21.1 |
| File Level Snapshots (Fshares) | \>=21.1 | n/a | \>=21.1 |

See Also:

- [Overview of Oracle ACFS](overview-acfs-advm.md) for information, including any limitations or restrictions, about storing data files in an Oracle ACFS file system
- [Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/acfsg&id=OSTMG-GUID-FBB5AA72-5208-48E1-BD8D-0FD4C6876F34) for more information about disk group compatibility attributes
- [Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/acfsg&id=OSTMG-GUID-BCA97B38-50AB-4B71-8D09-C67D8530D7BD) for information about the rebalancing process and the `ASM_POWER_LIMIT` initialization parameter

### Oracle Clusterware Resources and Oracle ACFS Administration

Oracle Clusterware resources support all aspects of Oracle ACFS. The resources are responsible for enabling and disabling volumes, loading drivers and mounting and unmounting file systems.

This section discusses the following topics:

- Summary of Oracle ACFS Resource-based Management
- High Availability Actions
- Creating Oracle ACFS Resources
- Node-Local or Clusterwide File Systems
- Monitoring Oracle ACFS resources
- Stopping Oracle ACFS resources
- Oracle ACFS resource Limitations

#### Summary of Oracle ACFS Resource-based Management

The following list provides a summary of Oracle ACFS resource-based management.

- The Oracle ACFS, Oracle Kernel Services (OKS), and Oracle ADVM drivers are dynamically loaded when the Oracle ASM instance is started.
	- Oracle ACFS
		This driver processes all Oracle ACFS file and directory operations.
		- Oracle ADVM
		This driver provides block device services for Oracle ADVM volume files that are used by file systems for creating file systems.
		- Oracle Kernel Services Driver (OKS)
		This driver provides portable driver services for memory allocation, synchronization primitives, and distributed locking services to Oracle ACFS and Oracle ADVM.
	The drivers are managed as a single resource set. For additional information, see " [Oracle ACFS Drivers Resource Management](acfs-advanced-topics.md) " and " [Oracle ACFS Driver Commands](acfs-advanced-topics.md) ".
- When a volume is created, Oracle ADVM creates a resource with the name of `ora.``DISKGROUP``.``VOLUME``.advm`. This resource is usually managed through transparent high availability calls from Oracle ASM and requires no user interaction. However, the user may choose to use the SRVCTL command interface to start and stop volumes as well as control the default state of the volume after an Oracle ASM restart. This is especially beneficial in a large cluster or an Oracle Flex ASM cluster, as volumes on other nodes may be operated upon.
	In addition, these Oracle ADVM resources can be used by other resources in the Oracle Clusterware stack to maintain dependency chains. Dependency chains ensure that the resources a program requires to run are available. For instance, if a resource was monitoring a backup application that was backing up to Oracle ADVM volume, the backup application would want to ensure that it specified the Oracle ADVM volume resource in it's `START` and `STOP` dependency list. Because the Oracle ADVM volume resource will enable the volume, this ensures that the volume is available before the backup begins.
- Oracle ACFS file systems are either manually mounted or dismounted using an Oracle ACFS or Oracle Clusterware command-line tool, or automatically mounted or dismounted based on an Oracle Clusterware resource action.
	For example, a file system hosting an Oracle Database home is named in the dependency list of the associated Oracle Database resource such that issuing a start on the database resource results in mounting the dependent Oracle ACFS hosted database home file system.
	Oracle ACFS file system resources provide the following actions:
	- MOUNT
		During the `START` operation the resource mounts the file system on the path configured in the resource. The Oracle ACFS file system resource requires all components of the Oracle ASM stack to be active (volume device, ASM) and ensures that they are active before attempting the mount.
		- UNMOUNT
		During the `STOP` operation, the resource attempts to unmount a file system.
- Oracle provides two resource types for Oracle Highly Available NFS. For more information, refer to Oracle ACFS NAS Maximum Availability eXtensions.

As with all Oracle Clusterware resources, these resources provide for high availability by monitoring the underlying device, file system, or driver to ensure that the object remains available. In the event that the underlying object becomes unavailable, each resource attempts to make the underlying object available again.

#### High Availability Actions

The following are the actions of the High Availability resources:

- Oracle ACFS resource
	This resource attempts to unmount the file system. After the unmount has succeeded, the resource remounts the file system, making the file system available again. If processes are active on the file system during unmount, the resource identifies and terminates those processes.
- Oracle ADVM resource
	This resource attempts to disable any volume device, and then reenable the volume device. At that point, any configured Oracle ACFS resource can remount the file system. If processes are active on the volume during this period, the resource identifies and terminates the processes.

#### Creating Oracle ACFS Resources

Oracle ACFS resources can be created with the following methods:

- Oracle ASM Configuration Assistant (ASMCA) provides a GUI that exposes the most common functionality. In all cases, creating a file system resource does not format the underlying file system. Attempts to start the resource require the user to format the file system either manually or with ASMCA.
- SRVCTL provides a highly flexible command line utility for creating Oracle ACFS file system resources through the `filesystem` object. Oracle ACFS resources created through this mechanism have access to the full feature set, including server pools.
- `acfsutil` commands provide an alternative method to create Oracle ACFS file system resources using the `registry` object. Oracle ACFS resources created through this methodology have access to a limited set of options.

The differences between SRVCTL and `acfsutil` commands are:

- Oracle ACFS resources created through SRVCTL and specifying a server pool or list of nodes are only mounted on one of those nodes. (node-local)
- Oracle ACFS resources created through SRVCTL can take advantage of Oracle Server Pools.
- Oracle ACFS resources created through `acfsutil` commands and specifying a list of nodes are mounted on all listed nodes. (node-local)
- Oracle ACFS resources created through `acfsutil` commands are created with `AUTOSTART` set to `ALWAYS`.
- Oracle ACFS resources created through SRVCTL allow for advanced Application ID functionality. Using this functionality enables the resource type to be set by the administrator. After the type is set, other resources can depend on this type, allowing different node-local file systems to be used to fulfill dependencies on each node. In a simplified example, this would allow the administrator to have a different device mounted on the `/log` directory on each node of the cluster, and be able to run an Apache resource. The Apache resource would specify the new type in its resource dependency structure, rather than specifying an individual resource.
- Oracle ACFS resources created through SRVCTL can specify additional `AUTOSTART` parameters. These parameters can be used to prevent the resource from starting on stack startup, to always force the resource to start, or to only start the resource if it was previously running.
- Oracle ACFS resources created through SRVCTL have access to functionality such as accelerator volumes.

The common elements of both SRVCTL and `acfsutil` commands are:

- User
	This is an additional user that can act upon the resource. By default, you must be the `root` user to start and stop an Oracle ACFS resource.
- Options
	These are mount options that should be used to mount the file system when the resource is starting.

#### Node-Local or Clusterwide File Systems

When creating Oracle ACFS file system resources, you can create a node-local file system or to create a clusterwide file system.

- Node-local
	This file system type is limited to the number of nodes it can mount on. Depending on if it is created with SRVCTL or `acfsutil` commands, it may only mount on one node, a subset of nodes, or all the configured nodes. In some cases, this could look the same as a full cluster configuration, but if new nodes are added to the cluster, the file system is not automatically mounted on them without modifying the list of allowable nodes.
- Clusterwide
	This type of file system mounts on all nodes of the cluster, with no exceptions. When new members are added to the cluster, the file system is automatically available on them. This type of resource is required for certain configurations, such as Oracle Database or Oracle HANFS.

#### Monitoring Oracle ACFS resources

Similar to all Oracle Clusterware resources, Oracle ACFS resources enables you to monitor the state of the system. You can do this monitoring with the following commands:

- Using SRVCTL commands
	When the command `srvctl` `status` `filesystem` or `srvctl` `status` `volume` is run, the output of the command reports if the file system is mounted or the volume is enabled, and which nodes this is true on.
- Using CRSCTL commands
	When the `crsctl` `status` `resource` command is run, a state of `ONLINE` is reported for each resource that is available, whether through a mounted file system or an enabled volume. A state of `OFFLINE` is reported for each resource that is not available, whether through an unmounted file system or a disabled volume. Additional status may be presented in the `STATUS` field of this output.

#### Stopping Oracle ACFS resources

You can be stop Oracle ACFS file system resources with the following methods:

- You can stop the entire Oracle Clusterware stack. When the Oracle Clusterware stack is stopped, all Oracle ACFS resources are automatically stopped.
- To stop individual resources, you can use SRVCTL management commands with the Oracle ACFS files system or volume object. If there are other resources that are depending on the resource that you are attempting to stop, then the command may require the `-force` option.
- You may engage a manual action, such as running `unmount` on a file system or by manually stopping a volume using ASMCMD or SQL\*Plus commands. In this case, the Oracle ACFS resource transitions to the `OFFLINE` state automatically.

Non-Oracle Grid Infrastructure usage of mount points can prevent unmounting and disabling of volumes in the kernel for some situations. For example:

- Network File System (NFS)
- Samba/Common Internet File System (CIFS)

If either of the previous examples reflects your situation, then ensure that you discontinue the use of the functionality before initiating a stack shutdown, file system unmount, or volume disable.

Additionally, some user space processes and system processes may use the file system or volume device in a manner that prevents the Oracle Grid Infrastructure stack from shutting down during a patch or upgrade. If this problem occurs, then use the `lsof` and `fuser` commands (Linux and UNIX) to identify processes which are active on the Oracle ACFS file systems and Oracle ADVM volumes. To ensure that these processes are no longer active, dismount all Oracle ACFS file systems or Oracle ADVM volumes and issue an Oracle Clusterware shutdown. Otherwise, errors may be raised during an Oracle Clusterware shutdown relating to activity on Oracle ACFS file systems or Oracle ADVM volumes, preventing the successful shutdown of Oracle Clusterware.

#### Oracle ACFS resource Limitations

Oracle ACFS has the following resource limitations:

- All Oracle ACFS resources require `root` privileges to create.
- All Oracle ACFS resources require `root` privileges to remove.
- All Oracle ACFS file system resources require `root` privileges to act upon, such as starting and stopping the resources, but can be configured to allow another user, such as a database user, to do so. In this case, the `root` user must be used to configure the resource.
- All Oracle ADVM volume resources allow the `ASMADMIN` user to act upon them.
- All Oracle ACFS resources are only available in Oracle RAC mode. Oracle ACFS resources are not supported in Oracle Restart configurations. For more information about Oracle ACFS and Oracle Restart, refer to [Oracle ACFS and Oracle Restart](acfs-advanced-topics.md).

### Oracle ACFS and Dismount or Shutdown Operations

It is important to dismount any active file system configured with an Oracle ADVM volume device file before an Oracle ASM instance is shutdown or a disk group is dismounted. After the file systems are dismounted, all open references to Oracle ASM files are removed and associated disk groups can be dismounted or the instance shut down.

If the Oracle ASM instance or disk group is forcibly shut down or fails while an associated Oracle ACFS is active, the file system is placed into an offline error state. If any file systems are currently mounted on Oracle ADVM volume files, the `SHUTDOWN` `ABORT` command should not be used to terminate the Oracle ASM instance without first dismounting those file systems. Otherwise, applications encounter IO errors and Oracle ACFS user data and metadata being written at the time of the termination may not be flushed to storage before the Oracle ASM storage is fenced. If it is not possible to dismount the file system, then you should run two `sync` (1) commands to flush cached file system data and metadata to persistent storage before issuing the `SHUTDOWN` `ABORT` operation.

Any subsequent attempt to access an offline file system returns an error. Recovering a file system from that state requires dismounting and remounting the Oracle ACFS file system. Dismounting an active file system, even one that is offline, requires stopping all applications using the file system, including any shell references. For example, a previous change directory (`cd`) into a file system directory. The Linux `fuser` or `lsof` commands list information about processes and open files.

See Also:

- [Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/acfsg&id=OSTMG-GUID-9C2208C8-B436-4A18-A5D7-0CE854751529) for information about shutting down an Oracle ASM instance
- [Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/acfsg&id=OSTMG-GUID-4782D609-766B-4686-B5E4-90A8EFC10DEA) for information about dismounting a disk group

### Oracle ACFS Encryption

Oracle ACFS encryption enables you to encrypt data stored on disk (data-at-rest).

The encryption feature protects data in an Oracle ACFS file system in encrypted format to prevent unauthorized use of data in the case of data loss or theft. Both encrypted and non-encrypted files can exist in the same Oracle ACFS file system.

Some encryption functionality requires system administrator privileges. This functionality incudes the commands for initiating, setting, and reconfiguring encryption.

System administrators and Oracle ACFS security administrators can initiate encryption operations. Also, unprivileged users can initiate encryption for files they own.

Oracle ACFS encryption provides two type of encryption keys:

- File Encryption Key
	This is a key for a file and is used to encrypt the data in the file.
- Volume Encryption Key
	This is a key for a file system and is used to encrypt the file encryption keys.

You must first create the encryption key store, then specify file system-level encryption parameters and identify the directories. No extra steps are required for a user to read encrypted files if the user has the appropriate privileges for accessing the file data.

Oracle ACFS encryption supports both Oracle Cluster Registry (OCR) and Oracle Key Vault as a key store. Both OCR and Oracle Key Vault can be used in the same cluster. However, a single file system uses either OCR or Oracle Key Vault as a key store, but not both. Oracle Key Vault is currently only available with file systems on Linux.

If you are using OCR as a key store, you can store volume encryption keys (VEKs) in either password-protected PKCS wallets or passwordless SSO wallets. You should back up the OCR after creating or updating a volume encryption key to ensure there is an OCR backup that contains all of the volume encryption keys (VEKs) for the file system.

If you are using Oracle Key Vault as a key store, note that Oracle Key Vault endpoints must be created with an endpoint type of “Oracle ACFS”. Additionally, all Oracle Key Vault endpoints within the same cluster must share the same endpoint password.

Oracle ACFS encryption protects data stored on secondary storage against the threat of theft or direct access to the storage medium. Data is never written to secondary storage in plaintext. Even if physical storage is stolen, the data stored cannot be accessed without the encryption keys. The encryption keys are never stored in plaintext. The keys are either obfuscated, or encrypted using a user-supplied password.

Auditing and diagnostic data are logged for Oracle ACFS encryption. The log files include information such as `acfsutil` commands that have been run, the use of security or system administrator privileges, and run-time failures. Logs are written to the following files:

- `mount_point` `/.Security` `/encryption/logs/encr-` `hostname_fsid``.log`
	The directory is created with `acfsutil` `encr` `set` command.
- `GRID_HOME` `/log/` `hostname` `/acfs/security/acfssec.log`
	The messages that are logged to this file are for commands that are not associated with a specific file system, such as `acfsutil` `encr` `init`. The directory is created during installation and is owned by the root user.

When an active log file grows to a pre-defined maximum size (10 MB), the file is automatically moved to `log_file_name``.bak`, the administrator is notified, and logging continues to the regular log file name. When the administrator is notified, the administrator must archive and remove the `log_file_name``.bak` file. If an active log file grows to the maximum size and the `log_file_name``.bak` file exists, logging stops until the backup file is removed. After the backup log file is removed, logging restarts automatically.

Note the following when working with Oracle ACFS encryption:

- A copy of an encrypted file is not encrypted unless the copy of the file is made in an encrypted directory.
	Some applications, such as the `vi` editor, re-create a file when the file is modified. The modified file is saved as a temporary file, the original file is removed, and temporary file is copied with the original file name as the destination name. This process creates a new file. The new file is not encrypted unless it is created in an encrypted directory. If you are planning to copy an encrypted file, you should ensure that the parent directory is also encrypted.
- Using encryption with database files on Oracle ACFS is not supported.
- Oracle ACFS encryption cannot be used with password-protected (PKCS) wallets if any of the file systems using encryption are configured to be mounted with the Oracle ACFS mount registry.
- ACFS encryption is not FIPS-140 compliant.

To use Oracle ACFS encryption functionality on Linux, the disk group compatibility attributes for `ASM` and `ADVM` must be set to `11.2.0.2` or higher. The disk group compatibility attributes for `ASM` and `ADVM` must be set to `11.2.0.3` or higher on Linux for the following cases:

- If encryption is configured for the first time on Oracle ASM 11g Release 2 (11.2.0.3).
- If encryption parameters must be changed or a new volume encryption key must be created following a software upgrade to Oracle ASM 11g Release 2 (11.2.0.3)..

Encryption information for Oracle ACFS file systems is displayed in the `V$ASM_ACFS_ENCRYPTION_INFO` view. To configure encryption and manage encrypted Oracle ACFS file systems, you can use the `acfsutil` `encr` command-line functions and Oracle ASM Configuration Assistant.

Note:

Starting with Oracle ACFS 21c, Oracle ACFS encryption is desupported on Solaris and Microsoft Windows operating systems. Oracle ACFS Encryption on Oracle Solaris and Microsoft Windows is based on RSA technology. Retirement of RSA technology has been announced. Oracle ACFS Encryption continues to be supported on Linux, and is unaffected by this deprecation, because Linux uses an alternative technology.

See Also:

- [acfsutil encr set](acfs-commands-encryption.md) and [acfsutil encr rekey](acfs-commands-encryption.md) for information about changing or creating a volume encryption key
- Oracle ACFS Features Enabled by Compatibility Attribute Settings for information about Oracle ACFS features and disk group compatibility attribute settings
- [About Oracle ACFS Snapshots](understand-acfs-concepts.md) for information about Oracle ACFS encryption and snapshots
- [Using Views to Display Oracle ACFS Information](views-acfs-advm-info.md) for information about `V$ASM_ACFS` views
- [Encrypting Oracle ACFS File Systems using OCR as Encryption Key Store](steps-manage-acfs.md) and [Oracle ACFS Command-Line Tools for Encryption](acfs-commands-encryption.md) for information about managing encryption with Oracle ACFS command-line tools
- [Managing Security and Encryption for Oracle ACFS with ASMCA](manage-acfs-advm-asmca.md) for information about using Oracle ASMCA with encryption features
- [Oracle Key Vault Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/acfsg&id=OKVAG-GUID-0D169EB8-C355-459A-9ABD-325CA5B46DD0) for information about Oracle Key Vault

### Oracle ACFS Compression

Oracle ACFS compression is enabled on a specified Oracle ACFS file system for general purpose files. Oracle ACFS compression is not supported for Oracle Database files.

Cached IO compression is performed asynchronously, after the application has written to the file. When enabling compression on a file system, existing files are not compressed, only newly-created files are compressed. When compression is disabled, compressed files are not uncompressed. Compressed files are associated with a compression unit and the compression algorithm operates on this unit. The default unit size is currently 32 K. `lzo` is the default compression algorithm and the only compression algorithm currently supported.

The `acfsutil` `compress` command sets and resets the compression state of a file system with `acfsutil` `compress` `on` and `acfsutil` `compress` `off`. To display the compression state and effectiveness of the compression operation, use the `acfsutil` `compress` `info` command. The `acfsutil` `info` `fs` and `acfsutil` `info` `file` commands have been enhanced to report on Oracle ACFS compression status.

Compressed files consume less disk space than non-compressed files. However, for applications using the file, the size reported is equal to the uncompressed file size, not the smaller compressed size. Some utilities, such as `ls` `-l`, report the uncompressed size of the file. Utilities such as `du`, `acfsutil` `compress` `info`, and `acfsutil` `info` `file`, report the actual disk allocation of the compressed file.

Note the following about Oracle ACFS compression.

- Oracle ACFS compression is not supported for Oracle ACFS file systems which are intended to hold database files. Instead, use Oracle Advanced Compression.
- Loopback mounts are not supported with compressed files. This includes files intended for use by Oracle ACFS remote service. If a loopback device is associated with a compressed file, read and write operations to the loopback device fail.
- A loopback device can be associated with an uncompressed file on an Oracle ACFS file system that has been enabled for compression.
- For Oracle Grid Infrastructure 12c release 2 (12.2.0.1), Oracle ACFS compression is supported on Linux and AIX.
- Oracle ACFS compression is only supported with Oracle ACFS snapshot-based replication that is available starting with Oracle Grid Infrastructure 12c release 2 (12.2.0.1).
- ADVM disk group compatibility must be set to `12.2` or higher.

See Also:

- [Oracle ACFS Command-Line Tools for Compression](acfs-commands-compression.md) for information about the Oracle ACFS compression commands
- [Oracle ACFS Command-Line Utilities](acfs-commands-utilities.md) for information about the `acfsutil` `info` commands

### Oracle ACFS Replication

Oracle ACFS snapshot-based replication enables replication of Oracle ACFS file systems across a network to a remote site, providing disaster recovery capability for the file system.

Oracle ACFS replication enables either a mounted file system or a snapshot of a mounted file system to be designated as a replication storage location. The source Oracle ACFS location of an Oracle ACFS replication relationship is referred to as a primary location. The target Oracle ACFS location of an Oracle ACFS replication relationship is referred to as a standby location.

Note:

- Oracle ACFS replication functionality supports only one standby location for each primary location.
- The standby location is read-only for as long as replication is active on it. Read-write snapshots may be created of the standby.
- A primary site running Linux, Solaris or AIX can replicate to a standby site running any of those operating systems where Oracle ACFS is supported.
	Note that application data is not modified in any cross-platform use of Oracle ACFS replication. Oracle ACFS replication only ensures the validity of its metadata when transferring between different operating systems.
- The primary and standby sites should be running the same version of the Oracle Grid Infrastructure software. When upgrading the sites, update the standby site first.
- Oracle ACFS replication is not supported with Oracle Restart.
- An Oracle Key Vault keystore is not supported on a standby file system containing replication locations.
- Oracle ACFS encryption cannot be undone on a primary file system containing replication locations.
	You cannot undo encryption on a file system having active snapshots. If you want to undo encryption on primary file system containing active replication locations, then first terminate replication. After replication has stopped, then undo encryption and start replication again.

A site can host both primary and standby locations. For example, if there are cluster sites `A` and `B`, a primary file system hosted at site `A` can be replicated to a standby snapshot at site `B`. At the same time, a primary snapshot hosted at site `B` can be replicated to a standby file system at site `A`. However, an Oracle ACFS file system or snapshot cannot be used simultaneously as a primary and a standby location.

Oracle ACFS snapshot-based replication operates by recording snapshots of the primary location. After the initial snapshot is transferred to the standby location, replication continues by transferring the changes between successive snapshots of the primary to the standby location. These replication operations can occur either in constant mode (enabling a new operation to start as soon as the previous one completes), or can be scheduled to occur at fixed intervals. This replication solution is by nature asynchronous.

Oracle ACFS replication uses snapshot functionality on the primary site initially to externalize both the contents of the initial snapshot, and later the differences between two specified snapshots. The result is called a snapshot duplication stream. The replication process then uses snapshot functionality on the standby site to apply this stream to the standby location, creating a duplicate of the primary location.

On the primary, because replication works by comparing successive snapshots, it is critical that there is enough disk space available on the site hosting the primary to contain the version of the primary recorded in each snapshot, as well as the current primary contents. In addition, there must always be enough space to create the snapshots required. Each replication snapshot is deleted when no longer needed.

On the standby, a backup snapshot is created at the end of each replication operation. This snapshot records the latest consistent contents of the standby, and can be used to recover those contents if a permanent outage occurs during the current replication operation. Each backup snapshot is deleted when the following replication operation is complete, so it must always be possible to create a backup snapshot. In addition, enough space must exist for the version of the standby captured in the snapshot and the current standby contents.

You should ensure that the primary and standby file systems do not run out of disk space. If either file system runs out of available storage, you should either expand the file system or free up space by removing files from the file system or any read-write snapshots present. You can also configure automatic resize to avoid running out of space.

If the primary file system runs out of space and you decide to free up space by removing files, then you should only remove files that are not being replicated. Replicated files have been stored in a snapshot pending transfer to the standby file system and are not deleted. You can delete any Oracle ACFS snapshots not created by replication.

Replication Configuration Information

Oracle ACFS replication uses the `ssh` utility as the transport between the primary and standby clusters. To enable the automated use of `ssh`, replication requires a specific user to be designated as the replication user, or repluser. For this user, two kinds of keys need to be configured. These keys must be available on each node where replication is enabled to run.

- On each node in each cluster, the repluser must have a host key stored for each node in the other cluster.
- On each node in each cluster, a public key for repluser, as defined on the other cluster, must be stored that is authorized to log in as repluser on that node..

These keys are required to ensure that replication running on a primary host is able to authenticate the standby host to which it is sending data using the host keys. Also, replication running on a primary host must be able to log in as the apply user on a standby host with the user keys to update the standby location. In addition, replication has the ability to reverse the roles being played by primary and standby. For this role reversal operation to be successful, primary and standby hosts require the same types of `ssh` keys to be configured. For more information, refer to [Configuring ssh for Use With Oracle ACFS Replication](acfs-advanced-topics.md).

Before using replication on a file system or snapshot, ensure that you have checked the following:

- There is sufficient network bandwidth to support replication between the primary and standby locations.
- The configuration of the sites hosting the primary and standby locations enable the standby file system to keep up with the rate of change on the primary location.
- Host keys and user keys for `ssh` have been configured properly.

Directories and files in an Oracle ACFS file system or snapshot can be tagged to select specific objects that you want to replicate in a file system.

Before replicating a given location, a replication configuration must be created to identify any necessary information, such as the site hosting the primary location, the site hosting the standby location, the file system to be replicated, the mount point of the file system for the location, and a list of tags.

The primary and standby sites must share the same user and group configurations, including all uids and gids in use in the two locations. The apply user repluser described previously must be configured on each node where replication is enabled. This user should be a member of the Oracle ASM administration group and must have Oracle ASM administrator user privileges.

Note:

The mappings between user names and numeric `uids`, and between group names and numeric `gids`, must be identical on both the primary cluster and the standby cluster. This is required to ensure that the numeric values are used in the same manner on both clusters because replication transfers only the numeric values from the primary to standby.

Replication Role Reversal

Oracle ACFS replication provides replication role reversal functionality, which enables the original primary and standby locations to reverse roles. Using the `acfsutil` `repl` `reverse` command, you can change the original primary to the new standby, and the original standby to the new primary. The role reversal functionality enhances replication to provide additional disaster recovery capabilities.

Replication Unplanned Failover

Oracle ACFS replication provides for unplanned failover functionality with the `acfsutil` `repl` `failover` command. The command can be invoked on the standby in both the planned failover case (primary up) and the unplanned failover case (primary down). To distinguish the two cases, `acfsutil` `repl` `failover` attempts for a specific amount of time to contact the primary. There is an option available to control how long the standby waits to hear from the primary before deciding that the primary is down.

When `acfsutil` `repl` `failover` attempts to contact the primary:

- If the primary responds, then the standby collaborates with the primary to do a planned failover with no data loss.
- If the primary does not respond, then the standby assumes that the primary is down, and initiates an unplanned failover with no involvement of the primary. There is a likely chance of incurring data loss.

Additional Information

To use Oracle ACFS replication functionality, the disk group compatibility attributes for `ASM` and `ADVM` must be set to `12.2` or higher for the disk groups that contain the file systems for the primary and standby locations. To use Oracle ACFS role reversal or unplanned failover replication functionality, the disk group compatibility attributes for `ASM` and `ADVM` must be set to `18.0` or higher for the disk groups that contain the file systems for the primary and standby locations.

To use Oracle ACFS replication on Solaris Sparc hardware, the system must be running Solaris 10 update 8 or later.

To configure replication and manage replicated Oracle ACFS locations, use the `acfsutil` `repl` command-line functions.

Note:

Starting with Oracle ACFS 21c, Oracle ACFS replication protocol version 1 is desupported. Replication protocol version 1 has been replaced with snapshot-based replication version 2, introduced in Oracle ACFS 12c Release 2 (12.2.0.1).

See Also:

- [Oracle ACFS Command-Line Tools for Replication](acfs-commands-replication.md) for information about Oracle ACFS `acfsutil` replication commands
- Oracle ACFS Replication with Encryption for information about using Oracle ACFS replication with other Oracle ACFS features
- [acfsutil size](acfs-commands-utilities.md) for information about resizing an Oracle ACFS file system
- Oracle ACFS Tagging for information on tagging
- Oracle ACFS Features Enabled by Compatibility Attribute Settings for information about Oracle ACFS features and disk group compatibility attribute settings
- [Replicating Oracle ACFS File Systems](steps-manage-acfs.md) for information about using the `acfsutil` `repl` command-line functions to configure replication and manage replicated Oracle ACFS file systems
- [Configuring Oracle ACFS Snapshot-Based Replication](acfs-advanced-topics.md) for information about converting an existing Oracle ACFS replication environment to the snapshot-based replication introduced in release 12.2.0.1
- [Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/acfsg&id=OSTMG-GUID-7396FD18-628B-4026-AA55-79C6D6205EAE) for information about Oracle ASM privileges
- Information about tuning your network on the Oracle Maximum Availability Architecture (MAA) website at [`https://www.oracle.com/database/technologies/high-availability/maa.html`](https://www.oracle.com/database/technologies/high-availability/maa.html)
- Data Guard Redo Transport & Network Configuration document for relevant information about tuning your network
- Additional information on the Oracle ACFS website at [`https://www.oracle.com/database/technologies/rac/acfs.html`](https://www.oracle.com/database/technologies/rac/acfs.html)

### Oracle ACFS Tagging

Oracle ACFS tagging assigns a common naming attribute to a group of files.

Oracle ACFS Replication can use this tag to select files with a unique tag name for replication to a different remote cluster site. The tagging option avoids having to replicate an entire Oracle ACFS file system.

Oracle ACFS implements tagging with Extended Attributes. Some editing tools and backup utilities do not retain the Extended Attributes of the original file by default; you must set a specific switch. The following list describes the necessary requirements and switch settings for some common utilities to ensure Oracle ACFS tag names are preserved on the original file.

- The `cp` command requires flags to preserve tag names.
	Install the `coreutils` library (version `coreutils-5.97-23.el5_4.1.src.rpm` or `coreutils-5.97-23.el5_4.2.x86_64.rpm` or later) on Linux to install versions of the `cp` command that supports Extended Attribute preservation with the `--preserve=xattr` switch and the `mv` command that supports Extended Attribute preservation without any switches.
	`cp` does not preserve tag names assigned to symbolic link files.
	The `cp` switches required to preserve tag names on files and directories are:
	- Linux: `--preserve=xattr`
		- Solaris: `-@`
		- AIX: `-U`
- The `cpio` file transfer utility requires flags to preserve tag names.
	The `cpio` switches required to preserve tag names on files and directories are:
	- Linux: `cpio` does not preserve tag names
		- Solaris: `-@` is required to preserve or restore tag names for files and directories, but does not preserve tag names for symbolic link files
		- AIX: `-U` is required to preserve or restore tag names for files and directories, but does not preserve tag names for symbolic link files
- `emacs` requires that the `backup-by-copying` option is set to a non-nil value to preserve tag names on the original file name rather than a backup copy. This option must be added to the `.emacs` file.
- The `pax` file transfer utility requires flags to preserve tag names.
	The `pax` switches required to preserve tag names on files and directories are:
	- Linux: `pax` does not preserve tag names
		- Solaris: `-@` is required to preserve or restore tag names for files and directories, but does not preserve tag names for symbolic link files
		- AIX: `-U` is required to preserve or restore tag names for files and directories, but does not preserve tag names for symbolic link files
- The `rsync` file transfer utility requires flags to preserve tag names.
	The `rsync` switches required to preserve tag names on files and directories are:
	- Linux: `-X` `-l` are required to preserve tag names for files and directories, but these switches do not preserve tag names for symbolic link files
		- Solaris: `rsync` does not preserve tag names
		- AIX: not available
- The `tar` backup utility can have flags set on the command line to preserve tag names on a file. However, `tar` does not retain the tag names assigned to symbolic link files.
	The `tar` switches required to preserve tag names on files and directories are:
	- Linux: `--xattrs`
		- Solaris: `-@`
		- AIX: `-U`
- The `vim` or `vi` editors require the `set bkc=yes` option in the `.vimrc` (Linux) file to make a backup copy of a file and overwrite the original. This preserves tag names on the original file.

To use Oracle ACFS tagging functionality on Linux, the disk group compatibility attributes for `ASM` and `ADVM` must be set to `11.2.0.2` or higher. To use Oracle ACFS tagging functionality on Solaris or AIX, the disk group compatibility attributes for `ASM` and `ADVM` must be set to `12.1` or higher.

See Also:

- Oracle ACFS Features Enabled by Compatibility Attribute Settings for information about Oracle ACFS features and disk group compatibility attribute settings
- [Tagging Oracle ACFS File Systems](steps-manage-acfs.md) and [Oracle ACFS Command-Line Tools for Tagging](acfs-commands-tagging.md) for information about using the `acfsutil` `tag` command-line functions to configure tagging and manage tagged Oracle ACFS file systems
- [Oracle ACFS Tagging Generic Application Programming Interface](acfs-advanced-topics.md) for information about Oracle ACFS tagging application programming interfaces (APIs)

### Oracle ACFS Replication with Encryption

Note:

Starting with Oracle ACFS 21c, Oracle ACFS Security (Vault) and ACFS Auditing are desupported. Desupporting cluster features with limited adoption allows Oracle to focus on improving core scaling, availability, and manageability across all features and functionality. Oracle ACFS Security (Vault) and ACFS Auditing are desupported.

Encryption can be enabled on an Oracle ACFS file system on which replication has been configured. The replicated standby file system is secured with the same encryption policies as the primary file system. For this replicated environment, the primary and standby file systems must both be 12.1 or higher installations. For more information about Oracle ACFS replication, refer to " Oracle ACFS Replication ".

To ensure successful replication, the standby file system must be a generic file system without encryption metadata on it. Oracle ACFS does not support using a standby file system that once had encryption and then had encryption removed. Additional conditions that must be met for Oracle ACFS encryption are listed in this section.

Note the following about Oracle ACFS encrypted file systems:

- Encrypted files on the primary file system remain encrypted on the standby file system with the same key and encryption parameters (algorithm and key length).
- Encryption operations done on the primary file system are replayed on the standby file system - on, off, and rekey.
- Encryption may be enabled before or after a file system is replicated. In either case, an encryption wallet is transparently created on the standby file system if one does not exist because `acfsutil` `encr` `init` has not been run on the standby file system.
- A password-protected wallet is not supported on the standby file system. If a PKCS wallet already exists on a site that is to be used as a standby file system, the administrator must use the `acfsutil` `keystore` `migrate` command to transfer all keys to an SSO wallet.

### Oracle ACFS Plugins

The Oracle ACFS plugin functionality enables a user space application to collect just-in-time Oracle ACFS file and Oracle ADVM volume metrics from the operating system environment.

Applications can use the Oracle ACFS plug-in infrastructure to create customized solutions that extend the general application file metric interfaces to include detailed Oracle ACFS file system and volume data.

The Oracle ACFS plug-in functionality can be enabled on separate Oracle ACFS file systems mounted on a standalone host or on one or more nodes of an Oracle Grid cluster where the Oracle ACFS file system is mounted. This functionality enables message communication between a node-local plugin enabled Oracle ACFS file system and an associated user space application module using Oracle ACFS plug-in application programming interfaces (APIs).

The plugin message APIs support both polling and posting message delivery models and multiple message payload types.

See Also:

- [Oracle ACFS Command-Line Utilities](acfs-commands-utilities.md) for information about Oracle ACFS plugin commands
- [Oracle ACFS Plug-in Generic Application Programming Interface](acfs-advanced-topics.md) for information about the Oracle ACFS plug-in application programming interface

### Oracle ACFS Accelerator Volume

Using an accelerator volume can improve performance by reducing the time to access and update Oracle ACFS metadata. You should create the accelerator volume on a disk group with storage that is significantly faster than the storage of the primary volume. For example, Solid State Disk (SSD) storage could be used. Oracle ADVM volumes are created with the ASMCMD `volcreate` command. For information about the `volcreate` command, refer to [volcreate](manage-advm-asmcmd.md).

The recommended size of the accelerator volume depends on the workload. It is especially helpful for files with many extents, especially if that extent metadata is updated frequently. You can use the `acfsutil` `info` `file` command to view a report on a file's extents. Database files generally have many extents and when Oracle ACFS snapshots are in use, the extent metadata is updated frequently. A workload that greatly benefits from an accelerator is a compressed file system.

If Oracle ACFS cannot allocate space on the accelerator for critical metadata, then that metadata is stored on the primary volume instead. Depending on the frequency of metadata updates, it can have a disproportionate impact on performance. If the slow metadata is written in the same transaction as the fast metadata, then the slow metadata brings the performance of the entire operation down.

The recommended starting accelerator size is minimally 0.6% of the size of the file system. If many snapshots are in use representing several points in time for a database workload, the recommendation is an additional 0.4% per snapshot. For example, a file system with 5 snapshots may need an accelerator whose size is 2.6% of the size of the primary volume. `acfsutil` `size` can be configured to automatically grow the accelerator as needed along with the primary volume. The accelerator increases in units of 64 mega bytes. The minimum size of the accelerator volume is 256 M. `mkfs` requires that the initial accelerator size be at least 0.4% of the size of the primary volume

The accelerator volume is linked to the primary volume specified with the `mkfs` command. When mounting a file system, only the primary volume is specified. If the accelerator volume becomes inaccessible for any reason after a file system with the volume is mounted, then the file system is taken offline. Only one storage accelerator volume can be associated with an Oracle ACFS file system. After an accelerator volume is associated with a file system, the volume cannot be disassociated from the file system.

The accelerator volume can be created on Linux environments with the `-a` option of the `mkfs` command. To create an accelerator volume on Linux, the value of `COMPATIBLE.ADVM` must be at least `12.2`. For information about the commands used to manage accelerator volumes, refer to:

- [mkfs](acfs-commands-linux.md) for information about creating an accelerator volume
- [acfsutil accel replace](acfs-commands-utilities.md) for information about replacing an existing accelerator volume

### Oracle ACFS NAS Maximum Availability eXtensions

Oracle ACFS NAS Maximum Availability eXtensions (Oracle ACFS NAS MAX) is a set of extensions that provide High Availability Extensions for Common NAS Protocols, such as NFS and SMB.

When using these extensions, the protocol in question is running in high availability mode, enabling the protocol to move between nodes in an Oracle RAC cluster. This functionality provides a way to address a single point of failure for a given protocol, so that if at least one node of the cluster is available, then the protocol is available. In addition to providing for high availability, the extensions provide for integration with common NAS protocols and the Oracle ACFS stack, enabling administrators to easily utilize these protocols without creating additional infrastructure. Note that the Oracle ACFS NAS Maximum Availability eXtensions functionality adds value to existing OS NAS protocol implementations, but does not replace them.

Oracle ACFS High Availability Network File System

High Availability Network File System (HANFS) for Oracle Grid Infrastructure provides uninterrupted service of NFS v2, v3, or v4 exported paths by exposing NFS exports on Highly Available Virtual IPs (HAVIP) and using Oracle Clusterware agents to ensure that the VIPs and NFS exports are always online. While base NFS supports file locking, HANFS does not support NFS file locking, except with NFS v4. Refer to Oracle ACFS HANFS with NFS Locks.

Note:

- This functionality relies on a working NFS server configuration available on the host computer. You must configure the NFS server before attempting to use the Oracle ACFS NFS export functionality.
- This functionality is not supported in Oracle Restart configurations.
- The HAVIP cannot be started until at least one file system export resource has been created for it.

To set up High Availability NFS for Oracle Grid Infrastructure, perform the following steps:

1. Add and register a new HAVIP resource.
	For example:
	```
	# srvctl add havip -id hrexports -address my_havip_name
	```
	In the example, `my_havip_name` is mapped in the domain name server (DNS) to the VIP address and is used by the client systems when mounting the file system.
	The initial processing of `srvctl` `add` `havip` ensures that:
	- The address being used is static, not dynamic
		- Any DNS names resolve to only one host, not round-robin multiple DNS resolutions
		- The network resource and provided IP address and resolved name are in the same subnet
		- The name is not in use
	SRVCTL creates the appropriate HAVIP name using the `id`, ensuring it is unique. As a final validation step, SRVCTL ensures that the `network` resource (if provided) of `ora.net#.network` exists. After this step, SRVCTL adds a new `havip` of type `ora.havip.type` with the name of `ora.``id``.havip`. In this example, the name is `ora.``hrexports``.havip`.
	Next SRVCTL modifies HAVIP start dependencies, such as `active` `dispersion`; sets the stop dependencies; and ensures the `description` attribute (if provided) is appropriately set.
2. Create a shared Oracle ACFS file system.
	High Availability NFS for Oracle Grid Infrastructure operates only with Oracle ACFS file systems configured for clusterwide accessibility and does not support Oracle ACFS file systems configured for access on particular subsets of cluster nodes. High Availability NFS is not supported with non-Oracle ACFS file systems.
3. Register the Oracle ACFS file system.
	For example:
	```
	$ srvctl add filesystem -device /dev/asm/d1volume1-295 -volume VOLUME1 \
	  -diskgroup HR_DATA -mountpath /oracle/cluster1/acfs1
	```
4. Create an Oracle ACFS file system export resource.
	For example:
	```
	# srvctl add exportfs -id hrexports -path /oracle/cluster1/acfs1 -name hrexport1
	```
	After the file system export resource has been created, then you can start the HAVIP created in step 1 to export the file system using the `srvctl` `start` `havip` command.
	The NFS mount option FSID is added to any export options, utilizing the FSID of the underlying Oracle ACFS file system plus a unique identifier. This FSID option provides for reliable fail over between nodes and allows the usage of snapshot mounting.
	The default mount and export options for configured exports are the defaults for the NFS server.
	Relative paths that are fully-qualified are converted to absolute paths. Relative paths that are not fully-qualified are not accepted as an export path.
	VIPs attempts to find the best server to run on based on available file systems and other running VIPs, but this dispersion only occurs during CSS membership change events, such as a node joining or leaving the cluster.
	Note:
	It is not recommended to start and stop exports individually; this functionality should be provided through the start and stop operations of HAVIP.
	When HAVIP is not running, exports can exist on different nodes. After the associated HAVIP is started, the exports gather on a single node.
	Clients that are using an export that is stopped while HAVIP is running raise the NFS error `estale`, and must dismount and remount the file system.
	When mounting an HANFS exported file system on a client, the following `CLIENT` mount options are recommended:
	```
	hard,intr,retrans=10000
	```

Oracle ACFS HANFS with NFS Locks

Oracle ACFS HANFS now supports HANFS NFS v4 with NFS Locks. This functionality is only available on specific operating system (OS) platforms. To activate this functionality, additional steps must be performed after the Oracle Grid Infrastructure software is installed. Note that after these steps are completed, the OS NFS server functionality of the cluster is managed by the Oracle Clusterware stack. In addition, the location of certain OS NFS configuration files will be moved from their default location to a designated Oracle ACFS file system.

Some common tasks are:

- Activate:` acfshanfs addnode`
- Uninstall: `acfshanfs uninstall`
- Check the installation status: `acfshanfs installed`
- Check if this platform is supported: `acfshanfs supported`

When activating the HANFS v4 lock functionality, the following command must be run on each node:

```
# grid_home/bin/acfshanfs addnode -nfsv4lock -volume volume_device
```

The volume is formatted with an Oracle ACFS file system and mounted on a designated Oracle ACFS clusterware mount point For example on Linux:

```
/dev/asm/nfs-81 on /var/lib/nfs type acfs (rw)
```

Restrictions on the Oracle ADVM volume include:

- No previously existing Oracle ACFS resource should exist for this new Oracle ADVM volume.
- No Oracle ACFS file system should exist on this Oracle ADVM volume.
- This Oracle ADVM volume should not be in use anywhere in the cluster.

When Oracle HANFS v4 lock functionality is activated, there are differences from normal HANFS operations. The differences are noted in the following list:

- The OS NFS server is under Oracle Clusterware control through the `ora.netstorageservice` resource. When starting and stopping the Oracle Clusterware stack, the OS NFS server is also started and stopped.
- This resource has a dependency on an Oracle ACFS file system: `ora.data_hostname.nfs.acfs`
	The hostname is the hostname of the first node on which the setup for Oracle HANFS locking has been run.
- Only Oracle HANFS should be used to export NFS file systems from the Oracle RAC cluster. The NFS server is configured and moved around the Oracle RAC cluster; only file systems exported by Oracle HANFS are accessible when the NFS server has migrated to an alternate cluster node.
- When locking is initialized, Oracle HANFS exports are run from only a single node, unlike non-locking mode, where Oracle HANFS exports are distributed throughout the cluster.
- On client nodes, mount the file system specifying NFS v4 as the NFS version. This prevents the server from defaulting to NFS v3, and enables support for the NFS v4 locking functionality.

After High Availability Locking is activated, control of HANFS with locking is the same as described previously in this section.

Oracle ACFS HANFS with High Availability SMB

Oracle ACFS supports High Availability Samba (SMB), also known as CIFS (Common Internet File System) in previous Microsoft implementations. This protocol is commonly used to interface with Microsoft servers and Active Directory Domains and is supported by various operating system (OS) implementations. However, Oracle ACFS High Availability SMB requires the Microsoft SMB implementation or Samba.

Note the following:

- Samba is available from www.samba.org
- Ensure that Samba or SMB is correctly configured on your host OS before attempting to utilize High Availability SMB.
- High Availability SMB is not supported in Oracle Restart mode.
- After adding an HAVIP resource, an SMB Export resource must also be added; otherwise, the HAVIP resource does not start.
- For highest performance and best results, ensure that both server and client are using SMB3. Note the following:
	- Use the newest version of Samba, v4 or later.
		- Use the latest Microsoft OS version (2012 or later). To check the SMB version, use the Powershell `cmdlet Get-SmbConnection` command.
		- Previous versions of SMB require that the client must remount the SMB export after a storage failure.
- Similar to HANFS, options may be specified on the command line and are passed to the host operating system. Appropriate error messages are passed back. If no options are provided to the SRVCTL command, the following default options apply:
	- Linux, Solaris, and AIX: Read Only, Browsable = True
- Supported Option Sets:
	- Linux, Solaris, or AIX: Any options supported by the Samba configuration stanza.

To set up High Availability SMB for Oracle Grid Infrastructure, perform the following steps:

1. Add and register a new HAVIP resource.
	For example:
	```
	# srvctl add havip -id hrexports -address my_havip_name
	```
	In the example, `my_havip_name` is mapped in the domain name server (DNS) to the VIP address and is used by the client systems when mounting the file system.
	The initial processing of `srvctl` `add` `havip` ensures that:
	- The address being used is static, not dynamic
		- Any DNS names resolve to only one host, not round-robin multiple DNS resolutions
		- The network resource and provided IP address and resolved name are in the same subnet
		- The name is not in use
	SRVCTL creates the appropriate HAVIP name using the `id`, ensuring it is unique. As a final validation step, SRVCTL ensures that the `network` resource (if provided) of `ora.net#.network` exists. After this step, SRVCTL adds a new `havip` of type `ora.havip.type` with the name of `ora.``id``.havip`. In this example, the name is `ora.``hrexports``.havip`.
	Next SRVCTL modifies HAVIP start dependencies, such as `active` `dispersion`; sets the stop dependencies; and ensures the `description` attribute (if provided) is appropriately set.
2. Create a shared Oracle ACFS file system.
	High Availability SMB for Oracle Grid Infrastructure operates only with Oracle ACFS file systems configured for clusterwide accessibility and does not support Oracle ACFS file systems configured for access on particular subsets of cluster nodes. High Availability NFS is not supported with non-Oracle ACFS file systems.
3. Register the Oracle ACFS file system.
	For example:
	```
	$ srvctl add filesystem -device /dev/asm/d1volume1-295 -volume VOLUME1 \
	  -diskgroup HR_DATA -mountpath /oracle/cluster1/acfs1
	```
4. Create an Oracle ACFS file system export resource.
	For example:
	```
	# srvctl add exportfs -id hrexports -path /oracle/cluster1/acfs1 -name hrexport1 –type SMB
	```
	After the file system export resource has been created, then you can start the HAVIP created in step 1 to export the file system using the `srvctl` `start` `havip` command.
	During the start of the resource, the Oracle ACFS Export resource creates a Samba configuration file (Linux, Solaris, or AIX) or runs the `net.exe` binary to export the file system.
	VIPs attempts to find the best server to run on based on available file systems and other running VIPs, but this operation only occurs during CSS membership change events, such as a node joining or leaving the cluster.
	Note:
	- It is not recommended to start and stop exports individually; this functionality should be provided through the start and stop operations of HAVIP.
	- When HAVIP is not running, exports can exist on different nodes. After the associated HAVIP is started, the exports gather on a single node.

See Also:

- [Creating an Oracle ACFS File System](steps-manage-acfs.md) for information about creating an Oracle ACFS file system
- [Oracle Clusterware Administration and Deployment Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/acfsg&id=CWADD-GUID-BF490C0F-C9AA-4A90-8DCD-B5A047AE9BBF) for information about the `srvctl` `add` `filesystem` command
- [Oracle Clusterware Administration and Deployment Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/acfsg&id=CWADD-GUID-58F85575-7D88-4D45-B097-6274FBBBB646) for information about Oracle Clusterware resources
- [Oracle Clusterware Administration and Deployment Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/acfsg&id=CWADD-GUID-1DCA9E3F-B929-4555-B673-921FF3588AC3) and [Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/acfsg&id=RACAD-GUID-2D617A25-0E8E-4B3E-95AA-8AD26DA12DF2) for information about SRVCTL commands