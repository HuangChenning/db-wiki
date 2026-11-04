---
title: Database PL/SQL Language Reference
book: Database PL/SQL Language Reference
doc_id: F31827-07
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/lnpls/INLINE-pragma.html
tags:
  - oracle
  - 21c
  - pl-sql-language-reference
---

The `INLINE` pragma specifies whether a subprogram invocation is to be inlined.

Inlining replaces a subprogram invocation with a copy of the invoked subprogram (if the invoked and invoking subprograms are in the same program unit).

Note:

The `INLINE` pragma affects only the immediately following declaration or statement, and only some kinds of statements. For details, see " [Subprogram Inlining](plsql-optimization-and-tuning.md) ".

Topics

Syntax

inline\_pragma::=

![inline_pragma](img/inline_pragma.gif)

> ```
> PRAGMA INLINE ( subprogram , { 'YES' | 'NO' } ) ;
> ```
>
> ![Oracle Logo](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/gifs/oracle.gif)[  
> Copyright © 1996, 2024, Oracle and/or its affiliates.](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/html/cpyr.htm)


Semantics

subprogram

Name of a subprogram. If `subprogram` is overloaded, then the `INLINE` pragma applies to every subprogram with that name.

YES

If `PLSQL_OPTIMIZE_LEVEL=2`, `'YES'` specifies that the subprogram invocation is to be inlined.

If `PLSQL_OPTIMIZE_LEVEL=3`, `'YES'` specifies that the subprogram invocation has a high priority for inlining.

NO

Specifies that the subprogram invocation is not to be inlined.

Examples

- [Example 13-1](plsql-optimization-and-tuning.md), "Specifying that Subprogram Is To Be Inlined"
- [Example 13-2](plsql-optimization-and-tuning.md), "Specifying that Overloaded Subprogram Is To Be Inlined"
- [Example 13-3](plsql-optimization-and-tuning.md), "Specifying that Subprogram Is Not To Be Inlined"
- [Example 13-4](plsql-optimization-and-tuning.md), "PRAGMA INLINE... 'NO' Overrides PRAGMA INLINE... 'YES'"