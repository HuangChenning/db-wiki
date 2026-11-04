---
title: "Oracle Automatic Storage Management Administrator's Guide"
book: "Oracle Automatic Storage Management Administrator's Guide"
doc_id: F34287-08
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/ostmg/part-iii-oracle-automatic-storage-management-cluster-file-system/managing-oracle-advm-with-asmcmd.html
tags:
  - oracle
  - 19c
  - automatic-storage-management-administrators-guide
---

## Managing Oracle ADVM with ASMCMD

Oracle ASM Command-Line Utility (ASMCMD) provides commands for managing Oracle ADVM volumes.

This chapter describes the Oracle Automatic Storage Management (Oracle ASM) Command-Line Utility (ASMCMD) volume management commands.

See also

- [Overview of Oracle ASM Dynamic Volume Manager](introducing-oracle-acfs-and-oracle-advm.md) for information about Oracle ASM Dynamic Volume Manager (Oracle ADVM)
- [Managing Oracle ADVM Volumes in a Disk Group](administering-oracle-asm-disk-groups.md) for information about using SQL statements to manage Oracle ADVM volumes
- [About ASMCMD](managing-oracle-asm-with-asmcmd.md) for information about using ASMCMD

## ASMCMD Volume Management Commands

This topic provides a summary of the Oracle ADVM volume management commands.

The table “Summary of ASMCMD volume management commands” lists the Oracle ADVM volume management commands with brief descriptions. To successfully run these commands, the local Oracle ASM instance must be running and the disk group required by this command must have been created and mounted in the Oracle ASM instance.

Table: Summary of ASMCMD volume management commands

| Command | Description |
| --- | --- |
| volcreate | Creates an Oracle ADVM volume in the specified disk group. |
| voldelete | Deletes an Oracle ADVM volume. |
| voldisable | Disables Oracle ADVM volumes in mounted disk groups. |
| volenable | Enables Oracle ADVM volumes in mounted disk groups. |
| volinfo | Displays information about Oracle ADVM volumes. |
| volresize | Resizes an Oracle ADVM volume. |
| volset | Sets attributes of an Oracle ADVM volume in mounted disk groups. |
| volstat | Reports volume I/O statistics. |

### volcreate

Purpose

Creates an Oracle ADVM volume in the specified disk group.

Syntax and Description

```
volcreate -G diskgroup -s size
   [ --column number ] [ --width stripe_width ]
   [--redundancy {high|mirror|unprotected}]
   [--primary {hot|cold}] [--secondary {hot|cold}] volume
```

The table “Options for the volcreate command” describes the options for the `volcreate` command.

Table: Options for the volcreate command

| Option | Description |
| --- | --- |
| `-G` `diskgroup` | Name of the disk group containing the volume. |
| `-s` `size` | Size of the volume to be created in units of `K`, `M`, `G`, or `T`. The value must be a positive integer. The unit designation must be appended to the number specified. A space is not allowed between the number and the unit designation. For example: `200M` or `20G` |
| `--column` `number` | Number of columns in a stripe set. Values range from `1` to `8`. The default value is `8`. |
| `--width` `stripe` | Stripe width of a volume in units of `K` or `M`. The value can range from 4 KB to 1 MB, at power-of-two intervals. The default is `1M`. |
| `--redundancy` { `high` \| `mirror` \| `unprotected` } | Redundancy of the Oracle ADVM volume which can be only specified for normal redundancy disk groups. If redundancy is not specified, the setting defaults to the redundancy level of the disk group and this is the recommended setting. The range of values is as follows: `unprotected` for non-mirrored redundancy, `mirror` for double-mirrored redundancy, or `high` for triple-mirrored redundancy. |
| `--primary` { `hot\|cold` } | Data placement specification for primary extents, either `hot` or `cold` region.  > Note: >  > Disk region attributes default to cold and cold is the only setting. |
| `--secondary` { `hot\|cold` } | Data placement specification for secondary extents, either `hot` or `cold` region.  > Note: >  > Disk region attributes default to cold and cold is the only setting. |
| `volume` | Name of the volume. Only alphanumeric characters and underscores are allowed. Hyphens are not allowed. The first character must be alphabetic. |

