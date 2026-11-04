---
title: DROP OPERATOR
book: SQL Language Reference
doc_id: E41084-04
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_8023.htm
tags:
  - oracle
  - 11g
  - sql-language-reference
---

Purpose

Use the `DROP` `OPERATOR` statement to drop a user-defined operator.

See Also:

- [CREATE OPERATOR](statements_6004.md) and [ALTER OPERATOR](statements_2004.md) for information on creating and modifying operators
- ["User-Defined Operators"](operators007.md) and [Oracle Database Data Cartridge Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e10765/operators.htm#ADDCI2100) for more information on operators in general
- [ALTER INDEXTYPE](statements_1011.md) for information on dropping an operator of a user-defined indextype

Prerequisites

The operator must be in your schema or you must have the `DROP` `ANY` `OPERATOR` system privilege.

Syntax

drop\_operator::=

![drop_operator](img/drop_operator.gif)

> ```
> DROP OPERATOR [ schema. ] operator [ FORCE ] ;
> ```
  

Semantics

schema

Specify the schema containing the operator. If you omit `schema`, then Oracle Database assumes the operator is in your own schema.

operator

Specify the name of the operator to be dropped.

FORCE

Specify `FORCE` to drop the operator even if it is currently being referenced by one or more schema objects, such as indextypes, packages, functions, procedures, and so on. The database marks any such dependent objects `INVALID`. Without `FORCE`, you cannot drop an operator if any schema objects reference it.

Examples

Dropping a User-Defined Operator: Example The following statement drops the operator `eq_op`:

```
DROP OPERATOR eq_op;
```

Because the `FORCE` clause is not specified, this operation will fail if any of the bindings of this operator are referenced by an indextype.