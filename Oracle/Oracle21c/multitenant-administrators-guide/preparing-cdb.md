---
title: "Administrator’s Guide"
book: "Multitenant Administrator's Guide"
doc_id: F31734-10
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/multi/preparing-cdb.html
tags:
  - oracle
  - 21c
  - multitenant-administrators-guide
---

Before creating the CDB, you must make many important decisions: physical layout, database character set, database block sizes, and so on.

**Parent topic:** [Creating CDBs](creating-and-configuring-a-multitenant-environment.md)

### Prerequisites for a Multitenant Environment

Prerequisites must be met for a multitenant environment.

The following minimum prerequisites must be met before you can create and use a multitenant environment:

- You must install or upgrade to Oracle Database 12c or later releases. Oracle Multitenant is not supported in Oracle Database 11g and earlier releases.
	The installation includes setting various environment variables unique to your operating system and establishing the directory structure for software and database files.
- The database compatibility level must be set to `12.0.0` or later.
- Sufficient memory must be available to start the Oracle Database instance.
	Size the memory required by a CDB to accommodate the workload of each of its containers and the number of containers.
- Sufficient disk storage space must be available for the planned PDBs on the computer that runs Oracle Database. In an Oracle RAC environment, sufficient shared storage must be available.
	The disk storage space required by a CDB is the sum of the space requirements for all PDBs that will reside in the CDB.

These prerequisites are discussed in the [Oracle Database Installation Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=GINST) or [Oracle Grid Infrastructure Installation and Upgrade Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=CWGEN) specific to your operating system. If you use the Oracle Universal Installer, then it will guide you through your installation and provide help in setting environment variables and establishing directory structure and authorizations.

See Also:

- [Oracle Database Installation Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=GINST) specific to your operating system
- [Oracle Database Upgrade Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=UPGRD005) for information about the database compatibility level

**Parent topic:** Preparing to Create a CDB

### Differences Between Oracle Home in Read-Only Mode and Read-Write Mode

The read-only Oracle home software image simplifies patching and mass rollouts of software across multiple database servers.

A read-only Oracle home (`ORACLE_HOME`) installation prevents both creation and modification of files inside the Oracle home directory.

Traditional read-write Oracle homes contain instance-specific files. If you patch these files, then you must patch each of them individually. However, when the Oracle home is read-only, instance-specific files are stored separately in the Oracle base directory (`ORACLE_BASE`), instead of in the Oracle home. Because of this configuration, you can use a read-only Oracle home as a software image that you can share across multiple database servers, because the Oracle home stores only the static files. This option simplifies patching and mass rollout, because when you want to distribute a patch to multiple database servers, you only need to update one Oracle home image.

Apart from the traditional `ORACLE_BASE` and `ORACLE_HOME` directories, the following additional directories exist in a read-only Oracle home:

- `ORACLE_BASE_HOME`: This is a subdirectory within the `ORACLE_BASE` directory. This directory contains user-specific files, instance-specific files, and log files.
- `ORACLE_BASE_CONFIG`: This directory is same as the `ORACLE_BASE` directory. This directory contains instance-specific dynamic files, such as configuration files.

See Also:

“Configuring Read-Only Oracle Homes” in the Oracle Database installation guide specific to your platform for more information about configuring an Oracle home in read-only mode.

**Parent topic:** Preparing to Create a CDB

### Deciding When to Create a CDB

You can create the CDB either during or after Oracle Database software installation.

The following are typical reasons to create a CDB after installation:

- You used Oracle Universal Installer (OUI) to install software only, and did not create a CDB.
- You want to create another CDB on the same host as an existing CDB. In this case, this chapter assumes that the new CDB uses the same Oracle home as the existing database. You can also create the CDB in a new Oracle home by running OUI again.

The techniques for creating a CDB are:

- With the Database Configuration Assistant (DBCA), a graphical tool.
	See " [Creating a CDB with DBCA](creating-and-configuring-an-oracle-database.md) ".
- With the `CREATE DATABASE ... ENABLE PLUGGABLE DATABASE` SQL command.
	See " [Creating a Database with the CREATE DATABASE Statement](creating-and-configuring-an-oracle-database.md) ".

**Parent topic:** Preparing to Create a CDB

### Deciding How to Configure the CDB

Prepare to create the CDB by research and careful planning.

