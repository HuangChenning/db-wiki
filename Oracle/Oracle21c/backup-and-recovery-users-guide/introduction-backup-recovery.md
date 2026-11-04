---
title: "Backup and Recovery User's Guide"
book: "Database Backup and Recovery User's Guide"
doc_id: F31836-11
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/bradv/introduction-backup-recovery.html
tags:
  - oracle
  - 21c
  - backup-and-recovery-users-guide
---

Become familiar with Oracle Database backup and recovery solutions.

Note:

To get started with Recovery Manager (RMAN) right away, proceed to [Getting Started with RMAN](getting-started-rman.md).

### 1.1 Purpose of Backup and Recovery

As a backup administrator, your principal duty is to devise, implement, and manage a backup and recovery strategy.

In general, the purpose of a [backup and recovery](glossary.md) strategy is to protect the database against data loss and reconstruct the database after data loss. Typically, backup administration tasks include the following:

- Planning and testing responses to different kinds of failures
- Configuring the database environment for backup and recovery
- Setting up a backup schedule
- Monitoring the backup and recovery environment
- Troubleshooting backup problems
- Recovering from data loss if the need arises

As a backup administrator, you may also be asked to perform other duties that are related to backup and recovery:

- Data archival, which involves creating a database copy for long-term storage
- Data transfer, which involves moving data from one database or one host to another

The purpose of this manual is to explain how to perform the preceding tasks.

#### 1.1.1 About Data Protection

As a backup administrator, your primary job is making and monitoring backups for data protection.

A [backup](glossary.md) is a copy of data of a database that you can use to reconstruct data. A backup can be either a [physical backup](glossary.md) or a [logical backup](glossary.md).

Physical backups are copies of the physical files used in storing and recovering a database. These files include data files, control files, and archived redo logs. Ultimately, every physical backup is a copy of files that store database information to another location, whether on disk or on offline storage media such as tape.

Logical backups contain logical data such as tables and stored procedures. You can use Oracle Data Pump to export logical data to binary files, which you can later import into the database. The Data Pump command-line clients `expdp` and `impdp` use the `DBMS_DATAPUMP` and `DBMS_METADATA` PL/SQL packages.

Physical backups are the foundation of any sound backup and recovery strategy. Logical backups are a useful supplement to physical backups in many circumstances but are not sufficient protection against data loss without physical backups.

Unless otherwise specified, the term backup as used in the backup and recovery documentation refers to a physical backup. Backing up a database is the act of making a physical backup. The focus in the backup and recovery documentation set is almost exclusively on physical backups.

Most of this manual focuses on RMAN-based backup and recovery. The most noteworthy are the following:

- Incremental backups
	An [incremental backup](glossary.md) stores only blocks changed since a previous backup. Thus, they provide more compact backups and faster recovery, thereby reducing the need to apply redo during [data file media recovery](glossary.md). If you enable [block change tracking](glossary.md), then you can improve performance by avoiding full scans of every input data file. You use the [`BACKUP INCREMENTAL`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=RCMRF107) command to perform incremental backups.
- Block media recovery
	You can repair a data file with only a small number of corrupt data blocks without taking it offline or restoring it from backup. You use the [`RECOVER BLOCK`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=RCMRF140) command to perform [block media recovery](glossary.md).
- Binary compression
	A [binary compression](glossary.md) mechanism integrated into Oracle Database reduces the size of backups.
- Encrypted backups
	RMAN uses [backup encryption](glossary.md) capabilities integrated into Oracle Database to store backup sets in an encrypted format. To create encrypted backups on disk, the database must use the Advanced Security Option. To create encrypted backups directly on tape, RMAN must use the Oracle Secure Backup SBT interface, but does not require the Advanced Security Option.
- Automated database duplication
	Easily create a copy of your database, supporting various storage configurations, including direct duplication between ASM databases.
- Cross-platform data conversion

Whether you use RMAN or user-managed methods, you can supplement physical backups with logical backups of schema objects made with Data Pump Export utility. You can later use Data Pump Import to re-create data after restore and recovery. Logical backups are mostly beyond the scope of the backup and recovery documentation.

See Also:

- [Backing Up the Database](backing-up-database.md)
- [Performing User-Managed Backup and Recovery](part-user-managed-backup-recovery.md)

#### 1.1.2 About Failures that Require Database Recovery

Although several problems can halt the normal operation of an Oracle Database or affect database I/O operations, not all of them require DBA intervention.

The following problems typically require DBA intervention and data recovery: [media failure](glossary.md), user errors, and application errors. Other failures may require DBA intervention without causing data loss or requiring recovery from backup. For example, you may need to restart the database after an instance failure or allocate more disk space after statement failure because of a full data file.

Media Failures

A media failure is a physical problem with a disk that causes a failure of a read from or write to a disk file that is required to run the database. Any database file can be vulnerable to a media failure. The appropriate recovery technique following a media failure depends on the files affected and the types of backup available.

One particularly important aspect of backup and recovery is developing a [disaster recovery](glossary.md) strategy to protect against catastrophic data loss, for example, the loss of an entire database host.

User Errors

User errors occur when, either due to an error in application logic or a manual mistake, data in a database is changed or deleted incorrectly. User errors are estimated to be the greatest single cause of database downtime.

Data loss due to user error can be either localized or widespread. An example of localized damage is deleting the wrong person from the employees table. This type of damage requires surgical detection and repair. An example of widespread damage is a batch job that deletes the company orders for the current month. In this case, drastic action is required to avoid a extensive database downtime.

While user training and careful management of privileges can prevent most user errors, your backup strategy determines how gracefully you recover the lost data when user error does cause data loss.

Application Errors

Sometimes a software malfunction can corrupt data blocks. In a [physical corruption](glossary.md), which is also called a media corruption, the database does not recognize the block at all: the [checksum](glossary.md) is invalid, the block contains all zeros, or the header and footer of the block do not match. If the corruption is not extensive, then you can often repair it easily with [block media recovery](glossary.md).

See Also:

[Oracle Database Utilities](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=SUTIL100) to learn how to use Data Pump

#### 1.1.3 About Data Archival

Data archival, although related to data protection, serves a different purpose. An archival backup is exempted from the normal backup and recovery strategy. These backups are typically archived onto separate storage media and retained for long periods.

For example, you may need to preserve a copy of a database as it existed at the end of a business quarter. This backup is not part of the disaster recovery strategy. The media to which these backups are written are often unavailable after the backup is complete. You may send the tape into fire storage or ship a portable hard drive to a testing facility. RMAN provides a convenient way to create a backup and exempt it from your [backup retention policy](glossary.md). This type of backup is known as an [archival backup](glossary.md).

See Also:

[Making Database Backups for Long-Term Storage](backing-up-database.md)

#### 1.1.4 About Data Transfer

RMAN backups can be used to transport databases and tablespaces across different platforms.

In some situations you may need to take a backup of a database or database component and move it to another location. For example, you can use Recovery Manager (RMAN) to create a database copy, create a tablespace copy that can be imported into another database, or move an entire database from one platform to another. These tasks are not strictly speaking part of a backup and recovery strategy, but they do require the use of database backups, and so may be included in the duties of a backup administrator.

See Also:

The chapters in [Transferring Data with RMAN](part-transfering-data-rman.md)

### 1.2 Oracle Backup and Recovery Solutions

Oracle provides multiple solutions for performing backup and recovery.

The following solutions are available when implementing a backup and recovery strategy:

- [Recovery Manager (RMAN)](glossary.md)
	Recovery Manager is fully integrated with the Oracle Database to perform a range of backup and recovery activities, including maintaining an [RMAN repository](glossary.md) of historical data about backups. You can access RMAN through the command line or through Oracle Enterprise Manager.
- [Oracle Enterprise Manager Cloud Control](glossary.md)
	Oracle Enterprise Manager Cloud Control (Cloud Control) provides a graphical front end and scheduling facilities for RMAN. You enter job parameters, specify a job schedule, and Cloud Control runs RMAN to conduct the backup and recovery operations.
- [Zero Data Loss Recovery Appliance (Recovery Appliance)](glossary.md)
	Recovery Appliance is a cloud-scale Engineered System that provides data protection for all Oracle Databases in the enterprise. Integrated with RMAN and Cloud Control, the Recovery Appliance provides a single repository for backups of multiple databases as described in " About Zero Data Loss Recovery Appliance ".
