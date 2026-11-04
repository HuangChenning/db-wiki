---
title: "Administrator's Guide"
book: "Advanced Cluster File System Administrator's Guide"
doc_id: F30297-04
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/acfsg/acfs-commands-linux.html
tags:
  - oracle
  - 21c
  - advanced-cluster-file-system-administrators-guide
---

This topic provides a summary of the Oracle ACFS commands for Linux environments.

Table 6-1 lists the Oracle ACFS commands for Linux environments with brief descriptions. The commands in Table 6-1 have been extended with additional options to support Oracle ACFS. All other Linux file system commands operate without change for Oracle ACFS.

For example, Oracle ACFS adds a set of Oracle ACFS-specific mount options to those provided with the base operating system platform. You should review both the mount options for the Linux platforms in addition to the Oracle ACFS-specific options for the complete set of file system mount options.

File systems on Oracle ADVM volumes that are not Oracle ACFS file systems, such as `ext3`, are managed with the same Linux commands that are listed in Table 6-1 using the file-specific options for the type of file system. You can refer to the `man` pages for options available for the Linux commands in Table 6-1.

Note:

When using Security-Enhanced Linux (SELinux) in enforcing mode with Oracle ACFS, ensure that the Oracle ACFS file systems are mounted with an SELinux default context. Refer to your Linux vendor documentation for information about the context mount option.

Table 6-1 Summary of Oracle ACFS commands for Linux environments

| Command | Description |
| --- | --- |
| fsck (offline mode) | Checks and repairs a dismounted Oracle ACFS file system. |
| fsck (online mode) | Checks and repairs a mounted Oracle ACFS file system. |
| mkfs | Creates an Oracle ACFS file system. |
| mount | Mounts an Oracle ACFS file system. |
| umount | Dismounts an Oracle ACFS file system. |

### fsck (offline mode)

Purpose

Checks and repairs a dismounted Oracle ACFS file system.

Syntax and Description

```
fsck -t acfs -h /dev/null
fsck [-a|-f] [-v]  -t acfs [-n|-y] [-x file_name] volume_device
```

`fsck` `-t` `acfs` `-h` `/dev/null` displays usage text and exits.

Table 6-2 contains the options available with the `fsck` command.

Table 6-2 Options for the offline fsck command on Linux

| Option | Description |
| --- | --- |
| `-a` | Specifies to automatically repair the file system. |
| `-f` | Forces the file system into mountable state without completing a file system check or repair. |
| `-v` | Specifies verbose mode. The progress is displayed as the operation occurs. Running in verbose mode can impact performance. |
| `-t acfs` | Specifies the type of file system on Linux. `acfs` designates the Oracle ACFS type. |
| `-n` | Answers no to any prompts. |
| `-y` | Answers yes to any prompts. |
| `-x file_name` | Specified for accelerator data collected by `acfsutil meta`. Only used for this type of data. |
| `volume_device` | Specifies the primary Oracle ADVM volume device. |

`fsck` checks and repairs an existing Oracle ACFS file system. This topic describes an offline mode of the `fsck` command that can only be run on a dismounted file system. For information about running `fsck` on a mounted file system, refer to fsck (online mode).

`root` privileges are required to run `fsck`. The Oracle ACFS driver must be loaded for `fsck` to work.

By default, `fsck` only checks for and reports any errors. The `-a` flag must be specified to instruct `fsck` to repair errors in the file system. Do not interrupt `fsck` during the repair operation.

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

You can use `acfsutil` `info` `id` `id` `mount_point` to attempt to determine the directory associated with `parent.``id`. This directory is assumed to be where the deleted object originated. For information about `acfsutil` `info`, see [acfsutil info file](acfs-commands-utilities.md).

If the parent directory is not known, the parent `id` field is set to `UNKNOWN`.

Note:

It is not possible to see the contents of the `/lost+found` directory from a snapshot.

Examples

The following example shows how to check and repair a dismounted Oracle ACFS file system.

