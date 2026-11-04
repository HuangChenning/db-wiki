---
title: EXECUTE IMMEDIATE Statement
book: PL/SQL Language Reference
doc_id: E25519-13
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e25519/executeimmediate_statement.htm
tags:
  - oracle
  - 11g
  - pl-sql-language-reference
---

The `EXECUTE` `IMMEDIATE` statement builds and runs a dynamic SQL statement in a single operation. Native dynamic SQL uses the `EXECUTE` `IMMEDIATE` statement to process most dynamic SQL statements.

Caution:

When using dynamic SQL, beware of SQL injection, a security risk. For more information about SQL injection, see ["SQL Injection"](dynamic.md).

Topics

Semantics

execute\_immediate\_statement

dynamic\_sql\_stmt

String literal, string variable, or string expression that represents a SQL statement. Its type must be either `CHAR`, `VARCHAR2`, or `CLOB`.

Note:

If `dynamic_sql_statement` is a `SELECT` statement, and you omit both `into_clause` and `bulk_collect_into_clause`, then `execute_immediate_statement` never executes.

For example, this statement never increments the sequence:

```
EXECUTE IMMEDIATE 'SELECT S.NEXTVAL FROM DUAL'
```

into\_clause

Specifies the variables or record in which to store the column values that the statement returns. For more information about this clause, see ["RETURNING INTO Clause"](returninginto_clause.md).

Restriction on into\_clause Use if and only if `dynamic_sql_stmt` returns a single row.

bulk\_collect\_into\_clause

Specifies one or more collections in which to store the rows that the statement returns. For more information about this clause, see ["RETURNING INTO Clause"](returninginto_clause.md).

Restriction on bulk\_collect\_into\_clause Use if and only if `dynamic_sql_stmt` can return multiple rows.

using\_clause

Specifies bind variables, using positional notation.

Note:

If you repeat placeholder names in `dynamic_sql_statement`, be aware that the way placeholders are associated with bind variables depends on the kind of dynamic SQL statement. For details, see ["Repeated Placeholder Names in Dynamic SQL Statements."](dynamic.md)

Restrictions on using\_clause

- Use if and only if `dynamic_sql_stmt` includes placeholders for bind variables.
- If `dynamic_sql_stmt` has a `RETURNING` `INTO` clause, `using_clause` can contain only `IN` bind variables. The bind variables in the `RETURNING` `INTO` clause are `OUT` bind variables by definition.

dynamic\_returning\_clause

Returns the column values of the rows affected by the dynamic SQL statement, in either individual variables or records. For more information about this clause, see ["RETURNING INTO Clause"](returninginto_clause.md).

Restriction on dynamic\_returning\_clause Use if and only if `dynamic_sql_stmt` has a `RETURNING` `INTO` clause.

using\_clause

IN, OUT, IN OUT

Parameter modes of bind variables. An `IN` bind variable passes its value to `dynamic_sql_stmt`. An `OUT` bind variable stores a value that `dynamic_sql_stmt` returns. An `IN` `OUT` bind variable passes its initial value to `dynamic_sql_stmt` and stores a value that `dynamic_sql_stmt` returns. Default: `IN`.

For DML a statement with a `RETURNING` clause, you can place `OUT` bind variables in the `RETURNING` `INTO` clause without specifying the parameter mode, which is always `OUT`.

bind\_argument

An expression whose value replaces its corresponding placeholder in `dynamic_sql_stmt` at run time.

Every placeholder in `dynamic_sql_stmt` must be associated with a `bind_argument` in the `USING` clause or `RETURNING` `INTO` clause (or both) or with a define variable in the `INTO` clause.

You can run `dynamic_sql_stmt` repeatedly using different values for the bind variables. You incur some overhead, because `EXECUTE` `IMMEDIATE` prepares the dynamic string before every execution.

Restriction on bind\_argument The value of `bind_argument` cannot be `TRUE`, `FALSE`, or `NULL`. To pass the value `NULL` to the dynamic SQL statement, use an uninitialized variable where you want to use `NULL`, as in ["Uninitialized Variable Represents NULL in USING Clause"](dynamic.md).

Examples

- [Example 7-1, "Invoking Subprogram from Dynamic PL/SQL Block"](dynamic.md)
- [Example 7-2, "Unsupported Data Type in Native Dynamic SQL"](dynamic.md)
- [Example 7-3, "Uninitialized Variable Represents NULL in USING Clause"](dynamic.md)
- [Example 7-5, "Repeated Placeholder Names in Dynamic PL/SQL Block"](dynamic.md)