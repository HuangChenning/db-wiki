---
title: Oracle ACFS Advanced Topics
book: "Automatic Storage Management Administrator's Guide"
doc_id: E18951-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e18951/asmfs_extra.htm
tags:
  - oracle
  - 11g
  - automatic-storage-management-administrators-guide
---

## B Oracle ACFS Advanced Topics

This appendix discusses limits, advanced administration, and troubleshooting for Oracle Automatic Storage Management Cluster File System (Oracle ACFS).

See Also:

Articles available at My Oracle Support (`https://support.oracle.com`) for information about Oracle ACFS and Oracle ADVM.

This appendix contains the following topics:

For information about Oracle ACFS, see [Chapter 5, "Introduction to Oracle ACFS"](asmfilesystem.md).

## Limits of Oracle ACFS

The limits of Oracle ACFS are discussed in this section.

The topics contained in this section are:

- Oracle ACFS Disk Space Usage
- Oracle ACFS Error Handling
- Oracle ACFS and NFS

Note:

Oracle ACFS does not support hard links on directories.

### Oracle ACFS Disk Space Usage

Oracle ACFS supports 2^40 (1 trillion) files in a file system. More than 4 billion files have been tested. 32-bit Linux systems are limited to 2^26 (67 million) files. Oracle ACFS supports 63 snapshots. These snapshots can be any combination of read-only and read-write. Oracle ACFS supports 64 mounted file systems on 32-bit systems, and 256 mounts on 64-bit systems. However, more file systems can be mounted if there is adequate memory.

Oracle ACFS preallocates large user files to improve performance when writing data. This storage is not returned when the file is closed, but it is returned when the file is deleted. Oracle ACFS also allocates local metadata files as nodes mount the file system for the first time. This can result in a mount failing due to an out of space error, and much of this storage must be contiguous. This storage is approximately 64-128 megabytes per node.

Oracle ACFS also keeps local bitmaps available to reduce contention on the global storage bitmap when searching for free space. This disk space is reported as `in` `use` by tools such as the UNIX `df` command even though some of it may not actually be allocated as of yet. This local storage pool can be as large as 128 megabytes per node and can allow space allocations to succeed, even though commands, such as `df`, report less space available than what is being allocated.

### Oracle ACFS Error Handling

Oracle ASM instance failure or forced shutdown while Oracle ACFS or another file system is using an Oracle ADVM volume results in I/O failures. The volumes must be closed and re-opened to access the volume again. This requires dismounting any file systems that were mounted when the local Oracle ASM instance failed. After the instance is restarted, the corresponding disk group must be mounted with the volume enabled followed by a remount of the file system. See ["Deregistering, Dismounting, and Disabling Volumes and Oracle ACFS File Systems"](asmfs_util001.md).

If any file systems are currently mounted on Oracle ADVM volume files, the `SHUTDOWN` `ABORT` command should not be used to terminate the Oracle ASM instance without first dismounting those file systems. Otherwise, applications encounter I/O errors and Oracle ACFS user data and metadata being written at the time of the termination may not be flushed to storage before the Oracle ASM storage is fenced. If there is not time to permit the file system to dismount, then you should run two `sync` (1) commands to flush cached file system data and metadata to persistent storage before issuing the `SHUTDOWN` `ABORT` operation.

Oracle ACFS does not interrupt the operating system environment when a metadata write fails, whether due to Oracle ASM instance failure or storage failure. Instead, Oracle ACFS isolates errors to an individual file system, putting it in an offline error state. The only operation that succeeds on that node for that file system from that point forward is a dismount operation. Another node recovers any outstanding metadata transactions, assuming it can write the metadata out to the storage. It is possible to remount the file system on the offlined node after the I/O condition is resolved.

It might not be possible for an administrator to dismount a file system while it is in the offline error state if there are processes referencing the file system, such as a directory of the file system being the current working directory for a process. To dismount the file system in this case it would be necessary to identify all processes on that node with references to files and directories on the file system and cause them to exit. The Linux `fuser` or `lsof` commands or Window `handle` command list information about processes and open files.

If Oracle ACFS detects inconsistent file metadata returned from a read operation, based on checksum or expected type comparisons, Oracle ACFS takes the appropriate action to isolate the affected file system components and generate a notification that `fsck` or `acfschkdsk` should be run as soon as possible. Each time the file system is mounted a notification is generated with a system event logger message until `fsck` or `acfschkdsk` is run.

### Oracle ACFS and NFS

