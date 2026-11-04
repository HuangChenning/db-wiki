---
title: connectStringSpec
book: Backup and Recovery Reference
doc_id: E10643-09
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcmsubcl004.htm
tags:
  - oracle
  - 11g
  - backup-and-recovery-reference
---

Purpose

Use the `connectStringSpec` subclause to specify the user name, password, and net service name for connecting to a target, recovery catalog, or auxiliary database. The connection is necessary to authenticate the user and identify the database.

Prerequisites

You must have `SYSDBA` privileges to `CONNECT` to a target or auxiliary database. Do not connect to the recovery catalog database as user `SYS`.

Usage Notes

RMAN connections to a database are specified and authenticated in the same way as SQL\*Plus connections to a database. The only difference is that RMAN connections to a target or auxiliary database require the `SYSDBA` privilege. The `AS SYSDBA` keywords are implied and cannot be explicitly specified. See [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/dba.htm#ADMIN00102) to learn about database connection options when using SQL\*Plus.

Caution:

Good security practice requires that passwords should not be entered in plain text on the command line. You should enter passwords in RMAN only when requested by an RMAN prompt. See [Oracle Database Security Guide](https://docs.oracle.com/cd/E11882_01/network.112/e36292/authentication.htm#DBSEG0032) to learn about password protection.

Semantics

| Syntax Element | Description |
| --- | --- |
| `/` | If you do not specify a user ID or password when connecting to a target database, then a slash establishes a connection as user `SYS` by using operating system authentication (see Example 4-12).  Note: The slash depends on platform-specific environment variables. |
| `userid` | Establishes a connection to the database for the specified user. If you do not specify a password, then RMAN obtains the password interactively by displaying a prompt (see Example 4-11). The characters are not displayed.  Note: The connect string must not contain any white space, but it can contain punctuation characters such as a slash (`/`) and an at sign (`@`). |
| `/` `password` | Establishes a connection for the specified user by using a password. If the target database is not open, then a password file must exist.  Caution: Passwords entered in plain text on the command line are a security vulnerability. More secure alternatives, such as entering passwords in response to a prompt, are available. |
| `@` `net_service_name` | Establishes a connection to the database through an optional Oracle Net net service name (see Example 4-10). |

Examples

Example 4-10 Connecting to a Target Database Without a Recovery Catalog

This example starts RMAN without specifying a database connection. The `CONNECT` command connects to a target database by using the Oracle Net service name `prod` in the default `NOCATALOG` mode. The `SYS` password is entered in response to a prompt.

```
% rman 
RMAN> CONNECT TARGET SYS@prod

target database Password: password
connected to target database: PROD (DBID=39525561)
```

Example 4-11 Connecting to a Target Database at the Operating System Command Line

This example connects to the target database as user `SYS` at the operating system command line, but without specifying a password. RMAN prompts for the password.

```
% rman TARGET SYS

Recovery Manager: Release 11.1.0.6.0 - Production on Wed Jul 11 17:51:30 2007

Copyright (c) 1982, 2007, Oracle.  All rights reserved.

target database Password: password
```

Example 4-12 Connecting to a Target Database with Operating System Authentication

This example starts RMAN and then connects to the target database `prod` using operating system authentication. The example also connects to the recovery catalog database `catdb` using a net service name.

```
% rman
RMAN> CONNECT TARGET /

connected to target database: PROD (DBID=39525561)

RMAN> CONNECT CATALOG rman@catdb

recovery catalog database Password: password
connected to recovery catalog database
```