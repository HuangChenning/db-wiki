---
title: Oracle ACFS Command-Line Utilities for Multiple Environments
book: "Automatic Storage Management Administrator's Guide"
doc_id: E18951-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e18951/asmfs_util010.htm
tags:
  - oracle
  - 11g
  - automatic-storage-management-administrators-guide
---

Table 13-73 contains a summary of the Oracle ACFS command utilities for multiple environments.

You can use `acfsutil` `help` on all platforms to display help text. You can run `acfsutil` `version` on all platforms to display the Oracle ACFS version.

When the options are entered with commands on a Windows platform, use `/` instead of `-` with the option. For example, you can display help for `acfsutil` on a Linux platform with `acfsutil` `-h`. On a Windows platform, use `acfsutil` `/h`.

Note that a mount point on a Windows operating system can be a drive letter or a directory including the drive letter.

Table 13-73 Summary of Oracle ACFS command utilities for multiple environments

| Command | Description |
| --- | --- |
| acfsdbg | Debugs an Oracle ACFS file system. |
| acfsutil info file | Displays information for a file in an Oracle ACFS file system. |
| acfsutil info fs | Displays detailed Oracle ACFS file system information. |
| acfsutil info id | Displays Oracle ACFS file system information for a given identifier and mount point. |
| acfsutil registry | Registers an Oracle ACFS file system with the Oracle ACFS mount registry. |
| acfsutil rmfs | Removes an Oracle ACFS file system. |
| acfsutil size | Resizes an Oracle ACFS file system. |
| acfsutil snap create | Creates a snapshot of an Oracle ACFS file system. |
| acfsutil snap delete | Deletes a snapshot of an Oracle ACFS file system. |
| acfsutil snap info | Displays information about Oracle ACFS file system snapshots. |
| acfsutil tune | Modifies or displays Oracle ACFS tunable parameters. |
| advmutil canonical | Displays the canonical name of an Oracle ADVM volume. |
| advmutil tune | Modifies or displays Oracle ADVM parameters. |
| advmutil volinfo | Displays information about Oracle ADVM volumes. |

## acfsdbg

Purpose

Debugs an Oracle ACFS file system.

Syntax and Description

  
`acfsdbg` `-h`  
`acfsdbg` \[`-r`\] \[`-l`\] `volume_device`  

Table 13-74 contains the options available with the `acfsdbg` command.

Table 13-74 Options for the acfsdbg command

| Option | Description |
| --- | --- |
| `-h` | Prints out the usage message which displays the various options that are available when invoking the `acfsdbg` command, then exits. |
| `-r` | Operates in read-only mode. No data is modified on the file system and all write commands are disabled. If the device is mounted anywhere, `acfsdbg` may not display the latest data because some of it is cached by the file system mounts. |
| `-l` | Processes kernel log files. The default is to not process the log files. |
| `volume_device` | Specifies the device name of the volume. |

`acfsdbg` is an extension to `fsck` and `acfschkdsk`, and is an interactive program that views and modifies on disk structures of the file system. This command is intended for experienced development and support engineers to examine on disk structures to diagnose problems. Use with caution.

When `acfsdbg` is started, it displays a command prompt. At the command prompt, you can enter the subcommands listed in Table 13-75.

You can also use `acfsdbg` for scripts by echoing `acfsdbg` subcommands with a shell pipe to the `acfsdbg` binary.

By default the file system is not modified when running the tool. If the `-l` option is used, the file system metadata in the transaction logs is applied before the interactive disk block dump session. The volume device must specify a volume with a dismounted Oracle ACFS file system. If the volume device has a mounted Oracle ACFS file system, `acfsdbg` displays an error message and exits.

You must be the administrator or a member of the Oracle ASM administrator group to run `acfsdbg`.

Subcommands

Table 13-75 lists the subcommands of `acfsdbg`.

Table 13-75 Subcommands for acfsdbg

