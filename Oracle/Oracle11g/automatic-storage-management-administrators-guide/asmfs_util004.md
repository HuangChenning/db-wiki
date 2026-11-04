---
title: Oracle ACFS Command-line Tools for the AIX Environment
book: "Automatic Storage Management Administrator's Guide"
doc_id: E18951-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e18951/asmfs_util004.htm
tags:
  - oracle
  - 11g
  - automatic-storage-management-administrators-guide
---

During the installation of Oracle ACFS and Oracle ADVM with Oracle Grid Infrastructure on AIX, several system security classes (authorizations) are created for Oracle ACFS and Oracle ADVM operations. These authorizations enable the following operations:

- Configuration of Oracle ACFS and Oracle ADVM devices
- Removal of Oracle ACFS and Oracle ADVM devices
- Definition of Oracle ACFS and Oracle ADVM devices

These authorizations are collected in a role (`oracle_devmgmt`) which is assigned by default to the Oracle Grid Infrastructure user and Oracle ASM administrator. You can run the `lsrole` or `rolelist` command after installation to see this new role. These commands can be run at any time to ensure that the user has the proper authorization to manage Oracle ACFS and Oracle ADVM.

For example, run the following as the Oracle ASM administrator:

```
$ rolelist -e
 oracle_devmgmt
```

After the initial installation on an AIX operating system, the shell from which the root script was run will not inherit the new role. If the role is not present for the user, then the `swrole` command must be run before performing Oracle ACFS or Oracle ADVM operations.

For example, run the following as the Oracle ASM administrator:

```
$ swrole oracle_devmgmt
```

Alternatively, you can open a new shell to perform Oracle ACFS or Oracle ADVM operations.

During the removal of Oracle Grid Infrastructure, the `oracle_devmgmt` role and its associated authorizations are deleted from the system.

See Also:

Oracle Grid Infrastructure on AIX, refer to [Oracle Grid Infrastructure Installation Guide for AIX Based Systems](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=GINST) for more information about installing

Note:

If a disk group is dismounted with the force option on AIX, any Oracle ADVM volumes device files that were on that disk group remain on the system. These files are removed when the disk group is remounted.

Table 13-11 contains a summary of the Oracle ACFS commands for the AIX operating system. The commands in Table 13-11 have been extended with additional options to support Oracle ACFS on AIX.

Table 13-11 Summary of Oracle ACFS commands for AIX

| Command | Description |
| --- | --- |
| fsck | Checks and repairs an Oracle ACFS file system on AIX. |
| mkfs | Creates an Oracle ACFS file system on AIX. |
| mount | Mounts an Oracle ACFS file system on AIX. |
| umount/umountall | Dismounts an Oracle ACFS file system on AIX. |

## fsck

Purpose

Checks and repairs an Oracle ACFS file system on the AIX operating system.

Syntax and Description

  
`fsck` `-V` `acfs` \[`-n` | `-y`\] \[`-o` `options`\] `volume_device`  

Table 13-12 contains the options available with the AIX `fsck` command.

Table 13-12 Options for the AIX fsck command

| Option | Description |
| --- | --- |
| `-V` `acfs` | Specifies an Oracle ADVM volume on AIX. `acfs` designates the Oracle ACFS type. |
| `-n` | Answers no to any prompts. |
| `-y` | Answers yes to any prompts. |
| `-o` `options` | Specifies that options follow (a, f, v). Options are preceded with the `-o` flag and entered as a comma-delimited string. For example: `-o` `a,v`  - `a` 	Specifies to automatically fix the file system. - `f` 	Forces the file system into mountable state without completing a file system check or fix. - `v` 	Specifies verbose mode. The progress is displayed as the operation occurs. - `vv` 	Specifies very verbose mode. The progress is displayed as the operation occurs. |
| `volume_device` | Specifies the primary Oracle ADVM volume device. |

`fsck` checks and repairs an existing Oracle ACFS. This command can only be run on a dismounted file system. `root` privileges are required to run `fsck`. The Oracle ACFS driver must be loaded for `fsck` to work.

By default, `fsck` only checks for and reports any errors. The `-a` flag must be specified to instruct `fsck` to fix errors in the file system.

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

Example 13-9 Using the fsck command

```
# /usr/sbin/fsck -V acfs -y -o a,v /dev/asm/volume1-123
```

## mkfs

Purpose

Creates an Oracle ACFS file system on the AIX operating system.

Syntax and Description

  
`mkfs` `-V` `acfs` `-o` `h` `/dev/null`  
`mkfs` `-V` `acfs` \[`-v` `name` \] \[`-s` `size`\]\[`-o` `options`\] `volume_device`  

`mkfs` `-V` `acfs` `-o` `h` `/dev/null` displays usage text and exits.

Table 13-13 contains the options available with the AIX `mkfs` command.

Table 13-13 Options for the AIX mkfs command

| Option | Description |
| --- | --- |
| `-V` `acfs` | Specifies the type of file system on AIX. `acfs` designates the Oracle ACFS type. |
| `-v` `name` | Specifies the name for the file system. A name can be a maximum of 64 characters. `acfsutil` `info` `fs` returns the name if one was specified. |
| `-s` `size` | Specifies the size of the file system in 512-byte units or in units of `K` \| `M` \| `G` \| `T` \| `P`. Units specified are in `K` (kilobytes), `M` (megabytes), `G` (gigabytes), `T` (terabytes), or `P` (petabytes). |
| `-o` `options` | Specifies that options follow (b, f, h, v). Options are preceded with the `-o` flag and entered as a comma-delimited string. For example: `-o` `f,v`  - `b=` `blocksize` 	Specifies the block size of the new file system. The default block size is 4K and this is the only size supported. - `f` 	Specifies the force option. This action creates the file system even if there is an existing Oracle ACFS on the volume device, although only if the file system is dismounted. This option overwrites structures on the original file system. Use this option with caution. - `h` 	Displays the usage text and exits. - `v` 	Specifies verbose mode. The progress is displayed as the operation occurs. |
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

