---
title: Backup and Recovery Reference
book: Database Backup and Recovery Reference
doc_id: F31837-09
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/rcmrf/CONNECT.html
tags:
  - oracle
  - 21c
  - backup-and-recovery-reference
---

Purpose

Use the `CONNECT` command to establish a connection between RMAN and a target, auxiliary, or recovery catalog database.

Prerequisites

RMAN connections to a database are specified and authenticated in the same way as SQL\*Plus connections to a database. The only difference is that RMAN connections to a target or auxiliary database require the `SYSBACKUP` or `SYSDBA` privilege.

To connect to the CDB, you connect to the root as a common user with the `SYSDBA` or `SYSBACKUP` privilege.

To connect to a PDB, you can connect either as a common user or a local user. The user creating the connection must have the privileges described in " [connectStringSpec](connectStringSpec.md) ".

See Also:

- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/rcmrf&id=ADMIN-GUID-7842AF72-DA25-4559-A8E7-9883D0C63BF2) to learn about database connection options when using SQL\*Plus
- [Oracle Database Backup and Recovery User’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/rcmrf&id=BRADV8123) to learn about using the `SYSBACKUP` administrative privilege

Caution:

Good security practice requires that passwords are not entered in plain text on the command line. Enter passwords in RMAN only when requested by an RMAN prompt. See [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/rcmrf&id=DBSEG0032) to learn about password protection.

See Also:

`RMAN` for command-line connection options

You can only run the `CONNECT TARGET`, `CONNECT CATALOG`, and `CONNECT AUXILIARY` commands at the RMAN prompt and only if RMAN is not already connected to the databases specified by these commands. To connect to a different target, catalog, or auxiliary database you must start a new RMAN session.

Usage Notes

To perform operations on the whole CDB, the root, or multiple PDBs, you connect as `TARGET` to the root and as a common user with the `SYSDBA` or `SYSBACKUP` privilege. To perform operations on a single PDB, you can connect as `TARGET` either to the root or to the PDB and as a local user or common user with the `SYSDBA` or `SYSBACKUP` privilege.

An RMAN session runs in `NOCATALOG` mode by default if all of the following conditions are met:

- You did not specify `CATALOG` or `NOCATALOG` when you started `RMAN`.
- You have not yet run `CONNECT CATALOG` in an RMAN session.
- You run a command such as `BACKUP` that requires an RMAN repository connection (as shown in Example 2-62).

See Also:

- [Oracle Database Concepts](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/rcmrf&id=CNCPT89234) for information about multitenant architecture concepts
- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/rcmrf&id=MULTI-GUID-2E5025EE-BED3-45A4-9EAA-B05C8DA66F97) for information about managing a multitenant environment

See Also:

[Oracle Database Backup and Recovery User’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/rcmrf&id=BRADV-GUID-E07231B2-F213-4F8F-8D02-E410A6DAE94C) for additional information about connecting to CDBs and PDBs

Syntax

connect::=

![connect](img/connect.gif)

> {CONNECT AUXILIARY | CONNECT CATALOG} connectStringSpec | CONNECT TARGET connectStringSpec
>
> ![Oracle Logo](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/gifs/oracle.gif)[  
> Copyright © 2023, 2024, Oracle and/or its affiliates.](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/html/cpyr.htm)


([connectStringSpec::=](connectStringSpec.md))

Semantics

| Syntax Element | Description |
| --- | --- |
| `CONNECT AUXILIARY` | Establishes a connection between RMAN and an auxiliary database instance.  Auxiliary instances are used with the `TRANSPORT TABLESPACE` and `DUPLICATE` commands, and during RMAN TSPITR. |
| `CONNECT CATALOG` | Establishes a connection between RMAN and a recovery catalog database.  If the recovery catalog is a virtual private catalog (see `CREATE CATALOG`), then the RMAN client connecting to this catalog must be at patch level 10.1.0.6 or 10.2.0.3. Oracle9i RMAN clients cannot connect to a virtual private catalog. This version restriction does not affect RMAN client connections to an Oracle Database 11g base recovery catalog, even if it has some virtual private catalog users.  RMAN issues an `RMAN-06445` error if you attempt to use the `CONNECT CATALOG` command in an RMAN session when RMAN is in the default `NOCATALOG` mode (see " Usage Notes ").  Note: You must use RMAN with a recovery catalog in a Data Guard environment. |
| `CONNECT TARGET` | Establishes a connection between RMAN and a target database.  Note: RMAN can connect to physical standby databases as `TARGET` in a Data Guard environment. If you run `CONNECT TARGET` for a database that has a `DB_UNIQUE_NAME` that is unknown to the recovery catalog, but the DBID identifies a registered database, then RMAN automatically and implicitly registers the database in the recovery catalog. |
| `connectStringSpec` | Specifies the connection information for the database. |

Examples

Example 2-61 Connecting to a Target Database Without a Recovery Catalog

This example starts RMAN in `NOCATALOG` mode and then connects to the target database with an Oracle Net service name `prod1`. `sbu` is a user who is granted the `SYSBACKUP` privilege.

```
% rman NOCATALOG
RMAN> CONNECT TARGET "sbu@prod1 AS SYSBACKUP";

target database Password: password
connected to target database: PROD1 (DBID=39525561)
```

Example 2-62 Connecting to a Target Database in the Default NOCATALOG Mode

This example starts RMAN without specifying either `CATALOG` or `NOCATALOG` and then uses operating system authentication to connect to a target database with operating system authentication. Because no `CONNECT CATALOG` command has been run, RMAN defaults to `NOCATALOG` mode when you run the `BACKUP` command.

```
% rman
RMAN> CONNECT TARGET /
RMAN> BACKUP DATABASE;
```

At this point in the RMAN session, you cannot run `CONNECT CATALOG` because the session has defaulted to `NOCATALOG` mode. An attempt to connect to the catalog in this session receives an error:

```
RMAN> CONNECT CATALOG rco@catdb

RMAN-00571: ===========================================================
RMAN-00569: =============== ERROR MESSAGE STACK FOLLOWS ===============
RMAN-00571: ===========================================================
RMAN-06445: cannot connect to recovery catalog after NOCATALOG has been used
```

Example 2-63 Connecting to Target, Recovery Catalog, and Auxiliary Databases

This example connects to a target database with operating system authentication and connects to the recovery catalog and auxiliary databases with password files. `sbu` is a user who is granted the `SYSBACKUP` privilege. RMAN prompts for the password.

```
% rman
RMAN> CONNECT TARGET;

connected to target database: PROD (DBID=39525561)

RMAN> CONNECT CATALOG rco@catdb;
 
recovery catalog database Password: password
connected to recovery catalog database

RMAN> CONNECT AUXILIARY "sbu@dupdb AS SYSBACKUP";

auxiliary database Password: password
connected to auxiliary database: DUPDB (not mounted)
```

Example 2-64 Connecting to the Root Using Operating System Authentication

This example connects to the root in a CDB using operating system authentication. By default, the connection is established using `SYSDBA` privilege.

```
%rman
RMAN> CONNECT TARGET /
```

Example 2-65 Connecting to a PDB as a Local User

This example connects to the PDB `hr_pdb` as the local user `sbu_pdb` who is granted the `SYSBACKUP` privilege on the `hr_pdb` PDB. `hrpdb` is the net service name corresponding to the PDB `hr_pdb`.

```
%rman
RMAN> CONNECT TARGET "sbu_pdb@hrpdb AS SYSBACKUP";
```