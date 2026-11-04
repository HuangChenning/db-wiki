---
title: "Administrator’s Guide"
book: "Multitenant Administrator's Guide"
doc_id: F31734-10
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/multi/dropping-application-container.html
tags:
  - oracle
  - 21c
  - multitenant-administrators-guide
---

You can drop an application container when you want to move the application container from one CDB to another or when you no longer need the application container.

Dropping an application container is very similar to dropping a PDB. When you drop an application container, the control file of the CDB is modified to eliminate all references to the dropped application container. Archived redo log files and backups associated with the application container are not removed, but you can use Oracle Recovery Manager (RMAN) to remove them.

When dropping an application container, you can either keep or delete the application container’s data files by using one of the following clauses in the `DROP PLUGGABLE DATABASE` statement:

- `KEEP DATAFILES`, the default, retains the data files.
	The application container’s temp file is removed even when `KEEP DATAFILES` is specified because the temp file is no longer needed.
- `INCLUDING DATAFILES` removes the data files from disk.
	If an application container was created with the `SNAPSHOT COPY` clause, then you must specify `INCLUDING DATAFILES` when you drop the application container.

The following prerequisites must be met:

- The application container must be in mounted mode, or it must be unplugged.
	See " [Modifying the Open Mode of PDBs](administering-pdbs-with-sql-plus.md) ".
	See " [Unplugging an Application Container](unplugging-application-container-cdb.md) ".
- The current user must have `SYSDBA` or `SYSOPER` administrative privilege, and the privilege must be either commonly granted or locally granted in the application container. The user must exercise the privilege using `AS SYSDBA` or `AS SYSOPER` at connect time.
- The application container must not have any application PDBs plugged into it.
- The application container must not have an application seed plugged into it.

Note:

This operation is destructive.

To drop an application container:

1. In SQL\*Plus, ensure that the current container is the CDB root.
	See " [About the Current Container](administering-a-cdb-with-sql-plus.md) " and " [Accessing a Container in a CDB with SQL\*Plus](administering-a-cdb-with-sql-plus.md) ".
2. Run the `DROP` `PLUGGABLE` `DATABASE` statement and specify the application container to drop.

Example 14-6 Dropping Application Container salesact While Keeping Its Data Files

```
DROP PLUGGABLE DATABASE salesact
  KEEP DATAFILES;
```

Example 14-7 Dropping Application Container salesact and Its Data Files

```
DROP PLUGGABLE DATABASE saleact
  INCLUDING DATAFILES;
```

See Also:

- " [Unplugging an Application Container](unplugging-application-container-cdb.md) "
- " [Dropping a PDB](removing-a-pdb.md) "
- " [Storage Requirements for Snapshot Copy PDBs](cloning-a-pdb.md) "
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=SQLRF55699)
- [Oracle Database Backup and Recovery User’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=BRADV89346) for information about RMAN

**Parent topic:** [Creating and Removing Application Containers and Seeds](creating-removing-application-containers-seeds-with-sql-plus.md)