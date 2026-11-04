---
title: SQL Language Reference
book: SQL Language Reference
doc_id: F31301-19
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/sqlrf/DROP-DIRECTORY.html
tags:
  - oracle
  - 21c
  - sql-language-reference
---

## DROP DIRECTORY

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
>
> ![Oracle Logo](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/gifs/oracle.gif)[  
> Copyright © 1996, 2025, Oracle and/or its affiliates.](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/html/cpyr.htm)


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