- User-managed backup and recovery
	In this solution, you perform backup and recovery with a mixture of host operating system commands and SQL\*Plus recovery commands. You are responsible for determining all aspects of when and how backups and recovery are done.

These solutions are supported by Oracle and are fully documented, but RMAN is the preferred solution for database backup and recovery. RMAN provides a common interface for backup tasks across different host operating systems, and offers several backup techniques not available through user-managed methods.

See Also:

" RMAN and Oracle Enterprise Manager Cloud Control "

### 1.3 Comparison of Oracle Backup Techniques

You can use multiple techniques to create backups of the Oracle Database. This section compares the Recovery Manager (RMAN), user-managed backups, and Data Pump techniques.

Table 1-1 summarizes the features of the different backup techniques.

Table 1-1 Feature Comparison of Backup Techniques

| Feature | Recovery Manager | User-Managed |
| --- | --- | --- |
| Closed database backups | Supported. Requires instance to be mounted. | Supported. |
| Open database backups | Supported. No need to use `BEGIN` / `END` `BACKUP` statements. | Supported. Must use `BEGIN` / `END` `BACKUP` statements. |
| Incremental backups | Supported. | Not supported. |
| Corrupt block detection | Supported. Identifies corrupt blocks and logs in `V$DATABASE_BLOCK_CORRUPTION`. | Not supported. |
| Automatic specification of files to include in a backup | Supported. Establishes the name and locations of all files to be backed up (whole database, tablespaces, data files, control files, and so on). | Not supported. Files to be backed up must be located and copied manually. |
| Backup repository | Supported. Backups are recorded in the control file, which is the main repository of RMAN metadata. Additionally, you can store this metadata in a recovery catalog, which is a schema in a different database. | Not supported. DBA must keep own records of backups. |
| Backups to a media manager | Supported. Interfaces with a media mnagement software. RMAN also supports proxy copy, a feature that enables a media manager to manage completely the transfer of data between disk and backup media. | Supported. Backup to tape is manual or controlled by a media manager. |
| Backup of initialization parameter file | Supported. | Supported. |
| Backup of password and networking files | Not supported. | Supported. |
| Platform-independent language for backups | Supported. | Not supported. |
| Backups to Oracle Cloud Infrastructure | Supported. | Supported. |

### 1.4 About Oracle Flashback Technology

Oracle Flashback technology provides a set of features that complements your physical backup and recovery strategy.

[Oracle Flashback Technology](glossary.md) provides an additional layer of data protection. Specifically, you can use the various features of Oracle Flashback to view past states of data and rewind your database without restoring backups or performing [point-in-time recovery](glossary.md). In general, flashback features are more efficient and less disruptive than media recovery in most situations in which they apply.

Oracle Flashback Technology enables you to use the following functionality:

- Logical Flashback Features
- Flashback Database

#### 1.4.1 Logical Flashback Features

The logical-level flashback features of Oracle Database do not depend on RMAN and are available whether or not RMAN is part of your backup strategy.

Most of the flashback features of Oracle operate at the logical level, enabling you to view and manipulate database objects. Except for Oracle Flashback Drop, the logical flashback features rely on **undo data**, which are records of the effects of each database update and the values overwritten in the update.

Oracle Database includes the following logical flashback features:

- Oracle Flashback Query
	You can specify a target time and run queries against a database, viewing results as they would appear at the target time. To recover from an unwanted change like an update to a table, you could choose a target time before the error and run a query to retrieve the contents of the lost rows. [Oracle Database Development Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=ADFNS1008) explains how to use this feature.
- Oracle Flashback Version Query
	You can view all versions of all rows that ever existed in one or more tables in a specified time interval. You can also retrieve metadata about the differing versions of the rows, including start and end time, operation, and transaction ID of the transaction that created the version. You can use this feature to recover lost data values and to audit changes to the tables queried. [Oracle Database Development Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=ADFNS1008) explains how to use this feature.
- Oracle Flashback Transaction Query
	You can view changes made by a single transaction, or by all the transactions during a specific time period. [Oracle Database Development Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=ADFNS1008) explains how to use this feature.
