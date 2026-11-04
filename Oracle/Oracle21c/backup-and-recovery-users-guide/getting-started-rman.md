---
title: "Backup and Recovery User's Guide"
book: "Database Backup and Recovery User's Guide"
doc_id: F31836-11
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/bradv/getting-started-rman.html
tags:
  - oracle
  - 21c
  - backup-and-recovery-users-guide
---

New users can start with RMAN right away by understanding the most important RMAN concepts and learning how to perform backup and recovery tasks.

Note that the topics described in this chapter are not a substitute for the rest of the backup and recovery documentation set.

### 2.1 Overview of the RMAN Environment

Recovery Manager (RMAN) is an Oracle Database client that performs backup and recovery tasks on your databases and automates administration of your backup strategies. It greatly simplifies backing up, restoring, and recovering database files.

The RMAN environment consists of the utilities and databases that play a role in backing up your data. At a minimum, the environment for RMAN must include the following components:

- A [target database](glossary.md)
	An Oracle Database to which RMAN is connected with the `TARGET` keyword. A target database is a database on which RMAN is performing backup and recovery operations. RMAN always maintains metadata about its operations on a database in the control file of the database. The RMAN metadata is known as the [RMAN repository](glossary.md).
- The [RMAN client](glossary.md)
	An Oracle Database executable that interprets commands, directs server sessions to execute those commands, and records its activity in the target database control file. The RMAN executable is automatically installed with the database and is typically located in the same directory as the other database executables. For example, the RMAN client on Linux is located in `$ORACLE_HOME/bin`.

Some environments use the following optional components:

- A [fast recovery area](glossary.md)
	A disk location in which the database can store and manage files related to backup and recovery. You set the fast recovery area location and size with the [`DB_RECOVERY_FILE_DEST `](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=REFRN10234) and [`DB_RECOVERY_FILE_DEST_SIZE`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=REFRN10235) initialization parameters.
- A [media management software](glossary.md)
	An application required for RMAN to interact with sequential media devices such as tape libraries. A media manager controls these devices during backup and recovery, managing the loading, labeling, and unloading of media. Media management devices are sometimes called [SBT](glossary.md) (system backup to tape) devices.
- A [recovery catalog](glossary.md)
	A separate database schema used to record RMAN activity against one or more target databases. A recovery catalog preserves RMAN repository metadata if the control file is lost, making it much easier to restore and recover following the loss of the control file. The database may overwrite older records in the control file, but RMAN maintains records forever in the catalog unless the records are deleted by the user.

This chapter explains how to use RMAN in the most basic configuration, which is without a recovery catalog or media manager.

See Also:

- [Recovery Manager Architecture](rman-architecture.md) for a more detailed overview of the RMAN environment
- [Oracle Database Backup and Recovery Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=RCMRF107) for `BACKUP` command syntax and semantics

### 2.2 Starting RMAN and Connecting to a Database: Quick Start

Before you perform any operations using RMAN, you must connect to a target database.

The RMAN client is started by issuing the `rman` command at the command prompt of your operating system. RMAN displays a prompt for your commands as shown in the following example:

```
% rman
RMAN>
```

RMAN connections to a database are specified and authenticated in the same way as SQL\*Plus connections to a database. The only difference is that RMAN connections to a target or auxiliary database require either the `SYSDBA` or `SYSBACKUP` privilege. Any user can be granted this privilege.

Caution:

Good security practice requires that you not enter passwords in plain text on the command line. Enter passwords in RMAN only when requested by an RMAN prompt. See [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=DBSEG0032) to learn about password protection.

Note:

For RMAN operations, auditing is always enabled, by default, in the unified auditing mode. However, auditing is disabled if you using a mixed mode auditing environment. See Oracle Database Security Guide to learn more about auditing.

You can connect to a database with command-line options or by using the [`CONNECT TARGET`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=RCMRF114) command. The following example starts RMAN and then connects to a target database through Oracle Net as user `sbu`, which is created with the `SYSBACKUP` privilege. RMAN prompts for a password.

```
% rman
RMAN> CONNECT TARGET "sbu@prod AS SYSBACKUP"

target database Password: password
connected to target database: PROD (DBID=39525561)
```

