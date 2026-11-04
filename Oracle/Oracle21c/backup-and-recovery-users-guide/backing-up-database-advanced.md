---
title: "Backup and Recovery User's Guide"
book: "Database Backup and Recovery User's Guide"
doc_id: F31836-11
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/bradv/backing-up-database-advanced.html
tags:
  - oracle
  - 21c
  - backup-and-recovery-users-guide
---

Learn how to perform advanced RMAN backup procedures such as backup optimization, duplexing backup sets, and limiting the size of backups.

See Also:

[Backing Up the Database](backing-up-database.md) for basic backup procedures

### 10.1 Limiting the Size of RMAN Backup Sets

You can use the `CONFIGURE` command to create persistent settings that govern backup set size.

This control is helpful when backing up very large files. If you do not have a backup set size persistently configured, then you can also use the `BACKUP... MAXSETSIZE` command to limit the size of backup sets.

You can use the `CONFIGURE` command, but not the `BACKUP` command, to set a limit for the size of individual backup pieces. This control is especially useful when you use a media manager that has restrictions on the sizes of files, or when you must back up very large files.

#### 10.1.1 About Backup Set Size

The `MAXSETSIZE` parameter of the `BACKUP` command specifies a maximum size for a backup set in units of bytes (default), kilobytes, megabytes, or gigabytes.

For example, to limit a backup set to 305 MB, specify `MAXSETSIZE 305M`. RMAN attempts to limit all backup sets to this size.

You can use `BACKUP...MAXSETSIZE` to limit the size of backup sets so that the database is divided among multiple backup sets. If the backup fails part way through, then you can use the restartable backup feature to back up only those files that were not backed up during the previous attempt.

In some cases the `MAXSETSIZE` value may be too small to contain the largest file that you are backing up. When determining whether `MAXSETSIZE` is too small, RMAN uses the size of the original data file rather than the file size after compression. RMAN displays an error stack such as the following:

```
RMAN-00571: ===========================================================
RMAN-00569: =============== ERROR MESSAGE STACK FOLLOWS ===============
RMAN-00571: ===========================================================
RMAN-03002: failure of backup command at 11/03/13 14:40:33
RMAN-06182: archive log larger than MAXSETSIZE: thread 1 seq 1
            /oracle/oradata/trgt/arch/archive1_1.dbf
```

#### 10.1.2 Limiting the Size of Backup Sets with BACKUP... MAXSETSIZE

Backup piece size is an issue in those situations where it exceeds the maximum file size of the file system or media management software. Use the `MAXSETSIZE` parameter of the `CONFIGURE` `CHANNEL` or `ALLOCATE` `CHANNEL` command to limit the size of backup pieces.

To limit the size of backup sets:

1. Start RMAN and connect to a target database and recovery catalog (if used).
2. Execute the `BACKUP` command with the `MAXSETSIZE` parameter.
	The following example backs up archived logs to tape, limiting the size of each backup set to 100 MB:
	```
	BACKUP DEVICE TYPE sbt
	  MAXSETSIZE 100M
	  ARCHIVELOG ALL;
	```

#### 10.1.3 Dividing the Backup of a Large Data File into Sections

If you specify the `SECTION SIZE` parameter on the `BACKUP` command, then RMAN creates a backup set in which each backup piece contains the blocks from one file section.

A file section is a contiguous range of blocks in a file. This type of backup is called a multisection backup.

Note:

You cannot specify `SECTION SIZE` with `MAXPIECESIZE`.

The purpose of multisection backups is to enable RMAN channels to back up a single large file in parallel. RMAN divides the work among multiple channels, with each channel backing up one file section in a file. Backing up a file in separate sections can improve the performance of backups of large data files.

If a multisection backup completes successfully, then no backup set generated during the backup contains a partial data file. If a multisection backup is unsuccessful, then the RMAN metadata can contain a record for a partial backup set. RMAN does not consider partial backups for restore and recovery. You must use the `DELETE` command to delete the partial backup set.

