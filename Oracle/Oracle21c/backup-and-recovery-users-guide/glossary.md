---
title: "Backup and Recovery User's Guide"
book: "Database Backup and Recovery User's Guide"
doc_id: F31836-11
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/bradv/glossary.html
tags:
  - oracle
  - 21c
  - backup-and-recovery-users-guide
---

### active database duplication

A duplicate database that is created over a network without restoring backups of the target database. This technique is an alternative to backup-based duplication.

### ancestor incarnation

The parent incarnation is the database incarnation from which the current incarnation branched following an `OPEN RESETLOGS` operation. The parent of the parent incarnation is an ancestor incarnation. Any parent of an ancestor incarnation is also an ancestor incarnation.

### application container

A named set of application PDB s that are plugged in to an application root.

### application PDB

A PDB that is plugged in to an application container.

### application root

The root container within an application container. Every application container has exactly one application root. An application root can contain common objects and is created with the `CREATE PLUGGABLE DATABASE` statement.

### archival backup

A database backup that is exempted from the normal backup and recovery strategy. Typically, these backups are archived onto separate storage media and retained for long periods.

### archived redo log

A copy of a filled member of an online redo log group made when the database is in `ARCHIVELOG` mode. After the LGWR process fills each online redo log with redo records, the archiver process copies the log to one or more redo log archiving destinations. This copy is the archived redo log. RMAN does not distinguish between an original archived redo log and an image copy of an archived redo log; both are considered image copies.

### archived redo log deletion policy

A configurable, persistent RMAN policy that governs when archived redo logs can be deleted. You can configure the policy with the `CONFIGURE ARCHIVELOG DELETION POLICY` command.

### archived redo log failover

An RMAN feature that enables RMAN to complete a backup even when some archived log destinations are missing logs or have logs with corrupt blocks. For example, if you back up logs in the fast recovery area that RMAN determines are corrupt, RMAN can search for logs in other archiving locations and back them up instead if they are intact.

### ARCHIVELOG mode

The mode of the database in which Oracle Database copies filled online redo logs to disk. Specify the mode at database creation or with the `ALTER` `DATABASE` `ARCHIVELOG` statement.

See Also: archived redo log, NOARCHIVELOG mode

### archiving

The operation in which a filled online redo log file is copied to an offline log archiving destination. An offline copy of an online redo logs is called an archived redo log. You must run the database in `ARCHIVELOG` mode to archive redo logs.

### asynchronous I/O

A server process can begin an I/O and then perform other work while waiting for the I/O to complete while RMAN is either reading or writing data. RMAN can also begin multiple I/O operations before waiting for the first I/O to complete.

### automatic channel allocation

The ability of RMAN to perform backup and restore tasks without requiring the use of the `ALLOCATE CHANNNEL` command. You can use the `CONFIGURE` command to specify disk and tape channels. Then, you can issue commands such as `BACKUP` and `RESTORE` at the RMAN command prompt without manually allocating channels. RMAN uses whatever configured channels that it needs to execute the commands.

### Automatic Diagnostic Repository (ADR)

A system-managed repository for storing and organizing database trace files and other diagnostic data. ADR provides a comprehensive view of all the serious errors encountered by the database and maintains all relevant data needed for problem diagnostic and their eventual resolution. The repository contains data describing incidents, traces, dumps, alert messages, data repair records, data integrity check records, SQL trace information, core dumps, and so on.

The initialization parameter `DIAGNOSTIC_DEST` specifies the location of the ADR base, which is the directory that contains one or more ADR homes. Each ADR home is used by a product or a product instance to store diagnostic data in well-defined subdirectories. For example, diagnostic data for an Oracle Database instance is stored in its ADR home, which includes an `alert` subdirectory for alert messages, a `trace` subdirectory for trace files, and so on. The easiest way to locate trace files and the alert log is to run the following SQL query: `SELECT NAME, VALUE FROM V$DIAG_INFO`.

### Automatic Storage Management (ASM)

A vertical integration of both the file system and the volume manager built specifically for Oracle Database files. ASM consolidates storage devices into easily managed disk groups and provides benefits such as mirroring and striping without requiring a third-party logical volume manager.

### automatic undo management mode

A mode of the database in which undo data is stored in a dedicated undo tablespace. The only undo management that you must perform is the creation of the undo tablespace. All other undo management is performed automatically.

### auxiliary channel

An RMAN channel that is connected to an auxiliary instance. An auxiliary channel is specified with the `AUXILIARY` keyword of the `ALLOCATE CHANNEL` or `CONFIGURE CHANNEL` command.

### auxiliary database

(1) A database created from target database backups with the RMAN `DUPLICATE` command.

(2) A temporary database that is restored to a new location and then started with a new instance name during tablespace point-in-time recovery (TSPITR). A TSPITR auxiliary database contains the recovery set and auxiliary set.

### auxiliary destination

In a transportable tablespace operation, the location on disk where auxiliary set files such as the parameter file, data files (other than those of the tablespaces being transported), control files, and online redo logs of the auxiliary instance can be stored.

### auxiliary instance

The Oracle instance associated with an auxiliary database, or the temporary instance used in tablespace point-in-time recovery (TSPITR) or a transportable tablespace operation.

### auxiliary set

In TSPITR, the set of files that is not in the recovery set but which must be restored in the auxiliary database for the TSPITR operation to be successful. In a transportable tablespace operation, the auxiliary set includes data files and other files required for the tablespace transport but which are not themselves part of the recovery set.

### backup

(1) A backup copy of data, that is, a database, tablespace, table, data file, control file, or archived redo log. Backups can be physical (at the database file level) or logical (at the database object level). Physical backups can be created by using RMAN to back up one or more data files, control files or archived redo log files. You can create logical backups with Data Pump Export.

(2) In an RMAN context, the output of the `BACKUP` command. The output format of a backup can be a backup set, proxy copy, or image copy. Logs archived by the database are considered copies rather than backups.

### backup and recovery

The set of concepts, procedures, and strategies involved in protecting the database against data loss due to media failure or users errors.

### backup-based duplication

A duplicate database that is created by restoring and recovering backups of the target database. This technique is an alternative to active database duplication.

### backup control file

A backup of the control file. You can back up the control file with the RMAN `backup` command or with the SQL statement `ALTER` `DATABASE` `BACKUP` `CONTROLFILE` `TO` `'` `filename` `'`.

### backup encryption

The encryption of backup sets by using an algorithm listed in `V$RMAN_ENCRYPTION_ALGORITHMS`. RMAN can transparently encrypt data written to backup sets and decrypt those backup sets when they are needed in a `RESTORE` operation. RMAN offers three modes of encryption: transparent, password protected, and dual mode.

### backup mode

