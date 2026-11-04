---
title: "Database Administrator’s Guide"
book: "Database Administrator's Guide"
doc_id: E85760-09
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/admin/creating-removing-application-containers-seeds-with-sql-plus.html
tags:
  - oracle
  - 12c
  - administrators-guide
---

You can create application containers and application seeds in several different ways, including using the CDB seed, cloning an existing PDB or non-CDB, and plugging in an unplugged PDB. You can also remove application containers from a CDB, and you can remove application seeds from application containers.

- Creating and Removing Application Containers with SQL\*Plus  
	You can create application containers in several different ways, including using the CDB seed, cloning an existing PDB or non-CDB, and plugging in an unplugged PDB. You can also remove application containers from a CDB.
- Creating and Removing Application Seeds with SQL\*Plus  
	You can create application seeds in several different ways, including using the CDB seed, cloning an existing PDB or non-CDB, and plugging in an unplugged PDB. You can also remove application seeds from application containers.
- Creating an Application PDB  
	You create an application PDB by running the `CREATE PLUGGABLE DATABASE` statement with an application root as the current container.

**Parent topic:** [Managing a Multitenant Environment](managing-a-multitenant-environment.md)

### 40.1 Creating and Removing Application Containers with SQL\*Plus

You can create application containers in several different ways, including using the CDB seed, cloning an existing PDB or non-CDB, and plugging in an unplugged PDB. You can also remove application containers from a CDB.

- Creating Application Containers  
	You can use the `CREATE PLUGGABLE DATABASE` statement to create an application container in a CDB.
- Unplugging an Application Container from a CDB  
	You can unplug an application container from a CDB.
- Dropping an Application Container  
	You can use the `DROP` `PLUGGABLE` `DATABASE` statement to drop an application container. You can drop an application container when you want to move the application container from one CDB to another or when you no longer need the application container.

**Parent topic:** Creating and Removing Application Containers and Seeds with SQL\*Plus

#### 40.1.1 Creating Application Containers

You can use the `CREATE PLUGGABLE DATABASE` statement to create an application container in a CDB.

- About Creating an Application Container  
	When you include the `AS APPLICATION CONTAINER` clause in the `CREATE PLUGGABLE DATABASE` statement, the statement creates a new application container.
- Preparing for Application Containers  
	Prerequisites must be met before creating an application container.
- Creating an Application Container  
	You can create an application container using the `CREATE` `PLUGGABLE` `DATABASE` statement with the `AS APPLICATION CONTAINER` clause.

**Parent topic:** Creating and Removing Application Containers with SQL\*Plus

##### 40.1.1.1 About Creating an Application Container

When you include the `AS APPLICATION CONTAINER` clause in the `CREATE PLUGGABLE DATABASE` statement, the statement creates a new application container.

An application container consists of an application root and a collection of application PDBs that store data for one or more applications. The application PDBs are plugged into the application root, and you can optionally create an application seed for quick and easy creation of new application PDBs. The application PDBs and application root can share application common objects.

There are three types of application common objects:

- Metadata-linked application common objects store the metadata for specific objects, such as tables, so that the containers that share the application common object have the same structure but different data.
- Data-linked application common objects are defined once in the application root and shared as read-only objects in the context of hosted application PDBs.
- Extended data-linked application common objects store shared data in the application root but also allow application PDBs to store data appended to that object. The appended data is local data that is unique to each application PDB.

You create an application container by including the `AS APPLICATION CONTAINER` clause in the `CREATE PLUGGABLE DATABASE` statement. You can use the following techniques to create an application container:

- Using the CDB seed
- Cloning an existing PDB or non-CDB
- Relocating a PDB
- Plugging in an unplugged PDB

When the current container is the CDB root and the `AS APPLICATION CONTAINER` clause is included in the `CREATE PLUGGABLE DATABASE` statement, an application container is created.

Note:

An application container cannot be unplugged or dropped if any application PDBs belong to it.

Migrating Existing Applications to an Application Container

You can migrate an application to an application container by creating an application container using an existing PDB. You must complete additional tasks when you are migrating an existing application to an application container. The PDBs that you plug in must contain the application’s database objects, including their data, and you must run procedures in the `DBMS_PDB` package to associate database objects with the application. Also, when application common users, roles, or profiles exist in the application root, you must run procedures in the `DBMS_PDB` package to associate them with the application.

After the application is migrated to the application container, you can create application PDBs in the application container, and you can create an application PDB using an existing PDB.

See Also:

" [Migrating an Existing Application to an Application Container](administering-application-containers-with-sql-plus.md) "

**Parent topic:** Creating Application Containers

##### 40.1.1.2 Preparing for Application Containers

Prerequisites must be met before creating an application container.

- The CDB must exist.
	See [Creating and Configuring a CDB](creating-and-configuring-a-cdb.md).