| Option | Description | Syntax |
| --- | --- | --- |
| `calculate` | Calculates simple arithmetic expressions  Valid operators: + - \* / % & \| ^ ~ << >>  White space starts a new expression  0-1 represents a negative 1 | `calculate` \[`-v`\] `expr` \[…\]     `-v` Verbose mode   `expr` Simple 2+2 expression |
| `cksum` | Generates and replaces checksum in header  Header offset can be an expression as used by the `calculate` subcommand  White space starts a new header offset  Command is disabled in read-only mode | `cksum` \[`-C` \| `-CE`\] `header_offset` \[…\]     `-C` Regenerate for normal structure checksum   `-CE` Re-generate for Extent structure checksum   `header_offset` Offset of the on disk structure header. The value can be an expression as used by the `calculate` subcommand |
| `close` | Closes the open handle to the device | `close` |
| `echo` | Echoes text on command line to stdout | `echo` |
| `fenum` | Displays the specified File Entry TAble (FETA) entry | `fenum` \[`-f` \| `-e` \| `-d`\] `FETA_entry_number`     `-f` Displays all on disk structures related to this structure   `-e` Displays all on disk extent information related to this structure   `-d` Casts the structure as a directory and displays its contents   `FETA_entry_number` The File Entry Table number used to identify a file on the file system |
| `help` | Displays help message | `help` |
| `offset` | Displays structure at disk offset | `offset` \[`-c cast`\] \[`-f` \| `-d`\] `disk_offset`     `-f` Displays all on disk structures related to this structure   `-d` Casts the structure as a directory and displays its contents   `disk_offset` Disk offset to display. The value can be an expression as used by the `calculate` subcommand |
| `open` | Opens a handle to a device. The default is the volume device name entered on the command line | `open` \[`volume_device`\] |
| `primary` | Sets the context of commands to the primary file system | `primary` |
| `prompt` | Sets the prompt to the specified string | `prompt` " `prompt_string` " |
| `quit` | Exits the `acfsdbg` debugger command | `quit` |
| `read` | Reads value from offset  The default size to read in is 8 bytes  The default count to read is 1 | `read` \[`-1` \| `-2` \| `-4` \| `-8` \| `-s`\] \[`count`\] `offset`     `-1` Read byte value   `-2` Read 2 byte (short) value   `-4` Read 4 byte (int) value   `-8` Read 8 byte (long) value   `-s` Read null- terminated string   `count` Number of values to read. If not specified, the default is 1   `offset` Disk offset to read. The value can be an expression as used by the `calculate` subcommand |
| `snapshot` | Sets the context of commands to the specified snapshot | `snapshot` `snapshot_name` |
| `write` | Writes hexadecimal, octal, or decimal values at the disk offset, estimating how many bytes to write based on value size or number of digits in leading 0 hexadecimal values  The disk offset can be an expression used by the `calculate` subcommand  Numeric values can also be an expression as used by the `calculate` subcommand  This command is disabled in read-only mode | `write` \[`-1` \| `-2` \| `-4` \| `-8` \| `-c` \| `-s`\] \[`-C` \| `-CE`\] `offset` `value`     `-1` Write byte value   `-2` Write 2 byte (short) value   `-4` Write 4 byte (int) value   `-8` Write 8 byte (long) value   `-c` Write text (no null termination). Enclose string in single-quotes (')   `-s` Write null-terminated string. Enclose string in quotes (")   `-C` Regenerate normal structure checksum   `-CE` Regenerate extent structure checksum   `offset` Disk offset to write. The value can be an expression used by the `calculate` subcommand   `value` The value to write. If numeric, the value can be an expression as used by the `calculate` subcommand |

Examples

Example 13-65 shows the use of the `acfsdbg` subcommand.

Example 13-65 Using the acfsdbg command

```
$ /sbin/acfsdbg /dev/asm/voume1-123
acfsdbg: version                   = 11.2.0.3.0
Oracle ASM Cluster File System (ACFS) On-Disk Structure Version: 39.0
The ACFS volume was created at  Mon Mar  2 14:57:45 2011
acfsdbg> 

acfsbdg> calculate 60*1024
    61,440
    61440
    61440
    0xf000
    0170000
    1111:0000:0000:0000

acfsdbg> prompt "acfsdbg test>"
acfsdbg test>

echo "offset 64*1024" | acfsdbg /dev/asm/volume1-123
```

## acfsutil info file

Purpose

Displays information for a file in an Oracle ACFS file system.

Syntax and Description

  
`acfsutil` `info` `file` `-h`  
`acfsutil` `info` `file` `path`  

`acfsutil` `info` `file` `-h` displays help text and exits.

Table 13-76 contains the options available with the `acfsutil` `info` `file` command.

Table 13-76 Options for the acfsutil info file command

| Option | Description |
| --- | --- |
| `path` | Specifies the full path name of a file. |

The `acfsutil` `info` `file` command displays information about a file in an Oracle ACFS file system. The information includes the extent map which details the locations of the blocks comprising the file and the used versus allocated storage for a file. Tagging information is also displayed for a file.

You must have read access to the specified file to run `acfsutil` `info` `file`.

Examples

The following is an example of `acfsutil` `info` `file`.

Example 13-66 Using the acfsutil info file command

```
$ /sbin/acfsutil info file /u01/app/acfsmounts/myacfs/myfile
```

## acfsutil info fs

Purpose

Displays detailed Oracle ACFS file system information.

Syntax and Description

  
`acfsutil` `info` `fs` `-h`  
`acfsutil` `info` `fs` \[ { `-o` `item` | `-s` \[`interval` \[`count`\] \] } \] \[`mount_point`\]  

`acfsutil` `info` `fs` `-h` displays help text and exits.

Table 13-77 contains the options available with the `acfsutil` `info` `fs` command.

Table 13-77 Options for the acfsutil info fs command

| Option | Description |
| --- | --- |
| `-o` | Displays the specific file system item from the following list:  - `freespace` - Amount of free space available in the file system - `totalspace` - Size of the file system - `mountpoints` - Mount points associated with file systems. - `volumes` - Number of volumes associated with the file system - `primaryvolume` - Path name of the device associated with file system - `available` - Length of time the file system has been available - `isadvm` - 1 if an Oracle ADVM volume is present, 0 if not - `ismountpoint` - 1 if `path` is the mount point, 0 if `path` is not a mount point - `isavailable` - 1 if the file system is available, 0 if file system is not available - `iscorrupt` - 1 if the file system is corrupt, 0 if file system is not corrupt - `isreplprimary` - 1 if primary file system, 0 if not - `isreplstandby` - 1 if standby file system, 0 if not - `diskgroup` - Name of the disk group associated with `path` - `redundancy` - Type of redundancy used by the Oracle ADVM volume - `replication` - 1 if file system has been initialized for replication as the primary or standby file system, 0 if not initialized for replication - `resizeincrement` - Allocation unit size in bytes of the Oracle ADVM volume used by `path` - `stripewidth` - Stripe width for the Oracle ADVM volume used by `path` - `stripecolumns` - Stripe set columns for the Oracle ADVM volume used by `path` |
| `-s` \[`interval` \[`count`\]\] | Displays file system statistics.  The optional `interval` parameter specifies the amount of time in seconds between each report. The first report contains statistics for the time since the file system mount. Each subsequent report contains statistics collected during the interval since the previous report.  The optional `count` parameter can be specified in conjunction with the `interval` parameter. If the `count` parameter is specified, the value of count determines the number of reports generated at interval seconds apart.  If the `interval` parameter is specified without the `count` parameter, the command generates reports continuously until you break out of the command with `Ctrl+c`. |
| `mount_point` | Specifies the directory where the file system is mounted. Not a valid option for replication data. |

`acfsutil` `info` `fs` displays information and statistics about Oracle ACFS file systems. If replication has been initiated on a the file system, additional flags and status information are displayed. The values for the replication status field are primary, standby, or disabled.

The `-o` `item` option displays file system information for the `item` specified.

The `-s` option displays the amount and rate of change currently on a file system for the node that the command is run on.

With no option specified, the command displays file system information that includes the volume device name, the size of the file system, the amount of space available on the volume device, the file system mount time on this node, the state of the file system, the user specified block size, the number of Oracle ACFS snapshots, the space consumed by snapshots in the file system, and the optional name or volume label associated with the file system. The possible file system states are displayed in the `flags` line. These states include:

- `Offline` indicates that the underlying devices are not accessible, possibly due to an Oracle ASM instance failure, disk group forced dismount, or an irrecoverable I/O error. The file system on this node can only be dismounted. All other attempts at access result in errors.
- `Available` indicates that the file system is on line and operational.
- `Corrupt` indicates that the file system should be checked and repaired at the earliest possible convenience to correct a detected inconsistency. For example, run the `fsck` command on Linux or the `acfschkdsk` command on Windows to check and repair the file system. Ensure that you run the command in repair mode to correct the problem. For more information, refer to ["fsck"](asmfs_util002.md) and ["acfschkdsk"](asmfs_util005.md).

Any user can run `acfsutil` `info` `fs`.

Examples

The following are examples of the use of `acfsutil` `info` `fs`.

Example 13-67 displays information about an Oracle ACFS file system in a Linux environment.

Example 13-67 Using the acfsutil info fs command on Linux

```
$ /sbin/acfsutil info fs
/primary
    ACFS Version: 11.2.0.2.0
    flags:        MountPoint,Available,Replication
    mount time:   Mon Oct 25 12:11:03 2010
    volumes:      1
    total size:   5368709120
    total free:   4144230400
    primary volume: /dev/asm/pvol-74
        label:
        flags:                 Primary,Available,ADVM
        on-disk version:       40.0
        allocation unit:       4096
        major, minor:          252, 37889
        size:                  5368709120
        free:                  4144230400
        ADVM diskgroup         REPLDG
        ADVM resize increment: 268435456
        ADVM redundancy:       unprotected
        ADVM stripe columns:   4
        ADVM stripe width:     131072
    number of snapshots:  0
    snapshot space usage: 0
    replication status: primary

/standby
    ACFS Version: 11.2.0.2.0
    flags:        MountPoint,Available,Replication
    mount time:   Mon Oct 25 12:11:03 2010
    volumes:      1
    total size:   5368709120
    total free:   5263945728
    primary volume: /dev/asm/svol-74
        label:
        flags:                 Primary,Available,ADVM
        on-disk version:       40.0
        allocation unit:       4096
        major, minor:          252, 37890
        size:                  5368709120
        free:                  5263945728
        ADVM diskgroup         REPLDG
        ADVM resize increment: 268435456
        ADVM redundancy:       unprotected
        ADVM stripe columns:   4
        ADVM stripe width:     131072
    number of snapshots:  0
    snapshot space usage: 0
    replication status: standby

$ /sbin/acfsutil info fs -o mountpoints,replication
/primary
1
/standby
1

$ /sbin/acfsutil info fs -o mountpoints,isreplprimary
/primary
1
/standby
0

$ /sbin/acfsutil info fs -o mountpoints,isreplstandby
/primary
0
/standby
1
```

Example 13-68 illustrates the use of `acfsutil` `info` `fs` in a Windows environment.

Example 13-68 Using the acfsutil info fs command on Windows

```
C:\oracle>acfsutil info fs /o freespace c:\oracle\acfsmounts\acfs1
968667136

C:\oracle>acfsutil info fs /o totalspace c:\oracle\acfsmounts\acfs1
1073741824

C:\oracle>acfsutil info fs /o volume c:\oracle\acfsmounts\acfs1
1

C:\oracle>acfsutil info fs /o primaryvolume c:\oracle\acfsmounts\acfs1
asm-volume1-311

C:\oracle>acfsutil info fs /o diskgroup c:\oracle\acfsmounts\acfs1
DATA

C:\oracle>acfsutil info fs /o redundancy c:\oracle\acfsmounts\acfs1
mirror
```

Example 13-69 illustrates the use of `acfsutil` `info` `fs` with `-s` option to display the current amount and rate of change on a file system.

Example 13-69 Using the acfsutil info fs command with the -s option

```
$ /sbin/acfsutil info fs -s /u01/app/acfsmounts/myacfs
    amount of change since mount:       359.22 MB
    average rate of change since mount: 3 KB

$ /sbin/acfsutil info fs -s 60 4 /u01/app/acfsmounts/myacfs
    amount of change since mount:       359.22 MB
    average rate of change since mount: 3 KB/s

    amount of change: 15.02 MB   rate of change: 256 KB/s
    amount of change: 9.46 MB   rate of change: 161 KB/s
    amount of change: 7.32 MB   rate of change: 125 KB/s
    amount of change: 6.89 MB   rate of change: 117 KB/s
...
```

## acfsutil info id

Purpose

Displays Oracle ACFS file system information for a given identifier and mount point.

Syntax and Description

  
`acfsutil` `info` `id` `-h`  
`acfsutil` `info` `id` `num` `mount_point`  

`acfsutil` `info` `id` `-h` displays help text and exits.

Table 13-78 contains the options available with the `acfsutil` `info` `id` command.

Table 13-78 Options for the acfsutil info id command

| Option | Description |
| --- | --- |
| `mount_point` | Specifies the directory where the file system is mounted. |
| `num` | Specifies the Oracle ACFS file identifier number reported by the Oracle ACFS driver. The number should be specified in decimal format. |

`acfsutil` `info` `id` is used to translate an internal numeric Oracle ACFS file identifier to a path name in the file system. This is useful when the Oracle ACFS driver reports I/O errors to the system event logger associated with a particular file in an Oracle ACFS and identifies it by its internal identifier. You must have administrator privileges or you must be a member of the Oracle ASM administrator group to run `acfsutil` `info` `id`.

Examples

The following is an example of `acfsutil` `info` `id`.

Example 13-70 Using the acfsutil info id command

```
$ /sbin/acfsutil info id 117 /u01/app/acfsmounts/myacfs
```

## acfsutil registry

Purpose

Registers an Oracle ACFS file system with the Oracle ACFS mount registry.

Syntax and Description

  
`acfsutil` `registry` `-h`  
`acfsutil` `registry`  
`acfsutil` `registry` `-a` \[`-f`\] \[`-n` { `nodes` | `all` } \]  
 \[`-o` `moptions`\] `device` `mount_point`  
`acfsutil` `registry` `-d` { `device` | `mount_point` }  
`acfsutil` `registry` `-l` \[`device` | `mount_point`\]  
`acfsutil` `registry` `-m` `device`  

`acfsutil` `registry` `-h` displays help text and exits.

Table 13-79 contains the options available with the `acfsutil` `registry` command.

Table 13-79 Options for the acfsutil registry command

| Option | Description |
| --- | --- |
| `-a` | Specifies to add the device, mount point, and associated `moptions` to the Oracle ACFS mount registry. The Oracle ASM volume device specified must exist on the local node to add the information to the mount registry.  The arguments represent all the information needed to mount the file system. At Oracle ACFS startup time these file systems are automatically mounted. On Windows the volume mount points on the specified directories are created if they do not exist.  Duplicate device entries are not allowed. Duplicate mount points are allowed but must be include the `-n` option for disjoint node-specific mounts. |
| `-d` | Deletes the device or mount point from the Oracle ACFS mount registry. If a mount point is specified and it is not unique in the Oracle ACFS mount registry, the command fails and you must run the command again specifying the device as an argument. |
| `-f` | This is used in combination with `-a` when the specified device might exist in the registry and the administrator wants to replace the registration. |
| `-n` | This is used in combination with `-a` and specifies an optional comma-delimited list of nodes, or the `all` keyword. This specifies which nodes should attempt to mount this device on the specified mount point. Host names should be specified. The `all` keyword is functionally equivalent to not specifying a list of nodes and indicates that the device should be mounted on all nodes. Mounting on all nodes is the default behavior. |
| `-o` `moptions` | Specifies the mount options for use when mounting the file system. Valid for Linux, Solaris, and AIX. For specific `-o` `moptions`, refer to the `mount` command for each operating system. All the options for each operating system are available except the `all` option. |
| `-l` | Lists all the mount points currently in the registry on a single line, with fields separated by a colon (`:`). |
| `-m` | Lists the registered mount point, if one exists, associated with the specified device. The mount point is only returned if the Oracle ACFS file system has been registered or has been previously mounted. |
| `mount_point` | Specifies the directory where the file system is mounted. |
| `device` | Specifies an Oracle ACFS device file that has been formatted. |

`acfsutil` `registry` adds or deletes a file system from the Oracle ACFS persistent mount registry. The mount registry is a global registry that is used at Oracle ACFS startup on each node to mount all file systems specified in it. `root` or `asmadmin` privileges are required to modify the registry. For information about operating system group privileges, see ["About Privileges for Oracle ASM"](asminst.md).

Any user is allowed to display the contents of the registry. To mount all the file systems in the Oracle ACFS mount registry, use the platform specific mount command with the `all` option. This is done automatically at Oracle ACFS startup on each node.

If no options are specified, the command displays all of the Oracle ACFS mounts in the registry.

Note:

Do not register an Oracle ACFS file system that has had an individual file system Cluster Ready Services (CRS) resource added. For example, do not register a file system with `acfsutil` `registry` if the Oracle ACFS file system has been registered using `srvctl` `add` `filesystem`.

See ["About the Oracle ACFS Mount Registry"](asmfilesystem.md).

Examples

The following examples show the use of `acfsutil` `registry`. The first example shows how to add the volume device file and file system mount point to the registry. The second example shows how to list the registered mount point associated with the specified volume device file. The third example shows how to delete the specified volume device file from the registry.

Example 13-71 Using the acfsutil registry command

```
$ /sbin/acfsutil registry -a /dev/asm/volume1-123 /u01/app/acfsmounts/myacfs

$ /sbin/acfsutil registry -m /dev/asm/volume1-123

$ /sbin/acfsutil registry -d /dev/asm/volume1-123
```

## acfsutil rmfs

Purpose

Removes an Oracle ACFS file system.

Syntax and Description

  
`acfsutil` `rmfs` `-h`  
`acfsutil` `rmfs` `device`  

`acfsutil` `rmfs` `-h` displays help text and exits.

Table 13-80 contains the options available with the `acfsutil` `rmfs` command.

Table 13-80 Options for the acfsutil rmfs command

| Option | Description |
| --- | --- |
| `device` | Specifies an Oracle ACFS device file that has been formatted. |

`acfsutil` `rmfs` is used to remove an Oracle ACFS that is dismounted. When the command is run, the superblock of the file system is disabled. `root` or `asmadmin` privileges are required to run this command. For information about operating system group privileges, see ["About Privileges for Oracle ASM"](asminst.md).

After `acfsutil` `rmfs` runs successfully, the `MOUNTPATH` and `USAGE` columns in the `V$ASM_VOLUME` view are cleared for the device. The removed Oracle ACFS can be restored using `fsck` or `acfschkdsk`. The device can be reformatted with a new Oracle ACFS using the `mkfs` or `acfsformat` commands.

Examples

The following example shows the use of `acfsutil` `rmfs` to remove the specified volume device file and associated file system.

Example 13-72 Using the acfsutil rmfs command

```
$ /sbin/acfsutil rmfs /dev/asm/volume1-123
```

## acfsutil size

Purpose

Resizes an Oracle ACFS file system.

Syntax and Description

  
`acfsutil` `size` `-h`  
`acfsutil` `size` \[`+` | `-`\] `n` `[K` | `M` | `G` | `T|P` \] \[`device`\] `mount_point`  

