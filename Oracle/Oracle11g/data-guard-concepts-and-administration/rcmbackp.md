---
title: Creating a Standby Database with Recovery Manager
book: Data Guard Concepts and Administration
doc_id: E41134-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e41134/rcmbackp.htm
tags:
  - oracle
  - 11g
  - data-guard-concepts-and-administration
---

## E Creating a Standby Database with Recovery Manager

This appendix describes how to use Oracle Recovery Manager to create a standby database. This appendix contains the following topics:

## E.1 Prerequisites

This appendix assumes that you have read the chapter on database duplication in [Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/cd/E11882_01/backup.112/e10642/rcmdupdb.htm#BRADV010). Because you use the `DUPLICATE` command to create a standby database with RMAN, you should familiarize yourself with the `DUPLICATE` command entry in [Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta020.htm#RCMRF126).

Familiarize yourself with how to create a standby database in [Chapter 3, "Creating a Physical Standby Database"](create_ps.md) and [Chapter 4, "Creating a Logical Standby Database"](create_ls.md) before you attempt the RMAN creation procedures described in this chapter.

## E.2 Overview of Standby Database Creation with RMAN

This section explains the purpose and basic concepts involved in standby database creation with RMAN.

### E.2.1 Purpose of Standby Database Creation with RMAN

You can use either manual techniques or the RMAN `DUPLICATE` command to create a standby database from backups of your primary database. Creating a standby database with RMAN has the following advantages over manual techniques:

- RMAN can create a standby database by copying the files currently in use by the primary database. No backups are required.
- RMAN can create a standby database by restoring backups of the primary database to the standby site. Thus, the primary database is not affected during the creation of the standby database.
- RMAN automates renaming of files, including Oracle Managed Files (OMF) and directory structures.
- RMAN restores archived redo log files from backups and performs media recovery so that the standby and primary databases are synchronized.

### E.2.2 Basic Concepts of Standby Creation with RMAN

The procedure for creating a standby database with RMAN is almost the same as for creating a duplicate database. You need to amend the duplication procedures described in [Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/cd/E11882_01/backup.112/e10642/toc.htm) to account for issues specific to a standby database.

To create a standby database with the `DUPLICATE` command you must connect as target to the primary database and specify the `FOR STANDBY` option. You cannot connect to a standby database and create an additional standby database. RMAN creates the standby database by restoring and mounting a control file. RMAN can use an existing backup of the primary database control file, so you do not need to create a control file backup especially for the standby database.

A standby database, unlike a duplicate database created by `DUPLICATE` without the `FOR` `STANDBY` `OPTION`, does not get a new DBID. Thus, you should not register the standby database with your recovery catalog.

#### E.2.2.1 Active Database and Backup-Based Duplication

You must choose between active and backup-based duplication. If you specify `FROM ACTIVE DATABASE`, then RMAN copies the datafiles directly from the primary database to the standby database. The primary database must be mounted or open.

If you not specify `FROM ACTIVE DATABASE`, then RMAN performs backup-based duplication. RMAN restores backups of the primary datafiles to the standby database. All backups and archived redo log files needed for creating and recovering the standby database must be accessible by the server session on the standby host. RMAN restores the most recent datafiles unless you execute the `SET UNTIL` command.

#### E.2.2.2 DB\_UNIQUE\_NAME Values in an RMAN Environment

A standby database, unlike a duplicate database created by `DUPLICATE` without the `FOR STANDBY` option, does not get a new DBID. When using RMAN in a Data Guard environment, you should always connect it to a recovery catalog. The recovery catalog can store the metadata for all primary and standby databases in the environment. You should not explicitly register the standby database in the recovery catalog.

A database in a Data Guard environment is uniquely identified by means of the `DB_UNIQUE_NAME` parameter in the initialization parameter file. The `DB_UNIQUE_NAME` must be unique across all the databases with the same DBID for RMAN to work correctly in a Data Guard environment.

See Also:

[Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/cd/E11882_01/backup.112/e10642/rcmarchi.htm#BRADV89379) for a conceptual overview of RMAN operation in a Data Guard environment

#### E.2.2.3 Recovery of a Standby Database

By default, RMAN does not recover the standby database after creating it. RMAN leaves the standby database mounted, but does not place the standby database in manual or managed recovery mode. RMAN disconnects and does not perform media recovery of the standby database.

If you want RMAN to recover the standby database after creating it, then the standby control file must be usable for the recovery. The following conditions must be met:

- The end recovery time of the standby database must be greater than or equal to the checkpoint SCN of the standby control file.
- An archived redo log file containing the checkpoint SCN of the standby control file must be available at the standby site for recovery.

One way to ensure these conditions are met is to issue the `ALTER` `SYSTEM` `ARCHIVE` `LOG` `CURRENT` statement after backing up the control file on the primary database. This statement archives the online redo log files of the primary database. Then, either back up the most recent archived redo log file with RMAN or move the archived redo log file to the standby site.

Use the `DORECOVER` option of the `DUPLICATE` command to specify that RMAN should recover the standby database. RMAN performs the following steps after creating the standby database files:

1. RMAN begins media recovery. If recovery requires archived redo log files, and if the log files are not already on disk, then RMAN attempts to restore backups.
2. RMAN recovers the standby database to the specified time, system change number (SCN), or log file sequence number, or to the latest archived redo log file generated if none of the preceding are specified.
3. RMAN leaves the standby database mounted after media recovery is complete, but does not place the standby database in manual or managed recovery mode.

#### E.2.2.4 Standby Database Redo Log Files

RMAN automatically creates the standby redo log files on the standby database. After the log files are created, the standby database maintains and archives them according to the normal rules for log files.

If you use backup-based duplication, then the only option when naming the standby redo log files on the standby database is the file names for the log files, as specified in the standby control file. If the log file names on the standby must be different from the primary file names, then one option is to specify file names for the standby redo logs by setting `LOG_FILE_NAME_CONVERT` in the standby initialization parameter file.

Note the following restrictions when specifying file names for the standby redo log files on the standby database:

- You must use the `LOG_FILE_NAME_CONVERT` parameter to name the standby redo log files if the primary and standby databases use different naming conventions for the log files.
- You cannot use the `SET` `NEWNAME` or `CONFIGURE` `AUXNAME` commands to rename the standby redo log files.
- You cannot use the `LOGFILE` clause of the `DUPLICATE` command to specify file names for the standby redo log files.
- If you want the standby redo log file names on the standby database to be the same as the primary redo log file names, then you must specify the `NOFILENAMECHECK` clause of the `DUPLICATE` command. Otherwise, RMAN signals an error even if the standby database is created on a different host.

#### E.2.2.5 Password Files for the Standby Database

If you are using active database duplication, then RMAN always copies the password file to the standby host because the password file on the standby database must be an exact copy of the password file on the target database. In this case, the `PASSWORD FILE` clause is not necessary. RMAN overwrites any existing password file for the auxiliary instance. With backup-based duplication you must copy the password file used on the primary to the standby, for Data Guard to ship logs.

## E.3 Using the DUPLICATE Command to Create a Standby Database

The procedure for creating a standby database is basically identical to the duplication procedure described in [Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/cd/E11882_01/backup.112/e10642/rcmdupdb.htm#BRADV168).

### E.3.1 Creating a Standby Database with Active Database Duplication

To create a standby database from files that are active in the primary database, specify both `FOR STANDBY` and `FROM ACTIVE DATABASE`. Optionally, specify the `DORECOVER` option to recover the database after standby creation.

This scenario assumes that the standby host and primary database host have the same directory structure.

To create a standby database from active database files:

1. Prepare the auxiliary database instance as explained in [Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/cd/E11882_01/backup.112/e10642/rcmdupdb.htm#BRADV167).
	Because you are using active database duplication, you must create a password file for the auxiliary instance and establish Oracle Net connectivity. This is a temporary password file as it will be overwritten during the duplicate operation.
2. Decide how to provide names for the standby control files, datafiles, online redo logs, and tempfiles. This step is explained in [Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/cd/E11882_01/backup.112/e10642/rcmdupdb.htm#BRADV298).
	In this scenario, the standby database files will be named the same as the primary database files.
3. Start and configure RMAN as explained in [Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/cd/E11882_01/backup.112/e10642/rcmdupdb.htm#BRADV299).
4. Execute the `DUPLICATE` command.
	The following example illustrates how to use `DUPLICATE` for active duplication. This example requires the `NOFILENAMECHECK` option because the primary database files have the same names as the standby database files. The `SET` clauses for SPFILE are required for log shipping to work properly. The `db_unique_name` must be set to ensure that the catalog and Data Guard can identify this database as being different from the primary.
	```
	DUPLICATE TARGET DATABASE
	  FOR STANDBY
	  FROM ACTIVE DATABASE
	  DORECOVER
	  SPFILE
	    SET "db_unique_name"="foou" COMMENT ''Is a duplicate''
	    SET LOG_ARCHIVE_DEST_2="service=inst3 ASYNC REGISTER
	     VALID_FOR=(online_logfile,primary_role)"
	    SET FAL_SERVER="inst1" COMMENT "Is primary"
	  NOFILENAMECHECK;
	```
	RMAN automatically copies the server parameter file to the standby host, starts the auxiliary instance with the server parameter file, restores a backup control file, and copies all necessary database files and archived redo logs over the network to the standby host. RMAN recovers the standby database, but does not place it in manual or managed recovery mode.

### E.3.2 Creating a Standby Database with Backup-Based Duplication

To create a standby database from backups, specify `FOR STANDBY` but do not specify `FROM ACTIVE DATABASE`. Optionally, specify the `DORECOVER` option to recover the database after standby creation.

This scenario assumes that the standby host and primary database host have the same directory structure.

To create a standby database from backups:

1. Make database backups and archived redo logs available to the auxiliary instance on the duplicate host as explained in [Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/cd/E11882_01/backup.112/e10642/rcmdupdb.htm#BRADV89931).
2. Prepare the auxiliary database instance as explained in [Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/cd/E11882_01/backup.112/e10642/rcmdupdb.htm#BRADV167).
3. Decide how to provide names for the standby control files, datafiles, online redo logs, and tempfiles. This step is explained in [Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/cd/E11882_01/backup.112/e10642/rcmdupdb.htm#BRADV298).
	In this scenario, the standby database files will be named the same as the primary database files.
4. Start and configure RMAN as explained in [Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/cd/E11882_01/backup.112/e10642/rcmdupdb.htm#BRADV299).
5. Execute the `DUPLICATE` command.
	The following example illustrates how to use `DUPLICATE` for backup-based duplication. This example requires the `NOFILENAMECHECK` option because the primary database files have the same names as the standby database files.
	```
	DUPLICATE TARGET DATABASE
	  FOR STANDBY
	  DORECOVER
	  SPFILE
	    SET "db_unique_name"="foou" COMMENT ''Is a duplicate''
	    SET LOG_ARCHIVE_DEST_2="service=inst3 ASYNC REGISTER
	     VALID_FOR=(online_logfile,primary_role)"
	    SET FAL_SERVER="inst1" COMMENT "Is primary"
	  NOFILENAMECHECK;
	```
	RMAN automatically copies the server parameter file to the standby host, starts the auxiliary instance with the server parameter file, and restores all necessary database files and archived redo logs to the standby host. RMAN recovers the standby database, but does not place it in manual or managed recovery mode.