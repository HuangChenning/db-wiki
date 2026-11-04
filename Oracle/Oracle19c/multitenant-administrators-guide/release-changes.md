---
title: "Administrator’s Guide"
book: "Multitenant Administrator's Guide"
doc_id: E96136-19
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/multi/release-changes.html
tags:
  - oracle
  - 19c
  - multitenant-administrators-guide
---

## Changes in This Release for Oracle Multitenant Administrator’s Guide

- Changes in Oracle Database Release 19c, Version 19.1  
	Oracle Multitenant Administrator's Guide for Oracle Database release 19c, version 19.1 has the following changes.
- Changes in Oracle Database Release 18c, Version 18.1

### Changes in Oracle Database Release 19c, Version 19.1

Oracle Multitenant Administrator's Guide for Oracle Database release 19c, version 19.1 has the following changes.

- New Features  
	The following major features are new in this release.

**Parent topic:** Changes in This Release for Oracle Multitenant Administrator’s Guide

#### New Features

The following major features are new in this release.

- Workload capture and replay in a PDB
	A local user can capture, replay, and report on a workload at the PDB level.
	See " [About Using Manageability Features in a CDB](administering-a-cdb-with-sql-plus.md) " and [Oracle Database Testing Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=GUID-C6C2FA1F-3474-4B5A-B814-C41415B4C248).
- ADDM analysis for PDBs
	You can use ADDM to analyze AWR data stored inside the PDB through an AWR snapshot taken inside the PDB. You can also analyze AWR data of a non-CDB, CDB root, or PDB imported into the AWR storage of a PDB. Automatic ADDM of a PDB is disabled by default. You can enable it for a PDB by enabling automatic AWR snapshots.
	See " [About Using Manageability Features in a CDB](administering-a-cdb-with-sql-plus.md) " and [Oracle Database Performance Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=GUID-843A596D-2D8B-422D-9C8D-73C0EF52739D).
- Database Vault Operations Control for infrastructure database administrators
	You can use Oracle Database Vault to block common users (for example, infrastructure DBAs) from accessing local data in PDBs. Thus, common users are blocked from accessing local data. Oracle Database Vault enables you to store sensitive data for your business applications and allow operations to manage the database infrastructure without having to access sensitive customer data.
	See " [Using Database Vault Operations Control to Restrict Multitenant Common User Access to Local PDB Data](using-oracle-database-vault-with-a-cdb.md) ".
- Support for multiple PDB shards in the same CDB
	A CDB can contain multiple PDBs as shard catalog databases. Also, a CDB can contain shard PDBs from different sharded databases (SDBs), each managed by its own separate catalog database.
	See [Using Oracle Sharding](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=GUID-AF8EE357-7CBC-4B42-8027-22084D08029D).
- Automated PDB relocation
	In Oracle Grid Infrastructure, you can use Oracle Fleet Patching and Provisioning to automate relocation of a PDB from one CDB to another. Automated relocation enables you to patch individual PDBs more quickly without exposing other PDBs to the changes in the patch.
	See [Oracle Clusterware Administration and Deployment Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=GUID-CCEC5960-EDA4-4A3F-9643-0CA308EA49AA).
- Cloning a remote PDB using DBCA
	You can clone a remote PDB using DBCA in silent mode.
	See " [About Cloning a Remote PDB](cloning-a-pdb.md) ".
- Remote PDB relocation
	You can use Database Configuration Assistant (DBCA) to relocate a PDB from a remote CDB to a local CDB.
	See " [Relocating a PDB Using DBCA: Example](relocating-a-pdb.md) ".
- Cloud object store support for Data Pump Import
	The `credential` parameter of `impdb` specifies the name of a credential object that contains the user name and password required to access an object store bucket. You can also specify a default credential using the database property `DEFAULT_CREDENTIAL`.
	See " [Setting the Default Credential in a PDB](managing-security-for-a-multitenant-environment.md) " and " [Using Data Pump to Move Data Into a CDB](using-database-utilities-in-a-cdb.md) ".

See Also:

[Oracle Database Licensing Information User Manual](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=DBLIC-GUID-0F9EB85D-4610-4EDF-89C2-4916A0E7AC87) for details on which features are supported for different editions and services

**Parent topic:** Changes in Oracle Database Release 19c, Version 19.1

### Changes in Oracle Database Release 18c, Version 18.1

The following are changes in Oracle Multitenant Administrator's Guide for Oracle Database release 18c, version 18.1.

- New Features

**Parent topic:** Changes in This Release for Oracle Multitenant Administrator’s Guide

#### New Features

The following features are new in this release:

- CDB fleet
	A **CDB fleet** is a collection of different CDBs that can be managed as one logical CDB.
	See " [Administering a CDB Fleet](configuring-cdb-fleet.md) ".
