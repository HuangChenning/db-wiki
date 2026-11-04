---
title: Getting Started with RMAN
book: "Backup and Recovery User's Guide"
doc_id: E10642-08
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/backup.112/e10642/rcmquick.htm
tags:
  - oracle
  - 11g
  - backup-and-recovery-users-guide
---

## 2 Getting Started with RMAN

This chapter is intended for new users who want to start using RMAN right away without first reading the more detailed chapters in this book. This chapter provides the briefest possible digest of the most important RMAN concepts and tasks. It is not a substitute for the rest of the backup and recovery documentation set.

This chapter contains the following topics:

## Overview of the RMAN Environment

Recovery Manager (RMAN) is an Oracle Database client that performs backup and recovery tasks on your databases and automates administration of your backup strategies. It greatly simplifies backing up, restoring, and recovering database files.

The RMAN environment consists of the utilities and databases that play a role in backing up your data. At a minimum, the environment for RMAN must include the following components:

- A [target database](glossary.md)
	An Oracle database to which RMAN is connected with the `TARGET` keyword. A target database is a database on which RMAN is performing backup and recovery operations. RMAN always maintains metadata about its operations on a database in the control file of the database. The RMAN metadata is known as the [RMAN repository](glossary.md).
- The [RMAN client](glossary.md)
	An Oracle Database executable that interprets commands, directs server sessions to execute those commands, and records its activity in the target database control file. The RMAN executable is automatically installed with the database and is typically located in the same directory as the other database executables. For example, the RMAN client on Linux is located in `$ORACLE_HOME/bin`.

Some environments use the following optional components:

- A [fast recovery area](glossary.md)
	A disk location in which the database can store and manage files related to backup and recovery. You set the fast recovery area location and size with the [`DB_RECOVERY_FILE_DEST`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams065.htm#REFRN10234) and [`DB_RECOVERY_FILE_DEST_SIZE`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams066.htm#REFRN10235) initialization parameters.
- A [media manager](glossary.md)
	An application required for RMAN to interact with sequential media devices such as tape libraries. A media manager controls these devices during backup and recovery, managing the loading, labeling, and unloading of media. Media management devices are sometimes called [SBT](glossary.md) (system backup to tape) devices.
- A [recovery catalog](glossary.md)
	A separate database schema used to record RMAN activity against one or more target databases. A recovery catalog preserves RMAN repository metadata if the control file is lost, making it much easier to restore and recover following the loss of the control file. The database may overwrite older records in the control file, but RMAN maintains records forever in the catalog unless the records are deleted by the user.

This chapter explains how to use RMAN in the most basic configuration, which is without a recovery catalog or media manager.

See Also:

- [Chapter 3, "Recovery Manager Architecture"](rcmarchi.md) for a more detailed overview of the RMAN environment
- [Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta007.htm#RCMRF107) for `BACKUP` command syntax and semantics

## Starting RMAN and Connecting to a Database

The RMAN client is started by issuing the `rman` command at the command prompt of your operating system. RMAN then displays a prompt for your commands as shown in the following example:

```
% rman
RMAN>
```

RMAN connections to a database are specified and authenticated in the same way as SQL\*Plus connections to a database. The only difference is that RMAN connections to a target or auxiliary database require the `SYSDBA` privilege. The `AS SYSDBA` keywords are implied and cannot be explicitly specified. See [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/dba.htm#ADMIN00102) to learn about database connection options for SQL\*Plus.

Caution:

Good security practice requires that passwords should not be entered in plain text on the command line. You should enter passwords in RMAN only when requested by an RMAN prompt. See [Oracle Database Security Guide](https://docs.oracle.com/cd/E11882_01/network.112/e36292/authentication.htm#DBSEG0032) to learn about password protection.

You can connect to a database with command-line options or by using the [`CONNECT TARGET`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta011.htm#RCMRF114) command. The following example starts RMAN and then connects to a target database through Oracle Net, `AS SYSDBA` is not specified because it is implied. RMAN prompts for a password.

```
% rman
RMAN> CONNECT TARGET SYS@prod

target database Password: password
connected to target database: PROD (DBID=39525561)
```

The following variation starts RMAN and then connects to a target database by using operating system authentication:

```
% rman
RMAN> CONNECT TARGET /

connected to target database: PROD (DBID=39525561)
```

To quit the RMAN client, enter `EXIT` at the RMAN prompt:

```
RMAN> EXIT
```

Syntax of Common RMAN Command-line Options

```
RMAN 
[ TARGET connectStringSpec 
| { CATALOG connectStringSpec } 
| LOG ['] filename ['] [ APPEND ]
.
.
. 
]...

connectStringSpec::=
['] [userid] [/ [password]] [@net_service_name] [']
```

The following example appends the output from an [RMAN session](glossary.md) to a text file at `/tmp/msglog.log`

```
% rman TARGET / LOG /tmp/msglog.log APPEND
```

See Also:

[Chapter 4, "Starting and Interacting with the RMAN Client,"](rcmcnctg.md) to learn more about starting and using the RMAN client

## Showing the Default RMAN Configuration

The RMAN backup and recovery environment is preconfigured for each target database. The configuration is persistent and applies to all subsequent operations on this target database, even if you exit and restart RMAN.

RMAN configured settings can specify backup devices, configure a connection to a backup device (known as a [channel](glossary.md)), policies affecting backup strategy, and others. The default configuration is adequate for most purposes.

To show the current configuration for a database:

1. Start RMAN and connect to a target database.
2. Run the `SHOW ALL` command.
	For example, enter the command at the RMAN prompt as follows:
	```
	RMAN> SHOW ALL;
	```

The output lists the `CONFIGURE` commands to re-create this configuration.

See Also:

[Chapter 5, "Configuring the RMAN Environment,"](rcmconfb.md) and [Chapter 6, "Configuring the RMAN Environment: Advanced Topics,"](rcmconfa.md) to learn how to configure the RMAN environment

## Backing Up a Database

Use the [`BACKUP`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta007.htm#RCMRF107) command to back up files. RMAN backs up data to the configured default device for the type of backup requested. By default, RMAN creates backups on disk. If a fast recovery area is enabled, and if you do not specify the `FORMAT` parameter (see Table 2-1), then RMAN creates backups in the recovery area and automatically gives them unique names.

By default, RMAN creates backup sets rather than image copies. A [backup set](glossary.md) consists of one or more backup pieces, which are physical files written in a format that only RMAN can access. A [multiplexed backup set](glossary.md) contains the blocks from multiple input files. RMAN can write backup sets to disk or tape.

If you specify `BACKUP` `AS` `COPY`, then RMAN copies each file as an [image copy](glossary.md), which is a bit-for-bit copy of a database file created on disk. Image copies are identical to copies created with operating system commands like `cp` on Linux or `COPY` on Windows, but are recorded in the RMAN repository and so are usable by RMAN. You can use RMAN to make image copies while the database is open.

See Also:

- [Chapter 8, "RMAN Backup Concepts,"](rcmcncpt.md) to learn concepts relating to RMAN backups
- [Chapter 9, "Backing Up the Database,"](rcmbckba.md) to learn how to back up database files with RMAN
- [Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta007.htm#RCMRF107) for `BACKUP` command syntax and semantics

### Backing Up a Database in ARCHIVELOG Mode

If a database runs in `ARCHIVELOG` mode, then you can back up the database while it is open. The backup is called an [inconsistent backup](glossary.md) because redo is required during recovery to bring the database to a consistent state. If you have the archived redo logs needed to recover the backup, open database backups are as effective for data protection as consistent backups.

To back up the database and archived redo logs while the database is open:

1. Start RMAN and connect to a target database.
2. Run the `BACKUP DATABASE` command.
	For example, enter the following command at the RMAN prompt to back up the database and all archived redo log files to the default backup device:
	```
	RMAN> BACKUP DATABASE PLUS ARCHIVELOG;
	```

### Backing Up a Database in NOARCHIVELOG Mode

If a database runs in `NOARCHIVELOG` mode, then the only valid database backup is a [consistent backup](glossary.md). For the backup to be consistent, the database must be mounted after a consistent shutdown. No recovery is required after restoring the backup.

To make a consistent database backup:

1. Start RMAN and connect to a target database.
2. Shut down the database consistently and then mount it.
	For example, enter the following commands to guarantee that the database is in a consistent state for a backup:
	```
	RMAN> SHUTDOWN IMMEDIATE;
	RMAN> STARTUP FORCE DBA;
	RMAN> SHUTDOWN IMMEDIATE;
	RMAN> STARTUP MOUNT;
	```
3. Run the `BACKUP DATABASE` command.
	For example, enter the following command at the RMAN prompt to back up the database to the default backup device:
	```
	RMAN> BACKUP DATABASE;
	```
	The following variation of the command creates image copy backups of all data files in the database:
	```
	RMAN> BACKUP AS COPY DATABASE;
	```
4. Open the database and resume normal operations.
	The following command opens the database:
	```
	RMAN> ALTER DATABASE OPEN;
	```

### Typical Backup Options

The `BACKUP` command includes a host of options, parameters, and clauses that control backup output. Table 2-1 lists some typical backup options.

Table 2-1 Common Backup Options

| Option | Description | Example |
| --- | --- | --- |
| `FORMAT` | Specifies a location and name for backup pieces and copies. You must use substitution variables to generate unique file names.  The most common substitution variable is `%U`, which generates a unique name. Others include `%d` for the DB\_NAME, `%t` for the backup set time stamp, `%s` for the backup set number, and `%p` for the backup piece number. | ``` BACKUP    FORMAT 'AL_%d/%t/%s/%p'    ARCHIVELOG LIKE '%arc_dest%'; ``` |
| `TAG` | Specifies a user-defined string as a label for the backup. If you do not specify a [tag](glossary.md), then RMAN assigns a default tag with the date and time. Tags are always stored in the RMAN repository in uppercase. | ``` BACKUP   TAG 'weekly_full_db_bkup'    DATABASE MAXSETSIZE 10M; ``` |

See Also:

["Specifying Backup Output Options"](rcmbckba.md)

### Making Incremental Backups

If you specify `BACKUP` `INCREMENTAL`, then RMAN creates an [incremental backup](glossary.md) of a database. Incremental backups capture block-level changes to a database made after a previous incremental backup. Incremental backups are generally smaller and faster to make than full database backups. Recovery with incremental backups is faster than using redo logs alone.

The starting point for an incremental backup strategy is a [level 0 incremental backup](glossary.md), which backs up all blocks in the database. An incremental backup at level 0 is identical in content to a [full backup](glossary.md), however, unlike a full backup the level 0 backup is considered a part of the incremental backup strategy.

A level 1 incremental backup contains only blocks changed after a previous incremental backup. If no level 0 backup exists in either the current or parent database [incarnation](glossary.md) when you run a level 1 backup, then RMAN makes a level 0 backup automatically.

Note:

You cannot make incremental backups when a `NOARCHIVELOG` database is open, although you can make incremental backups when the database is mounted after a consistent shutdown.

A level 1 backup can be a [cumulative incremental backup](glossary.md), which includes all blocks changed since the most recent level 0 backup, or a [differential incremental backup](glossary.md), which includes only blocks changed since the most recent incremental backup. Incremental backups are differential by default.

When restoring incremental backups, RMAN uses the level 0 backup as the starting point, then updates changed blocks based on level 1 backups where possible to avoid reapplying changes from redo one at a time. Recovering with incremental backups requires no additional effort on your part. If incremental backups are available, then RMAN uses them during recovery.

To make incremental backups of the database:

1. Start RMAN and connect to a target database.
2. Run the `BACKUP INCREMENTAL` command.
	The following example creates a level 0 incremental backup to serve as a base for an incremental backup strategy:
	```
	BACKUP INCREMENTAL LEVEL 0 DATABASE;
	```
	The following example creates a level 1 cumulative incremental backup:
	```
	BACKUP INCREMENTAL LEVEL 1 CUMULATIVE DATABASE;
	```
	The following example creates a level 1 differential incremental backup:
	```
	BACKUP INCREMENTAL LEVEL 1 DATABASE;
	```

See Also:

["Incremental Backups"](rcmcncpt.md) for a more detailed conceptual overview of incremental backups and ["Making and Updating Incremental Backups"](rcmbckba.md)

#### Making Incrementally Updated Backups

The RMAN [incrementally updated backup](glossary.md) feature is an efficient incremental backup strategy. The strategy has the following main features:

- The strategy requires a level 0 data file copy as a base. This copy has either a system-defined or user-defined tag.
- Periodically, level 1 differential backups are created with the same tag as the level 0 data file copy. The `BACKUP FOR RECOVER OF COPY` command specifies that an incremental backup should contain only blocks changed since the most recent incremental backup with the same tag.
- Periodically, the incremental backups are applied to the level 0 data file copy. Because the data file copy has been updated with more recent changes, it now requires less media recovery.

Table 2-2 explains which options to use with `FOR RECOVER OF COPY` to implement an incrementally updated backup strategy.

Table 2-2 FOR RECOVER OF COPY Options

| BACKUP Option | Description | Example |
| --- | --- | --- |
| `FOR RECOVER OF COPY WITH TAG` `'` `tag_name` `'` | Use `TAG` to identify the tag of the data file copy serving as basis for the backup strategy. RMAN automatically assigns the same tag to every level 1 backup of this copy.  If no level 0 data file copy with the specified tag exists in either the current or parent database [incarnation](glossary.md), then RMAN creates a level 0 data file copy with the specified tag. | ``` BACKUP    INCREMENTAL LEVEL 1   FOR RECOVER OF COPY    WITH TAG 'incr_update'   DATABASE; ``` |
| `FOR RECOVER OF COPY DATAFILECOPY FORMAT '` `format` `'` | Specifies where RMAN creates the data file copy if a copy does not exist. If you add a new data file to the database, then you do not need to change your script, because RMAN automatically creates the level 0 copy required by the incremental backup routine. | ``` BACKUP    INCREMENTAL LEVEL 1   FOR RECOVER OF COPY   DATAFILECOPY FORMAT   '/disk2/df1.cpy'   DATABASE; ``` |

To implement an incrementally updated backup strategy:

1. Start RMAN and connect to a target database.
2. Run the `RECOVER COPY` and `BACKUP INCREMENTAL` commands.
	The following script, run on a regular basis, is all that is required to implement a strategy based on incrementally updated backups.
	```
	RECOVER COPY OF DATABASE 
	  WITH TAG 'incr_update';
	BACKUP 
	  INCREMENTAL LEVEL 1
	  FOR RECOVER OF COPY WITH TAG 'incr_update'
	  DATABASE;
	```

See Also:

["Incrementally Updating Backups"](rcmbckba.md)

### Validating Database Files and Backups

You can use the `VALIDATE` command to confirm that all database files exist, are in their correct location, and are free of physical corruption. The `CHECK LOGICAL` option also checks for logical block corruption.

To validate database files:

1. Start RMAN and connect to a target database.
2. Run the `BACKUP VALIDATE ...` command for the desired files.
	For example, enter the following commands to validate all database files and archived redo log files for physical and logical corruption:
	```
	BACKUP VALIDATE CHECK LOGICAL
	  DATABASE ARCHIVELOG ALL;
	```
	You can also use the [`VALIDATE`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta2024.htm#RCMRF162) command to check individual data blocks, as shown in the following example:
	```
	VALIDATE DATAFILE 4 BLOCK 10 TO 13;
	```
	You can also validate backup sets, as shown in the following example:
	```
	VALIDATE BACKUPSET 3;
	```
	You specify backup sets by primary key, which is shown in the output of the `LIST BACKUP` command.

See Also:

- [Chapter 16, "Validating Database Files and Backups"](rcmvalid.md)
- [Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta007.htm#RCMRF107) for `VALIDATE` command syntax and semantics

### Scripting RMAN Operations

RMAN supports the use of command files to manage recurring tasks such as weekly backups. A [command file](glossary.md) is a client-side text file containing RMAN commands, exactly as you enter them at the RMAN prompt. You can use any file extension. The [`RUN`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta2012.htm#RCMRF151) command provides a degree of flow-of-control in your scripts.

To create and run a command file:

1. Use a text editor to create a command file.
	For example, create a command file with the following contents:
	```
	# my_command_file.txt
	CONNECT TARGET /
	BACKUP DATABASE PLUS ARCHIVELOG;
	LIST BACKUP;
	EXIT;
	```
2. Start RMAN and then execute the contents of a command file by running the [`@`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta001.htm#RCMRF100) command at the RMAN prompt:
	```
	% rman
	RMAN> @/my_dir
	/my_command_file.txt
	  # runs specified command file
	```
	You can also launch RMAN with a command file to run, as shown here:
	```
	% rman @/my_dir
	/my_command_file.txt
	```

See Also:

["Using Command Files with RMAN"](rcmcnctg.md) to learn more about command files, and ["Using Substitution Variables in Command Files"](rcmcnctg.md) to learn how to use substitution variables in command files and pass parameters at run time

## Reporting on RMAN Operations

The RMAN [`LIST`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta027.htm#RCMRF132) and [`REPORT`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta2006.htm#RCMRF147) commands generate reports on backup activities based on the RMAN repository. Use the [`SHOW ALL`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta2015.htm#RCMRF154) command to display the current RMAN configuration.

### Listing Backups

Run the `LIST` `BACKUP` and `LIST` `COPY` commands to display information about backups and data file copies listed in the repository. For backups, you can control the format of `LIST` output with the options in Table 2-3 and Table 2-4.

Table 2-3 LIST Options for Backups

| Option | Example | Explanation |
| --- | --- | --- |
| `BY` `BACKUP` | `LIST` `BACKUP` `OF` `DATABASE` `BY` `BACKUP` | Organizes the output by backup set. This is the default mode of presentation. |
| `BY` `FILE` | `LIST` `BACKUP` `BY` `FILE` | Lists the backups according to which file was backed up. |
| `SUMMARY` | `LIST` `BACKUP` `SUMMARY` | Displays summary output. |

For both backups and copies you have additional options shown in Table 2-4.

Table 2-4 Additional LIST Options

| Option | Example | Explanation |
| --- | --- | --- |
| `EXPIRED` | `LIST` `EXPIRED` `COPY` | Lists backups that are recorded in the RMAN repository but that were not present at the expected location on disk or tape during the last `CROSSCHECK` command. An [expired backup](glossary.md) may have been deleted by an operating system utility. |
| `RECOVERABLE` | `LIST` `BACKUP RECOVERABLE` | Lists data file backups or copies that have status `AVAILABLE` in the RMAN repository and that can be restored and recovered. |

To list backups and copies:

1. Start RMAN and connect to a target database.
2. Run the `LIST` command at the RMAN prompt.
	You can display specific objects, as in the following examples:
	```
	LIST BACKUP OF DATABASE;
	LIST COPY OF DATAFILE 1, 2;
	LIST BACKUP OF ARCHIVELOG FROM SEQUENCE 10;
	LIST BACKUPSET OF DATAFILE 1;
	```

### Reporting on Database Files and Backups

The `REPORT` command performs more complex analysis than `LIST`. Some main options are shown in Table 2-5.

Table 2-5 REPORT Options

| Option | Example | Explanation |
| --- | --- | --- |
| `NEED` `BACKUP` | `REPORT` `NEED` `BACKUP DATABASE` | Shows which files need backing up under current retention policy. Use optional `REDUNDANCY` and `RECOVERY` `WINDOW` parameters to specify different criteria. |
| `OBSOLETE` | `REPORT` `OBSOLETE` | Lists backups that are obsolete under the configured [backup retention policy](glossary.md). Use the optional `REDUNDANCY` and `RECOVERY` `WINDOW` parameters to override the default. |
| `SCHEMA` | `REPORT` `SCHEMA` | Reports the tablespaces and data files in the database at the current time (default) or a different time. |
| `UNRECOVERABLE` | `REPORT` `UNRECOVERABLE` | Lists all data files for which an unrecoverable operation has been performed against an object in the data file since the last backup of the data file. |

To generate reports of database files and backups:

1. Start RMAN and connect to a target database.
2. Run the `REPORT` command at the RMAN prompt.
	The following example reports backups that are obsolete according to the currently configured backup retention policy:
	```
	REPORT OBSOLETE;
	```
	The following example reports the data files and temp files in the database:
	```
	REPORT SCHEMA;
	```

See Also:

["Reporting on Backups and Database Schema"](rcmreprt.md) to learn how to use the `REPORT` command for RMAN reporting

## Maintaining RMAN Backups

RMAN repository metadata is always stored in the control file of the target database. The [RMAN maintenance commands](glossary.md) use this metadata when managing backups.

### Cross-checking Backups

The [`CROSSCHECK`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta015.htm#RCMRF119) command synchronizes the logical records of RMAN backups and copies with the files on storage media. If a backup is on disk, then `CROSSCHECK` determines whether the header of the file is valid. If a backup is on tape, then RMAN queries the RMAN repository for the names and locations of the backup pieces. It is a good idea to crosscheck backups and copies before deleting them.

To crosscheck all backups and copies on disk:

1. Start RMAN and connect to a target database.
2. Run the `CROSSCHECK` command, as shown in the following example:
	```
	CROSSCHECK BACKUP;
	CROSSCHECK COPY;
	```

See Also:

["Crosschecking the RMAN Repository"](rcmmaint.md) to learn how to crosscheck RMAN backups

### Deleting Obsolete Backups

The [`DELETE`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta016.htm#RCMRF121) command removes RMAN backups and copies from disk and tape, updates the status of the files to `DELETED` in the control file repository, and removes the records from the recovery catalog (if you use a catalog). If you run RMAN interactively, and if you do not specify the `NOPROMPT` option, then `DELETE` displays a list of files and prompts for confirmation before deleting any file in the list.

The `DELETE OBSOLETE` command is particular useful because RMAN deletes backups and data file copies recorded in the RMAN repository that are obsolete, that is, no longer needed. You can use options on the `DELETE` command to specify what is obsolete or use the configured [backup retention policy](glossary.md).

To delete obsolete backups and copies:

1. Start RMAN and connect to a target database.
2. Run the `DELETE OBSOLETE` command, as shown in the following example:
	```
	DELETE OBSOLETE;
	```

See Also:

["Deleting RMAN Backups and Archived Redo Logs"](rcmmaint.md) to learn how to use the `DELETE` command

## Diagnosing and Repairing Failures with Data Recovery Advisor

The simplest way to diagnose and repair database problems is to use the [Data Recovery Advisor](glossary.md). This Oracle Database tool provides an infrastructure for diagnosing persistent data failures, presenting repair options to the user, and automatically executing repairs.

See Also:

["Overview of Data Recovery Advisor"](rcmrepai.md)

### Listing Failures and Determining Repair Options

A [failure](glossary.md) is a persistent data corruption detected by the Health Monitor. Examples include physical and logical data block corruptions and missing data files. Each failure has a [failure priority](glossary.md) and [failure status](glossary.md). The priority can be `CRITICAL`, `HIGH`, or `LOW`. The status can be `OPEN` or `CLOSED`.

You can run the [`LIST`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta027.htm#RCMRF132) `FAILURE` command to show all known failures. If failures exist, then run the [`ADVISE FAILURE`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta003.htm#RCMRF166) command in the same session to determine manual and automated repair options. The following example illustrates these two commands (sample output included).

Example 2-1 LIST FAILURE and ADVISE FAILURE

```
RMAN> LIST FAILURE;
 
List of Database Failures
=========================
 
Failure ID Priority Status    Time Detected Summary
---------- -------- --------- ------------- -------
142        HIGH     OPEN      23-APR-07     One or more non-system datafiles are missing
101        HIGH     OPEN      23-APR-07     Datafile 1: '/disk1/oradata/prod/system01.dbf' 
                                            contains one or more corrupt blocks

RMAN> ADVISE FAILURE;
 
List of Database Failures
=========================
 
Failure ID Priority Status    Time Detected Summary
---------- -------- --------- ------------- -------
142        HIGH     OPEN      23-APR-07     One or more non-system datafiles are missing
101        HIGH     OPEN      23-APR-07     Datafile 1: '/disk1/oradata/prod/system01.dbf' 
                                            contains one or more corrupt blocks
 
analyzing automatic repair options; this may take some time
using channel ORA_DISK_1
analyzing automatic repair options complete
 
Mandatory Manual Actions
========================
no manual actions available
 
Optional Manual Actions
=======================
1. If file /disk1/oradata/prod/users01.dbf was unintentionally renamed or moved, restore it
 
Automated Repair Options
========================
Option Repair Description
------ ------------------
1      Restore and recover datafile 28; Perform block media recovery of 
       block 56416 in file 1
  Strategy: The repair includes complete media recovery with no data loss
  Repair script: /disk1/oracle/log/diag/rdbms/prod/prod/hm/reco_660500184.hm
```

The `ADVISE FAILURE` output shows both manual and automated repair options. First try to fix the problem manually. If you cannot fix the problem manually, then review the automated repair section.

An automated [repair option](glossary.md) describes a server-managed repair for one or more failures. Repairs are consolidated when possible so that a single repair can fix multiple failures. The repair option indicates which repair is performed and whether data is lost by performing the repair operation.

In Example 2-1, the output indicates the file name of a repair script containing RMAN commands. If you do not want to use Data Recovery Advisor to repair the failure automatically, then you can use the script as the basis of your own recovery strategy.

See Also:

["Listing Failures"](rcmrepai.md) and ["Determining Repair Options"](rcmrepai.md)

### Repairing Failures

After running `LIST FAILURE` and `ADVISE FAILURE` in an [RMAN session](glossary.md), you can run [`REPAIR FAILURE`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta2004.htm#RCMRF199) to execute a repair option. If you execute `REPAIR FAILURE` with no other command options, then RMAN uses the first repair option of the most recent `ADVISE FAILURE` command in the current session. Alternatively, specify the repair option number obtained from the most recent `ADVISE FAILURE` command. Example 2-2 illustrates how to repair the failures identified in Example 2-1.

Example 2-2 REPAIR FAILURE

```
RMAN> REPAIR FAILURE;
```

By default, `REPAIR FAILURE` prompts for confirmation before it begins executing. After executing a repair, Data Recovery Advisor reevaluates all existing failures on the possibility that they may also have been fixed. Data Recovery Advisor always verifies that failures are still relevant and automatically closes fixed failures. If a repair fails to complete because of an error, then the error triggers a new assessment and re-evaluation of existing failures and repairs.

See Also:

["Repairing Failures"](rcmrepai.md)

## Rewinding a Database with Flashback Database

You can use the [Oracle Flashback Database](glossary.md) to rewind the whole database to a past time. Unlike media recovery, you do not need to restore data files to return the database to a past state.

To use the RMAN [`FLASHBACK DATABASE`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta023.htm#RCMRF194) command, your database must have been previously configured to generate [flashback logs](glossary.md). This configuration task is described in ["Flashback Database"](flashdb.md). Flashback Database works by rewinding changes to the data files that exist at the moment that you run the command. You cannot use the command to repair media failures or missing data files.

The database must be mounted when you issue `FLASHBACK DATABASE`. If you have previously created a [restore point](glossary.md), then you can flash back to this restore point if it falls within the [flashback database window](glossary.md).

To rewind a database with Flashback Database:

1. Start RMAN and connect to a target database.
2. Ensure that the database is in a mounted state.
	The following commands shut down and then mount the database:
	```
	SHUTDOWN IMMEDIATE;
	STARTUP MOUNT;
	```
3. Run the `FLASHBACK DATABASE` command.
	The following examples illustrate different forms of the command:
	```
	FLASHBACK DATABASE TO SCN 861150;
	FLASHBACK DATABASE 
	  TO RESTORE POINT BEFORE_CHANGES;
	FLASHBACK DATABASE    
	  TO TIMESTAMP TO_DATE(04-DEC-2009  03:30:00','DD-MON-YYYY HH24:MI:SS');
	```
4. After performing the Flashback Database, open the database read-only in SQL\*Plus and run some queries to verify the database contents.
	Open the database read-only as follows:
	```
	SQL "ALTER DATABASE OPEN READ ONLY";
	```
5. If satisfied with the results, then issue the following sequence of commands to shut down and then open the database:
	```
	SHUTDOWN IMMEDIATE;
	STARTUP MOUNT;
	ALTER DATABASE OPEN RESETLOGS;
	```

See Also:

["Rewinding a Database with Flashback Database"](rcmflash.md)

## Restoring and Recovering Database Files

Use the [`RESTORE`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta2008.htm#RCMRF149) and [`RECOVER`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta2001.htm#RCMRF140) commands for RMAN restore and recovery of physical database files. Restoring data files is retrieving them from backups as needed for a recovery operation. Media recovery is the application of changes from redo logs and incremental backups to a restored data file to bring the data file forward to a desired SCN or point in time.

See Also:

[Chapter 17, "Performing Complete Database Recovery"](rcmcomre.md)

### Preparing to Restore and Recover Database Files

If you must recover the database because a media failure damages database files, then you should first ensure that you have the necessary backups. You can use the `RESTORE ... PREVIEW` command to report, but not restore, the backups that RMAN could use to restore to the specified time. RMAN queries the metadata and does not actually read the backup files. The database can be open when you run this command.

To preview a database restore and recovery:

1. Start RMAN and connect to the target database.
2. Optionally, list the current tablespaces and data files, as shown in the following command:
	```
	RMAN> REPORT SCHEMA;
	```
3. Run the `RESTORE DATABASE` command with the `PREVIEW` option.
	The following command specifies `SUMMARY` so that the backup metadata is not displayed in verbose mode (sample output included):
	```
	RMAN> RESTORE DATABASE PREVIEW SUMMARY;
	 
	Starting restore at 21-MAY-07
	allocated channel: ORA_DISK_1
	channel ORA_DISK_1: SID=80 device type=DISK
	 
	List of Backups
	===============
	Key     TY LV S Device Type Completion Time #Pieces #Copies Compressed Tag
	------- -- -- - ----------- --------------- ------- ------- ---------- ---
	11      B  F  A DISK        18-MAY-07       1       2       NO         TAG20070518T181114
	13      B  F  A DISK        18-MAY-07       1       2       NO         TAG20070518T181114
	using channel ORA_DISK_1
	 
	List of Archived Log Copies for database with db_unique_name PROD
	=====================================================================
	 
	Key     Thrd Seq     S Low Time
	------- ---- ------- - ---------
	47      1    18      A 18-MAY-07
	        Name: /disk1/oracle/dbs/db1r_60ffa882_1_18_0622902157.arc
	 
	Media recovery start SCN is 586534
	Recovery must be done beyond SCN 587194 to clear datafile fuzziness
	validation succeeded for backup piece
	Finished restore at 21-MAY-07
	```

### Recovering the Whole Database

Use the `RESTORE` `DATABASE` and `RECOVER` `DATABASE` commands to recover the whole database. You must have previously made backups of all needed files. This scenario assumes that you can restore all data files to their original locations. If the original locations are inaccessible, then use the `SET NEWNAME` command as described in ["Restoring Datafiles to a Nondefault Location"](rcmcomre.md).

To recover the whole database:

1. Prepare for recovery as explained in "Preparing to Restore and Recover Database Files".
2. Place the database in a mounted state.
	The following example terminates the database instance (if it is started) and mounts the database:
	```
	RMAN> STARTUP FORCE MOUNT;
	```
3. Restore the database.
	The following example uses the preconfigured disk channel to restore the database:
	```
	RMAN> RESTORE DATABASE;
	```
4. Recover the database, as shown in the following example:
	```
	RMAN> RECOVER DATABASE;
	```
5. Open the database, as shown in the following example:
	```
	RMAN> ALTER DATABASE OPEN;
	```

### Recovering Tablespaces

Use the `RESTORE` `TABLESPACE` and `RECOVER` `TABLESPACE` commands on individual tablespaces when the database is open. In this case, you must take the tablespace that needs recovery offline, restore and then recover the tablespace, and bring the recovered tablespace online.

If you need to restore a data file to a new location, then use the RMAN `SET NEWNAME` command within a `RUN` command to specify the new file name. Afterward, use a `SWITCH DATAFILE ALL` command, which is equivalent to using the SQL statement `ALTER DATABASE RENAME FILE`, to update the control file to reflect the new names for all data files for which a `SET NEWNAME` has been issued in the `RUN` command.

Unlike in user-managed media recovery, you should not place an online tablespace in [backup mode](glossary.md). Unlike user-managed tools, RMAN does not require extra logging or backup mode because it knows the format of data blocks.

To recover an individual tablespace when the database is open:

1. Prepare for recovery as explained in "Preparing to Restore and Recover Database Files".
2. Take the tablespace to be recovered offline:
	The following example takes the `USERS` tablespace offline:
	```
	RMAN> SQL 'ALTER TABLESPACE users OFFLINE';
	```
3. Restore and recover the tablespace.
	The following `RUN` command, which you execute at the RMAN prompt, sets a new name for the data file in the `USERS` tablespace:
	```
	RUN
	{
	  SET NEWNAME FOR DATAFILE '/disk1/oradata/prod/users01.dbf' 
	    TO '/disk2/users01.dbf';
	  RESTORE TABLESPACE users;
	  SWITCH DATAFILE ALL;   # update control file with new file names
	  RECOVER TABLESPACE users;
	}
	```
4. Bring the tablespace online, as shown in the following example:
	```
	RMAN> SQL 'ALTER TABLESPACE users ONLINE';
	```

You can also use `RESTORE DATAFILE` and `RECOVER DATAFILE` for recovery at the data file level.

### Recovering Individual Data Blocks

RMAN can recover individual corrupted data file blocks. When RMAN performs a complete scan of a file for a backup, any corrupted blocks are listed in `V$DATABASE_BLOCK_CORRUPTION`. Corruption is usually reported in alert logs, trace files, or results of SQL queries.

To recover data blocks:

1. Obtain the block numbers of the corrupted blocks if you do not have this information.
	The easiest way to locate trace files and the alert log is to connect SQL\*Plus to the target database and execute the following query:
	```
	SQL> SELECT NAME, VALUE 
	  2  FROM V$DIAG_INFO;
	```
2. Start RMAN and connect to the target database.
3. Run the `RECOVER` command to repair the blocks.
	The following RMAN command recovers all corrupted blocks:
	```
	RMAN> RECOVER CORRUPTION LIST;
	```
	You can also recover individual blocks, as shown in the following example:
	```
	RMAN> RECOVER DATAFILE 1 BLOCK 233, 235 DATAFILE 2 BLOCK 100 TO 200;
	```