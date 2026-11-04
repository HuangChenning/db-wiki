---
title: Database PL/SQL Language Reference
book: Database PL/SQL Language Reference
doc_id: E96448-09
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/restrictions-record-inserts-and-updates.html
tags:
  - oracle
  - 19c
  - pl-sql-language-reference
---

## Restrictions on Record Inserts and Updates

These restrictions apply to record inserts and updates:

- Record variables are allowed only in these places:
	- On the right side of the `SET` clause in an `UPDATE` statement
		- In the `VALUES` clause of an `INSERT` statement
		- In the `INTO` subclause of a `RETURNING` clause
	Record variables are not allowed in a `SELECT` list, `WHERE` clause, `GROUP` `BY` clause, or `ORDER` `BY` clause.
- The keyword `ROW` is allowed only on the left side of a `SET` clause. Also, you cannot use `ROW` with a subquery.
- In an `UPDATE` statement, only one `SET` clause is allowed if `ROW` is used.
- If the `VALUES` clause of an `INSERT` statement contains a record variable, no other variable or value is allowed in the clause.
- If the `INTO` subclause of a `RETURNING` clause contains a record variable, no other variable or value is allowed in the subclause.
- These are not supported:
	- Nested `RECORD` types
		- Functions that return a `RECORD` type
		- Record inserts and updates using the `EXECUTE` `IMMEDIATE` statement.