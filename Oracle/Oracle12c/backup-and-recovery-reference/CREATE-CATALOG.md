---
title: Database Backup and Recovery Reference
book: Database Backup and Recovery Reference
doc_id: E85640-04
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/rcmrf/CREATE-CATALOG.html
tags:
  - oracle
  - 12c
  - backup-and-recovery-reference
---

Purpose

Use the `CREATE CATALOG` command to create a recovery catalog.

The recovery catalog can be a base recovery catalog or a virtual private catalog. In Oracle Database 12c Release 1 (12.1.0.1), you must explicitly use the `CREATE VIRTUAL CATALOG` command to create a virtual private catalog. In Oracle Database 12c Release 1 (12.1.0.2), the virtual private catalog is created automatically when catalog privileges are granted to the virtual private catalog owner.

- A base recovery catalog is a database schema that contains RMAN metadata for a set of target databases.
- A virtual private catalog is a set of security policies that restrict user access to a subset of a base recovery catalog.

See Also:

- [Oracle Database Backup and Recovery User's Guide](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/rcmrf&id=BRADV179) to learn how to create the recovery catalog
- [RMAN Compatibility](rman-compatibility.md) to learn about the requirements for the compatibility of the recovery catalog and the other components of the RMAN environment

Prerequisites

Execute this command only at the RMAN prompt. RMAN must be connected to the recovery catalog database either through the `CATALOG` command-line option or the `CONNECT` `CATALOG` command, and the catalog database must be open. A connection to a target database is not required.

The recovery catalog owner for the base recovery catalog must be granted the `RECOVERY_CATALOG_OWNER` role. The recovery catalog is created in the default tablespace of the recovery catalog owner.

Note:

Starting with Oracle Database 12c Release 1 (12.1.0.2), the recovery catalog database must use the Enterprise Edition.

In Oracle Database 12c Release 1 (12.1.0.1), the database user who owns the virtual private catalogs must be granted the `RECOVERY_CATALOG_OWNER` role. This user must also be granted space privileges in the tablespace where the recovery catalog tables will reside. In Oracle Database 12c Release 1 (12.1.0.2), it is sufficient to grant the `CREATE SESSION` privilege to the database user who owns the virtual private catalogs. Starting with Oracle Database 12c Release 1 (12.1.0.2), virtual private catalogs can be created only when using Oracle Database Enterprise Edition.

If you are creating a virtual private catalog, then the base recovery catalog owner must have used the RMAN `GRANT` command to grant either the `CATALOG` or `REGISTER` privilege (see Example 2-71).

See the `CONNECT` `CATALOG` description for restrictions for RMAN client connections to a virtual catalog when the RMAN client is from release Oracle Database 10g or earlier.

Usage Notes

Typically, you create the recovery catalog in a database created especially for this purpose. Do not create the recovery catalog in a privileged schema such as `SYS` or `SYSBACKUP`.

The best practice is to create one recovery catalog that serves as the central RMAN repository for many databases. For this reason it is called the base recovery catalog.

The owner of the base recovery catalog can `GRANT` or `REVOKE` restricted access to the catalog to other database users. Each restricted user has full read/write access to his own metadata, which is called a virtual private catalog. The RMAN metadata is stored in the schema of the virtual private catalog owner. The owner of the base recovery catalog controls what each virtual catalog user can access.

You must take an extra step when intending to use a 10.2 or earlier release of RMAN with a virtual catalog. Before using the virtual private catalog, this user must connect to the recovery catalog database as the virtual catalog owner and execute the following PL/SQL procedure (where `base_catalog_owner` is the database user who owns the base recovery catalog):

```
base_catalog_owner.DBMS_RCVCAT.CREATE_VIRTUAL_CATALOG
```

Syntax

createCatalog::=

![createcatalog](img/createcatalog.gif)

> CREATE \[VIRTUAL\] CATALOG


Semantics

| Syntax Element | Description |
| --- | --- |
| `VIRTUAL` | Creates a virtual private catalog in an existing recovery catalog.  Run this command after connecting RMAN to the recovery catalog database as the virtual catalog user.  Note: All of the mechanisms for virtual private catalogs are in the recovery catalog schema itself. The security is provided by the catalog database, not by the RMAN client. |

Examples

Example 2-70 Creating a Recovery Catalog and Registering a Database

Assume that you start SQL\*Plus and connect to the recovery catalog `catdb` with administrator privileges. You execute the `CREATE USER` statement as follows, replacing password with a user-specified password (see [Oracle Database Security Guide](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/rcmrf&id=DBSEG33223) for information on creating secure passwords). The SQL statement creates a user `rco` in database `catdb` and grant the `rco` user the `RECOVERY_CATALOG_OWNER` role.

```
SQL> CREATE USER rco IDENTIFIED BY password
  2  DEFAULT TABLESPACE cattbs
  3  QUOTA UNLIMITED ON cattbs;
SQL> GRANT recovery_catalog_owner TO rco;
SQL> EXIT
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

Example 2-71 Creating a Virtual Private Catalog

Assume that you created the recovery catalog and registered a database as shown in Example 2-70. Now you want to create a virtual private catalog for database user `vpc1`. The database version is Oracle Database 12c Release 1 (12.1.0.2). You start SQL\*Plus and connect to recovery catalog database `catdb` with administrator privileges. You create the `vpc1` user and grant recovery catalog ownership as follows, replacing password with a user-specified password (see [Oracle Database Security Guide](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/rcmrf&id=DBSEG33223) for information on creating secure passwords):

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

Because this operator eventually intends to use the virtual catalog with Oracle Database 10g target databases, the operator must execute the `CREATE_VIRTUAL_CATALOG` PL/SQL procedure before using the virtual catalog (as explained in " Usage Notes "). In the following example, the backup operator connects to the recovery catalog database as `vpc1` and executes the PL/SQL procedure as follows:

```
SQL> CONNECT vpc1@catdb
Enter password: password
Connected.
SQL> BEGIN 
  2  rco.DBMS_RCVCAT.CREATE_VIRTUAL_CATALOG;
  3  END;
  4  /
```