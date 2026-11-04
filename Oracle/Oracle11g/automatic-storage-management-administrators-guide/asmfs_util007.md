---
title: Oracle ACFS Command-Line Tools for Replication
book: "Automatic Storage Management Administrator's Guide"
doc_id: E18951-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e18951/asmfs_util007.htm
tags:
  - oracle
  - 11g
  - automatic-storage-management-administrators-guide
---

Table 13-29 contains a summary of the commands for Oracle ACFS replication.

You can run `acfsutil` `help` on all platforms to display help text. You can run `acfsutil` `version` on all platforms to display the Oracle ACFS version.

When the options are entered with commands on a Windows platform, use `/` instead of `-` with the option. For example, you can display help for `acfsutil` on a Linux platform with `acfsutil` `-h`. On a Windows platform, use `acfsutil` `/h`.

Note that a mount point on a Windows operating system can be a drive letter or a directory including the drive letter.

You must use a trailing back slash when specifying a drive letter mount point with replication commands on Windows platforms. For example, use `p:\` (not `p:`) for a drive letter mount point. If the trailing back slash is omitted, this could trigger a Windows path substitution mechanism that replaces the drive letter with the last accessed path on that drive.

Table 13-29 Summary of commands for Oracle ACFS replication

| Command | Description |
| --- | --- |
| acfsutil repl bg | Starts, stops, or displays information about the Oracle ACFS replication background processes. |
| acfsutil repl compare | Verifies that files have been replicated on an Oracle ACFS file system. |
| acfsutil repl info | Displays information about replication processing on an Oracle ACFS file system. |
| acfsutil repl init | Initiates replication on files in an Oracle ACFS file system. |
| acfsutil repl pause | Pauses replication on an Oracle ACFS file system. |
| acfsutil repl resume | Resumes replication on an Oracle ACFS file system. |
| acfsutil repl sync | Synchronizes primary and standby file systems. |
| acfsutil repl terminate | Stops all replication activity on the Oracle ACFS file system. |
| acfsutil repl trace | Specifies the trace level for replication information. |
| acfsutil repl update | Updates replication information while replication is running. |

## acfsutil repl bg

Purpose

Starts, stops, or displays information about the Oracle ACFS replication background processes.

Syntax and Description

  
`acfsutil` `repl` `bg` `-h`  
`acfsutil` `repl` `bg` { `start` | `stop` | `info` } `mount_point`  

`acfsutil` `repl` `bg` `-h` displays help text and exits.

Table 13-30 contains the options available with the `acfsutil` `repl` `bg` command.

Table 13-30 Options for the acfsutil repl bg command

| Option | Description |
| --- | --- |
| `start` | Starts the replication background processing. |
| `stop` | Stops the replication background processing |
| `info` | Displays information about the replication background processes. |
| `mount_point` | Specifies the directory where the file system is mounted. |

Oracle ACFS replication uses background processes to transport file system changes, to communicate between the sites hosting the primary and standby file systems, to monitor the state of replication processing, and to apply file system changes to the standby file system. These background processes must be running for replication to function.

When replication is started with the `acfsutil` `repl` `init` command, these background processes are started and are registered with Oracle Clusterware so that they are automatically restarted after a reboot or system crash. Usually it is not necessary to run the `acfsutil` `repl` `bg` command because Oracle Clusterware automatically starts and stops the background processes as file systems are mounted and unmounted or node membership changes after replication is initialized. However, replication cannot progress if one of the daemons is not running. In this case running `repl` `bg` `stop` followed by `repl` `bg` `start` ensures that all the daemons are running.

`acfsutil` `bg` `start` ensures that all the necessary daemons for replication are running. The daemons may run on different cluster nodes. `acfsutil` `bg` `stop` ensures that no daemons for the file system are running on the local node and relocates the daemons to another node if available.

You must have system administrator privileges to run the `acfsutil` `repl` `bg` `start` or `acfsutil` `repl` `bg` `stop` commands.You must have system administrator or Oracle ASM administrator privileges to run the `acfsutil` `repl` `bg` `info` command.

Examples

Example 13-24 shows the use of the `acfsutil` `repl` `bg` command.

Example 13-24 Using the acfsutil repl bg command

```
$ /sbin/acfsutil repl bg start /u01/app/acfsmounts/myacfs

$ /sbin/acfsutil repl bg stop /u01/app/acfsmounts/myacfs