Warning:

Specifying `--redundancy` `unprotected` means that Oracle ASM mirroring is not available for data recovery with the Oracle ADVM volume. The redundancy setting (`normal`) of the disk group does not provide mirroring for an unprotected Oracle ADVM volume. The `unprotected` configuration is not recommended for production environments as intermittent storage access failures can result in the loss of data. Backups are strongly recommended.

When creating an Oracle ADVM volume, a volume device name is created with a unique Oracle ADVM persistent disk group number that is concatenated to the end of the volume name. The unique number can be one to three digits.

On Linux, the volume device name is in the format *volume\_name* `-` *nnn*, such as `volume1-123`. On Windows the volume device name is in the format `asm-` *volume\_name* `-` *nnn*, such as `asm-volume1-123`.

On Linux platforms, the volume name must be less than or equal to eleven alphanumeric characters, starting with an alphabetic character. On AIX platforms, the volume name must be less than or equal to twenty three alphanumeric characters, starting with an alphabetic character. On Windows and Solaris platforms, the volume name must be less than or equal to thirty alphanumeric characters, starting with an alphabetic character.

You can determine the volume device name with the `volinfo` command.

If the `--column` option is set to `1`, then striping is disabled and the stripe width equals the default volume extent size (64 MB). Setting the `--column` option to 8 (the default) is recommended to achieve optimal performance with database data files and other files.

A successful volume creation automatically enables the volume device.

The volume device file functions as any other disk or logical volume to mount file systems or for applications to use directly.

When creating an accelerator volume, create the volume on a disk group with storage that is significantly faster than the primary volume's storage.

Before creating an Oracle ADVM volume on AIX, ensure that the necessary user authorizations have been created.

Examples

The following is an example of the `volcreate` command that creates `volume1` in the `data` disk group with the size set to 10 gigabytes.

Example: Using the ASMCMD volcreate command

```
ASMCMD [+] >  volcreate -G data -s 10G --width 1M --column 8 volume1

ASMCMD [+] > volinfo -G data volume1
Diskgroup Name: DATA

         Volume Name: VOLUME1
         Volume Device: /dev/asm/volume1-123
         State: ENABLED
         Size (MB): 10240
         Resize Unit (MB): 64
         Redundancy: MIRROR
         Stripe Columns: 8
         Stripe Width (K): 1024
         Usage:
         Mountpath:
```

See also

- [Creating an Oracle ACFS File System](managing-oracle-acfs-with-command-line-tools.md) for information on mounting the volume device file
- volinfo for information about the `volinfo` command.
- [Limits of Oracle ADVM](understanding-oracle-acfs-advanced-topics.md) for information about Oracle ADVM limits
- [mkfs](managing-oracle-acfs-with-command-line-tools.md) for information about the accelerator volume
- [Mirroring, Redundancy, and Failure Group Options](administering-oracle-asm-disk-groups.md) for information about redundancy settings
- [Oracle ACFS Command-Line Tools for the AIX Environment](managing-oracle-acfs-with-command-line-tools.md) for information about user authorizations on AIX

### voldelete

Purpose

Deletes an Oracle ADVM volume.

Syntax and Description

```
voldelete -G diskgroup volume
```

The table “Options for the voldelete command” describes the options for the `voldelete` command.

Table: Options for the voldelete command

| Option | Description |
| --- | --- |
| `-G` `diskgroup` | Name of the disk group containing the volume. |
| `volume` | Name of the volume. |

To successfully run this command, the local Oracle ASM instance must be running and the disk group required by this command must be mounted in the Oracle ASM instance. Before deleting a volume, you must ensure that there are no active file systems associated with the volume.

Examples

The following is an example of the `voldelete` command that deletes `volume1` from the `data` disk group.

Example: Using the ASMCMD voldelete command

```
ASMCMD [+] > voldelete -G data volume1
```

### voldisable

Purpose

Disables Oracle ADVM volumes in mounted disk groups and removes the volume device on the local node.

Syntax and Description

```
voldisable { --all |{ -G diskgroup { -a | volume } } }
```

The table “Options for the voldisable command” describes the options for the `voldisable` command.

