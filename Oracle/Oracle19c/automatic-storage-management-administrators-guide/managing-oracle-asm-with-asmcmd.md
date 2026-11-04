---
title: "Oracle Automatic Storage Management Administrator's Guide"
book: "Oracle Automatic Storage Management Administrator's Guide"
doc_id: F34287-08
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/ostmg/part-ii-oracle-asm-instances-and-disk-groups/managing-oracle-asm-with-asmcmd.html
tags:
  - oracle
  - 19c
  - automatic-storage-management-administrators-guide
---

## Managing Oracle ASM with ASMCMD

Oracle Automatic Storage Management (Oracle ASM) Command-Line Utility (ASMCMD) provides commands for managing Oracle ASM.

Note:

Oracle does not recommend using identifiers for Oracle Database object names that must be quoted. While the use of quoted identifiers may be valid as names in some command-line tools or in SQL statements, such as `CREATE` `DISKGROUP` " `1DATA` ", the names may not be valid when using other tools that manage the object. For more information about naming Oracle Database objects, refer to [*Oracle Database SQL Language Reference*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19&id=SQLRF-GUID-75337742-67FD-4EC0-985F-741C93D918DA).

## About ASMCMD

ASMCMD is a command-line utility that you can use to manage Oracle ASM instances, disk groups, file access control for disk groups, files and directories within disk groups, templates for disk groups, and volumes.

You can run the ASMCMD utility in either interactive or noninteractive mode.

### Types of ASMCMD Commands

The types of ASMCMD commands are listed in the table.

Table: Types of ASMCMD commands

| Category | Commands |
| --- | --- |
| Oracle ASM instance management | For a list of commands, refer to ASMCMD Instance Management Commands |
| Oracle ASM client cluster | For a list of commands, refer to ASMCMD Member Cluster Management Commands |
| Oracle ASM file management | For a list of commands, refer to ASMCMD File Management Commands |
| Oracle ASM disk group management | For a list of commands, refer to ASMCMD Disk Group Management Commands |
| Oracle ASM file group management | For a list of commands, refer to ASMCMD File Group Management Commands |
| Oracle ASM template management | For a list of commands, refer to ASMCMD Template Management Commands |
| Oracle ASM file access control | For a list of commands, refer to ASMCMD File Access Control Commands |

### About Oracle ASM Files, File Names, Directories, and Aliases

ASMCMD works with Oracle ASM files, directories, and aliases. Before using ASMCMD, you should understand how these common computing concepts apply to the Oracle ASM environment.

#### System-Generated File Name or Fully Qualified File Name

Every file created in Oracle ASM gets a system-generated file name, otherwise known as a fully qualified file name. This is similar to a complete path name in a local file system.

Oracle ASM generates file names according to the following scheme:

```
+diskGroupName/databaseName/fileType/fileTypeTag.fileNumber.incarnation
```

An example of a fully qualified file name is the following:

`+data/orcl/CONTROLFILE/Current.256.541956473`

In the previous fully qualified file name, `data` is the disk group name, `orcl` is the database name, `CONTROLFILE` is the file type, and so on.

Only the slash (/) is supported by ASMCMD. File Names are not case sensitive, but are case retentive. If you type a path name as lowercase, ASMCMD retains the lowercase.

For more information about Oracle ASM file names, refer to [Fully Qualified File Name Form](administering-oracle-asm-files-directories-and-templates.md).

#### Directory

As in other file systems, an Oracle ASM directory is a container for files, and an Oracle ASM directory can be part of a tree structure of other directories. The fully qualified file name represents a hierarchy of directories in which the plus sign (+) represents the root directory. In each disk group, Oracle ASM automatically creates a directory hierarchy that corresponds to the structure of the fully qualified file names in the disk group. The directories in this hierarchy are known as system-generated directories.

ASMCMD enables you to move up and down in this directory hierarchy with the `cd` (change directory) command. The ASMCMD `ls` (list directory) command lists the contents of the current directory, while the `pwd` command prints the name of the current directory.

When you start ASMCMD, the current directory is set to root (+). For an Oracle ASM instance with two disk groups, for example, `data` and `fra`, entering an `ls` command with the root directory as the current directory produces the following output:

```
ASMCMD> ls
data/
fra/
```

The following example demonstrates navigating the Oracle ASM directory tree (refer to the fully qualified file name shown previously):

```
ASMCMD> cd +data/orcl/CONTROLFILE
ASMCMD> ls
Current.256.541956473
Current.257.541956475
```

You can create your own directories as subdirectories of the system-generated directories using the ASMCMD `mkdir` command. The directories that you create can have subdirectories, and you can navigate the hierarchy of both system-generated directories and user-created directories with the `cd` command.

The following example creates the directory `mydir` under `orcl` in the disk group `data`:

`ASMCMD> mkdir +data/orcl/mydir`

Note:

The directory `orcl` is a system-generated directory. The contents of `data` represent the contents of disk group `data`.

If you start ASMCMD with the `-p` flag, then ASMCMD shows the current directory as part of its prompt. See Including the Current Directory in the ASMCMD Prompt.

```
ASMCMD [+] > cd data/orcl
ASMCMD [+data/orcl] >
```

ASMCMD retains the case of the directory that you entered.

#### Alias

Aliases are file names that are references or pointers to system-generated file names. However, aliases are user-friendly names. Aliases are similar to symbolic links in UNIX or Linux computers. You can create aliases to simplify Oracle ASM file name administration. You can create aliases with the `mkalias` ASMCMD command or a SQL `ALTER` `DISKGROUP` command.

An alias has at a minimum the disk group name as part of its complete path. You can create aliases at the disk group level or in any system-generated or user-created subdirectory. The following are examples of aliases:

```
+data/ctl1.f
+data/orcl/ctl1.f
+data/mydir/ctl1.f
```

If you run the ASMCMD `ls` (list directory) with the `-l` flag, each alias is listed with the system-generated file to which the alias refers.

`ctl1.f => +data/orcl/CONTROLFILE/Current.256.541956473`

For more information about aliases, refer to [Alias Oracle ASM File Name Forms](administering-oracle-asm-files-directories-and-templates.md).

#### Absolute Path and Relative Path

When you run an ASMCMD command that accepts a file name or directory name as an argument, you can use the name as either an absolute path or a relative path.

An absolute path refers to the full path of a file or directory. An absolute path begins with a plus sign (+) followed by a disk group name, followed by subsequent directories in the directory tree. The absolute path includes directories until the file or directory of interest is reached. A complete system-generated file name, otherwise known as the fully qualified file name, is an example of an absolute path to a file.

Using an absolute path enables the command to access the file or directory regardless of where the current directory is set. The following `rm` command uses an absolute path for the file name:

`ASMCMD [+] > rm` `+data/orcl/datafile/users.259.555341963`

The following `cd` command uses an absolute path to the directory.

`ASMCMD [+data/mydir] > cd +data/orcl/CONTROLFILE`

A relative path includes only the part of the file name or directory name that is not part of the current directory. That is, the path to the file or directory is relative to the current directory.

In the following example, the `rm` command operates on the file `undotbs1.272.557429239`, which in this case is a relative path. ASMCMD appends the current directory to the command argument to obtain the absolute path to the file. In this example this is `+data/orcl/DATAFILE/undotbs1.272.557429239`.

```
ASMCMD [+] > cd +data
ASMCMD [+data] > cd orcl/DATAFILE
ASMCMD [+data/orcl/DATAFILE] > ls
EXAMPLE.269.555342243
SYSAUX.257.555341961
SYSTEM.256.555341961
UNDOTBS1.258.555341963
UNDOTBS1.272.557429239
USERS.259.555341963
ASMCMD [+data/orcl/DATAFILE] >
 rm undotbs1.272.557429239
```

Paths to directories can also be relative. You can go up or down the hierarchy of the current directory tree branch by providing a directory argument to the `cd` command whose path is relative to the current directory.

In addition, you can use the pseudo-directories "`.`" and "`..`" rather than a directory name. The "`.`" pseudo-directory is the current directory. The "`..`" pseudo-directory is the parent directory of the current directory.

The following example demonstrates how to use relative directory paths and pseudo-directories:

```
ASMCMD [+data/orcl] > cd DATAFILE
ASMCMD [+data/orcl/DATAFILE] >cd ..
ASMCMD [+data/orcl] >
```

#### Wildcard Characters

The wildcard characters `*` and `%` match zero or more characters anywhere within an absolute or relative path, which saves typing of the full directory or file name. The two wildcard characters behave identically. There are various ASMCMD commands that accept wildcards, such as `cd`, `du`, `find`, `ls`, `lsattr`, `lsdg`, `lsdsk`, `lsgrp`, `lsusr`, and `rm`.

If a wildcard pattern matches only one directory when using wildcard characters with `cd`, then `cd` changes the directory to that destination. If the wildcard pattern matches multiple directories, then ASMCMD does not change the directory but instead returns an error.

If you are running ASMCMD commands in noninteractive mode, then with most operating systems you must enclose the wildcard characters in quotes. For more information, refer to Running ASMCMD in Noninteractive Mode.

Example: Using wildcards with ASMCMD commands

```
ASMCMD [+] > cd +data/orcl/*FILE
ASMCMD-08005: +data/orcl/*FILE: ambiguous

ASMCMD [+] > cd +data/orcl/C*
ASMCMD [+data/orcl/CONTROLFILE] >

ASMCMD [+] > ls +fra/orcl/A%
2009_07_13/
2009_07_14/

ASMCMD [+] >  ls +fra/orcl/ARCHIVELOG/2009%

+fra/orcl/ARCHIVELOG/2009_07_13/:
thread_1_seq_3.260.692103543
thread_1_seq_4.261.692108897
thread_1_seq_5.262.692125993
thread_1_seq_6.263.692140729
thread_1_seq_7.264.692143333

+fra/orcl/ARCHIVELOG/2009_07_14/:
thread_1_seq_8.271.692158265
thread_1_seq_9.272.692174597

ASMCMD [+] > ls data/orcl/*

+data/orcl/CONTROLFILE/:
Current.260.692103157

+data/orcl/DATAFILE/:
EXAMPLE.265.692103187
SYSAUX.257.692103045
SYSTEM.256.692103045
UNDOTBS1.258.692103045
USERS.259.692103045

+data/orcl/ONLINELOG/:
group_1.261.692103161
group_2.262.692103165
group_3.263.692103169

+data/orcl/PARAMETERFILE/:
spfile.266.692103315

+data/orcl/TEMPFILE/:
TEMP.264.692103181
spfileorcl.ora
```

### Preparing to Run ASMCMD

You should review the information in this topic before running the ASMCMD utility.

You can run the ASMCMD utility in either interactive or noninteractive mode. Before running ASMCMD, review the items in the following list.

- Log in to the host which contains the Oracle ASM instance that you plan to administer.
	You must log in as a user that has SYSASM or SYSDBA privileges through operating system authentication. The SYSASM privilege is the required connection to administer the Oracle ASM instance.
- To connect to the Oracle ASM instance, run ASMCMD that is located in the `bin` subdirectory of the Oracle Grid Infrastructure home (Oracle ASM home).
	Connect as SYSASM, the default connection, to administer an Oracle ASM instance.
	Ensure that the `ORACLE_HOME` and `ORACLE_SID` environment variables to refer to the Oracle ASM instance. Depending on your operating system, you might have to set other environment variables to properly connect to the Oracle ASM instance.
	Ensure that the `bin` subdirectory of your Oracle Grid Infrastructure home is in your `PATH` environment variable.
	The default value of the Oracle ASM SID for a single-instance database is `+ASM`. In Oracle Real Application Clusters environments, the default value of the Oracle ASM SID on any node is `+ASM` *node#*.
- To use most of the ASMCMD commands, ensure that the Oracle ASM instance is started and the Oracle ASM disk groups are mounted.
	If the Oracle ASM instance is not running, ASMCMD runs only those commands that do not require an Oracle ASM instance. The commands include `startup`, `shutdown`, `lsdsk`, `help`, and `exit`. If you attempt to run other ASMCMD commands, an error message displays.
- You can connect to the database instance as SYSDBA by running ASMCMD that is located in the `bin` directory of the Oracle Database home.
	Ensure that the `ORACLE_HOME` and `ORACLE_SID` environment variables to refer to the database instance. Depending on your operating system, you might have to set other environment variables to properly connect to the database instance.
	You must include the `--privilege` option to connect as SYSDBA.
	With this connection, there is a limited set of operations that can be run.
	When administering disk groups, Oracle recommends that you run ASMCMD from the database home of the database instance that is the owner of the files in the disk group.

See also

- [Authentication for Accessing Oracle ASM Instances](administering-oracle-asm-instances.md) for more information about authentication for accessing Oracle ASM instances
- Specifying the Type of Connection for more information about specifying connection options
- [The SYSDBA Privilege for Managing Oracle ASM Components](administering-oracle-asm-instances.md) for more information about permissions and connections
- [Oracle Database Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19&id=ADMIN-GUID-7842AF72-DA25-4559-A8E7-9883D0C63BF2) for more information about setting environment variables
- [Oracle Database Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19&id=ADMIN-GUID-C1656511-35F7-4517-8A43-574A5B60136C) for information about operating system authentication

### Running ASMCMD in Interactive Mode

The interactive mode of the ASMCMD utility provides a shell-like environment where you are prompted to enter ASMCMD commands.

#### Syntax for Starting ASMCMD

The syntax for starting ASMCMD in interactive mode is:

```
asmcmd [-V]
asmcmd [--nocp] [-v {errors|warnings|normal|info|debug}]
  [--privilege connection_type ] [-p]
  [--inst instance_name] [--discover]
```

Table: ASMCMD interactive options

