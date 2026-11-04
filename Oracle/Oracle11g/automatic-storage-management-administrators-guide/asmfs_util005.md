---
title: Oracle ACFS Command-line Tools for Windows Environments
book: "Automatic Storage Management Administrator's Guide"
doc_id: E18951-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e18951/asmfs_util005.htm
tags:
  - oracle
  - 11g
  - automatic-storage-management-administrators-guide
---

Table 13-16 contains a summary of the Oracle ACFS file system commands for Windows. These commands have been extended to support Oracle ACFS. All other Windows file system commands operate without change for Oracle ACFS.

Table 13-16 Summary of Oracle ACFS file system commands for Windows

| Command | Description |
| --- | --- |
| acfschkdsk | Checks and repairs an Oracle ACFS file system on Windows. |
| acfsdismount | Dismounts an Oracle ACFS on Windows. |
| acfsformat | Creates an Oracle ACFS file system on Windows. |
| acfsmountvol | Mounts an Oracle ACFS file system on Windows. |
| acfsutil detach | Prepares the Oracle ACFS driver for module unload on Windows. |

Table 13-17 contains a summary of the non-Oracle ACFS file system commands for Windows.

Table 13-17 Summary of Non-Oracle ACFS file system commands for Windows

| Command | Description |
| --- | --- |
| advmutil dismount | Dismounts Oracle ASM volume devices for file systems that are not Oracle ACFS on Windows. |
| advmutil list | Lists Oracle ASM volume devices for file systems that are not Oracle ACFS on Windows. |
| advmutil mount | Mounts Oracle ASM volume devices for file systems that are not Oracle ACFS on Windows. |

## acfschkdsk

Purpose

Checks and repairs an Oracle ACFS file system.

Syntax and Description

  
`acfschkdsk` `/h`  
`acfschkdsk` \[`/a` | `/f`\] \[`/v`\] \[`/vv`\] \[`/n` | `/y`\] `volume_device`  

Table 13-18 contains the options available with the `acfschkdsk` command.

Table 13-18 Options for the acfschkdsk command

| Option | Description |
| --- | --- |
| `/a` | Specifies to automatically repair the file system. |
| `/f` | Forces the file system into mountable state without completing a file system check or repair. |
| `/v` | Specifies verbose mode. The progress is displayed as the operation occurs. |
| `/vv` | Specifies very verbose mode. The progress is displayed as the operation occurs. |
| `/h` | Displays the usage help text and exits. |
| `/n` | Answers no to any prompts. |
| `/y` | Answers yes to any prompts. |
| `volume_device` | Specifies the Oracle ADVM volume device. |

`acfschkdsk` checks and repairs an existing Oracle ACFS. This command can only be run on a file system that has been dismounted clusterwide.

The Oracle ACFS driver must be loaded for `acfschkdsk` to work. If the driver is not loaded, the administrator is prompted to ensure this is intentional. For information about loading drivers, see ["Oracle ACFS Drivers Resource Management"](asmfs_extra.md).

The Oracle ACFS driver normally ensures that `acfschkdsk` is the only user of the file system clusterwide. In extreme cases it may be necessary to fix a file system without loading the driver if the file system automount causes the system to fail. The verifications that are normally done by the driver for exclusive access are bypassed in this case.

By default `acfschkdsk` only checks for and only reports errors. The `/a` flag must be specified to instruct `acfschkdsk` to repair errors in the file system.

In a few cases, `acfschkdsk` prompts for questions before proceeding to check a file system. For example, if `acfschkdsk` detects that another `acfschkdsk` is in progress on the file system, or if `acfschkdsk` detects that the Oracle ACFS driver is not loaded, or if the file system does not appear to be Oracle ACFS. In checking mode, `acfschkdsk` also prompts if there are transaction logs that have not been processed completely due to an incomplete shutdown. To run in a non-interactive mode, include either the `/y` or `/n` options to answer yes or no to any questions.

`acfschkdsk` creates working files before it checks a file system. These working files are created in the `temp` directory if space is available. If insufficient space is available, `acfschkdsk` attempts to write in the current working directory. The files `acfschkdsk` creates are roughly the size of the file system being checked divided by 32K. At most two files are allocated. These files are deleted when `acfschkdsk` has finished.

In the event that `acfschkdsk` finds a file or directory in the file system for which it cannot determine its name or intended location (possibly due to a corruption in its parent directory), it places this object in the `\lost+found` directory when `acfschkdsk` is run in fix mode. For security reasons, only the Windows `Administrator` can read files in `\lost+found`. If the administrator can later determine the original name and location of the file based on its contents, the file can be moved or copied into its intended location.

The file names in the `\lost+found` directory are in the following formats:

