---
title: Database PL/SQL Language Reference
book: Database PL/SQL Language Reference
doc_id: F31827-07
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/lnpls/SERIALLY_REUSABLE-pragma.html
tags:
  - oracle
  - 21c
  - pl-sql-language-reference
---

The `SERIALLY_REUSABLE` pragma specifies that the package state is needed for only one call to the server (for example, an OCI call to the database or a stored procedure invocation through a database link).

After this call, the storage for the package variables can be reused, reducing the memory overhead for long-running sessions.

This pragma is appropriate for packages that declare large temporary work areas that are used once in the same session.

The `SERIALLY_REUSABLE` pragma can appear in the `declare_section` of the specification of a bodiless package, or in both the specification and body of a package, but not in only the body of a package.

Topics

Syntax

serially\_reusable\_pragma::=

![serially_reusable_pragma](img/serially_reusable_pragma.gif)

> ```
> PRAGMA SERIALLY_REUSABLE ;
> ```
>
> ![Oracle Logo](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/gifs/oracle.gif)[  
> Copyright © 1996, 2024, Oracle and/or its affiliates.](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/html/cpyr.htm)


Examples

- [Example 11-4](plsql-packages.md), "Creating SERIALLY\_REUSABLE Packages"
- [Example 11-5](plsql-packages.md), "Effect of SERIALLY\_REUSABLE Pragma"
- [Example 11-6](plsql-packages.md), "Cursor in SERIALLY\_REUSABLE Package Open at Call Boundary"