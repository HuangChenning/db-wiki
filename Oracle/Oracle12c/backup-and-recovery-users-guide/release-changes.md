---
title: "Database Backup and Recovery User's Guide"
book: "Database Backup and Recovery User's Guide"
doc_id: E85627-04
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/bradv/release-changes.html
tags:
  - oracle
  - 12c
  - backup-and-recovery-users-guide
---

This preface contains:

### Changes in Oracle Database 12c Release 2 (12.2.0.1)

The following are changes in the Oracle Database Backup and Recovery User’s Guide for Oracle Database 12c Release 2 (12.2.0.1).

New Features

- Support for restore points in PDBs
	You can create a PDB restore point, which is a restore point that is specific to a single [pluggable database (PDB)](glossary.md). Creating a PDB restore point for a particular PDB ensures that there are no name conflicts with restore points defined for other PDBs in the [multitenant container database (CDB)](glossary.md).
- Flashback Database support for PDBs
	You can perform a Flashback Database operation for a single PDB without impacting other PDBs in the [multitenant container database (CDB)](glossary.md). This enables you to rewind only the specified PDB, instead of the entire CDB, to a previous point in time. A Flashback Database operation on a particular PDB does not impact other PDBs in the CDB.
	In Oracle Database 12c Release 1 (12.1), to perform a flashback database operation for a CDB across PDB point-in-time recovery (PITR), you had to make all data files in the PDB for which PITR was performed offline. This restriction is now removed. You can perform a flashback database operation on a CDB across PDB PITR or PDB flashback with `COMPATIBLE` set to 12.2 or higher.
	See:
	- [Basic Concepts of Performing Flashback Database for CDBs and PDBs](rman-performing-flashback-dbpitr.md)
	- [Performing a Flashback Database Operation for a Whole CDB](rman-performing-flashback-dbpitr.md)
	- [Performing a Flashback Database Operation for PDBs](rman-performing-flashback-dbpitr.md)
	- [Performing Flashback Database with SQL\*Plus](user-managed-flashback-dbpitr.md)
- Enhancements to recovering tables and table partitions
	Before performing table recovery, RMAN checks if there is sufficient space on the target host to create the auxiliary instance that is used during recovery. You can also recover tables and table partitions into a schema that is different from the source schema in which they originally existed.
	See:
	- [Steps Performed By RMAN to Recover Tables and Table Partitions](rman-recovering-tables-partitions.md)
	- [About Recovering Tables and Partitions Into a New Schema](rman-recovering-tables-partitions.md)
	- [Example: Recovering a Table into a New Schema](rman-recovering-tables-partitions.md)
- Enhancements to cross-platform transport
	You can perform cross-platform transport of a PDB into a new CDB. Encrypted tablespaces can be transported across platforms. You can also restore and recover files across platforms and over the network.
	See:
	- [Performing Cross-Platform Transport of a Closed PDB](rman-transporting-data-across-platforms.md)
	- [Performing Cross-Platform Transport of a PDB Using Inconsistent Backups](rman-transporting-data-across-platforms.md)
	- [Steps to Transport Read-Only Tablespaces to a Different Platform Using Backup Sets](rman-transporting-data-across-platforms.md)
	- [Steps to Transport Inconsistent Tablespaces to a Different Platform](rman-transporting-data-across-platforms.md)
	- [Performing Cross-Platform Transport of Data Files Over the Network](rman-transporting-data-across-platforms.md)
- Enhancements to database duplication
	You can use the `DUPLICATE` command to create an Oracle Data Guard far sync instance.
	See [Duplicating the Whole Database](rman-duplicating-databases.md).
- Backup and recovery support for application containers
	You can use RMAN to perform backup, complete recovery, and point-in-time recovery of application containers. This includes the application root and one or more application PDBs.
	See:
	- [Backing Up Application Containers](backing-up-database.md)
	- [Performing Complete Recovery of Application Containers](rman-complete-database-recovery.md)
	- [Performing Point-in-Time Recovery of Application PDBs](rman-performing-flashback-dbpitr.md)
- Backup and Recovery of Sparse Databases
	RMAN enables you to perform backup, recovery, and backup-based duplication for sparse databases with the `COMPATIBLE` initialization parameter set to 12.2 or higher. You can also backup and recover individual sparse data files, tablespaces, CDBs, and PDBs.

### Changes in Oracle Database 12c Release 1 (12.1.0.2)

The following are changes in Backup and Recovery User's Guide for Oracle Database 12c Release 1 (12.1.0.2).

#### New Features

The following are the new features in this release:

- Oracle Virtual Private Database (VPD) for RMAN virtual private catalog
	The RMAN recovery catalog is created and managed using VPD. This provides better performance and scalability when a large number of virtual private catalogs are created.
	See:
	" [Creating and Managing Virtual Private Catalogs](managing-recovery-catalog.md) "

### Changes in Oracle Database 12c Release 1 (12.1.0.1)

