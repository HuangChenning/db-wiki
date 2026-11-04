---
title: DROP HIERARCHY
book: SQL Language Reference
doc_id: E96310-37
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/DROP-HIERARCHY.html
tags:
  - oracle
  - 19c
  - sql-language-reference
---

## Purpose

Use the `DROP` `HIERARCHY` statement to drop a hierarchy. A `HIERARCHY` object is a component of analytic views.

## Prerequisites

To drop a hierarchy in your own schema, you must have the `DROP` `HIERARCHY` system privilege. To drop a hierarchy in another user’s schema, you must have the `DROP` `ANY` `HIERARCHY` system privilege.

## Syntax

## drop\_hierarchy::=

[Description of the illustration drop\_hierarchy.eps](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/img_text/drop_hierarchy.html)

## Semantics

## IF EXISTS

Specify `IF EXISTS` to drop an existing hierarchy.

**Note:** You can only use `IF EXISTS` from Release 19.28 and up.

## schema

Specify the schema in which the hierarchy exists. If you do not specify a schema, then Oracle Database looks for the hierarchy in your own schema.

## hierarchy\_name

Specify the name of the hierarchy to drop.

## Example

The following statement drops the specified hierarchy object:

```md
DROP HIERARCHY product_hier;
```