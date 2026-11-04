---
title: "Administrator's Guide"
book: "Advanced Cluster File System Administrator's Guide"
doc_id: F30297-04
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/acfsg/manage-acfs-advm-asmca.html
tags:
  - oracle
  - 21c
  - advanced-cluster-file-system-administrators-guide
---

Oracle ASM Configuration Assistant (ASMCA) provides utilities for managing Oracle Advanced Cluster File System (Oracle ACFS) and Oracle ASM Dynamic Volume Manager (Oracle ADVM).

Oracle ASM Configuration Assistant (ASMCA) supports installing and configuring Oracle ASM instances, Oracle ASM disk groups, Oracle ASM Dynamic Volume Manager (Oracle ADVM) volumes, and Oracle Advanced Cluster File System (Oracle ACFS) file systems. In addition, you can use the ASMCA command-line interface.

This chapter discusses the following topics:

- ASMCA GUI Tool for Managing Oracle ACFS and Oracle ADVM
- ASMCA Command-Line Interface for Managing Oracle ACFS and Oracle ADVM

See Also:

- [Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/acfsg&id=OSTMG-GUID-877EB0F8-E9CA-4C97-965C-AACBB256B12D) for information about managing Oracle ASM instances and disk groups with ASMCA

Note:

Some ASMCA functionality and menu options are only available in specific environments, such as an Oracle RAC configuration. For details about a specific ASMCA page, access the online help provided with the Help button.

### ASMCA GUI Tool for Managing Oracle ACFS and Oracle ADVM

This section contains the following topics:

#### Managing Oracle ADVM Volumes with ASMCA

Note:

When creating an Oracle ADVM volume for an Oracle ACFS file system that is intended to store database files, use the ASMCMD `volcreate` command or the SQL `ALTER` `DISKGROUP` `ADD` `VOLUME` SQL statement rather than the ASMCA tool to ensure that the column striping is set to 1.

Oracle ASM Configuration Assistant enables you to create or configure an Oracle ADVM volume.

Right click a selected volume in the Oracle ASM Configuration Assistant screen to display the configuration options menu.

The menu includes options to:

- Enable disabled volumes and disable enabled volumes
- View status details
- Resize volumes that have not been mounted on an Oracle ACFS file system
- Delete volumes

There are options for creating a volume, enabling all volumes, and disabling all volumes.

Click Create to display the dialog for creating a volume. You must provide a unique volume name for the existing Oracle ASM disk group that you select from the list of disk groups. You must also specify the size for the volume. You can optionally choose to display advanced options for creating a volume which enables you to specify the redundancy level and striping characteristics.

The compatibility parameters `COMPATIBLE.ASM` and `COMPATIBLE.ADVM` must be set to `11.2` or higher for the disk group to contain an Oracle ADVM volume. To use Oracle ACFS encryption, replication, security, or tagging, the disk group on which the volume is created for the file system must have compatibility attributes for `ASM` and `ADVM` set to `11.2.0.2` or higher.

Before creating an Oracle ADVM volume on AIX, ensure that the necessary user authorizations have been created.

See Also:

- [volcreate](manage-advm-asmcmd.md) for information about the advanced options when creating a volume
- [Oracle ACFS Features Enabled by Compatibility Attribute Settings](understand-acfs-admin.md) for information about Oracle ACFS features and disk group compatibility attribute settings
- [Oracle ACFS Command-Line Tools for the AIX Environment](acfs-commands-aix.md) for information about creating an Oracle ADVM volume on the AIX operating system
- [Managing Oracle ADVM with ASMCMD](manage-advm-asmcmd.md) for information about creating a volume with the ASMCMD `volcreate` command
- [Introducing Oracle ACFS and Oracle ADVM](intro-acfs-advm.md) for an overview of Oracle ACFS
- [Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/acfsg&id=OSTMG-GUID-17B6982D-DC71-40D2-BB9B-A6C659DD187E) for information about the `ALTER` `DISKGROUP` `ADD` `VOLUME` SQL statement to administer volumes

#### Managing Oracle ACFS File Systems with ASMCA

Oracle ASM Configuration Assistant enables you to create or configure an Oracle ACFS file system.

To configure an existing file system, right click a selected file system in the Oracle ASM Configuration Assistant screen to display the configuration options menu.

The menu includes options to:

- View status details
- Mount and dismount the file system
- Resize the file system
- Delete the file system
- Display or execute the security commands
- Create or delete snapshots

Some commands require root privileges, such as mounting a file system. ASMCA generates the command for you to run manually as `root`.

There are buttons for Create, Mount All, Dismount All, and Security and Encryption commands.

Oracle ASM Configuration Assistant enables you to create an Oracle ACFS file system.

Select Create, then select the type of Oracle ACFS file system you want to create and an existing Oracle ADVM volume from the lists. Specify the mount point field; the mount point must be an existing directory. The file system must be mounted to make it available. You can choose to enable the Auto Mount option. You can also provide a description of the file system in the Description field.

