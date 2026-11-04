---
title: "Backup and Recovery User's Guide"
book: "Database Backup and Recovery User's Guide"
doc_id: F31836-11
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/bradv/starting-interacting-with-rman-client.html
tags:
  - oracle
  - 21c
  - backup-and-recovery-users-guide
---

Use the RMAN command-line interface to make connections to a multitenant container database (CDB),pluggable database (PDB), or application root.

### 4.1 Starting and Exiting RMAN

The RMAN executable is automatically installed with the database and is typically located in the same directory as the other database executables. For example, the RMAN client on Linux is located in `$ORACLE_HOME/bin`.

You have the following basic options for starting RMAN:

- Start the RMAN executable at the operating system command line without specifying any connection options, as in the following example:
	```
	% rman
	```
- Start the RMAN executable at the operating system command line, as in the following examples:
	```
	% rman TARGET /
	% rman TARGET sbu@prod NOCATALOG
	```

To quit RMAN and terminate the program, enter `EXIT` or `QUIT` at the RMAN prompt:

```
RMAN> EXIT
```

### 4.2 Making Database Connections with RMAN

You can create connections to the root or a pluggale database (PDB). There are multiple methods of connecting to the database and authenticating these connections.

#### 4.2.1 About RMAN Database Connection Types

To perform useful work, the RMAN client must connect to a database.

Table 4-1 describes the types of database connections that you can make with RMAN.

Table 4-1 Overview of RMAN Database Connections

| Type of Database Connection | Keyword | Description |
| --- | --- | --- |
| target database | `TARGET` | A database to be backed up or recovered by RMAN |
| recovery catalog database | `CATALOG` | A database that provides an optional backup store for the RMAN repository in addition to the control file. |
| auxiliary instance or auxiliary database | `AUXILIARY` | A physical standby database, or a database instance created for performing a specific task such as creating a duplicate database, transporting tablespaces, or performing tablespace point-in-time recovery (TSPITR).  For many tasks that use an auxiliary database, RMAN creates an automatic auxiliary instance for use during the task, connects to it, performs the task, and then destroys it when the task is completed. You do not give any explicit command to connect to automatic auxiliary instances. |

#### 4.2.2 About Authentication for RMAN Database Connections

Users connecting with RMAN to a target or auxiliary database require either the `SYSDBA` or `SYSBACKUP` system privilege.

These privileges are not required when connecting to the recovery catalog. You must grant the `RECOVERY_CATALOG_OWNER` role to the catalog schema owner. Users can also connect to the recovery catalog using the VPC credentials that have been created by the recovery catalog owner.

The same authentication options that are available with SQL\*Plus are available with RMAN. The most common ways to authenticate with the target and auxiliary databases are:

- Operating system authentication
	The prerequisites for connecting using operating system authentication are described in "Authentication Using the Operating System".
- Password file authentication
	The prerequisites for connecting using password file authentication are described in "Authentication Using a Password File".

Neither of these methods requires the database to be open. Operating system authentication is used only to connect locally. Password file authentication can be used to connect locally or remotely.

##### 4.2.2.1 Authentication Using the Operating System

RMAN connections to a target or auxiliary database can be made using operating system authentication.

The following are the prerequisites for connecting to a database using operating system authentication (OS authentication):

- You must set the `ORACLE_SID` environment variable, specifying the system identifier (SID) for the database.
	For example, to set the SID to `prod` in some UNIX shells, you enter:
	```
	% ORACLE_SID=prod; export ORACLE_SID
	```
- You must be a member of the OSDBA operating system group to connect with the `SYSDBA` privilege or the OSBACKUPDBA operating system group to connect with the `SYSBACKUP` privilege.
	On UNIX and Linux, the OSDBA group is typically named `dba`, and the OSBACKUPDBA group is typically named `backupdba`. These names are assigned during database installation.

##### 4.2.2.2 Authentication Using a Password File

Use a password file for either local or remote access. If a database uses a password file to authenticate administrative users, then RMAN can connect using a password.