Table: Options for the voldisable command

| Option | Description |
| --- | --- |
| `--all` | Specifies all volumes within all disk groups. |
| `-G` `diskgroup` | Name of the disk group containing the volume. |
| `-a` | Specifies all volumes within the specified disk group. |
| `volume` | Name of the volume. |

You can disable volumes before shutting down an Oracle ASM instance or dismounting a disk group to verify that the operations can be accomplished normally without including a force option due to open volume files. Disabling a volume also prevents any subsequent opens on the volume or device file because it no longer exists.

Before disabling a volume, you must ensure that there are no active file systems associated with the volume. You must first dismount the Oracle ACFS file system before disabling the volume. Refer to [Deregistering, Dismounting, and Disabling Volumes and Oracle ACFS File Systems](managing-oracle-acfs-with-command-line-tools.md).

You can delete a volume without first disabling the volume.

Examples

The following is an example of the `voldisable` command that disables `volume1` in the `data` disk group.

Example: Using the ASMCMD voldisable command

```
ASMCMD [+] > voldisable -G data volume1
```

### volenable

Purpose

Enables Oracle ADVM volumes in mounted disk groups.

Syntax and Description

```
volenable {  --all |{ -G diskgroup { -a | volume } } }
```

The table “Options for the volenable command” describes the options for the `volenable` command.

Table: Options for the volenable command

| Option | Description |
| --- | --- |
| `--all` | Specifies all volumes within all disk groups. |
| `-G` `diskgroup` | Name of the disk group containing the volume. |
| `-a` | Specifies all volumes within the specified disk group. |
| `volume` | Name of the volume. |

A volume is enabled when it is created.

Examples

The following is an example of the `volenable` command that enables `volume1` in the `data` disk group.

Example: Using the ASMCMD volenable command

```
ASMCMD [+] > volenable -G data volume1
```

### volinfo

Purpose

Displays information about Oracle ADVM volumes.

Syntax and Description

```
volinfo {  --all |{ -G diskgroup { -a | volume } } }
volinfo {--show_diskgroup |--show_volume}  volumedevice
```

The table “Options for the volinfo command” describes the options for the `volinfo` command.

Table: Options for the volinfo command

| Option | Description |
| --- | --- |
| `--all` | Specifies all volumes within all disk groups. |
| `-G` `diskgroup` | Name of the disk group containing the volume. |
| `-a` | Specifies all volumes within the specified disk group. |
| `volume` | Name of the volume. |
| `--show_diskgroup` | Returns only the disk group name. A volume device name is required. |
| `--show_volume` | Returns only the volume name. A volume device name is required. |
| `volumedevice` | Name of the volume device. |

Examples

The first example displays information about the `volume1` volume in the `data` disk group. This example was produced in a Linux environment. The second example displays information about the `volume1` volume in the `data` disk group and was produced in a Windows environment.

The `Mountpath` field contains the path where the volume is currently mounted or where the volume was last mounted.

Example: Using the ASMCMD volinfo command

```
ASMCMD [+] > volinfo -G data volume1
Diskgroup Name: DATA
         Volume Name: VOLUME1
         Volume Device: /dev/asm/volume1-123
         State: ENABLED
         Size (MB): 10240
         Resize Unit (MB): 64
         Redundancy: MIRROR
         Stripe Columns: 8
         Stripe Width (K): 1024
         Usage: ACFS
         Mountpath: /acfsmounts/acfs1

ASMCMD [+] > volinfo -G data -a
Diskgroup Name: DATA
         Volume Name: VOLUME1
         Volume Device: \\.\asm-volume1-311
         State: ENABLED
         Size (MB): 10240
         Resize Unit (MB): 64
         Redundancy: MIRROR
         Stripe Columns: 8
         Stripe Width (K): 1024
         Usage: ACFS
         Mountpath: C:\oracle\acfsmounts\acfs1
```

### volresize

Purpose

Resizes an Oracle ADVM volume.

Syntax and Description

```
volresize -G diskgroup -s size [ -f ] volume
```

The table “Options for the volresize command” describes the options for the `volresize` command.

Table: Options for the volresize command