- PDB snapshot carousel
	A **PDB snapshot** is a point-in-time copy of a PDB. The source PDB can be open read-only or read/write while the snapshot is created. You can create snapshots manually using the `SNAPSHOT` clause of `CREATE PLUGGABLE DATABASE` (or `ALTER PLUGGABLE DATABASE`), or automatically using the `EVERY interval` clause. When a PDB is enabled for snapshots, you can create multiple snapshots (point-in-time copies) of the PDB. The library of snapshots is called a PDB snapshot carousel. You can quickly clone a new PDB based on any snapshot in the carousel. In this way, you can perform point-in-time recovery to any snapshot in the carousel, or rapidly create a PDB by cloning any snapshot.
	See " [User Interface for PDB Snapshot Carousel](administering-pdb-snapshots.md) " and " [Administering a PDB Snapshot Carousel](administering-pdb-snapshots.md) ".
- Logical partitioning
	A container map enables a session to issue SQL statements that are routed to the appropriate PDB, depending on the value of a predicate used in the SQL statement. The partitioning column in the map table does not need to match a column in the metadata-linked table. For example, if the table `sales` is enabled for the container map `pdb_map_tbl`, and if `sales` does not have the column used to partition `pdb_map_tbl`, then queries with the predicate `CONTAINERS(sales)` are still routed to the PDBs specified in the map table.
	See " [Container Maps](overview-of-the-multitenant-architecture.md) ".
- Refreshable PDB switchover
	A **refreshable clone PDB** is a read-only clone that can periodically synchronize with its source PDB. You can reverse the roles, transforming the source PDB into the clone and the clone into the source. This technique can be useful for load balancing. Also, if the source PDB fails, then you can resume operations on the clone PDB, rendering a CDB-level Oracle Data Guard failover unnecessary.
	See " [About Refreshable Clone PDBs](cloning-a-pdb.md) " and " [Switching Over a Refreshable Clone PDB](administering-pdbs-with-sql-plus.md) ".
- Lockdown profile enhancements
	You can create, alter, or drop lockdown profiles in application containers. Also, you can create lockdown profiles based on a static or a dynamic base profile.
	See " [Overview of PDB Lockdown Profiles](overview-of-the-multitenant-architecture.md) ", " [About Restricting PDB Users for Enhanced Security](administering-a-cdb-with-sql-plus.md) ", and " [Restricting Operations on PDBs Using PDB Lockdown Profiles](managing-security-for-a-multitenant-environment.md) ".
- DBCA enhancements
	You can use DBCA to clone a local PDB or duplicate a CDB. Duplication is only supported in silent mode.
	See " [About CDB Creation with DBCA](creating-and-configuring-a-cdb.md) " and " [About Cloning a Local PDB](cloning-a-pdb.md) ".
- Usable backups of non-CDBs and relocated PDBs
	When you are cloning a non-CDB as a PDB or relocating a PDB, you can use the `DBMS_PDB.EXPORTRMANBACKUP` procedure to export RMAN backup metadata into the PDB dictionary. This metadata enables backups of the source non-CDB or PDB to be usable for restore and recovery of the target PDB.
	See " [General Prerequisites for PDB Creation](overview-of-pdb-creation.md) ".
- RMAN duplication of a PDB to another CDB
	You can clone a PDB from a source CDB to an existing CDB that is open read/write.
	See " [Techniques for Creating a PDB](overview-of-pdb-creation.md) "
- Relocation of sessions during planned maintenance
	Application Continuity can drain database sessions during planned maintenance when the application submits a connection test, at request boundaries, and at good places to fail over. The relocation is transparent to applications. This feature is on by default for all maintenance operations invoked at the database service and PDB levels: stop service, relocate service, relocate PDB, and stop PDB.
	See " [Managing Services for PDBs](administering-pdbs-with-sql-plus.md) ", " [How PDB Relocation Works](relocating-a-pdb.md) ", and [Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=RACAD-GUID-C1EF6BDA-5F90-448F-A1E2-DC15AD5CFE75).
- Copying a PDB in an Oracle Data Guard environment
	When performing a remote clone in a primary database, or plugging in a PDB in a primary database, you can set initialization parameters in a standby database that automates copying the data files for the newly created PDB.
	See " [Cloning a Remote PDB: Basic Steps](cloning-a-pdb.md) " and " [Plugging In an Unplugged PDB](plugging-in-a-pdb.md) ".
- Parallel statement queuing at the PDB level
	You can configure parallel statement queuing for a PDB just as for a non-PDB using the `PARALLEL_SERVERS_TARGET` initialization parameter. At the PDB level, the default is based on the `CPU_COUNT` setting for the PDB. At the CDB level, the default value is the value of the `PARALLEL_MAX_SERVERS` initialization parameter.
	See " [Utilization Limits for PDBs](using-oracle-resource-manager-for-pdbs-with-sql-plus.md) ".
- Split mirror clone PDBs
	When a PDB resides in Oracle ASM, you can use a split mirroring technique to clone a PDB. The cloned PDB is independent of the original PDB. The principal use case is to rapidly provision test and development PDBs in an Oracle ASM environment.
	See " [Creating a Split Mirror Clone PDB](cloning-a-pdb.md) ".

**Parent topic:** Changes in Oracle Database Release 18c, Version 18.1