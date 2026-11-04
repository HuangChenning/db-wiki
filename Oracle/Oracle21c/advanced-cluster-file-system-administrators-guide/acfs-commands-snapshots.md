---
title: "Administrator's Guide"
book: "Advanced Cluster File System Administrator's Guide"
doc_id: F30297-04
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/acfsg/acfs-commands-snapshots.html
tags:
  - oracle
  - 21c
  - advanced-cluster-file-system-administrators-guide
---

This topic provides a summary of commands to manage Oracle ACFS snapshots.

Table 6-43 lists Oracle ACFS snapshot commands with brief descriptions. For an overview of Oracle ACFS snapshots, refer to [About Oracle ACFS Snapshots](understand-acfs-concepts.md).

For more information about running Oracle ACFS `acfsutil` commands, refer to [About Using Oracle ACFS Command-Line Tools](steps-manage-acfs.md).

Table 6-43 Summary of commands for Oracle ACFS snapshots

| Command | Description |
| --- | --- |
| acfsutil snap convert | Converts the type of an existing snapshot. |
| acfsutil snap create | Creates a snapshot of an Oracle ACFS file system or an existing snapshot. |
| acfsutil snap delete | Deletes a snapshot of an Oracle ACFS file system. |
| acfsutil snap duplicate apply | Updates a duplicate snapshot or file system. |
| acfsutil snap duplicate create | Creates a duplicate of an existing snapshot. |
| acfsutil snap info | Displays information about Oracle ACFS file system snapshots. |
| acfsutil snap link | Creates or deletes a snapshot link. |
| acfsutil snap quota | Sets the quota limit for a specified snapshot. |
| acfsutil snap remaster | Remasters a file system with a specified snapshot. |
| acfsutil snap rename | Renames a snapshot. |

### acfsutil snap convert

Purpose

Converts the type of an existing snapshot image from read-only to read-write or read-write to read-only.

Syntax and Description

```
acfsutil snap convert -h
acfsutil snap convert [-r|-w] snap_shot mount_point
```

`acfsutil` `snap` `convert` `-h` displays help text and exits.

The following table contains the options available with the `acfsutil` `snap` `convert` command.

Table 6-44 Options for the acfsutil snap convert command

| Option | Description |
| --- | --- |
| `-r` | Converts snapshot to read-only snapshot. |
| `-w` | Converts snapshot to read-write snapshot. |
| `snap_shot` | Specifies the name of the snapshot to be converted. |
| `mount_point` | Specifies the directory where the file system is mounted. |

`acfsutil` `snap` `convert` converts the type of an existing snapshot image from a read-only snapshot image to a read-write snapshot image, or from a read-write snapshot image to a read-only snapshot image.

The type option (`-r` or `-w`) is required for the convert operation. Specifying a type parameter that matches the type of the existing snapshot image results in no conversion and no failure. An 11.2 read-only snapshot image can be converted to a read-write snapshot image, but this conversion results in an update of the Oracle ACFS on-disk structure version. After the Oracle ACFS on-disk structure version has been updated, the updated version is not compatible with previous Oracle ACFS 11.2 versions.

Administrator privileges are required to use this command or you must be a member of the Oracle ASM administrator group.

Examples

Example 6-39 shows the use of the `acfsutil` `snap` `convert` command.

Example 6-39 Using the acfsutil snap convert command

```
$ acfsutil snap convert -w midday_test1 /acfsmounts/critical_apps

$ acfsutil snap convert -r midday_test2 /acfsmounts/critical_apps
```

### acfsutil snap create

Purpose

Creates a read-only or read-write snapshot of an Oracle ACFS file system or an existing snapshot.

Syntax and Description

```
acfsutil snap create -h
acfsutil snap create [-r|-w] [-p parent_snap_shot] snap_shot mount_point
```

`acfsutil` `snap` `create` `-h` displays help text and exits.

