---
title: "Administrator's Guide"
book: "Advanced Cluster File System Administrator's Guide"
doc_id: F30297-04
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/acfsg/acfs-commands-replication.html
tags:
  - oracle
  - 21c
  - advanced-cluster-file-system-administrators-guide
---

This topic provides a summary of the commands for Oracle ACFS snapshot-based replication.

Table 6-21 lists the Oracle ACFS snapshot-based replication commands with brief descriptions. For an overview of Oracle ACFS replication, refer to [Oracle ACFS Replication](understand-acfs-admin.md).

For information about running Oracle ACFS `acfsutil` commands, refer to [About Using Oracle ACFS Command-Line Tools](steps-manage-acfs.md).

Most `acfsutil` `repl` commands may be run either with system administrator privileges or as the replication user repluser. This is true for all `acfsutil repl` commands except for the following commands that read but never modify replication state:

- The `acfsutil` `repl` `info` and `acfsutil` `repl` `bg` `info` commands may be run by any Oracle ASM administrator user.
- The `acfsutil` `repl` `compare` command is allowed to be run by any Oracle ASM administrator user, but should be run as `root` to maximize its access to the files being compared.

Note:

Starting with Oracle ACFS 21c, Oracle ACFS replication protocol version 1 is desupported. Replication protocol version 1 has been replaced with snapshot-based replication version 2, introduced in Oracle ACFS 12c Release 2 (12.2.0.1).

Table 6-21 Summary of commands for Oracle ACFS replication

| Command | Description |
| --- | --- |
| acfsutil repl bg | Starts, stops, or displays information about the Oracle ACFS replication background processes. |
| acfsutil repl compare | Verifies that files have been replicated on an Oracle ACFS storage location. |
| acfsutil repl failover | Converts the role of the replication standby location to that of a primary location in the event of an unplanned failure. |
| acfsutil repl info | Displays information about replication processing on an Oracle ACFS storage location. |
| acfsutil repl init | Initiates replication on files in an Oracle ACFS storage location. |
| acfsutil repl pause | Pauses replication on an Oracle ACFS storage location. |
| acfsutil repl resume | Resumes replication on an Oracle ACFS storage location. |
| acfsutil repl reverse | Reverses the roles of the replication primary and standby storage location. |
| acfsutil repl sync | Synchronizes primary and standby storage locations. |
| acfsutil repl terminate | Stops all replication activity on the Oracle ACFS storage location. |
| acfsutil repl trace | Specifies the trace level for replication information. |
| acfsutil repl update | Updates replication information while replication is running. |

### acfsutil repl bg

Purpose

Starts, stops, or displays information about the Oracle ACFS replication background processes.

Syntax and Description

```
acfsutil repl bg -h
acfsutil repl bg {start | stop | info} [snap_shot@]mount_point
```

`acfsutil` `repl` `bg` `-h` displays help text and exits.

The following table contains the options available with the `acfsutil` `repl` `bg` command.

Table 6-22 Options for the acfsutil repl bg command

| Option | Description |
| --- | --- |
| `start` | Starts the replication background processing. |
| `stop` | Stops the replication background processing |
| `info` | Displays information about the replication background process through the associated clusterware resource. If the resource is `ONLINE` on a node in the primary cluster, the process is running. Otherwise, the process is not running. |
| \[`snap_shot@`\] `mount_point` | Specifies a location being replicated, either the mount point or a snapshot of a mounted primary file system. |

Oracle ACFS replication uses a background process on the primary cluster to transport file system changes to the standby location, either a file system or snapshot. This process must be running for replication to function. When replication is started with the `acfsutil` `repl` `init` command, the process is started and registered with Oracle Clusterware, enabling an automatic restart after a reboot or system crash. This process is clusterwide.

To determine if the Oracle ACFS replication background process is running at the primary site, you can run the `acfsutil` `repl` `bg` `info` command on the primary cluster. For examples of the use of the command, refer to Example 6-19.

Note:

A primary file system containing a location participating in replication can always be unmounted, even if its replication background process is running. The `umount` command stops the background process if it is necessary to enable the unmount to proceed. Any in-progress replication operation is interrupted. When a primary file system containing a location participating in replication is remounted, replication automatically restarts and the background process is restarted.

A standby file system containing a location participating in replication can be unmounted only if a replication operation is not currently in progress on it. If a replication operation is in progress, then an attempt to unmount the file system fails with an indication that the file system is busy.

Examples

Example 6-19 shows the use of the `acfsutil` `repl` `bg` command to display information about replication processes.

Example 6-19 Using the acfsutil repl bg command

```
$ /sbin/acfsutil repl bg info /acfsmounts/acfs1
Resource:      ora.repl.dupd.crsdg1.crsdg1vol1.acfs
Target State:  ONLINE             
Current State: ONLINE on primnode1
```

### acfsutil repl compare

Purpose

Verifies that files have been replicated on an Oracle ACFS storage location.

Syntax and Description

```
acfsutil repl compare -h 
acfsutil repl compare [-v] [ -a [-s] | -t { all | tagname, ...} [-s] ]           
[snap_shot@]primary_mount_point [snap_shot@]standby_mount_point
```

