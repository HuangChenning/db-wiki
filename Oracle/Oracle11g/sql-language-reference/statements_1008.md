---
title: ALTER FLASHBACK ARCHIVE
book: SQL Language Reference
doc_id: E41084-04
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_1008.htm
tags:
  - oracle
  - 11g
  - sql-language-reference
---

Purpose

Use the `ALTER` `FLASHBACK` `ARCHIVE` statement for these operations:

- Designate a flashback data archive as the default flashback data archive for the system
- Add a tablespace for use by the flashback data archive
- Change the quota of a tablespace used by the flashback data archive
- Remove a tablespace from use by the flashback data archive
- Change the retention period of the flashback data archive
- Purge the flashback data archive of old data that is no longer needed

See Also:

Oracle Database Advanced Application Developer's Guide and [CREATE FLASHBACK ARCHIVE](statements_5010.md) for more information on using flashback data archives

Prerequisites

You must have the `FLASHBACK` `ARCHIVE` `ADMINISTER` system privilege to alter a flashback data archive in any way. You must also have appropriate privileges on the affected tablespaces to add, modify, or remove a flashback data archive tablespace.

Syntax

alter\_flashback\_archive::=

![alter_flashback_archive](img/alter_flashback_archive.gif)

> ```
> ALTER FLASHBACK ARCHIVE flashback_archive
>   { SET DEFAULT
>   | { ADD | MODIFY } TABLESPACE tablespace [flashback_archive_quota]
>   | REMOVE TABLESPACE tablespace_name
>   | MODIFY RETENTION flashback_archive_retention
>   | PURGE { ALL | BEFORE { SCN expr | TIMESTAMP expr } }
>   | [NO] OPTIMIZE DATA
>   };
> ```
  
  

flashback\_archive\_quota::=

![flashback_archive_quota](img/flashback_archive_quota.gif)

> ```
> QUOTA integer { M | G | T | P | E }
> ```
  
  

flashback\_archive\_retention::=

![flashback_archive_retention](img/flashback_archive_retention.gif)

> ```
> RETENTION integer {YEAR | MONTH | DAY}
> ```
  

Semantics

flashback\_archive

Specify the name of an existing flashback data archive.

SET DEFAULT

You must be logged in as `SYSDBA` to specify this clause. Use this clause to designate this flashback data archive as the default flashback data archive for the system. When a `CREATE` `TABLE` or `ALTER` `TABLE` statement specifies the `flashback_archive_clause` without specifying a flashback data archive name, the database uses the default flashback data archive to store data from that table.

This statement overrides any previous designation of a different flashback data archive as the default.

See Also:

The `CREATE` `TABLE` [flashback\_archive\_clause](statements_7002.md) for more information

ADD TABLESPACE

Use this clause to add a tablespace to the flashback data archive. You can use the `flashback_archive_quota` clause to specify the amount of space that can be used by the flashback data archive in the new tablespace. If you omit that clause, then the flashback data archive has unlimited space in the newly added tablespace.

MODIFY TABLESPACE

Use this clause to change the tablespace quota of a tablespace already used by the flashback data archive.

REMOVE TABLESPACE

Use this clause to remove a tablespace from use by the flashback data archive. You cannot remove the last remaining tablespace used by the flashback data archive.

If the tablespace to be removed contains any data within the retention period of the flashback archive, then that data will be dropped as well. Therefore, you should move your data to another tablespace before removing the tablespace with this clause.

MODIFY RETENTION

Use this clause to change the retention period of the flashback data archive.

PURGE

Use this clause to purge data from the flashback data archive.

- Specify `PURGE` `ALL` to remove all data from the flashback data archive. This historical information can be retrieved using a flashback query only if the SCN or timestamp specified in the flashback query is within the undo retention duration.
- Specify `PURGE` `BEFORE` `SCN` to remove all data from the flashback data archive before the specified system change number.
- Specify `PURGE` `BEFORE` `TIMESTAMP` to remove all data from the flashback data archive before the specified timestamp.

\[NO\] OPTIMIZE DATA

This clause has the same semantics as the [\[NO\] OPTIMIZE DATA](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_5010.htm#BGEBGFCA) clause of `CREATE` `FLASHBACK` `ARCHIVE`.

See Also:

[CREATE FLASHBACK ARCHIVE](statements_5010.md) for information on creating flashback data archives and for some simple examples of using flashback data archives