---
title: "%TYPE Attribute"
book: PL/SQL Language Reference
doc_id: E25519-13
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e25519/type_attribute.htm
tags:
  - oracle
  - 11g
  - pl-sql-language-reference
---

The `%TYPE` attribute lets you declare a constant, variable, collection element, record field, or subprogram parameter to be of the same data type as a previously declared variable or column (without knowing what that type is). The item declared with `%TYPE` is the referencing item, and the previously declared item is the referenced item.

The referencing item inherits the following from the referenced item:

- Data type and size
- Constraints (unless the referenced item is a column)

The referencing item does not inherit the initial value of the referenced item.

If the declaration of the referenced item changes, then the declaration of the referencing item changes accordingly.

Topics

- Syntax
- Semantics
- Examples
- Related Topics

Semantics

collection\_variable

Name of a collection variable.

Restriction on collection\_variable In a constant declaration, `collection_variable` cannot be an associative array variable.

cursor\_variable

Name of a cursor variable.

db\_table\_or\_view

Name of a database table or view that is accessible when the declaration is elaborated.

column

Name of a column of `db_table_or_view`.

object

Name of an instance of an ADT.

record\_variable

Name of a record variable.

field

Name of a field of `record_variable`.

scalar\_variable

Name of a scalar variable.