`acfsutil` `size` `-h` displays help text and exits.

Table 13-81 contains the options available with the `acfsutil` `size` command.

Table 13-81 Options for the acfsutil size command

| Option | Description |
| --- | --- |
| \[`+` \| `-`\] `n` | Specifies the new size for the Oracle ACFS file system where `n` is a valid positive whole number greater than zero. The number can be preceded by a `+` or - to indicate the amount to add or decrease. If no operand exists, the new size is the absolute size. |
| `K` \| `M` \| `G` \| `T` \| `P` | Specifies that the integer supplied for size is in the units of `K` (Kilobytes), `M` (Megabytes), `G` (Gigabytes), `T` (Terabytes), or `P` (Petabytes). If the unit indicator is specified, then it must be appended to the integer. If omitted, the default unit is bytes. |
| `device` | Specifies the optional volume device file. |
| `mount_point` | Specifies the directory where the file system is mounted |

`acfsutil` `size` grows or shrinks the mounted Oracle ACFS and its underlying Oracle ADVM storage to match the new size specified. This operation also resizes the underlying Oracle ASM Volume file to match the new length that is specified. The disk group must have enough free storage to accommodate any requested increase to the file system size.

Reducing a file system size returns unused storage space located at the end of the file system to the disk group. Shrinking in this release is intended for accidents when the wrong initial size or resize increment was specified, and before the storage was actually used. After storage has been used for user data or file system metadata, it may not be possible to shrink the file system, even if the files using that storage have been deleted.

