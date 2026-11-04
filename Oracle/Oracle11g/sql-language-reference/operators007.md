---
title: User-Defined Operators
book: SQL Language Reference
doc_id: E41084-04
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e41084/operators007.htm
tags:
  - oracle
  - 11g
  - sql-language-reference
---

Like built-in operators, user-defined operators take a set of operands as input and return a result. However, you create them with the `CREATE` `OPERATOR` statement, and they are identified by user-defined names. They reside in the same namespace as tables, views, types, and standalone functions.

After you have defined a new operator, you can use it in SQL statements like any other built-in operator. For example, you can use user-defined operators in the select list of a `SELECT` statement, the condition of a `WHERE` clause, or in `ORDER` `BY` clauses and `GROUP` `BY` clauses. However, you must have `EXECUTE` privilege on the operator to do so, because it is a user-defined object.

See Also:

[CREATE OPERATOR](statements_6004.md) for an example of creating an operator and [Oracle Database Data Cartridge Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e10765/operators.htm#ADDCI2100) for more information on user-defined operators