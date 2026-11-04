---
title: Database PL/SQL Language Reference
book: Database PL/SQL Language Reference
doc_id: E96448-09
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/SERIALLY_REUSABLE-pragma.html
tags:
  - oracle
  - 19c
  - pl-sql-language-reference
---

## SERIALLY\_REUSABLE Pragma

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
> Copyright © 1996, 2026, Oracle and/or its affiliates.](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/html/cpyr.htm)


Examples

- [Example 10-4](serially_reusable-packages.md), "Creating SERIALLY\_REUSABLE Packages"
- [Example 10-5](serially_reusable-packages.md), "Effect of SERIALLY\_REUSABLE Pragma"
- [Example 10-6](serially_reusable-packages.md), "Cursor in SERIALLY\_REUSABLE Package Open at Call Boundary"