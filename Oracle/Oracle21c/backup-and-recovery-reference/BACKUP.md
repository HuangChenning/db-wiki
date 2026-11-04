---
title: Backup and Recovery Reference
book: Database Backup and Recovery Reference
doc_id: F31837-09
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/rcmrf/BACKUP.html
tags:
  - oracle
  - 21c
  - backup-and-recovery-reference
---

Purpose

Use the `BACKUP` command to back up a primary or standby database, the root, one or more pluggable databases (PDBs), tablespace, data file (current or copy), control file (current or copy), server parameter file, archived redo log file, or backup set.

Prerequisites

RMAN must be connected to a target database. See the `CONNECT` and `RMAN` commands to learn how to connect to a database as `TARGET`.

Database Archiving Modes

If the target database is in `ARCHIVELOG` mode, then the database must be mounted or open with a current control file. Backups made while the database is open are inconsistent. You must apply redo log files after restoring an inconsistent backup to make the database consistent.

If the target database is in `NOARCHIVELOG` mode, then the database must be mounted after a consistent shutdown when you make the backup. The shutdown is only consistent if you successfully execute the `SHUTDOWN` command with the `NORMAL`, `IMMEDIATE`, or `TRANSACTIONAL` options. You cannot use RMAN to back up a `NOARCHIVELOG` database after an instance failure or `SHUTDOWN ABORT`.

Encrypted Backups

To create encrypted backups using a password-based software keystore, you must have the `SYSBACKUP` and `SYSKM` privileges. The SYSKM privilege is required to.

Backing Up Data for Cross-Platform Transport

To create backup sets that transport data to another platform, the `COMPATIBLE` parameter in the target database must be 12.0.0 or higher.

To back up the entire database for cross-platform transport, the source and destination platform must use the same endian format. The source database must be open in read-only mode.

While backing up tablespaces for cross-platform transport, if the `ALLOW INCONSISTENT` clause is not used, the tablespaces must be in read-only mode.

Preplugin Backups

- The `COMPATIBLE` initialization parameter must be set to 18.0.0 or higher on both the source and destination CDB.
- The source database must be in `ARCHIVELOG` mode.
- The source database must be in read-write mode.
- The backup location containing the preplugin backups must be accessible to the destination database.

Backup Media

RMAN can only back up files onto valid media. If you specify `DEVICE TYPE DISK`, then RMAN makes backups to random access disks. You can make a backup on any device that can store a data file. If the statement `CREATE TABLESPACE` `tablespace_name` `DATAFILE` `'` `filename` `'` works, then `'` `filename` `'` is a valid backup path name. If you specify `DEVICE TYPE sbt`, then you can back up files to any media supported by the media manager.

When backing up Oracle Database files to disk, the logical block size of the files must be an even multiple of the physical block size of the destination device. For example, a disk device with a block size of 2 KB can only be used as a destination for backups of Oracle files with logical block sizes of 2 KB, 4 KB, 6 KB and so on. In practice, most disk drives have physical block sizes of 512 bytes, so this limitation rarely affects backup. However, you can encounter this limitation when using `BACKUP ... DEVICE TYPE           DISK` to back your database up to a writeable CD or DVD, or some other device that has a larger physical block size.

Channels

If no automatic channel is configured for the specified device type, then you must manually allocate a channel for each `BACKUP` execution. If no manual channel is allocated, then RMAN uses the default channels set with the `CONFIGURE` command. RMAN has a `DISK` channel preconfigured but no preconfigured `sbt` channels.

Note:

Backups that use the disk test API are not supported for production backups. Instead, use the preconfigured `DISK` channel or manually allocate a `DISK` channel.

Usage Notes

RMAN can only back up data files, control files, server parameter files, archived redo log files, and RMAN backups of these files. RMAN cannot make backups of other database-related files such as network configuration files, password files, the block change tracking file, and the contents of the Oracle home directory. Likewise, some features of Oracle Database, such as external tables or the `BFILE` data type, store data in files other than those in the preceding list. RMAN cannot back up these files.

RMAN decomposes a `BACKUP` command into multiple independent backup steps. RMAN can execute each independent step on any channel allocated for a specific device. If multiple channels are allocated, and if one channel fails or encounters a problem during a backup step, then RMAN attempts to complete the work on another channel. RMAN reports a message in `V$RMAN_OUTPUT` and in the output to the interactive session or log file when channel failover occurs.

RMAN backups made on one platform can be transported to a different platform only if you use either the `FOR TRANSPORT` or `TO PLATFORM` clause while creating the backup.

