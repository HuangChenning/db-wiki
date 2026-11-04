---
title: DROP LIBRARY Statement
book: PL/SQL Language Reference
doc_id: E25519-13
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e25519/drop_library.htm
tags:
  - oracle
  - 11g
  - pl-sql-language-reference
---

The `DROP` `LIBRARY` statement drops an external procedure library from the database.

Topics

Prerequisites

You must have the `DROP` `ANY` `LIBRARY` system privilege.

Syntax

drop\_library::=

  
[Description of the illustration drop\_library.gif](https://docs.oracle.com/cd/E11882_01/appdev.112/e25519/img_text/drop_library.htm)  

Semantics

library\_name

Name of the external procedure library being dropped.

Example

Dropping a Library: Example The following statement drops the `ext_lib` library, which was created in ["Creating a Library: Examples"](create_library.md):

```
DROP LIBRARY ext_lib;
```