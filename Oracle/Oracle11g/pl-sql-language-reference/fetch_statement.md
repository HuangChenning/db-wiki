---
title: FETCH Statement
book: PL/SQL Language Reference
doc_id: E25519-13
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e25519/fetch_statement.htm
tags:
  - oracle
  - 11g
  - pl-sql-language-reference
---

The `FETCH` statement retrieves rows of data from the result set of a multiple-row query—one row at a time, several rows at a time, or all rows at once—and stores the data in variables, records, or collections.

Topics

Semantics

cursor

Name of an open explicit cursor. To open an explicit cursor, use the ["OPEN Statement"](open_statement.md).

If you try to fetch from an explicit cursor before opening it or after closing it, PL/SQL raises the predefined exception `INVALID_CURSOR`.

cursor\_variable

Name of an open cursor variable. To open a cursor variable, use the ["OPEN FOR Statement"](openfor_statement.md). The cursor variable can be a formal subprogram parameter (see ["Cursor Variables as Subprogram Parameters"](static.md)).

If you try to fetch from a cursor variable before opening it or after closing it, PL/SQL raises the predefined exception `INVALID_CURSOR`.

:host\_cursor\_variable

Name of a cursor variable declared in a PL/SQL host environment, passed to PL/SQL as a bind variable, and then opened. To open a host cursor variable, use the ["OPEN FOR Statement"](openfor_statement.md). Do not put space between the colon (:) and `host_cursor_variable`.

The data type of a host cursor variable is compatible with the return type of any PL/SQL cursor variable.

into\_clause

To have the `FETCH` statement retrieve one row at a time, use this clause to specify the variables or record in which to store the column values of a row that the cursor returns. For more information about `into_clause`, see ["into\_clause"](returninginto_clause.md).

bulk\_collect\_into\_clause \[ LIMIT numeric\_expression \]

Use `bulk_collect_into_clause` to specify one or more collections in which to store the rows that the `FETCH` statement returns. For more information about `bulk_collect_into_clause`, see ["bulk\_collect\_into\_clause"](returninginto_clause.md).

To have the `FETCH` statement retrieve all rows at once, omit `LIMIT` `numeric_expression`.

To limit the number of rows that the `FETCH` statement retrieves at once, specify `LIMIT` `numeric_expression`.

Restrictions on bulk\_collect\_into\_clause

- You cannot use `bulk_collect_into_clause` in client programs.
- When the `FETCH` statement requires implicit data type conversions, `bulk_collect_into_clause` can have only one `collection` or `host_array`.

Examples

- [Example 5-48, "FETCH Assigns Values to Record that Function Returns"](composites.md)
- [Example 6-6, "FETCH Statements Inside LOOP Statements"](static.md)
- [Example 6-7, "Fetching Same Explicit Cursor into Different Variables"](static.md)
- [Example 6-26, "Fetching Data with Cursor Variables"](static.md)
- [Example 6-27, "Fetching from Cursor Variable into Collections"](static.md)
- [Example 6-42, "FETCH with FOR UPDATE Cursor After COMMIT Statement"](static.md)
- [Example 7-4, "Native Dynamic SQL with OPEN FOR, FETCH, and CLOSE Statements"](dynamic.md)
- [Example 12-22, "Bulk-Fetching into Two Nested Tables"](tuning.md)
- [Example 12-23, "Bulk-Fetching into Nested Table of Records"](tuning.md)
- [Example 12-24, "Limiting Bulk FETCH with LIMIT"](tuning.md)

Related Topics

In this chapter:

- ["Assignment Statement"](assignment_statement.md)
- ["CLOSE Statement"](close_statement.md)
- ["Cursor Variable Declaration"](cursor_variable.md)
- ["Explicit Cursor Declaration and Definition"](explicit_cursor.md)
- ["OPEN Statement"](open_statement.md)
- ["OPEN FOR Statement"](openfor_statement.md)
- ["RETURNING INTO Clause"](returninginto_clause.md)
- ["%ROWTYPE Attribute"](rowtype_attribute.md)
- ["SELECT INTO Statement"](selectinto_statement.md)
- ["%TYPE Attribute"](type_attribute.md)

In other chapters:

- ["FETCH Statement for Assigning Row to Record Variable"](composites.md)
- ["Fetching Data with Explicit Cursors"](static.md)
- ["Query Result Set Processing With Cursor FOR LOOP Statements"](static.md)
- ["Fetching Data with Cursor Variables"](static.md)
- ["OPEN FOR, FETCH, and CLOSE Statements"](dynamic.md)
- ["FETCH Statement with BULK COLLECT Clause"](tuning.md)
- ["Fetching from Results of Pipelined Table Functions"](tuning.md)