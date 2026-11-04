---
title: "Administrator’s Guide"
book: "Multitenant Administrator's Guide"
doc_id: E96136-19
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/multi/backing-up-and-recovering-cdbs-and-pdbs.html
tags:
  - oracle
  - 19c
  - multitenant-administrators-guide
---

## 20 Backing Up and Recovering CDBs and PDBs

- Overview of Backing Up and Recovering CDBs and PDBs  
	When using the multitenant architecture, you can perform backup and recovery operations on a whole multitenant container database (CDB), the root, or one or more pluggable databases (PDBs).
- Backup and Complete Recovery of CDBs  
	To perform backup and complete recovery operations on a whole multitenant container database (CDB), you connect as `TARGET` to the root.
- Backup and Complete Recovery of PDBs  
	You can perform backup and complete recovery operations on a single pluggable database (PDB) or on multiple PDBs.
- Point-in-Time Recovery in a Multitenant Environment  
	You can perform point-in-time recovery of the whole multitenant container database (CDB) or a particular pluggable database (PDB).
- Flashback Database in a Multitenant Environment  
	You can perform a Flashback Database operation for a whole multitenant container database (CDB) or for a particular pluggable (PDB).

**Parent topic:** [Using Oracle Features in a Multitenant Environment](using-oracle-features-in-a-multitenant-environment.md)

### Overview of Backing Up and Recovering CDBs and PDBs

When using the multitenant architecture, you can perform backup and recovery operations on a whole multitenant container database (CDB), the root, or one or more pluggable databases (PDBs).

The Oracle Recovery Manager (RMAN) commands used to backup and recover CDBs and PDBs are the same as those used for non-CDBs, with minor variations in the syntax. The backup and recovery operations performed on non-CDBs can also be performed on CDBs and PDBs. This includes the following:

- Full and incremental backups
- Complete and point-in-time recovery (PITR)
- Flashback Database
- Reporting operations (such as listing backups and cross-checking backups)

About Connecting to CDBs and PDBs

You can connect to the root in one of the following ways:

- Connect using operating system authentication
	You are connected to the root as the `SYS` user with the `SYSDBA` privilege.
- Connect locally as a common user
- Connect as a common user through Oracle Net Services

To connect as `TARGET` to a PDB, use one of the following techniques:

- Connect with a net service name that resolves to a database service for that PDB
- Connect locally as a common user or local user with the `SYSDBA` or `SYSBACKUP` privilege

Note:

Certain operations are not available when you connect directly to a PDB. See [Oracle Database Backup and Recovery User’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=BRADV673) for a list of these operations.

See Also:

The following sections in the Oracle Database Backup and Recovery User’s Guide provide detailed information about backing up and recovering PDBs:

- [Connecting as Target to the Root](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=BRADV674)
- [Connecting as Target to a PDB](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=BRADV678)

**Parent topic:** Backing Up and Recovering CDBs and PDBs

### Backup and Complete Recovery of CDBs

To perform backup and complete recovery operations on a whole multitenant container database (CDB), you connect as `TARGET` to the root.

The connection must be established as a common user with the `SYSDBA` or `SYSBACKUP` privilege.

After you connect to the root, the same commands that are used to perform operations on non-CDBs are used to perform backup and complete recovery on the entire CDB.

See Also:

The following sections in the Oracle Database Backup and Recovery User’s Guide provide detailed information about performing backup and complete recovery of CDBs:

- " [Backing Up a Whole CDB](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=BRADV731) "
- " [Performing Complete Recovery of a Whole CDB](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=BRADV746) "
- " [Validating a Whole CDB](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=BRADV744) "
- " [Reporting in CDBs](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=BRADV740) "

**Parent topic:** Backing Up and Recovering CDBs and PDBs

### Backup and Complete Recovery of PDBs

You can perform backup and complete recovery operations on a single pluggable database (PDB) or on multiple PDBs.

Backups of PDBs

When relocating a PDB or cloning a non-CDB as a PDB, you may want to retain the use of preplugin backups. For preplugin backups to be usable in the destination CDB, metadata about the preplugin backups must be exported to the RMAN repository of the destination CDB.

