---
title: ASMCMD Volume Management Commands
book: "Automatic Storage Management Administrator's Guide"
doc_id: E18951-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e18951/asm_util007.htm
tags:
  - oracle
  - 11g
  - automatic-storage-management-administrators-guide
---

This section describes the ASMCMD volume management commands.

For information about Oracle ASM Dynamic Volume Manager (Oracle ADVM), refer to ["Overview of Oracle ASM Dynamic Volume Manager"](asmfilesystem.md). For information about using SQL statements to manage volumes, refer to ["Managing Volumes in a Disk Group"](asmdiskgrps.md).

Table 12-66 provides a summary of the Oracle ADVM volume management commands. To successfully run these commands, the local Oracle ASM instance must be running and the disk group required by this command must have been created and mounted in the Oracle ASM instance.

Table 12-66 Summary of ASMCMD volume management commands

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

## volcreate

Purpose

Creates an Oracle ADVM volume in the specified disk group.

Syntax and Description

  
`volcreate` `-G` `diskgroup` `-s` `size`  
 `[` `--column` `number` `]` `[` `--width` `stripe_width` `]`  
 \[`--redundancy` { `high` | `mirror` | `unprotected` } \]  
 \[`--primary` { `hot` | `cold` }\] \[`--secondary` { `hot` | `cold` }\] `volume`  

Table 12-67 describes the options for the `volcreate` command.

Table 12-67 Options for the volcreate command

| Option | Description |
| --- | --- |
| `-G` `diskgroup` | Name of the disk group containing the volume. |
| `-s` `size` | Size of the volume to be created in units of `K`, `M`, `G`, or `T`. The unit designation must be appended to the number specified. No space is allowed. For example: `200M` or `20G` |
| `--column` `number` | Number of columns in a stripe set. Values range from `1` to `8`. The default value is `4`. |
| `--width` `stripe` | Stripe width of a volume. The value can range from 4 KB to 1 MB, at power-of-two intervals, with a default of 128 KB. |
| `--redundancy` { `high` \| `mirror` \| `unprotected` } | Redundancy of the Oracle ADVM volume which can be specified for normal redundancy disk groups. The range of values is as follows: `unprotected` for non-mirrored redundancy, `mirror` for double-mirrored redundancy, or `high` for triple-mirrored redundancy. If redundancy is not specified, the setting defaults to the redundancy level of the disk group. |
| `--primary` { `hot\|cold` } | Intelligent Data Placement specification for primary extents, either `hot` or `cold` region. |
| `--secondary` { `hot\|cold` } | Intelligent Data Placement specification for secondary extents, either `hot` or `cold` region. |
| `volume` | Name of the volume. Only alphanumeric characters are allowed; hyphens are not allowed. The first character must be alphabetic. |

When creating an Oracle ADVM volume, a volume device name is created with a unique Oracle ADVM persistent disk group number that is concatenated to the end of the volume name. The unique number can be one to three digits.

On Linux, the volume device name is in the format `volume_name` `-` `nnn`, such as `volume1-123`. On Windows the volume device name is in the format `asm-` `volume_name` `-` `nnn`, such as `asm-volume1-123`. For information on mounting the volume device file, see ["Creating an Oracle ACFS File System"](asmfs_util001.md).

On Linux platforms, the volume name must be less than or equal to eleven alphanumeric characters, starting with an alphabetic character. On AIX platforms, the volume name must be less than or equal to twenty three alphanumeric characters, starting with an alphabetic character. On Windows and Solaris platforms, the volume name must be less than or equal to thirty alphanumeric characters, starting with an alphabetic character.

You can determine the volume device name with the `volinfo` command, described in "volinfo".

If the `--column` option is set to `1`, then striping is disabled and the stripe width is equal to the volume extent size. The volume extent size is 8 MB if the disk group allocation unit (AU) is less than or equal to 8 MB. If the AU size is greater than 8 MB, then the Oracle ADVM volume extent size is equivalent to the disk group AU size.

A successful volume creation automatically enables the volume device.

The volume device file functions as any other disk or logical volume to mount file systems or for applications to use directly.

For information about redundancy settings, see ["Mirroring, Redundancy, and Failure Group Options"](asmdiskgrps.md). For information about hot and cold disk regions, see ["Intelligent Data Placement"](asmdiskgrps.md).

Before creating an Oracle ADVM volume on AIX, ensure that the necessary user authorizations have been created. For information, refer to ["Oracle ACFS Command-line Tools for the AIX Environment"](asmfs_util004.md).