When using the multitenant architecture, you can connect to the root or to a specified pluggable database (PDB) as described in " [Making Database Connections with RMAN](starting-interacting-with-rman-client.md) ".

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

The following example appends the output from an RMAN session to a text file at `/tmp/msglog.log`

```
% rman TARGET / LOG /tmp/msglog.log APPEND
```

Caution:

If the Oracle Database Windows services is running with a LP user, then you must manually grant the permissions required for the LP user to access the Oracle wallet. Otherwise, RMAN returns the ORA-28759 error message.

See Also:

[Starting and Interacting with the RMAN Client](starting-interacting-with-rman-client.md), to learn more about starting and using the RMAN client

### 2.3 Showing the Default RMAN Configuration

The RMAN backup and recovery environment is preconfigured for each target database. The configuration is persistent and applies to all subsequent operations on this target database, even if you exit and restart RMAN.

RMAN configuration settings can specify backup devices, set up connections to those devices (known as [channel](glossary.md) s), set policies affecting backup strategy, and more.

To show the current configuration for a database:

1. Start RMAN and connect to a target database as described in " Starting RMAN and Connecting to a Database ".
2. Run the `SHOW ALL` command.
	For example, enter the command at the RMAN prompt as follows:
	```
	RMAN> SHOW ALL;
	```

The output lists the `CONFIGURE` commands to re-create this configuration.

See Also:

[Configuring the RMAN Environment](configuring-rman-client-basic.md), and [Configuring the RMAN Environment: Advanced Topics](configuring-rman-client-advanced.md), to learn how to configure the RMAN environment

### 2.4 Backing Up a Database: Quick Start

Use the BACKUP command to back up files. RMAN backs up data to the configured default device for the type of backup requested.

By default, RMAN creates backups on disk. If a fast recovery area is enabled, and if you do not specify the `FORMAT` parameter (see Table 2-1), then RMAN creates backups in the recovery area and automatically gives them unique names.

By default, RMAN creates backup sets rather than image copies. A [backup set](glossary.md) consists of one or more backup pieces, which are physical files written in a format that only RMAN can access. A [multiplexed backup set](glossary.md) contains the blocks from multiple input files. RMAN can write backup sets to disk or tape.

If you specify `BACKUP` `AS` `COPY`, then RMAN copies each file as an [image copy](glossary.md), which is a bit-for-bit copy of a database file created on disk. Image copies are identical to copies created with operating system commands like `cp` on Linux or `COPY` on Windows, but are recorded in the RMAN repository and so are usable by RMAN. You can use RMAN to make image copies while the database is open.

The following sections describe backing up databases in different modes:

See Also:

- [RMAN Backup Concepts](rman-backup-concepts.md), to learn concepts relating to RMAN backups
- [Backing Up the Database](backing-up-database.md), to learn how to back up database files with RMAN
- [Oracle Database Backup and Recovery Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=RCMRF107) for `BACKUP` command syntax and semantics

#### 2.4.1 About Typical RMAN Backup Options

The `BACKUP` command includes a host of options, parameters, and clauses that control backup output.

Table 2-1 lists some typical backup options.

Table 2-1 Common Backup Options

| Option | Description | Example |
| --- | --- | --- |
| `FORMAT` | Specifies a location and name for backup pieces and copies. You must use substitution variables to generate unique file names.  The most common substitution variable is `%U`, which generates a unique name. Others include `%d` for the DB\_NAME, `%t` for the backup set time stamp, `%s` for the backup set number, and `%p` for the backup piece number. | ``` BACKUP    FORMAT 'AL_%d/%t/%s/%p'    ARCHIVELOG LIKE '%arc_dest%'; ``` |
| `TAG` | Specifies a user-defined string as a label for the backup. If you do not specify a [tag](glossary.md), then RMAN assigns a default tag with the date and time. Tags are always stored in the RMAN repository in uppercase. | ``` BACKUP   TAG 'weekly_full_db_bkup'    DATABASE MAXSETSIZE 10M; ``` |

See Also:

- " [Specifying Backup Output Options](backing-up-database.md) "
- [Oracle Database Backup and Recovery Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=RCMRF195) for information about the format options

#### 2.4.2 Backing Up a Database in ARCHIVELOG Mode

If a database runs in `ARCHIVELOG` mode, then you can back up the database while it is open.

A backup is called an [inconsistent backup](glossary.md) if it contains changes after its checkpoint. If you have the archived redo logs needed to recover the backup, open database backups are as effective for data protection as consistent backups.

To back up the database and archived redo logs while the database is open:

1. Start RMAN and connect to a target database as described in " Starting RMAN and Connecting to a Database ".
2. Run the `BACKUP DATABASE` command.
	For example, enter the following command at the RMAN prompt to back up the database and all archived redo log files to the default backup device:
	```
	RMAN> BACKUP DATABASE PLUS ARCHIVELOG;
	```

#### 2.4.3 Backing Up a Database in NOARCHIVELOG Mode

If a database runs in `NOARCHIVELOG` mode, then the only valid database backup is a consistent backup.

For the backup to be consistent, the database must be mounted after a consistent shutdown. Recovery is not specifically required after restoring the backup, but you would lose any transactions made after the backup. You can recover with archived logs from a [consistent backup](glossary.md) to minimize data loss.

To make a consistent database backup:

1. Start RMAN and connect to a target database as described in " Starting RMAN and Connecting to a Database ".
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

#### 2.4.4 Making Incremental Backups: Quick Start

Incremental backups capture block-level changes to a database made after a previous incremental backup.

If you specify `BACKUP` `INCREMENTAL`, then RMAN creates an [incremental backup](glossary.md) of a database. Incremental backups are generally smaller and faster to make than full database backups. Recovery with incremental backups is faster than using redo logs alone.

The starting point for an incremental backup strategy is a [level 0 incremental backup](glossary.md), which backs up all blocks in the database. An incremental backup at level 0 is identical in content to a [full backup](glossary.md), however, unlike a full backup the level 0 backup is considered a part of the incremental backup strategy.

A level 1 incremental backup contains only blocks changed after a previous incremental backup. If no level 0 backup exists in either the current or parent database [incarnation](glossary.md) when you run a level 1 backup, then RMAN makes a level 0 backup automatically.

Note:

You cannot make incremental backups when a `NOARCHIVELOG` database is open, although you can make incremental backups when the database is mounted after a consistent shutdown.

A level 1 backup can be a [cumulative incremental backup](glossary.md), which includes all blocks changed since the most recent level 0 backup, or a [differential incremental backup](glossary.md), which includes only blocks changed since the most recent incremental backup. Incremental backups are differential by default.

During a restore operation, RMAN will first restore a level 0 backup, then automatically apply incremental backups and redo logs as needed. This will re-apply the changes that were made to the database since the start of the backup.

To make incremental backups of the database:

1. Start RMAN and connect to a target database as described in " Starting RMAN and Connecting to a Database ".
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

" [About RMAN Incremental Backups](rman-backup-concepts.md) " for a more detailed conceptual overview of incremental backups and " [Making and Updating RMAN Incremental Backups](backing-up-database.md) "

#### 2.4.5 Making Incrementally Updated Backups

Incrementally updated backups enable you to implement an efficient incremental forever backup strategy.

The RMAN [incrementally updated backup](glossary.md) feature has the following main features:

- The strategy requires a level 0 data file copy as a base. This copy has either a system-defined or user-defined tag.
- Periodically, level 1 differential backups are created with the same tag as the level 0 data file copy. The `BACKUP FOR RECOVER OF COPY` command specifies that an incremental backup contains only blocks changed since the most recent incremental backup with the same tag.
- Periodically, the incremental backups are applied to the level 0 data file copy. Because the data file copy has been updated with more recent changes, it now requires less media recovery.

Table 2-2 explains which options to use with `FOR RECOVER OF COPY` to implement an incrementally updated backup strategy.

Table 2-2 FOR RECOVER OF COPY Options

