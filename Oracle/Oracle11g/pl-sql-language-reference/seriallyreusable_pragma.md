---
title: SERIALLY_REUSABLE Pragma
book: PL/SQL Language Reference
doc_id: E25519-13
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e25519/seriallyreusable_pragma.htm
tags:
  - oracle
  - 11g
  - pl-sql-language-reference
---

The `SERIALLY_REUSABLE` pragma specifies that the package state is needed for only one call to the server (for example, an OCI call to the database or a stored procedure invocation through a database link). After this call, the storage for the package variables can be reused, reducing the memory overhead for long-running sessions.

This pragma is appropriate for packages that declare large temporary work areas that are used once in the same session.

The `SERIALLY_REUSABLE` pragma can appear in the `declare_section` of the specification of a bodiless package, or in both the specification and body of a package, but not in only the body of a package.

Topics

Syntax

serially\_resuable\_pragma::=

  
[Description of the illustration serially\_reusable\_pragma.gif](https://docs.oracle.com/cd/E11882_01/appdev.112/e25519/img_text/serially_reusable_pragma.htm)