The technique for making the backups usable depends on the type of operation:

- Creating a PDB by cloning a non-CDB
	When the non-CDB is opened in read/write mode, you must execute the `DBMS_PDB.EXPORTRMANBACKUP` procedure as the last step before cloning. When plugging in the non-CDB as a PDB to a destination CDB, the operation copies the backup metadata of the source non-CDB into the data dictionary of the destination CDB.
- Relocating a PDB to another CDB
	When you unplug the source PDB, the backup metadata is automatically exported. Therefore, you do not need to execute `DBMS_PDB.EXPORTRMANBACKUP`.

Preplugin backups are usable only on the destination CDB into which you plug in the source non-CDB or PDB.

Note:

- [Oracle Database Backup and Recovery User’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=GUID-7D69CBCA-123F-49FF-85E9-F5C70E47202D) to learn about preplugin backups
- [Oracle Database Backup and Recovery User’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=GUID-7F9F8913-2838-4066-A000-048B35A70EA4) to learn how to create a preplugin backup of the whole database
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=ARPLS-GUID-69EE6FF6-225F-4CC5-BBA5-3AFD01E4131F) to learn more about the `DBMS_PDB.EXPORTRMANBACKUP` procedure

Syntax for Backup Commands

Although the Oracle Recovery Manager (RMAN) commands are the same, the syntax used to perform operations on multiple PDBs contains some modifications.

To perform backup and complete recovery operations on a single PDB, you can connect as `TARGET` to either of the following containers:

- PDB
	In this case, use the same commands that you would use to backup or recover non-CDBs. For example, to back up a PDB, use the `BACKUP DATABASE` command.
- `CDB$ROOT`
	In this case, use the `PLUGGABLE DATABASE` clause in your RMAN commands. The following command backs up the PDB `hrpdb` when connected to the root:
	```
	BACKUP PLUGGABLE DATABASE hrpdb;
	```
	To perform backup and complete recovery operations on multiple PDBs using a single command, you must connect to the root. Use the `PLUGGABLE DATABASE` clause followed by the list of PDBs on which you want to perform the operation. The following example backs up the PDBs `hrpdb`, `salespdb`, and `invpdb` when connected to the root:
	```
	BACKUP PLUGGABLE DATABASE hrpdb, salespdb, invpdb;
	```

See Also:

The following sections in the Oracle Database Backup and Recovery User’s Guide provide detailed information about backing up and recovering PDBs:

- " [Connecting as Target to a PDB](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=BRADV678) "
- " [Connecting as Target to the Root](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=BRADV674) "
- " [Backing Up PDBs with RMAN](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=BRADV735) "
- " [Performing Complete Recovery of PDBs with RMAN](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=BRADV749) "
- " [Validating PDBs](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=BRADV745) "
- " [Reporting in PDBs](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=BRADV741) "

**Parent topic:** Backing Up and Recovering CDBs and PDBs

### Point-in-Time Recovery in a Multitenant Environment

You can perform point-in-time recovery of the whole multitenant container database (CDB) or a particular pluggable database (PDB).

Point-in-Time Recovery of a CDB

To perform point-in-time recovery of a CDB, you must meet the following prerequisites:

- You must be logged in to the root container as a common user with the `SYSDBA` or `SYSBACKUP` privilege.
- The CDB must be mounted.

When performing the recovery operation, use the same commands that you use for non-CDBs.

Point-in-Time Recovery of a PDB

When a PDB is closed in an open or closed CDB, you can recover the PDB to a past point in time. The technique depends on the undo mode of the CDB. The following table describes the differences.

Table 20-1 Differences in Point-in-Time Recovery Techniques

| Undo Mode | Auxiliary Instance Used? | Connect as TARGET to... | RMAN Commands to Use for Recovery |
| --- | --- | --- | --- |
| Shared | Yes | CDB root | Include the `PLUGGABLE DATABASE` clause to specify the PDB that must be recovered.  RMAN uses an auxiliary destination to store temporary files created during recovery. If a fast recovery area has been configured, then it is used as the auxiliary destination. You can explicitly specify an auxiliary destination using the `AUXILIARY DESTINATION` clause in the `RECOVER` command. |
| Local | No | CDB root or PDB | When connected to the PDB, use the same commands that you use for non-CDBs. When connected to the root, include the `PLUGGABLE DATABASE` clause to specify the PDB that must be recovered. |

