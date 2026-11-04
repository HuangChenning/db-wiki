---
title: UPDATE Statement Extensions
book: PL/SQL Language Reference
doc_id: E25519-13
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e25519/update_statement.htm
tags:
  - oracle
  - 11g
  - pl-sql-language-reference
---

PL/SQL extends the `update_set_clause` and `where_clause` of the SQL `UPDATE` statement as follows:

- In the `update_set_clause`, you can specify a record. For each selected row, the `UPDATE` statement updates each column with the value of the corresponding record field.
- In the `where_clause`, you can specify a `CURRENT` `OF` clause, which restricts the `UPDATE` statement to the current row of the specified cursor.

See Also:

[Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_10008.htm#SQLRF01708) for the syntax of the SQL `UPDATE` statement

Topics

- Syntax
- Semantics
- Examples
- Related Topics

Syntax

update\_set\_clause::=

  
[Description of the illustration update\_set\_clause.gif](https://docs.oracle.com/cd/E11882_01/appdev.112/e25519/img_text/update_set_clause.htm)  
  

where\_clause::=

  
[Description of the illustration where\_clause.gif](https://docs.oracle.com/cd/E11882_01/appdev.112/e25519/img_text/where_clause.htm)  

Semantics

record

Name of a record variable that represents a row of the item described by `dml_table_expression_clause`. That is, for every column of the row, the record must have a field with a compatible data type. If a column has a `NOT` `NULL` constraint, then its corresponding field cannot have a `NULL` value.

for\_update\_cursor

Name of a `FOR` `UPDATE` cursor; that is, an explicit cursor associated with a `FOR` `SELECT` `UPDATE` statement.

Related Topics

In this chapter:

- ["Explicit Cursor Declaration and Definition"](explicit_cursor.md)
- ["Record Variable Declaration"](record_definition.md)
- ["%ROWTYPE Attribute"](rowtype_attribute.md)

In other chapters:

- ["Updating Rows with Records"](composites.md)
- ["Restrictions on Record Inserts and Updates"](composites.md)
- ["SELECT FOR UPDATE and FOR UPDATE Cursors"](static.md)