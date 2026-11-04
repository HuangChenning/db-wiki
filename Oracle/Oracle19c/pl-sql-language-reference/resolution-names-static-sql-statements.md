---
title: Database PL/SQL Language Reference
book: Database PL/SQL Language Reference
doc_id: E96448-09
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/resolution-names-static-sql-statements.html
tags:
  - oracle
  - 19c
  - pl-sql-language-reference
---

## Resolution of Names in Static SQL Statements

Static SQL is described in [PL/SQL Static SQL](static-sql.md).

When the PL/SQL compiler finds a static SQL statement:

1. If the statement is a `SELECT` statement, the PL/SQL compiler removes the `INTO` clause.
2. The PL/SQL compiler sends the statement to the SQL subsystem.
3. The SQL subsystem checks the syntax of the statement.
	If the syntax is incorrect, the compilation of the PL/SQL unit fails. If the syntax is correct, the SQL subsystem determines the names of the tables and tries to resolve the other names in the scope of the SQL statement.
4. If the SQL subsystem cannot resolve a name in the scope of the SQL statement, then it sends the name back to the PL/SQL compiler. The name is called an escaped identifier.
5. The PL/SQL compiler tries to resolve the escaped identifier.
	First, the compiler tries to resolve the identifier in the scope of the PL/SQL unit. If that fails, the compiler tries to resolve the identifier in the scope of the schema. If that fails, the compilation of the PL/SQL unit fails.
6. If the compilation of the PL/SQL unit succeeds, the PL/SQL compiler generates the text of the regular SQL statement that is equivalent to the static SQL statement and stores that text with the generated computer code.
7. At run time, the PL/SQL runtime system invokes routines that parse, bind, and run the regular SQL statement.
	The bind variables are the escaped identifiers (see step [^2]).
8. If the statement is a `SELECT` statement, the PL/SQL runtime system stores the results in the PL/SQL targets specified in the `INTO` clause that the PL/SQL compiler removed in step [^1].

Note:

Bind variables can be evaluated in any order. If a program determines order of evaluation, then at the point where the program does so, its behavior is undefined.

[^1]: If the statement is a `SELECT` statement, the PL/SQL compiler removes the `INTO` clause.

[^undefined]: The PL/SQL compiler sends the statement to the SQL subsystem.

[^undefined]: The SQL subsystem checks the syntax of the statement.

If the syntax is incorrect, the compilation of the PL/SQL unit fails. If the syntax is correct, the SQL subsystem determines the names of the tables and tries to resolve the other names in the scope of the SQL statement.

[^2]: If the SQL subsystem cannot resolve a name in the scope of the SQL statement, then it sends the name back to the PL/SQL compiler. The name is called an escaped identifier.

[^undefined]: The PL/SQL compiler tries to resolve the escaped identifier.

First, the compiler tries to resolve the identifier in the scope of the PL/SQL unit. If that fails, the compiler tries to resolve the identifier in the scope of the schema. If that fails, the compilation of the PL/SQL unit fails.

[^undefined]: If the compilation of the PL/SQL unit succeeds, the PL/SQL compiler generates the text of the regular SQL statement that is equivalent to the static SQL statement and stores that text with the generated computer code.

[^undefined]: At run time, the PL/SQL runtime system invokes routines that parse, bind, and run the regular SQL statement.

The bind variables are the escaped identifiers (see step 4).

[^undefined]: If the statement is a `SELECT` statement, the PL/SQL runtime system stores the results in the PL/SQL targets specified in the `INTO` clause that the PL/SQL compiler removed in step 1.