See Also:

The following sections in the Oracle Database Backup and Recovery User’s Guide for more information about point-in-time recovery.

- " [Overview of Restore Points in a Multitenant Environment](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=BRADV-GUID-1150031F-3C15-40C8-BA91-A387F75DC49A) "
- " [Creating CDB Restore Points](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=BRADV-GUID-952278F2-DBBA-4CB9-AAC4-616B56837AAB) "
- " [Creating PDB Restore Points](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=BRADV-GUID-9363C4B9-48E5-470F-B13B-43FA56667978) "
- " [Performing Point-in-Time Recovery of CDBs and PDBs](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=BRADV-GUID-031D9695-A9D2-4381-A840-39BD3CC19946) "

**Parent topic:** Backing Up and Recovering CDBs and PDBs

### Flashback Database in a Multitenant Environment

You can perform a Flashback Database operation for a whole multitenant container database (CDB) or for a particular pluggable (PDB).

RMAN uses an auxiliary destination to store temporary files created during point-in-time recovery. By default, the fast recovery area is used as the auxiliary destination. You can explicitly specify an auxiliary destination using the `AUXILIARY DESTINATION` clause in the `RECOVER` command.

Flashback of CDBs

To perform Flashback Database for a CDB, you must meet the following prerequisites:

- You must be connected to the root as a common user with the `SYSDBA` or `SYSBACKUP` privilege.
- The CDB must be mounted.

Specify the target point in time for the flashback operation using a CDB restore point, time expression, or SCN. A CDB restore point is accessible to every PDB within the CDB. However, the restore point does not reflect the PDB sub-incarnation of any of its PDBs.

Flashback of PDBs

When a PDB is closed and the CDB is open, you can perform a flashback database operation for this PDB using the `FLASHBACK DATABASE` command. Performing a Flashback Database operation on a particular PDB modifies only data files related to that PDB. The other PDBs in the CDB are not impacted and are available for use. Note that a PDB restore point is accessible only to the PDB in which it is defined and can be used for operations only on this PDB.

Table 20-2 Differences in Flashback Techniques

| CDB Undo Mode | Auxiliary Instance Used? | Connect as TARGET to... | Commands |
| --- | --- | --- | --- |
| Shared | Yes | CDB root | Use the `FLASHBACK PLUGGABLE DATABASE` command. You can only flash back to a clean PDB restore point.  RMAN uses an auxiliary destination to store temporary files created during flashback. If a fast recovery area has been configured, then it is used as the auxiliary destination. You can explicitly specify an auxiliary destination using the `AUXILIARY DESTINATION` clause in the `FLASHBACK PLUGGABLE DATABASE` command. |
| Local | No | CDB root or PDB | Use the `FLASHBACK PLUGGABLE DATABASE` command. You can specify the target point in time for the flashback operation using a CDB restore point, PDB restore point, time expression, or target SCN. |

See Also:

The following sections in the Oracle Database Backup and Recovery User’s Guide for more information about flashback of CDBs and PDBs:

- " [Overview of Restore Points in a Multitenant Environment](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=BRADV-GUID-1150031F-3C15-40C8-BA91-A387F75DC49A) "
- " [Creating CDB Restore Points](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=BRADV-GUID-952278F2-DBBA-4CB9-AAC4-616B56837AAB) "
- " [Creating PDB Restore Points](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=BRADV-GUID-9363C4B9-48E5-470F-B13B-43FA56667978) "
- " [Performing a Flashback Database Operation for a Whole CDB](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=BRADV-GUID-8466CA3C-652A-4AAB-88EB-8815575D6266) "
- " [Performing a Flashback Database Operation for PDBs](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=BRADV-GUID-C1215E86-9A7B-4EC9-9777-2A18BD627394) "

**Parent topic:** Backing Up and Recovering CDBs and PDBs