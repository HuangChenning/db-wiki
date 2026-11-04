---
title: "Administrator's Guide"
book: "Advanced Cluster File System Administrator's Guide"
doc_id: F30297-04
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/acfsg/acfs-commands-solaris.html
tags:
  - oracle
  - 21c
  - advanced-cluster-file-system-administrators-guide
---

This topic provides a summary of the Oracle ACFS commands for Solaris.

Note:

If a disk group is dismounted with the force option on Solaris, any Oracle ADVM volumes device files that were on that disk group remain on the system. These files are removed when the disk group is remounted.

Table 6-7 lists the Oracle ACFS commands for Solaris with brief descriptions. The commands in Table 6-7 have been extended with additional options to support Oracle ACFS on Solaris.

Table 6-7 Summary of Oracle ACFS commands for Solaris

| Command | Description |
| --- | --- |
| fsck | Checks and repairs an Oracle ACFS file system on Solaris. |
| mkfs | Creates an Oracle ACFS file system on Solaris. |
| mount | Mounts an Oracle ACFS file system on Solaris. |
| umount/umountall | Dismounts an Oracle ACFS file system on Solaris. |

### fsck

Purpose

Checks and repairs an Oracle ACFS file system on the Solaris operating system.

Syntax and Description

```
fsck -F acfs -o h /dev/null
fsck -F acfs [{-n|N}|{-y|Y}] [-o options] volume_device
```

`fsck` `-F` `acfs` `-o` `h` `/dev/null` displays usage text and exits.

Table 6-8 contains the options available with the `fsck` command.

Table 6-8 Options for the Solaris fsck command

| Option | Description |
| --- | --- |
| `-F` `acfs` | Specifies the type of file system on Solaris. `acfs` designates the Oracle ACFS type. |
| `-n` \| `N` | Answers no to any prompts. |
| `-y` \| `Y` | Answers yes to any prompts. |
| `-o` | Specifies that options follow (a, f, h, v). Options are preceded with the `-o` flag and entered as a comma-delimited string. For example: `-o` `a,v`  - `a` 	Specifies to automatically fix the file system. - `f` 	Forces the file system into mountable state without completing a file system check or fix. - `h` 	Displays the usage text and exits. - `v` 	Specifies verbose mode. The progress is displayed as the operation occurs. Running in verbose mode can impact performance. |
| `volume_device` | Specifies an Oracle ADVM device file. |

`fsck` checks and repairs an existing Oracle ACFS file system. This command can only be run on a dismounted file system. `root` privileges are required to run `fsck`. The Oracle ACFS driver must be loaded for `fsck` to work.

By default, `fsck` only checks for and reports any errors. The `-o` `a` option must be specified to instruct `fsck` to fix errors in the file system. Do not interrupt `fsck` during the repair operation.

In a few cases, `fsck` prompts for questions before proceeding to check a file system. These cases include:

- If `fsck` detects that another `fsck` is in progress on the file system
- If `fsck` detects that the Oracle ACFS driver is not loaded
- If the file system does not appear to be Oracle ACFS

In checking mode, `fsck` also prompts if there are transaction logs that have not been processed completely due to an incomplete shutdown. To run in a non-interactive mode, include either the `-y` or `-n` options to answer yes or no to any questions.

`fsck` creates working files before it checks a file system. These working files are created in `/usr/tmp` if space is available. `/tmp` is used if `/usr/tmp` does not exist. If insufficient space is available in the `tmp` directory, `fsck` attempts to write to the current working directory. The files that `fsck` creates are roughly the size of the file system being checked divided by 32K. At most three such files are allocated. For example, a 2 GB file system being checked causes `fsck` to generate one to three 64K working files in the `/usr/tmp` directory. These files are deleted after `fsck` has finished.

In the event that `fsck` finds a file or directory in the file system for which it cannot determine its name or intended location (possibly due to a corruption in its parent directory), it places this object in the `/lost+found` directory when `fsck` is run in fix mode. For security reasons only the `root` user on Linux can read files in `/lost+found`. If the administrator can later determine the original name and location of the file based on its contents, the file can be moved or copied into its intended location.

The file names in the `/lost+found` directory are in the following formats:

```
parent.id.file.id.time-in-sec-since-1970
parent.id.dir.id.time-in-sec-since-1970
```

The `id` fields are the internal Oracle ACFS numeric identifiers for each file and directory in the file system.

You can use `acfsutil` `info` `id` `id` `mount_point` to attempt to determine the directory associated with `parent.``id`. This directory is assumed to be where the deleted object originated. For information about `acfsutil` `info`, see " [acfsutil info file](acfs-commands-utilities.md) ".

If the parent directory is not known, the parent `id` field is set to `UNKNOWN`.

Note:

It is not possible to see the contents of the `/lost+found` directory from a snapshot.

Examples

The following example shows how to check and repair an Oracle ACFS file system.

Example 6-8 Using the fsck command

```
# /usr/sbin/fsck -F acfs -y -o a /dev/asm/volume1-123
```