The database must use a password file for you to connect remotely using a net service name.

Caution:

Good security practice requires that passwords not be entered in plain text on the command line. Enter passwords in RMAN only when requested by an RMAN prompt.

The database creates an entry in the password file when you grant the `SYSDBA` or `SYSBACKUP` privilege to a user. You can then connect to the target or auxiliary database as this user even if the database is not open.

To support connecting through the password file with the `SYSBACKUP` privilege, the password file must be created in or upgraded to the format for Oracle Database 12c Release 1 (12.1) or later.

If neither `AS SYSBACKUP` nor `AS SYSDBA` is specified in the connection string, then the default used is `AS SYSDBA`. In this case, no enclosing quotes are required.

Example 4-1 Password File Authentication as SYSDBA - Explicit

In this example, the `sdba` user has been granted the `SYSDBA` privilege:

```
% rman target '"sdba@prod1 as sysdba"' 

target database Password: password
connected to target database: PROD1 (DBID=39525561)
```

Example 4-2 Password File Authentication as SYSBACKUP - Explicit

In this example, the `sbu` user is granted the `SYSBACKUP` privilege in the target database:

```
% rman target '"sbu@prod1 as sysbackup"' 

target database Password: password
connected to target database: PROD1 (DBID=39525561)
```

Example 4-3 Password File Authentication as SYSDBA - Implicit

```
% rman target sbu@prod1

target database Password: password
connected to target database: PROD1 (DBID=39525561)
```

#### 4.2.3 Methods of Making RMAN Database Connections

Database connections can be made from the RMAN client or the operating system command line. These connections can be authenticated using a password file or with operating system authentication.

##### 4.2.3.1 Making Database Connections from the RMAN Prompt

If you start RMAN without a connect string on the operating system command line, then you must issue a `CONNECT TARGET` command at the RMAN prompt to connect to a target database.

To make a database connection from the RMAN prompt:

1. On the operating system command line, start the RMAN client without making a database connection.
	```
	% rman
	RMAN>
	```
2. At the RMAN prompt, enter one or more `CONNECT` commands.

Example 4-4 Connecting from RMAN Prompt with OS Authentication - Implicit

```
RMAN> connect target /
```

Because no system privilege is specified, `AS` `SYSDBA` is assumed.

Example 4-5 Connecting from RMAN Prompt with OS Authentication - Explicit

```
RMAN> connect target "/ as sysdba"
```

When including a system privilege, the enclosing quotation marks (single or double) are required.

##### 4.2.3.2 Making RMAN Connections from the Operating System Command Line

RMAN connections to the root container can be made from the operating system command line.

To make database connections from the operating system command line:

1. Ensure that the prerequisites described in "Authentication Using the Operating System" are met.
2. Enter the `rman` command followed by the connection information.
	Use the `CATALOG` keyword to connect to a recovery catalog. You can also start RMAN without specifying `NOCATALOG` or `CATALOG`. If you do not specify `NOCATALOG` on the command line, and if you do not specify `CONNECT                                                   CATALOG` after RMAN has started, then RMAN defaults to `NOCATALOG` mode the first time that you run a command that requires the use of the RMAN repository.
3. Execute the required RMAN commands after the RMAN prompt is displayed.

Note:

After you have executed a command that uses the RMAN repository in `NOCATALOG` mode, you must exit and restart RMAN to be able to connect to a recovery catalog.

Example 4-6 Connecting to a Target Database from the System Prompt Using Operating System Authentication

This example illustrates a connection to a root container in a target database using operating system authentication. The `NOCATALOG` option indicates that a recovery catalog is not used in the session.

```
% rman TARGET / NOCATALOG

connected to target database: PROD (DBID=39525561)
using target database control file instead of recovery catalog
```

Example 4-7 Connecting to a Target Database from the System Prompt by Using Net Service Names

This example illustrates a connection to a target database that uses a net service name and password file authentication. RMAN prompts for the password.