`acfsutil` `repl` `compare` `-h` displays help text and exits.

The following table contains the options available with the `acfsutil` `repl` `compare` command.

Table 6-23 Options for the acfsutil repl compare command

| Option | Description |
| --- | --- |
| `-a` | Compares all files and their extended attribute names. |
| `-t` { `all` \| `tagname`, `...` } | Compares files with all or some tag names specified in the `acfsutil` `repl` `init` operation. The `all` option specifies all tag names supplied in the `acfsutil` `repl` `init` operation. A comma-delimited list of tag names must only use tag names specified during the `acfsutil` `repl` `init` operation. |
| `-s` | Skips comparisons on symlinks for extended attributes and tags when using the `-a` or `-t` option. The symlinks are still checked for everything else, such as permissions and ownership. |
| `-v` | Causes the name of the file in each location to be output after the file is compared. |
| `[snap_shot@]primary_mount_point` | Specifies a location being replicated, either the mount point or a snapshot of a mounted primary file system. |
| `[snap_shot@]standby_mount_point` | Specifies a location being replicated, either the mount point or a snapshot of a mounted standby file system. |

The `acfsutil` `repl` `compare` command verifies all or part of the primary location has been replicated to the standby location. The standby location must be mounted locally for comparison. Best results are obtained when the primary location is changing as little as possible. The command always tries to check all files on the primary location against those on the standby location. To maximize the ability of the command to check all files, it should be invoked as the root user. However, this is not required -- the command will try to compare files when invoked as any user.

The `-a` option is typically used when no tag names were specified during the `acfsutil` `repl` `init` operation. The `-a` option compares all files on the primary location against those on the standby location. The `-a` option also enables tests for extra files on the standby location that do not exist on the primary. When testing for extra files, the command also attempts to check extended attributes. However, if NFS is used to mount the standby location locally, the standby cannot be checked for matching extended attributes due to limitations in the NFS protocol.

The `-t` option is used when tags were specified during the `acfsutil` `repl` `init` operation. The `-t` operation locates all file names on the primary location with the specified tag names and compares them to the corresponding files on the standby. The `-t` option takes as arguments either `all` option or a comma-delimited list of tag names. If the `-t` option is used with the `all` argument, then all tag names supplied during the `acfsutil` `repl` `init` operation are selected. Otherwise, any specified tag names must exactly match a tag name supplied during the `acfsutil` `repl` `init` operation. The `-t` option also tests for extra files on the standby location that do not have an associated tag name that was specified during the `acfsutil` `repl` `init` operation. If NFS is used to mount the standby location locally, the standby cannot be checked for matching tag names and extended attributes due to limitations in the NFS protocol.

You can use the `acfsutil` `repl` `info` `-c` option to determine which tags were specified during the `acfsutil` `repl` `init` operation.

The `-a` and `-t` options cannot both be specified at that same time. When `-a` or `-t` is provided, the `—s` option can also be specified to skip extended attribute comparisons for symlinks. If neither the `-a` nor `-t` option is provided, a primary to standby file comparison is done without testing tag names nor extended attributes.

The `-v` option may be specified to output the name of each file after the file is compared.

Examples

Example 6-20 shows the use of the `acfsutil` `repl` `compare` command.

Example 6-20 Using the acfsutil repl compare command

```
$ /sbin/acfsutil repl compare /acfsmounts/acfs1 /nfs_mounted_standby
```

### acfsutil repl failover

Purpose

Converts the role of the replication standby location to that of a primary location, and potentially the role of the corresponding primary location to that of a standby.

Syntax and Description

```
acfsutil repl failover -h
acfsutil repl failover [-T timeout] [snap_shot@]mount_point
```

`acfsutil` `repl` `failover` `-h` displays help text and exits.

The following table contains the options available with the `acfsutil` `repl` failover command.

Table 6-24 Options for the acfsutil repl failover command

| Option | Description |
| --- | --- |
| `-T timeout` | Specifies the time to wait (minutes) before determining that the primary location is unavailable. If the `-T` option is omitted, the primary location is checked once for availability. |
| \[`snap_shot@`\] `mount_point` | Specifies a location being replicated, either the mount point or a snapshot of a mounted file system. |

The `acfsutil` `repl` `failover` command reverses the role of a replication standby location such that it becomes a replication primary location. The failover command insures that the standby location contains an exact copy of the results of the last successful replication transfer. If necessary, the command restores the location back to its state as of that transfer. `acfsutil` `repl` `failover` behaves differently based on the scenario in which it was run:

- Both the standby location and corresponding primary location are operating normally
	In this scenario, the command reverses the replication relationship. There is no data loss. Note that failover fails in this case if replication is paused. To enable this case to succeed, run `acfsutil` `repl` `resume`.
- The primary location is not currently available, but you want to wait until it is back online
	In this scenario, the command verifies the status of the replication primary. If the primary is not accessible and the timeout period has expired (if specified), then the command restores the standby location to its state as of the last successful replication transfer and converts it into a replication primary. Some data loss is possible, for example if there was a transfer in process when the primary location became unavailable. When the original primary location becomes available, it is aware that the failover command has been run and converts itself into a replication standby location.
