---
title: Oracle ACFS Command-line Tools for Linux and UNIX Environments
book: "Automatic Storage Management Administrator's Guide"
doc_id: E18951-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e18951/asmfs_util002.htm
tags:
  - oracle
  - 11g
  - automatic-storage-management-administrators-guide
---

Table 13-1 contains a summary of the Oracle ACFS commands for Linux and UNIX. The commands in Table 13-1 have been extended with additional options to support Oracle ACFS. All other Linux and UNIX file system commands operate without change for Oracle ACFS.

For example, Oracle ACFS adds a set of Oracle ACFS-specific mount options to those provided with the base operating system platform. You should review both the mount options for the Linux and UNIX platforms in addition to the Oracle ACFS-specific options for the complete set of file system mount options.

File systems on Oracle ADVM volumes that are not Oracle ACFS file systems, such as `ext3`, are managed with the same Linux commands that are listed in Table 13-1 using the file-specific options for the type of file system. You can refer to the `man` pages for options available for the Linux commands in Table 13-1.

Note:

Security-Enhanced Linux (SELinux) is not supported on Oracle ACFS file systems.

Table 13-1 Summary of Oracle ACFS commands for Linux and UNIX

| Command | Description |
| --- | --- |
| fsck | Checks and repairs an Oracle ACFS file system. |
| mkfs | Creates an Oracle ACFS file system. |
| mount | Mounts an Oracle ACFS file system. |
| umount | Dismounts an Oracle ACFS file system. |

## fsck

Purpose

Checks and repairs an Oracle ACFS file system.

Syntax and Description

  
`fsck` `-t` `acfs` `-h` `/dev/null`  
`fsck` \[`-a` | `-f`\] \[`-v`\] \[`-vv`\] `-t` `acfs` \[`-n` | `-y`\] `volume_device`  

`fsck` `-t` `acfs` `-h` dev/null displays usage text and exits.

Table 13-2 contains the options available with the `fsck` command.

Table 13-2 Options for the Linux fsck command

| Option | Description |
| --- | --- |
| `-a` | Specifies to automatically repair the file system. |
| `-f` | Forces the file system into mountable state without completing a file system check or repair. |
| `-v` | Specifies verbose mode. The progress is displayed as the operation occurs. |
| `-vv` | Specifies very verbose mode. The progress is displayed as the operation occurs. |
| `-h` | Displays the usage help text and exits. |
| `-n` | Answers no to any prompts. |
| `-y` | Answers yes to any prompts. |
| `volume_device` | Specifies the primary Oracle ADVM volume device. |

`fsck` checks and repairs an existing Oracle ACFS. This command can only be run on a dismounted file system. `root` privileges are required to run `fsck`. The Oracle ACFS driver must be loaded for `fsck` to work.

By default, `fsck` only checks for and reports any errors. The `-a` flag must be specified to instruct `fsck` to repair errors in the file system.

In a few cases, `fsck` prompts for questions before proceeding to check a file system. These cases include:

- If `fsck` detects that another `fsck` is in progress on the file system
- If `fsck` detects that the Oracle ACFS driver is not loaded
- If the file system does not appear to be Oracle ACFS

In checking mode, `fsck` also prompts if there are transaction logs that have not been processed completely due to an incomplete shutdown. To run in a non-interactive mode, include either the `-y` or `-n` options to answer yes or no to any questions.

`fsck` creates working files before it checks a file system. These working files are created in `/usr/tmp` if space is available. `/tmp` is used if `/usr/tmp` does not exist. If insufficient space is available in the `tmp` directory, `fsck` attempts to write to the current working directory. The files that `fsck` creates are roughly the size of the file system being checked divided by 32K. At most two such files are allocated. For example, a 2 GB file system being checked causes `fsck` to generate one or two 64K working files in the `/usr/tmp` directory. These files are deleted after `fsck` has finished.

In the event that `fsck` finds a file or directory in the file system for which it cannot determine its name or intended location (possibly due to a corruption in its parent directory), it places this object in the `/lost+found` directory when `fsck` is run in fix mode. For security reasons only the `root` user on Linux can read files in `/lost+found`. If the administrator can later determine the original name and location of the file based on its contents, the file can be moved or copied into its intended location.