Note:

Defragmenting a file system is not supported in this release; only unused storage can be deallocated from the end of the file system.

The size value is rounded up based on the block size of the file system and the allocation unit of the Oracle ASM volume device file. To determine the Oracle ASM volume device resize increment, examine the `RESIZE_UNIT_MB` field in the `V$ASM_VOLUME` view, or look for `Resize` `Unit` in the output of `asmcmd` `volinfo` or `acfsutil` `info` `fs`.

There is a limit of 5 extents for the file system's internal storage bitmap. This causes any attempts to increase the file system to fail after it has been increased four or more times. However, if after increasing the file system four times or more times the file system size is decreased, then you may be able to increase the file system size again if the size of the increase is less than the size of the decrease.

When the limit on a file system expansion has been reached, running `fsck` or `acfschkdsk` with the `-a` option may consolidate the internal storage bitmap, allowing future file system expansion.

`root` or users who are members of the `asmadmin` group can run this command. For information about operating system group privileges, see ["About Privileges for Oracle ASM"](asminst.md).

Examples

The following example shows the use of `acfsutil` `size`. This example increases the primary device file of `/u01/app/acfsmounts/myacfs` file system by 500 MB.

Example 13-73 Using the acfsutil size command

```
$ /sbin/acfsutil size +500M /u01/app/acfsmounts/myacfs
```