### mkfs

Purpose

Creates an Oracle ACFS file system on the Solaris operating system.

Syntax and Description

```
mkfs -F acfs -o h /dev/null
mkfs -F acfs [-o options] [-c release_version] volume_device [size]
```

`mkfs` `-F` `acfs` `-o` `h` `/dev/null` displays usage text and exits.

Table 6-9 contains the options available with the `mkfs` command.

Table 6-9 Options for the Solaris mkfs command

| Option | Description |
| --- | --- |
| `-F` `acfs` | Specifies the type of file system on Solaris. `acfs` designates the Oracle ACFS type. |
| `-o` `options` | Specifies that options follow (f, h, n, v). Options are preceded with the `-o` flag and entered as a comma-delimited string. For example: `-o` `f,v`  - `h` 	Displays the usage text and exits. - `f` 	Specifies the force option. This action creates the file system even if there is an existing Oracle ACFS on the volume device, although only if the file system is dismounted. This option overwrites structures on the original file system. Use this option with caution. - `i=512 \| i=4096` 	Specifies a file system with metadata block size of 512 or 4096 bytes. - `n` = `name` 	Specifies the name for the file system. A name can be a maximum of 64 characters. `acfsutil` `info` `fs` returns the name if one was specified. - `v` 	Specifies verbose mode. The progress is displayed as the operation occurs. |
| `-c` `release_version` | Creates an Oracle ACFS file system with Oracle ACFS release compatibility set to the value of release\_version. |
| `volume_device` | Specifies an Oracle ADVM device file. |
| `size` | Specifies the size of the file system in 512-byte units or in units of `K` \| `M` \| `G` \| `T` \| `P`. Units specified are in `K` (kilobytes), `M` (megabytes), `G` (gigabytes), `T` (terabytes), or `P` (petabytes). |

You can use `mkfs` to create the on disk structure needed for Oracle ACFS file system to be mounted. The `mkfs` command is the traditional Linux command used to build a file system. After `mkfs` runs successfully, the `USAGE` column in the `V$ASM_VOLUME` view displays `ACFS`. `root` privilege is not required. The ownership of the volume device file dictates who can run this command.

The value specified with the `-c release_version` option must be greater than or equal to the value of `COMPATIBLE.ADVM` for the disk group, and must be less than or equal to the running Oracle Grid infrastructure release version. If `—c release_version` is not specified, the value of `COMPATIBLE.ADVM` is used. After the compatibility is set, it cannot be downgraded. The `—c release_version` option can be used in situations where it is not possible, or desirable, to update `COMPATIBLE.ADVM` and `COMPATIBLE.ASM` for the disk group, but you want to use an Oracle ACFS feature that requires a compatibility increase. After the Oracle ACFS compatibility is updated, it is no longer possible to mount the file system with an older Oracle Grid infrastructure release. To change the compatibility of an existing file system, refer to “ [acfsutil compat set](acfs-commands-utilities.md) ”. For information about Oracle ASM disk group compatibility attributes, see [Oracle ACFS Features Enabled by Compatibility Attribute Settings](understand-acfs-admin.md).

The minimum file system size is 200 MB for the 512 byte metadata block size format and 512 MB for the 4 KB metadata block size format.

The Oracle ACFS driver must be loaded for `mkfs` to work.

The following list summarizes the use of the `-o i` option and metadata block size based on the value of the `COMPATIBLE.ADVM` disk group attribute.

- If `COMPATIBLE.ADVM` is set to `12.2` or greater, then the metadata block size is `4096` bytes by default.
- If `COMPATIBLE.ADVM` is set to less than `12.2`, then the block size is set to 512 bytes.
- If `COMPATIBLE.ADVM` is set to less than `12.2` and the logical sector size is not 512 bytes, then the command fails.

User data IO continues to support transfers as small as 512 bytes for normal user IO requests. When the Oracle ADVM volume of the file system has a logical disk sector size of 4 K, user Direct IO requests should be aligned on 4 K file offsets and be a multiple of 4 KB lengths for the best performance. Note that only 4 K metadata block size formats support ADVM volumes with 4 K logical disk sectors.

The `COMPATIBLE.ADVM` value must be set to `12.2` or greater to format an Oracle ADVM volume whose logical disk size is 4096 or to use the `-o i=4096` option to format an Oracle ADVM volume whose logical disk sector size is 512 bytes.

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

See [Managing Oracle ADVM with ASMCMD](manage-advm-asmcmd.md) .

Next create an Oracle ACFS file system on the volume device file.

Example 6-9 Using the mkfs command

```
$ /usr/sbin/mkfs -F acfs /dev/asm/volume1-123
```

### mount

Purpose

Mounts an Oracle ACFS file system on the Solaris operating system.

Syntax and Description

```
mount -F acfs -o h /tmp /dev/null
mount -F acfs [-r] [-o options] volume_device mount_point
```

