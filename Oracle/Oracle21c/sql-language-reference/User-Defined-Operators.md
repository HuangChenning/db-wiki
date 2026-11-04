---
title: SQL Language Reference
book: SQL Language Reference
doc_id: F31301-19
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/sqlrf/User-Defined-Operators.html
tags:
  - oracle
  - 21c
  - sql-language-reference
---

## User-Defined Operators

Like built-in operators, user-defined operators take a set of operands as input and return a result. However, you create them with the `CREATE` `OPERATOR` statement, and they are identified by user-defined names. They reside in the same namespace as tables, views, types, and standalone functions.

After you have defined a new operator, you can use it in SQL statements like any other built-in operator. For example, you can use user-defined operators in the select list of a `SELECT` statement, the condition of a `WHERE` clause, or in `ORDER` `BY` clauses and `GROUP` `BY` clauses. However, you must have `EXECUTE` privilege on the operator to do so, because it is a user-defined object.

See Also:

[CREATE OPERATOR](CREATE-OPERATOR.md) for an example of creating an operator and [Oracle Database Data Cartridge Developer's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlrf&id=ADDCI2100) for more information on user-defined operators