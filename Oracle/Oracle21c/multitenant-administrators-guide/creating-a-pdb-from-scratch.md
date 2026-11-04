---
title: "Administrator’s Guide"
book: "Multitenant Administrator's Guide"
doc_id: F31734-10
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/multi/creating-a-pdb-from-scratch.html
tags:
  - oracle
  - 21c
  - multitenant-administrators-guide
---

Use the `CREATE PLUGGABLE DATABASE` statement to create a PDB in a CDB using the files of the PDB seed (`PDB$SEED`).

You can also use this statement to create an application PDB in an application container using the files of an application seed or the PDB seed.

- About Creating a PDB from Scratch  
	Use the `CREATE PLUGGABLE DATABASE` statement to create a new PDB by using the files of the PDB seed or an application PDB from the files of an application seed or the PDB seed.
- Creating a PDB  
	Using the `CREATE PLUGGABLE DATABASE` statement, you can create a PDB from the PDB seed, and you can create an application PDB from an application seed or the PDB seed.
- Creating a PDB: Examples  
	These examples create a new PDB named `salespdb` and a `salesadm` local administrator given different factors.

See Also:

[Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=SQLRF55686) for more information about the `CREATE PLUGGABLE DATABASE` statement

**Parent topic:** [Creating PDBs and Application Containers](creating-pdbs.md)

### About Creating a PDB from Scratch

Use the `CREATE PLUGGABLE DATABASE` statement to create a new PDB by using the files of the PDB seed or an application PDB from the files of an application seed or the PDB seed.

The statement copies these files to a new location and associates them with the new PDB. The following figure illustrates how this technique creates a new PDB in a CDB with the CDB root as the current container.

Figure 7-1 Create a PDB in the CDB Root Using the PDB$SEED Files

![Figure 7-1 Create a PDB in the CDB Root Using the PDB$SEED Files](img/admin0891.png)

> This illustration shows a CDB with a `CDB$ROOT` container, a `PDB$SEED` container plugged into the root, and several PDBs plugged into the root. One PDB is a new PDB. The illustration shows the `PDB$SEED` files associated with the `PDB$SEED` container. The illustration shows the seed's files copied to a new location. The copied files are the files of the new PDB. The illustration shows the copied files associated with the new PDB. A `CREATE` `PLUGGABLE` `DATABASE` statement uses these copied files to create the new PDB.


The following figure illustrates how this technique creates a new application PDB in an application container with the application root as the current container.

Figure 7-2 Create a PDB in an Application Root Using the Application Seed Files

![Figure 7-2 Create a PDB in an Application Root Using the Application Seed Files](img/admin114.png)

> This illustration shows a CDB with the following components:
>
> - The CDB has a `CDB$ROOT` container.
> - A `PDB$SEED` container is plugged into the root container.
> - Several PDBs are plugged into the root container.
> - An application container is plugged into the root container.
> - The application container has an application root container.
> - The application container has an application seed plugged into it.
> - The application container has two application PDBs plugged into its application root container.
>
> The illustration shows the application seed files associated with the application seed container. The illustration shows the application seed's files copied to a new location. The copied files are the files of the new application PDB. The illustration shows the copied files associated with the new application PDB. A `CREATE` `PLUGGABLE` `DATABASE` statement uses these copied files to create the new application PDB.


See Also:

When an application container includes an application seed, and a `CREATE PLUGGABLE DATABASE` statement is run in the application root to create an application PDB from the seed, the application PDB is created using the application seed. However, when an application container does not include an application seed, and a `CREATE PLUGGABLE DATABASE` statement is run in the application root to create an application PDB from the seed, the application PDB is created using the PDB seed (`PDB$SEED` ).

When you create a new PDB or application PDB from the seed, you must specify an administrator for the PDB or application PDB in the `CREATE PLUGGABLE DATABASE` statement. The statement creates the administrator as a local user in the PDB and grants the `PDB_DBA` role locally to the administrator.

Before creating a PDB using the PDB seed or an application seed, address the questions that apply to creating a PDB from the seed in [Table 6-3](overview-of-pdb-creation.md). The table describes which `CREATE PLUGGABLE DATABASE` clauses you must specify based on different factors.

See Also:

- " [PDB Storage](overview-of-pdb-creation.md) "
- " [Creating an Application PDB](creating-application-pdb.md) "

**Parent topic:** Creating a PDB from Scratch

### Creating a PDB

Using the `CREATE PLUGGABLE DATABASE` statement, you can create a PDB from the PDB seed, and you can create an application PDB from an application seed or the PDB seed.

Prerequisites