- Plan the PDBs  
	Plan the tables and indexes for the pluggable databases (PDBs) and estimate the amount of space they require.
- Plan the Physical Layout  
	Plan the layout of the underlying operating system files your CDB will comprise.
- Learn How to Manage Initialization Parameters  
	Familiarize yourself with the initialization parameters that can be included in an initialization parameter file.
- Select the Character Set  
	You must choose a character set for the CDB.
- Decide Which Time Zones to Support  
	Consider which time zones your CDB must support.
- Select the Database and Redo Log Block Sizes  
	Select the standard database block size for the CDB.
- Plan the SYSTEM and SYSAUX Tablespaces  
	There is a separate `SYSAUX` and `SYSTEM` tablespace for the CDB root and for each PDB.
- Plan the Temporary Tablespaces  
	Plan to use default temporary tablespaces.
- Choose the Undo Mode  
	Plan to use an undo tablespace to manage your undo data.
- Plan the Services for Your Application  
	Plan for the database services required to meet the needs of your applications.
- Learn How to Start Up and Shut Down a CDB  
	Familiarize yourself with the principles and options of starting up and shutting down a database instance and mounting and opening a CDB.
- Plan for Oracle RAC  
	If you plan to use Oracle RAC, then plan for an Oracle RAC environment.

**Parent topic:** Preparing to Create a CDB

#### Plan the PDBs

Plan the tables and indexes for the pluggable databases (PDBs) and estimate the amount of space they require.

In a CDB, most user data resides in the PDBs. The root contains no user data or minimal user data. Plan for the PDBs that will be part of the CDB. The disk storage space requirement for a CDB is the space required for the Oracle Database installation plus the sum of the space requirements for all PDBs that will be part of the CDB.

The `MAX_PDBS` initialization parameter specifies a limit on the total number of PDBs that you can create in a CDB root or application root. The default value and maximum value for `MAX_PDBS` depend on your Oracle Database offering. See [Oracle Database Licensing Information User Manual](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=DBLIC-GUID-0F9EB85D-4610-4EDF-89C2-4916A0E7AC87) for details on which features are supported for different editions and services.

You can also create application containers in a CDB. An application container is a collection of application PDBs that store the data for one or more applications. In addition, application containers support user-created application common objects that can be shared by the application PDBs in the application container.

**Parent topic:** Deciding How to Configure the CDB

#### Plan the Physical Layout

Plan the layout of the underlying operating system files your CDB will comprise.

There are separate data files for the CDB root, `PDB$SEED`, each PDB, each application root, and each application PDB.

There is one online redo log for a single-instance CDB, or one online redo log for each instance of an Oracle Real Application Clusters (Oracle RAC) CDB. Also, for Oracle RAC, all data files and online redo log files must be on shared storage.

See Also:

- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=ADMIN-GUID-4A3C4616-0D81-4BBA-8EAD-FCAA8AD5C15A) for information about using Oracle Managed Files
- [Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=GUID-BC612D35-5399-4A35-843E-CF76E3D3CDB5)
- [Oracle Database Performance Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=GUID-B89C41F4-B12A-49E1-BFB9-5BF978E2D6B3)
- [Oracle Database Backup and Recovery User’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=GUID-9997EF87-B293-44D4-92F3-DD938E79170D)
- [Oracle Grid Infrastructure Installation and Upgrade Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=CWGEN) for information about configuring storage for Oracle RAC
- Your Oracle operating system–specific documentation, including the appropriate Oracle Database installation guide.

**Parent topic:** Deciding How to Configure the CDB

#### Learn How to Manage Initialization Parameters

Familiarize yourself with the initialization parameters that can be included in an initialization parameter file.

Before creating a CDB, ensure that you are familiar with the concept and operation of a server parameter file (SPFILE). An SPFILE file lets you store and manage your initialization parameters persistently in a server-side binary file.

A CDB uses a single SPFILE or a single text initialization parameter file (PFILE). Values of initialization parameters set for the root can be inherited by PDBs. You can set some initialization parameters for a PDB by using the `ALTER` `SYSTEM` statement.

The CDB root must be the current container when you operate on an SPFILE. The user who creates or modifies the SPFILE must be a common user with `SYSDBA`, `SYSOPER`, or `SYSBACKUP` administrative privilege, and the user must exercise the privilege by connecting `AS SYSDBA`, `AS SYSOPER`, or `AS SYSBACKUP` respectively.

