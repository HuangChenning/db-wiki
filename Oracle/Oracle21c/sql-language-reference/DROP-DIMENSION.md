---
title: SQL Language Reference
book: SQL Language Reference
doc_id: F31301-19
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/sqlrf/DROP-DIMENSION.html
tags:
  - oracle
  - 21c
  - sql-language-reference
---

## DROP DIMENSION

Purpose

Use the `DROP` `DIMENSION` statement to remove the named dimension.

This statement does not invalidate materialized views that use relationships specified in dimensions. However, requests that have been rewritten by query rewrite may be invalidated, and subsequent operations on such views may execute more slowly.

See Also:

- [CREATE DIMENSION](CREATE-DIMENSION.md) and [ALTER DIMENSION](ALTER-DIMENSION.md) for information on creating and modifying a dimension
- [Oracle Database Concepts](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlrf&id=CNCPT511) for general information about dimensions

Prerequisites

The dimension must be in your own schema or you must have the `DROP` `ANY` `DIMENSION` system privilege to use this statement.

Syntax

drop\_dimension::=

![drop_dimension](img/drop_dimension.gif)

> ```
> DROP DIMENSION [ schema. ] dimension ;
> ```
>
> ![Oracle Logo](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/gifs/oracle.gif)[  
> Copyright © 1996, 2025, Oracle and/or its affiliates.](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/html/cpyr.htm)


Semantics

schema

Specify the name of the schema in which the dimension is located. If you omit `schema`, then Oracle Database assumes the dimension is in your own schema.

dimension

Specify the name of the dimension you want to drop. The dimension must already exist.

Examples

Dropping a Dimension: Example

This example drops the `sh.customers_dim` dimension:

```
DROP DIMENSION customers_dim;
```

See Also:

" [Creating a Dimension: Examples](CREATE-DIMENSION.md) " and " [Modifying a Dimension: Examples](ALTER-DIMENSION.md) " for examples of creating and modifying this dimension