If you specify a section size that is larger than the size of the file, then RMAN does not use multisection backup for the file. If you specify a small section size that would produce more than 256 sections, then RMAN increases the section size to a value that results in exactly 256 sections.

To make a multisection backup:

1. Start RMAN and connect to a target database and recovery catalog (if used).
2. If necessary, configure channel parallelism so that RMAN can make the backup parallel.
3. Execute `BACKUP` with the `SECTION SIZE` parameter.
	For example, suppose that the `users` tablespace contains a single data file of 900 MB. Also assume that three SBT channels are configured, with the parallelism setting for the SBT device set to 3. You can break up the data file in this tablespace into file sections as shown in the following example:
	```
	BACKUP
	  SECTION SIZE 300M
	  TABLESPACE users;
	```
	In this example, each of the three SBT channels backs up a 300 MB file section of the `users` data file.

### 10.2 Using Backup Optimization to Skip Files

You run the `CONFIGURE BACKUP OPTIMIZATION` command to enable backup optimization. When certain criteria are met, RMAN skips backups of files that are identical to files that are already backed up.

Example 10-1 Configuring Backup Optimization

This example shows an RMAN configuration that is used in the examples in this section on backup optimization. The commands configure backup optimization and a retention policy.

```
CONFIGURE DEFAULT DEVICE TYPE TO sbt;
CONFIGURE BACKUP OPTIMIZATION ON;
CONFIGURE RETENTION POLICY TO RECOVERY WINDOW OF 4 DAYS;
```

With this configuration, you run the following command every night to back up the database to tape:

```
BACKUP DATABASE;
```

Because backup optimization is configured, RMAN skips backups of offline and read-only data files only if the most recent backups were made on or after the earliest point in the recovery window. RMAN does not skip backups when the most recent backups are older than the window. For example, optimization ensures you do not end up with a new backup of a read-only data file every night, so long as one backup set containing this file exists within the recovery window.

#### 10.2.1 Optimizing a Daily Archived Log Backup to a Single Tape: Scenario

Assume that you want to back up all the archived logs every night, but you do not want to have multiple copies of each log sequence number. With RMAN configured as shown in Example 10-1, you run the following command in a script nightly at 1 a.m.:

```
BACKUP DEVICE TYPE sbt 
  ARCHIVELOG ALL;
```

RMAN skips all logs except those produced in the last 24 hours. In this way, you keep only one copy of each archived log on tape.

#### 10.2.2 Optimizing a Daily Archived Log Backup to Multiple Media Families: Scenario

In Oracle Secure Backup, a media family is a named group of volumes with a set of shared, user-defined attributes. In this scenario, you back up logs that are not on tape to one media family, then back up the same logs to a second media family. Finally, you delete old logs.

Example 10-2 Backing Up Archived Redo Logs to Multiple Media Families

With RMAN configured as shown in this example, run the following script at the same time every night to back up the logs generated during the previous day to two separate media families.

```
# The following command backs up just the logs that are not on tape. The 
# first copies are saved to the tapes from the media family "log_family1".
RUN
{
  ALLOCATE CHANNEL c1 DEVICE TYPE sbt
    PARMS 'ENV=(OB_MEDIA_FAMILY=log_family1)';
  BACKUP ARCHIVELOG ALL;
}
# Make one more copy of the archived logs and save them to tapes from a 
# different media family
RUN
{
  ALLOCATE CHANNEL c2 DEVICE TYPE sbt 
    PARMS 'ENV=(OB_MEDIA_FAMILY=log_family2)';
  BACKUP ARCHIVELOG
    NOT BACKED UP 2 TIMES;
}
```

After running the script in this example, you can delete unneeded logs by executing `DELETE ARCHIVELOG ALL`.