```
parent.id.file.id.time-in-sec-since-1970
parent.id.dir.id.time-in-sec-since-1970
```

The `id` fields are the internal Oracle ACFS numeric identifiers for each file and directory in the file system.

You can use `acfsutil` `info` `id` `id` `mount_point` to attempt to determine the directory associated with `parent.``id`. This directory is assumed to be where the deleted object originated. For information about `acfsutil` `info`, see ["acfsutil info file"](asmfs_util010.md).

If the parent directory is not known, the parent `id` field is set to `UNKNOWN`.

Note:

It is not possible to see the contents of the `\lost+found` directory from a snapshot.

Examples

The following example shows how to check an Oracle ACFS file system on Windows. The verbose mode is enabled in this example.

Example 13-13 Using the acfschkdsk command

```
C:\> acfschkdsk /v asm-volume1-311
```

## acfsdismount

Purpose

Dismounts an Oracle ACFS file system and removes its mount point (name space attachment).

Syntax and Description

  
`acfsdismount` `/h`  
`acfsdismount` \[`/v`\] { `drive_letter` | `mount_point` }  
`acfsdismount` \[`/v`\] `/all`  

Table 13-19 contains the options available with the `acfsdismount` command.

Table 13-19 Options for the acfsdismount command

| Option | Description |
| --- | --- |
| `/v` | Specifies verbose mode. The progress is displayed as the operation occurs. |
| `/h` | Displays help text and exits. |
| `/all` | Specifies to dismount all Oracle ACFS file systems on this node. |
| `drive_letter` | Specifies the drive letter followed by a colon. |
| `mount_point` | Specifies the full path of the mount point including the drive letter. |

`acfsdismount` removes the mount point (name space attachment) for the specified file system on the current node and dismounts the file system if it is mounted. When the file system is in the dismounted state, the data is preserved on the device and the file system can be re-mounted with the `acfsmountvol` command.

Windows Administrator privileges are required to use the `acfsdismount` command.

Examples

The following examples show how to dismount an Oracle ACFS file system. The first example dismounts a file system using only the drive letter. The second example dismounts a file system using the full path name. The third examples dismounts all mounted file systems. All the examples enable the verbose mode.

Example 13-14 Using the acfsdismount command

```
C:\> acfsdismount /v O:

C:\> acfsdismount /v O:\mnt\

C:\oracle>acfsdismount /v /all
acfsdismount: valid path name: C:\oracle\acfsmounts\acfs1\
acfsdismount: opening handle to volume C:\oracle\acfsmounts\acfs1
acfsdismount: locking volume C:\oracle\acfsmounts\acfs1
acfsdismount: dismounting volume C:\oracle\acfsmounts\acfs1
acfsdismount: removing volume mount point on C:\oracle\acfsmounts\acfs1\
acfsdismount: closing handle to volume C:\oracle\acfsmounts\acfs1 and exiting cleanly
```

## acfsformat

Purpose

Creates an Oracle ACFS file system.

Syntax and Description

  
`acfsformat` `/h`  
`acfsformat` \[`/v`\] \[`/f`\] \[`/b` `blocksize`\] \[`/n` `name`\] `volume_device` \[`blocks`\]  

Table 13-20 contains the options available with the `acfsformat` command.

Table 13-20 Options for the acfsformat command

| Option | Description |
| --- | --- |
| `/v` | Specifies verbose mode. The progress is displayed as the operation occurs. |
| `/n` `name` | Specifies the name for the file system. This is also known as a volume label. `acfsutil` `info` `fs` returns the name if one was specified. This can also be displayed from the `VOL_LABEL` column in the `V$ASM_ACFSVOLUMES` view. |
| `/f` | Specifies the force option. This action creates the file system even if there is an existing Oracle ACFS on the device, although only if the file system is dismounted. This option overwrites structures on the original file system. Use this option with caution. |
| `/h` | Displays the usage help text. |
| `/b` `blocksize` | The default block size is 4K and this is the only size supported in 11g Release 2 11.2). |
| `blocks` | Specifies the number of blocks that the file system should consume on the named device. The quantity specified can be in units of `K` (kilobytes), `M` (megabytes), `G` (gigabytes), or `T` (terabytes). If a unit is not specified, the default is bytes. If number of blocks specified is not a multiple of the block size, than the value is rounded up to the closest multiple. If this option is not specified, the entire device is consumed. |
| `volume_device` | Specifies an Oracle ADVM device file to be formatted. |

`acfsformat` creates the on disk structure needed for Oracle ACFS to be mounted. `acfsformat` performs a quick format on the target volume. After `acfsformat` runs successfully, the `USAGE` column in the `V$ASM_VOLUME` view displays `ACFS`.