The following table contains the options available with the `acfsutil` `snap` `create` command.

Table 6-45 Options for the acfsutil snap create command

| Option | Description |
| --- | --- |
| `-r` | Creates a read-only snapshot. This is the default setting. |
| `-w` | Creates a read-write snapshot. |
| `snap_shot` | Specifies a name for the snapshot. The name provided must follow host operating system specific naming rules for directories. The`.ACFS/snaps` directory itself cannot be snapped. |
| `-p` `parent_snap_shot` | Specifies the name of an existing snapshot image within the Oracle ACFS file system. |
| `mount_point` | Specifies the directory where the file system is mounted. |

`acfsutil` `snap` `create` creates a read-only or read-write snapshot of the Oracle ACFS file system mounted on `mount_point` or creates a snapshot of an existing snapshot if the `-p` option is specified. You can specify `-r` for read-only or `-w` for read-write; read-only is the default if neither `-r` or `-w` are specified.

The read-write snapshot enables the fast creation of an Oracle ACFS snapshot image that can be both read and written without impacting the state of the Oracle ACFS file system hosting the snapshot images. You can use the read-write functionality for testing new versions of application software or running test scenarios on production file data without modifying the original file system.

During the create snapshot operation duplicate data within the source file system or snapshot is copied to the new snapshot. The create operation makes a copy of a file system or snapshot whose last update was performed by an `acfsutil` `snap` `duplicate` `apply` operation. This updated file system or snapshot is known as the apply target. The data written to an apply target comes from the snapshot duplication stream of an `acfsutil` `snap` `duplicate` `create` operation. An apply target contains metadata that identifies the stream that updated the target. This metadata ensures that any future `acfsutil` `snap` `duplicate` `apply` operation for the apply target has a starting point that matches the endpoint of the previous stream that updated the target.

Snapshots are not separate file systems. The snapshot appears in the `.ACFS/snaps/` `snapshot` directory and initially is a complete replica of the file system at the time the snapshot command was given. A read-only snapshot continues to preserve that initial point-in-time view. A read-write snapshot can be modified by updates written directly to the files located within the `.ACFS/snaps/` `snapshot` hierarchy.

A symbol link (symlink) file is a pointer to a path specified at the time that the symlink is created. For any existing symlink in the source of the `acfsutil` `snap` `create` command, a new link is made in the snapshot; however, the stored path to the symlink target is not modified during snap creation time. When an absolute path is used as the target of the link, the link target of the snapshot still refers to the absolute path, outside the newly-created snapshot namespace. Future modifications to the targeted file can occur through the snapshot symlink, not to a new target inside the snapshot namespace. The contents of the targeted file can also be changed outside of the snapshot. Because of this behavior, you should use relative path targets for all symlinks that are within the same file system.

Any user can access the snapshot directory by specifying the path name. However, the.`ACFS` directory itself is hidden from directory listings of the root of the file system. This prevents recursive commands, such as `rm` `-rf` or `acfsutil` `tag` `set` `-r`, from the root of the file system inadvertently operating on snapshot files.

Snapshots usually use very little storage initially as they share file system blocks with the original file system until a file changes.

Tools such as `du` report the total disk space usage of the snapshotted files, which includes the storage shared with the original versions of the files. To determine the total space used for the snapshots, use the `acfsutil` `snap` `info` or `acfsutil` `info` `fs` command.

Oracle ACFS snapshots are immediately available for use after they are created. They are always online under the`.ACFS/snaps` directory when the original file system is mounted. No separate command is needed to mount them.

The `acfsutil` `snap` `create` operation fails if the cluster is in rolling migration.

Creation from an existing snapshot is not permitted if there are:

- Any snapshots present in the file system that were created with the `ADVM` compatibility set to less than 12.1
- Any snapshots of the file system that were created after `ADVM` compatibility was set to `12.1` but while 11.2 snapshots existed
- Any snapshot deletion cleanup operations still running in the background for the above conditions
	You can display pending snapshot operations with the `acfsutil` `snap` `info` command.