If your goal is to delete logs from disk that have been backed up two times to SBT, then the simplest way to achieve the goal is with an archived redo log deletion policy. The following one-time configuration specifies that archived redo logs are eligible for deletion from disk if two archived log backups exist on tape:

```
CONFIGURE ARCHIVELOG DELETION POLICY 
  TO BACKED UP 2 TIMES TO DEVICE TYPE sbt;
```

#### 10.2.3 Creating a Weekly Secondary Backup of Archived Logs: Example

Assume a more sophisticated scenario in which your goal is to back up the archived logs to tape every day. You are worried about tape failure, however, so you want to ensure that you have more than one copy of each log sequence number on a separate tape before you perform your weekly deletion of logs from disk. This scenario assumes that the database is not using a fast recovery area.

First, perform a one-time configuration as follows:

```
CONFIGURE BACKUP OPTIMIZATION ON;
CONFIGURE DEVICE TYPE sbt PARALLELISM 1;
CONFIGURE default DEVICE TYPE TO sbt;
CONFIGURE CHANNEL DEVICE TYPE sbt PARMS 'ENV=(OB_MEDIA_FAMILY=first_copy);
```

Because you have optimization enabled, you can run the following command every evening to back up all archived logs to the `first_copy` media family that have not already been backed up:

```
BACKUP ARCHIVELOG ALL TAG first_copy;
```

Every Friday evening you create an additional backup of all archived logs in a different media family. After the backup, you want to delete all archived logs that have at least two copies on tape. So you run the following script:

```
RUN
{
  # manually allocate a channel, to specify that the backup run by this
  # channel goes to both media families "first_copy" and "second_copy"
  ALLOCATE CHANNEL c1 DEVICE TYPE sbt
      PARMS 'ENV=(OB_MEDIA_FAMILY=second_copy)';
  ALLOCATE CHANNEL c2 DEVICE TYPE sbt
      PARMS 'ENV=(OB_MEDIA_FAMILY=first_copy)';
  BACKUP 
    CHANNEL c1 
    ARCHIVELOG 
    UNTIL TIME 'SYSDATE' 
    NOT BACKED UP 2 TIMES # back up only logs without 2 backups on tape
    TAG SECOND_COPY; 
  BACKUP 
    CHANNEL c2 
    ARCHIVELOG 
    UNTIL TIME 'SYSDATE' 
    NOT BACKED UP 2 TIMES # back up only logs without 2 backups on tape
    TAG FIRST_COPY;
}

# now delete from disk all logs that have been backed up to tape at least twice
DELETE 
  ARCHIVELOG ALL
  BACKED UP 2 TIMES TO DEVICE TYPE sbt;
```

The following table explains the effects of the daily and weekly backup scripts.

Table 10-1 Effects of Daily and Weekly Scripts

| Script | Tape Contents After Script | Disk Contents After Script |
| --- | --- | --- |
| Daily | Archived logs that have not yet been backed up are now in media family `first_copy`. | All archived logs created since the last `DELETE` command are still on disk. |
| Weekly | Archived logs that have fewer than two backups on tape are now in media families `first_copy` and `second_copy`. | All archived logs that have been backed up at least twice to tape are deleted. |

After the weekly backup, you can send the tape from the media family `second_copy` to offsite storage. Use this tape backup only if the primary tape from pool `first_copy` is damaged. Because the secondary tape is offsite, you do not want RMAN to use it for recovery, so you can mark the backup as unavailable:

```
CHANGE BACKUP OF ARCHIVELOG TAG SECOND_COPY UNAVAILABLE;
```

### 10.3 Skipping Offline, Read-Only, and Inaccessible Files

By default, the `BACKUP` command terminates when it cannot access a data file.

You can specify parameters to prevent termination, as listed in Table 10-2.

Table 10-2 BACKUP... SKIP Options