Before creating a PDB from the PDB seed (`PDB$SEED`) or an application PDB from an application seed or the PDB seed, complete the prerequisites described in " [General Prerequisites for PDB Creation](overview-of-pdb-creation.md) ".

To create a PDB:

1. In SQL\*Plus, ensure that the current container is the CDB root or an application root.
	When the current container is the CDB root, the PDB is created in the CDB using the files of the PDB seed.
	When the current container is an application root, the application PDB is created in the application container using the files of the application seed. If there is no application seed in the application container, then the application PDB is created in the application container using the files of the PDB seed.
2. Run the `CREATE PLUGGABLE DATABASE` statement, and specify a local administrator for the PDB. Specify other clauses when they are required.
	After you create the PDB, it is in mounted mode, and its status is `NEW`. You can view the open mode of a PDB by querying the `OPEN_MODE` column in the `V$PDBS` view. You can view the status of a PDB by querying the `STATUS` column of the `CDB_PDBS` or `DBA_PDBS` view.
	A new default service is created for the PDB. The service has the same name as the PDB and can be used to access the PDB. Oracle Net Services must be configured properly for clients to access this service.
3. Open the new PDB in read/write mode.
	You must open the new PDB in read/write mode for Oracle Database to complete the integration of the new PDB into the CDB. An error is returned if you attempt to open the PDB in read-only mode. After the PDB is opened in read/write mode, its status is `NORMAL`.
4. Back up the PDB.
	A PDB cannot be recovered unless it is backed up.

A local user with the name of the specified local administrator is created and granted the `PDB_DBA` common role locally in the PDB. If this user was not granted administrator privileges during PDB creation, then use the `SYS` and `SYSTEM` common users to administer to the PDB.

Note:

If an error is returned during PDB creation, then the PDB being created might be in an `UNUSABLE` state. You can check a PDB's state by querying the `CDB_PDBS` or `DBA_PDBS` view, and you can learn more about PDB creation errors by checking the alert log. An unusable PDB can only be dropped, and it must be dropped before a PDB with the same name as the unusable PDB can be created.

See Also:

- " [About Container Access in a CDB](administering-a-cdb-with-sql-plus.md) "
- " [Modifying the Open Mode of PDBs](administering-pdbs-with-sql-plus.md) " for more information
- [Oracle Database Backup and Recovery User’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=BRADV-GUID-655DC5F5-FF8D-4A73-B67D-F5AAE20CA382) for information about backing up a PDB

**Parent topic:** Creating a PDB from Scratch

### Creating a PDB: Examples

These examples create a new PDB named `salespdb` and a `salesadm` local administrator given different factors.

In addition to creating the `salespdb` PDB, this statement grants the `PDB_DBA` role to the PDB administrator `salesadm` and grants the specified predefined Oracle roles to the `PDB_DBA` role locally in the PDB.

In each example, the root to which the new PDB belongs depends on the current container when the `CREATE PLUGGABLE DATABASE` statement is run:

- When the current container is the CDB root, the new PDB is created in the CDB root.
- When the current container is an application root in an application container, the new PDB is created as an application PDB in the application root.

- Creating a PDB Using No Clauses: Example  
	This example shows the simplest way to create a PDB.
- Creating a PDB and Granting Predefined Oracle Roles to the PDB Administrator: Example  
	This example uses the `ROLES` parameter to grant a predefined role.
- Creating a PDB Using Multiple Clauses: Example  
	This example creating a PDB using the `STORAGE`, `DEFAULT TABLESPACE`, `PATH_PREFIX`, and `FILE_NAME_CONVERT` clauses.

**Parent topic:** Creating a PDB from Scratch

#### Creating a PDB Using No Clauses: Example

This example shows the simplest way to create a PDB.

This example assumes the following factors:

- Storage limits are not required for the PDB. Therefore, the `STORAGE` clause is not required.
- The PDB does not require a default tablespace.
- The `PATH_PREFIX` clause is not required.
- The `FILE_NAME_CONVERT` clause and the `CREATE_FILE_DEST` clause are not required.
	Either Oracle Managed Files is enabled for the CDB, or the `PDB_FILE_NAME_CONVERT` initialization parameter is set. The files associated with the PDB seed or application seed will be copied to a new location based on the Oracle Managed Files configuration or the initialization parameter setting.
- There is no file with the same name as the new temp file that will be created in the target location. Therefore, the `TEMPFILE REUSE` clause is not required.
- No predefined Oracle roles need to be granted to the `PDB_DBA` role.

The following statement creates the PDB:

```
CREATE PLUGGABLE DATABASE salespdb ADMIN USER salesadm IDENTIFIED BY pwd;
```