- The primary location is not currently available and you do not want to wait until it is back online
	In this scenario, the command verifies the status of the replication primary. If the primary is not accessible and the timeout period has expired (if specified), then the command restores the standby location to its state as of the last successful replication transfer and converts it into a replication primary. Some data loss is possible, for instance if there was a transfer in process when the primary location became unavailable. After the failover command has been run, you have two options:
	- First, a new standby location can be configured using the `acfsutil` `repl` `update` command. Note that it is harmless if the original primary returns (as a standby) after you have specified the new standby. The original primary location remains idle (as a standby) until you run `acfsutil` `repl` `terminate` `standby` for that location.
		- Alternatively, you can terminate replication by running `acfsutil` `repl` `terminate` `primary` on the new primary.

When the current primary location is active, you should quiesce application updates to the primary before running `acfsutil` `repl` `failover`. Any updates attempted to the current primary location before its conversion to a standby are discarded. Any updates attempted to it after its conversion fail, just as updates would to any other standby location.

When application updates are resumed, they must be directed to the new primary location.

Examples

The following example shows the use of the `acfsutil` `repl` `failover` command. The command is invoked on the standby location (`/repl_data`).

Example 6-21 Using the acfsutil repl failover command

```
acfsutil repl failover /repl_data
```

See Also:

- acfsutil repl update for information about updating replication information
- [Configuring Oracle ACFS Snapshot-Based Replication](acfs-advanced-topics.md) for information about configuring `ssh` for use with Oracle ACFS replication

### acfsutil repl info

Purpose

Displays information about replication processing on an Oracle ACFS storage location.

Syntax and Description

```
acfsutil repl info -h 

acfsutil repl info -c [-v] {[snap_shot@]mount_point}                    

acfsutil repl info -c -u user [-o sshStrictKey=yn_value] standby_host [standby_host...]
                    [snap_shot@]primary_mount_point

acfsutil repl info -c -u user [-o sshStrictKey=yn_value] primary_host [primary_host...]
                    [snap_shot@]standby_mount_point

acfsutil repl info -s [-v][-l] [-n number{m|h|d|w|y}] 
                   {-f eventlog | [snap_shot@]mount_point}}

acfsutil repl info [-a|-e|-t] [-v][-l]
                   {-f eventlog | [snap_shot@]mount_point }
```

`acfsutil` `repl` `info` `-h` displays help text and exits.

The following table contains the options available with the `acfsutil` `repl` `info` command.

Table 6-25 Options for the acfsutil repl info command

| Option | Description |
| --- | --- |
| `-a` | Displays only apply records from the replication event log. An apply record contains the date and time that the set of replicated changes were captured on the primary location and the date and time that they were applied on the standby location. |
| `-c` | Displays configuration information. |
| `-e` | Displays only error records from the replication event log. |
| `-f` `eventlog` | Specifies the absolute path to the replication event log to be used as the source of the information. The default location is: `mount_point` `/.ACFS/repl/logs/ReplicationEventsLog` |
| `-h` | Displays help text. |
| `-l` | Displays last event only. |
| `-n` `number` { `m` \| `h` \| `d` \| `w` \| `y` } | Specifies the interval to display information. `number` specifies the number of minutes (`m`), hours (`h`), days (`d`), weeks (`w`), or years (`y`). For example: `-n` `5d`  The statistics are summarized in the units of time specified. |
| `-u user` | Validates the host and user keys currently configured between the current host and each standby host specified with a standby argument, using user as the user for which access is validated. |
| `-o sshStrictKey=yn_value` | Specifies whether `ssh` should use strict host-key checking. A value starting with `y` enables this checking, which is the default setting. A value starting with `n` disables the checking. |
| `-s` | Displays statistical information. It is important that the primary and standby nodes are running a network time service to ensure that the statistics are meaningful. |
| `-t` | Displays only transport records from the replication event log. |
| `-v` | Displays verbose output. |
| `standby_host` | Specifies a hostname or IP address for one of the standby hosts to be processed when the `-u` option is specified. |
| \[`snap_shot@`\] `primary_mount_point` | Specifies a location participating in replication, either a directory or a snapshot where the primary file system is mounted. |
| `primary_host` | Specifies a hostname or IP address for one of the primary hosts to be processed when the `-u` option is specified. |
| \[`snap_shot@`\] `standy_mount_point` | Specifies a location participating in replication, either a directory or a snapshot where the standby file system is mounted. |
| \[`snap_shot@`\] `mount_point` | Specifies a location being replicated, either the mount point or a snapshot of a mounted primary or standby file system. |

To display information about replication configuration, use `acfsutil` `repl` `info` with the `-c` option. The configuration information includes a `Applied` `primary` `as` `of` timestamp that identifies the point in time on the primary location that the standby location represents. You can use this timestamp to set back a database to this point in time if it is necessary to keep the data in Oracle ACFS location synchronized with the database data replicated with Oracle Data Guard.

When specifying the `-u` option, the command should be run as `repluser`, the replication user. With this option, the command confirms that `ssh`, as used by snapshot-based replication, can connect from the local cluster to the remote cluster. The command should be used in two contexts:

- On each host of the primary cluster, to confirm that `ssh` can connect to all standby hosts and log in as user on each host
- On each host of the standby cluster, to confirm that `ssh` can connect to all primary hosts and log in as user on each host

When the command is run on a primary host, each standby\_host string specifies a hostname or host IP address for a standby node. The specified \[`snap_shot@`\] `primary_mount_point` should be the active Oracle ACFS location in the primary cluster that is to be used for replication.

When the command is run on a standby host, each primary\_host string specifies a hostname or host IP address for a primary node. The specified \[`snap_shot@`\] `standby_mount_point` should be the active Oracle ACFS location in the standby cluster that is to be used for replication.

In all cases, the user specified should be the same as the repluser specified in the `acsfutil` `repl` `init` command. If strict host-key checking was or is to be disabled for this instance of replication, for example with `acsfutil` `repl` `init` `primary` using `-o sshStrictKey=no`, then the option should also be specified here to skip host-key validation. `acfsutil` `repl` `info` `-c` `-u` can be run at any time, whether or not replication is currently active on the specified Oracle ACFS location.

To display information about replication statistics, use `acfsutil` `repl` `info` with the `-s` option.

To display information about all replication events, use `acfsutil` `repl` `info` with no options. To display information about a specific kind of event, use `acfsutil` `repl` `info` with the `-a`, `-e`, or `-t` option.

Examples

Example 6-22 shows the use of the `acfsutil` `repl` `info` command.

Example 6-22 Using the acfsutil repl info command

The validation command has the following format:

```
# /sbin/acfsutil repl info -c -u repluser standby-addr1 [standby-addr2 …] my_primary_mountpoint
```

The command confirms that user `repluser` can use `ssh` to connect to each standby-addr given in the same way as replication does when initializing. The my\_primary\_mountpoint given should be the active Oracle ACFS mount point that is to be used for replication.

If you have two standby nodes named standby1 and standby2, and also have a VIP named standby12\_vip that can designate either node, then you can validate the key setup for the standby1 /standby2 cluster by running the following command on each node of the primary cluster:

```
# /sbin/acfsutil repl info -c -u repluser standby1 standby2 my_primary_mountpoint
```

The same command would be used for validation using the VIP standby12\_vip to connect to the cluster.

If you plan to disable strict host key checking, you can skip this checking by adding the `-o` `sshStrictKey=no` option to the command line.

Additional commands for displaying statistics and apply records are the following:

```
$ /sbin/acfsutil repl info -s -n 5d /acfsmounts/acfs1

$ /sbin/acfsutil repl info -a -v /acfsmounts/acfs1
```

### acfsutil repl init

Purpose

Initiates replication on all the files in an Oracle ACFS storage location or only those files with a specified list of tags.

Syntax and Description

```
acfsutil repl init -h

acfsutil repl init standby -u repluser [-d trace_level] [snap_shot@]standby_mount_point

acfsutil repl init primary -s repluser@netname { -C | -M | -i interval} [tag_name...]
                           [-m [snap_shot@]standby_mount_point] [-d trace_level] [-z {on | off}] 
                           [-o sshCmdPath=pathname] [-o sshStrictKey=ynvalue] 
                           [-o sshCipher=ciphername] [-o sshOptions=options] [-p [repluser@]netname]
                           [snap_shot@]primary_mount_point
```

`acfsutil` `repl` `init` `-h` displays help text and exits.

The following table contains the options available with the `acfsutil` `repl` `init` command.

Table 6-26 Options for the acfsutil repl init command