Examples

The following is an example of the `volcreate` command that creates `volume1` in the `data` disk group with the size set to 10 gigabytes.

Example 12-68 Using the ASMCMD volcreate command

```
ASMCMD [+] >  volcreate -G data -s 10G --width 64K --column 8 volume1

ASMCMD [+] > volinfo -G data volume1
Diskgroup Name: DATA
 
         Volume Name: VOLUME1
         Volume Device: /dev/asm/volume1-123
         State: ENABLED
         Size (MB): 10240
         Resize Unit (MB): 64
         Redundancy: MIRROR
         Stripe Columns: 8
         Stripe Width (K): 64
         Usage: 
         Mountpath:
```

## voldelete

Purpose

Deletes an Oracle ADVM volume.

Syntax and Description

  
`voldelete` `-G` `diskgroup` `volume`  

Table 12-68 describes the options for the `voldelete` command.

Table 12-68 Options for the voldelete command

| Option | Description |
| --- | --- |
| `-G` `diskgroup` | Name of the disk group containing the volume. |
| `volume` | Name of the volume. |

To successfully run this command, the local Oracle ASM instance must be running and the disk group required by this command must be mounted in the Oracle ASM instance. Before deleting a volume, you must ensure that there are no active file systems associated with the volume.

Examples

The following is an example of the `voldelete` command that deletes `volume1` from the `data` disk group.

Example 12-69 Using the ASMCMD voldelete command

```
ASMCMD [+] > voldelete -G data volume1
```

## voldisable

Purpose

Disables Oracle ADVM volumes in mounted disk groups and removes the volume device on the local node.

Syntax and Description

  
`voldisable` { `-a` | `-G` `diskgroup` `-a` | `-G` `diskgroup` `volume` }  

Table 12-69 describes the options for the `voldisable` command.

Table 12-69 Options for the voldisable command

| Option | Description |
| --- | --- |
| `-a` | When used without a disk group name, specifies all volumes within all disk groups.  When used with a disk group name (`-G` `diskgroup` `-a`), specifies all volumes within that disk group. |
| `-G` `diskgroup` | Name of the disk group containing the volume. |
| `volume` | Name of the volume. |

You can disable volumes before shutting down an Oracle ASM instance or dismounting a disk group to verify that the operations can be accomplished normally without including a force option due to open volume files. Disabling a volume also prevents any subsequent opens on the volume or device file because it no longer exists.

Before disabling a volume, you must ensure that there are no active file systems associated with the volume. You must first dismount the Oracle ACFS file system before disabling the volume. See ["Dismounting an Oracle ACFS File System"](asmfs_util001.md).

You can delete a volume without first disabling the volume.

Examples

The following is an example of the `voldisable` command that disables `volume1` in the `data` disk group.

Example 12-70 Using the ASMCMD voldisable command

```
ASMCMD [+] > voldisable -G data volume1
```

## volenable

Purpose

Enables Oracle ADVM volumes in mounted disk groups.

Syntax and Description

  
`volenable` { `-a` | `-G` `diskgroup` `-a` | `-G` `diskgroup` `volume` }  

Table 12-70 describes the options for the `volenable` command.

Table 12-70 Options for the volenable command

| Option | Description |
| --- | --- |
| `-a` | When used without a disk group name, specifies all volumes within all disk groups.  When used with a disk group name (`-G` `diskgroup` `-a`), specifies all volumes within that disk group. |
| `-G` `diskgroup` | Name of the disk group containing the volume. |
| `volume` | Name of the volume. |

A volume is enabled when it is created.

Examples

The following is an example of the `volenable` command that enables `volume1` in the `data` disk group.

Example 12-71 Using the ASMCMD volenable command

```
ASMCMD [+] > volenable -G data volume1
```

## volinfo

Purpose

Displays information about Oracle ADVM volumes.

Syntax and Description

  
`volinfo` { `-a` | `-G` `diskgroup` `-a` | `-G` `diskgroup` `volume` }  
`volinfo` { `--show_diskgroup` | `--show_volume` } `volumedevice`  

Table 12-71 describes the options for the `volinfo` command.

Table 12-71 Options for the volinfo command

| Option | Description |
| --- | --- |
| `-a` | When used without a disk group name, specifies all volumes within all disk groups.  When used with a disk group name (`-G` `diskgroup` `-a`), specifies all volumes within that disk group. |
| `-G` `diskgroup` | Name of the disk group containing the volume. |
| `volume` | Name of the volume. |
| `--show_diskgroup` | Returns only the disk group name. A volume device name is required. |
| `--show_volume` | Returns only the volume name. A volume device name is required. |
| `volumedevice` | Name of the volume device. |