| BACKUP Option | Description | Example |
| --- | --- | --- |
| `FOR RECOVER OF COPY WITH TAG` ` '` `tag_name` `'` | Use `TAG` to identify the tag of the data file copy serving as basis for the backup strategy. RMAN automatically assigns the same tag to every level 1 backup of this copy.  If no level 0 data file copy with the specified tag exists in either the current or parent database [incarnation](glossary.md), then RMAN creates a level 0 data file copy with the specified tag. | ``` BACKUP    INCREMENTAL LEVEL 1   FOR RECOVER OF COPY    WITH TAG 'incr_update'   DATABASE; ``` |
| `FOR RECOVER OF COPY DATAFILECOPY FORMAT '` `format` `'` | Specifies where RMAN creates the data file copy if a copy does not exist. If you add a new data file to the database, then you do not need to change your script, because RMAN automatically creates the level 0 copy required by the incremental backup routine. | ``` BACKUP    INCREMENTAL LEVEL 1   FOR RECOVER OF COPY   DATAFILECOPY FORMAT   '/disk2/df1.cpy'   DATABASE; ``` |

To implement an incrementally updated backup strategy:

1. Start RMAN and connect to a target database as described in " Starting RMAN and Connecting to a Database ".
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

" [Incrementally Updating Backups](backing-up-database.md) "

#### 2.4.6 Validating Database Files and Backups: Quick Start

RMAN validation checks a backup to determine whether it can be restored. Validation also checks for corrupt blocks and missing files.

Use the `VALIDATE` command to confirm that all database files exist, are in their correct location, and are free of physical corruption. The `CHECK LOGICAL` option also checks for logical block corruption.

To validate database files:

1. Start RMAN and connect to a target database as described in " Starting RMAN and Connecting to a Database ".
2. Run the `BACKUP VALIDATE ...` command for the desired files.
	For example, enter the following commands to validate all database files and archived redo log files for physical and logical corruption:
	```
	BACKUP VALIDATE CHECK LOGICAL
	  DATABASE ARCHIVELOG ALL;
	```
	You can also use the [`VALIDATE`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=RCMRF162) command to check individual data blocks, as shown in the following example:
	```
	VALIDATE DATAFILE 4 BLOCK 10 TO 13;
	```
	You can also validate backup sets, as shown in the following example:
	```
	VALIDATE BACKUPSET 3;
	```
	You specify backup sets by primary key, which is shown in the output of the `LIST BACKUP` command.

See Also:

- [Validating Database Files and Backups](validating-database-files-backups.md)
- [Oracle Database Backup and Recovery Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=RCMRF107) for `VALIDATE` command syntax and semantics

#### 2.4.7 Scripting RMAN Operations

RMAN supports the use of command files to manage recurring tasks such as weekly backups.

A [command file](glossary.md) is a client-side text file containing RMAN commands, exactly as you enter them at the RMAN prompt. You can use any file extension.

Stored scripts are an alternative to command files that allow scripts to be available to any RMAN client that can connect to the target database and its recovery catalog.

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
2. Start RMAN and then execute the contents of a command file by running the [`@`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=RCMRF100) command at the RMAN prompt:
	```
	@/my_dir/my_command_file.txt  # runs specified command file
	```
	You can also start RMAN with a command file to run, as shown here:
	```
	% rman @/my_dir/my_command_file.txt
	```

See Also:

- " [Using Command Files with RMAN](starting-interacting-with-rman-client.md) " to learn more about command files
- " [Using Substitution Variables in Command Files](starting-interacting-with-rman-client.md) " to learn how to use substitution variables in command files and pass parameters at run time

### 2.5 Reporting on RMAN Operations: Quick Start

RMAN can use the information stored in the RMAN repository to generate reports on backup activities.

Use the RMAN [`LIST`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=RCMRF132) and [`REPORT`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=RCMRF147) commands for reporting on backup operations. Use the [`SHOW ALL`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=RCMRF154) command to display the current RMAN configuration. In addition, RMAN provides a comprehensive set of views for generating custom reports.

This section contains the following topics:

- Listing Backups
- Reporting on Database Files and Backups

#### 2.5.1 Listing Backups: Quick Start

The `LIST` `BACKUP` and `LIST` `COPY` commands display information about backups and data file copies listed in the repository.