- Oracle Flashback Transaction
	You can reverse a transaction. Oracle Database determines the dependencies between transactions and in effect creates a compensating transaction that reverses the unwanted changes. The database rewinds to a state as if the transaction, and any transactions that could be dependent on it, had never happened. [Oracle Database Development Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=ADFNS1008) explains how to use this feature.
- Oracle Flashback Table
	You can recover a table or set of tables to a specified point in time earlier without taking any part of the database offline. In many cases, Flashback Table eliminates the need to perform more complicated point-in-time recovery operations. Flashback Table restores tables while automatically maintaining associated attributes such as current indexes, triggers, and constraints, and in this way enabling you to avoid finding and restoring database-specific properties. " [Rewinding a Table with Flashback Table](rman-performing-flashback-dbpitr.md) " explains how to use this feature.
- Oracle Flashback Drop
	You can reverse the effects of a `DROP` `TABLE ` statement. " [Rewinding a DROP TABLE Operation with Flashback Drop](rman-performing-flashback-dbpitr.md) " explains how to use this feature.

A [flashback data archive](glossary.md) enables you to use some logical flashback features to access data from far back in the past. A flashback data archive consists of one or more tablespaces or parts of tablespaces. When you create a flashback data archive, you specify the name, retention period, and tablespace. You can also specify a default flashback data archive. The database automatically purges old historical data the day after the retention period expires.

You can turn flashback archiving on and off for individual tables. By default, flashback archiving is turned off for every table.

See Also:

- [Performing Flashback and Database Point-in-Time Recovery](rman-performing-flashback-dbpitr.md) to learn how to perform Flashback Table and Flashback Drop
- [Oracle Database Development Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=ADFNS1008) for more information on the logical flashback features

#### 1.4.2 Flashback Database

Flashback Database enables you to revert an Oracle Database to a previous point in time.

At the physical level, [Oracle Flashback Database](glossary.md) provides a more efficient data protection alternative to [database point-in-time recovery (DBPITR)](glossary.md). If the current data files have unwanted changes, then you can use the RMAN command [`FLASHBACK DATABASE`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=RCMRF194) to revert the data files to their contents at a past time. The end product is much like the result of a DBPITR, but is generally much faster because it does not require restoring data files from backup and requires less redo than media recovery.

Flashback Database uses [flashback logs](glossary.md) to access past versions of data blocks and some information from archived redo logs. Flashback Database requires that you configure a [fast recovery area](glossary.md) for a database because the flashback logs can only be stored there. Flashback logging is not enabled by default. Space used for flashback logs is managed automatically by the database and balanced against space required for other files in the fast recovery area.

Oracle Database also supports restore points along with Flashback Database and backup and recovery. A [restore point](glossary.md) is an alias corresponding to a [system change number (SCN)](glossary.md). You can create a restore point at any time if you anticipate needing to return part or all of a database to its contents at that time. A [guaranteed restore point](glossary.md) ensures that you can use Flashback Database to return a database to the time of the restore point.

See Also:

" [Rewinding a Database with Flashback Database](rman-performing-flashback-dbpitr.md) " to learn how to perform Flashback Database with the [`FLASHBACK DATABASE`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=RCMRF194) command

### 1.5 About Data Recovery Advisor

The Data Recovery Advisor provides a single point of entry for Oracle backup and recovery solutions. It is a tool that automatically diagnoses persistent data failures, presents appropriate repair options, and performs repairs at your request.

You can use the [Data Recovery Advisor](glossary.md) through Oracle Enterprise Manager or through the RMAN command-line client.

Note:

Starting in Oracle Database 19c, the Data Recovery Advisor (DRA) feature is deprecated.

The deprecation of DRA includes deprecation of the following Oracle Recovery Manager (RMAN) commands: `LIST FAILURE`, `ADVISE FAILURE`, `REPAIR                     FAILURE`, and `CHANGE FAILURE`. Database administrators will no longer have access to these commands. There is no replacement feature for DRA.

A database failure usually manifests itself as a set of symptoms: error messages, alerts, trace files and dumps, and failed data integrity checks. Data Recovery Advisor automatically diagnoses and informs you of these failures. For Data Recovery Advisor, a [failure](glossary.md) is a persistent data corruption that can be directly mapped to a set of repair actions. Each failure has a status of open or closed. Each failure also has a priority of critical, high, or low.

