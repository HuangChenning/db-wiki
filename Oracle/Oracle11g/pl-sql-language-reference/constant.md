---
title: Constant Declaration
book: PL/SQL Language Reference
doc_id: E25519-13
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e25519/constant.htm
tags:
  - oracle
  - 11g
  - pl-sql-language-reference
---

A constant holds a value that does not change.

A constant declaration specifies the name, data type, and value of the constant and allocates storage for it. The declaration can also impose the `NOT` `NULL` constraint.

Topics

Semantics

constant

Name of the constant that you are declaring.

datatype

Data type for which a variable can be declared with an initial value.

NOT NULL

Imposes the `NOT` `NULL` constraint on the constant. For information about this constraint, see ["NOT NULL Constraint"](fundamentals.md).

expression

Initial value for the constant. `expression` must have a data type that is compatible with `datatype`. When `constant_declaration` is elaborated, the value of `expression` is assigned to `constant`.