- The CDB must be in read/write mode.
- The current user must be a common user whose current container is the CDB root.
- The current user must have the `CREATE` `PLUGGABLE` `DATABASE` system privilege.
- You must decide on a unique application container name for each application container. Each application container name must be unique with regards to all of the containers in a single CDB, and each application container name must be unique within the scope of all the CDBs whose instances are reached through a specific listener.
	The application container name is used to distinguish an application container from other containers in the CDB. Application container names follow the same rules as service names, which includes being case-insensitive. See [Oracle Database Net Services Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=NETRF175) for information about the rules for service names.
- If you are creating an application container in an Oracle Data Guard configuration with a physical standby database, then additional tasks must be completed before creating an application container. See [Oracle Data Guard Concepts and Administration](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=SBYDB5260) for more information.
- If you are migrating an existing application to an application container using a PDB, then it must be possible to clone the PDB to the application root, relocate the PDB to the application root, or plug the PDB into the application root.

See Also:

- " [About the Current Container](administering-a-cdb-with-sql-plus.md) "
- " [Migrating an Existing Application to an Application Container](administering-application-containers-with-sql-plus.md) "

**Parent topic:** Creating Application Containers

##### 40.1.1.3 Creating an Application Container

You can create an application container using the `CREATE` `PLUGGABLE` `DATABASE` statement with the `AS APPLICATION CONTAINER` clause.

Before creating an application container, complete the prerequisites described in " Preparing for Application Containers ".

1. In SQL\*Plus, ensure that the current container is the CDB root.
2. Run the `CREATE` `PLUGGABLE` `DATABASE` statement, and include the `AS APPLICATION CONTAINER` clause. Specify other clauses when they are required.
	After you create the application container, it is in mounted mode, and its status is `NEW`. You can view the open mode of an application container by querying the `OPEN_MODE` column in the `V$PDBS` view. You can view the status of an application container by querying the `STATUS` column of the `CDB_PDBS` or `DBA_PDBS` view.
	A new default service is created for the application container. The service has the same name as the application container and can be used to access the application container. Oracle Net Services must be configured properly for clients to access this service.
3. Open the new application container in read/write mode.
	You must open the new application container in read/write mode for Oracle Database to complete the integration of the new application container into the CDB. An error is returned if you attempt to open the application container in read-only mode. After the application container is opened in read/write mode, its status is `NORMAL`.
4. Back up the application container.A application container cannot be recovered unless it is backed up.
	Note:
	If an error is returned during application container creation, then the application container being created might be in an `UNUSABLE` state. You can check a application container's state by querying the `CDB_PDBS` or `DBA_PDBS` view, and you can learn more about application container creation errors by checking the alert log. An unusable application container can only be dropped, and it must be dropped before an application container or PDB with the same name as the unusable application container can be created.
5. If you are migrating an existing application to the application container, then follow the instructions in " [Migrating an Existing Application to an Application Container](administering-application-containers-with-sql-plus.md) ".

The application container is created with an application root. You can create application PDBs in the application container.

Example 40-1 Creating an Application Container Using the CDB Seed

This example assumes the following factors:

- Storage limits are not required for the application container. Therefore, the `STORAGE` clause is not required.
- The application container does not require a default tablespace.
- The `PATH_PREFIX` clause is not required.
- The `FILE_NAME_CONVERT` clause and the `CREATE_FILE_DEST` clause are not required.
	Either Oracle Managed Files is enabled for the CDB, or the `PDB_FILE_NAME_CONVERT` initialization parameter is set. The files associated with the CDB seed will be copied to a new location based on the Oracle Managed Files configuration or the initialization parameter setting.
- There is no file with the same name as the new temp file that will be created in the target location. Therefore, the `TEMPFILE REUSE` clause is not required.
- No predefined Oracle roles need to be granted to the `PDB_DBA` role.

Given the preceding factors, the following statement creates the application container from the CDB seed:

```
CREATE PLUGGABLE DATABASE salesact AS APPLICATION CONTAINER ADMIN USER salesadm IDENTIFIED BY password;
```

Example 40-2 Creating an Application Container by Cloning a Local PDB

This example assumes the following factors:

- The `PATH_PREFIX` clause is not required.
- The `FILE_NAME_CONVERT` clause is required to specify the target locations of the copied files. In this example, the files are copied from /disk1/oracle/pdb1/ to /disk2/oracle/hract/.
	The `CREATE_FILE_DEST` clause is not used, and neither Oracle Managed Files nor the `PDB_FILE_NAME_CONVERT` initialization parameter is used to specify the target locations of the copied files.
	To view the location of the data files for a PDB, run the query in [Example 45-7](viewing-information-about-cdbs-and-pdbs-with-sql-plus.md).
