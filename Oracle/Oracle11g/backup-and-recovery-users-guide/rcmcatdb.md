---
title: Managing a Recovery Catalog
book: "Backup and Recovery User's Guide"
doc_id: E10642-08
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/backup.112/e10642/rcmcatdb.htm
tags:
  - oracle
  - 11g
  - backup-and-recovery-users-guide
---

## 13 Managing a Recovery Catalog

This chapter explains how to manage an RMAN recovery catalog. The catalog is a database schema that contains the RMAN repository data for one or more target databases. This chapter contains the following topics:

## Overview of the Recovery Catalog

This section explains the basic concepts related to managing a recovery catalog.

### Purpose of the Recovery Catalog

A [recovery catalog](glossary.md) is a database schema used by RMAN to store metadata about one or more Oracle databases. Typically, you store the catalog in a dedicated database. A recovery catalog provides the following benefits:

- A recovery catalog creates redundancy for the RMAN repository stored in the control file of each [target database](glossary.md). The recovery catalog serves as a secondary metadata repository. If the target control file and all backups are lost, then the RMAN metadata still exists in the recovery catalog.
- A recovery catalog centralizes metadata for all your target databases. Storing the metadata in a single place makes reporting and administration tasks easier to perform.
- A recovery catalog can store metadata history much longer than the control file. This capability is useful if you must do a recovery that goes further back in time than the history in the control file. The added complexity of managing a recovery catalog database can be offset by the convenience of having the extended backup history available.

Some RMAN features function only when you use a recovery catalog. For example, you can store RMAN scripts in a recovery catalog. The chief advantage of a [stored script](glossary.md) is that it is available to any RMAN client that can connect to the target database and recovery catalog. Command files are only available if the RMAN client has access to the file system on which they are stored.

A recovery catalog is required when you use RMAN in a Data Guard environment. By storing backup metadata for all primary and standby databases, the catalog enables you to offload backup tasks to one standby database while enabling you to restore backups on other databases in the environment.

### Basic Concepts for the Recovery Catalog

The recovery catalog contains metadata about RMAN operations for each registered target database. When RMAN is connected to a recovery catalog, RMAN obtains its metadata exclusively from the catalog. The catalog includes the following types of metadata:

- Data file and archived redo log backup sets and backup pieces
- Data file copies
- Archived redo logs and their copies
- Database structure (tablespaces and datafiles)
- Stored scripts, which are named user-created sequences of RMAN commands
- Persistent RMAN configuration settings

#### Database Registration

The process of enrolling of a database in a recovery catalog for RMAN use is called [registration](glossary.md). The recommended practice is to register every [target database](glossary.md) in your environment in a single recovery catalog. For example, you can register databases `prod1`, `prod2`, and `prod3` in a single catalog owned by `catowner` in the database `catdb`.

See Also:

"Registering a Database in the Recovery Catalog"

#### Centralization of Metadata in a Base Recovery Catalog

The owner of a centralized recovery catalog, which is also called the [base recovery catalog](glossary.md), can grant or revoke restricted access to the catalog to other database users. Each restricted user has full read/write access to his own metadata, which is called a [virtual private catalog](glossary.md). The RMAN metadata is stored in the schema of the virtual private catalog owner. The owner of the base recovery catalog determines which objects each virtual private catalog user can access.

You can use a recovery catalog in an environment in which you use or have used different versions of Oracle Database. As a result, your environment can have different versions of the RMAN client, recovery catalog database, recovery catalog schema, and target database. "Importing and Moving a Recovery Catalog" explains how to merge multiple recovery catalog schemas into one.

See Also:

"Creating and Managing Virtual Private Catalogs"

#### Recovery Catalog Resynchronization

For RMAN operations such as backup, restore, and crosscheck, RMAN always first updates the control file and then propagates the metadata to the recovery catalog. This flow of metadata from the mounted control file to the recovery catalog, which is known as recovery catalog [resynchronization](glossary.md), ensures that the metadata that RMAN obtains from the control file is current.

See Also:

"Resynchronizing the Recovery Catalog"

#### Stored Scripts

You can use a [stored script](glossary.md) as an alternative to a command file for managing frequently used sequences of RMAN commands. The script is stored in the recovery catalog rather than on the file system.

A local stored script is associated with the target database to which RMAN is connected when the script is created, and can only be executed when you are connected to this target database. A global stored script can be run against any database registered in the recovery catalog. A virtual private catalog user has read-only access to global scripts. Creating or updating global scripts must be done while connected to the base recovery catalog.

See Also:

"Managing Stored Scripts"

#### Recovery Catalog in a Data Guard Environment

As explained in ["RMAN in a Data Guard Environment"](rcmarchi.md), you must use a recovery catalog to manage RMAN metadata for all physical databases, both primary and standby databases, in the Data Guard environment. RMAN uses the recovery catalog as the single source of truth for the Data Guard environment.

RMAN can use the recovery catalog to update a primary or standby control file in a [reverse resynchronization](glossary.md). In this case, the metadata flows from the catalog to the control file rather than the other way around. RMAN automatically performs resynchronizations in most situations in which they are needed. Thus, you should not need to use the `RESYNC` command to manually resynchronize very often.

See Also:

[Oracle Data Guard Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e41134/rman.htm#SBYDB04700) to learn how to configure the RMAN environment for use with a standby database

### Basic Steps of Managing a Recovery Catalog

The basic steps for setting up a recovery catalog for use by RMAN are as follows:

1. Create the recovery catalog.
	"Creating a Recovery Catalog" explains how to perform this task.
2. Register your target databases in the recovery catalog.
	This step enables RMAN to store metadata for the target databases in the recovery catalog. "Registering a Database in the Recovery Catalog" explains this task.
3. If needed, catalog any older backups whose records are no longer stored in the target control file.
	"Cataloging Backups in the Recovery Catalog" explains how to perform this task.
4. If needed, create virtual private catalogs for specific users and determine the metadata to which they are permitted access.
	"Creating and Managing Virtual Private Catalogs" explains how to perform this task.
5. Protect the recovery catalog by including it in your backup and recovery strategy.
	"Protecting the Recovery Catalog" explains how to back up and recover the catalog and increase its availability.

The remainder of the chapter explains how to manage the recovery catalog after it is operational. You can perform the following tasks:

- "Managing Stored Scripts" explains how to store RMAN scripts in the recovery catalog and manage them.
- [Chapter 11, "Reporting on RMAN Operations"](rcmreprt.md) explains how to report on RMAN operations. You can use the `LIST` and `REPORT` commands with or without a recovery catalog. ["Querying Recovery Catalog Views"](rcmreprt.md) explains how to report on RMAN operations with fixed views in the recovery catalog.
- "Maintaining a Recovery Catalog" explains a variety of tasks for ongoing recovery catalog maintenance, including how to import one recovery catalog into another recovery catalog.

If you no longer want to maintain a recovery catalog, then see "Dropping a Recovery Catalog".

## Creating a Recovery Catalog

This section explains the phases of recovery catalog creation. This section contains the following topics:

- Configuring the Recovery Catalog Database
- Creating the Recovery Catalog Schema Owner
- Executing the CREATE CATALOG Command

### Configuring the Recovery Catalog Database

When you use a recovery catalog, RMAN requires that you maintain a recovery catalog schema. The recovery catalog is stored in the default tablespace of the schema. The `SYS` user cannot be the owner of the recovery catalog.

Decide which database you will use to install the recovery catalog schema, and also how you will back up this database. Also, decide whether to operate the catalog database in `ARCHIVELOG` mode, which is recommended.

Note:

Do not use the target database to be backed up as the database for the recovery catalog. The recovery catalog must be protected if the target database is lost.

#### Planning the Size of the Recovery Catalog Schema

You must allocate space to be used by the catalog schema. The size of the recovery catalog schema depends upon the number of databases monitored by the catalog. The schema also grows as the number of archived redo log files and backups for each database increases. Finally, if you use RMAN stored scripts stored in the catalog, some space must be allocated for those scripts.

For example, assume that the `trgt` database has 100 files, and that you back up the database once a day, producing 50 backup sets containing 1 backup piece each. If you assume that each row in the backup piece table uses the maximum amount of space, then one daily backup consumes less than 170 kilobytes in the recovery catalog. So, if you back up once a day for a year, then the total storage in this period is about 62 megabytes. Assume approximately the same amount for archived logs. Thus, the worst case is about 120 megabytes for a year for metadata storage. For a more typical case in which only a portion of the backup piece row space is used, 15 MB for each year is realistic.

If you plan to register multiple databases in your recovery catalog, then remember to add up the space required for each one based on the previous calculation to arrive at a total size for the default tablespace of the recovery catalog schema.

#### Allocating Disk Space for the Recovery Catalog Database

If you are creating your recovery catalog in an existing database, then add enough room to hold the default tablespace for the recovery catalog schema. If you are creating a new database to hold your recovery catalog, then in addition to the space for the recovery catalog schema itself, allow space for other files in the recovery catalog database:

- `SYSTEM` and `SYSAUX` tablespaces
- Temporary tablespaces
- Undo tablespaces
- Online redo log files

Most of the space used in the recovery catalog database is devoted to supporting tablespaces, for example, the `SYSTEM`, temporary, and undo tablespaces. Table 13-1 describes typical space requirements.

Table 13-1 Typical Recovery Catalog Space Requirements for 1 Year

| Type of Space | Space Requirement |
| --- | --- |
| `SYSTEM` tablespace | 90 MB |
| Temp tablespace | 5 MB |
| Rollback or undo tablespace | 5 MB |
| Recovery catalog tablespace | 15 MB for each database registered in the recovery catalog |
| Online redo logs | 1 MB each (three groups, each with two members) |

Caution:

Ensure that the recovery catalog and target databases do not reside on the same disk. If both your recovery catalog and your target database suffer hard disk failure, then your recovery process is much more difficult. If possible, take other measures as well to eliminate common points of failure between your recovery catalog database and the databases that you are backing up.

### Creating the Recovery Catalog Schema Owner

After choosing the recovery catalog database and creating the necessary space, you are ready to create the owner of the recovery catalog and grant this user necessary privileges. Assume the following background information for the instructions in the following sections:

- User `SYS` has `SYSDBA` privileges on the recovery catalog database `catdb`.
- A tablespace called `tools` in the recovery catalog database `catdb` stores the recovery catalog. If you use an RMAN reserved word as a tablespace name, you must enclose it in quotes and put it in uppercase. (See [Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmcomma004.htm#RCMRF909) for a list of RMAN reserved words.)
- A tablespace called `temp` exists in the recovery catalog database.

To create the recovery catalog schema in the recovery catalog database:

1. Start SQL\*Plus and connect with administrator privileges to the database containing the recovery catalog. In this example, the database is `catdb`.
2. Create a user and schema for the recovery catalog. For example, you could enter the following SQL statement (replacing password with a user-defined password):
	```
	CREATE USER rman IDENTIFIED BY password
	  TEMPORARY TABLESPACE temp 
	  DEFAULT TABLESPACE tools 
	  QUOTA UNLIMITED ON tools;
	```
	Note:
	Create a password that is secure. See [Oracle Database Security Guide](https://docs.oracle.com/cd/E11882_01/network.112/e36292/authentication.htm#DBSEG33223) for more information.
3. Grant the `RECOVERY_CATALOG_OWNER` role to the schema owner. This role provides the user with all privileges required to maintain and query the recovery catalog.
	```
	GRANT RECOVERY_CATALOG_OWNER TO rman;
	```

### Executing the CREATE CATALOG Command

After creating the catalog owner, create the catalog tables with the RMAN `CREATE` `CATALOG` command. The command creates the catalog in the default tablespace of the catalog owner.

To create the recovery catalog:

1. Start RMAN and connect to the database that will contain the catalog. Connect to the database as the recovery catalog owner.
2. Run the `CREATE` `CATALOG` command to create the catalog. The creation of the catalog can take several minutes. If the catalog tablespace is this user's default tablespace, then you can run the following command:
	```
	RMAN> CREATE CATALOG;
	```
	You can specify the tablespace name for the catalog in the `CREATE` `CATALOG` command. For example:
	```
	RMAN> CREATE CATALOG TABLESPACE cat_tbs;
	```
	Note:
	If the tablespace name that you want to use for the recovery catalog is an RMAN reserved word, then it be uppercase and enclosed in quotes. For example:
	```
	CREATE CATALOG TABLESPACE 'CATALOG';
	```
3. You can check the results by using SQL\*Plus to query the recovery catalog to see which tables were created:
	```
	SQL> SELECT TABLE_NAME FROM USER_TABLES;
	```

See Also:

[Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/toc.htm) for the SQL syntax for the `GRANT` and `CREATE` `USER` statements, and [Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta013.htm#RCMRF117) for `CREATE` `CATALOG` command syntax

## Registering a Database in the Recovery Catalog

This section describes how to maintain target database records in the recovery catalog. It contains the following sections:

- About Registration of a Database in the Recovery Catalog
- Registering a Database with the REGISTER DATABASE Command

### About Registration of a Database in the Recovery Catalog

The process of enrolling of a [target database](glossary.md) in a recovery catalog is called [registration](glossary.md). If a target database is not registered in the recovery catalog, then RMAN cannot use the catalog to store metadata for operations on this database. You can still perform RMAN operations on an unregistered database: RMAN always stores its metadata in the control file of the target database.

If you are not using the recovery catalog in a Data Guard environment, then use the `REGISTER` command to register each database. Each database must have a unique [DBID](glossary.md). If you use the RMAN `DUPLICATE` command or the `CREATE DATABASE` statement in SQL, then the database is assigned a unique DBID automatically. If you create a database by other means, then the copied database may have the same DBID as its source database. You can change the DBID with the `DBNEWID` utility so that you can register the source and copy databases in the same catalog.

You can use the `UNREGISTER` command to unregister a database from the recovery catalog.

#### About Standby Database Registration

In a Data Guard environment, the primary and standby databases share the same DBID and database name. To be eligible for registration in the recovery catalog, each database in the Data Guard environment must have different `DB_UNIQUE_NAME` values. The `DB_UNIQUE_NAME` parameter for a database is set in its initialization parameter file.

If you use RMAN in a Data Guard environment, then you can use the `REGISTER DATABASE` command only for the primary database. You can use the following techniques to register a standby database in the recovery catalog:

- When you connect to a standby database as `TARGET`, RMAN automatically registers the database in the recovery catalog.
- When you run the `CONFIGURE DB_UNIQUE_NAME` command for a standby database that is not known to the recovery catalog, RMAN automatically registers this standby database if its primary database is registered.

See Also:

- "Unregistering a Target Database from the Recovery Catalog"
- [Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta020.htm#RCMRF126) for `DUPLICATE` command syntax
- [Oracle Database Utilities](https://docs.oracle.com/cd/E11882_01/server.112/e22490/dbnewid.htm#SUTIL014) to learn how to use the `DBNEWID` utility to change the DBID
- [Oracle Data Guard Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e41134/rman.htm#SBYDB04700) to learn about using RMAN in a Data Guard environment

### Registering a Database with the REGISTER DATABASE Command

The first step in using a recovery catalog with a target database is registering the target database in the recovery catalog. If you use the catalog in a Data Guard environment, then you can only register the primary database in this way.

Use the following procedure:

1. Start RMAN and connect to a target database and recovery catalog. The recovery catalog database must be open.
	For example, issue the following command to connect to the catalog database with the net service name `catdb` as user `rman` (who owns the catalog schema):
	```
	% rman TARGET / CATALOG rman@catdb
	```
2. If the target database is not mounted, then mount or open it:
	```
	STARTUP MOUNT;
	```
3. Register the target database in the connected recovery catalog:
	```
	REGISTER DATABASE;
	```
	RMAN creates rows in the catalog tables to contain information about the target database, then copies all pertinent data about the target database from the control file into the catalog, synchronizing the catalog with the control file.
4. Verify that the registration was successful by running `REPORT` `SCHEMA`:
	```
	REPORT SCHEMA;
	Report of database schema
	File Size(MB)   Tablespace       RB segs Datafile Name
	---- ---------- ---------------- ------- -------------------
	1        307200 SYSTEM             NO    /oracle/oradata/trgt/system01.dbf
	2         20480 UNDOTBS            YES   /oracle/oradata/trgt/undotbs01.dbf
	3         10240 CWMLITE            NO    /oracle/oradata/trgt/cwmlite01.dbf
	4         10240 DRSYS              NO    /oracle/oradata/trgt/drsys01.dbf
	5         10240 EXAMPLE            NO    /oracle/oradata/trgt/example01.dbf
	6         10240 INDX               NO    /oracle/oradata/trgt/indx01.dbf
	7         10240 TOOLS              NO    /oracle/oradata/trgt/tools01.dbf
	8         10240 USERS              NO    /oracle/oradata/trgt/users01.dbf
	```

## Cataloging Backups in the Recovery Catalog

If you have data file copies, backup pieces, or archived logs on disk, then you can catalog them in the recovery catalog with the `CATALOG` command. When using a recovery catalog, cataloging older backups that have aged out of the control file lets RMAN use the older backups during restore operations. The following commands illustrate this technique:

```
CATALOG DATAFILECOPY '/disk1/old_datafiles/01_01_2003/users01.dbf';
CATALOG ARCHIVELOG '/disk1/arch_logs/archive1_731.dbf', 
                   '/disk1/arch_logs/archive1_732.dbf';
CATALOG BACKUPPIECE '/disk1/backups/backup_820.bkp';
```

You can also catalog multiple backup files in a directory at once by using the `CATALOG START WITH` command, as shown in the following example:

```
CATALOG START WITH '/disk1/backups/';
```

RMAN lists the files to be added to the RMAN repository and prompts for confirmation before adding the backups. Be careful when creating your prefix with `CATALOG START WITH`. RMAN scans all paths for all files on disk that begin with the specified prefix. The prefix is not just a directory name. Using the wrong prefix can cause the cataloging of the wrong set of files.

For example, assume that a group of directories `/disk1/backups`, `/disk1/backups-year2003`, `/disk1/backupsets`, and `/disk1/backupsets/test` and so on, all contain backup files. The following command catalogs all files in all of these directories, because `/disk1/backups` is a prefix for the paths for all of these directories:

```
CATALOG START WITH '/disk1/backups';
```

To catalog only backups in the `/disk1/backups` directory, the correct command would be as follows:

```
CATALOG START WITH '/disk1/backups/';
```

## Creating and Managing Virtual Private Catalogs

### About Virtual Private Catalogs

By default, all of the users of an RMAN recovery catalog have full privileges to insert, update, and delete any metadata in the catalog. For example, if the administrators of two unrelated databases share the same recovery catalog, each administrator could, whether inadvertently or maliciously, destroy catalog data for the other's database. In many enterprises, this situation is tolerated because the same people manage many different databases and also manage the recovery catalog. But in other enterprises where clear separation of duty exists between administrators of various databases, and between the DBA and the administrator of the recovery catalog, you may desire to restrict each database administrator to modify only backup metadata belonging to those databases that they are responsible for, while still keeping the benefits of a single, centrally-managed, RMAN recovery catalog. This goal can be achieved by implementing [virtual private catalog](glossary.md) s.

Every 11g recovery catalog supports virtual private catalogs, but they are not used unless explicitly created. There is no restriction to the number of virtual private catalogs that can created beneath one recovery catalog. Each virtual private catalog is owned by a database schema user which is different than the user who owns the recovery catalog.

After creating one or more virtual private catalogs, using the directions that follow, the administrator for the recovery catalog grants each virtual private catalog the privilege to use that catalog for one or more databases that are currently registered in the recovery catalog. The administrator of the recovery catalog can also grant the privilege to register new databases while using a virtual private catalog.

Note:

Every virtual private catalog has access to all global stored scripts and those non-global stored scripts that belong to those databases for which this virtual private catalog has privileges. Virtual private catalogs cannot access non-global stored scripts that belong to databases that they do not have privileges for, and they cannot create global stored scripts.

The basic steps for creating a virtual private catalog are as follows:

1. Create the database user who will own the virtual private catalog (if this user does not exist) and grant this user access privileges.
	This task is described in "Creating and Granting Privileges to a Virtual Private Catalog Owner".
2. Create the virtual private catalog.
	This task is described in "Creating a Virtual Private Catalog".

After the virtual private catalog is created, you can revoke catalog access privileges as necessary. This task is described in "Revoking Privileges from a Virtual Private Catalog Owner". "Dropping a Virtual Private Catalog" explains how to drop a virtual private catalog.

If the recovery catalog is a virtual private catalog, then the RMAN client connecting to it must be at patch level 10.1.0.6 or 10.2.0.3. Oracle9i RMAN clients cannot connect to a virtual private catalog. This version restriction does not affect RMAN client connections to an Oracle Database 11g base recovery catalog, even if it has some virtual private catalog users.

See Also:

[Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/compat.htm#RCMRF908) for details about RMAN version compatibility

### Creating and Granting Privileges to a Virtual Private Catalog Owner

This section assumes that you created the base recovery catalog.

Assume that the following databases are registered in the base recovery catalog: `prod1`, `prod2`, and `prod3`. The database user who owns the base recovery catalog is `catowner`. You want to create database user `vpc1` and grant this user access privileges only to `prod1` and `prod2`. By default, a virtual private catalog owner has no access to the base recovery catalog.

To create and grant privileges to a virtual private catalog owner:

1. Start SQL\*Plus and connect to the recovery catalog database with administrator privileges.
2. If the user that will own the virtual private catalog does not exist, then create the user.
	For example, if you want to create database user `vpc1` to own the catalog, then you could execute the following command (replacing password with a user-defined password):
	```
	SQL> CREATE USER vpc1 IDENTIFIED BY password
	  2  DEFAULT TABLESPACE vpcusers
	  3  QUOTA UNLIMITED ON vpcusers;
	```
	Note:
	Create a password that is secure. See [Oracle Database Security Guide](https://docs.oracle.com/cd/E11882_01/network.112/e36292/authentication.htm#DBSEG33223) for more information.
3. Grant the `RECOVERY_CATALOG_OWNER` role to the database user that will own the virtual private catalog, and then exit SQL\*Plus.
	The following example grants the role to user `vpc1`:
	```
	SQL> GRANT recovery_catalog_owner TO vpc1;
	SQL> EXIT;
	```
4. Start RMAN and connect to the recovery catalog database as the base recovery catalog owner (not the virtual private catalog owner).
	The following example connects to the base recovery catalog as `catowner`:
	```
	% rman
	RMAN> CONNECT CATALOG catowner@catdb;
	recovery catalog database Password: password
	connected to recovery catalog database
	```
5. Grant desired privileges to the virtual private catalog owner.
	The following example gives user `vpc1` access to the metadata for `prod1` and `prod2` (but not `prod3`):
	```
	RMAN> GRANT CATALOG FOR DATABASE prod1 TO vpc1;
	RMAN> GRANT CATALOG FOR DATABASE prod2 TO vpc1;
	```
	You can also use a DBID rather than a database name. The virtual private catalog user does not have access to the metadata for any other databases registered in the recovery catalog.
	You can also grant the user the ability to register new target databases in the recovery catalog. For example:
	```
	RMAN> GRANT REGISTER DATABASE TO vpc1;
	```

### Creating a Virtual Private Catalog

This section assumes that the virtual private catalog owner has been given the `RECOVERY_CATALOG_OWNER` database role. Also, the base recovery catalog owner used the `GRANT` command to give the virtual private catalog owner access to metadata in the base recovery catalog.

To create a virtual private catalog:

1. Start RMAN and connect to the recovery catalog database as the virtual private catalog owner (not the base recovery catalog owner).
	The following example connects to the recovery catalog as `vpc1`:
	```
	% rman
	RMAN> CONNECT CATALOG vpc1@catdb;
	```
2. Create the virtual private catalog.
	The following command creates the virtual private catalog:
	```
	RMAN> CREATE VIRTUAL CATALOG;
	```
3. If you intend to use a 10.2 or earlier release of RMAN with this virtual private catalog, then execute the following PL/SQL procedure (where base\_catalog\_owner is the database user who owns the base recovery catalog):
	```
	SQL> EXECUTE base_catalog_owner.DBMS_RCVCAT.CREATE_VIRTUAL_CATALOG;
	```

### Revoking Privileges from a Virtual Private Catalog Owner

This section assumes that you have created a virtual private catalog.

Assume that two databases are registered in the base recovery catalog: `prod1` and `prod2`. As owner of the base recovery catalog, you have granted the `vpc1` user access privileges to `prod1`. You have also granted this user the right to register databases in his virtual private catalog. Now you want to revoke privileges from `vpc1`.

To revoke privileges from a virtual private catalog owner:

1. Start RMAN and connect to the recovery catalog database as the recovery catalog owner (not the virtual private catalog owner).
	The following example connects to the recovery catalog as `catowner`:
	```
	% rman
	RMAN> CONNECT CATALOG catowner@catdb;
	```
2. Revoke specified privileges from the virtual private catalog owner.
	The following command revokes access to the metadata for `prod1` from virtual private catalog owner `vpc1`:
	```
	REVOKE CATALOG FOR DATABASE prod1 FROM vpc1;
	```
	You can also specify a DBID rather than a database name. The catalog `vpc1` retains all other granted catalog privileges.
	You can also revoke the privilege to register new target databases in the recovery catalog. For example:
	```
	REVOKE REGISTER DATABASE FROM vpc1;
	```

### Dropping a Virtual Private Catalog

This section assumes that you have created a virtual private catalog and now want to drop it. When you drop a virtual private catalog, you do not remove the base recovery catalog itself, but only drop the synonyms and views that refer to the base recovery catalog.

To drop a virtual private catalog:

1. Start RMAN and connect to the recovery catalog database as the virtual private catalog owner (not the base recovery catalog owner).
	The following example connects to the recovery catalog as user `vpc1`:
	```
	% rman
	RMAN> CONNECT CATALOG vpc1@catdb;
	```
2. Drop the catalog.
	If you are using an Oracle Database 11g or later RMAN executable, then drop the virtual private catalog with the `DROP CATALOG` command:
	```
	RMAN> DROP CATALOG;
	```
	If you are using an Oracle Database 10g or earlier RMAN executable, then you cannot use the `DROP CATALOG` command. Instead, connect SQL\*Plus to the catalog database as the virtual private catalog user, then execute the following PL/SQL procedure (where base\_catalog\_owner is the database user who owns the base recovery catalog):
	```
	SQL> EXECUTE base_catalog_owner.DBMS_RCVCAT.DELETE_VIRTUAL_CATALOG;
	```

## Protecting the Recovery Catalog

Include the recovery catalog database in your backup and recovery strategy. If you do not back up the recovery catalog and a disk failure occurs that destroys the recovery catalog database, then you may lose the metadata in the catalog. Without the recovery catalog contents, recovery of your other databases is likely to be more difficult.

### Backing Up the Recovery Catalog

A single recovery catalog can store metadata for multiple target databases. Consequently, loss of the recovery catalog can be disastrous. You should back up the recovery catalog frequently. This section provides general guidelines for developing a strategy for protecting the recovery catalog.

#### Backing Up the Recovery Catalog Frequently

The recovery catalog database is a database like any other, and is also a key part of your backup and recovery strategy. Protect the recovery catalog as you would protect any other part of your database, by backing it up. The backup strategy for your recovery catalog database should be part of your overall backup and recovery strategy.

Back up the recovery catalog with the same frequency that you back up a target database. For example, if you make a weekly whole database backup of a target database, then back up the recovery catalog after the backup of the target database. This backup of the recovery catalog can help you in a disaster recovery scenario. Even if you must restore the recovery catalog database with a control file autobackup, you can use the full record of backups in your restored recovery catalog database to restore the target database.

#### Choosing the Appropriate Technique for Physical Backups

When backing up the recovery catalog database, you can use RMAN to make the backups. As illustrated in Figure 13-1, start RMAN with the `NOCATALOG` option so that the repository for RMAN is the control file in the catalog database.

Figure 13-1 Using the Control File as the Repository for Backups of the Recovery Catalog

![Figure 13-1 Using the Control File as the Repository for Backups of the Recovery Catalog](img/bradv009.gif)

> This illustration presents using the control file as the repository for backups of the catalog. RMAN is used to back up the target database. Metadata about backups of the target database are stored in the recovery catalog database. RMAN is also used to back up the catalog database. Metadata about backups of the recovery catalog database are stored in the catalog database control file. RMAN takes autobackups of the control file of the recovery catalog database.
  

Follow these guidelines when developing an RMAN backup strategy for the recovery catalog database:

- Run the recovery catalog database in `ARCHIVELOG` mode so that you can do point-in-time recovery if needed.
- Set the retention policy to a `REDUNDANCY` value greater than `1`.
- Back up the database to two separate media (for example, disk and tape).
- Run `BACKUP` `DATABASE` `PLUS` `ARCHIVELOG` at regular intervals, to a media manager if available, or just to disk.
- Do not use another recovery catalog as the repository for the backups.
- Configure the control file autobackup feature to `ON`.

With this strategy, the control file autobackup feature ensures that the recovery catalog database can always be recovered, so long as the control file autobackup is available.

See Also:

["Performing Disaster Recovery"](rcmadvre.md) for more information for recovery with a control file autobackup

#### Separating the Recovery Catalog from the Target Database

A recovery catalog is only effective when separated from the data that it is designed to protect. Thus, you should never store a recovery catalog containing the RMAN repository for a database in the same database as the target database. Also, do not store the catalog database on the same disks as the target database.

To illustrate why data separation is advised, assume that you store the catalog for database `prod1` in `prod1`. If `prod1` suffers a total media failure, and if the recovery catalog for `prod1` is also stored in `prod1`, then if you lose the database you also lose the recovery catalog. At this point the only option is to restore an autobackup of the control file for `prod1` and use it to restore and recover the database without the benefit of any information stored in the recovery catalog.

#### Exporting the Recovery Catalog Data for Logical Backups

Logical backups of the RMAN recovery catalog created with the Data Pump Export utility can be a useful supplement for physical backups. If a recovery catalog database is damaged, you can use Data Pump Import to quickly reimport the exported recovery catalog data into another database and rebuild the catalog.

### Recovering the Recovery Catalog

Restoring and recovering the recovery catalog database is much like restoring and recovering any other database with RMAN. You can restore the control file and server parameter file for the recovery catalog database from an autobackup, then restore and perform complete recovery on the rest of the database. If you are in a situation where you are using multiple recovery catalogs, then you can also use another recovery catalog to record metadata about backups of this recovery catalog database.

If recovery of the recovery catalog database through the normal Oracle recovery procedures is not possible, then you must re-create the catalog. Examples of this worst-case scenario include:

- A recovery catalog database that has never been backed up
- A recovery catalog database that has been backed up, but cannot be recovered because the data file backups or archived logs are not available

You have the following options for partially re-creating the contents of the missing recovery catalog:

- Use the `RESYNC` `CATALOG` command to update the recovery catalog with any RMAN repository information from the control file of the target database or a control file copy. Any metadata from control file records that aged out of the control file is lost.
- Issue `CATALOG START WITH...` commands to recatalog any available backups.

To minimize the likelihood of this worst-case scenario, your backup strategy should at least include backing up the recovery catalog. This technique is described in "Backing Up the Recovery Catalog".

See Also:

- [Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta008.htm#RCMRF109) for information about the `CATALOG` command
- [Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta015.htm#RCMRF119) for information about the `CROSSCHECK` command

## Managing Stored Scripts

As explained in "About Stored Scripts", you can store scripts in the recovery catalog. This section explains how to create and manage stored scripts.

### About Stored Scripts

You can use a [stored script](glossary.md) as an alternative to a command file for managing frequently used sequences of RMAN commands. The script is stored in the recovery catalog rather than on the file system.

Stored scripts can be local or global. A local script is associated with the target database to which RMAN is connected when the script is created, and can only be executed when you are connected to that target database. A global stored script can be run against any database registered in the recovery catalog, if the RMAN client is connected to the recovery catalog and a target database.

The commands allowable within the brackets of the `CREATE SCRIPT` command are the same commands supported within a `RUN` block. Any command that is legal within a `RUN` command is permitted in the stored script. The following commands are not legal within stored scripts: `RUN`, `@`, and `@@`.

When specifying a script name, RMAN permits but generally does not require that you use quotes around the name of a stored script. If the name begins with a digit or is an RMAN reserved word, however, then you must put quotes around the name to use it as a stored script name. Consider avoiding stored script names that begin with nonalphabetic characters or that are the same as RMAN reserved words.

Consider using a naming convention to avoid confusion between global and local stored scripts. For the `EXECUTE SCRIPT`, `DELETE SCRIPT` and `PRINT SCRIPT` commands, if the script name passed as an argument is not the name of a script defined for the connected target instance, then RMAN looks for a global script by the same name. For example, if the global script `global_backup` is in the recovery catalog, but no local stored script `global_backup` is defined for the target database, then the following command deletes the global script:

```
DELETE SCRIPT global_backup;
```

To use commands related to stored scripts, even global scripts, you must be connected to both a recovery catalog and a target database instance.

### Creating Stored Scripts

You can use the `CREATE SCRIPT` command to create a stored script. If `GLOBAL` is specified, then a global script with this name must not exist in the recovery catalog. If `GLOBAL` is not specified, then a local script must not exist with the same name for the same target database. You can also use the `REPLACE SCRIPT` to create a script or update an existing script.

To create a stored script:

1. Start RMAN and connect to a target database and recovery catalog (if used).
2. Run the `CREATE` `SCRIPT` command.
	The following example illustrates creation of a local script:
	```
	CREATE SCRIPT full_backup 
	{     
	  BACKUP DATABASE PLUS ARCHIVELOG;
	  DELETE OBSOLETE;
	}
	```
	For a global script, the syntax is similar:
	```
	CREATE GLOBAL SCRIPT global_full_backup 
	{     
	  BACKUP DATABASE PLUS ARCHIVELOG;
	  DELETE OBSOLETE;
	}
	```
	Optionally, you can provide a `COMMENT` with descriptive information:
	```
	CREATE GLOBAL SCRIPT global_full_backup 
	COMMENT 'use only with ARCHIVELOG mode databases'
	{     
	  BACKUP DATABASE PLUS ARCHIVELOG;
	  DELETE OBSOLETE;
	}
	```
	You can also create a script by reading its contents from a text file. The file must begin with a left brace (`{`) character, contain a series of commands valid within a `RUN` block, and end with a right brace (`}`) character. Otherwise, a syntax error is signalled, just as if the commands were entered at the keyboard.
	```
	CREATE SCRIPT full_backup 
	  FROM FILE '/tmp/my_script_file.txt';
	```
3. Examine the output.
	If no errors are displayed, then RMAN successfully created the script and stored in the recovery catalog.

See Also:

[Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmcomma004.htm#RCMRF909) for the list of RMAN reserved words

### Replacing Stored Scripts

To update stored scripts, use the `REPLACE` `SCRIPT` command. If you are replacing a local script, then you must be connected to the target database that you connected to when you created the script. If the script does not exist, then RMAN creates it.

To replace a stored script:

1. Start RMAN and connect to a target database and recovery catalog (if used).
2. Execute `REPLACE SCRIPT`.
	This following example updates the script `full_backup` with new contents:
	```
	REPLACE SCRIPT full_backup 
	{
	  BACKUP DATABASE PLUS ARCHIVELOG;
	}
	```
	You can update global scripts by specifying the `GLOBAL` keyword as follows:
	```
	REPLACE GLOBAL SCRIPT global_full_backup 
	COMMENT 'A script for full backup to be used with any database'
	{
	  BACKUP AS BACKUPSET DATABASE PLUS ARCHIVELOG;
	}
	```
	As with `CREATE SCRIPT`, you can update a local or global stored script from a text file with the following form of the command:
	```
	REPLACE GLOBAL SCRIPT global_full_backup 
	  FROM FILE '/tmp/my_script_file.txt';
	```

See Also:

[Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta2005.htm#RCMRF145) for `REPLACE` `SCRIPT` command syntax

### Executing Stored Scripts

Use the `EXECUTE SCRIPT` command to run a stored script. If `GLOBAL` is specified, then a global script with this name must exist in the recovery catalog; otherwise, RMAN returns error `RMAN-06004`. If `GLOBAL` is not specified, then RMAN searches for a local stored script defined for the current target database. If no local script with this name is found, then RMAN searches for a global script by the same name and executes it if one is found.

To execute a stored script:

1. Start RMAN and connect to a target database and recovery catalog (if used).
2. If needed, use `SHOW` to examine your configured channels.
	Your script uses the automatic channels configured at the time you execute the script. Use `ALLOCATE` `CHANNEL` commands in the script if you must override the configured channels. Because of the `RUN` block, if an RMAN command in the script fails, subsequent RMAN commands in the script do not execute.
3. Run `EXECUTE` `SCRIPT`. This command requires a `RUN` block, as shown in the following example:
	```
	RUN 
	{ 
	  EXECUTE SCRIPT full_backup; 
	}
	```
	The preceding command invokes a local script if one exists with the name specified. If no local script is found, but there is a global script with the name specified, then RMAN executes the global script.
	You can also use `EXECUTE GLOBAL SCRIPT` to control which script is invoked if a local and a global script have the same name. If there is no local script called `global_full_backup`, the following two commands have the same effect:
	```
	RUN 
	{
	  EXECUTE GLOBAL SCRIPT global_full_backup;
	}
	RUN
	{ 
	  EXECUTE SCRIPT global_full_backup; 
	}
	```

See Also:

[Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta021.htm#RCMRF127) for `EXECUTE` `SCRIPT` command syntax

### Creating and Executing Dynamic Stored Scripts

You can specify substitution variables in the [`CREATE SCRIPT`](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta014.htm#RCMRF118) command. When you start RMAN on the command line, the `USING` clause specifies one or more values for use in substitution variables in a command file. As in SQL\*Plus, `&1` indicates where to place the first value, `&2` indicates where to place the second value, and so on.

To create and use a dynamic stored script:

1. Create a command file that contains a `CREATE SCRIPT` statement with substitution variables for values that must be dynamically updated.
	The following example uses substitution variables for the name of the tape set, for a string in the `FORMAT` specification, and for the name of the restore point.
	```
	CREATE SCRIPT quarterly { 
	  ALLOCATE CHANNEL c1
	    DEVICE TYPE sbt
	    PARMS 'ENV=(OB_MEDIA_FAMILY=&1)';
	  BACKUP
	    TAG &2
	    FORMAT '/disk2/bck/&1%U.bck'
	    KEEP FOREVER
	    RESTORE POINT &3
	    DATABASE;
	}
	```
2. Connect RMAN to a target database (which must be mounted or open) and recovery catalog, specifying the initial values for the recovery catalog script.
	For example, enter the following command:
	```
	% rman TARGET / CATALOG rman@catdb USING arc_backup bck0906 FY06Q3
	```
	A recovery catalog is required for `KEEP FOREVER`, but is not required for any other `KEEP` option.
3. Run the command file created in the first step to create the stored script.
	For example, run the `/tmp/catscript.rman` command file as follows:
	```
	RMAN> @/tmp/catscript.rman
	```
	This step creates but does not execute the stored script.
4. Every quarter, execute the stored script, passing values for the substitution variables.
	The following example executes the recovery catalog script named `quarterly`. The example specifies `arc_backup` as the name of the media family (set of tapes), `bck1206` as part of the `FORMAT` string and `FY06Q4` as the name of the restore point.
	```
	RUN
	{ 
	  EXECUTE SCRIPT quarterly 
	    USING arc_backup
	          bck1206
	          FY06Q4;
	}
	```

See Also:

["Making Database Backups for Long-Term Storage"](rcmbckba.md)

### Printing Stored Scripts

The `PRINT` `SCRIPT` command displays a stored script or writes it out to a file.

To print stored scripts:

1. Start RMAN and connect to a target database and recovery catalog.
2. Run the `PRINT SCRIPT` command as follows:
	```
	PRINT SCRIPT full_backup;
	```
	To send the contents of a script to a file, use this form of the command:
	```
	PRINT SCRIPT full_backup 
	  TO FILE '/tmp/my_script_file.txt';
	```
	For global scripts, the analogous syntax would be as follows:
	```
	PRINT GLOBAL SCRIPT global_full_backup;
	PRINT GLOBAL SCRIPT global_full_backup 
	  TO FILE '/tmp/my_script_file.txt';
	```

See Also:

[Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta028.htm#RCMRF136) for `PRINT` `SCRIPT` command syntax

### Listing Stored Script Names

Use the `LIST ... SCRIPT NAMES` command to display the names of scripts defined in the recovery catalog. `LIST GLOBAL SCRIPT NAMES` and `LIST ALL SCRIPT NAMES` are the only commands that work when RMAN is connected to a recovery catalog without connecting to a target instance; the other forms of the `LIST ... SCRIPT NAMES` command require a recovery catalog connection.

To list stored script names:

1. Start RMAN and connect to a target database and recovery catalog.
2. Run the `LIST ... SCRIPT NAMES` command.
	For example, run the following command to list the names of all global and local scripts that can be executed for the currently connected target database:
	```
	LIST SCRIPT NAMES;
	```
	The following example lists only global script names:
	```
	LIST GLOBAL SCRIPT NAMES;
	```
	To list the names of all scripts stored in the current recovery catalog, including global scripts and local scripts for all target databases registered in the recovery catalog, use the following form of the command:
	```
	LIST ALL SCRIPT NAMES;
	```
	For each script listed, the output indicates which target database the script is defined for (or whether a script is global).

See Also:

[Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta027.htm#RCMRF132) for `LIST` `SCRIPT NAMES` command syntax and output format

### Deleting Stored Scripts

Use the `DELETE GLOBAL SCRIPT` command to delete a stored script from the recovery catalog.

To delete a stored script:

1. Start RMAN and connect to a target database and recovery catalog.
2. Enter the `DELETE SCRIPT` command.
	If you use `DELETE SCRIPT` without `GLOBAL`, and there is no stored script for the target database with the specified name, then RMAN looks for a global stored script by the specified name and deletes the global script if it exists. For example, suppose you enter the following command:
	```
	DELETE SCRIPT 'global_full_backup';
	```
	In this case, RMAN looks for a script `global_full_backup` defined for the connected target database, and if it did not find one, it searches the global scripts for a script called `global_full_backup` and delete that script.
	To delete a global stored script, use `DELETE GLOBAL SCRIPT`:
	```
	DELETE GLOBAL SCRIPT 'global_full_backup';
	```

See Also:

[Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta017.htm#RCMRF122) for `DELETE` `SCRIPT` command syntax

### Executing a Stored Script at RMAN Startup

To run the RMAN client and start a stored script in the recovery catalog on startup, use the `SCRIPT` argument when starting the RMAN client. For example, you could enter the following command to execute script `/tmp/fbkp.cmd`:

```
% rman TARGET / CATALOG rman@catdb SCRIPT '/tmp/fbkp.cmd';
```

You must connect to a recovery catalog, which contains the stored script, and target database, to which the script applies, when starting the RMAN client.

If local and global stored scripts are defined with the same name, then RMAN always executes the local script.

See Also:

[Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta2011.htm#RCMRF111) for full RMAN client command line syntax

## Maintaining a Recovery Catalog

This section describes various management and maintenance tasks. This section contains the following topics:

- About Recovery Catalog Maintenance
- Resynchronizing the Recovery Catalog
- Updating the Recovery Catalog After Changing a DB\_UNIQUE\_NAME
- Unregistering a Target Database from the Recovery Catalog
- Resetting the Database Incarnation in the Recovery Catalog
- Upgrading the Recovery Catalog
- Importing and Moving a Recovery Catalog

### About Recovery Catalog Maintenance

After you have created a recovery catalog and registered your target databases, you must maintain this catalog. For example, you must run the [RMAN maintenance commands](glossary.md), which are explained in [Chapter 12, "Maintaining RMAN Backups and Repository Records"](rcmmaint.md), to update backup records and to delete backups that are no longer needed. You must perform this type of maintenance regardless of whether you use RMAN with a recovery catalog. Other types of maintenance, such as upgrading a recovery catalog schema, are specific to use of RMAN with a recovery catalog.

If you use a recovery catalog in a Data Guard environment, then special considerations apply for backups and database files recorded in the catalog. See ["RMAN File Management in a Data Guard Environment"](rcmarchi.md) for an explanation of when backups are accessible to RMAN and how RMAN maintenance commands work with accessible backups.

### Resynchronizing the Recovery Catalog

When RMAN performs a [resynchronization](glossary.md), it compares the recovery catalog to either the current or backup control file of the target database and updates the catalog with metadata that is missing or changed. Most RMAN commands perform a resynchronization automatically when the target control file is mounted and the catalog is available. In a Data Guard environment, RMAN can perform a [reverse resynchronization](glossary.md) to update a database control file with metadata from the catalog.

#### About Resynchronization of the Recovery Catalog

Resynchronization of the recovery catalog ensures that the metadata that RMAN obtains from the control file stays current. Resynchronizations can be full or partial.

In a [partial resynchronization](glossary.md), RMAN reads the current control file of the target database to update changed metadata about new backups, new archived redo logs, and so on. RMAN does not resynchronize metadata about the database physical schema.

In a [full resynchronization](glossary.md), RMAN updates all changed records, including those for the database schema. RMAN performs a full resynchronization after structural changes to database (adding or dropping database files, creating new incarnation, and so on) or after changes to the RMAN persistent configuration.

RMAN creates a [snapshot control file](glossary.md), which is a temporary backup control file, when it performs a full resynchronization. The database ensures that only one RMAN session accesses a snapshot control file at any point in time. RMAN creates the snapshot control file in an operating system-specific location on the target database host. You can specify the name and location of the snapshot control file, as explained in ["Configuring the Snapshot Control File Location"](rcmconfa.md).

This snapshot control file ensures that RMAN has a consistent view of the control file. Because the control file is intended for short-term use, it is not registered in the catalog. RMAN records the control file checkpoint in the recovery catalog to indicate the currency of the catalog.

See Also:

[Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta2009.htm#RCMRF150) for more information about the `RESYNC` command

##### Recovery Catalog Resynchronization in a Data Guard Environment

RMAN only automatically resynchronizes the recovery catalog with a database when connected to this database as `TARGET`. Thus, RMAN does not automatically resynchronize every database in a Data Guard environment when connected as `TARGET` to one database in the environment. You can use the `RESYNC CATALOG FROM DB_UNIQUE_NAME` command to manually resynchronize the recovery catalog with a database in the Data Guard environment.

For an example of a manual resynchronization, assume that RMAN is connected as `TARGET` to production database `prod`, and that you have used `CONFIGURE` to create a configuration for `dgprod3`. If you run `RESYNC CATALOG FROM DB_UNIQUE_NAME dgprod3`, then RMAN resynchronizes the recovery catalog with the `dgprod3` control file. In this case RMAN performs both a normal resynchronization, in which metadata flows from the `dgprod3` control file to the catalog, and a [reverse resynchronization](glossary.md). In a reverse resynchronization, RMAN uses the persistent configurations in the recovery catalog to update the `dgprod3` control file.

See Also:

[Oracle Data Guard Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e41134/toc.htm)

#### Deciding When to Resynchronize the Recovery Catalog

RMAN automatically resynchronizes the recovery catalog when RMAN is connected to a target database and recovery catalog and you have executed RMAN commands. Thus, you should not need to manually run the `RESYNC` `CATALOG` command very often. The following sections describe situations requiring a manual catalog resynchronization.

##### Resynchronizing After the Recovery Catalog is Unavailable

If the recovery catalog is unavailable when you issue RMAN commands that cause a partial resynchronization, then open the catalog database later and resynchronize it manually with the `RESYNC` `CATALOG` command.

For example, the target database may be in New York while the recovery catalog database is in Japan. You may not want to make daily backups of the target database in `CATALOG` mode, to avoid depending on the availability of a geographically distant database. In such a case you could connect to the catalog as often as feasible and run the `RESYNC` `CATALOG` command.

##### Resynchronizing in ARCHIVELOG Mode When You Back Up Infrequently

Assume that a target database runs in `ARCHIVELOG` mode. Also assume that you do the following:

- Back up the database infrequently (for example, hundreds of redo logs are archived between database backups)
- Generate a high number of log switches every day (for example, 1000 switches between catalog resynchronizations)

In this case, you may want to manually resynchronize the recovery catalog regularly because the recovery catalog is not updated automatically when a redo log switch occurs or when a redo log is archived. The database stores metadata about redo log switches and archived redo logs only in the control file. You must periodically resynchronize to propagate this information into the recovery catalog.

How frequently you must resynchronize the recovery catalog depends on the rate at which the database archives redo logs. The cost of the operation is proportional to the number of records in the control file that have been inserted or changed since the previous resynchronization. If no records have been inserted or changed, then the cost of resynchronization is very low; if many records have been inserted or changed, then the resynchronization is more time-consuming.

##### Resynchronizing After Configuring a Standby Database

You can create or change an RMAN configuration for a standby database even when not connected to this database as `TARGET`. You perform this task with the `CONFIGURE DB_UNIQUE_NAME` or `CONFIGURE ... FOR DB_UNIQUE_NAME` command. As explained in "Manually Resynchronizing the Recovery Catalog", you can resynchronize the standby database manually to update the control file of the standby database.

##### Resynchronizing the Recovery Catalog Before Control File Records Age Out

Your goal is to ensure that the metadata in the recovery catalog is current. Because the recovery catalog obtains its metadata from the target control file, the currency of the data in the catalog depends on the currency of the data in the control file. You must make sure that the backup metadata in the control file is recorded in the catalog before it is overwritten with new records.

The `CONTROL_FILE_RECORD_KEEP_TIME` initialization parameter determines the minimum number of days that records are retained in the control file before they are candidates for being overwritten. Thus, you must ensure that you resynchronize the recovery catalog with the control file records before these records are erased. You should perform either of the following actions at intervals less than the `CONTROL_FILE_RECORD_KEEP_TIME` setting:

- Make a backup, thereby performing an implicit resynchronization of the recovery catalog
- Manually resynchronize the recovery catalog with the `RESYNC` `CATALOG` command

Make sure that `CONTROL_FILE_RECORD_KEEP_TIME` is longer than the interval between backups or resynchronizations. Otherwise, control file records could be reused before they are propagated to the recovery catalog. An extra week is a safe margin in most circumstances.

Caution:

Never set `CONTROL_FILE_RECORD_KEEP_TIME` to `0`. If you do, then backup records may be overwritten in the control file before RMAN can add them to the catalog.

One problem can arise if the control file becomes too large. The size of the target database control file grows depending on the number of:

- Backups that you perform
- Archived redo logs that the database generates
- Days that this information is stored in the control file

If the control file grows so large that it can no longer expand because it has reached either the maximum number of blocks or the maximum number of records, then the database may overwrite the oldest records even if their age is less than the `CONTROL_FILE_RECORD_KEEP_TIME` setting. In this case, the database writes a message to the alert log. If you discover that this situation occurs frequently, then reducing the value of `CONTROL_FILE_RECORD_KEEP_TIME` and increase the frequency of resynchronizations.

See Also:

- [Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams036.htm#REFRN10020) for more information about the `CONTROL_FILE_RECORD_KEEP_TIME` parameter
- [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/control.htm#ADMIN006) for more detailed information on other aspects of control file management
- ["Preventing the Loss of Control File Records"](rcmmaint.md) to learn how to monitor the overwriting of control file records

#### Manually Resynchronizing the Recovery Catalog

Use `RESYNC` `CATALOG` to force a full resynchronization of the recovery catalog with a target database control file. You can specify a database unique name with `RESYNC FROM DB_UNIQUE_NAME` or `ALL`, depending on whether you want to resynchronize a specific database or all databases in the Data Guard environment. Typically, you would perform this operation after you have run the `CONFIGURE` command for a standby database, but have not yet connected to this standby database.

1. Start RMAN and connect to a target database and recovery catalog.
2. Mount or open the target database:
	```
	STARTUP MOUNT;
	```
3. Resynchronize the recovery catalog.
	Run the `RESYNC` `CATALOG` command at the RMAN prompt as follows:
	```
	RESYNC CATALOG;
	```
	The following example resynchronizes the control file of `standby1`:
	```
	RESYNC CATALOG FROM DB_UNIQUE_NAME standby1;
	```
	The following variation resynchronizes the control files for all databases in the Data Guard environment:
	```
	RESYNC CATALOG FROM DB_UNIQUE_NAME ALL;
	```
	See Also:
	- [Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta2009.htm#RCMRF150) for `RESYNC` `CATALOG` command syntax
	- [Oracle Data Guard Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e41134/rman.htm#SBYDB04700) to learn how to configure the RMAN environment for use with a standby database

### Updating the Recovery Catalog After Changing a DB\_UNIQUE\_NAME

You may decide to change the `DB_UNIQUE_NAME` of a database in a Data Guard environment. In this case, you can run the `CHANGE DB_UNIQUE_NAME` command to associate the metadata stored in recovery catalog for the old `DB_UNIQUE_NAME` to the new `DB_UNIQUE_NAME`. The `CHANGE DB_UNIQUE_NAME` command does not actually change the `DB_UNIQUE_NAME` of the database itself. Instead, it updates the catalog metadata for the database whose unique name has been or will be changed.

The following procedure assumes that the `DB_UNIQUE_NAME` of the primary database is `prodny`, and that you have changed the `DB_UNIQUE_NAME` of a standby database from `prodsf1` to `prodsf2`. You can use the same procedure after changing the `DB_UNIQUE_NAME` of a primary database, except in Step 1 connect RMAN as `TARGET` to a standby database instead of a primary database.

To update the recovery catalog after a `DB_UNIQUE_NAME` is changed:

1. Connect RMAN to the primary database as `TARGET` and also to the recovery catalog. For example, enter the following commands:
	```
	% rman
	RMAN> CONNECT CATALOG catowner@catdb
	recovery catalog database Password: password
	connected to recovery catalog database
	RMAN> CONNECT TARGET SYS@prodny
	target database Password: password
	connected to target database: PRODNY (DBID=39525561)
	```
2. List the `DB_UNQUE_NAME` values known to the recovery catalog.
	Run the following `LIST` command:
	```
	RMAN> LIST DB_UNIQUE_NAME OF DATABASE;
	```
3. Change the `DB_UNIQUE_NAME` in the RMAN metadata.
	The following example changes the database unique name from standby database `prodsf1` to `prodsf2`:
	```
	RMAN> CHANGE DB_UNIQUE_NAME FROM prodsf1 TO prodsf2;
	```

### Unregistering a Target Database from the Recovery Catalog

You can use the `UNREGISTER DATABASE` command to unregister a database from the recovery catalog. When a database is unregistered from the recovery catalog, all RMAN repository records in the recovery catalog are lost. The database can be registered again, but the recovery catalog records for that database are then based on the contents of the control file at the time of reregistration. Records older than the `CONTROLFILE_RECORD_KEEP_TIME` setting in the target database control file are lost. Stored scripts, which are not stored in the control file, are also lost.

#### Unregistering a Target Database When Not in a Data Guard Environment

This scenario assumes that you are not using the recovery catalog to store metadata for primary and standby databases.

To unregister a database:

1. Start RMAN and connect as `TARGET` to the database to unregister. Also connect to the recovery catalog.
	It is not necessary to connect to the target database, but if you do not, then you must specify the name of the target database in the `UNREGISTER` command. If multiple databases have the same name in the recovery catalog, then you must create a `RUN` block around the command and use `SET DBID` to set the DBID for the database.
2. Make a note of the DBID as displayed by RMAN at startup.
	For example, RMAN outputs a line of the following form when it connects to a target database that is open:
	```
	connected to target database: PROD (DBID=39525561)
	```
3. As a precaution, it may be useful to list all of the backups recorded in the recovery catalog using `LIST BACKUP SUMMARY` and `LIST COPY SUMMARY`. This way, you can recatalog backups not known to the control file if you later decide to reregister the database.
4. If your intention is to actually delete all backups of the database completely, then run `DELETE` statements to delete all existing backups. Do not delete all backups if your intention is only to remove the database from the recovery catalog and rely on the control file to store the RMAN metadata for this database.
	The following commands illustrate how to delete backups:
	```
	DELETE BACKUP DEVICE TYPE sbt;
	DELETE BACKUP DEVICE TYPE DISK;
	DELETE COPY;
	```
	RMAN lists the backups that it intends to delete and prompts for confirmation before deleting them.
5. Run the `UNREGISTER` `DATABASE` command. For example:
	```
	UNREGISTER DATABASE;
	```
	RMAN displays the database name and DBID, and prompts you for a confirmation:
	```
	database name is "RDBMS" and DBID is 931696259
	 
	Do you really want to unregister the database (enter YES or NO)? yes
	```
	When the process is complete, RMAN outputs the following message:
	```
	database unregistered from the recovery catalog
	```

#### Unregistering a Standby Database

The `UNREGISTER` command supports a `DB_UNIQUE_NAME` clause for use in a Data Guard environment. You can use this clause to remove metadata for a specific database.

The recovery catalog associates a backup with a particular database. When you unregister a database, RMAN updates the database name for these backup files to `null`. Thus, the backups are still recorded but have no owner. You can execute the `CHANGE ... RESET DB_UNIQUE_NAME` command to associate ownership of the currently ownerless backups to a different database. If you specify `INCLUDING BACKUPS` on the `UNREGISTER` command, then RMAN removes the backup metadata for the unregistered database as well.

In this scenario, assume that primary database `lnx3` has an associated standby database `standby`. You want to unregister the standby database.

To unregister a standby database:

1. Start RMAN and connect as `TARGET` to the primary database. Also, connect RMAN to a recovery catalog.
	For example, enter the following commands:
	```
	% rman
	RMAN> CONNECT TARGET SYS@lnx3
	target database Password: password
	connected to target database: LNX3 (DBID=781317675)
	RMAN> CONNECT CATALOG rman@catdb
	```
2. List the database unique names.
	For example, execute the `LIST DB_UNIQUE_NAME` command as follows:
	```
	RMAN> LIST DB_UNIQUE_NAME OF DATABASE;
	List of Databases
	DB Key  DB Name DB ID             Database Role   Db_unique_name
	------- ------- ----------------- --------------- ------------------
	1       LNX3    781317675         STANDBY         STANDBY
	1       LNX3    781317675         PRIMARY         LNX3
	```
3. Run the `UNREGISTER` `DB_UNIQUE_NAME` command.
	For example, execute the `UNREGISTER` command as follows to unregister database `standby`:
	```
	RMAN> UNREGISTER DB_UNIQUE_NAME standby;
	```
	RMAN displays the database name and DBID, and prompts you for a confirmation:
	```
	database db_unique_name is "standby", db_name is "LNX3" and DBID is 781317675
	 
	Do you really want to unregister the database (enter YES or NO)? yes
	```
	When the process is complete, RMAN outputs the following message:
	```
	database with db_unique_name standby unregistered from the recovery catalog
	```

### Resetting the Database Incarnation in the Recovery Catalog

As explained in ["Database Incarnations"](rcmrvcon.md), you create an [incarnation](glossary.md) of the database when you open the database with the `RESETLOGS` option. You can access a record of the new incarnation in the `V$DATABASE_INCARNATION` view.

If you open the database with the `RESETLOGS` option, then a new database incarnation record is automatically created in the recovery catalog. The database also implicitly and automatically issues a `RESET` `DATABASE` command, which specifies that this new incarnation of the database is the current incarnation. All subsequent backups and log archiving done by the target database is associated with the new database incarnation.

Whenever RMAN returns the database to an SCN before the current `RESETLOGS` SCN, using either `RESTORE` and `RECOVER` or `FLASHBACK DATABASE`, the `RESET DATABASE TO INCARNATION` command is required. However, you do not need to execute `RESET DATABASE TO INCARNATION` explicitly in the following scenarios because RMAN runs the command implicitly with Flashback.

- You use `FLASHBACK DATABASE` to rewind the database to an SCN in the [direct ancestral path](glossary.md) (see ["Database Incarnations"](rcmrvcon.md) for an explanation of the direct ancestral path).
- You use `FLASHBACK DATABASE` to rewind the database to a [restore point](glossary.md).

The following procedure explains how to reset the database incarnation when recovering through a `RESETLOGS`.

To reset the recovery catalog to an older incarnation for media recovery:

1. Determine the incarnation key of the desired database incarnation. Obtain the incarnation key value by issuing a `LIST` command:
	```
	LIST INCARNATION OF DATABASE trgt;
	List of Database Incarnations
	DB Key  Inc Key   DB Name   DB ID       STATUS     Reset SCN    Reset Time
	------- -------   -------   ------      -------    ----------   ----------
	1       2         TRGT      1224038686  PARENT     1            02-JUL-02
	1       582       TRGT      1224038686  CURRENT    59727        10-JUL-02
	```
	The incarnation key is listed in the `Inc Key` column.
2. Reset the database to the old incarnation. For example, enter:
	```
	RESET DATABASE TO INCARNATION 2;
	```
3. If the control file of the previous incarnation is available and mounted, then skip to Step 6 of this procedure. Otherwise, shut down the database and start it without mounting. For example:
	```
	SHUTDOWN IMMEDIATE
	STARTUP NOMOUNT
	```
4. Restore a control file from the old incarnation. If you have a control file tagged, then specify the tag. Otherwise, you can run the `SET` `UNTIL` command, as in this example:
	```
	RUN 
	{
	  SET UNTIL 'SYSDATE-45';
	  RESTORE CONTROLFILE; # only if current control file is not available
	}
	```
5. Mount the restored control file:
	```
	ALTER DATABASE MOUNT;
	```
6. Run `RESTORE` and `RECOVER` commands to restore and recover the database files from the prior incarnation, then open the database with the `RESETLOGS` option. For example, enter:
	```
	RESTORE DATABASE;
	RECOVER DATABASE;
	ALTER DATABASE OPEN RESETLOGS;
	```
	See Also:
	[Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta2007.htm#RCMRF148) for `RESET` `DATABASE` syntax, [Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta027.htm#RCMRF132) for `LIST` syntax

### Upgrading the Recovery Catalog

This section explains what a recovery catalog upgrade is and when you must do it.

#### About Recovery Catalog Upgrades

If you use a version of the recovery catalog schema that is older than that required by the RMAN client, then you must upgrade it. The compatibility matrix in [Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/compat001.htm#RCMRF005) explains which schema versions are compatible with which versions of RMAN. For example, you must upgrade the catalog if you use an Oracle Database 11g RMAN client with a release 10.2 version of the recovery catalog schema.

The Oracle Database 10gR1 version of the recovery catalog schema requires the `CREATE TYPE` privilege. If you created the recovery catalog owner in a release before 10gR1, and if you granted the `RECOVERY_CATALOG_OWNER` role when it did not include the `CREATE TYPE` privilege, then you must grant `CREATE TYPE` to this user explicitly before upgrading the catalog.

You receive an error when issuing `UPGRADE` `CATALOG` if the recovery catalog is at a version greater than that required by the RMAN client. RMAN permits the `UPGRADE` `CATALOG` command to be run if the recovery catalog is current and does not require upgrading, however, so that you can re-create packages at any time if necessary. Check the message log for error messages generated during the upgrade.

##### Special Considerations in a Data Guard Environment

Assume that you upgrade the recovery catalog schema to Oracle Database 11g in a Data Guard environment. When RMAN connects to a standby database, it automatically registers the new database information and resynchronizes to obtain the file names from the control file.

During the resynchronization, RMAN associates the names with the target database name. Because the recovery catalog contains historical metadata, some records in the catalog are not known to the control file. For example, the `standby1` control file does not know about all backups made on `primary1`. The database unique names for these old records is `null`. As explained in "About Recovery Catalog Maintenance", you can use `CROSSCHECK` to fix these records.

#### Determining the Schema Version of the Recovery Catalog

The schema version of the recovery catalog is stored in the recovery catalog itself. The information is important in case you maintain multiple databases of different versions in your production system, and must determine whether the catalog schema version is usable with a specific target database version.

To determine the schema version of the recovery catalog:

1. Start SQL\*Plus and connect to the recovery catalog database as the catalog owner.
2. Query the `RCVER` table to obtain the schema version, as in the following example (sample output included):
	```
	SELECT *
	FROM   rcver;
	VERSION
	------------
	10.02.00
	```

If the table displays multiple rows, then the highest version in the `RCVER` table is the current catalog schema version. The table stores only the major version numbers and not the patch numbers. For example, assume that the `rcver` table displays the following rows:

```
VERSION
------------
08.01.07
09.00.01
10.02.00
```

These rows indicate that the catalog was created with a release 8.1.7 executable, then upgraded to release 9.0.1, and finally upgraded to release 10.2.0. The current version of the catalog schema is 10.2.0.

See Also:

[Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/compat001.htm#RCMRF005) for the complete set of compatibility rules governing the RMAN environment

#### Using the UPGRADE CATALOG Command

This scenario assumes that you are upgrading a recovery catalog schema to the current version.

To upgrade the recovery catalog:

1. If you created the recovery catalog owner in a release before 10gR1, and if the `RECOVERY_CATALOG_OWNER` role did not include the `CREATE TYPE` privilege, then grant it.
	For example, start SQL\*Plus and connect to the recovery catalog database with administrator privileges. You can then execute the following `GRANT` statement:
	```
	SQL> GRANT CREATE TYPE TO rman;
	SQL> EXIT;
	```
2. Start RMAN and connect RMAN to the recovery catalog database.
3. Run the `UPGRADE` `CATALOG` command:
	```
	RMAN> UPGRADE CATALOG;
	recovery catalog owner is rman 
	enter UPGRADE CATALOG command again to confirm catalog upgrade
	```
4. Run the `UPDATE` `CATALOG` command again to confirm:
	```
	RMAN> UPGRADE CATALOG;
	recovery catalog upgraded to version 11.01.00
	DBMS_RCVMAN package upgraded to version 11.01.00
	DBMS_RCVCAT package upgraded to version 11.01.00
	```

See Also:

- [Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta2023.htm#RCMRF161) for `UPGRADE` `CATALOG` command syntax
- [Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/compat.htm#RCMRF908) for information about recovery catalog compatibility
- [Oracle Database Upgrade Guide](https://docs.oracle.com/cd/E11882_01/server.112/e23633/toc.htm) for complete compatibility and migration information

### Importing and Moving a Recovery Catalog

You can use the `IMPORT CATALOG` command in RMAN to merge one recovery catalog schema into another. This command is useful in the following situations:

- You have multiple recovery catalog schemas for different versions of the database. You want to merge all existing schemas into one without losing backup metadata.
- You want to move a recovery catalog from one database to another database.

#### About Recovery Catalog Imports

When using `IMPORT CATALOG`, the source catalog schema is the catalog schema that you want to import into a different schema. The destination catalog schema is the catalog schema into which you intend to import the source catalog schema.

By default, RMAN imports metadata from all target databases registered in the source recovery catalog. Optionally, you can specify the list of database IDs to be imported from the source catalog schema.

By default, RMAN unregisters the imported databases from the source catalog schema after a successful import. To indicate whether the unregister was successful, RMAN prints messages before and after unregistering the merged databases. You can also specify the `NO UNREGISTER` option to specify that the databases should not be unregistered from the destination catalog.

A [stored script](glossary.md) is either global or local. It is possible for global scripts, but not local scripts, to have name conflicts during import because the destination schema contains the script name. In this case, RMAN renames the global script name to `COPY OF` `script_name`. For example, RMAN renames `bp_cmd` to `COPY OF bp_cmd`.

If the renamed global script is still not unique, then RMAN renames it to `COPY(2) OF` `script_name`. If this script name also exists, then RMAN renames the script to `COPY(3) OF` `script_name`. RMAN continues the `COPY(``n``) OF` pattern until the script is uniquely named.

#### Prerequisites for Importing a Recovery Catalog

As shown in compatibility matrix in [Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/compat001.htm#RCMRF005), a target database, recovery catalog database, and recovery catalog schema can be at different database versions. The recommended practice is to import all existing recovery catalogs into a single recovery catalog at the latest version of the recovery catalog schema. "Determining the Schema Version of the Recovery Catalog" explains how to determine the catalog version. Check the compatibility matrix to determine which schema versions are compatible in your environment.

When using `IMPORT CATALOG`, the version of the source recovery catalog schema must be equal to the current version of the RMAN executable with which you run the command. If the source catalog schema is a lower version, then upgrade it to the current version before importing the schema. "Upgrading the Recovery Catalog" explains how to upgrade. If the source recovery catalog schema is a higher version, then retry the import with a higher version RMAN executable.

No database can be registered in both the source and destination catalog schema. If a database is currently registered in both catalog schemas, then unregister the database from source catalog schema before performing the import.

#### Importing a Recovery Catalog

When importing one recovery catalog into another, no connection to a target database is necessary. RMAN only needs connectivity to the source and destination catalogs.

In this example, database `srcdb` contains a 10.2 recovery catalog schema owned by user `102cat`, while database `destdb` contains an 11.1 recovery catalog schema owned by user `111cat`.

To import a recovery catalog:

1. Start RMAN and connect as `CATALOG` to the destination recovery catalog schema. For example:
	```
	% rman
	RMAN> CONNECT CATALOG 111cat@destdb;
	```
2. Import the source recovery catalog schema, specifying the connection string for the source catalog.
	For example, enter the following command to import the catalog owned by `102cat` on database `srcdb`:
	```
	IMPORT CATALOG 102cat@srcdb;
	```
	A variation is to import metadata for a subset of the target databases registered in the source catalog. You can specify the databases by DBID or database name, as shown in the following examples:
	```
	IMPORT CATALOG 102cat@srcdb DBID=1423241, 1423242;
	IMPORT CATALOG 102cat@srcdb DB_NAME=prod3, prod4;
	```
3. Optionally, connect to a target database to check that the metadata was successfully imported. For example, the following commands connect to database `prod1` as `TARGET` and list all backups for this database:
	```
	LIST BACKUP;
	```

#### Moving a Recovery Catalog

The procedure for moving a recovery catalog from one database to another is a variation of the procedure for importing a catalog. In this scenario, the source database is the database containing the existing recovery catalog, while the destination database will contain the moved recovery catalog.

To move a recovery catalog from the source database to the destination database:

1. Create a recovery catalog on the destination database, but do not register any databases in the new catalog.
	"Creating a Recovery Catalog" explains how to perform this task.
2. Import the source catalog into the catalog created in the preceding step.
	"Importing a Recovery Catalog" explains how to perform this task.

## Dropping a Recovery Catalog

The `DROP` `CATALOG` command removes those objects that were created by the `CREATE CATALOG` command. If the user who owns the recovery catalog also owns objects that were not created by `CREATE CATALOG`, then the `DROP CATALOG` command does not remove these objects.

If you drop a recovery catalog, and if you have no backups of the recovery catalog schema, then backups of all target databases registered in this catalog may become unusable. However, the control file of every target database still retains a record of recent backups of this database.

The `DROP` `CATALOG` command is not appropriate for unregistering a single database from a recovery catalog that has multiple target databases registered. Dropping the recovery catalog deletes the recovery catalog record of backups for all target databases registered in the catalog.

To drop a recovery catalog schema:

1. Start RMAN and connect to a target database and recovery catalog. Connect to the recovery catalog as the owner of the catalog schema to be dropped.
	The following example connects to a recovery catalog as user `catowner`:
	```
	% rman TARGET / CATALOG catowner@catdb
	```
2. Run the `DROP` `CATALOG` command:
	```
	DROP CATALOG;
	recovery catalog owner is catowner
	enter DROP CATALOG command again to confirm catalog removal
	```
3. Run the `DROP` `CATALOG` command again to confirm:
	```
	DROP CATALOG;
	```
	Note:
	Even after you drop the recovery catalog, the control file still contains records about the backups. To purge RMAN repository records from the control file, re-create the control file.
	See Also:
	[Oracle Database Backup and Recovery Reference](https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta018.htm#RCMRF125) for `DROP` `CATALOG` command syntax, and "Unregistering a Target Database from the Recovery Catalog" to learn how to unregister a database from the catalog