The database mode (also called **hot backup mode**) initiated when you issue the `ALTER` `TABLESPACE` `...` `BEGIN` `BACKUP` or `ALTER` `DATABASE` `BEGIN` `BACKUP` command before taking an online backup. You take a tablespace out of backup mode when you issue the `ALTER` `TABLESPACE` `...` `END` `BACKUP` or `ALTER` `DATABASE` `END` `BACKUP` command.

When making a user-managed backup of data files in an online tablespace, you must place the tablespace in backup mode to protect against the possibility of a fractured block. In backup mode, updates to the database create more than the usual amount of redo. Each time a block in the buffer cache becomes dirty, the database must write an image of the changed block to the redo log file, in addition to recording the changes to the data. RMAN does not require you to put the database in backup mode.

See Also: corrupt block

### backup optimization

A configuration enabling RMAN to automatically skip backups of files that it has already backed up. You enable and disable backup optimization with the `CONFIGURE` command.

### backup piece

The physical file format used to store an RMAN backup set. Each logical backup set contains one or more physical backup pieces.

### backup retention policy

A user-defined policy for determining how long backups and archived logs must be retained for media recovery. You can define a retention policy in terms of backup redundancy or a recovery window. RMAN retains the data file backups required to satisfy the current retention policy, and any archived redo logs required for complete recovery of those data file backups.

### backup set

A backup of one or more data files, control files, server parameter files, and archived redo log files. Each backup set consists of one or more binary files. Each binary file is called a backup piece. Backup pieces are written in a proprietary format that can only be created or restored by RMAN.

Backup sets are produced by the RMAN `BACKUP` command. A backup set usually consists of only one backup piece. RMAN divides the contents of a backup set among multiple backup pieces only if you limit the backup piece size using the `MAXPIECESIZE` option of the `ALLOCATE CHANNEL` or `CONFIGURE CHANNEL` command.

See Also: unused block compression, multiplexing, RMAN

### backup undo optimization

The exclusion of undo not needed for recovery of an RMAN backup because the it describes and contains already-committed transactions. For example, a user updates the `salaries` table in the `USERS` tablespace. The change is written to the `USERS` tablespace, while the before image of the data is written to the `UNDO` tablespace. A subsequent RMAN backup of the `UNDO` tablespace may not include the undo for the salary change. Backup undo optimization is built-in RMAN behavior and cannot be disabled.

### backup window

A period of time during which a backup activity must complete.

### base recovery catalog

The entirety of the recovery catalog schema. The base recovery catalog is distinguished from a virtual private catalog, which is a subset of a recovery catalog.

### binary compression

A technique whereby RMAN applies a compression algorithm to data in backup sets.

### block change tracking

A database option that causes Oracle Database to track data file blocks affected by each database update. The tracking information is stored in a block change tracking file. When block change tracking is enabled, RMAN uses the record of changed blocks from the change tracking file to improve incremental backup performance by only reading those blocks known to have changed, instead of reading data files in their entirety.

### block change tracking file

A binary file used by RMAN to record changed blocks to improve incremental backup performance. You create and rename this file with the `ALTER DATABASE` statement.

### block media recovery

The recovery of specified blocks within a data file with the Recovery Manager `RECOVER ... BLOCK` command. Block media recovery leaves the affected data files online and restores and recovers only the damaged or corrupted blocks.

### breaking a mirror

The termination of a disk mirroring procedure so that a mirror image is no longer kept up-do-date.

### CDB

An Oracle Database installation that contains at least one PDB. A CDB also contains one root and one seed. Every Oracle Database is a CDB.

### CDB restore point

An alias for an SCN or a point in time in a multitenant container database (CDB). CDB restore points are accessible to all PDBs within the CDB.

### channel

An RMAN channel represents one stream of data to or from a backup device. A channel can either be a `DISK` channel (used to perform disk I/O) or an SBT channel (used to perform I/O through a third-party media management software). Each allocated channel starts a new Oracle Database session. The session then performs backup, restore, and recovery operations.

See Also: target database

### channel parallelism

Allocating multiple channels for RMAN operations.

### checkpoint

A data structure that defines an SCN in the redo thread of a database. Checkpoints are recorded in the control file and each data file header, and are a crucial element of recovery.

### checksum

A number calculated by the database from all the bytes stored in a data or redo block. If the `DB_BLOCK_CHECKSUM` initialization parameter is enabled, then the database calculates the checksum for every data file or online redo log block and stores it in the block header when writing to disk. The database can use the checksum value to check consistency.

### circular reuse records

Control file records containing information used by RMAN for backups and recovery operations. These records are arranged in a logical ring. When all available record slots are full, Oracle either expands the control file to make room for a new records or overwrites the oldest record. The `CONTROL_FILE_RECORD_KEEP_TIME` initialization parameter controls how many days records must be kept before they can be overwritten. The default for `CONTROL_FILE_RECORD_KEEP_TIME` is 7 days.

See Also: noncircular reuse records

### closed backup

A backup of one or more database files taken while the database is closed. Typically, closed backups are whole database backups. If you closed the database consistently, then all the files in the backup are consistent. Otherwise, the backups are inconsistent.

See Also: consistent shutdown, consistent backup

### cold backup

See closed backup

### command file

In an RMAN context, a client-side text file containing a sequence of RMAN commands. You can run command files with the `@` or `@@` commands from within RMAN or from the operating system prompt with the `@` or `CMDFILE` parameters.

### common user

In a multitenant container database (CDB), a database user that exists with the same identity in the root and in every existing and future PDB.

### complete recovery

Recovery of one or more data files that applies all redo generated after the restored backup. Typically, you perform complete media recovery when media failure damages one or more data files or control files. You fully recover the damaged files using all redo generated since the restored backup was taken.

See Also: incomplete recovery

### consistent backup

A whole database backup that you can open with the `RESETLOGS` option without performing media recovery. You do not need to apply redo to this backup to make it consistent. Unless you apply the redo generated since the consistent backup was created, however, you lose all transactions since the time of the consistent backup.

You can only take consistent backups after you have performed a consistent shutdown of the database. The database must not be re-opened until the backup has completed.

See Also: fuzzy file, inconsistent backup

### consistent shutdown

A database shut down with the `IMMEDIATE`, `TRASACTIONAL`, or `NORMAL` options of the statement. A database shut down cleanly does not require recovery; it is already in a consistent state.

### control file autobackup

The automatic backup of the current control file and server parameter file that RMAN makes after backups and, if the database is in `ARCHIVELOG` mode, after structural changes.

The control file autobackup has a default file name that allows RMAN to restore it even if the control file and recovery catalog are lost. You can override the default file name.

### convert script

A script generated by the `CONVERT DATABASE` command that you can use to convert data file formats on the destination host.

