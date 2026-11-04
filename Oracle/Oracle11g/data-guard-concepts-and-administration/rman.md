---
title: Using RMAN to Back Up and Restore Files
book: Data Guard Concepts and Administration
doc_id: E41134-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e41134/rman.htm
tags:
  - oracle
  - 11g
  - data-guard-concepts-and-administration
---

## 11 Using RMAN to Back Up and Restore Files

This chapter describes backup strategies using Oracle Recovery Manager (RMAN) with Data Guard and standby databases. RMAN can perform backups with minimal effect on the primary database and quickly recover from the loss of individual datafiles, or the entire database. RMAN and Data Guard can be used together to simplify the administration of a Data Guard configuration.

This chapter contains the following topics:

Note:

Because a logical standby database is not a block-for-block copy of the primary database, you cannot use a logical standby database to back up the primary database.

See Also:

- [Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/cd/E11882_01/backup.112/e10642/toc.htm) for more information about RMAN concepts and about using RMAN in a Data Guard environment
- [Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/toc.htm) for detailed information about all RMAN commands used in this chapter

## 11.1 About RMAN File Management in a Data Guard Configuration

RMAN uses a recovery catalog to track filenames for all database files in a Data Guard environment. A recovery catalog is a database schema used by RMAN to store metadata about one or more Oracle databases. The catalog also records where the online redo logs, standby redo logs, tempfiles, archived redo logs, backup sets, and image copies are created.

### 11.1.1 Interchangeability of Backups in a Data Guard Environment

RMAN commands use the recovery catalog metadata to behave transparently across different physical databases in the Data Guard environment. For example, you can back up a tablespace on a physical standby database and restore and recover it on the primary database. Similarly, you can back up a tablespace on a primary database and restore and recover it on a physical standby database.

Note:

Backups of logical standby databases are not usable at the primary database.

Backups of standby control files and nonstandby control files are interchangeable. For example, you can restore a standby control file on a primary database and a primary control file on a physical standby database. This interchangeability means that you can offload control file backups to one database in a Data Guard environment. RMAN automatically updates the filenames for database files during restore and recovery at the databases.

### 11.1.2 Association of Backups in a Data Guard Environment

The recovery catalog tracks the files in the Data Guard environment by associating every database file or backup file with a `DB_UNIQUE_NAME`. The database that creates a file is associated with the file. For example, if RMAN backs up the database with the unique name of `standby1`, then `standby1` is associated with this backup. A backup remains associated with the database that created it unless you use the `CHANGE` `... RESET DB_UNIQUE_NAME` to associate the backup with a different database.

### 11.1.3 Accessibility of Backups in a Data Guard Environment

The accessibility of a backup is different from its association. In a Data Guard environment, the recovery catalog considers disk backups as accessible only to the database with which it is associated, whereas tape backups created on one database are accessible to all databases. If a backup file is not associated with any database, then the row describing it in the recovery catalog view shows `null` for the `SITE_KEY` column. By default, RMAN associates files whose `SITE_KEY` is `null` with the target database.

RMAN commands such as `BACKUP`, `RESTORE`, and `CROSSCHECK` work on any accessible backup. For example, for a `RECOVER COPY` operation, RMAN considers only image copies that are associated with the database as eligible to be recovered. RMAN considers the incremental backups on disk and tape as eligible to recover the image copies. In a database recovery, RMAN considers only the disk backups associated with the database and all files on tape as eligible to be restored.

To illustrate the differences in backup accessibility, assume that databases `prod` and `standby1` reside on different hosts. RMAN backs up datafile 1 on `prod` to `/prmhost/disk1/df1.dbf` on the production host and also to tape. RMAN backs up datafile 1 on `standby1` to `/sbyhost/disk2/df1.dbf` on the standby host and also to tape. If RMAN is connected to database `prod`, then you cannot use RMAN commands to perform operations with the `/sbyhost/disk2/df1.dbf` backup located on the standby host. However, RMAN does consider the tape backup made on `standby1` as eligible to be restored.

Note:

You can FTP a backup from a standby host to a primary host or vice versa, connect as `TARGET` to the database on this host, and then [`CATALOG`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta008.htm#RCMRF109) the backup. After a file is cataloged by the target database, the file is associated with the target database.

## 11.2 About RMAN Configuration in a Data Guard Environment

In a Data Guard configuration, the process of backing up control files, datafiles, and archived logs can be offloaded to the standby system, thereby minimizing the effect of backups on the production system. These backups can be used to recover the primary or standby database.

RMAN uses the `DB_UNIQUE_NAME` initialization parameter to distinguish one database site from another database site. Thus, it is critical that the uniqueness of `DB_UNIQUE_NAME` be maintained in a Data Guard configuration.

Only the primary database must be explicitly registered using the RMAN `REGISTER DATABASE` command. You do this after connecting RMAN to the recovery catalog and primary database as target.

Use the RMAN `CONFIGURE` command to set the RMAN configurations. When the `CONFIGURE` command is used with the `FOR DB_UNIQUE_NAME` option, it sets the RMAN site-specific configuration for the database with the DB\_UNIQUE\_NAME you specify.

For example, after connecting to the recovery catalog, you could use the following commands at an RMAN prompt to set the default device type to `SBT` for the `BOSTON` database that has a DBID of 1625818158. The RMAN `SET DBID` command is required only if you are not connected to a database as target.

```
SET DBID 1625818158;
CONFIGURE DEFAULT DEVICE TYPE TO SBT FOR DB_UNIQUE_NAME BOSTON;
```

## 11.3 Recommended RMAN and Oracle Database Configurations

This section describes the following RMAN and Oracle Database configurations, each of which can simplify backup and recovery operations:

- Oracle Database Configurations on Primary and Standby Databases
- RMAN Configurations at the Primary Database
- RMAN Configurations at a Standby Database Where Backups are Performed
- RMAN Configurations at a Standby Where Backups Are Not Performed

Configuration Assumptions

The configurations described in this section make the following assumptions:

- The standby database is a physical standby database, and backups are taken only on the standby database. See Section 11.9.1 for procedural changes if backups are taken on both primary and standby databases.
- An RMAN recovery catalog is required so that backups taken on one database server can be restored to another database server. It is not sufficient to use only the control file as the RMAN repository because the primary database will have no knowledge of backups taken on the standby database.
	The RMAN recovery catalog organizes backup histories and other recovery-related metadata in a centralized location. The recovery catalog is configured in a database and maintains backup metadata. A recovery catalog does not have the space limitations of the control file and can store more historical data about backups.
	A catalog server, physically separate from the primary and standby sites, is recommended in a Data Guard configuration because a disaster at either site will not affect the ability to recover the latest backups.
	See Also:
	[Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/cd/E11882_01/backup.112/e10642/rcmcatdb.htm#BRADV8015) for more information about managing a recovery catalog
- All databases in the configuration use Oracle Database 11g Release 1 (11.1).
- Oracle Secure Backup software or 3rd-party media management software is configured with RMAN to make backups to tape.

### 11.3.1 Oracle Database Configurations on Primary and Standby Databases

The following Oracle Database configurations are recommended on every primary and standby database in the Data Guard environment:

- Configure a fast recovery area for each database (the recovery area is local to a database).
	The fast recovery area is a single storage location on a file system or Oracle Automatic Storage Management (Oracle ASM) disk group where all files needed for recovery reside. These files include the control file, archived logs, online redo logs, flashback logs, and RMAN backups. As new backups and archived logs are created in the fast recovery area, older files (which are either outside of the retention period, or have been backed up to tertiary storage) are automatically deleted to make room for them. In addition, notifications can be set up to alert the DBA when space consumption in the fast recovery area is nearing its predefined limit. The DBA can then take action, such as increasing the recovery area space limit, adding disk hardware, or decreasing the retention period.
	Set the following initialization parameters to configure the fast recovery area:
	```
	DB_RECOVERY_FILE_DEST = <mount point or Oracle ASM Disk Group>
	DB_RECOVERY_FILE_DEST_SIZE = <disk space quota>
	```
	See Also:
	[Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/cd/E11882_01/backup.112/e10642/rcmconfb.htm#BRADV8183) for more information about configuring a fast recovery area
- Use a server parameter file (SPFILE) so that it can be backed up to save instance parameters in backups.
- Enable Flashback Database on primary and standby databases.
	When Flashback Database is enabled, Oracle Database maintains flashback logs in the fast recovery area. These logs can be used to roll the database back to an earlier point in time, without requiring a complete restore.
	See Also:
	[Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/cd/E11882_01/backup.112/e10642/flashdb.htm#BRADV595) for more information about enabling Flashback Database

### 11.3.2 RMAN Configurations at the Primary Database

To simplify ongoing use of RMAN, you can set a number of persistent configuration settings for each database in the Data Guard environment. These settings control many aspects of RMAN behavior. For example, you can configure the backup retention policy, default destinations for backups to tape or disk, default backup device type, and so on. You can use the `CONFIGURE` command to set and change RMAN configurations. The following RMAN configurations are recommended at the primary database:

1. Connect RMAN to the primary database and recovery catalog.
2. Configure the retention policy for the database as `n` days:
	```
	CONFIGURE RETENTION POLICY TO RECOVERY WINDOW OF <n> DAYS;
	```
	This configuration lets you keep the backups necessary to perform database recovery to any point in time within the specified number of days.
	Use the `DELETE` `OBSOLETE` command to delete any backups that are not required (per the retention policy in place) to perform recovery within the specified number of days.
3. Specify when archived logs can be deleted with the `CONFIGURE ARCHIVELOG DELETION POLICY` command. For example, if you want to delete logs after ensuring that they shipped to all destinations, use the following configuration:
	```
	CONFIGURE ARCHIVELOG DELETION POLICY TO SHIPPED TO ALL STANDBY;
	```
	If you want to delete logs after ensuring that they were applied on all standby destinations, use the following configuration:
	```
	CONFIGURE ARCHIVELOG DELETION POLICY TO APPLIED ON ALL STANDBY;
	```
4. Configure the connect string for the primary database and all standby databases, so that RMAN can connect remotely and perform resynchronization when the `RESYNC CATALOG FROM DB_UNIQUE_NAME` command is used. When you connect to the target instance, you must provide a net service name. This requirement applies even if the other database instance from where the resynchronization is done is on the local host. The target and remote instances must use the same `SYSDBA` password, which means that both instances must already have password files. You can create the password file with a single password so you can start all the database instances with that password file. For example, if the TNS alias to connect to a standby in Boston is `boston_conn_str`, you can use the following command to configure the connect identifier for the `BOSTON` database site:
	```
	CONFIGURE DB_UNIQUE_NAME BOSTON CONNECT IDENTIFIER 'boston_conn_str';
	```
	Note that the `'boston_conn_str'` does not include a username and password. It contains only the Oracle Net service name that can be used from any database site to connect to the `BOSTON` database site.
	After connect identifiers are configured for all standby databases, you can verify the list of standbys by using the `LIST DB_UNIQUE_NAME OF DATABASE` command.

See Also:

- [Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/cd/E11882_01/backup.112/e10642/rcmconfa.htm#BRADV006) for more information about RMAN configurations
- [Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta010.htm#RCMRF113) for more information about the RMAN `CONFIGURE` command

### 11.3.3 RMAN Configurations at a Standby Database Where Backups are Performed

The following RMAN configurations are recommended at a standby database where backups are done:

1. Connect RMAN to the standby database (where backups are performed) as target, and to the recovery catalog.
2. Enable automatic backup of the control file and the server parameter file:
	```
	CONFIGURE CONTROLFILE AUTOBACKUP ON;
	```
3. Skip backing up datafiles for which there already exists a valid backup with the same checkpoint:
	```
	CONFIGURE BACKUP OPTIMIZATION ON;
	```
4. Configure the tape channels to create backups as required by media management software:
	```
	CONFIGURE CHANNEL DEVICE TYPE SBT PARMS '<channel parameters>';
	```
5. Specify when the archived logs can be deleted with the `CONFIGURE ARCHIVELOG DELETION POLICY` command.
	Because the logs are backed up at the standby site, it is recommended that you configure the `BACKED UP` option for the log deletion policy.

See Also:

[Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/cd/E11882_01/backup.112/e10642/rcmconfb.htm#BRADV89439) for more information about enabling deletion policies for archived redo logs

### 11.3.4 RMAN Configurations at a Standby Where Backups Are Not Performed

The following RMAN configurations are recommended at a standby database where backups are not done:

1. Connect RMAN to the standby database as target, and to the recovery catalog.
2. Enable automatic deletion of archived logs once they are applied at the standby database:
	```
	CONFIGURE ARCHIVELOG DELETION POLICY TO APPLIED ON ALL STANDBY;
	```

## 11.4 Backup Procedures

This section describes the RMAN scripts and procedures used to back up Oracle Database in a Data Guard configuration. The following topics are covered:

- Using Disk as Cache for Tape Backups
- Performing Backups Directly to Tape

Note:

Oracle's Maximum Availability Architecture (MAA) best practices recommend that backups be taken at both the primary and the standby databases to reduce MTTR, in case of double outages and to avoid introducing new site practices upon switchover and failover.

Backups of Server Parameter Files

Prior to Oracle Database 11g, backups of server parameter files (SPFILEs) were assumed to be usable at any other standby database. However, in practice, it is not possible for all standby databases to use the same SPFILE. To address this problem, RMAN does not allow an SPFILE backup taken at one database site to be used at another database site. This restriction is in place only when the `COMPATIBLE` initialization parameter is set to 11.0.0.

The standby database allows you to offload all backup operations to one specific standby database, except the backups of SPFILE. However, if the `COMPATIBLE` initialization parameter is set to 11.0.0, the SPFILE can be backed up to disk and cataloged manually at standby sites where backups are written to tape. The additional metadata stored in SPFILE backup sets enables RMAN to identify which database SPFILE is contained in which backup set. Thus, the appropriate SPFILE backup is chosen during restore from tape.

### 11.4.1 Using Disk as Cache for Tape Backups

The fast recovery area on the standby database can serve as a disk cache for tape backup. Disk is used as the primary storage for backups, with tape providing long term, archival storage. Incremental tape backups are taken daily and full tape backups are taken weekly. The commands used to perform these backups are described in the following sections.

#### 11.4.1.1 Commands for Daily Tape Backups Using Disk as Cache

When deciding on your backup strategy, Oracle recommends that you take advantage of daily incremental backups. Datafile image copies can be rolled forward with the latest incremental backups, thereby providing up-to-date datafile image copies at all times. RMAN uses the resulting image copy for media recovery just as it would use a full image copy taken at that system change number (SCN), without the overhead of performing a full image copy of the database every day. An additional advantage is that the time-to-recover is reduced because the image copy is updated with the latest block changes and fewer redo logs are required to bring the database back to the current state.

To implement daily incremental backups, a full database backup is taken on the first day, followed by an incremental backup on day two. Archived redo logs can be used to recover the database to any point in either day. For day three and onward, the previous day's incremental backup is merged with the datafile copy and a current incremental backup is taken, allowing fast recovery to any point within the last day. Redo logs can be used to recover the database to any point during the current day.

The script to perform daily backups looks as follows (the last line, `DELETE ARCHIVELOG ALL` is only needed if the fast recovery area is not used to store logs):

```
RESYNC CATALOG FROM DB_UNIQUE_NAME ALL;
RECOVER COPY OF DATABASE WITH TAG 'OSS';
BACKUP DEVICE TYPE DISK INCREMENTAL LEVEL 1 FOR RECOVER OF COPY WITH TAG 'OSS' DATABASE;
BACKUP DEVICE TYPE SBT ARCHIVELOG ALL;
BACKUP BACKUPSET ALL;
DELETE ARCHIVELOG ALL;
```

The standby control file will be automatically backed up at the conclusion of the backup operation because the control file auto backup is enabled.

Explanations for what each command in the script does are as follows:

- `RESYNC CATALOG FROM DB_UNIQUE_NAME ALL`
	Resynchronizes the information from all other database sites (primary and other standby databases) in the Data Guard setup that are known to recovery catalog. For `RESYNC CATALOG FROM DB_UNIQUE_NAME` to work, RMAN should be connected to the target using the Oracle Net service name and all databases must use the same password file.
- `RECOVER COPY OF DATABASE WITH TAG 'OSS'`
	Rolls forward level 0 copy of the database by applying the level 1 incremental backup taken the day before. In the example script just shown, the previous day's incremental level 1 was tagged `OSS`. This incremental is generated by the `BACKUP DEVICE TYPE DISK ... DATABASE` command. On the first day this command is run there will be no roll forward because there is no incremental level 1 yet. A level 0 incremental will be created by the `BACKUP DEVICE TYPE DISK ... DATABASE` command. Again on the second day there is no roll forward because there is only a level 0 incremental. A level 1 incremental tagged `OSS` will be created by the `BACKUP DEVICE TYPE DISK ... DATABASE` command. On the third and following days, the roll forward will be performed using the level 1 incremental tagged `OSS` created on the previous day.
- `BACKUP DEVICE TYPE DISK INCREMENTAL LEVEL 1 FOR RECOVER OF COPY WITH TAG 'OSS' DATABASE`
	Create a new level 1 incremental backup. On the first day this command is run, this will be a level 0 incremental. On the second and following days, this will be a level 1 incremental.
- `BACKUP DEVICE TYPE SBT ARCHIVELOG ALL`
	Backs up archived logs to tape according to the deletion policy in place.
- `BACKUP BACKUPSET ALL`
	Backs up any backup sets created as a result of incremental backup creation.
- `DELETE ARCHIVELOG ALL`
	Deletes archived logs according to the log deletion policy set by the `CONFIGURE ARCHIVELOG DELETION POLICY` command. If the archived logs are in a fast recovery area, then they are automatically deleted when more open disk space is required. Therefore, you only need to use this command if you explicitly want to delete logs each day.

#### 11.4.1.2 Commands for Weekly Tape Backups Using Disk as Cache

To back up all recovery-related files to tape, use the following command once a week:

```
BACKUP RECOVERY FILES;
```

This ensures that all current incremental, image copy, and archived log backups on disk are backed up to tape.

### 11.4.2 Performing Backups Directly to Tape

Oracle's Media Management Layer (MML) API lets third-party vendors build a media manager, software that works with RMAN and the vendor's hardware to allow backups to sequential media devices such as tape drives. A media manager handles loading, unloading, and labeling of sequential media such as tapes. You must install Oracle Secure Backup or third-party media management software to use RMAN with sequential media devices.

Take the following steps to perform backups directly to tape, by default:

1. Connect RMAN to the standby database (as the target database) and recovery catalog.
2. Execute the `CONFIGURE` command as follows:
	```
	CONFIGURE DEFAULT DEVICE TYPE TO SBT;
	```

In this scenario, full backups are taken weekly, with incremental backups taken daily on the standby database.

See Also:

[Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/cd/E11882_01/backup.112/e10642/rcmconfb.htm#BRADV132) for more information about how to configure RMAN for use with a media manager

#### 11.4.2.1 Commands for Daily Backups Directly to Tape

Take the following steps to perform daily backups directly to tape:

1. Connect RMAN to the standby database (as target database) and to the recovery manager.
2. Execute the following RMAN commands:
	```
	RESYNC CATALOG FROM DB_UNIQUE_NAME ALL;
	BACKUP AS BACKUPSET INCREMENTAL LEVEL 1 DATABASE PLUS ARCHIVELOG; 
	DELETE ARCHIVELOG ALL;
	```

These commands resynchronize the information from all other databases in the Data Guard environment. They also create a level 1 incremental backup of the database, including all archived logs. On the first day this script is run, if no level 0 backups are found, then a level 0 backup is created.

The `DELETE ARCHIVELOG ALL` command is necessary only if all archived log files are not in a fast recovery area.

#### 11.4.2.2 Commands for Weekly Backups Directly to Tape

One day a week, take the following steps to perform a weekly backup directly to tape:

1. Connect RMAN to the standby database (as target database) and to the recovery catalog.
2. Execute the following RMAN commands:
	```
	BACKUP AS BACKUPSET INCREMENTAL LEVEL 0 DATABASE PLUS ARCHIVELOG;
	DELETE ARCHIVELOG ALL;
	```

These commands resynchronize the information from all other databases in the Data Guard environment, and create a level 0 database backup that includes all archived logs.

The `DELETE ARCHIVELOG ALL` command is necessary only if all archived log files are not in a fast recovery area.

## 11.6 Reporting in a Data Guard Environment

Use the RMAN `LIST`, `REPORT`, and `SHOW` commands with the `FOR DB_UNIQUE_NAME` clause to view information about a specific database.

For example, after connecting to the recovery catalog, you could use the following commands to display information for a database with a DBID of 1625818158 and to list the databases in the Data Guard environment. The `SET DBID` command is required only if you are not connected to a database as `TARGET`. The last three commands list archive logs, database file names, and RMAN configuration information for a database with a `DB_UNIQUE_NAME` of `BOSTON`.

```
SET DBID 1625818158;
LIST DB_UNIQUE_NAME OF DATABASE;
LIST ARCHIVELOG ALL FOR DB_UNIQUE_NAME BOSTON;
REPORT SCHEMA FOR DB_UNIQUE_NAME BOSTON;
SHOW ALL FOR DB_UNIQUE_NAME BOSTON;
```

## 11.7 Performing Backup Maintenance in a Data Guard Environment

The files in a Data Guard environment (datafiles, archived logs, backup pieces, image copies, and proxy copies) are associated with a database through use of the `DB_UNIQUE_NAME` parameter. Therefore, it is important that the value supplied for `DB_UNIQUE_NAME` be unique for each database in a Data Guard environment. This information, along with file-sharing attributes, is used to determine which files can be accessed during various RMAN operations.

File sharing attributes state that files on disk are accessible only at the database with which they are associated, whereas all files on tape are assumed to be accessible by all databases. RMAN commands such as `BACKUP` and `RESTORE`, as well as other maintenance commands, work according to this assumption. For example, during a roll-forward operation of an image copy at a database, only image copies associated with the database are rolled forward. Likewise, all incremental backups on disk and all incremental backups on tape will be used to roll forward the image copies. Similarly, during recovery operations, only disk backups associated with the database and files on tape will be considered as sources for backups.

See Also:

[Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/toc.htm) for detailed information about RMAN commands

### 11.7.1 Changing Metadata in the Recovery Catalog

You can use the RMAN `CHANGE` command with various operands to change metadata in the recovery catalog, as described in the following sections.

Changing File Association from One Standby Database to Another

Use the `CHANGE` command with the `RESET DB_UNIQUE_NAME` option to alter the association of files from one database to another within a Data Guard environment. The `CHANGE` command is useful when disk backups or archived logs are transferred from one database to another and you want to use them on the database to which they were transferred. The `CHANGE` command can also change the association of a file from one database to another database, without having to directly connect to either database using the `FOR DB_UNIQUE_NAME` and `RESET DB_UNIQUE_NAME TO` options.

Changing DB\_UNIQUE\_NAME for a Database

If the value of the `DB_UNIQUE_NAME` initialization parameter changes for a database, the same change must be made in the Data Guard environment. The RMAN recovery catalog, after connecting to that database instance, will know both the old and new value for `DB_UNIQUE_NAME`. To merge the information for the old and new values within the recovery catalog schema, you must use the RMAN `CHANGE DB_UNIQUE_NAME` command. If RMAN is not connected to the instance with the changed `DB_UNIQUE_NAME` parameter, then the `CHANGE DB_UNIQUE_NAME` command can also be used to rename the `DB_UNIQUE_NAME` in the recovery catalog schema. For example, if the instance parameter value for a database was changed from `BOSTON_A` to `BOSTON_B`, the following command should be executed at the RMAN prompt after connecting to a target database and recovery catalog:

```
CHANGE DB_UNIQUE_NAME FROM BOSTON_A TO BOSTON_B;
```

Making Backups Unavailable or Removing Their Metadata

Use `CHANGE` command options such as `AVAILABLE`, `UNAVAILABLE`, `KEEP`, and `UNCATALOG` to make backups available or unavailable for restore and recovery purposes, and to keep or remove their metadata.

See Also:

[Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta009.htm#RCMRF110) for more information about the RMAN `CHANGE` command

### 11.7.2 Deleting Archived Logs or Backups

Use the `DELETE` command to delete backup sets, image copies, archived logs, or proxy copies. To delete only files that are associated with a specific database, you must use the `FOR DB_UNIQUE_NAME` option with the `DELETE` command.

File metadata is deleted for all successfully deleted files associated with the current target database (or for files that are not associated with any known database). If a file could not be successfully deleted, you can use the `FORCE` option to remove the file's metadata.

When a file associated with another database is deleted successfully, its metadata in the recovery catalog is also deleted. Any files that are associated with other databases, and that could not be successfully deleted, are listed at the completion of the `DELETE` command, along with instructions for you to perform the same operation at the database with which the files are associated (files are grouped by database). Note that the `FORCE` option cannot be used to override this behavior. If you are certain that deleting the metadata for the non-deletable files will not cause problems, you can use the `CHANGE RESET DB_UNIQUE_NAME` command to change the metadata for association of files with the database and use the `DELETE` command with the `FORCE` option to delete the metadata for the file.

See Also:

[Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta016.htm#RCMRF121) for more information about the RMAN `DELETE` command

### 11.7.3 Validating Recovery Catalog Metadata

Use the `CROSSCHECK` command to validate and update file status in the recovery catalog schema. To validate files associated with a specific database, use the `FOR DB_UNIQUE_NAME` option with the `CROSSCHECK` command.

Metadata for all files associated with the current target database (or for any files that are not associated with any database), will be marked `AVAILABLE` or `EXPIRED` according to the results of the `CROSSCHECK` operation.

If a file associated with another database is successfully inspected, its metadata in the recovery catalog is also changed to `AVAILABLE`. Any files that are associated with other databases, and that could not be inspected successfully, are listed at the completion of the `CROSSCHECK` command, along with instructions for you to perform the same operation at the database with which the files are associated (files are grouped by site). If you are certain of the configuration and still want to change status metadata for unavailable files, you can use the `CHANGE RESET DB_UNIQUE_NAME` command to change metadata for association of files with the database and execute the `CROSSCHECK` command to update status metadata to `EXPIRED`.

See Also:

[Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta015.htm#RCMRF119) for more information about the RMAN `CROSSCHECK` command

## 11.8 Recovery Scenarios in a Data Guard Environment

The examples in the following sections assume you are restoring files from tape to the same system on which the backup was created. If you need to restore files to a different system, you need to configure the channels for that system before executing restore and recover commands. You can set the configuration for a nonexistent database using the `SET DBID` command and the `CONFIGURE` command with `FOR DB_UNIQUE_NAME`. See the Media Management documentation for more information about how to access RMAN backups from different systems.

The following scenarios are described in this section:

- Recovery from Loss of Datafiles on the Primary Database
- Recovery from Loss of Datafiles on the Standby Database
- Recovery from Loss of a Standby Control File
- Recovery from Loss of the Primary Control File
- Recovery from Loss of an Online Redo Log File
- Incomplete Recovery of the Primary Database

### 11.8.1 Recovery from Loss of Datafiles on the Primary Database

You can recover from loss of datafiles on the primary database by using backups or by using the files on a standby database, as described in the following sections.

Using Backups

Issue the following RMAN commands to restore and recover datafiles. You must be connected to both the primary and recovery catalog databases.

```
RESTORE DATAFILE n,m...;
RECOVER DATAFILE n,m...;
```

Issue the following RMAN commands to restore and recover tablespaces. You must be connected to both the primary and recovery catalog databases.

```
RESTORE TABLESPACE tbs_name1, tbs_name2, ...
RECOVER TABLESPACE tbs_name1, tbs_name2, ...
```

Using Files On a Standby Database

As of Oracle 11g, you can use files on a standby database to recover a lost datafile. This works well if the standby is up-to-date and the network connection is sufficient enough to support the file copy between the standby and primary.

Start RMAN and take the following steps to copy the datafiles from the standby to the primary:

1. Connect to the standby database as the target database:
	```
	CONNECT TARGET sys@standby
	```
	You are prompted for a password:
	```
	target database Password: password
	```
2. Connect to the primary database as the auxiliary database:
	```
	CONNECT AUXILIARY sys@primary
	```
	You are prompted for a password:
	```
	target database Password: password
	```
3. Back up the datafile on the standby host across the network to a location on the primary host. For example, suppose that `/disk1/df2.dbf` is the name of datafile 2 on the standby host. Suppose that `/disk8/datafile2.dbf` is the name of datafile 2 on the primary host. The following command would copy datafile 2 over the network to `/disk9/df2copy.dbf`:
	```
	BACKUP AS COPY DATAFILE 2 AUXILIARY FORMAT '/disk9/df2copy.dbf';
	```
4. Exit the RMAN client as follows:
	```
	EXIT;
	```
5. Start RMAN and connect to the primary database as target, and to the recovery catalog:
	```
	CONNECT TARGET sys@primary;
	target database Password: password
	CONNECT CATALOG rman@catdb;
	recovery catalog database Password: password
	```
6. Use the `CATALOG DATAFILECOPY` command to catalog this datafile copy so that RMAN can use it.:
	```
	CATALOG DATAFILECOPY '/disk9/df2copy.dbf';
	```
	Then use the `SWITCH DATAFILE` command to switch the datafile copy so that `/disk9/df2copy.dbf` becomes the current datafile:
	```
	RUN {
	  SET NEWNAME FOR DATAFILE 2 TO '/disk9/df2copy.dbf';
	  SWITCH DATAFILE 2;
	}
	```

### 11.8.2 Recovery from Loss of Datafiles on the Standby Database

To recover the standby database after the loss of one or more datafiles, you must restore the lost files to the standby database from the backup using the RMAN `RESTORE DATAFILE` command. If all the archived redo log files required for recovery of damaged files are accessible on disk by the standby database, restart Redo Apply.

If the archived redo log files required for recovery are not accessible on disk, use RMAN to recover the restored datafiles to an SCN/log sequence greater than the last log applied to the standby database, and then restart Redo Apply to continue the application of redo data, as follows:

1. Connect SQL\*Plus to the standby database.
2. Stop Redo Apply using the SQL `ALTER DATABASE ...` statement.
3. In a separate terminal, start RMAN and connect to both the standby and recovery catalog databases (use the `TARGET` keyword to connect to the standby instance).
4. Issue the following RMAN commands to restore and recover datafiles on the standby database:
	```
	RESTORE DATAFILE <n,m,...>;
	RECOVER DATABASE;
	```
	To restore a tablespace, use the RMAN `'RESTORE TABLESPACE` `tbs_name1, tbs_name2, ...`' command.
5. At the SQL\*Plus prompt, restart Redo Apply using the SQL `ALTER DATABASE ...` statement.

See Also:

[Section 7.3](log_apply.md) and [Section 7.4](log_apply.md) for more information about starting and stopping Redo Apply

### 11.8.3 Recovery from Loss of a Standby Control File

Oracle software allows multiplexing of the standby control file. To ensure the standby control file is multiplexed, check the `CONTROL_FILES` initialization parameter, as follows:

```
SQL> SHOW PARAMETER CONTROL_FILES;

NAME                                 TYPE        VALUE
 ------------------------------------ ----------- ------------------------------
control_files                        string      <cfilepath1>,<cfilepath2>
```

If one of the multiplexed standby control files is lost or is not accessible, Oracle software stops the instance and writes the following messages to the alert log:

```
ORA-00210: cannot open the specified controlfile
ORA-00202: controlfile: '/disk1/oracle/dbs/scf3_2.f'
ORA-27041: unable to open file
```

You can copy an intact copy of the control file over the lost copy, then restart the standby instance using the following SQL statements:

```
SQL> STARTUP MOUNT;
SQL> ALTER DATABASE RECOVER MANAGED STANDBY DATABASE DISCONNECT FROM SESSION;
```

You can restore the control file from backups by executing the `RESTORE CONTROLFILE` command and then the `RECOVER DATABASE` command. The `RECOVER DATABASE` command automatically fixes the file names in the control file to match the files existing at that database, and recovers the database to the most recently received log sequence at the database.

The other alternative is to create a new control file from the primary database, copy it to all multiplexed locations, and manually rename the data file names to match files existing on disk.

### 11.8.4 Recovery from Loss of the Primary Control File

Oracle software allows multiplexing of the control file on the primary database. If one of the control files cannot be updated on the primary database, the primary database instance is shut down automatically.

You can restore the control file from backups by executing the `RESTORE CONTROLFILE` command and the `RECOVER DATABASE` command. The `RECOVER DATABASE` command automatically fixes the file names in the control file to match the files existing at that database, and recovers the database.

The other alternative is to create a new control file using `CREATE CONTROLFILE` SQL command. It is possible to re-create the control file provided all data files and online logs are not lost.

See Also:

[Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/cd/E11882_01/backup.112/e10642/toc.htm) for detailed information about using RMAN to recover from the loss of control files

### 11.8.5 Recovery from Loss of an Online Redo Log File

Oracle recommends multiplexing the online redo log files. The loss of all members of an online redo log group causes Oracle software to terminate the instance. If only some members of a log file group cannot be written, they will not be used until they become accessible. The views `V$LOGFILE` and `V$LOG` contain more information about the current status of log file members in the primary database instance.

When Oracle software is unable to write to one of the online redo log file members, the following alert messages are returned:

```
ORA-00313: open failed for members of log group 1 of thread 1
ORA-00312: online log 1 thread 1: '/disk1/oracle/dbs/t1_log1.f'
ORA-27037: unable to obtain file status
SVR4 Error: 2: No such file or directory
Additional information: 3
```

If the access problem is temporary due to a hardware issue, correct the problem and processing will continue automatically. If the loss is permanent, a new member can be added and the old one dropped from the group.

To add a new member to a redo log group, issue the following statement:

```
SQL> ALTER DATABASE ADD LOGFILE MEMBER 'log_file_name' REUSE TO GROUP n;
```

You can issue this statement even when the database is open, without affecting database availability.

If all members of an inactive group that has been archived are lost, the group can be dropped and re-created.

In all other cases (loss of all online log members for the current `ACTIVE` group, or an inactive group which has not yet been archived), you must fail over to the standby database. Refer to [Chapter 8](role_management.md) for the failover procedure.

### 11.8.6 Incomplete Recovery of the Primary Database

Incomplete recovery of the primary database is normally done in cases such as when the database is logically corrupted (by a user or an application) or when a tablespace or datafile was accidentally dropped from database.

Depending on the current database checkpoint SCN on the standby database instances, you can use one of the following procedures to perform incomplete recovery of the primary database. All the procedures are in order of preference, starting with the one that is the least time consuming.

Using Flashback Database Using Flashback Database is the recommended procedure when the Flashback Database feature is enabled on the primary database, none of the database files are lost, and the point-in-time recovery is greater than the oldest flashback SCN or the oldest flashback time. See [Section 13.3](scenarios.md) for the procedure to use Flashback Database to do point-in-time recovery.

Using the standby database instance This is the recommended procedure when the standby database is behind the desired incomplete recovery time, and Flashback Database is not enabled on the primary or standby databases:

1. Recover the standby database to the desired point in time.
	```
	RECOVER DATABASE UNTIL TIME 'time';
	```
	Alternatively, incomplete recovery time can be specified using the SCN or log sequence number:
	```
	RECOVER DATABASE UNTIL SCN incomplete recovery SCN';
	RECOVER DATABASE UNTIL LOGSEQ incomplete recovery log sequence number THREAD thread number;
	```
2. Open the standby database in read-only mode to verify the state of database.
	If the state is not what is desired, use the LogMiner utility to look at the archived redo log files to find the right target time or SCN for incomplete recovery. Alternatively, you can start by recovering the standby database to a point that you know is before the target time, and then open the database in read-only mode to examine the state of the data. Repeat this process until the state of the database is verified to be correct. Note that if you recover the database too far (that is, past the SCN where the error occurred) you cannot return it to an earlier SCN.
3. Activate the standby database using the SQL `ALTER DATABASE ACTIVATE STANDBY DATABASE` statement. This converts the standby database to a primary database, creates a new resetlogs branch, and opens the database. See [Section 9.4](manage_ps.md) to learn how the standby database reacts to the new reset logs branch.

Using the primary database instance If all of the standby database instances have already been recovered past the desired point in time and Flashback Database is not enabled on the primary or standby database, then this is your only option.

Use the following procedure to perform incomplete recovery on the primary database:

1. Use LogMiner or another means to identify the time or SCN at which all the data in the database is known to be good.
2. Using the time or SCN, issue the following RMAN commands to do incomplete database recovery and open the database with the `RESETLOGS` option (after connecting to catalog database and primary instance that is in `MOUNT` state):
	```
	RUN 
	{
	SET UNTIL TIME 'time';
	RESTORE DATABASE;
	RECOVER DATABASE;
	}
	ALTER DATABASE OPEN RESETLOGS;
	```

After this process, all standby database instances must be reestablished in the Data Guard configuration.

## 11.9 Additional Backup Situations

The following sections describe how to modify the backup procedures for other configurations, such as when the standby and primary databases cannot share backup files; the standby instance is only used to remotely archive redo log files; or the standby database filenames are different than the primary database.

### 11.9.1 Standby Databases Too Geographically Distant to Share Backups

If the standby databases are far apart from one another, the backups taken on them may not be easily accessible by the primary system or other standby systems. Perform a complete backup of the database on all systems to perform recovery operations. The fast recovery area can reside locally on the primary and standby systems (that is, the fast recovery area does not have to be the same for the primary and standby databases).

In this scenario, you can still use the general strategies described in Section 11.8, with the following exceptions:

- Backup files created by RMAN must be tagged with the local system name, and with `RESTORE` operations that tag must be used to restrict RMAN from selecting backups taken on the same host. In other words, the `BACKUP` command must use the `TAG` system name option when creating backups; the `RESTORE` command must use the `FROM TAG` system name option; and the `RECOVER` command must use the `FROM TAG` system name `ARCHIVELOG TAG` system name option.
- Disaster recovery of the standby site:
	1. Start the standby instance in the `NOMOUNT` state using the same parameter files with which the standby was operating earlier.
		2. Create a standby control file on the primary instance using the SQL `ALTER DATABASE CREATE STANDBY CONTROLFILE AS` filename statement, and use the created control file to mount the standby instance.
		3. Issue the following RMAN commands to restore and recover the database files:
		```
		RESTORE DATABASE FROM TAG 'system name';
		RECOVER DATABASE FROM TAG 'system name' ARCHIVELOG TAG 'system name';
		```
		4. Restart Redo Apply.

The standby instance will fetch the remaining archived redo log files.

### 11.9.2 Standby Database Does Not Contain Datafiles, Used as a FAL Server

Use the same procedure described in Section 11.4, with the exception that the RMAN commands that back up database files cannot be run against the FAL server. The FAL server can be used as a backup source for all archived redo log files, thus off-loading backups of archived redo log files to the FAL server.

### 11.9.3 Standby Database File Names Are Different From Primary Database

Note:

As of Oracle Database 11g, the recovery catalog can resynchronize the file names from each standby database site. However, if the file names from a standby database were never resynchronized for some reason, then you can use the procedure described in this section to do so.

If the database filenames are not the same on the primary and standby databases that were never resynchronized, the `RESTORE` and `RECOVER` commands you use will be slightly different. To obtain the actual datafile names on the standby database, query the `V$DATAFILE` view and specify the `SET NEWNAME` option for all the datafiles in the database:

```
RUN 
{
SET NEWNAME FOR DATAFILE 1 TO 'existing file location for file#1 from V$DATAFILE';
SET NEWNAME FOR DATAFILE 2 TO 'existing file location for file#2 from V$DATAFILE';
…
…
 SET NEWNAME FOR DATAFILE n TO 'existing file location for file#n from V$DATAFILE';
 RESTORE {DATAFILE <n,m,…> | TABLESPACE tbs_name_1, 2, …| DATABASE;
SWITCH DATAFILE ALL; 
RECOVER DATABASE {NOREDO};
}
```

Similarly, the RMAN `DUPLICATE` command should also use the `SET NEWNAME` option to specify new filenames during standby database creation. Or you could set the `LOG_FILE_NAME_CONVERT` and `DB_FILE_NAME_CONVERT` parameters.

See Also:

[Section 13.5, "Creating a Standby Database That Uses OMF or Oracle ASM"](scenarios.md) for information about precedence rules when both the `DB_FILE_NAME_CONVERT` and `DB_CREATE_FILE_DEST` parameters are set on the standby

## 11.10 Using RMAN Incremental Backups to Roll Forward a Physical Standby Database

In some situations, RMAN incremental backups can be used to synchronize a physical standby database with the primary database. You can use the RMAN `BACKUP INCREMENTAL FROM SCN` command to create a backup on the primary database that starts at the current SCN of the standby, which can then be used to roll the standby database forward in time.

The steps described in this section apply to situations in which RMAN incremental backups may be useful because the physical standby database either:

- Lags far behind the primary database
- Has widespread nologging changes
- Has nologging changes on a subset of datafiles

Note:

Oracle recommends the use of a recovery catalog when performing this operation. These steps are possible without a recovery catalog, but great care must be taken to correct the file names in the restored control file.

See Also:

[Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/cd/E11882_01/backup.112/e10642/toc.htm) for more information about RMAN incremental backups

### 11.10.1 Steps for Using RMAN Incremental Backups

Except where stated otherwise, the following steps apply to all three situations just listed.

1. Stop Redo Apply on the standby database:
	```
	SQL> ALTER DATABASE RECOVER MANAGED STANDBY DATABASE CANCEL;
	```
2. On the standby database, compute the `FROM SCN` for the incremental backup. This is done differently depending on the situation:
	- On a standby that lags far behind the primary database, query the `V$DATABASE` view and record the current SCN of the standby database:
		```
		SQL> SELECT CURRENT_SCN FROM V$DATABASE;
		CURRENT_SCN
		-----------
		     233995
		```
		- On a standby that has widespread nologging changes, query the `V$DATAFILE` view to record the lowest `FIRST_NONLOGGED_SCN`:
		```
		SQL> SELECT MIN(FIRST_NONLOGGED_SCN) FROM V$DATAFILE -
		> WHERE FIRST_NONLOGGED_SCN>0;
		MIN(FIRST_NONLOGGED_SCN)
		------------------------
		                  223948
		```
		- On a standby that has nologging changes on a subset of datafiles, query the `V$DATAFILE` view, as follows:
		```
		SQL> SELECT FILE#, FIRST_NONLOGGED_SCN FROM V$DATAFILE -
		> WHERE FIRST_NONLOGGED_SCN > 0;
		FILE#      FIRST_NONLOGGED_SCN
		---------- -------------------
		         4              225979
		         5              230184
		```
3. Connect to the primary database as the RMAN target and create an incremental backup from the current SCN (for a standby lagging far behind the primary) or from the lowest `FIRST_NONLOGGED_SCN` (for a standby with widespread nologging changes) of the standby database that was recorded in step 2:
	```
	RMAN> BACKUP INCREMENTAL FROM SCN 233995 DATABASE FORMAT '/tmp/ForStandby_%U' tag 'FORSTANDBY';
	```
	If the standby has nologging changes on a subset of datafiles, then create an incremental backup for each datafile listed in the `FIRST_NONLOGGED_SCN` column (recorded in step 2), as follows:
	```
	RMAN> BACKUP INCREMENTAL FROM SCN 225979 DATAFILE 4 FORMAT '/tmp/ForStandby_%U' TAG 'FORSTANDBY';
	RMAN> BACKUP INCREMENTAL FROM SCN 230184 DATAFILE 5 FORMAT '/tmp/ForStandby_%U' TAG 'FORSTANDBY';
	```
	The `BACKUP` commands shown generate datafile backups, as well as a control file backup that will be used in step 7.
4. If the backup pieces are not on shared storage, then transfer all the backup pieces created on the primary to the standby:
	```
	scp /tmp/ForStandby_* standby:/tmp
	```
5. If you had to copy the backup pieces in the previous step, or if you are not connected to the recovery catalog for the entire process, then you must catalog the new backup pieces on the standby (otherwise, go on to the next step):
	```
	RMAN> CATALOG START WITH '/tmp/ForStandby';
	```
6. Connect to the standby database as the RMAN target and execute the `REPORT SCHEMA` statement to ensure that the standby database site is automatically registered and that the files names at the standby site are displayed:
	```
	RMAN> REPORT SCHEMA;
	```
7. Connect to the standby database as the RMAN target and apply incremental backups by executing the following commands. Note that the `RESTORE STANDBY CONTROLFILE FROM TAG` command only works if you are connected to the recovery catalog for the entire process. Otherwise, you must use the `RESTORE STANDBY CONTROLFILE FROM '<control file backup filename>'` command.
	```
	RMAN> STARTUP FORCE NOMOUNT;
	RMAN> RESTORE STANDBY CONTROLFILE FROM TAG 'FORSTANDBY';
	RMAN> ALTER DATABASE MOUNT;
	RMAN> RECOVER DATABASE NOREDO;
	```
	Note:
	If a recovery catalog is used, then the RMAN `RECOVER` command will fix the path names for datafiles in the standby control file. If no recovery catalog is used, then you must manually edit the file names in your standby control file or use the RMAN `SET NEWNAME` command to assign the datafile names. See [Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta2014.htm#RCMRF153) for more information about the RMAN `RECOVER` and `SET NEWNAME` commands.
8. On standbys that have widespread nologging changes or that have nologging changes on a subset of datafiles, query the `V$DATAFILE` view to verify there are no datafiles with nologged changes. The following query should return zero rows:
	```
	SQL> SELECT FILE#, FIRST_NONLOGGED_SCN FROM V$DATAFILE -
	> WHERE FIRST_NONLOGGED_SCN > 0;
	```
	Note:
	The incremental backup will become obsolete in 7 days, or you can remove it now using the RMAN `DELETE` command.
9. Start Redo Apply on the physical standby database:
	```
	SQL> ALTER DATABASE RECOVER MANAGED STANDBY DATABASE -
	> USING CURRENT LOGFILE DISCONNECT FROM SESSION;
	```