The file names in the `/lost+found` directory are in the following formats:

```
parent.id.file.id.time-in-sec-since-1970
parent.id.dir.id.time-in-sec-since-1970
```

The `id` fields are the internal Oracle ACFS numeric identifiers for each file and directory in the file system.

You can use `acfsutil` `info` `id` `id` `mount_point` to attempt to determine the directory associated with `parent.``id`. This directory is assumed to be where the deleted object originated. For information about `acfsutil` `info`, see ["acfsutil info file"](asmfs_util010.md).

If the parent directory is not known, the parent `id` field is set to `UNKNOWN`.

Note:

It is not possible to see the contents of the `/lost+found` directory from a snapshot.

Examples

The following example shows how to check and repair an Oracle ACFS file system.

Example 13-1 Using the fsck command

```
# /sbin/fsck -a -v -y -t acfs /dev/asm/volume1-123
```

## mkfs

Purpose

Creates an Oracle ACFS file system.

Syntax and Description

  
`mkfs` `-t` `acfs` `-h`  
`mkfs` \[`-v`\] \[`-f`\] `-t` `acfs` \[`-b` `blocksize`\] \[`-n` `name` \] `volume_device` \[`size`\]  

`mkfs` `-t` `acfs` `-h` displays usage text and exits.

Table 13-3 contains the options available with the `mkfs` command.

Table 13-3 Options for the Linux mkfs command

| Option | Description |
| --- | --- |
| `-t` `acfs` | Specifies the type of file system on Linux. `acfs` designates the Oracle ACFS type. |
| `-v` | Specifies verbose mode. The progress is displayed as the operation occurs. |
| `-n` `name` | Specifies the name for the file system. A name can be a maximum of 64 characters. `acfsutil` `info` `fs` returns the name if one was specified. |
| `-f` | Specifies the force option. This action creates the file system even if there is an existing Oracle ACFS on the volume device, although only if the file system is dismounted. This option overwrites structures on the original file system. Use this option with caution. |
| `-h` | Displays the usage help text and exits. |
| `-b` `blocksize` | The default block size is 4K and this is the only size supported in 11g Release 2 (11.2). |
| `size` | Specifies the size that the file system should consume on the named device. The quantity specified can be in units of `K` (kilobytes), `M` (megabytes), `G` (gigabytes), `T` (terabytes), or `P` (petabytes). If a unit is not specified, the default is bytes.  If the size specified is not a multiple of the block size, then the value is rounded up to the closest multiple. If this option is not specified, the entire device is consumed. |
| `volume_device` | Specifies an Oracle ADVM device file that is to be formatted. |

`mkfs` is used to create the on disk structure needed for Oracle ACFS file system to be mounted. The `mkfs` command is the traditional UNIX command used to build a file system. After `mkfs` runs successfully, the `USAGE` column in the `V$ASM_VOLUME` view displays `ACFS`. `root` privilege is not required. The ownership of the volume device file dictates who can run this command. The minimum file system size is 200 MB. The Oracle ACFS driver must be loaded for `mkfs` to work.

Examples

Before creating an Oracle ACFS file system, first determine which Oracle ADVM volume devices are available. You can use the ASMCMD `volinfo` command to display information about the volumes and volume devices.

```
ASMCMD [+] > volinfo -a
...
         Volume Name: VOLUME1
         Volume Device: /dev/asm/volume1-123
         State: ENABLED
...
```

See ["volinfo"](asm_util007.md).

Next create an Oracle ACFS file system on the volume device file.

Example 13-2 Using the mkfs command

```
$ /sbin/mkfs -t acfs /dev/asm/volume1-123
```

## mount

Purpose

Mounts an Oracle ACFS file system.

Syntax and Description

  
`mount` `-h`  
`mount` \[`-v`\] `-t` `acfs` \[`-o` `options`\] `volume_device` `mount_point`  
`mount`  

`mount` `-h` displays usage text and exits.