### copy

To back up a bit-for-bit image of an Oracle file (Oracle data files, control files, and archived redo logs) onto disk. You can copy in two ways:

- Using operating system utilities (for example, the UNIX `cp` or `dd`)
- Using the RMAN `BACKUP` `AS` `COPY` command

See Also: backup

### corrupt block

An Oracle block that is not in a recognized Oracle format, or whose contents are not internally consistent. Typically, corruptions are caused by faulty hardware or operating system problems. Oracle identifies corrupt blocks as either logically corrupt (an Oracle internal error) or media corrupt (the block format is not correct).

You can repair a media corrupt block with block media recovery, or dropping the database object that contains the corrupt block so that its blocks are reused for another object. If media corruption is due to faulty hardware, then neither solution works until the hardware fault is corrected.

### crash recovery

The automatic application of online redo records to a database after either a single-instance database crashes or all instances of an Oracle Real Applications Cluster configuration crash. Crash recovery only requires redo from the online logs; archived redo logs are not required.

See Also: recover

### cross-platform backup

A backup that is created on the source database and can be restored on the destination database that is running on a different platform than the source platform. Cross-platform backups are used to transport data across platforms.

Cross-platform operations can be performed either on the source database or destination database. However, they are often performed on the destination database because this is the usually the non-production database.

### crosscheck

A check to determine whether files on disk or in the media management catalog correspond to the data in the RMAN repository. Because the media management software can mark tapes as expired or unusable, and because files can be deleted from disk or otherwise become corrupted, the RMAN repository can contain outdated information about backups. Run the `CROSSCHECK` command to perform a crosscheck.

See Also: validation

### cumulative incremental backup

An incremental backup that backs up all the blocks changed since the most recent backup at level 0. When recovering with cumulative incremental backups, only the most recent cumulative incremental backup must be applied.

See Also: differential incremental backup, incremental backup

### current incarnation

The database incarnation in which the database is currently generating redo.

### current online redo log

The online redo log file in which the LGWR background process is currently logging redo records.

See Also: redo log, redo log group

### data integrity check

An invocation of a checker, which is a diagnostic procedure registered with the Health Monitor.

### data repair

The use of media recovery or Oracle Flashback Technology to recover lost or corrupted data.

### Data Recovery Advisor

An Oracle Database tool that automatically diagnoses persistent data failures, presents repair options to the user, and executes repairs at the user's request.

### database area

A location for the Oracle managed data files, control files, and online redo log files. The database area is specified by the `DB_CREATE_FILE_DEST` initialization parameter.

### database checkpoint

The thread checkpoint that has the lowest SCN. All changes in all enabled redo threads with SCNs before the database checkpoint SCN are guaranteed to have been written to disk.

See Also: checkpoint, data file checkpoint

### database identifier

See DBID

### database point-in-time recovery (DBPITR)

The recovery of an entire database to a specified past target time, SCN, or log sequence number.

See Also: incomplete recovery, tablespace point-in-time recovery (TSPITR)

### database registration

See registration

### data file checkpoint

A data structure that defines an SCN in the redo thread of a database for a particular data file. Every data file has a checkpoint SCN, which you can view in `V$DATAFILE.CHECKPOINT_CHANGE#`. All changes with an SCN lower than this SCN are guaranteed to be in the data file.

### data file media recovery

The application of redo records to a restored data file to roll it forward to a more current time. Unless you are doing block media recovery, the data file must be offline while being recovered.

### DBID

An internal, uniquely generated number that differentiates databases. Oracle creates this number automatically when you create the database.

### destination database

The database into which data from the source database is being transported.

### destination host

The computer on which a duplicate database resides.

### destination platform

When transporting data across platforms, the platform on which the destination database is running.

### differential incremental backup

A type of incremental backup that backs up all blocks that have changed since the most recent backup at level 1 or level 0. For example, in a differential level 1 backup RMAN determines which level 1 or level 0 incremental backup is most recent and then backs up all blocks changed since that backup. Differential backups are the default type of incremental backup. When recovering using differential incremental backups, RMAN must apply all differential incremental level 1 backups since the restored data file backup.

See Also: cumulative incremental backup, incremental backup

### direct ancestral path

When multiple `OPEN RESETLOGS` operations have been performed, the incarnation path that includes the parent incarnation of the current database incarnation and each ancestor incarnation of the current incarnation.

### disaster recovery

A strategic response to the loss of all data associated with a database installation. For example, a fire may destroy a server in a data center, forcing you to reinstall Oracle Database on a new server and recover the lost database from backups.

### disk controller

A hardware component that is responsible for controlling one or more disk drives.

### disk group

A collection of disks that are managed as a unit by Automatic Storage Management (ASM). The components of a disk group include disks, files, and allocation units.

### disk quota

A user-specified limit to the size of the fast recovery area. When the disk quota is reached, Oracle automatically deletes files that are no longer needed.

### duplexed backup set

In RMAN, a duplexed backup set is an RMAN-generated identical copy of a backup set. Each backup piece is in the original backup set is copied, with each copy getting a unique copy number (for example, `0tcm8u2s_1_1` and `0tcm8u2s_1_2`).

### duplicate database

A database created from target database backups using the RMAN duplicate command.

See Also: auxiliary database

### expired backup

A backup whose status in the RMAN repository is `EXPIRED`, which means that the backup was not found. RMAN marks backups and copies as expired when you run a `CROSSCHECK` command and the files are absent or inaccessible.

### export

The extraction of logical data (that is, not physical files) from a database into a binary file using Data Pump Export. You can then use Data Pump Import to import the data into a database.

See Also: logical backup

### export dump file

A file created by the Data Pump Export utility. The dump file set is made up of one or more disk files that contain table data, database object metadata, and control information. The files are written in a proprietary, binary format.

### failure

For Data Recovery Advisor, a failure is a persistent data corruption that has been diagnosed by the database. A failure can manifest itself as observable symptoms such as error messages and alerts, but a failure is different from a symptom because it represents a diagnosed problem. Failures are recorded in a repository for diagnostic data located outside of the database.

For each failure, Data Recovery Advisor generates a problem statement that unambiguously describes it. Examples of failures include inaccessible data files and corrupted undo segments. Data Recovery Advisor maps every failure to a repair option or set of repair options.

### failure priority

The priority of a failure diagnosed by Data Recovery Advisor. Every failure that is not closed has `CRITICAL`, `HIGH`, or `LOW` status. You can manually change the status of `HIGH` and `LOW` failures with the `CHANGE` command.

### failure status

The status of a failure diagnosed by Data Recovery Advisor. Every failure has `OPEN` or `CLOSED` status.

### fast recovery area