| If you specify... | Then RMAN skips... |
| --- | --- |
| `SKIP` `INACCESSIBLE` | Data files that RMAN cannot read. |
| `SKIP` `OFFLINE` | Offline data files. Some offline data files can still be read because they exist on disk. Others have been deleted or moved and so cannot be read, making them inaccessible. |
| `SKIP` `READONLY` | Data files in read-only tablespaces. |

The following example uses an automatic channel to back up the database, and skips all data files that might cause the backup job to terminate.

Example 10-3 Skipping Files During an RMAN Backup

```
BACKUP DATABASE
  SKIP INACCESSIBLE
  SKIP READONLY
  SKIP OFFLINE;
```

### 10.4 Duplexing Backup Sets

RMAN can make up to four copies of a backup set simultaneously, each an exact duplicate of the others.

A copy of a duplexed backup set is a copy of each backup piece in the backup set, with each copy getting a unique copy number (for example, `0tcm8u2s_1_1` and `0tcm8u2s_1_2`). It is not possible to duplex backup sets to the fast recovery area.

You can use `BACKUP...COPIES` or `CONFIGURE...BACKUP                 COPIES` to duplex backup sets. RMAN can duplex backups to either disk or tape, but cannot duplex backups to tape and disk simultaneously. For `DISK` channels, specify multiple values in the `FORMAT` option to direct the multiple copies to different physical disks. For SBT channels, if you use a media manager that supports Version 2 of the SBT API, then the media manager automatically writes each copy to a separate medium (for example, a separate tape). When backing up to tape, ensure that the number of copies does not exceed the number of available tape devices.

Duplexing applies only to backup sets, not image copies. It is an error to specify the `BACKUP... COPIES` when creating image copy backups, and the `CONFIGURE... BACKUP COPIES ` setting is ignored for image copy backups.

#### 10.4.1 Duplexing Backup Sets with CONFIGURE BACKUP COPIES

The `CONFIGURE...BACKUP COPIES` command specifies the number of identical backup sets to create on the specified device type.

To duplex a backup with CONFIGURE... BACKUP COPIES:

This setting applies to all backup sets except control file autobackups (because the autobackup of a control file always produces one copy) and backup sets when backed up with the `BACKUP BACKUPSET` command.

1. Configure the number of copies on the desired device type for data files and archived redo logs on the desired device types.
	By default, `CONFIGURE...BACKUP COPIES` is set to `1` for each device type. The following example configures duplexing for data files and archived logs on tape and also duplexing for data files (but not archived redo logs) on disk:
	```
	CONFIGURE DEVICE TYPE sbt PARALLELISM 1;
	CONFIGURE DEFAULT DEVICE TYPE TO sbt;
	CONFIGURE CHANNEL DEVICE TYPE DISK FORMAT '/disk1/%U', '/disk2/%U';
	CONFIGURE DATAFILE BACKUP COPIES FOR DEVICE TYPE sbt TO 2;
	CONFIGURE ARCHIVELOG BACKUP COPIES FOR DEVICE TYPE sbt TO 2;
	CONFIGURE DATAFILE BACKUP COPIES FOR DEVICE TYPE DISK TO 2;
	```
2. Execute the `BACKUP` command.
	The following command backs up the database and archived logs to tape, making two copies of each data file and archived log:
	```
	BACKUP AS BACKUPSET DATABASE PLUS ARCHIVELOG;
	```
	Because of the configured formats for the disk channel, the following command backs up the database to disk, placing one copy of the backup sets produced in the `/disk1` directory and the other in the `/disk2` directory:
	```
	BACKUP DEVICE TYPE DISK AS BACKUPSET DATABASE;
	```
	If the `FORMAT` clause were not configured on `CONFIGURE CHANNNEL`, then you specify `FORMAT` on the `BACKUP` command itself. For example, you issue the following command:
	```
	BACKUP AS BACKUPSET DATABASE 
	  FORMAT '/disk1/%U', 
	         '/disk2/%U';
	```