```
% rman TARGET sbu@prod NOCATALOG

target database Password: password
connected to target database: PROD (DBID=39525561)
```

#### 4.2.4 About Performing Operations on CDBs and PDBs

You can perform RMAN operations on a whole multitenant container database (CDB), the root only, or one or more pluggable databases (PDBs).

Make RMAN connections to CDBs according to the following rules:

- To perform operations on the whole CDB (for example, to back up the whole CDB), connect as target to the root.
- To perform operations on the root only (for example, to back up the root), connect as target to the root.
- To perform operations on a single PDB, connect as target either to the root or to the PDB.
	- If you connect to the root, you must use the `PLUGGABLE DATABASE` syntax in your RMAN commands. For example, to back up a PDB, you use the `BACKUP PLUGGABLE DATABASE` command.
		- If instead you connect directly to the PDB, use the same commands that you would use when connected to a database. For example, to back up a PDB, you would use the `BACKUP DATABASE` command.
- To perform operations on two or more PDBs with a single command, you connect as target to the root.
	For example, to back up both the `sales` and `hr` PDBs, you connect to the root and submit the following command:
	```
	BACKUP PLUGGABLE DATABASE sales, hr;
	```

Note:

If you connect as target to a CDB with operating system authentication, you are connected to the root.

#### 4.2.5 Connecting as Target to the Root

There are several ways to connect as target to the root.

The three most common ways are as follows:

- Connecting locally as a common user, as shown in Example 4-8
- Connecting with operating system authentication, as shown in Example 4-9
- Connecting as a common user through Oracle Net Services, using a net service name, as shown in Example 4-12

In all cases, you must connect as a user with the `SYSDBA` or `SYSBACKUP` privilege.

Example 4-8 Connecting Locally to the Root

This example connects locally to the root using the `SYS` user, which is a common user. The connection is established using the `SYSDBA` privilege.

```
rman target sys

target database Password: password
connected to target database: CDB (DBID=659628168)
```

Example 4-9 Connecting to the Root using Operating System Authentication with SYSDBA Privilege - Implicit

This example connects locally to the root using operating system authentication. The connection is established as the `SYS` user with `SYSDBA` privilege.

```
rman target /
 
connected to target database: CDB (DBID=659628168)
```

If neither `AS SYSBACKUP` nor `AS SYSDBA` is specified in the connection string, then the default used is `AS                     SYSDBA`.

Example 4-10 Connecting to the Root using Operating System Authentication with the SYSDBA Privilege - Explicit

This example connects locally to the root using operating system authentication. The connection is established as the `SYS` user with `SYSBACKUP` privilege explicitly mentioned.

```
% rman target '"/ as sysbackup"'
```

Example 4-11 Connecting to Target Database and a Recovery Catalog

In this example, the target connection uses operating system authentication, and the recovery catalog database connection uses a net service name and password file authentication. The recovery catalog owner is user `rco`. RMAN prompts for the password of the recovery catalog user.

```
RMAN> connect target /
RMAN> connect catalog rco@catdb

recovery catalog database Password: password
connected to recovery catalog database
```

Example 4-12 Connecting to the Root with a Net Service Name

This example assumes that there is a `sales` net service name that resolves to a database service for the root, and that there is a common user named `c##bkuser` that has the `SYSBACKUP` privilege.

```
rman target c##bkuser@sales
 
target database Password: password
connected to target database: CDB (DBID=659628168)
```

Example 4-13 Connecting with Password File Authentication

```
RMAN> connect target "sbu@prod AS SYSBACKUP"

target database Password: password
connected to target database: PROD (DBID=39525561)
```

Example 4-14 Connecting to a Target Database from System Prompt When Password Contains a Semi-colon

This example illustrates a connection to a target database that uses a net service name and password file authentication. The password contains a special character, the semi-colon.

```
rman TARGET "'sbu/rman;pwd@prod AS SYSBACKUP'"

connected to target database: PROD (DBID=2004181664)
```

Note:

For security reasons, Oracle recommends that you do not specify the password at the command line. You should supply the password only when prompted to do so.