For backups, you can control the format of `LIST` output with the options in Table 2-3 and Table 2-4.

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

1. Start RMAN and connect to a target database as described in " Starting RMAN and Connecting to a Database ".
2. Run the `LIST` command at the RMAN prompt.
	You can display specific objects, as in the following examples:
	```
	LIST BACKUP OF DATABASE;
	LIST COPY OF DATAFILE 1, 2;
	LIST BACKUP OF ARCHIVELOG FROM SEQUENCE 10;
	LIST BACKUPSET OF DATAFILE 1;
	```

#### 2.5.2 Reporting on Database Files and Backups: Quick Start

The `REPORT` command performs more complex reporting analysis than the `LIST` command.

Table 2-5 displays some of the main options of the REPORT command.

Table 2-5 REPORT Options

| Option | Example | Explanation |
| --- | --- | --- |
| `NEED` `BACKUP` | `REPORT` `NEED` `BACKUP DATABASE` | Shows which files need backing up under current retention policy. Use optional `REDUNDANCY` and `RECOVERY` `WINDOW` parameters to specify different criteria. |
| `OBSOLETE` | `REPORT` `OBSOLETE` | Lists backups that are obsolete under the configured [backup retention policy](glossary.md). Use the optional `REDUNDANCY` and `RECOVERY` `WINDOW` parameters to override the default. |
| `SCHEMA` | `REPORT` `SCHEMA` | Reports the tablespaces and data files in the database at the current time (default) or a different time. |
| `UNRECOVERABLE` | `REPORT` `UNRECOVERABLE` | Lists all data files for which an unrecoverable operation has been performed against an object in the data file since the last backup of the data file. |

To generate reports of database files and backups:

1. Start RMAN and connect to a target database as described in " Starting RMAN and Connecting to a Database ".
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

" [Reporting on Backups and Database Schema](reporting-rman-operations.md) " to learn how to use the `REPORT` command for RMAN reporting

### 2.6 Maintaining RMAN Backups

RMAN repository metadata is always stored in the control file of the target database. The RMAN maintenance commands use this metadata when managing backups.

This section contains the following topics:

- Cross-checking Backups
- Deleting Obsolete Backups

#### 2.6.1 Cross-checking Backups: Quick Start

Use the `CROSSCHECK` command to synchronize the logical records of RMAN backups and copies with the files on storage media.

If a backup is on disk, then `CROSSCHECK` determines whether the header of the file is valid. If a backup is on tape, then RMAN queries the RMAN repository for the names and locations of the backup pieces. It is a good idea to crosscheck backups and copies before deleting them.

To crosscheck all backups and copies on disk:

1. Start RMAN and connect to a target database as described in " Starting RMAN and Connecting to a Database ".
2. Run the `CROSSCHECK` command, as shown in the following example:
	```
	CROSSCHECK BACKUP;
	CROSSCHECK COPY;
	```

See Also:

" [Crosschecking the RMAN Repository](maintaining-rman-backups.md) " to learn how to crosscheck RMAN backups

#### 2.6.2 Deleting Obsolete Backups: Quick Start

The DELETE command removes RMAN backups and copies from disk and tape, updates the status of the files to `DELETED` in the control file repository, and removes the records from the recovery catalog (if you use a catalog).

If you run RMAN interactively, and if you do not specify the `NOPROMPT` option, then `DELETE` displays a list of files and prompts for confirmation before deleting any file in the list. The `DELETE OBSOLETE` command is particular useful because RMAN deletes backups and data file copies recorded in the RMAN repository that are obsolete, that is, no longer needed. You can use options on the `DELETE` command to specify what is obsolete or use the configured [backup retention policy](glossary.md).

To delete obsolete backups and copies:

1. Start RMAN and connect to a target database as described in " Starting RMAN and Connecting to a Database ".
2. Run the `DELETE OBSOLETE` command, as shown in the following example:
	```
	DELETE OBSOLETE;
	```

See Also:

" [Deleting RMAN Backups and Archived Redo Logs](maintaining-rman-backups.md) " to learn how to use the `DELETE` command

### 2.7 Diagnosing and Repairing Failures with Data Recovery Advisor: Quick Start