Windows Administrator privileges are not required to use this command. The minimum file system size is 200 MB. The Oracle ACFS driver must be loaded for `acfsformat` to work.

Examples

This example shows how to create an Oracle ACFS file system. The verbose option is specified in this example.

Example 13-15 Using the acfsformat command

```
C:\> acfsformat /v asm-volume1-311
```

## acfsmountvol

Purpose

Mounts an Oracle ACFS file system.

Syntax and Description

  
`acfsmountvol` `/h`  
`acfsmountvol`  
`acfsmountvol` \[`/v`\] `/all`  
`acfsmountvol` \[`/v`\] { `drive_letter` | `dir` } `volume_device`  

Table 13-21 contains the options available with the `acfsmountvol` command.

Table 13-21 Options for the acfsmountvol command

| Option | Description |
| --- | --- |
| `/v` | Specifies verbose mode. The progress is displayed as the operation occurs. |
| `/h` | Displays the help usage text and exits. |
| `/all` | Reads the ACFS mount registry created with `acfsutil` `registry` and mounts the file systems listed in it on this node. |
| `drive_letter` | The Windows drive letter to link to an Oracle ADVM volume device. |
| `dir` | Specifies the full directory of the mount point including the drive letter. |
| `volume_device` | Specifies an Oracle ADVM volume device file that has been formatted by `acfsformat`. |

`acfsmountvol` attaches an Oracle ACFS to the file system hierarchy at the specified path name or drive letter. `dir` must be an empty directory. Oracle ACFS mount points can be created on any empty directory and they can be hierarchical (nested).

After `acfsmountvol` runs successfully, the `MOUNTPATH` column in the `V$ASM_VOLUME` view displays the full path or drive letter on which the file system is now mounted. If no arguments are specified, the command lists all mounted Oracle ACFS file systems on this node.

It is not always possible to return the cause of a mount failure to the `acfsmountvol` command. When this happens Oracle ACFS writes the cause of the failure to the Windows system event logger.

An Oracle ACFS file system should only be mounted on one mount point. The same mount point name should be used on all cluster members.

Windows Administrator privileges are required to mount an Oracle ACFS.

Examples

The first example shows how to mount `asm-volume1-311` on the mount point identified as the `F:` drive. The second example shows how to mount `asm-volume1-215` on the mount point specified by `c:\oracle\acfsmounts\acfs1\`. The first two examples enable verbose mode. The third example lists all the mounted file systems on the node.

Example 13-16 Using the acfsmountvol command

```
C:\> acfsmountvol  /v  F:  asm-volume1-215

C:\> acfsmountvol /v  c:\oracle\acfsmounts\acfs1  asm-volume1-311

C:\oracle>acfsmountvol
   asm-volume1-311
       C:\oracle\acfsmounts\acfs1
```

## acfsutil detach

Purpose

Prepares the Oracle ACFS driver for module unload.

Syntax and Description

`acfsutil` `detach`

`acfsutil` `detach` prepares Oracle ACFS for having its driver unloaded. Oracle ACFS registers itself as a base file system upon driver load. In order for the Windows service control manager to send a stop command to the driver, Oracle ACFS must unregister itself as a base file system in addition to deleting any device objects associated with the driver.

After `acfsutil` `detach` has completed successfully, and all volumes have been dismounted, then the administrator can run the Windows service control manager's stop command to the Oracle ACFS driver. If the `acfsutil` `detach` command is not used, then the `stop` command does not call the Oracle ACFS driver unload routine. This command can only be run by the Windows `Administrator`. It is called automatically by the Oracle ACFS shutdown scripts.

Examples

The following examples show how to detach all Oracle ACFS file systems and unload drivers on Windows. The first example dismounts all the Oracle ACFS file systems volume devices. The second example detaches the volume devices.

Example 13-17 Using the acfsutil detach command

```
C:\> acfsdismount /all