An optional disk location that you can use to store recovery-related files such as control file and online redo log copies, archived redo log files, flashback logs, and RMAN backups. Oracle Database and RMAN manage the files in the fast recovery area automatically. You can specify the disk quota, which is the maximum size of the fast recovery area. Formerly referred to as flash recovery area.

### file section

A contiguous range of blocks in a data file. A multisection backup processes a large file in parallel by copying each section to a separate backup piece.

### flashback data archive

A historical repository of transactional changes to every record in a table for the duration of the record's lifetime. A flashback data archive enables you to use some logical flashback features to transparently access historical data from far in the past.

### flashback database window

The range of SCNs for which there is currently enough flashback log data to support the `FLASHBACK` `DATABASE` command. The flashback database window cannot extend further back than the earliest SCN in the available flashback logs.

### flashback logs

Oracle-generated logs used to perform flashback database operations. The database can only write flashback logs to the fast recovery area. Flashback logs are written sequentially and are not archived. They cannot be backed up to disk.

### flashback retention target

A user-specified time or SCN that specifies how far into the past you want to be able to perform a flashback of the database.

### foreign archived redo log

An archived redo log received by a logical standby database for a LogMiner session. Unlike normal archived logs, foreign archived logs have a different DBID. For this reason, they cannot be backed up or restored on a logical standby database.

### foreign data file

A data file that does not belong to the target database, but is being plugged into the target database during a tablespace transport operation.

### foreign data file copy

A data file that was created when a cross-platform backup is restored in the destination database. It cannot be directly plugged in to the destination database because it is inconsistent.

### foreign tablespace

A set of foreign data file s that comprise a tablespace in the source database. These foreign data files do not belong to the target database, but are being transported into the target database from the source database.

### fractured block

A block in which the header and footer are not consistent at a given SCN. In a user-managed backup, an operating system utility can back up a data file at the same time that DBWR is updating the file. It is possible for the operating system utility to read a block in a half-updated state, so that the block that is copied to the backup media is updated in its first half, while the second half contains older data. In this case, the block is fractured.

For non-RMAN backups, the `ALTER TABLESPACE ... BEGIN BACKUP` or `ALTER DATABASE BEGIN BACKUP` command is the solution for the fractured block problem. When a tablespace is in backup mode, and a change is made to a data block, the database logs a copy of the entire block image before the change so that the database can reconstruct this block if media recovery finds that this block was fractured.

### full backup

A non-incremental RMAN backup. The word "full" does not refer to how much of the database is backed up, but to the fact that the backup is not incremental. Consequently, you can make a full backup of one data file.

### full resynchronization

An RMAN operation that updates the recovery catalog with all changed metadata in the database's control file. You can initiate a full catalog resynchronization by issuing the RMAN command `RESYNC` `CATALOG`. (It is rarely necessary to use `RESYNC` `CATALOG` because RMAN automatically performs resynchronizations when needed.)

### fuzzy file

A data file that contains at least one block with an SCN greater than or equal to the checkpoint SCN in the data file header. Fuzzy files are possible because database writer does not update the SCN in the file header with each file block write. For example, this situation occurs when Oracle updates a data file that is in backup mode. A fuzzy file that is restored always requires media recovery.

### guaranteed restore point

A restore point for which the database is guaranteed to retain the flashback logs for an Oracle Flashback Database operation. Unlike a normal restore point, a guaranteed restore point does not age out of the control file and must be explicitly dropped. Guaranteed restore points use space in the fast recovery area, which must be defined.

### hot backup

See online backup

### hot backup mode

See backup mode

### image copy

A bit-for-bit copy of a single data file, archived redo log file, or control file that is:

- Usable as-is to perform recovery (unlike a backup set, which uses unused block compression and is in an RMAN-specific format)
- Generated with the RMAN `BACKUP` `AS` `COPY` command, an operating system command such as the UNIX `cp`, or by the Oracle archiver process

### incarnation

A separate version of a database. The incarnation of the database changes when you open it with the `RESETLOGS` option, but you can recover backups from a prior incarnation so long as the necessary redo is available.

### incomplete recovery

A synonym for database point-in-time recovery (DBPITR).

See Also: complete recovery, media recovery, recover

### inconsistent backup

A backup in which some files in the backup contain changes that were made after the files were checkpointed. This type of backup needs recovery before it can be made consistent. Inconsistent backups are usually created by taking online database backups. You can also make an inconsistent backup by backing up data files while a database is closed, either:

- Immediately after the crash of an Oracle instance (or, in an Oracle RAC configuration, all instances)
- After shutting down the database using `SHUTDOWN` `ABORT`

Inconsistent backups are only useful if the database is in `ARCHIVELOG` mode and all archived redo logs created since the backup are available.

See Also: consistent backup, online backup, system change number (SCN), whole database backup

### incremental backup

An RMAN backup in which only modified blocks are backed up. Incremental backups are classified by **level**. A level 0 incremental backup performs the same function as a full backup in that they both back up all blocks that have ever been used. The difference is that a full backup does not affect blocks backed up by subsequent incremental backups, whereas an incremental backup affects blocks backed up by subsequent incremental backups.

Incremental backups at level 1 back up only blocks that have changed since previous incremental backups. Blocks that have not changed are not backed up. An incremental backup can be either a differential incremental backup or a cumulative incremental backup.

### incremental forever

After a full backup, only incremental backups are stored. This allows for faster recovery because the current image copy of the database is readily available.

### incrementally updated backup

An RMAN data file copy that is updated by an incremental backup. An effective backup strategy is to copy a data file, make an incremental backup, and then merge the incremental backup into the image copy. This strategy reduces the time required for media recovery because the image copy is updated with the latest data block changes.

### instance failure

The termination of an Oracle instance due to a hardware failure, Oracle internal error, or `SHUTDOWN` `ABORT` statement. Crash or instance recovery is always required after an instance failure.

### instance recovery

In an Oracle RAC configuration, the application of redo data to an open database by an instance when this instance discovers that another instance has crashed.

See Also: recover

### interblock corruption

A type of block corruption in which the corruption occurs between blocks rather than within the block itself. This type of corruption can only be logical corruption.

### intrablock corruption

A type of block corruption in which the corruption occurs within the block itself. This type of corruption can be either a physical corruption or logical corruption.

### level 0 incremental backup

An RMAN incremental backup that backs up all data blocks in the data files being backed up. An incremental backup at level 0 is identical in content to a full backup, but unlike a full backup the level 0 backup is considered a part of the incremental backup strategy.

### level of multiplexing

The number of input files simultaneously read and then written into the same RMAN backup piece.

### local user

In a multitenant container database (CDB), any user that is not a common user. A local user exists in exactly one PDB.

### LogMiner

A utility that enables log files to be read, analyzed, and interpreted by SQL statements.

