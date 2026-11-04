---
title: DROP LIBRARY
book: SQL Language Reference
doc_id: E41084-04
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_8020.htm
tags:
  - oracle
  - 11g
  - sql-language-reference
---

Purpose

Use the `DROP` `LIBRARY` statement to remove an external procedure library from the database.

See Also:

[CREATE LIBRARY](statements_6001.md) for information on creating a library

Prerequisites

You must have the `DROP` `ANY` `LIBRARY` system privilege.

Syntax

drop\_library::=

  
[Description of the illustration ''drop\_library.gif''](https://docs.oracle.com/cd/E11882_01/server.112/e41084/img_text/drop_library.htm)  

Semantics

library\_name

Specify the name of the external procedure library being dropped.

Examples

Dropping a Library: Example The following statement drops the `ext_lib` library:

```
DROP LIBRARY ext_lib;
```