- Storage limits must be enforced for the application root. Therefore, the `STORAGE` clause is required. Specifically, all tablespaces that belong to the application root must not exceed 2 gigabytes. This storage limit does not apply to the application PDBs that are plugged into the application root.
- There is no file with the same name as the new temp file that will be created in the target location. Therefore, the `TEMPFILE REUSE` clause is not required.

Given the preceding factors, the following statement clones `hract` as an application container from the `pdb1` PDB:

```
CREATE PLUGGABLE DATABASE hract AS APPLICATION CONTAINER FROM pdb1 
  FILE_NAME_CONVERT = ('/disk1/oracle/pdb1/', '/disk2/oracle/hract/')
  STORAGE (MAXSIZE 2G);
```

Note:

If you are migrating an existing application to the new application container, then follow the instructions in " [Migrating an Existing Application to an Application Container](administering-application-containers-with-sql-plus.md) ".

Example 40-3 Creating an Application Container by Plugging In an Unplugged PDB

This example assumes the following factors:

- The new application container is not based on the same unplugged PDB that was used to create an existing PDB or application container in the CDB. Therefore, the `AS` `CLONE` clause is not required.
- The `PATH_PREFIX` clause is not required.
- The XML file does not accurately describe the current locations of the files. Therefore, the `SOURCE_FILE_NAME_CONVERT` clause or `SOURCE_FILE_DIRECTORY` clause is required. In this example, the XML file indicates that the files are in /disk1/oracle/payroll/, but the files are in /disk2/oracle/payroll/, and the `SOURCE_FILE_NAME_CONVERT` clause is used.
- The files are in the correct location. Therefore, `NOCOPY` is included.
- Storage limits must be enforced for the application container. Therefore, the `STORAGE` clause is required. Specifically, all tablespaces that belong to the application container must not exceed 2 gigabytes.
- A file with the same name as the temp file specified in the XML file exists in the target location. Therefore, the `TEMPFILE REUSE` clause is required.

Given the preceding factors, the following statement plugs in the PDB:

```
CREATE PLUGGABLE DATABASE payrollact AS APPLICATION CONTAINER USING '/disk1/usr/payrollpdb.xml' 
  SOURCE_FILE_NAME_CONVERT = ('/disk1/oracle/payroll/', '/disk2/oracle/payroll/')
  NOCOPY
  STORAGE (MAXSIZE 2G)
  TEMPFILE REUSE;
```

Note:

If you are migrating an existing application to the new application container, then follow the instructions in " [Migrating an Existing Application to an Application Container](administering-application-containers-with-sql-plus.md) ".

#### 40.1.2 Unplugging an Application Container from a CDB

You can unplug an application container from a CDB.

- About Unplugging an Application Container  
	Unplugging an application container disassociates the application container from a CDB. You unplug an application container when you want to move the application container to a different CDB or when you no longer want the application container to be available.
- Unplugging an Application Container  
	You must meet prerequisites when unplugging an application container.

**Parent topic:** Creating and Removing Application Containers with SQL\*Plus

##### 40.1.2.1 About Unplugging an Application Container

Unplugging an application container disassociates the application container from a CDB. You unplug an application container when you want to move the application container to a different CDB or when you no longer want the application container to be available.

Unplugging an application container is similar to unplugging a PDB. To unplug a application container, connect to its CDB root and use the `ALTER` `PLUGGABLE` `DATABASE` statement to specify an XML file or a.pdb file. When you specify an XML file (.xml extension), it will contain metadata about the application container after it is unplugged. The SQL statement creates the XML file, and it contains the required information to enable a `CREATE` `PLUGGABLE` `DATABASE` statement on a target CDB to plug in the application container. When you specify a.pdb file, it contains a compressed archive of the XML file that describes the application container and the files used by the application container (such as the data files and wallet file). A.pdb file enables you to copy a single, compressed file (instead of multiple files) to a new location to plug the application container into a CDB.

Before it can be unplugged, the application container must not have any application PDBs plugged into it, and it must be closed. When you unplug an application container, the unplugged application container is in mounted mode. The unplug operation makes some changes in the application container’s data files to record, for example, that the application container was successfully unplugged. Because it is still part of the CDB, the unplugged application container is included in an RMAN backup of the entire CDB. Such a backup provides a convenient way to archive the unplugged application container in case it is needed in the future.

To completely remove the application container from the CDB, you can drop it. The only operation supported on an unplugged application container is dropping the application container. The application container must be dropped from the CDB before it can be plugged back into the same CDB. An application container is usable only when it is plugged into a CDB.

See Also:

- " [Unplugging a PDB from a CDB](creating-and-removing-pdbs-with-sql-plus.md) "
- " Dropping an Application Container "
- " [Modifying the Open Mode of PDBs](administering-a-cdb-with-sql-plus.md) " for information about closing a PDB
- " [Using the ALTER SYSTEM Statement to Modify a PDB](administering-pdbs-with-sql-plus.md) " for information about initialization parameters and unplugged PDBs
- [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=DBSEG573) for information about common users and local users