See Also: archived redo log

### log sequence number

A number that uniquely identifies a set of redo records in a redo log file. When Oracle fills one online redo log file and switches to a different one, Oracle automatically assigns the new file a log sequence number.

See Also: log switch, redo log

### log switch

The point at which LGWR stops writing to the active redo log file and switches to the next available redo log file. LGWR switches when either the active log file is filled with redo records or you force a switch manually.

See Also: redo log

### logical backup

A backup of database schema objects, such as tables. Logical backups are created and restored with the Oracle Data Pump Export utility. You can restore objects from logical backups using the Data Pump Import utility.

### logical corruption

A type of corruption in which the block has a valid checksum, the header and footer match, and so on, but the contents are logically inconsistent.

### logical flashback features

The set of Oracle Flashback Technology features other than Oracle Flashback Database. The logical features enable you to view or rewind individual database objects or transactions to a past time.

### long-term backup

A backup that you want to exclude from a backup retention policy, but want to record in the recovery catalog. Typically, long-term backups are snapshots of the database that you may want to use in the future for report generation.

### lost write

A write to persistent storage that the database believes has occurred based on information from the I/O subsystem, when in fact the write has not occurred.

### mean time to recover (MTTR)

The time required to perform recovery.

### media failure

Damage to the disks containing any of the files used by Oracle, such as the data files, archived redo log files, or control file. When Oracle detects media failure, it takes the affected files offline.

See Also: media recovery

### media management catalog

A catalog of records maintained by a media management software. This catalog is completely independent from the RMAN recovery catalog. The Oracle Secure Backup catalog is an example of a media management catalog.

### media management library

A software library that RMAN can use to back up to tertiary storage. An SBT interface conforms to a published API and is supplied by a media management vendor. Oracle Secure Backup includes an SBT interface for use with RMAN.

### media management software

An Oracle or third-party software library that integrates with Recovery Manager so that database backups can be written directly to SBT devices.

### media manager multiplexing

Multiplexing in which the media management software rather than RMAN manages the mixing of blocks during an RMAN backup. One type of media manager multiplexing occurs when the media manager writes the concurrent output from multiple RMAN channels to a single sequential device. Another type occurs when a backup mixes database files and non-database files on the same tape.

### media recovery

The application of redo or incremental backups to a restored backup data file or individual data block.

When performing media recovery, you can recover a database, tablespace, data file, or set of blocks within a data file. Media recovery can be either complete recovery (in which all changes in the redo logs are applied) or incomplete recovery (in which only changes up to a specified point in time are applied). Media recovery is only possible when the database is in `ARCHIVELOG` mode.

See Also: block media recovery, recover

### mirroring

Maintaining identical copies of data on one or more disks. Typically, mirroring is performed on duplicate hard disks at the operating system level, so that if one disk is unavailable, the other disk can continue to service requests without interruptions. When mirroring files, Oracle Database writes once while the operating system writes to multiple disks. When multiplexing files, Oracle Database writes the same data to multiple files.

### MTTR

See mean time to recover (MTTR)

### multiplexed backup set

A backup set that contains blocks from multiple input files. For example, you could multiplex 10 data files into one backup set. Only whole files, never partial files, are included in a backup set.

### multiplexing

The meaning of the term depends on which files are multiplexed.

- Online redo logs: The automated maintenance of multiple identical copies of the online redo log.
- Control file: The automated maintenance of multiple identical copies of a database control file.
- Backup set: The RMAN technique of reading database files simultaneously from the disks and then writing the blocks to the same backup piece.
- Archived redo logs: The Oracle archiver process can archive multiple copies of a redo log.

See Also: mirroring

### multisection backup

An RMAN backup set in which each backup piece contains a file section, which is a contiguous range of blocks in a data file. A multisection backup set contains multiple backup pieces, but a backup set never contains only a part of a data file.

You create a multisection backup by specifying the `SECTION SIZE` parameter on the `BACKUP` command. An RMAN channel can process each file section independently, either serially or in parallel. Thus, in a multisection backup, multiple channels can back up a single file.

### multitenant architecture

The architecture that enables an Oracle database to function as a multitenant container database (CDB).

### multitenant container database (CDB)

See CDB

### native transfer rate

In a tape drive, the speed of writing to a tape without compression. This speed represents the upper limit of the backup rate.

### NOARCHIVELOG mode

The mode of the database in which Oracle does not require filled online redo logs to be archived before they can be overwritten. Specify the mode at database creation or change it with the `ALTER` `DATABASE` `NOARCHIVELOG` command.

If you run in `NOARCHIVELOG` mode, it severely limits the possibilities for recovery of lost or damaged data.

See Also: archived redo log, ARCHIVELOG mode

### noncircular reuse records

Control file records containing critical information needed by the Oracle database. These records are never automatically overwritten. Some examples of information in noncircular reuse records include the locations of data files and online redo logs.

See Also: circular reuse records

### normal restore point

A label for an SCN or time. For commands that support an SCN or time, you can often specify a restore point. Normal restore points exist in the circular list and can be overwritten in the control file. However, if the restore point pertains to an archival backup, then it is preserved in the recovery catalog.

### obsolete backup

A backup that is not needed to satisfy the current backup retention policy. For example, if your retention policy dictates that you must maintain one backup of each data file, but you have two backups of data file `1`, then the second backup of data file `1` is considered obsolete.

### offline normal

A tablespace is offline normal when taken offline with the `ALTER` `TABLESPACE` `...` `OFFLINE` `NORMAL` statement. The data files in the tablespace are checkpointed and do not require recovery before being brought online. If a tablespace is not taken offline normal, then its data files must be recovered before being brought online.

### offsite backup

An SBT backup that requires retrieval by the media management software before RMAN can restore it. You can list offsite backups with `RESTORE ... PREVIEW`.

### online backup

A backup of one or more data files taken while a database is open and the data files are online.

### online redo log

The online redo log is a set of two or more files that record all changes made to the database. Whenever a change is made to the database, Oracle generates a redo record in the redo buffer. The LGWR process writes the contents of the redo buffer into the online redo log.

The current online redo log is the one being written to by LGWR. When LGWR gets to the end of the file, it performs a log switch and begins writing to a new log file. If you run the database in `ARCHIVELOG` mode, then each filled online redo log file must be copied to one or more archiving locations before LGWR can overwrite them.

See Also: archived redo log

### online redo log group

The Oracle online redo log consists of two or more online redo log groups. Each group contains one or more identical online redo log members. An online redo log member is a physical file containing the redo records.

### online redo log member

A physical online redo log file within an online redo log group. Each log group must have one or more members. Each member of a group is identical.

### operating system backup

See user-managed backup

### operating system backup and recovery

See user-managed backup and recovery