Example 6-2 Using the fsck command in offline mode

```
# /sbin/fsck -a -y -t acfs /dev/asm/volume1-123
```

### fsck (online mode)

Purpose

Checks and repairs a mounted Oracle ACFS file system.

Syntax and Description

```
fsck -t acfs -h /dev/null

fsck [-a] [-v] -t acfs -O mount_point -- -C cow_file_path -S cow_file_size
fsck.acfs [-a] [-v] -O -C cow_file_path -S cow_file_size mount_point
```

Note:

The latter two syntax formats are equivalent. When invoking the Linux `fsck` command, the `--` separator must be placed before either the `-C` or `-S` options to ensure that the options are correctly passed to the Oracle ACFS `fsck` command. When directly invoking the ACFS `fsck.acfs` command, the `--` separator is not required.

`fsck` `-t` `acfs` `-h` `/dev/null` displays usage text and exits.

Table 6-3 contains the options available with the `fsck` command.

Table 6-3 Options for the online fsck command on Linux

| Option | Description |
| --- | --- |
| `-a` | Specifies to automatically repair the file system. |
| `-v` | Specifies verbose mode. The progress is displayed as the operation occurs. Running in verbose mode can impact performance. |
| `-t acfs` | Specifies the type of file system on Linux. `acfs` designates the Oracle ACFS type. |
| `-O` | Specifies to run in an online mode that enables checking of a mounted Oracle ACFS file system. |
| `-C cow_file_path` | Specifies the location of the Copy-On-Write (COW) file required by online `fsck`. |
| `-s cow_file_size` | Specifies the size of the Copy-On-Write (COW) file required by online `fsck`.  The quantity specified can be in units of `K` (kilobytes), `M` (megabytes), `G` (gigabytes), `T` (terabytes), or `P` (petabytes). If a unit is not specified, the default is bytes. |
| `mount_point` | Specifies the directory where the file system is mounted. |

`fsck` checks and repairs an existing Oracle ACFS file system. This topic describes an online mode of the `fsck` command that can be run on a mounted file system. For information about running `fsck` in offline mode, refer to fsck (offline mode).

When online `fsck` is run on a mounted file system, online `fsck` initially creates a point-in-time snapshot of the file system metadata. Online `fsck` then executes file system checks against this metadata snapshot. Because the file system is mounted and live, file system metadata can be created or updated underneath online `fsck`. However, any new or updated metadata is not checked by online `fsck` because online `fsck` checks only the initial metadata snapshot.

Online `fsck` utilizes a special file called a Copy-On-Write (COW) file. While online `fsck` is running on a file system, whenever any file system metadata must be updated, the original version of the metadata is first copied into the COW file to preserve it for file system checks. The COW file helps preserve the metadata snapshot that is checked by online `fsck`.

The size of the COW file must be chosen in advance. As a result, the COW file has a limited amount of space for preserving copies of metadata. If the COW file runs out of space while preserving copies of metadata, then online `fsck` may be forced to stop. The size of the COW file must be chosen carefully to avoid running out of space during execution of online `fsck`. The appropriate size of the COW file depends on the amount of file system metadata that may change during the execution of online `fsck`, which is workload dependent and may need to be determined empirically. Oracle recommends the size of the COW file to start at 5% of the file system undergoing online `fsck`.

The COW file must be placed on a separate Oracle ACFS file system. The separate Oracle ACFS file system must be mounted on the same nodes as the Oracle ACFS file system undergoing online `fsck`.

The COW file is a temporary file that supports the execution of online `fsck` and is deleted after online `fsck` is complete.

The Oracle ACFS file system undergoing online `fsck` must have the same mount point path on all nodes. The Oracle ACFS file system storing the COW file must also have the same mount point path on all nodes.

Online `fsck` has the following restrictions and limitations while the command is running on an Oracle ACFS file system:

- Another instance of online `fsck` cannot be started within the same cluster.
- A mount of the file system on a new node causes online `fsck` to stop.
- If the separate Oracle ACFS file system containing the COW file is unmounted on any node, then that situation may cause online `fsck` to stop.
- Deleted snapshots within the file system do not have their storage freed until the completion of online `fsck`.
- Resizing the file system with `acfsutil` `size` is not allowed and returns an error. Automatic resizing is also not allowed until online `fsck` completes.
- A freeze of the file system with `acfsutil` `freeze` causes online `fsck` to wait for the freeze to end.

By default, online `fsck` only checks for and reports any errors. The `-a` flag must be specified to instruct online `fsck` to repair errors in the file system. Note that online `fsck` can only repair a limited set of file system errors. Most file system errors require offline `fsck` for repair.

Examples

The following example shows how to check and repair a mounted Oracle ACFS file system.

Example 6-3 Using the fsck command in online mode

```
# /sbin/fsck -a -t acfs -O /acfs_mountpoint_1 -- -C /acfs_mountpoint_2/cow_file -S 512M

# /sbin/fsck.acfs -O -C /acfs_mountpoint_2/cow_file -S 512M /acfs_mountpoint_1
```

### mkfs

Purpose

Creates an Oracle ACFS file system.

Syntax and Description

```
mkfs -t acfs -h
mkfs [-v] [-f] -t acfs [-i {512 | 4096}] [-n name ] [-a accelerator_volume] 
     [-c release_version] volume_device [size]
```

`mkfs` `-t` `acfs` `-h` displays usage text and exits.

Table 6-4 contains the options available with the `mkfs` command.

Table 6-4 Options for the Linux mkfs command

| Option | Description |
| --- | --- |
| `-t` `acfs` | Specifies the type of file system on Linux. `acfs` designates the Oracle ACFS type. |
| `-v` | Specifies verbose mode. The progress is displayed as the operation occurs. |
| `-i {512 \| 4096}` | Specifies a file system with metadata block size of 512 or 4096 bytes. |
| `-n` `name` | Specifies the name for the file system. A name can be a maximum of 64 characters. `acfsutil` `info` `fs` returns the name if one was specified. |
| `-f` | Specifies the force option. This action creates the file system even if there is an existing Oracle ACFS on the volume device, although only if the file system is dismounted. This option overwrites structures on the original file system. Use this option with caution. |
| `-h` | Displays the usage help text and exits. |
| `size` | Specifies the size that the file system should consume on the named device. The quantity specified can be in units of `K` (kilobytes), `M` (megabytes), `G` (gigabytes), `T` (terabytes), or `P` (petabytes). If a unit is not specified, the default is bytes.  If this option is not specified, the entire device is consumed. |
| `-a` `accelerator_volume` | Specifies a secondary Oracle ACFS volume that is used by Oracle ACFS to store critical metadata. |
| `-c` `release_version` | Creates an Oracle ACFS file system with Oracle ACFS release compatibility set to the value of release\_version. |
| `volume_device` | Specifies an existing Oracle ADVM device file that is to be formatted. This device is the primary volume. |

You can use `mkfs` to create the on disk structure needed for Oracle ACFS file system to be mounted. The `mkfs` command is the traditional Linux command used to build a file system. After `mkfs` runs successfully, the `USAGE` column in the `V$ASM_VOLUME` view displays `ACFS`. Oracle ADVM volumes are created with the ASMCMD `volcreate` command. For information about the `volcreate` command, refer to [volcreate](manage-advm-asmcmd.md).

The value specified with the `-c release_version` option must be greater than or equal to the value of `COMPATIBLE.ADVM` for the disk group, and must be less than or equal to the running Oracle Grid infrastructure release version. If `—c release_version` is not specified, the value of `COMPATIBLE.ADVM` is used. After the compatibility is set, it cannot be downgraded. The `—c release_version` option can be used in situations where it is not possible, or desirable, to update `COMPATIBLE.ADVM` and `COMPATIBLE.ASM` for the disk group, but you want to use an Oracle ACFS feature that requires a compatibility increase. After the Oracle ACFS compatibility is updated, it is no longer possible to mount the file system with an older Oracle Grid infrastructure release. To change the compatibility of an existing file system, refer to [acfsutil compat set](acfs-commands-utilities.md). For information about Oracle ASM disk group compatibility attributes, see [Oracle ACFS Features Enabled by Compatibility Attribute Settings](understand-acfs-admin.md).

