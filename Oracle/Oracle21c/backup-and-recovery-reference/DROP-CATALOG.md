---
title: Backup and Recovery Reference
book: Database Backup and Recovery Reference
doc_id: F31837-09
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/rcmrf/DROP-CATALOG.html
tags:
  - oracle
  - 21c
  - backup-and-recovery-reference
---

Purpose

Use the `DROP CATALOG` command to remove the recovery catalog.

See Also:

[Oracle Database Backup and Recovery User’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/rcmrf&id=BRADV189) to learn how to drop the recovery catalog

Prerequisites

Execute this command only at the RMAN prompt.

You must be connected to the recovery catalog schema with the `CATALOG` command-line option or the `CONNECT` `CATALOG` command. The recovery catalog database must be open.

You do not have to be connected to a target database.

Usage Notes

After you execute `DROP CATALOG`, RMAN prompts you to enter the command again to confirm that you want to perform the operation.

To bypass the command confirmation step, execute the `DROP CATALOG` command with the `NOPROMPT` option when you run it the first time.

A base recovery catalog is created with `CREATE CATALOG`. To drop the base recovery catalog, execute `DROP CATALOG` while connected to the recovery catalog database as the recovery catalog owner.

Note:

When you drop the base recovery catalog, all RMAN metadata is removed from the recovery catalog. Any backups recorded in the recovery catalog but not in a target database control are not usable by RMAN.

When connected to a virtual private catalog, the `DROP CATALOG` command does not remove the base recovery catalog itself, but only drops the security policies that are used to restrict user access to the base catalog..

Syntax

dropCatalog::=

![dropcatalog](img/dropcatalog.gif)

> DROP CATALOG \[NOPROMPT\]
>
> ![Oracle Logo](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/gifs/oracle.gif)[  
> Copyright © 2023, 2024, Oracle and/or its affiliates.](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/html/cpyr.htm)


Semantics

NOPROMPT

Bypasses the confirmation step while dropping a catalog.