---
title: REGISTER DATABASE
book: Backup and Recovery Reference
doc_id: E10643-09
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta2002.htm
tags:
  - oracle
  - 11g
  - backup-and-recovery-reference
---

Purpose

Use the `REGISTER DATABASE` command to register the target database in the recovery catalog so that RMAN can maintain its metadata. RMAN obtains all information it needs to register the target database from the target database itself.

See Also:

[Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/cd/E11882_01/backup.112/e10642/rcmcatdb.htm#BRADV11001) and `CREATE CATALOG`

Prerequisites

Execute this command only at the RMAN prompt. RMAN must be connected to a recovery catalog and a mounted or open target database. The database that you are registering must not be currently registered in the recovery catalog.

You can only register a target database with a DBID that is unique within the recovery catalog. Databases with the same name are permitted if the DBID values are different. The database that you are registering must not be a standby database.

Usage Notes

RMAN automatically registers a new standby database in the recovery catalog when the primary database for the standby database is registered in the recovery catalog, and either of the following conditions is true:

- RMAN is connected to a database instance that has a `DB_UNIQUE_NAME` unknown to the recovery catalog.
- You execute the `CONFIGURE` `DB_UNIQUE_NAME` command for a database that is not known to the recovery catalog.

The `REGISTER DATABASE` command fails when RMAN detects duplicate DBIDs. This situation can arise when databases are created by copying files from an existing database rather than by using the `DUPLICATE` command. If this failure occurs, then you can change the DBID of the copied database with the DBNEWID utility and then retry the `REGISTER DATABASE` command.

If you open a database with the `RESETLOGS` option and later register this database in the recovery catalog, then the recovery catalog records the `DB_NAME` for the old incarnations as `UNKNOWN` because the old incarnations were not previously registered. You should not try to remove these records.

Note:

If you are using RMAN with different target databases that have the same database name and DBID, then be careful to always specify the correct recovery catalog schema when invoking RMAN.

See Also:

[Oracle Database Utilities](https://docs.oracle.com/cd/E11882_01/server.112/e22490/toc.htm) to learn how to use the DBNEWID utility

Example

Example 3-8 Registering a Database

This example registers a new target database in the recovery catalog. Sample output is included.

```
RMAN> CONNECT TARGET /
 
connected to target database: PROD (DBID=1619241818)
 
RMAN> CONNECT CATALOG rman@catdb
 
recovery catalog database Password: password
connected to recovery catalog database

RMAN> REGISTER DATABASE;
 
database registered in recovery catalog
starting full resync of recovery catalog
full resync complete
```