The following initialization parameters are important:

- To create a CDB, the `ENABLE_PLUGGABLE_DATABASE` initialization parameter must be set to `TRUE`.
- Create the global database name for the CDB root by setting both the `DB_NAME` and `DB_DOMAIN` initialization parameters. The global database name of the root is the global database name of the CDB. The global database name of a PDB is defined by the PDB name and the `DB_DOMAIN` initialization parameter.

See Also:

- " [About the Current Container](administering-a-cdb-with-sql-plus.md) "
- " [Modifying a CDB with ALTER SYSTEM](administering-a-cdb-with-sql-plus.md) "
- " [Listing the Modifiable Initialization Parameters in PDBs](administering-a-cdb-with-sql-plus.md) "
- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=ADMIN-GUID-2DA8C61C-58B0-4892-8E5D-E7A9120BC120) for information about schema objects
- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=ADMIN-GUID-9698EA9B-013C-40AC-8CFB-12171A4B4974) for information about determining the global database name
- [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=GUID-FD266F6F-D047-4EBB-8D96-B51B1DCA2D61)

**Parent topic:** Deciding How to Configure the CDB

#### Select the Character Set

You must choose a character set for the CDB.

When selecting the database character set for the CDB, you must consider the current character sets of the databases that you want to consolidate (plug) into this CDB. Oracle recommends AL32UTF8 for the CDB database character set and AL16UTF6 for the CDB national character set because they provide the most flexibility.

When upgrading a non-CDB to a PDB, it is best to migrate the non-CDB to AL32UTF8 first. You can use Oracle Database Migration Assistant for Unicode (DMU) to migrate a non-CDB to AL32UTF8. After a CDB is created, you cannot migrate the character set of the CDB using DMU.

- Default CDB Character Set  
	It is important to select the right character set for your CDB. Oracle recommends AL32UTF8 as the CDB character set.
- Different Character Sets for CDB and PDBs  
	When the character set of the CDB root is AL32UTF8, PDBs that are plugged into the CDB can have a different character set from the CDB root.

See Also:

[Oracle Database Globalization Support Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=GUID-09777A99-B7DD-4695-9B2B-278122131000)

**Parent topic:** Deciding How to Configure the CDB

##### Default CDB Character Set

It is important to select the right character set for your CDB. Oracle recommends AL32UTF8 as the CDB character set.

AL32UTF8 is Oracle's name for the UTF-8 encoding of the Unicode standard. The Unicode standard is the universal character set that supports most of the currently spoken languages of the world. The use of the Unicode standard is indispensable for any multilingual technology, including database processing.

After a CDB is created and accumulates production data, changing the database character set is a time consuming and complex project. Therefore, it is very important to select the right character set at installation time. Even if the database does not currently store multilingual data but is expected to store multilingual data within a few years, the choice of AL32UTF8 for the database character set is usually the only good decision. The universality and flexibility of Unicode typically outweighs some additional cost associated with it, such as slightly slower text processing compared to single-byte character sets and higher storage space requirements for non-ASCII text compared to non-Unicode character sets.

If you do not want to use AL32UTF8, and you are not restricted in your choice by a vendor requirement, then Oracle suggests that you use one of the character sets listed as recommended for the database. The recommended character sets were selected based on the requirements of modern client operating systems. Oracle Universal Installer (OUI) presents the recommended list only, and Database Configuration Assistant (DBCA) must be used separately to choose a non-recommended character set. In addition, the default database creation configuration in DBCA allows the selection of the recommended character sets only. You must use the advanced configuration mode of DBCA or the `CREATE DATABASE` statement to select a non-recommended character set.

If no character set choice is presented in an OUI or a DBCA installation mode, then AL32UTF8 is used as the database character set, unless a custom database template with another character set has been selected.

Note:

- AL32UTF8 is the proper implementation of the Unicode encoding UTF-8. AL32UTF8 is used as the default database character set while creating a database using Oracle Universal Installer (OUI) as well as Oracle Database Configuration Assistant (DBCA).
- You can only select an ASCII-based character set for the database on an ASCII-based platform.

Caution:

Do not use UTF8 as the database character set unless required unless explicitly requested by your application vendor. Despite having a very similar name, UTF8 is not a proper implementation of the Unicode encoding UTF-8. If the UTF8 character set is used where UTF-8 processing is expected, data loss and security issues may occur. This is especially true for Web related data, such as XML and URL addresses.

