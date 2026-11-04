---
title: CREATE CATALOG
book: Backup and Recovery Reference
doc_id: E10643-09
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta013.htm
tags:
  - oracle
  - 11g
  - backup-and-recovery-reference
---

Purpose

Use the `CREATE CATALOG` command to create a recovery catalog.

The recovery catalog can be a base recovery catalog or a virtual private catalog.

- A base recovery catalog is a database schema that contains RMAN metadata for a set of target databases.
- A virtual private catalog is a set of synonyms and views that enable user access to a subset of a base recovery catalog.

See Also:

- [Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/cd/E11882_01/backup.112/e10642/rcmcatdb.htm#BRADV179) to learn how to create the recovery catalog
- [Appendix B, "RMAN Compatibility"](compat.md) to learn about the requirements for the compatibility of the recovery catalog and the other components of the RMAN environment

Prerequisites

Execute this command only at the RMAN prompt. RMAN must be connected to the recovery catalog database either through the `CATALOG` command-line option or the `CONNECT` `CATALOG` command, and the catalog database must be open. A connection to a target database is not required.

The recovery catalog owner, whether the catalog is a base recovery catalog or a virtual private catalog, must be granted the `RECOVERY_CATALOG_OWNER` role. This user must also be granted space privileges in the tablespace where the recovery catalog tables will reside. The recovery catalog is created in the default tablespace of the recovery catalog owner.

If you are creating a virtual private catalog, then the base recovery catalog owner must have used the RMAN `GRANT` command to grant either the `CATALOG` or `REGISTER` privilege (see Example 2-59).

See the `CONNECT` `CATALOG` description for restrictions for RMAN client connections to a virtual catalog when the RMAN client is from release Oracle Database 10g or earlier.

Usage Notes

Typically, you create the recovery catalog in a database created especially for this purpose. It is not recommended to create the recovery catalog in the `SYS` schema.

The best practice is to create one recovery catalog that serves as the central RMAN repository for many databases. For this reason it is called the base recovery catalog.

The owner of the base recovery catalog can `GRANT` or `REVOKE` restricted access to the catalog to other database users. Each restricted user has full read/write access to his own metadata, which is called a virtual private catalog. The RMAN metadata is stored in the schema of the virtual private catalog owner. The owner of the base recovery catalog controls what each virtual catalog user can access.

You must take an extra step when intending to use a 10.2 or earlier release of RMAN with a virtual catalog. Before using the virtual private catalog, this user must connect to the recovery catalog database as the virtual catalog owner and execute the following PL/SQL procedure (where `base_catalog_owner` is the database user who owns the base recovery catalog):

```
base_catalog_owner.DBMS_RCVCAT.CREATE_VIRTUAL_CATALOG
```

See Also:

[Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/toc.htm) for more information about the `RECOVERY_CATALOG_OWNER` role

Syntax

createCatalog::=

![createcatalog](img/createcatalog.gif)

> **CREATE** \[ **VIRTUAL** \] **CATALOG**
  

Semantics

| Syntax Element | Description |
| --- | --- |
| `VIRTUAL` | Creates a virtual private catalog in an existing recovery catalog.  Run this command after connecting RMAN to the recovery catalog database as the virtual catalog user.  Note: All of the mechanisms for virtual private catalogs are in the recovery catalog schema itself. The security is provided by the catalog database, not by the RMAN client. |

Examples

Example 2-58 Creating a Recovery Catalog and Registering a Database

Assume that you start SQL\*Plus and connect to the recovery catalog `catdb` with administrator privileges. You execute the `CREATE USER` statement as follows, replacing password with a user-specified password (see [Oracle Database Security Guide](https://docs.oracle.com/cd/E11882_01/network.112/e36292/authentication.htm#DBSEG33223) for information on creating secure passwords). The SQL statement creates a user `catowner` in database `catdb` and grant the `catowner` user the `RECOVERY_CATALOG_OWNER` role.

```
SQL> CREATE USER catowner IDENTIFIED BY password
  2  DEFAULT TABLESPACE cattbs
  3  QUOTA UNLIMITED ON cattbs;
SQL> GRANT recovery_catalog_owner TO catowner;
SQL> EXIT
```

You then start RMAN and run the following RMAN commands to connect to the recovery catalog database as `catowner` and create the recovery catalog:

```
RMAN> CONNECT CATALOG catowner@catdb

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

Example 2-59 Creating a Virtual Private Catalog

Assume that you created the recovery catalog and registered a database as shown in Example 2-58. Now you want to create a virtual private catalog for database user `vpc1`. You start SQL\*Plus and connect to recovery catalog database `catdb` with administrator privileges. You create the `vpc1` user and grant recovery catalog ownership as follows, replacing password with a user-specified password (see [Oracle Database Security Guide](https://docs.oracle.com/cd/E11882_01/network.112/e36292/authentication.htm#DBSEG33223) for information on creating secure passwords):

```
SQL> CREATE USER vpc1 IDENTIFIED BY password
  2  DEFAULT TABLESPACE vpcusers
  3  QUOTA UNLIMITED ON vpcusers;
SQL> GRANT recovery_catalog_owner TO vpc1;
SQL> EXIT
```

You then start RMAN and connect to the recovery catalog database as the catalog owner `catowner`. By default, the virtual catalog owner has no access to the base recovery catalog. You use the `GRANT` command to grant virtual private catalog access to `vpc1` for RMAN operations on database `prod1` (but not `prod2`):

```
RMAN> CONNECT CATALOG catowner@catdb
 
recovery catalog database Password: password
connected to recovery catalog database

RMAN> GRANT CATALOG FOR DATABASE prod1 TO vpc1;
RMAN> EXIT;
```

At this point the backup operator who will use virtual private catalog `vpc1` is ready to create the virtual catalog. In the following example, the backup operator connects to the recovery catalog database as `vpc1` and creates the virtual private catalog for `vpc1`

```
RMAN> CONNECT CATALOG vpc1@catdb

recovery catalog database Password: password
connected to recovery catalog database

RMAN> CREATE VIRTUAL CATALOG;
RMAN> EXIT;
```

Because this operator eventually intends to use the virtual catalog with Oracle Database 10g target databases, the operator must execute the `CREATE_VIRTUAL_CATALOG` PL/SQL procedure before using the virtual catalog (as explained in "Usage Notes"). In the following example, the backup operator connects to the recovery catalog database as `vpc1` and executes the PL/SQL procedure as follows:

```
SQL> CONNECT vpc1@catdb
Enter password: password
Connected.
SQL> BEGIN 
  2  catowner.DBMS_RCVCAT.CREATE_VIRTUAL_CATALOG;
  3  END;
  4  /
```