---
title: Database PL/SQL Language Reference
book: Database PL/SQL Language Reference
doc_id: E96448-09
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/plsql-name-resolution.html
tags:
  - oracle
  - 19c
  - pl-sql-language-reference
---

## B PL/SQL Name Resolution

This appendix explains PL/SQL name resolution; that is, how the PL/SQL compiler resolves ambiguous references to identifiers.

An unambiguous identifier reference can become ambiguous if you change identifiers in its compilation unit (that is, if you add, rename, or delete identifiers).

Note:

The `AUTHID` property of a stored PL/SQL unit affects the name resolution of SQL statements that the unit issues at run time. For more information, see " [Invoker's Rights and Definer's Rights (AUTHID Property)](invokers-rights-and-definers-rights-authid-property.md) ".

Topics

- [Qualified Names and Dot Notation](qualified-names-and-dot-notation.md)
- [Column Name Precedence](column-name-precedence.md)
- [Differences Between PL/SQL and SQL Name Resolution Rules](differences-pl-sql-and-sql-name-resolution-rules.md)
- [Resolution of Names in Static SQL Statements](resolution-names-static-sql-statements.md)
- [What is Capture?](what-is-capture.md)
- [Avoiding Inner Capture in SELECT and DML Statements](avoiding-inner-capture-select-and-dml-statements.md)