Example 4-15 Connecting to Target and a Recovery Catalog from the System Prompt

This example illustrates a connection that uses Oracle Net authentication for the target and recovery catalog databases. In both cases RMAN prompts for a password.

```
% rman TARGET sbu@prod CATALOG rco@catdb

target database Password: password
connected to target database: PROD (DBID=39525561)
recovery catalog database Password: password
connected to recovery catalog database
```

#### 4.2.6 Connecting as Target to a PDB

You can connect to a PDB either from the RMAN prompt or the operating system command line.

To connect as target to a PDB, you must:

- Connect with a net service name that resolves to a database service for that PDB.
- Connect as a local user or common user with the `SYSDBA` privilege.

Example 4-16 Connecting As Target to a PDB

This example illustrates a connection to a PDB. It assumes the following

- You want to perform RMAN operations on a PDB named `hrpdb`.
- The net service name `hrpdb` resolves to a database service for the `hrpdb` PDB.
- The local user `hrbkup` was created in the `hrpdb` PDB and granted the `SYSDBA` privilege.
```
rman target hrbkup@hrpdb
 
target database Password: password
connected to target database: CDB (DBID=659628168)
```

Example 4-17 Connecting to a PDB and Recovery Catalog

This example illustrates a connection to a PDB and recovery catalog. It assumes the following:

- You want to perform operations on a PDB named `salespdb`. The `SYS` user is used to connect to the PDB.
- The net service name `salespdb` resolves to a database service for the `salespdb` PDB.
- The connection to the recovery catalog is created using the recovery catalog owner, `rco`. The net service name for the recovery catalog database is `catdb`.

Enter the passwords for the `sys` and `rco` users when prompted.

```
RMAN> connect target "sys@salespdb as sysdba"
target database Password: 
connected to target database: DBMAIN:SALESPDB (DBID=1661283172)

RMAN> connect catalog rco@catdb 
recovery catalog database Password: 
connected to recovery catalog database
```

##### 4.2.6.1 Restrictions When Connected to a PDB

Certain restrictions apply when you connect directly to a pluggable database (PDB):

The following operations are not available when you connect as target directly to a PDB:

- Back up archived logs
- Delete archived logs
- Delete archived log backups
- Restore archived logs (RMAN does restore archived logs when required during media recovery.)
- Point-in-time recovery (PITR) when using shared undo mode
- TSPITR when using shared undo mode
- Table recovery when using shared undo mode
- Duplicate database when using shared undo mode
- Flashback operations when using shared undo mode
- Running Data Recovery Advisor
- Report/delete obsolete
- Register database
- Import catalog
- Reset database
- Configuring the RMAN environment (using the `CONFIGURE` command)

Note:

Starting in Oracle Database 19c, the Data Recovery Advisor (DRA) feature is deprecated.

The deprecation of DRA includes deprecation of the following Oracle Recovery Manager (RMAN) commands: `LIST FAILURE`, `ADVISE FAILURE`, `REPAIR                     FAILURE`, and `CHANGE FAILURE`. Database administrators will no longer have access to these commands. There is no replacement feature for DRA.

#### 4.2.7 Connecting RMAN to an Auxiliary Database

Connection to an auxiliary database is required for certain tasks such as database duplication and tablespace point-in-time recovery (TSPITR).

The form of an auxiliary connection is identical to a target database connection, except that you use the `AUXILIARY` keyword instead of the `TARGET` keyword.

Note:

When you use the `DUPLICATE ... FROM                     ACTIVE DATABASE` command, a net service name is required.

Example 4-18 Connecting to Target and Auxiliary Databases from the RMAN Prompt

This example illustrates a connection to a target database using operating system authentication, and the auxiliary database connection uses a net service name and password file authentication.

```
% rman
RMAN> CONNECT TARGET /
RMAN> CONNECT AUXILIARY sbu@aux

auxiliary database Password: password
connected to auxiliary database: AUX (DBID=30472568)
```

