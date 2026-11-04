---
title: Backup and Recovery Reference
book: Database Backup and Recovery Reference
doc_id: F31837-09
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/rcmrf/SQL-Quoted.html
tags:
  - oracle
  - 21c
  - backup-and-recovery-reference
---

Purpose

The `SQL` command executes a SQL statement or a PL/SQL stored procedure from within RMAN. This syntax is available for compatibility with Oracle Database Release 11.2 and earlier, but for ease of use, refer to `SQL`.

See Also:

[Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/rcmrf&id=SQLRF-GUID-04D8EBB3-583D-4969-8344-E221000E9CD9)

Prerequisites

None.

Syntax

quotedsqlcommand::=

![quotedsqlcommand](img/quotedsqlcommand.gif)

> SQL \[CHANNEL \['\] channel\_id \['\]\] ' command '
>
> ![Oracle Logo](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/gifs/oracle.gif)[  
> Copyright © 2023, 2024, Oracle and/or its affiliates.](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/html/cpyr.htm)


Semantics

| Syntax Element | Description |
| --- | --- |
| `CHANNEL` `channel_id` | Specifies the case-sensitive name of a channel to use when executing an RMAN command within a `RUN` command.  The channel must first be allocated by `ALLOCATE CHANNEL` in this `RUN` command. If you do not set this parameter, then RMAN uses the default channel. |
| `'` `command` `'` | Specifies a SQL statement for execution (see Example 3-71). `SELECT` statements are not permitted.  You must use duplicate single quotes to insert a single quote into a quoted string when the quoted string uses the same style of quoting. For example, if the string that RMAN passes to SQL contains a file name, then the file name must be enclosed in duplicate single quotes and the entire string following the `SQL` keyword must be enclosed in double quotes (see Example 3-72).  Note: Because `EXECUTE` is a SQL\*Plus command, you cannot execute a PL/SQL program unit by specifying `EXECUTE` within the RMAN `SQL` command. Instead, you must use the `BEGIN` and `END` keywords. For example, to execute the PL/SQL procedure `rman.rman_purge` with the `SQL` command, issue the following command:  ``` SQL 'BEGIN rman.rman_purge; END;'; ``` |

Examples

Example 3-71 Archiving the Unarchived Online Logs

This example backs up a tablespace and then archives all unarchived online redo logs.

```
BACKUP TABLESPACE users;
sql 'ALTER SYSTEM ARCHIVE LOG CURRENT';
```

Example 3-72 Specifying a File Name Within a Quoted String

This example specifies a file name by using duplicate single quotes within a double-quoted string.

```
sql 'ALTER TABLESPACE users ADD DATAFILE ''/disk1/oradata/users02.dbf'' 
  SIZE 100K AUTOEXTEND ON NEXT 10K MAXSIZE 100K';
```