Failures are detected by data integrity checks, which are diagnostic procedures to assess the health of the database or its components. If a [data integrity check](glossary.md) reveals a failure, then Data Recovery Advisor automatically assesses the effect of a set of failures and maps it to a set of repair options. Usually, Data Recovery Advisor presents both automated and manual repair options.

Data Recovery Advisor determines the best automated repair option and its effect on the database. The [repair option](glossary.md) may include repairs such as data file restore and recovery, media recovery, Flashback Database, and so on. Before presenting an automated repair option, Data Recovery Advisor validates it for the specific environment and the availability of media components required to complete the proposed repair.

If you choose an automated repair option, then RMAN coordinates sessions on the Oracle Database to perform the [repair](glossary.md) for you. The Data Recovery Advisor tool verifies the repair success and closes the appropriate failures.

See Also:

[Diagnosing and Repairing Failures with Data Recovery Advisor](diagnosing-repairing-failures-dra.md), to learn how to use Data Recovery Advisor

### 1.6 RMAN and Oracle Enterprise Manager Cloud Control

RMAN functionality can also be accessed using Oracle Enterprise Manager Cloud Control.

This section contains:

- About Oracle Enterprise Manager Cloud Control
- Accessing the Database Home Page Using Cloud Control
- Performing Backup and Recovery Tasks with Cloud Control

#### 1.6.1 About Oracle Enterprise Manager Cloud Control

Oracle Enterprise Manager Cloud Control (Cloud Control) is a browser-based management interface for Oracle Database.

Cloud Control provides a graphical front end and scheduling facilities for RMAN. You enter job parameters, specify a job schedule, and Cloud Control runs RMAN at the designated time or designated repeat interval to conduct the backup and recovery operations. Cloud Control provides access to RMAN through a set of wizards. These wizards lead you through a variety of recovery procedures based on an analysis of your database, your available backups, and your data recovery objectives.

By using Cloud Control, you can perform the simpler restore and recovery scenarios outlined in this documentation. You can also use more sophisticated restore and recovery techniques such as point-in-time recovery and Oracle Flashback operations, which allow for efficient repair of media failures and user errors. Using Cloud Control is often simpler than the RMAN command-line client.

To use Cloud Control, you start by accessing the Database Home page as described in Accessing the Database Home Page Using Cloud Control.

Performing Backup and Recovery Tasks with Cloud Control describes how to use Cloud Control for backup and recovery.

#### 1.6.2 Accessing the Database Home Page Using Cloud Control

The Database Home page is the main database management page in Oracle Enterprise Manager Cloud Control (Cloud Control).

After you log in to Cloud Control, you go to the Database Home page for the target database for backup and recovery tasks.

To access the Database Home page in Cloud Control:

1. Start Cloud Control.
	The URL for accessing Cloud Control has the following syntax:
	```
	http://hostname.domain:portnumber/em
	```
	Obtain the URL from your Oracle Enterprise Manager administrator or your database administrator.
2. On the Welcome page, enter your Cloud Control user name and password, and then click Login.
3. From the Targets menu, select Databases.
4. On the Databases page, if not already selected, select Search List to display a list of the available target databases.
5. Select the target database that you want to modify by clicking the database name.
	The home page for the target database appears. The first time that you interact with the database (for example, by selecting from the menu options), the Database Login page appears.
6. On the login page for the target database, log in as a user with the appropriate privileges. For example, to log in as user `SYS` with the `SYSDBA` privilege:
	- User Name: Enter `SYS`.
		- Password: Enter the `SYS` user's password.
		- Connect As: From the list, select Sysdba Role.

#### 1.6.3 Performing Backup and Recovery Tasks with Cloud Control

You can perform a variety of both simple and advanced backup and recovery tasks with Oracle Enterprise Manager Cloud Control (Cloud Control).

To perform backup and recovery tasks with Cloud Control:

1. Access the Database Home page for the target database as described in Accessing the Database Home Page Using Cloud Control.
2. From the Availability menu, select Backup and Recovery, and then select an option.

