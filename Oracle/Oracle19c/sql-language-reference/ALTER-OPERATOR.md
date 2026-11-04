---
title: ALTER OPERATOR
book: SQL Language Reference
doc_id: E96310-37
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/ALTER-OPERATOR.html
tags:
  - oracle
  - 19c
  - sql-language-reference
---

## Purpose

Use the `ALTER` `OPERATOR` statement to add bindings to, drop bindings from, or compile an existing operator.

**See Also:** [CREATE OPERATOR](CREATE-OPERATOR.md)

## Prerequisites

The operator must already have been created by a previous `CREATE` `OPERATOR` statement. The operator must be in your own schema or you must have the `ALTER` `ANY` `OPERATOR` system privilege. You must have the `EXECUTE` object privilege on the operators and functions referenced in the `ALTER` `OPERATOR` statement.

## Syntax

## alter\_operator::=

[Description of the illustration alter\_operator.eps](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/img_text/alter_operator.html)

(*add\_binding\_clause::=*, *drop\_binding\_clause::=*)

## add\_binding\_clause::=

[Description of the illustration add\_binding\_clause.eps](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/img_text/add_binding_clause.html)

(*implementation\_clause::=*, *using\_function\_clause::=*)

## implementation\_clause::=

[Description of the illustration implementation\_clause.eps](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/img_text/implementation_clause.html)

(*context\_clause::=*)

## context\_clause::=

[Description of the illustration context\_clause.eps](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/img_text/context_clause.html)

## using\_function\_clause::=

[Description of the illustration using\_function\_clause.eps](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/img_text/using_function_clause.html)

## drop\_binding\_clause::=

[Description of the illustration drop\_binding\_clause.eps](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/img_text/drop_binding_clause.html)

## Semantics

## IF EXISTS

Specify `IF EXISTS` to alter an existing operator.

**Note:** You can only use `IF EXISTS` from Release 19.28 and up.

## schema

Specify the schema containing the operator. If you omit this clause, then Oracle Database assumes the operator is in your own schema.

## operator

Specify the name of the operator to be altered.

## add\_binding\_clause

Use this clause to add an operator binding and specify its parameter data types and return type. The signature must be different from the signature of any existing binding for this operator.

If a binding of an operator is associated with an indextype and you add another binding to the operator, then Oracle Database does not automatically associate the new binding with the indextype. If you want to make such an association, then you must issue an explicit `ALTER` `INDEXTYPE` … `ADD` `OPERATOR` statement.

## implementation\_clause

This clause has the same semantics in `CREATE` `OPERATOR` and `ALTER` `OPERATOR` statements. For full information, refer to *[implementation\_clause](CREATE-OPERATOR.md)* in the documentation on `CREATE` `OPERATOR`.

## context\_clause

This clause has the same semantics in `CREATE` `OPERATOR` and `ALTER` `OPERATOR` statements. For full information, refer to *[context\_clause](CREATE-OPERATOR.md)* in the documentation on `CREATE` `OPERATOR`.

## using\_function\_clause

This clause has the same semantics in `CREATE` `OPERATOR` and `ALTER` `OPERATOR` statements. For full information, refer to *[using\_function\_clause](CREATE-OPERATOR.md)* in the documentation on `CREATE` `OPERATOR`.

## drop\_binding\_clause

Use this clause to specify the list of parameter data types of the binding you want to drop from the operator. You must specify `FORCE` if the binding has any dependent objects, such as an indextype or an ancillary operator binding. If you specify `FORCE`, then Oracle Database marks `INVALID` all objects that are dependent on the binding. The dependent objects are revalidated the next time they are referenced in a DDL or DML statement or a query.

You cannot use this clause to drop the only binding associated with this operator. Instead you must use the `DROP` `OPERATOR` statement. Refer to [DROP OPERATOR](DROP-OPERATOR.md) for more information.

## COMPILE

Specify `COMPILE` to cause Oracle Database to recompile the operator.

## Examples

**Compiling a User-defined Operator: Example**

The following example compiles the operator `eq_op` (which was created in “ [Creating User-Defined Operators: Example](CREATE-OPERATOR.md) ”):

```md
ALTER OPERATOR eq_op COMPILE;
```