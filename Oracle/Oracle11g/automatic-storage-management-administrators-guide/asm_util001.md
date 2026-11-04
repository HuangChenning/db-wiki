---
title: About ASMCMD
book: "Automatic Storage Management Administrator's Guide"
doc_id: E18951-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e18951/asm_util001.htm
tags:
  - oracle
  - 11g
  - automatic-storage-management-administrators-guide
---

ASMCMD is a command-line utility that you can use to manage Oracle ASM instances, disk groups, file access control for disk groups, files and directories within disk groups, templates for disk groups, and volumes.

You can run the ASMCMD utility in either interactive or noninteractive mode.

This section contains the following topics:

## Types of ASMCMD Commands

The types of ASMCMD commands are listed in Table 12-1.

Table 12-1 Types of ASMCMD commands

| Category | Commands |
| --- | --- |
| [ASMCMD Instance Management Commands](asm_util002.md) | [dsget](asm_util002.md), [dsset](asm_util002.md), [lsct](asm_util002.md), [lsop](asm_util002.md), [lspwusr](asm_util002.md), [orapwusr](asm_util002.md), [shutdown](asm_util002.md), [spbackup](asm_util002.md), [spcopy](asm_util002.md), [spget](asm_util002.md), [spmove](asm_util002.md), [spset](asm_util002.md), [startup](asm_util002.md) |
| [ASMCMD File Management Commands](asm_util003.md) | [cd](asm_util003.md), [cp](asm_util003.md), [du](asm_util003.md), [find](asm_util003.md), [ls](asm_util003.md), [lsof](asm_util003.md), [mkalias](asm_util003.md), [pwd](asm_util003.md), [rm](asm_util003.md), [rmalias](asm_util003.md) |
| [ASMCMD Disk Group Management Commands](asm_util004.md) | [chdg](asm_util004.md), [chkdg](asm_util004.md), [dropdg](asm_util004.md), [iostat](asm_util004.md), [lsattr](asm_util004.md), [lsdg](asm_util004.md), [lsdsk](asm_util004.md), [lsod](asm_util004.md), [md\_backup](asm_util004.md), [md\_restore](asm_util004.md), [mkdg](asm_util004.md), [mount](asm_util004.md), [offline](asm_util004.md), [online](asm_util004.md), [rebal](asm_util004.md), [remap](asm_util004.md), [setattr](asm_util004.md), [umount](asm_util004.md) |
| [ASMCMD Template Management Commands](asm_util005.md) | [chtmpl](asm_util005.md), [lstmpl](asm_util005.md), [mktmpl](asm_util005.md), [rmtmpl](asm_util005.md) |
| [ASMCMD File Access Control Commands](asm_util006.md) | [chgrp](asm_util006.md), [chmod](asm_util006.md), [chown](asm_util006.md), [groups](asm_util006.md), [grpmod](asm_util006.md), [lsgrp](asm_util006.md), [lsusr](asm_util006.md), [mkgrp](asm_util006.md), [mkusr](asm_util006.md), [passwd](asm_util006.md), [rmgrp](asm_util006.md), [rmusr](asm_util006.md) |
| [ASMCMD Volume Management Commands](asm_util007.md) | [volcreate](asm_util007.md), [voldelete](asm_util007.md), [voldisable](asm_util007.md), [volenable](asm_util007.md), [volinfo](asm_util007.md), [volresize](asm_util007.md), [volset](asm_util007.md), [volstat](asm_util007.md) |

## About Oracle ASM Files, Filenames, Directories, and Aliases

ASMCMD works with Oracle ASM files, directories, and aliases. Before using ASMCMD, you should understand how these common computing concepts apply to the Oracle ASM environment.

This section contains the following topics about some key definitions:

- System-Generated Filename or Fully Qualified Filename
- Directory
- Alias
- Absolute Path and Relative Path
- Wildcard Characters

### System-Generated Filename or Fully Qualified Filename

Every file created in Oracle ASM gets a system-generated filename, otherwise known as a fully qualified filename. This is similar to a complete path name in a local file system.

Oracle ASM generates filenames according to the following scheme:

```
+diskGroupName/databaseName/fileType/fileTypeTag.fileNumber.incarnation
```

An example of a fully qualified filename is the following:

`+data/orcl/CONTROLFILE/Current.256.541956473`

In the previous fully qualified filename, `data` is the disk group name, `orcl` is the database name, `CONTROLFILE` is the file type, and so on.

Only the slash (/) is supported by ASMCMD. Filenames are not case sensitive, but are case retentive. If you type a path name as lowercase, ASMCMD retains the lowercase.

For more information about Oracle ASM filenames, refer to ["Fully Qualified File Name Form"](asmfiles.md).

### Directory