Administrator privileges are required to use this command or you must be a member of the Oracle ASM administrator group.

Examples

Example 6-40 shows the use of the `acfsutil` `snap` `create` command to create snapshots on a Linux platform.

Example 6-40 Using the acfsutil snap create command on Linux

```
$ /sbin/acfsutil snap create -w midday_test1 /acfsmounts/critical_apps

$ /sbin/acfsutil snap create -w midday_test2 /acfsmounts/critical_apps

$ /sbin/acfsutil snap create payroll_report1 /acfsmounts/critical_apps

$ /sbin/acfsutil snap create payroll_report2 /acfsmounts/critical_apps

$ ls /acfsmounts/critical_apps/.ACFS/snaps
midday_test1  midday_test2  payroll_report1  payroll_report2
```

See Also:

- [About Oracle ACFS Snapshots](understand-acfs-concepts.md) for information about Oracle ACFS snapshots
- [Oracle ACFS Disk Space Usage](acfs-advanced-topics.md) for information about the number of snapshots supported
- acfsutil snap info for information about displaying pending snapshots operations
- [acfsutil info fs](acfs-commands-utilities.md) for information about displaying the space used for snapshots
- Oracle ACFS Command-Line Tools for Snapshots for information about the `acfsutil` `snap` `duplicate` `apply` and `acfsutil` `snap` `duplicate` `create` commands

### acfsutil snap delete

Purpose

Deletes a snapshot of an Oracle ACFS file system.

Syntax and Description

```
acfsutil -h snap delete
acfsutil snap delete snapshot mount_point
```

`acfsutil` `-h` `snap` `delete` displays help text and exits.

Table 6-46 contains the options available with the `acfsutil` `snap` `delete` command.

Table 6-46 Options for the acfsutil snap delete command

| Option | Description |
| --- | --- |
| `snapshot` | Specifies a name for the snapshot. |
| `mount_point` | Specifies the directory where the file system is mounted. |

`acfsutil` `snap` `delete` deletes the snapshot named `snapshot` in the Oracle ACFS mounted on `mount_point`. After successful completion of the command, the representation of the snapshot in the`.ACFS/snaps` directory is removed. The command succeeds even if there are open files or directory references; however, storage associated with the snapshot is not released until all such references are closed.

The disk space used by the snapshot being deleted is released by a background task after the completion of the `acfsutil` `snap` `delete` command or after the last close of a file in the snapshot. If one of these background threads is running to clean up a deleted snapshot, then the `acfsutil` `snap` `info` command shows a pending delete operation. For information about the `acfsutil` `snap` `info` command, refer to " acfsutil snap info ".

The `acfsutil` `snap` `delete` operation fails if the cluster is in rolling migration.

Administrator privileges are required to use this command or you must be a member of the Oracle ASM administrator group.

Examples

Example 6-41 shows the use of the `acfsutil` `snap` `delete` command.

Example 6-41 Using the acfsutil snap delete command

```
$ /sbin/acfsutil snap delete midday_test1 /acfsmounts/critical_apps
acfsutil snap delete: Snapshot operation is complete.
```

### acfsutil snap duplicate apply

Purpose

Applies a previously created duplicated snapshot to an Oracle ACFS snapshot or file system.

Syntax and Description

```
acfsutil snap duplicate apply -h
acfsutil snap duplicate apply [-b | -B snap_shot] [-d trace_level] [snap_shot] mount_point
```

`acfsutil snap duplicate apply` `-h` displays help text and exits.

The following table contains the options available with the `acfsutil snap duplicate apply` command.

Table 6-47 Options for the acfsutil snap duplicate apply command