**Parent topic:** Unplugging an Application Container from a CDB

##### 40.1.2.2 Unplugging an Application Container

You must meet prerequisites when unplugging an application container.

- The current user must have `SYSDBA` or `SYSOPER` administrative privilege, and the privilege must be either commonly granted or locally granted in the PDB. The user must exercise the privilege using `AS` `SYSDBA` or `AS` `SYSOPER` at connect time.
- The application container must have been opened at least once.
- The application container must not have any application PDBs plugged into it.
- The application container must not have an application seed plugged into it.

Note:

If you are unplugging an application container that includes data that was encrypted with Transparent Data Encryption, then follow the instructions in [Oracle Database Advanced Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=ASOAG10441).

To unplug an application container:

1. In SQL\*Plus, ensure that the current container is the root of the CDB.
	See " [About the Current Container](administering-a-cdb-with-sql-plus.md) " and " [Accessing a Container in a CDB with SQL\*Plus](administering-a-cdb-with-sql-plus.md) ".
2. Close the application container.
	In an Oracle Real Application Clusters (Oracle RAC) environment, the application container must be closed on all instances.
3. Run the `ALTER` `PLUGGABLE` `DATABASE` statement with the `UNPLUG` `INTO` clause, and specify the application container to unplug and the name and location of the application container’s XML metadata file or.pdb file.

Example 40-4 Unplugging Application Container salesact

This `ALTER` `PLUGGABLE` `DATABASE` statement unplugs the application container `salesact` and creates the salesact.xml metadata file in the /oracle/data/ directory:

```
ALTER PLUGGABLE DATABASE salesact UNPLUG INTO '/oracle/data/saleact.xml';
```

**Parent topic:** Unplugging an Application Container from a CDB

#### 40.1.3 Dropping an Application Container

You can use the `DROP` `PLUGGABLE` `DATABASE` statement to drop an application container. You can drop an application container when you want to move the application container from one CDB to another or when you no longer need the application container.

Dropping an application container is very similar to dropping a PDB. When you drop an application container, the control file of the CDB is modified to eliminate all references to the dropped application container. Archived redo log files and backups associated with the application container are not removed, but you can use Oracle Recovery Manager (RMAN) to remove them.

When dropping an application container, you can either keep or delete the application container’s data files by using one of the following clauses:

- `KEEP` `DATAFILES`, the default, retains the data files.
	The application container’s temp file is removed even when `KEEP` `DATAFILES` is specified because the temp file is no longer needed.
- `INCLUDING` `DATAFILES` removes the data files from disk.
	If an application container was created with the `SNAPSHOT` `COPY` clause, then you must specify `INCLUDING` `DATAFILES` when you drop the application container.

The following prerequisites must be met:

- The application container must be in mounted mode, or it must be unplugged.
	See " [Modifying the Open Mode of PDBs](administering-a-cdb-with-sql-plus.md) ".
	See " Unplugging an Application Container ".
- The current user must have `SYSDBA` or `SYSOPER` administrative privilege, and the privilege must be either commonly granted or locally granted in the application container. The user must exercise the privilege using `AS` `SYSDBA` or `AS` `SYSOPER` at connect time.
- The application container must not have any application PDBs plugged into it.
- The application container must not have an application seed plugged into it.

Note:

This operation is destructive.

To drop an application container:

1. In SQL\*Plus, ensure that the current container is the CDB root.
	See " [About the Current Container](administering-a-cdb-with-sql-plus.md) " and " [Accessing a Container in a CDB with SQL\*Plus](administering-a-cdb-with-sql-plus.md) ".
2. Run the `DROP` `PLUGGABLE` `DATABASE` statement and specify the application container to drop.

Example 40-5 Dropping Application Container salesact While Keeping Its Data Files

```
DROP PLUGGABLE DATABASE salesact
  KEEP DATAFILES;
```

Example 40-6 Dropping Application Container salesact and Its Data Files

```
DROP PLUGGABLE DATABASE saleact
  INCLUDING DATAFILES;
```

**Parent topic:** Creating and Removing Application Containers with SQL\*Plus

### 40.2 Creating and Removing Application Seeds with SQL\*Plus

You can create application seeds in several different ways, including using the CDB seed, cloning an existing PDB or non-CDB, and plugging in an unplugged PDB. You can also remove application seeds from application containers.

- Creating Application Seeds  
	You can use the `CREATE PLUGGABLE DATABASE` statement to create an application seed in an application container.
- Unplugging an Application Seed from an Application Container  
	You can unplug an application seed from an application container.
- Dropping an Application Seed  
	You can use the `DROP` `PLUGGABLE` `DATABASE` statement to drop an application seed. You can drop an application seed when you no longer need it.