When exporting file systems through NFS on Linux, use the `-fsid=num` exports option. This option forces the file system identification portion of the file handle used to communicate with NFS clients to be the specified number instead of a number derived from the major and minor number of the block device on which the file system is mounted. You can use any 32-bit number for `num`, but it must be unique among all the exported file systems. In addition, `num` must be unique among members of the cluster and must be the same `num` on each member of the cluster for a given file system. This is needed because Oracle ASM DVM block device major numbers are not guaranteed to be the same across reboots of the same node or across different nodes in the cluster.

## Limits of Oracle ADVM

The limits of Oracle ADVM and these discussed in this section.

The default configuration for an Oracle ADVM volume is four columns of 64 megabytes (MB) extents in length and a 128 KB stripe width. Oracle ADVM writes data as 128 kilobytes (KB) stripe chunks in round robin fashion to each column and fills a stripe set of four 64 MB extents with 2000 stripe chunks before moving to a second stripe set of four 64 MB extents for volumes greater than 256 MB. Note that setting the number of columns on an Oracle ADVM dynamic volume to 1 effectively turns off striping for the Oracle ADVM volume.

On Linux platforms Oracle ASM Dynamic Volume Manager (Oracle ADVM) volume devices are created as block devices regardless of the configuration of the underlying storage in the Oracle ASM disk group. Do not use `raw` `(8)` to map Oracle ADVM volume block devices into raw volume devices.

## Oracle ACFS Drivers Resource Management

The Oracle ACFS drivers resource is supported only for Oracle Grid Infrastructure cluster configurations; it is not supported for Oracle Restart configurations. See "Oracle ACFS and Oracle Restart".

The Oracle ACFS drivers resource (`ora.drivers.acfs`) is created by the Grid Infrastructure root script that is run following the Grid Infrastructure installation. The Oracle ASM instance resource (`ora.asm`) names the drivers resource as a weak dependency. Consequently, the start action for the drivers resource is also called whenever the start action for the `ora.asm` resource is issued. The start action for the drivers resource includes support for loading the Oracle ACFS, Oracle ADVM, and Oracle Kernel Services Driver (OKS) drivers into the operating system.

Following an Oracle Grid Infrastructure installation on Linux and UNIX platforms, a root script is run that includes actions for copying the Oracle ACFS components; including the Oracle ACFS, OKS, and Oracle ADVM drivers; into operating system-specific locations.

The Oracle ASM instance is started during the Grid Infrastructure installation process whenever Oracle Clusterware Registry (OCR) and the voting files are configured within an Oracle ASM disk group. In that case, the Oracle ACFS drivers are initially loaded during Grid Infrastructure Installation based on the resource dependency. The Oracle ASM instance can also be started using the Oracle ASM Configuration Assistant and the Oracle ACFS drivers are loaded based on that action. In steady state mode, the Oracle ACFS drivers are automatically loaded during Oracle Clusterware initialization when the Oracle High Availability Services Daemon (OHASD) calls the start action for the Oracle ASM instance resource that also results in loading the Oracle ACFS drivers due to the resource dependency relationship. The start action for the Oracle ACFS drivers resource attempts to load the Oracle ACFS, Oracle ADVM, and OKS drivers into the native operating system.

The policy for the Oracle ACFS drivers is that they remain loaded until Oracle Clusterware is shut down. The `ora.drivers.acfs` resource is managed automatically by Oracle High Availability Services Daemon (OHASD) and its state cannot be manually manipulated by `srvctl` or `crsctl`.

## Oracle ACFS Registry Resource Management

The Oracle ACFS registry resource is supported only for Oracle Grid Infrastructure cluster configurations; it is not supported for Oracle Restart configurations. See "Oracle ACFS and Oracle Restart".

The Oracle ACFS registry resource (`ora.registry.acfs`) is created by the root script that is run following Grid Infrastructure installation. The start action for the Oracle ACFS mount registry resource is automatically called during Grid Infrastructure initialization to activate the local node state of the clusterwide Oracle ACFS mount registry. If this initialization is successful, the state of this resource is set to `online`; otherwise, the state of the resource is set to `offline`. The state of the Oracle ACFS registry resource is determined only by the active state of the mount registry. The `online` status is independent of any registry contents or the current state of any individual registered file systems that may exist within the Oracle ACFS registry.

In addition to activating the local node state of the mount registry, the Oracle ACFS registry resource start action assists in establishing a clusterwide Oracle ACFS file name space. On each node, the resource start action scans the contents of the clusterwide mount registry and mounts any file systems designated for mounting on the local cluster member. Before mounting a registered file system, the resource start action confirms that the associated file system storage stack is active and will mount the disk group, enable the volume file, and create the mount point if necessary to complete the mount operation.

