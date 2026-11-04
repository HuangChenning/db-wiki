---
title: DROP DIRECTORY
book: SQL Language Reference
doc_id: E41084-04
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_8012.htm
tags:
  - oracle
  - 11g
  - sql-language-reference
---

Purpose

Use the `DROP` `DIRECTORY` statement to remove a directory object from the database.

See Also:

[CREATE DIRECTORY](statements_5007.md) for information on creating a directory

Prerequisites

To drop a directory, you must have the `DROP` `ANY` `DIRECTORY` system privilege.

Caution:

Do not drop a directory when files in the associated file system are being accessed by PL/SQL or OCI programs.

Syntax

drop\_directory::=

  
[Description of the illustration ''drop\_directory.gif''](https://docs.oracle.com/cd/E11882_01/server.112/e41084/img_text/drop_directory.htm)  

Semantics

directory\_name

Specify the name of the directory database object to be dropped.

Oracle Database removes the directory object but does not delete the associated operating system directory on the server file system.

Examples

Dropping a Directory: Example The following statement drops the directory object `bfile_dir`:

```
DROP DIRECTORY bfile_dir;
```

See Also:

["Creating a Directory: Examples"](statements_5007.md)