**Parent topic:** Creating and Removing Application Containers and Seeds with SQL\*Plus

#### 40.2.1 Creating Application Seeds

You can use the `CREATE PLUGGABLE DATABASE` statement to create an application seed in an application container.

- About Creating an Application Seed  
	You can use the `CREATE` `PLUGGABLE` `DATABASE` statement with the `AS SEED` clause to create a new application seed in an application container.
- Preparing for an Application Seed  
	Prerequisites must be met before creating an application seed.
- Creating an Application Seed  
	You create an application seed by including the `AS SEED` clause in the `CREATE PLUGGABLE DATABASE` statement.

**Parent topic:** Creating and Removing Application Seeds with SQL\*Plus

##### 40.2.1.1 About Creating an Application Seed

You can use the `CREATE` `PLUGGABLE` `DATABASE` statement with the `AS SEED` clause to create a new application seed in an application container.

You can use an application seed to provision an application container with application PDBs that have the application root’s applications installed. Typically, the application container’s applications are installed in the application root before the application seed is created. After the application seed is created, it is synchronized with the application root so that the applications are installed in the application seed. When that is complete, any PDBs created using the application seed have the applications installed. When an application in the application root is upgraded or patched, the application seed must be synchronized with the application root to apply these changes.

You create an application seed by including the `AS SEED` clause in the `CREATE PLUGGABLE DATABASE` statement.

An application container can have zero or one application seed. When you create an application seed using the `AS SEED` clause, you do not specify its name. The application seed name is always application\_container\_name `$SEED`, where application\_container\_name is the name of the application seed’s application container. For example, an application seed in the `salesact` application container must be named `salesact$SEED`.

When you create a new application seed, you must specify an administrator for the application container in the `CREATE` `PLUGGABLE` `DATABASE` statement. The statement creates the administrator as a local user in the application container and grants the `PDB_DBA` role locally to the administrator.

##### 40.2.1.2 Preparing for an Application Seed

Prerequisites must be met before creating an application seed.

Ensure that the following prerequisites are met before creating an application seed:

- The CDB must exist.
	See [Creating and Configuring a CDB](creating-and-configuring-a-cdb.md).
- The CDB must be in read/write mode.
- The application container to which the application seed will belong must be in read/write mode.
- The current user must be a common user whose current container is the application root to which the application seed will belong.
- The current user must have the `CREATE` `PLUGGABLE` `DATABASE` system privilege.
- For the application seed to include the application for the application container, the application must be installed in the application root.

See Also:

- " [About the Current Container](administering-a-cdb-with-sql-plus.md) "
- [Managing Applications in an Application Container](administering-application-containers-with-sql-plus.md)

**Parent topic:** Creating Application Seeds

##### 40.2.1.3 Creating an Application Seed

You create an application seed by including the `AS SEED` clause in the `CREATE PLUGGABLE DATABASE` statement.

An application seed in an application container is similar to the seed in a CDB. An application seed enables you to create application PDBs that meet the requirements of an application container quickly and easily.

Before creating an application seed, complete the prerequisites described in " Preparing for an Application Seed ".

1. In SQL\*Plus, ensure that the current container is the application root.
2. Run the `CREATE` `PLUGGABLE` `DATABASE` statement, and include the `AS SEED` clause, to create the application seed. Specify other clauses when they are required.
	After you create the application seed, it is in mounted mode, and its status is `NEW`. You can view the open mode of an application seed by querying the `OPEN_MODE` column in the `V$PDBS` view. You can view the status of an application seed by querying the `STATUS` column of the `CDB_PDBS` or `DBA_PDBS` view.
	A new default service is created for the application seed. The service has the same name as the application seed and can be used to access the application seed. Oracle Net Services must be configured properly for clients to access this service.
3. Open the new application seed in read/write mode.
4. You must open the new application seed in read/write mode for Oracle Database to complete the integration of the new application seed into the application container. An error is returned if you attempt to open the application seed in read-only mode. After the application seed is opened in read/write mode, its status is `NORMAL`.
5. Perform one or more of the following actions:
	- If the application seed was created from the CDB seed, then switch container to the application seed, and use an `ALTER PLUGGABLE DATABASE` statement with the `SYNC` clause to synchronize the application seed. Synchronizing with the application root instantiates one or more of the application root’s applications in the application seed.
		- If the application seed was created from an application root, then switch container to the application seed, and run the pdb\_to\_apppdb.sql script to convert the application root to an application PDB.
	These actions are not required when the application seed is created by cloning an application PDB.
6. Close the application seed, and then open it in open read-only mode.
7. Back up the application seed.
	An application seed cannot be recovered unless it is backed up.
	Note:
	- If an error is returned during application seed creation, then the application seed being created might be in an `UNUSABLE` state. You can check an application seed’s state by querying the `CDB_PDBS` or `DBA_PDBS` view, and you can learn more about application seed creation errors by checking the alert log. An unusable application seed can only be dropped.
	- When an application in the application root is upgraded or patched in the application root, the application seed must synchronize with the application root to include the changes.

