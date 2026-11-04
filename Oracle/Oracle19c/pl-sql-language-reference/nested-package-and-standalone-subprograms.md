---
title: Database PL/SQL Language Reference
book: Database PL/SQL Language Reference
doc_id: E96448-09
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/nested-package-and-standalone-subprograms.html
tags:
  - oracle
  - 19c
  - pl-sql-language-reference
---

## Nested, Package, and Standalone Subprograms

You can create a subprogram either inside a PL/SQL block (which can be another subprogram), inside a package, or at schema level.

A subprogram created inside a PL/SQL block is a nested subprogram. You can either declare and define it at the same time, or you can declare it first and then define it later in the same block (see " [Forward Declaration](forward-declaration.md) "). A nested subprogram is stored in the database only if it is nested in a standalone or package subprogram.

A subprogram created inside a package is a package subprogram. You declare it in the package specification and define it in the package body. It is stored in the database until you drop the package. (Packages are described in [PL/SQL Packages](plsql-packages.md).)

A subprogram created at schema level is a standalone subprogram. You create it with the `CREATE` `FUNCTION` or `CREATE` `PROCEDURE` statement. It is stored in the database until you drop it with the `DROP` `FUNCTION` or `DROP` `PROCEDURE` statement. (These statements are described in [SQL Statements for Stored PL/SQL Units](sql-statements-for-stored-plsql-units.md).)

A stored subprogram is either a package subprogram or a standalone subprogram. A stored subprogram is affected by the `AUTHID` and `ACCESSIBLE` `BY` clauses, which can appear in the `CREATE` `FUNCTION`, `CREATE` `PROCEDURE`, and `CREATE` `PACKAGE` statements. The `AUTHID` clause affects the name resolution and privilege checking of SQL statements that the subprogram issues at run time (for more information, see " [Invoker's Rights and Definer's Rights (AUTHID Property)](invokers-rights-and-definers-rights-authid-property.md) "). The `ACCESSIBLE` `BY` clause specifies a white list of PL/SQL units that can access the subprogram.