Examples

The first example displays information about the `volume1` volume in the `data` disk group. This example was produced in a Linux environment. The second example displays information about the `volume1` volume in the `data` disk group and was produced in a Windows environment.

The mount path field displays the last mount path for the volume.

Example 12-72 Using the ASMCMD volinfo command

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
         Stripe Width (K): 64
         Usage: ACFS
         Mountpath: /u01/app/acfsmounts/acfs1

ASMCMD [+] > volinfo -G data -a
Diskgroup Name: DATA
         Volume Name: VOLUME1
         Volume Device: \\.\asm-volume1-311
         State: ENABLED
         Size (MB): 1024
         Resize Unit (MB): 32
         Redundancy: MIRROR
         Stripe Columns: 4
         Stripe Width (K): 128
         Usage: ACFS
         Mountpath: C:\oracle\acfsmounts\acfs1
```

## volresize

Purpose

Resizes an Oracle ADVM volume.

Syntax and Description

  
`volresize` `-G` `diskgroup` `-s` `size` `[` `-f` `]` `volume`  

Table 12-72 describes the options for the `volresize` command.

Table 12-72 Options for the volresize command

| Option | Description |
| --- | --- |
| `-G` `diskgroup` | Name of the disk group containing the volume. |
| `-f` | Forces the shrinking of a volume that is not an Oracle ACFS volume and suppresses any warning message. |
| `volume` | Name of the volume. |
| `-s` `size` | New size of the volume in units of `K`, `M`, `G`, or `T`. |

If the volume is mounted on a non-Oracle ACFS file system, then dismount the file system first before resizing. If the new size is smaller than current, you are warned of possible data corruption. Unless the `-f` (force) option is specified, you are prompted whether to continue with the operation.

If there is an Oracle ACFS file system on the volume, then you cannot resize the volume with the `volresize` command. You must use the `acfsutil` `size` command, which also resizes the volume and file system. For information, see ["acfsutil size"](asmfs_util010.md).

Examples

The following is an example of the `volresize` command that resizes `volume1` in the `data` disk group to 20 gigabytes.

Example 12-73 Using the ASMCMD volresize command

```
ASMCMD [+] > volresize -G data -s 20G volume1
```

## volset

Purpose

Sets attributes of an Oracle ADVM volume in mounted disk groups.

Syntax and Description

  
`volset` `-G` `diskgroup` `[` `--usagestring` `string``]`  
 `[``--mountpath` `mount_path` `]`  
 \[`--primary` { `hot` | `cold` }\] \[`--secondary` { `hot` | `cold` }\] `volume`  

Table 12-73 describes the options for the `volset` command.

Table 12-73 Options for the volset command

| Option | Description |
| --- | --- |
| `-G` `diskgroup` | Name of the disk group containing the volume. |
| `--usagestring` `string` | Optional usage string to tag a volume which can be up to 30 characters. This string is set to `ACFS` when the volume is attached to an Oracle ACFS file system and should not be changed. |
| `--mountpath` `mount_path` | Optional string to tag a volume with its mount path string which can be up to 1024 characters. This string is set when the file system is mounted and should not be changed. |
| `--primary` { `hot\|cold` } | Intelligent Data Placement specification for primary extents, either `hot` or `cold` region. |
| `--secondary` { `hot\|cold` } | Intelligent Data Placement specification for secondary extents, either `hot` or `cold` region. |
| `volume` | Name of the volume. |

When running the `mkfs` command to create a file system, the usage field is set to `ACFS` and `mountpath` field is reset to an empty string if it has been set. The `usage` field should remain at `ACFS`.

When running the `mount` command to mount a file system, the `mountpath` field is set to the mount path value to identify the mount point for the file system. After the value is set by the `mount` command, the `mountpath` field should not be updated.

Examples

The following is an example of a `volset` command that sets the `usage` string for a volume that is not associated with a file system.

Example 12-74 Using the ASMCMD volset command

```
ASMCMD [+] > volset -G data --usagestring 'no file system created' volume1
```

## volstat

Purpose

Reports I/O statistics for Oracle ADVM volumes.

Syntax and Description

  
`volstat` \[`-G` `diskgroup`\] \[`volume`\]  
  

Table 12-74 describes the options for the `volstat` command.

Table 12-74 Options for the volstat command

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

Example 12-75 Using the ASMCMD volstat command

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