3. Issue a `LIST BACKUP` command to see a listing of backup sets and pieces.
	For example, enter the following command:
	```
	LIST BACKUP SUMMARY;
	```
	The `#Copies` column shows the number of backup sets, which may have been produced by duplexing or by multiple backup commands.

#### 10.4.2 Duplexing Backup Sets with BACKUP... COPIES

The `COPIES` option of the `BACKUP` command overrides every other `COPIES` or `DUPLEX` setting to control duplexing of backup sets.

To duplex a backup with BACKUP... COPIES:

1. Specify the number of identical copies with the `COPIES` option of the `BACKUP` command. For example, run the following to make three copies of each backup set in the default `DISK` location:
	```
	BACKUP AS BACKUPSET DEVICE TYPE DISK 
	  COPIES 3 
	  INCREMENTAL LEVEL 0 
	  DATABASE;
	```
	Because you specified `COPIES` in the `BACKUP` command, RMAN makes three backup sets of each data file regardless of the `CONFIGURE DATAFILE COPIES` setting.
2. Issue a `LIST BACKUP` command to see a listing of backup sets and pieces (the `#Copies` column shows the number of copies, which may have been produced through duplexing or through multiple invocations of the `BACKUP` command). For example, enter:
	```
	LIST BACKUP SUMMARY;
	```

### 10.5 Making Split Mirror Backups with RMAN

Many sites keep a backup of the database stored on disk in case a media failure occurs on the primary database or an incorrect user action requires point-in-time recovery. A data file backup on disk simplifies the restore step of recovery, making recovery much quicker and more reliable.

Caution:

Never make backups, split mirror or otherwise, of online redo logs. Restoring online redo log backups can create two archived logs with the same sequence number but different contents. Also, it is best to use the `BACKUP                         CONTROLFILE` command rather than a split mirror to make control file backups.

One way of creating a data file backup on disk is to use disk mirroring. For example, the operating system can maintain three identical copies of each file in the database. In this configuration, you can split off a mirrored copy of the database to use as a backup.

RMAN does not automate the splitting of mirrors, but can make use of split mirrors in backup and recovery. For example, RMAN can treat a split mirror of a data file as a data file copy, and can also back up this copy to disk or tape. The procedure in this section explains how to make a split mirror backup with the `ALTER                     SYSTEM SUSPEND/RESUME` functionality.

Some mirroring technology does not require Oracle Database to suspend all I/O before a mirror can be separated and used as a backup. Refer to your storage manager, volume manager, or file system documentation for information about whether you must suspend I/O from the database instance.

To make a split mirror backup of a tablespace by using SUSPEND/RESUME:

1. Start RMAN and then place the tablespaces to back up into backup mode with the `ALTER TABLESPACE ... BEGIN BACKUP` statement. (To place all tablespaces in backup mode, you can the `ALTER DATABASE BEGIN                         BACKUP` instead.)
	For example, to place tablespace `users` in backup mode, you connect RMAN to a target database and run the following `SQL` command:
	```
	ALTER TABLESPACE users BEGIN BACKUP;
	```
2. Suspend I/O if your mirroring software or hardware requires it. For example, enter the following command in RMAN:
	```
	ALTER SYSTEM SUSPEND;
	```
3. Split the mirrors for the underlying data files contained in these tablespaces.
4. Take the database out of the suspended state. For example, enter the following command in RMAN:
	```
	ALTER SYSTEM RESUME;
	```
5. Take the tablespaces out of backup mode. For example, enter:
	```
	ALTER TABLESPACE users END BACKUP;
	```
	You can also use `ALTER DATABASE END BACKUP` to take all tablespaces out of backup mode.
6. Catalog the user-managed mirror copies as data file copies with the `CATALOG` command. For example, enter:
	```
	CATALOG DATAFILECOPY '/dk2/oradata/trgt/users01.dbf'; # catalog split mirror
	```