| Option | Description |
| --- | --- |
| `primary` | Specifies replication of the primary location. |
| `standby` | Specifies replication of the standby location. |
| `-s` repluser@netname | Specifies a standard `ssh` connection string for the primary site to contact the standby site.  The repluser in the connection string is the user that `ssh` logs in as on the standby node. Choose a minimally-privileged user identity. The user should have Oracle ASM administrator privileges and should belong to the Oracle DBA group.  Note:  The same user and group identities (including all `uids` and `gids`) must be specified for the replication user on both your primary cluster and your standby cluster.  The netname in the connection string specifies a network endpoint, such as a host name, VIP name, or IP address. |
| `—C` | Specifies replication in constant mode. Snapshots are continuously generated and replicated to the standby site. As soon as the replication of each snapshot completes, the generation of a new snapshot is started. |
| `—M` | Specifies replication in manual mode. After the initial replication operation is performed, no further replication occurs until requested manually by running `acfsutil` `repl` `sync`. |
| `—i` interval | Specifies replication in interval (scheduled) mode. A new snapshot is taken and replicated with the frequency specified, if possible. A suffix must be given to specify the units in which interval is measured. The suffix must be either `s` (seconds), `` `m` `` (minutes), `h` (hours), `d` (days), or `w` (weeks). For example, `30m` is thirty minutes and `2h` is two hours. |
| `tag_name` | Specifies one or more tag names to be used in restricting replication. When tag names are specified, only files that are tagged with at least one of the those tag names are replicated. For information about Oracle ACFS tags, refer [Oracle ACFS Tagging](understand-acfs-admin.md). |
| `-m` `[snap_shot@]standby_mount_point` | Specifies the standby storage location, if it is different than the primary location. |
| `-d` `trace_level` | Specifies the trace level setting \[0..6\]. |
| `-z` `on` \| `off` | Turns on or off compression of the replication data stream sent from primary to standby. |
| `-o sshCmdPath=pathname` | Specifies the pathname to the `ssh` command. |
| `-o sshStrictKey=ynvalue` | Specifies whether `ssh` should use strict host-key checking. A value starting with `y` enables this checking, which is the default setting. A value starting with `n` disables the checking. |
| `-o sshCipher=ciphername` | Specifies the cipher that is passed to `ssh` to encrypt its sessions. |
| `-o sshOptions=options` | Specifies options to be passed to each invocation of `ssh` made by replication. No restrictions are imposed on the contents of options. However, the resulting invocation of `ssh` is validated before replication is started, and `acfsutil` `repl` `init` `primary` fails if the validating invocation of `ssh` fails. |
| `-p [repluser@]netname` | Specifies the network endpoint for the primary location. netname names a network endpoint, such as a host name, VIP name, or IP address. netname is checked to ensure it can be accessed. repluser, if given, must match the repluser specified to `acfsutil` `repl` `init` `standby`.  If `-p` is not given, then the SCAN VIP associated with the primary cluster, if available, is used as the network endpoint for the primary location. If the SCAN VIP is not available, then the hostname of the machine where this command was invoked is used. |
| `-u` | Specifies the repluser. |
| `[snap_shot@]standby_mount_point` | Specifies a location being replicated, either the mount point or a snapshot of a mounted standby file system. |
| `[snap_shot@]primary_mount_point` | Specifies a location being replicated, either the mount point or a snapshot of a mounted primary file system. |

The `acfsutil` `repl` `init` `primary` and `standby` commands initiate replication between a specified primary site and a specified standby site. The `acfsutil` `repl` `init` `standby` command must be run first. Next, run the `acfsutil` `repl` `init` `primary` command.

When the `acfsutil` `repl` `init` `primary` command completes successfully, processing begins to replicate initial copies of all specified files to the standby location. In addition, any changes to these files and any new files subsequently created in the primary storage location are captured and transported to the standby location. However, successful completion of the command does not indicate that the specified files have been copied in full to the standby location. To monitor the progress of the initial replication of all specified files to the standby location, users can run the `acfsutil` `repl` `info` `-c` command.

The initial replication operation is based on a snapshot of the primary location, which is transferred to the standby location in its entirety. Each subsequent replication operation uses a later snapshot of the primary location, and only the differences between that snapshot and the last previous snapshot are transferred to the standby location.

All directories in the primary location are always replicated to the standby, even if tags are specified.

Symbolic link files are replicated as is. If the symbolic link resolves to an absolute path name, and that path name does not exist on the standby location, then referencing the symbolic link results in errors.

On platforms that support named sockets, character device files or block device files, these file types are not replicated.

The file system containing a primary or standby storage location can be mounted on only one mount point in its cluster. The file system does not have to be mounted on all of the nodes in a cluster, but if it is mounted, it must be mounted on the mount point specified with the `acfsutil` `repl` `init` command. In addition, no other file system can be mounted on that mount point on other nodes.

A single Oracle ACFS location cannot be configured both as a primary and a standby location. If replication is configured on the same host or within the same cluster, then the primary and standby locations cannot use the same named mount point.

Replication is allowed between sites running any combination of the Linux, Solaris or AIX operating systems.

Examples

Example 6-23 shows the use of the `acfsutil` `repl` `init` to initiate snapshot-based replication from the primary to standby site.

Example 6-23 Using the acfsutil repl init command

```
# /sbin/acfsutil repl init standby -u my_repluser /my_standby/repl_data

# /sbin/acfsutil repl init primary -s my_repluser@my_host -i 2h
                                   -m /my_standby/repl_data /my_primary/repl_data
```

### acfsutil repl pause

Purpose

Pauses replication on an Oracle ACFS primary location.

Syntax and Description

```
acfsutil repl pause -h
acfsutil repl pause [snap_shot@]mount_point
```

`acfsutil` `repl` `pause` `-h` displays help text and exits.

The following table contains the options available with the `acfsutil` `repl` `pause` command.

Table 6-27 Options for the acfsutil repl pause command

| Option | Description |
| --- | --- |
| \[`snap_shot@`\] `mount_point` | Specifies a location being replicated, either the mount point or a snapshot of a mounted primary file system. |

The `acfsutil` `repl` `pause` command is issued at the primary replication site only. To continue replication operations, `acfsutil` `repl` `resume` should be run at a later time on the same primary site.

`acfsutil` `repl` `pause` stops the operation of the replication daemon temporarily. Subsequent running of `acfsutil` `repl` `resume` resumes the operation of the daemon.

If `acfsutil` `repl` `pause` is run while a replication operation is active, then the active replication operation completes regardless of the pause action. The pause operation is not effective in this case, and the command does not return, until the current data stream has been applied on the standby. After that, operations are not performed for this replication until the `acfsutil` `repl` `resume` is issued.

Note:

If replication is paused when using `acfsutil` `repl` `reverse`, or when using `acfsutil` `repl` `failover` with both the primary and the standby operating normally, then planned failover fails. To enable planned failover to succeed in these situations, run `acfsutil` `repl` `resume`.

Examples

Example 6-24 shows the use of the `acfsutil` `repl` `pause` command.

Example 6-24 Using the acfsutil repl pause command

```
$ /sbin/acfsutil repl pause /acfsmounts/acfs1
```

### acfsutil repl resume

Purpose

Resumes replication on an Oracle ACFS location where replication has been paused.

Syntax and Description

```
acfsutil repl resume -h
acfsutil repl resume [snap_shot@]mount_point
```

`acfsutil` `repl` `resume` `-h` displays help text and exits.

The following table contains the options available with the `acfsutil` `repl` `resume` command.

Table 6-28 Options for the acfsutil repl resume command

| Option | Description |
| --- | --- |
| \[`snap_shot@`\] `mount_point` | Specifies a location being replicated, either the mount point or a snapshot of a mounted primary file system. |

The `acfsutil` `repl` `resume` command resumes the replication process after the `acfsutil` `repl` `pause` command has been run. This command should be run on the same primary site soon after replication has been paused with the `acfsutil` `repl` `pause` command.

Examples

Example 6-25 shows the use of the `acfsutil` `repl` `resume` command.

Example 6-25 Using the acfsutil repl resume command

```
$ /sbin/acfsutil repl resume /acfsmounts/acfs1
```

### acfsutil repl reverse

Purpose

Reverses the roles of the replication primary and standby locations.

Syntax and Description

```
acfsutil repl reverse -h
acfsutil repl reverse primary [snap_shot@]mount_point
acfsutil repl reverse standby [-o sshCmdPath=path_name] [snap_shot@]mount_point
```

`acfsutil` `repl` `reverse` `-h` displays help text and exits.

The following table contains the options available with the `acfsutil` `repl` `reverse` command.

Table 6-29 Options for the acfsutil repl reverse command

| Option | Description |
| --- | --- |
| `primary` | Specifies the primary location. |
| `standby` | Specifies the standby location. |
| `-o sshCmdPath=path_name` | Specifies the path\_name to the `ssh` command on the current standby location. |
| \[`snap_shot@`\] `mount_point` | Specifies a location being replicated, either the mount point or a snapshot of a mounted file system. |

The `acfsutil` `repl` `reverse` command reverses the roles of a replication primary and standby location without requiring replication to be terminated and restarted. First, complete the necessary configuration for role reversal replication that is described in [Configuring Oracle ACFS Snapshot-Based Replication](acfs-advanced-topics.md). After the configuration is completed, perform the following steps for role reversal of the primary and standby:

1. To begin the role reversal, run the `acfsutil` `repl` `reverse` `primary` operation in the primary cluster. This step ensures that the primary replication location, standby replication location, and the backup snapshot of the standby are all identical, and then converts the current primary to be a standby. Replication is now suspended until the final step is completed.
2. To complete the role reversal, run the `acfsutil` `repl` `reverse` `standby` operation in the standby cluster. This step converts the current standby replication location to be a primary location, then resumes replication from the new primary to the new standby.

You should quiesce application updates to the current primary before running `acfsutil` `repl` `reverse` `primary`. Any updates attempted to the current primary after its conversion to a standby fail, just as updates would to any other standby. When application updates are resumed, they must be directed to the new primary. Note that role reversal fails if replication is paused. To enable role reversal, run `acfsutil` `repl` `resume`.

Examples

The following example shows the use of the `acfsutil` `repl` `reverse` command.

Example 6-26 Using the acfsutil repl reverse command

```
acfsutil repl reverse primary /my_primary/repl_data
acfsutil repl reverse standby /my_standby/repl_data
```

### acfsutil repl sync

Purpose

Synchronizes primary and standby locations.

Syntax and Description

```
acfsutil repl sync -h
acfsutil repl sync [apply] [snap_shot@]mount_point
```

`acfsutil` `repl` `sync` `-h` displays help text and exits.

The following table contains the options available with the `acfsutil` `repl` `sync` command.

Table 6-30 Options for the acfsutil repl sync command

| Option | Description |
| --- | --- |
| `apply` | Specifies that all changes be applied to the standby location. Currently has no effect on the operation of the command. |
| \[`snap_shot@`\] `mount_point` | Specifies a location being replicated, either the mount point or a snapshot of a mounted primary file system. |

The `acfsutil` `repl` `sync` command can be used to synchronize the state of the primary site and the standby site. This command can only be run on the primary site. Users should first quiesce their applications and issue a `sync(1)` call to ensure that the synchronized state is known and meaningful to the user. Running `acfsutil` `repl` `sync` then ensures all outstanding replication data is shipped from the primary site to the standby site. Specifically, the command enables any in-progress replication operation to complete, and then performs replication one final time to ensure that all changes on the primary have been replicated.

The command completes successfully when all of the changes have been successfully applied to the replication location on the standby site. At this point, unless an unmount of the last node on the primary site cluster is about to occur, applications may be restarted.