### Oracle Enterprise Manager Cloud Control

The primary product for managing your database is Oracle Enterprise Manager Cloud Control (Cloud Control), a Web-based interface. After you have installed the Oracle Database software, created or upgraded a database, and configured the network, you can use Cloud Control to manage your database. Cloud Control also provides an interface for performance advisors and for Oracle utilities such as SQL\*Loader and Recovery Manager (RMAN).

### Oracle Flashback Database

The return of the whole database to a prior consistent SCN by the `FLASHBACK DATABASE` command in RMAN or SQL. A database flashback is different from traditional media recovery because it does not involve the restore of physical files, instead restoring your current data files to past states using saved images of changed data blocks. This feature uses flashback logs and archived redo logs.

### Oracle Flashback Technology

A set of Oracle Database features that provide an additional layer of data protection. These features include Oracle Flashback Query, Oracle Flashback Version Query, Oracle Flashback Transaction Query, Oracle Flashback Transaction, Oracle Flashback Table, Oracle Flashback Drop, and Oracle Flashback Database.

You can use flashback features to view past states of data and rewind parts or all of your database. In general, flashback features are more efficient and less disruptive than media recovery in most situations in which they apply.

### Oracle managed file

A database file managed by the Oracle Managed Files feature.

### Oracle Managed Files (OMF)

A service that automates naming, location, creation, and deletion of database files such as control files, redo log files, data files and others, based on a few initialization parameters. You can use Oracle managed files on top of a traditional file system supported by the host operating system, for example, VxFS or ODM. It can simplify many aspects of the database administration by eliminating the need to devise your own policies for such details.

### Oracle Secure Backup

An Oracle media manager that supplies reliable data protection through file system backup to tape. The Oracle Secure Backup SBT interface also enables you to use RMAN to back up Oracle databases. All major tape drives and tape libraries in SAN, Gigabit Ethernet, and SCSI environments are supported.

### Oracle-suggested backup strategy

A backup strategy available through a wizard in Oracle Enterprise Manager. The strategy involves periodically applying a level 1 incremental backup to a level 0 backup to create an incremental forever. If run daily, this strategy provides 24 hour point-in-time recovery from disk.

### Oracle VSS writer

A service on Windows systems that acts as coordinator between an Oracle Database instance and other Volume Shadow Copy Service (VSS) components, enabling data providers to create a shadow copy of files managed by the Oracle instance. For example, the Oracle VSS writer can place data files in hot backup mode to provide a recoverable copy of these data files in a shadow copy set.

### orphaned backups

Backups that were not made in the direct ancestral path of the current incarnation of the database. Orphaned backups cannot be used in the current incarnation.

### parallel recovery

A form of recovery in which several processes simultaneously apply changes from redo log files. The `RECOVERY_PARALLELISM` initialization parameter determines the level of parallelism for instance and crash recovery. You can use the `PARALLEL` and `NOPARALLEL` options of the `RECOVER` command to control parallelism for media recovery.Oracle Database automatically chooses the optimum degree of recovery parallelism. Usually, manually setting the level of parallelism for instance, crash, or media recovery is not recommended or necessary.

### parent incarnation

The database incarnation from which the current incarnation branched following an `OPEN RESETLOGS` operation.

### partial resynchronization

A type of resynchronization in which RMAN transfers data about archived logs, backup sets, and data file copies from the target control file to the recovery catalog.

### password file

A file created by the `ORAPWD` command, and required if you want to connect using the `SYSDBA` or `SYSBACKUP` privilege over a network. For details on password files, see the [Oracle Database Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=ADMIN10241).

### PDB

In a multitenant container database (CDB), a portable collection of schemas, schema objects, and nonschema objects that appears to an application as a separate database.

### PDB restore point

An alias for an SCN or a point in time in a particular pluggable database (PDB). A PDB restore point is applicable only to the PDB in which it is defined and cannot be used to perform operations either on other PDBs or the CDB.

### physical backup

A backup of physical files. A physical backup contrasts with a logical backup such as a table export.

### physical corruption

A type of corruption in which the database does not recognize a corrupt block. The database may not recognize the block because the checksum is invalid, the block contains all zeros, or the header and footer of the block do not match.

### physical schema

The data files, control files, and redo logs in a database at a given time. Issue the RMAN `REPORT` `SCHEMA` command to obtain a list of tablespaces and data files.

### physical standby database

A copy of a production database that you can use for disaster protection.

### pluggable database (PDB)

See PDB

### point-in-time recovery

The incomplete recovery of database files to a noncurrent time. Point-in-time recovery is also known as incomplete recovery.

See Also: media recovery, recover

### problem

A critical error in the database that is recorded in the Automatic Diagnostic Repository (ADR). Critical errors include internal errors and other severe errors. Each problem has a problem key, which is a set of attributes that describe the problem. The problem key includes the ORA error number, error parameter values, and other information.

### proxy copy

A backup in which the media management software manages the transfer of data between the media storage device and disk during RMAN backup and restore operations.

### raw device

A disk or partition without a file system. Thus, you cannot use `ls`, Windows Explorer, and so on to view their contents. The raw partition appears to Oracle Database as a single file.

### recover

To recover a database file or a database is typically to perform media recovery, crash recovery, or instance recovery. This term can also be used generically to refer to reconstructing or re-creating lost data by any means.

See Also: complete recovery, incomplete recovery

### recovery

When used to refer to a database file or a database, the application of redo data or incremental backups to database files to reconstruct lost changes. The three types of recovery are instance recovery, crash recovery, and media recovery. Oracle Database performs the first two types of recovery automatically using online redo records; only media recovery requires you to restore a backup and issue commands.

See Also: complete recovery, incomplete recovery

### recovery catalog

A set of Oracle tables and views used by RMAN to store RMAN repository information about one or more Oracle databases. RMAN uses this metadata to manage the backup, restore, and recovery of Oracle databases.

Use of a recovery catalog is optional although it is highly recommended. For example, starting with Oracle Database 11g, a single recovery catalog schema can keep track of database file names for all databases in a Data Guard environment. This catalog schema also keeps track of where the online redo logs, standby redo logs, temp files, archived redo logs, backup sets, and image copies are created for all databases.

The primary storage for RMAN repository information for a database is always in the control file of the database. A recovery catalog is periodically updated with RMAN repository data from the control file. For the loss of a control file, the recovery catalog can provide most or all of the lost metadata required for restore and recovery of the database. The recovery catalog can also store records of archival backups and RMAN stored scripts for use with target databases.

See Also: recovery catalog database

### recovery catalog database

An Oracle Database that contains a recovery catalog schema.

### recovery catalog schema

The recovery catalog database schema that contains the recovery catalog tables and views.

### Recovery Manager (RMAN)