| Option | Description |
| --- | --- |
| `—b` | Specifies that a backup snapshot is generated after a successful completion of the command. The name of the backup is generated in the format `SDBACKUP_seccnt_sourcesnap_targetsnap`, which is described in the text of this topic. |
| `—B snap_shot` | Specifies that a backup snapshot with the name specified is generated after a successful completion of the command. |
| `-d` `trace_level` | Specifies the trace level setting \[0..6\] for the command execution. |
| `snap_shot` | Specifies that the named snapshot of that file system is the target. The specified snapshot must exist and must be writable. If the snap\_shot is not specified, the target for the apply operation is the file system currently mounted at the mount point |
| `mount_point` | Specifies the directory where the duplicate snapshot is applied. |

The `acfsutil` `snap` `duplicate` `apply` command uses the snapshot duplication stream produced by `acfsutil snap duplicate create` to update the specified target file system or snapshot. The stream of data is read from the standard input.

If the target has never been applied to by a `acfsutil` `snap` `duplicate` `apply` operation, this is an initial apply, and the target must be initially empty. If the target has been applied to by a previous apply operation, this is an incremental apply, and the initial contents of the target must match the contents of the older snapshot used to produce the snapshot duplication stream.

If the contents of the target no longer match the older snapshot for the stream, the command returns an error and the stream is not applied. The target must not be updated by other means while the apply operation is in progress. If another update occurs, the command returns an error and stops applying the snapshot duplication stream. If the data stream being applied is identical to the last data stream applied to the specified target, the command exits without writing anything to the target with a status value of `2`.

If the `-b` or `—B` option is specified, then a backup snapshot is taken of the target after the apply operation completes the update. Because the snapshot taken for an apply operation is automatically deleted when the next apply operation completes, the snapshot present is the one from the last-completed apply operation. The backup snapshot provides a known and consistent version of the target for the last successful apply operation and a comparison point to identify the in-progress changes made by a `acfsutil snap duplicate apply` operation.

If a name was not specified with the `—B` option, then a backup snapshot has a name of the form `SDBACKUP_seccnt_sourcesnap` or `SDBACKUP_seccnt_sourcesnap_targetsnap`. In the name string, `seccnt` is a local timestamp (number of seconds since the Unix epoch) indicating the point at which the target was captured by the backup snapshot. `sourcesnap` indicates the snapshot from the source file system that was applied by the last completed `acfsutil snap duplicate apply` operation. `targetsnap`, if present, indicates the snapshot name in the target file system that was updated by the last completed `acfsutil` `snap` `duplicate` `apply` operation.

System administrator (`root`) privileges are required to use this command.

The `acfsutil` `snap` `duplicate` `apply` command produces an exit status of `0` on success, `1` if a fatal error occurs, or `2` if the data stream read matches the last previous data stream applied to the specified target.

For information about displaying snapshot information, refer to " acfsutil snap info ".

Examples

Example 6-42 shows the use of the `acfsutil` `snap` `duplicate` `apply` command. Because the command expects to read a binary data stream from its standard input, this command is normally used in a pipeline with the `acfsutil` `snap` `duplicate` `create` command, as shown in the example.

Example 6-42 Using the acfsutil snap duplicate apply command

```
$ /sbin/acfsutil snap duplicate create new_snapshot_name /acfsmounts/critical_apps | \
      /sbin/acfsutil snap duplicate apply /acfsmounts/ca_backups
```

### acfsutil snap duplicate create

Purpose

Creates a duplicate snapshot of an existing snapshot.

Syntax and Description

```
acfsutil snap duplicate create -h
acfsutil snap duplicate create [-r] [-d trace_level] [-p parent_snapshot]
                               [-i old_snapshot] new_snapshot mount_point
```

`acfsutil snap duplicate create` `-h` displays help text and exits.

Table 6-48 contains the options available with the `acfsutil` `snap` `duplicate` `create` command.

Table 6-48 Options for the acfsutil snap duplicate create command

