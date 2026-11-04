---
title: Backup and Recovery Reference
book: Database Backup and Recovery Reference
doc_id: F31837-09
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/rcmrf/UPGRADE-CATALOG.html
tags:
  - oracle
  - 21c
  - backup-and-recovery-reference
---

Purpose

Use the `UPGRADE CATALOG` command to upgrade a recovery catalog schema from an older version to the version required by the RMAN client.

Prerequisites

RMAN must be connected to the recovery catalog database, which must be open, as the owner of the recovery catalog. You cannot use the `UPGRADE CATALOG` command while connected to a virtual private catalog (see `CREATE CATALOG` command). Only the base catalog can be upgraded.

The recovery catalog must not already be at a version greater than needed by the RMAN executable; otherwise, RMAN issues an error. RMAN displays all error messages generated during the upgrade in the message log.

The Oracle Database 10gR1 version of the recovery catalog schema requires the `CREATE TYPE` privilege. If you created the recovery catalog owner in a release before 10gR1, and if you granted the `RECOVERY_CATALOG_OWNER` role to this user when the role did not include the `CREATE TYPE` privilege, then you must grant `CREATE TYPE` to this user explicitly before performing the upgrade.

If you are upgrading a recovery catalog to Oracle Database 12c Release 2 (12.2) or higher, then you must run the `dbmsrmansys.sql` script that manages recovery catalog privileges. Additionally, if virtual private catalogs are used, then you must run the `dbmsrmanvpc.sql` script that upgrades virtual private catalogs. Starting with Oracle Database 12c Release 1 (12.1.0.2), the recovery catalog database must use Oracle Database Enterprise Edition.

Usage Notes

RMAN prompts you to enter the `UPGRADE CATALOG` command two consecutive times to confirm the upgrade. To bypass the additional confirmation step, enter the `UPGRADE CATALOG` command with the `NOPROMPT` option while running it the first time.

RMAN permits the command to be run if the recovery catalog is already current so that the packages can be re-created if necessary.

If an upgrade to a base recovery catalog requires changes to an existing virtual private catalog, then RMAN makes these changes automatically the next time RMAN connects to that virtual private catalog.

The `UPGRADE CATALOG` command does not run scripts to perform an upgrade. Instead, RMAN sends various SQL DDL statements to the recovery catalog to update the recovery catalog schema with new tables, views, columns, and so on.

Syntax

upgradeCatalog::=

![upgradecatalog](img/upgradecatalog.gif)

> UPGRADE CATALOG {NOPROMPT | TABLESPACE tablespace\_name NOPROMPT}
>
> ![Oracle Logo](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/gifs/oracle.gif)[  
> Copyright © 2023, 2024, Oracle and/or its affiliates.](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/html/cpyr.htm)


Semantics

NOPROMPT

Bypasses the confirmation step while upgrading the catalog.

TABLESPACE tablespace\_name NOPROMPT

Bypasses the confirmation step while upgrading the specified tablespace.

Example

Example 3-84 Upgrading a Recovery Catalog

This example connects RMAN to recovery catalog database `catdb` and then upgrades it to a more current version:

```
RMAN> CONNECT CATALOG rco@catdb

recovery catalog database Password: password
connected to recovery catalog database 
PL/SQL package RCO.DBMS_RCVCAT version 11.02.00.04 in RCVCAT database is too old

RMAN> UPGRADE CATALOG;

recovery catalog owner is RCO 
enter UPGRADE CATALOG command again to confirm catalog upgrade 

RMAN> UPGRADE CATALOG;

recovery catalog upgraded to version 12.02.00.00
DBMS_RCVMAN package upgraded to version 12.02.00.00
DBMS_RCVCAT package upgraded to version 12.02.00.00
```