The check action for the Oracle ACFS registry resource assists in maintaining the clusterwide Oracle ACFS file system name space. On each node, the check action scans the contents of the mount registry for newly created entries and mounts any Oracle ACFS file systems registered for mounting on the local node. Consequently, a new Oracle ACFS file system can be created and registered on one node of the cluster, and is automatically mounted on all cluster members designated by the Oracle ACFS registry entry.

The Oracle ACFS registry resource check action also assists with file system recoveries. Recovering a file system from an offline state requires dismounting and remounting the file system. As the Oracle ACFS registry resource check action scans the mount registry searching for newly created file systems, it also checks for any offline file systems on the local node and if found, attempts to dismount and remount each offline file system. If the remount is successful, the file system transitions from offline to fully active status.

The Oracle ACFS registry resource stop action is usually called during the Grid Infrastructure shutdown sequence of operations. To transition the registry resource to an offline state, all file systems on this cluster member that are configured with Oracle ADVM devices must be dismounted. A mounted file system maintains an open reference on its Oracle ADVM device special file and associated dynamic volume file that must be closed before the Oracle ASM instance can be shutdown normally. The registry resource stop action scans the operating system's internal mount table searching for any mounted file system that is configured with an Oracle ADVM device file. If any is found, the stop action attempts to dismount that file system. However, if there are open references resulting from applications or users of that file system, then the file system cannot be dismounted until these are closed. If the dismount operation fails, the process IDs of any processes holding an open reference on the file system are displayed and logged to enable the administrator to resolve the open references and dismount the file systems. The internal mount table entries can include registered and unregistered Oracle ACFS file systems, and other local file systems that were mounted on an Oracle ADVM device file.

The Oracle ACFS registry resource clean action is called implicitly if the resource stop action fails to transition the resource to the offline state. In that case, the registry resource clean action can be called to effectively force the resource offline. The registry resource clean action scans the operating system internal mount table searching for any file system that is mounted upon an Oracle ADVM device. If any is found, the resource clean action attempts to `umount` the file system as in the resource stop action. However, if there are open references that prevent the file system from being dismounted, the clean resource action displays and logs the Process Identifiers of any process holding a reference, terminates the referencing processes, and then dismounts the file system. At the completion of the clean action, the registry resource is set to an offline state and other participants in the Grid Infrastructure shutdown sequence can now be stopped.

Whenever Oracle Clusterware is started on a cluster node, the Oracle ACFS startup operations for the node consult the cluster mount registry and attempt to mount all Oracle ACFS file systems that are registered for this node. Following each file system addition to the mount registry, the newly registered file system is automatically mounted on each node designated by the registry entry. If a registered file system is automatically mounted and is later dismounted, it is not automatically remounted until the system is rebooted or Oracle Clusterware is restarted. It can be manually remounted using the `mount` command or Oracle Enterprise Manager.

The Oracle ACFS cluster mount registry action routines attempt to mount each Oracle ACFS file system on its registered mount point and create the mount point if it does not exist. The registry action routines also mount any Oracle ASM disk groups and enable any Oracle ADVM volumes required to support the Oracle ACFS mount operation. In the event that a file system enters into an offline error state, the registry action routines attempt to recover the file system and return it to an on-line state by dismounting and remounting the file system. For information about the offline error state, see ["About Oracle ACFS Integration with Oracle ASM"](asmfilesystem.md).

## Oracle ACFS Individual File System Resource Management

The Oracle ACFS individual file system resource is supported only for Oracle Grid Infrastructure cluster configurations; it is not supported for Oracle Restart configurations. See "Oracle ACFS and Oracle Restart".

Oracle ASM Configuration Assistant (ASMCA) facilitates the creation of Oracle ACFS individual file system resources (`ora.``diskgroup``.``volume``.acfs`). During database creation with Database Configuration Assistant (DBCA), the individual file system resource is included in the dependency list of its associated disk group so that stopping the disk group also attempts to stop any dependent Oracle ACFS file systems.

An Oracle ACFS individual file system resource is typically created for use with application resource dependency lists. For example, if an Oracle ACFS file system is configured for use as an Oracle Database home, then a resource created for the file system can be included in the resource dependency list of the Oracle Database application. This dependency causes the file system and stack to be automatically mounted due to the start action of the database application.