| Option | Description |
| --- | --- |
| `-r` | Specifies to mark the snap duplication stream as a restart stream. This option is intended for use on the second or later attempt to create and apply a given stream. This option might be necessary if an earlier attempt terminated prematurely. |
| `-d ` trace\_level | Specifies the trace level setting \[0..6\] for the command execution. |
| `-p` `parent_snapshot` | Specifies the name of a parent snapshot image of which both the `old_snapshot` and `new_snapshot` are children.  This option ensures that both snapshots are children (snap-of-snap) of the same snapshot. If the `—p` option is not specfied, then either the `new_snapshot` must be a child of the `old_snapshot`, or the two snapshots must be snapshots of the base file system at the specified mount point. |
| `—i` `old_snapshot` | Specifies the name of an existing snapshot. |
| `new_snapshot` | Specifies a name for the new snapshot. |
| `mount_point` | Specifies the directory where the file system is mounted. This is the mount point of the file system of which the snapshots were taken. |

The `acfsutil` `snap` `duplicate` `create` command externalizes snapshot-related data in a form suitable for use by snap duplicate apply to create a different instance of a compatible snapshot. This externalized data is called a snapshot duplication stream.

If only the new snapshot name is specified, then this command encodes the entire contents of the named snapshot (the difference between an empty snapshot and this snapshot). This is an initial snap duplicate operation.

If both the old snapshot name and new snapshot name are given, this command encodes only the differences between the two snapshots. This is an incremental snap duplicate operation.

In either case, this command writes the snapshot duplication stream to its standard output.

System administrator (`root`) privileges are required to use this command.

The `acfsutil` `snap` `duplicate` `create` command produces an exit status of `0` on success or `1` if a fatal error occurs.

For information about displaying snapshot information, refer to " acfsutil snap info ".

Examples

Example 6-43 shows the use of the `acfsutil` `snap` `duplicate` `create` command. Because the command writes a binary data stream to its standard output, this command is normally used in a pipeline with the `acfsutil` `snap` `duplicate` `apply` command, as shown in the example.

Example 6-43 Using the acfsutil snap duplicate create command

```
$ /sbin/acfsutil snap duplicate create new_snapshot_name /acfsmounts/critical_apps | \
      /sbin/acfsutil snap duplicate apply /acfsmounts/ca_backups
```

### acfsutil snap info

Purpose

Displays information about Oracle ACFS file system snapshots.

Syntax and Description

```
acfsutil snap info -h
acfsutil snap info [-t] [snap_shot] mount_point
```

`acfsutil` `snap` `info` `-h` displays help text and exits.

The following table contains the options available with the `acfsutil` `snap` `info` command.

Table 6-49 Options for the acfsutil snap info command

| Option | Description |
| --- | --- |
| `-t` | Displays a tree structure for the specified snapshot and mount point. |
| `snap_shot` | Specifies a name for the snapshot. |
| `mount_point` | Specifies the directory where the file system is mounted. |

The `acfsutil` `snap` `info` command displays information about an individual specified snapshot or all snapshots in the specified Oracle ACFS file system.

The snapshot name, snapshot type, parent name, creation date and time, and space used are displayed. The parent name is either the mount point, or the parent snapshot if the snapshot was created from an existing snapshot.

The type of a snapshot is indicated by one or more of the following strings. Any relevant strings are displayed on the same line.

- `RO` - snapshot is read-only
- `RW` - snapshot is read-write
- `Primary` - snapshot is a primary storage location for replication
- `Standby` - snapshot is a standby storage location for replication
- `REPL` - snapshot is an internal snapshot used by replication
- `DUP` - snapshot or its parent is a target of snap duplicate apply

The appearance of the string `REPL` is not related to whether a snapshot is a replication primary or standby. This string appears only if the snapshot is one that was created by replication for its own internal use.

The string `DUP` appears if either of the following conditions is true:

- The snapshot is in use as the target of an apply operation.
- The parent of the snapshot was in use as the target of an apply operation at the point when the snapshot was created.