Successfully unmounting a replicated location on the primary site does not guarantee that all changes made prior to the unmount have been successfully sent to the standby site or applied to the standby location. If the primary location is on a file system that is unmounted on one primary site node, but remains mounted on one or more primary site nodes, changes to the location made before the unmount continue to be transported to the standby site from the other nodes after the unmount. However, if you are in the process of unmounting the primary location on the last primary site node where it is mounted, and if you want to know that all file system changes on the primary location up to that point have been successfully applied to the standby location, then you should perform the following operations to ensure that the standby location is up to date.

- Quiesce applications on the primary site which modify the replication location.
- Run `acfsutil` `repl` `sync`.

After `acfsutil` `repl` `sync` has returned successfully, you can unmount the file system which contains the participating replication location. Unmounting the file system stops the replication background process for that location.

Examples

Example 6-27 shows the use of the `acfsutil` `repl` `sync` command.

Example 6-27 Using the acfsutil repl sync command

```
$ /sbin/acfsutil repl sync /acfsmounts/acfs1
```

### acfsutil repl terminate

Purpose

Stops all replication activity on the Oracle ACFS location at the site where it is run.

Syntax and Description

```
acfsutil repl terminate -h
acfsutil repl terminate primary [-d trace_level] [snap_shot@]mount_point 
acfsutil repl terminate standby [remote [-f]] [immediate] [-k] [-d trace_level] [snap_shot@]mount_point
```

`acfsutil` `repl` `terminate` `-h` displays help text and exits.

The following table contains the options available with the `acfsutil` `repl` `terminate` command.

Table 6-31 Options for the acfsutil repl terminate command

| Option | Description |
| --- | --- |
| `primary` | Stops replication on the primary location. |
| `standby` | Stops replication on the standby location. |
| `remote  [-f]` | Stops replication processing on the primary location before stopping the processing on the standby location.  When the remote keyword is given, the `-f` option forces the termination of replication on the standby location even if replication on the primary location cannot be terminated. |
| `immediate` | Stops replication processing immediately on the standby location. |
| `—k` | Specifies to keep any backup snapshot that is present for the standby. However, this option does not ensure that a backup snapshot exists, and the absence of such a backup snapshot is not an error.  If this option is not specified, then any backup snapshot present is deleted. |
| `-d` `trace_level` | Specifies the trace level setting \[0..6\]. |
| \[`snap_shot@`\] `mount_point` | Specifies a location being replicated, either the mount point or a snapshot of a mounted file system. |

The `acfsutil` `repl` `terminate` command stops all replication processing. When terminating replication, you should terminate replication for the primary location first, and then the standby location. If you want to ensure all changes are sent to the standby location before terminating the primary site, ensure that all applications are quiesced and run the `acfsutil` `repl` `sync` command. The terminate command must be run on both sites if both sites hosting the locations are available.

After `acfsutil` `repl` `terminate` `standby` has been run, you can use the standby location in read-write mode. If you want to restart replication after running `acfsutil` `repl` `terminate`, then you must restart replication from the beginning with the `acfsutil` `repl` `init` command.

The `repl` `terminate` `standby` command waits until replication data at the standby location has been applied. If you want to terminate replication immediately without applying all the replication data, use the `immediate` option. However, this option can leave some files at the standby location in an indeterminate state.

To momentarily stop Oracle ACFS replication, you can use the `acfsutil` `repl` `pause` command, followed soon after by the `acfsutil` `repl` `resume` command.

Note:

Running `acfsutil` `repl` `terminate` `standby` with the `remote` option fails:
- If the primary location is paused.
- While the primary location is converting to a standby.
	For example, if `acfsutil` `repl` `reverse` `primary` has been invoked on the primary location.

Examples

Example 6-28 shows the use of the `acfsutil` `repl` `terminate` command.

Example 6-28 Using the acfsutil repl terminate command

```
$ /sbin/acfsutil repl terminate /acfsmounts/acfs1
```

### acfsutil repl trace

Purpose

Sets the replication trace level for gathering trace information on an Oracle ACFS location.

Syntax and Description

```
acfsutil repl trace -h
acfsutil repl trace level [snap_shot@]mount_point
```

`acfsutil` `repl` `trace` `-h` displays help text and exits.

The following table contains the options available with the `acfsutil` `repl` `trace` command.

Table 6-32 Options for the acfsutil repl trace command

| Option | Description |
| --- | --- |
| `level` | Specifies the trace level setting \[0..6\]. The default level is 2. |
| \[`snap_shot@`\] `mount_point` | Specifies a location being replicated, either the mount point or a snapshot of a mounted file system. |

Increasing the trace level can have a performance impact and should be done at the recommendation of Oracle support services.

Trace files for Oracle ACFS replication are stored in the following location:

```
GRID_BASE/diag/crs/hostname/crs/trace
```

In the location above, `GRID_BASE` specifies the `ORACLE_BASE` of the Oracle Grid Infrastructure home.

Examples

Example 6-29 shows the use of the `acfsutil` `repl` `trace` command.

Example 6-29 Using the acfsutil repl trace command

```
$ /sbin/acfsutil repl trace 5 /acfsmounts/acfs1
```