AL32UTF8 and UTF8 character sets are not compatible with each other as they have different maximum character widths. AL32UTF8 has a maximum character width of 4 bytes, whereas UTF8 has a maximum character width of 3 bytes.

##### Different Character Sets for CDB and PDBs

When the character set of the CDB root is AL32UTF8, PDBs that are plugged into the CDB can have a different character set from the CDB root.

PDBs that you create from `PDB$SEED` inherit the AL32UTF8 character set from it, but you can migrate the PDB to a different character set. When the character set of the root is not AL32UTF8, all PDBs in the CDB use the character set of the CDB root.

Note:

Oracle Multitenant does not support a LOB in one container from being accessed by a container with a different character set using data links, extended data links, or the `CONTAINERS()` clause. For example, if the CDB root and `salespdb` have different character sets, then a `CONTAINERS()` query run in the CDB root should not access LOBs stored in `salespdb`.

**Parent topic:** Select the Character Set

#### Decide Which Time Zones to Support

Consider which time zones your CDB must support.

You can set the time zones for the entire CDB (including all PDBs). You can also set the time zones individually for each PDB.

See Also:

" [Specifying the Database Time Zone File](create-cdb-adv.md) " for information about specifying the database time zone and time zone file

**Parent topic:** Deciding How to Configure the CDB

#### Select the Database and Redo Log Block Sizes

Select the standard database block size for the CDB.

This is specified at CDB creation by the `DB_BLOCK_SIZE` initialization parameter and cannot be changed after the CDB is created. The standard block size applies to the entire CDB.

If you plan to store online redo log files on disks with a 4K byte sector size, then determine whether you must manually specify the online redo log block size.

- " [Specifying Database Block Sizes](create-cdb-adv.md) " to learn how to specify database block sizes
- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=ADMIN-GUID-AC858C69-317E-4193-838D-59F8DDEA1927) for information about planning the block size of redo log files

**Parent topic:** Deciding How to Configure the CDB

#### Plan the SYSTEM and SYSAUX Tablespaces

There is a separate `SYSAUX` and `SYSTEM` tablespace for the CDB root and for each PDB.

You must determine the appropriate initial sizing for the `SYSAUX` tablespace. Also, plan to use a default tablespace for non- `SYSTEM` users to prevent inadvertently saving database objects in the `SYSTEM` tablespace. You can specify a separate default tablespace for the CDB root and for each PDB.

See Also:

- " [About the SYSAUX Tablespace](create-cdb-adv.md) " for information about the `SYSAUX` tablespace
- " [Creating a Default Permanent Tablespace](create-cdb-adv.md) " for information about creating a default permanent tablespace
- " [About Container Modification When Connected to CDB Root](administering-a-cdb-with-sql-plus.md) "

**Parent topic:** Deciding How to Configure the CDB

#### Plan the Temporary Tablespaces

Plan to use default temporary tablespaces.

A default temporary tablespace exists for every container in the CDB. Therefore, the CDB root and every PDB, application root, and application PDB has its own default temporary tablespace.

Oracle Database uses the shared temporary tablespace for recursive SQL only. Hosted PDB tenants do not use this tablespace directly.

See Also:

- " [About Container Modification When Connected to CDB Root](administering-a-cdb-with-sql-plus.md) "
- " [Creating a Default Temporary Tablespace](create-cdb-adv.md) " for information about creating a default temporary tablespace

**Parent topic:** Deciding How to Configure the CDB

#### Choose the Undo Mode

Plan to use an undo tablespace to manage your undo data.

A CDB can run in different undo modes. You can configure a CDB to have one active undo tablespace for the entire CDB or a separate undo tablespace for each container in the CDB. You can specify the undo mode during CDB creation, and you can change the undo mode after the CDB is created.

When you choose to have one active undo tablespace for the entire CDB, shared undo is used, and local undo is disabled. In this configuration, there is one active undo tablespace for a single-instance CDB. When local undo is enabled, there is one undo tablespace for each container in a single instance configuration. For an Oracle RAC CDB, each PDB has one undo tablespace in each node in which it is open. With shared undo, only a common user who has the appropriate privileges and whose current container is the root can create an undo tablespace.

