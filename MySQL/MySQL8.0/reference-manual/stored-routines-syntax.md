---
title: "27.2.1 Stored Routine Syntax"
book: MySQL 8.0 Reference Manual
version: "8.0"
source: "https://dev.mysql.com/doc/refman/8.0/en/stored-routines-syntax.html"
tags:
  - mysql
  - mysql-8.0
  - reference-manual
---

MySQL 8.0 Reference Manual Including MySQL NDB Cluster 8.0

### 27.2.1 Stored Routine Syntax

A stored routine is either a procedure or a function. Stored routines are created with the [`CREATE       PROCEDURE`](create-procedure.md) and [`CREATE       FUNCTION`](create-function.md) statements (see [Section 15.1.17, “CREATE PROCEDURE and CREATE FUNCTION Statements”](create-procedure.md)). A procedure is invoked using a [`CALL`](call.md) statement (see [Section 15.2.1, “CALL Statement”](call.md)), and can only pass back values using output variables. A function can be called from inside a statement just like any other function (that is, by invoking the function's name), and can return a scalar value. The body of a stored routine can use compound statements (see [Section 15.6, “Compound Statement Syntax”](sql-compound-statements.md)).

Stored routines can be dropped with the [`DROP       PROCEDURE`](drop-procedure.md) and [`DROP       FUNCTION`](drop-function.md) statements (see [Section 15.1.29, “DROP PROCEDURE and DROP FUNCTION Statements”](drop-procedure.md)), and altered with the [`ALTER PROCEDURE`](alter-procedure.md) and [`ALTER FUNCTION`](alter-function.md) statements (see [Section 15.1.7, “ALTER PROCEDURE Statement”](alter-procedure.md)).

A stored procedure or function is associated with a particular database. This has several implications:

- When the routine is invoked, an implicit ``USE           *`db_name`*`` is performed (and undone when the routine terminates). [`USE`](use.md) statements within stored routines are not permitted.
- You can qualify routine names with the database name. This can be used to refer to a routine that is not in the current database. For example, to invoke a stored procedure `p` or function `f` that is associated with the `test` database, you can say `CALL test.p()` or `test.f()`.
- When a database is dropped, all stored routines associated with it are dropped as well.

Stored functions cannot be recursive.

Recursion in stored procedures is permitted but disabled by default. To enable recursion, set the [`max_sp_recursion_depth`](server-system-variables.md) server system variable to a value greater than zero. Stored procedure recursion increases the demand on thread stack space. If you increase the value of [`max_sp_recursion_depth`](server-system-variables.md), it may be necessary to increase thread stack size by increasing the value of [`thread_stack`](server-system-variables.md) at server startup. See [Section 7.1.8, “Server System Variables”](server-system-variables.md), for more information.

MySQL supports a very useful extension that enables the use of regular [`SELECT`](select.md) statements (that is, without using cursors or local variables) inside a stored procedure. The result set of such a query is simply sent directly to the client. Multiple [`SELECT`](select.md) statements generate multiple result sets, so the client must use a MySQL client library that supports multiple result sets. This means the client must use a client library from a version of MySQL at least as recent as 4.1. The client should also specify the `CLIENT_MULTI_RESULTS` option when it connects. For C programs, this can be done with the [`mysql_real_connect()`](https://docs.oracle.com/cd/E17952_01/c-api-8.0-en/mysql-real-connect.html) C API function. See [mysql\_real\_connect()](https://docs.oracle.com/cd/E17952_01/c-api-8.0-en/mysql-real-connect.html), and [Multiple Statement Execution Support](https://docs.oracle.com/cd/E17952_01/c-api-8.0-en/c-api-multiple-queries.html).

In MySQL 8.0.22 and later, a user variable referenced by a statement in a stored procedure has its type determined the first time the procedure is invoked, and retains this type each time the procedure is invoked thereafter.