| Option | Description |
| --- | --- |
| \- `V` | Displays the version of ASMCMD and then exits. |
| `--nocp` | Disables connection pooling. For information about connection pooling, refer to [*Oracle Database Administrator's Guide*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19&id=ADMIN-GUID-9B3A136E-D275-417B-B6F4-59A45D42655F). |
| `-v` `display_level` | Displays additional information with some commands to help users diagnose problems and writes to a message file when logging is required. `normal` is the default if the display level is not specified. |
| `--privilege` `connection_type` | Specifies the privilege to connect as when accessing an Oracle ASM or database instance. Can be either `SYSASM` or `SYSDBA`. The default is `SYSASM` and is used when administering the Oracle ASM instance. |
| `-p` | Displays the current directory in the prompt. |
| `--inst` `instance_name` | Specifies to connect to a specific Oracle ASM instance. |
| `--discover` | Uses the discovery string obtained from listener, not from the `ORACLE_SID` environmental variable. |

The `ORACLE_HOME` and `ORACLE_SID` environment variables determine the instance to which ASMCMD connects. ASMCMD establishes a bequeath connection in the same manner as `SQLPLUS` `/` `AS` `SYSASM` which requires the user to be a member of the `OSASM` group.

When Oracle Flex ASM is enabled, ASMCMD connects to any one of the Oracle ASM instances running in the cluster. The connection to the Oracle ASM instance does not depend on the `ORACLE_HOME` and `ORACLE_SID` environment variables. The ASMCMD alert log shows which instance ASMCMD is connected to. If you want to connect to a specific Oracle ASM instance, then use the `--inst` option.

ASMCMD can be started with multiple options. For example:

```
asmcmd -p -v info
```

For the majority of the examples in this chapter, ASMCMD was started with the `-p` option.

#### Running ASMCMD without Any Options

To run ASMCMD in interactive mode without any options:

1. Enter the following at the operating system command prompt:
	`asmcmd`
	Oracle displays an ASMCMD command prompt as follows:
	`ASMCMD>`
2. Enter an ASMCMD command and press `Enter`. The command runs and displays its output, if any, and then ASMCMD prompts for the next command.
3. Continue entering ASMCMD commands until you have completed the tasks.
4. Enter the `exit` or `quit` command to exit ASMCMD.

#### Specifying the Type of Connection

You can specify the `--privilege` option to choose the type of connection, either `SYSASM` or `SYSDBA`. The default value is `SYSASM` and is used when administering an Oracle ASM instance. Connect as `SYSDBA` when connecting to the database instance.

For example:

`$ asmcmd --privilege sysasm`

#### Specifying the Verbose Mode

You can specify the `-v` option with the `asmcmd` command to display additional information with some commands to help users diagnose problems as shown in the following example:

```
$ asmcmd -v debug
```

When there is a message that must be logged during `asmcmd` operations, the message is written to the `alert.log` file or the `trace.trc` file.

The `alert.log` file is created or updated when `asmcmd` is started with the `-v` `errors`, `-v` `warnings`, or `-v` `normal` display level. The `trace.trc` file is created or updated when `asmcmd` is started with the `-v` `info` or `-v` `debug` display level.

By default, the `alert.log` is file created in the `$ORACLE_BASE/diag/asmcmd/user_` *username* `/` *hostname* `/alert/` directory. By default, the `trace.trc` file is created in the `$ORACLE_BASE/diag/asmcmd/user_` *username* `/` *hostname* `/trace/` directory.

Under certain circumstances, `$ORACLE_BASE` and `$ORACLE_HOME` can be set to override the default locations of the `alert.log` and `trace.trc` files.

#### Including the Current Directory in the ASMCMD Prompt

You can specify the `-p` option with the `asmcmd` command to include the current directory in the ASMCMD prompt as shown in the following example:

```
$ asmcmd -p
ASMCMD [+] > cd data
ASMCMD [+data] >
```

#### Displaying the ASMCMD Version Number

You can specify the `-V` option when starting `asmcmd` to display the `asmcmd` version number. After displaying the version number, `asmcmd` immediately exits.

For example:

```
$ asmcmd -V
  asmcmd version 19.0.0.0.0
```

### Running ASMCMD in Noninteractive Mode

In noninteractive mode, you run a single ASMCMD command by including the command and command options on the command line when invoking ASMCMD. ASMCMD runs the command, generates output if any, and then exits. The noninteractive mode is especially useful for running scripts.

On most operating systems, wildcard characters must be enclosed in quotes when running ASMCMD commands in noninteractive mode.

To run ASMCMD in noninteractive mode where *command* is any valid ASMCMD command and *options* is a list of command options, at the command prompt enter the following:

`asmcmd` *command* *options*

In noninteractive mode, ASMCMD returns the codes listed in the following table.

Table: ASMCMD return codes

| Type | Return Code | Description |
| --- | --- | --- |
| General | 0 | No issues for the command. |
| General | 1 | Internal error. |
| General | 255 or -1 | External user error as returned by a command. |
| `lsdsk` | 0 | Results include member disks only. |
| `lsdsk` | 1 | Results include candidate disks only. |
| `lsdsk` | 2 | Results include both member and candidate disks. |

The following example shows how to run ASMCMD in the noninteractive mode. The first command runs the `ls` command to list the disk groups for the Oracle ASM instance. The second command redirects the output of the `lsod` command to the `my_lsod_test` file. The third command runs `lsdsk` using a pattern with a wildcard character to list specific disks in the `data` disk group. Note that wildcard characters must be enclosed in quotes when running ASMCMD in noninteractive mode on most operating systems.

Example: Running ASMCMD commands in noninteractive mode

```
$ asmcmd ls -l
State    Type    Rebal  Name
MOUNTED  NORMAL  N      DATA/
MOUNTED  NORMAL  N      FRA/

$ asmcmd lsod --suppressheader -G data > my_lsod_test

$ asmcmd lsdsk -G data '/devices/diska*'
Path
/devices/diska1
/devices/diska2
/devices/diska3
```

Example: Displaying a return code when running ASMCMD in noninteractive mode

```
$ asmcmd ls -l dat
ASMCMD-08001: diskgroup 'dat' does not exist or is not mounted

$ echo $?
255
```

Example: Running ASMCMD commands in a script

```
#!/bin/sh
for ((i = 1; i <=3; i++))
 do
   asmcmd lsdsk -G data '/devices/diska'$i
done

$ ./asmcmd_test_script
Path
/devices/diska1
Path
/devices/diska2
Path
/devices/diska3
```

### Getting Help

Type `help` at the ASMCMD prompt or as a command in noninteractive mode to view general information about ASMCMD and a list of available ASMCMD commands.

You can type `help` *command* to display help text for a specific command, including usage information about how to run the command with its options.

The following is an example of the use of the `help` command.

Example: Displaying ASMCMD help text

```
ASMCMD [+] > help startup
        startup [--nomount] [--restrict] [--pfile <pfile.ora>]

        Start the ASM instance.

        [--nomount]           specifies the nomount option.
        [--restrict]          start the instance in restricted mode.
        [--pfile <pfile.ora>] specifies the location of the pfile.
```

## ASMCMD Instance Management Commands

This topic provides a summary of the ASMCMD instance management commands.

Some commands in this section affect the Grid Plug and Play (GPnP) profile, which is a resource in a clustered configuration. In an Oracle Restart configuration, the profile is actually located in a resource attribute, not the Grid Plug and Play (GPnP) profile. However, the functionality of the commands is the same for both configurations.

Note:

After a change has been made to the location of the password file, the following SQL statement should be executed to flush the password file metadata cache.  
`SQL> ALTER SYSTEM FLUSH PASSWORDFILE_METADATA_CACHE`

The location of the password file can be changed by running `orapwd`, or the ASMCMD `pwcopy`, `pwcreate`, `pwdelete`, `pwmove`, or `pwset` command.

See also

[Oracle Grid Infrastructure Installation and Upgrade Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/ostmg&id=CWGEN) for your operating system for information about installing and configuring Oracle Grid Infrastructure

The following table lists the Oracle ASM instance management commands with brief descriptions.

Table: Summary of ASMCMD instance management commands

| Command | Description |
| --- | --- |
| dsget | Retrieves the discovery diskstring value that is used by the Oracle ASM instance and its clients. |
| dsset | Sets the disk discovery diskstring value that is used by the Oracle ASM instance and its clients. |
| lsct | Lists information about current Oracle ASM clients. |
| lsop | Lists the current operations on a disk group or Oracle ASM instance. |
| lspwusr | Lists the users from an Oracle ASM password file. |
| orapwusr | Adds, drops, or changes an Oracle ASM password user. |
| pwcopy | Copies a password file to the specified location. |
| pwcreate | Creates a password file at the specified location. |
| pwdelete | Deletes a password file at the specified location. |
| pwget | Returns the location of the password file. |
| pwmove | Moves the location of the password file. |
| pwset | Sets the location of the password file. |
| showclustermode | Displays the current mode of the Oracle ASM cluster. |
| showclusterstate | Displays the current state of the cluster. |
| showpatches | Lists the patches applied to the Oracle Grid Infrastructure home. |
| showversion | Displays the Oracle ASM cluster release and software patch levels. |
| shutdown | Shuts down an instance. |
| spbackup | Backs up an Oracle ASM SPFILE. |
| spcopy | Copies an Oracle ASM SPFILE. |
| spget | Retrieves the location of the Oracle ASM SPFILE. |
| spmove | Moves an Oracle ASM SPFILE. |
| spset | Sets the location of the Oracle ASM SPFILE. |
| startup | Starts up an instance. |

### dsget

Purpose

Retrieves the discovery diskstring value that is used by the Oracle ASM instance and its clients.

Syntax and Description

```
dsget [ --normal | --parameter | --profile [-f] ]
```

The syntax options for the `dsget` command are described in the following table.

Table: Options for the dsget command

| Option | Description |
| --- | --- |
| `--normal` | Retrieves the discovery string from the Grid Plug and Play (GPnP) profile and the one that is set in the Oracle ASM instance. It returns one row each for the profile and parameter setting. This is the default setting. |
| `--parameter` | Retrieves the `ASM_DISKSTRING` parameter setting of the Oracle ASM instance. |
| `--profile` \[ `-f` \] | Retrieves the discovery string from the GPnP profile. If `-f` is specified with `--profile`, `dsget` retrieves the discovery string from the local GPnP profile. |

Example

The following example uses `dsget` to retrieve the current discovery diskstring value from the GPnP profile and the `ASM_DISKSTRING` parameter.

Example: Using the ASMCMD dsget command

```
ASMCMD [+] > dsget
profile: /devices1/disk*
parameter: /devices2/disk*
```

### dsset

Purpose

Sets the discovery diskstring value that is used by the Oracle ASM instance and its clients.

The specified diskstring must be valid for existing mounted disk groups. The updated value takes effect immediately.

Syntax and Description

```
dsset [ --normal | --parameter | --profile [-f] ] diskstring
```

The syntax options for the `dsset` command are described in the following table.

Table: Options for the dsset command

| Option | Description |
| --- | --- |
| `--normal` | Sets the discovery string in the Grid Plug and Play (GPnP) profile and in the Oracle ASM instance. The update occurs after the Oracle ASM instance has successfully validated that the specified discovery string has discovered all the necessary disk groups and voting files. This command fails if the instance is not using a server parameter file (SPFILE).  This is the default setting. |
| `--parameter` | Specifies that the diskstring is updated in memory after validating that the discovery diskstring discovers all the current mounted disk groups and voting files. The diskstring is not persistently recorded in either the SPFILE or the GPnP profile. |
| `--profile` \[ `-f` \] | Specifies the discovery diskstring that is pushed to the GPnP profile without any validation by the Oracle ASM instance, ensuring that the instance can discover all the required disk groups. The update is guaranteed to be propagated to all the nodes that are part of the cluster.  If `-f` is specified with `--profile`, the specified diskstring is pushed to the local GPnP profile without any synchronization with other nodes in the cluster. This command option updates only the local profile file. This option should only be used for recovery. The command fails if the Oracle Clusterware stack is running. |
| `diskstring` | Specifies the value for the discovery diskstring. |

For information about disk discovery and the discovery diskstring, see [Oracle ASM Disk Discovery](administering-oracle-asm-disk-groups.md).

Example

The following example uses `dsset` to set the current value of the discovery diskstring in the GPnP profile.

Example: Using the ASMCMD dsset command

```
ASMCMD [+] > dsset /devices1/disk*,/devices2/disk*
```

### lsct

Purpose

Lists information about current Oracle ASM clients from the `V$ASM_CLIENT` view. A client, such as Oracle Database or Oracle ASM Dynamic Volume Manager (Oracle ADVM), uses disk groups that are managed by the Oracle ASM instance to which ASMCMD is currently connected.

Syntax and Description

```
lsct [--suppressheader] [-g] disk_group
```

The following table lists the options for the `lsct` command.

Table: Options for the lsct command

| Option | Description |
| --- | --- |
| `-g` | Selects from the `GV$ASM_CLIENT` view. `GV$ASM_CLIENT.INST_ID` is included in the output. |
| `--suppressheader` | Suppresses column headings. |
| `disk_group` | Specifies the disk group. |

Client information is only listed for the specified disk group.

Example

The following example displays information about the clients that are accessing the `data` disk group.

Example: Using the ASMCMD lsct command

```
ASMCMD [+] > lsct data
DB_Name  Status    Software_Version  Compatible_version  Instance_Name  Disk_Group
+ASM     CONNECTED       19.0.0.0.0          19.0.0.0.0  +ASM           DATA
asmvol   CONNECTED       19.0.0.0.0          19.0.0.0.0  +ASM           DATA
orcl     CONNECTED       19.0.0.0.0          19.0.0.0.0  orcl           DATA
```

### lsop

Purpose

Lists the current operations on a disk group in an Oracle ASM instance.

Syntax and Description

```
lsop
```

`lsop` displays information from the `V$ASM_OPERATION` view.

Example

The following are examples of the `lsop` command. The examples list operations on the disk groups of the current Oracle ASM instance.

Example: Using the ASMCMD lsop command

```
ASMCMD [+] > lsop
Group_Name  Dsk_Num  State  Power
DATA        REBAL    WAIT   2

ASMCMD [+] > lsop
Group_Name  Dsk_Num  State  Power
FRA         REBAL    REAP   3
```

### lspwusr

Purpose

List the users from the local Oracle ASM password file.

Syntax and Description

```
lspwusr [--suppressheader]
```

The following table lists the options for the `lspwusr` command.

Table: Options for the lspwusr command

| Option | Description |
| --- | --- |
| `--suppressheader` | Suppresses column headers from the output. |

Examples

The following is an example of the `lspwusr` example. The example lists the current users in the local Oracle ASM password file.

Example: Using the ASMCMD lspwusr command

```
ASMCMD [+] > lspwusr
Username sysdba sysoper sysasm
     SYS   TRUE    TRUE   TRUE
 ASMSNMP   TRUE   FALSE  FALSE
```

### orapwusr

Purpose

Add, drop, or modify an Oracle ASM password file user.

Syntax and Description

```
orapwusr { --add | --modify | --delete | grant {sysasm|sysdba|sysoper} |
  --revoke {sysasm|sysdba|sysoper} } user
```

The following table lists the options for the `orapwusr` command.

Table: Options for the orapwusr command

| Option | Description |
| --- | --- |
| `--add` | Adds a user to the password file. Also prompts for a password. |
| `--modify` | Changes the password for the specified user. |
| `--delete` | Drops a user from the password file. |
| `--grant` `role` | Sets the role for the user. The options are `sysasm`, `sysdba`, and `sysoper`. |
| `--revoke` `role` | Removes the role for the user. The options are `sysasm`, `sysdba`, and `sysoper`. |
| `user` | Name of the user to add, drop, or modify. |

`orapwusr` attempts to update passwords on all nodes in a cluster. This command requires the SYSASM privilege to run. A user logged in as SYSDBA cannot change its password using this command.

Examples

The following is an example of the `orapwusr` command. This example adds the `hruser` to the Oracle ASM password file.

Example: Using the ASMCMD orapwusr command

```
ASMCMD [+] > orapwusr --add hruser
```

### pwcopy

Purpose

Copies an Oracle ASM or database instance password file to the specified location.

Syntax and Description

```
pwcopy [--asm |--dbuniquename string] source  destination [-f]
```

Table: Options for the pwcopy command

| Option | Description |
| --- | --- |
| `--asm` | The `--asm` option associates the password file with the Oracle ASM instance that ASMCMD is logged into. |
| `--dbuniquename` `string` | The `--dbuniquename` `string` option identifies the database unique name associated with the password file. |
| `source` | The `source` value identifies the location where the existing password file is located. |
| `destination` | The `destination` value identifies the location where you want to copy the password file. |
| `-f` | The `-f` option enables the password file to be copied without any checks. |

`pwcopy` copies a password file from one disk group to another, from the operating system to a disk group, or from a disk group to the operating system. If the `-f` option is specified, then the password file can be copied to the same disk group.

Either `--asm` or - `-dbuniquename` is required to identify a CRSD resource. When either `--asm` or - `-dbuniquename` is included in the `pwcopy` command, the target file is set to the current password file.

The `compatible.asm` disk group attribute must be set to `12.1` or higher for the disk group where the password is to be copied.

The `SYSASM` or `SYSDBA` privilege is required to manage the Oracle ASM and database password files.

Example

The following example copies an Oracle ASM password file in one disk group to a different disk group. Because the `pwcopy` command includes the `--asm` option, the target file (`+fra/orapwasm_new`) is set to the current password file.

Example: Using the ASMCMD pwcopy command

```
ASMCMD [+] > pwcopy --asm +DATA/orapwasm +FRA/orapwasm_new
copying +DATA/orapwasm -> +FRA/orapwasm_new
```

### pwcreate

Purpose

Creates an Oracle ASM or Oracle Database instance password file at the specified location.

Note:

Do not use `pwcreate` to create a new Oracle ASM password file when Oracle ASM is configured in a cluster. If the Oracle ASM password file is inaccessible in a cluster configuration, you must restore the password file using an available backup rather than create a new file. For articles about recreating a shared Oracle ASM password file in a cluster, such as document 1929673.1, refer to articles at [My Oracle Support](https://support.oracle.com/) ([https://support.oracle.com](https://support.oracle.com/)).

Syntax and Description

```
pwcreate { --asm  |--dbuniquename string } [-f] [--format format] file_path [sys_password]
```

Table: Options for the pwcreate command

| Option | Description |
| --- | --- |
| `--asm` | Associates the password file with the Oracle ASM instance that ASMCMD is logged into. |
| `--dbuniquename` `string` | Specifies the Oracle Database unique name associated with the password file. |
| `-f` | Forces a deletion of the existing password file and creates a new password file. |
| `--format` `format` | Specifies the format in which the password is created. Values are `12` and `12.2`. If not specified, then `12.2` is the default value. |
| `file_path` | Specifies the location where the password file is created. |
| `sys_password` | Specifies the initial `SYS` password. If this option is omitted, then the you are prompted for the password. |

`pwcreate` creates a password file in the disk group specified by *file\_path*. The initial `SYS` password is specified by *sys\_password*.

Either `--asm` or - `-dbuniquename` is required. The `compatible.asm` disk group attribute must be set to `12.1` or higher for the disk group where the password is to be located.

The `SYSASM` or `SYSDBA` privilege is required to manage the Oracle ASM and database password files.

For additional information, refer to [Managing a Shared Password File in a Disk Group](administering-oracle-asm-instances.md).

Example

The following example creates an Oracle Database password file in an Oracle ASM disk group.

Example: Using the ASMCMD pwcreate command

```
ASMCMD [+] > pwcreate --dbuniquename orcl '+data/ORCL/orapwdb'
Enter password for SYS:
```

### pwdelete

Purpose

Deletes an Oracle ASM or database instance password file.

Syntax and Description

```
pwdelete { --asm |--dbuniquename string | file_path }
```

Table: Options for the pwdelete command

| Option | Description |
| --- | --- |
| `--asm` | The `--asm` option associates the password file with the Oracle ASM instance that ASMCMD is logged into. |
| `--dbuniquename` `string` | The `--dbuniquename` `string` option identifies the database unique name associated with the password file. |
| `file_path` | The `file_path` value identifies the location where the password file is located. |

`pwdelete` deletes the specified password file. Either `--asm` or - `-dbuniquename` is required to identify a CRSD resource and to remove the password location from the CRSD resource.

The `SYSASM` or `SYSDBA` privilege is required to manage the Oracle ASM and database password files.

Example

The following example deletes the specified password file from a disk group.

Example: Using the ASMCMD pwdelete command

```
ASMCMD [+] > pwdelete +FRA/orapwasm_bak
```

### pwget

Purpose

Returns the location of the password file for the Oracle ASM or database instance.

Syntax and Description

```
pwget { --asm | --dbuniquename string }
```

Table: Options for the pwget command

| Option | Description |
| --- | --- |
| `--asm` | The `--asm` option associates the password file with the Oracle ASM instance that ASMCMD is logged into. |
| `--dbuniquename` `string` | The `--dbuniquename` `string` option identifies the database unique name associated with the password file. |

`pwget` returns the location of the password file for the Oracle ASM instance identified by `--asm` or the database instance identified by - `-dbuniquename`.

The `SYSASM` or `SYSDBA` privilege is required to manage the Oracle ASM and database password files.

Example

The following example returns the location of the Oracle ASM password file.

Example: Using the ASMCMD pwget command

```
ASMCMD [+] > pwget --asm
+DATA/orapwasm
```

### pwmove

Purpose

Moves an Oracle ASM or database instance password file to the specified location.

Syntax and Description

```
pwmove { --asm | --dbuniquename string } source  destination [-f]
```

Table: Options for the pwmove command

| Option | Description |
| --- | --- |
| `--asm` | The `--asm` option associates the password file with the Oracle ASM instance that ASMCMD is logged into. |
| `--dbuniquename` `string` | The `--dbuniquename` `string` option identifies the database unique name associated with the password file. |
| `source` | The `source` value identifies the location where the existing password file is located. |
| `destination` | The `destination` value identifies the location where you want to move the password file. |
| `-f` | The `-f` option clears the password file for any associated resource and the new file is registered. |

`pwmove` moves a password file from one disk group to another, from the operating system to a disk group, or from a disk group to the operating system. If the `-f` option is specified, then a password file can be moved to a file in the same disk group.

Either `--asm` or - `-dbuniquename` is required to identify a CRSD resource.

The `compatible.asm` disk group attribute must be set to `12.1` or higher for the disk group where the password is to be moved.

The `SYSASM` or `SYSDBA` privilege is required to manage the Oracle ASM and database password files.

Example

The following example moves a password file from one disk group to another disk group.

Example: Using the ASMCMD pwmove command

```
ASMCMD [+] > pwmove --asm +FRA/orapwasm_bak +DATA/orapwasm
moving +FRA/orapwasm_bak -> +DATA/orapwasm
```

### pwset

Purpose

Sets the location of the password file for an Oracle ASM or database instance.

Syntax and Description

```
pwset { --asm  | --dbuniquename string } file_path
```

Table: Options for the pwset command

| Option | Description |
| --- | --- |
| `--asm` | The `--asm` option associates the password file with the Oracle ASM instance that ASMCMD is logged into. |
| `--dbuniquename` `string` | The `--dbuniquename` `string` option identifies the database unique name associated with the password file. |
| `file_path` | The `file_path` value identifies the location where the password file is located. |

`pwset` sets the location of the password file for an Oracle ASM or database instance to the value specified by *file\_path*. Either - `-dbuniquename` or `--asm` is required to identify a CRSD resource.

The `SYSASM` or `SYSDBA` privilege is required to manage the Oracle ASM and database password files.

Example

The following example sets the location of the Oracle ASM password file in a disk group.

Example: Using the ASMCMD pwset command

```
ASMCMD [+] > pwset --asm +DATA/orapwasm
```

### showclustermode

Purpose

Displays the current mode of the Oracle ASM cluster.

Syntax and Description

```
showclustermode
```

`showclustermode` displays the mode that the Oracle ASM cluster is currently in. The possible return values are **ASM cluster: Flex mode enabled** or **ASM cluster: Flex mode disabled**.

Example

The following example shows the use of the `showclustermode` command.

Example: Using the ASMCMD showclustermode command

```
ASMCMD [+] > showclustermode
ASM cluster : Flex mode disabled
```

### showclusterstate

Purpose

Displays the current state of the cluster.

Syntax and Description

```
showclusterstate
```

`showclusterstate` displays the state that the Oracle ASM cluster is currently in. The possible values returned are **Normal**, **In Rolling Patch**, or **In Rolling Upgrade** mode.

Example

This example shows the use of the `showclusterstate` command.

Example: Using the ASMCMD showclusterstate command

```
ASMCMD [+] > showclusterstate
```

### showpatches

Purpose

Lists the patches applied on the Oracle Grid Infrastructure home.

Syntax and Description

```
showpatches [-l]
```

The following table lists the options for the `showpatches` command.

Table: Options for the showpathches command

| Option | Description |
| --- | --- |
| `-l` | Displays all details about the patches. |

`showpatches` lists the patches that have been applied to the Oracle Grid Infrastructure home.

Example

This example shows the use of the `showpatches` command.

Example: Using the ASMCMD showpatches command

```
ASMCMD [+] > showpatches -l
Oracle ASM release patch level is [0] and no patches have been applied on the local node. The release patch string is [18.1.0.0.0].
```

### showversion

Purpose

Displays the patch levels of the Oracle ASM cluster release and software.

Syntax and Description

```
showversion [[[--releasepatch] [--softwarepatch]] | [--active]]
```

The following table lists the options for the `showversion` command.

Table: Options for the showversion command

| Option | Description |
| --- | --- |
| `--releasepatch` | Displays the cluster level patch version.  Use `asmcmd` `showversion` `--active` instead. |
| `--softwarepatch` | Displays the patch level on the local node.  Use `asmcmd` `showpatches` `-l` instead. |
| `--active` | Displays the active version and active patch level |

`showversion` displays the Oracle ASM cluster release and software patch levels. The release and software patch options may differ depending whether the Oracle ASM or Oracle Grid Infrastructure home is being patched.

Note:

The `releasepatch` and `softwarepatch` options may be different when the Oracle Grid Infrastructure or Oracle ASM home is being patched. When in normal mode, the options should be same. When there is no Oracle ASM instance connected, release patch information is not displayed.

Example

This example shows the use of the `showversion` command.

Example: Using the ASMCMD showversion command

```
ASMCMD [+] > showversion --active
Oracle ASM active version on the cluster is [19.0.0.0.0]. The cluster upgrade state is [NORMAL]. The cluster active patch level is [0].
```

### shutdown

Purpose

Shuts down an instance.

Syntax and Description

```
shutdown [--target target_instance] [--normal | --abort|--immediate ]
```

Table: Options for the shutdown command

| Option | Description |
| --- | --- |
| `--target` `target_instance` | Specify the target instance. The value of `target_instance` could be either Oracle ASM ( `ASM` ), IOServer ( `IOS` ), or Oracle ASM proxy ( `APX` ) instance. |
| `--normal` | Shut down normal. This is the default action. |
| `--abort` | Shut down stopping all existing operations. |
| `--immediate` | Shut down immediately. |

The default target instance is determined by the `ORACLE_SID` environmental variable. The default action is a normal shutdown.

Oracle strongly recommends that you shut down all database instances that use the Oracle ASM instance and dismount all file systems mounted on Oracle ASM Dynamic Volume Manager (Oracle ADVM) volumes before attempting to shut down the Oracle ASM instance with the `--abort` option.

For more information about shutting down an Oracle ASM instance, see " [About Shutting Down an Oracle ASM Instance](administering-oracle-asm-instances.md) ".

Example

The following are examples of the `shutdown` command. The first example performs a shut down of the Oracle ASM instance with normal action. The second example performs a shut down with immediate action. The third example performs a shut down that stops all existing operations.

Example: Using the ASMCMD shutdown command

```
ASMCMD [+] > shutdown --target ASM --normal

ASMCMD [+] > shutdown --target ASM --immediate

ASMCMD [+] > shutdown --target ASM --abort
```

### spbackup

Purpose

Backs up an Oracle ASM SPFILE to a backup file.

Syntax and Description

```
spbackup source destination
```

This table lists the options for the `spbackup` command.

Table: Options for the spbackup command

| Option | Description |
| --- | --- |
| `source` | Specifies the source file name. |
| `destination` | Specifies the destination file. |

`spbackup` should be used when you want to make single or multiple backups of an SPFILE in the same or a different disk group without creating an SPFILE in the target disk group.

Note the following about the use of `spbackup`:

- `spbackup` can back up an Oracle ASM SPFILE from a disk group to a disk group or to an operating system file.
- `spbackup` can back up an Oracle ASM SPFILE from an operating system file to a disk group.
- `spbackup` can back up an Oracle ASM SPFILE when the SPFILE is being used by an open Oracle ASM instance.
- `spbackup` can make multiple backups of an Oracle ASM SPFILE in the same disk group.

`spbackup` does not affect the GPnP profile. The backup file that is created is not a special file type and is not identified as an SPFILE. This backup file cannot be copied with `spcopy`. To copy this backup file to and from a disk group, use the ASMCMD `cp` command.

To make a copy of a backup file in a disk group that is identified as an SPFILE file:

1. Use the ASMCMD `cp` command to copy the backup file from the disk group to an operating system file. See " cp ".
2. Use the ASMCMD spcopy command to copy the operating system file to a disk group. See " spcopy ".

Example

The following are examples of the `spbackup` command. The first example backs up the SPFILE in the `data` disk group. The second example backs up the SPFILE from the `data` disk group to the `fra` disk group.

Example: Using the ASMCMD spbackup command

```
ASMCMD> spbackup  +DATA/asm/asmparameterfile/registry.253.721810181
                  +DATA/spfileBackASM.bak

ASMCMD> spbackup  +DATA/asm/asmparameterfile/registry.253.721810181
                  +FRA/spfileBackASM.bak
```

### spcopy

Purpose

Copies an Oracle ASM SPFILE from the source location to an SPFILE in the destination location.

Syntax and Description

```
spcopy [-u] source destination
```

This table lists the options for the `spcopy` command.

Table: Options for the spcopy command

| Option | Description |
| --- | --- |
| `-u` | Updates the Grid Plug and Play (GPnP) profile. |
| `source` | Specifies the source file name. |
| `destination` | Specifies the destination. |

Note the following about the use of `spcopy`:

- `spcopy` can copy an Oracle ASM SPFILE from a disk group to a different disk group or to an operating system file.
- `spcopy` can copy an Oracle ASM SPFILE from an operating system file to a disk group.
- `spcopy` can copy an Oracle ASM SPFILE when the SPFILE is being used by an open Oracle ASM instance.
- `spcopy` cannot make multiple copies of an Oracle ASM SPFILE in the same disk group. You can use `spbackup` for that purpose.

To update the GPnP profile, include the `-u` option with `spcopy`. You can also use `spset` to update the GPnP profile if `spcopy` is run without the `-u` option.

After copying the SPFILE and updating the GPnP profile, you must restart the instance with the SPFILE in the new location to use that SPFILE. When the Oracle ASM instance is running with the SPFILE in the new location, you can remove the source SPFILE.

To copy an Oracle ASM SPFILE into a disk group using `spcopy`, the `COMPATIBLE.ASM` attribute must be set to `11.2` or greater in the target disk group.

Example

The following are examples of the `spcopy` command. The first example copies the Oracle ASM SPFILE from the `data` disk group to the `fra` disk group. The second example copies the Oracle ASM SPFILE from the `data` disk group to an operating system location. The third example copies an Oracle ASM SPFILE from an operating system location to the `data` disk group and updates the GPnP profile with the `-u` option.

Example: Using the ASMCMD spcopy command

```
ASMCMD> spcopy  +DATA/asm/asmparameterfile/registry.253.721810181
                +FRA/spfileCopyASM.ora

ASMCMD> spcopy +DATA/asm/asmparameterfile/registry.253.721810181
                $ORACLE_HOME/dbs/spfileCopyASM.ora

ASMCMD> spcopy -u /oracle/product/11.2.0/grid/dbs/spfileTestASM.ora
                  +DATA/ASM/spfileCopyASM.ora
```

See also

- spset for information about using the ASMCMD `spset` command
- [About Backing Up, Copying, and Moving an Oracle ASM Initialization Parameter File](administering-oracle-asm-instances.md) for information about copying and moving an Oracle ASM instance initialization parameter file after upgrading
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19&id=SQLRF-GUID-D3E295B7-A3A4-43D3-8BBD-5CBE171A2E52) for information about creating a server parameter file with the `CREATE SPFILE` SQL statement

### spget

Purpose

Retrieves the location of the Oracle ASM SPFILE from the Grid Plug and Play (GPnP) profile.

Syntax and Description

```
spget
```

The location retrieved by `spget` is the location in the GPnP profile, but not always the location of the SPFILE currently used. For example, the location could have been recently updated by `spset` or `spcopy` with the `-u` option on an Oracle ASM instance that has not been restarted. After the next restart of the Oracle ASM, this location points to the Oracle ASM SPFILE currently being used.

Example

The following is an example of the `spget` command that retrieves and displays the location of the SPFILE from the GPnP profile.

Example: Using the ASMCMD spget command

```
ASMCMD [+] > spget
+DATA/ASM/ASMPARAMETERFILE/registry.253.813507611
```

### spmove

Purpose

Moves an Oracle ASM SPFILE from source to destination and automatically updates the GPnP profile.

Syntax and Description

```
spmove source destination
```

This table lists the options for the `spmove` command.

Table: Options for the spmove command

| Option | Description |
| --- | --- |
| `source` | Specifies the source file. |
| `destination` | Specifies the destination file. |

Note the following about the use of `spmove`:

- `spmove` can move an Oracle ASM SPFILE when the open instance is using a PFILE or a different SPFILE. After moving the SPFILE, you must restart the instance with the SPFILE in the new location to use that SPFILE.
- `spmove` cannot move an Oracle ASM SPFILE when the SPFILE is being used by an open Oracle ASM instance.

For information about copying and moving an Oracle ASM instance initialization parameter file after upgrading, see " [About Backing Up, Copying, and Moving an Oracle ASM Initialization Parameter File](administering-oracle-asm-instances.md) ".

To use `spmove` to move an Oracle ASM SPFILE into a disk group, the disk group attribute `COMPATIBLE.ASM` must be set to `11.2` or greater.

Example

The following are examples of the `spmove` command. The first example moves an Oracle ASM SPFILE from the `data` disk group to an operating system location. The second example moves an SPFILE from an operating system location to the `data` disk group.

Example: Using the ASMCMD spmove command

```
ASMCMD> spmove +DATA/spfileASM.ora
               /oracle/product/11.2.0/grid/dbs/spfileMoveASM.ora

ASMCMD> spmove /oracle/product/11.2.0/grid/dbs/spfile+ASM.ora
               +DATA/ASM/spfileMoveASM.ora
```

### spset

Purpose

Sets the location of the Oracle ASM SPFILE in the Grid Plug and Play (GPnP) profile.

Syntax and Description

```
spset location
```

This table lists the options for the `spset` command.

Table: Options for the spset command

| Option | Description |
| --- | --- |
| `location` | Specifies the location of the Oracle ASM SPFILE. The location is the full path to the SPFILE. |

Example

The following is an example of the `spset` command that sets the location of the Oracle ASM SPFILE command in the `data` disk group.

Example: Using the ASMCMD spset command

```
ASMCMD> spset +DATA/asm/asmparameterfile/asmspfile.ora
```

### startup

Purpose

Starts up the default instance.

Syntax and Description

```
startup [--mount] [--nomount] [--restrict] [ --pfile pfile ]
```

This table lists the options for the `startup` command.

Table: Options for the startup command

| Option | Description |
| --- | --- |
| `--mount` | Specifies a mount operation. This is the default action. |
| `--nomount` | Specifies no mount operation. |
| `--restrict` | Specifies restricted mode. |
| `--pfile` `pfile` | Oracle ASM initialization parameter file. |

This command starts up an instance specified by the `ORACLE_SID` environmental variable. The variable could be set to the Oracle ASM, IOServer, or APX proxy instance.

The default action for an Oracle ASM instance is a startup that mounts disk groups and enables Oracle ASM Dynamic Volume Manager (Oracle ADVM) volumes.

Example

The following is an example of the `startup` command that starts the Oracle ASM instance (`ORACLE_SID=+ASM`) without mounting disk groups and uses the `asm_init.ora` initialization parameter file.

Example: Using the ASMCMD startup command

```
ASMCMD> startup --nomount --pfile asm_init.ora
```

See also

- [About Mounting Disk Groups at Startup](administering-oracle-asm-instances.md) for information about disk groups that are mounted at startup time
- [About Starting Up an Oracle ASM Instance](administering-oracle-asm-instances.md) for more information about starting up an Oracle ASM instance

## ASMCMD Member Cluster Management Commands

This topic provides a summary of the ASMCMD member cluster management commands that are used with Oracle ASM remote instances.

Unless otherwise specified, the ASMCMD cluster management commands should be executed in the Oracle ASM-CSS cluster.

For information about Oracle Flex ASM, refer to " [Managing Oracle Flex ASM](managing-oracle-flex-asm.md) ".

This table lists the ASMCMD member cluster management commands with brief descriptions.

Table: Summary of ASMCMD member cluster management commands

| Command | Description |
| --- | --- |
| chcc | Modifies a configuration for a member cluster. |
| mkcc | Creates a configuration for a member cluster. |
| lscc | Lists the configured member clusters. |
| rmcc | Removes the configuration for a member cluster. |

See also

- [Oracle Grid Infrastructure Installation and Upgrade Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/ostmg&id=CWGEN) for information about installing clusters and cluster name requirements
- [Oracle Clusterware Administration and Deployment Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19&id=CWADD-GUID-6BA197F8-44D4-4663-8191-1CB24EF5F117) for information about member clusters

### chcc

Purpose

Modifies the configuration for a member cluster.

Syntax and Description

```
chcc cluster_name [--direct | --indirect]
  [--version member_cluster_version]
```

The following table lists the options for the `chcc` command.

Table: Options for the chcc command

| Option | Description |
| --- | --- |
| `cluster_name` | Specifies the name of the member cluster. |
| `--direct` | Specifies direct storage access. |
| `--indirect` | Specifies indirect storage access. |
| `--version` `member_cluster_version` | Specifies the five digit member cluster version if it is different than the storage server version. The storage server version is used if not specified. |

To modify the storage access method of a member cluster, you perform the following steps.

1. As the Oracle Grid Infrastructure user at the Domain Services Cluster (DSC), change the member cluster storage access configuration with the `chcc` command.
2. As the Oracle Grid Infrastructure user at the Domain Services Cluster (DSC), export the member cluster configuration into a new cluster manifest file with the `mkcc` command.
	You can ignore the warning messages reported when the `mkcc` command is issued.
3. After you have exported the new cluster manifest file, as the root user on the nodes of member cluster you copy the new cluster manifest file to the nodes with the `rootcrs.sh` script.

Examples

The following examples show how to modify the storage access method from direct to indirect Oracle ASM storage for the member cluster `--asm` and `--gimr` components.

Example: Using the ASMCMD chcc command

As the Oracle Grid Infrastructure user at the Domain Services Cluster (DSC), run the following commands:

```
$ asmcmd chcc memberCluster1 --indirect

$ asmcmd mkcc memberCluster1 /export/cluster_manifest_new.xml --asm --gimr
```

As the root user at the member cluster, copy the new cluster manifest file to the member cluster with the following commands.

1. Run the `rootcrs.sh` script on every node in the member cluster.
	```
	# rootcrs.sh --convertcluster STORAGE_ACCESS -manifestfile cluster_manifest_new.xml
	```
2. Run the `rootcrs.sh` script with the `-lastnode` option on last node in the member cluster.
	```
	# rootcrs.sh --convertcluster STORAGE_ACCESS -manifestfile cluster_manifest_new.xml -lastnode
	```

### lscc

Purpose

Lists the configured member clusters.

Syntax and Description

```
lscc [--suppressheader] [-l] [cluster_name | --file wrap]
```

The following table lists the options for the `lscc` command.

Table: Options for the lscc command

| Option | Description |
| --- | --- |
| `-suppressheader` | Suppresses column headings from the output. |
| `-l` | Displays all details. |
| `cluster_name` | Specifies the name of the member cluster. |
| `--file` | Displays information about the contents of the cluster manifest file. |
| `wrap` | Specifies the full path of the XML file to export the credentials. |

Examples

The following example lists the configured member clusters.

Example: Using the ASMCMD lscc command

```
ASMCMD [+] > lscc
--------------------------------------------------------------------------------
           NAME        VERSION GUID
================================================================================
 memberCluster1     12.2.0.0.0 78015b1e78756f88bf119fd8e5146df4
 memberCluster2     12.2.0.0.0 3de3bbd75e9a7f17bfe027b477b5bcae
================================================================================

ASMCMD [+] > lscc -l
--------------------------------------------------------------------------------
           NAME        VERSION GUID                             ASM GIMR TFA ACFS RHP
=====================================================================================
 memberCluster1     12.2.0.0.0 78015b1e78756f88bf119fd8e5146df4 YES  YES YES  YES YES
 memberCluster2     12.2.0.0.0 3de3bbd75e9a7f17bfe027b477b5bcae YES  YES YES  YES  NO
=====================================================================================

ASMCMD [+] > lscc memberCluster1 --suppressheader
 memberCluster1     12.2.0.0.0 78015b1e78756f88bf119fd8e5146df4

ASMCMD [+] > lscc memberCluster1 --suppressheader -l
 memberCluster1     12.2.0.0.0 78015b1e78756f88bf119fd8e5146df4 ASM,GIMR,TFA,ACFS,RHP
```

### mkcc

Purpose

Creates the configuration for a member cluster.

Syntax and Description

```
mkcc cluster_name manifest_file [--direct]
  [--version member_cluster_version]
  [--guid member_cluster_guid]
  [--gimr gimr_pdb/export_dir]
  [--asm] [--gimr] [--rhp] [--acfs] [--tfa]
```

The following table lists the options for the `mkcc` command.

Table: Options for the mkcc command

| Option | Description |
| --- | --- |
| `cluster_name` | Specifies the name of the member cluster. |
| `manifest_file` | Specifies the full path of the XML file to export the credentials. |
| `--direct` | Specifies direct storage access. If not specified, the storage access is indirect. |
| `--version` `member_cluster_version` | Specifies the five digit member cluster version if it is different than the storage server version. The storage server version is used if not specified. |
| `--guid` `member_cluster_guid` | Specifies the 32-character, globally unique identifier for the member cluster. When this option is specified, `mkcc` does not generate a new GUID. If there is a cluster already configured with the specified GUID, then the command fails. |
| `--gimr` `gimr_pdb/export_dir` | Specifies the directory from which to import the GIMR PDB when converting a standalone cluster to a member cluster. |
| `--asm` | Generate credentials and configuration for an Oracle ASM member cluster. |
| `--gimr` | Generate credentials and configuration for an Oracle GIMR member cluster. |
| `--rhp` | Generate credentials and configuration for an Oracle RHP member cluster. |
| `--acfs` | Generate credentials and configuration for an Oracle ACFS member cluster. |
| `--tfa` | Generate credentials and configuration for an Oracle TFA member cluster. |

The member cluster name must conform to the same rules as a cluster name. The name must be unique across your enterprise, must be at least one character long and no more than 15 characters in length, must be alphanumeric, cannot begin with a numeral, and may contain hyphens (-). Underscore characters (\_) are not allowed.

If no member cluster component options are specified, the default is to configure all of the components and store their credentials in the same manifest file.

GNS credentials are not generated by the `asmcmd` `mkcc` command. To configure the member cluster as a GNS Client, run the following command as a privileged user to export the GNS instance client data configuration to the cluster manifest file:

```
srvctl export gns -clientdata manifest_file -role CLIENT
```

Examples

The following example creates credentials for the member cluster `--asm` and `--gimr` components and exports the credentials to a cluster manifest file.

Example: Using the ASMCMD mkcc command

```
ASMCMD [+] > mkcc memberCluster1 /tmp/member_cluster1.xml --version 12.2.0.0.0 --asm --gimr
```

### rmcc

Purpose

Removes the configuration for a member cluster.

Syntax and Description

```
rmcc cluster_name [-f]
```

The following table lists the options for the `rmcc` command.

Table: Options for the rmcc command

| Option | Description |
| --- | --- |
| `cluster_name` | Specifies the name of the member cluster. |
| `-f` | Specifies to force the removal of member cluster credentials. |

Examples

The following example removes the configuration for a member cluster.

Example: Using the ASMCMD rmcc command

```
ASMCMD [+] > rmcc memberCluster1
```

## ASMCMD Oracle ASM Filter Driver Management Commands

This topic provides a summary of the ASMCMD Oracle ASM filter driver (Oracle ASMFD) management commands.

See also

[*Oracle Grid Infrastructure Installation Guide*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/ostmg&id=CWGEN) for your operating system for information about installing and configuring Oracle Grid Infrastructure

This table lists the Oracle ASM Filter Driver management commands with brief descriptions.

Table: Summary of ASMCMD Oracle ASM Filter Driver management commands

| Command | Description |
| --- | --- |
| afd\_configure | Configures Oracle ASM Filter Driver. |
| afd\_deconfigure | Deconfigures Oracle ASM Filter Driver. |
| afd\_di | Manipulates the data integrity state in the Oracle ASM Filter Driver. |
| afd\_dsget | Retrieves the Oracle ASM Filter Driver diskstring value. |
| afd\_dsset | Sets the Oracle ASM Filter Driver diskstring value. |
| afd\_filter | Sets the Oracle ASM Filter Driver mode on a given disk path. |
| afd\_label | Sets an Oracle ASM Filter Driver label to a disk. |
| afd\_lsdsk | Lists Oracle ASM Filter Driver disks. |
| afd\_lslbl | Lists the disks that contain Oracle ASM Filter Driver labels. |
| afd\_refresh | Refreshes Oracle ASM Filter Driver disks using the AFD discovery string. |
| afd\_scan | Scans for Oracle ASM Filter Driver disks. |
| afd\_state | Returns the state of Oracle ASM Filter Driver. |
| afd\_unlabel | Clears an existing Oracle ASM Filter Driver label. |

### afd\_configure

Purpose

Configures Oracle ASM Filter Driver.

Syntax and Description

```
# asmcmd afd_configure  [-d

| -e] [-f]
```

The following table lists the options for the `afd_configure` command.

Table: Options for the afd\_configure command

| Option | Description |
| --- | --- |
| `-d` | Disables Oracle ASMFD filtering mode. |
| `-e` | Enables Oracle ASMFD filtering mode. |
| `-f` | Force Oracle ASMFD configuration. |

The `afd_configure` command must be run noninteractively as a `root` user. Before running the command on a node, the Oracle Clusterware stack must be shut down on that node. After the `afd_configure` command has been run, restart Oracle Clusterware on each node. After running `afd_configure`, the default filtering state is enabled.

Example

The following example configures Oracle ASM Filter Driver on the node on which the command was run. `$ORACLE_HOME` in the example refers to the Oracle Grid Infrastructure home.

Example: Using the afd\_configure command

```
# $ORACLE_HOME/bin/asmcmd afd_configure
```

See also

- [Administering Oracle ASM Filter Driver](administering-oracle-asm-filter-driver.md) for information about Oracle ASM Filter Driver
- [Oracle Grid Infrastructure Installation and Upgrade Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/ostmg&id=CWGEN) for your operating system for information about installing and configuring Oracle Grid Infrastructure

## ASMCMD Audit Files Management Commands

This document describes the ASMCMD Oracle ASM audit files management commands.

The following table provides a summary of ASMCMD audit files management commands.

Table: Summary of ASMCMD audit files management commands

| Command | Description |
| --- | --- |
| audcleanaudittrail | Deletes the audit files of the specified audit trail type. |
| audclearproperty | Clears the value for the specified audit property. |
| audcleartimestamp | Clears the last archive timestamp set by " `audsettimestamp` " command. |
| audcreatejob | Creates a purge job for specified audit trail type. |
| auddropjob | Drops the specified audit purge job. |
| audsetdebug | Sets the tracing to the specified debug level. |
| audsetjobinterval | Sets the job interval for the specified audit purge job. |
| audsetjobstatus | Sets the status of the specified purge job to either " `enable` " or " `disable` " state. |
| audsetproperty | Sets the value of specified audit property for given audit trail type. |
| audsettimestamp | Sets the last archive timestamp for specified audit trail type. |
| audshowtimestamp | Displays the last archive timestamps set by " `audsettimestamp` " command. |
| lsaudcleanupjobs | Displays the configured audit trail purge jobs. |
| lsaudconfigparams | Displays the configured audit trail properties for the given audit trail type. |

### audcleanaudittrail

Purpose

Deletes the audit files of the specified audit trail type. The command will delete the files based on Last Archive Timestamp set using " `audsettimestamp` " command, if `--useTimestamp` option is specified. Else, it will delete all the files that are not being actively written to.

Syntax and Description

```
audcleanaudittrail {--os|--uni} [--useTimestamp]
```

Options for the `audcleanaudittrail` command

Table: Options for the audcleanaudittrail command

| Option | Description |
| --- | --- |
| `--os` | Cleans up audit files of OS audit trail type. |
| `--uni` | Cleans up audit files of Unified audit trail type. |
| `--useTimestamp` | If specified, uses last archive timestamp in cleaning up the audit records. |

Examples

The following are examples of `audcleanaudittrail` command.

In the example below, the audit files of OS audit trail type that are older than the timestamp specified by " `audsettimestamp` " command will be deleted.

Example: Using the ASMCMD audcleanaudittrail command

```
ASMCMD> audcleanaudittrail --os --useTimestamp
```

In the example below, the audit files of Unified audit trail type that are older than the timestamp specified by " `audsettimestamp` " command will be deleted

Example: Using the ASMCMD audcleanaudittrail command

```
ASMCMD> audcleanaudittrail --uni --useTimestamp
```

### audclearproperty

Purpose

Clears the value for the specified audit property. When `--use_def` argument is used, the value of the property is set to its respective default value.

Syntax and Description

```
audclearproperty {--file_max_size|--file_max_age} [--use_def] {--os|--uni}
```

Options for the `audclearproperty` command

Table: Options for the audclearproperty command

| Option | Description |
| --- | --- |
| `--file_max_size` | Maximum audit file size  **Note:** For more details, see [Administering Oracle ASM audit trail](administering-oracle-asm-instances.md) |
| `--file_max_age` | Maximum audit file age  **Note:** For more details, see [Administering Oracle ASM audit trail](administering-oracle-asm-instances.md) |
| `--use_def` | Resets or sets the value back to default value. |
| `--os` | Clears property of OS audit trail type. |
| `--uni` | Clears property of Unified audit trail type. |

Note:

The default value for the age of an audit file is 5 Days and the default value for the size of an audit file is 10 MB.

Examples

The following are examples of `audclearproperty` command.

The example below sets the `file_max_size` property for the audit files of OS audit trail type to its default value.

Example: Using the ASMCMD audclearproperty command

```
ASMCMD> audclearproperty --file_max_size --use_def --os
```

The example below specifies to clear the `file_max_age` property for the audit files of Unified audit trail type. In other words, it sets `file_max_age` property to zero.

Example: Using the ASMCMD audclearproperty command

```
ASMCMD> audclearproperty --file_max_age --uni
```

### audcleartimestamp

Purpose

Clears the last archive timestamp set by audsettimestamp.

Syntax and Description

```
audcleartimestamp {--os  --inst <instancenumber> |--uni}
```

Options for the `audcleartimestamp` command

Table: Options for the audcleartimestamp command

| Option | Description |
| --- | --- |
| `--os` | Clears the last archive timestamp set for OS audit trail type. |
| `--uni` | Clears the last archive timestamp set for Unified audit trail type. |
| `--inst` `<instancenumber>` | Instance number |

Examples

The following are examples of `audcleartimestamp` command.

The example below clears the last archive timestamp set for instance number 1 of OS audit trail type.

Example: Using the ASMCMD audcleartimestamp command

```
ASMCMD> audcleartimestamp --os --inst 1
```

The example below clears the last archive timestamp set for Unified audit trail type.

Example: Using the ASMCMD audcleartimestamp command

```
ASMCMD> audcleartimestamp --uni
```

### audcreatejob

Purpose

Creates a purge job for specified audit trail type. The purge job runs at a frequency specified by `--int` and purges the audit files.

Syntax and Description

```
audcreatejob --name <job_name> --int <purge_int> {--os | --uni} [--use_ts]
```

Options for the `audcreatejob` command.

Table: Options for the audcreatejob command

| Option | Description |
| --- | --- |
| `--name` `<job_name>` | Name of the purge job |
| `--int` `<purge_int>` | Purge interval in hours |
| `--os` | Purge job for OS audit trail type |
| `--uni` | Purge job for Unified audit trail type |
| `--use_ts` | When specified, the purge will be based on the last archive timestamp set by audsettimestamp command. |

Examples

The following are examples for `audcreatejob` command.

The example below creates a job called `OSAUD_PURGE` with purge interval 10 hours for OS audit trail type and the job will use the timestamp, set earlier using `audsettimestamp`, while purging audit files (since `--use_ts` is specified).

Example: Using the ASMCMD audcreatejob command

```
ASMCMD> audcreatejob --name OSAUD_PURGE --int 10 --os --use_ts
```

The example below creates a job called `OSAUD_NOTS` with purge interval 10 hours for OS audit trail type and the job will NOT use the timestamp, set earlier using `audsettimestamp`, while purging audit files (since `--use_ts` is NOT specified).

Example: Using the ASMCMD audcreatejob command

```
ASMCMD> audcreatejob --name OSAUD_NOTS --int 10 -os
```

### auddropjob

Purpose

Drops the specified audit purge job. This command does not require any audit trail type information.

Syntax and Description

```
auddropjob --name <job_name>
```

Options for the `auddropjob` command.

Table: Options for the auddropjob command

| Option | Description |
| --- | --- |
| `--name` `<job_name>` | Name of the purge job |

Examples

The following drops the audit purge job `OSAUD_PURGE`.

Example: Using the ASMCMD auddropjob command

```
ASMCMD> auddropjob --name OSAUD_PURGE
```

### audsetdebug

Purpose

Sets the tracing to the specified debug level.

Syntax and Description

```
audsetdebug {--debug | --error}
```

Options for the `audsetdebug` command.

Table: Options for the audsetdebug command

| Option | Description |
| --- | --- |
| `--debug` | Dumps all debug information into the traces. |
| `--error` | Dumps only error information into the traces. |

Note:

The default debug level is "error".

Examples

The following example sets the debug level to " `debug` ".

Example: Using the ASMCMD audsetdebug command

```
ASMCMD> audsetdebug --debug
```

### audsetjobinterval

Purpose

Sets the job interval for the specified audit purge job.

Syntax and Description

```
audsetjobinterval --name <job_name>  --int <interval>
```

Options for the `audsetjobinterval` command.

Table: Options for the audsetjobinterval command

| Option | Description |
| --- | --- |
| `--name` `<job_name>` | Name of audit purge job |
| `--int` `<interval>` | Interval in hours |

Examples

The following example sets the interval of audit cleanup job `OSAUD_PURGE` to 10 hours.

Example: Using the ASMCMD audsetjobinterval command

```
ASMCMD> audsetjobinterval --name OSAUD_PURGE --int 10
```

### audsetjobstatus

Purpose

Sets the status of the specified purge job to enabled or disabled state.

Syntax and Description

```
audsetjobstatus --name <job_name>  {--disable | --enable}
```

Options for the `audsetjobstatus` command.

Table: Options for the audsetjobstatus command

| Option | Description |
| --- | --- |
| `--name` `<job_name>` | Audit purge job name |
| `--enable/--disable` | Enables or disables the given job. |

Note:

Audit purge job, when disabled, will not purge audit files periodically.

Examples

The following example disables the audit job `OSAUD_PURGE`.

Example: Using the ASMCMD audsetjobstatus command

```
ASMCMD> audsetjobstatus --name OSAUD_PURGE --disable
```

### audsetproperty

Purpose

Sets the value of specified audit property for given audit trail type.

Syntax and Description

```
audsetproperty {--file_max_size | --file_max_age } --val <value> {--os | --uni}
```

Options for the `audsetproperty` command.

Table: Options for the audsetproperty command

| Option | Description |
| --- | --- |
| `--file_max_size` | Maximum size of the audit file  **Note:** The value for `file_max_size` property must be in range \[1,2000000\] KB. |
| `--file_max_age` | Maximum age of the audit file  **Note:** The value for `file_max_age` property must be in range \[1, 497\] days. |
| `--val` `<value>` | Value of the property |
| `--os` | Sets property for OS audit trail type. |
| `--uni` | Sets property for Unified audit trail type. |

Examples

The following are examples of the `audsetproperty` command.

The example below sets the `file_max_size` property for the audit files of OS audit trail type audit file to 10 KB.

Example: Using the ASMCMD audsetproperty command

```
ASMCMD> audsetproperty --file_max_size --val 10 --os
```

The example below sets the `file_max_age` property for the audit files of Unified audit trail type to 10 Days.

Example: Using the ASMCMD audsetproperty command

```
ASMCMD> audsetproperty --file_max_age --val 10 --uni
```

### audsettimestamp

Purpose

Sets the last archive timestamp for specified audit trail type. This timestamp will be used by the audit purge job and `audcleanaudittrail` command, if they are configured with `--useTimestamp` option. In case of OS audit trail type, instance number is required.

Syntax and Description

```
audsettimestamp {--os|--uni} [--inst <id>] <timestamp>
```

Options for the `audsettimestamp` command.

Table: Options for the audsettimestamp command

| Option | Description |
| --- | --- |
| `--os` | Last archive timestamp for OS audit trail type |
| `--uni` | Last archive timestamp for Unified audit trail type |
| `--inst` `<id>` | Instance number |
| `<timestamp>` | Timestamp |

Examples

The following example sets the last archive timestamp of OS audit trail type in instance number 1.

Example: Using the ASMCMD audsettimestamp command

```
ASMCMD> audsettimestamp --os --inst 1 22-AUG-2012 07:48:53
```

### audshowtimestamp

Purpose

Displays the last archive timestamp set using " `audsettimestamp` " command.

Syntax and Description

```
audshowtimestamp [{--os|--uni}] [-g]
```

Options for the `audshowtimestamp` command.

Table: Options for audshowtimestamp command

| Option | Description |
| --- | --- |
| `--os` | Displays last archive timestamp set for OS audit trail type. |
| `--uni` | Displays last archive timestamp set for Unified audit trail type. |
| `-g` | Displays clusterwide timestamp information. |

Examples

The following are examples of the `audshowtimestamp` command.

The example below displays the last archive timestamp set for OS audit trail type.

Example: Using the ASMCMD audshowtimestamp command

```
ASMCMD> audshowtimestamp --os
```

The example below displays the clusterwide timestamp information for OS audit trail type.

Example: Using the ASMCMD audshowtimestamp command

```
ASMCMD> audshowtimestamp --os -g
```

See also

- [Database Reference](https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/V-ASM_AUDIT_LAST_ARCH_TS.html#GUID-92CBF38B-DF4E-4070-8873-CC0FB803CCD3) for `V$ASM_AUDIT_LAST_ARCH_TS`

### lsaudcleanupjobs

Purpose

Displays the configured audit trail purge jobs.

Syntax and Description

```
lsaudcleanupjobs [--os |--uni]
```

Options for the `lsaudcleanupjobs` command.

Table: Options for lsaudcleanupjobs command

| Option | Description |
| --- | --- |
| `--os` | Displays only the purge job configured for OS audit trail type. |
| `--uni` | Displays only the purge job configured for Unified audit trail type. |

Note:

`lsaudcleanupjobs` displays the purge jobs configured for both OS and Unified audit trail types, when no audit trail option is provided.

Examples

The following example queries audit cleanup jobs configured for OS audit trail type.

Example: Using the ASMCMD lsaudcleanupjobs command

```
ASMCMD> lsaudcleanupjobs --os
```

See also

- [Database Reference](https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/V-ASM_AUDIT_CLEANUP_JOBS.html#GUID-9356CDB7-4760-4FC3-B2AD-0E62E5ED6061) for `V$ASM_AUDIT_CLEANUP_JOBS`

### lsaudconfigparams

Purpose

Displays the configured audit trail properties for the given audit trail type.

Syntax and Description

```
lsaudconfigparams [{--os|--uni}]
```

Options for the `lsaudconfigparams` command.

Table: Options for lsaudconfigparams command

| Option | Description |
| --- | --- |
| `--os` | Displays only the audit trail properties of OS audit trail type. |
| `--uni` | Displays only the audit trail properties of unified audit trail type. |

Note:

`lsaudconfigparams` displays the audit configuration properties for both OS and Unified audit trail type, when no audit trail type option is provided.

Examples

The following example queries audit configuration parameters for OS audit trail type.

Example: Using the ASMCMD lsaudconfigparams command

```
ASMCMD> lsaudconfigparams --os
```

See also

[Database Reference](https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/V-ASM_AUDIT_CONFIG_PARAMS.html#GUID-D8B813F8-B689-4467-AA84-D0DDD4223870) for `V$ASM_AUDIT_CONFIG_PARAMS`

## ASMCMD File Management Commands

This topic provides a summary of the ASMCMD file management commands.

This table lists the ASMCMD file management commands with brief descriptions.

Table: Summary of ASMCMD file management commands

| Command | Description |
| --- | --- |
| amdu\_extract | Extracts a file from a disk group. |
| cd | Changes the current directory to the specified directory. |
| cp | Enables you to copy files between disk groups, and between a disk group and the operating system. |
| du | Displays the total disk space occupied by files in the specified Oracle ASM directory and all of its subdirectories, recursively. |
| find | Lists the paths of all occurrences of the specified name (with wildcards) under the specified directory. |
| ls | Lists the contents of an Oracle ASM directory, the attributes of the specified file, or the names and attributes of all disk groups. |
| lsof | Lists the open files. |
| mapblk | Displays where the specified file and block is located, including device path and offset within disk. |
| mkalias | Creates an alias for system-generated file names. |
| mkdir | Creates Oracle ASM directories. |
| pwd | Displays the path of the current Oracle ASM directory. |
| rm | Deletes the specified Oracle ASM files or directories. |
| rmalias | Deletes the specified alias, retaining the file that the alias points to. |

### amdu\_extract

Purpose

Extracts a file from a disk group.

Syntax and Description

```
amdu_extract diskgroup [--sys_filename] file_name disk_string
```

Table: Options for the amdu\_extract command

| Option | Description |
| --- | --- |
| `diskgroup` | Name of the disk group where the file is located. |
| `--sys_filename` | If this option is specified, then the `file_name` should point to the system Oracle ASM file name, not the file alias. |
| `file_name` | Name of the file to extract.  The file name must be one of the following:  - An Oracle ASM alias name - A system Oracle ASM filename if the `--sys_filename` option is specified  The file name can be specified as an absolute or a relative path. |
| `disk_string` | Value for the Oracle ASM discovery disk string. |

`amdu_extract` calls the Oracle ASM Metadata Dump Utility (AMDU) command to extract a file using an Oracle ASM alias name.

Example

The following is an example of the `amdu_extract` command used to extract a file from the data disk group.

Example: Using the ASMCMD amdu\_extract command

```
ASMCMD> amdu_extract data data/orcl/my_alias_filename /devices/disk*
```

### cd

Purpose

Changes the current directory to the specified directory.

Syntax and Description

```
cd [dir]
```

This table lists the options for the `cd` command.

Table: Options for the cd command

| Option | Description |
| --- | --- |
| `dir` | Name of the directory. |

*dir* can be specified as either an absolute path or a relative path, including the `.` and `..` pseudo-directories. *dir* can contain wildcard characters. See " Wildcard Characters ".

Examples

The following are examples of the `cd` command changing into various directories.

Example: Using the ASMCMD cd command

```
ASMCMD [+data/hr] > cd +data/orcl

ASMCMD [+data/orcl] > cd DATAFILE

ASMCMD [+data/orcl/DATAFILE] >cd ..
```

### cp

Purpose

Enables you to copy files between Oracle ASM disk groups and between a disk group and the operating system.

Syntax and Description

```
cp src_file [--target target_type] [--service service_name] [--port port_num] [connect_str:]tgt_file
```

The following table contains the syntax options for the `cp` command.

Table: Options for the cp command

| Option | Description |
| --- | --- |
| `--target` `target_type` | Specifies the target type of the instance that ASMCMD must be connected to for the copy operation. Valid options are `ASM`, `IOS`, or `APX`. |
| `--service` `service_name` | Specifies the Oracle ASM instance name if not the default +ASM. |
| `--port` `port_num` | Specifies the listener port number. The default is 1521. |
| `connect_str` | Specifies the connection string for a remote instance. |
| `src_file` | Name of the source file to copy. |
| `tgt_file` | A user alias for the created target file name or an alias directory name. |

`cp` cannot copy files between two remote instances. The local Oracle ASM instance must be either the source or the target of the operation.

You can use the `cp` command to:

- Copy files from a disk group to the operating system
- Copy files from a disk group to a disk group
- Copy files from the operating system to a disk group

Some file types cannot be the source or destination of the cp command. These file types include the OCR, SPFILE, Password file, and Oracle Keystore file types. To back up, copy, or move an Oracle ASM SPFILE, use the spbackup, spcopy, or spmove commands. To create, copy, or move a Password file, use the pwcreate, pwcopy, or pwmove commands. To copy an OCR backup file type, the source must be from a disk group.

The format of copied files is portable between Little-Endian and Big-Endian systems if the files exist in an Oracle ASM disk group. Oracle ASM automatically converts the format when the files are written. For copying a non-Oracle ASM file from or to an Oracle ASM disk group, you can copy the file to a different endian platform and then use one of the commonly used utilities to convert the file.

*connect\_str* is not required for a local instance copy, which is the default case. For a remote instance copy, you must specify the connect string and Oracle ASM prompts for a password in a non-echoing prompt. The *connect\_str* is in the form:

- *user* `@` *host*`.`*SID*  
	*user*, *host*, and *SID* are required in the *connect\_str* parameter. The default port number is `1521` and can be changed with the `--port` option.
- The connection privilege (`SYSASM` or `SYSDBA`) is determined by the use of the `--privilege` option when starting ASMCMD.
- *src\_file* must be either a fully qualified file name or an Oracle ASM alias.
- During an ASMCMD copy process, the Oracle ASM server creates an Oracle Managed File (OMF) file in the following format:
- *diskgroup* `/` *db\_unique\_name* `/` *file\_type* `/` *file\_name*`.`*#*`.`*#*

where *db\_uniq\_name* is set to `ASM` and *#* is a string of digits. In the copy process, ASMCMD `cp` creates the directory structure for the destination and creates a user alias from that location to the actual OMF file that is created.

Examples

The following are examples of the `cp` command. The first example shows a copy of a file in the `data` disk group to a file on the operating system. The second example shows a copy of a file on the operating system to the `data` disk group. The third example shows how to copy a file in the `data` disk group to a remote server. You are prompted to enter a password.

Example: Using the ASMCMD cp command

```
ASMCMD [+] > cp +data/orcl/datafile/EXAMPLE.265.691577295 /mybackups/example.bak
copying +data/orcl/datafile/EXAMPLE.265.691577295 -> /mybackups/example.bak

ASMCMD [+] >  cp /mybackups/examples.bak  +data/orcl/datafile/myexamples.bak
copying /mybackups/examples.bak -> +data/orcl/datafile/myexamples.bak

ASMCMD [+] > cp +data/orcl/datafile/EXAMPLE.265.691577295 sys@myserver.+ASM:/scratch/backup/myexamples.bak
Enter Password:
```

See also

Specifying the Type of Connection for more information about connection options with ASMCMD

[Oracle Database Net Services Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19&id=NETAG-GUID-855C5E77-9F2C-44E4-BD77-32FDF2D9196D) for more information about connection strings

### du

Purpose

Displays the total space used for files in the specified directory and in the entire directory tree under the directory.

Syntax and Description

```
du [--suppressheader] [dir]
```

This table lists the syntax options for the `du` command.

Table: Options for the du command

| Option | Description |
| --- | --- |
| `dir` | Name of the directory. |
| `--suppressheader` | Suppresses column headings from the output. |

If you do not specify *dir*, then information about the current directory is displayed. *dir* can contain wildcard characters. See " Wildcard Characters ".

The following two values are displayed, both in units of megabytes.

- `Used_MB` - This value does not include mirroring.
- `Mirror_used_MB` - This value includes mirroring.

For example, if a normal redundancy disk group contains 100 MB of data and each file in the disk group is 2-way mirrored, then `Used_MB` is 100 MB and `Mirror_used_MB` is roughly 200 MB.

Example

The following is an example of the `du` command. The example shows disk space used in the `orcl` directory in the `data` disk group, including all of the directories under the `orcl` directory.

Example: Using the ASMCMD du command

```
ASMCMD [+] > du data/orcl
Used_MB      Mirror_used_MB
   1756                3519
```

### find

Purpose

Displays the absolute paths of all occurrences of the specified name pattern (with wildcards) in a specified directory and its subdirectories.

Syntax and Description

```
find [--type type] dir pattern
```

This table lists the syntax options for the `find` command.

Table: Options for the find command

| Option | Description |
| --- | --- |
| `--type` `type` | Type of target to find. |
| `dir` | Directory name where you want to start searching. |
| `pattern` | Name of a target or a wildcard pattern. |

This command searches the specified directory and all subdirectories under it in the directory tree for the supplied *pattern*. The value used for *pattern* can be a directory name or a file name, and can include wildcard characters. See " Wildcard Characters ".

The ASMCMD `find` command is case insensitive.

In the output of the command, directory names are suffixed with the slash character (/) to distinguish them from file names.

Use the `--type` flag to find all the files of a particular type (specified as *type*). For example, you can search for control files by specifying *type* as `CONTROLFILE`. Valid values for *type* are listed in [Table 5-1](administering-oracle-asm-files-directories-and-templates.md). These are type values from the `type` column of the `V$ASM_FILE` view.

Examples

The following are examples of the `find` command. The first example searches the `data` disk group for files that begin with `undo`. The second example returns the absolute path of all the control files (`--type` `CONTROLFILE`) in the `+data/orcl` directory.

Example: Using the ASMCMD find command

```
ASMCMD [+] > find +data undo*
+data/ORCL/DATAFILE/UNDOTBS1.258.691577151

ASMCMD [+] >  find --type CONTROLFILE +data/orcl *
+data/orcl/CONTROLFILE/Current.260.691577263
```

### ls

Purpose

Lists the contents of an Oracle ASM directory, the attributes of the specified file, or the names and attributes of all disk groups.

Syntax and Description

```
ls [--suppressheader] [-lsdtLg][--absolutepath][--reverse]
    [--permission][pattern]
```

This table lists the syntax options for the `ls` command.

Table: Options for the ls command

| Option | Description |
| --- | --- |
| (none) | Displays only file names and directory names. |
| `-l` | Displays extended file information, including striping and redundancy information and whether the file was system-generated (indicated by `Y` under the `SYS` column) or user-created (as with an alias, indicated by `N` under the `SYS` column). When used in the " `ls -l +` " command, displays directory information.  Not all possible file attributes or disk group attributes are included. To view the complete set of column values for a file or a disk group, query the `V$ASM_FILE` and `V$ASM_DISKGROUP` views. |
| `-s` | Displays file space information. |
| `-d` | If the value for the `pattern` argument is a directory, then `ls` displays information about that directory, rather than the directory contents. Typically used with another flag, such as the `-l` flag. |
| `--reverse` | Reverses the sort order of the listing. |
| `-t` | Sorts the listing by timestamp (latest first) instead of by name. |
| `-L` | If the value for the `pattern` argument is an alias, then ASMCMD displays information about the file that it references. Typically used with another flag, such as the `-l` flag. |
| `--absolutepath` | For each listed file, displays the absolute path of the alias that references it, if any. |
| `-g` | `GV$ASM_DISKGROUP.INST_ID` is included in the output. |
| `--suppressheader` | Suppresses column headings. |
| `--permission` | Shows the permissions of a file ( `V$ASM_FILE.permission`, `V$ASM_FILE.owner`, `V$ASM_FILE.usergroup`, `V$ASM_ALIAS.name` ). |
| `pattern` | Name of a file, directory, or a pattern. |

Command options enable you to modify and customize the output of the command. This table lists the options and their descriptions. For disk group information, this command queries the `V$ASM_DISKGROUP_STAT` view by default. If you specify all of the options, then the command shows a union of their attributes, with duplicates removed. If you enter `ls` `+`, the top level directory structure is displayed.

*pattern* can be a file name, directory name, or a pattern including wildcard characters. See " Wildcard Characters ".

- If *pattern* is a directory name, then `ls` lists the contents of the directory and depending on flag settings, `ls` also lists information about each directory member. Directories are listed with a trailing slash (/) to distinguish them from files.
- If the value that you enter for *pattern* is a file name, then `ls` lists the file and depending on the flag settings, `ls` also lists information about the file. The file must be located in the current directory if the file name is specified with a relative path.

Examples

The following are examples of the `ls` command that display various information about directories and the contents of the directories.

Example: Using the ASMCMD ls command

```
ASMCMD [+] > ls +data/orcl/datafile
EXAMPLE.265.691577295
SYSAUX.257.691577149
SYSTEM.256.691577149
UNDOTBS1.258.691577151
USERS.259.691577151

ASMCMD [+] > ls -lt +data/orcl/datafile
Type      Redund  Striped  Time             Sys  Name
DATAFILE  MIRROR  COARSE   JUL 13 08:00:00  Y    EXAMPLE.265.691577295
DATAFILE  MIRROR  COARSE   JUL 13 05:00:00  Y    SYSAUX.257.691577149
DATAFILE  MIRROR  COARSE   JUL 13 02:00:00  Y    USERS.259.691577151
DATAFILE  MIRROR  COARSE   JUL 13 02:00:00  Y    UNDOTBS1.258.691577151
DATAFILE  MIRROR  COARSE   JUL 13 02:00:00  Y    SYSTEM.256.691577149

ASMCMD [+] > ls -l +data/orcl/datafile/sy*
Type      Redund  Striped  Time             Sys  Name
DATAFILE  MIRROR  COARSE   JUL 13 05:00:00  Y    SYSAUX.257.691577149
DATAFILE  MIRROR  COARSE   JUL 13 02:00:00  Y    SYSTEM.256.691577149

ASMCMD [+] > ls -s  +data/orcl/datafile
Block_Size  Blocks      Bytes       Space  Name
      8192   12801  104865792   214958080  EXAMPLE.265.691577295
      8192   88321  723525632  1452277760  SYSAUX.257.691577149
      8192   88321  723525632  1452277760  SYSTEM.256.691577149
      8192    7681   62922752   131072000  UNDOTBS1.258.691577151
      8192     641    5251072    12582912  USERS.259.691577151

ASMCMD [+] > ls --permission  +data/orcl/datafile
User  Group  Permission  Name
              rw-rw-rw-  EXAMPLE.265.691577295
              rw-rw-rw-  SYSAUX.257.691577149
              rw-rw-rw-  SYSTEM.256.691577149
              rw-rw-rw-  UNDOTBS1.258.691577151
              rw-rw-rw-  USERS.259.691577151
```

### lsof

Purpose

Lists the open files of the local clients.

Syntax and Description

```
lsof [--suppressheader] {-G diskgroup|--dbname db| -C instance}
```

This table lists the syntax options for the `lsof` command.

Table: Options for the lsof command

| Option | Description |
| --- | --- |
| `--suppressheader` | Suppresses column headings. |
| `-G` `diskgroup` | List files only from the specified disk group. |
| `--dbname` `db` | List files only from the specified database. |
| `-C` `instance` | List files only from the specified instance. |

Example

The following are examples of the `lsof` command. The first example lists the open files for the `data` disk group. The second example lists the open files for the Oracle ASM instance.

Example: Using the ASMCMD lsof command

```
ASMCMD [+] > lsof -G data
DB_Name  Instance_Name  Path
orcl     orcl           +data/orcl/controlfile/current.260.691577263
orcl     orcl           +data/orcl/datafile/example.265.691577295
orcl     orcl           +data/orcl/datafile/sysaux.257.691577149
orcl     orcl           +data/orcl/datafile/system.256.691577149
orcl     orcl           +data/orcl/datafile/undotbs1.258.691577151
orcl     orcl           +data/orcl/datafile/users.259.691577151
orcl     orcl           +data/orcl/onlinelog/group_1.261.691577267
orcl     orcl           +data/orcl/onlinelog/group_2.262.691577271
orcl     orcl           +data/orcl/onlinelog/group_3.263.691577275
orcl     orcl           +data/orcl/tempfile/temp.264.691577287

ASMCMD [+] > lsof -C +ASM
DB_Name  Instance_Name  Path
asmvol   +ASM           +data/VOLUME1.271.679226013
asmvol   +ASM           +data/VOLUME2.272.679227351
```

### mapblk

Purpose

Displays where the specified file and block is located, including device path and offset within disk.

Syntax and Description

```
mapblk [-l] [--suppressheader] <file> <block>
```

This table lists the syntax options for the `mapblk` command.

Table: Options for the mapblk command

| Option | Description |
| --- | --- |
| `(none)` | Displays `Logic_Ext`, `Block_Size`, `Offset`, `Disk_Num`, `Path`. |
| `-l` | Displays extended information, including `Disk_Name`, `AU_Size`, `File_Num`, `Ext_Num`, `AU_Num`. |
| `--suppressheader` | Suppresses column header from the output. |

The `mapblk` command displays where the specified file and block is located, including device path and offset within disk. The columns for the `mapblk` command output are described below:

- `Logic_Ext` - ASM logical extent number. 0 is primary extent. 1 and 2 are secondary extents
- `Block_Size` - Logical block size (in bytes)
- `Offset` - Offset within ASM disk (in logical blocks)
- `Disk_Num` - ASM disk number
- `Path` - Device path of ASM disk
- `Disk_Name` - ASM disk name
- `AU_Size` - Allocation Unit size (in bytes)
- `File_Num` - ASM file number
- `Ext_Num` - ASM virtual Extent number
- `AU_Num` - Allocation Unit number

Example

The following example the of `mapblk` command displays datafile `+DATA/DB1/datafile/TBS1.256.863259515` block number 10 is located to offset 2058 in logical blocks(8192 bytes) within `/dev/sdd1` and offset 4618 in logical blocks(8192 bytes) within `/dev/sde1` disk group.

Example: Using the ASMCMD mapblk command

```
ASMCMD [+] > mapblk +DATA/DB1/datafile/TBS1.256.863259515 10
        Logic_Ext  Block_Size  Offset  Disk_Num  Path
                0        8192    2058         3  /dev/sdd1
                1        8192    4618         4  /dev/sde1
```

### mkalias

Purpose

Creates an alias for the specified system-generated file name.

Syntax and Description

```
mkalias file alias
```

This table lists the syntax options for the `mkalias` command.

Table: Options for the mkalias command

| Option | Description |
| --- | --- |
| `file` | System-generated file name. |
| `alias` | Alias for the file name. |

*alias* must be in the same disk group as the system-generated file. Only one alias is permitted for each Oracle ASM file.

Example

The following example creates the `sysaux.f` alias for the fully qualified file name `+data/orcl/DATAFILE/SYSAUX.257.721811945`. Following the `mkalias` command, `ls` `--absolutepath` is run to check the results.

Example: Using the ASMCMD mkalias command

```
ASMCMD [+data/orcl/datafile] > mkalias SYSAUX.257.721811945 sysaux.f

ASMCMD [+data/orcl/datafile] > ls --absolutepath
none => EXAMPLE.265.721812093
+DATA/ORCL/DATAFILE/sysaux.f => SYSAUX.257.721811945
none => SYSTEM.256.721811945
none => UNDOTBS1.258.721811945
none => USERS.259.721811947
sysaux.f
```

### mkdir

Purpose

Creates Oracle ASM directories under the current directory.

Syntax and Description

```
mkdir dir [dir . . .]
```

This table lists the syntax options for the `mkdir` command.

Table: Options for the mkdir command

| Option | Description |
| --- | --- |
| `dir` | Directory name to create. |

The directory from which `mkdir` is run can be a system-created or user-created directory. You cannot create a directory at the root (+) level.

Example

The following is an example of the `mkdir` command. The example creates the directories `subdir1` and `subdir2` at the disk group level in the disk group `data`.

Example: Using the ASMCMD mkdir command

```
ASMCMD [+data] > mkdir subdir1 subdir2

ASMCMD [+data] > ls
ASM/
ORCL/
subdir1/
subdir2/
```

### pwd

Purpose

Displays the absolute path of the current directory.

Syntax and Description

```
pwd
```

Example

The following is an example of the `pwd` command. The example displays the current directory.

Example: Using the ASMCMD pwd command

```
ASMCMD [+data/orcl/datafile] > pwd
+data/orcl/datafile
```

### rm

Purpose

Deletes the specified Oracle ASM files and directories.

Syntax and Description

```
rm [-f|-r] pattern [pattern...]
```

This table lists the syntax options for the `rm` command.

Table: Options for the rm command

| Option | Description |
| --- | --- |
| `-r` | Recursively deletes files and subdirectories. |
| `-f` | Deletes files and subdirectories without prompting for confirmation. |
| `pattern` | Name of a file, directory, or wildcard pattern. |

If *pattern* is a file or alias, then the `rm` command can delete the file or alias only if it is not currently in use. If *pattern* is a directory, then the `rm` command can delete it only if it is empty (unless the `-r` flag is used) and it is not a system-generated directory. If *pattern* is an alias, then the `rm` command deletes both the alias and the file to which the alias refers. To delete only an alias and retain the file that the alias references, use the `rmalias` command.

Note:

When you delete all of the files in a system-created directory, the directory is removed. If the parent directories are empty, all of the parent directories are also removed.

*pattern* can contain wildcard characters. See " Wildcard Characters ".

If you use a wildcard, the `rm` command deletes all of the matches except nonempty directories, unless you use the `-r` flag. To recursively delete, use the `-r` flag. With `-r` option you can delete a nonempty directory, including all files and directories in it and in the entire directory tree underneath it. If you use the `-r` flag or a wildcard character, then the `rm` command prompts you to confirm the deletion before proceeding, unless you specify the `-f` flag.If a wildcard character matches an alias or a system-generated file that has an alias, then both the alias and the system-generated file that it references are deleted. When using the `-r` flag to delete an alias that matches a wildcard pattern, either the alias or the system-generated file that has an alias must be present in the directory in which you run the `rm` command.

For example, if you have a user alias, `+data/dir1/file.alias` that points to `+data/orcl/DATAFILE/System.256.146589651`, then running the `rm -r +data/dir1` command removes the `+data/dir1/file.alias` and `+data/orcl/DATAFILE/System.256.146589651`.

Example

The following are examples of the `rm` command. The first example deletes the `myexamples.bak` file. The second example removes the `subdir2` directory and its contents.

Example: Using the ASMCMD rm command

```
ASMCMD [+data/orcl/datafile] > rm myexamples.bak

ASMCMD [+data] > rm -r subdir2
You may delete multiple files and/or directories.
Are you sure? (y/n) y
```

### rmalias

Purpose

Removes the specified aliases, retaining the files that the aliases reference.

Syntax and Description

```
rmalias [-r] alias [alias...]
```

This table lists the syntax options for the `rmalias` command.

Table: Options for the rmalias command

| Option | Description |
| --- | --- |
| `-r` | Recursively removes aliases. |
| `alias` | Alias for the file name or directory. |

The `-r` flag enables you to remove all of the aliases in the current directory and in the entire directory tree beneath the current directory. If any user-created directories become empty after deleting aliases, they are also deleted. Files and directories created by the system are not deleted.

Example

The following is an example of the `rmalias` command. The example deletes the alias `sysaux.f`, retaining the data file that it references.

Example: Using the ASMCMD rmalias command

```
ASMCMD [+data/orcl/datafile] > rmalias sysaux.f
```

## ASMCMD Disk Group Management Commands

This topic provides a summary of the ASMCMD disk group management commands.

This table lists the ASMCMD disk group management commands with brief descriptions.

Table: Summary of ASMCMD Disk group management commands

| Command | Description |
| --- | --- |
| chdg | Changes a disk group (add, drop, rebalance, or migrate on the Exadata appliance). |
| chkdg | Checks or repairs a disk group. |
| dropdg | Drops a disk group. |
| iostat | Displays I/O statistics for disks. |
| lsattr | Lists the attributes of a disk group. |
| lsdg | Lists disk groups and their information. |
| lsdsk | Lists disks Oracle ASM disks. |
| lsod | Lists open devices. |
| md\_backup | Creates a backup of the metadata of mounted disk groups. |
| md\_restore | Restores disk groups from a backup of the metadata. |
| mkdg | Creates a disk group. |
| mount | Mounts a disk group. |
| offline | Offlines a disk or a failure group. |
| online | Onlines a disk or a failure group. |
| rebal | Rebalances a disk group. |
| remap | Relocates data in a range of physical blocks on a disk. |
| setsparseparent | Sets the parent for a sparse child file. |
| setattr | Sets attributes in a disk group. |
| stamp | Stamps the disk, site, and failure group labels in disk headers. |
| stamplist | Displays the disk, site, and failure group labels in disk headers. |
| umount | Dismounts a disk group. |

### chdg

Purpose

Modifies a disk group based on an XML configuration file.

Syntax and Description

```
chdg { config_file.xml | 'contents_of_xml_file' }
```

This table lists the syntax options for the `chdg` command.

Table: Options for the chdg command

| Option | Description |
| --- | --- |
| `config_file` | Name of the XML file that contains the changes for the disk group. `chdg` searches for the XML file in the directory where ASMCMD was started unless a path is specified. |
| `contents_of_xml_file` | The XML script enclosed in single quotations. |

The modifications include the following:

- adding, dropping, and resizing disks
- rebalancing or replacing the power level of a disk group
	The power level can be set to the same values as the `ASM_POWER_LIMIT` initialization parameter
- migrating an Exadata appliance from one fixed configuration to another
	The migration adds more disks (an equal number of disks) to each of the existing failure groups (or cells) in the disk group.

The modification includes adding, replacing, or deleting disks from an existing disk group, and the setting rebalance or replace power level. The power level can be set to the same values as the `ASM_POWER_LIMIT` initialization parameter. The modification also includes the migration from one fixed appliance configuration to another fixed appliance configuration on the Exadata appliance. The migration adds more disks (and equal number of disks) to each of the existing failure groups (or cells) in the disk group.

When adding disks to a disk group, the diskstring must be specified in a format similar to the `ASM_DISKSTRING` initialization parameter.

The failure groups are optional parameters. The default causes every disk to belong to a its own failure group.

Dropping disks from a disk group can be performed through this operation. An individual disk can be referenced by its Oracle ASM disk name. A set of disks that belong to a failure group can be specified by the failure group name.

You can resize a disk inside a disk group with `chdg`. The resize operation fails if there is not enough space for storing data after the resize.

This example shows the basic structure and the valid tags with their respective attributes for the `chdg` XML configuration file.

Example: Tags for the chdg XML configuration template

```
<chdg> update disk clause (add/delete disks/failure groups)
      name         disk group to change
      power        power to perform rebalance or replace

<add>  items to add are placed here
</add>

<replace>  items to replace are placed here
</replace>

<drop> items to drop are placed here
</drop>

<migrate> items to be migrated to another appliance configuration on EXADATA
</migrate>

<fg>  failure group
      name         failure group name
</fg>

<dsk> disk
      name         disk name
      string       disk path
      size         size of the disk to add
      force        true specifies to use the force option
</dsk>

</chdg>
```

Example 1

The following is an example of an XML configuration file for `chdg`. This XML file alters the disk group named `data`. The failure group `fg1` is dropped and the disk `data_0001` is also dropped. The `/dev/disk5` disk is added to failure group `fg2`. The rebalance power level is set to `3`.

Example: chdg sample XML configuration file

```
<chdg name="data" power="3">
  <drop>
    <fg name="fg1"></fg>
    <dsk name="data_0001"/>
  </drop>
  <add>
    <fg name="fg2">
      <dsk string="/dev/disk5"/>
    </fg>
  </add>
</chdg>
```

Example 2

The following is another example of an XML configuration file for `chdg`. This XML file migrates the failure group named `FG_01`.

Example: chdg sample XML configuration file

```
<chdg name="DATAC1 >
       <migrate>
         <add>
            <fg name = "EXA04CEL01">
              <dsk string="o/192.168.10.18/DATAC1_CD_10_exa04cel01" name= "DATAC1_CD_10_exa04cel01" />
              <dsk string="o/192.168.10.18/DATAC1_CD_11_exa04cel01" name= "DATAC1_CD_11_exa04cel01" />
            </fg>
            <fg name = "EXA04CEL02">
              <dsk string="o/192.168.10.20/DATAC1_CD_10_exa04cel02" name= "DATAC1_CD_10_exa04cel02" />
              <dsk string="o/192.168.10.20/DATAC1_CD_11_exa04cel02" name= "DATAC1_CD_11_exa04cel02" />
            </fg>
            <fg name = "EXA04CEL03""
              <dsk string="o/192.168.10.22/DATAC1_CD_10_exa04cel03" name= "DATAC1_CD_10_exa04cel03" />
              <dsk string="o/192.168.10.22/DATAC1_CD_11_exa04cel03" name= "DATAC1_CD_11_exa04cel03" />
            </fg>
         </add>
       </migrate>
</chdg>
```

Example 3

The following are examples of the `chdg` command with the configuration file or configuration information on the command line.

Example: Using the ASMCMD chdg command

```
ASMCMD [+] > chdg data_config.xml

ASMCMD [+] > chdg '<chdg name="data" power="3">
        <drop><fg name="fg1"></fg><dsk name="data_0001"/></drop>
        <add><fg name="fg2"><dsk string="/dev/disk5"/></fg></add></chdg>'
```

See also

- [ASM\_POWER\_LIMIT](administering-oracle-asm-instances.md) for information about the `ASM_POWER_LIMIT` initialization parameter
- [ASM\_DISKSTRING](administering-oracle-asm-instances.md) for information about the `ASM_DISKSTRING` initialization parameter
- [Oracle ASM Failure Groups](administering-oracle-asm-disk-groups.md) for information about failure groups
- [Dropping Disks from Disk Groups](administering-oracle-asm-disk-groups.md) for information about dropping disks
- [Resizing Disks in Disk Groups](administering-oracle-asm-disk-groups.md) for information about resizing disks,
- mkdg for information about creating a disk group with ASMCMD `mkdg`
- [Altering Disk Groups](administering-oracle-asm-disk-groups.md) for information about altering disk groups
- [Enabling the Oracle ASM appliance.mode Attribute](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19&id=SAGUG-GUID-E80B8D86-81C6-4EC1-B586-C0822F01D5B4)

### chkdg

Purpose

Checks or repairs the metadata of a disk group.

Syntax and Description

```
chkdg [--repair] diskgroup
```

This table lists the syntax options for the `chkdg` command.

Table: Options for the chkdg command

| Option | Description |
| --- | --- |
| `--repair` | Repairs the disk group. |
| `diskgroup` | Name of disk group to check or repair. |

`chkdg` checks the metadata of a disk group for errors and optionally repairs the errors.

Example

The following is an example of the `chkdg` command used to check and repair the `data` disk group.

Example: Using the ASMCMD chkdg command

```
ASMCMD [+] > chkdg --repair data
```

### dropdg

Purpose

Drops a disk group.

Syntax and Description

```
dropdg [-r [-f]] diskgroup
```

This table lists the syntax options for the `dropdg` command.

Table: Options for the dropdg command

| Option | Description |
| --- | --- |
| `-f` | Force the operation. Only applicable if the disk group cannot be mounted. |
| `-r` | Recursive, include contents. |
| `diskgroup` | Name of disk group to drop. |

`dropdg` drops an existing disk group. The disk group should not be mounted on multiple nodes.

Example

These are examples of the use of `dropdg`. The first example forces the drop of the disk group `data`, including any data in the disk group. The second example drops the disk group `fra`, including any data in the disk group.

Example: Using the ASMCMD dropdg command

```
ASMCMD [+] > dropdg -r -f data

ASMCMD [+] > dropdg -r fra
```

### iostat

Purpose

Displays I/O statistics for Oracle ASM disks in mounted disk groups.

Syntax and Description

```
iostat [--suppressheader] [-et] [--io] [--region]
  [-G diskgroup] [interval]
```

`iostat` lists disk group statistics using the `V$ASM_DISK_STAT` view.

This table lists the syntax options for the `iostat` command.

Table: Options for the iostat command

| Option | Description |
| --- | --- |
| `-e` | Displays error statistics (Read\_Err, Write\_Err). |
| `-G` `diskgroup` | Displays statistics for the disk group name. |
| `--suppressheader` | Suppresses column headings. |
| `--io` | Displays information in number of I/Os, instead of bytes. |
| `-t` | Displays time statistics (Read\_Time, Write\_Time). |
| `--region` | Displays information for cold and hot disk regions (Cold\_Reads, Cold\_Writes, Hot\_Reads, Hot\_Writes).  > Note: >  > Disk region attributes default to cold and cold is the only permitted setting. This means that values for Hot\_Reads and Hot\_Writes are zero. |
| `interval` | Refreshes the statistics display based on the interval value (seconds). Use CTRL+C to stop the interval display. |

This table shows the statistics for a disk group. To view the complete set of statistics for a disk group, use the `V$ASM_DISK_STAT` and `V$ASM_DISK_IOSTAT` views.

Table: Attribute descriptions for iostat command output

| Attribute Name | Description |
| --- | --- |
| Group\_Name | Name of the disk group. |
| Dsk\_Name | Name of the disk. |
| Reads | Number of bytes read from the disk. If the `--io` option is entered, then the value is displayed as number of I/Os. |
| Writes | Number of bytes written to the disk. If the `--io` option is entered, then the value is displayed as number of I/Os. |
| Cold\_Reads | Number of bytes read from the cold disk region. If the `--io` option is entered, then the value is displayed as number of I/Os. |
| Cold\_Writes | Number of bytes written from the cold disk region. If the `--io` option is entered, then the value is displayed as number of I/Os. |
| Hot\_Reads | Number of bytes read from the hot disk region. If the `--io` option is entered, then the value is displayed as number of I/Os.  **Note:** Disk region attributes default to cold and cold is the only permitted setting. This means that values for Hot\_Reads and Hot\_Writes are zero. |
| Hot\_Writes | Number of bytes written to the hot disk region. If the `--io` option is entered, then the value is displayed as number of I/Os.  **Note:** Disk region attributes default to cold and cold is the only permitted setting. This means that values for Hot\_Reads and Hot\_Writes are zero. |
| Read\_Err | Number of failed I/O read requests for the disk. |
| Write\_Err | Number of failed I/O write requests for the disk. |
| Read\_Time | I/O time (in seconds) for read requests for the disk if the `TIMED_STATISTICS` initialization parameter is set to `TRUE` (0 if set to `FALSE` ). |
| Write\_Time | I/O time (in seconds) for write requests for the disk if the `TIMED_STATISTICS` initialization parameter is set to `TRUE` (0 if set to `FALSE` ). |

If a refresh interval is not specified, the number displayed represents the total number of bytes or I/Os. If a refresh interval is specified, then the value displayed (bytes or I/Os) is the difference between the previous and current values, not the total value.

Example

The following are examples of the `iostat` command. The first example displays disk I/O statistics for the `data` disk group in total number of bytes. The second example displays disk I/O statistics for the `data` disk group in total number of I/O operations.

Example: Using the ASMCMD iostat command

```
ASMCMD [+] > iostat -G data
Group_Name  Dsk_Name   Reads       Writes
DATA        DATA_0000  180488192   473707520
DATA        DATA_0001  1089585152  469538816
DATA        DATA_0002  191648256   489570304
DATA        DATA_0003  175724032   424845824
DATA        DATA_0004  183421952   781429248
DATA        DATA_0005  1102540800  855269888
DATA        DATA_0006  171290624   447662592
DATA        DATA_0007  172281856   361337344
DATA        DATA_0008  173225472   390840320
DATA        DATA_0009  288497152   838680576
DATA        DATA_0010  196657152   375764480
DATA        DATA_0011  436420096   356003840

ASMCMD [+] > iostat --io -G data
Group_Name  Dsk_Name   Reads  Writes
DATA        DATA_0000  2801   34918
DATA        DATA_0001  58301  35700
DATA        DATA_0002  3320   36345
DATA        DATA_0003  2816   10629
DATA        DATA_0004  2883   34850
DATA        DATA_0005  59306  38097
DATA        DATA_0006  2151   10129
DATA        DATA_0007  2686   10376
DATA        DATA_0008  2105   8955
DATA        DATA_0009  9121   36713
DATA        DATA_0010  3557   8596
DATA        DATA_0011  17458  9269
```

### lsattr

Purpose

Lists the attributes of a disk group.

Syntax and Description

```
lsattr [--suppressheader][-G diskgroup ] [-lm] [pattern]
```

This table lists the syntax options for the `lsattr` command.

Table: Options for the lsattr command

| Option | Description |
| --- | --- |
| `-G` `diskgroup` | Disk group name. |
| `--suppressheader` | Suppresses column headings. |
| `-l` | Display names with values. |
| `-m` | Displays additional information, such as the RO and Sys columns. |
| `pattern` | Display the attributes that contain pattern expression. |

Note:

Attributes are only displayed for disk groups where `COMPATIBLE.ASM` is set to 11.1 or higher.

Information about disk group attributes is retrieved from the `V$ASM_ATTRIBUTE` view. For information about disk group attributes, refer to [Managing Disk Group Attributes](administering-oracle-asm-disk-groups.md).

The RO (read-only) column identifies those attributes that can only be set when a disk group is created. The **Sys** column identifies those attributes that are system-created.

To display information about the disk group template attributes, refer to lstmpl.

To set disk group attributes, refer to setattr.

Example

The following are examples of the `lsattr` command. The first displays information about all attributes for the `data` disk group. The second example displays only those attributes with names containing the string `compat` for the `fra` disk group. Note the use of both the `%` and `*` wildcard characters on Linux.

Example: Using the ASMCMD lsattr command

```
ASMCMD [+] > lsattr -lm -G data
Group_Name  Name                        Value         RO  Sys
DATA        access_control.enabled      FALSE         N   Y
DATA        access_control.umask        066           N   Y
DATA        appliance._partnering_type  GENERIC       Y   Y
DATA        ate_conversion_done         true          Y   Y
DATA        au_size                     1048576       Y   Y
DATA        cell.smart_scan_capable     FALSE         N   N
DATA        cell.sparse_dg              allnonsparse  N   N
DATA        compatible.advm             19.0.0.0.0    N   Y
DATA        compatible.asm              19.0.0.0.0    N   Y
DATA        compatible.rdbms            19.0.0.0.0    N   Y
DATA        content.check               FALSE         N   Y
DATA        content.type                data          N   Y
DATA        content_hardcheck.enabled   FALSE         N   Y
DATA        disk_repair_time            12.0h         N   Y
DATA        failgroup_repair_time       24.0h         N   Y
DATA        idp.boundary                auto          N   Y
DATA        idp.type                    dynamic       N   Y
DATA        logical_sector_size         512           N   Y
DATA        phys_meta_replicated        true          Y   Y
DATA        preferred_read.enabled      FALSE         N   Y
DATA        scrub_async_limit           1             N   Y
DATA        scrub_metadata.enabled      TRUE          N   Y
DATA        sector_size                 512           N   Y
DATA        thin_provisioned            FALSE         N   Y
DATA        vam_migration_done          false         Y   Y

ASMCMD [+] > lsattr -G fra -l %compat*
Name              Value
compatible.advm   19.0.0.0.0
compatible.asm    19.0.0.0.0
compatible.rdbms  19.0.0.0.0
```

### lsdg

Purpose

Lists mounted disk groups and their information. `lsdg` queries `V$ASM_DISKGROUP_STAT` by default. If the `--discovery` flag is specified, the `V$ASM_DISKGROUP` is queried instead. The output also includes notification of any current rebalance operation for a disk group. If a disk group is specified, then `lsdg` returns only information about that disk group.

Syntax and Description

```
lsdg [--suppressheader] [-g] [--discovery] [pattern]
```

This table lists the options for the `lsdg` command.

Table: Options for the lsdg command

| Option | Description |
| --- | --- |
| (none) | Displays the disk group attributes listed in the next table. |
| `--discovery` | Selects from `V$ASM_DISKGROUP`, or from `GV$ASM_DISKGROUP` if the -g flag is also specified. This option is always enabled if the Oracle ASM instance is version 10.1 or earlier. This flag is disregarded if `lsdg` is running in non-connected mode. |
| `-g` | Selects from `GV$ASM_DISKGROUP_STAT`, or from `GV$ASM_DISKGROUP` if the `--discovery` flag is also specified. `GV$ASM_DISKGROUP.INST_ID` is included in the output.  The Rebal attribute value is derived from the value of the OPERATION column in the `GV$ASM_OPERATION` view. The PASS column in `GV$ASM_OPERATION` also indicates if a rebalance operation is running. |
| `--suppressheader` | Suppresses column headings. |
| `pattern` | Returns only information about the specified disk group or disk groups that match the supplied pattern. See " Wildcard Characters ". |

This table shows the attributes for each disk group. To view the complete set of attributes for a disk group, use the `V$ASM_DISKGROUP_STAT` or `V$ASM_DISKGROUP` view.

See also

[*Oracle Database Reference*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19&id=REFRN-GUID-5CF77719-75BE-4312-84A3-49A7C6A20393) for descriptions of disk group information displayed in the `V$ASM_DISKGROUP` view

Table: Attribute descriptions for lsdg command output

| Attribute Name | Description |
| --- | --- |
| State | State of the disk group. For example, `BROKEN`, `CONNECTED`, `DISMOUNTED`, `MOUNTED`, `QUIESCING`, or `UNKNOWN`. |
| Type | Disk group redundancy. For example, `NORMAL`, `HIGH`, `FLEX`, or `EXTERNAL`. |
| Rebal | `Y` indicates that a rebalance operation is in progress. |
| Sector | Sector size in bytes. |
| Block | Block size in bytes. |
| AU | Allocation unit size in bytes. |
| Total\_MB | Size of the disk group in megabytes. |
| Free\_MB | Free space in the disk group in megabytes, without regard to redundancy. From the `V$ASM_DISKGROUP` view. |
| Req\_mir\_free\_MB | Amount of space that must be available in the disk group to restore full redundancy after the most severe failure that can be tolerated by the disk group. This is the `REQUIRED_MIRROR_FREE_MB` column from the `V$ASM_DISKGROUP` view. |
| Usable\_file\_MB | Amount of free space, adjusted for mirroring, that is available for new files. From the `V$ASM_DISKGROUP` view. |
| Offline\_disks | Number of offline disks in the disk group. Offline disks are eventually dropped. |
| Voting\_files | Specifies whether the disk group contains voting files ( `Y` or `N` ). |
| Name | Disk group name. |

Example

The following example lists the attributes of the `data` disk group.

Example: Using the ASMCMD lsdg command

```
ASMCMD [+] > lsdg data
State    Type    Rebal  Sector  Block       AU  Total_MB  Free_MB  Req_mir_free_MB  Usable_file_MB
MOUNTED  NORMAL  N         512   4096  4194304     12288     8835             1117            3859

(continued)
Offline_disks  Voting_files  Name
            0             N  DATA
```

### lsdsk

Purpose

Lists Oracle ASM disks.

Syntax and Description

```
lsdsk [--suppressheader] [-kptgMI] [-G diskgroup ]
  [ --member|--candidate]
  [--discovery][--statistics][pattern]
```

This table lists the options for the `lsdsk` command.

Table: Options for the lsdsk command

| Option | Description |
| --- | --- |
| (none) | Displays the `PATH` column of the `V$ASM_DISK_STAT` view. |
| `-k` | Displays the `TOTAL_MB`, `FREE_MB`, `OS_MB`, `NAME`, `FAILGROUP`, `LIBRARY`, `LABEL`, `UDID`, `PRODUCT`, `REDUNDANCY`, and `PATH` columns of the `V$ASM_DISK` view. |
| `--statistics` | Displays the `READS`, `WRITES`, `READ_ERRS`, `WRITE_ERRS`, `READ_TIME`, `WRITE_TIME`, `BYTES_READ`, `BYTES_WRITTEN`, and the `PATH` columns of the `V$ASM_DISK` view. |
| `-p` | Displays the `GROUP_NUMBER`, `DISK_NUMBER`, `INCARNATION`, `MOUNT_STATUS`, `HEADER_STATUS`, `MODE_STATUS`, `STATE`, and the `PATH` columns of the `V$ASM_DISK` view. |
| `-t` | Displays the `CREATE_DATE`, `MOUNT_DATE`, `REPAIR_TIMER`, and the `PATH` columns of the `V$ASM_DISK` view. |
| `-g` | Selects from `GV$ASM_DISK_STAT`, or from `GV$ASM_DISK` if the `--discovery` flag is also specified. `GV$ASM_DISK.INST_ID` is included in the output. |
| `--discovery` | Selects from `V$ASM_DISK`, or from `GV$ASM_DISK` if the -g flag is also specified. This option is always enabled if the Oracle ASM instance is version 10.1 or earlier. This flag is disregarded if `lsdsk` is running in non-connected mode. |
| `--suppressheader` | Suppresses column headings. |
| `-I` | Scans disk headers for information rather than extracting the information from an Oracle ASM instance. This option forces non-connected mode. |
| `-G` | Restricts results to only those disks that belong to the group specified by `diskgroup`. |
| `-M` | Displays the disks that are visible to some but not all active instances. These are disks that, if included in a disk group, cause the mount of that disk group to fail on the instances where the disks are not visible. |
| `--candidate` | Restricts results to only disks having membership status equal to `CANDIDATE`. |
| `--member` | Restricts results to only disks having membership status equal to `MEMBER`. |
| `pattern` | Returns only information about the specified disks that match the supplied pattern. |

The `lsdsk` command can run in connected or non-connected mode. The connected mode is always attempted first. The `-I` option forces non-connected mode.

- In connected mode, `lsdsk` uses the `V$ASM_DISK_STAT` and `V$ASM_DISK` dynamic views to retrieve disk information. The `V$ASM_DISK_STAT` view is used by default.
- In non-connected mode, `lsdsk` scans disk headers to retrieve disk information. Some information is not available in this mode and some options are not valid combinations with this mode.

Note:

The non-connected mode is not supported on Windows.

*pattern* restricts the output to only disks that match the pattern specified. Wild-card characters and slashes (`/` or `\`) can be part of the pattern. *pattern* should be specified as the last option for the command. For information about wildcards, see " Wildcard Characters ".

The `-k`, `-p`, `-t`, and `--statistics` options modify how much information is displayed for each disk. If any combination of the options are specified, then the output shows the union of the attributes associated with each flag.

Example

The following are examples of the `lsdsk` command. The first and second examples list information about disks in the `data` disk group. The third example lists information about candidate disks.

Example: Using the ASMCMD lsdsk command

```
ASMCMD [+] > lsdsk -t -G data
Create_Date  Mount_Date  Repair_Timer  Path
13-JUL-09    13-JUL-09   0             /devices/diska1
13-JUL-09    13-JUL-09   0             /devices/diska2
13-JUL-09    13-JUL-09   0             /devices/diska3
13-JUL-09    13-JUL-09   0             /devices/diskb1
13-JUL-09    13-JUL-09   0             /devices/diskb2
13-JUL-09    13-JUL-09   0             /devices/diskb3
13-JUL-09    13-JUL-09   0             /devices/diskc1
13-JUL-09    13-JUL-09   0             /devices/diskc2
...

ASMCMD [+] > lsdsk -p -G data /devices/diska*
Group_Num  Disk_Num      Incarn  Mount_Stat  Header_Stat  Mode_Stat  State   Path
        1         0  2105454210  CACHED      MEMBER       ONLINE     NORMAL  /devices/diska1
        1         1  2105454199  CACHED      MEMBER       ONLINE     NORMAL  /devices/diska2
        1         2  2105454205  CACHED      MEMBER       ONLINE     NORMAL  /devices/diska3

ASMCMD [+] > lsdsk --candidate -p
Group_Num  Disk_Num      Incarn  Mount_Stat  Header_Stat  Mode_Stat  State   Path
        0         5  2105454171  CLOSED      CANDIDATE    ONLINE     NORMAL  /devices/diske1
        0        25  2105454191  CLOSED      CANDIDATE    ONLINE     NORMAL  /devices/diske2
        0        18  2105454184  CLOSED      CANDIDATE    ONLINE     NORMAL  /devices/diske3
        0        31  2105454197  CLOSED      CANDIDATE    ONLINE     NORMAL  /devices/diskk1
        0        21  2105454187  CLOSED      CANDIDATE    ONLINE     NORMAL  /devices/diskk2
        0        26  2105454192  CLOSED      CANDIDATE    ONLINE     NORMAL  /devices/diskk3
        0        14  2105454180  CLOSED      CANDIDATE    ONLINE     NORMAL  /devices/diskl1
...
```

### lsod

Purpose

Lists the open Oracle ASM disks.

Syntax and Description

```
lsod [--suppressheader] [-G diskgroup] [--process process] [pattern]
```

This table lists the syntax options for the `lsod` command.

Table: Options for the lsod command

| Option | Description |
| --- | --- |
| `--suppressheader` | Suppresses column header information from the output. |
| `-G` `diskgroup` | Specifies the disk group that contains the open disks. |
| `--process` `process` | Specifies a pattern to filter the list of processes. |
| `pattern` | Specifies a pattern to filter the list of disks. |

The rebalance operation (`RBAL`) opens a disk both globally and locally so the same disk may be listed twice in the output for the `RBAL` process.

Example

The following are examples of the `lsod` command. The first example lists the open devices associated with the `data` disk group and the `LGWR` process. The second example lists the open devices associated with the `LGWR` process for disks that match the `diska` pattern.

Example: Using the ASMCMD lsod command

```
ASMCMD [+] > lsod -G data --process *LGWR*
Instance Process                  OSPID Path
1        oracle@myserver02 (LGWR) 26593 /devices/diska1
1        oracle@myserver02 (LGWR) 26593 /devices/diska2
1        oracle@myserver02 (LGWR) 26593 /devices/diska3
1        oracle@myserver02 (LGWR) 26593 /devices/diskb1
1        oracle@myserver02 (LGWR) 26593 /devices/diskb2
1        oracle@myserver02 (LGWR) 26593 /devices/diskb3
1        oracle@myserver02 (LGWR) 26593 /devices/diskd1

ASMCMD [+] > lsod --process *LGWR* *diska*
Instance Process                  OSPID Path
1        oracle@myserver02 (LGWR) 26593 /devices/diska1
1        oracle@myserver02 (LGWR) 26593 /devices/diska2
1        oracle@myserver02 (LGWR) 26593 /devices/diska3
```

### md\_backup

Purpose

The `md_backup` command creates a backup file containing metadata for one or more disk groups.

Syntax and Description

```
md_backup backup_file
  [-G 'diskgroup [,diskgroup,...]'] --acfs_sec_encr
```

This table describes the options for the `md_backup` command.

Table: Options for the md\_backup command

| Option | Description |
| --- | --- |
| `backup_file` | Specifies the backup file in which you want to store the metadata. |
| `-G` `diskgroup` | Specifies the disk group name of the disk group that must be backed up |
| `--acfs_sec_encr` | Specifies that security, encryption, or audit metadata information from Oracle ACFS is backed up. |

By default all the mounted disk groups are included in the backup file, which is saved in the current working directory if a path is not specified with the file name.

The `md_backup` command backs up Oracle Automatic Storage Management Cluster File System (Oracle ACFS) metadata information for the contained Oracle ASM Dynamic Volume Manager(Oracle ADVM) volumes, including stripe size, redundancy, and other items. This command also backs up Oracle ACFS file system configuration metadata, such as compression and resize attributes, block size, and created snapshots. Additional metadata and configuration attributes may be backed up; however, Oracle ACFS file system data and Oracle ACFS CRS Resource information is not backed up.

Example

The first example shows the use of the backup command when run without the disk group option. This example backs up all the mounted disk groups and creates the backup image in the `/scratch/backup/alldgs20100422` file. The second example creates a backup of the `data` disk group. The metadata backup that this example creates is saved in the `/scratch/backup/data20100422` file.

Example: Using the ASMCMD md\_backup command

```
ASMCMD [+] > md_backup /scratch/backup/alldgs20100422
Disk group metadata to be backed up: DATA
Disk group metadata to be backed up: FRA
Current alias directory path: ORCL/ONLINELOG
Current alias directory path: ORCL/PARAMETERFILE
Current alias directory path: ORCL
Current alias directory path: ASM
Current alias directory path: ORCL/DATAFILE
Current alias directory path: ORCL/CONTROLFILE
Current alias directory path: ASM/ASMPARAMETERFILE
Current alias directory path: ORCL/TEMPFILE
Current alias directory path: ORCL/ARCHIVELOG/2010_04_20
Current alias directory path: ORCL
Current alias directory path: ORCL/BACKUPSET/2010_04_21
Current alias directory path: ORCL/ARCHIVELOG/2010_04_19
Current alias directory path: ORCL/BACKUPSET/2010_04_22
Current alias directory path: ORCL/ONLINELOG
Current alias directory path: ORCL/BACKUPSET/2010_04_20
Current alias directory path: ORCL/ARCHIVELOG
Current alias directory path: ORCL/BACKUPSET
Current alias directory path: ORCL/ARCHIVELOG/2010_04_22
Current alias directory path: ORCL/DATAFILE
Current alias directory path: ORCL/CONTROLFILE
Current alias directory path: ORCL/ARCHIVELOG/2010_04_21

ASMCMD [+] > md_backup /scratch/backup/data20100422 -G data
Disk group metadata to be backed up: DATA
Current alias directory path: ORCL/ONLINELOG
Current alias directory path: ASM
Current alias directory path: ORCL/CONTROLFILE
Current alias directory path: ASM/ASMPARAMETERFILE
Current alias directory path: ORCL/PARAMETERFILE
Current alias directory path: ORCL
Current alias directory path: ORCL/DATAFILE
Current alias directory path: ORCL/TEMPFILE
```

### md\_restore

Purpose

The `md_restore` command restores disk groups from a metadata backup file.

Syntax and Description

```
md_restore  backup_file [--silent]
  [--full|--nodg|--newdg -o 'old_diskgroup:new_diskgroup [,...]']
   [--acfs_sec_encr user:group |
    --acfs_sec_encr user:group --acfs_audit user:mgr_group:auditor_group ]
  [-S sql_script_file] [-G 'diskgroup [,diskgroup...]']
```

This table describes the options for the `md_restore` command.

Table: Options for the md\_restore command

| Option | Description |
| --- | --- |
| `backup_file` | Reads the metadata information from `backup_file`. |
| `--silent` | Ignore errors. Typically, if `md_restore` encounters an error, it stops. Specifying this flag ignores any errors. |
| `--full` | Specifies to create a disk group and restore metadata. |
| `--nodg` | Specifies to restore metadata only. |
| `--newdg` `-o` `old_diskgroup` `:` `new_diskgroup` \] | Specifies to create a disk group with a different name when restoring metadata. The `-o` option is required with `--newdg`. |
| `--acfs_sec_encr` `user` `:` `group` | Restores the metadata of security or encryption or both. The colon separated user and group is used for security metadata restoration. During metadata restore, security or encryption or both must be initialized. If security or encryption or both are not pre-initialized, the colon separated values passed to the `--acfs_sec_encr` option are used to initialize security. Encryption is initialized with the SSO wallet. |
| `--acfs_audit` `user` `:` `mgr_group` `:` `auditor_group` | Restores audit metadata information on an Oracle ACFS file system. The colon separated values are used to initialize and execute audit commands. During metadata restore, audit must be initialized. If audit is not pre-initialized, the audit layer is initialized using the colon separated values given to the `--acfs_audit` option. The `--acfs_audit` option requires the `--acfs_sec_encr` option. |
| `-S` `sql_script_file` | Write SQL commands to the specified SQL script file instead of executing the commands. |
| `-G` `diskgroup` | Select the disk groups to be restored. If no disk groups are defined, then all disk groups are restored. |

Example

Note the following when restoring Oracle ACFS information:

- When restoring the metadata of a file system, the user id is set to the user id that owned the file system when the metadata backup was created. This user id should exist on the restore cluster.
- `md_restore` restores Oracle ACFS metadata information. To run the metadata restore for Oracle ACFS file systems, a script is created. This script must be run as `root` to format file systems. Metadata for the contained Oracle ADVM volumes, such as stripe size and redundancy, is restored. Oracle ACFS file system configuration metadata, such as compression and resize attributes, block size, and created snapshots, is also restored. Oracle ACFS file System data and ACFS CRS Resource information is not restored.
- If using the `--silent` option while specifying a single disk group, and there is a dependency due to Oracle ADVM metadata or Oracle ACFS accelerators on another disk group, that dependency is dropped, and you must manually recreate that dependency later.
- When restoring Oracle ACFS encryption or security, file system extended attributes (xattrs) must be restored with the user data. It is very important to document that xattrs need to be stored and restored with the file system application data. Without the xattrs, there is no security or encryption. xattrs describe which security realms the file is a part of. With no xattr, the file ends up in no realm. The converse is that a file with xattrs, but no security initialized, ends up in no realm.
- During metadata restore, a file with a list of previously configured snapshots is created. Snapshot data is not restored, as the point in time sparse snapshot views cannot be recreated.
- If Oracle ACFS security is in use, and the metadata security information for the file system has not been backed up, this information may be copied by the security administrator to the metadata backup file location, and then restored with the rest of the disk group information.
- If Oracle ACFS security and encryption is being restored, the user and password may be pre-initialized. If it is not, the username provided is used to initialize Oracle ACFS security and encryption, with a default password which is displayed.

The first example restores the disk group `data` from the backup script and creates a copy. The second example takes an existing disk group `data` and restores its metadata. The third example restores disk group `data` completely but the new disk group that is created is named `data2`. The fourth example restores from the backup file after applying the overrides defined in the `override.sql` script file.

Example: Using the ASMCMD md\_restore command

```
ASMCMD [+] > md_restore --full -G data --silent /scratch/backup/alldgs20100422

ASMCMD [+] > md_restore --nodg -G data --silent /scratch/backup/alldgs20100422

ASMCMD [+] > md_restore --newdg -o 'data:data2' --silent /scratch/backup/data20100422

ASMCMD [+] > md_restore -S override.sql --silent /scratch/backup/data20100422
```

### mkdg

Purpose

Creates a disk group based on an XML configuration file.

Syntax and Description

```
mkdg { config_file.xml | 'contents_of_xml_file' }
```

This table lists the syntax options for the `mkdg` command.

Table: Options for the mkdg command

| Option | Description |
| --- | --- |
| `config_file` | Name of the XML file that contains the configuration for the new disk group. `mkdg` searches for the XML file in the directory where ASMCMD was started unless a path is specified. |
| `contents_of_xml_file` | The XML script enclosed in single quotations. |

`mkdg` creates a new disk group with an XML configuration file that specifies the name of the disk group, redundancy, attributes, and paths of the disks that form the disk group. Redundancy is an optional parameter; the default is normal redundancy. For some types of redundancy, disks are required to be gathered into failure groups. In the case that failure groups are not specified for a disk group, each disk in the disk group belongs to its own failure group.

The `mkdg` command only mounts a disk group on the local node.

It is possible to set some disk group attribute values during disk group creation. Some attributes, such as `AU_SIZE` and `SECTOR_SIZE`, can be set only during disk group creation.

This exmaple shows the basic structure and the valid tags with their respective attributes for the `mkdg` XML configuration file.

Example: Tags for mkdg XML configuration file

```
<dg>  disk group
      name         disk group name
      redundancy   normal, external, high

<fg>  failure group
      name         failure group name
</fg>

<dsk> disk
      name         disk name
      string       disk path
      size         size of the disk to add
      force        true specifies to use the force option
</dsk>

<a>   attribute
      name         attribute name
      value        attribute value
</a>

</dg>
```

Example

The following is an example of an XML configuration file for `mkdg`. The configuration file creates a disk group named `data` with `normal` redundancy. Two failure groups, `fg1` and `fg2`, are created, each with two disks identified by associated disk strings. The disk group compatibility attributes are all set to `19.0`.

Example: mkdg sample XML configuration file

```
<dg name="data" redundancy="normal">
  <fg name="fg1">
    <dsk string="/dev/disk1"/>
    <dsk string="/dev/disk2"/>
  </fg>
  <fg name="fg2">
    <dsk string="/dev/disk3"/>
    <dsk string="/dev/disk4"/>
  </fg>
  <a name="compatible.asm" value="19.0"/>
  <a name="compatible.rdbms" value="19.0"/>
  <a name="compatible.advm" value="19.0"/>
</dg>
```

The following are examples of the `mkdg` command. The first example runs `mkdg` with an XML configuration file in the directory where ASMCMD was started. The second example runs `mkdg` using information on the command line.

Example: Using the ASMCMD mkdg command

```
ASMCMD [+] > mkdg data_config.xml

ASMCMD [+] > mkdg '<dg name="data"><dsk string="/dev/disk*"/></dg>'
```

See also

- [Managing Disk Group Attributes](administering-oracle-asm-disk-groups.md) for more information about disk groups attributes
- [Disk Group Compatibility](administering-oracle-asm-disk-groups.md) for information about disk group compatibility attributes
- chdg for information about altering a disk group with ASMCMD `chdg`
- [Creating Disk Groups](administering-oracle-asm-disk-groups.md) for information about creating a disk group

### mount

Purpose

Mounts a disk group.

Syntax and Description

```
mount [--restrict] { [-a] | [-f] diskgroup[ diskgroup ...] }
```

This table lists the syntax options for the `mount` command.

Table: Options for the mount command

| Option | Description |
| --- | --- |
| `diskgroup` | Name of the disk group. |
| `-a` | Mounts all disk groups. |
| `--restrict` | Mounts in restricted mode. |
| `-f` | Forces the mount operation. |

This operation mounts one or more disk groups. A disk group can be mounted with or without force or restricted options. For more information about mounting disk groups, see " [Mounting and Dismounting Disk Groups](administering-oracle-asm-disk-groups.md) ".

Example

The following are examples of the `mount` command showing the use of the force, restrict, and all options.

Example: Using the ASMCMD mount command

```
ASMCMD [+] > mount -f data

ASMCMD [+] > mount --restrict data

ASMCMD [+] > mount -a
```

### offline

Purpose

Offline disks or failure groups that belong to a disk group.

Syntax and Description

```
offline -G diskgroup
  { -F failgroup |-D disk}
  [-t {minutes | hours}]
```

This table lists the syntax options for the `offline` command.

Table: Options for the offline command

| Option | Description |
| --- | --- |
| `-G` `diskgroup` | Disk group name. |
| `-F` `failgroup` | Failure group name. |
| `-D` `disk` | Specifies a single disk name. |
| `-t` `minutes` \| `hours` | Specifies the time before the specified disk is dropped as `n` `m` or `n` `h`, where `m` specifies minutes and `h` specifies hours. For example, `120m` or `2h`.The default unit is hours. |

When a failure group is specified, this implies all the disks that belong to it should be offlined.

Example

The following are examples of the `offline` command. The first example offlines the `failgroup1` failure group of the `data` disk group. The second example offlines the `data_0001` disk of the `data` disk group with a time of `1.5` hours before the disk is dropped.

Example: Using the ASMCMD offline command

```
ASMCMD [+] > offline -G data -F failgroup1

ASMCMD [+] > offline -G data -D data_0001 -t 1.5h
```

### online

Purpose

Online all disks, a single disk, or a failure group that belongs to a disk group.

Syntax and Description

```
disk
```

This table lists the syntax options for the `online` command.

Table: Options for the online command

| Option | Description |
| --- | --- |
| `-a` | Online all offline disks in the disk group. |
| `-G` `diskgroup` | Disk group name. |
| `-F` `failgroup` | Failure group name. |
| `-D` `disk` | Disk name. |
| `--power` `n` | Specifies the power option ( `1` to `1024` ) which determines the level of resources for the disk resync and disk group rebalance. Larger values result in faster disk resync and disk group rebalance. The default is `1`. |
| `-w` | Wait option. Causes ASMCMD to wait for the disk group to be rebalanced before returning control to the user. The default is not waiting. |

When a failure group is specified, this implies all the disks that belong to it should be onlined.

Example

The following are examples of the `online` command. The first example onlines all disks in the `failgroup1` failure group of the `data` disk group with the `wait` option enabled. The second example onlines the `data_0001` disk in the `data` disk group.

Example: Using the ASMCMD online command

```
ASMCMD [+] > online -G data -F failgroup1 -w

ASMCMD [+] > online -G data -D data_0001
```

### rebal

Purpose

Rebalances a disk group.

Syntax and Description

```
rebal [--default | --modify power] [--with phase,... | --without phase,...]
  [--power power] [-w] diskgroup
```

This table lists the syntax options for the `rebal` command.

Table: Options for the rebal command

| Option | Description |
| --- | --- |
| `-default` | Sets the rebalance power to the default, which is the value of the `ASM_POWER_LIMIT` initialization parameter. This option does not restart the rebalance operation. |
| `--modify` `power` | Modifies the rebalance power without restarting the rebalance operation. Accepted values are the same as `ASM_POWER_LIMIT` ( `0` to `1024` ). A value of `0` disables rebalancing. |
| `--with` `phase` | Runs rebalance only on the specified phases. Available phases are `prepare`, `balance`, and `compact`. The phases must be separated by a single comma. If this option is specified, at least one phase must be specified. |
| `--without` `phase` | Does not run rebalance on the specified phases. Phases are `prepare`, `balance`, and `compact`. The phases must be separated by a single comma. If this option is specified, at least one phase must be specified. |
| `--power` `power` | Specifies the power setting. Accepted values are the same as `ASM_POWER_LIMIT` ( `0` to `1024` ). A value of `0` disables rebalancing. |
| `-w` | Specifies the wait option. ASMCMD waits for the disk group to be rebalanced before returning control to the user. The default is not waiting. |
| `diskgroup` | Specifies the disk group name. |

The power level can be set to the same values as the `ASM_POWER_LIMIT` initialization parameter. A value of `0` disables rebalancing. If the rebalance power is not specified, the value defaults to the setting of the `ASM_POWER_LIMIT` initialization parameter.

You can determine if a rebalance operation is occurring with the ASMCMD `lsop` command.

Example

In the following example, the first `rebal` command rebalances the `FRA` disk group with a power level set to `4`, performing only the `balance` and `compact` phases. The second `rebal` command rebalances the `DATA` disk group with the rebalance power set to `1`, but does not restart the rebalance operation.

Example: Using the ASMCMD rebal command

```
ASMCMD [+] > rebal --with balance,compact --power 4 FRA

ASMCMD [+] > lsop
Group_Name  Operation  State  Power
FRA         REBAL      RUN    4

ASMCMD [+] > rebal --modify 1 DATA
```

### remap

Purpose

Marks a range of blocks as unusable on the disk and relocates any data allocated in that range.

Syntax and Description

```
remap diskgroup disk block_range
```

This table lists the syntax options for the `remap` command.

Table: Options for the remap command

| Option | Description |
| --- | --- |
| `diskgroup` | Disk group name in which a disk must have data relocated. |
| `disk` | Name of the disk that must have data relocated. The name must match the `NAME` column in the `V$ASM_DISK` view. |
| `block_range` | Range of physical blocks to relocate in the format `start_range_number` `-` `end_range_number`. |

The `remap` command only relocates blocks. It does not correct or repair blocks that contain corrupted contents. The command uses a physical block size based on the `SECTOR_SIZE` disk group attribute.

Examples

The first example remaps blocks `5000` through `5999` for disk `DATA_0001` in disk group `DATA`. The second example remaps blocks `6230` through `6339` for disk `FRA_0002` in disk group `FRA`

Example: Using the ASMCMD remap command

```
ASMCMD [+] > remap DATA DATA_0001 5000-5999

ASMCMD [+] > remap FRA FRA_0002 6230-6339
```

### setsparseparent

Purpose

Sets the parent for a sparse child file.

Syntax and Description

```
setsparseparent child_file1 [child_file2 ...] parent_file
```

The following table lists the syntax options for the `setsparseparent` command.

Table: Options for the setsparseparent command

| Option | Description |
| --- | --- |
| `child_fileN` | Name of the child file. |
| `parent_file` | Name of the parent file. |

The following are the examples of `setsparseparent` command. The first example sets a parent file in the data disk group to a sparse file in the sparse disk group. The second example sets a parent file in the data disk group to multiple sparse files in the sparse disk group.

Example: Using the ASMCMD setsparseparent command

```
ASMCMD [+] > setsparseparent +SPARSEDG/child.1.10 +DATA/parent.1.f
setting parent of +SPARSEDG/child.1.10 to +DATA/parent.1.f

ASMCMD [+] > setsparseparent +SPARSEDG/child.1a.10 +SPARSEDG/child.1b.11 +SPARSEDG/child.1c.12 +DATA/parent.1.f
setting parent of +SPARSEDG/child.1a.10 to +DATA/parent.1.f
setting parent of +SPARSEDG/child.1b.11 to +DATA/parent.1.f
setting parent of +SPARSEDG/child.1c.12 to +DATA/parent.1.f
```

### setattr

Purpose

Sets the attributes for an Oracle ASM disk group.

Syntax and Description

```
setattr -G diskgroup attribute_name attribute_value
```

This table lists the syntax options for the `setattr` command.

Table: Options for the setattr command

| Option | Description |
| --- | --- |
| `-G` `diskgroup` | Disk group name. |
| `attribute_name` | Name of the attribute. |
| `attribute_value` | Value of the attribute. |

The `COMPATIBLE.ASM` attribute must be advanced before advancing other disk group compatibility attributes and its value must be greater than or equal to the value of other disk group compatibility attributes.

For information about disk group attributes, see " [Managing Disk Group Attributes](administering-oracle-asm-disk-groups.md) ".

Example

The following are examples of the `setattr` command. The first example sets the disk group attribute `COMPATIBLE.ASM` for the `data` disk group. The second example sets the disk group attribute `COMPATIBLE.RDBMS` for the `data` disk group.

Example: Using the ASMCMD setattr command

```
ASMCMD [+] > setattr -G data compatible.asm 19.0

ASMCMD [+] > setattr -G data compatible.rdbms 19.0
```

### stamp

Purpose

Stamps the disk, site, and failure group labels in disk headers.

Syntax and Description

```
stamp --dscstr disk_discovery_string
  [--site site_name --failgroup failgroup_name]
  [--disk disk_label] [-f]
```

The following table describes the options for the `stamp` command.

Table: Options for the stamp command

| Option | Description |
| --- | --- |
| `--dscstr` `disk_discovery_string` | Specifies the disk discovery string that identifies the disks on which to stamp labels. |
| `--site` `site_name` | Specifies the site label name. |
| `--failgroup` `failgroup_name` | Specifies the failure group label. Required when the site label is specified. |
| `--disk` `disk_label` | Specifies the disk label. |
| `-f` | Specifies to force the action. |

ASMCMD `stamp` enables the users to stamp the disk, site, and fail group labels on disk headers. Using `stamp` is more efficient than individually specifying label information during installation and creation of disk groups.

Site label and fail groups labels are used for the site names and fail group names when creating and altering a disk group. Disk labels are only intended for use with Oracle ASM filter driver (AFD) and Oracle ASM libraries.

At least one label specification (`--site` with `--failgroup` or `--disk`) must be provided.

Examples

The following example shows the use of the ASMCMD `stamp` command on the disks identified by the `/dev/sd*` disk discovery string.

Example: Using ASMCMD stamp

```
ASMCMD [+] > stamp --dscstr "/dev/sd*" --site "SALTLAKE-CENTER" --failgroup "fg1" --disk "DISK1"
```

### stamplist

Purpose

Displays the disk, site and failure group labels in disk headers.

Syntax and Description

```
stamp --dscstr disk_discovery_string  {[--site] [--failgroup] [--disk]}
```

The following table describes the options for the `stamplist` command.

Table: Options for the stamplist command

| Option | Description |
| --- | --- |
| `--dscstr` `disk_discovery_string` | Specifies the disk discovery string that identifies the disks for which to display labels. |
| `--site` | Displays the site label name. |
| `--failgroup` | Displays the failure group label. |
| `--disk` | Displays the disk label. |

You must specify at least one of the `--site`, `--failgroup`, or `--disk` options.

Examples

The following example shows the use of the ASMCMD `stamplist` command to display site, failure group, and disk labels of the disks identified by the `/dev/sd*` disk discovery string.

Example: Using ASMCMD stamplist

```
ASMCMD [+] > stamplist --dscstr "/dev/sd*" --site --failgroup --disk
```

### umount

Purpose

Dismounts a disk group.

Syntax and Description

```
umount { -a | [-f] diskgroup }
```

This table lists the syntax options for the `umount` command.

Table: Options for the umount command

| Option | Description |
| --- | --- |
| `diskgroup` | Name of the disk group. |
| `-a` | Dismounts all mounted disk groups. These disk groups are listed in the output of the `V$ASM_DISKGROUP` view. |
| `-f` | Forces the dismount operation. |

Example

The following are examples of the `umount` command. The first example dismounts all disk groups mounted on the Oracle ASM instance. The second example forces the dismount of the `data` disk group.

Example: Using the ASMCMD umount command

```
ASMCMD [+] > umount -a

ASMCMD [+] > umount -f data
```

## ASMCMD File Group Management Commands

This topic provides a summary of the ASMCMD commands that enable you to manage Oracle ASM file groups and quota groups.

The following table lists the ASMCMD file group and quota group commands with brief descriptions.

Table: Summary of ASMCMD file group commands

| Command | Description |
| --- | --- |
| chfg | Modifies a file group in a disk group based on an XML configuration file or script. |
| chqg | Modifies a quota group in the disk group. |
| lsfg | List file groups in a disk group. |
| lsqg | Lists the quota groups in a disk group. |
| mkfg | Creates a file group in a disk group based on an XML configuration file or script. |
| mkqg | Adds a quota group to the disk group. |
| mvfg | Moves a file group in a disk group to the specified quota group. |
| mvfile | Moves a file to the specified file group in the same disk group where the file is stored. |
| rmfg | Removes an existing file group from a disk group. |
| rmqg | Drops a quota group from a disk group. |

See also

- [Managing Oracle ASM Flex Disk Groups](administering-oracle-asm-disk-groups.md) for more information about Oracle file groups
- [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19&id=REFRN-GUID-8C5690B0-DE10-4460-86DF-80111869CF4C) for information about the `V$ASM` views that contain file group and quota group information.
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19&id=SQLRF-GUID-22D73AB6-7063-4627-A2ED-18D521ED2557) for information about administering Oracle ASM file groups and quota groups with SQL statements

### chfg

Purpose

Changes the attributes of a file group in a disk group based on an XML configuration file or script.

Syntax and Description

```
chfg { config_file.xml | 'contents_of_xml_script' }
```

The following table lists the options for the `chfg` command.

Table: Options for the chfg command

| Option | Description |
| --- | --- |
| `config_file.xml` | Name of the XML file that contains the changes for the file group. `chfg` searches for the XML file in the current working directory of ASMCMD unless a path is specified |
| `contents_of_xml_script.xml` | The contents of an XML script enclosed in single quotes. |

The root element of the XML configuration file or script is the `<file_group>` tag and has these attributes:

- `name`: file group name
- `dg`: disk group name to which the file group belongs

You can set properties using these tag:

- `name`: property name
- `value`: property value
- `file_type`: property file type (optional)
- `template`: Oracle ASM template name (optional)

Using an Oracle ASM template for a file group property requires an Oracle ASM File Access Control check.

The following is an example of an XML configuration file for `chfg`. The configuration file alters a file group named `filegroup1` on disk group `dg_data1`. The file group is associated with quota group `quotagroup1`.

```
<filegroup name="filegroup1" dg="dg_data1">
  <p name="quota_group" value="quotagroup1"/>
</filegroup>
```

For information about Oracle ASM File Groups, refer to [Managing Oracle ASM Flex Disk Groups](administering-oracle-asm-disk-groups.md).

Example

The following examples show the use of the `chfg` command using an XML configuration file and an XML script.

Example: Using the chfg command

```
ASMCMD [+] > chfg config_file.xml

ASMCMD [+] > chfg '<filegroup name="filegroup1" dg="dg_data1">
                  <p name="redundancy" value="high"/>
                  </filegroup>'
```

### chqg

Purpose

Modifies a quota group in the disk group.

Syntax and Description

```
chqg -G disk_group quota_group property value
```

The following table lists the options for the `chqg` command.

Table: Options for the chqg command

| Option | Description |
| --- | --- |
| `-G` `disk_group` | Specifies the disk group. |
| `quota_group` | Specifies the quota group. |
| `property` | Specifies the name of the property. |
| `value` | Specifies the value of the property. |

The `chqg` command modifies the specified property in the specified quota group of the specified disk group. For information about Oracle ASM File and Quota Groups, refer to " [Managing Oracle ASM Flex Disk Groups](administering-oracle-asm-disk-groups.md) ".

The following are examples of the `chqg` command. The first example modifies the `quota` property of the quota group `quota_grp1` in the `data` disk group. The second example modifies the `quota` property of the quota group `quota_grp2` in the `data` disk group.

Example: Using the chqg command

```
ASMCMD [+] > chqg -G data quota_grp1 quota 200G

ASMCMD [+] > chqg -G data quota_grp2 quota UNLIMITED
```

### lsfg

Purpose

List file groups in a disk group.

Syntax and Description

```
lsfg [-G disk_group] [--filegroup file_group] [--suppressheader]
```

The following table lists the options for the `lsfg` command.

Table: Options for the lsfg command

| Option | Description |
| --- | --- |
| `-G` `disk_group` | Specifies the disk group. |
| `-filegroup` `file_group` | Specifies the file group. |
| `-suppressheader` | Suppresses the headers in the output of the command. |

If the disk group option is specified, then `lsfg` returns only information about file groups in the specified disk group. If the file group option is specified, then `lsfg` returns only information about that file group.

The information about file groups is retrieved from `V$ASM_FILEGROUP` and `V$ASM_FILEGROUP_PROPERTY` views.

The following example shows the use of the `lsfg` command. The first command in the example displays the properties of the file group `FG1` in the `DATA` disk group. The second command lists all the file groups and their properties in the `DATA` disk group.

Example: Using the lsfg command

```
ASMCMD [+] > lsfg -G DATA
File Group         Disk Group  Quota Group  Used Quota MB  Client Name  Client Type
DEFAULT_FILEGROUP  DATA        GENERIC      0
VOLUME1            DATA        GENERIC      3123           VOLUME1      VOLUME
ORCL               DATA        GENERIC      5488           ORCL         DATABASE

ASMCMD [+] > lsfg -G DATA --filegroup ORCL
File Group  Disk Group  Property           Value       File Type
ORCL        DATA        PRIORITY           MEDIUM
ORCL        DATA        STRIPING           COARSE      CONTAINER
ORCL        DATA        REDUNDANCY         HIGH        CONTROLFILE
ORCL        DATA        STRIPING           FINE        CONTROLFILE
ORCL        DATA        REDUNDANCY         MIRROR      DATAFILE
ORCL        DATA        STRIPING           COARSE      DATAFILE
...
```

### lsqg

Purpose

Lists the quota groups in a disk group.

Syntax and Description

```
lsqg [-G disk_group] [--quotagroup quota_group] [--suppressheader]
```

The following table lists the options for the `lsqg` command.

Table: Options for the lsqg command

| Option | Description |
| --- | --- |
| `-G` `disk_group` | Specifies the disk group. |
| `-quotagroup` `quota_group` | Specifies the quota group. |
| `-suppressheader` | Suppresses the headers in the output of the command. |

If the disk group option is specified, then `lsqg` returns only information about quota groups in the specified disk group. If the quota group option is specified, then `lsqg` returns only information about that quota group.

The information about file groups is retrieved from `V$ASM_QUOTAGROUP` view.

The following example shows the use of the `lsqg` command. The first command in the example displays the properties of the file group `QG1` in the `DATA` disk group. The second command lists all the quota groups and their properties in the `DATA` disk group. The third command lists all the quota groups with name `QG1` in all the disk groups mounted by the current Oracle ASM instance. The fourth command lists all the quota groups in all the disk groups mounted by the current Oracle ASM instance.

Example: Using the lsqg command

```
ASMCMD [+] > lsqg -G DATA --quotagroup QG1
Used_Quota_MB  Quota_Limit_MB
100            200

ASMCMD [+] > lsqg -G DATA
Quotagroup_Num  Quotagroup_Name  Used_Quota_MB  Quota_Limit_MB
1               GENERIC          12357          262143
2               QG1              100            200
3               QG2              400            420

ASMCMD [+] > lsqg --quotagroup QG1
Group_Num  Quotagroup_Num  Used_Quota_MB  Quota_Limit_MB
1          2               100            200
3          5               821            1024

ASMCMD [+] > lsqg
Group_Num  Quotagroup_Num  Quotagroup_Name  Used_Quota_MB  Quota_Limit_MB
1          1               GENERIC          12357          262143
1          2               QG1              100            200
1          3               QG2              400            420
2          1               GENERIC          54000          262143
3          1               GENERIC          11             262143
3          5               QG1              821            1024
```

### mkfg

Purpose

Creates a file group in a disk group based on an XML configuration file or script.

Syntax and Description

```
mkfg { config_file.xml | 'contents_of_xml_script' }
```

The following table lists the options for the `mkfg` command.

Table: Options for the mkfg command

| Option | Description |
| --- | --- |
| `config_file.xml` | Name of the XML file that contains the configuration information for the file group. `mkfg` searches for the XML file in the current working directory of ASMCMD unless a path is specified |
| `contents_of_xml_script.xml` | The contents of an XML script enclosed in single quotes. |

The root element of the XML configuration file or script is the `<file_group>` tag and has these attributes:

- `name`: file group name
- `dg`: disk group name to which the file group belongs
- `client_type`: database, cluster, volume
- `client_name`: database, CDB, PDB, cluster or volume name

You can set properties using these tag:

- `name`: property name
- `value`: property value
- `file_type`: property file type (optional)
- `template`: Oracle ASM template name (optional)

Using an Oracle ASM template for a file group property requires an Oracle ASM File Access Control check.

The following is an example of an XML configuration file for `mkfg`. The configuration file creates a file group named `filegroup1` on disk group `dg_data1` for a database named `sample`. The file group is associated with quota group `quotagroup1`. The files in this file group have the redundancy set to mirror, except for the control file, which has a high redundancy. All other attributes are set to the default value.

```
<filegroup name="filegroup1" dg="dg_data1" client_type="database" client_name="sample">
  <p name="redundancy" value="mirror"/>
  <p name="redundancy" value="high" file_type="controlfile"/>
  <p name="quota_group" value="quotagroup1"/>
</filegroup>
```

For information about Oracle ASM File Groups, refer to " [Managing Oracle ASM Flex Disk Groups](administering-oracle-asm-disk-groups.md) ".

Example

The following examples show the use of the `mkfg` command using an XML configuration file and an XML script.

Example: Using the mkfg command

```
ASMCMD [+] > mkfg config_file.xml

ASMCMD [+] > mkfg '<filegroup name="filegroup1" dg="dg_data1" client_type="database" client_name="sample">
                   </filegroup>'
```

### mkqg

Purpose

Adds a quota group to the disk group.

Syntax and Description

```
mkqg -G disk_group quota_group [property] [value]
```

The following table lists the options for the `chqg` command.

Table: Options for the mkqg command

| Option | Description |
| --- | --- |
| `-G` `disk_group` | Specifies the disk group. |
| `quota_group` | Specifies the quota group. |
| `property` | Specifies the name of the property. |
| `value` | Specifies the value of the property. |

The `mkqg` command adds the specified quota group with an optional the specified property to the specified disk group. For information about Oracle ASM file and quota groups, refer to " [Managing Oracle ASM Flex Disk Groups](administering-oracle-asm-disk-groups.md) ".

The following are examples of the `mkqg` command. The first example adds the quota group `quota_grp1` to the `data` disk group without specifying a property. The second example adds the quota group `quota_grp2` to the `data` disk group while specifying the `quota` property.

Example: Using the mkqg command

```
ASMCMD [+] > mkqg -G data quota_grp1

ASMCMD [+] > mkqg -G data quota_grp2 quota 100G
```

### mvfg

Purpose

Moves a file group in a disk group to the specified quota group.

Moving a file group to a different quota group requires only the `SYSASM` privilege.

Syntax and Description

```
mvfg -G disk_group --filegroup file_group quota_group
```

The following table lists the options for the `mvfg` command.

Table: Options for the mvfg command

| Option | Description |
| --- | --- |
| `-G` `disk_group` | Specifies the disk group. |
| `-filegroup` `file_group` | Specifies the file group. |
| `quota_group` | Specifies the quota group. |

The following is an example of the `mvfg` command. In the example, the file group `FG1` in the `DATA` disk group is moved to the quota group `QG1`

Example: Using the mvfg command

```
ASMCMD [+] > mvfg -G DATA --filegroup FG1 QG1
```

### mvfile

Purpose

Moves a file to the specified file group in the same disk group where the file is stored.

Moving a file between file groups requires an Oracle ASM File Access Control check.

Syntax and Description

```
mvfile file_name --filegroup file_group
```

The following table lists the options for the `mvfile` command.

Table: Options for the mvfile command

| Option | Description |
| --- | --- |
| `file_name` | Specifies the file to be moved. |
| `-filegroup` `file_group` | Specifies the file group name. |

The following `mvfile` commands move the specified Oracle ASM file to the named file group.

Example: Using the mvfile command

```
ASMCMD [+] > mvfile +data/orcl/controlfile/Current.260.684924747 --filegroup FG1

ASMCMD [+fra/orcl/archivelog/flashback] > mvfile log_7.264.684968167 --filegroup FG1
```

### rmfg

Purpose

Removes an existing file group from a disk group.

Syntax and Description

```
rmfg [-r] disk_group file_group
```

The following table lists the options for the `rmfg` command.

Table: Options for the rmfg command

| Option | Description |
| --- | --- |
| `-r` | Specifies a recursive operation. |
| `disk_group` | Specifies the disk group. |
| `file_group` | Specifies the file group. |

The `-r` option specifies a recursive removal, including contents. All files in the disk group that the file group contains are removed at the same time that the file group is removed. You must specify this option to remove a file group that contains any files. If you omit this option and the file group is not empty, then ASMCMD returns an error and does not remove the file group.

The following example shows the use of the `rmfg` command. The first command in the example removes file group `FG1` from the `DATA1` disk group. The second command removes file group `FG2`, and its contents, from the `DATA2` disk group.

Example: Using the rmfg command

```
ASMCMD [+] > rmfg DATA1 FG1
 ASMCMD [+] > rmfg -r DATA2 FG2
```

### rmqg

Purpose

Removes a quota group from a disk group.

Syntax and Description

```
rmqg -G disk_group quota_group
```

The following table lists the options for the `rmqg` command.

Table: Options for the rmqg command

| Option | Description |
| --- | --- |
| `-G` `disk_group` | Specifies the disk group. |
| `quota_group` | Specifies the quota group. |

The following example shows the use of the `rmqg` command. The command in the example removes quota group `QG1` from the `DATA` disk group.

Example: Using the rmqg command

```
ASMCMD [+] > rmqg -G DATA QG1
```

## ASMCMD Template Management Commands

This topic provides a summary of the ASMCMD template management commands.

This table lists the ASMCMD template management commands with brief descriptions.

Table: Summary of ASMCMD template management commands

| Command | Description |
| --- | --- |
| chtmpl | Changes the attributes of a template. |
| lstmpl | Lists disk group templates. |
| mktmpl | Adds a template to a disk group. |
| rmtmpl | Removes a template from a disk group. |

### chtmpl

Purpose

Changes the attributes of a template.

Syntax and Description

```
chtmpl -G diskgroup { [--striping {coarse|fine}]
  [--redundancy {high|mirror|unprotected} ] } template
```

This table lists the syntax options for the `chtmpl` command.

Table: Options for the chtmpl command

| Option | Description |
| --- | --- |
| `-G` `diskgroup` | Name of the disk group. |
| `template` | Name of the template to change. |
| `--striping` { `coarse` \| `fine` } | Striping specification, either `coarse` or `fine`. |
| `--redundancy` { `high` \| `mirror` \| `unprotected` } | Redundancy specification, either `high`, `mirror`, or `unprotected`. |

At least one of the following options is required: `--striping` or `--redundancy`.

For information about updating templates, see " [Modifying a Disk Group Template](administering-oracle-asm-files-directories-and-templates.md) ".

Example

The following is an example of the `chtmpl` command that updates the `mytemplate` template of the `data` disk group. The redundancy attribute is set to high and the striping attribute is set to fine.

Example: Using the ASMCMD chtmpl command

```
ASMCMD [+] > chtmpl -G data --redundancy high --striping fine mytemplate
```

### lstmpl

Purpose

Lists all templates for all disk groups or the templates for a specified disk group.

Syntax and Description

```
lstmpl [--suppressheader] [-l] [-G diskgroup] [pattern]
```

This table lists the syntax options for the `lstmpl` command.

Table: Options for the lstmpl command

| Option | Description |
| --- | --- |
| `-G` `diskgroup` | Specifies disk group name. |
| `--suppressheader` | Suppresses column headings. |
| `-l` | Displays all details. |
| `pattern` | Displays the templates that match pattern expression. |

For information about template attributes, see " [Template Attributes](administering-oracle-asm-files-directories-and-templates.md) ".

Example

The following is an example of the `lstmpl` command. The example lists all details of the templates in the `data` disk group.

Example: Using the ASMCMD lstmpl command

```
ASMCMD [+] > lstmpl -l -G data

Group_Name  Group_Num  Name                       Stripe  Sys  Redund  PriReg  MirrReg
DATA        1          ARCHIVELOG                 COARSE  Y    MIRROR  COLD    COLD
DATA        1          ASMPARAMETERFILE           COARSE  Y    MIRROR  COLD    COLD
DATA        1          AUDIT_SPILLFILES           COARSE  Y    MIRROR  COLD    COLD
DATA        1          AUTOBACKUP                 COARSE  Y    MIRROR  COLD    COLD
DATA        1          AUTOLOGIN_KEY_STORE        COARSE  Y    MIRROR  COLD    COLD
DATA        1          BACKUPSET                  COARSE  Y    MIRROR  COLD    COLD
DATA        1          CHANGETRACKING             COARSE  Y    MIRROR  COLD    COLD
DATA        1          CONTROLFILE                FINE    Y    HIGH    COLD    COLD
DATA        1          DATAFILE                   COARSE  Y    MIRROR  COLD    COLD
DATA        1          DATAGUARDCONFIG            COARSE  Y    MIRROR  COLD    COLD
DATA        1          DUMPSET                    COARSE  Y    MIRROR  COLD    COLD
DATA        1          FLASHBACK                  COARSE  Y    MIRROR  COLD    COLD
DATA        1          FLASHFILE                  COARSE  Y    MIRROR  COLD    COLD
DATA        1          INCR XTRANSPORT BACKUPSET  COARSE  Y    MIRROR  COLD    COLD
DATA        1          KEY_STORE                  COARSE  Y    MIRROR  COLD    COLD
DATA        1          OCRFILE                    COARSE  Y    MIRROR  COLD    COLD
DATA        1          ONLINELOG                  COARSE  Y    MIRROR  COLD    COLD
DATA        1          PARAMETERFILE              COARSE  Y    MIRROR  COLD    COLD
DATA        1          TEMPFILE                   COARSE  Y    MIRROR  COLD    COLD
DATA        1          VOTINGFILE                 COARSE  Y    MIRROR  COLD    COLD
DATA        1          XTRANSPORT                 COARSE  Y    MIRROR  COLD    COLD
DATA        1          XTRANSPORT BACKUPSET       COARSE  Y    MIRROR  COLD    COLD
```

### mktmpl

Purpose

Adds a template to a disk group.

Syntax and Description

```
mktmpl -G diskgroup [--striping {coarse|fine}]
  [--redundancy {high|mirror|unprotected}] template
```

This table lists the syntax options for the `mktmpl` command.

Table: Options for the mktmpl command

| Option | Description |
| --- | --- |
| `-G` `diskgroup` | Name of the disk group. |
| `template` | Name of the template to create. |
| `--striping` { `coarse` \| `fine` } | Striping specification, either `coarse` or `fine`. |
| `--redundancy` { `high` \| `mirror` \| `unprotected` } | Redundancy specification, either `high`, `mirror`, or `unprotected`. |

For information about adding templates, see [Adding Templates to a Disk Group](administering-oracle-asm-files-directories-and-templates.md).

Example

The following is an example of the `mktmpl` command that adds the `mytemplate` template to the `data` disk group. The new template has the redundancy set to mirror and the striping set to coarse.

Example: Using the ASMCMD mktmpl command

```
ASMCMD [+] > mktmpl -G data --redundancy mirror --striping coarse mytemplate
```

### rmtmpl

Purpose

Removes a template from a disk group.

Syntax and Description

```
template
```

This table lists the syntax options for the `rmtmpl` command.

Table: Options for the rmtmpl command

| Option | Description |
| --- | --- |
| `-G` `diskgroup` | Name of the disk group. |
| `template` | Name of the template to delete. |

For information about template attributes, see " [Template Attributes](administering-oracle-asm-files-directories-and-templates.md) ".

Example

The following is an example of the `rmtmpl` command that removes the `mytemplate` template from the `data` disk group.

Example: Using the ASMCMD rmtmpl command

```
ASMCMD [+] > rmtmpl -G data mytemplate
```

## ASMCMD File Access Control Commands

This topic provides a summary of the ASMCMD Oracle ASM File Access Control commands.

For information about Oracle ASM File Access Control, see [Managing Oracle ASM File Access Control for Disk Groups](administering-oracle-asm-disk-groups.md).

When administering users with ASMCMD, the users must be existing operating system users and their user names must have corresponding operating system user IDs. However, only users in the same cluster as the Oracle ASM instance can be validated.

Note:

When modifying ownership of files, the previous owner of a file cannot be dropped while the file is still open even after the ownership of the file has changed.

This table lists the ASMCMD Oracle ASM File Access Control commands with brief descriptions.

Table: Summary of ASMCMD file access control commands

| Command | Description |
| --- | --- |
| chgrp | Changes the user group of a file or list of files. |
| chmod | Changes permissions of a file or list of files. |
| chown | Changes the owner of a file or list of files. |
| groups | Lists the user groups to which a user belongs. |
| grpmod | Adds or removes users from an existing user group. |
| lsgrp | Lists user groups. |
| lsusr | Lists users in a disk group. |
| mkgrp | Creates a new user group. |
| mkusr | Adds a user to disk group. |
| passwd | Changes the password of a user. |
| rmgrp | Deletes a user group. |
| rmusr | Deletes a user from a disk group. |
| rpusr | Replaces one a user with another in a disk group. |

### chgrp

Purpose

Changes the user group of a file or list of files.

Syntax and Description

```
chgrp usergroup file [file ...]
```

This table lists the syntax options for the `chgrp` command.

Table: Options for the chgrp command

| Option | Description |
| --- | --- |
| `usergroup` | Name of the user group. |
| `file` | Name of a file. |

Only the file owner or the Oracle ASM administrator can use this command. If the user is the file owner, then the user must also be either the owner or a member of the group for this command to succeed.

This command accepts a file name or multiple file names separated by spaces.

If you change the user group settings of an open file, then the operation currently running on the file completes using the old user group settings. The new settings take effect when re-authentication is required.

Examples

The following are examples of the `chgrp` command that change the Oracle ASM user group of the specified files.

Example: Using the ASMCMD chgrp command

```
ASMCMD [+] > chgrp asm_data +data/orcl/controlfile/Current.260.684924747

ASMCMD [+fra/orcl/archivelog/flashback] > chgrp asm_fra log_7.264.684968167 log_8.265.684972027
```

### chmod

Purpose

Changes permissions of a file or list of files.

Syntax and Description

```
chmod mode file [file ...]
```

*mode* can be one of the following forms:

- { `ugo` | `ug` | `uo` | `go` | `u` | `g` | `o` | `a` } { `+` | `-` } { `r` | `w` | `rw` }
	`a` specifies permissions for all users, `u` specifies permissions for the owner of the file, `g` specifies the group permissions, and `o` specifies permissions for other users.
- { `0` | `4` | `6` } { `0` | `4` | `6` } { `0` | `4` | `6` }
	The first digit specifies `owner` permissions, the second digit specifies `group` permissions, and the third digit specifies `other` permissions.

This table lists the syntax options for the `chmod` command.

Table: Options for the chmod command

| Option | Description |
| --- | --- |
| `6` | Read write permissions |
| `4` | Read only permissions |
| `0` | No permissions |
| `u` | Owner permissions, used with `r` or `w` |
| `g` | Group permissions, used with `r` or `w` |
| `o` | Other user permissions, used with `r` or `w` |
| `a` | All user permissions, used with `r` or `w` |
| `+` | Add a permission, used with `r` or `w` |
| `-` | Removes a permission, used with `r` or `w` |
| `r` | Read permission |
| `w` | Write permission |
| `file` | Name of a file |

This command accepts a file name or multiple file names separated by spaces.

You can only set file permissions to read-write, read-only, and no permissions. You cannot set file permissions to write-only.

If you change the permission settings of an open file, then the operation currently running on the file completes using the old permission settings. The new settings take effect when re-authentication is required.

To view the permissions on a file, use the ASMCMD `ls` command with the `--permission` option. See " ls ".

Examples

The following are examples of the `chmod` command that change the permissions of the specified files.

Example: Using the ASMCMD chmod command

```
ASMCMD [+fra/orcl/archivelog/flashback] > chmod ug+rw log_7.264.684968167 log_8.265.684972027

ASMCMD [+fra/orcl/archivelog/flashback] > chmod 640 log_7.264.684968167 log_8.265.684972027

ASMCMD [+] > ls --permission +fra/orcl/archivelog/flashback
User      Group      Permission  Name
grid      asm_fra     rw-r-----  log_7.264.684968167
grid      asm_fra     rw-r-----  log_8.265.684972027
```

### chown

Purpose

Changes the owner of a file or list of files.

Syntax and Description

```
chown user[:usergroup ] file [file ...]
```

This table lists the syntax options for the `chown` command.

Table: Options for the chown command

| Option | Description |
| --- | --- |
| `user` | The name of the user that becomes the new owner. |
| `usergroup` | Name of the user group to which the user belongs. |
| `file` | Name of a file. |

*user* typically refers to the user that owns the database instance home. Oracle ASM File Access Control uses the operating system (OS) name to identify a database.

This command accepts a file name or multiple file names separated by spaces.

If you change the ownership settings of an open file, then the following applies:

- The operation currently running on the file completes using the old ownership and user group settings. The new settings take effect when re-authentication is required.
- The new owner of the file cannot be dropped from the disk group until all instances in a cluster are restarted in a rolling manner.

Only the Oracle ASM administrator can use this command.

Examples

The following are examples of the `chown` command that change the owner of the specified files to the `oracle1` operating system user.

Example: Using the ASMCMD chown command

```
ASMCMD [+fra/orcl/archivelog/flashback] > chown oracle1 log_7.264.684968167 log_8.265.684972027

ASMCMD [+fra/orcl/archivelog/flashback] > chown oracle1:asm_fra log_9.264.687650269
```

### groups

Purpose

Lists all the user groups to which the specified user belongs.

Syntax and Description

```
groups diskgroup user
```

This table lists the syntax options for the `groups` command.

Table: Options for the groups command

| Option | Description |
| --- | --- |
| `diskgroup` | Name of the disk group to which the user belongs. |
| `user` | Name of the user. |

Examples

The following is an example of the `groups` command that displays the user groups of the `data` disk group to which the `oracle1` user belongs.

Example: Using the ASMCMD groups command

```
ASMCMD [+] > groups data oracle1
asm_data
```

### grpmod

Purpose

Adds or removes operating system (OS) users to and from an existing Oracle ASM user group.

Syntax and Description

```
grpmod { --add | --delete } diskgroup usergroup user [user...]
```

This table lists the syntax options for the `grpmod` command.

Table: Options for the grpmod command

| Option | Description |
| --- | --- |
| `--add` | Specifies to add users to the user group. |
| `--delete` | Specifies to delete users from the user group. |
| `diskgroup` | Name of the disk group to which the user group belongs. |
| `usergroup` | Name of the user group. |
| `user` | Name of the user to add or remove from the user group. |

Only the owner of the user group can use this command. The command requires the SYSASM privilege to run.

This command accepts an operating system user name or multiple user names separated by spaces. The operating system users are typically owners of a database instance home.

Examples

The following are examples of the `grpmod` command. The first example adds the `oracle1` and `oracle2` users to the `asm_fra` user group of the `fra` disk group. The second example removes the `oracle2` user from the `asm_data` user group of the `data` disk group.

Example: Using the ASMCMD grpmod command

```
ASMCMD [+] > grpmod --add fra asm_fra oracle1 oracle2

ASMCMD [+] > grpmod --delete data asm_data oracle2
```

### lsgrp

Purpose

Lists all Oracle ASM user groups or only groups that match a specified pattern.

Syntax and Description

```
lsgrp [--suppressheader][-a] [ -G diskgroup ] [ pattern ]
```

This table lists the syntax options for the `lsgrp` command.

Table: Options for the lsgrp command

| Option | Description |
| --- | --- |
| `--suppressheader` | Suppresses column headings. |
| `-a` | Lists all columns. |
| `-G` `diskgroup` | Limits the results to the specified disk group name. |
| `pattern` | Displays the user groups that match the pattern expression. |

Examples

The following are examples of the `lsgrp` command. The first example displays a subset of information about the user groups whose name matches the `asm%` pattern. The second example displays all information about all the user groups.

Example: Using the ASMCMD lsgrp command

```
ASMCMD [+] > lsgrp asm%
DG_Name  Grp_Name   Owner
FRA      asm_fra    grid
DATA     asm_data   grid

ASMCMD [+] > lsgrp -a
DG_Name  Grp_Name   Owner     Members
FRA      asm_fra    grid      oracle1
DATA     asm_data   grid      oracle1 oracle2
```

### lsusr

Purpose

Lists Oracle ASM users in a disk group.

Syntax and Description

```
lsusr [--suppressheader][-a] [-G diskgroup ] [ pattern ]
```

This table lists the syntax options for the `lsusr` command.

Table: Options for the lsusr command

| Option | Description |
| --- | --- |
| `-a` | List all users and the disk groups to which the users belong. |
| `--suppressheader` | Suppresses column headings. |
| `-G` `diskgroup` | Limits the results to the specified disk group name. |
| `pattern` | Displays the users that match the pattern expression. |

Examples

The following is an example of the `lsusr` command. The example lists users in the `data` disk group and also shows the operating system Id assigned to the user.

Example: Using the ASMCMD lsusr command

```
ASMCMD [+] > lsusr -G data
User_Num OS_ID OS_Name
3        1001  grid
1        1021  oracle1
2        1022  oracle2
```

### mkgrp

Purpose

Creates a new Oracle ASM user group.

Syntax and Description

```
mkgrp diskgroup usergroup [user] [user...]
```

This table lists the syntax options for the `mkgrp` command.

Table: Options for the mkgrp command

| Option | Description |
| --- | --- |
| `diskgroup` | Name of the disk group to which the user group is added. |
| `usergroup` | Name of the user group to add. 30 is the maximum number of characters. |
| `user` | Name of the database user to add to the user group. |

You can optionally specify a list of users to be included as members of the new user group.

Examples

The following is an example of the `mkgrp` command. This example creates the `asm_data` user group in the `data` disk group and adds the `oracle1` and `oracle2` users to the user group.

Example: Using the ASMCMD mkgrp command

```
ASMCMD [+] > mkgrp data asm_data oracle1 oracle2
```

### mkusr

Purpose

Adds an operating system (OS) user to a disk group.

Syntax and Description

```
mkusr diskgroup user
```

This table lists the syntax options for the `mkusr` command.

Table: Options for the mkusr command

| Option | Description |
| --- | --- |
| `diskgroup` | Specifies the name of the disk group to which the user is to be added. |
| `user` | Name of the user to add. |

The user to be added must be a valid operating system user. Only a user authenticated as `SYSASM` can run this command.

Examples

The following are examples of the `mkusr` command. The first example adds the `oracle1` user to the `data` disk group. The second example adds the `oracle2` user to the `fra` disk group.

Example: Using the ASMCMD mkusr command

```
ASMCMD [+] > mkusr data oracle1

ASMCMD [+] > mkusr fra oracle2
```

### passwd

Purpose

Changes the password of a user.

Syntax and Description

```
passwd user
```

This table lists the syntax options for the `passwd` command.

Table: Options for the passwd command

| Option | Description |
| --- | --- |
| `user` | Name of the user. |

An error is raised if the user does not exist in the Oracle ASM password file. The user is first prompted for the current password, then the new password. The command requires the SYSASM privilege to run.

Examples

The following is an example of the `passwd` command that changes the password of the `oracle2` user.

Example: Using the ASMCMD passwd command

```
ASMCMD [+] > passwd oracle2
Enter old password (optional):
Enter new password: ******
```

### rmgrp

Purpose

Removes a user group from a disk group.

Syntax and Description

```
rmgrp diskgroup usergroup
```

This table lists the syntax options for the `rmgrp` command.

Table: Options for the rmgrp command

| Option | Description |
| --- | --- |
| `diskgroup` | Name of the disk group to which the user group belongs. |
| `usergroup` | Name of the user group to delete. |

Removing a group might leave some files without a valid user group. To ensure that those files have a valid group, explicitly update those files to a valid user group. See " chgrp ".

The command must be run by the owner of the user group and also requires the SYSASM privilege to run.

Examples

The following is an example of the `rmgrp` command that removes the `asm_data` user group from the `data` disk group.

Example: Using the ASMCMD rmgrp command

```
ASMCMD [+] > rmgrp data asm_data
```

### rmusr

Purpose

Deletes an operating system (OS) user from a disk group.

Syntax and Description

```
rmusr [-r] diskgroup user
```

This table lists the syntax options for the `rmusr` command.

Table: Options for the rmusr command

| Option | Description |
| --- | --- |
| `-r` | Removes all files in the disk group that the user owns at the same time that the user is removed. |
| `diskgroup` | Specifies the name of the disk group from which the user is to be deleted. |
| `user` | Name of the user to delete. |

The command requires the SYSASM privilege to run.

Examples

The following is an example of the `rmusr` command that removes the `oracle2` user from the `data` disk group.

Example: Using the ASMCMD rmusr command

```
ASMCMD [+] > rmusr data oracle2
```

### rpusr

Purpose

Replaces one operating system (OS) user with another in a disk group.

Syntax and Description

```
rpusr diskgroup user1 user2
```

This table lists the syntax options for the `rpusr` command.

Table: Options for the rpusr command

| Option | Description |
| --- | --- |
| `diskgroup` | Specifies the name of the disk group. |
| `user1` | Name of the user to be replaced. |
| `user2` | Name of user that replaces the existing user in the disk group. |

The `rpusr` command replaces one operating system user with another in an Oracle ASM disk group. The replacement user must not be a user currently in the disk group user list.

If the command succeeds, all files that were previously owned by current user are now owned by the replacement user. The current user is automatically removed from the user list of the disk group. Adding the current user back to the disk group is possible but this user will not own any files.

When changing the ownership of an open file, the new owner cannot be dropped with the owner's files until all instances within a cluster are restarted.

The command requires the SYSASM privilege to run.

Examples

The following is an example of the `rpusr` command that replaces the `oracle1` user with the `oracle2` user in the `data` disk group.

Example: Using the ASMCMD rpusr command

```
ASMCMD [+] > rpusr data oracle1 oracle2
```

### afd\_deconfigure

Purpose

Deconfigures Oracle ASM Filter Driver.

Syntax and Description

```
# asmcmd afd_deconfigure [-f]
```

The following table lists the options for the `afd_deconfigure` command.

Table: Options for the afd\_deconfigure command

| Option | Description |
| --- | --- |
| `-f` | Force Oracle ASMFD deconfiguration. |

The `afd_deconfigure` command must be run noninteractively as a `root` user. Before running the command on a node, the Oracle Clusterware stack must be shut down on that node. After the `afd_deconfigure` command has been run, restart Oracle Clusterware on each node.

Example

The following example deconfigures Oracle ASM Filter Driver on the node on which the command was run. `$ORACLE_HOME` in the example refers to the Oracle Grid Infrastructure home.

Example: Using the afd\_deconfigure command

```
# $ORACLE_HOME/bin/asmcmd afd_deconfigure
```

See also

- [Administering Oracle ASM Filter Driver](administering-oracle-asm-filter-driver.md) for information about Oracle ASM Filter Driver
- [Oracle Grid Infrastructure Installation and Upgrade Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/ostmg&id=CWGEN) for your operating system for information about installing and configuring Oracle Grid Infrastructure

### afd\_di

Purpose

Manipulates the data integrity state in the Oracle ASM Filter Driver (Oracle ASMFD).

Syntax and Description

```
afd_di {-e | -d | -q}
```

The following table lists the options for the `afd_di` command.

Table: Options for the afd\_di command

| Option | Description |
| --- | --- |
| `-e` | Enables data integrity in Oracle ASMFD. |
| `-d` | Disables data integrity in Oracle ASMFD. |
| `-q` | Queries data integrity in Oracle ASMFD. |

For information about Oracle ASM Filter Driver, refer to " [Administering Oracle ASM Filter Driver](administering-oracle-asm-filter-driver.md) ".

Example

The following example shows the use of the `afd_di` command to enable data integrity in the Oracle ASMFD driver

Example: Using the ASMCMD afd\_di command

```
ASMCMD [+] > afd_di -e
```

### afd\_dsget

Purpose

Retrieves the Oracle ASM Filter Driver discovery diskstring value.

Syntax and Description

```
afd_dsget
```

For information about Oracle ASM Filter Driver, refer to [Administering Oracle ASM Filter Driver](administering-oracle-asm-filter-driver.md).

Example

The following example returns the current Oracle ASM Filter Driver discovery diskstring value.

Example: Using the afd\_dsget command

```
ASMCMD [+] > afd_dsget
AFD discovery string: /dev/rdsk/mydisks/*
```

### afd\_dsset

Purpose

Sets the Oracle ASM Filter Driver discovery diskstring value.

Syntax and Description

```
afd_dsset afd_diskstring
```

The syntax options for the `afd_dsset` command are described in this table.

Table: Options for the afd\_dsset command

| Option | Description |
| --- | --- |
| `afd_diskstring` | Specifies the value for the Oracle ASM Filter Driver discovery diskstring. |

For information about Oracle ASM Filter Driver, refer to [Administering Oracle ASM Filter Driver](administering-oracle-asm-filter-driver.md).

Example

The following example sets the current Oracle ASM Filter Driver discovery diskstring value.

Example: Using the afd\_dsset command

```
ASMCMD [+] > afd_dsset /dev/rdsk/mydisks/*
```

### afd\_filter

Purpose

Sets the Oracle ASM Filter Driver filtering mode on a given disk path.

Syntax and Description

```
afd_filter {-e | -d } [disk_path]
```

The syntax options for the `afd_filter` command are described in the following table.

Table: Options for the afd\_filter command

| Option | Description |
| --- | --- |
| `-e` | Enables Oracle ASM Filter Driver mode. |
| `-d` | Disables Oracle ASM Filter Driver mode. |
| `disk_path` | Specifies the path to the disks. |

If the command is executed without specifying a disk path, then filtering is set at the node level.

Example

The following example uses `afd_filter` to enable Oracle ASM Filter Driver filtering on a specified disk path.

Example: Using the afd\_filter command

```
ASMCMD [+] > afd_filter -e /dev/sdq
```

### afd\_label

Purpose

Sets an Oracle ASM Filter Driver (Oracle ASMFD) label to the specified disk.

Syntax and Description

```
afd_label afd_label disk_path [--migrate | --rename] [--init] [--force]
```

The syntax options for the `afd_label` command are described in this table.

Table: Options for the afd\_label command

| Option | Description |
| --- | --- |
| `afd_label` | Specifies an Oracle ASM Filter Driver label. |
| `disk_path` | Specifies the path to the disks to which the label is applied. |
| `--migrate` | Specifies to migrate Oracle ASM Filter Driver disk labels to all disks in the `disk_path`.. |
| `--rename` | Specifies to label a disk that was previously labeled. |
| `--init` | Specifies to set an Oracle ASMFD label during the initialize stage. This option is not allowed if Oracle ASMFD is already loaded. |
| `--force` | Causes the `afd_label` command to execute all steps. |

For information about Oracle ASM Filter Driver, refer to " [Administering Oracle ASM Filter Driver](administering-oracle-asm-filter-driver.md) ".

Example

The following example sets an Oracle ASM Filter Driver label to a specified disk.

Example: Using the afd\_label command

```
ASMCMD [+] > afd_label 'disk0' '/dev/rdsk/mydisks/disk0'
```

### afd\_lsdsk

Purpose

Lists Oracle ASM Filter Driver disks.

Syntax and Description

```
afd_lsdsk [--all]
```

The following table lists the options for the `afd_lsdsk` command.

Table: Options for the afd\_lsdsk command

| Option | Description |
| --- | --- |
| `--all` | Lists all Oracle ASMFD disks clusterwide. |

Example

The following example lists Oracle ASM Filter Driver disks.

Example: Using the afd\_lsdsk commmand

```
ASMCMD [+] > afd_lsdsk
--------------------------------------------------------------------------------
Label                     Filtering   Path
================================================================================
DISK0                       ENABLED   /dev/sdd
DISK1                      DISABLED   /dev/sdm
DISK2                       ENABLED   /dev/sdq
```

### afd\_lslbl

Purpose

Scans operating system disks using the specified discovery string and lists the disks that contain Oracle ASM Filter Driver labels.

Syntax and Description

```
afd_lslbl [disk_string]
```

The following table lists the options for the `afd_lslbl` command.

Table: Options for the afd\_lslbl command

| Option | Description |
| --- | --- |
| `disk_string` | Specifies an optional disk path string for filtering. |

For information about Oracle ASM Filter Driver, refer to " [Administering Oracle ASM Filter Driver](administering-oracle-asm-filter-driver.md) ".

Example

The following example shows the use of the `afd_lslbl` command to list disks that contain Oracle ASMFD labels.

Example: Using the ASMCMD afd\_lslbl command

```
ASMCMD [+]> afd_lslbl '/dev/sd*'

Label                 Duplicate  Path
=======================================
DISK0                 /dev/sdd
DISK1                 /dev/sdm
```

### afd\_refresh

Purpose

Refreshes Oracle ASM Filter Driver disks using the AFD discovery string.

Syntax and Description

```
afd_refresh [--all]
```

The following table lists the options for the `afd_refresh` command.

Table: Options for the afd\_refresh command

| Option | Description |
| --- | --- |
| `--all` | Specifies a clusterwide refresh. |

If the Oracle ASM Filter Driver disks are owned by the `root` user, then you must run `afd_refresh` `--all` as `root` to ensure that accurate disk sizes are displayed in the `V$ASM_DISK` view.

For information about Oracle ASM Filter Driver, refer to [Administering Oracle ASM Filter Driver](administering-oracle-asm-filter-driver.md).

Example

The following example uses `afd_refresh` to refresh Oracle ASMFD disks

Example: Using the ASMCMD afd\_refresh command

```
ASMCMD [+]> afd_refresh
```

### afd\_scan

Purpose

Scans for Oracle ASM Filter Driver disks.

Syntax and Description

```
afd_scan [afd_diskstring] [--all]
```

The syntax options for the `afd_scan` command are described in this table.

Table: Options for the afd\_scan command

| Option | Description |
| --- | --- |
| `afd_diskstring` | Specifies the value for the Oracle ASM Filter Driver discovery diskstring. |
| `--all` | Specifies a clusterwide scan for Oracle ASMFD disks. |

`afd_scan` scans for Oracle ASM Filter Driver disks using the specified discovery string. If the command is executed without specifying a disk string, then `afd_scan` uses the Oracle ASM Filter Driver discovery diskstring value in the `afd.conf` file.

For information about Oracle ASM Filter Driver, refer to [Administering Oracle ASM Filter Driver](administering-oracle-asm-filter-driver.md).

Example

The following example scans for Oracle ASM Filter Driver disks with a specified diskstring.

Example: Using the afd\_scan command

```
ASMCMD [+] > afd_scan /dev/sd*
```

### afd\_state

Purpose

Returns the state of Oracle ASM Filter Driver.

Syntax and Description

```
afd_state [--all]
```

This table lists the options for the `afd_state` command.

Table: Options for the afd\_state command

| Option | Description |
| --- | --- |
| `--all` | The `--all` option runs a clusterwide check. |

For information about Oracle ASM Filter Driver, refer to [Administering Oracle ASM Filter Driver](administering-oracle-asm-filter-driver.md).

Example

The following example returns the current state of Oracle ASM Filter Driver.

Example: Using the afd\_state command

```
ASMCMD [+] > afd_state
ASMCMD-9526: The AFD state is 'LOADED' and filtering is 'DEFAULT' on host 'myhost'
```

### afd\_unlabel

Purpose

Clears a specified Oracle ASM filter driver (Oracle ASMFD) label.

Syntax and Description

```
afd_unlabel afd_label {afd_label | 'disk_path'} [-f] [--init]
```

The syntax options for the `afd_unlabel` command are described in this table.

Table: Options for the afd\_unlabel command

| Option | Description |
| --- | --- |
| `afd_unlabel` | Specifies an existing Oracle ASM Filter Driver label to clear. |
| `'` `disk_path` `'` | Specifies to clear a label determined by an existing disk path. If a disk needs to be unlabeled during the initialization stage, then it can be done only by using its disk path. |
| `-f` | Forces the clearing of the label if the disk is an Oracle ASM member disk and there are no pending opens of the disk. |
| `--init` | Specifies to clear an Oracle ASMFD label during the initialize stage. This option is not allowed if Oracle ASMFD is already loaded. |

For information about Oracle ASM Filter Driver, refer to " [Administering Oracle ASM Filter Driver](administering-oracle-asm-filter-driver.md) ".

Example

The following example clears an existing Oracle ASM Filter Driver label.

Example: Using the afd\_unlabel command

```
ASMCMD [+] > afd_unlabel 'disk0'
```