As in other file systems, an Oracle ASM directory is a container for files, and an Oracle ASM directory can be part of a tree structure of other directories. The fully qualified filename represents a hierarchy of directories in which the plus sign (+) represents the root directory. In each disk group, Oracle ASM automatically creates a directory hierarchy that corresponds to the structure of the fully qualified filenames in the disk group. The directories in this hierarchy are known as system-generated directories.

ASMCMD enables you to move up and down in this directory hierarchy with the `cd` (change directory) command. The ASMCMD `ls` (list directory) command lists the contents of the current directory, while the `pwd` command prints the name of the current directory.

When you start ASMCMD, the current directory is set to root (+). For an Oracle ASM instance with two disk groups, for example, `data` and `fra`, entering an `ls` command with the root directory as the current directory produces the following output:

  
`ASMCMD> ls`  
`data/`  
`fra/`  

The following example demonstrates navigating the Oracle ASM directory tree (refer to the fully qualified filename shown previously):

  
`ASMCMD> cd +data/orcl/CONTROLFILE`  
`ASMCMD> ls`  
`Current.256.541956473`  
`Current.257.541956475`  

You can create your own directories as subdirectories of the system-generated directories using the ASMCMD `mkdir` command. The directories that you create can have subdirectories, and you can navigate the hierarchy of both system-generated directories and user-created directories with the `cd` command.

The following example creates the directory `mydir` under `orcl` in the disk group `data`:

`ASMCMD> mkdir +data/orcl/mydir`

Note:

The directory `orcl` is a system-generated directory. The contents of `data` represent the contents of disk group `data`.

If you start ASMCMD with the `-p` flag, then ASMCMD shows the current directory as part of its prompt. See "Including the Current Directory in the ASMCMD Prompt".

  
`ASMCMD [+] > cd data/orcl`  
`ASMCMD [+data/orcl] >`  

ASMCMD retains the case of the directory that you entered.

### Alias

Aliases are filenames that are references or pointers to system-generated filenames. However, aliases are user-friendly names. Aliases are similar to symbolic links in UNIX or Linux computers. You can create aliases to simplify Oracle ASM filename administration. You can create aliases with the `mkalias` ASMCMD command or a SQL `ALTER` `DISKGROUP` command.

An alias has at a minimum the disk group name as part of its complete path. You can create aliases at the disk group level or in any system-generated or user-created subdirectory. The following are examples of aliases:

  
`+data/ctl1.f`  
`+data/orcl/ctl1.f`  
`+data/mydir/ctl1.f`  

If you run the ASMCMD `ls` (list directory) with the `-l` flag, each alias is listed with the system-generated file to which the alias refers.

`ctl1.f => +data/orcl/CONTROLFILE/Current.256.541956473`

For more information about aliases, refer to ["Alias Oracle ASM Filename Forms"](asmfiles.md).

### Absolute Path and Relative Path

When you run an ASMCMD command that accepts a filename or directory name as an argument, you can use the name as either an absolute path or a relative path.

An absolute path refers to the full path of a file or directory. An absolute path begins with a plus sign (+) followed by a disk group name, followed by subsequent directories in the directory tree. The absolute path includes directories until the file or directory of interest is reached. A complete system-generated filename, otherwise known as the fully qualified filename, is an example of an absolute path to a file.

Using an absolute path enables the command to access the file or directory regardless of where the current directory is set. The following `rm` command uses an absolute path for the filename:

`ASMCMD [+] > rm` `+data/orcl/datafile/users.259.555341963`

The following `cd` command uses an absolute path to the directory.

`ASMCMD [+data/mydir] > cd +data/orcl/CONTROLFILE`

A relative path includes only the part of the filename or directory name that is not part of the current directory. That is, the path to the file or directory is relative to the current directory.

In the following example, the `rm` command operates on the file `undotbs1.272.557429239`, which in this case is a relative path. ASMCMD appends the current directory to the command argument to obtain the absolute path to the file. In this example this is `+data/orcl/DATAFILE/undotbs1.272.557429239`.

  
`ASMCMD [+] > cd +data`  
`ASMCMD [+data] > cd orcl/DATAFILE`  
`ASMCMD [+data/orcl/DATAFILE] > ls`  
`EXAMPLE.269.555342243`  
`SYSAUX.257.555341961`  
`SYSTEM.256.555341961`  
`UNDOTBS1.258.555341963`  
`UNDOTBS1.272.557429239`  
`USERS.259.555341963`  
`ASMCMD [+data/orcl/DATAFILE] >` `rm undotbs1.272.557429239`  

Paths to directories can also be relative. You can go up or down the hierarchy of the current directory tree branch by providing a directory argument to the `cd` command whose path is relative to the current directory.

In addition, you can use the pseudo-directories "`.`" and "`..`" rather than a directory name. The "`.`" pseudo-directory is the current directory. The "`..`" pseudo-directory is the parent directory of the current directory.

