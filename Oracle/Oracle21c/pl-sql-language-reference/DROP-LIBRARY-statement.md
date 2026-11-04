---
title: Database PL/SQL Language Reference
book: Database PL/SQL Language Reference
doc_id: F31827-07
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/lnpls/DROP-LIBRARY-statement.html
tags:
  - oracle
  - 21c
  - pl-sql-language-reference
---

The `DROP` `LIBRARY` statement drops an external procedure library from the database.

Topics

Prerequisites

You must have the `DROP` `ANY` `LIBRARY` system privilege.

Syntax

drop\_library::=

![drop_library](img/drop_library.gif)

> ```
> DROP LIBRARY library_name ;
> ```
>
> ![Oracle Logo](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/gifs/oracle.gif)[  
> Copyright © 1996, 2024, Oracle and/or its affiliates.](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/html/cpyr.htm)


Semantics

library\_name

Name of the external procedure library being dropped.

Example

Example 15-36 Dropping a Library

The following statement drops the `ext_lib` library, which was created in " [CREATE LIBRARY Statement](CREATE-LIBRARY-statement.md) ":

```
DROP LIBRARY ext_lib;
```