---
title: SQL Language Reference
book: SQL Language Reference
doc_id: E83703-08
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/sqlrf/DROP-HIERARCHY.html
tags:
  - oracle
  - 12c
  - sql-language-reference
---

Purpose

Use the `DROP` `HIERARCHY` statement to drop a hierarchy. A `HIERARCHY` object is a component of analytic views.

Prerequisites

To drop a hierarchy in your own schema, you must have the `DROP` `HIERARCHY` system privilege. To drop a hierarchy in another user's schema, you must have the `DROP` `ANY` `HIERARCHY` system privilege.

Syntax

drop\_hierarchy::=

![drop_hierarchy](img/drop_hierarchy.gif)

> ```
> DROP HIERARCHY [ schema. ] hierarchy_name;
> ```


Semantics

schema

Specify the schema in which the hierarchy exists. If you do not specify a schema, then Oracle Database looks for the hierarchy in your own schema.

hierarchy\_name

Specify the name of the hierarchy to drop.

Example

The following statement drops the specified hierarchy object:

```
DROP HIERARCHY product_hier;
```