## acfsutil snap create

Purpose

Creates a read-only or read-write snapshot of an Oracle ACFS file system.

Syntax and Description

  
`acfsutil` `snap` `create` `-h`  
`acfsutil` `snap` `create` \[`-r` | `-w`\] `snapshot` `mount_point`  

`acfsutil` `snap` `create` `-h` displays help text and exits.

Table 13-82 contains the options available with the `acfsutil` `snap` `create` command.

Table 13-82 Options for the acfsutil snap create command

| Option | Description |
| --- | --- |
| `-r` | Creates a read-only snapshot. This is the default setting. |
| `-w` | Creates a read-write snapshot. |
| `snapshot` | Specifies a name for the snapshot. The name provided must be a valid directory name. The`.ACFS/snaps` directory itself cannot be snapped. |
| `mount_point` | Specifies the directory where the file system is mounted. |

`acfsutil` `snap` `create` creates a read-only or read-write snapshot of the Oracle ACFS mounted on `mount_point`. You can specify `-r` for read-only or `-w` for read-write; read-only is the default if neither `-r` or `-w` are specified.

The read-write snapshot enables the fast creation of an Oracle ACFS snapshot image that can be both read and written without impacting the state of the Oracle ACFS file system hosting the snapshot images. The read-write functionality can be used for testing new versions of application software or running test scenarios on production file data without modifying the original file system.

