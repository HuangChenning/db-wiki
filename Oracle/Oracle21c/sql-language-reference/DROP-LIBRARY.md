---
title: SQL Language Reference
book: SQL Language Reference
doc_id: F31301-19
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/sqlrf/DROP-LIBRARY.html
tags:
  - oracle
  - 21c
  - sql-language-reference
---

## DROP LIBRARY

Purpose

Use the `DROP` `LIBRARY` statement to remove an external procedure library from the database.

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
> Copyright © 1996, 2025, Oracle and/or its affiliates.](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/html/cpyr.htm)


Semantics

library\_name

Specify the name of the external procedure library being dropped.

Examples

Dropping a Library: Example

The following statement drops the `ext_lib` library:

```
DROP LIBRARY ext_lib;
```