| Option | Description |
| --- | --- |
| `-G` `diskgroup` | Name of the disk group containing the volume. |
| `-f` | Forces the shrinking of a volume that is not an Oracle ACFS volume and suppresses any warning message. |
| `volume` | Name of the volume. |
| `-s` `size` | New size of the volume in units of `K`, `M`, `G`, or `T`. |

If the volume is mounted on a non-Oracle ACFS file system, then dismount the file system first before resizing. If the new size is smaller than current, you are warned of possible data corruption. Unless the `-f` (force) option is specified, you are prompted whether to continue with the operation.

If there is an Oracle ACFS file system on the volume, then you cannot resize the volume with the `volresize` command. You must use the `acfsutil` `size` command, which also resizes the volume and file system. For information, see " [acfsutil size](managing-oracle-acfs-with-command-line-tools.md) ".

Examples

The following is an example of the `volresize` command that resizes `volume1` in the `data` disk group to 20 gigabytes.

Example: Using the ASMCMD volresize command

```
ASMCMD [+] > volresize -G data -s 20G volume1
```

### volset

Purpose

Sets attributes of an Oracle ADVM volume in mounted disk groups.

Syntax and Description

```
volset -G diskgroup [ --usagestring string]
  [--mountpath  mount_path ]
  [--primary {hot|cold}] [--secondary {hot|cold}] volume
```

The table “Options for the volset command” describes the options for the `volset` command.

Table: Options for the volset command

| Option | Description |
| --- | --- |
| `-G` `diskgroup` | Name of the disk group containing the volume. |
| `--usagestring` `string` | Optional usage string to tag a volume which can be up to 30 characters. This string is set to `ACFS` when the volume is attached to an Oracle ACFS file system and should not be changed. |
| `--mountpath` `mount_path` | Optional string to tag a volume with its mount path string which can be up to 1024 characters. This string is set when the file system is mounted and should not be changed. |
| `--primary` { `hot\|cold` } | Data placement specification for primary extents, either `hot` or `cold` region.  > Note: >  > Disk region attributes default to cold and cold is the only setting. |
| `--secondary` { `hot\|cold` } | Data placement specification for secondary extents, either `hot` or `cold` region.  > Note: >  > Disk region attributes default to cold and cold is the only setting. |
| `volume` | Name of the volume. |

When running the `mkfs` command to create a file system, the usage field is set to `ACFS` and `mountpath` field is reset to an empty string if it has been set. The `usage` field should remain at `ACFS`.

When running the `mount` command to mount a file system, the `mountpath` field is set to the mount path value to identify the mount point for the file system. After the value is set by the `mount` command, the `mountpath` field should not be updated.

Examples

The following is an example of a `volset` command that sets the `usage` string for a volume that is not associated with a file system.

Example: Using the ASMCMD volset command

```
ASMCMD [+] > volset -G data --usagestring 'no file system created' volume1
```

### volstat

Purpose

Reports I/O statistics for Oracle ADVM volumes.

Syntax and Description

```
volstat [-G diskgroup] [volume]
```

The table “Options for the volstat command” describes the options for the `volstat` command.

Table: Options for the volstat command

| Option | Description |
| --- | --- |
| `-G` `diskgroup` | Name of the mounted disk group containing the volume. |
| `volume` | Name of the volume. |

The following apply when using the `volstat` command.

- If the disk group is not specified and the volume name is specified, all mounted disk groups are searched for the specified volume name.
- If the disk group name is specified and the volume name is omitted, all volumes are displayed for the named disk group.
- If both the disk group name and the volume name are omitted, all volumes on all disk groups are displayed.

Examples

The following is an example of the `volstat` command that displays information about volumes in the `data` disk group.

Example: Using the ASMCMD volstat command

```
ASMCMD [+] > volstat -G data
DISKGROUP NUMBER / NAME:  1 / DATA
---------------------------------------
  VOLUME_NAME
     READS           BYTES_READ      READ_TIME       READ_ERRS
     WRITES          BYTES_WRITTEN   WRITE_TIME      WRITE_ERRS
  -------------------------------------------------------------
  VOLUME1
     10085           2290573312      22923           0
     1382            5309440         1482            0
```