C:\> acfsutil detach
```

## advmutil dismount

Purpose

The `advmutil` `dismount` command dismounts Oracle ADVM volume devices for file systems that are not Oracle ACFS.

Syntax and Description

  
`advmutil` `dismount` \[`/unregister`\] { `drive_letter` | `dir` }  
`advmutil` `dismount` \[`/unregister`\] \[`/all` | `/dg=` `disk_group`\]  

Table 13-22 contains the options available with the Windows `advmutil` `dismount` command.

Table 13-22 Options for the advmutil dismount command

| Option | Description |
| --- | --- |
| `drive_letter` | Specifies the drive letter to dismount. |
| `dir` | Specifies the directory of the mount point, including the drive letter. |
| `/a` ll | Specifies to dismount all file systems on this node. |
| `/unregister` | Optionally unregister an Oracle ADVM volume device and its drive letter from the system registry. Upon startup of the Oracle ASM instance and Oracle ACFS, the unregistered drive letter and Oracle ADVM volume symbolic links are not created. |
| `/dg=` `disk_group` | Optional name of the disk group containing the registered Oracle ADVM volume devices to create drive letters or possibly mount or dismount file systems. |

Note:

To format an Oracle ADVM volume device with NTFS, it must be mounted on a drive letter. After formatting, Oracle ADVM volume devices with NTFS can be mounted on either a drive letter or a directory.

To successfully run this command, the local Oracle ASM instance must be running and the disk groups required by this command must have been created and mounted in the Oracle ASM instance and volumes enabled.

Examples

These examples show how to dismount a file system that is not Oracle ACFS.

1. The first example shows how to remove a drive letter for an Oracle ADVM volume device which disallows access to the file system.
2. The second example shows how to remove a drive letter for an Oracle ADVM volume device which disallows access to the file system and removes it from the registry.
3. The third example shows how to remove a drive letter for all registered Oracle ADVM volume devices which disallows access to all file systems.
4. The fourth example shows how to remove a drive letter for all registered Oracle ADVM volume devices in a particular Oracle ASM disk group which disallows access to all related file systems.

Example 13-18 Using the advmutil dismount command

```
C:\> advmutil dismount H:

C:\> advmutil dismount H: /unregister

C:\> advmutil dismount /all

C:\> advmutil dismount /dg=data
```

## advmutil list

Purpose

The `advmutil` `list` command lists the Oracle ADVM volume devices that were registered with `advmutil` `mount` `/register.`

Syntax and Description

  
`advmutil` `list` `/registry`  

Table 13-23 contains the options available with the Windows `advmutil` `list` command.

Table 13-23 Options for the advmutil list command

| Option | Description |
| --- | --- |
| `list` `/registry` | Lists the drive letter and corresponding Oracle ADVM volume device name contained in the Windows registry. |

To successfully run this command, the local Oracle ASM instance must be running and the disk groups required by this command must have been created and mounted in the Oracle ASM instance and volumes enabled.

For information about listing Oracle ADVM volume devices for Oracle ACFS, see ["acfsutil info file"](asmfs_util010.md).

Examples

The following example shows how to list all entries in the system registry.

Example 13-19 Using the advmutil list command

```
C:\> advmutil list /registry

  Drive Letter     Asm Volume
  ===================================
  H:               asm-volume1-123
  K:               asm-volume2-245
```

## advmutil mount

Purpose

The `advmutil` `mount` command mounts Oracle ADVM volume devices for file systems that are not Oracle ACFS.

Syntax and Description

  
`advmutil` `mount` \[`/register`\] { `drive_letter` | `dir` } `volume_device`  
`advmutil` `mount` `/all`  

Table 13-24 contains the options available with the Windows `advmutil` `mount` command.

Table 13-24 Options for the advmutil mount command

| Option | Description |
| --- | --- |
| `drive_letter` | Specifies the drive letter to mount. |
| `dir` | Specifies the directory of the mount point, including the drive letter. |
| `volume_device` | Indicates the Oracle ADVM volume device. |
| `/a` ll | Specifies to mount all non-Oracle ACFS file systems on this node. |
| `/register` | Optionally register an Oracle ADVM volume device and its drive letter in the Windows system registry. After startup of the Oracle ASM instance and Oracle ACFS, all registered drive letters and Oracle ADVM volume symbolic links are created. This allows for automatic file system mounting by Windows as is also done for Oracle ACFS file systems. |

Note:

To format an Oracle ADVM volume device with NTFS, it must be mounted on a drive letter. After formatting, Oracle ADVM volume devices with NTFS can be mounted on either a drive letter or a directory.

To successfully run this command, the local Oracle ASM instance must be running and the disk groups required by this command must have been created and mounted in the Oracle ASM instance and volumes enabled.

For information about registering Oracle ADVM volume devices for Oracle ACFS, see ["acfsutil registry"](asmfs_util010.md).

Examples

These examples show how to mount a file system that is not Oracle ACFS.

1. The first example shows how to create a drive letter for an Oracle ASM volume device for use as a non-Oracle ACFS access which you could then use to format the volume for use with NTFS.
2. The second example shows how to create a drive letter for an Oracle ASM volume device for use as a non-Oracle ACFS access which you could then use to format the volume for use with NTFS and save it in the Windows system registry.
3. The third example shows how to create a drive letter for all Oracle ASM volume devices which were saved in the system registry which also allows a file system to be accessible.

Example 13-20 Using the advmutil mount command

```
C:\> advmutil mount H: asm-volume1-123

C:\> advmutil mount H: asm-volume1-123 /register

C:\> advmutil mount /all
```