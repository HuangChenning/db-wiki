---
title: "Starting and Interacting with the RMAN Client"
book: "Backup and Recovery User's Guide"
doc_id: E10642-08
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/backup.112/e10642/rcmcnctg.htm
tags:
  - oracle
  - 11g
  - backup-and-recovery-users-guide
---

## 4 Starting and Interacting with the RMAN Client

This chapter explains how to start the RMAN command-line interface and make database connections. This chapter contains the following topics:

## Starting and Exiting RMAN

The RMAN executable is automatically installed with the database and is typically located in the same directory as the other database executables. For example, the RMAN client on Linux is located in `$ORACLE_HOME/bin`. You have the following basic options for starting RMAN:

- Start the RMAN executable at the operating system command line without specifying any connection options, as in the following example:
	```
	% rman
	```
- Start the RMAN executable at the operating system command line while connecting to a [target database](glossary.md) and, possibly, to a [recovery catalog](glossary.md), as in the following examples:
	```
	% rman TARGET /                       # operating system authentication
	% rman TARGET SYS@prod NOCATALOG      # RMAN prompts for SYS password
	% rman TARGET / CATALOG rco@catdb     # RMAN prompts for rco password
	```

Note:

Most RMAN commands require that RMAN connect to at least a target database to perform useful work. See "Making Database Connections with RMAN" for more details about connecting RMAN to different types of databases.

To quit RMAN and terminate the program, enter `EXIT` or `QUIT` at the RMAN prompt:

```
RMAN> EXIT
```

See Also:

[Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta2011.htm#RCMRF111) for RMAN command-line syntax

## Specifying the Location of RMAN Output

By default, RMAN writes command output to standard output. To redirect output to a log file, enter the `LOG` parameter on the command line when starting RMAN, as in the following example:

```
% rman LOG /tmp/rman.log
```

In this case, RMAN displays command input but does not display the RMAN output. The easiest way to send RMAN output both to a log file and to standard output is to use the Linux `tee` command or its equivalent. For example, the following technique enables both input and output to be visible in the RMAN command-line interface:

```
% rman | tee rman.log
RMAN>
```

See Also:

[Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta2011.htm#RCMRF111) to learn about RMAN command-line options

## Setting Globalization Support Environment Variables for RMAN

Before invoking RMAN, it may be useful to set the `NLS_DATE_FORMAT` and `NLS_LANG` environment variables. These variables determine the format used for the time parameters in RMAN commands such as [`RESTORE`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta2008.htm#RCMRF149), [`RECOVER`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta2001.htm#RCMRF140), and [`REPORT`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta2006.htm#RCMRF147).

The following example shows typical language and date format settings:

```
NLS_LANG=american
NLS_DATE_FORMAT='Mon DD YYYY HH24:MI:SS'
```

If you are going to use RMAN to connect to an unmounted database and mount the database later while RMAN is still connected, then set the `NLS_LANG` environment variable so that it also specifies the character set used by the database.

A database that is not mounted assumes the default character set, which is `US7ASCII`. If your character set is different from the default, then RMAN returns errors after the database is mounted. For example, if the character set is `WE8DEC`, then to avoid errors, you can set the `NLS_LANG` variable as follows:

```
NLS_LANG=american_america.we8dec
```

In order for the environment variable [`NLS_DATE_FORMAT`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams147.htm#REFRN10119) to be applied and override the defaults set for the server in the server initialization file, the environment variable `NLS_LANG` must also be set.

See Also:

- [Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/toc.htm) for more information about the `NLS_LANG` and `NLS_DATE_FORMAT` parameters
- [Oracle Database Globalization Support Guide](https://docs.oracle.com/cd/E11882_01/server.112/e10729/toc.htm)

## Entering RMAN Commands

You can enter RMAN commands either directly from the RMAN prompt or read them in from a text file.

This section contains the following topics:

- Entering RMAN Commands at the RMAN Prompt
- Using Command Files with RMAN
- Entering Comments in RMAN Command Files
- Using Substitution Variables in Command Files
- Checking RMAN Syntax

### Entering RMAN Commands at the RMAN Prompt

When the RMAN client is ready for your commands, it displays the command prompt, as in this example:

```
RMAN>
```

Enter commands for RMAN to execute. For example:

```
RMAN> CONNECT TARGET
RMAN> BACKUP DATABASE;
```

Most RMAN commands take some parameters and must end with a semicolon. Some commands, such as [`STARTUP`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta2019.htm#RCMRF158), [`SHUTDOWN`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta2016.htm#RCMRF155), and [`CONNECT`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta011.htm#RCMRF114), can be used with or without a semicolon.

When you enter a line of text that is not a complete command, RMAN prompts for continuation input with a line number. For example:

```
RMAN> BACKUP DATABASE
2> INCLUDE CURRENT 
3> CONTROLFILE
4> ;
```

### Using Command Files with RMAN

For repetitive tasks, you can create a text file containing RMAN commands, and start the RMAN client with the `@` argument, followed by a file name. For example, create a text file `cmdfile1` in the current directory containing one line of text as shown here:

```
BACKUP DATABASE PLUS ARCHIVELOG;
```

You can run this command file from the command line as shown in this example, and the command contained in it is executed:

```
% rman TARGET / @cmdfile1
```

After the command completes, RMAN exits.

You can also use the [`@`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta001.htm#RCMRF100) command at the RMAN command prompt to execute the contents of a command file during an [RMAN session](glossary.md). RMAN reads the file and executes the commands in it. For example:

```
RMAN> @cmdfile1
```

After the command file contents have been executed, RMAN displays the following message:

```
RMAN>  **end-of-file**
```

Unlike the case where a command file is executed from the operating system command line, RMAN does not exit.

See Also:

[Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta2011.htm#RCMRF111) for RMAN command-line syntax

### Entering Comments in RMAN Command Files

The comment character in RMAN is a pound sign (`#`). All text from the pound sign to the end of the line is ignored. For example, the following command file contents backs up the database and archived redo log files and includes comments:

```
# Command file name: mybackup.rman
# The following command backs up the database
BACKUP DATABASE;
# The following command backs up the archived redo logs
BACKUP ARCHIVELOG ALL;
```

The following example shows that you can break a single RMAN command across multiple lines:

```
RMAN> BACKUP # this is a comment
2> SPFILE;

Starting backup at 30-APR-07
allocated channel: ORA_DISK_1
     .
     .
     .
```

### Using Substitution Variables in Command Files

When running a command file, you can specify one or more values in a `USING` clause for use in substitution variables in a command file. In this way, you can make your command files dynamic.

As in SQL\*Plus, `&1` indicates where to place the first value, `&2` where to place the second value, and so on. The substitution variable syntax is `&` `integer` followed by an optional period, for example, `&1.3`. The optional period is part of the variable and replaced with the value, thus enabling the substitution text to be immediately followed by another integer. For example, if you pass the value `mybackup` to a command file containing the variable `&1.3`, then the result of the substitution is `mybackup3`.

The following procedure explains how to create and use a dynamic shell script that calls a command file containing substitution variables.

To create and use a dynamic shell script:

1. Create an RMAN command file that uses substitution variables.
	The following example shows the contents of a command file named `quarterly_backup.cmd`, which is run every quarter. The script uses substitution variables for the name of the tape set, for a string in the `FORMAT` specification, and for the name of the restore point to be created.
	```
	# quarterly_backup.cmd
	CONNECT TARGET /
	RUN
	{
	  ALLOCATE CHANNEL c1
	    DEVICE TYPE sbt
	    PARMS 'ENV=(OB_MEDIA_FAMILY=&1)';
	  BACKUP DATABASE 
	    TAG &2 
	    FORMAT '/disk2/bck/&1%U.bck'
	    KEEP FOREVER 
	    RESTORE POINT &3;
	}
	EXIT;
	```
2. Create a shell script that you can use to run the RMAN command file created in the previous step.
	The following example creates a shell script named `runbackup.sh`. The example creates shell variables for the format and restore point name and accepts the values for these variables as command-line arguments to the script.
	```
	#!/bin/tcsh
	# name: runbackup.sh
	# usage: use the tag name and number of copies as arguments
	set media_family = $argv[1]
	set format = $argv[2]set restore_point = $argv[3]
	rman @'/disk1/scripts/whole_db.cmd' USING $media_family $format $restore_point
	```
3. Execute the shell script created in the previous step, specifying the desired arguments on the command line.
	The following example runs the `runbackup.sh` shell script and passes it `archival_backup` as the media family name, `bck0906` as the format string, and `FY06Q3` as the restore point name.
	```
	% runbackup.sh archival_backup bck0906 FY06Q3
	```

See Also:

[Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta001.htm#RCMRF100) for `@` syntax

### Checking RMAN Syntax

You may want to test RMAN commands for syntactic correctness without executing them. Use the command-line argument `CHECKSYNTAX` to start the RMAN client in a mode in which it only parses the commands that you enter and returns an `RMAN-00558` error for commands that are not legal RMAN syntax.

See Also:

[Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta2011.htm#RCMRF111) to learn about the `CHECKSYNTAX` command-line option

#### Checking RMAN Syntax at the Command Line

You can check the syntax of RMAN commands interactively without actually executing the commands.

To check RMAN syntax at the command line:

1. Start RMAN with the `CHECKSYNTAX` parameter.
	For example, enter the following commands:
	```
	% rman CHECKSYNTAX
	```
2. Enter the RMAN commands to be tested.
	The following shows a sample interactive session, with user-entered text in bold.
	```
	RMAN> run [ backup database; ]
	 
	RMAN-00571: ===========================================================
	RMAN-00569: =============== ERROR MESSAGE STACK FOLLOWS ===============
	RMAN-00571: ===========================================================
	RMAN-00558: error encountered while parsing input commands
	RMAN-01006: error signaled during parse 
	 RMAN-02001: unrecognized punctuation symbol "["
	 
	RMAN> run { backup database; }
	The command has no syntax errors
	RMAN>
	```

#### Checking RMAN Syntax in Command Files

To test commands in a command file, start RMAN with the `CHECKSYNTAX` parameter and use the [`@`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta001.htm#RCMRF100) command to name the command file to be passed.

To test commands in a command file:

1. Use a text editor to create a command file.
	Assume that you create the `/tmp/goodcmdfile` with the following contents:
	```
	# command file with legal syntax
	RESTORE DATABASE; 
	RECOVER DATABASE;
	```
	Assume that you create another command file, `/tmp/badcmdfile`, with the following contents:
	```
	# command file with bad syntax commands
	RESTORE DATABASE
	RECOVER DATABASE
	```
2. Run the command file from the RMAN prompt in the following format, where `filename` is the name of the command file:
	```
	% rman CHECKSYNTAX @filename
	```
	The following example shows the output when you run `/tmp/goodcmdfile` with `CHECKSYNTAX`:
	```
	RMAN> # command file with legal syntax
	2> restore database;
	3> recover database;
	4>
	The cmdfile has no syntax errors
	 
	Recovery Manager complete.
	```
	In contrast, the following example shows the output when you run `/tmp/badcmdfile` with `CHECKSYNTAX`:
	```
	RMAN> #command file with syntax error
	2> restore database
	3> recover
	RMAN-00571: ===========================================================
	RMAN-00569: =============== ERROR MESSAGE STACK FOLLOWS===============
	RMAN-00571: ===========================================================
	RMAN-00558: error encountered while parsing input commands
	RMAN-01005: syntax error: found "recover": expecting one of: "archivelog, 
	      channel, check, controlfile, clone, database, datafile, device, 
	      from, force, high, (, preview, ;, skip, spfile, standby, tablespace, 
	      until, validate"
	RMAN-01007: at line 3 column 1 file: /tmp/badcmdfile
	```

As explained in "Using Substitution Variables in Command Files", you make your command files dynamic by including substitution variables. When you check the syntax of a command file that contains substitution variables, RMAN prompts you to enter values. Example 4-1 illustrates what happens you enter invalid values when checking the syntax of a dynamic command file. The text in bold indicates text entered as the prompt.

Example 4-1 Checking the Syntax of a Command File with Bad Syntax

```
RMAN> CONNECT TARGET *
2> BACKUP TAG 
Enter value for 1: mybackup
abc COPIES 
Enter value for 2: mybackup
abc
RMAN-00571: ===========================================================
RMAN-00569: =============== ERROR MESSAGE STACK FOLLOWS ===============
RMAN-00571: ===========================================================
RMAN-00558: error encountered while parsing input commands
RMAN-01009: syntax error: found "identifier": expecting one of: "integer"
RMAN-01008: the bad identifier was: mybackup
RMAN-01007: at line 2 column 25 file: /tmp/whole_db.cmd
```

RMAN indicates a syntax error because the string `mybackup` is not a valid argument for `COPIES`.

## Making Database Connections with RMAN

This section explains how to connect the RMAN client to target databases. It contains the following topics:

- About RMAN Database Connections
- Connecting RMAN to an Auxiliary Database
- Making RMAN Database Connections Within Command Files
- Diagnosing RMAN Connection Problems

### About RMAN Database Connections

To perform useful work, the RMAN client must connect to a database. The following table describes the types of database connections that you can make with RMAN.

Table 4-1 Overview of RMAN Database Connections

| Type of Database Connection | Keyword | Description |
| --- | --- | --- |
| [target database](glossary.md) | `TARGET` | A database to be backed up or restored by RMAN |
| [recovery catalog database](glossary.md) | `CATALOG` | A database that provides an optional backup store for the RMAN repository in addition to the control file. |
| [auxiliary instance](glossary.md) or [auxiliary database](glossary.md) | `AUXILIARY` | A [physical standby database](glossary.md), or a database instance created for performing a specific task such as creating a [duplicate database](glossary.md), transporting tablespaces, or performing [tablespace point-in-time recovery (TSPITR)](glossary.md).  For many tasks that use an auxiliary database, RMAN creates an automatic auxiliary instance for use during the task, connects to it, performs the task, and then destroys it when the task is completed. You do not give any explicit command to connect to automatic auxiliary instances. |

#### Authentication for RMAN Database Connections

RMAN connections to a database are specified and authenticated in the same way as SQL\*Plus connections to a database. The only difference is that RMAN connections to a target or auxiliary database require the `SYSDBA` privilege. The `AS SYSDBA` keywords are implied for target and auxiliary connections and cannot be explicitly specified.

A `SYSDBA` privilege is not required when connecting to the recovery catalog. You must grant the `RECOVERY_CATALOG_OWNER` role to the catalog schema owner.

See Also:

[Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/dba.htm#ADMIN00102) to learn about database connection options when using SQL\*Plus

##### Authentication for RMAN Database Connections Using the Operating System

To connect to a database using operating system authentication, you must set the environment variable specifying the Oracle SID. For example, to set the SID to `prod` in some UNIX shells, you would enter:

```
% ORACLE_SID=prod; export ORACLE_SID
```

A special operating system groups controls `SYSDBA` connections when using operating system authentication. This group is generically referred to as OSDBA. The group is created and assigned a specific name as part of the database installation process. The specific name varies depending upon your operating system.

If the current operating system user is a member of the OSDBA group, and if the Oracle SID is set, then RMAN can connect to this database with `SYSDBA` privileges as follows:

```
% rman TARGET /
```

##### Authentication for RMAN Database Connections Using a Password File

If a database uses a [password file](glossary.md), then RMAN can use a password to connect to this database. Use a password file for either local or remote access. You must use a password file if you are connecting remotely as `SYSDBA` with a net service name.

Caution:

Good security practice requires that passwords should not be entered in plain text on the command line. You should enter passwords in RMAN only when requested by an RMAN prompt. See [Oracle Database Security Guide](https://docs.oracle.com/cd/E11882_01/network.112/e36292/authentication.htm#DBSEG0032) to learn about password protection.

You can start RMAN without a password in the connect string, as in this example:

```
% rman TARGET SYS@prod

target database Password: password
connected to target database: PROD1 (DBID=39525561)
```

RMAN prompts for a password and does not echo the characters.

### Making RMAN Database Connections from the Operating System Command Line

To connect to a target database from the operating system command line, enter the `rman` command followed by the connection information. You can begin executing commands after the RMAN prompt is displayed.

In the examples in this chapter, the generic values have the meanings shown in Table 4-2.

Table 4-2 Values in Examples

| Value Used in Example | Meaning |
| --- | --- |
| `SYS` | User with `SYSDBA` privileges |
| `prod` | The net service name for the target database |
| `rco` | User that owns the recovery catalog schema. This is a user defined in the recovery catalog database that has been granted the `RECOVERY_CATALOG_OWNER` role. |
| `catdb` | The net service name for the recovery catalog database |
| `aux` | The net service name for an auxiliary instance |

Example 4-2 illustrates a connection to a target database that uses operating system authentication. The `NOCATALOG` option indicates that a recovery catalog is not used in the session.

Example 4-2 Connecting to a Target Database from the System Prompt

```
% rman TARGET / NOCATALOG

connected to target database: PROD (DBID=39525561)
using target database control file instead of recovery catalog
 
RMAN>
```

Example 4-3 illustrates a connection to a target database that uses Oracle Net authentication. RMAN prompts for the password.

Example 4-3 Connecting to a Target Database from the System Prompt

```
% rman TARGET SYS@prod NOCATALOG

target database Password: password
connected to target database: PROD (DBID=39525561)

RMAN>
```

Use the `CATALOG` keyword to connect to a recovery catalog. Example 4-4 illustrates a connection that uses Oracle Net authentication for the target and recovery catalog databases. In both cases RMAN prompts for a password.

Example 4-4 Connecting to Target and Catalog Databases from the System Prompt

```
% rman TARGET SYS@prod CATALOG rco@catdb

target database Password: password
connected to target database: PROD (DBID=39525561)
recovery catalog database Password: password
connected to recovery catalog database

RMAN>
```

You can also start RMAN without specifying `NOCATALOG` or `CATALOG`. If you do not specify `NOCATALOG` on the command line, and if you do not specify [`CONNECT CATALOG`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta011.htm#RCMRF114) after RMAN has started, then RMAN defaults to `NOCATALOG` mode the first time that you run a command that requires the use of the RMAN repository.

Note:

After you have executed a command that uses the RMAN repository in `NOCATALOG` mode, you must exit and restart RMAN to be able to connect to a recovery catalog.

If you connect to the target database on the operating system command line, then you can begin executing commands after the RMAN prompt is displayed.

### Making Database Connections from the RMAN Prompt

If you start RMAN without connecting to a target database, then you must issue a [`CONNECT TARGET`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta011.htm#RCMRF114) command at the RMAN prompt to connect to a target database and begin performing useful work.

To make a database connection from the RMAN prompt:

1. On the operating system command line, start the RMAN client without making a database connection. For example, enter `rman` as follows:
	```
	% rman
	RMAN>
	```
2. At the RMAN prompt, enter one or more `CONNECT` commands.
	The following example connects to a target database using operating system authentication:
	```
	RMAN> CONNECT TARGET /
	```
	The following alternative example connects to a target database and then a recovery catalog. The target connection uses operating system authentication, whereas the catalog database connection uses Oracle Net authentication. RMAN prompts for the password of the recovery catalog user.
	```
	RMAN> CONNECT TARGET /
	RMAN> CONNECT CATALOG rco@catdb
	recovery catalog database Password: password
	connected to recovery catalog database
	```
	The following example connects to a target database with database-level credentials. RMAN prompts for the `SYS` password.
	```
	% rman
	RMAN> CONNECT TARGET SYS@prod
	target database Password: password
	connected to target database: PROD (DBID=39525561)
	```

See Also:

[Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta011.htm#RCMRF114) to learn about the `CONNECT` command

### Connecting RMAN to an Auxiliary Database

To use the [`DUPLICATE`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta020.htm#RCMRF126) command, you must connect to an [auxiliary instance](glossary.md). To perform RMAN [tablespace point-in-time recovery (TSPITR)](glossary.md), you may also need to connect to an auxiliary instance.

Note:

When you use the `DUPLICATE ... FROM ACTIVE DATABASE` command, a net service name is required. See ["Step 5: Creating an Initialization Parameter File and Starting the Auxiliary Instance"](rcmdupdb.md) for more details.

The form of an auxiliary connection is identical to a target database connection, except that you use the `AUXILIARY` keyword instead of the `TARGET` keyword. Example 4-5 connects to a target database and auxiliary instance from the RMAN prompt.

Example 4-5 Connecting to the Target and Auxiliary Databases from the RMAN Prompt

```
% rman
RMAN> CONNECT TARGET /
RMAN> CONNECT AUXILIARY SYS@aux

auxiliary database Password: password
connected to auxiliary database: PROD (DBID=30472568)
```

See Also:

- [Chapter 24, "Duplicating a Database"](rcmdupdb.md) for more details on using the [`DUPLICATE`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta020.htm#RCMRF126) command
- [Chapter 21, "Performing RMAN Tablespace Point-in-Time Recovery (TSPITR)"](rcmtspit.md) for more details on performing TSPITR

### Making RMAN Database Connections Within Command Files

If you create an RMAN command file which uses a [`CONNECT`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta011.htm#RCMRF114) command with database level credentials (user name and password), then anyone with read access to this file can learn the password. There is no secure way to incorporate a `CONNECT` string with a password into a command file.

If you create an RMAN command file which uses a `CONNECT` command, then RMAN does not echo the connect string when you run the command file with the [`@`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta001.htm#RCMRF100) command. This behavior prevents connect strings from appearing in any log files that contain RMAN output. For example, suppose you create a command file `listbkup.rman` as follows:

```
cat > listbkup.rman << EOF
CONNECT TARGET /
LIST BACKUP;
EOF
```

You execute this script by running RMAN with the `@` command line option as follows:

```
% rman @listbkup.rman
```

When the command file executes, RMAN replaces the connection string with an asterisk, as shown in the following output:

```
RMAN> CONNECT TARGET *
2> LIST BACKUP;
3>
connected to target database: RDBMS (DBID=771530996)

using target database control file instead of recovery catalog

List of Backup Sets
===================
. . .
```

### Diagnosing RMAN Connection Problems

When diagnosing errors RMAN encounters in connecting to the target, catalog and auxiliary databases, using SQL\*Plus to connect to the databases directly can reveal underlying problems with the connection information or the databases.

#### Diagnosing Target and Auxiliary Database Connection Problems

RMAN always connects to target and auxiliary databases using the `SYSDBA` privilege. Thus, when using SQL\*Plus to diagnose connection problems to the target or auxiliary databases, request a `SYSDBA` connection to reproduce RMAN behavior.

For example, suppose that the following RMAN command encountered connection errors:

```
RMAN> CONNECT TARGET /
```

You reproduce the preceding connection attempt with the SQL\*Plus command as follows:

```
SQL> CONNECT / AS SYSDBA
```

#### Diagnosing Recovery Catalog Connection Problems

When RMAN connects to the recovery catalog database, it does not use the `SYSDBA` privilege. So, when you are using SQL\*Plus to diagnose connection problems to the recovery catalog database, you must enter the database connect string exactly as it was entered into RMAN. Do not specify `AS SYSDBA`.

## Using the RMAN Pipe Interface

The RMAN pipe interface is an alternative method for issuing commands to RMAN and receiving the output from those commands. With this interface, RMAN obtains commands and sends output by using the `DBMS_PIPE` PL/SQL package instead of the operating system shell. Using this interface, it is possible to write a portable programmatic interface to RMAN.

The pipe interface is invoked by using the `PIPE` command-line parameter for the RMAN client. RMAN uses two private pipes: one for receiving commands and the other for sending output. The names of the pipes are derived from the value of the `PIPE` parameter. For example, you can invoke RMAN with the following command:

```
% rman PIPE abc TARGET /
```

RMAN opens the two pipes in the target database: `ORA$RMAN_ABC_IN`, which RMAN uses to receive user commands, and `ORA$RMAN_ABC_OUT`, which RMAN uses to send all output back to RMAN. All messages on both the input and output pipes are of type `VARCHAR2`.

RMAN does not permit the pipe interface to be used with public pipes, because they are a potential security problem. With a public pipe, any user who knows the name of the pipe can send commands to RMAN and intercept its output.

If the pipes are not initialized, then RMAN creates them as private pipes. If you want to put commands on the input pipe before starting RMAN, you must first create the pipe by calling `DBMS_PIPE.CREATE_PIPE`. Whenever a pipe is not explicitly created as a private pipe, the first access to the pipe automatically creates it as a public pipe, and RMAN returns an error if it is told to use a public pipe.

Note:

If multiple RMAN sessions can run against the target database, then you must use unique pipe names for each [RMAN session](glossary.md). The `DBMS_PIPE.UNIQUE_SESSION_NAME` function is one method that you can use to generate unique pipe names.

### Executing Multiple RMAN Commands in Succession Through a Pipe: Example

This scenario assumes that the application controlling RMAN wants to run multiple commands in succession. After each command is sent down the pipe and executed and the output returned, RMAN pauses and waits for the next command.

To execute RMAN commands through a pipe:

1. Start RMAN by connecting to a target database (required) and specifying the `PIPE` option. For example, issue:
	```
	% rman PIPE abc TARGET /
	```
	You can also specify the `TIMEOUT` option, which forces RMAN to exit automatically if it does not receive any input from the input pipe in the specified number of seconds. For example, enter:
	```
	% rman PIPE abc TARGET / TIMEOUT 60
	```
2. Connect to the target database and put the desired commands on the input pipe by using `DBMS_PIPE.PACK_MESSAGE` and `DBMS_PIPE.SEND_MESSAGE`. In pipe mode, RMAN issues message `RMAN-00572` when it is ready to accept input instead of displaying the standard RMAN prompt.
3. Read the RMAN output from the output pipe by using `DBMS_PIPE.RECEIVE_MESSAGE` and `DBMS_PIPE.UNPACK_MESSAGE`.
4. Repeat Steps 2 and 3 to execute further commands with the same RMAN instance that was started in Step 1.
5. If you used the `TIMEOUT` option when starting RMAN, then RMAN terminates automatically after not receiving any input for the specified length of time. To force RMAN to terminate immediately, send the `EXIT` command.

### Executing RMAN Commands in a Single Job Through a Pipe: Example

This scenario assumes that the application controlling RMAN wants to run one or more commands as a single job. After running the commands that are on the pipe, RMAN exits.

To execute RMAN commands in a single job through a pipe:

1. After connecting to the target database, create a pipe (if it does not exist under the name `ORA$RMAN_` pipe `_IN`).
2. Put the desired commands on the input pipe. In pipe mode, RMAN issues message `RMAN-00572` when it is ready to accept input instead of displaying the standard RMAN prompt.
3. Start RMAN with the `PIPE` option, and specify `TIMEOUT` `0`. For example, enter:
	```
	% rman PIPE abc TARGET / TIMEOUT 0
	```
4. RMAN reads the commands that were put on the pipe and executes them by using `DBMS_PIPE.PACK_MESSAGE` and `DBMS_PIPE.SEND_MESSAGE`. When it has exhausted the input pipe, RMAN exits immediately.
5. Read RMAN output from the output pipe by using `DBMS_PIPE.RECEIVE_MESSAGE` and `DBMS_PIPE.UNPACK_MESSAGE`.
	See Also:
	[Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/d_pipe.htm#ARPLS038) for documentation on the `DBMS_PIPE` package