The `snapshot` `space` `usage` amount includes snapshot metadata. If all the files are deleted from a snapshot, some metadata still remains and that amount is displayed with `acfsutil` `snap` `info`.

When using an accelerator volume, the reported `snapshot` `space` `usage` amount can include space that is in use on the accelerator volume.

To reclaim the disk space used by snapshots, delete the snapshots. Deleting the files within the snapshots may not reclaim this disk space.

The `acfsutil` `snap` `info` command shows the status of a snapshot that is in the process of being deleted as follows:

- When waiting on files to be closed:
	```
	snapshot_name (delete waiting for last close)
	```
- When freeing the storage for the snapshot in the background:
	```
	snapshot_name (delete in progress)
	```

Oracle ACFS caches and asynchronously updates snapshot storage usage statistics. If an Oracle ASM instance is terminated, power is lost to the machine, or the Oracle ACFS file system goes offline for any reason, one of these cached updates may be lost. This loss can result in the display of a message similar to `Reported` `snapshot` `space` `usage` `is` `inaccurate` when `acfsutil` `snap` `info` is run.

Examples

Example 6-44 shows the use of the `acfsutil` `snap` `info` command on a Linux platform. The command output contains information about a read-only (RO) snapshot, a read-write (RW) snapshot with quota information, a snapshot in `delete` `waiting` `for` `last` `close` status, and a snapshot in `delete` `in` `progress` status. After a delete operation completes on a snapshot and the background process finishes the clean up of a deleted snapshot, messages about the delete operation do not appear in the output.

Example 6-44 Using the acfsutil snap info command on Linux

```
$ /sbin/acfsutil snap info /acfsmounts/critical_apps/
snapshot name:               midday_test (delete waiting for last close)
snapshot creation time:      Tue Apr  5 10:52:55 2016

snapshot name:               payroll_report1
snapshot location:           /acfsmounts/critical_apps/.ACFS/snaps/payroll_report1
RO snapshot or RW snapshot:  RW
parent name:                 /acfsmounts/critical_apps/
snapshot creation time:      Tue Apr  5 10:52:59 2016
storage added to snapshot:   95514624   (  91.09 MB )

quota:                       104857600  ( 100.00 MB )
quota usage:                 91 %

snapshot name:               midday_test2 (delete in progress)
snapshot creation time:      Mon Apr 11 11:40:13 2016

snapshot name:               payroll_report2
snapshot location:           /acfsmounts/critical_apps/.ACFS/snaps/payroll_report2
RO snapshot or RW snapshot:  RO
parent name:                 midday_test2
snapshot creation time:      Mon Apr 11 12:05:42 2016
storage added to snapshot:   1081344   (   1.03 MB )

    number of snapshots:  3 (active)
                          1 (delete in progress)
        snapshot space usage: 102084608  (  97.36 MB )

$ /sbin/acfsutil snap info -t /acfsmounts/critical_apps
/acfsmounts/critical_apps RW    
midday_test               RW    /acfsmounts/critical_apps
payroll_report1           RW    /acfsmounts/critical_apps
midday_test2              RW    /acfsmounts/critical_apps
payroll_report2           RO    midday_test2 

$ /sbin/acfsutil snap info -t midday_test2 /acfsmounts/critical_apps
midday_test2              RW    
payroll_report2           RO    midday_test2
```

### acfsutil snap link

Purpose

Creates or deletes a snapshot link.

Syntax and Description

```
acfsutil snap link -h
acfsutil snap link -s snap_shot path_to_link
acfsutil snap link -s snap_shot -d path_to_link
```

`acfsutil` `snap` `link` `-h` displays help text and exits.

The following table contains the options available with the `acfsutil` `snap` `link` command.

Table 6-50 Options for the acfsutil snap link command

