---
title: SQL Language Reference
book: SQL Language Reference
doc_id: F31301-19
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/sqlrf/ALTER-HIERARCHY.html
tags:
  - oracle
  - 21c
  - sql-language-reference
---

## ALTER HIERARCHY

Purpose

Use the `ALTER` `HIERARCHY` statement to rename or compile a hierarchy. For other alterations, use `CREATE` `OR` `REPLACE` `HIERARCHY`.

Prerequisites

To alter a hierarchy in your own schema, you must have the `ALTER` `HIERARCHY` system privilege. To alter a hierarchy in another user's schema, you must have the `ALTER` `ANY` `HIERARCHY` system privilege or have been granted `ALTER` directly on the hierarchy.

Syntax

alter\_hierarchy::=

![alter_hierarchy](img/alter_hierarchy.gif)

> ```
> ALTER HIERARCHY [ schema. ] hierarchy_name 
>   { RENAME TO new_hier_name | COMPILE };
> ```
>
> ![Oracle Logo](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/gifs/oracle.gif)[  
> Copyright © 1996, 2025, Oracle and/or its affiliates.](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/html/cpyr.htm)


Semantics

schema

Specify the schema in which the hierarchy exists. If you do not specify a schema, then Oracle Database looks for the hierarchy in your own schema.

hierarchy\_name

Specify the name of the hierarchy.

RENAME TO

Specify `RENAME` `TO` to change the name of the hierarchy.

COMPILE

Specify `COMPILE` to compile the hierarchy.

new\_hier\_name

Specify a new name for the hierarchy.

Example

The following statement changes the name of a hierarchy:

```
ALTER HIERARCHY product_hier RENAME TO myproduct_hier;
```