### 1.7 About Zero Data Loss Recovery Appliance

Zero Data Loss Recovery Appliance (Recovery Appliance) is a cloud-scale Engineered System that is designed to protect all the Oracle Databases in your enterprise. It achieves significant efficiencies in performance and manageability of backups by offloading most Oracle Database backup and restore processing to a centralized Recovery Appliance.

Recovery Appliance stores and manages backups of multiple databases on a unified disk pool, using an incremental-forever backup strategy described in " [About the Incremental-Forever Backup Strategy for Recovery Appliance](rman-backup-concepts.md) ". It continually compresses, deduplicates, and validates backups at the Oracle block level, while quickly creating full virtual backups on demand.

See Also:

[Zero Data Loss Recovery Appliance Protected Database Configuration Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=AMPDB760) for information about the advantages of Recovery Appliance

Multiple client databases—known as protected databases—share a single, centrally-managed Recovery Appliance catalog that resides on the Recovery Appliance. All protected databases that send backups to Recovery Appliance must use this catalog. Virtual private catalog technology enforces separation of duties among the protected database DBAs and the Recovery Appliance administrator.

Real-time redo transport minimizes the window of potential data loss that exists between successive archived log backups. Redo data from the protected database is written directly to the recovery appliance as it is generated.

Recovery Appliance is integrated with Cloud Control and RMAN. An accompanying media management library is used for communication between RMAN and Recovery Appliance. Cloud Control enables administrators to centrally manage and monitor the data protection of all protected databases in the enterprise.

Oracle Secure Backup, the tape management component of Recovery Appliance, is preinstalled on Recovery Appliance. For disaster recovery, Recovery Appliance can replicate backups to other Recovery Appliances. A single Recovery Appliance can service multiple protected databases of different versions and from different platforms.

See Also:

- [Zero Data Loss Recovery Appliance Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=AMAGD199)
- [Zero Data Loss Recovery Appliance Protected Database Configuration Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=AMPDB623)

#### 1.7.1 Using RMAN with Recovery Appliance

You can use most RMAN commands to back up to and recover from Zero Data Loss Recovery Appliance (Recovery Appliance).

To make backups to Recovery Appliance, you must first set the required configuration parameters and allocate one or more SBT channels.

See Also:

- [About RMAN in a Recovery Appliance Environment](rman-architecture.md)
- [About Real-time Redo Transport for Recovery Appliance](rman-complete-database-recovery.md)
- [About the Incremental-Forever Backup Strategy for Recovery Appliance](rman-backup-concepts.md)
- [Configuring RMAN to Make Backups to Recovery Appliance](configuring-rman-client-basic.md)
- [Zero Data Loss Recovery Appliance Protected Databases Configuration Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/bradv&id=AMPDB752) for information about RMAN commands with modified behavior in Recovery Appliance

### 1.8 Backup and Recovery Documentation Roadmap

The backup and recovery documentation roadmap is divided into two main paths: RMAN and user-managed backup and recovery. Optional paths are shown as splitting off and then rejoining each main path.

Figure 1-1 illustrates the recommended way to navigate the backup and recovery documentation. You can either implement your backup and recovery strategy with RMAN, which is recommended, or with user-managed tools.

Figure 1-1 Backup and Recovery Documentation Roadmap

![Figure 1-1 Backup and Recovery Documentation Roadmap](img/bradv043.png)

> This graphic illustrates the backup and recovery documentation roadmap. The graphic resembles a flow chart and at the top is the Backup and Recovery Concepts in the Concepts Guide. All items following this one are chapters in the Backup and Recovery User's Guide. The second box represents the Introduction to Backup and Recovery chapter. After this box, there are two separate branches.
>
> The path on the right represents the user-managed recovery and contains boxes that represent the following chapters, in the order listed: Backing Up the Database and Performing Database Flashback and Recovery. This box can either lead to the End box directly or through the Performing Database Recovery: Advanced.
>
> The other path represents backup and recovery operations performed using RMAN and it contains the following boxes, from top to bottom, in the order listed: Starting RMAN, Configuring the RMAN Environment, Backing Up the Database, Reporting on RMAN Operations, Maintaining RMAN Backups, Using the Data Recovery Advisor, Performing Flashback and DBPITR, and Performing Complete Database Recovery. After this, there are two paths, one of which connects directly to the box labeled End. The other path connect to End through the following boxes, listed from top to bottom: Performing Block Media Library, Performing Advanced RMAN Recovery, and Tuning RMAN Performance.


