---
title: "User's Guide and Reference"
book: "SQL*Plus User's Guide and Reference"
doc_id: F31846-03
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/sqpug/database-administration-with-SQL-Plus.html
tags:
  - oracle
  - 21c
  - sqlplus-users-guide-and-reference
---

This chapter provides a brief overview of the database administration tools available in SQL\*Plus, and discusses the following topics:

This chapter is intended for use by database administrators. You must have database administrator privileges to use this functionality.

For more information on database administration, see the [Oracle Database Concepts](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqpug&id=CNCPT) manual.

### 11.1 Overview

Special operations such as starting up or shutting down a database are performed by a database administrator (DBA). The DBA has certain privileges that are not assigned to normal users. The commands outlined in this chapter would normally be used by a DBA.

For more information about security and roles in SQL\*Plus, see [SQL\*Plus Security](SQL-Plus-security.md).

### 11.2 Introduction to Database Startup and Shutdown

An Oracle database may not always be available to all users. To open or close a database, or to start up or shut down an instance, you must have DBA privileges or be connected as SYSOPER or SYSDBA. Other users cannot change the current status of an Oracle database.

#### 11.2.1 Database Startup

To start a database:

1. Start an instance
	An instance controls the background processes and the allocation of memory area to access an Oracle database.
2. Mount the database
	Mounting the database associates it with a previously started instance.
3. Open the database
	Opening the database makes it available for normal database operations.

Example 11-1 Starting an Instance

To start an Oracle Database instance, without mounting the database, enter

```
STARTUP NOMOUNT
```

Example 11-2 Mounting the Database

To start an instance, mount the database, but leave the database closed, enter

```
STARTUP MOUNT
```

Example 11-3 Opening the Database

To start an instance using the Oracle Database Server parameter file INITSALES.ORA, mount and open the database named SALES, and restrict access to database administrators, enter

```
STARTUP OPEN sales PFILE=INITSALES.ORA RESTRICT
```

where SALES is the database name specified in the DB\_NAME parameter in the INITSALES.ORA parameter file.

For more information about database startup, see [Starting Up and Shutting Down](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqpug&id=ADMIN-GUID-045DE684-6680-4099-A49E-2F5B5FA59670). For more information about starting a database, see the [STARTUP](STARTUP.md) command.

#### 11.2.2 PDB Startup

A Pluggable Database (PDB) is a self-contained collection of schemas and schema objects that exist inside a Consolidated Database.

To start a pluggable database:

1. Start SQL\*Plus with the `/NOLOG` argument:
	```
	sqlplus /nolog
	```
2. Issue a `CONNECT` command using easy connect or a net service name to connect to the PDB.
3. Issue a STARTUP command.

Another way to open a pluggable database is to connect to the CDB and use the following command:

```
ALTER PLUGGABLE DATABASE pdbname OPEN;
```

For more information about database startup, see [Starting Up and Shutting Down](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqpug&id=ADMIN-GUID-045DE684-6680-4099-A49E-2F5B5FA59670). For more information about starting a database, see the [STARTUP](STARTUP.md) command.

#### 11.2.3 Database Shutdown

Shutting down a database involves three steps:

1. Closing the database
	When a database is closed, all database and recovery data in the SGA are written to the datafiles and redo log files, and all online datafiles are closed.
2. Dismounting the database
	Dismounting the database disassociates the database from an instance and closes the control files of the database.
3. Shutting down the instance
	Shutting down an instance reclaims the SGA from memory and terminates the background Oracle Database processes that constitute an Oracle Database instance.

Example 11-4 Shutting Down the Database

To shut down the database normally after it has been opened and mounted, enter

```
SHUTDOWN
```

For more information about database shutdown, see [Shutting Down a Database](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqpug&id=ADMIN-GUID-3661B282-5C34-4E32-BC6A-906A72712866). For information about stopping a database, see the [SHUTDOWN](SHUTDOWN.md) command.

```
Database closed.
Database dismounted.
ORACLE instance shut down.
```

#### 11.2.4 PDB Shutdown

To shutdown a pluggable database (PDB):

1. Connect to the PDB with the required privileges.
2. Run the `SHUTDOWN` command.

Note:

When the current container is a PDB, the `SHUTDOWN` command only closes the PDB, not the CDB instance.

For more information about database startup, see the [Oracle Database Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqpug&id=ADMIN14103) guide. For more information about starting a database, see the [STARTUP](STARTUP.md) command.

### 11.3 Redo Log Files

Every Oracle database has a set of two or more redo log files. The set of redo log files for a database is collectively referred to as the database's redo log.

The redo log is used to record changes made to data. If, for example, there is a database failure, the redo log is used to recover the database. To protect against a failure involving the redo log itself, Oracle Database has a mirrored redo log so that two or more copies of the redo log can be maintained on different disks.

#### 11.3.1 ARCHIVELOG Mode

Operating a database in ARCHIVELOG mode enables the archiving of the online redo log.

The SQL ALTER SYSTEM command enables a complete recovery from disk failure as well as instance failure, because all changes made to the database are permanently saved in an archived redo log.

For more information about redo log files and database archiving modes, see the [ARCHIVE LOG](ARCHIVE-LOG.md) command.

To list the details of the current log file being archived, enter

```
ARCHIVE LOG LIST
```
```
Database log mode              Archive Mode 
Automatic archival             Enabled 
Archive destination            /vobs/oracle/dbs/arch 
Oldest online log sequence     221 
Next log sequence to archive   222 
Current log sequence           222
```

### 11.4 Database Recovery

If a damaged database is in ARCHIVELOG mode, it is a candidate for either complete media recovery or incomplete media recovery operations. To begin media recovery operations use the RECOVER command. For more information about recovering data, see the [RECOVER](RECOVER.md) command.

In order to begin recovery operations, you must have DBA privileges.

To recover the database up to a specified time using a control backup file, enter

```
RECOVER DATABASE UNTIL TIME '1998-11-23:12:47:30'-
USING BACKUP CONTROLFILE
```

To recover two offline tablespaces, enter

```
RECOVER TABLESPACE ts1, ts2
```

Make sure that the tablespaces you are interested in recovering have been taken offline, before proceeding with recovery for those tablespaces.