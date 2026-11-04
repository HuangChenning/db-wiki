---
title: SQL Language Reference
book: SQL Language Reference
doc_id: F31301-19
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/sqlrf/COLLATE-Operator.html
tags:
  - oracle
  - 21c
  - sql-language-reference
---

## COLLATE Operator

The `COLLATE` operator determines the collation for an expression. This operator enables you to override the collation that the database would have derived for the expression using standard collation derivation rules.

`COLLATE` is a postfix unary operator. It has the same precedence as other unary operators, but it is evaluated after all prefix unary operators have been evaluated.

You can apply this operator to expressions of type `VARCHAR2`, `CHAR`, `LONG`, `NVARCHAR`, or `NCHAR`.

The `COLLATE` operator takes one argument, `collation_name`, for which you can specify a named collation or pseudo-collation. If the collation name contains a space, then you must enclose the name in double quotation marks.

Table 4-3 describes the `COLLATE` operator.

Table 4-3 COLLATE Operator

| Operator | Purpose | Example |
| --- | --- | --- |
| `COLLATE` `collation_name` | Determines the collation for an expression | ``` SELECT last_name   FROM employees   ORDER BY last_name COLLATE GENERIC_M; ``` |

See Also:

- [Compound Expressions](Compound-Expressions.md) for information on using the `COLLATE` operator in a compound expression
- [Oracle Database Globalization Support Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlrf&id=NLSPG-GUID-4146F48A-FB6F-4593-8098-BDF45404EB24) for more information on the `COLLATE` operator