Table 13-4 contains the options available with the `mount` command.

Table 13-4 Options for the Linux mount command

| Option | Description |
| --- | --- |
| `-h` | Displays the usage help text and exits. |
| `-t` `acfs` | Specifies the type of file system on Linux. `acfs` designates the Oracle ACFS type. |
| `-v` | Specifies verbose mode. The progress is displayed as the operation occurs. |
| `-o` | Options are specified with the `-o` flag followed by a comma-delimited string of options. The following options are available:  - `all` 	Reads the Oracle ACFS mount registry created with the `acfsutil` `registry` command and mounts the file systems in it. A `mount` `-t` `acfs` `-o` `all` command is automatically run at Oracle ACFS startup. 	When the `-o` `all` option is specified, other `-o` options are ignored. To specify mount options for a registry entry, include those options with the `acfsutil` `registry` command when you add the entry to the registry. - `ro` 	Mounts the file system in read-only mode. - `norootsuid` 	Fails the execution of binaries by non-root users whose permissions allow set user Id execution, and are owned by root. An attempt to run these executables as a non-root user fails with a permission denied error. - `rootsuid` 	Allows the execution of binaries by non-root users of set user Id files owned by root. This is the default action. |
| `volume_device` | Specifies an Oracle ADVM volume device file that has been formatted by `mkfs`. `device` is required but can be a dummy value. |
| `mount_point` | Specifies the directory where the file system is mounted. This directory must exist before you run the `mount` command. |

`mount` attaches a file system to the Oracle ACFS hierarchy at the mount point that is the name of a directory. The mount happens on the node where the mount command was issued. The mount command returns an error if the file system is not in a dismounted state on this node.

It is not always possible to return the cause of a mount failure to the `mount` command. When this happens Oracle ACFS writes the cause of the failure to the system console and associated system log file.

After `mount` runs successfully, the `MOUNTPATH` field in the `V$ASM_VOLUME` view displays the directory name on which the file system is now mounted.

An Oracle ACFS file system should only be mounted on one mount point. The same mount point name should be used on all cluster members.

The `mount` command lists all mounted file systems if it is run with no parameters.

`root` privilege is required to run `mount`.

Examples

The first example shows how to mount `volume1-123` on the mount point `/u01/app/acfsmounts/myacfs`. The second example shows how to mount all the registered Oracle ACFS file systems. The dummy names (`none`) have been entered for the device and directory as they are required, but not used, when the `all` option is specified.

Example 13-3 Using the mount command

```
# /bin/mount -t acfs /dev/asm/volume1-123 /u01/app/acfsmounts/myacfs

# /bin/mount -t acfs -o all none none
```

## umount

Purpose

Dismounts an Oracle ACFS file system.

Syntax and Description

  
`umount` `-h`  
`umount` \[`-v`\] `volume_device` | `mount_point`  
`umount` `-a` `[-t` `acfs`\]  

`umount` `-h` displays usage text and exits.

Table 13-5 contains the options available with the `umount` command.

Table 13-5 Options for the Linux umount command

| Option | Description |
| --- | --- |
| `-h` | Displays the usage help text and exits. |
| `-t` `acfs` | Specifies the type of file system on Linux. `acfs` designates the Oracle ACFS type. |
| `-v` | Specifies verbose mode. The progress is displayed as the operation occurs. |
| `-a` | Specifies to dismount all Oracle ACFS file systems on this node. |
| `volume_device` | Specifies an Oracle ADVM volume device file that has been formatted by `mkfs`. |
| `mount_point` | Specifies the directory where the file system is mounted. This directory must exist before you run the `mount` command. |

`umount` detaches an Oracle ACFS from the file system hierarchy on the current node. If the file system is busy, `umount` fails.

`root` privileges are required to run the `umount` command.

Examples

The following examples show how to dismount an Oracle ACFS file system. The first example uses the volume device file and the second example uses the file system.

Example 13-4 Using the umount command

```
# /bin/umount /dev/asm/volume1-123

# /bin/umount /u01/app/acfsmounts/myacfs
```