7. Back up the data file copies. For example, run the `BACKUP` `DATAFILECOPY` command at the prompt:
	```
	BACKUP DATAFILECOPY '/dk2/oradata/trgt/users01.dbf';
	```
8. When you are ready to resilver a split mirror, first use the `CHANGE...UNCATALOG` command to uncatalog the data file copies you cataloged in Step 6. For example, enter:
	```
	CHANGE DATAFILECOPY '/dk2/oradata/trgt/users01.dbf' UNCATALOG;
	```
9. Resilver the split mirror for the affected data files.

### 10.6 Encrypting RMAN Backups

You can protect RMAN backup sets with backup encryption. Encrypted backups cannot be read if they are obtained by unauthorized users.

The RMAN backup encryption feature requires the Enterprise Edition of the database.

#### 10.6.1 About RMAN Backup Encryption Settings

Backup encryption is performed based on the specified encryption settings.

Encryption can be set with the following commands:

- `CONFIGURE ENCRYPTION`
	You can use this command to persistently configure transparent encryption. You cannot persistently configure dual mode or password mode encryption.
- `SET ENCRYPTION`
	You can use this command to configure dual mode or password mode encryption at the RMAN session level.

Note:

Keystore-based encryption is more secure than password-based encryption because no passwords are involved. Use password-based encryption only when absolutely necessary because your backups must be transportable.

The database uses a new encryption key for every encrypted backup. The backup encryption key is then encrypted with either the password, the database master key, or both, depending on the chosen encryption mode. Individual backup encryption keys or passwords are never stored in clear text.

A single restore operation can process backups encrypted in different modes. For each backup piece that it restores, RMAN checks whether it is encrypted. Transparently encrypted backups need no intervention if the Oracle keystore is open and available.

If password encryption is detected, then RMAN searches for a matching key in the list of passwords entered in the `SET DECRYPTION` command. If RMAN finds a usable key, then the restore operation proceeds. Otherwise, RMAN searches for a key in the Oracle keystore. If RMAN finds a usable key, then the restore operation proceeds; otherwise, RMAN signals an error that the backup piece cannot be decrypted.

Note:

If RMAN restores a set of backups created with different passwords, then all required passwords must be included with `SET DECRYPTION`.

RMAN encryption is a CPU-intensive operation and can affect backup performance. The actual amount of CPU utilization during encryption depends on whether both input and output devices for disk and SBT produce and consume data faster than the CPU can encrypt it. Here are a few guidelines for managing and trying to maximize CPU performance:

- Because encrypted backups consume more CPU resources than unencrypted backups, you can improve performance of encrypted backups to disk by using more RMAN channels. A general rule is to use the same number of channels as the number of CPU cores in your system. For example, use two channels for a dual-core processor.
- If both the disk subsystem and SBT-subsystem are fast, you can expect very high CPU utilization. You may want to consider slowing the rate of the backup by setting the RMAN `READRATE` parameter. For example, you can set an upper limit for block reads so that RMAN does not consume excessive disk bandwidth and thereby degrade online performance.

#### 10.6.2 Making Transparent-Mode Encrypted Backups

If you have configured transparent encryption with the `CONFIGURE` command, then no additional commands are required to create encrypted backups. Make RMAN backups as normal.

#### 10.6.3 Making Password-Mode Encrypted Backups

You can set an encryption password in an RMAN session by executing the `SET ENCRYPTION BY PASSWORD` command. If transparent encryption is configured, then specify the `ONLY` keyword to indicate that the backups are protected with a password and not with the configured transparent encryption.

To make password-mode encrypted backups:

Note:

Create a password that is secure. See [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=DBSEG33223) for more information.

