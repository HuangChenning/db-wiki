---
title: Configuring Backup and Recovery
book: High Availability Best Practices
doc_id: E10803-06
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e10803/config_backuprec.htm
tags:
  - oracle
  - 11g
  - high-availability-best-practices
---

## 8 Configuring Backup and Recovery

A data protection plan is not complete without a sound backup and recovery strategy to protect against system and storage failures. Oracle delivers a comprehensive data protection suite for backup and recovery of Oracle database and unstructured, application files.

The primary focus of this chapter is best practice configuration for backup and recovery for the Oracle database. File system data protection offerings are introduced along with pointers on where to find more information.

This chapter contains the following topics:

Table 8-1 provides a quick reference summary of the Oracle backup and recovery suite.

Table 8-1 Backup and Recovery Summary

| Technology | Recommended use with Oracle Database | Recommended use with File System Data | Comments |
| --- | --- | --- | --- |
| Recovery Manager (RMAN) | Yes | No | Native backup utility for the Oracle database |
| Oracle Secure Backup | Yes | Yes | Tape backup management software |
| Oracle Secure Backup Cloud Module | Yes | No | Backup to Amazon S3 storage |
| Flashback Technologies | Yes | No | Logical error correction leveraging undo data of the Oracle database |
| Flashback Database | Yes | No | Continuous Data Protection (CDP) leveraging flashback logs |
| Automatic Clustered File System (ACFS) Snapshots (for file system clones and disaster recovery) | No | Yes | Read-only or read/write copy-on-write version of the file system. Replication available. |
| ZFS Snapshots (for database clones such as dev/test) | Yes | Yes | Read-only or read/write copy-on-write version of the database for testing and development |
| ZFS Snapshots for backup/restore | No | Yes | Read-only or read/write copy-on-write version of the file system for testing, development and backup |

## 8.1 Oracle Database Backup and Recovery Products and Features

This section discusses the motivation and tools for maintaining good database backups, for using Oracle database recovery features, and for using backup options and strategies made possible with Oracle database features.

### 8.1.1 Understand When to Use Backups

Using backups to resolve an unscheduled outage of a production database may not allow you to meet your Recovery Time Objective (RTO) and Recovery Point Objective (RPO) or service-level requirements. For example, some outages are handled best by using Flashback Database or a standby database. However, some situations require using database backups, including the sample situations shown in Table 8-2.

Table 8-2 Sample Situations that Require Database Backup

| Situations that require Database Backup | Description |
| --- | --- |
| Setting Up the Initial Data Guard Environment | During initial setup of a standby database, you can either use a backup of the primary database that is made accessible to the secondary site to create the initial standby database, or use RMAN network-enabled database duplication to create the standby database without the need for a pre-existing backup. To perform an over-the-network duplication you must include the RMAN `FROM ACTIVE DATABASE` option in the `DUPLICATE` command. |
| Recovering from Data Failures Using File or Block Media Recovery | When a block corruption, media failure, or other physical data failure occurs in an environment that does not include Data Guard, the only method of recovery is to restore from existing backups. |
| Resolving a Double Failure | A double failure scenario is a situation that affects the availability of both the production and the standby databases. An example of a double failure scenario is a site outage at the secondary site, which eliminates fault tolerance, followed by a media failure on the production database. Whether the standby must be re-created depends on the type of outage at the secondary site. If the secondary site outage was temporary and did not involve the physical destruction of files, then after the secondary site is brought back online it can continue to receive redo data from the production database. Otherwise, the resolution of this situation is to re-create the production database from an available backup and then re-create the standby database.  Some multiple failures, or more appropriately disasters, such as a primary site outage followed by a secondary site outage, might require the use of backups that exist only in an offsite location. Developing and following a process to deliver and maintain backup tapes at an offsite location is necessary to restore service in this worst case scenario. |

See Also:

- [Oracle Data Guard Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e41134/create_ps.htm#SBYDB00200) for information about creating a standby database
- [Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/cd/E11882_01/backup.112/e10642/rcmdupdb.htm#BRADV010) for information about the `DUPLICATE` command

### 8.1.2 Use Recovery Manager (RMAN) to Backup Database Files

Recovery Manager (RMAN) is Oracle's utility to backup and recover the Oracle Database. Because of its tight integration with the database, RMAN determines automatically what files must be backed up. More importantly, RMAN knows what files must be restored for media-recovery operations. RMAN uses server sessions to perform backup and recovery operations and stores metadata about backups in a repository. RMAN offers many advantages over typical user-managed backup methods, including:

- Online database backups without placing tablespaces in backup mode
- Efficient block-level incremental backups
- Data block integrity checks during backup and restore operations
- Test backups and restores without actually performing the operation
- Synchronize a physical standby database with the primary database

RMAN automates backup and recovery. While user-managed methods require you to:

- Locate backups for each data file
- Copy backups to the correct place using operating system commands
- Choose which logs to apply

RMAN fully automates these backup and recovery tasks.

There are also capabilities of Oracle backup and recovery that are only available when using RMAN, such as automated tablespace point-in-time recovery and block media recovery.

See Also:

For more information, see the following chapters:
- [Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/cd/E11882_01/backup.112/e10642/rcmblock.htm#BRADV89781) for information about performing block media recovery
- [Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/cd/E11882_01/backup.112/e10642/rcmtspit.htm#BRADV009) for information about performing RMAN Tablespace Point-in-Time Recovery (TSPITR)
- [Oracle Data Guard Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e41134/rman.htm#SBYDB00759) for information about Using RMAN Incremental Backups to Roll Forward a Physical Standby Database

### 8.1.3 Use Oracle Secure Backup for Backups to Tape

Oracle Secure Backup delivers unified data protection for heterogeneous environments with a common management interface across the spectrum of servers. Protecting both Oracle databases and unstructured data, Oracle Secure Backup provides centralized tape backup management for your entire IT environment, including:

- Oracle database through the Oracle Secure Backup built-in integration with Recovery Manager (RMAN)
- File system data protection: For UNIX, Windows, and Linux servers
- Network Attached Storage (NAS) data protection leveraging the Network Data Management Protocol (NDMP)

Oracle Secure Backup is integrated with RMAN providing the media management layer (MML) for Oracle database tape backup and restore operations. The tight integration between these two products delivers high-performance Oracle database tape backup.

Specific performance optimizations between RMAN and Oracle Secure Backup that reduce tape consumption and improve backup performance are:

- Unused block compression: Eliminates the time and space usage needed to backup unused blocks
- Backup undo optimization: Eliminates the time and space usage needed to backup undo that is not required to recover the current backup.

You can manage the Oracle Secure Backup environment using the command line, the Oracle Secure Backup Web tool, and Oracle Enterprise Manager.

Using the combination of RMAN and Oracle Secure Backup provides an end-to-end tape backup solution, eliminating the need for third-party backup software.

See Also:

- [Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/cd/E11882_01/backup.112/e10642/rcmcncpt.htm#BRADV193) for more information about unused block compression and backup undo optimization
- The Oracle Secure Backup platform and NAS and tape device compatibility matrixes:
	`http://www.oracle.com/technetwork/database/secure-backup/learnmore/index.html`

#### 8.1.3.1 Using Oracle Secure Backup for Backups to Amazon S3 Storage

Users can take advantage of the Internet-based data storage services offered by Amazon Web Services (AWS) Simple Storage Service (S3) for their database backup needs. The OSB Cloud Module enables RMAN to use S3 as a repository for Oracle Database backups. This provides an easy-to-manage, cost-efficient, and scalable alternative to maintaining in-house data storage and a local, fully configured backup infrastructure. RMAN with the OSB Cloud module is also the recommended means of backing up an Oracle Database that is running on AWS's Elastic Compute Cloud (EC2).

Users must establish an account with AWS to pay for their storage and network transfer costs as appropriate. Additionally, users must consider their security requirements and network resources, and configure their backups appropriately. Since backups to S3 may travel to AWS on the public Internet, and will be stored on a public cloud facility, it may be necessary to encrypt them to protect the data in transit and at rest at S3. This requirement may not apply for certain databases or in certain configurations, for example when the database runs on EC2 or inside AWS's Virtual Private Cloud (VPC).

Users must also configure the degree of network parallelism (using RMAN channels) to match the network capabilities between the database and S3 (which may include a portion of the public Internet). Multiple simultaneous channels may achieve the highest throughput overall, as RMAN takes full advantage of such parallelism.

### 8.1.4 Use Restore Points for Creating Database Snapshots

Oracle provides restore points and guaranteed restore points:

- Restore points protect against logical failures at risky points during database maintenance. Creating a normal restore point assigns a restore point name to a specific point in time or SCN, that is a snapshot of the data as of that time. Normal restore points are available with Flashback Table, Flashback Database, and all RMAN recovery-related operations.
- Guaranteed restore points are recommended for database-wide maintenance such as database or application upgrades, or running batch processes. Guaranteed restore points are integrated with Flashback Database and enforce the retention of all flashback logs required for flashing back to the guaranteed restore point. After maintenance activities complete and the results are verified, you should delete guaranteed restore points that are no longer needed to reclaim flashback log space.

See Also:

[Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/cd/E11882_01/backup.112/e10642/flashdb.htm#BRADV71000) for more information about using restore points and guaranteed restore points with a Flashback Database

## 8.2 Backup and Recovery Configuration and Administration Best Practices

This section describes best practices for determining backup frequency, using the RMAN recovery catalog, and for using Oracle database backup options such as Block Change Tracking.

### 8.2.1 Determine a Backup Frequency and Retention Policy

It is important to determine a backup frequency policy and to perform regular backups. A backup retention policy helps ensure that needed data is not destroyed.

Factors Determining Backup Frequency Frequent backups are essential for any recovery scheme. You should base the frequency and content of backups on the following criteria:

- Criticality of the data: The Recovery Point Objective (RPO) determines how much data your business can acceptably lose if a failure occurs. The more critical the data, the lower the RPO and the more frequently data should be backed up. If you are going to back up certain tablespaces more often than others, with the goal of getting better RPO for those tablespaces, then you also must plan for doing TSPITR as part of your recovery strategy. This requires considerably more planning and practice than DBPITR, because you must ensure that the tablespaces you plan to TSPITR are self-contained.
- Estimated repair time: The Recovery Time Objective (RTO) determines the acceptable amount of time needed for recovery. Repair time is dictated by restore time plus recovery time. The lower the RTO, the higher the frequency of backups, that is, backups are more current, thereby reducing recovery time.
- Volume of changed data: The rate of database change effects how often data is backed up:
	- For read-only data, perform backups frequently enough to adhere to retention policies.
		- For frequently changing data, perform backups more often to reduce the RTO.

To simplify database backup and recovery, the Oracle Suggested Backup Strategy uses the fast recovery area, incremental backups, and incrementally updated backup features. After the initial image copy backup to the FRA, only the changed blocks are captured in the incremental backups thereafter and subsequently applied to the image copy, thereby updating the copy to the most current incremental backup time (that is, incrementally updating the backup).

See Also:

- [Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/cd/E11882_01/backup.112/e10642/rcmtspit.htm#BRADV009) for information about Performing RMAN Tablespace Point-in-Time Recovery (TSPITR)
- [Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/cd/E11882_01/backup.112/e10642/rcmflash.htm#BRADV84152) for information about Performing Database Point-in-Time Recovery
- [Oracle Database 2 Day DBA](https://docs.oracle.com/cd/E11882_01/server.112/e10897/backrest.htm#ADMQS09322) for information about Using the Oracle Suggested Backup Strategy

Establishing a Backup Retention Policy A backup retention policy is a rule set regarding which backups must be retained, on disk or other backup media, to meet recovery and other requirements. It may be safe to delete a specific backup because it has been superseded by more recent backups or because it has been stored on tape. You may also have to retain a specific backup on disk for other reasons such as archival or regulatory requirements. A backup that is no longer needed to satisfy the backup retention policy is said to be obsolete.

Base your backup retention policy on redundancy or on a recovery window:

- In a redundancy-based retention policy, specify a number n such that you always keep at least n distinct backups of each file in your database.
- In a recovery window-based retention policy, specify an earlier time interval, for example, one week or one month, and keep all backups required to let you perform point-in-time recovery to any point during that window.

Keeping Archival Backups Some businesses must retain some backups for much longer than their day-to-day backup retention policy. RMAN allows for this with the Long-term Archival Backup feature. Rather than becoming obsolete according to the database's backup retention policy, archival backups either never become obsolete or become obsolete when their time limit expires.

You can use the RMAN `BACKUP` command with the `KEEP` option to retain backups for longer than your ordinary retention policy. This option specifies the backup as an archival backup, which is a self-contained backup that is exempt from the configured retention policy. This allows you to retain certain backups for much longer than usual, when needed for such reasons as satisfying statutory retention requirements. Using the `KEEP` `FOREVER` option, a recovery catalog is required because the backup records eventually age out of the control file (otherwise, without a recovery catalog, loss may occur when you retain backups for much longer than usual using the database control file). Only the archived redo log files required to make an archival backup consistent are retained. For more information about the RMAN recovery catalog, see Section 8.2.2, "Use an RMAN Recovery Catalog".

See Also:

[Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/cd/E11882_01/backup.112/e10642/rcmbckba.htm#BRADV89551) for information about Archival Backups for Long-Term Storage

### 8.2.2 Use an RMAN Recovery Catalog

To protect and keep backup metadata for longer retention times than can be accommodated by the control file, you can create a recovery catalog. You should create the recovery catalog schema in a dedicated standalone database. Do not locate the recovery catalog with other production data. If you use Oracle Enterprise Manager, you can create the recovery catalog schema in the Oracle Enterprise Manager repository database.

The advantages of using a recovery catalog include:

- Storing backup information for a longer retention period than what can be feasibly stored in the control file. If the control file is too small to hold additional backup metadata, then existing backup information is overwritten, making it difficult to restore and recover using those backups.
- Stores metadata for multiple databases.
- Offloading backups to a physical standby database and using those backups to restore and recover the primary database. Similarly, you can back up a tablespace on a primary database and restore and recover it on a physical standby database. Note that backups of logical standby databases are not usable at the primary database.

See Also:

[Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/cd/E11882_01/backup.112/e10642/rcmarchi.htm#BRADV103) for more information about RMAN repository and the recovery catalog

### 8.2.3 Create Backups in NOCATALOG Mode and Then RESYNC CATALOG

When creating backups to disk or tape, use the target database control file as the RMAN repository so that the success of the backup does not depend on the availability of the database connection to the recovery catalog. To use the target database control file as the RMAN repository, run RMAN with the `NOCATALOG` option. Immediately after the backup is complete, the new backup information stored in the target database control file should be synchronized to the recovery catalog using the `RESYNC CATALOG` command.

See Also:

[Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta2009.htm#RCMRF150) for more information about the `RESYNC CATALOG` command

### 8.2.4 Enable Block Change Tracking for Incremental Backups

Oracle database includes the `BLOCK CHANGE TRACKING` feature for incremental backups which improves incremental backup performance by keeping track of which database blocks have changed since the previous backup. If `BLOCK CHANGE TRACKING` is enabled then RMAN uses the block change tracking file to identify which blocks to include in an incremental backup. This avoids the need to scan every block in the data file, reducing the number of disk reads during backup.

Starting with Oracle Database 11g, you can enable `BLOCK CHANGE TRACKING` on both the primary and physical standby databases. You should enable change tracking for any database where incremental backups are being performed. For example, if backups have been completely offloaded to a physical standby database, then Block Change Tracking should be enabled for that database (this requires Active Data Guard). If backups are being performed on both the primary and physical standby databases, then enable Block Change Tracking for both databases.

See Also:

- [Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/cd/E11882_01/backup.112/e10642/rcmbckba.htm#BRADV89536) for information about Enabling and Disabling Block Change Tracking
- [Oracle Database Backup and Recovery Basics](https://docs.oracle.com/cd/E11882_01/backup.112/e10642/rcmbckba.htm#BRADV8125) for more information about Block Change Tracking

### 8.2.5 Enable Autobackup for the Control File and Server Parameter File

You should configure RMAN to automatically back up the control file and the server parameter file (SPFILE) whenever the database structure metadata in the control file changes or when a backup record is added.

The control file autobackup option enables RMAN to recover the database even if the current control file, catalog, and SPFILE are lost. Enable the RMAN autobackup feature with the `CONFIGURE CONTROLFILE AUTOBACKUP ON` statement.

You should enable autobackup for both the primary and standby databases. For example, after connecting to the primary database, as the target database, and the recovery catalog, issue the following command:

```
CONFIGURE CONTROLFILE AUTOBACKUP ON;
```

See Also:

- [Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/cd/E11882_01/backup.112/e10642/rcmconfb.htm#BRADV89407) for information about Configuring Control File and Server Parameter File Autobackups
- [Oracle Data Guard Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e41134/rman.htm#SBYDB4855) for more information about RMAN Configurations at a Standby Database Where Backups are Performed

### 8.2.6 Offload Backups to a Physical Standby Database

In an Oracle Data Guard configuration you can offload the process of backing up control files, data files, and archived redo log files to a physical standby database system, thereby minimizing the effect of performing backups on the primary system. You can use these backups to recover the primary or standby database.

Note:

Backups of logical standby databases are not usable on the primary database.

See Also:

[Oracle Data Guard Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e41134/rman.htm#SBYDB04700) for information about using RMAN to back up and restore files

### 8.2.7 Set UNDO Retention for Flashback Query and Flashback Table Needs

To ensure a database is enabled to use Flashback Query, Flashback Versions Query, and Flashback Transaction Query, implement the following:

- Set the `UNDO_MANAGEMENT` initialization parameter to `AUTO`. This ensures the database is using an undo tablespace.
- Set the `UNDO_RETENTION` initialization parameter to a value that allows `UNDO` to be kept for a length of time that allows success of your longest query back in time or to recover from human errors.
- Set the `RETENTION` `GUARANTEE` clause for the undo tablespace to guarantee that unexpired undo will not be overwritten.

The Flashback Table also relies on the undo data to recover the tables. Enabling Automatic Undo Management is recommended and the `UNDO_RETENTION` parameter must be set to a period for which the Flashback Table is needed. If a given table does not contain the required data after a Flashback Table, it can be flashed back further, flashed forward, or back to its original state, if there is sufficient `UNDO` data.

See Also:

- [Oracle Database Advanced Application Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e41502/adfns_flashback.htm#ADFNS1008) for information about Flashback
- [Oracle Database Advanced Application Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e41502/adfns_flashback.htm#ADFNS01003) for information about Flashback Query

## 8.3 Backup to Disk Best Practices

Review the following priorities to determine your disk backup strategy:

- Overall backup time
- Impact to resource consumption
- Space used by the backup
- Recovery time

Table 8-3 compares different backup alternatives against the different priorities you might have. Using Table 8-3 as a guide, you can choose the best backup approach for your specific business requirements. You might want to minimize backup space while sacrificing recovery time. Alternatively, you might choose to place a higher priority on recovery and backup times while space is not an issue.

Table 8-3 Comparing Backup to Disk Options

| Backup Option | Overall Backup Time   1: Fastest   5: Slowest | Impact on Resource Consumption   1: Lowest   5: Highest | Space Used by Backup   1: Least   5: Most | Recovery Time   1: Fastest   5: Slowest |
| --- | --- | --- | --- | --- |
| Data file image copy | 5 | 5 | 5 | 1  No restore (switch to fast recovery area copy) |
| Full or level 0 backup set | 4 | 4 | 3 | 3 |
| Differential incremental backup set (level 1); applied to previous level 0 and level 1 backups during recovery | 1 | 1 | 1 | 5 |
| Cumulative incremental backup set (level 1); applied to previous level 0 backup during recovery | 2 | 2 | 2 | 4 |
| Incrementally updated backup (level 1); incremental applied to image copy after backup | 3 | 1 | 5 | 1  No restore (switch to fast recovery area copy) |

Backup to Disk: Best Practices for Optimizing Recovery Times If restore time is your primary concern then perform either a database copy or an incremental backup with immediate apply of the incremental to the copy. These are the only options that provide an immediate usable backup of the database, which you then must recover only to the time of the failure using archived redo log files created since the last incremental backup was performed.

Backup to Disk: Best Practices for Minimizing Space Usage If space usage is your primary concern then perform an incremental backup with a deferred apply of the incremental to the copy. If you perform a cumulative level 1 incremental backup, then it stores only those blocks that have been changed since the last level 0 backup:

- With a cumulative incremental backup apply only the last level 1 backup to the level 0 backup.
- With a differential incremental backup apply all level 1 backups to the level 0 backup.

A cumulative incremental backup usually consumes more space in the fast recovery area than a differential incremental backup.

Backup to Disk: Best Practices for Minimizing System Resource Consumption (I/O and CPU) If system resource consumption is your primary concern then an incremental backup with a Block Change Tracking enabled consumes the least amount of resources on the database.

Example

For many applications, only a small percentage of the entire database is changed each day even if the transaction rate is very high. In many cases, applications repeatedly modify the same set of blocks; so, the total unique, changed block set is small.

For example, a database contains about 600 GB of user data, not including temp files and redo logs. Every 24 hours, approximately 2.5% of the database is changed, which is approximately 15 GB of data. In this example, MAA testing recorded the following results:

- Level 0 backup takes 180 minutes, including `READ` s from the data area and `WRITE` s to the fast recovery area
- Level 1 backup takes 20 minutes, including `READ` s from the data area and `WRITE` s to the fast recovery area
- Rolling forward and merging an existing image copy in the fast recovery area with a newly created incremental backup takes only 45 minutes, including `READ` s and `WRITE` s from the fast recovery area.

In this example, the level 0 backup (image copy) takes 180 minutes. This is the same amount of time it takes to perform a full backup set.

Subsequent backups are level 1 (incremental), which take 20 minutes, so the potential impact on the data area is reduced. That backup is then applied to the existing level 0 backup, which takes 45 minutes. This process does not perform I/O to the data area, so there is no impact (assuming the fast recovery area and data area use separate storage). The total time to create the incremental backup and apply it to the existing level 0 backup is 65 minutes (20+45).

The result is the same using incrementally updated backups or full backup sets, a full backup of the database is created. The incremental approach takes 115 minutes less time (64% less) than simply creating a full backup set. In addition, the I/O impact is less, particularly against the data area which should have less detrimental effect on production database performance.

Thus, for this example when you compare a full backup set strategy versus starting with an image copy, performing only incremental backups, and then rolling forward the copy, the net savings are:

Thus, for this example when you compare always taking full backups versus starting with a level 0 backup, performing only incremental backups, and then rolling forward the level 0 backup, the net savings are:

- 115 minutes or 64% time savings to create a complete backup
- Reduced I/O on the database during backups

See Also:

[Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/cd/E11882_01/backup.112/e10642/rcmbckba.htm#BRADV8003) for more information about backing up the database

## 8.4 Backup to Tape Best Practices

Recovery Manager (RMAN) provides automated disk backup for the Oracle database and is integrated with media management products such as Oracle Secure Backup for backup to tape. Whether your Oracle database backup strategy uses disk, tape, or both, the combination of RMAN and Oracle Secure Backup delivers a comprehensive solution to meet your specific requirements.

### 8.4.1 Initial RMAN Oracle Secure Backup Configuration

When installing Oracle Secure Backup, the System Backup Tape (SBT) libraries for RMAN tape backups are automatically linked. Using Oracle Enterprise Manager Database Control you can manage the Oracle Secure Backup backup domain from tape vaulting to backup and restore operations. The tight integration between RMAN, Oracle Enterprise Manager Database Control, and Oracle Secure Backup makes initial configuration a simple process.

Perform the following four steps to perform initial configuration and prepare to backup a database to tape:

1. Define your Oracle Secure Backup Administrative Server in Oracle Enterprise Manager Database Control enabling the Oracle Secure Backup domain to be managed through Oracle Enterprise Manager.
2. Pre-authorize an Oracle Secure Backup user for use with RMAN allowing the RMAN backup/restore be performed without having to explicitly login to Oracle Secure Backup.
3. Set-up media policies in Oracle Secure Backup to be used for RMAN backups.
4. Establish RMAN backup settings such as parallelism and compression.

Note:

If you use Oracle Secure Backup or tape-side compression, do not also use RMAN compression.

See Also:

[Oracle Secure Backup Administrator's Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=OBADM197) for more information about using Recovery Manager with Oracle Secure Backup

### 8.4.2 Define Oracle Secure Backup Media Policies for Tape Backups

Once backup data stored on tape is no longer needed, its lifecycle is complete and the tape media can be reused. Management requirements during a tape's lifecycle (retention period) may include duplication and vaulting across multiple storage locations. Oracle Secure Backup provides effective media lifecycle management through user-defined media policies, including:

- Retention
- Tape duplication
- Vaulting: rotation of tapes between multiple locations

Media lifecycle management may be as simple as defining appropriate retention settings or more complex to include tape duplication with the original and duplicate(s) having different retention periods and vaulting requirements. Oracle Secure Backup media families, often referred to as tape pools, provide the media lifecycle management foundation.

The best practice recommendation is to leverage content-managed media families which use defined RMAN retention parameters associated with the database to determine when the tape may be reused (effectively an expired tape). A specific expiration date is not associated with content-managed tapes as is done with time-managed. The expiration or recycling of these tapes is based on the attribute associated with the backup images on the tape. All backup images written to content-managed tapes automatically have an associated "content-manages reuse" attribute. Since the recycling of content-managed tapes adheres to user-defined RMAN retention settings, RMAN instructs Oracle Secure Backup when to change the backup image attribute to "deleted".

The RMAN `DELETE` `OBSOLETE` command communicates which backup pieces (images) are no longer required to meet the user-defined RMAN retention periods. Once Oracle Secure Backup receives this communication, the backup image attribute is changed to "deleted". The actual backup image is not deleted but the attribute is updated within the Oracle Secure Backup catalog. Once all backup images on tape have a deleted attribute, Oracle Secure Backup considers the tape eligible for reuse, similar to that of an expired time-managed tape.

Oracle Secure Backup provides policy-based media management for RMAN backup operations through user-defined Database Backup Storage Selectors. One Database Backup Storage Selector (SSEL) may apply to multiple databases or multiple SSELs may be associated with a single database. For example, you would create two SSEL for a database when using RMAN duplexing and each copy should be written to a different media family. The SSEL contains the following information:

- Database name / ID or applicable to all databases
- Hostname or applicable to all hosts
- Content: archive logs, full, incremental, autobackup or applicable to all
- RMAN copy number (applicable when RMAN duplexing is configured)
- Media family name
- Name(s) of devices to which operations are restricted (if no device restrictions are configured, Oracle Secure Backup uses any available device)
- Wait time (duration) for available tape resources
- Encryption setting

Oracle Secure Backup automatically uses the storage selections defined within a SSEL without further user intervention. To override the storage selections for one time backup operations or other exceptions, define alternate media management parameters in the RMAN backup script. For more information, see:

`http://www.oracle.com/technetwork/database/secure-backup/documentation/index.html`

### 8.4.3 Create Tape Backups from the Fast Recovery Area

You can easily backup the Fast Recovery Area (FRA) to tape with the RMAN command: `BACKUP RECOVERY AREA`. Using this disk to tape backup method instead of performing a separate backup of the production database to tape provides a few distinct advantages:

- Saves tape consumption by creating an optimized backup of the Fast Recovery Area (FRA) thereby eliminating unnecessary backup of files already protected on tape
- Enables RMAN to use better restore intelligence from disk then tape as necessary, otherwise, RMAN would restore from the most recent backup regardless of media type
- Reduces I/O on the production database since the FRA uses a separate disk group

Upon restoration, RMAN automatically selects the most appropriate backup to restore from disk or tape. If the required backup is on tape, RMAN would restore or recovery the database directly from tape media through integration with Oracle Secure Backup. As RMAN has intimate knowledge of what files are necessary for recovery, restoration from disk or tape is an automated process.

While it is possible to backup the FRA or other RMAN disk backup to tape outside of RMAN by performing a file system backup of the disk area using the media management software, it is not recommended. If RMAN is not aware of the tape backup then restoration is an error-prone, manual process:

1. DBA must determine what files are needed for the restoration.
2. Media manager administrator would then restore designated files from tape backups to a disk location.
3. Once files on disk, DBA would initiate an RMAN restore or recovery from the disk location.

The combination of RMAN and Oracle Secure Backup provides an integrated Oracle database tape backup solution.

See Also:

[Oracle Database 2 Day DBA](https://docs.oracle.com/cd/E11882_01/server.112/e10897/backrest.htm#ADMQS09113) for more information about the Fast Recovery Area

### 8.4.4 Managing Offsite Backup Tapes

Backup tapes are highly portable and often stored at offsite locations for disaster recovery purposes. These tapes are first created from within a tape device but often are removed from the hardware device. Once backup tapes are removed from a hardware device the tapes may be stored in an on-site or offsite location. You can effectively manage tape movement between multiple locations using Oracle Secure Backup rotation policies.

For Oracle database restoration, a restore request is submitted from RMAN to Oracle Secure Backup. If the tapes are within the library, the restore begins immediately assuming device availability. However, if the tapes needed for restore could be offsite; you may want to confirm the location of tapes before you issue the restore command. With RMAN and Oracle Secure Backup you can easily do so by issuing the following RMAN command(s):

- `RESTORE DATABASE PREVIEW` command provides a list of tapes needed for restoration which are offsite.
- `RESTORE DATABASE PREVIEW RECALL` command initiates a recall operation through Oracle Secure Backup to return the tapes from offsite to the tape device for restoration. Once the tapes are on-site, you can begin the RMAN restore operation.

See Also:

- [Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/cd/E11882_01/backup.112/e10642/rcmcomre.htm#BRADV89768) for more information about recalling offsite backups with RMAN
- [Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/cd/E11882_01/backup.112/e10642/rcmcomre.htm#BRADV8140) for more information about previewing backups used in restore operations

## 8.5 Backup and Recovery Operations and Maintenance Best Practices

This section outlines procedures to regularly check for corruption of data files using the Data Recovery Advisor, for testing recovery procedures, and for backing up the recovery catalog database.

### 8.5.1 Diagnose Data Failures and Present Repair Options

Data Recovery Advisor is an Oracle Database tool that automatically diagnoses data failures, determines and presents appropriate repair options, and executes repairs at the user's request. In this context, a data failure is a corruption or loss of persistent data on disk. By providing a centralized tool for automated data repair, Data Recovery Advisor improves the manageability and reliability of an Oracle database and thus helps reduce the mean time to recover (MTTR).

See Also:

[Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/cd/E11882_01/backup.112/e10642/rcmrepai.htm#BRADV246) for information about using Data Recovery Advisor

### 8.5.2 Regularly Check Database Files for Corruption

Use the RMAN `VALIDATE` command to regularly check database files for block corruption that has not yet been reported by a user session or by normal backup operations. RMAN scans the specified files and checks for physical and logical errors, but does not actually perform the backup or recovery operation. Oracle database records the address of the corrupt block and the type of corruption in the control file. Access these records through the `V$DATABASE_BLOCK_CORRUPTION` view, which can be used by RMAN block media recovery.

To detect all types of corruption that are possible to detect, specify the `CHECK LOGICAL` option.

See Also:

[Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/cd/E11882_01/backup.112/e10642/rcmvalid.htm#BRADV90063) for information about Validating Database Files and Backups

### 8.5.3 Periodically Test Recovery Procedures

Complete, successful, and tested backups are fundamental to the success of any recovery. Create test plans for different outage types. Start with the most common outage types and progress to the least probable. Using the RMAN `DUPLICATE` command is a good way to perform recovery testing, because it requires restoring from backups and performing media recovery.

Monitor the backup procedure for errors, and validate backups by testing your recovery procedures periodically. Also, validate the ability to restore the database using the RMAN command `RESTORE...VALIDATE`.

See Also:

- [Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/cd/E11882_01/backup.112/e10642/rcmdupdb.htm#BRADV010) for information about `DUPLICATE` command
- [Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/cd/E11882_01/backup.112/e10642/rcmvalid.htm#BRADV8156) for information about validating backups before restoring them

### 8.5.4 Backup the RMAN and Oracle Secure Backup Catalogs on a Regular Basis

Include the recovery catalog database in your backup and recovery strategy. If you do not back up the recovery catalog and a disk failure occurs that destroys the recovery catalog database, then you may lose the metadata in the catalog. Without the recovery catalog contents, recovery of your other databases is likely to be more difficult.

The Oracle Secure Backup catalog maintains backup metadata, scheduling and configuration details for the backup domain. Just as it's important to protect the RMAN catalog or control file, the Oracle Secure Backup catalog should be backed up on a regular basis.

See Also:

- [Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/cd/E11882_01/backup.112/e10642/rcmcatdb.htm#BRADV8015) for information about managing a recovery catalog
- [Oracle Secure Backup Administrator's Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=OBADM) for information about the Oracle Secure Backup administrative server backup catalog

### 8.5.5 Use Procedures to Backup Files Outside the Database

Oracle Secure Backup provides tape backup for non-Oracle files. Oracle Secure Backup does not have pro-active checking as the database does. Use the features available to backup files outside the database. For more information, see Section 8.6, "Backup Files Outside the Database".

## 8.6 Backup Files Outside the Database

Oracle IT environments include both database and application files that must be protected for short and long-term retention requirements. Differences exist between backing up database and unstructured files. In addition, managing backup and recovery often crosses organizational areas such as DBA for the database and system administration for file system data could cross organizational areas. The Oracle data protection suite offers a cohesive solution meeting your complete needs for Oracle database and non Oracle database storage.

### 8.6.1 ACFS Snapshots

An Oracle ACFS snapshot is an online, read-only, point in time copy of an Oracle ACFS file system. The snapshot copy is space-efficient and uses Copy-On-Write functionality. Before an Oracle ACFS file extent is modified or deleted, its current value is copied to the snapshot to maintain the point-in-time view of the file system.

Oracle ACFS snapshot can support the online recovery of files inadvertently modified or deleted from a file system. With up to 63 snapshot views supported for each file system, flexible online file recovery solutions spanning multiple views can be employed. An Oracle ACFS snapshot can also be used as the source of a file system backup, as it can be created on demand to deliver a current, consistent, online view of an active file system.

See Also:

- [Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e18951/asmfilesystem.htm#OSTMG33000) for more information About Oracle ACFS Snapshots
- [Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e18951/asmfs_em.htm#OSTMG29100) for information about Managing Oracle ACFS Snapshots with Oracle Enterprise Manager

### 8.6.2 Oracle Sun ZFS Storage Appliance Snapshots

Oracle's Sun ZFS Storage Appliance provides an integrated high performance backup solution and is also a cost effective platform for disaster recovery for non-Database files. Ever-growing amounts of data present system and database administrators with many challenges—the thorniest of which are associated with the complex process of backup and recovery. Without reliable data protection and processes, mission-critical data is at risk.

Oracle's Sun ZFS Storage Appliance is an easy-to-deploy Unified Storage System that ensures that backup window and recovery time objectives (RTO) are met by providing timely recovery in the event of a disaster.

Oracle's Sun ZFS Storage Appliance supports unlimited snapshot capability. A snapshot similar to Oracle ACFS is a read-only, point-in-time copy of a file system (for information about Oracle ACFS, see Section 8.6.1, "ACFS Snapshots"). It is instantaneously created and no space is allocated initially. Blocks are allocated as changes are made to the base file system (copy-on-write). The snapshots are either initiated manually or can be automated by scheduling at specific intervals. The snapshot data can be directly accessed for any backup purposes. Any reads to the snapshot blocks are served by the base file system's block. When changes happen to the base file system, the older block is now referenced by the snapshot and the new changed block is referenced by the file system.

Oracle's Sun ZFS Storage Appliance is also recommended for development and test systems that are snapshots taken from the standby database in a Data Guard environment.

Snapshot rollback is the process to bring the base file system to the point in time when the snapshot is taken. The rollback process discards all the changes that happened to the base file system from the time of the snapshot to the time of rollback. This removes the need for a data restore process.

See Also:

- `http://www.oracle.com/products/servers-storage/storage/nas/resources/index.html` for documentation on Oracle's Sun ZFS Storage Appliance
- The MAA white paper "Oracle Database Cloning Solution Using Oracle's Sun ZFS Storage Appliance And Oracle Data Guard" from the MAA Best Practices area for Oracle Database at
	`http://www.oracle.com/goto/maa`
- The MAA white paper "Oracle Database Cloning Using Oracle Recovery Manager and Sun ZFS Storage Appliance" from the MAA Best Practices area for Oracle Databases at
	`http://www.oracle.com/goto/maa`

### 8.6.3 Tape Backups

Oracle Secure Backup provides centralized tape backup management for heterogeneous file system data and the Oracle database. Oracle Secure Backup offers multiple backups levels with full, cumulative and differential incrementals. For more information, see Section 8.4, "Backup to Tape Best Practices". In addition, a full offsite backup level may be scheduled without interfering with the regular full/incremental schedule. File system backups can be performed at the file, directory, file system, or raw partition level meeting even the most stringent requirements within user-defined backup windows.

For file system backup operations, you define Oracle Secure Backup "datasets" which describes what to backup. A dataset is a textual description employing a lightweight language to communicate how to build and organize files to be protected. Being Oracle Database aware, Oracle Secure Backup can skip database files during file system backups by using the "exclude oracle database files" directive within the dataset.

See Also:

The [Oracle Secure Backup Administrator's Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=OBADM220) for more information about file system backup operations