Note:

Starting in Oracle Database 19c, the Data Recovery Advisor (DRA) feature is deprecated.

The deprecation of DRA includes deprecation of the following Oracle Recovery Manager (RMAN) commands: `LIST FAILURE`, `ADVISE FAILURE`, `REPAIR                     FAILURE`, and `CHANGE FAILURE`. Database administrators will no longer have access to these commands. There is no replacement feature for DRA.

#### 1.8.1 Recovery Manager Documentation Roadmap

This section provides a roadmap for navigating the backup and recovery documentation when using RMAN as your principal backup and recovery solution.

Begin by reading " [Getting Started with RMAN](getting-started-rman.md) ". This brief chapter, which explains the most basic RMAN techniques, may be adequate for your purposes. For a more comprehensive explanation of how to implement a backup and recovery strategy with RMAN, read the chapters in the following order (optional chapters are not listed):

1. Read " [Starting and Interacting with the RMAN Client](starting-interacting-with-rman-client.md) ".
	This chapter explains how to start the RMAN client and connect to databases.
2. Read " [Configuring the RMAN Environment](configuring-rman-client-basic.md) ".
	This chapter explains how to perform basic tasks such as configuring a [fast recovery area](glossary.md), [backup retention policy](glossary.md), and [archived redo log deletion policy](glossary.md).
3. Read " [Backing Up the Database](backing-up-database.md) ".
	This chapter explains how to implement a basic backup strategy.
4. Read " [Reporting on RMAN Operations](reporting-rman-operations.md) ".
	This chapter explains how to monitor RMAN backup and recovery operations. Specifically, the chapter explains how to use the reporting commands (`LIST`, `REPORT`, and `SHOW`) and the relevant V$ and recovery catalog views.
5. Read " [Maintaining RMAN Backups and Repository Records](maintaining-rman-backups.md) ".
	This chapter explains how to verify the existence of backups, change the repository status of backups, delete backups, and perform other maintenance tasks.
6. Read " [Diagnosing and Repairing Failures with Data Recovery Advisor](diagnosing-repairing-failures-dra.md) ".
	This chapter explains how to use the Data Recovery Advisor tool. You can use it to list failures, obtain advice about to respond to these failures, and in some cases automatically repair the failures.
	Note:
	Starting in Oracle Database 19c, the Data Recovery Advisor (DRA) feature is deprecated.
	The deprecation of DRA includes deprecation of the following Oracle Recovery Manager (RMAN) commands: `LIST FAILURE`, `ADVISE FAILURE`, `REPAIR                     FAILURE`, and `CHANGE FAILURE`. Database administrators will no longer have access to these commands. There is no replacement feature for DRA.
7. Read " [Performing Flashback and Database Point-in-Time Recovery](rman-performing-flashback-dbpitr.md) ".
	This chapter explains how to use the `FLASHBACK DATABASE` command and perform point-in-time recovery with the `RECOVER DATABASE` command.
8. Read " [Performing Complete Database Recovery](rman-complete-database-recovery.md) ".
	This chapter explains how to recover individual tablespaces or the database.

#### 1.8.2 User-Managed Backup and Recovery Documentation Roadmap

This section provides a roadmap for navigating the backup and recovery documentation when you do not use RMAN as your principal backup and recovery solution.

In this case, you must use third-party tools to make your backups and SQL or SQL\*Plus commands to perform recovery. Read the chapters in the following order:

1. Read [Making User-Managed Database Backups](user-managed-database-backups.md).
	This chapter explains how to make backups with third-party tools.
2. Read [Performing User-Managed Database Flashback and Recovery](user-managed-flashback-dbpitr.md).
	This chapter explains how to use the SQL statement `FLASHBACK DATABASE` and to perform recovery with the SQL\*Plus `RECOVER` command.
3. Read [Performing User-Managed Recovery: Advanced Scenarios](user-managed-recovery-advanced.md).
	This chapter explains various recovery scenarios.