Example 4-19 Connecting to Target and Auxiliary Databases from the System Prompt

This example illustrates a connection to a target database and an auxiliary database from the system prompt. The target connection uses operating system authentication and the auxiliary connection uses a net service name and password file authentication.

```
% rman target / auxiliary sbu@aux

auxiliary database Password: password
connected to auxiliary database: AUX (DBID=30472568)
```

#### 4.2.8 Making RMAN Database Connections Within Command Files

You can make a database connection by creating an RMAN command file containing a `CONNECT` command.

If you create an RMAN command file that uses a `CONNECT` command with database level credentials (user name and password), then anyone with read access to this file can learn the password. There is no secure way to incorporate a `CONNECT` string with a password into a command file.

If you create an RMAN command file that uses a `CONNECT` command, then RMAN does not echo the connect string when you run the command file with the `@` command. This behavior prevents connect strings from appearing in any log files that contain RMAN output. For example, suppose that you create a command file `listbkup.rman` as follows:

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

### 4.3 Diagnosing RMAN Connection Problems

When you are diagnosing errors that RMAN encounters in connecting to the target, catalog and auxiliary databases, consider using SQL\*Plus to connect to the databases directly. This action can reveal underlying problems with the connection information or the databases.

#### 4.3.1 Diagnosing Target and Auxiliary Database Connection Problems

RMAN connects to target and auxiliary databases using the `SYSDBA` or `SYSBACKUP` privilege. Thus, when you use SQL\*Plus to diagnose connection problems to the target or auxiliary databases, request a `SYSDBA` or `SYSBACKUP` connection to reproduce RMAN behavior.

For example, suppose that the following RMAN command encountered connection errors:

```
RMAN> CONNECT TARGET /
```

You reproduce the preceding connection attempt with the SQL\*Plus command as follows:

```
SQL> CONNECT / AS SYSBACKUP
```

#### 4.3.2 Diagnosing Recovery Catalog Connection Problems

Use SQL\*Plus to diagnose recovery catalog connection problems.

When RMAN connects to the recovery catalog database, it does not use the `SYSDBA` or `SYSBACKUP` privilege. When you use SQL\*Plus to diagnose connection problems to the recovery catalog database, you must enter the database connect string exactly as it was entered into RMAN. Do not specify `AS SYSBACKUP` or `AS SYSDBA`.

### 4.4 Entering RMAN Commands

You can enter RMAN commands either directly from the RMAN prompt or read them in from a text file.

This section describes the ways of running RMAN commands.

#### 4.4.1 Entering RMAN Commands at the RMAN Prompt

When the RMAN client is ready for your commands, it displays the command prompt.

The following is an example of the RMAN command prompt:

```
RMAN>
```

Enter commands for RMAN to execute. For example:

```
RMAN> CONNECT TARGET
RMAN> BACKUP DATABASE;
```

Most RMAN commands take several parameters and must end with a semicolon. Some commands, such as `STARTUP`, `SHUTDOWN`, and `CONNECT`, can be used with or without a semicolon.

When you enter a line of text that is not a complete command, RMAN prompts for continuation input with a line number. For example:

```
RMAN> BACKUP DATABASE
2> INCLUDE CURRENT 
3> CONTROLFILE
4> ;
```

#### 4.4.2 Using Command Files with RMAN

For repetitive tasks, you can create a text file containing RMAN commands, and start the RMAN client with the `@` argument, followed by a file name.

For example, create a text file `cmdfile1` in the current directory containing one line of text as shown here:

```
BACKUP DATABASE PLUS ARCHIVELOG;
```

You can run this command file from the command line as shown in this example, and the command contained in it is executed:

```
% rman TARGET / @cmdfile1
```

After the command completes, RMAN exits.

You can also use the [`@`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=RCMRF100) command at the RMAN command prompt to execute the contents of a command file during an RMAN session. RMAN reads the file and executes the commands in it. For example:

```
RMAN> @cmdfile1
```

After the command file contents have been executed, RMAN displays the following message:

```
RMAN>  **end-of-file**
```

Unlike the case where a command file is executed from the operating system command line, RMAN does not exit.

#### 4.4.3 Entering Comments in RMAN Command Files

The comment character in RMAN is a pound sign (`#`). All text from the pound sign to the end of the line is ignored.

For example, the contents of the following command file back up the database and archived redo log files and include comments:

```
# Command file name: mybackup.rman
# The following command backs up the database
BACKUP DATABASE;
# The following command backs up the archived redo logs
BACKUP ARCHIVELOG ALL;
```

The following example shows how you can break a single RMAN command across multiple lines:

```
RMAN> BACKUP # this is a comment
2> SPFILE;
```

#### 4.4.4 Using Substitution Variables in Command Files

When running a command file, you can specify one or more values in a `USING` clause for use in substitution variables in a command file. In this way, you can make your command files dynamic.

As in SQL\*Plus, `&1` indicates where to place the first value, `&2` where to place the second value, and so on. The substitution variable syntax is `&` `integer` followed by an optional period, for example, `&1.3`. The optional period is part of the variable and replaced with the value, thus enabling the substitution text to be immediately followed by another integer. For example, if you pass the value `mybackup` to a command file containing the variable `&1.3`, then the result of the substitution is `mybackup3`.

The following procedure explains how to create and use a dynamic shell script that calls a command file containing substitution variables.

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
	set format = $argv[2]
	set restore_point = $argv[3]
	rman @'/disk1/scripts/quarterly_backup.cmd' USING $media_family $format $restore_point
	```
3. Execute the shell script created in the previous step, specifying the desired arguments on the command line.
	The following example runs the `runbackup.sh` shell script and passes it `archival_backup` as the media family name, `bck0906` as the format string, and `FY06Q3` as the restore point name.
	```
	% runbackup.sh archival_backup bck0906 FY06Q3
	```

### 4.5 Setting Globalization Support Environment Variables for RMAN

Before invoking RMAN, it may be useful to set the `NLS_DATE_FORMAT` and `NLS_LANG` environment variables. These variables determine the format used for the time parameters in RMAN commands such as `RESTORE`, `RECOVER`, and `REPORT`.

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

For the environment variable `NLS_DATE_FORMAT` to be applied and override the defaults set for the server in the server initialization file, the environment variable `NLS_LANG` must also be set.

### 4.6 Specifying the Location of RMAN Output

By default, RMAN writes command output to standard output. To redirect output to a log file, enter the `LOG` parameter on the command line when you start RMAN.

The following example writes RMAN command output to the file `rman.log:`

```
% rman LOG /tmp/rman.log
```

In this case, RMAN displays command input but does not display the RMAN output. The easiest way to send RMAN output both to a log file and to standard output is to use the Linux `tee` command or its equivalent. For example, the following technique enables both input and output to be visible in the RMAN command-line interface:

```
% rman | tee rman.log
RMAN>
```

### 4.7 Checking RMAN Syntax

You can test RMAN commands for syntactic correctness without executing them. Use the command-line argument `CHECKSYNTAX` to start the RMAN client in a mode in which it only parses the commands that you enter and returns an `RMAN-00558` error for commands that are not legal RMAN syntax.

You can check the syntax of RMAN commands either at the command line or in command files.

#### 4.7.1 Checking RMAN Syntax at the Command Line

You can check the syntax of RMAN commands interactively without actually executing the commands.

To check RMAN syntax at the command line:

1. Start RMAN with the `CHECKSYNTAX` parameter:
	```
	% rman CHECKSYNTAX
	```
2. Enter the RMAN commands to be tested.

The following example shows a sample interactive session, with user-entered text in bold.

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

#### 4.7.2 Checking RMAN Syntax in Command Files

To test commands in a command file, start RMAN with the `CHECKSYNTAX` parameter and use the `@` command to name the command file to be passed.

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

Example 4-20 Checking the Syntax of a Command File with Correct Syntax

This example shows the output when you run `/tmp/goodcmdfile` with `CHECKSYNTAX`:

```
RMAN> # command file with legal syntax
2> restore database;
3> recover database;
4>
The cmdfile has no syntax errors
 
