---
title: Database PL/SQL Language Reference
book: Database PL/SQL Language Reference
doc_id: E96448-09
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/pl-sql-functions-that-sql-statements-can-invoke.html
tags:
  - oracle
  - 19c
  - pl-sql-language-reference
---

## PL/SQL Functions that SQL Statements Can Invoke

To be invocable from SQL statements, a stored function (and any subprograms that it invokes) must obey the following purity rules, which are meant to control side effects:

- When invoked from a `SELECT` statement or a parallelized `INSERT`, `UPDATE`, `DELETE`, or `MERGE` statement, the subprogram cannot modify any database tables.
- When invoked from an `INSERT`, `UPDATE`, `DELETE`, or `MERGE` statement, the subprogram cannot query or modify any database tables modified by that statement.
	If a function either queries or modifies a table, and a DML statement on that table invokes the function, then ORA-04091 (mutating-table error) occurs. There is one exception: ORA-04091 does not occur if a single-row `INSERT` statement that is not in a `FORALL` statement invokes the function in a `VALUES` clause.
- When invoked from a `SELECT`, `INSERT`, `UPDATE`, `DELETE`, or `MERGE` statement, the subprogram cannot execute any of the following SQL statements (unless `PRAGMA` `AUTONOMOUS_TRANSACTION` was specified):
	- Transaction control statements (such as `COMMIT`)
		- Session control statements (such as `SET` `ROLE`)
		- System control statements (such as `ALTER` `SYSTEM`)
		- Database definition language (DDL) statements (such as `CREATE`), which are committed automatically
	(For the description of `PRAGMA` `AUTONOMOUS_TRANSACTION`, see " [AUTONOMOUS\_TRANSACTION Pragma](AUTONOMOUS_TRANSACTION-pragma.md) ".)

If any SQL statement in the execution part of the function violates a rule, then a runtime error occurs when that statement is parsed.

The fewer side effects a function has, the better it can be optimized in a `SELECT` statement, especially if the function is declared with the option `DETERMINISTIC` or `PARALLEL_ENABLE` (for descriptions of these options, see " [DETERMINISTIC Clause](DETERMINISTIC-clause.md) " and " [PARALLEL\_ENABLE Clause](PARALLEL_ENABLE-clause.md) ").

See Also:

- [Oracle Database Development Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=ADFNS00908) for information about restrictions on PL/SQL functions that SQL statements can invoke
- " [Tune Function Invocations in Queries](minimizing-cpu-overhead.md) "