---
title: Scalar Variable Declaration
book: PL/SQL Language Reference
doc_id: E25519-13
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e25519/variable_declaration.htm
tags:
  - oracle
  - 11g
  - pl-sql-language-reference
---

A scalar variable stores a value with no internal components. The value can change.

A scalar variable declaration specifies the name and data type of the variable and allocates storage for it. The declaration can also assign an initial value and impose the `NOT` `NULL` constraint.

You reference a scalar variable by its name.

Topics

Semantics

variable

Name of the variable that you are declaring.

datatype

Name of a scalar data type, including any qualifiers for size, precision, and character or byte semantics. For information about scalar data types, see [Chapter 3, "PL/SQL Data Types"](datatypes.md).

NOT NULL

Imposes the `NOT` `NULL` constraint on the variable. For information about this constraint, see ["NOT NULL Constraint"](fundamentals.md).

expression

Value to be assigned to the variable when the declaration is elaborated. `expression` and `variable` must have compatible data types.

Examples

- [Example 2-9, "Scalar Variable Declarations"](fundamentals.md)
- [Example 2-11, "Variable and Constant Declarations with Initial Values"](fundamentals.md)
- [Example 2-12, "Variable Initialized to NULL by Default"](fundamentals.md)
- [Example 2-13, "Variable Declaration with NOT NULL Constraint"](fundamentals.md)