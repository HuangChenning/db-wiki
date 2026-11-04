---
title: DROP DIMENSION
book: SQL Language Reference
doc_id: E96310-37
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/DROP-DIMENSION.html
tags:
  - oracle
  - 19c
  - sql-language-reference
---

## Purpose

Use the `DROP` `DIMENSION` statement to remove the named dimension.

This statement does not invalidate materialized views that use relationships specified in dimensions. However, requests that have been rewritten by query rewrite may be invalidated, and subsequent operations on such views may execute more slowly.

**See Also:**

- [CREATE DIMENSION](CREATE-DIMENSION.md) and [ALTER DIMENSION](ALTER-DIMENSION.md) for information on creating and modifying a dimension
- [*Oracle Database Concepts*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/sqlrf&id=CNCPT511) for general information about dimensions

## Prerequisites

The dimension must be in your own schema or you must have the `DROP` `ANY` `DIMENSION` system privilege to use this statement.

## Syntax

## drop\_dimension::=

[Description of the illustration drop\_dimension.eps](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/img_text/drop_dimension.html)

## Semantics

## schema

Specify the name of the schema in which the dimension is located. If you omit *schema*, then Oracle Database assumes the dimension is in your own schema.

## dimension

Specify the name of the dimension you want to drop. The dimension must already exist.

## Examples

**Dropping a Dimension: Example**

This example drops the `sh.customers_dim` dimension:

```md
DROP DIMENSION customers_dim;
```

**See Also:** “ [Creating a Dimension: Examples](CREATE-DIMENSION.md) ” and “ [Modifying a Dimension: Examples](ALTER-DIMENSION.md) ” for examples of creating and modifying this dimension