Data Recovery Advisor is an Oracle Database tool that provides an infrastructure for diagnosing persistent data failures, presenting repair options to the user, and executes repairs at the user’s request.

This section contains the following topics:

- Listing Failures and Determining Repair Options
- Repairing Failures

Note:

Starting in Oracle Database 19c, the Data Recovery Advisor (DRA) feature is deprecated.

The deprecation of DRA includes deprecation of the following Oracle Recovery Manager (RMAN) commands: `LIST FAILURE`, `ADVISE FAILURE`, `REPAIR                     FAILURE`, and `CHANGE FAILURE`. Database administrators will no longer have access to these commands. There is no replacement feature for DRA.

See Also:

" [Overview of Data Recovery Advisor](diagnosing-repairing-failures-dra.md) "

#### 2.7.1 Listing Failures and Determining Repair Options

A failure is a persistent data corruption detected by the Health Monitor. Examples include physical and logical data block corruptions and missing data files.

Each failure has a [failure priority](glossary.md) and [failure status](glossary.md). The priority can be `CRITICAL`, `HIGH`, or `LOW`. The status can be `OPEN` or `CLOSED`.

You can run the [`LIST`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=RCMRF132) `FAILURE` command to show all known failures. If failures exist, then run the [`ADVISE FAILURE`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=RCMRF166) command in the same session to determine repair options. The `ADVISE FAILURE` output shows both manual and automated repair options. First try to fix the problem manually. If you cannot fix the problem manually, then review the automated repair section.

An automated [repair option](glossary.md) describes a server-managed repair for one or more failures. Repairs are consolidated when possible so that a single repair can fix multiple failures. The repair option indicates which repair is performed and whether data is lost by performing the repair operation.

Note:

Starting in Oracle Database 19c, the Data Recovery Advisor (DRA) feature is deprecated.

The deprecation of DRA includes deprecation of the following Oracle Recovery Manager (RMAN) commands: `LIST FAILURE`, `ADVISE FAILURE`, `REPAIR                     FAILURE`, and `CHANGE FAILURE`. Database administrators will no longer have access to these commands. There is no replacement feature for DRA.

See Also:

" [Listing Failures](diagnosing-repairing-failures-dra.md) " and " [Determining Repair Options](diagnosing-repairing-failures-dra.md) "

Listing Failures and Determining Repair Options illustrates the commands to list failures and determine repair options. The output indicates the file name of a repair script containing RMAN commands. If you do not want to use Data Recovery Advisor to repair the failure automatically, then you can use the script as the basis of your own recovery strategy.

Example 2-1 LIST FAILURE and ADVISE FAILURE

