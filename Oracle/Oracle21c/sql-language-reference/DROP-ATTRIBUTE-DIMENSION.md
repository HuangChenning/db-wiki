---
title: SQL Language Reference
book: SQL Language Reference
doc_id: F31301-19
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/sqlrf/DROP-ATTRIBUTE-DIMENSION.html
tags:
  - oracle
  - 21c
  - sql-language-reference
---

## DROP ATTRIBUTE DIMENSION

Purpose

Use the `DROP` `ATTRIBUTE` `DIMENSION` statement to drop an attribute dimension. An `ATTRIBUTE` `DIMENSION` object is a component of analytic views.

Prerequisites

To drop an attribute dimension in your own schema, you must have the `DROP` `ATTRIBUTE` `DIMENSION` system privilege. To drop an analytic view in another user's schema, you must have the `DROP` `ANY` `ATTRIBUTE` `DIMENSION` system privilege.

Syntax

drop\_attribute\_dimension::=

![drop_attribute_dimension](img/drop_attribute_dimension.gif)

> ```
> DROP ATTRIBUTE DIMENSION [ schema. ] attr_dimension_name;
> ```
>
> ![Oracle Logo](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/gifs/oracle.gif)[  
> Copyright © 1996, 2025, Oracle and/or its affiliates.](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/html/cpyr.htm)


Semantics

schema

Specify the schema in which the attribute dimension exists. If you do not specify a schema, then Oracle Database looks for the attribute dimension in your own schema.

attr\_dimension\_name

Specify the name of the attribute dimension to drop.

Example

The following statement drops the specified attribute dimension object:

```
DROP ATTRIBUTE DIMENSION product_attr_dim;
```