$ /sbin/acfsutil repl bg info /u01/app/acfsmounts/myacfs
```

## acfsutil repl compare

Purpose

Verifies that files have been replicated on an Oracle ACFS file system.

Syntax and Description

  
`acfsutil` `repl` `compare` `-h`  
`acfsutil` `repl` `compare` \[`-a`\] \[`-t` { `all` | `tagname`,...}\]  
 `primary_mount_point` `standby_mount_point`  

`acfsutil` `repl` `compare` `-h` displays help text and exits.

Table 13-31 contains the options available with the `acfsutil` `repl` `compare` command.

Table 13-31 Options for the acfsutil repl compare command

| Option | Description |
| --- | --- |
| `-a` | Compares all files and their extended attribute names. |
| `-t` { `all` \| `tagname`,... } | Compares files with all or some of the tag names specified in the `acfsutil` `repl` `init` operation. The `all` option specifies all tag names supplied in the `acfsutil` `repl` `init` operation. A comma separated list of tag names must only use tag names specified during the `acfsutil` `repl` `init` operation. |
| `primary_mount_point` | Specifies the directory where the primary file system is mounted. |
| `standby_mount_point` | Specifies the directory where the standby file system is mounted. |

The `acfsutil` `repl` `compare` command verifies all or part of the primary mount point has been replicated to the standby mount point. The standby mount point must be mounted locally for comparison. Best results are obtained when the primary file system is changing as little as possible.

The `-a` option is typically used when no tag names were specified during the `acfsutil` `repl` `init` operation. The `-a` option compares all files on the primary file system against those on the standby file system. The `-a` option also tests for extra files on the standby file system that do not exist on the primary.

The `-t` option is used when tags were specified during the `acfsutil` `repl` `init` operation. The `-t` operation locates all file names on the primary file system with the specified tag names and compares them to the corresponding files on the standby. The `-t` option takes as arguments either `all` option or a comma separated list of tag names. If the `-t` option is used with `all`, then all tag names supplied during the `acfsutil` `repl` `init` operation are selected. Otherwise, any specified tag names must exactly match a tag name supplied during the `acfsutil` `repl` `init` operation. The `-t` option also tests for extra files on the standby file system that do not have an associated tag name that was specified during the `acfsutil` `repl` `init` operation. The `acfsutil` `repl` `info` `-c` option can be used to determine what tags were specified during the `acfsutil` `repl` `init` operation.

If neither the `-a` nor `-t` option is provided, a primary to standby file comparison is done without testing tag names nor extended attributes.

If NFS is used to mount the standby file system locally, the standby cannot be checked for matching tag names and extended attributes due to limitations in the NFS protocol.

Examples

Example 13-25 shows the use of the `acfsutil` `repl` `compare` command.

Example 13-25 Using the acfsutil repl compare command

```
$ /sbin/acfsutil repl compare /u01/app/acfsmounts/myacfs /nfs_mounted_standby
```

## acfsutil repl info

Purpose

Displays information about replication processing on an Oracle ACFS file system.

Syntax and Description

  
`acfsutil` `repl` `info` `-h`  
`acfsutil` `repl` `info` `-c` \[`-v`\] `mount_point`  
`acfsutil` `repl` `info` `-s` \[`-v`\]\[`-l`\] \[`-n` `number` {m| `h` | `d` | `w` | `y` }\]  
 \[`-r` `start_time` \[`#` `stop_time`\]\] \[`-f` `eventlog`\] `mount_point`  
`acfsutil` `repl` `info` \[`-a` | `-e` | `-t`\] \[`-v`\]\[`-l`\]  
 \[`-r` `start_time` \[`#` `stop_time`\]\] \[`-f` `eventlog`\] `mount_point`  

`acfsutil` `repl` `info` `-h` displays help text and exits.

Table 13-32 contains the options available with the `acfsutil` `repl` `info` command.

Table 13-32 Options for the acfsutil repl info command

