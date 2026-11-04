---
title: DROP DIRECTORY
book: SQL Language Reference
doc_id: E96310-37
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/DROP-DIRECTORY.html
tags:
  - oracle
  - 19c
  - sql-language-reference
---

## Purpose

Use the `DROP` `DIRECTORY` statement to remove a directory object from the database.

**See Also:** [CREATE DIRECTORY](CREATE-DIRECTORY.md) for information on creating a directory

## Prerequisites

To drop a directory, you must have the `DROP` `ANY` `DIRECTORY` system privilege.

**Note:** Do not drop a directory when files in the associated file system are being accessed by PL/SQL or OCI programs.

## Syntax

## drop\_directory::=

[Description of the illustration drop\_directory.eps](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/img_text/drop_directory.html)

## Semantics

## IF EXISTS

Specify `IF EXISTS` to drop an existing directory.

**Note:** You can only use `IF EXISTS` from Release 19.28 and up.

## directory\_name

Specify the name of the directory database object to be dropped.

Oracle Database removes the directory object but does not delete the associated operating system directory on the server file system.

## Examples

**Dropping a Directory: Example**

The following statement drops the directory object `bfile_dir`:

```md
DROP DIRECTORY bfile_dir;
```

**See Also:** “ [Creating a Directory: Examples](CREATE-DIRECTORY.md) ”