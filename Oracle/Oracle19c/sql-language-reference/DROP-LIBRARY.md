---
title: DROP LIBRARY
book: SQL Language Reference
doc_id: E96310-37
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/DROP-LIBRARY.html
tags:
  - oracle
  - 19c
  - sql-language-reference
---

## Purpose

Use the `DROP` `LIBRARY` statement to remove an external procedure library from the database.

**See Also:** [CREATE LIBRARY](CREATE-LIBRARY.md) for information on creating a library

## Prerequisites

You must have the `DROP` `ANY` `LIBRARY` system privilege.

## Syntax

## drop\_library::=

[Description of the illustration drop\_library.eps](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/img_text/drop_library.html)

## Semantics

## IF EXISTS

Specify `IF EXISTS` to drop an existing library.

## library\_name

Specify the name of the external procedure library being dropped.

## Examples

**Dropping a Library: Example**

The following statement drops the `ext_lib` library:

```md
DROP LIBRARY ext_lib;
```