Recovery Manager complete.
```

Example 4-21 Checking the Syntax of a Command File with Bad Syntax

This example shows the output when you run `/tmp/badcmdfile` with `CHECKSYNTAX`:

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

Example 4-22 Checking the Syntax of a Command File that Contains Substitution Variables

You make your command files dynamic by including substitution variables. When you check the syntax of a command file that contains substitution variables, RMAN prompts you to enter values. This example illustrates what happens if you enter invalid values when checking the syntax of a dynamic command file. The text in bold indicates text entered at the prompt.

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

### 4.8 Using the RMAN Pipe Interface

The RMAN pipe interface is an alternative method for issuing commands to RMAN and receiving the output from those commands. Using this interface, it is possible to write a portable programmatic interface to RMAN.

With the pipe interface, RMAN obtains commands and sends output by using the `DBMS_PIPE` PL/SQL package instead of the operating system shell. The pipe interface is invoked by using the `PIPE` command-line parameter for the RMAN client. RMAN uses two private pipes: one for receiving commands and the other for sending output. The names of the pipes are derived from the value of the `PIPE` parameter. For example, you can invoke RMAN with the following command:

```
% rman PIPE abc TARGET /
```

RMAN opens the two pipes in the target database: `ORA$RMAN_ABC_IN`, which RMAN uses to receive user commands, and `ORA$RMAN_ABC_OUT`, which RMAN uses to send all output back to RMAN. All messages on both the input and output pipes are of type `VARCHAR2`.

RMAN does not permit the pipe interface to be used with public pipes, because they are a potential security problem. With a public pipe, any user who knows the name of the pipe can send commands to RMAN and intercept its output.

If the pipes are not initialized, then RMAN creates them as private pipes. If you want to put commands on the input pipe before starting RMAN, you must first create the pipe by calling `DBMS_PIPE.CREATE_PIPE`. Whenever a pipe is not explicitly created as a private pipe, the first access to the pipe automatically creates it as a public pipe, and RMAN returns an error if it is told to use a public pipe.

Note:

If multiple RMAN sessions can run against the target database, then you must use unique pipe names for each RMAN session. The `DBMS_PIPE.UNIQUE_SESSION_NAME` function is one method that you can use to generate unique pipe names.

#### 4.8.1 Executing Multiple RMAN Commands in Succession Through a Pipe: Example

This example assumes that the application controlling RMAN wants to run multiple commands in succession. After each command is sent down the pipe and executed and the output returned, RMAN pauses and waits for the next command.

To execute RMAN commands through a pipe:

1. Start RMAN by connecting to a target database (required) and specifying the `PIPE` option. For example, enter:
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

#### 4.8.2 Executing RMAN Commands in a Single Job Through a Pipe: Example

This example assumes that the application controlling RMAN wants to run one or more commands as a single job. After running the commands that are on the pipe, RMAN exits.

To execute RMAN commands in a single job through a pipe:

1. After connecting to the target database, create a pipe (if it does not already exist under the name `ORA$RMAN_` pipe `_IN`).
2. Put the desired commands on the input pipe. In pipe mode, RMAN issues message `RMAN-00572` when it is ready to accept input instead of displaying the standard RMAN prompt.
3. Start RMAN with the `PIPE` option, and specify `TIMEOUT` `0`. For example, enter:
	```
	% rman PIPE abc TARGET / TIMEOUT 0
	```
4. RMAN reads the commands that were put on the pipe and executes them by using `DBMS_PIPE.PACK_MESSAGE` and `DBMS_PIPE.SEND_MESSAGE`. When it has exhausted the input pipe, RMAN exits immediately.
5. Read RMAN output from the output pipe by using `DBMS_PIPE.RECEIVE_MESSAGE` and `DBMS_PIPE.UNPACK_MESSAGE`.