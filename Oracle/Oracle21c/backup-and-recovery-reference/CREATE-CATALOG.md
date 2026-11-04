---
title: Backup and Recovery Reference
book: Database Backup and Recovery Reference
doc_id: F31837-09
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/rcmrf/CREATE-CATALOG.html
tags:
  - oracle
  - 21c
  - backup-and-recovery-reference
---

Purpose

Use the `CREATE CATALOG` command to create a base recovery catalog. A virtual private catalog is created automatically when catalog privileges are granted to the virtual private catalog owner.

- A base recovery catalog is a database schema that contains RMAN metadata for a set of target databases.
- A virtual private catalog is a set of security policies that restrict user access to a subset of a base recovery catalog.

See Also:

- [Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/rcmrf&id=BRADV179) to learn how to create the recovery catalog
- " [RMAN Compatibility](rman-compatibility.md) " to learn about the requirements for the compatibility of the recovery catalog and the other components of the RMAN environment

Prerequisites

Execute this command only at the RMAN prompt. RMAN must be connected to the recovery catalog database either through the `CATALOG` command-line option or the `CONNECT` `CATALOG` command, and the catalog database must be open. A connection to a target database is not required.

The recovery catalog owner for the base recovery catalog must be granted the `RECOVERY_CATALOG_OWNER` role. The recovery catalog is created in the default tablespace of the recovery catalog owner.

You must have run the `dbmsrmansys.sql` script to grant additional privileges that are required for the `RECOVERY_CATALOG_OWNER` role.

Note:

Starting with Oracle Database 12c Release 1 (12.1.0.2), the recovery catalog database must use the Enterprise Edition.

The database user who owns a virtual private catalog must be granted the `CREATE SESSION` privilege. Starting with Oracle Database 12c Release 1 (12.1.0.2), virtual private catalogs can be created only when using Oracle Database Enterprise Edition.

If you are creating a virtual private catalog, then:
- You must use SQL\*Plus to connect to the recovery catalog database as the `SYS` user with `SYSDBA` privilege.
- The base recovery catalog owner must have used the RMAN `GRANT` command to grant either the `CATALOG` or `REGISTER` privilege (see Example 2-72).

See the `CONNECT` `CATALOG` description for restrictions for RMAN client connections to a virtual catalog when the RMAN client is from release Oracle Database 10g or earlier.

Usage Notes

Typically, you create the recovery catalog in a database created especially for this purpose. Do not create the recovery catalog in a privileged schema such as `SYS` or `SYSBACKUP`.

The best practice is to create one recovery catalog that serves as the central RMAN repository for many databases. For this reason it is called the base recovery catalog.

The owner of the base recovery catalog can `GRANT` or `REVOKE` restricted access to the catalog to other database users. Each restricted user has full read/write access to his own metadata, which is called a virtual private catalog. The RMAN metadata is stored in the schema of the virtual private catalog owner. The owner of the base recovery catalog controls what each virtual catalog user can access.

Syntax

createCatalog::=

![createcatalog](img/createcatalog.gif)

> CREATE CATALOG
>
> ![Oracle Logo](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/gifs/oracle.gif)[  
> Copyright © 2023, 2024, Oracle and/or its affiliates.](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/html/cpyr.htm)


Examples

Example 2-71 Creating a Recovery Catalog and Registering a Database

Assume that you start SQL\*Plus and connect to the recovery catalog `catdb` with administrator privileges. You execute the `CREATE USER` statement as follows, replacing password with a user-specified password (see [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/rcmrf&id=DBSEG33223) for information on creating secure passwords). The SQL statement creates a user `rco` in database `catdb` and grant the `rco` user the `RECOVERY_CATALOG_OWNER` role.

```
SQL> CREATE USER rco IDENTIFIED BY password
  2  DEFAULT TABLESPACE cattbs
  3  QUOTA UNLIMITED ON cattbs;
SQL> GRANT recovery_catalog_owner TO rco;
SQL> EXIT
```

Next, you run the `dbmsrmansys.sql` script to grant additional privileges that are required for the `RECOVERY_CATALOG_OWNER` role.
```
SQL> @$ORACLE_HOME/rdbms/admin/dbmsrmansys.sql
```

You then start RMAN and run the following RMAN commands to connect to the recovery catalog database as `rco` and create the recovery catalog:

```
RMAN> CONNECT CATALOG rco@catdb

recovery catalog database Password: password
connected to recovery catalog database

RMAN> CREATE CATALOG;
```

In the same RMAN session, you connect to a target database using operating system authentication and use the `REGISTER DATABASE` command to register this database in the catalog:

```
RMAN> CONNECT TARGET /
RMAN> REGISTER DATABASE;
RMAN> EXIT
```

Example 2-72 Creating a Virtual Private Catalog

Assume that you created the recovery catalog and registered a database as shown in Example 2-71. Now you want to create a virtual private catalog for database user `vpc1`. The database version is Oracle Database 12c Release 1 (12.1.0.2). You start SQL\*Plus and connect to recovery catalog database `catdb` as the `SYS` user with `SYSDBA` privilege.

You create the `vpc1` user and grant recovery catalog ownership as follows, replacing password with a user-specified password (see [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/rcmrf&id=DBSEG33223) for information on creating secure passwords):

```
SQL> CREATE USER vpc1 IDENTIFIED BY password
  2  DEFAULT TABLESPACE vpcusers;
SQL> GRANT CREATE SESSION TO vpc1;
SQL> EXIT
```

You then start RMAN and connect to the recovery catalog database as the catalog owner `rco`. By default, the virtual catalog owner has no access to the base recovery catalog. You use the `GRANT` command to grant virtual private catalog access to `vpc1` for RMAN operations on database `prod1` (but not `prod2`):

```
RMAN> CONNECT CATALOG rco@catdb
 
recovery catalog database Password: password
connected to recovery catalog database

RMAN> GRANT CATALOG FOR DATABASE prod1 TO vpc1;
RMAN> EXIT;
```

Now the backup operator who will use virtual private catalog `vpc1` is ready to create the virtual catalog. In the following example, the backup operator connects to the recovery catalog database as `vpc1` and registers the database prod1 with `vpc1`.

The virtual private catalog is created automatically when catalog privileges are granted to the virtual private catalog owner.

```
RMAN> CONNECT CATALOG vpc1@catdb

recovery catalog database Password: password
connected to recovery catalog database

RMAN> REGISTER DATABASE prod1;
RMAN> EXIT;
```