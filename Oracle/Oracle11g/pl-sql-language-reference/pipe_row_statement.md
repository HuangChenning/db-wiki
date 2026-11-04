---
title: PIPE ROW Statement
book: PL/SQL Language Reference
doc_id: E25519-13
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e25519/pipe_row_statement.htm
tags:
  - oracle
  - 11g
  - pl-sql-language-reference
---

The `PIPE` `ROW` statement, which can appear only in the body of a pipelined table function, returns a table row (but not control) to the invoker of the function.

Note:

- If a pipelined table function is part of an autonomous transaction, then it must `COMMIT` or `ROLLBACK` before each `PIPE` `ROW` statement, to avoid an error in the invoking subprogram.
- To improve performance, the PL/SQL runtime system delivers the piped rows to the invoker in batches.

Topics

- Syntax
- Semantics
- Examples
- Related Topics

Syntax

pipe\_row\_statement::=

  
[Description of the illustration pipe\_row\_statement.gif](https://docs.oracle.com/cd/E11882_01/appdev.112/e25519/img_text/pipe_row_statement.htm)  

Semantics

row

Row (table element) that the function returns to its invoker, represented by an expression whose type is that of the table element.

If the expression is a record variable, it must be explicitly declared with the data type of the table element. It cannot be declared with a data type that is only structurally identical to the element type. For example, if the element type has a name, then the record variable cannot be declared explicitly with `%TYPE` or `%ROWTYPE` or implicitly with `%ROWTYPE` in a cursor `FOR` `LOOP` statement.

Examples

- [Example 12-29, "Creating and Invoking Pipelined Table Function"](tuning.md)
- [Example 12-30, "Pipelined Table Function Transforms Each Row to Two Rows"](tuning.md)
- [Example 12-32, "Pipelined Table Function with Two Cursor Variable Parameters"](tuning.md)
- [Example 12-33, "Pipelined Table Function as Aggregate Function"](tuning.md)
- [Example 12-34, "Pipelined Table Function Does Not Handle NO\_DATA\_NEEDED"](tuning.md)
- [Example 12-35, "Pipelined Table Function Handles NO\_DATA\_NEEDED"](tuning.md)