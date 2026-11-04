---
title: "Administrator’s Guide"
book: "Multitenant Administrator's Guide"
doc_id: F31734-10
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/multi/dropping-application-seed.html
tags:
  - oracle
  - 21c
  - multitenant-administrators-guide
---

You can use the `DROP` `PLUGGABLE` `DATABASE` statement to drop an application seed. You can drop an application seed when you no longer need it.

When you drop an application seed, the control file of the CDB is modified to eliminate all references to the dropped application seed. Archived redo log files and backups associated with the application seed are not removed, but you can use Oracle Recovery Manager (RMAN) to remove them.

When dropping an application seed, you can either keep or delete the application seed’s data files by using one of the following clauses:

- `KEEP DATAFILES`, the default, retains the data files.
	The application seed’s temp file is removed even when `KEEP DATAFILES` is specified because the temp file is no longer needed.
- `INCLUDING DATAFILES` removes the data files from disk.
	If an application seed was created with the `SNAPSHOT COPY` clause, then you must specify `INCLUDING DATAFILES` when you drop the application seed.

The following prerequisites must be met:

- The application seed must be in mounted mode, or it must be unplugged.
- The current user must have `SYSDBA` or `SYSOPER` administrative privilege, and the privilege must be either commonly granted or locally granted in the application container. The user must exercise the privilege using `AS SYSDBA` or `AS SYSOPER` at connect time.

To drop an application seed:

1. In SQL\*Plus, ensure that the current container is the application root of the application container to which the application seed belongs.
2. Run the `DROP PLUGGABLE DATABASE` statement and specify the application seed.

Example 14-12 Dropping Application Seed salesact$SEED While Keeping Its Data Files

```
DROP PLUGGABLE DATABASE salesact$SEED
  KEEP DATAFILES;
```

Example 14-13 Dropping Application Seed salesact$SEED and Its Data Files

```
DROP PLUGGABLE DATABASE saleact$SEED
  INCLUDING DATAFILES;
```

See Also:

- " [About Container Access in a CDB](administering-a-cdb-with-sql-plus.md) "
- " [Modifying the Open Mode of PDBs](administering-pdbs-with-sql-plus.md) "
- " [Unplugging an Application Seed](unplugging-application-seed-application-container.md) "
- " [Storage Requirements for Snapshot Copy PDBs](cloning-a-pdb.md) "
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=SQLRF55699)
- [Oracle Database Backup and Recovery User’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=BRADV89346) for information about RMAN

**Parent topic:** [Creating and Removing Application Containers and Seeds](creating-removing-application-containers-seeds-with-sql-plus.md)