Snapshots are not separate file systems. The snapshot appears in the `.ACFS/snaps/` `snapshot` directory and initially is a complete replica of the file system at the time the snapshot command was given. A read-only snapshot continues to preserve that initial point-in-time view. A read-write snapshot can be modified by updates written directly to the files located within the `.ACFS/snaps/` `snapshot` hierarchy.

Any user can access the snapshot directory by specifying the path name. However, the.`ACFS` directory itself is hidden from directory listings of the root of the file system. This prevents recursive commands, such as `rm` `-rf` or `acfsutil` `tag` `set` `-r`, from the root of the file system inadvertently operating on snapshot files.

Snapshots usually use very little storage initially as they share file system blocks with the original file system until a file changes.

Tools such as `du` report the total disk space usage of the snapshotted files, which includes the storage shared with the original versions of the files. To determine the total space used for the snapshots, use the `acfsutil` `snap` `info` or `acfsutil` `info` `fs` command. See "acfsutil info fs".

Oracle ACFS snapshots are immediately available for use after they are created. They are always online under the`.ACFS/snaps` directory when the original file system is mounted. No separate command is needed to mount them.

Administrator privileges are required to use this command or you must be a member of the Oracle ASM administrator group.

For more information about Oracle ACFS snapshots, see ["About Oracle ACFS Snapshots"](asmfilesystem.md).

Examples

Example 13-74 shows the use of the `acfsutil` `snap` `create` command.

Example 13-74 Using the acfsutil snap create command

```
$ acfsutil snap create -w midday_test1 /u01/critical_apps

$ acfsutil snap create -w midday_test2 /u01/critical_apps

$ /sbin/acfsutil snap create payroll_report1 /u01/critical_apps

$ /sbin/acfsutil snap create payroll_report2 /u01/critical_apps

$ ls /u01/critical_apps/.ACFS/snaps
midday_test1  midday_test2  payroll_report1  payroll_report2
```

## acfsutil snap delete

Purpose

Deletes a snapshot of an Oracle ACFS file system.

Syntax and Description

  
`acfsutil` `snap` `delete` `-h`  
`acfsutil` `snap` `delete` `snapshot` `mount_point`  

`acfsutil` `snap` `delete` `-h` displays help text and exits.