The primary utility for physical backup and recovery of Oracle databases. RMAN keeps records of Oracle databases in its own structure called an RMAN repository, manages storage of backups, validates backups. You can use it with or without the central information repository called a recovery catalog. If you do not use a recovery catalog, then RMAN uses the database's control file to store information necessary for backup and recovery operations. You can use RMAN with third-party media management software to back up files to tertiary storage.

See Also: backup piece, backup set, copy, media management software, recovery catalog

### recovery set

One or more tablespaces that are being recovered to an earlier point in time during tablespace point-in-time recovery (TSPITR). After TSPITR, all database objects in the recovery set have been recovered to the same point in time.

See Also: auxiliary set

### recovery window

A recovery window is one type of RMAN backup retention policy, in which the DBA specifies a period of time and RMAN ensures retention of backups and archived redo logs required for point-in-time recovery to any time during the recovery window. The interval always ends with the current time and extends back in time for the number of days specified by the user.

For example, if the retention policy is set for a recovery window of seven days, and the current time is 11:00 AM on Tuesday, RMAN retains the backups required to allow point-in-time recovery back to 11:00 AM on the previous Tuesday.

### recycle bin

A data dictionary table containing information about dropped objects. Dropped tables and any associated objects such as indexes, constraints, nested tables, and so on are not removed and still occupy space. The Flashback Drop feature uses the recycle bin to retrieve dropped objects.

### redo log

A redo log can be either an online redo log or an archived redo log. The online redo log is a set of two or more redo log groups that records all changes made to Oracle data files and control files. An archived redo log is a copy of an online redo log that has been written to an offline destination.

### redo log group

Each online redo log member (which corresponds to an online redo log file) belongs to a redo log group. Redo log groups contain one or more members. A redo log group with multiple members is called a multiplexed redo log group. The contents of all members of a redo log group are identical.

### redo thread

The redo generated by an instance. If the database runs in a single instance configuration, then the database has only one thread of redo.

### redundancy

In a retention policy, the setting that determines many copies of each backed-up file to keep. A redundancy-based retention policy is contrasted with retention policy that uses a recovery window.

### redundancy set

A set of backups enabling you to recover from the failure or loss of any Oracle Database file.

### registration

In RMAN, the execution of a `REGISTER` `DATABASE` command to record the existence of a target database in the recovery catalog. A target database is uniquely identified in the catalog by its DBID. You can register multiple databases in the same catalog, and also register the same database in multiple catalogs.

### repair

For Data Recovery Advisor, a repair is an action or set of actions that fixes one or more failure s. Examples repairs include block media recovery, data file media recovery, Oracle Flashback Database, and so on.

### repair option

For Data Recovery Advisor, one possible technique for repairing a failure. Different repair options are intended to fix the same problem, but represent different advantages and disadvantages in terms of repair time and data loss.

### RESETLOGS

A technique for opening a database that archives any current online redo logs (if using `ARCHIVELOG` mode), resets the log sequence number to 1, and clears the online redo logs. An `ALTER DATABASE OPEN RESETLOGS` statement begins a new database incarnation. The starting SCN for the new incarnation, sometimes called the `RESETLOGS` SCN, is the incomplete recovery SCN of the media recovery preceding the `OPEN RESETLOGS`, plus one.

An `ALTER DATABASE OPEN RESETLOGS` statement is required after incomplete recovery or recovery with a backup control file. An `OPEN` `RESETLOGS` operation does not affect the recoverability of the database. Backups from before the `OPEN` `RESETLOGS` operation remain valid and can be used along with backups taken after the `OPEN` `RESETLOGS` operation to repair any damage to the database.

### resilver a split mirror

The process of making the contents of a split mirror identical with the contents of the storage devices from which the mirror was split. The operating system or the hardware managing the mirror refreshes a broken mirror from the half that is up-to-date and then maintains both sides of the mirror.

### restartable backup

The feature that enables RMAN to back up only those files that have not been backed up since a specified date. The unit of restartability is last completed backup set or image copy. You can use this feature after a backup fails to back up the parts of the database missed by the failed backup.

### restore

The replacement of a lost or damaged file with a backup. You can restore files either with commands such as UNIX `cp` or the RMAN `RESTORE` command.

### restore failover

The automatic search by RMAN for usable backups in a restore operation if a corrupted or inaccessible backup is found.

### restore optimization

The default behavior in which RMAN avoids restoring data files from backup when possible.

### restore point

A user-defined a name associated with an SCN of the database corresponding to the time of the creation of the restore point. A restore point can be a guaranteed restore point or a normal restore point.

### resynchronization

The operation that updates the recovery catalog with current metadata from the target database control file. You can initiate a full resynchronization of the catalog by issuing a `RESYNC` `CATALOG` command. A partial resynchronization transfers information to the recovery catalog about archived redo log files, backup sets, and data file copies. RMAN resynchronizes the recovery catalog automatically when needed.

### retention policy

See backup retention policy

### reverse resynchronization

In a Data Guard environment, the updating of a primary or standby database control file with metadata obtained from the recovery catalog. For example, if you configure persistent RMAN settings for a standby database that is not the connected target database, then RMAN performs a reverse resynchronization the next time RMAN connects as target to the standby database. In this way, the recovery catalog keeps the metadata in the control files in a Data Guard environment up to date.

### RMAN

See Recovery Manager (RMAN)

### RMAN backup job

The set of `BACKUP` commands executed within a single RMAN session. For example, assume that you start the RMAN client, execute `BACKUP DATABASE`, `BACKUP ARCHIVELOG`, and `RECOVER COPY`, and then exit the RMAN client. The RMAN backup job consists of the database backup and the archived redo log backup.

### RMAN client

An Oracle Database executable that interprets commands, directs server sessions to execute those commands, and records its activity in the target database control file. The RMAN executable is automatically installed with the database and is typically located in the same directory as the other database executables. For example, the RMAN client on Linux is named `rman` and is located in `$ORACLE_HOME/bin`.

### RMAN job

The set of RMAN commands executed in an RMAN session. For example, assume that you start the RMAN client, execute `BACKUP DATABASE`, `BACKUP ARCHIVELOG`, and `RECOVER COPY`, and then exit the RMAN client. The RMAN job consists of the two backups and the roll forward of the data file copy.

### RMAN maintenance commands

Commands that you can use to manage RMAN metadata records and backups. The maintenance commands are `CATALOG`, `CHANGE`, `CROSSCHECK`, and `DELETE`.

### RMAN repository

The record of RMAN metadata about backup and recovery operations on the target database. The authoritative copy of the RMAN repository is always stored in the control file of the target database. A recovery catalog can also be used for longer-term storage of the RMAN repository, and can serve as an alternate source of RMAN repository data if the control file of your database is lost.