The minimum file system size is 200 MB for the 512 byte metadata block size format and 512 MB for the 4 KB metadata block size format.

The Oracle ACFS driver must be loaded for `mkfs` to operate successfully.

`root` privilege is not required. The ownership of the volume device file dictates who can run this command.

Oracle ACFS Accelerator Volume

Using an accelerator volume can improve performance by reducing the time to access and update Oracle ACFS metadata. You should create the accelerator volume on a disk group with storage that is significantly faster than the storage of the primary volume. The accelerator volume is created with the `-a` option of the `mkfs` command. For more information, refer to [Oracle ACFS Accelerator Volume](understand-acfs-admin.md).

4 KB Sector/Metadata

The following list summarizes the use of the `-i` option and metadata block size based on the value of the `COMPATIBLE.ADVM` disk group attribute.

- If `COMPATIBLE.ADVM` is set to `20.1` or greater, then the primary and accelerator volumes can use a mix of different logical sector sizes, such as 512 bytes and 4096 bytes.
- If `COMPATIBLE.ADVM` is set to `12.2` or greater, then the metadata block size is `4096` bytes by default.
- If `COMPATIBLE.ADVM` is set to less than `12.2`, then the block size is set to 512 bytes.
- If `COMPATIBLE.ADVM` is set to less than `12.2` and the logical sector size is not 512 bytes, then the command fails.

User data IO continues to support transfers as small as 512 bytes for normal user IO requests. When the Oracle ADVM volume of the file system has a logical disk sector size of 4 K, user Direct IO requests should be aligned on 4 K file offsets and be a multiple of 4 KB lengths for the best performance. Note that only 4 K metadata block size formats support ADVM volumes with 4 K logical disk sectors.

The `COMPATIBLE.ADVM` value must be set to `12.2` or greater to format an Oracle ADVM volume whose logical disk size is 4096 or to use the `-i 4096` option to format an Oracle ADVM volume whose logical disk sector size is 512 bytes.

Examples

Before creating an Oracle ACFS file system, first determine which Oracle ADVM volume devices are available. You can use the ASMCMD `volinfo` command to display information about the volumes and volume devices. For example:

```
ASMCMD [+] > volinfo -a
...
         Volume Name: VOLUME1
         Volume Device: /dev/asm/volume1-123
         State: ENABLED
...
```

For information about the `volcreate` and `volinfo` commands, refer to [Managing Oracle ADVM with ASMCMD](manage-advm-asmcmd.md).

This command creates an Oracle ACFS file system on a volume device file.

Example 6-4 Using the mkfs command

```
$ /sbin/mkfs -t acfs /dev/asm/volume1-123
```

Example 6-5 Using the mkfs command to create an accelerator volume

This command creates an Oracle ACFS file system with an accelerator volume.

```
$ /sbin/mkfs -t acfs -a /dev/asm/volume2-130 /dev/asm/volume1-127
```

### mount

Purpose

Mounts an Oracle ACFS file system.

Syntax and Description

```
mount -h
mount [-v] -n -t acfs [-o options] volume_device mount_point
mount
```

`mount` `-h` displays usage text and exits.

Table 6-5 contains the options available with the `mount` command.

Table 6-5 Options for the Linux mount command