RMAN backups made in a previous release of Oracle Database are usable after a database migration or upgrade. See My Oracle Support Note 790559.1 at [`https://support.oracle.com/rs?type=doc&id=790559.1`](https://support.oracle.com/rs?type=doc&id=790559.1) for information about this procedure.

If you change the `DB_NAME` for a database, but not its DBID, then RMAN considers backups made of the database with the previous `DB_NAME` as eligible to be restored.

Incremental Backups

An `INCREMENTAL` backup at level 0 backs up all data blocks in data files being backed up. An incremental backup at level 0 is identical in content to a `FULL` backup, but unlike a full backup the level 0 backup is a part of the incremental backup strategy.

A level 1 backup copies only changed blocks. A level 1 incremental backup is either differential or `CUMULATIVE`. If cumulative, RMAN backs up all blocks changed since the most recent level 0 backup. If differential, RMAN backs up blocks updated since the most recent level 0 or level 1 incremental backup. You can apply a level 1 backup of a standby database to a level 0 backup of a primary database, and also apply a level 1 backup of a primary database to a level 0 backup of a standby database.

Incremental backups at level 0 can be either backup sets or image copies, but incremental backups at level 1 can only be backup sets.

The database performs checks when attempting to create a level 1 incremental backup to ensure that the incremental backup is usable by a subsequent `RECOVER` command. Among the checks performed are:

- A level 0 backup must exist for each data file in the `BACKUP` command as the base backup for an incremental strategy. Level 0 backups must not have status `UNAVAILABLE`. If no level 0 backup exists, then RMAN makes a level 0 backup automatically.
- Sufficient incremental backups taken since level 0 must exist and be available such that the incremental backup to be created is usable.

Note:

When creating an incremental backup, RMAN considers backups from parent incarnations as valid. For example, assume you make a level 0 backup and then `OPEN RESETLOGS`. If you make a level 1 incremental backup, then RMAN backs up all blocks changed since the pre- `RESETLOGS` level 0 backup. When making a level 1 backup, RMAN only makes a new level 0 backup if no level 0 is available in either the current or parent database incarnation.

You can improve incremental backup performance by enabling block change tracking on a primary or standby database. In this case, RMAN keeps a record of which blocks have changed in the block change tracking file.

The change tracking file maintains bitmaps that mark changes in the data files between backups. The database performs a bitmap switch before each backup. Oracle Database automatically manages space in the change tracking file to retain block change data that covers the 8 most recent backups. After the maximum of 8 bitmaps is reached, the most recent bitmap is overwritten by the bitmap that tracks the current changes.

The first level 0 incremental backup scans the entire data file. Subsequent incremental backups use the block change tracking file to scan only the blocks that have been marked as changed since the last backup. An incremental backup can be optimized only when it is based on a parent backup that was made after the start of the oldest bitmap in the block change tracking file.

Consider the 8-bitmap limit when developing your incremental backup strategy. For example, if you make a level 0 database backup followed by 7 differential incremental backups, then the block change tracking file now includes 8 bitmaps. If you then make a cumulative level 1 incremental backup, RMAN cannot optimize the backup because the bitmap corresponding to the parent level 0 backup is overwritten with the bitmap that tracks the current changes.

See Also:

[Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/rcmrf&id=BRADV8125) for details about block change tracking

Backups of Sparse Databases

RMAN enables you to back up sparse databases. This could include backing up a sparse data file, a tablespace containing some sparse data files, a PDB containing some sparse data files, and a CDB containing some sparse PDBs in the backup set or image copy format. A sparse backup is an RMAN object that contains data blocks of sparse data files from their dedicated delta storage space. To perform a sparse backup, the `COMPATIBLE` initialization parameter for the sparse database must be 12. 2 or higher.

While performing a sparse backup, RMAN, by default, backs up data blocks of sparse data files from their delta storage space during a backup. It does not back up the logical data blocks from the backing data files. The backing data files in a sparse database environment must be read-only.

If you want to perform a traditional full or incremental backup on a sparse database to back up both, local and remote data blocks, then you can choose to run the backup with the `FROM NONSPARSE` option.

For databases with the `COMPATIBLE` initialization parameter less than 12.2, RMAN continues to perform the traditional backup and recovery operation for sparse databases in the non-sparse mode.

Encryption of Backup Sets

RMAN can transparently encrypt data written to backup sets and decrypt those backup sets when they are needed in a `RESTORE` operation. To create encrypted backups on disk, the database must use the Advanced Security Option. To create encrypted backups directly on tape, RMAN must use the Oracle Secure Backup SBT interface, but does not require the Advanced Security Option. RMAN issues an `ORA-19916` error if you attempt to create encrypted RMAN backups using an SBT library other than Oracle Secure Backup.

RMAN can encrypt backups by using several different encryption algorithms, which are listed in `V$RMAN_ENCRYPTION_ALGORITHMS`. RMAN supports three modes of encryption for backups:

- Transparent encryption, in which RMAN can create and restore encrypted backups with no special DBA intervention if the data is already protected with Transparent Data Encryption (TDE) in the Oracle Database
- Password-based encryption, where a password is specified during the backup, and the same password must be supplied to restore the backup
- Dual-mode encryption, where backups can be created using either transparent encryption or password-based encryption, and where decryption can be performed based upon either the Oracle software keystore, or a password the DBA supplies at decryption time

Note:

Keystore-based encryption is more secure than password-based encryption because no passwords are involved. Use password-based encryption only when absolutely necessary because your backups must be transportable.

The `CONFIGURE` and `SET` commands manage the encryption settings for database backups. See the reference entries for those commands for more details. Backup sets containing archived redo log files are encrypted if any of the following is true:

- `SET ENCRYPTION ON` is in effect when the backup is being created.
- Encryption is configured for the whole database or at least one tablespace.

See Also:

- [Oracle Database Backup and Recovery User’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/rcmrf&id=BRADV-GUID-21D5FCCE-7AF1-4CF8-BC53-2496ECE3C56E) for an overview of the backup encryption, a guide to its use, and information on choosing among different modes of encryption
- [Oracle Database Advanced Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/rcmrf&id=ASOAG10139) to learn about TDE tablespace encryption and Oracle software keystores

Backing Up Standby Databases

The RMAN `BACKUP` command backs up the standby database exactly the same as a primary database, except that the backup takes place on the standby site. The primary database has no influence on the backup of the standby database.

When you connect to the standby database to perform the backup, use the `TARGET` keyword and not the `AUXILIARY` keyword.

The state of the standby database when the backup is made determines whether the backup is consistent or inconsistent. To make a consistent backup, the standby database must shutdown cleanly and be mounted, but not placed in recovery mode. Any other status results in an inconsistent backup and must be restored using media recovery.

RMAN Backups in a Data Guard Environment

A recovery catalog is required when you are performing RMAN operations in a Data Guard environment. The catalog enables all RMAN operations to be transparently executable at any primary or standby database. You can offload primary database backups onto any standby database in the environment; the RMAN backups are interchangeable. If you use RMAN in `NOCATALOG` mode, then RMAN uses only the metadata in the mounted control file.

In a Data Guard environment, the database that creates a backup or copy is associated with the file. For example, if RMAN connects as `TARGET` to database `prod` and backs it up, then this database backup is associated with `prod`. A backup remains associated with the database that created in unless you use the `CHANGE ... RESET DB_UNIQUE_NAME` to associate the backup with a different database.

The association of a backup is different from its accessibility. The recovery catalog considers disk backups as accessible only to the database in the Data Guard environment on which it was created, whereas tape backups created on one database are considered accessible to all databases. If a backup file is not associated with any database, then the row describing it in the recovery catalog view shows `null` for the `SITE_KEY` column. By default, RMAN associates files whose `SITE_KEY` is `null` with the database to which RMAN is connected as `TARGET`.

In a Data Guard environment, RMAN commands can operate on any backups that are accessible. For example, assume that databases `prod` and `standby1` reside on different hosts. RMAN backs up data file 1 on `prod` to `/prodhst/disk1/df1.dbf` on the production host and also to tape. RMAN backs up data file 1 on `standby1` to `/sby1hst/disk2/df1.dbf` on the standby host and also to tape. If RMAN is connected to database `prod` as `TARGET`, then you cannot use RMAN to perform operations with the `/sby1hst/disk2/df1.dbf` backup located on the standby host. However, RMAN considers the tape backup made on `standby1` as eligible to be restored.

Note:

You can FTP a backup from a standby host to a primary host or vice versa and then `CATALOG` it. After a file is cataloged by the target database, the file is associated with the target database.

If backups are accessible to RMAN, you can use RMAN maintenance commands such as `CHANGE`, `CROSSCHECK`, and `DELETE` for backups when connected to any primary or standby database.

See Also:

[Oracle Data Guard Concepts and Administration](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/rcmrf&id=SBYDB04700) to learn how to use RMAN to back up and restore files in a Data Guard environment

Backing Up Data for Cross-Platform Transport

The `BACKUP` command can create backup sets that are used to transport an entire database, data files, or tablespaces from one platform to another. To create cross-platform backups, use either the `FOR TRANSPORT` or `TO PLATFORM` clause in the `BACKUP` command. The `V$TRANSPORTABLE_PLATFORM` view contains the list of platforms supported for cross-platform transport.

See Also:

[Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/rcmrf&id=BRADV05432) for information about how to create backup sets for cross-platform data transportation

List of Clauses Incompatible with TO PLATFORM and FOR TRANSPORT

You can use the `BACKUP` command to create backup sets for cross-platform data transportation. To indicate that a backup is for cross-platform transportation, use either the `FOR TRANSPORT` or `TO PLATFORM` clauses.

When you use either the `FOR TRANSPORT` or `TO PLATFORM` clause, you cannot use the following clauses of the `BACKUP` command:

- `CUMULATIVE`
- forRecoveryOfSpec
- keepOption
- notBackedUpSpec
- `PROXY`
- `TAG`
- `VALIDATE`

Syntax

backup::=

![backup](img/backup.gif)

> BACKUP \[ {backupOperand}...\] backupSpec \[backupSpec\]... \[PLUS ARCHIVELOG \[ {backupSpecOperand}...\]\]
>
> ![Oracle Logo](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/gifs/oracle.gif)[  
> Copyright © 2023, 2024, Oracle and/or its affiliates.](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/html/cpyr.htm)


(backupOperand::=, backupSpec::=, backupSpecOperand::=)

backupOperand::=

![backupoperand](img/backupoperand.gif)

> backupTypeSpec | CHANNEL \['\] channel\_id \['\] | CHECK LOGICAL | CONSISTENT | COPIES integer | CUMULATIVE | DEVICE TYPE deviceSpecifier | DISKRATIO integer | duration | fileNameConversionSpec | FILESPERSET integer | FORCE | {AUXILIARY FORMAT { formatSpec \[, formatSpec\]... | NEW} | FORMAT formatSpec \[, formatSpec\]... | TO DESTINATION toDestSpec \[, toDestSpec\]...} | forRecoveryOfSpec | FOR {TRANSPORT \[ALLOW INCONSISTENT\] | TRANSPORT UNPLUG INTO ' filename '} | FROM PLATFORM ' platform ' | FULL | INCREMENTAL {LEVEL | FROM SCN} integer | keepOption | MAXSETSIZE sizeSpec | notBackedUpSpec | NOCHECKSUM | NOEXCLUDE | POOL integer | PROXY \[ONLY\] | REUSE | SECTION SIZE sizeSpec | skipSpec | TAG \['\] tag\_name \['\] | TO PLATFORM quoted\_string {\[UNPLUG INTO ' filename '\] | ALLOW INCONSISTENT} | VALIDATE \[MIRROR {ALL | integer}\]


(backupTypeSpec::=, [deviceSpecifier::=](deviceSpecifier.md), [fileNameConversionSpec::=](fileNameConversionSpec.md), [formatSpec::=](formatSpec.md), [toDestSpec::=](toDestSpec.md), forRecoveryOfSpec::=, [keepOption::=](keepOption.md), notBackedUpSpec::=, [sizeSpec::=](sizeSpec.md), skipSpec::=)

backupSpec::=

![backupspec](img/backupspec.gif)

> \[ {\] {archivelogRecordSpecifier | {BACKUPSET { {ALL | completedTimeSpec | FROM TAG \['\] tag\_name \['\] \[, \['\] tag\_name \['\]\]...} | primaryKey \[, primaryKey\]...} | BACKUPPIECE ' filename ' \[, ' filename '\]...} | CONTROLFILECOPY {' filename ' | ALL | LIKE ' string\_pattern '} | copyOfSpec | CURRENT CONTROLFILE | {DATABASE \[ROOT\] | PLUGGABLE DATABASE pdb\_name \[, pdb\_name\]...} | datafileCopySpec | DATAFILE datafileSpec \[, datafileSpec\]... | {DATAPUMP \[ { {FORMAT formatSpec | SKIP DATAFILES| EXCLUDE {STATISTICS | TABLE\_STATISTICS | INDEX\_STATISTICS}}}...\] | {RECOVERY AREA | DB\_RECOVERY\_FILE\_DEST} | RECOVERY FILES | SPFILE | TABLESPACE \['\] tablespace\_name \['\] \[, \['\] tablespace\_name \['\]\]...} \[ {backupSpecOperand}...\] \[}\]


([archivelogRecordSpecifier::=](archivelogRecordSpecifier.md), [completedTimeSpec::=](completedTimeSpec.md), copyOfSpec::=, datafileCopySpec::=, [datafileSpec::=](datafileSpec.md), backupSpecOperand::=)

backupSpecOperand::=

![backupspecoperand](img/backupspecoperand.gif)

> CHANNEL \['\] channel\_id \['\] | DELETE \[ALL\] INPUT | DISKRATIO integer | FILESPERSET integer | FORCE | {AUXILIARY FORMAT { formatSpec \[, formatSpec\]... | NEW} | FORMAT formatSpec \[, formatSpec\]... | TO DESTINATION toDestSpec \[, toDestSpec\]...} | FROM TAG \['\] tag\_name \['\] | INCLUDE CURRENT CONTROLFILE | keepOption | MAXSETSIZE sizeSpec | notBackedUpSpec | NOEXCLUDE | POOL integer | REUSE | SECTION SIZE sizeSpec | skipSpec | TAG \['\] tag\_name \['\]


([formatSpec::=](formatSpec.md), [toDestSpec::=](toDestSpec.md) [keepOption::=](keepOption.md), notBackedUpSpec::=, [sizeSpec::=](sizeSpec.md), skipSpec::=)

backupTypeSpec::=

![backuptypespec](img/backuptypespec.gif)

> AS {\[COMPRESSED\] BACKUPSET | COPY | {NONSPARSE | SPARSE} {\[COMPRESSED\] BACKUPSET | COPY}}
>
> ![Oracle Logo](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/gifs/oracle.gif)[  
> Copyright © 2023, 2024, Oracle and/or its affiliates.](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/html/cpyr.htm)


copyOfSpec::=

![copyofspec](img/copyofspec.gif)

> COPY OF { {DATABASE \[ROOT\] | PLUGGABLE DATABASE pdb\_name \[, pdb\_name\]...} | DATAFILE datafileSpec \[, datafileSpec\]... | TABLESPACE \['\] tablespace\_name \['\] \[, \['\] tablespace\_name \['\]\]...}
>
> ![Oracle Logo](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/gifs/oracle.gif)[  
> Copyright © 2023, 2024, Oracle and/or its affiliates.](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/html/cpyr.htm)


([datafileSpec::=](datafileSpec.md))

datafileCopySpec::=

![datafilecopyspec](img/datafilecopyspec.gif)

> DATAFILECOPY { ' filename ' \[, ' filename '\]... | {ALL | LIKE ' string\_pattern ' | FROM TAG \['\] tag\_name \['\] \[, \['\] tag\_name \['\]\]...} \[NODUPLICATES\]}
>
> ![Oracle Logo](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/gifs/oracle.gif)[  
> Copyright © 2023, 2024, Oracle and/or its affiliates.](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/html/cpyr.htm)


duration::=

![duration](img/duration.gif)

> DURATION integer: integer \[ { {MINIMIZE {LOAD | TIME} | PARTIAL}}...\]
>
> ![Oracle Logo](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/gifs/oracle.gif)[  
> Copyright © 2023, 2024, Oracle and/or its affiliates.](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/html/cpyr.htm)


forRecoveryOfSpec::=

![forrecoveryofspec](img/forrecoveryofspec.gif)

> FOR RECOVER OF {COPY \[ { {DATAFILECOPY FORMAT formatSpec | WITH TAG \['\] tag\_name \['\]}}...\] | TAG \['\] tag\_name \['\]}
>
> ![Oracle Logo](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/gifs/oracle.gif)[  
> Copyright © 2023, 2024, Oracle and/or its affiliates.](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/html/cpyr.htm)


([formatSpec::=](formatSpec.md))

notBackedUpSpec::=

![notbackedupspec](img/notbackedupspec.gif)

> NOT BACKED UP \[ {AT ANY SCN | integer TIMES | SINCE TIME ' date\_string '}\]
>
> ![Oracle Logo](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/gifs/oracle.gif)[  
> Copyright © 2023, 2024, Oracle and/or its affiliates.](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/html/cpyr.htm)


skipSpec::=

![skipspec](img/skipspec.gif)

> SKIP {INACCESSIBLE | OFFLINE | READONLY}
>
> ![Oracle Logo](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/gifs/oracle.gif)[  
> Copyright © 2023, 2024, Oracle and/or its affiliates.](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/html/cpyr.htm)


Semantics

backup

This clause specifies the objects to be backed up and the options to control the backup. Refer to backupOperand::= for the syntax diagram.

| Syntax Element | Description |
| --- | --- |
| `backupOperand` | Specifies various options for the `BACKUP` command. |
| `backupSpec` | Specifies one or more objects to be backed up.  Each `backupSpec` clause generates one or more backup sets (`AS BACKUPSET`) or image copies (`AS COPY`). For `AS BACKUPSET`, the `backupSpec` clause generates multiple backup sets if the number of data files specified in or implied by its list of objects exceeds the `FILESPERSET` limit. |
| `   PLUS ARCHIVELOG` | Includes archived redo log files in the backup (see Example 2-13). Causes RMAN to perform the following steps:  1. Run an `ALTER SYSTEM ARCHIVE LOG CURRENT` statement. 2. Run the `BACKUP ARCHIVELOG ALL` command. If backup optimization is enabled, then RMAN only backs up logs that have not yet been backed up. 3. Back up the files specified in the `BACKUP` command. 4. Run an `ALTER SYSTEM ARCHIVE LOG CURRENT` statement. 5. Back up any remaining archived redo log files. If backup optimization is not enabled, then RMAN backs up the logs generated in step 1 plus all the logs generated during the backup.  In a CDB, you can backup archived redo logs only when you connect to the root as a common user with the `SYSDBA` or `SYSBACKUP` privilege. You cannot include archive logs in the backup when connected to a PDB.  Note: You cannot specify `PLUS ARCHIVELOG` on the `BACKUP ARCHIVELOG` command or `BACKUP AS COPY INCREMENTAL` command (or `BACKUP INCREMENTAL` command when the default backup type is `COPY`). You cannot specify `PLUS ARCHIVELOG` when also specifying `INCREMENTAL FROM SCN`.  Note: Unless the online redo log is archived at the end of the backup, `DUPLICATE` is not possible with this backup.  Note: This clause cannot be used with the `KEEP UNTIL` clause. |
| `backupSpecOperand` | Specifies a variety of options and parameters that affect the `backupSpec` clause. |

backupOperand

This subclause specifies options such as the device type and output format. Refer to backupOperand::= for the syntax diagram.

| Syntax Element | Description |
| --- | --- |
| `backupTypeSpec` | Specifies the type of backup being created, either backup sets (`AS BACKUPSET`) or image copies (`AS COPY`).  See Also: `backupTypeSpec` for details |
| `CHANNEL` `channel_id` | Specifies the case-sensitive name of a channel to use when creating backups. Use any meaningful name, for example `ch1` or `dev1`. The database uses the channel ID to report I/O errors. If you do not set this parameter, then RMAN dynamically assigns the backup sets to any available channels during execution.  As shown in Example 2-23, you can use `CHANNEL` to specify which channels back up which files.  Note: You can also specify this parameter in the `backupSpec` clause. |
| `CHECK LOGICAL` | Tests data and index blocks that pass physical corruption checks for logical corruption (see Example 2-25). This option typically adds 1-3% overhead.  Examples of logical corruption are corruption of a row piece or index entry. If RMAN finds logical corruption, then it logs the block in the alert log and server session trace file. The `SET` `MAXCORRUPT` command specifies the total number of physical and logical corruptions permitted in a data file.  By default, the `BACKUP` command computes a checksum for each block and stores it in the backup. If you specify the `NOCHECKSUM` option, then RMAN does not perform a checksum of the blocks when writing the backup.  If `SET MAXCORRUPT` and `NOCHECKSUM` are not set, then `CHECK` `LOGICAL` detects all types of corruption that are possible to detect during a backup. |
| `CONSISTENT` | Creates consistent backupsets of the specified database or PDB. A single consistent backup is sufficient to restore a database or a PDB to a consistent state.  Note: This clause cannot be used with the `KEEP` and `AS COPY` options. |
| `COPIES` `integer` | Sets the number of identical backups (`1` - `4`) that RMAN creates. The default value is `1`.  You can use multiple format strings to specify different names and locations for the copies. Example 2-22 illustrates a duplexed backup to different locations on disk.  RMAN can duplex backups to either disk or tape, but cannot duplex backups to tape and disk simultaneously. When backing up to tape, ensure that the number of copies does not exceed the number of available tape devices. Also, if `COPIES` is greater than 1, then the `BACKUP_TAPE_IO_SLAVES` initialization parameter must be enabled on the target database.  You can specify duplexing in multiple commands. The order of precedence is as follows, with settings higher on the list overriding lower settings:  1. `BACKUP` `COPIES` 2. `SET` `BACKUP` `COPIES` 3. `CONFIGURE` `...` `BACKUP` `COPIES`  Note: This option does not apply with `AS COPY` and results in an error message.  Note: Duplexing cannot be used when creating files in the fast recovery area. |
| `CUMULATIVE` | Copies the data blocks used since the most recent level 0 backup (see Example 2-16).  Note: This option does not apply with `AS COPY` and results in an error message. |
| `DEVICE TYPE` `deviceSpecifier` | Allocates automatic channels for the specified device type only. For example, if you configure disk and tape channels, then configure `sbt` as the default device type, then the following command allocates disk channels only:  ``` BACKUP DEVICE TYPE DISK DATABASE; ```  The `DEVICE TYPE` option is valid only for automatic channels and is not valid for manually allocated channels. You cannot use the `DEVICE TYPE` option for a device other than `DISK` if you have not run `CONFIGURE` `DEVICE TYPE` for this device.  Note: To specify a disk channel for the `BACKUP RECOVERY AREA` command, you must use the `TO DESTINATION` of the subclause [toDestSpec](allocOperandList.md).  See Also: `deviceSpecifier` |
| `DISKRATIO` `integer` | Directs RMAN to populate each backup set with data files from at least integer disks.  This parameter is only enabled when you are backing up data files or control files, and when the operating system can give RMAN disk contention and node affinity data. To manually disable this feature, set `DISKRATIO` to `0`.  For example, assume that data files are distributed across 10 disks. If the disks supply data at 10 bytes/second, and if the tape drive requires 50 bytes/second to keep streaming, then set `DISKRATIO` to `5` to direct RMAN to include data files from at least 5 disks in each backup set.  If you set `FILESPERSET` but not `DISKRATIO`, then `DISKRATIO` defaults to the same value as `FILESPERSET`. If you specify neither parameter, then `DISKRATIO` defaults to 4. RMAN compares the `DISKRATIO` value to the actual number of devices involved in the backup and uses the lowest value. For example, if `DISKRATIO` is 4 and the data files are located on three disks, then RMAN attempts to include data files from three disks in each backup set.  The `DISKRATIO` parameter is easier for data file backups when the data files are striped or reside on separate disk spindles and you either:  - Use a high-bandwidth tape drive that requires several data files to be multiplexed to keep the tape drive streaming. - Make backups while the database is open and spread the I/O load across several disk spindles to leave bandwidth for online operations.  Note: Do not spread I/O over more than the minimum number of disks required to keep the tape streaming. Otherwise, you increase restore time for a file without increasing performance. |
| `duration` | Specifies options related to the maximum time for a backup command to run.  See Also: `duration` |
| `fileNameConversionSpec` | This option is valid only when `BACKUP` is creating image copies. Files being copied are renamed according to the specified patterns. If a file being backed up has a name that does not match any of the specified rename patterns, then RMAN uses `FORMAT` to name the output image copies. If no `FORMAT` is specified, then RMAN uses the default format `%U`.  See Also: `fileNameConversionSpec` for file renaming patterns |
| `FILESPERSET` `integer` | Specifies the maximum number of input files to include in each output backup set. This parameter is only relevant when `BACKUP` generates backup sets.  RMAN backs up the files in each `backupSpec` as one or more backup sets. When the number of files in each `backupSpec` exceeds the `FILESPERSET` setting, then RMAN splits the files into multiple backup sets accordingly. The default value for `FILESPERSET` is `64`.  The RMAN behavior is illustrated by the following `BACKUP` commands:  ``` BACKUP AS BACKUPSET (DATAFILE 3, 4, 5, 6, 7) (DATAFILE 8, 9); BACKUP AS BACKUPSET DATAFILE 3, 4, 5, 6, 7, 8, 9; BACKUP AS BACKUPSET DATAFILE 3, ... 72; ```  In the first command, RMAN places data files 3, 4, 5, 6, and 7 into one backup set and data files 8 and 9 into another backup set. In the second command, RMAN places all data files into one backup set. In the third command, the ellipses indicate data files 3 through 72. Because in this case RMAN is backing up 70 data files, RMAN places 64 files in one backup set and 6 in another.  By default, RMAN divides files among backup sets to make optimal use of channel resources. The number of files to be backed up is divided by the number of channels. If the result is less than 64, then this number is the `FILESPERSET` value. Otherwise, `FILESPERSET` defaults to 64.  Note: You cannot specify the number of backup pieces that are in a backup set. |
| `FORCE` | Forces RMAN to ignore backup optimization. That is, even if `CONFIGURE` `BACKUP OPTIMIZATION` is set to `ON`, RMAN backs up all specified files.  Note: You can also specify this option in the `backupSpecOperand` clause.  The command `BACKUP DATABASE FORCE PLUS ARCHIVELOG` is equivalent to `BACKUP DATABASE PLUS ARCHIVELOG FORCE`. |
| `AUXILIARY FORMAT` | Copies the files on the target database to the specified location on the auxiliary instance. RMAN can only generate image copies when `AUXILIARY FORMAT` is specified. RMAN must be connected to both `TARGET` and `AUXILIARY` instances and have access to auxiliary channels.  You can use the `BACKUP AUXILIARY FORMAT` command to copy data files, archived logs, controlfile, and server parameter file (spfile) over the network between primary and standby databases. For example, if a data file on a primary database was lost, you could `CONNECT` to the standby database as `TARGET` and the primary database as `AUXILIARY`, and copy an intact data file from the standby host to the primary host.  See Also: Example 2-30 |
| `formatSpec` | Specifies a pattern for naming the output image copies on an auxiliary instance. The path must be valid on the auxiliary host.  See Also: `formatSpec` for valid substitution variables |
| `   NEW` | Creates an image copy in the directory specified in the `DB_CREATE_FILE_DEST` initialization parameter of the auxiliary instance. The image copy is an Oracle-managed file. |
| `FORMAT` `formatSpec` | Specifies a pattern for naming the output backup pieces or image copies (see Example 2-17). For `AS COPY`, if one or more of the directories mentioned in the specified format does not exist, then RMAN signals an error.  The default location for disk backups depends on whether a fast recovery area is enabled and whether `FORMAT` is specified:  - If a fast recovery area is enabled, and if you do specify `FORMAT`, then RMAN names the output files according to the `FORMAT` setting. If no location is specified in `FORMAT`, then RMAN creates the backup in a platform-specific location—not in the recovery area. - If a fast recovery area is enabled, and if you do not specify `FORMAT`, then RMAN creates the backup in the recovery area and uses the substitution variable `%U` to name the backup. - If a fast recovery area is not enabled, and if you do not specify `FORMAT`, then RMAN creates the backup in a platform-specific location and uses `%U` to name the backup.  To create RMAN backups in the fast recovery area with names in Oracle Managed Files format, do not specify the `FORMAT` clause on the `BACKUP` command or channel.  Note: You cannot specify an Oracle Managed Files file name as the format for a backup. For example, if `+DISK1/datafile/system.732.609791431` is an OMF file name, then you cannot specify this file name in the `FORMAT` parameter.  Backup pieces must have unique names. The maximum length of a backup piece file name is platform-specific. For backups to a media manager, the length is also limited by the limit in the supported version of the media management API. Vendors supporting SBT 1.1 must support file names up to 14 characters. Some SBT 1.1 vendors may support longer file names. Vendors supporting SBT 2.0 must support file names up to 512 characters. Some SBT 2.0 vendors may support longer file names.  You cannot specify multiple, identical `FORMAT` strings within a single `backupSpec` (for example, `BACKUP DATAFILE 3 TO '/tmp/df3.f', DATAFILE 4 TO '/tmp/df4.f'`). However, RMAN permits a single `FORMAT` string to exist in multiple `backupSpec` clauses.  Note: If you are making an archival backup with the `KEEP` option (see Example 2-26), then the format string must contain `%U`. The autobackup also uses this format string.  See Also: `formatSpec` for valid substitution variables |
| `TO DESTINATION` `toDestSpec` | Specifies the directory where the backup is created. This parameter is valid for disk and not SBT channels. The backup files are created in an Oracle Managed Files (OMF) directory. Backup skips the files only when backups do not exist in the specified `TO DESTINATION`. |
| `forRecoveryOfSpec` | Identifies the backup being created as an incremental backup to be used in rolling forward an image copy.  See Also: `forRecoveryOfSpec` |
| `FOR TRANSPORT` | Creates a cross-platform backup using backup sets. You can back up data files, tablespaces, or an entire database. While creating a cross-platform tablespace backup, use the `DATAPUMP` clause to back up the metadata of the transported tablespaces. This metadata is used on the destination database to plug in the transported tablespaces.  Backup sets created by a cross-platform backup are not catalogued in the control file.  Before you backup the whole database for cross-platform transport, ensure that the database is in read-only mode. You can transport a database only if the source and destination use the same endian format.  While backing up tablespaces, the tablespaces being backed must be in read-only mode, unless the `ALLOW INCONSISTENT` clause is used. To transport tablespaces, the source and destination can use different endian formats. When `FOR TRANSPORT` is used, endian conversion is performed on the destination database.  See Also: " Backing Up Data for Cross-Platform Transport "  Note: Cross-platform backups using backup sets are supported from Oracle Database 12c Release 1 (12.1). |
| `ALLOW INCONSISTENT` | Enables you to backup tablespaces that are not in read-only mode.  You cannot use `ALLOW INCONSISTENT` for cross-platform whole database backups.  Although the backup is created, you cannot plug these tablespaces directly into the target database because they are inconsistent. You must later create an incremental backup of the tablespaces when they are in read-only mode. This incremental backup must contain the `DATAPUMP ` clause, which is used to create a backup set containing an export dump file of the tablespace metadata.  See Also: [Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/rcmrf&id=BRADV05432) for more information about creating an restoring inconsistent tablespace backups. |
| `FOR TRANSPORT UNPLUG INTO filename` | Creates a cross-platform consistent backup of a PDB using backup sets. The metadata required to plug the PDB into a different CDB is stored in the XML file specified using filename.  You can use this backup to perform cross-platform transport of the PDB to any supported platform. The PDB that is being transported must be closed before it is unplugged. The CDB to which this PDB belongs must be in read-write mode. |
| `FULL` | Creates a backup of all blocks of data files included in the backup. `FULL` is the opposite of `INCREMENTAL`. RMAN makes full backups by default if neither `FULL` nor `INCREMENTAL` is specified.  A full backup has no effect on subsequent incremental backups and is not considered a part of any incremental backup strategy. A full image copy backup can be incrementally updated, however, by applying incremental backups with the `RECOVER` command.  Note: Unused block compression, which is described in the entry for `BACKUP` `AS BACKUPSET`, causes some data file blocks to be skipped during full backups. |
| `INCREMENTAL LEVEL` `integer` | Copies only those data blocks that have changed since the last incremental `integer` backup, where `integer` is `0` or `1` (see Example 2-16).  See " Incremental Backups " for an explanation of incremental backups. |
| `INCREMENTAL FROM SCN` `integer` | Creates an incremental backup of all specified data files that includes all data file blocks changed at SCNs greater than or equal to the specified SCN.  One use of this option is to refresh a standby database with changes from the primary database (see Example 2-24, and the chapter on RMAN backups in [Oracle Data Guard Concepts and Administration](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/rcmrf&id=SBYDB04700)). This backup contains all changed blocks since the standby database was created or last synchronized. At the standby database, you can use `RECOVER` with `NOREDO` to apply the incremental backup. All changed blocks captured in the incremental backup are applied at the standby database, bringing it current with the primary database.  If you are not making incremental backups based on Volume Shadow Copy Service (VSS) snapshots, then specify `formatSpec` when you specify `INCREMENTAL FROM SCN`. The `FORMAT` string should include substitution variables such as `%U` because RMAN generates a control file backup.  If you specify `FROM SCN` with the `NOKEEP` option, and if you do not specify `formatSpec` when you specify `INCREMENTAL FROM SCN`, then RMAN creates incremental backups in the fast recovery area so that you can create incremental backups based on VSS snapshots in a Windows environment. In this way, you can use incremental backup sets and VSS shadow copies in conjunction. The checkpoint SCN value specified in the `FROM SCN` parameter should be same as the `BACKUP_CHECKPOINT` value in the VSS backup metadata document. If block change tracking is enabled, then the backups use the change tracking mechanism, which significantly reduces the time taken to create incremental backups. RMAN can apply incremental backups from the fast recovery area during recovery transparently.  Note: You cannot use `PLUS ARCHIVELOG` when also specifying `INCREMENTAL FROM SCN`.  See Also: [Oracle Database Platform Guide for Microsoft Windows](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/rcmrf&id=NTQRF280) to learn about making backups with VSS |
| `keepOption` | Overrides any configured retention policy for this backup so that the backup is not considered obsolete, as shown in Example 2-26.  You can use the `KEEP` syntax to generate archival database backups that satisfy business or legal requirements. The `KEEP` setting is an attribute of the backup set (not individual backup piece) or image copy.  Note: You cannot use `KEEP` with `BACKUP BACKUPSET`.  With the `KEEP` syntax, you can keep the backups so that they are considered obsolete after a specified time (`KEEP UNTIL`), or make them never obsolete (`KEEP FOREVER`). As shown in Example 2-27, you must be connected to a recovery catalog when you specify `KEEP FOREVER`.  Note: You can use `CHANGE` to alter the status of a backup generated with `KEEP`.  Note: You cannot use `KEEP UNTIL` with `PLUS ARCHIVELOG`.  See Also: `keepOption` for more information about backups made with the `KEEP` option |
| `MAXSETSIZE` `sizeSpec` | Specifies a maximum size for a backup set (as shown in Example 2-17). RMAN limits all backup sets to this size.  It is possible for a backup set to span multiple tapes, so blocks from each data file are written to multiple tapes. If one tape of a multivolume backup set fails, then you lose the data on all the tapes rather than just one. Because a backup set always includes a whole file rather than part of a file, you can use `MAXSETSIZE` to specify that each backup set can fit on one tape.  Specify size in bytes (default), kilobytes (`K`), megabytes (`M`), or gigabytes (`G`). For example, to limit a backup set to 3 MB, specify `MAXSETSIZE 3M`. The default size is in bytes, rounded down from kilobytes. For example, `MAXSETSIZE 3000` is rounded down to 2 KB (2048 bytes). The minimum value must be greater than or equal to the database block size.  The default number of files in each backup set is determined by `FILESPERSET`, which defaults to 64. When you specify `MAXSETSIZE`, RMAN attempts to limit the size in bytes of the backup sets according to the `MAXSETSIZE` parameter. The limit on the number of files in a backup set applies even if the total size of the resulting backup set is less than `MAXSETSIZE`.  Note: This option results in an error message if used with `BACKUP` `AS COPY`. If you run `BACKUP AS COPY` on a channel that has `MAXSETSIZE` set, then `MAXSETSIZE` is silently ignored. |
| `notBackedUpSpec` | Limits the set of archived redo log files to be backed up according to whether a specified number of backups are present (and not obsolete), or whether the logs have been backed up since a specified date.  See Also: `notBackedUpSpec` |
| `NOCHECKSUM` | Suppresses block checksums during the backup.  A checksum is a number that is computed from the contents of a data block. `DB_BLOCK_CHECKSUM` is a database initialization parameter that controls the writing of checksums for the blocks in data files in the database (not backups). If `DB_BLOCK_CHECKSUM` is `typical`, then the database computes a checksum for each block during normal operations and stores it in the block before writing it to disk. When the database reads the block from disk later, it recomputes the checksum and compares it to the stored value. If they do not match, then the block is damaged.  Note: You cannot disable checksums for data files in the `SYSTEM` tablespace even if `DB_BLOCK_CHECKSUM=false`.  By default, the `BACKUP` command computes a checksum for each block and stores it in the backup. The `BACKUP` command ignores the values of `DB_BLOCK_CHECKSUM` because this initialization parameter applies to data files in the database, not backups. If you specify the `NOCHECKSUM` option, then RMAN does not perform a checksum of the blocks when writing the backup.  When restoring a backup data file, RMAN honors the `DB_BLOCK_CHECKSUM` initialization parameter setting. RMAN clears the checksum if `DB_BLOCK_CHECKSUM` is set to `false`. If set to `typical`, then RMAN verifies the checksum when restoring from the backup and writing to the data file.  Note: You can turn off checksum checking by specifying `NOCHECKSUM`, but other physical consistency checks, such as checks of the block headers and footers, cannot be disabled.  See Also: [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/rcmrf&id=REFRN-GUID-A0F72B65-BC1C-441B-824E-03ADCE66063A) for more information about the `DB_BLOCK_CHECKSUM` initialization parameter |
| `NOEXCLUDE` | When specified on a `BACKUP` `DATABASE` or `BACKUP COPY OF DATABASE` command, RMAN backs up all tablespaces, including any for which a `CONFIGURE` `EXCLUDE` command has been entered. This option does not override `SKIP` `OFFLINE` or `SKIP READONLY`. |
| `POOL` `integer` | Specifies the media pool in which the backup is stored. Consult your media management documentation to see whether `POOL` is supported.  Note: This option does not work with `AS COPY` and results in an error. |
| `PROXY` | Backs up the specified files with the proxy copy functionality, which gives the media management software control over the data transfer between storage devices and the data files on disk. The media manager—not RMAN—decides how and when to move data.  When you run `BACKUP` with the `PROXY` option, RMAN performs these steps:  1. Searches for a channel of the specified device type that is proxy-capable. If no such channel is found, then RMAN issues a warning and attempts a conventional (that is, non-proxy) backup of the specified files. 2. If RMAN locates a proxy-capable channel, then it calls the media manager to check if it can proxy copy the files. If the media manager cannot proxy copy, then RMAN uses conventional backup sets to back up the files.  Note: If you specify `PROXY`, then the `%p` variable must be included in the `FORMAT` string either explicitly or implicitly within `%U`.  Note: This option does not work with `AS COPY` and results in an error. |
| `   ONLY` | Causes the database to issue an error message when it cannot proxy copy rather than creating conventional backup sets. If you do not want RMAN to try a conventional copy when a proxy copy fails, use the `ONLY` option. |
| `REUSE` | Enables RMAN to overwrite an existing backup or copy with the same name as the file that `BACKUP` is currently creating. |
| `SECTION SIZE` `sizeSpec` | Specifies the size of each backup section produced during a data file or data file copy backup.  By setting this parameter, RMAN can create a multisection backup. In a multisection backup, RMAN creates a backup piece that contains one file section, which is a contiguous range of blocks in a file. All sections of a multisection backup are the same size.  File sections enable RMAN to create multiple steps for the backup of a single large data file. RMAN channels can process each step independently and in parallel, with each channel producing one section of a multisection backup set.  Multisection backups can be stored either as image copies or backup sets (both full and incremental). To create multisection image copies or incremental backups, the `COMPATIBLE` parameter must be 12.0.0 or higher.  See Also: [Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/rcmrf&id=BRADV665) for more information about multisection image copies.  Note: RMAN always creates multisection backups with `FILESPERSET` set to 1.  If you specify a section size that is larger than the size of the file, then RMAN does not use multisection backup for the file. If you specify a small section size that would produce more than 256 sections, then RMAN increases the section size to a value that results in exactly 256 sections.  Note: Depending on where you specify this parameter in the RMAN syntax, you can specify different section sizes for different files in the same backup job.  Note: You cannot use `SECTION SIZE` with `MAXPIECESIZE`. |
| `skipSpec` | Excludes data files or archived redo log files from the backup if they are inaccessible, offline, or read-only.  See Also: `skipSpec` for details. |
| `TAG` `tag_name` | Specifies a user-specified tag name for a backup set, proxy copy, data file copy, or control file copy. The tag is applied to the output files generated by the `BACKUP` command.  The tag name is not case-sensitive. The name must be 30 characters or less. The characters are limited to the characters that are valid in file names on the target file system. For example, ASM does not support the use of the hyphen (`-`) character in the file names it uses internally, so `weekly-incremental` is not a valid tag name for backups in ASM disk groups. Environment variables are not valid in the `TAG` parameter.  Typically, a tag name is a meaningful name such as `MON_PM_BKUP` or `WEEKLY_FULL_BKUP`. Tags are reusable, so that backup set 100 can have the tag `MON_PM_BKUP` one week while backup set 105 has the same tag the next week.  If you do not specify a tag name, then by default RMAN creates a tag for backups (except for control file autobackups). The default tag uses the format `TAG` `YYYYMMDDTHHMMSS`, where `YYYY` is the year, `MM` is the month, `DD` is the day, `HH` is the hour (in 24-hour format), `MM` is the minutes, and `SS` is the seconds. For example, a backup of data file `1` might receive the tag `TAG20130208T133437`. The date and time refer to when RMAN started the backup. If multiple backup sets are created by one `BACKUP` `AS BACKUPSET` command, then each backup piece is assigned the same default tag.  You can also specify the tag at the `backupSpec` level. If you specify the tag at:  - The command level, then all backup sets created by the command have the tag. - The `backupSpec` level, then backup sets created with different backup specifications can have different tags. - Both levels, then the tag in the `backupSpec` takes precedence.  Note: A tag is an attribute of each backup piece in a given copy of a backup set (for `AS BACKUPSET`) or each image copy (for `AS COPY`). For example, if you run `BACKUP AS BACKUPSET COPIES 1 DATABASE TAG TUE_PM`, then only one copy of the backup set exists and each backup piece has tag `TUE_PM`. Assume that this backup set has primary key `1234`. If you then run `BACKUP BACKUPSET 1234 TAG WED_PM`, then the first copy of the backup set has tag `TUE_PM` and the second copy of the backup set has tag `WED_PM`. |
| `TO PLATFORM '` `platform` `'` | Specifies the full name of the destination platform to which the cross-platform backup will be transported. If you omit `TO PLATFORM`, RMAN assumes that the destination platform is the same as the source platform.  Backup sets created by a cross-platform backup are not catalogued in the control file.  You can use either `FOR TRANSPORT` or `TO PLATFORM` to indicate that a backup is a cross-platform backup. If you specify a platform name using `TO PLATFORM`, endianess conversion, if required, is performed on the source platform. Therefore, you can restore this cross-platform backup only on the specified platform. If you omit `TO PLATFORM`, you can restore this cross-platform backup on any supported platform. The `V$TRANSPORTABLE_PLATFORM` view provides information about the supported platforms.  See Also: " FOR TRANSPORT "  See Also: " Backing Up Data for Cross-Platform Transport " for information about the mode in which the database or tablespace is opened before creating a cross-platform backup  Note: Cross-platform backups using backup sets are supported from Oracle Database 12c Release 1 (12.1). |
| `ALLOW INCONSISTENT` | Enables you to backup tablespaces that are not in read-only mode.  You cannot use `ALLOW INCONSISTENT` for cross-platform whole database backups.  See Also: " ALLOW INCONSISTENT " |
| `TO PLATFORM UNPLUG INTO filename` | Creates a cross-platform consistent backup of a PDB using backup sets. The metadata required to plug the PDB into a different CDB is stored in the XML file specified using filename.  You use this backup to perform cross-platform transport of the PDB to the specified platform. The PDB must be closed before it is unplugged. The CDB must be in read-write mode. |
| `VALIDATE` | Scans the specified files and verifies their contents, testing whether this file can be backed up and whether the data blocks are corrupt.  RMAN creates no output files. This option is equivalent to using the `VALIDATE` command on the database files specified in the backup.  If you do not specify `CHECK LOGICAL`, then `BACKUP VALIDATE` checks for physical corruption only. If you specify `CHECK LOGICAL`, then `BACKUP VALIDATE` checks for both physical and logical corruption. RMAN populates the `V$DATABASE_BLOCK_CORRUPTION` view with any corruptions that it finds.  You can use the `SET` `MAXCORRUPT` command to set a limit for the number of corrupt blocks tolerated during the backup validation. The default is zero.  If you execute `BACKUP INCREMENTAL` with `VALIDATE`, then the behavior depends on whether block change tracking is enabled. If change tracking is enabled, then RMAN validates only changed blocks; otherwise, RMAN validates all blocks in the files included in the backup.  Note: You cannot validate backups of backup sets. |

backupSpec

This subclause specifies a list of one or more objects to be backed up. Each backupSpec clause generates one or more backup sets (`AS BACKUPSET`) or image copies (`AS COPY`). For `AS BACKUPSET`, the backupSpec clause generates multiple backup sets if the number of data files specified in or implied by its list of objects exceeds the default limit of 4 data files or 16 archived redo log files in each backup set. Refer to backupSpec::= for the syntax diagram.

| Syntax Element | Description |
| --- | --- |
| `archivelogRecordSpecifier` | Specifies a range of archived redo log files to be backed up.  To back up archived redo logs in a CDB, connect to the root as a common user with the `SYSDBA` or `SYSBACKUP` privilege. You cannot back up archived redo logs when connected to a PDB.  When backing up archived redo log files, RMAN can perform archived log failover automatically. RMAN backs up the log when at least one archived log corresponding to a given log sequence number and thread is available. Also, if the copy that RMAN is backing up contains corrupt blocks, then it searches for good copies of these blocks in other copies of the same archived redo log files.  RMAN does not signal an error if the command finds no logs to back up, since this situation probably exists because no new logs were generated after the previous `BACKUP ARCHIVELOG ALL` `DELETE INPUT` command. The only exception to this behavior is when the `SEQUENCE` number clause is specified. In this scenario, RMAN signals the `RMAN-06004` error if an archived redo log file of the specified sequence is not found.  If you specify `BACKUP ARCHIVELOG ALL`, then RMAN backs up exactly one copy of each distinct log sequence number. For example, if you archive to multiple destinations, RMAN backs up one copy of each log sequence number—not each copy of each log sequence number. For other commands, such as `DELETE` `ALL` does refer to every log, even duplicate log sequences.  If the database is open when you run `BACKUP ARCHIVELOG`, and if the `UNTIL` clause or `SEQUENCE` parameter is not specified, then RMAN runs `ALTER SYSTEM ARCHIVE LOG CURRENT`.  Note: If you run `BACKUP ARCHIVELOG ALL`, or if the specified log range includes logs from prior incarnations, then RMAN backs up logs from prior incarnations to ensure availability of all logs that may be required for recovery through an `OPEN RESETLOGS`.  See Also: `archivelogRecordSpecifier` for syntax, and [Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/rcmrf&id=BRADV-GUID-4481CA5F-B1B5-4819-9E6B-7184951EC81A) explanations of backup failover for logs and automatic log switching |
| `BACKUPSET` | Specifies a backup of backup sets. Use this parameter with the `DEVICE TYPE` `sbt` clause to offload backups on disk to tape (as shown in Example 2-21). You cannot back up from tape to tape or from tape to disk: only from disk to disk or disk to tape.  If you specify the `DELETE INPUT` option on the `BACKUP BACKUPSET` command, then RMAN deletes all copies of the backup set that exist on disk. For example, if you duplexed a backup to 4 locations, then RMAN deletes all 4 backup sets. The `ALL` option does not add any functionality.  RMAN performs **backup set failover** when backing up backup sets. RMAN searches for all available backup copies when the copy that it is trying to back up is corrupted or missing. This behavior is similar to RMAN's behavior when backing up archived redo log files that exist in multiple archiving destinations.  If **backup optimization** is enabled when you back up a backup set, and if the identical backup set has been backed up to the same device type, then RMAN skips the backup of this backup set.  Starting with Oracle Database Release 18c, you can use the `BACKUP AS COMPRESSED BACKUPSET` command to compress backup sets that were not created using compression.  You can use `BACKUP ... BACKUPSET` to back up unencrypted backup sets in encrypted format. Before running the `BACKUP` command, enable encryption using the `SET ENCRYPTION FOR DATABASE ON` command.  Note: When you use the `BACKUP BACKUPSET` command with encrypted backup sets, the backup sets are backed up in their encrypted form. Because `BACKUP BACKUPSET` just copies the encrypted backup set to disk or tape, no decryption key is needed during a `BACKUP BACKUPSET` operation. The data is never decrypted during any part of the operation. The `BACKUP BACKUPSET` command can neither encrypt nor decrypt backup sets.  Note: You can duplex backups of backup sets with `BACKUP COPIES` and `SET` `BACKUP COPIES`. |
| `   ALL` | Specifies all backup sets.  When used with CDBs, RMAN skips backing up the backups of PDBs that were dropped. There is no way to back up backup sets of dropped PDBs. |
| `completedTimeSpec` | Identifies backup sets according to completion time.  See Also: `completedTimeSpec` |
| `integer` | Specifies backup sets according to primary key. You can obtain the primary keys for backup sets from the output of the `LIST` `BACKUP` command. |
| `  FROM TAG` `tag_name` | Identifies one or more backup sets by tag name. If multiple backup sets have the same tag name, then they are all are backed up. The `tag_name` is not case-sensitive. |
| `CONTROLFILECOPY` | Specifies one or more control file copies for backups.  A control file copy can be created with the `BACKUP AS COPY CURRENT CONTROLFILE` command or the SQL `ALTER DATABASE BACKUP CONTROLFILE TO '...'` command.  Note: A control file autobackup is not a control file copy. |
| `   '` `filename` `'` | Specifies a control file copy by file name. |
| `   ALL` | Specifies all control file copies. |
| `   LIKE` ` '` `string_pattern` `'` | Specifies a control file copy by a file name pattern. The percent sign (`%`) as a wildcard meaning 0 o r more characters; an underscore (`_`) is a wildcard meaning 1 character. |
| `copyOfSpec` | Makes a backup of previous image copies of data files and possibly control files.  See Also: `copyOfSpec` |
| `CURRENT CONTROLFILE` | Specifies the current control file. When backing up as a backup set, RMAN first creates a snapshot control file for read consistency. You can configure the location of the snapshot control file with the `CONFIGURE` command. In an Oracle Real Application Clusters (Oracle RAC) environment, the following restrictions apply:  - The snapshot control file location must be on shared storage—that is, storage that is accessible by all Oracle RAC instances. - The destination of an image copy of the current control file must be shared storage. |
| `APPLICATION ROOT DATABASE app_root_name` | Creates a backup of all data files in the application root.  Connect to the CDB root as a common user with the `SYSDBA` or `SYSBACKUP` privilege. Or, connect to the application root as an application common user with the `SYSDBA` or `SYSBACKUP` privilege. |
| `DATABASE` | Creates a backup of all data files in the whole database or a single pluggable database (PDB). To back up a CDB, connect to the root as a common user with the `SYSDBA` or `SYSBACKUP` privilege. To back up a PDB, connect to the PDB as a common user or local user with the `SYSDBA` or `SYSBACKUP` privilege.  If generating a backup set, then RMAN can include only data files and control files: it cannot include archived redo log files.  In an application container, creates a backup of all data files in the application container. This includes the application root and all application PDBs that belong to this application root. Connect to the application root as an application common user with the `SYSDBA` or `SYSBACKUP` privilege.  If the `backupSpec` includes data file 1, and if `CONFIGURE CONTROLFILE AUTOBACKUP ` is `OFF`, then RMAN automatically includes the control file in the backup. If the instance is started with a server parameter file, then RMAN also includes this parameter file in the backup.  If the `backupSpec` includes data file 1, and if `CONFIGURE CONTROLFILE AUTOBACKUP` is `ON`, then RMAN does not automatically include the control file in the output. Instead, RMAN generates a separate control file autobackup piece. If the instance is started with a server parameter file, then RMAN includes this parameter file in the autobackup piece.  Full database backups are usually either image copies or compressed backup sets. Image copies are more flexible than backup sets for some purposes (such as use in an incrementally updated backups strategy), and compressed backup sets make more efficient use of storage space, if the CPU overhead involved in creating them is tolerable.  Note: To force RMAN to include the current control file in the backup when `CONTROLFILE AUTOBACKUP` is `ON`, specify the `INCLUDE CURRENT CONTROLFILE` clause.  Note: Proxy PDBs are not backed up during a CDB backup.  See Also: The `TABLESPACE` description to learn about backup behavior when the database includes bigfile tablespaces |
| `DATABASE ROOT` | In a CDB, creates a backup of the data files in the root. Connect to the root as a common user with the common `SYSDBA` or `SYSBACKUP` privilege.  In an application container, creates a backup of the files in the application root and all application PDBs. Connect to the application root as an application common user with the `SYSDBA` or `SYSBACKUP` privilege.  See the previous description of `DATABASE`. |
| `PLUGGABLE DATABASE` `pdb_name` | Creates a backup of the data files in one or more PDBs. Specify multiple PDBs using a comma-delimited list. Connect to the root as a common user with the `SYSDBA` or `SYSBACKUP` privilege.  With application containers, use this clause as follows:  - To back up one or more application PDBs, connect to the application root as an application common user with the `SYSDBA` or `SYSBACKUP` privilege. Use a comma-delimited list to specify multiple application PDBs. - To back up the application root and all application PDBs, connect to the CDB root as a common user with the `SYSDBA` or `SYSBACKUP` privilege and specify the application root name as `pdb_name`.  Note: Backing up a proxy PDB is not supported |
| `datafileCopySpec` | Specifies the file names of one or more data file image copies.  See Also: `datafileCopySpec` for details |
| `DATAFILE` `datafileSpec` | Specifies a list of one or more data files. Refer to description of `BACKUP` `DATABASE` for RMAN behavior when data file 1 is backed up.  See Also: `datafileSpec` |
| `DATAPUMP` | Specifies that a Data Pump export dump file is created while performing a cross-platform tablespace backup.  The export dump file contains the metadata of the read-only tablespaces being transported. You need this metadata to plug in the tablespaces at the destination database. The dump file is created in s separate backup set. If you use the `DATAPUMP` clause with the `INCREMENTAL FROM SCN`, then the tablespace must be in read-only mode.  This clause cannot be used with the `ALLOW INCONSISTENT` clause. |
| `FORMAT ` `formatSpec` | Specifies the pattern used to store the backup piece that contains the export dump file. If the `FORMAT` is omitted, then the format provided in the `BACKUP` command is used. If no `FORMAT` clause was used for the `BACKUP` command too, the default format is used for the backup pieces. |
| `SKIP DATAFILES` | Excludes data files for backup. |
| `EXCLUDE` | Excludes statistics from the data pump export operation.  To avoid creating large memory demands, you can choose to exclude statistics data in the export dump file. Use any or all of the following keywords to specify the criteria for `EXCLUDE`: - `STATISTICS` - `TABLE STATISTICS` - `INDEX STATISTICS` |
| `    STATISTICS` | Excludes statistics while creating the export dump file. |
| `   TABLE STATISTICS` | Excludes table statistics while creating the export dump file. |
| `  INDEX STATISTICS` | Excludes index statistics while creating the export dump file. |
| `RECOVERY AREA` | Backs up recovery files created in the current and all previous fast recovery area destinations. Backups can go to SBT and disk. To backup to disk, you must use the `TO DESTINATION` syntax outlined in [toDestSpec](allocOperandList.md).  Recovery files are full and incremental backup sets, control file autobackups, data file copies, and archived redo log files. If an archived redo log file is missing or corrupted, then RMAN looks outside of the recovery area for a good copy of the log that it can use for the backup. Flashback logs, the current control file, and online redo log files are not backed up.  By default, backup optimization is enabled for this command even if the `CONFIGURE` `BACKUP OPTIMIZATION` setting is `OFF`. You can disable backup optimization for `BACKUP RECOVERY AREA` by specifying `FORCE`.  Note: If the fast recovery area is not enabled but was enabled previously, then files created in the previous fast recovery area location are backed up. |
| `DB_RECOVERY_FILE_DEST` | `RECOVERY AREA` and `DB_RECOVERY_FILE_DEST` are synonyms. |
| `RECOVERY FILES` | Backs up all recovery files on disk, whether they are stored in the fast recovery area or other locations on disk. The backups can go to SBT or disk. To backup to disk, you must use the `TO DESTINATION` syntax outlined in [toDestSpec](allocOperandList.md).  Recovery files include full and incremental backup sets, control file autobackups, archived redo log files, and data file copies.  By default, backup optimization is enabled for this command even if the `CONFIGURE` `BACKUP OPTIMIZATION` setting is `OFF`. You can disable backup optimization for `RECOVERY FILES` by specifying `FORCE`. |
| `SPFILE` | Includes the server parameter file in a backup set. The `AS COPY` option is not supported for server parameter file backups.  RMAN backs up the server parameter file currently in use by the target database. RMAN cannot back up the server parameter file when the instance was started with an initialization parameter file. RMAN cannot make incremental backups of the `SPFILE`. |
| `TABLESPACE` `tablespace_name` | Specifies the names of one or more tablespaces. RMAN translates tablespace names internally into a list of data files, then backs up all data files that are currently part of the tablespaces. If the `SYSTEM` tablespace (and thus data file 1) is included in the backup, and if `CONTROLFILE AUTOBACKUP` is not configured, then RMAN also creates a copy of the control file.  When connected to the root in a CDB, refers to tablespaces in the root. Refers to tablespaces in a PDB when connected directly to a PDB.  You cannot back up locally-managed temporary tablespaces, although you can back up dictionary-managed tablespaces.  If the following conditions are met, then RMAN can back up transportable tablespaces that have not been made read/write after being transported:  - The `COMPATIBLE` initialization parameter is set to 11.0.0 or higher. - You are using an Oracle Database 11g or later RMAN client.  If any of the preceding conditions is not met, then RMAN automatically skips transportable tablespaces that have not yet been made read/write. If you specify a transportable tablespace explicitly when any of the conditions is not met, then RMAN issues an error saying that the tablespace does not exist.  Note: If you rename a tablespace, then RMAN detects that the tablespace has changed its name and updates the recovery catalog on the next resynchronization. |
| `backupSpecOperand` | The `backupSpecOperand` that follows a `backupSpec` specifies options that apply to the `backupSpec`. |

backupSpecOperand

This subclause specifies a variety of options and parameters that affect the `backupSpec` clause. Many subclauses are also used with `backupOperand`. Options that are not shared in common with `backupOperand` are listed here. Refer to backupSpecOperand::= for the syntax diagram.

| Syntax Element | Description |
| --- | --- |
| `DELETE [ALL] INPUT` | Deletes the input files after successfully backing them up.  Specify this option only when backing up archived redo log files, data file copies (`COPY OF` or `DATAFILECOPY`), or backup sets. The `BACKUP ARCHIVELOG` command only backs up one copy of each distinct log sequence number, so if the `DELETE INPUT` option is used without the `ALL` keyword, RMAN only deletes the copy of the file that it backs up.  Specifying the `DELETE INPUT` option is equivalent to issuing the `DELETE` command for the input files. When backing up archived redo log files, RMAN uses the configured settings to determine whether an archived redo log can be deleted (`CONFIGURE ARCHIVELOG DELETION POLICY TO BACKED UP`).  The `ALL` option applies only to archived redo log files. If you run `DELETE ALL INPUT`, then the command deletes all copies of corresponding archived redo log files or data file copies that match the selection criteria in the `BACKUP` command (as shown in Example 2-19). For example, if you specify the `SEQUENCE` `n` clause, then RMAN deletes all archived redo log files with same sequence number `n`.  Note: The database retains archived redo log files in the fast recovery area if possible and deletes them automatically when disk space is required. You can use the `BACKUP DELETE INPUT`, `DELETE` `ARCHIVELOG`, and `DELETE OBSOLETE` commands to delete log files manually from inside or outside the recovery area. You do not need to specify `BACKUP DELETE INPUT` when backing up the recovery area because the database automatically deletes log files based on the archived redo log deletion policy and other fast recovery area rules. |
| `FROM TAG` `tag_name` | Identifies files by tag name (see Example 2-18). Only the files that match the tag\_name are backed up. Defined in context with several other commands. |
| `INCLUDE CURRENT CONTROLFILE` | Creates a snapshot of the current control file and places it into one of backup sets produced by the `BACKUP` command.  Note: This option does not apply with `AS COPY` and results in an error message. |

backupTypeSpec

This subclause specifies the form of the `BACKUP` command output: backup set or image copy. Refer to backupTypeSpec::= for the syntax diagram.

| Syntax Element | Description |
| --- | --- |
| `AS BACKUPSET` | Creates backup sets on the specified device. This is the default backup type.  `AS` `BACKUPSET` is the only possibility when backing up to tape, and for creating level 1 incremental backups to any destination. Backup sets are RMAN-specific logical structures. The backup set is the smallest unit of a backup.  The `FILESPERSET` parameter of the `BACKUP` command determines the maximum number of files in each backup set. Archived redo log files and data files are never combined into a single backup set.  When using encrypted backups, data files from tablespaces with different encryption settings are never written into the same backup set.  RMAN cannot back up files with different block sizes into the same backup set. RMAN can back up tablespaces with different block sizes, but puts each differently sized data file into its own backup set.  When unused block compression is applied, RMAN reads only the blocks that are currently allocated to a table. RMAN still checks each of the blocks to see whether the header has marked the block as unused. If a block has been unused, it is not written to the backup.  Unused block compression is turned on automatically when all of the following five conditions are true:  1. The `COMPATIBLE` initialization parameter is set to 10.2 or higher. 	Note: If `COMPATIBLE` is set to 10.2, then only tablespaces created with 10.2 compatibility are optimized to exclude blocks that do not currently contain data. If `COMPATIBLE` is set to 11.0.0 or higher, however, then the first backup that produces backup sets after COMPATIBLE is set to 11.0.0 or higher updates the headers of all locally managed data files so that all locally managed data files can be optimized. 2. There are currently no guaranteed restore points defined for the database. 3. The data file is locally managed 4. The data file is being backed up to a backup set as part of a full backup or a level 0 incremental backup 5. The backup set is created on disk or Oracle Secure Backup is the media manager. 	Note: When backing up to a media manager that is not Oracle Secure Backup, RMAN copies all the blocks regardless of whether they contain data or not.  Note: A corrupt unused block is not harmful. This is because when a block is corrupt and RMAN does not read it because of unused block compression, RMAN does not detect the corruption.  Each backup set contains at least one **backup piece**, which is an RMAN-specific physical file containing the backed up data. You can also use the `BACKUP` command to generate a **proxy copy**, which is a backup in which the entire data transfer is conducted by a media manager.  RMAN only records complete backup sets in the RMAN repository. There are no partial backup sets. When a `BACKUP` command creates backup pieces but does not produce a complete backup set, the backup pieces are discarded.  Note: You cannot stripe a single backup set across multiple channels. You also cannot stripe a single input file across multiple backup sets.  See Also: [Oracle Secure Backup Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/rcmrf&id=OBADM183) to learn how to use Oracle Secure Backup with RMAN |
| `AS COMPRESSED BACKUPSET` | Enables binary compression.  RMAN compresses the data written into the backup set to reduce the overall size of the backup set. All backups that create backup sets can create compressed backup sets. Restoring compressed backup sets is no different from restoring uncompressed backup sets.  RMAN applies a binary compression algorithm as it writes data to backup sets. This compression is similar to the compression provided by many media manager vendors. When backing up to a locally attached tape device, compression provided by the media management vendor is usually preferable to the binary compression provided by `BACKUP AS COMPRESSED BACKUPSET`. Therefore, use uncompressed backup sets and turn on the compression provided by the media management vendor when backing up to locally attached tape devices. Do not use RMAN binary compression and media manager compression together.  Some CPU overhead is associated with compressing backup sets. If the target database is running at or near its maximum load, then you may find the overhead unacceptable. In most other circumstances, compressing backup sets saves enough disk space to be worth the CPU overhead. |
| `AS COPY` | Creates image copies (rather than backup sets).  An image copy is a byte-for-byte identical copy of the original file. You can create image copy backups of data files, control files, data file copies, control file copies, and archived redo log files. Image copy files can only exist on disk. When using incrementally updated backups, the level 0 incremental must be an image copy backup.  By default, `BACKUP` generates backup sets. You can change the default backup type for disk backups to image copies using the `CONFIGURE` `DEVICE TYPE ... BACKUP TYPE TO COPY` command.  RMAN chooses a location for the copy according to the following rules, listed in order of precedence:  1. `FORMAT` specified on `BACKUP` command for the object being backed up 2. `FORMAT` specified for the `BACKUP` command 3. `fileNameConversionSpec` setting for `BACKUP` command 4. `CONFIGURE CHANNEL` `integer` `... FORMAT` 5. `CONFIGURE CHANNEL DEVICE TYPE ... FORMAT` 6. Platform-specific default `FORMAT` (which includes a `%U` for generating a unique file name)  You can create and restore image copy backups with RMAN or use a native operating system command for copying files. When you use RMAN, copies are recorded in the RMAN repository and are more easily available for use in restore and recovery. Otherwise, you must use the `CATALOG` command to add the user-managed copies to the RMAN repository so that RMAN can use them.  You cannot make a copy of a backup set, although you can make an image copy of an image copy. To back up a backup set, use `BACKUP BACKUPSET`. |
| `AS SPARSE BACKUPSET` | Creates sparse backups of sparse data files in the backup set format. To use this clause, the `COMPATIBLE` initialization parameter of the database being backed up must be set to 12.2 or higher.  If you run this command on a non-sparse database, then RMAN performs a traditional backup in the backup set format.  This setting overrides the default device type parameter set using the [CONFIGURE](CONFIGURE.md) command.  See the `AS BACKUPSET` clause for more information on the backup set format. |
| `AS NONSPARSE BACKUPSET` | Creates traditional (non-sparse) backups of data files in a sparse environment, in the backup set format. The source data files can be sparse and non-sparse. To use this clause, the `COMPATIBLE` initialization parameter of the database being backed up must be set to 12.2 or higher.  See the `AS BACKUPSET` clause for more information on the backup set format. |
| `AS SPARSE COMPRESSED BACKUPSET` | Creates sparse backups of sparse data files in the compressed backup set format. To use this clause, the `COMPATIBLE` initialization parameter of the database must be set to 12.2 or higher.  If you run this command on a non-sparse database, then RMAN performs a traditional backup in the compressed backup set format.  This setting overrides the default device type parameter set using the [CONFIGURE](CONFIGURE.md) command.  See the `AS COMPRESSED BACKUPSET` clause for more information on the compressed backup set format. |
| `AS NONSPARSE COMPRESSED BACKUPSET` | Creates traditional (non-sparse) backups of data files in a sparse environment, in the compressed backup set format. The source data files can be sparse and non-sparse. To use this clause, the `COMPATIBLE` initialization parameter of the database must be set to 12.2 or higher.  See the `AS COMPRESSED BACKUPSET` clause for more information on the compressed backup set format. |
| `AS SPARSE COPY` | Creates sparse backups of sparse data files in the image copy format. To use this clause, the `COMPATIBLE` initialization parameter of the database must be set to 12.2 or higher.  If you run this command on a non-sparse database, then RMAN performs a traditional full backup in the image copy format.  This setting overrides the default device type parameter set using the [CONFIGURE](CONFIGURE.md) command.  See the `AS COPY` clause for more information on the image copy format. |
| `AS NONSPARSE COPY` | Creates traditional (non-sparse) backups of data files in a sparse environment in the image copy format. The source data files can be sparse and non-sparse. To use this clause, the `COMPATIBLE` initialization parameter of the database must be set to 12.2 or higher.  See the `AS COPY` clause for more information on the image copy format. |

copyOfSpec

This subclause specifies the form of the `BACKUP` command output: backup set or image copy. Refer to copyOfSpec::= for the syntax diagram.

| Syntax Element | Description |
| --- | --- |
| `COPY OF DATABASE` | Makes a backup of previous image copies of all data files and control files in the database. All data files that would normally be included by `BACKUP` `DATABASE` are expected to have copies: if not, RMAN signals an error. It is not necessary for all copies to have been produced by a single `BACKUP` command. If multiple copies exist of data file, then RMAN backs up the latest. Optionally, specify the copies by tag name (for example, `FULL_COLD_COPY`).  In a CDB, creates a backup of previous image copies of all data files and control files in the CDB. You connect to the root to back up the whole CDB. In a PDB, creates a backup of previous image copies of all data files and control files in the PDB. To backup a PDB, connect to that PDB.  Note: The output of this command can be image copies or backup sets. |
| `COPY OF DATABASE ROOT` | In a CDB, makes a backup of previous image copies of the data files and control files in the root. See the previous description of `COPY OF DATABASE`. |
| `COPY OF PLUGGABLE DATABASE ` `pdb_name` | In a CDB, makes a backup of previous image copies of the data files and controls files in one or more PDBs. Use a comma-delimited list to specify multiple PDBs and connect to the root. |
| `COPY OF DATAFILE` `datafileSpec` | Makes a backup of a previous image copy of one or more data files. Specify the data file by file number (`DATAFILE 3`) or file name (`DATAFILE '?/oradata/trgt/users01.dbf'`). You specify the data file name and not the file name of the copy of the data file. If multiple copies of a data file exist, then RMAN backs up the most recent copy.  Note: It is not necessary for the image copies that you are backing up to have been created by a single `BACKUP` command.  Note: The output of this command can be image copies or backup sets.  See Also: `datafileSpec` |
| `COPY OF TABLESPACE` `tablespace_name` | Makes a backup of previous image copies of the data files in one or more specified tablespaces. All data files that are normally included by `BACKUP` `TABLESPACE` should have copies: if not, then RMAN signals an error. It is not necessary for all copies to have been produced by a single `BACKUP` command. If multiple copies exist of data file, then RMAN backs up the latest.  Specify the tablespaces in the list by tablespace name (for example, `users`) or specify a particular copy by tag name (for example, `0403_CPY_OF_USERS`). If you do not specify `TAG`, then RMAN backs up the most recent data file copy for each data file in the tablespace.  Note: The output of this command can be image copies or backup sets. |

datafileCopySpec

This subclause specifies data file copies. Refer to datafileCopySpec::= for the syntax diagram.

| Syntax Element | Description |
| --- | --- |
| `'` `filename` `'` | Specifies the file names of one or more data file image copies. |
| `ALL` | Specifies all data file image copies for back up.  When used with CDBs, RMAN skips backing up all copies of PDBs that were dropped. |
| `LIKE` `'` `string_pattern` `'` | Specifies a file name pattern. The percent sign (`%`) is a wildcard that means zero or more characters; an underscore (`_`) is a wildcard that means one character. |
| `FROM TAG` `tag_name` | Specifies a list of one or more data file copies, identified by the tag name. If multiple data file copies with this tag exist, then RMAN backs up only the most current data file copy of any particular data file. Tags are not case sensitive. |
| `   NODUPLICATES` | Prevents the inclusion of identical data file copies in a backup operation (Example 2-29). For each set of duplicate data file copies, the file with the most recent timestamp is selected. |

duration

This subclause specifies data file copies. Refer to duration::= for the syntax diagram.

| Syntax Element | Description |
| --- | --- |
| `DURATION` `hh:mm` | Specifies a maximum time for a backup command to run. If a backup command does not complete in the specified duration, then the backup stops.  Without the `PARTIAL` option, the backup command is considered to have failed if it does not complete in the specified duration, and RMAN reports an error. If the backup command is part of a `RUN` block, then subsequent commands in the `RUN` block do not execute. |
| `   MINIMIZE` `{LOAD \| TIME}` | With disk backups, you can use `MINIMIZE TIME` run the backup at maximum speed (default), or `MINIMIZE LOAD` to slow the rate of backup to lessen the load on the system. With `MINIMIZE LOAD` the backup takes the full specified duration.  If you specify `TIME`, then file most recently backed up is given the lowest priority to back up. This scheduling mechanism provides for the eventual complete backup of the database during successive backup windows, as different data files are backed up in round-robin fashion. |
| `   PARTIAL` | With the `PARTIAL` option, the command is considered to have completed successfully and no error is reported by RMAN even if the whole backup is not completed in the specified duration.  Without the `PARTIAL` option, the backup command is considered to have failed if it does not complete in the specified duration, and RMAN reports an error. If the backup command is part of a `RUN` block, then subsequent commands in the `RUN` block do not execute.  Whether `PARTIAL` is used or not, all backup sets completed before the backup is interrupted are retained and can be used in `RESTORE` and `RECOVER` operations. |

forRecoveryOfSpec

This subclause specifies a backup for use in an incrementally updated backup strategy. You must specify `INCREMENTAL LEVEL 1` when specifying `FOR RECOVER OF`. Refer to forRecoveryOfSpec::= for the syntax diagram.

| Syntax Element | Description |
| --- | --- |
| `FOR RECOVER OF COPY` | Specifies that this incremental backup contains all changes since a previous data file copy or incremental backup. By default, RMAN creates a differential incremental backup. You must specify `CUMULATIVE` to force RMAN to create cumulative backups.  Use the `WITH TAG` clause to separate this incremental backup strategy from the rest of your backup strategies. If you do not specify `WITH TAG`, then RMAN uses the most recent data file copy as the basis for the incremental backup.  A `BACKUP INCREMENTAL LEVEL 1 FOR RECOVER OF COPY` command can create image copies or backup sets. RMAN creates level 0 image copies if no such copies exist, but otherwise creates backup sets.  See Also: [Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/rcmrf&id=BRADV8186) to learn how to make incrementally updated backups |
| `   WITH TAG ` `tag_name` | Specifies the tag of the level 0 incremental backup serving as the basis of the backup strategy (see Example 2-20).  By using the `BACKUP INCREMENTAL ... WITH TAG` syntax, you can create level 1 incremental backups suitable for rolling forward a level 0 image copy. You can then use `RECOVER` `COPY OF ... WITH TAG` to apply level 1 backups to this copy. In this way, the strategy continues to roll forward the data file copy so that media recovery does not need to apply as many changes. This technique is the basis for the Enterprise Manager strategy for disk backups.  When `WITH TAG` is specified, RMAN automatically assigns all new incremental backups in the strategy the same tag as the level 0 data file copy. RMAN decides which blocks to include in the level 1 backup based on the available incremental backups that have this tag.  Note: If the `BACKUP` command has both the `TAG` and `WITH TAG` options, then RMAN issues a warning stating that the `TAG` option is ignored and that incremental backups receive the tag specified by `WITH TAG`.  If no level 0 backup with the tag specified in the `WITH TAG` parameter exists in either the current or parent database incarnation, then `FOR RECOVER OF COPY` option creates a level 0 data file copy tagged with the value specified in the `WITH TAG` parameter. |
| `   DATAFILECOPY  FORMAT` `formatSpec` | Specifies a pattern for naming the output image copies.  If you add a data file to the database, then you do not need to change the backup script because RMAN automatically creates the level 0 data file copy required by the incrementally updated backup strategy for the newly created file. |
| `FOR RECOVER OF TAG` `tag_name` | Backs up the archived redo log files or incremental backups that are intended to recover the level 0 incremental backup specified by `tag_name`.  For example, the `BACKUP INCREMENTAL LEVEL 1 FOR RECOVER OF TAG wholedb ARCHIVELOG ALL` command backs up all archived redo log files needed to recover the level 0 incremental backup tagged `wholedb`. |

notBackedUpSpec

This subclause specifies that RMAN only backs up files that have not yet been backed up to the same device type. Refer to notBackedUpSpec::= for the syntax diagram.

| Syntax Element | Description |
| --- | --- |
| `NOT BACKED UP` | Backs up only those files—of the files specified on the `BACKUP` command—that RMAN has never backed up for the same device type (see Example 2-28).  This subclause is a convenient way to back up new data files after adding them to the database. RMAN does not examine data file checkpoints, but backs up any data file that is not already backed up. You can also specify `NOT BACKED UP` when backing up backup sets.  Using `BACKUP` with this clause does manually what an archived redo log deletion policy can do automatically. If you specify the `CONFIGURE` `ARCHIVELOG DELETION POLICY TO BACKED UP` `integer` `TIMES` command, then a `BACKUP ARCHIVELOG ALL` command copies all logs unless `integer` backups exist on the specified device type. If `integer` backups of the logs exist, then the `BACKUP` command skips the logs. In this way, the archived log deletion policy functions as a default `NOT BACKED UP` `integer` `TIMES` clause on the `BACKUP` command.  Archival backups created with the `KEEP` option are not counted when evaluating the `NOT BACKED UP` subclause. For example, if you issue the command  ``` BACKUP ARCHIVELOG SEQUENCE 345 NOT BACKED UP 3 TIMES ```  and the specified log is already backed up into two non- `KEEP` backup sets and one `KEEP` backup set, then that command backs up the log one more time.  Note: This clause overrides backup optimization (`CONFIGURE BACKUP OPTIMIZATION`) and archived redo log file deletion policies (`CONFIGURE ARCHIVELOG DELETION POLICY`). |
| `AT ANY SCN` | Backs up only those data files that have not been backed up at any SCN.  This option is a convenient way to back up only the new data files. When you use the `BACKUP DATAFILECOPY ALL` command to back up disk backups that are part of an incrementally updated backup strategy to tape or Oracle Cloud, using the `SINCE TIME` clause also backs up data files that are already backed up. Use `AT ANY SCN` to only back up new data files that have never been backed up. |
| `integer` `TIMES` | Backs up only those archived redo log files that have not been backed up at least `integer` times.  Note: You can only specify `NOT BACKED UP` `integer` `TIMES` when backing up archived redo log files into backup sets.  To determine the number of backups for a file, RMAN only considers backups created on the same device type as the current backup.  This option is a convenient way to back up archived redo log files on a specified media. For example, you want to keep at least three copies of each log on tape. |
| `   SINCE TIME` `'` `date_string` `'` | Specifies the date after which RMAN backs up files that have no backups.  The `date_string` is either a date in the current `NLS_DATE_FORMAT` or a SQL date expression such as `'SYSDATE-1'`. When calculating the number of backups for a file, RMAN only considers backups created on the same device type as the current backup.  This option is a convenient way to back up data files that were not backed up during a previous failed backup. For example, you back up the database, but the instance fails halfway through. You can restart the backup with the `NOT BACKED UP SINCE TIME` clause and avoid backing up those files that are already backed up. If `AS BACKUPSET` is specified, then this feature is only useful if RMAN generates multiple backup sets during the backup.  When determining whether a file has been backed up, the `SINCE` date is compared with the completion time of the most recent backup. For `BACKUP AS BACKUPSET`, the completion time for a file in a backup set is the completion time of the entire backup set. In other words, all files in the same backup set have the same completion time. |

skipSpec

This subclause specifies which files to exclude from the backup. Refer to skipSpec::= for the syntax diagram.

| Syntax Element | Description |
| --- | --- |
| `SKIP` | Excludes data files or archived redo log files according to the criteria specified by the following keywords.  Note: You can also specify this option in the `backupSpec` clause. |
| `   INACCESSIBLE` | Excludes data files or archived redo log files that cannot be read due to I/O errors.  A data file is only considered inaccessible if it cannot be read. Some offline data files can still be read because they still exist on disk. Others have been deleted or moved and so cannot be read, making them inaccessible. |
| `   OFFLINE` | Excludes offline data files. |
| `   READONLY` | Excludes read-only data files. |

Examples

Example 2-13 Backing Up a Database

This example starts the RMAN client from the operating system command line and then connects to a target database using operating system authentication. The `BACKUP` command backs up all data files, the current control file, the server parameter file, and archived redo log files to the default storage device:

```
% rman
RMAN> CONNECT TARGET /
RMAN> BACKUP DATABASE PLUS ARCHIVELOG;
```

Example 2-14 Backing Up a Sparse Database

This example uses the `BACKUP` command to backup a sparse database in the backup set format and the archive log.

```
RMAN> BACKUP AS SPARSE BACKUPSET DATABASE PLUS ARCHIVELOG;
```

Example 2-15 Backing Up Multiple PDBs

This example connects to the root using operating system authentication and then creates backups of the PDBs `hr_pdb` an `sales_pdb`.

```
%rman
RMAN> CONNECT TARGET /
RMAN> BACKUP PLUGGABLE DATABASE hr_pdb, sales_pdb;
```

Example 2-16 Performing a Cumulative Incremental Backup

This example backs up all blocks changed in the database since the most recent level 0 incremental backup. If no level 0 backup exists when you run a level 1 backup, then RMAN makes a level 0 backup automatically. Any inaccessible files are skipped.

```
BACKUP 
  INCREMENTAL LEVEL 1 CUMULATIVE
  SKIP INACCESSIBLE 
  DATABASE;
```

Example 2-17 Distributing a Backup Across Multiple Disks

This example backs up tablespaces to two different disks and lets RMAN perform automatic parallelization of the backup. The `%U` in the `FORMAT` string is a substitution variable that generates a unique file name for each output image copy.

```
RUN
{
  ALLOCATE CHANNEL dev1 DEVICE TYPE DISK FORMAT '/disk1/%U';
  ALLOCATE CHANNEL dev2 DEVICE TYPE DISK FORMAT '/disk2/%U'; 
  BACKUP AS COPY
    TABLESPACE SYSTEM, tools, users, undotbs;
}
```

Example 2-18 Identifying Data File Copies by Tag

In this example, you back up data file image copies to tape. The `BACKUP` command locates all data file copies with the tag `LATESTCOPY`, backs them up to tape, and names the backups using substitution variables. The variable `%f` specifies the absolute file number, whereas `%d` specifies the name of the database. After the data file copies are on tape, the example deletes all image copies with the tag `LATESTCOPY`.

```
BACKUP 
  DEVICE TYPE sbt
  DATAFILECOPY 
    FROM TAG 'LATESTCOPY'
  FORMAT 'Datafile%f_Database%d';
DELETE COPY TAG 'LATESTCOPY';
```

Example 2-19 Backing Up and Deleting Archived Redo Log Files

This example assumes that you have two archiving destinations set: `/disk2/PROD/archivelog/` and `/disk1/arch/`. The command backs up one archived redo log for each unique sequence number. For example, if archived redo log 1000 is in both directories, then RMAN only backs up one copy this log. The `DELETE INPUT` clause with the `ALL` keyword deletes all archived redo log files from both archiving directories after the backup.

```
BACKUP DEVICE TYPE sbt
  ARCHIVELOG LIKE '/disk%arc%'
  DELETE ALL INPUT;
```

Sample output for the preceding command appears as follows:

```
Starting backup at 12-MAR-13
allocated channel: ORA_SBT_TAPE_1
channel ORA_SBT_TAPE_1: SID=150 device type=SBT_TAPE
channel ORA_SBT_TAPE_1: Oracle Secure Backup
channel ORA_SBT_TAPE_1: starting archived log backup set
channel ORA_SBT_TAPE_1: specifying archived log(s) in backup set
input archived log thread=1 sequence=4 RECID=4 STAMP=616789551
input archived log thread=1 sequence=5 RECID=5 STAMP=616789551
input archived log thread=1 sequence=6 RECID=6 STAMP=616789554
input archived log thread=1 sequence=7 RECID=7 STAMP=616789731
input archived log thread=1 sequence=8 RECID=8 STAMP=616789825
input archived log thread=1 sequence=9 RECID=10 STAMP=616789901
input archived log thread=1 sequence=10 RECID=12 STAMP=616789985
channel ORA_SBT_TAPE_1: starting piece 1 at 12-MAR-13
channel ORA_SBT_TAPE_1: finished piece 1 at 12-MAR-13
piece handle=0vice0g7_1_1 tag=TAG20130312T105917 comment=API Version 2.0,MMS Version 10.1.0.3
channel ORA_SBT_TAPE_1: backup set complete, elapsed time: 00:00:25
channel ORA_SBT_TAPE_1: deleting archived log(s)
archived log file name=/disk2/PROD/archivelog/2013_03_09/o1_mf_1_4_2z45sgrc_.arc RECID=4 STAMP=616789551
archived log file name=/disk2/PROD/archivelog/2013_03_09/o1_mf_1_5_2z45sgrc_.arc RECID=5 STAMP=616789551
archived log file name=/disk2/PROD/archivelog/2013_03_09/o1_mf_1_6_2z45sl3g_.arc RECID=6 STAMP=616789554
archived log file name=/disk2/PROD/archivelog/2013_03_09/o1_mf_1_7_2z45z2kt_.arc RECID=7 STAMP=616789731
archived log file name=/disk2/PROD/archivelog/2013_03_09/o1_mf_1_8_2z4620sk_.arc RECID=8 STAMP=616789825
archived log file name=/disk1/arch/archiver_1_8_616789153.arc RECID=9 STAMP=616789825
archived log file name=/disk2/PROD/archivelog/2013_03_09/o1_mf_1_9_2z464dhk_.arc RECID=10 STAMP=616789901
archived log file name=/disk1/arch/archiver_1_9_616789153.arc RECID=11 STAMP=616789901
archived log file name=/disk2/PROD/archivelog/2013_03_09/o1_mf_1_10_2z4670gr_.arc RECID=12 STAMP=616789985
archived log file name=/disk1/arch/archiver_1_10_616789153.arc RECID=13 STAMP=616789985
Finished backup at 12-MAR-13
 
Starting Control File and SPFILE Autobackup at 12-MAR-13
piece handle=c-28643857-20130312-02 comment=API Version 2.0,MMS Version 10.1.0.3
Finished Control File and SPFILE Autobackup at 12-MAR-13
```

Example 2-20 Scripting Incrementally Updated Backups

By incrementally updating backups, you can avoid the overhead of making full image copy backups of data files, while also minimizing media recovery time. For example, if you run a daily backup script, then you never have more than one day of redo to apply for media recovery.

Assume you run the following script daily. On first execution, the script creates an image copy backup of the database on disk with the specified tag. On second execution, the script creates a level 1 differential incremental backup of the database. On every subsequent execution, RMAN applies the level 1 incremental backup to the data file copy and then makes a new level 1 backup.

```
RUN
{
  RECOVER COPY OF DATABASE 
    WITH TAG 'incr_update';
  BACKUP
    INCREMENTAL LEVEL 1
    FOR RECOVER OF COPY WITH TAG 'incr_update'
    DATABASE;
}
```

Example 2-21 Backing Up Disk-Based Backup Sets to Tape

Assume your goal is to keep recent backup sets on disk and older backup sets on tape. Also, you want to avoid keeping copies of the same backup set on disk and tape simultaneously. This example backs up backup sets created more than two weeks ago to tape and then deletes the backup pieces from disk.

```
BACKUP
  DEVICE TYPE sbt 
  BACKUPSET
    COMPLETED BEFORE 'SYSDATE-14' 
  DELETE INPUT;
```

Example 2-22 Duplexing a Database Backup

This example uses the `COPIES` parameter to create two compressed backups of the database, with each backup on a separate disk. The output locations are specified in the `FORMAT` parameter.

```
BACKUP AS COMPRESSED BACKUPSET
  DEVICE TYPE DISK 
  COPIES 2
  DATABASE
  FORMAT '/disk1/db_%U', '/disk2/db_%U';
```

Example 2-23 Specifying How Channels Divide Workload

This example explicitly parallelizes a backup by using the `CHANNEL` parameter to specify which channels back up which files and to which locations.

```
RUN
{
  ALLOCATE CHANNEL ch1 DEVICE TYPE sbt
    PARMS 'ENV=(OB_DEVICE_1=stape1)';
  ALLOCATE CHANNEL ch2 DEVICE TYPE sbt
    PARMS 'ENV=(OB_DEVICE_1=stape2)';
  BACKUP 
    (DATABASE        # ch1 backs up database to tape drive stape1
      CHANNEL ch1)
    (ARCHIVELOG ALL
      CHANNEL ch2);  # ch2 backs up archived redo log files to tape drive stape2
}
```

Example 2-24 Creating an Incremental Backup for Refresh of a Standby Database

In this example, your goal is make an incremental backup of the primary database and use it to update an associated standby database. You start the RMAN client, `CONNECT` to the primary database as `TARGET`, and then connect to the recovery catalog. The `BACKUP` command creates an incremental backup of the primary database that can be applied at a standby database to update it with changes since the specified SCN.

```
RMAN> CONNECT TARGET /

connected to target database: PROD (DBID=39525561)

RMAN> CONNECT CATALOG rco@catdb

recovery catalog database Password: password
connected to recovery catalog database

RMAN> BACKUP DEVICE TYPE DISK
2> INCREMENTAL FROM SCN 404128 DATABASE
3>  FORMAT '/disk1/incr_standby_%U';
```

Example 2-25 Specifying Corruption Tolerance for Data File Backups

This example assumes a database that contains five data files. It uses the `SET` `MAXCORRUPT` command to indicate than only one corruption is tolerated in each data file. Because the `CHECK LOGICAL` option is specified on the `BACKUP` command, RMAN checks for both physical and logical corruption.

```
RUN
{
  SET MAXCORRUPT FOR DATAFILE 1,2,3,4,5 TO 1;
  BACKUP CHECK LOGICAL
    DATABASE;
}
```

Example 2-26 Creating a Consistent Database Backup for Archival Purposes

This example uses a `keepOption` to create an archival backup set that cannot be considered obsolete for one year. The example backs up the database, archives the redo in the current online logs to ensure that this new backup is consistent, and backs up only those archived redo log files needed to restore the data file backup to a consistent state.

The `BACKUP` command also creates a restore point to match the SCN at which this backup is consistent. The `FORMAT` parameter must be capable of creating multiple backup pieces in multiple backup sets.

```
BACKUP DATABASE
  FORMAT '/disk1/archival_backups/db_%U.bck' 
  TAG quarterly
  KEEP UNTIL TIME 'SYSDATE + 365'
  RESTORE POINT Q1FY06;
```

Example 2-27 Exempting Copies from the Retention Policy

The following example copies two data files and exempts them from the retention policy forever. The control file and server parameter file are also backed up, even with autobackup off.

`KEEP` ` FOREVER` requires a recovery catalog.

```
SHUTDOWN IMMEDIATE;
STARTUP MOUNT;
BACKUP
  KEEP FOREVER
  FORMAT '?/dbs/%U_longterm.cpy'
  TAG LONGTERM_BCK
  DATAFILE 1 DATAFILE 2;
ALTER DATABASE OPEN;
```

Example 2-28 Backing Up Files That Need Backups

Assume that you back up the database and archived redo log files every night to tape by running the following command.

```
BACKUP
  MAXSETSIZE 500M
  DATABASE PLUS ARCHIVELOG;
```

The preceding command sets an upper limit to the size of each backup set so that RMAN produces multiple backup sets. Assume that the media management device fails halfway through the backup and is then restarted. The next day you discover that only half the backup sets completed. In this case, you can run the following command in the evening:

```
BACKUP 
  NOT BACKED UP SINCE TIME 'SYSDATE-1'
  MAXSETSIZE 500M
  DATABASE PLUS ARCHIVELOG;
```

With the preceding command, RMAN backs up only files not backed up during in the previous 24 hours. When RMAN determines that a backup from the specified time window is available, it displays output like the following:

```
skipping datafile 1; already backed up on 18-JAN-13
skipping datafile 2; already backed up on 18-JAN-13
skipping datafile 3; already backed up on 18-JAN-13
```

If you place the `NOT` `BACKED` `UP` `SINCE` clause immediately after the `BACKUP` command, then it affects all objects to be backed up. You can also place it after individual `backupSpec` clauses to cause only backups for those objects described by the `backupSpec` to be subject to the limitation.

Example 2-29 Using NODUPLICATES To Back Up Data File Copies

This example creates a data file copy of data file 2 named `/disk2/df2.cpy`. The example then backs up this data file copy to the `/disk1` and `/disk3` directories. The `NODUPLICATES` option on the final `BACKUP` command indicates that only one copy of data file `2` is backed up.

```
BACKUP AS COPY
  DATAFILE 2
  FORMAT '/disk2/df2.cpy' TAG my_tag;
BACKUP AS COPY
  DATAFILECOPY '/disk2/df2.cpy' 
  FORMAT '/disk1/df2.cpy';
BACKUP AS COPY
  DATAFILECOPY '/disk1/df2.cpy' 
  FORMAT '/disk3/df2.cpy';
BACKUP
  DEVICE TYPE sbt
  DATAFILECOPY ALL NODUPLICATES; # backs up only copy of data file 2
```

Example 2-30 Copying Archived Log From Operating System File to ASM

```
BACKUP AS COPY REUSE 
ARCHIVELOG LIKE "/ade/b/369893928/oracle/work/arc_dest/arcr_1_11_686060575.arc"
AUXILIARY FORMAT "+RCVAREA";
```

Example 2-31 Multisection Backup of Data Files as Image Copies

This example creates a multisection backup of the data file `users_df.dbf`. The backup is created as image copies and each backup piece cannot exceed 150MB.

```
BACKUP AS COPY
SECTION SIZE 150M
DATAFILE '/oradata/dbs/users_df.dbf';
```

Example 2-32 Multisection Incremental Backup of Database as Backup Sets

This example creates a multisection incremental backup of the database as backup sets. The incremental backup includes all data file blocks that changed at SCN greater than or equal to 8564. The `FORMAT` clause is mandatory when you use `INCREMENTAL FROM SCN` to create a multisection incremental backup.

```
BACKUP
FORMAT '/tmp/datafiles/db_incr_ms_%U'
INCREMENTAL FROM SCN 8564
SECTION SIZE 400M
DATABASE;
```

Example 2-33 Multisection Incremental Backup of Tablespaces

This example creates a multisection incremental backup of the tablespace `orders` as backup sets. Before creating the backup, three channels are explicitly allocated using the `ALLOCATE CHANNEL` command. Therefore, RMAN uses these channels to write, in parallel, to the backup pieces.

```
run {
   ALLOCATE CHANNEL MY_CH1 TYPE DISK;
   ALLOCATE CHANNEL MY_CH2 TYPE DISK;
   ALLOCATE CHANNEL MY_CH3 TYPE DISK;
   BACKUP
     INCREMENTAL LEVEL 1
     AS COMPRESSED BACKUPSET
     SECTION SIZE 100M
     TABLESPACE sales;
    };
```

Example 2-34 Cross-Platform Backup of the Entire Database

This example creates a cross-platform backup of the entire database for transport to the Linux x86 64-bit platform. The source platform is Microsoft Windows IA (32-bit) and the backup is stored in a backup set named `full_db.bck`. The database must be placed in read-only mode before the backup is created.

```
BACKUP
    TO PLATFORM='Linux x86 64-bit'
    FORMAT '/tmp/xplat_backups/full_db.bck'
    DATABASE;
```

Example 2-35 Cross-Platform Backup of a Consistent Tablespace

This example backs up the tablespace `example` for cross-platform transport. The tablespace must be placed in read-only mode before the backup is performed. The backup set containing the tablespace data is called `example_readonly.bck`. The metadata required to plug this tablespace into the target database is stored in the backup set `example_dmp.bck`.

```
BACKUP
   FOR TRANSPORT
   FORMAT '/tmp/xplat_backups/example_readonly.bck'
   TABLESPACE example
   DATAPUMP FORMAT '/tmp/xplat_backups/example_dmp.bck';
```

Example 2-36 Cross-Platform Backup of a Tablespace Using Multiple Backup Sets

This example creates a cross-platform backup of the tablespace `example` using multiple backup sets. Ensure that the tablespace is read-only before you create the backup. Because `FILESPERSET` is set to 1, each backup set contains only one input file. The backup sets use unique names that begin with `db_multiple_`.

```
BACKUP
   FOR TRANSPORT
   FILESPERSET 1
   FORMAT '/tmp/xplat_backups/db_multiple_%U'
   TABLESPACE example
   DATAPUMP FORMAT '/tmp/xplat_backups/db_multiple.dmp';
```

Example 2-37 Cross-Platform Backup of a Tablespace Using Multiple Backup Pieces

This example creates a cross-platform backup of the tablespace `example`. The backup uses multiple backup pieces because `MAXPIECESIZE` is set in the `ALLOCATE CHANNEL` command. Ensure that the tablespace is in read-only mode before the backup is created.

```
RUN
{
   ALLOCATE CHANNEL c1 DEVICE TYPE disk MAXPIECESIZE 301464;
   BACKUP
      FOR TRANSPORT
      FORMAT '/tmp/xplat_backups/example_multi-piece.bck'
      TABLESPACE example
      DATAPUMP FORMAT '/tmp/xplat_backups/example_multi-piece_dmp.bck';}
```

Example 2-38 Cross-Platform Inconsistent Backup of a Tablespace

This example creates a cross-platform level 0 incremental backup of the tablespace `example`. The tablespace is in read-write mode at the time of creating the backup and, therefore, you use `ALLOW INCONSISTENT` to create an inconsistent backup.

Note that inconsistent backups of tablespaces cannot be used to directly plug the tablespace into the destination database. You must use an incremental backup of the tablespace that is created when the tablespace is read-only to make the tablespace consistent. Example 2-39 describes how to create a cross-platform incremental backup.

```
BACKUP
    FOR TRANSPORT
    ALLOW INCONSISTENT
    INCREMENTAL LEVEL 0
    FORMAT '/tmp/xplat_backups/example_inconsist.bck'
    TABLESPACE example;
```

Example 2-39 Cross-Platform Incremental Backup of a Tablespace

This example creates a cross-platform level 1 incremental backup of the tablespace `example`. The tablespace is placed in read-only mode before this backup is created. This backup contains changes made to the tablespace after the most recent incremental backup was created. The backup is stored in a backup set called `example_inconsist_incr.bck`. The metadata required to plug the tablespace into the destination database is stored in the backup set `example_incr_dmp.bck`.

You can use this level 1 incremental backup, along with the level 0 incremental backup created in Example 2-38, to transport the tablespace example to a different platform. On the destination database, you first restore the level 0 incremental backup created in Example 2-38 to create a set of foreign data files. These foreign data files are inconsistent because the tablespace was in read/write mode when the level 0 incremental backup was created. You then apply a level 1 incremental backup to the foreign data files. Next, you plug the tablespace in to the destination database by restoring the backup set specified in the `DATAPUMP` clause. See [Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/rcmrf&id=BRADV783) for a complete example of performing cross-platform inconsistent tablespace transport using backup sets.

In most scenarios, after creating the level 0 incremental backup, you create multiple level 1 incremental backups with the tablespace is placed in read/write mode. The final incremental level 1 backup is created with the tablespace placed in read-only mode. These incremental backups that are created and applied over time help minimize the data divergence between the source and destination database.

```
BACKUP
   FOR TRANSPORT
   INCREMENTAL LEVEL 1
   TABLESPACE example
   FORMAT '/tmp/xplat_backups/example_inconsist_incr.bck'
   DATAPUMP FORMAT '/tmp/xplat_backups/example_incr_dmp.bck';
```