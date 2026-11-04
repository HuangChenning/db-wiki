---
title: Backing Up the Database
book: "Backup and Recovery User's Guide"
doc_id: E10642-08
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/backup.112/e10642/rcmbckba.htm
tags:
  - oracle
  - 11g
  - backup-and-recovery-users-guide
---

## 9 Backing Up the Database

This chapter explains how to perform the most basic backup tasks and implement backup strategies using RMAN. This chapter contains the following topics:

See Also:

- [Chapter 10, "Backing Up the Database: Advanced Topics"](rcmbckad.md) to learn about more advanced topics such as backup optimization, duplexing, backup encryption, and restartable backups
- [Oracle Data Guard Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e41134/rman.htm#SBYDB04700) to learn how to perform RMAN backup and recovery in a Data Guard environment

## Overview of RMAN Backups

This section provides an overview of RMAN backups.

### Purpose of RMAN Backups

The primary purpose of RMAN backups is to protect your data. If a [media failure](glossary.md) or disaster occurs, then you can restore your backups and recover lost changes.

You can also make backups to preserve data for long-time archival, as explained in "Making Database Backups for Long-Term Storage", and to transfer data, as explained in the chapters included in [Part III, "Transferring Data with RMAN"](part_tra.md).

### Basic Concepts of RMAN Backups

As explained in [Chapter 8, "RMAN Backup Concepts"](rcmcncpt.md), you can back up all or part of your database with the [`BACKUP`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta007.htm#RCMRF107) command from within the RMAN client. Many of the techniques described in this chapter are also used in the Oracle suggested backup strategy provided by Enterprise Manager and described in [Oracle Database 2 Day DBA](https://docs.oracle.com/cd/E11882_01/server.112/e10897/backrest.htm#ADMQS009).

In many cases, after your database has been configured in accordance with your backup strategy, you can back up the database by entering the following command at the RMAN prompt:

```
RMAN> BACKUP DATABASE;
```

RMAN uses the configured settings, the records of previous backups, and the control file record of the database structure to determine an efficient set of steps for the backup. RMAN then performs these steps.

As explained in ["RMAN File Management in a Data Guard Environment"](rcmarchi.md), you can run RMAN backups at any database in a Data Guard environment. Any backup of any database in the environment is usable for recovery of any other database if the backup is accessible. You can offload all backups of database files, including control file backups, to a [physical standby database](glossary.md) and thereby avoid consuming resources on the primary database.

See Also:

- [Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta007.htm#RCMRF107) to learn about the `BACKUP` command
- [Oracle Data Guard Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e41134/rman.htm#SBYDB04700) to learn how to back up a standby database with RMAN

## Specifying Backup Output Options

If you specify only the minimum required options for an RMAN command such as [`BACKUP DATABASE`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta007.htm#RCMRF107), then RMAN determines the destination device, locations for backup output, and a backup tag automatically based on your configured environment and built-in RMAN defaults.

You can also provide arguments to `BACKUP` to override these defaults. The most typical options are described in the following sections:

- Specifying the Device Type for an RMAN Backup
- Specifying Backup Set or Copy for an RMAN Backup to Disk
- Specifying a Format for RMAN Backups
- Specifying Tags for an RMAN Backup
- Making Compressed Backups

See Also:

[Chapter 10, "Backing Up the Database: Advanced Topics"](rcmbckad.md) to learn about advanced backup options such as duplexing and restarting backups

### Specifying the Device Type for an RMAN Backup

The `BACKUP` command takes a `DEVICE TYPE` clause that specifies whether to back up to disk or tape device. Example 9-1 illustrates a backup to disk.

Example 9-1 Specifying Device Type DISK

```
BACKUP DATABASE 
  DEVICE TYPE DISK;
```

When you run `BACKUP` without a `DEVICE TYPE` clause, RMAN stores the backup on the configured default device (disk or [SBT](glossary.md)). You set the default device with the [`CONFIGURE DEFAULT DEVICE TYPE`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta010.htm#RCMRF113) command described in ["Configuring the Default Device for Backups: Disk or SBT"](rcmconfb.md).

### Specifying Backup Set or Copy for an RMAN Backup to Disk

RMAN can create backups on disk as image copies or as backup sets. ["Configuring the Default Type for Backups: Backup Sets or Copies"](rcmconfb.md) explains how to configure the default disk device. You can override this default with the `AS` `COPY` or `AS` `BACKUPSET` clauses. To back up to disk as image copies, use `BACKUP` `AS` `COPY` as shown in Example 9-2.

Example 9-2 Making Image Copies

```
BACKUP AS COPY
  DEVICE TYPE DISK 
  DATABASE;
```

To back up your data into backup sets, use the `AS BACKUPSET` clause. You can allow backup sets to be created on the configured default device, or direct them specifically to disk or tape, as shown Example 9-3.

Example 9-3 Making Backup Sets

```
BACKUP AS BACKUPSET 
  DATABASE;

BACKUP AS BACKUPSET 
  DEVICE TYPE DISK 
  DATABASE;

BACKUP AS BACKUPSET 
  DEVICE TYPE SBT 
  DATABASE;
```

### Specifying a Format for RMAN Backups

RMAN provides a range of options to name the files generated by the `BACKUP` command. RMAN uses the following set of rules to determine the format of the output files, which are listed in order of precedence:

1. If a [`FORMAT`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsubcl010.htm#RCMRF195) parameter is specified on the `BACKUP` command, then this setting controls the generated file name.
	For example, you can direct the output to a specific location, as shown in the following command:
	```
	BACKUP DATABASE 
	  FORMAT "/disk1/backup_%U";  # specifies a location on the file system
	```
	In this case, backups are stored with generated unique file names with the prefix `/disk1/backup_`. The `%U` substitution variable, used to generate a unique string at this point in the file name, is required.
	You can also use the `FORMAT` parameter to name an ASM disk group as the backup destination, as shown in the following example:
	```
	BACKUP DATABASE 
	  FORMAT '+dgroup1';  # specifies an ASM disk group
	```
	No `%U` is required in this case because [Automatic Storage Management (ASM)](glossary.md) generates unique file names as needed. However, you can specify `%U` if desired.
	Note:
	If you specify `FORMAT` when a fast recovery area is enabled, then RMAN obeys the `FORMAT` setting. If no location is specified in the `FORMAT` clause, then RMAN creates the backup in a platform-specific location.
2. If a `FORMAT` setting is configured for the specific channel used for the backup, then this setting controls the generated file name.
3. If a `FORMAT` setting is configured for the device type used for the backup, then this setting controls the generated file name.
4. If a [fast recovery area](glossary.md) is enabled during a disk backup, and if `FORMAT` is not specified, then RMAN creates the backup with an automatically generated name in the fast recovery area.
5. If none of the other conditions in this list apply, then the default location and file name format of the backup are platform-specific.

See Also:

[Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsubcl010.htm#RCMRF195) to learn about the `FORMAT` clause, and the installation guides in the Oracle Database documentation library to learn about the default file locations for your platform

#### Specifying Multiple Formats for Disk Backups

Typically, you do not need to specify a format when backing up to tape because the default `%U` variable generates a unique file name for tape backups. When backing up to disk, however, you can specify a format to spread the backup across several drives for improved performance. In this case, allocate one `DISK` channel for each disk drive and specify the format string on the [`ALLOCATE CHANNEL`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta004.htm#RCMRF102) command so that the file names are on different disks. For example, issue the following command:

```
RUN
{ 
  ALLOCATE CHANNEL disk1 DEVICE TYPE DISK FORMAT '/disk1/%d_backups/%U';
  ALLOCATE CHANNEL disk2 DEVICE TYPE DISK FORMAT '/disk2/%d_backups/%U';
  ALLOCATE CHANNEL disk3 DEVICE TYPE DISK FORMAT '/disk3/%d_backups/%U';
  BACKUP AS COPY DATABASE; 
}
```

You can distribute backups in this manner by default in the future, by configuring channels as follows:

```
CONFIGURE DEVICE TYPE DISK PARALLELISM 3;
CONFIGURE DEFAULT DEVICE TYPE TO DISK;
CONFIGURE CHANNEL 1 DEVICE TYPE DISK FORMAT '/disk1/%d_backups/%U';
CONFIGURE CHANNEL 2 DEVICE TYPE DISK FORMAT '/disk2/%d_backups/%U';
CONFIGURE CHANNEL 3 DEVICE TYPE DISK FORMAT '/disk3/%d_backups/%U';
BACKUP AS COPY DATABASE;
```

### Specifying Tags for an RMAN Backup

RMAN attaches a character string called a [tag](glossary.md) to every backup it creates, as a way of identifying the backup. You can either accept the default tag or specify your own with the `TAG` parameter of the `BACKUP` command.

#### About Backup Tags

User-specified tags are a useful way to indicate the purpose or usage of different classes of backups or copies. You can tag backup sets, proxy copies, data file copies, or control file copies. For example, you can tag data file copies that you intend to use in a [`SWITCH`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta2020.htm#RCMRF159) command as `for_switch_only` and file copies that should be used only for a [`RESTORE`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta2008.htm#RCMRF149) command as `for_restore_only`.

Tags do not need to be unique, so multiple backup sets or image copies can have the same tag, for example, `weekly_backup`. Assume that you specify that a data file should be restored from backups that have a specific tag. If multiple backups of the requested file has the desired tag, then RMAN restores the most recent backup that has the desired tag, within any constraints on the `RESTORE` command.

In practice, tags are often used to distinguish a series of backups created as part of a single strategy, such as an incremental backup strategy. For example, you might create a weekly incremental backups with a tag like `BACKUP TAG weekly_incremental`. Many forms of the `BACKUP` command let you associate a tag with a backup, and many `RESTORE` and [`RECOVER`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta2001.htm#RCMRF140) commands let you specify a tag to restrict which backups to use in the `RESTORE` or `RECOVER` operation.

If you do not explicitly specify a tag with the `TAG` parameter of the `BACKUP` command, then RMAN implicitly creates a default tag for backups (except for control file autobackups). The format of the tag is `TAG` `YYYYMMDD` `T` `HHMMSS`, where `YYYY` is the year, `MM` is the month, `DD` is the day, `HH` is the hour (in 24-hour format), `MM` is the minutes, and `SS` is the seconds. For example, a backup of data file `1` may get the tag `TAG20070208T133437`. The date and time refer to when RMAN started the backup in the time zone of the instance performing the backup. If multiple backup sets are created by one `BACKUP` command, then each backup piece has the same default tag.

Tags are stored in uppercase, regardless of the case used when entering them. The maximum length of a backup tag is 30 bytes. Tags cannot use operating system environment variables or use special formats such as `%T` or `%D`.

See Also:

[Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta007.htm#RCMRF107) for the default format description in `BACKUP` `...` `TAG`

#### Specifying Tags for Backup Sets and Image Copies

The characters in a tag must be limited to the characters that are legal in file names on the target database file system. For example, [Automatic Storage Management (ASM)](glossary.md) does not support the use of the hyphen (`-`) in the file names it uses internally, so a tag including a hyphen (such as `weekly-incr`) is not a legal tag name for backups in ASM disk groups.

When you tag a backup set, the tag is an attribute of each backup piece in a given copy of a backup set. If you create a [multiplexed backup set](glossary.md), then each copy of the backup set is assigned the same tag. Example 9-4 creates one backup set with the tag `MONDAYBKP`.

Example 9-4 Applying a Tag to a Backup Set

```
BACKUP AS BACKUPSET
  COPIES 1 
  DATAFILE 7
  TAG mondaybkp;
```

When you specify a tag for image copies, the tag applies to each individual copy. Example 9-5 shows that copies of data files in tablespaces `users` and `tools` are assigned the tag `MONDAYCPY`.

Example 9-5 Applying Tags to Image Copies

```
BACKUP AS COPY 
  TABLESPACE users, tools
  TAG mondaycpy;
```

You can use `FROM TAG` to copy an image copy with a specific tag, and then use `TAG` to assign the output copy a different tag. Example 9-6 creates new copies of all image copies of the database that have the tag `full_cold_copy` and gives the new copies the tag `new_full_cold_copy`.

Example 9-6 Assigning Tags to Output Copies

```
BACKUP AS COPY
  COPY OF DATABASE
    FROM TAG full_cold_copy
  TAG new_full_cold_copy;
```

### Making Compressed Backups

For any use of the `BACKUP` command that creates backup sets, you can take advantage of RMAN support for [binary compression](glossary.md) of backup sets. Specify the `AS COMPRESSED BACKUPSET` option to the `BACKUP` command.

RMAN compresses the backup set contents before writing them to disk. The details of which binary compression level is used are automatically recorded in the backup set. There is no need to explicitly mention the type of compression used or how to decompress the backup set in the recovery operation.

Example 9-7 backs up the entire database and archived logs to the configured default backup destination (disk or tape), producing compressed backup sets.

Example 9-7 Making Compressed Backups

```
BACKUP 
  AS COMPRESSED BACKUPSET 
  DATABASE PLUS ARCHIVELOG;
```

Binary compression creates some performance overhead during backup and restore operations. Binary compression consumes CPU resources, so compressed backups should not be scheduled when CPU usage is high. However, the following circumstances may warrant paying the performance penalty:

- You are using disk-based backups when disk space in your fast recovery area or other disk-based backup destination is limited.
- You are performing your backups to some device over a network when reduced network bandwidth is more important than CPU usage.
- You are using some archival backup media such as CD or DVD, where reducing backup sizes saves on media costs and archival storage.

See Also:

For performance details regarding backup sets, consult the ["Binary Compression for Backup Sets"](rcmcncpt.md) and the `AS COMPRESSED BACKUPSET` option of the `BACKUP` command in [Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta007.htm#RCMRF107).

## Backing Up Database Files with RMAN

This section contains the following topics:

- Backing Up a Whole Database with RMAN
- Backing Up Tablespaces and Datafiles with RMAN
- Backing Up Control Files with RMAN
- Backing Up Server Parameter Files with RMAN
- Backing Up a Database in NOARCHIVELOG Mode

### Backing Up a Whole Database with RMAN

You can perform a [whole database backup](glossary.md) with the database mounted or open. To perform a whole database backup, from the RMAN prompt, use the [`BACKUP DATABASE`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta007.htm#RCMRF107) command.

You may want to exclude specified tablespaces from a whole database backup. As explained in ["Configuring Tablespaces for Exclusion from Whole Database Backups"](rcmconfa.md), you can persistently skip tablespaces across RMAN sessions by executing the [`CONFIGURE EXCLUDE`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta010.htm#RCMRF113) command for each tablespace that you always want to skip. You can override the configured setting with `BACKUP ... NOEXCLUDE`.

To back up the database:

1. Start RMAN and connect to a target database and a recovery catalog (if used).
2. Ensure the database is mounted or open.
3. Issue the [`BACKUP DATABASE`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta007.htm#RCMRF107) command at the RMAN prompt.
	The simplest form of the command requires no options or parameters:
	```
	BACKUP DATABASE;
	```
	For a list of what files are backed up (datafiles, control file, server parameter file) see the `BACKUP` command keyword `DATABASE` in Oracle Database Backup and Recovery Reference.
	The following example backs up the database, switches the online redo logs, and includes archived logs in the backup:
	```
	BACKUP DATABASE PLUS ARCHIVELOG;
	```
	By archiving the logs immediately after the backup, you ensure that you have a full set of archived logs through the time of the backup. In this way, you guarantee that you can perform media recovery after restoring this backup.

See Also:

- [Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta007.htm#RCMRF107) to learn about the `BACKUP` command and [Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta011.htm#RCMRF114) to learn about the `CONNECT` command
- ["Skipping Offline, Read-Only, and Inaccessible Files"](rcmbckad.md) to learn how to use `BACKUP ... SKIP` to skip inaccessible data files or data files that are in offline or read-only tablespaces

### Backing Up Tablespaces and Datafiles with RMAN

You can back up one or more tablespaces with the `BACKUP TABLESPACE` command or one or more datafiles with the `BACKUP DATAFILE` command. When you specify tablespaces, RMAN translates the tablespace name internally into a list of datafiles. The database can be mounted or open. Tablespaces can be read/write or read-only.

Note:

Transportable tablespaces do not have to be in read/write mode for backup as in previous releases.

RMAN automatically backs up the control file and the server parameter file (if the instance was started with a server parameter file) when data file `1` is included in the backup. If [control file autobackup](glossary.md) is enabled, then RMAN writes the current control file and server parameter file to a separate autobackup piece. Otherwise, RMAN includes these files in the backup set that contains data file `1`.

To back up tablespaces or datafiles:

1. Start RMAN and connect to a target database and a recovery catalog (if used).
2. If the database instance is not started, then either mount or open the database.
3. Run the `BACKUP` `TABLESPACE` command or `BACKUP DATAFILE` command at the RMAN prompt.
	The following example backs up the `users` and `tools` tablespaces to tape:
	```
	BACKUP
	  DEVICE TYPE sbt
	  TABLESPACE users, tools;
	```
	The following example uses an SBT channel to back up data files `1` through `4` and a data file copy stored at `/tmp/system01.dbf` to tape:
	```
	BACKUP 
	  DEVICE TYPE sbt 
	  DATAFILE 1,2,3,4 
	  DATAFILECOPY '/tmp/system01.dbf';
	```

### Backing Up Control Files with RMAN

You can back up the control file when the database is mounted or open. RMAN uses a [snapshot control file](glossary.md) to ensure a read-consistent version. If the [`CONFIGURE CONTROLFILE AUTOBACKUP`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta010.htm#RCMRF113) command is set to `ON` (by default it is `OFF`), then RMAN automatically backs up the control file and server parameter file after every backup and after database structural changes. The [control file autobackup](glossary.md) contains metadata about the previous backup, which is crucial for [disaster recovery](glossary.md).

Note:

You can restore a backup of a control file made on one Data Guard database to any other database in the environment. Primary and standby control file backups are interchangeable. See [Oracle Data Guard Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e41134/rman.htm#SBYDB04700) to learn how to use RMAN to restore files on a standby database.

If the autobackup feature is not set, then you must manually back up the control file in one of the following ways:

- Run `BACKUP` `CURRENT` `CONTROLFILE`.
- Include a backup of the control file within any backup by using the `INCLUDE` `CURRENT` `CONTROLFILE` option of the `BACKUP` command.
- Back up data file `1`, because RMAN automatically includes the control file and server parameter file in backups of data file `1`.
	Note:
	If the control file block size is not equal to the block size for data file `1`, then the control file cannot be written into the same backup set as the data file. RMAN writes the control file into a backup set by itself if the block size is different. The `V$CONTROLFILE.BLOCK_SIZE` column indicates the control file block size, whereas the `DB_BLOCK_SIZE` initialization parameter indicates the block size of data file `1`.

#### Making a Manual Backup of the Control File

A manual backup of the control file is different from a control file autobackup. RMAN makes a control file autobackup after the files specified in the `BACKUP` command are backed up. Thus, the autobackup—unlike a manual control file backup—contains metadata about the backup that just completed. Also, RMAN can automatically restore autobackups without the use of a recovery catalog.

To make a manual backup, you can either specify `INCLUDE` `CURRENT` `CONTROLFILE` when backing up other files or specify `BACKUP CURRENT CONTROLFILE`. You can also back up control files copies on disk by specifying the `CONTROLFILECOPY` parameter.

To manually back up the control file:

1. Start RMAN and connect to a target database and a recovery catalog (if used).
2. Ensure the target database is mounted or open.
3. Execute the `BACKUP` command with the desired control file clause.
	The following example backs up tablespace `users` to tape and includes the current control file in the backup:
	```
	BACKUP DEVICE TYPE sbt 
	  TABLESPACE users 
	  INCLUDE CURRENT CONTROLFILE;
	```
	The following example backs up the current control file to the default disk device:
	```
	BACKUP AS COPY
	  CURRENT CONTROLFILE 
	  FORMAT '/tmp/control01.ctl';
	```
	The following example backs up the control file copy created in the previous example to tape:
	```
	BACKUP AS COPY 
	  CURRENT CONTROLFILE 
	  FORMAT '/tmp/control01.ctl';
	BACKUP DEVICE TYPE sbt 
	  CONTROLFILECOPY '/tmp/control01.ctl';
	```
	If the control file autobackup feature is enabled, then RMAN makes two control file backups in these examples: the explicit backup of the files specified in the `BACKUP` command and the control file and server parameter file autobackup.
	See Also:
	[Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta010.htm#RCMRF113) to learn about the `CONFIGURE CONTROLFILE AUTOBACKUP` command

### Backing Up Server Parameter Files with RMAN

As explained in "Backing Up Control Files with RMAN", RMAN automatically backs up the current server parameter file in certain cases. The `BACKUP` `SPFILE` command backs up the parameter file explicitly. The server parameter file that is backed up is the one currently in use by the instance.

To back up the server parameter file:

1. Start RMAN and connect to a target database and a recovery catalog (if used).
2. Ensure the target database is mounted or open.
	The database must have been started with a server parameter file. If the instance is started with a client-side initialization parameter file, then RMAN issues an error if you execute `BACKUP ... SPFILE`.
3. Execute the `BACKUP ... SPFILE` command.
	The following example backs up the server parameter file to tape:
	```
	BACKUP DEVICE TYPE sbt SPFILE;
	```

### Backing Up a Database in NOARCHIVELOG Mode

You can only backup a database in `NOARCHIVELOG` mode when the database is closed and in a consistent state. The script shown in Example 9-8 puts the database into the correct mode for a consistent, whole database backup and then backs up the database. The script assumes that [control file autobackup](glossary.md) is enabled for the database.

Example 9-8 Backing Up a Database in NOARCHIVELOG Mode

```
SHUTDOWN IMMEDIATE; 
# Start up the database in case it suffered instance failure or was 
# closed with SHUTDOWN ABORT before starting this script. 
STARTUP FORCE DBA; 
SHUTDOWN IMMEDIATE; 
STARTUP MOUNT;
# this example uses automatic channels to make the backup
BACKUP 
  INCREMENTAL LEVEL 0
  MAXSETSIZE 10M
  DATABASE
  TAG 'BACKUP_1';
# Now that the backup is complete, open the database. 
ALTER DATABASE OPEN;
```

You can skip tablespaces, such as read-only tablespaces, but any skipped tablespace that has not been offline or read-only since its last backup is lost if the database has to be restored from a backup.

## Backing Up Archived Redo Logs with RMAN

Archived redo logs are the key to successful media recovery. You should back them up regularly.

### About Backups of Archived Redo Logs

Several features of RMAN backups are specific to archived redo logs. For example, you can use `BACKUP ... DELETE` to delete one or all copies of archived redo logs from disk after backing them up to backup sets.

#### Archived Redo Log Failover

Even if your redo logs are being archived to multiple destinations and you use RMAN to back up archived redo logs, RMAN selects only one copy of the archived redo log file to include in the backup set. Because logs with the same log sequence number are identical, RMAN does not need to include more than one log copy.

The [archived redo log failover](glossary.md) feature enables RMAN to complete a backup even when some archiving destinations are missing logs or contain logs with corrupt blocks. If at least one log corresponding to a given log sequence and thread is available in the fast recovery area or any of the archiving destinations, then RMAN tries to back it up. If RMAN finds a corrupt block in a log file during backup, it searches other destinations for a copy of that log without corrupt blocks.

For example, assume that you archive logs 121 through 124 to two destinations: `/arch1` and `/arch2`. Table 9-1 shows the archived redo log records in the control file.

Table 9-1 Sample Archived Redo Log Records

| Sequence | Filename in /arch1 | Filename in /arch2 |
| --- | --- | --- |
| 121 | `/arch1/archive1_121.arc` | `/arch2/archive1_121.arc` |
| 122 | `/arch1/archive1_122.arc` | `/arch2/archive1_122.arc` |
| 123 | `/arch1/archive1_123.arc` | `/arch2/archive1_123.arc` |
| 124 | `/arch1/archive1_124.arc` | `/arch2/archive1_124.arc` |

However, unknown to RMAN, a user deletes logs 122 and 124 from the `/arch1` directory. Afterward, you run the following backup:

```
BACKUP ARCHIVELOG
  FROM  SEQUENCE 121 
  UNTIL SEQUENCE 125;
```

With failover, RMAN completes the backup, using logs 122 and 124 in `/arch2`.

#### Online Redo Log Switching

Another important RMAN feature is automatic online redo log switching. To make an open database backup of archived redo logs that includes the most recent online redo log, you can execute the `BACKUP` command with any of the following clauses:

- `PLUS ARCHIVELOG`
- `ARCHIVELOG ALL`
- `ARCHIVELOG FROM ...`

Before beginning the backup, RMAN switches out of the current redo log group, and archives all online redo logs that have not yet been archived, up to and including the redo log group that was current when the command was issued. This feature ensures that the backup contains all redo generated before the start of the command.

An effective way of backing up archived redo logs is the `BACKUP` `...` `PLUS` `ARCHIVELOG` command, which causes RMAN to do the following:

1. Runs the [`ALTER SYSTEM`](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_2014.htm#SQLRF00902) `ARCHIVE` `LOG` `CURRENT` statement.
2. Runs `BACKUP` `ARCHIVELOG` `ALL`. If [backup optimization](glossary.md) is enabled, then RMAN skips logs that it has already backed up to the specified device.
3. Backs up the rest of the files specified in the `BACKUP` command.
4. Runs the `ALTER` `SYSTEM` `ARCHIVE` `LOG` `CURRENT` statement.
5. Backs up any remaining archived logs generated during the backup. If backup optimization is not enabled, then RMAN backs up the logs generated in Step 1 plus all the logs generated during the backup.

The preceding steps guarantee that data file backups taken during the command are recoverable to a consistent state. Also, unless the online redo log is archived at the end of the backup, `DUPLICATE` is not possible with the backup.

### Backing Up Archived Redo Log Files

To back up archived logs, use the `BACKUP` `ARCHIVELOG` command. If [backup optimization](glossary.md) is enabled, then RMAN skips backups of archived logs that have already been backed up to the specified device.

To back up archived redo log files:

1. Start RMAN and connect to a target database and a recovery catalog (if used).
2. Ensure that the target database is mounted or open.
3. Execute the `BACKUP ARCHIVELOG` or `BACKUP ... PLUS ARCHIVELOG` command.
	The following example backs up the database and all archived redo logs:
	```
	BACKUP DATABASE PLUS ARCHIVELOG;
	```
	The following example uses a configured disk or SBT channel to back up one copy of each log sequence number for all archived redo logs:
	```
	BACKUP ARCHIVELOG ALL;
	```
	You can also specify a range of archived redo logs by time, SCN, or log sequence number, as in the following example:
	```
	BACKUP ARCHIVELOG 
	  FROM TIME  'SYSDATE-30'
	  UNTIL TIME 'SYSDATE-7';
	```

### Backing Up Only Archived Redo Logs That Need Backups

You can indicate that RMAN should automatically skip backups of archived redo logs in the following ways:

- Configure [backup optimization](glossary.md).
	As explained in ["Backup Optimization and the CONFIGURE command"](rcmconfb.md), if you enable [backup optimization](glossary.md), then the [`BACKUP ARCHIVELOG`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta007.htm#RCMRF107) command skips backing up files when an identical archived log has already been backed up to the specified device type. An archived log is considered identical to another when it has the same DBID, thread, sequence number, and `RESETLOGS` SCN and time.
- Configure an [archived redo log deletion policy](glossary.md).
	As explained in ["Configuring an Archived Redo Log Deletion Policy"](rcmconfb.md), if the deletion policy is configured with the `BACKED UP` `integer` `TIMES` clause, then a `BACKUP ARCHIVELOG` command copies the logs unless `integer` backups already exist on the specified device type. If `integer` backups of the logs exist, then the `BACKUP ARCHIVELOG` command skips the logs.

The `BACKUP ... NOT BACKED UP` `integer` `TIMES` command specifies that RMAN should back up only those archived log files that have not been backed up at least `integer` times to the specified device. To determine the number of backups for a file, RMAN only considers backups created on the same device type as the current backup.

The `BACKED UP` clause is a convenient way to back up archived logs to a specified device type. For example, you can specify that RMAN should keep two copies of each archived redo log on tape and skip additional backups.

To back up archived redo logs that need backups:

1. Start RMAN and connect to a target database and a recovery catalog (if used).
2. Ensure that the target database is mounted or open.
3. Ensure that appropriate channels are configured for the backup.
4. Execute the `BACKUP ARCHIVELOG` command with the `NOT BACKED UP` clause.
	```
	BACKUP ARCHIVELOG ALL NOT BACKED UP 2 TIMES;
	```

See Also:

["Using Backup Optimization to Skip Files"](rcmbckad.md) for scenarios using `NOT BACKED UP`

### Deleting Archived Redo Logs After Backups

The `BACKUP ARCHIVELOG` `... DELETE INPUT` command deletes archived log files after they are backed up. This command eliminates the separate step of manually deleting archived redo logs.

With `DELETE` `INPUT`, RMAN deletes only the specific copy of the archived log chosen for the backup set. With `DELETE` `ALL` `INPUT`, RMAN deletes each backed-up archived redo log file from all log archiving destinations.

As explained in ["Configuring an Archived Redo Log Deletion Policy"](rcmconfb.md), the `BACKUP ... DELETE INPUT` and `DELETE ARCHIVELOG` commands obey the [archived redo log deletion policy](glossary.md) for logs in all archiving locations. For example, if you specify that logs should only be deleted when backed up at least twice to tape, then `BACKUP ... DELETE` honors this policy.

For the following procedure, assume that you archive to `/arc_dest1`, `/arc_dest2`, and the fast recovery area.

To delete archived redo logs after a backup:

1. Start RMAN and connect to a target database and a recovery catalog (if used).
2. Ensure that the target database is mounted or open.
3. Run the `BACKUP` command with the `DELETE INPUT` clause.
	Assume that you run the following `BACKUP` command:
	```
	BACKUP DEVICE TYPE sbt 
	  ARCHIVELOG ALL 
	    DELETE ALL INPUT;
	```
	In this case, RMAN backs up only one copy of each log sequence number in these archiving locations. RMAN deletes all copies of any log that it backed up from both the fast recovery area and the other archiving destinations.
	If you had specified `DELETE` `INPUT` rather than `DELETE` `ALL` `INPUT`, then RMAN would have only deleted the specific archived redo log files that it backed up. For example, RMAN would delete the logs in `/arc_dest1` if these files were used as the source of the backup, but leave the contents of the `/arc_dest2` intact.

See Also:

- [Oracle Data Guard Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e41134/rman.htm#SBYDB04700) to learn about archived redo log management with standby databases
- [Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta010.htm#RCMRF113) to learn about the `CONFIGURE ARCHIVELOG DELETION POLICY` command
- [Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta016.htm#RCMRF121) to learn about the `DELETE ARCHIVELOG` command
- ["Deleting RMAN Backups and Archived Redo Logs"](rcmmaint.md)

## Making and Updating Incremental Backups

As explained in ["Incremental Backups"](rcmcncpt.md), an [incremental backup](glossary.md) copies only data file blocks that have changed since a specified previous backup. An incremental backups is either a [cumulative incremental backup](glossary.md) or [differential incremental backup](glossary.md).

Although the content of the backups is the same, `BACKUP DATABASE` and `BACKUP INCREMENTAL LEVEL 0 DATABASE` are different. A [full backup](glossary.md) is not usable as part of an incremental strategy, whereas a [level 0 incremental backup](glossary.md) is the basis of an incremental strategy. No RMAN command can change a full backup into a level 0 incremental backup.

As with full backups, RMAN can make incremental backups of an `ARCHIVELOG` mode database that is open. If the database is in `NOARCHIVELOG` mode, then RMAN can make incremental backups only after a consistent shutdown.

### Purpose of Incremental Backups

The primary reasons for making incremental backups part of your strategy are:

- Faster daily backups if [block change tracking](glossary.md) is enabled (see "Using Block Change Tracking to Improve Incremental Backup Performance")
- Ability to roll forward data file image copies, thereby reducing recovery time and avoiding repeated full backups.
- Less bandwidth consumption when backing up over a network.
- Improved performance when the aggregate tape bandwidth for tape write I/Os is much less than the aggregate disk bandwidth for disk read I/Os.
- Possibility of recovering changes to objects created with the `NOLOGGING` option.
	For example, direct load inserts do not create redo log entries, so their changes cannot be reproduced with media recovery. Direct load inserts do change data blocks, however, and these blocks are captured by incremental backups.
- Synchronize a physical standby database with the primary database. You can use the RMAN `BACKUP INCREMENTAL FROM SCN` command to create a backup on the primary database that starts at the current SCN of the standby database, which you can then use to roll forward the standby database. See [Oracle Data Guard Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e41134/rman.htm#SBYDB04700) to learn how to apply incremental backups to a standby database.

See Also:

[Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/tspaces.htm#ADMIN11374) for more information about `NOLOGGING` mode

### Planning an Incremental Backup Strategy

Choose a backup strategy according to an acceptable [MTTR](glossary.md) (mean time to recover). For example, you can implement a three-level backup scheme so that a level 0 backup is taken monthly, a cumulative level 1 is taken weekly, and a differential level 1 is taken daily. In this strategy, you never have to apply more than a day of redo for complete recovery.

When deciding how often to take level 0 backups, a general rule is to take a new level 0 backup whenever 20% or more of the data has changed. If the rate of change to your database is predictable, then you can observe the size of your incremental backups to determine when a new level 0 backup is appropriate. The following SQL query determines the number of blocks written to an incremental level 1 backup of each data file with at least 20% of its blocks backed up:

```
SELECT   FILE#, INCREMENTAL_LEVEL, COMPLETION_TIME, 
         BLOCKS, DATAFILE_BLOCKS 
FROM     V$BACKUP_DATAFILE 
WHERE    INCREMENTAL_LEVEL > 0 
AND      BLOCKS / DATAFILE_BLOCKS > .2
ORDER BY COMPLETION_TIME;
```

Compare the number of blocks in level 1 backups to a level 0 backup. For example, if you create only level 1 cumulative backups, then take a new level 0 backup when the most recent level 1 backup is about half of the size of the level 0 backup.

An effective way to conserve disk space is to make incremental backups to disk, and then offload the backups to tape with the `BACKUP` `AS` `BACKUPSET` command. Incremental backups are generally smaller than full backups, which limits the space required to store them until they are moved to tape. When the incremental backups on disk are backed up to tape, the tape is more likely to stream because all blocks of the incremental backup are copied to tape. There is no possibility of delay due to time required for RMAN to locate changed blocks in the datafiles.

Another strategy is to use incrementally updated backups as explained in "Incrementally Updating Backups". In this strategy, you create an image copy of each data file, then periodically roll forward this copy by making and then applying a level 1 incremental backup. In this way you avoid the overhead of making repeated full image copies of your data files, but enjoy all of the advantages.

In a Data Guard environment, you can offload incremental backups to a [physical standby database](glossary.md). Incremental backups of a standby and primary database are interchangeable. Thus, you can apply an incremental backup of a standby database to a primary database, or apply an incremental backup of a primary database to a standby database.

See Also:

[Oracle Data Guard Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e41134/rman.htm#SBYDB04700) to learn how to back up a standby database with RMAN. In particular, consult Chapter 9, "Managing Physical and Snapshot Standby Databases"

### Making Incremental Backups

After starting RMAN, run the `BACKUP` `INCREMENTAL` command at the RMAN prompt. By default incremental backups are differential.

To make an incremental backup:

1. Start RMAN and connect to a target database and a recovery catalog (if used).
2. Ensure that the target database is mounted or open.
3. Execute the `BACKUP INCREMENTAL` command with the desired options.
	Use the `LEVEL` parameter to indicate the incremental level. The following example makes a level 0 incremental database backup.
	```
	BACKUP
	  INCREMENTAL LEVEL 0
	  DATABASE;
	```
	The following example makes a [differential incremental backup](glossary.md) at level 1 of the `SYSTEM` and `tools` tablespaces. It only backs up those data blocks changed since the most recent level 1 or level 0 backup.
	```
	BACKUP
	  INCREMENTAL LEVEL 1
	  TABLESPACE SYSTEM, tools;
	```
	The following example makes a [cumulative incremental backup](glossary.md) at level 1 of the tablespace `users`, backing up all blocks changed since the most recent level 0 backup.
	```
	BACKUP
	  INCREMENTAL LEVEL 1 CUMULATIVE
	  TABLESPACE users;
	```

#### Making Incremental Backups of a VSS Snapshot

You can use the [Volume Shadow Copy Service (VSS)](glossary.md) with the Oracle VSS writer to make a [shadow copy](glossary.md) or snapshot of files in a database. You must use a third-party backup program other than RMAN to make VSS snapshots with the Oracle VSS writer. In this case, the [fast recovery area](glossary.md) automates management of files that are backed up in a VSS snapshot and deletes them as needed.

You can use the `BACKUP INCREMENTAL LEVEL 1 ... FROM SCN` command in RMAN to create incremental backups in the fast recovery area. Thus, you can use this command to create an incremental level 1 backup of a VSS shadow copy. RMAN can apply incremental backups during recovery transparently.

See Also:

[Oracle Database Platform Guide for Microsoft Windows](https://docs.oracle.com/cd/E11882_01/win.112/e10845/toc.htm) to learn how to make VSS backups with RMAN

### Incrementally Updating Backups

By incrementally updating backups, you can avoid the overhead of making full image copy backups of datafiles, while also minimizing time required for media recovery of your database. For example, if you run a daily backup script, then you never have more than 1 day of redo to apply for media recovery.

To incrementally update data file backups:

1. Create a full image copy backup of a data file with a specified tag.
2. At regular intervals (such as daily), make a level 1 differential incremental backup of the data file and use the same tag as the base data file copy.
3. Apply the incremental backup to the most recent backup with the same tag.

This technique rolls forward the backup to the time when the level 1 incremental backup was made. RMAN can restore this [incrementally updated backup](glossary.md) and apply changes from the redo log. The result is the same as restoring a data file backup taken at the SCN of the most recently applied incremental level 1 backup.

Note:

If you run `RECOVER COPY` daily without specifying an `UNTIL TIME`, then a continuously updated image copy cannot satisfy a [recovery window](glossary.md) of more than a day. The incrementally updated backup feature is an optimization for fast media recovery.

#### Incrementally Updating Backups: Basic Example

To create incremental backups for use in an incrementally updated backups strategy, use the `BACKUP ...` `FOR` `RECOVER` `OF` `COPY` `WITH` `TAG` form of the `BACKUP` command. The command is best understood in a sample script that implements the strategy.

The script in Example 9-9, run regularly, is all that is required to implement a strategy based on incrementally updated backups.

Example 9-9 Basic Incremental Update Script

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

To understand the script and the strategy, you must understand the effects of these two commands when no data file copies or incremental backups exist. Note two important features:

- The `BACKUP` command in Example 9-9 does not always create a level 1 incremental backup.
- The [`RECOVER`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta2001.htm#RCMRF140) command in Example 9-9 causes RMAN to apply any available incremental level 1 backups with the specified tag to a set of data file copies with the same tag.

Table 9-2 shows the effect of the script when it is run once per day starting Monday.

Table 9-2 Effect of Basic Script When Run Daily

| Command | Monday | Tuesday | Wednesday | Thursday Onward |
| --- | --- | --- | --- | --- |
| `RECOVER` | Because no incremental backup or data file copy exists, the command generates a message (but not an error). That is, the command has no effect. | A database copy now exists, but no incremental level 1 backup exists with which to recover it. Thus, the `RECOVER` command has no effect. | The level 1 incremental backup made on Tuesday is applied to the database copy, bringing the copy up to the checkpoint SCN of the level 1 incremental backup. | The level 1 incremental backup made yesterday is applied to the database copy, bringing the copy up to the checkpoint SCN of the level 1 incremental backup. |
| `BACKUP` | No level 0 image copy exists, so the command creates an image copy of the database and applies the tag `incr_update`. This copy is needed to begin the cycle of incremental updates.  Note: If the script sets `DEVICE` `TYPE` `sbt`, then the first run creates the copy on disk, not on tape. Subsequent runs make level 1 backups on tape. | The command makes an incremental level 1 backup and assigns it the tag `incr_update`. This backup contains blocks that changed between Monday and Tuesday. | The command makes an incremental level 1 backup and assigns it the tag `incr_update`. This backup contains blocks that changed between Tuesday and Wednesday. | The command makes an incremental level 1 backup and assigns it the tag `incr_update`. This backup contains blocks that changed between now and the most recent backup with the tag `incr_update`. |

Note the following additional details about Example 9-9:

- Each time a data file is added to the database, an image copy of the new data file is created the next time the script runs. The next run makes the first level 1 incremental for the added data file. On all subsequent runs the new data file is processed like any other data file.
- You must use tags to identify the data file copies and incremental backups in this strategy so that they do not interfere with other backup strategies. If you use multiple incremental backup strategies, then RMAN cannot unambiguously create incremental level 1 backups unless you tag level 0 backups.
	The incremental level 1 backups to apply to those image copies are selected based upon the tag of the image copy datafiles and the available incremental level 1 backups. The tag is essential in the selection of the incremental level backups.
- After the third run of the script, the following files would be available for a point-in-time recovery:
	- An image copy of the database, as of the checkpoint SCN of the preceding run of the script, 24 hours earlier
		- An incremental backup for the changes after the checkpoint SCN of the preceding run
		- Archived redo logs including all changes between the checkpoint SCN of the image copy and the current time
	If you must restore and recover your database during the following 24 hours, then you can restore the data files from the incrementally updated data file copies. You can then apply changes from the most recent incremental level 1 and the redo logs to reach the desired SCN. At most, you have 24 hours of redo to apply, which limits how long point-in-time recovery takes to finish.

See Also:

[Oracle Database 2 Day DBA](https://docs.oracle.com/cd/E11882_01/server.112/e10897/backrest.htm#ADMQS009) to see how this technique is used in the Oracle backup strategy with Enterprise Manager

#### Incrementally Updated Backups: Advanced Example

You can extend the basic script in Example 9-9 to provide fast recoverability to a window greater than 24 hours. Example 9-10 shows how to maintain a window of seven days by specifying the beginning time of your window of recoverability in the `RECOVER` command.

Example 9-10 Advanced Incremental Update Script

```
RUN
{
  RECOVER COPY OF DATABASE 
    WITH TAG 'incr_update' 
    UNTIL TIME 'SYSDATE - 7';
  BACKUP
    INCREMENTAL LEVEL 1 
    FOR RECOVER OF COPY WITH TAG 'incr_update'
    DATABASE;
}
```

Table 9-3 shows the effect of the script when it is run once per day starting Monday, January 1.

Table 9-3 Effect of Advanced Script When Run Daily

| Command | Monday 1/1 | Tuesday 1/2 - Monday 1/8 | Tuesday 1/9 | Wednesday 1/10 Onward |
| --- | --- | --- | --- | --- |
| `RECOVER` | Because no incremental backup or data file copy exists, the command generates a message (but not an error). That is, the command has no effect. | A database copy exists, but `SYSDATE-7` specifies a time before the base copy was created. For example, on Wednesday `SYSDATE-7` specifies the Wednesday before Monday 1/1. Thus, the `RECOVER` command has no effect. | `SYSDATE-7` now specifies a date after the base copy was created. The database copy made on Monday 1/1 is updated with the incremental backup made on Tuesday 1/2, bringing the copy up to the checkpoint SCN of the level 1 incremental backup. | The database copy is updated with the incremental backup made 7 days ago, bringing the copy up to the checkpoint SCN of the level 1 incremental backup. |
| `BACKUP` | No level 0 image copy exists, so the command creates an image copy of the database and applies the tag `incr_update`. This copy is needed to begin the cycle of incremental updates.  Note: If the script sets `DEVICE` `TYPE` `sbt`, then the first run creates the copy on disk, not on tape. Subsequent runs make level 1 backups on tape. | The command makes an incremental level 1 backup and assigns it the tag `incr_update`. This backup contains blocks that changed between yesterday and today. | The command makes an incremental level 1 backup and assigns it the tag `incr_update`. This backup contains blocks that changed between Monday 1/8 and Tuesday 1/9. | The command makes an incremental level 1 backup and assigns it the tag `incr_update`. This backup contains blocks that changed between yesterday and today. |

As with the basic script in Example 9-9, you have fast recoverability to any point in time between the SCN of the data file copies and the present. RMAN can use both block changes from the incremental backups and individual changes from the redo logs. Because you have the daily level 1 incremental backups, you never need to apply more than 1 day of redo.

See Also:

[Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta2001.htm#RCMRF140) to learn about the `RECOVER` command

### Using Block Change Tracking to Improve Incremental Backup Performance

The [block change tracking](glossary.md) feature for incremental backups improves backup performance by recording changed blocks for each data file.

#### About Block Change Tracking

If block change tracking is enabled on a primary or standby database, then RMAN uses a [block change tracking file](glossary.md) to identify changed blocks for incremental backups. By reading this small bitmap file to determine which blocks changed, RMAN avoids having to scan every block in the data file that it is backing up.

Block change tracking is disabled by default. Nevertheless, the benefits of avoiding full data file scans during backup are considerable, especially if only a small percentage of data blocks are changed between backups. If your backup strategy involves incremental backups, then block change tracking is recommended. Block change tracking does not change the commands used to perform incremental backups. The change tracking file requires no maintenance after initial configuration.

You can only enable block change tracking at a physical standby database if a license for the Oracle Active Data Guard option is enabled.

##### Space Management in the Block Change Tracking File

The change tracking file maintains bitmaps that mark changes in the datafiles between backups. The database performs a bitmap switch before each backup. Oracle Database automatically manages space in the change tracking file to retain block change data that covers the eight most recent backups. After the maximum of eight bitmaps is reached, the oldest bitmap is overwritten by the bitmap that tracks the current changes.

The first level 0 incremental backup scans the entire data file. Subsequent incremental backups use the block change tracking file to scan only the blocks that have been marked as changed since the last backup. An incremental backup can be optimized only when it is based on a parent backup that was made after the start of the oldest bitmap in the block change tracking file.

Consider the eight-bitmap limit when developing your incremental backup strategy. For example, if you make a level 0 database backup followed by seven differential incremental backups, then the block change tracking file now includes eight bitmaps. If you then make a cumulative level 1 incremental backup, then RMAN cannot optimize the backup, because the bitmap corresponding to the parent level 0 backup is overwritten with the bitmap that tracks the current changes.

##### Location of the Block Change Tracking File

One block change tracking file is created for the whole database. By default, the change tracking file is created as an [Oracle managed file](glossary.md) in the destination specified by the [`DB_CREATE_FILE_DEST`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams053.htm#REFRN10034) initialization parameter. You can also place the change tracking file in any location that you choose, by specifying its name when enabling block change tracking. Oracle recommends against using a raw device (that is, a disk without a file system) as a change tracking file.

Note:

In an Oracle RAC environment, the change tracking file must be located on shared storage accessible from all nodes in the cluster.

RMAN does not support backup and recovery of the change tracking file. The database resets the change tracking file when it determines that the change tracking file is invalid. If you restore and recover the whole database or a subset, then the database resets the block change tracking file and starts tracking changes again. After you make a level 0 incremental backup, the next incremental backup can use change tracking data.

##### Size of the Block Change Tracking File

The size of the block change tracking file is proportional to the size of the database and the number of enabled threads of redo. The size of the block change tracking file can increase and decrease as the database changes. The size is not related to the frequency of updates to the database.

Typically, the space required for block change tracking for a single instance is approximately 1/30,000 the size of the data blocks to be tracked. For an Oracle RAC environment, it is 1/30,000 of the size of the database, times the number of enabled threads.

The following factors that may cause the file to be larger than this estimate suggests:

- To avoid the overhead of allocating space as your database grows, the block change tracking file size starts at 10 megabytes. New space is allocated in 10 MB increments. Thus, for any database up to approximately 300 gigabytes, the file size is no smaller than 10 MB, for up to approximately 600 gigabytes the file size is no smaller than 20 megabytes, and so on.
- For each data file, a minimum of 320 kilobytes of space is allocated in the block change tracking file, regardless of the size of the data file. Thus, if you have a large number of relatively small data files, the change tracking file is larger than for databases with a smaller number of larger data files containing the same data.

#### Enabling and Disabling Block Change Tracking

You can enable block change tracking when the database is either open or mounted. This section assumes that you intend to create the block change tracking file as an Oracle Managed File in the [database area](glossary.md), which is where the database maintains active database files such as data files, control files, and online redo log files. See ["Overview of the Fast Recovery Area"](rcmconfb.md) to learn about the database area and [fast recovery area](glossary.md).

To enable block change tracking:

1. Start SQL\*Plus and connect to a target database with administrator privileges.
2. Ensure that the `DB_CREATE_FILE_DEST` initialization parameter is set.
	```
	SHOW PARAMETER DB_CREATE_FILE_DEST
	```
	If the parameter is not set, and if the database is open, then you can set the parameter with the following form of the [`ALTER SYSTEM`](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_2014.htm#SQLRF00902) statement:
	```
	ALTER SYSTEM SET 
	  DB_CREATE_FILE_DEST = '/disk1/bct/'
	  SCOPE=BOTH SID='*';
	```
3. Enable block change tracking.
	Execute the following `ALTER DATABASE` statement:
	```
	ALTER DATABASE ENABLE BLOCK CHANGE TRACKING;
	```
	You can also create the change tracking file in a location that you choose yourself by using the following form of SQL statement:
	```
	ALTER DATABASE ENABLE BLOCK CHANGE TRACKING 
	  USING FILE '/mydir/rman_change_track.f' REUSE;
	```
	The `REUSE` option tells Oracle Database to overwrite any existing block change tracking file with the specified name.

#### Disabling Block Change Tracking

This section assumes that the block change tracking feature is currently enabled. When you disable block change tracking, the database removes the block change tracking file from the operating system.

To disable block change tracking:

1. Start SQL\*Plus and connect to a target database with administrator privileges.
2. Ensure that the target database is mounted or open.
3. Disable block change tracking.
	Execute the following `ALTER DATABASE` statement:
	```
	ALTER DATABASE DISABLE BLOCK CHANGE TRACKING;
	```

#### Checking Whether Change Tracking is Enabled

You can query the [`V$BLOCK_CHANGE_TRACKING`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1070.htm#REFRN30030) view to determine whether change tracking is enabled, and if it is, the file name of the block change tracking file.

To determine whether change tracking is enabled:

Enter the following query in SQL\*Plus (sample output included):

```
COL STATUS   FORMAT A8
COL FILENAME FORMAT A60
 
SELECT STATUS, FILENAME
FROM   V$BLOCK_CHANGE_TRACKING;

STATUS   FILENAME
-------- ------------------------------------------------------------
ENABLED  /disk1/bct/RDBMS/changetracking/o1_mf_2f71np5j_.chg
```

#### Changing the Location of the Block Change Tracking File

To move the change tracking file, use the [`ALTER DATABASE RENAME FILE`](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_1004.htm#SQLRF00802) statement. The database must be mounted. The statement updates the control file to refer to the new location and preserves the contents of the change tracking file. If you cannot shut down the database, then you can disable and enable block change tracking. In this case, you lose the contents of the existing block change tracking file.

To change the location of the change tracking file:

1. Start SQL\*Plus and connect to a target database.
2. If necessary, determine the current name of the change tracking file:
	```
	SQL> SELECT FILENAME FROM V$BLOCK_CHANGE_TRACKING;
	```
3. If possible, shut down the database. For example:
	```
	SQL> SHUTDOWN IMMEDIATE
	```
	If you shut down the database, then skip to the next step. If you choose not to shut down the database, then execute the following SQL statements and skip all remaining steps:
	```
	SQL> ALTER DATABASE DISABLE BLOCK CHANGE TRACKING;
	SQL> ALTER DATABASE ENABLE BLOCK CHANGE TRACKING USING FILE 'new_location';
	```
	In this case you lose the contents of the block change tracking file. Until the next time you complete a level 0 incremental backup, RMAN must scan the entire file.
4. Using host operating system commands, move the change tracking file to its new location.
5. Mount the database and move the change tracking file to a location that has more space. For example:
	```
	ALTER DATABASE RENAME FILE
	   '/disk1/bct/RDBMS/changetracking/o1_mf_2f71np5j_.chg' TO 
	   '/disk2/bct/RDBMS/changetracking/o1_mf_2f71np5j_.chg';
	```
	This statement changes the location of the change tracking file while preserving its contents.
6. Open the database:
	```
	SQL> ALTER DATABASE OPEN;
	```

See Also:

[Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/toc.htm) to learn about the [`ALTER DATABASE`](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_1004.htm#SQLRF00802) statement and the [`ALTER SYSTEM`](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_2014.htm#SQLRF00902) statement

## Making Database Backups for Long-Term Storage

This section explains the basic concepts and tasks involved in making backups for long-term storage.

### Purpose of Archival Backups

You can use [`BACKUP`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta007.htm#RCMRF107) `... KEEP` to create a backup that is both all-inclusive and exempt from the [backup retention policy](glossary.md). The backup is all-inclusive because every file needed to restore and recover the database is backed up to a single disk or tape location. The `KEEP` option also specifies that the backup should be exempt from the retention policy either forever or for a specified period of time. The general name for a backup created with `BACKUP ... KEEP` is an [archival backup](glossary.md).

As explained in ["Data Preservation"](rcmintro.md), one purpose of a backup and recovery strategy is to preserve data. You can use `BACKUP ... KEEP` to retain a database backup for longer than the time dictated by the retention policy. For example, you can back up the database on the first day of every year to satisfy a regulatory requirement and store the media offsite. Years after you make the archival backup, you could restore and recover it to query the data as it appeared at the time of the backup.

Another purpose of an archival backup is to create a backup to restore for testing purposes and then delete. For example, you can back up the database, restore the database in a test environment, and then discard the archival backup after the test database is operational. A related purpose is to create a self-contained backup that you can delete after transferring it to another user or host. For example, another user might want a copy of the database for reporting or testing.

### Basic Concepts of Archival Backups

You can exempt a backup from the retention policy by using the `KEEP` option with the `BACKUP` command. You can also use the `KEEP` and `NOKEEP` options of the [`CHANGE`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta009.htm#RCMRF110) command to change the status of an existing backup. Backups with `KEEP` attributes are valid backups that can be recovered like any other backups.

You can specify an end date for an archival backup with the [`KEEP UNTIL TIME`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsubcl019.htm#RCMRF160) clause, or specify that the backup should be kept `FOREVER`. If you specify `UNTIL`, then RMAN marks the backup as obsolete when the `UNTIL` time has passed, regardless of any configured retention policy. For example, if you specify `KEEP UNTIL TIME '01-JAN-08'`, then the backup is obsolete one second after midnight on January 1. If you specify an `UNTIL TIME` of 9:00 p.m, then the backup is obsolete at 9:01 p.m.

When you specify `KEEP` on the `BACKUP` command, RMAN generates multiple backup sets. Note the following characteristics of the `BACKUP ... KEEP` command:

- It automatically backs up the data files, control file (even if the [control file autobackup](glossary.md) is disabled), and the server parameter file.
- It automatically generates an archived redo log backup to ensure that the database backup can be recovered to a consistent state.
- If the `FORMAT`, `POOL`, or `TAG` parameters are specified, then they are used for all backups. For this reason, the `FORMAT` string must allow for the creation of multiple backup pieces. Specifying the `%U` substitution variable is the easiest way to meet this requirement.
- It supports an optional `RESTORE POINT` clause that creates a [normal restore point](glossary.md), which is a label for an SCN to which the backup must be recovered to be made consistent. The SCN is captured just after the data file backups complete. RMAN resynchronizes restore points with the [recovery catalog](glossary.md) and maintains the restore points as long as the backup exists. ["Listing Restore Points"](flashdb.md) explains how to display restore points.

See Also:

[Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta009.htm#RCMRF110) for `CHANGE` syntax and [Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta007.htm#RCMRF107) for `BACKUP ... KEEP` syntax

### Making an Archival Backup for Long-Term Storage

Typically, you make an archival backup to tape. Because your data protection backups are most likely to be on a set of tapes that remain accessible and are recycled, it is advisable to earmark a set of tapes for the archival backup. You can write the archival backup to this special set of tapes and then place them in offsite storage.

You can vary the procedure for creating an archival backup by creating a [stored script](glossary.md) or shell script that updates dynamically. When you run the script, you can dynamically set the name of the restore point, backup format, and so on.

See Also:

- ["Backup-Based Duplication Without a Target Connection: Example"](rcmdupdb.md) to learn the recommended technique for restoring an archival backup
- ["Using Substitution Variables in Command Files"](rcmcnctg.md) and ["Creating and Executing Dynamic Stored Scripts"](rcmcatdb.md) to learn how to make archival backups with RMAN command files.

#### Making an Archival Backup

This scenario makes a long-term archival backup with a backup [tag](glossary.md) of `QUARTERLY` and assigns it to a special family of Oracle Secure Backup tapes reserved for long-term storage. Note the following features of this example:

- The `FOREVER` keyword indicates that this backup is never eligible for deletion by the [backup retention policy](glossary.md).
- The [`BACKUP`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta007.htm#RCMRF107) command creates the restore point named `FY06Q4` to match the SCN at which point this backup is consistent.

To make a long-term archival backup:

1. Start RMAN and connect to a target database and recovery catalog.
	The target database can be open or mounted. A recovery catalog is required for `KEEP FOREVER`, but is not required for any other `KEEP` option.
2. Run `BACKUP ... KEEP` to make the backup.
	The following example generates a data file and archived log backup and creates a [normal restore point](glossary.md). The specified restore point must not already exist.
	The log backup contains just those archived logs needed to restore this backup to a consistent state. The database performs a online redo log switch to archive the redo that is in the current online logs and is necessary to make this new backup consistent. The control file autobackup has a copy of the restore point, so it can be referenced as soon as the control file is restored.
	```
	RUN
	{
	  ALLOCATE CHANNEL c1 
	    DEVICE TYPE sbt
	    PARMS 'ENV=(OB_MEDIA_FAMILY=archival_backup)';
	  BACKUP DATABASE
	    TAG quarterly
	    KEEP FOREVER
	    RESTORE POINT FY06Q4;
	}
	```
	The following variation keeps the backup for 365 days instead of keeping it forever. After a year has passed, the backup becomes obsolete regardless of the backup retention policy settings.
	```
	RUN
	{
	  ALLOCATE CHANNEL c1 DEVICE TYPE sbt
	    PARMS 'ENV=(OB_MEDIA_FAMILY=archival_backup)';
	  BACKUP DATABASE
	    TAG quarterly
	    KEEP UNTIL TIME 'SYSDATE+365'
	    RESTORE POINT FY06Q4;
	}
	```

See Also:

["Understanding Flashback Database, Restore Points and Guaranteed Restore Points"](flashdb.md) to learn about restore points

### Making a Temporary Archival Backup

One purpose of an archival backup is for creating a test database. The technique for making a test database is essentially the same as the technique described in "Making an Archival Backup for Long-Term Storage". The difference is that you intend to delete the backup soon after creating it.

You can specify the temporary status of the backup with the `BACKUP ... KEEP UNTIL` parameter. Assume that you want to make a backup and then restore it to a new host the same day. In this case, you can specify `KEEP UNTIL` `TIME SYSDATE+1` to indicate that RMAN should override the retention policy for this backup for only one day. After one day, the backup becomes obsolete, regardless of any configured backup retention policy.

The command in Example 9-11 makes an archival backup on a temporary disk with the tag `TESTDB`. The example creates a normal restore point, which is a label for the time to which the backup should be recovered. RMAN only backs up the archived redo logs if the database is open during the backup. Archived logs are not needed for offline backups and so are not backed up.

Example 9-11 Creating a Temporary Archival Backup

```
BACKUP DATABASE
  FORMAT '/disk1/oraclebck/%U' 
  TAG TESTDB 
  KEEP UNTIL TIME 'SYSDATE+1' 
  RESTORE POINT TESTDB06;
```

The recommended technique for restoring an archival backup is to use the [`DUPLICATE`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta020.htm#RCMRF126) command. Refer to ["Backup-Based Duplication Without a Target Connection: Example"](rcmdupdb.md).

## Backing Up RMAN Backups

This section explains how to back up backup sets and image copies.

### About Backups of Backups

You can use the [`BACKUP BACKUPSET`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta007.htm#RCMRF107) command to back up backup sets produced by other backup jobs. You can also use `BACKUP RECOVERY AREA` to back up recovery files created in the current and all previous [fast recovery area](glossary.md) destinations. Recovery files are full and incremental backup sets, control file autobackups, data file copies, and archived redo logs. SBT and disk backups are supported for `BACKUP RECOVERY AREA`. For disk backups of the recovery files, you must use the `TO DESTINATION` option.

The preceding commands are especially useful in the following scenarios:

- Ensuring that all backups exist both on disk and on tape.
- Moving backups from disk to tape and then freeing space on disk. This task is especially important when the database uses a fast recovery area so that the space can be reused as needed.

You can also use the `BACKUP` `COPY` `OF` command to back up image copies of datafiles, control files, and archived redo logs. The output of this command can be either backup sets or image copies, so you can generate backup sets from image copies. This form of backup is used to back up a database backup created as image copies on disk to tape.

#### Multiple Copies of Backup Sets

`BACKUP` `BACKUPSET` creates additional copies of backup pieces in a backup set, but does not create a new backup set. Thus, `BACKUP` `BACKUPSET` is similar to using the `DUPLEX` or `MAXCOPIES` option of `BACKUP` (see ["Duplexing Backup Sets"](rcmbckad.md)). The extra copy of a backup set created by `BACKUP` `BACKUPSET` is not a new backup set, just as copies of a backup set produced by other forms of the `BACKUP` command are not separate backup sets.

#### Effect of a Backup Retention Policy on Backups of Backups

For a backup [retention policy](glossary.md) based on [redundancy](glossary.md), a backup set is counted as one instance of a backup. This statement is true even if there are multiple copies of the backup pieces that form the backup set, such as when a backup set has been backed up from disk to tape.

For a recovery window retention policy, either all of the copies of a backup set are obsolete, or none of them are. This point is easiest to grasp when viewing the output of the [`LIST`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta027.htm#RCMRF132) and [`REPORT`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta2006.htm#RCMRF147) commands.

To view the effect of a backup retention policy on backups of backups:

1. Back up a data file.
	The following example backs up data file `5`:
	```
	BACKUP AS BACKUPSET DATAFILE 5;
	```
2. Run the `LIST` command for the data file backup from Step 1.
	For example, run the following command (sample output included).
	```
	LIST BACKUP OF DATAFILE 5 SUMMARY;
	 
	List of Backups
	===============
	Key     TY LV S Device Type Completion Time #Pieces #Copies Compressed Tag
	------- -- -- - ----------- --------------- ------- ------- ---------- ---
	18      B  F  A DISK        04-AUG-07       1       1       NO         TAG20070804T160 134
	```
3. Use the backup set key from the previous step to back up the backup set.
	For example, enter the following command:
	```
	BACKUP BACKUPSET 18;
	```
4. Run the same `LIST` command that you ran in Step 2.
	For example, run the following command (sample output included).
	```
	LIST BACKUP OF DATAFILE 5 SUMMARY;
	 
	List of Backups
	===============
	Key     TY LV S Device Type Completion Time #Pieces #Copies Compressed Tag
	------- -- -- - ----------- --------------- ------- ------- ---------- ---
	18      B  F  A DISK        04-AUG-07       1       2       NO         TAG20070804T160 134
	```
	Only one backup set is shown in this output, but there are now two copies of it.
5. Generate a report to see the effect of these copies under a redundancy-based backup retention policy.
	For example, issue the following command:
	```
	REPORT OBSOLETE REDUNDANCY 1;
	```
	None of the copies is reported as obsolete because both copies of the backup set have the same values for `set_stamp` and `set_count`.
6. Generate a report to see the effect of these copies under a recovery window-based backup retention policy.
	For example, issue the following command:
	```
	REPORT OBSOLETE RECOVERY WINDOW 1 DAY;
	```
	None of the copies of the backup set is reported as obsolete or based on the `CHECKPOINT_CHANGE#` of this backup set, for the current time and the availability of other backups.
	See Also:
	- ["Configuring a Redundancy-Based Retention Policy"](rcmconfb.md)
	- [Chapter 11, "Reporting on RMAN Operations"](rcmreprt.md) to learn how to use the `LIST` and `REPORT` commands

### Backing Up Backup Sets with RMAN

This section explains how to use the `BACKUP BACKUPSET` command to copy backup sets from disk to tape. The procedure assumes that you have configured an [SBT](glossary.md) device as your default device.

To back up backup sets from disk to tape:

1. If you are backing up a subset of available backup sets, then execute the `LIST BACKUPSET` command to obtain their primary keys.
	The following example lists the backup sets in summary form:
	```
	RMAN> LIST BACKUPSET SUMMARY;
	List of Backups
	===============
	Key TY LV S Device Type Completion Time #Pieces #Copies Comp Tag
	--- -- -- - ----------- --------------- ------- ------- ---- ---
	1   B  F  A DISK        28-MAY-07       1       1       NO   TAG20070528T132432
	2   B  F  A DISK        29-MAY-07       1       1       NO   TAG20070529T132433
	3   B  F  A DISK        30-MAY-07       1       1       NO   TAG20070530T132434
	```
	The following example lists details about backup set 3:
	```
	RMAN> LIST BACKUPSET 3;
	List of Backup Sets
	===================
	BS Key  Type LV Size       Device Type Elapsed Time Completion Time
	------- ---- -- ---------- ----------- ------------ ---------------
	3       Full    8.33M      DISK        00:00:01     30-MAY-07
	        BP Key: 3   Status: AVAILABLE  Compressed: NO  Tag: TAG20070530T132434
	        Piece Name: /disk1/oracle/dbs/c-35764265-20070530-02
	  Control File Included: Ckp SCN: 397221       Ckp time: 30-MAY-07
	  SPFILE Included: Modification time: 30-MAY-07
	  SPFILE db_unique_name: PROD
	```
2. Execute the `BACKUP` `BACKUPSET` command.
	The following example backs up all disk backup sets to tape and then deletes the input disk backups:
	```
	BACKUP BACKUPSET ALL
	  DELETE INPUT;
	```
	The following example backs up only the backup sets with the primary key 1 and 2 to tape and then deletes the input disk backups:
	```
	BACKUP BACKUPSET 1,2
	  DELETE INPUT;
	```
3. Optionally, execute the [`LIST`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta027.htm#RCMRF132) command to see a listing of backup sets and pieces.
	The output lists all copies, including backup piece copies created by `BACKUP` `BACKUPSET`.

### Backing Up Image Copy Backups with RMAN

This section explains how to use the `BACKUP` command to back up image copies to tape. It is assumed that you have configured an [SBT](glossary.md) device as your default device.

When backing up image copies that have multiple copies of the datafiles, specifying tags for the backups makes it easier to identify the input image copy. All image copies of datafiles have tags. The tag of an image copy is inherited by default when the image copy is backed up as a new image copy.

To back up image copies from disk to tape:

1. Issue the `BACKUP` `... COPY OF` or `BACKUP DATAFILECOPY` command.
	The following example backs up data file copies that have the tag `DBCopy`:
	```
	BACKUP DATAFILE COPY FROM TAG monDBCopy;
	```
	The following example backs up the latest image copies of a database to tape, assigns the tag `QUARTERLY_BACKUP`, and deletes the input disk backups:
	```
	BACKUP DEVICE TYPE sbt
	  TAG "quarterly_backup"
	  COPY OF DATABASE 
	  DELETE INPUT;
	```
2. Optionally, issue the [`LIST`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta027.htm#RCMRF132) command to see a listing of backup sets. The output lists all copies, including backup piece copies created by the `BACKUP` `BACKUPSET` command.