| Option | Description |
| --- | --- |
| `—s snap_shot` | Specifies the name of an Oracle ACFS snapshot in the Oracle ACFS file system. |
| `-d` | Deletes the specified snapshot link. |
| `path_to_link` | Specifies a directory in the Oracle ACFS file system. |

You can create or delete snapshot links with the `acfsutil` `snap` `link` command. A snapshot link provides access to the contents of a snapshot using an alternate path which does not include the `.ACFS/snaps` directory, the default location where snapshot are created.

A snapshot link is a specialized hard link that requires that only one snapshot link may exist for a snapshot. Snapshot links can only be created in the primary file system, not within another snapshot. Snapshot links can be recreated to change the name or location of the snapshot link. The name that you specify for a snapshot link does not have to be the same as the name or the snapshot to which it links. A snapshot link does require on disk changes and the `COMPATIBLE.ADVM` disk group attribute must be set to `18.0` or higher. Snapshot links can only be created and deleted with the `acfsutil` `snap` `link` command. The links cannot be moved or removed with normal operating system commands.

You can display information about snapshot links with the `acfsutil` `snap` `info` command. You can use `acfsutil` `snap` `info` `snap_shot` to determine whether the specified snapshot has a link.

Examples

The following example shows the use of the `acfsutil` `snap` `link` command. After a new snapshot is created, a link is created to the new snapshot.

Example 6-45 Using the acfsutil snap link command

```
$ /sbin/acfsutil snap create -w snap1 /usmmnt  
acfsutil snap create: Snapshot operation is complete.

$ /sbin/acfsutil snap link -s snap1 /usmmnt/dir1/link
acfsutil snap link: Snapshot operation is complete.

$ /sbin/acfsutil snap info /usmmnt
snapshot name:               snap1
snapshot location:           /usmmnt/.ACFS/snaps/snap1
snapshot link:               /usmmnt/dir1/link
RO snapshot or RW snapshot:  RW
parent name:                 /usmmnt
...
```

### acfsutil snap quota

Purpose

Sets the quota limit for a specified snapshot.

Syntax and Description

```
acfsutil -h snap quota

acfsutil snap quota [+|-]n[K|M|G|T|P] snapshot mount_point
```

`acfsutil` `—h` `snap` `quota` displays help text and exits.

The following table contains the options available with the `acfsutil` `snap` `quota` command.

Table 6-51 Options for the acfsutil snap quota command

| Option | Description |
| --- | --- |
| \[`+` \| `-`\] `n`  `K` \| `M` \| `G` \| `T` \| `P` | Specifies the quota limit size for the Oracle ACFS snapshot where `n` is a valid positive whole number greater than zero. The number can be preceded by a `+` or - to indicate the amount to add or decrease. If no operand exists, the new size is the absolute size.  Specifies that the integer supplied for size is in the units of `K` (Kilobytes), `M` (Megabytes), `G` (Gigabytes), `T` (Terabytes), or `P` (Petabytes). If the unit indicator is specified, then it must be appended to the integer. If omitted, the default unit is bytes. |
| `snapshot` | Specifies a name of the snapshot. |
| `mount_point` | Specifies the directory where the file system is mounted. |

The acfsutil snap quota command sets the quota limit for a specified snapshot on the specified Oracle ACFS file system.

The quota can be larger than the size of the file system because a file system can be resized or automatically resized.

The quota limit specified does not reserve space. The quota only establishes an upper limit on the amount of storage that can be added to the snapshot.

Only snapshots created after ADVM compatibility (`COMPATIBLE.ADVM`) has been set to `12.2` or greater have storage accounting tracking and the ability to have quotas set.

Snapshots can be converted from read-write (RW) to read-only (RO) and vice versa. Both RW and RO snapshots can have a quota.

There is a grace period and advanced warnings for quota usage. A warning message is written to both the alert log and the console if the requested storage allocation causes the local storage usage to be near or exceeding more than `90%` of the quota. If an allocation exceeds the quota, then the write or other modifying operation fails as `EDQUOT`, or it may fail as `ENOSPC`, depending whether the quota limit is set larger than the size of the file system.