`mount` `-F` `acfs` `-o` `h` `/tmp` `/dev/null` displays usage text and exits.

Table 6-10 contains the options available with the `mount` command.

Table 6-10 Options for the Solaris mount command

| Option | Description |
| --- | --- |
| `-F` `acfs` | Specifies the type of file system on Solaris. `acfs` designates the Oracle ACFS type. |
| `-r` | Mounts in read-only mode. |
| `-o` | Specifies that options follow. Options are preceded with the `-o` flag followed by a comma-delimited string of options. For example: `-o` `all,v`  The following options are available:  - `all` 	Reads the Oracle ACFS managed file systems in the Oracle Clusterware namespace, mounting all file systems with the `AUTO_START=always`. 	The `-o` `all` option requires two placeholders to satisfy the command arguments: a dummy argument for the volume device and any valid directory. 	When the `-o` `all` option is specified, other `-o` options are ignored. 	To specify mount options for a registry entry, include those options with the `acfsutil` `registry` command when you add the entry to the registry. - `devices` / `nodevices` 	Allows or disallows the opening of any character or block special devices from this mount. - `exec` / `noexec` 	Allows or disallows the execution of programs in this file system. - `h` 	Displays the usage help text and exits. - `rootsuid` / `norootsuid` 	Allows or disallows the execution of `setuid` to root executables (binaries by non-root users whose permissions allow set user Id execution, and are owned by root). `rootsuid` is the default action. If `norootsuid` is specified, an attempt to run these executables as a non-root user fails with a permission denied error. - `ro` 	Mounts the file system in read-only mode. - `rw` 	Mounts the file system in read-write mode. - `setuid` / `nosetuid` 	Allows or disallows the execution of `setuid` and `setgid` programs. - `suid` / `nosuid` 	Allows or disallows the execution of `setuid` and `setgid` programs and the opening of any character or block special devices from this mount. - `v` 	Specifies verbose mode. The progress is displayed as the operation occurs. |
| `volume_device` | Specifies an Oracle ADVM volume device file that has been formatted by `mkfs`. `device` is required but can be a dummy value. |
| `mount_point` | Specifies the directory where the file system is mounted. This directory must exist before you run the `mount` command. |

`mount` attaches a file system to the Oracle ACFS hierarchy at the mount point that is the name of a directory. The mount occurs on the node where the mount command was issued. The mount command returns an error if the file system is not in a dismounted state on this node.

It is not always possible to return the cause of a mount failure to the `mount` command. When this happens Oracle ACFS writes the cause of the failure to the system console and associated system log file.

After `mount` runs successfully, the `MOUNTPATH` field in the `V$ASM_VOLUME` view displays the directory name on which the file system is now mounted.

An Oracle ACFS file system should only be mounted on one mount point. The same mount point name should be used on all cluster members.

`root` privilege is required to run `mount`.

Examples

The first example shows how to mount `volume1-123` on the mount point `/acfsmounts/acfs1`. The second example shows how to mount all the registered Oracle ACFS file systems. Placeholder arguments must be provided for the volume device name and mount point when specifying the `-o` `all` option. The volume device can be a dummy value, such as `none`. Any valid directory can be specified for the mount point, such as `/tmp`.

Example 6-10 Using the mount command

```
# /sbin/mount -F acfs /dev/asm/volume1-123 /acfsmounts/acfs1

# /sbin/mount -F acfs -o all none /tmp
```

### umount/umountall

Purpose

Dismounts an Oracle ACFS file system on the Solaris operating system.

Syntax and Description

```
umount -V [mount_point | volume_device]
umountall -F acfs
```

`unmountall` `-F` `acfs` dismounts all Oracle ACFS file systems.

Table 6-11 contains the options available with the `umount` command.

Table 6-11 Options for the Solaris umount command

| Option | Description |
| --- | --- |
| `-V` | Echoes the complete command line, but does not run the command. Use this option to verify and validate the command line before execution. Valid only with `umount`. |
| `mount_point` | Specifies the directory where the file system is mounted. Valid only with `umount`. |
| `volume_device` | Specifies the Oracle ADVM volume device name associated with the file system. Valid only with `umount`. |
| `-F` `acfs` | Specifies the type of file system on Solaris. `acfs` designates the Oracle ACFS type. Valid only with `umountall`. |

`umount` and `umountall` detach an Oracle ACFS from the file system hierarchy on the current node.

The `umount` and `umountall` commands do not return control back to the operating system prompt until the file system has been completely unmounted.

If a file system is busy, `umount` and `umountall` fail.

`root` privileges are required to run the `umount` and `umountall` commands.

Examples

The following examples show how to dismount an Oracle ACFS file system. The first example specifies the mount point of the file system to dismount. The second example specifies the volume device associated with the file system to dismount. The third example dismounts all Oracle ACFS file systems.

Example 6-11 Using the umount command

```
# /sbin/umount /dev/asm/volume1-123

# /sbin/umount /acfsmounts/acfs1

# /sbin/umountall -F acfs
```