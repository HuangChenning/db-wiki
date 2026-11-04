---
title: Database PL/SQL Language Reference
book: Database PL/SQL Language Reference
doc_id: E96448-09
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/unhandled-exceptions.html
tags:
  - oracle
  - 19c
  - pl-sql-language-reference
---

## Unhandled Exceptions

If there is no handler for a raised exception, PL/SQL returns an unhandled exception error to the invoker or host environment, which determines the outcome.

If a stored subprogram exits with an unhandled exception, PL/SQL does not roll back database changes made by the subprogram.

The `FORALL` statement runs one DML statement multiple times, with different values in the `VALUES` and `WHERE` clauses. If one set of values raises an unhandled exception, then PL/SQL rolls back all database changes made earlier in the `FORALL` statement. For more information, see " [Handling FORALL Exceptions Immediately](bulk-sql-and-bulk-binding.md) " and " [Handling FORALL Exceptions After FORALL Statement Completes](bulk-sql-and-bulk-binding.md) ".

Tip:

Avoid unhandled exceptions by including an `OTHERS` exception handler at the top level of every PL/SQL program.