An Oracle ACFS file system that is to be mounted from a dependency action should not be included in the Oracle ACFS mount registry.

The start action for an Oracle ACFS individual file system resource is to mount the file system. This individual file system resource action includes confirming that the associated file system storage stack is active and mounting the disk group, enabling the volume file, and creating the mount point if necessary to complete the mount operation. If the file system is successfully mounted, the state of the resource is set to `online`; otherwise, it is set to `offline`.

The check action for an individual file system resource verifies that the file system is mounted. It sets the state of the resource to `online` status if mounted, otherwise the status is set to `offline`.

The stop action for an Oracle ACFS individual file system resource attempts to dismount the file system. If the file system cannot be dismounted due to open references, the stop action displays and logs the process identifiers for any processes holding a reference.

Use of the `srvctl` `start` and `stop` actions to manage the individual file system resources maintains their correct resource state.

## Oracle ACFS and Oracle Restart

Oracle Restart does not support root-based Oracle ACFS resources for this release. Consequently, the following operations are not automatically performed:

- Loading Oracle ACFS drivers
- Mounting Oracle ACFS file systems listed in the Oracle ACFS mount registry
- Mounting resource-based Oracle ACFS database home file systems

The Oracle ACFS resources associated with these actions are not created for Oracle Restart configurations.

While Oracle ACFS resource management is fully supported for Oracle Grid Infrastructure configurations, the Oracle ACFS resource-based management actions must be replaced with alternative, sometimes manual, operations in Oracle Restart configurations.

## Understanding Oracle ACFS I/O Failure Console Messages

Oracle ACFS logs information for I/O failures in the operating-specific system event log.

A console message has the following format:

```
[Oracle ACFS]: I/O failure (error_code) with device device_name during a operation_name op_type.
file_entry_num Starting offset: offset. Length of data transfer: io_length bytes.
Impact: acfs_type   Object: object_type   Oper.Context: operation_context 
Snapshot?: yes_or_no AcfsObjectID: acfs_object_id . Internal ACFS Location: code_location.
```

The italicized variables in the console message syntax correspond to the following:

- I/O failure
	The operating system specific error code, in Hex, seen by Oracle ACFS for a failed I/O. This may indicate a hardware problem, or it might indicate a failure to initiate the I/O for some other reason.
- Device
	The device involved, usually the ADVM device file, but under some circumstances it might be a string indicating the device minor number
- Operation name
	The kind of operation involved:
	`user` `data`, `metadata`, or `paging`
- Operation type
	The type of operation involved:
	`synch` `read`, `synch` `write`, `asynch` `read`, or `asynch` `write`
- File entry number
	The Oracle ACFS File entry number of the file system object involved, as a decimal number. The `acfsutil` `info` `fileid` tool finds the corresponding file name.
- Offset
	The disk offset of the I/O, as a decimal number.
- Length of I/O
	The length of the I/O in bytes, as decimal number.
- File system object impacted
	An indication that the file system object involved is either node-local, or is a resource accessed clusterwide. For example:
	`Node` or `Cluster`
- Type of object impacted
	A string indicating the kind of file system object involved, when possible. For example:
	`Unknown`, `User` `Dir.`, `User` `Symlink`, `User` `File`, `Sys.Dir`, `Sys.File`, or `MetaData`
	- `Sys.Dir.`
		Oracle ACFS-administered directory within the visible namespace
		- `sys.File`
		Oracle ACFS-administered file within the visible namespace
		- `MetaData`
		Oracle ACFS-administered resources outside of the visible namespace
- Operational context
	A higher-level view of what code context was issuing the I/O. This is for use by Oracle Support Services. For example:
	`Unknown`, `Read`, `Write`, `Grow`, `Shrink`, `Commit`, or `Recovery`
- Snapshot
	An indication of whether, if possible to determine, the data involved was from a Snapshot. For example:
	`Yes`, `No`, or `?`
- Object type of the file system
	An internal identifier for the type of file system object. For use by Oracle Support Services.
- Location of the code
	An internal identifier of the code location issuing this message. For use by Oracle Support Services.

The following is an example from `/var/log/messages` in a Linux environment:

```
[Oracle ACFS]: I/O failure (0xc0000001) with device /dev/sdb during a metadata synch write .
Fenum Unknown. Starting offset: 67113984. Length of data transfer: 2560 bytes.
Impact: Node   Object: MetaData   Oper.Context: Write
Snapshot?: ?  AcfsObjectID: 8  . Internal ACFS Location: 5 .
```