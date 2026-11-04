---
title: DROP CATALOG
book: Backup and Recovery Reference
doc_id: E10643-09
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsynta018.htm
tags:
  - oracle
  - 11g
  - backup-and-recovery-reference
---

Purpose

Use the `DROP CATALOG` command to remove the recovery catalog or a virtual private catalog.

See Also:

[Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/cd/E11882_01/backup.112/e10642/rcmcatdb.htm#BRADV189) to learn how to drop the recovery catalog

Prerequisites

Execute this command only at the RMAN prompt.

You must be connected to the recovery catalog schema or virtual private catalog schema with the `CATALOG` command-line option or the `CONNECT` `CATALOG` command. The recovery catalog database must be open.

You do not have to be connected to a target database.

Usage Notes

After you execute `DROP CATALOG`, RMAN prompts you to enter the command again to confirm that you want to perform the operation.

A base recovery catalog is created with `CREATE CATALOG`, whereas a virtual private catalog is created with `CREATE VIRTUAL CATALOG`. To drop the base recovery catalog, execute `DROP CATALOG` while connected to the recovery catalog database as the recovery catalog owner.

Caution:

When you drop the base recovery catalog, all RMAN metadata is removed from the recovery catalog. Any backups recorded in the recovery catalog but not in a target database control are not usable by RMAN.

To drop a virtual private catalog, execute the `DROP CATALOG` command while connected to the virtual private catalog. When connected to a virtual private catalog, the `DROP CATALOG` command does not remove the base recovery catalog itself, but only drops the synonyms and views that refer to the base catalog.

You must use a different technique to drop a virtual catalog when using a 10.2 or earlier release of the RMAN client. Before dropping the virtual private catalog, the user must connect to the recovery catalog database as the virtual private catalog owner and execute the following PL/SQL procedure (where `base_catalog_owner` is the database user who owns the base recovery catalog):

```
base_catalog_owner.DBMS_RCVCAT.DROP_VIRTUAL_CATALOG
```

If you drop the base recovery catalog but not the virtual private catalog, then the virtual catalog is unusable. However, if a dedicated database user owns the virtual private catalog, then you can execute `DROP USER ... CASCADE` to remove the virtual catalog.

Syntax

dropCatalog::=

![dropcatalog](img/dropcatalog.gif)

> **DROP CATALOG;**
  

Example

Example 2-70 Dropping a Virtual Private Catalog

Assume that you want to remove the virtual private catalog belonging to database user `vpu1`, but do not want to drop the base recovery catalog. This example connects to the recovery catalog database as `vpu1` and drops the virtual private catalog for this user. The base recovery catalog is not affected by the removal of this virtual private catalog.

```
RMAN> CONNECT CATALOG vpu1@catdb

recovery catalog database Password: password
connected to recovery catalog database
 
RMAN> DROP CATALOG;
 
recovery catalog owner is VPU1
enter DROP CATALOG command again to confirm catalog removal
 
RMAN> DROP CATALOG;
 
virtual catalog dropped
```