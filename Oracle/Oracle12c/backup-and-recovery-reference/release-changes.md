---
title: Database Backup and Recovery Reference
book: Database Backup and Recovery Reference
doc_id: E85640-04
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/rcmrf/release-changes.html
tags:
  - oracle
  - 12c
  - backup-and-recovery-reference
---

This preface contains:

### Changes in Oracle Database 12c Release 2 (12.2.0.1)

The following are changes in the Oracle Database Backup and Recovery Reference for Database 12c Release 2 (12.2.0.1).

New Features

- Perform flashback on a pluggable database (PDB) to a specified point in time
	You can perform a flashback database operation to rewind an individual PDB to a previous point in time. This enables you to reverse unwanted changes made to a single PDB without impacting the operation of the remaining PDBs.
	See [FLASHBACK DATABASE](FLASHBACK-DATABASE.md).
- Validation and recovery of nonlogged data blocks
	In a Data Guard environment, you can perform recovery of nonlogged data blocks by fetching data blocks from the primary or physical standby database. You can also perform validation to determine if the data blocks in the nonlogged block ranges are still invalid.
	See [RECOVER](RECOVER.md) and [VALIDATE](VALIDATE.md).
- Enhancements to table recovery
	You can use the `REMAP TABLE` clause to recover tables or table partitions into a schema that is different from the schema in which these objects originally existed.
	See [RECOVER](RECOVER.md).
- Enhancements to the `DUPLICATE` command
	Use the `FOR FARSYNC` clause of the `DUPLICATE` command to create an Oracle Data Guard far sync instance by duplicating a target database.
	[DUPLICATE](DUPLICATE.md)
	To duplicate a database that uses transparent encryption with a password-based keystore, the password used to open the keystore is provided to the auxiliary instance using the `SET DECRYPTION WALLET OPEN` command.
	[SET](SET.md)
- Enhancements to cross-platform transport
	RMAN supports cross-platform transport of a PDB into a target CDB. You can perform cross-platform transport of tablespaces over the network. Encrypted tablespaces can also be transported to different platforms.
	See [BACKUP](BACKUP.md), [RECOVER](RECOVER.md), [RESTORE](RESTORE.md), and [foreignFileSpec](foreignFileSpec.md).
- Backup and Recovery of Sparse Databases
	RMAN enables you to backup, restore, recover, and duplicate sparse data files, tablespaces, CDBs, PDBs, and whole databases with the `COMPATIBLE` initialization parameter set to 12.2 or higher.
	See [BACKUP](BACKUP.md), [DUPLICATE](DUPLICATE.md), [RECOVER](RECOVER.md), [RESTORE](RESTORE.md)

### Changes in Oracle Database 12c Release 1 (12.1.0.2)

The following are changes in Backup and Recovery Reference for Oracle Database 12c Release 1 (12.1.0.2).

#### New Features

- Oracle Virtual Private Database (VPD) for RMAN Virtual Private Catalogs
	The RMAN catalog is created and managed using VPD. This provides better performance and scalability for the recovery catalog especially with a large number of virtual private catalogs. The implementation details are transparent to users.
	See:
	- " [CREATE CATALOG](CREATE-CATALOG.md) "
	- " [DROP CATALOG](DROP-CATALOG.md) "
	- " [UPGRADE CATALOG](UPGRADE-CATALOG.md) "

### Changes in Oracle Database 12c Release 1 (12.1.0.1)

The following are changes in Backup and Recovery Reference for Oracle Database 12c Release 1 (12.1.0.1).

#### New Features

- Support for multitenant container databases and pluggable databases
	RMAN supports backup and recovery of multitenant container databases (CDBs) and pluggable databases (PDBs), which are introduced in Oracle Database 12c. The support includes backing up CDBs and PDBs and performing both complete and point-in-time recovery of entire CDBs or individual PDBs.
- Cross-platform backup and restore enhancements
	RMAN enables you to transport data across platforms by using full and incremental backup sets. Incremental backups can be used to reduce application downtime required when transporting tablespaces across platforms.
- Recovering tables and table partitions
	RMAN can recover tables and table partitions to a specified point in time from previously-created RMAN backups.
	See " [RECOVER](RECOVER.md) ".
- Recovering and restoring files over a network
	RMAN enables you to recover a database, data files, tablespaces, or control files by using backup sets from a physical standby database. RMAN transfers the backup sets over the network to the destination host. This is useful in a Data Guard environment when you want to synchronize the standby and primary databases.
- Improved support for third-party snapshot technologies using Storage Snapshot Optimization
	Storage Snapshot Optimization enables you to use storage snapshot technology to backup and recover Oracle databases without placing them in `BACKUP` mode. The snapshot technology must adhere to certain qualifications.
	See:
	- " [RECOVER](RECOVER.md) "
	- " [Recovery Using Storage Snapshots](RECOVER.md) "
- Incremental and multisection backup improvements
	The multisection technology provided by RMAN, which allows very large files to be backed up and restored by multiple channels in parallel, can now be applied to both incremental backups and image copies.
- `SYSBACKUP` Privilege
	The `SYSBACKUP` administrative privilege encompasses the permissions required for backup and recovery, including the ability to connect to a closed database. System administrators can grant `SYSBACKUP` instead of `SYSDBA` to users who perform backup and recovery, thus reducing the proliferation of the `SYSDBA` privilege. In contrast to `SYSDBA`, `SYSBACKUP` does not include data access privileges such as `SELECT ANY TABLE`.
- Active database duplication enhancements
	RMAN can now use backup sets to perform active database duplication. When sufficient auxiliary channels are allocated, the auxiliary instance connects to the target instance and retrieves the backup sets over the network, thus reducing the processing load on the target instance. Unused block compression can be used during the duplication process, thus reducing the size of backups transported over the network. You can also encrypt backups and use multisection backups while performing active database duplication
	See " [DUPLICATE](DUPLICATE.md) ".
- SQL interface enhancements
	You can now issue most SQL commands in RMAN without preceding the command with the SQL keyword and enclosing the SQL command in quotes. This greatly simplifies the syntax when the SQL command itself requires quotation marks. For a few commands that exist in both RMAN and SQL, you can specify the SQL keyword to eliminate ambiguity.
	The SQL `ALTER` command replaces the RMAN command. The new RMAN `DESCRIBE` command provides the functionality of the SQL\*Plus `DESCRIBE` command.
- DUPLICATE enhancements
	You can use the `NOOPEN` clause to specify that the duplicate database must not be opened using `RESETLOGS` after it is created. You may prefer not to open the duplicate database if you want to change the initialization parameters of the duplicate database or if opening the duplicate database may start services in the duplicate database that will conflict with the original database.
	See " [DUPLICATE](DUPLICATE.md) ".