| Option | Description |
| --- | --- |
| `-h` | Displays the usage help text and exits. |
| `-t` `acfs` | Specifies the type of file system on Linux. `acfs` designates the Oracle ACFS type. |
| `-v` | Specifies verbose mode. The progress is displayed as the operation occurs. |
| `-n` | Specifies not to update the `/etc/mtab` file. |
| `-o` | Options are specified with the `-o` flag followed by a comma-delimited string of options. The following options are available:  - `all` 	Reads the Oracle ACFS managed file systems in the Oracle Clusterware namespace, mounting all file systems with the `AUTO_START=always`. 	When the `-o` `all` option is specified, other `-o` options are ignored. 	To specify mount options for a registry entry, include those options with the `acfsutil` `registry` command when you add the entry to the registry. - `ro` 	Mounts the file system in read-only mode. - `norootsuid` 	Fails the execution of binaries by non-root users whose permissions allow set user Id execution, and are owned by root. An attempt to run these executables as a non-root user fails with a permission denied error. - `rootsuid` 	Allows the execution of binaries by non-root users of set user Id files owned by root. This is the default action. - `nodeleteopen` 	Fails the deletion of any file that is open. |
| `volume_device` | Specifies a primary Oracle ADVM volume device file that has been formatted by `mkfs`. `device` is required but can be a dummy value. |
| `mount_point` | Specifies the directory where the file system is mounted. This directory must exist before you run the `mount` command. |

`mount` attaches a file system to the Oracle ACFS hierarchy at the mount point that is the name of a directory. The mount happens on the node where the mount command was issued. The mount command returns an error if the file system is not in a dismounted state on this node.

It is not always possible to return the cause of a mount failure to the `mount` command. When this happens Oracle ACFS writes the cause of the failure to the system console and associated system log file.

After `mount` runs successfully, the `MOUNTPATH` field in the `V$ASM_VOLUME` view displays the directory name on which the file system is now mounted.

An Oracle ACFS file system should only be mounted on one mount point. The same mount point name should be used on all cluster members.

The `mount` command lists all mounted file systems if it is run with no parameters.

`root` privilege is required to run `mount`.

Examples

The first example shows how to mount `volume1-123` on the mount point `/acfsmounts/acfs1`. The second example shows how to mount all the registered Oracle ACFS file systems. The dummy names (`none`) have been entered for the device and directory as they are required, but not used, when the `all` option is specified.

Example 6-6 Using the mount command

```
# /bin/mount -t acfs /dev/asm/volume1-123 /acfsmounts/acfs1

# /bin/mount -t acfs -o all none none
```

### umount

Purpose

Dismounts an Oracle ACFS file system.

Syntax and Description

```
umount -h
umount [-v] -l -n volume_device |mount_point
umount -a -l -n [-t acfs]
```

`umount` `-h` displays usage text and exits.

Table 6-6 contains the options available with the `umount` command.

Table 6-6 Options for the Linux umount command

| Option | Description |
| --- | --- |
| `-h` | Displays the usage help text and exits. |
| `-t` `acfs` | Specifies the type of file system on Linux. `acfs` designates the Oracle ACFS type. |
| `-v` | Specifies verbose mode. The progress is displayed as the operation occurs. |
| `-a` | Specifies to dismount all Oracle ACFS file systems on this node. |
| `-l` | Specifies a lazy unmount. The Oracle ACFS file system is dismounted, but the cleanup of all references to the file system occurs when the system is no longer busy. |
| `-n` | Specifies not to update the `/etc/mtab` file. |
| `volume_device` | Specifies an Oracle ADVM volume device file that has been formatted by `mkfs`. |
| `mount_point` | Specifies the directory where the file system is mounted. This directory must exist before you run the `mount` command. |

`umount` detaches an Oracle ACFS from the file system hierarchy on the current node.

The `umount` command does not return control back to the operating system prompt until the file system has been completely unmounted.

If the file system is busy, `umount` fails.

`root` privileges are required to run the `umount` command.

Examples

The following examples show how to dismount an Oracle ACFS file system. The first example uses the volume device file and the second example uses the file system.

Example 6-7 Using the umount command

```
# /bin/umount /dev/asm/volume1-123

# /bin/umount /acfsmounts/acfs1
```