1. Start RMAN and connect to a target database and recovery catalog (if used).
2. Execute the `SET ENCRYPTION ON IDENTIFIED BY` `password` `ONLY` command.
	The following example sets the encryption password for all tablespaces (where password is a placeholder for the actual password that you enter) in the backup and specifies `ONLY` to indicate that the encryption is password-only:
	```
	SET ENCRYPTION IDENTIFIED BY password ONLY ON FOR ALL TABLESPACES;
	```
3. For example, enter the following command:
	```
	BACKUP DATABASE PLUS ARCHIVELOG;
	```

#### 10.6.4 Making Dual-Mode Encrypted Backups

Use the `SET ENCRYPTION BY PASSWORD` command at the RMAN prompt to make password-protected backups. If transparent encryption is configured, then omit the `ONLY` keyword to indicate that the backups are protected with both a password and the configured transparent encryption.

To make dual-mode encrypted backups:

Note:

Create a password that is secure. See [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=DBSEG33223) for more information.

1. Start RMAN and connect to a target database and recovery catalog (if used).
2. Execute the `SET ENCRYPTION BY PASSWORD` command, making sure to omit the `ONLY` keyword.
	The following example sets the encryption password for all tablespaces (where password is a placeholder for the actual password that you enter) in the backup and omits `ONLY` to indicate dual-mode encryption:
	```
	SET ENCRYPTION IDENTIFIED BY password ON FOR ALL TABLESPACES;
	```
3. For example, enter the following command:
	```
	BACKUP DATABASE PLUS ARCHIVELOG;
	```

### 10.7 Restarting RMAN Backups

With the restartable backup feature, RMAN backs up only those files that were not backed up after a specified date.

#### 10.7.1 About Restartable Backups

The minimum unit of restartability is a data file. However, if a backup set contains one backup piece, and if this piece contains blocks from multiple data files, then the unit of restartability is the backup piece. The unit of restartability for image copies is a data file.

The benefit of restartable backups is that if the backup generates multiple backup sets, then the backup sets that completed successfully do not have to be rerun. However, if the entire database is written into one backup set, and if the backup fails halfway through, then the entire backup has to be restarted.

Any I/O errors that RMAN encounters when reading files or writing to the backup pieces or image copies cause RMAN to terminate the backup job in progress. For example, if RMAN tries to back up a data file but the data file is not on disk, then RMAN terminates the backup. If multiple channels are being used or redundant copies of backups are being created, however, then RMAN may be able to continue the backup without user intervention.

RMAN can back up only those files that have not been backed up since a specified date. Use this feature after a backup fails to back up the parts of the database missed by the failed backup.

You can restart a backup by specifying the `SINCE TIME` clause on the `BACKUP` command. If the `SINCE TIME` is later than the completion time, then RMAN backs up the file. If you use `BACKUP DATABASE NOT                 BACKED UP` without the `SINCE TIME` parameter, then RMAN only backs up files that have never been backed up.

#### 10.7.2 Restarting a Backup After It Partially Completes

Use the `SINCE TIME` parameter of the `BACKUP` command to specify a date after which a new backup is required.

If the `SINCE TIME` is later than the completion time, then RMAN backs up the file. If you use `BACKUP DATABASE NOT BACKED UP` without the `SINCE TIME` parameter, then RMAN only backs up files that have never been backed up.

To only back up files that were not backed up after a specified date:

1. Start RMAN and connect to a target database and recovery catalog (if used).
2. Run the `BACKUP ... NOT BACKED UP SINCE TIME` command.
	Specify a valid date in the `SINCE TIME` parameter. The following example uses the default configured channel to back up all database files and archived redo logs that have not been backed up in the last two weeks:
	```
	BACKUP 
	  NOT BACKED UP SINCE TIME 'SYSDATE-14'
	  DATABASE PLUS ARCHIVELOG;
	```

### 10.8 Managing Backup Windows

This section explains how to use backup windows to set limits for the time span in which a backup job can complete.

#### 10.8.1 About Backup Windows

A backup window is a period of time during which a backup must complete. For example, you may want to restrict your database backups to a window of time when user activity on your system is low, such as between 2:00 a.m. and 6:00 a.m.

