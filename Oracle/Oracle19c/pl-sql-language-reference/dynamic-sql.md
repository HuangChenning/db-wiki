---
title: Database PL/SQL Language Reference
book: Database PL/SQL Language Reference
doc_id: E96448-09
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/dynamic-sql.html
tags:
  - oracle
  - 19c
  - pl-sql-language-reference
---

## 7 PL/SQL Dynamic SQL

Dynamic SQL is a programming methodology for generating and running SQL statements at run time.

It is useful when writing general-purpose and flexible programs like ad hoc query systems, when writing programs that must run database definition language (DDL) statements, or when you do not know at compile time the full text of a SQL statement or the number or data types of its input and output variables.

PL/SQL provides two ways to write dynamic SQL:

- Native dynamic SQL, a PL/SQL language (that is, native) feature for building and running dynamic SQL statements
- `DBMS_SQL` package, an API for building, running, and describing dynamic SQL statements

Native dynamic SQL code is easier to read and write than equivalent code that uses the `DBMS_SQL` package, and runs noticeably faster (especially when it can be optimized by the compiler). However, to write native dynamic SQL code, you must know at compile time the number and data types of the input and output variables of the dynamic SQL statement. If you do not know this information at compile time, you must use the `DBMS_SQL` package. You must also use the `DBMS_SQL` package if you want a stored subprogram to return a query result implicitly (not through an `OUT` `REF` `CURSOR` parameter).

When you need both the `DBMS_SQL` package and native dynamic SQL, you can switch between them, using the " [DBMS\_SQL.TO\_REFCURSOR Function](dbms_sql-package.md) " and " [DBMS\_SQL.TO\_CURSOR\_NUMBER Function](dbms_sql-package.md) ".

Topics