| Option | Description |
| --- | --- |
| `-a` | Displays only apply records from the replication event log. An apply record contains the date and time that the set of file system changes were captured on the primary file system and the date and time that they were applied on the standby file system. |
| `-c` | Displays configuration information. |
| `-e` | Displays only error records from the replication event log. |
| `-f` `eventlog` | Specifies the path to the replication event log to be used as the source of the information. The default location is: `mount_point` `/.ACFS/repl/logs/ReplicationEventsLog` |
| `-h` | Displays help text. |
| `-l` | Displays last event only. |
| `-n` `number` { `m` \| `h` \| `d` \| `w` \| `y` } | Specifies the interval to display information. `number` specifies the number of minutes (`m`), hours (`h`), days (`d`), weeks (`w`), or years (`y`). For example: `-n` `5d`  The statistics are summarized in the units of time specified. |
| `-r` `start_time` \[`#` `stop_time`\] | Specifies the start and stop time to display information. The format for the time period is `yyyy-nn-ddThh:mm:ss`.     `yyyy` - year   `nn` - month (01..12)   `dd` - day (01..31)   `hh` - hour (00..23)   `mm` - minute (00..59)   `ss` - second (00..59)    For example:  `-r` `2010-05-05T08:30:00#2010-05-05T15:30:00` |
| `-s` | Displays statistical information. This option is valid only when run on the primary file system. It is important that the primary and standby nodes are running a network time service to ensure that the statistics are meaningful. |
| `-t` | Displays only transport records from the replication event log. |
| `-v` | Displays verbose output. |
| `mount_point` | Specifies the directory where the file system is mounted. |

To display information about replication configuration, use `acfsutil` `repl` `info` with the `-c` option. To display information about replication statistics, use `acfsutil` `repl` `info` with the `-s` option. To display information about replication events, use `acfsutil` `repl` `info` with the `-a`, `-e`, or `-t` options.

You must have system administrator or Oracle ASM administrator privileges to run this command.

Examples

Example 13-26 shows the use of the `acfsutil` `repl` `info` command.

Example 13-26 Using the acfsutil repl info command

```
$ /sbin/acfsutil repl info -c /u01/app/acfsmounts/myacfs

$ /sbin/acfsutil repl info -s -n 5d /u01/app/acfsmounts/myacfs

$ /sbin/acfsutil repl info -a -v /u01/app/acfsmounts/myacfs
```

## acfsutil repl init

Purpose

Initiates replication on all the files in an Oracle ACFS file system or only those files with a specified list of tags.

Syntax and Description

  
`acfsutil` `repl` `init` `-h`  
  
`acfsutil` `repl` `init` `primary` `-s` `standby_connect_string` \[`tagname`...\]  
 \[`-m` `standby_mount_point`\] \[`-c` `primary_service`\]  
 \[`-d` `trace_level`\] \[`-z` { `on` | `off` }\] `mount_point`  
  
`acfsutil` `repl` `init` `standby` `-p` `primary_connect_string`  
 \[`-c` `standby_service`\] \[`-d` `trace_level`\] `mount_point`  

`acfsutil` `repl` `init` `-h` displays help text and exits.

Table 13-33 contains the options available with the `acfsutil` `repl` `init` command.

Table 13-33 Options for the acfsutil repl init command

| Option | Description |
| --- | --- |
| `primary` | Specifies replication of the primary file system. |
| `standby` | Specifies replication of the standby file system. |
| `-s` `standby_conncect_string` | Specifies the connection string for the site hosting the standby file system. The user in the connection string must have `SYSASM` and `SYSDBA` privileges. |
| `-p` `primary_conncect_string` | Specifies the connection string for the site hosting the primary file system. The user in the connection string must have `SYSASM` and `SYSDBA` privileges. |
| `tagname` | Specifies the tag names of the files to be replicated. |
| `-m` `standby_mount_point` | Specifies the directory where the standby file system is mounted if it is different than the primary file system. This is valid only for the primary file system initialization. |
| `-c` `primary_service` | Specifies the service name for the primary file system. Required if the primary file system is using a different service name than the standby file system. |
| `-c` `standby_service` | Specifies the service name for the standby file system. Required if the standby file system is using a different service name than the primary file system. |
| `-d` `trace_level` | Specifies the trace level setting (0..6) for replication logs. |
| \- `z` `on` \| `off` | Turn on or off compression on replication logs. Compression is off by default. |
| `mount_point` | Specifies the directory where the file system is mounted. For `repl` `init` `primary`, `mount_point` specifies the primary file system. For `repl` `init` `standby`, `mount_point` specifies the standby file system. |