Example 40-7 Creating an Application Seed From the CDB Seed

This example assumes the following factors:

- The application seed is being created in an application container named `salesact`.
- Storage limits are not required for the application seed. Therefore, the `STORAGE` clause is not required.
- The application seed does not require a default tablespace.
- The `PATH_PREFIX` clause is not required.
- The `FILE_NAME_CONVERT` clause and the `CREATE_FILE_DEST` clause are not required.
	Either Oracle Managed Files is enabled for the CDB, or the `PDB_FILE_NAME_CONVERT` initialization parameter is set. The files associated with the CDB seed will be copied to a new location based on the Oracle Managed Files configuration or the initialization parameter setting.
- There is no file with the same name as the new temp file that will be created in the target location. Therefore, the `TEMPFILE REUSE` clause is not required.
- No predefined Oracle roles need to be granted to the `PDB_DBA` role.

Given the preceding factors, the following statement creates the application seed from the CDB seed, opens the application seed, switches containers to the application seed, synchronizes the application seed with all of the applications in the application root, closes the application seed, and opens the application seed in open read-only mode:

```
CREATE PLUGGABLE DATABASE AS SEED ADMIN USER actseedadm IDENTIFIED BY password;
ALTER PLUGGABLE DATABASE salesact$SEED OPEN;
ALTER SESSION SET CONTAINER=salesact$SEED;
ALTER PLUGGABLE DATABASE APPLICATION ALL SYNC;
ALTER PLUGGABLE DATABASE CLOSE IMMEDIATE;
ALTER PLUGGABLE DATABASE OPEN READ ONLY;
```

Because the application container name is `salesact`, the application seed name is `salesact$SEED`.

A local user with the name of the specified local administrator is created and granted the `PDB_DBA` common role locally in the application seed. If this user was not granted administrator privileges during application seed creation, then use the SYS and SYSTEM common users to administer to the application seed.

The application seed was synchronized with the application root when it was created. Therefore, the application seed includes the applications installed in the application root and the application common objects that are part of those applications. When a new application PDB is created using the application seed, the application PDB also includes the installed applications and application common objects.

Example 40-8 Creating an Application Seed From an Application PDB

This example assumes the following factors:

- The application seed is being created in an application container named `salesact`.
- The application seed is being created in an application PDB in the application container named `salesapppdb`.
- Storage limits are not required for the application seed. Therefore, the `STORAGE` clause is not required.
- The application seed does not require a default tablespace.
- The `PATH_PREFIX` clause is not required.
- The `FILE_NAME_CONVERT` clause and the `CREATE_FILE_DEST` clause are not required.
	Either Oracle Managed Files is enabled for the CDB, or the `PDB_FILE_NAME_CONVERT` initialization parameter is set. The files associated with the application root will be copied to a new location based on the Oracle Managed Files configuration or the initialization parameter setting.
- There is no file with the same name as the new temp file that will be created in the target location. Therefore, the `TEMPFILE REUSE` clause is not required.

Given the preceding factors, the following statement creates the application seed from the application root, opens the application seed, closes the application seed, and opens the application seed in open read-only mode:

```
CREATE PLUGGABLE DATABASE AS SEED FROM salesapppdb;
ALTER PLUGGABLE DATABASE salesact$SEED OPEN;
ALTER PLUGGABLE DATABASE CLOSE IMMEDIATE;
ALTER PLUGGABLE DATABASE OPEN READ ONLY;
```

Because the application container name is `salesact`, the application seed name is `salesact$SEED`.

The application seed was created from an application PDB. Therefore, the application seed includes the applications installed in the application root and the application common objects that are part of those applications. When a new application PDB is created using the application seed, the application PDB also includes the installed applications and application common objects.

Example 40-9 Creating an Application Seed From an Application Root

This example assumes the following factors:

- The application seed is being created in an application container named `salesact`. The application seed is cloned from the root of the application container.
- Storage limits are not required for the application seed. Therefore, the `STORAGE` clause is not required.
- The application seed does not require a default tablespace.
- The `PATH_PREFIX` clause is not required.
- The `FILE_NAME_CONVERT` clause and the `CREATE_FILE_DEST` clause are not required.
	Either Oracle Managed Files is enabled for the CDB, or the `PDB_FILE_NAME_CONVERT` initialization parameter is set. The files associated with the application root will be copied to a new location based on the Oracle Managed Files configuration or the initialization parameter setting.
- There is no file with the same name as the new temp file that will be created in the target location. Therefore, the `TEMPFILE REUSE` clause is not required.

Given the preceding factors, the following statement creates the application seed from the application root, opens the application seed, switches containers to the application seed, runs the pdb\_to\_apppdb.sql script to convert the application root to an application PDB, closes the application seed, and opens the application seed in open read-only mode:

```
CREATE PLUGGABLE DATABASE AS SEED FROM salesact;
ALTER PLUGGABLE DATABASE salesact$SEED OPEN;
ALTER SESSION SET CONTAINER=salesact$SEED;
@$ORACLE_HOME/rdbms/admin/pdb_to_apppdb.sql
ALTER PLUGGABLE DATABASE CLOSE IMMEDIATE;
ALTER PLUGGABLE DATABASE OPEN READ ONLY;
```

Because the application container name is `salesact`, the application seed name is `salesact$SEED`.

The application seed was created from the application root. Therefore, the application seed includes the applications installed in the application root and the application common objects that are part of those applications. When a new application PDB is created using the application seed, the application PDB also includes the installed applications and application common objects.

#### 40.2.2 Unplugging an Application Seed from an Application Container

You can unplug an application seed from an application container.

- About Unplugging an Application Seed  
	Unplugging an application seed disassociates the application seed from an application container. You unplug an application seed when you no longer want the application seed to be available.
- Unplugging an Application Seed  
	You must meet prerequisites when unplugging an application seed.

**Parent topic:** Creating and Removing Application Seeds with SQL\*Plus

##### 40.2.2.1 About Unplugging an Application Seed

Unplugging an application seed disassociates the application seed from an application container. You unplug an application seed when you no longer want the application seed to be available.

Unplugging an application seed is similar to unplugging a PDB. To unplug a application seed, connect to its application root and use the `ALTER` `PLUGGABLE` `DATABASE` statement to specify an XML file or a.pdb file. When you specify an XML file (.xml extension), it will contain metadata about the application seed after it is unplugged. The SQL statement creates the XML file, and it contains the required information to enable a `CREATE` `PLUGGABLE` `DATABASE` statement on a target CDB to plug it in as a PDB or an application PDB. When you specify a.pdb file, it contains a compressed archive of the XML file that describes the application seed and the files used by the application seed (such as the data files and wallet file). A.pdb file enables you to copy a single, compressed file (instead of multiple files) to a new location to plug in as a PDB or an application PDB.

Before it can be unplugged, the application seed must be closed. When you unplug an application seed, the unplugged application seed is in mounted mode. The unplug operation makes some changes in the application seed’s data files to record, for example, that the application seed was successfully unplugged. Because it is still part of the application container, the unplugged application seed is included in an RMAN backup of the entire CDB. Such a backup provides a convenient way to archive the unplugged application seed in case it is needed in the future.

To completely remove the application seed from the application container, you can drop it. The only operation supported on an unplugged application seed is dropping the application seed. The application seed must be dropped from the application container before it can be plugged back into the same application container. An application seed is usable only when it is plugged into an application container.

See Also:

- " [Unplugging a PDB from a CDB](creating-and-removing-pdbs-with-sql-plus.md) "
- " Dropping an Application Seed "
- " [Modifying the Open Mode of PDBs](administering-a-cdb-with-sql-plus.md) " for information about closing a PDB
- " [Using the ALTER SYSTEM Statement to Modify a PDB](administering-pdbs-with-sql-plus.md) " for information about initialization parameters and unplugged PDBs
- [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=DBSEG573) for information about common users and local users

**Parent topic:** Unplugging an Application Seed from an Application Container

##### 40.2.2.2 Unplugging an Application Seed

You must meet prerequisites when unplugging an application seed.

The following prerequisites must be met:

- The current user must have `SYSDBA` or `SYSOPER` administrative privilege, and the privilege must be either commonly granted or locally granted in the application container. The user must exercise the privilege using `AS` `SYSDBA` or `AS` `SYSOPER` at connect time.
- The application seed must have been opened at least once.

Note:

If you are unplugging an application seed that includes data that was encrypted with Transparent Data Encryption, then follow the instructions in [Oracle Database Advanced Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=ASOAG10441).

To unplug an application seed:

1. In SQL\*Plus, ensure that the current container is the application root of the application container to which the application seed belongs.
	See " [About the Current Container](administering-a-cdb-with-sql-plus.md) " and " [Accessing a Container in a CDB with SQL\*Plus](administering-a-cdb-with-sql-plus.md) ".
2. Close the application seed.
	In an Oracle Real Application Clusters (Oracle RAC) environment, the application seed must be closed on all instances.
3. Run the `ALTER` `PLUGGABLE` `DATABASE` statement with the `UNPLUG` `INTO` clause, and specify the application seed to unplug and the name and location of the application seed’s XML metadata file or.pdb file.

Example 40-10 Unplugging Application Seed salesact$SEED

This `ALTER` `PLUGGABLE` `DATABASE` statement unplugs the application seed `salesact$SEED` and creates the salesact$SEED.xml metadata file in the /oracle/data/ directory:

```
ALTER PLUGGABLE DATABASE salesact$SEED UNPLUG INTO '/oracle/data/saleact$SEED.xml';
```

**Parent topic:** Unplugging an Application Seed from an Application Container

#### 40.2.3 Dropping an Application Seed

You can use the `DROP` `PLUGGABLE` `DATABASE` statement to drop an application seed. You can drop an application seed when you no longer need it.

When you drop an application seed, the control file of the CDB is modified to eliminate all references to the dropped application seed. Archived redo log files and backups associated with the application seed are not removed, but you can use Oracle Recovery Manager (RMAN) to remove them.

When dropping an application seed, you can either keep or delete the application seed’s data files by using one of the following clauses:

- `KEEP` `DATAFILES`, the default, retains the data files.
	The application seed’s temp file is removed even when `KEEP` `DATAFILES` is specified because the temp file is no longer needed.
- `INCLUDING` `DATAFILES` removes the data files from disk.
	If an application seed was created with the `SNAPSHOT` `COPY` clause, then you must specify `INCLUDING` `DATAFILES` when you drop the application seed.

The following prerequisites must be met:

- The application seed must be in mounted mode, or it must be unplugged.
	See " [Modifying the Open Mode of PDBs](administering-a-cdb-with-sql-plus.md) ".
	See " Unplugging an Application Seed ".
- The current user must have `SYSDBA` or `SYSOPER` administrative privilege, and the privilege must be either commonly granted or locally granted in the application container. The user must exercise the privilege using `AS` `SYSDBA` or `AS` `SYSOPER` at connect time.

To drop an application seed:

1. In SQL\*Plus, ensure that the current container is the application root of the application container to which the application seed belongs.
	See " [About the Current Container](administering-a-cdb-with-sql-plus.md) " and " [Accessing a Container in a CDB with SQL\*Plus](administering-a-cdb-with-sql-plus.md) ".
2. Run the `DROP` `PLUGGABLE` `DATABASE` statement and specify the application seed.

Example 40-11 Dropping Application Seed salesact$SEED While Keeping Its Data Files

```
DROP PLUGGABLE DATABASE salesact$SEED
  KEEP DATAFILES;
```

Example 40-12 Dropping Application Seed salesact$SEED and Its Data Files

```
DROP PLUGGABLE DATABASE saleact$SEED
  INCLUDING DATAFILES;
```

**Parent topic:** Creating and Removing Application Seeds with SQL\*Plus

### 40.3 Creating an Application PDB

You create an application PDB by running the `CREATE PLUGGABLE DATABASE` statement with an application root as the current container.

You can create application PDBs using the same SQL statements that you use to create PDBs in the CDB root. The newly created PDB is an application PDB when the `CREATE PLUGGABLE DATABASE` statement is run in an application root. The statement must be run in an application root and has an explicit dependency on the application database defined in that application root.

Before creating an application PDB, complete the prerequisites described in " [Preparing for PDBs](creating-and-removing-pdbs-with-sql-plus.md) ". You must also complete the prerequisites for the specific type of PDB you are creating. For example, if you are cloning a PDB, then you must meet the prerequisites PDB cloning.

1. In SQL\*Plus, ensure that the current container is the application root.
2. Run a `CREATE` `PLUGGABLE` `DATABASE` statement.
	After you create the application PDB, it is in mounted mode, and its status is `NEW`. You can view the open mode of an application PDB by querying the `OPEN_MODE` column in the `V$PDBS` view. You can view the status of an application PDB by querying the `STATUS` column of the `CDB_PDBS` or `DBA_PDBS` view.
	A new default service is created for the application PDB. The service has the same name as the application PDB and can be used to access the application PDB. Oracle Net Services must be configured properly for clients to access this service.
3. Open the new application PDB in read/write mode.
4. You must open the new application PDB in read/write mode for Oracle Database to complete the integration of the new application PDB into the application container. An error is returned if you attempt to open the application PDB in read-only mode. After the application PDB is opened in read/write mode, its status is `NORMAL`.
5. Switch container to the application PDB.
6. Use an `ALTER PLUGGABLE DATABASE` statement with the `SYNC` clause to synchronize the application PDB.
	Synchronizing with the application PDB instantiates one or more of the application root’s applications in the application PDB.
7. Close the application PDB, and then open it in open read-only mode.
8. Back up the application PDB.
	An application PDB cannot be recovered unless it is backed up.
	Note:
	- If an error is returned during application PDB creation, then the application PDB being created might be in an `UNUSABLE` state. You can check an application PDB’s state by querying the `CDB_PDBS` or `DBA_PDBS` view, and you can learn more about application PDB creation errors by checking the alert log. An unusable application PDB can only be dropped.
	- When an application in the application root is upgraded or patched in the application root, the application PDB must synchronize with the application root to include the changes.