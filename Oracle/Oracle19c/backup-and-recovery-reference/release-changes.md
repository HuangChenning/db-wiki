---
title: Backup and Recovery Reference
book: Oracle AI Database Backup and Recovery Reference
doc_id: E96242-15
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/rcmrf/release-changes.html
tags:
  - oracle
  - 19c
  - backup-and-recovery-reference
---

## Changes in This Release for Backup and Recovery Reference

This preface contains:

- Changes in Oracle Database Release 19c
- Changes in Oracle Database Release 18c, Version 18.1

### Changes in Oracle Database Release 19c

The following are changes in Oracle Database Backup and Recovery Reference for Oracle Database release 19c.

New Features

- `PLUGGABLE DATABASE` clause in `GRANT` and `REVOKE` commands
	You can grant and revoke privileges on a specific PDB to a database user. See [GRANT](GRANT.md) and [REVOKE](REVOKE.md).
- Recovery catalog support for PDBs
	You can connect to the recovery catalog when you are connected to a target PDB.
	See [CONNECT](CONNECT.md).

Deprecated Features

- Starting in Oracle Database 19c, the Data Recovery Advisor (DRA) feature is deprecated.
	The deprecation of DRA includes deprecation of the following Oracle Recovery Manager (RMAN) commands: `LIST FAILURE`, `ADVISE FAILURE`, `REPAIR                     FAILURE`, and `CHANGE FAILURE`. Database administrators will no longer have access to these commands. There is no replacement feature for DRA.
- The `RECOVER…SNAPSHOT TIME` method of recovering a database to a point in time using a particular snapshot is deprecated in Oracle Database 19c.
	Instead of `RECOVER…SNAPSHOT TIME`, Oracle recommends that you use `ALTER DATABASE BEGIN/END BACKUP` before and after creating the storage snapshot of the data files and then use `RECOVER .. UNTIL                     TIME` to a specific timestamp or system change number (SCN) after the `END BACKUP` completion time. Oracle recommends that `ALTER DATABASE BEGIN/END BACKUP` always be used when performing snapshots on a running database to ensure data recovery integrity. Archived log redo logs must be separately backed up and restored for recovery operations.
	See [Recovery Using Storage Snapshot Optimization](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/rcmrf&id=BRADV-GUID-5A3BB8EE-291F-41C6-976C-1F304069FF0B) in the Backup and Recovery User's Guide for detailed examples.

### Changes in Oracle Database Release 18c, Version 18.1

The following are changes in Oracle Database Backup and Recovery Reference for Oracle Database release 18c, version 18.1.

New Features

- Duplicate PDBs to an existing CDB
	The `DUPLICATE PLUGGABLE DATABASE` command is used to duplicate a PDB to an existing CDB.
	See Also:
	[DUPLICATE](DUPLICATE.md)
- Duplicate databases to Oracle Cloud
	An on-premises database can be duplicated to Oracle Cloud. Similarly, you can duplicate a database in Oracle Cloud as an on-premises database.
	See Also:
	`AS ENCRYPTED` and `AS DECRYPTED` clauses in [DUPLICATE](DUPLICATE.md)
- RMAN backups usable after migration
	RMAN backups of a non-CDB or PDB that were created before the non-CDB or PDB was migrated and plugged in to a different target CDB can be used for recovery operations in the target CDB.