See Also: recovery catalog database, resynchronization

### RMAN session

An RMAN session begins when the RMAN client is started and ends when you exit from the client or the RMAN process is terminated. Multiple RMAN commands can be executed in a single RMAN session.

### rollback segments

Database segments that record the before-images of changes to the database.

### rolling back

The use of rollback segments to undo uncommitted changes applied to the database during the rolling forward stage of recovery.

### rolling forward

The application of redo records or incremental backups to data files and control files to recover changes to those files.

See Also: rolling back

### root

In a multitenant container database (CDB), a system-supplied set of schemas, schema objects, and non-schema objects that functions as the parent for PDB s. Every CDB has only one root and all PDBs belong to the root.

### RUN block

A series of RMAN commands that are executed sequentially.

### SBT

System Backup to Tape. This term specifies a nondisk backup device type, typically a tape library or tape drive. RMAN supports channels of type disk and SBT.

### shadow copy

In the Volume Shadow Copy Service (VSS) infrastructure on Windows, a consistent snapshot of a component or volume.

### snapshot control file

A copy of a database control file created in an operating system-specific location by Recovery Manager. RMAN creates the snapshot control file so that it has a consistent version of a control file to use when either resynchronizing the recovery catalog or backing up the control file.

### source database

The database that you are copying when you create a duplicate database. When transporting data to another platform, the source database is the database that contains the data that is to be transported.

### source host

The host on which a source database resides.

### source platform

When transporting data, the platform on which the source database is running. The source database contains the data to be transported to a destination database running on a different platform.

### sparse backup

An RMAN backup that backs up one or more sparse data files. For each sparse data file, a full backup of the shadow file (not the base file) is created.

### sparse database

A database that contains one or more sparse data files.

### sparse data file

A logical Oracle object that is created as the shadow of a base data file. The base data file is read-only. The sparse data file is read-write and contains the updates made to the base data file.

### split mirror backup

A backup of database files that were previously mirrored. Some third-party tools enable you to use mirroring a set of disks or logical devices, that is, maintain an exact duplicate of the primary data in another location. Splitting a mirror involves separating the file copies so that you can use them independently. With the `ALTER SYSTEM SUSPEND/RESUME` database feature, you can suspend I/O to the database, split the mirror, and make a backup of the split mirror.

### stored script

A sequence of RMAN commands stored in the recovery catalog. Stored scripts can be global or local. Global scripts can be shared by all databases registered in the recovery catalog.

### synchronous I/O

A server process can perform only one task at a time while RMAN is either reading or writing data.

### system change number (SCN)

A stamp that defines a committed version of a database at a point in time. Oracle assigns every committed transaction a unique SCN.

### tablespace destination

In a transportable tablespace operation, the location on disk which (by default) contains the data file copies and other output files when the tablespace transport command completes.

### tablespace point-in-time recovery (TSPITR)

The recovery of one or more non- `SYSTEM` tablespaces to a noncurrent time. You use RMAN to perform TSPITR.

### tag

Identifier for an RMAN backup. If you generate a backup set, then the tag is assigned to each backup piece rather than to the backup set. If you do not specify a tag for a backup, then RMAN assigns one automatically.

### target database

In an RMAN environment, the database to which you are connected as `TARGET`. The target database is the database on which you are performing RMAN operations.

### target host

The computer on which a target database resides.

### target instance

In an RMAN environment, the instance associated with a target database.

### temp file

A file that belongs to a temporary tablespace and is created with the `TEMPFILE` option. Temporary tablespaces cannot contain permanent database objects such as tables, and are typically used for sorting. Because temp files cannot contain permanent objects, RMAN does not back them up. RMAN does keep track of the locations of temp files in the control file, however, and during recovery re-creates the temp files as needed at those locations.

### transport script

A script generated by the `CONVERT DATABASE` command. This script contains SQL statements used to create the new database on the destination platform.

### transportable tablespace

A feature that transports a set of tablespaces from one database to another, or from one database to itself. Transporting a tablespace into a database is like creating a tablespace with loaded data.

### transportable tablespace set

Data files for the set of tablespaces in a transportable tablespace operation, and an export file containing metadata for the set of tablespaces. You use Data Pump Export to perform the export of metadata.

### trial recovery

A simulated recovery initiated with the `RECOVER ... TEST` command in RMAN or SQL\*Plus. A trial recovery applies redo in a way similar to normal media recovery, but it never writes its changes to disk and it always rolls back its changes. Trial recovery occurs only in memory.

### undo retention period

The minimum amount of time that Oracle Database attempts to retain old undo data in the undo tablespace before overwriting it. Old (committed) undo data that is older than the current undo retention period is said to be expired. Old undo data with an age that is less than the current undo retention period is said to be unexpired.

### undo tablespace

A dedicated tablespace that stores only undo information when the database is run in automatic undo management mode.

### unused block compression

A feature by which RMAN reduces the size of data file backup sets by skipping data blocks. RMAN always skips blocks that have never been used. Under certain conditions, which are described in the `BACKUP AS BACKUPSET` entry in [Oracle Database Backup and Recovery Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=RCMRF107), RMAN also skips previously used blocks that are not currently being used.

### user-managed backup

A backups made using a non-RMAN method, for example, using an operating system utility. For example, you can make a user-managed backup by running the `cp` command on Linux or the `COPY` command on Windows. A user-managed backup is also called an operating system backup.

### user-managed backup and recovery

A backup and recovery strategy for an Oracle Database that does not use RMAN. This term is equivalent to operating system backup and recovery. You can back up and restore database files using operating system utilities (for example, the `cp` command in UNIX), and recover using the SQL\*Plus `RECOVER` command.

### validation

In an RMAN context, a test that checks database files for block corruption or checks a backup set to determine whether it can be restored. RMAN can check for both physical and logical block corruption.

### virtual private catalog

A subset of the metadata in a base recovery catalog to which a database user is granted access. The owner of a base recovery catalog can grant or revoke restricted access to the recovery catalog to other database users. Each restricted user has full read/write access to his own virtual private catalog.

### Volume Shadow Copy Service (VSS)

An infrastructure on Windows server platforms that enables requestors, writers, and providers to participate in the creation of a consistent snapshot called a shadow copy. The VSS service uses well-defined COM interfaces. See [Oracle Database Platform Guide for Microsoft Windows](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=NTQRF280) to learn how to use RMAN with VSS.

### whole database backup

A backup of the control file and all data files that belong to a database.

### Zero Data Loss Recovery Appliance (Recovery Appliance)

An enterprise-level, cloud-scale Engineered System, that provides a single, centralized repository for backups of all your Oracle Databases. You can use RMAN commands to backup your target databases to Recovery Appliance.