Table 13-83 contains the options available with the `acfsutil` `snap` `delete` command.

Table 13-83 Options for the acfsutil snap delete command

| Option | Description |
| --- | --- |
| `snapshot` | Specifies a name for the snapshot. |
| `mount_point` | Specifies the directory where the file system is mounted. |

`acfsutil` `snap` `delete` deletes the snapshot named `snapshot` in the Oracle ACFS mounted on `mount_point`. After successful completion of the command, the representation of the snapshot in the`.ACFS/snaps` directory is removed. The command fails if any file within the snapshot is open on any cluster node. Note that the disk space used by the snapshot being deleted is freed by a background task after the completion of the `acfsutil` `snap` `delete` command. If one of these background threads is running to clean up a deleted snapshot, then the `acfsutil` `snap` `info` command shows a pending delete operation.

Administrator privileges are required to use this command or you must be a member of the Oracle ASM administrator group.

Examples

Example 13-75 shows the use of the `acfsutil` `snap` `delete` command.

Example 13-75 Using the acfsutil snap delete command

```
$ /sbin/acfsutil snap delete midday_test1 /u01/critical_apps
acfsutil snap delete: Snapshot operation is complete.
```

## acfsutil snap info

Purpose

Displays information about Oracle ACFS file system snapshots.

Syntax and Description

  
`acfsutil` `snap` `info` `-h`  
`acfsutil` `snap` `info` \[`snapshot`\] `mount_point`  

`acfsutil` `snap` `info` `-h` displays help text and exits.

Table 13-84 contains the options available with the `acfsutil` `snap` `delete` command.

Table 13-84 Options for the acfsutil snap info command

| Option | Description |
| --- | --- |
| `snapshot` | Specifies a name for the snapshot. |
| `mount_point` | Specifies the directory where the file system is mounted. |

The `acfsutil` `snap` `info` command displays information about an individual specified snapshot or all snapshots in the specified Oracle ACFS file system. The snapshot name, snapshot type (RO or RW), and creation date and time are displayed.

The snapshot space usage amount includes snapshot metadata. If all the files are deleted from a snapshot, some of the metadata still remains and that amount is displayed with `acfsutil` `snap` `info`.

The `acfsutil` `snap` `info` command also shows pending delete operations.

Examples

Example 13-76 shows the use of the `acfsutil` `snap` `info` command when there is a pending delete operation. When the background process finishes the clean up of the deleted snapshot, the delete pending row does not appear in the output.

Example 13-76 Using the acfsutil snap info command

```
$ /sbin/acfsutil snap info /u01/critical_apps
snapshot name:               midday_test2
RO snapshot or RW snapshot:  RW
snapshot creation time:      Fri Feb 18 06:10:59 2011

snapshot name:               payroll_report1
RO snapshot or RW snapshot:  RO
snapshot creation time:      Tue Feb 22 06:56:34 2011

snapshot name:               payroll_report2
RO snapshot or RW snapshot:  RO
snapshot creation time:      Tue Feb 22 06:57:21 2011

    number of snapshots:  3 (active)
                          1 (delete pending)
    snapshot space usage: 8383348736
```

## acfsutil tune

Purpose

The `acfsutil` `tune` command displays the value of a specific tunable parameter or all Oracle ACFS tunable parameters, or sets the value of a tunable parameter in a persistent manner on a particular node.

Syntax and Description

  
`acfsutil` `tune` `-h`  
`acfsutil` `tune` \[`tunable_name`\]  
`acfsutil` `tune` `tunable_name` `=` `value`  

`acfsutil` `tune` `-h` displays help text and exits.

Table 13-85 contains the options available with the `acfsutil` `tune` command.

Table 13-85 Options for the acfsutil tune command

| Option | Description |
| --- | --- |
| `tunable_name` | Specifies the name of the tunable parameter. |
| `value` | Specifies the value for a tunable parameter. |

The only Oracle ACFS tunable parameter is `AcfsMaxOpenFiles`, which limits the number of open Oracle ACFS files on Windows and AIX. Normally you do not have to change the value of this tunable parameter; however, you may want to consider increasing the value if you have a large working set of files in your Oracle ACFS file systems.

Changing a tunable parameter has an immediate effect and persists across restarts. You must be a root user or the Windows `Administrator` to change the value of a tunable parameter.

Examples

The first example prints Oracle ACFS tunable parameters. The second example changes the value of a tunable parameter.

Example 13-77 Using the acfsutil tune command

```
$ /sbin/acfsutil tune

$ acfsutil tune AcfsMaxOpenFiles=50000
```

## advmutil canonical

Purpose

`advmutil` `canonical` displays the canonical name of the specified Oracle ADVM device name.

Syntax and Description

  
`advmutil` `-h`  
`advmutil` `canonical` `volume_device`  

`advmutil` `-h` displays help text and exits.

Table 13-86 contains the options available with the `advmutil` `canonical` command.

Table 13-86 Options for the advmutil canonical command

| Option | Description |
| --- | --- |
| `volume_device` | Specifies a string identifying a Oracle ADVM volume device. |