The best practice is to use local undo for a CDB. Shared undo is supported primarily for upgrade and transitional purposes only. Although there is minor overhead associated with local undo when compared with shared undo, the benefits of local undo make it preferable in most environments. Local undo makes unplug operations and point in time recovery faster, and it is required for some features, such as relocating a PDB. By default, DBCA creates new CDBs with local undo enabled.

In a CDB, the `UNDO_MANAGEMENT` initialization parameter must be set to `AUTO`, and an undo tablespace is required to manage the undo data.

When local undo is not enabled, undo tablespaces are visible in static data dictionary views and dynamic performance (V$) views when the current container is the root. Undo tablespaces are visible only in dynamic performance views when the current container is a PDB.

Also, when local undo is disabled, Oracle Database silently ignores undo tablespace and rollback segment operations when the current container is a PDB.

See Also:

- " [Setting the Undo Mode in a CDB Using ALTER DATABASE](administering-a-cdb-with-sql-plus.md) "
- " [About the Current Container](administering-a-cdb-with-sql-plus.md) "
- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=ADMIN-GUID-2C865CF9-A8B5-4BF1-A451-E8C08D3611F0) for information about managing undo

**Parent topic:** Deciding How to Configure the CDB

#### Plan the Services for Your Application

Plan for the database services required to meet the needs of your applications.

The root and each PDB might require several services. You can create services for the root or for individual PDBs.

Database services have an optional `PDB` property. You can create services and associate them with a particular PDB by specifying the `PDB` property. Services with a null `PDB` property are associated with the CDB root.

You can also use the `DBMS_SERVICE` supplied PL/SQL package to create services and associate them with PDBs. When you run `CREATE_SERVICE` procedure, the service is associated with the current container.

You can manage services with the SRVCTL utility, Oracle Enterprise Manager Cloud Control, and the `DBMS_SERVICE` supplied PL/SQL package.

When you create a PDB, a new default service for the PDB is created automatically. The service has the same name as the PDB. You cannot manage this service with the SRVCTL utility. However, you can create user-defined services and customize them for your applications.

See Also:

- " [Managing Services for PDBs](administering-pdbs-with-sql-plus.md) "
- " [Managing Application Workloads with Database Services](create-cdb-adv.md) "
- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=ADMIN-GUID-B2D64FD5-0DE7-4201-AB0F-3941955CADB8) to learn about using SRVCTL with a single-instance database
- [Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=RACAD-GUID-3ED4DBCE-A148-462B-8A79-534A3F0D6E7D) for information about using the SRVCTL utility with an Oracle RAC database

**Parent topic:** Deciding How to Configure the CDB

#### Learn How to Start Up and Shut Down a CDB

Familiarize yourself with the principles and options of starting up and shutting down a database instance and mounting and opening a CDB.

In a CDB, the CDB root and all containers share a single database instance, or, when using Oracle RAC, multiple concurrent instances. You can start up and shut down an entire CDB, which in turn determines the state of hosted PDBs. When the CDB is open, you can control the open mode of PDBs by using either an `ALTER PLUGGABLE                 DATABASE` statement in the context of the CDB or PDB to open or close hosted PDBs. To maintain backward compatibility, the `ALTER DATABASE OPEN` statement is supported when it is executed and a PDB is the current container.

You can also use the SQL\*Plus `STARTUP` command and the SQL\*Plus `SHUTDOWN` command when a PDB is the current container. However, the SQL\*Plus `STARTUP MOUNT` command is a CDB-only operation and cannot be used when a PDB is the current container.

See Also:

- " [Modifying the Open Mode of PDBs](administering-pdbs-with-sql-plus.md) "
- " [Modifying a PDB with the ALTER PLUGGABLE DATABASE Statement](administering-pdbs-with-sql-plus.md) "
- " [Starting Up and Shutting Down a CDB](administering-a-cdb-with-sql-plus.md) "

**Parent topic:** Deciding How to Configure the CDB

#### Plan for Oracle RAC

If you plan to use Oracle RAC, then plan for an Oracle RAC environment.

The Oracle RAC documentation describes special considerations for a CDB in an Oracle RAC environment. See your platform-specific Oracle RAC installation guide for information about creating a CDB in an Oracle RAC environment.

See Also:

[Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=GUID-57166C75-59D4-4037-81CD-8CAD753DA64D)

**Parent topic:** Deciding How to Configure the CDB