Example 13-10 Using the mkfs command

```
$ /usr/sbin/mkfs -V acfs /dev/asm/volume1-123
```

## mount

Purpose

Mounts an Oracle ACFS file system on the AIX operating system.

Syntax and Description

  
`mount` `-V` `acfs` `-o` `h` `/dev/null` `/xxx`  
`mount` `-v` `acfs` \[`-o` `options`\] `volume_device` `mount_point`  

`mount` `-V` `acfs` `-o` `h` `/dev/null` `/xxx` displays usage text and exits.

Table 13-14 contains the options available with the `mount` command.

Table 13-14 Options for the AIX mount command

| Option | Description |
| --- | --- |
| `-v` `acfs` | Specifies the type of file system on AIX. `acfs` designates the Oracle ACFS type. |
| `-o` `options` | Specifies that options follow. Options are preceded with the `-o` flag followed by a comma-delimited string of options. For example: `-o` `all,ro,v`  The following options are available:  - `all` 	Reads the Oracle ACFS mount registry created with the `acfsutil` `registry` command and mounts the file systems in it. A `mount` `-V` `acfs` `-o` `all` command is automatically run at Oracle ACFS startup. 	The `-o` `all` option requires two placeholders to satisfy the command arguments: a dummy argument for the volume device and directory. 	When the `-o` `all` option is specified, other `-o` options are ignored. To specify mount options for a registry entry, include those options with the `acfsutil` `registry` command when you add the entry to the registry. - `h` 	Displays the usage help text and exits. - `nosuid` 	Specifies that the execution of `setuid` and `setgid` programs by way of this mount is not allowed. - `nodev` 	Specifies that you cannot open devices from this mount. - `norootsuid` 	Fails the execution of binaries by non-root users whose permissions allow set user Id execution, and are owned by root. An attempt to run these executables as a non-root user fails with a permission denied error. - `rootsuid` 	Allows the execution of binaries by non-root users of set user Id files owned by root. This is the default action. - `ro` 	Mounts the file system in read-only mode. - `rw` 	Mounts the file system in read-write mode. - `v` 	Specifies verbose mode. The progress is displayed as the operation occurs. |
| `volume_device` | Specifies an Oracle ADVM volume device file that has been formatted by `mkfs`. `device` is required but can be a dummy value. |
| `mount_point` | Specifies the directory where the file system is mounted. This directory must exist before you run the `mount` command. |

`mount` attaches a file system to the Oracle ACFS hierarchy at the mount point that is the name of a directory. The mount happens on the node where the mount command was issued. The mount command returns an error if the file system is not in a dismounted state on this node.

It is not always possible to return the cause of a mount failure to the `mount` command. When this happens Oracle ACFS writes the cause of the failure to the system console and associated system log file.

After `mount` runs successfully, the `MOUNTPATH` field in the `V$ASM_VOLUME` view displays the directory name on which the file system is now mounted.

An Oracle ACFS file system should only be mounted on one mount point. The same mount point name should be used on all cluster members.

`root` privilege is required to run `mount`.

Examples

The first example shows how to mount `volume1-123` on the mount point `/u01/app/acfsmounts/myacfs`. The second example shows how to mount all the registered Oracle ACFS file systems. The dummy names (`none`) have been entered as placeholders for the device and directory as these arguments are required, but not used, when the `all` option is specified.

Example 13-11 Using the mount command

```
# /usr/sbin/mount -v acfs /dev/asm/volume1-123 /u01/app/acfsmounts/myacfs

# /usr/sbin/mount -v acfs -o all none none
```

## umount/umountall

Purpose

Dismounts an Oracle ACFS file system on the AIX operating system.

Syntax and Description

  
`umount` \[`mount_point` | `volume_device`\]  
`umountall` `-F` `acfs`  

`unmountall` `-F` `acfs` dismounts all Oracle ACFS file systems.

Table 13-15 contains the options available with the `umount` command.

Table 13-15 Options for the AIX umount command

| Option | Description |
| --- | --- |
| `mount_point` | Specifies the directory where the file system is mounted. Valid only with `umount`. |
| `volume_device` | Specifies the Oracle ADVM volume device name associated with the file system. Valid only with `umount`. |
| `-F` `acfs` | Specifies the type of file system on AIX. `acfs` designates the Oracle ACFS type. Valid only with `umountall`. |

`umount` and `umountall` detach an Oracle ACFS from the file system hierarchy on the current node. If a file system is busy, `umount` and `umountall` fail.

`root` privileges are required to run the `umount` and `umountall` commands.

Examples

The following examples show how to dismount an Oracle ACFS file system. The first example specifies the mount point of the file system to dismount. The second example specifies the volume device associated with the file system to dismount. The third example dismounts all Oracle ACFS file systems.

Example 13-12 Using the umount command

```
# /usr/sbin/umount /dev/asm/volume1-123

# /usr/sbin/umount /u01/app/acfsmounts/myacfs

# /usr/sbin/umountall -F acfs
```