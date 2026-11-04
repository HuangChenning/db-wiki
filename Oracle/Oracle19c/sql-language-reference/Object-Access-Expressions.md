---
title: Object Access Expressions
book: SQL Language Reference
doc_id: E96310-37
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/Object-Access-Expressions.html
tags:
  - oracle
  - 19c
  - sql-language-reference
---

An object access expression specifies attribute reference and method invocation.

## object\_access\_expression::=

![object_access_expression](img/object_access_expression.gif)

> ```
> { table_alias.column.
> | object_table_alias.
> | (expr).
> }
> { attribute [.attribute ]...
>   [.method ([ argument [, argument ]... ]) ]
> | method ([ argument [, argument ]... ])
> }
> ```
>
> [Copyright ©](https://docs.oracle.com/pls/topic/lookup?ctx=en/legal&id=cpyr) 2026,1996, Oracle and/or its affiliates.


[Description of the illustration object\_access\_expression.eps](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/img_text/object_access_expression.html)

The column parameter can be an object or `REF` column. If you specify *expr*, then it must resolve to an object type.

When a type’s member function is invoked in the context of a SQL statement, if the `SELF` argument is null, Oracle returns null and the function is not invoked.

## Examples

The following example creates a table based on the sample `oe.order_item_typ` object type, and then shows how you would update and select from the object column attributes.

```md
CREATE TABLE short_orders (
   sales_rep VARCHAR2(25), item order_item_typ);

UPDATE short_orders s SET sales_rep = 'Unassigned';

SELECT o.item.line_item_id, o.item.quantity FROM short_orders o;
```