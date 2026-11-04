---
title: "%ROWTYPE Attribute"
book: PL/SQL Language Reference
doc_id: E25519-13
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e25519/rowtype_attribute.htm
tags:
  - oracle
  - 11g
  - pl-sql-language-reference
---

The `%ROWTYPE` attribute lets you declare a record that represents either a full or partial row of a database table or view. For every column of the full or partial row, the record has a field with the same name and data type. If the structure of the row changes, then the structure of the record changes accordingly.

The record fields do not inherit the constraints or initial values of the corresponding columns.

Topics

Semantics

explicit\_cursor\_name

Name of an explicit cursor. For every column selected by the query associated with `explicit_cursor_name`, the record has a field with the same name and data type.

cursor\_variable\_name

Name of a strong cursor variable. For every column selected by the query associated with `cursor_variable_name`, the record has a field with the same name and data type.

db\_table\_or\_view\_name

Name of a database table or view that is accessible when the declaration is elaborated. For every column of `db_table_or_view_name`, the record has a field with the same name and data type.

Examples

- [Example 5-38, "%ROWTYPE Variable Represents Full Database Table Row"](composites.md)
- [Example 5-39, "%ROWTYPE Variable Does Not Inherit Initial Values or Constraints"](composites.md)
- [Example 5-40, "%ROWTYPE Variable Represents Partial Database Table Row"](composites.md)
- [Example 5-41, "%ROWTYPE Variable Represents Join Row"](composites.md)
- [Example 5-45, "Assigning %ROWTYPE Record to RECORD Type Record"](composites.md)