The following are changes in Backup and Recovery User's Guide for Oracle Database 12c Release 1 (12.1.0.1).

#### New Features

The following are new features in this release:

- Support for multitenant container databases and pluggable databases
	RMAN provides backup and recovery of multitenant container databases (CDBs), which are introduced in Oracle Database 12c Release 1 (12.1). This support includes backup and point-in-time recovery of specified pluggable databases (PDBs).
	See:
	- " [Backing Up CDBs and PDBs](backing-up-database.md) "
	- " [Performing Point-in-Time Recovery of CDBs and PDBs](rman-performing-flashback-dbpitr.md) "
	- " [Performing Crash and Instance Recovery of CDBs](user-managed-flashback-dbpitr.md) "
- `SYSBACKUP` Privilege
	The `SYSBACKUP` administrative privilege encompasses the permissions required for backup and recovery, including the ability to connect to a closed database. System administrators can grant `SYSBACKUP` instead of `SYSDBA` to users who perform backup and recovery, thus reducing the proliferation of the `SYSDBA` privilege. In contrast to `SYSDBA`, `SYSBACKUP` does not include data access privileges such as `SELECT ANY TABLE`.
	See:
	" [Making Database Connections with RMAN](starting-interacting-with-rman-client.md) "
- Storage Snapshot Optimization
	Storage Snapshot Optimization enables you to use third-party technologies to take a storage snapshot of your database without putting the database in `BACKUP` mode. You can then use the snapshot to recover all or part of the database.
	See:
	- " [Making Backups with Third-Party Snapshot Technologies](user-managed-database-backups.md) "
	- " [Recovery Using Storage Snapshot Optimization](user-managed-flashback-dbpitr.md) "
- SQL Interface Improvements
	You can now issue most SQL commands in RMAN without preceding the command with the SQL keyword. For a few commands that exist in both RMAN and SQL and have very different uses, you can specify the `SQL` keyword to eliminate ambiguity. You no longer need to enclose the SQL command in quotes, which greatly simplifies the syntax when the SQL command itself requires quotation marks. The SQL `ALTER` command replaces the RMAN command.
	The new RMAN `DESCRIBE` command provides the functionality of the SQL\*Plus `DESCRIBE` command.
	See:
	[Oracle Database Backup and Recovery Reference](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/bradv&id=RCMRF)
- Multisection Backup Improvements
	RMAN provides multisection backup support for incremental backups and image copies. Wherever possible, unused block compression and Block Change Tracking are used in conjunction with multisection incremental backups. This improves backup and restore performance.
	See:
	- " [Specifying Multisection Incremental Backups](backing-up-database.md) "
	- " [Making Multisection Backups Using Image Copies](backing-up-database.md) "
- Restoring and Recovering Files Over a Network
	You can now restore or recover a database, data files, tablespaces, or control files by using backup sets from a physical standby database. RMAN transfers the backup sets, over the network, to the destination host. This is useful in a Data Guard environment when you want to synchronize the standby and primary databases.
	See:
	" [Restoring and Recovering Files Over the Network](rman-recovery-advanced.md) "
- Active Database Duplication Improvements
	RMAN can now perform active database duplication using backup sets. When sufficient auxiliary channels are allocated, the auxiliary instance connects to the target instance and retrieves the backup sets over the network, thus reducing the processing load on the target instance. Unused block compression can be used during the duplication process, thus reducing the size of backups transported over the network. You can specify the binary compression level to be used. You can also encrypt backups and use multisection backups while performing active database duplication.
	See:
	" [About Active Database Duplication with RMAN](rman-duplicating-databases.md) "
- Cross-Platform Backup and Restore Improvements
	You can transport data across platforms by using full and incremental backup sets. Incremental backups can reduce overall application downtime during cross-platform data migration.
	See:
	[Transporting Data Across Platforms](rman-transporting-data-across-platforms.md)
- Recovering Tables and Table Partitions from RMAN Backups
	RMAN can recover tables and table partitions to a specified point in time from previously-created RMAN backups.
	See:
	[Recovering Tables and Table Partitions from RMAN Backups](rman-recovering-tables-partitions.md)
- Unified auditing and RMAN
	Unified auditing consolidates all the Oracle Database audit records into one single audit trail. To use unified auditing, you must first upgrade your database to Oracle Database 12c Release 1 (12.1) and then migrate your database to use unified auditing.
	See:
	- [Oracle Database Upgrade Guide](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/bradv&id=UPGRD52810) for details about migrating your database to use unified auditing
	- [Oracle Database Security Guide](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/bradv&id=DBSEG401) for details about how to locate RMAN unified auditing information
- `DUPLICATE` enhancements
	You can specify that the duplicate database must not be opened using `RESETLOGS` after it is created. You may prefer not to open the duplicate database if you want to change the initialization parameters of the duplicate database or if opening the duplicate database may start services in the duplicate database that will conflict with the source database.
	See:
	" [Specifying the State of the Duplicate Database](rman-duplicating-databases.md) "