### acfsutil repl update

Purpose

Updates the replication configuration after replication has started and is running on an Oracle ACFS location.

Syntax and Description

```
acfsutil repl update -h

acfsutil repl update  [-s netname] [-C | -M | -i interval] 
                      [-d trace_level] [-z {on | off}] [-p netname]
                      [-o sshCmdPath=pathname] [-o sshStrictKey=ynvalue] 
                      [-o sshCipher=ciphername] [-o sshOptions=options] [-P]
                      [-m snap_shot@]standby_mount_point] [snap_shot@]primary_mount_point

acfsutil repl update [-d trace_level] [snap_shot@]standby_mount_point
```

`acfsutil` `repl` `update` `-h` displays help text and exits.

The following table contains the options available with the `acfsutil` `repl` `update` command.

Table 6-33 Options for the acfsutil repl update command

| Option | Description |
| --- | --- |
| `-s ` netname | Specifies a new network endpoint for the primary site to contact the standby site.  netname specifies a network endpoint, such as a host name, VIP name, or IP address.  netname is checked to ensure it can be accessed. |
| `—C` | Specifies replication in constant mode. Snapshots are continuously generated and replicated to the standby site. As soon as the replication of each snapshot completes, the generation of a new snapshot is started. |
| `—M` | Specifies replication in manual mode. After the next replication operation is performed, no further replication occurs until requested manually by running `acfsutil` `repl` `sync`. |
| `—i` interval | Specifies replication in interval (scheduled) mode. A new snapshot is taken and replicated with the frequency specified, if possible. A suffix must be given to specify the units in which interval is measured. The suffix must be either `s` (seconds), `` `m` `` (minutes), `h` (hours), `d` (days), or `w` (weeks). For example, `30m` is thirty minutes and `2h` is two hours. |
| `-d` `trace_level` | Specifies the trace level setting \[0..6\]. |
| `-z` `on` \| `off` | Turns on or off compression of the replication data stream sent from primary to standby. |
| `-o sshCmdPath=pathname` | Specifies the pathname to the `ssh` command. |
| `-o sshStrictKey=ynvalue` | Specifies whether `ssh` should use strict host-key checking. A value starting with `y` enables this checking, which is the default setting. A value starting with `n` disables the checking. |
| `-o sshCipher=ciphername` | Specifies the cipher that is passed to `ssh` to encrypt its sessions. |
| `-o sshOptions=options` | Specifies options to be passed to each invocation of `ssh` made by replication. No restrictions are imposed on the contents of options. However, the resulting invocation of `ssh` is immediately validated, and `acfsutil` `repl` `update` fails if the validating invocation of `ssh` fails. |
| `-p ` netname | Specifies a new network endpoint for the primary site. netname names a network endpoint, such as a host name, VIP name, or IP address. netname is checked to ensure it can be accessed. |
| `-P` | Removes any network endpoint previously specified with the `-p` option to `acfsutil` `repl` `update` or `acfsutil` `repl` `init` `primary`, and restores the default network endpoint. Specifically, the SCAN VIP associated with the primary cluster, if available, is used as the network endpoint for the primary location. If the SCAN VIP is not available, the hostname of the machine where this command was invoked is used. |
| \[-m `snap_shot@`\] `standby_mount_point]` | Specifies the standby storage area. |
| \[`snap_shot@`\] `primary_mount_point` | Specifies a location being replicated, either the mount point or a snapshot of a mounted primary file system. |
| \[`snap_shot@`\] `standby_mount_point` | Specifies a location being replicated, either the mount point or a snapshot of a mounted standby file system. |

The `acfsutil` `repl` `update` command updates replication information and configuration after replication has been started. For example, a system administrator can change the network interface that is currently being used by replication to connect to the remote site. Issuing the `acfsutil` `repl` `update` command to update the configuration in this situation enables replication to continue running uninterrupted.

If `acfsutil` `repl` `update` is run on the primary site, then the command can be used to change the replication interval or tracing level, change the cipher used by or the pathname used for `ssh`, and turn compression on or off. The command can also be used to alter the network interface name (hostname or VIP name) that is used to connect to the standby site, or to update the standby storage location. If these updates, with the `-m` or `-s` option, designate a different storage location than was previously in use, then the previous standby storage location is left unchanged. The location is still marked as a replication standby, but can no longer be used for replication. The location is now simply a read-only file system or snapshot. To revert the previous standby to normal read-write status, run `acfsutil` `repl` `terminate` `standby` on it.

If `acfsutil` `repl` `update` is run on the standby site, the command can be used to alter the tracing level.

At least one of the options must be specified when issuing this command; the command cannot be run with only the required location.

The `acfsutil` `repl` `update` command returns success when the updated information has been accepted on the local site. If the replication interval is changed with the `-C` or `-i` option, a replication operation occurs at the point when `acfsutil` `repl` `update` is run. The next replication operation occurs based on the newly-specified interval.

Examples

Example 6-30 shows the use of the `acfsutil` `repl` `update` command.

Example 6-30 Using the acfsutil repl update command

```
$ /sbin/acfsutil repl update -i 1h /my_primary/repl_data
```