RMAN backs up the least recently backed up files first. By default, RMAN backs up the files at the maximum possible speed. Specifying a window does not mean that RMAN backs up data faster than normal to ensure that the backup completes before the window ends.

By default, if the backup is not complete within the `DURATION` time, then RMAN interrupts the backup and reports an error. If the `BACKUP` command is in a [`RUN`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=RCMRF151) command, then the `RUN` command terminates. Any completed backup sets are retained and can be used in restore operations, even if the entire backup is not complete. Thus, if you retry a job that was interrupted when the available duration expired, each successive attempt covers more of the files needing backup. Any incomplete backup sets are discarded.

#### 10.8.2 Specifying a Backup Duration

Use the `DURATION` parameter of the `BACKUP` command to specify how long a given backup job is allowed to run.

To specify a backup duration:

1. Start RMAN and connect to a target database and recovery catalog (if used).
2. Execute the `BACKUP DURATION` command.
	For example, run the following command at 2:00 a.m. to specify that the backup runs until 6:00 a.m.:
	```
	BACKUP 
	  DURATION 4:00 
	  TABLESPACE users;
	```

#### 10.8.3 Permitting Partial Backups in a Backup Window

When you specify `PARTIAL`, RMAN does not report an error when a backup is interrupted because of the end of the backup window. Instead, RMAN displays a message showing which files are not backed up.

If the `BACKUP` command is part of a `RUN` block, then the remaining commands in the `RUN` block continue to execute.

If you specify `FILESPERSET 1`, then RMAN puts each file into its own backup set. When a backup is interrupted at the end of the backup window, only the backup of the file currently being backed up is lost. All backup sets completed during the window are saved, minimizing the lost work caused by the end of the backup window.

To prevent RMAN from issuing an error when a backup partially completes:

1. Start RMAN and connect to a target database and recovery catalog (if used).
2. Execute the [`BACKUP DURATION`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=RCMRF107) command with the `PARTIAL` option.
	For example, you run the following command at 2:00 a.m. to specify that the backup runs until 6:00 a.m. and that each data file is in a separate backup set:
	```
	BACKUP 
	  DURATION 4:00 PARTIAL 
	  TABLESPACE users 
	  FILESPERSET 1;
	```

#### 10.8.4 Minimizing Backup Load and Duration

When using `DURATION` you can run the backup with the maximum possible performance, or run as slowly as possible while still finishing within the allotted time, to minimize the performance impact of backup tasks.

Example 10-4 Using MINIMIZE TIME with BACKUP DURATION

This example maximizes performance by using the `MINIMIZE TIME` option with `DURATION`.

```
BACKUP 
  DURATION 4:00 PARTIAL 
  MINIMIZE TIME 
  DATABASE 
  FILESPERSET 1;
```

Example 10-5 Using MINIMIZE LOAD with BACKUP DURATION

This example uses the `MINIMIZE LOAD` option to extend the backup to use the full time available. RMAN monitors the progress of the running backup, and periodically estimates how long the backup takes to complete at its present rate. If RMAN estimates that the backup will finish before the end of the backup window, then it slows down the rate of backup so that the full available duration is used. This reduces the overhead on the database associated with the backup.

```
BACKUP 
  DURATION 4:00 
  MINIMIZE LOAD 
  DATABASE 
  FILESPERSET 1;
```

Note these issues when using `DURATION` and `MINIMIZE LOAD` with a tape backup:

- Efficient backup to tape requires tape streaming. If you use `MINIMIZE LOAD`, then RMAN may reduce the rate of backup to the point where tape streaming is not optimal.
- RMAN holds the tape resource for the entire duration of the backup window. This prevents the use of the tape resource for any other purpose during the backup window.

Because of these concerns, it is not recommended that you use `MINIMIZE LOAD` when backing up to tape.