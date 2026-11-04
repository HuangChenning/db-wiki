---
title: SQL Language Reference
book: SQL Language Reference
doc_id: F31301-19
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/sqlrf/CREATE-FUNCTION.html
tags:
  - oracle
  - 21c
  - sql-language-reference
---

## CREATE FUNCTION

Purpose

Functions are defined using PL/SQL. Therefore, this section provides some general information but refers to [Oracle Database PL/SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlrf&id=LNPLS01370) for details of syntax and semantics.

Use the `CREATE` `FUNCTION` statement to create a standalone stored function or a call specification.

- A stored function (also called a user function or user-defined function) is a set of PL/SQL statements you can call by name. Stored functions are very similar to procedures, except that a function returns a value to the environment in which it is called. User functions can be used as part of a SQL expression.
- A call specification declares a Java method or a third-generation language (3GL) routine so that it can be called from PL/SQL. You can also use the `CALL` SQL statement to call such a method or routine. The call specification tells Oracle Database which Java method, or which named function in which shared library, to invoke when a call is made. It also tells the database what type conversions to make for the arguments and return value.

Note:

You can also create a function as part of a package using the `CREATE` `PACKAGE` statement.

See Also:

- [CREATE PROCEDURE](CREATE-PROCEDURE.md) for a general discussion of procedures and functions, [CREATE PACKAGE](CREATE-PACKAGE.md) for information on creating packages, [ALTER FUNCTION](ALTER-FUNCTION.md) and [DROP FUNCTION](DROP-FUNCTION.md) for information on modifying and dropping a function
- [CREATE LIBRARY](CREATE-LIBRARY.md) for information on shared libraries
- [Oracle Database Development Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlrf&id=ADFNS010) for more information about registering external functions

Prerequisites

To create or replace a function in your own schema, you must have the `CREATE` `PROCEDURE` system privilege. To create or replace a function in another user's schema, you must have the `CREATE` `ANY` `PROCEDURE` system privilege.

Syntax

Functions are defined using PL/SQL. Therefore, the syntax diagram in this book shows only the SQL keywords. Refer to Oracle Database PL/SQL Language Reference for the PL/SQL syntax, semantics, and examples.

create\_function::=

![create_function](img/create_function.gif)

> ```
> CREATE [ OR REPLACE ]
> [ EDITIONABLE | NONEDITIONABLE ]
> FUNCTION plsql_function_source
> ```
>
> ![Oracle Logo](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/gifs/oracle.gif)[  
> Copyright © 1996, 2025, Oracle and/or its affiliates.](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/html/cpyr.htm)


(`plsql_function_source`: See [Oracle Database PL/SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlrf&id=LNPLS2178).)

Semantics

OR REPLACE

Specify `OR` `REPLACE` to re-create the function if it already exists. Use this clause to change the definition of an existing function without dropping, re-creating, and regranting object privileges previously granted on the function. If you redefine a function, then Oracle Database recompiles it.

Users who had previously been granted privileges on a redefined function can still access the function without being regranted the privileges.

If any function-based indexes depend on the function, then Oracle Database marks the indexes `DISABLED`.

See Also:

[`ALTER` `FUNCTION`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlrf&id=SQLRF00804) for information on recompiling functions using SQL

\[ EDITIONABLE | NONEDITIONABLE \]

Use these clauses to specify whether the function is an editioned or noneditioned object if editioning is enabled for the schema object type `FUNCTION` in `schema`. The default is `EDITIONABLE`. For information about editioned and noneditioned objects, see [Oracle Database Development Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlrf&id=ADFNS99923).

plsql\_function\_source

See [Oracle Database PL/SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlrf&id=LNPLS2178) for the syntax and semantics of the `plsql_function_source`, including examples.