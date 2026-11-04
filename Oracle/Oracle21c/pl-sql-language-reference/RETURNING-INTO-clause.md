---
title: Database PL/SQL Language Reference
book: Database PL/SQL Language Reference
doc_id: F31827-07
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/lnpls/RETURNING-INTO-clause.html
tags:
  - oracle
  - 21c
  - pl-sql-language-reference
---

The `RETURNING` `INTO` clause specifies the variables in which to store the values returned by the statement to which the clause belongs.

The variables can be either individual variables or collections. If the statement affects no rows, then the values of the variables are undefined.

The static `RETURNING` `INTO` clause belongs to a `DELETE`, `INSERT`, or `UPDATE` statement. The dynamic `RETURNING` `INTO` clause belongs to the `EXECUTE` `IMMEDIATE` statement.

Note:

You cannot use the `RETURNING` `INTO` clause for remote or parallel deletes.

Topics

Syntax

static\_returning\_clause::=

![static_returning_clause](img/static_returning_clause.gif)

> ```
> { RETURNING | RETURN } column [, column ]...
>   { into_clause | bulk_collect_into_clause }
> ```
>
> ![Oracle Logo](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/gifs/oracle.gif)[  
> Copyright © 1996, 2024, Oracle and/or its affiliates.](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/html/cpyr.htm)


dynamic\_returning\_clause::=

![dynamic_returning_clause](img/dynamic_returning_clause.gif)

> ```
> { RETURNING | RETURN } { into_clause | bulk_collect_into_clause }
> ```
>
> ![Oracle Logo](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/gifs/oracle.gif)[  
> Copyright © 1996, 2024, Oracle and/or its affiliates.](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/html/cpyr.htm)


into\_clause::=

![into_clause](img/into_clause.gif)

> ```
> INTO { variable [, variable ]... | record )
> ```
>
> ![Oracle Logo](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/gifs/oracle.gif)[  
> Copyright © 1996, 2024, Oracle and/or its affiliates.](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/html/cpyr.htm)


bulk\_collect\_into\_clause::=

![bulk_collect_into_clause](img/bulk_collect_into_clause.gif)

> ```
> BULK COLLECT INTO { collection | :host_array }
>   [, { collection | :host_array } ]...
> ```
>
> ![Oracle Logo](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/gifs/oracle.gif)[  
> Copyright © 1996, 2024, Oracle and/or its affiliates.](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/html/cpyr.htm)


Semantics

static\_returning\_clause

column

Expression whose value is the name of a column of a database table.

into\_clause

Specifies the variables or record in which to store the column values that the statement returns.

Restriction on into\_clause

Use `into_clause` in `dynamic_returning_clause` if and only if `dynamic_sql_stmt` (which appears in " [EXECUTE IMMEDIATE Statement](EXECUTE-IMMEDIATE-statement.md) ") returns a single row.

record

The name of a record variable in which to store the row that the statement returns. For each select\_list item in the statement, the record must have a corresponding, type-compatible field.

variable

Either the name of a scalar variable in which to store a column that the statement returns or the name of a host cursor variable that is declared in a PL/SQL host environment and passed to PL/SQL as a bind variable. Each select\_list item in the statement must have a corresponding, type-compatible variable. The data type of a host cursor variable is compatible with the return type of any PL/SQL cursor variable.

Restriction on variable

`variable` cannot have the data type `BOOLEAN`.

bulk\_collect\_into\_clause

Specifies one or more existing collections or host arrays in which to store the rows that the statement returns. For each select\_list item in the statement, `bulk_collect_into_clause` must have a corresponding, type-compatible `collection` or `host_array`.

For the reason to use this clause, see " [Bulk SQL and Bulk Binding](plsql-optimization-and-tuning.md) ".

Restrictions on bulk\_collect\_into\_clause

- Use the `bulk_collect_into_clause` clause in `dynamic_returning_clause` if and only if `dynamic_sql_stmt` (which appears in " [EXECUTE IMMEDIATE Statement](EXECUTE-IMMEDIATE-statement.md) ") can return multiple rows.
- You cannot use `bulk_collect_into_clause` in client programs.
- When the statement that includes `bulk_collect_into_clause` requires implicit data type conversions, `bulk_collect_into_clause` can have only one `collection` or `host_array`.

collection

Name of a collection variable in which to store the rows that the statement returns.

Restrictions on collection

- `collection` cannot be the name of an associative array that is indexed by a string.
- When the statement requires implicit data type conversions, `collection` cannot be the name of a collection of a composite type.

:host\_array

Name of an array declared in a PL/SQL host environment and passed to PL/SQL as a bind variable. Do not put space between the colon (:) and `host_array`.

Examples

- [Example 6-58](plsql-collections-and-records.md), "UPDATE Statement Assigns Values to Record Variable"
- [Example 7-1](static-sql.md), "Static SQL Statements"
- [Example 13-25](plsql-optimization-and-tuning.md), "Returning Deleted Rows in Two Nested Tables"
- [Example 13-26](plsql-optimization-and-tuning.md), "DELETE with RETURN BULK COLLECT INTO in FORALL Statement"

Related Topics

In this chapter:

- " [DELETE Statement Extension](DELETE-statement-extension.md) "
- " [EXECUTE IMMEDIATE Statement](EXECUTE-IMMEDIATE-statement.md) "
- " [FETCH Statement](FETCH-statement.md) "
- " [SELECT INTO Statement](SELECT-INTO-statement.md) "
- " [UPDATE Statement Extensions](UPDATE-statement-extensions.md) "

In other chapters:

- " [Using SQL Statements to Return Rows in PL/SQL Record Variables](plsql-collections-and-records.md) "
- " [EXECUTE IMMEDIATE Statement](dynamic-sql.md) "
- " [RETURNING INTO Clause with BULK COLLECT Clause](plsql-optimization-and-tuning.md) "