The following example demonstrates how to use relative directory paths and pseudo-directories:

  
`ASMCMD [+data/orcl] > cd DATAFILE`  
`ASMCMD [+data/orcl/DATAFILE] >cd ..`  
`ASMCMD [+data/orcl] >`

### Wildcard Characters

The wildcard characters `*` and `%` match zero or more characters anywhere within an absolute or relative path, which saves typing of the full directory or file name. The two wildcard characters behave identically. There are various ASMCMD commands that accept wildcards. These include `cd`, `du`, `find`, `ls`, `lsattr`, `lsdg`, `lsdsk`, `lsgrp`, `lsusr`, and `rm`.

If a wildcard pattern matches only one directory when using wildcard characters with `cd`, then `cd` changes the directory to that destination. If the wildcard pattern matches multiple directories, then ASMCMD does not change the directory but instead returns an error.

Example 12-1 illustrates the use of wildcards.

Example 12-1 Using wildcards with ASMCMD commands

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

## Preparing to Run ASMCMD

You can run the ASMCMD utility in either interactive or noninteractive mode.

Before running ASMCMD, review the items in the following list.

- Log in to the host which contains the Oracle ASM instance that you plan to administer.
	You must log in as a user that has SYSASM or SYSDBA privileges through operating system authentication. The SYSASM privilege is the required connection to administer the Oracle ASM instance. See ["Authentication for Accessing Oracle ASM Instances"](asminst.md).
	See Also:
	Refer to the [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/dba.htm#ADMIN11010) for information about operating system authentication
- To connect to the Oracle ASM instance, run ASMCMD that is located in the `bin` subdirectory of the Oracle Grid Infrastructure home (Oracle ASM home).
	Connect as SYSASM, the default connection, to administer an Oracle ASM instance.
	Ensure that the `ORACLE_HOME` and `ORACLE_SID` environment variables to refer to the Oracle ASM instance. Depending on your operating system, you might have to set other environment variables to properly connect to the Oracle ASM instance.
	Ensure that the `bin` subdirectory of your Oracle Grid Infrastructure home is in your `PATH` environment variable.
	See Also:
	Refer to the [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/dba.htm#ADMIN00102) for more information about setting environment variables
	The default value of the Oracle ASM SID for a single-instance database is `+ASM`. In Oracle Real Application Clusters environments, the default value of the Oracle ASM SID on any node is `+ASM` `node#`.
- To use most of the ASMCMD commands, ensure that the Oracle ASM instance is started and the Oracle ASM disk groups are mounted.
	If the Oracle ASM instance is not running, ASMCMD runs only those commands that do not require an Oracle ASM instance. The commands include `startup`, `shutdown`, `lsdsk`, `help`, and `exit`. If you attempt to run other ASMCMD commands, an error message displays.
- You can connect to the database instance as SYSDBA by running ASMCMD that is located in the `bin` directory of the Oracle Database home.
	Ensure that the `ORACLE_HOME` and `ORACLE_SID` environment variables to refer to the database instance. Depending on your operating system, you might have to set other environment variables to properly connect to the database instance.
	You must include the `--privilege` option to connect as SYSDBA. See "Specifying the Type of Connection".
	With this connection, there is a limited set of operations that can be run. For more information, see ["The SYSDBA Privilege for Managing Oracle ASM Components"](asminst.md).
	When administering disk groups, Oracle recommends that you run ASMCMD from the database home of the database instance that is the owner of the files in the disk group.

## Running ASMCMD in Interactive Mode

The interactive mode of the ASMCMD utility provides a shell-like environment where you are prompted to enter ASMCMD commands. The syntax for starting ASMCMD in interactive mode is:

  
`asmcmd` \[`-V`\]  
`asmcmd` \[`-v` { `errors` | `warnings` | `normal` | `info` | `debug` }\]  
 \[ `--privilege` `connection_type` \] \[`-p`\]  

Table 12-2 summarizes the ASMCMD options.

Table 12-2 ASMCMD interactive options

| Option | Description |
| --- | --- |
| \- `V` | Displays the version of ASMCMD and then exits. |
| `-v` `display_level` | Displays additional information with some commands to help users diagnose problems and writes to a message file when logging is required. `normal` is the default if the display level is not specified. |
| `--privilege` `connection_type` | Specifies the privilege to connect as when accessing an Oracle ASM or database instance. Can be either `SYSASM` or `SYSDBA`. The default is `SYSASM` and is used when administering the Oracle ASM instance. |
| `-p` | Displays the current directory in the prompt. |

ASMCMD can be started with multiple options. For example:

  
`asmcmd` `-p` `-v` `info`  

For the majority of the examples in this chapter, ASMCMD was started with the `-p` option.

### Running ASMCMD without Any Options

To run ASMCMD in interactive mode without any options:

1. Enter the following at the operating system command prompt:
	`asmcmd`
	Oracle displays an ASMCMD command prompt as follows:
	`ASMCMD>`
2. Enter an ASMCMD command and press `Enter`. The command runs and displays its output, if any, and then ASMCMD prompts for the next command.
3. Continue entering ASMCMD commands until you have completed the tasks.
4. Enter the `exit` or `quit` command to exit ASMCMD.

### Specifying the Type of Connection

You can specify the `--privilege` option to choose the type of connection, either `SYSASM` or `SYSDBA`. The default value is `SYSASM` and is used when administering an Oracle ASM instance. Connect as `SYSDBA` when connecting to the database instance.

For example:

`$ asmcmd --privilege sysasm`

### Specifying the Verbose Mode

You can specify the `-v` option with the `asmcmd` command to display additional information with some commands to help users diagnose problems as shown in the following example:

  
`$ asmcmd -v` `debug`  

When there is a message that must be logged during `asmcmd` operations, the message is written to the `alert.log` file or the `trace.trc` file.

The `alert.log` file is created or updated when `asmcmd` is started with the `-v` `errors`, `-v` `warning`, or `-v` `normal` display level. The `trace.trc` file is created or updated when `asmcmd` is started with the `-v` `info` or `-v` `debug` display level.

By default, the `alert.log` is file created in the `$ORACLE_HOME/log/diag/asmcmd/user_` `username` `/` `hostname` `/alert/` directory. By default, the `trace.trc` file is created in the `$ORACLE_HOME/log/diag/asmcmd/user_` `username` `/` `hostname` `/trace/` directory.

Under certain circumstances, `$ORACLE_BASE` and `$ORACLE_HOME` can be set to override the default locations of the `alert.log` and `trace.trc` files.

### Including the Current Directory in the ASMCMD Prompt

You can specify the `-p` option with the `asmcmd` command to include the current directory in the ASMCMD prompt as shown in the following example:

  
`$ asmcmd -p`  
`ASMCMD [+] > cd data`  
`ASMCMD [+data] >`

### Displaying the ASMCMD Version Number

You can specify the `-V` option when starting `asmcmd` to display the `asmcmd` version number. After displaying the version number, `asmcmd` immediately exits.

For example:

  
`$ asmcmd -V`  
`asmcmd version 11.2.0.3.0`  
`$`

## Running ASMCMD in Noninteractive Mode

In noninteractive mode, you run a single ASMCMD command by including the command and command options on the command line when invoking ASMCMD. ASMCMD runs the command, generates output if any, and then exits. The noninteractive mode is especially useful for running scripts.

To run ASMCMD in noninteractive mode where `command` is any valid ASMCMD command and `options` is a list of command options, at the command prompt enter the following:

`asmcmd` `command` `options`

In noninteractive mode, ASMCMD returns the codes listed in Table 12-3.

Table 12-3 ASMCMD return codes

| Type | Return Code | Description |
| --- | --- | --- |
| General | 0 | No issues for the command. |
| General | 1 | Internal error. |
| General | 255 or -1 | External user error as returned by a command. |
| `lsdsk` | 0 | Results include member disks only. |
| `lsdsk` | 1 | Results include candidate disks only. |
| `lsdsk` | 2 | Results include both member and candidate disks. |

Example 12-2 shows how to run ASMCMD in the noninteractive mode. The first example runs the `ls` command to list the disk groups for the Oracle ASM instance. The second example redirects the output of the `lsod` command to the `my_lsod_test` file. The third example runs `lsdsk` using a pattern with a wildcard character to list specific disks in the `data` disk group.

Example 12-2 Running ASMCMD commands in noninteractive mode

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

Example 12-3 raises an error with an incorrect disk group name and the return code equal (255) is displayed.

Example 12-3 Displaying a return code when running ASMCMD in noninteractive mode

```
$ asmcmd ls -l dat
ASMCMD-08001: diskgroup 'dat' does not exist or is not mounted

$ echo $?
255
```

Example 12-4 shows an example of ASMCMD commands run in noninteractive mode inside a script.

Example 12-4 Running ASMCMD commands in a script

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

## Getting Help

Type `help` at the ASMCMD prompt or as a command in noninteractive mode to view general information about ASMCMD and a list of available ASMCMD commands.

You can type `help` `command` to display help text for a specific command, including usage information about how to run the command with its options.

The following is an example of the use of the `help` command.

Example 12-5 Displaying ASMCMD help text

```
ASMCMD [+] > help startup
        startup [--nomount] [--restrict] [--pfile <pfile.ora>]
 
        Start the ASM instance.
 
        [--nomount]           specifies the nomount option.
        [--restrict]          start the instance in restricted mode.
        [--pfile <pfile.ora>] specifies the location of the pfile.
```