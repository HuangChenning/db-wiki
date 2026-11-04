---
title: Database PL/SQL Language Reference
book: Database PL/SQL Language Reference
doc_id: E96448-09
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/advantages-pl-sql.html
tags:
  - oracle
  - 19c
  - pl-sql-language-reference
---

## Advantages of PL/SQL

### Tight Integration with SQL

PL/SQL is tightly integrated with SQL, the most widely used database manipulation language.

For example:

- PL/SQL lets you use all SQL data manipulation, cursor control, and transaction control statements, and all SQL functions, operators, and pseudocolumns.
- PL/SQL fully supports SQL data types.
	You need not convert between PL/SQL and SQL data types. For example, if your PL/SQL program retrieves a value from a column of the SQL type `VARCHAR2`, it can store that value in a PL/SQL variable of the type `VARCHAR2`.
	You can give a PL/SQL data item the data type of a column or row of a database table without explicitly specifying that data type (see " [Using the %TYPE Attribute](main-features-pl-sql.md) " and " [Using the %ROWTYPE Attribute](main-features-pl-sql.md) ").
- PL/SQL lets you run a SQL query and process the rows of the result set one at a time (see " [Processing a Query Result Set One Row at a Time](main-features-pl-sql.md) ").
- PL/SQL functions can be declared and defined in the `WITH` clauses of SQL `SELECT` statements (see [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=SQLRF01702)).

PL/SQL supports both static and dynamic SQL. Static SQL is SQL whose full text is known at compile time. Dynamic SQL is SQL whose full text is not known until run time. Dynamic SQL lets you make your applications more flexible and versatile. For more information, see [PL/SQL Static SQL](static-sql.md) and [PL/SQL Dynamic SQL](dynamic-sql.md).

### High Performance

PL/SQL lets you send a block of statements to the database, significantly reducing traffic between the application and the database.

Bind Variables

When you embed a SQL `INSERT`, `UPDATE`, `DELETE`, `MERGE`, or `SELECT` statement directly in your PL/SQL code, the PL/SQL compiler turns the variables in the `WHERE` and `VALUES` clauses into bind variables (for details, see " [Resolution of Names in Static SQL Statements](resolution-names-static-sql-statements.md) "). Oracle Database can reuse these SQL statements each time the same code runs, which improves performance.

PL/SQL does not create bind variables automatically when you use dynamic SQL, but you can use them with dynamic SQL by specifying them explicitly (for details, see " [EXECUTE IMMEDIATE Statement](native-dynamic-sql.md) ").

Subprograms

PL/SQL subprograms are stored in executable form, which can be invoked repeatedly. Because stored subprograms run in the database server, a single invocation over the network can start a large job. This division of work reduces network traffic and improves response times. Stored subprograms are cached and shared among users, which lowers memory requirements and invocation overhead. For more information about subprograms, see " [Subprograms](main-features-pl-sql.md) ".

Optimizer

The PL/SQL compiler has an optimizer that can rearrange code for better performance. For more information about the optimizer, see " [PL/SQL Optimizer](pl-sql-optimizer.md) ".

### High Productivity

PL/SQL has many features that save designing and debugging time, and it is the same in all environments.

PL/SQL lets you write compact code for manipulating data. Just as a scripting language like PERL can read, transform, and write data in files, PL/SQL can query, transform, and update data in a database.

If you learn to use PL/SQL with one Oracle tool, you can transfer your knowledge to other Oracle tools. For an overview of PL/SQL features, see " [Main Features of PL/SQL](main-features-pl-sql.md) ".

### Portability

PL/SQL is a portable and standard language for Oracle development.

You can run PL/SQL applications on any operating system and platform where Oracle Database runs.

### Scalability

PL/SQL stored subprograms increase scalability by centralizing application processing on the database server.

The shared memory facilities of the shared server let Oracle Database support thousands of concurrent users on a single node. For more information about subprograms, see " [Subprograms](main-features-pl-sql.md) "

For further scalability, you can use Oracle Connection Manager to multiplex network connections. For information about Oracle Connection Manager, see [Oracle Database Net Services Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=NETRF-GUID-C74FD877-06D2-44EF-A506-F7CAE9141B36)

### Manageability

PL/SQL stored subprograms increase manageability because you can maintain only one copy of a subprogram, on the database server, rather than one copy on each client system.

Any number of applications can use the subprograms, and you can change the subprograms without affecting the applications that invoke them. For more information about subprograms, see " [Subprograms](main-features-pl-sql.md) ".

### Support for Object-Oriented Programming

PL/SQL allows defining object types that can be used in object-oriented designs.

PL/SQL supports object-oriented programming with " [Abstract Data Types](main-features-pl-sql.md) ".