When the `acfsutil` `repl` `init` `primary` command completes successfully, processing begins to replicate initial copies of all specified files to the standby file system. In addition, any changes to these files and any new files subsequently created in the file system on the primary file system are captured and transported to the standby file system. However, successful completion of the command does not indicate that the specified files have been copied in full to the standby file system. To monitor the progress of the initial replication of all specified files to the standby file system, users run the `acfsutil` `repl` `info` `-c` command.

The first phase of the initial replication copy process begins with a complete copy of the file system directory tree structure, not the files within the directory tree, to the standby file system. During this time, attempts to rename directories may fail. After the directory tree structure has been successfully copied to the standby file system, replication initialization begins the second phase of the initial copy process: copying all files to be replicated to the standby file system. While a file is being copied to the standby file system during this initial replication phase, writes and truncates to that file are blocked.

Symbolic link files are replicated as is. If the symbolic link resolves to an absolute path name, and that path name does not exist on the standby file system, then referencing the symbolic link results in errors.

A new service name must be created for replication. You cannot use the `+ASM` service name. You must specify a unique service name for each file system that you want to replicate when there are multiple replicated file systems on a node or cluster.

A file system being replicated can only be mounted on one path for the primary or standby file system. Otherwise, dismounting any one of the paths on a node where it is mounted on multiple paths stops the replication background threads.

A replicated Oracle ACFS file system must be mounted on the same directory within a cluster. The file system does not have to be mounted on all of the nodes in a cluster, but if it is mounted, it must be mounted on the directory specified with the `acfsutil` `repl` `init` command. In addition, no other file system can be mounted on that directory on other nodes.

A single Oracle ACFS file system cannot be configured both as a primary and a standby file system. If replication is configured on the same host or within the same cluster, then the primary and standby file systems cannot use the same named mount point.

The primary file system must have a minimum size of 4 GB for each node that is mounting the file system. The standby file system must have a minimum size of 4 GB and should be sized appropriately for the amount of data being replicated and the space necessary for the replication logs sent from the primary file system.

The sites hosting the primary and standby file systems must be running the same operating system and must have the same machine architecture.

Oracle wallets can also be used to manage security credentials.

See Also:

- [Oracle Database Advanced Security Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e40393/asowalet.htm#ASOAG160) for information about Oracle wallets
- [Oracle Database SecureFiles and Large Objects Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e18294/adlob_hierarch.htm#ADLOB46075) for information about wallet management
- [Oracle Database Net Services Reference](https://docs.oracle.com/cd/E11882_01/network.112/e10835/sqlnet.htm#NETRF182) for information about wallet parameters in the `SQLNET.ORA` file

You must have system administrator privileges to run this command.

Examples

Example 13-27 shows the use of the `acfsutil` `repl` `init` command.

Example 13-27 Using the acfsutil repl init command

```
$ /sbin/acfsutil repl init primary 
     -s standby_admin/standby_passwd@standby_repl_site
     -m /standby/repl_data -c primary_repl_service 
     /acfsmounts/repl_data

$ /sbin/acfsutil repl init standby 
    -p primary_admin/primary_passwd@primary_repl_site
    -c standby_repl_service /standby/repl_data
```

## acfsutil repl pause

Purpose

Pauses replication on an Oracle ACFS file system.

Syntax and Description

  
`acfsutil` `repl` `pause` `-h`  
`acfsutil` `repl` `pause` `mount_point`  

`acfsutil` `repl` `pause` `-h` displays help text and exits.

Table 13-34 contains the options available with the `acfsutil` `repl` `pause` command.

Table 13-34 Options for the acfsutil repl pause command

| Option | Description |
| --- | --- |
| `mount_point` | Specifies the directory where the file system is mounted. |

The `acfsutil` `repl` `pause` command temporarily stops the replication process until the `acfsutil` `repl` `resume` command is run. The command can be run at either the site hosting the primary or a standby file system. `acfsutil` `repl` `resume` should be run soon after `acfsutil` `repl` `pause` to resume replication.

The `acfsutil` `repl` `pause` command can be used to temporarily stop the transportation of replication logs from the primary file system to the standby file system, but logs continue to be generated on the primary file system. Note that logs are not deleted until they are transported to the standby file system and applied to the standby file system.

The `acfsutil` `repl` `pause` command can also be used to temporarily stop the application of replication logs to a standby file system, but the command does not stop the transportation of logs to the standby file system. Note that logs are not deleted from the standby file system until they are applied to the file system.

When replication is paused on either the site hosting the primary or standby file system, replication logs still accumulate on the standby and primary file system. These logs can consume all available storage space in the file system so you must check available storage on the sites hosting the file systems if you have paused replication. Ensure that you run `acfsutil` `repl` `resume` before the accumulated replication logs consume all available space in the file system.

You must have system administrator or Oracle ASM administrator privileges to run this command.

Examples

Example 13-28 shows the use of the `acfsutil` `repl` `pause` command.

Example 13-28 Using the acfsutil repl pause command

```
$ /sbin/acfsutil repl pause /u01/app/acfsmounts/myacfs
```

## acfsutil repl resume

Purpose

Resumes replication on an Oracle ACFS file system where replication has been paused.

Syntax and Description

  
`acfsutil` `repl` `resume` `-h`  
`acfsutil` `repl` `resume` `mount_point`  

`acfsutil` `repl` `resume` `-h` displays help text and exits.

Table 13-35 contains the options available with the `acfsutil` `repl` `resume` command.

Table 13-35 Options for the acfsutil repl resume command

| Option | Description |
| --- | --- |
| `mount_point` | Specifies the directory where the file system is mounted. |

This command resumes the replication process after the `acfsutil` `repl` `pause` command has been run. This command should be run soon after replication has been paused with the `acfsutil` `repl` `pause` command.

You must have system administrator or Oracle ASM administrator privileges to run this command.

Examples

Example 13-29 shows the use of the `acfsutil` `repl` `resume` command.

Example 13-29 Using the acfsutil repl resume command

```
$ /sbin/acfsutil repl resume /u01/app/acfsmounts/myacfs
```

## acfsutil repl sync

Purpose

Synchronizes primary and standby file systems.

Syntax and Description

  
`acfsutil` `repl` `sync` `-h`  
`acfsutil` `repl` `sync` \[`apply`\] `mount_point`  

`acfsutil` `repl` `sync` `-h` displays help text and exits.

Table 13-36 contains the options available with the `acfsutil` `repl` `sync` command.

Table 13-36 Options for the acfsutil repl sync command

| Option | Description |
| --- | --- |
| `apply` | Specifies that all changes be applied to the standby file system. |
| `mount_point` | Specifies the directory where the primary file system is mounted. |

The `acfsutil` `repl` `sync` command can be used to synchronize the state of the primary and standby file system. This command can only be run on the site hosting the primary file system.

You should first quiesce your applications and run a sync(1) call so that the synchronized state is known and meaningful to you. The `acfsutil` `repl` `sync` command then causes all outstanding replication data to be shipped from the primary to the standby file system.

The `acfsutil` `repl` `sync` command returns success when this transfer is complete or, if the `apply` parameter is supplied, when all of these changes have been successfully applied to the standby file system. At this point, unless an unmount of the last node on the primary site cluster is about to occur, applications can be restarted. `acfsutil` `repl` `sync` can be used before dismounting the file system on the last node to ensure that all modifications have been sent to the standby file system.

If `acfsutil` `repl` `info` `-c` reports the primary file system is in the `Initializing` state, the `acfsutil` `repl` `sync` command does not guarantee that all files to be replicated in the file system have been sent to the standby file system. Files that existed in the file system before running the `acfsutil` `repl` `init` command are sent to the standby file system in the background.

You must have system administrator or Oracle ASM administrator privileges to run this command.

Examples

Example 13-30 shows the use of the `acfsutil` `repl` `sync` command.

Example 13-30 Using the acfsutil repl sync command

```
$ /sbin/acfsutil repl sync /u01/app/acfsmounts/myacfs
```

## acfsutil repl terminate

Purpose

Stops all replication activity on the Oracle ACFS file system at the site where it is run.

Syntax and Description

  
`acfsutil` `repl` `terminate` `-h`  
`acfsutil` `repl` `terminate` `primary` `mount_point`  
`acfsutil` `repl` `terminate` `standby` \[`immediate`\] `mount_point`  

`acfsutil` `repl` `terminate` `-h` displays help text and exits.

Table 13-37 contains the options available with the `acfsutil` `repl` `terminate` command.

Table 13-37 Options for the acfsutil repl terminate command

| Option | Description |
| --- | --- |
| `primary` | Stops replication on the primary file system. |
| `standby` | Stops replication on the standby file system. |
| `immediate` | Stops replication processing immediately on the standby file system. |
| `mount_point` | Specifies the directory where the file system is mounted. |

The `acfsutil` `repl` `terminate` command stops all replication processing. When terminating replication, you should terminate replication for the primary file system first, and then the standby file system. If you want to ensure all changes are sent to the standby file system before terminating the primary site, ensure that all applications are quiesced and run the `acfsutil` `repl` `sync` command. The terminate command must be run on both sites if both sites hosting the file systems are available.

After `acfsutil` `repl` `terminate` `standby` has been run, you can use the standby file system in read-write mode. After `acfsutil` `repl` `terminate` has been run on either the primary file system or standby file system, you must start replication from the beginning with the `acfsutil` `repl` `init` command.

The `repl` `terminate` `standby` command waits until replication data at the standby file system has been applied. If you want to terminate replication immediately without applying all the replication data, use the `immediate` option. However, this option can leave some files at the standby file system in an indeterminate state.

To momentarily stop Oracle ACFS replication, you can use the `acfsutil` `repl` `pause` command, followed soon after by the `acfsutil` `repl` `resume` command.

You must have system administrator privileges to run this command.

Examples

Example 13-31 shows the use of the `acfsutil` `repl` `terminate` command.

Example 13-31 Using the acfsutil repl terminate command

```
$ /sbin/acfsutil repl terminate /u01/app/acfsmounts/myacfs
```

## acfsutil repl trace

Purpose

Sets the replication trace level for gathering trace information on an Oracle ACFS file system.

Syntax and Description

  
`acfsutil` `repl` `trace` `-h`  
`acfsutil` `repl` `trace` `level` `mount_point`  

`acfsutil` `repl` `trace` `-h` displays help text and exits.

Table 13-39 contains the options available with the `acfsutil` `repl` `trace` command.

Table 13-38 Options for the acfsutil repl trace command

| Option | Description |
| --- | --- |
| `level` | Specifies the trace level setting (0..6). The default level is 2. |
| `mount_point` | Specifies the directory where the file system is mounted. |

Increasing the trace level can have a performance impact and should be done at the recommendation of Oracle support services.

Trace files for Oracle ACFS replication are stored in the following locations:

```
GRID_HOME/log/host_name/acfsrepl*
GRID_HOME/log/host_name/client/acfsutil.log
```

You must have system administrator or Oracle ASM administrator privileges to run this command.

Examples

Example 13-32 shows the use of the `acfsutil` `repl` `trace` command.

Example 13-32 Using the acfsutil repl trace command

```
$ /sbin/acfsutil repl trace 5 /u01/app/acfsmounts/myacfs
```

## acfsutil repl update

Purpose

Updates replication information while replication is running on an Oracle ACFS file system.

Syntax and Description

  
`acfsutil` `repl` `update` `-h`  
`acfsutil` `repl` `update`  
 \[`-p` `primary_connect_string` \] \[`-s` `standby_connect_string`\] \[`-z` { `on` | `off` }\]  
 `mount_point`  

`acfsutil` `repl` `update` `-h` displays help text and exits.

Table 13-39 contains the options available with the `acfsutil` `repl` `update` command.

Table 13-39 Options for the acfsutil repl update command

| Option | Description |
| --- | --- |
| `-p` `primary_connect_string` | Specifies the connection string for the primary file system. The user in the connection string must have `SYSASM` and `SYSDBA` privileges. |
| `-s` `standby_connect_string` | Specifies the connection string for the standby file system. The user in the connection string must have `SYSASM` and `SYSDBA` privileges. |
| \- `z` `on` \| `off` | Turn on or off compression on replication logs. Compression is off by default. |
| `mount_point` | Specifies the directory where the file system is mounted. |

The `acfsutil` `repl` `update` command updates replication information after replication has been started. This command can only be run on the site hosting the primary file system. The connection strings for the primary and standby file systems can be altered.

You can specify any combination of the `-p`, `-s`, and `-z` options, but you must specify at least one of the options.

While replication is running, compression can be turned on or off with the `-z` option.

You must have system administrator privileges to run this command.

Examples

Example 13-33 shows the use of the `acfsutil` `repl` `update` command.

Example 13-33 Using the acfsutil repl update command

```
$ /sbin/acfsutil repl update -s mystandby@oracle.com /u01/app/acfsmounts/myacfs
```