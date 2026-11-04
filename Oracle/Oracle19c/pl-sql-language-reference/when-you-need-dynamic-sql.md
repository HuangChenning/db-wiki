---
title: Database PL/SQL Language Reference
book: Database PL/SQL Language Reference
doc_id: E96448-09
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/when-you-need-dynamic-sql.html
tags:
  - oracle
  - 19c
  - pl-sql-language-reference
---

## When You Need Dynamic SQL

In PL/SQL, you need dynamic SQL to run:

- SQL whose text is unknown at compile time
	For example, a `SELECT` statement that includes an identifier that is unknown at compile time (such as a table name) or a `WHERE` clause in which the number of subclauses is unknown at compile time.
- SQL that is not supported as static SQL
	That is, any SQL construct not included in " [Description of Static SQL](description-static-sql.md) ".

If you do not need dynamic SQL, use static SQL, which has these advantages:

- Successful compilation verifies that static SQL statements reference valid database objects and that the necessary privileges are in place to access those objects.
- Successful compilation creates schema object dependencies.
	For information about schema object dependencies, see [Oracle Database Development Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=ADFNS99967).

For information about using static SQL statements with PL/SQL, see [PL/SQL Static SQL](static-sql.md).