---
title: SQL Language Reference
book: SQL Language Reference
doc_id: E83703-08
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/sqlrf/DROP-DIRECTORY.html
tags:
  - oracle
  - 12c
  - sql-language-reference
---

Purpose

Use the `DROP` `DIRECTORY` statement to remove a directory object from the database.

See Also:

[CREATE DIRECTORY](CREATE-DIRECTORY.md) for information on creating a directory

Prerequisites

To drop a directory, you must have the `DROP` `ANY` `DIRECTORY` system privilege.

Note:

Do not drop a directory when files in the associated file system are being accessed by PL/SQL or OCI programs.

Syntax

drop\_directory::=

![drop_directory](img/drop_directory.gif)

> ```
> DROP DIRECTORY directory_name ;
> ```


Semantics

directory\_name

Specify the name of the directory database object to be dropped.

Oracle Database removes the directory object but does not delete the associated operating system directory on the server file system.

Examples

Dropping a Directory: Example

The following statement drops the directory object `bfile_dir`:

```
DROP DIRECTORY bfile_dir;
```

See Also:

" [Creating a Directory: Examples](CREATE-DIRECTORY.md) "