There are several different formats that can identify an Oracle ADVM volume device, but a normalized, unambiguous (canonical) name should be used when the volume device name is used with other commands such as `SRVCTL`.

For example, on the Windows operating system you can use the following prefixes with a volume device name: `\\.\`, `\??\`, `\\?\`

The `advmutil` `canonical` command would return the canonical name that another utility would recognize without having to strip off extra characters. The command would most likely be used in a script.

Examples

The following examples show the use of `advmutil` `canonical` on a Windows operating system. For each example, the command returns the canonical name of the volume device.

Example 13-78 Using advmutil canonical

```
[C:\]advmutil canonical asm-volume1-274
asm-volume1-274
 
[C:\]advmutil canonical \\.\asm-volume1-274
asm-volume1-274
 
[C:\]advmutil canonical \\?\asm-volume1-274
asm-volume1-274
 
[C:\]advmutil canonical \??\asm-volume1-274
asm-volume1-274
```

## advmutil tune

Purpose

`advmutil` `tune` displays the value of a specific Oracle ADVM parameter or sets the value of a specific Oracle ADVM parameter.

Syntax and Description

  
`advmutil` `-h`  
`advmutil` `tune` `parameter` \[`=` `value`\]  

`advmutil` `-h` displays help text and exits.

Table 13-87 contains the options available with the `advmutil` `tune` command.

Table 13-87 Options for the advmutil tune command

| Option | Description |
| --- | --- |
| `parameter` | Specifies the parameter for which you want to set or display the value. |
| `value` | Optional value provided to set the value of the specified parameter. |

If a value is not provided, the `advmutil` `tune` command displays the value that is currently assigned to the specified parameter.

The parameters that can be specified with `advmutil` `tune` are the maximum kernel memory (`max_memory`) or the maximum time in minutes for the deadlock timer (`deadlock_timer`).

The maximum kernel memory (`max_memory`) specifies the maximum operating system (OS) kernel memory in megabytes that can be consumed by the Oracle ASM Dynamic Volume Manager driver to cache Oracle ASM extent maps.

Note:

The `deadlock_timer` parameter should only be set by Oracle Support Services.

Examples

The first example sets the maximum kernel memory. The second example queries the current setting for the maximum kernel memory to be consumed by the Oracle ADVM. The third example changes the maximum time in minutes for the deadlock timer. The fourth example queries the current setting of a parameter.

Example 13-79 Using advmutil tune

```
$ /sbin/advmutil tune max_memory = 40

$ /sbin/advmutil tune max_memory
  max_memory = 40 (0x28)

$ /sbin/advmutil tune deadlock_timer = 20

$ /sbin/advmutil tune deadlock_timer
  deadlock_timer = 20 (0x14)
```

## advmutil volinfo

Purpose

`advmutil` `volinfo` displays information about Oracle ADVM volume devices.

Syntax and Description

  
`advmutil` `-h`  
`advmutil` `volinfo` \[`-l`\]\[`-L`\] \[`volume_device`\]  

`advmutil` `-h` displays help text and exits.

Table 13-88 contains the options available with the `advmutil` `volinfo` command.

Table 13-88 Options for the advmutil volinfo command

| Option | Description |
| --- | --- |
| `volume_device` | Specifies an optional volume device name. |
| `-l` | Separates the Oracle ADVM volume device information by field descriptions and colons on one line. |
| `-L` | Separates the Oracle ADVM volume device information by spaces on one line. |

`advmutil` `volinfo` displays information about Oracle ADVM volume devices in a list format by default. The `-l` option on Linux (`/l` on Windows) formats the display into a colon-separated string with field descriptions. The `-L` option on Linux (`/L` on Windows) formats the display into a space-separated string in a format suitable for scripting.

Examples

The first example displays information about an Oracle ADVM volume device, using the `advmutil` `volinfo` command with the volume device name. The second example displays information about the volume device using the `-l` option. The third example displays information about the volume device using the `-L` option.

Example 13-80 Using advmutil volinfo

```
$ /sbin/advmutil volinfo /dev/asm/volume1-123
Device : /dev/asm/volume1-228
Interface Version: 1
Size (MB): 256
Resize Increment (MB): 32
Redundancy: mirror
Stripe Columns: 4
Stripe Width (KB): 128
Disk Group: DATA
Volume: VOLUME1
Compatible.advm : 11.2.0.0.0

$ /sbin/advmutil volinfo -l /dev/asm/volume1-228
Device : /dev/asm/volume1-228 : Interface Version : 1 : Size (MB) : 256 : 
Resize Increment (MB) : 32 : Redundancy : mirror : Stripe Columns : 4 : 
Stripe Width (KB) : 128 : Disk Group : DATA : Volume : VOLUME1 : 
Compatible.advm : 11.2.0.0.0

$ /sbin/advmutil volinfo -L /dev/asm/volume1-228
/dev/asm/volume1-228  1  256 32  mirror  4  128  DATA  VOLUME1  11.2.0.0.0
```