The mount command must be manually run as root at an operating system prompt.

You can choose to create an Oracle ACFS file system for an Oracle Database.

See Also:

- [mount](acfs-commands-linux.md) for information about mounting an Oracle ACFS file system on Linux
- Creating an Oracle ACFS File System for Database Use for more information about creating a file system for a database home
- [Introducing Oracle ACFS and Oracle ADVM](intro-acfs-advm.md) for additional information about Oracle ACFS
- [Basic Steps to Manage Oracle ACFS Systems](steps-manage-acfs.md) for a summary of the basic steps for creating an Oracle ACFS file system

#### Managing Security and Encryption for Oracle ACFS with ASMCA

Oracle ASM Configuration Assistant enables you to configure security and encryption for an Oracle ACFS file system.

You must initialize the security system as the first step in configuring security for an Oracle ACFS file system. You must also initialize the encryption system as the first step in encrypting an Oracle ACFS file system. You do not have to use both Oracle ACFS security and encryption on the same file system. If you decide to use both security and encryption, then encryption must be initialized and set before enabling encryption on a security realm.

In the dialog that displays, enter the information to specify the security administrator and the operating system group of the security administrator. You can choose to create a password protected wallet. After you complete the entry fields in the dialog, click Show Command to display the commands you must run as a root or Administrator user at an operating system prompt. For example:

```
# /sbin/acfsutil sec init -u grid -g asmadmin
# /sbin/acfsutil encr init
```

After security has been initialized, you can use the menu options to manage security and encryption for an Oracle ACFS file system.

The menu includes options to:

- Set encryption
- Enable and disable encryption
- Prepare and enable security
- Enable and disable security

See Also:

- [acfsutil encr init](acfs-commands-encryption.md) for information about the `acfsutil` `encr` `init` command
- [Oracle ACFS Encryption](understand-acfs-admin.md) for information about Oracle ACFS encryption
- [Encrypting Oracle ACFS File Systems using OCR as Encryption Key Store](steps-manage-acfs.md) for a summary of the basic steps for setting up encryption on an Oracle ACFS file system
- [Oracle ACFS Command-Line Utilities](acfs-commands-utilities.md) for information about the `acfsutil` `encr` command

#### Creating an Oracle ACFS File System for Database Use

To create an Oracle ACFS file system for database use, you can select the Create ACFS for Database Use from the disk group configuration options menu to display the dialog entry box.

Note:

When creating an Oracle ADVM volume for an Oracle ACFS file system that is intended to store database files, use the ASMCMD `volcreate` command or the SQL `ALTER` `DISKGROUP` `ADD` `VOLUME` SQL statement rather than the ASMCA tool to ensure that the column striping is set to 1.

In this dialog, you must enter:

- Volume Name
	This is the name of the Oracle ADVM volume you want to create.
- Mount Point
	This is the mount point for the file system where you want to install the database home. The file system that contains the database home should not be located under the Oracle Grid Infrastructure base (`ORACLE_BASE` for grid) directory.
- Size in gigabytes (GB)
	The default is 7 GB and the minimum recommended size.
- Owner Name
	This is the operating system name of the user that installs the database and owns the software in the database home.
- Owner Group
	This is the operating system group of the owner of the database home.

The mount point must be an existing directory. The file system must be mounted to make it available.

Select Automatically run configuration commands to run ASMCA configuration commands automatically. To use this option, you must provide the `root` credentials on the ASMCA Settings page.

The mount command may also be run manually as `root` at an operating system prompt.

See Also:

- [volcreate](manage-advm-asmcmd.md) for information about the `volcreate` command
- [Overview of Oracle ASM Dynamic Volume Manager](overview-advm.md) for information about Oracle ADVM volumes
- [About Oracle ACFS and Oracle Database Homes](understand-acfs-concepts.md) for information about mount points and database homes
- [mount](acfs-commands-linux.md) for information about mounting an Oracle ACFS file system on Linux
- [About the Oracle ACFS Mount Registry](understand-acfs-concepts.md) for information on the mount registry
- [Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/acfsg&id=OSTMG-GUID-17B6982D-DC71-40D2-BB9B-A6C659DD187E) for information about the `ALTER` `DISKGROUP` `ADD` `VOLUME` SQL statement to administer volumes

### ASMCA Command-Line Interface for Managing Oracle ACFS and Oracle ADVM

The ASMCA command-line interface provides non-GUI support for configuring Oracle ASM disk groups, volumes, and Oracle ACFS.

- ASMCA Commands for Oracle ACFS and Oracle ADVM

See Also:

- [Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/acfsg&id=OSTMG-GUID-877EB0F8-E9CA-4C97-965C-AACBB256B12D) for general information about running the ASMCA command-line interface and about options that are common to multiple commands

