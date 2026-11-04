---
title: DROP ATTRIBUTE DIMENSION
book: SQL Language Reference
doc_id: E96310-37
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/DROP-ATTRIBUTE-DIMENSION.html
tags:
  - oracle
  - 19c
  - sql-language-reference
---

## Purpose

Use the `DROP` `ATTRIBUTE` `DIMENSION` statement to drop an attribute dimension. An `ATTRIBUTE` `DIMENSION` object is a component of analytic views.

## Prerequisites

To drop an attribute dimension in your own schema, you must have the `DROP` `ATTRIBUTE` `DIMENSION` system privilege. To drop an analytic view in another user’s schema, you must have the `DROP` `ANY` `ATTRIBUTE` `DIMENSION` system privilege.

## Syntax

## drop\_attribute\_dimension::=

[Description of the illustration drop\_attribute\_dimension.eps](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/img_text/drop_attribute_dimension.html)

## IF EXISTS

Specify `IF EXISTS` to drop an existing attribute dimension.

**Note:** You can only use `IF EXISTS` from Release 19.28 and up.

## Semantics

## schema

Specify the schema in which the attribute dimension exists. If you do not specify a schema, then Oracle Database looks for the attribute dimension in your own schema.

## attr\_dimension\_name

Specify the name of the attribute dimension to drop.

## Example

The following statement drops the specified attribute dimension object:

```md
DROP ATTRIBUTE DIMENSION product_attr_dim;
```