```
RMAN> LIST FAILURE;
 
Database Role: PRIMARY
List of Database Failures
=========================
 
Failure ID Priority Status    Time Detected Summary
---------- -------- --------- ------------- -------
142        HIGH     OPEN      23-APR-13     One or more non-system datafiles are missing
101        HIGH     OPEN      23-APR-13     Datafile 1: '/disk1/oradata/prod/system01.dbf' 
                                            contains one or more corrupt blocks

RMAN> ADVISE FAILURE;
 
Database Role: PRIMARY
List of Database Failures
=========================
 
Failure ID Priority Status    Time Detected Summary
---------- -------- --------- ------------- -------
142        HIGH     OPEN      23-APR-13     One or more non-system datafiles are missing
101        HIGH     OPEN      23-APR-13     Datafile 1: '/disk1/oradata/prod/system01.dbf' 
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

#### 2.7.2 Repairing Failures: Quick Start

Use the RMAN `REPAIR FAILURE` command to repair failures that were detected.

After running `LIST FAILURE` and `ADVISE FAILURE` in an [RMAN session](glossary.md), you can run [`REPAIR FAILURE`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=RCMRF199) to execute a repair option. If you execute `REPAIR FAILURE` with no other command options, then RMAN uses the first repair option of the most recent `ADVISE FAILURE` command in the current session. Alternatively, specify the repair option number obtained from the most recent `ADVISE FAILURE` command. The following example illustrates how to repair the failures identified in Example 2-1.

```
RMAN> REPAIR FAILURE;
```

By default, `REPAIR FAILURE` prompts for confirmation before it begins executing. After executing a repair, Data Recovery Advisor reevaluates all existing failures on the possibility that they may also have been fixed. Data Recovery Advisor always verifies that failures are still relevant and automatically closes fixed failures. If a repair fails to complete because of an error, then the error triggers a new assessment and re-evaluation of existing failures and repairs.

Note:

Starting in Oracle Database 19c, the Data Recovery Advisor (DRA) feature is deprecated.

The deprecation of DRA includes deprecation of the following Oracle Recovery Manager (RMAN) commands: `LIST FAILURE`, `ADVISE FAILURE`, `REPAIR                     FAILURE`, and `CHANGE FAILURE`. Database administrators will no longer have access to these commands. There is no replacement feature for DRA.

See Also:

" [Repairing Failures](diagnosing-repairing-failures-dra.md) "

### 2.8 Rewinding a Database with Flashback Database: Quick Start

You can use the Oracle Flashback Database to rewind the whole database to a past time. Unlike media recovery, you do not need to restore data files to return the database to a past state.

To use the RMAN [`FLASHBACK DATABASE`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=RCMRF194) command, your database must have been previously configured to generate [flashback logs](glossary.md). This configuration task is described in " [About Flashback Database](using-flasback-database-restore-points.md) ". Flashback Database works by rewinding changes to the data files that exist at the moment that you run the command. You cannot use the flashback database to repair media failures or missing data files.

The database must be mounted when you issue `FLASHBACK DATABASE`. You can flashback to any time within the [flashback database window](glossary.md). If you have previously created a [restore point](glossary.md), that is a convenience, but not required.

To rewind a database with Flashback Database:

1. Start RMAN and connect to a target database as described in " Starting RMAN and Connecting to a Database ".
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
	ALTER DATABASE OPEN READ ONLY;
	```
5. If satisfied with the results, then issue the following sequence of commands to shut down and then open the database:
	```
	SHUTDOWN IMMEDIATE;
	STARTUP MOUNT;
	ALTER DATABASE OPEN RESETLOGS;
	```

See Also:

" [Rewinding a Database with Flashback Database](rman-performing-flashback-dbpitr.md) "

### 2.9 Restoring and Recovering Database Files: Quick Start

Use the `RESTORE` and `RECOVER` commands for RMAN restore and recovery of physical database files.

Restoring data files is retrieving them from backups as needed for a recovery operation. Media recovery is the application of changes from redo logs and incremental backups to a restored data file to bring the data file forward to a desired SCN or point in time.

This section contains the following topics:

- Preparing to Restore and Recover Database Files
- Recovering the Whole Database
- Recovering Tablespaces
- Recovering Individual Data Blocks

See Also:

[Performing Complete Database Recovery](rman-complete-database-recovery.md)

#### 2.9.1 Preparing to Restore and Recover Database Files: Quick Start

To recover the database because a media failure damages database files, then first ensure that you have the necessary backups.

You can use the `RESTORE ... PREVIEW` command to report, but not restore, the backups that RMAN can use to restore to the specified time. RMAN queries the metadata and does not actually read the backup files. The database can be open when you run this command.

To preview a database restore and recovery:

1. Start RMAN and connect to the target database as described in " Starting RMAN and Connecting to a Database ".
2. Optionally, list the current tablespaces and data files, as shown in the following command:
	```
	RMAN> REPORT SCHEMA;
	```