#### ASMCA Commands for Oracle ACFS and Oracle ADVM

This section describes the commands that can be run with ASMCA command-line to manage Oracle ACFS objects.

- Create an Oracle ACFS Snapshot
- Delete an Oracle ACFS Snapshot
- Create a Volume
- Create an Oracle ACFS File System

##### Create an Oracle ACFS Snapshot

`—createACFSSnapshot` creates an Oracle Advanced Cluster File System (Oracle ACFS) snapshot.

Syntax

```
asmca -silent
   -createACFSSnapshot
       (-acfsMountPoint mount_path )
       (-snapshotName snapshot_name )
       [-snapshotMode { r|w } ]
       [-parentSnapshotName parent_snapshot_name ]
```

Table 4-1 contains the options available with the `—createACFSSnapshot` command.

Table 4-1 Options for the -createACFSSnapshot command

| Option | Description |
| --- | --- |
| `-acfsMountPoint` `mount_path` | Specifies an existing path to be used as the mount point. This is required in an Oracle RAC environment. |
| `-snapshotName` `anapshot_name` | Specifies the name of the Oracle ACFS snapshot. |
| `-snapshotMode` `r\|w` | Specifies the mode of the Oracle ACFS snapshot, either read-only (`r`) or read-write (`w`). |
| `-parentSnapshotName` `parent_snapshot_name` | Specifies the name of the Oracle ACFS parent snapshot. |

##### Delete an Oracle ACFS Snapshot

`—deleteACFSSnapshot` deletes an existing Oracle Advanced Cluster File System (Oracle ACFS) snapshot.

Syntax

```
asmca -silent
   -deleteACFSSnapshot
       (-acfsMountPoint mount_path )
       (-snapshotName snapshot_name )
```

Table 4-2 contains the options available with the `—deleteACFSSnapshot` command.

Table 4-2 Options for the -deleteACFSSnapshot command

| Option | Description |
| --- | --- |
| `-acfsMountPoint` `mount_path` | Specifies an existing path to be used as the mount point. This is required in an Oracle RAC environment. |
| `-snapshotName` `anapshot_name` | Specifies the name of the Oracle ACFS snapshot. |

##### Create a Volume

`-createVolume` creates Oracle ADVM volumes.

Syntax

```
asmca -silent
      -createVolume
        { -volumeName volume_name
         -volumeDiskGroup diskgroup
         -volumeSizeGB size_GB
         [ -volumeRedundancy { INHERIT | HIGH | NORMAL | EXTERNAL } ] ... }
       [-sysAsmPassword sysasm_password ]
```

Table 4-3 contains the options available with the - `createVolume` command.

Table 4-3 Options for the -createVolume command

| Option | Description |
| --- | --- |
| `-volumeName` `volume_name` | Specifies the name of the volume to create. |
| `-volumeDiskGroup` `diskgroup` | Specifies the name of the disk group where you want to create the volume. |
| `-volumeSizeGB` `size_GB` | Specifies the size of the volume in Gigabytes. |
| `-volumeRedundancy` { `INHERIT` \| `HIGH` \| `NORMAL` \| `EXTERNAL` } | Specifies the redundancy setting for the volume. |

Examples

To create an Oracle ADVM volume:

Example 4-1 Using asmca -silent -createVolume

```
$ asmca -silent
        -createVolume
           -volumeName volume1 
           -volumeDiskGroup mynewdg 
           -volumeSizeGB 1 

Volume volume1 created successfully.
```

##### Create an Oracle ACFS File System

\- `createACFS` creates an Oracle Advanced Cluster File System (Oracle ACFS).

This command does not mount the Oracle ACFS file system. For information about mounting an Oracle ACFS file system, refer to [mount](acfs-commands-linux.md) for Linux environments.

Syntax

```
asmca -silent
      -createACFS
       { -acfsVolumeDevice volume_device }
       { -acfsMountPoint mount_path }
       [-acfsUserName acfs_username ]
       [-acfsUserGroup acfs_usergroup ]
       [-sysAsmPassword sysasm_password ]
```

Table 4-4 contains the options available with the - `createACFS` command.

Table 4-4 Options for the -createACFS command

| Option | Description |
| --- | --- |
| `-acfsVolumeDevice` `volume_device` | Specifies the name of the Oracle ADVM volume device. |
| `-acfsMountPoint` `mount_path` | Specifies an existing path to be used as the mount point. This is required in an Oracle RAC environment. |
| `-acfsUserName` `acfs_username` | Specifies the Oracle ACFS user name. |
| `-acfsUserGroup` `acfs_usergroup` | Specifies the Oracle ACFS group name. |

Examples

To create an Oracle ACFS file system:

Example 4-2 Using asmca -silent -createACFS

```
$ asmca -silent
        -createACFS
           -acfsVolumeDevice /dev/asm/volume1-457
           -acfsMountPoint /acfsmounts/acfs1
```