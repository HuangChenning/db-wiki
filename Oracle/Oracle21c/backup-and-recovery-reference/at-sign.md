---
title: Backup and Recovery Reference
book: Database Backup and Recovery Reference
doc_id: F31837-09
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/rcmrf/at-sign.html
tags:
  - oracle
  - 21c
  - backup-and-recovery-reference
---

Purpose

Use the `@` command to execute a series of RMAN commands stored in an operating system file with the specified path name.

Note:

The file must contain complete RMAN commands. Partial commands generate syntax errors.

Prerequisites

The command file must contain complete RMAN commands.

If you use the `@` command within a `RUN` command, then the `@` command must be on its own line (see Example 2-2).

Usage Notes

RMAN processes the file as though its contents were entered instead of the @ command. As shown in Example 2-3, you can specify substitution variables in a command file and then pass values to the command file during execution.

See Also:

`RMAN` to learn more about using substitution variables in RMAN

Syntax

@::=

![GUID-B4267AFF-0B73-48BA-8226-020F1131CF51-default](img/GUID-B4267AFF-0B73-48BA-8226-020F1131CF51-default.gif)

> @ filename
>
> ![Oracle Logo](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/gifs/oracle.gif)[  
> Copyright © 2023, 2024, Oracle and/or its affiliates.](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/html/cpyr.htm)


Semantics

| Syntax Element | Description |
| --- | --- |
| `filename` | Specifies the name of a command file, for example, `@/oracle/dbs/cmd/cmd1.rman`. If you do not specify the absolute path name, then the current working directory is assumed, for example, `@cmd1.rman`.  Any file extension (or no file extension) is valid. Do not use quotes around the string or leave whitespace between the `@` keyword and the file name. |

Examples

Example 2-1 Running a Command File from the Operating System Command Line

This example creates an RMAN command file and then executes it from the operating system command line.

```
% echo "BACKUP DATABASE;" > backup_db.rman
% rman TARGET / @backup_db.rman
```

Example 2-2 Running a Command File Within RMAN

This example shows how you can execute a command file from the RMAN prompt and from within a `RUN` command. User-entered text appears in bold.

```
RMAN> @backup_db.rman
RMAN> RUN {
2> @backup_db.rman
3> backup database;
4> **end-of-file**
5> }
```

Example 2-3 Specifying Substitution Variables

Suppose that you use a text editor to create command file `whole_db.rman` with the following contents:

```
# name: whole_db.rman
BACKUP TAG &1 COPIES &2 DATABASE;
EXIT;
```

The following example starts RMAN from the operating system prompt and connects to the target database. The example then runs the `@` command, passing variables to the command file to create two database backups with tag `Q106`:

```
% rman TARGET /
RMAN> @/tmp/whole_db.rman Q106 2
```