3. Run the `RESTORE DATABASE` command with the `PREVIEW` option.
	The following command specifies `SUMMARY` so that the backup metadata is not displayed in verbose mode (sample output included):
	```
	RMAN> RESTORE DATABASE PREVIEW SUMMARY;
	 
	Starting restore at 21-MAY-13
	allocated channel: ORA_DISK_1
	channel ORA_DISK_1: SID=80 device type=DISK
	 
	List of Backups
	===============
	Key     TY LV S Device Type Completion Time #Pieces #Copies Compressed Tag
	------- -- -- - ----------- --------------- ------- ------- ---------- ---
	11      B  F  A DISK        18-MAY-13       1       2       NO         TAG20070518T181114
	13      B  F  A DISK        18-MAY-13       1       2       NO         TAG20070518T181114
	using channel ORA_DISK_1
	 
	List of Archived Log Copies for database with db_unique_name PROD
	=====================================================================
	 
	Key     Thrd Seq     S Low Time
	------- ---- ------- - ---------
	47      1    18      A 18-MAY-13
	        Name: /disk1/oracle/dbs/db1r_60ffa882_1_18_0622902157.arc
	 
	Media recovery start SCN is 586534
	Recovery must be done beyond SCN 587194 to clear datafile fuzziness
	validation succeeded for backup piece
	Finished restore at 21-MAY-13
	```

#### 2.9.2 Recovering the Whole Database: Quick Start

Use the `RESTORE` `DATABASE` and `RECOVER` `DATABASE` commands to recover the whole database.

You must have previously made backups of all needed files. This scenario assumes that you can restore all data files to their original locations. If the original locations are inaccessible, then use the `SET NEWNAME` command as described in " [About Restoring Data Files to a Nondefault Location](rman-complete-database-recovery.md) ".

To recover the whole database:

1. Prepare for recovery as explained in " Preparing to Restore and Recover Database Files ".
2. Place the database in a mounted state.
	The following example terminates the database instance (if it is started) and mounts the database:
	```
	RMAN> STARTUP FORCE MOUNT;
	```
3. The following example uses the preconfigured disk channel to restore the database:
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

#### 2.9.3 Recovering Tablespaces: Quick Start

Use the `RESTORE` `TABLESPACE` and `RECOVER` `TABLESPACE` commands on individual tablespaces when the database is open. In this case, you must take the tablespace that needs recovery offline, restore and then recover the tablespace, and bring the recovered tablespace online.

If you cannot restore a data file to its original location, then use the RMAN `SET NEWNAME` command within a `RUN` block to specify the new file name and location. Afterward, use a `SWITCH DATAFILE ALL` command to update the control file to reflect the new names for all data files for which a `SET           NEWNAME` has been issued in the `RUN` command.

Unlike user-managed media recovery, you do not place an online tablespace in [backup mode](glossary.md). RMAN does not require extra logging or backup mode because it knows the format of data blocks.

To recover an individual tablespace when the database is open:

1. Prepare for recovery as explained in " Preparing to Restore and Recover Database Files ".
2. Take the tablespace to be recovered offline.
	The following example takes the `USERS` tablespace offline:
	```
	RMAN> ALTER TABLESPACE users OFFLINE;
	```
3. The following `RUN` command, which you execute at the RMAN prompt, sets a new name for the data file in the `USERS` tablespace:
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
	RMAN> ALTER TABLESPACE users ONLINE;
	```

You can also use `RESTORE DATAFILE` and `RECOVER DATAFILE` for recovery at the data file level.

See Also:

- " [Performing Complete Recovery of a Tablespace](rman-complete-database-recovery.md) "
- " [About Online Backups and Backup Mode](rman-backup-concepts.md) "

#### 2.9.4 Recovering Individual Data Blocks: Quick Start

RMAN can recover individual corrupted data file blocks.

When RMAN performs a complete scan of a file for a backup, any corrupted blocks are listed in `V$DATABASE_BLOCK_CORRUPTION`. Corruption is usually reported in alert logs, trace files, or results of SQL queries.

To recover data blocks:

1. Start RMAN and connect to the target database as described in " Starting RMAN and Connecting to a Database ".
2. Obtain the block numbers of the corrupted blocks if you do not have this information.
	```
	RMAN> SELECT NAME, VALUE FROM V$DIAG_INFO;
	```
3. Run the `RECOVER` command to repair the blocks.
	The following RMAN command recovers all corrupted blocks:
	```
	RMAN> RECOVER CORRUPTION LIST;
	```
	You can also recover individual blocks, as shown in the following example:
	```
	RMAN> RECOVER DATAFILE 1 BLOCK 233, 235 DATAFILE 2 BLOCK 100 TO 200;
	```

See Also:

[Performing Block Media Recovery](rman-block-media-recovery.md)