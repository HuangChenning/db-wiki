---
title: Simple Expressions
book: SQL Language Reference
doc_id: E96310-37
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/Simple-Expressions.html
tags:
  - oracle
  - 19c
  - sql-language-reference
---

A simple expression specifies a column, pseudocolumn, constant, sequence number, or null.

## simple\_expression::=

![simple_expression](img/simple_expression.gif)

> ```
> { [ query_name.
>   | [schema.] { table. | view. | materialized view. }
>   | t_alias.
>   ] { column | ROWID }
> | ROWNUM
> | string
> | number
> | sequence. { CURRVAL | NEXTVAL }
> | NULL
> }
> ```
>
> [Copyright ©](https://docs.oracle.com/pls/topic/lookup?ctx=en/legal&id=cpyr) 2026,1996, Oracle and/or its affiliates.


[Description of the illustration simple\_expression.eps](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/img_text/simple_expression.html)

In addition to the schema of a user, *schema* can also be “ `PUBLIC` ” (double quotation marks required), in which case it must qualify a public synonym for a table, view, or materialized view. Qualifying a public synonym with “ `PUBLIC` ” is supported only in data manipulation language (DML) statements, not data definition language (DDL) statements.

You can specify `ROWID` only with a table, not with a view or materialized view. `NCHAR` and `NVARCHAR2` are not valid pseudocolumn data types.

**See Also:** [Pseudocolumns](Pseudocolumns.md) for more information on pseudocolumns and *[subquery\_factoring\_clause](SELECT.md)* for information on *query\_name*

Some valid simple expressions are:

```md
employees.last_name
'this is a text string'
10
N'this is an NCHAR string'
```