See Also:

- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=ADMIN-GUID-4A3C4616-0D81-4BBA-8EAD-FCAA8AD5C15A) for information about using Oracle Managed Files
- [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=REFRN10322) for information about the `PDB_FILE_NAME_CONVERT` initialization parameter
- [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=DBSEG33223) for guidelines about choosing passwords

**Parent topic:** Creating a PDB: Examples

#### Creating a PDB and Granting Predefined Oracle Roles to the PDB Administrator: Example

This example uses the `ROLES` parameter to grant a predefined role.

This example assumes the following factors:

- Storage limits are not required for the PDB. Therefore, the `STORAGE` clause is not required.
- The PDB does not require a default tablespace.
- The `PATH_PREFIX` clause is not required.
- The `FILE_NAME_CONVERT` clause and the `CREATE_FILE_DEST` clause are not required.
	Either Oracle Managed Files is enabled, or the `PDB_FILE_NAME_CONVERT` initialization parameter is set. The files associated with the PDB seed or application seed will be copied to a new location based on the Oracle Managed Files configuration or the initialization parameter setting.
- There is no file with the same name as the new temp file that will be created in the target location. Therefore, the `TEMPFILE REUSE` clause is not required.
- The `PDB_DBA` role should be granted the following predefined Oracle role locally: `DBA`.

The following statement creates the PDB:

```
CREATE PLUGGABLE DATABASE salespdb 
  ADMIN USER salesadm IDENTIFIED BY password
    ROLES=(DBA);
```

See Also:

- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=ADMIN-GUID-4A3C4616-0D81-4BBA-8EAD-FCAA8AD5C15A) for information about using Oracle Managed Files
- [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=REFRN10322) for information about the `PDB_FILE_NAME_CONVERT` initialization parameter
- [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=DBSEG33223) for guidelines about choosing passwords

**Parent topic:** Creating a PDB: Examples

#### Creating a PDB Using Multiple Clauses: Example

This example creating a PDB using the `STORAGE`, `DEFAULT TABLESPACE`, `PATH_PREFIX`, and `FILE_NAME_CONVERT` clauses.

This example assumes the following factors:

- Storage limits must be enforced for the PDB. Therefore, the `STORAGE` clause is required. Specifically, all tablespaces that belong to the PDB must not exceed 2 gigabytes.
- A default permanent tablespace is required for any non-administrative users for which you do not specify a different permanent tablespace. Specifically, this example creates a default permanent tablespace named `sales` with the following characteristics:
	- The single data file for the tablespace is `sales01.dbf`, and the statement creates it in the `/disk1/oracle/dbs/salespdb` directory.
		- The `SIZE` clause specifies that the initial size of the tablespace is 250 megabytes.
		- The `AUTOEXTEND` clause enables automatic extension for the file.
- The path prefix must be added to the PDB directory object paths. Therefore, the `PATH_PREFIX` clause is required. In this example, the path prefix `/disk1/oracle/dbs/salespdb/` is added to the PDB’s directory object paths.
- The `CREATE_FILE_DEST` clause will not be used, Oracle Managed Files is not enabled, and the `PDB_FILE_NAME_CONVERT` initialization parameter is not set. Therefore, the `FILE_NAME_CONVERT` clause is required. Specify the location of the data files for the PDB seed or application seed on your system. In this example, Oracle Database copies the files from `/disk1/oracle/dbs/pdbseed` to `/disk1/oracle/dbs/salespdb`.
- There is no file with the same name as the new temp file that will be created in the target location. Therefore, the `TEMPFILE REUSE` clause is not required.
- No predefined Oracle roles need to be granted to the `PDB_DBA` role.

The following statement creates the PDB:

```
CREATE PLUGGABLE DATABASE salespdb 
  ADMIN USER salesadm IDENTIFIED BY password
  STORAGE (MAXSIZE 2G)
  DEFAULT TABLESPACE sales 
    DATAFILE '/disk1/oracle/dbs/salespdb/sales01.dbf' SIZE 250M 
    AUTOEXTEND ON
    PATH_PREFIX = '/disk1/oracle/dbs/salespdb/'
    FILE_NAME_CONVERT = ('/disk1/oracle/dbs/pdbseed/', 
                         '/disk1/oracle/dbs/salespdb/');
```

See Also:

- " [Example 15-34](administering-a-cdb-with-sql-plus.md) " to learn how to view the location of the data files for the PDB seed or application seed
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=SQLRF53869) for more information about the `DEFAULT TABLESPACE` clause
- [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=DBSEG33223) for guidelines about choosing passwords

**Parent topic:** Creating a PDB: Examples