System administrator (`root`) privileges are required to use this command.

You can display snapshot information, including the quota limit and quota usage percentage, with the `acfsutil` `snap` `info` command. For information about `acfsutil` `snap` `info`, refer to " acfsutil snap info ".

Examples

The following example shows the use of the `acfsutil` `snap` `quota` command.

Example 6-46 Using the acfsutil snap quota command

```
$ /sbin/acfsutil snap quota +500M snap_test /acfsmounts/acfs1
```

### acfsutil snap remaster

Purpose

Remasters an Oracle ACFS file system with a snapshot.

Syntax and Description

```
acfsutil snap remaster -h
acfsutil snap remaster { snapshot | -c } -f volume
```

`acfsutil snap remaster` `-h` displays help text and exits.

Table 6-52 contains the options available with the `acfsutil` `snap` `remaster` command.

Table 6-52 Options for the acfsutil snap remaster command

| Option | Description |
| --- | --- |
| `—c` | Continues the interrupted remaster operation. After the command has started, the remastering must run to completion. |
| `—f` | Forces the operation and does not prompt for questions. |
| `snapshot` | Specifies the name of an existing snapshot. |
| `volume` | Specifies specifies the primary Oracle ADVM volume device path for the file system. |

This command accepts a snapshot name or the `—c` option.

The specified snapshot is used for the base of the file system, replacing the current base of the file system. Using an existing read-only or read-write snapshot, the command reintegrates the snapshot extents into the base of the current file system creating a new remastered file system with the point in time state of the snapshot. The remastered file system is left with no snapshots. This operation must be done on an unmounted file system and it cannot be reversed.

Use the `-c` option, instead of the snapshot name, to complete an interrupted snapshot remastering.

You cannot remaster a file system on which replication, security, or encryption is running. You must terminate replication, security, or encryption before running the `acfsutil` `snap` `remaster` command. In addition, you cannot remaster a file system with plugins enabled.

Administrator privileges are required to use this command or you must be a member of the Oracle ASM administrator group.

Examples

Example 6-47 shows the use of the `acfsutil` `snap` `remaster` command.

Example 6-47 Using the acfsutil snap remaster command

```
$ /sbin/acfsutil snap remaster snapshot volume
```

### acfsutil snap rename

Purpose

Renames an Oracle ACFS snapshot.

Syntax and Description

```
acfsutil snap rename -h
acfsutil snap rename old_snapshot new_snapshot mount_point
```

`acfsutil snap rename` `-h` displays help text and exits.

Table 6-53 contains the options available with the `acfsutil` `snap` `duplicate create` command.

Table 6-53 Options for the acfsutil snap rename command

| Option | Description |
| --- | --- |
| `old_snapshot` | Specifies the name of an existing snapshot. |
| `new_snapshot` | Specifies a name for the new snapshot. |
| `mount_point` | Specifies the directory where the file system is mounted. |

The `acfsutil` `snap` `rename` command is used to safely rename an existing snapshot in the filesystem.

While a snapshot with open files can be renamed, applications accessing files in that snapshot experience the same behavior as operating in a non-snap directory tree in which one of the parent directories was renamed.

Renaming snapshots used in conjunction with pluggable databases (PDBs) is not supported at this time. Such a snapshot should not be renamed.

Replication-specific snapshots cannot be renamed as this may cause complications and inconsistencies with replication.

Administrator privileges are required to use this command or you must be a member of the Oracle ASM administrator group.

For information about displaying snapshot information, refer to " acfsutil snap info ".

Examples

Example 6-48 shows the use of the `acfsutil snap rename` command.

Example 6-48 Using the acfsutil snap rename command

```
$ /sbin/acfsutil snap rename old_snapshot_name new_snapshot_name /acfsmounts/critical_apps
```