---
title: INLINE Pragma
book: PL/SQL Language Reference
doc_id: E25519-13
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e25519/inline_pragma.htm
tags:
  - oracle
  - 11g
  - pl-sql-language-reference
---

The `INLINE` pragma specifies whether a subprogram invocation is to be inlined. Inlining replaces a subprogram invocation with a copy of the invoked subprogram (if the invoked and invoking subprograms are in the same program unit).

Note:

The `INLINE` pragma affects only the immediately following declaration or statement, and only some kinds of statements. For details, see ["Subprogram Inlining"](tuning.md).

Topics

Syntax

inline\_pragma::=

![inline_pragma](img/inline_pragma.gif)

> ```
> PRAGMA INLINE ( subprogram , { 'YES' | 'NO' } ) ;
> ```
>
> [Copyright © 1996, 2014, Oracle and/or its affiliates. All rights reserved.](https://docs.oracle.com/cd/E11882_01/dcommon/html/cpyr.htm)
  

Semantics

subprogram

Name of a subprogram. If `subprogram` is overloaded, then the `INLINE` pragma applies to every subprogram with that name.

YES

If `PLSQL_OPTIMIZE_LEVEL=2`, `'YES'` specifies that the subprogram invocation is to be inlined.

If `PLSQL_OPTIMIZE_LEVEL=3`, `'YES'` specifies that the subprogram invocation has a high priority for inlining.

NO

Specifies that the subprogram invocation is not to be inlined.

Examples

- [Example 12-1, "Specifying that Subprogram Is To Be Inlined"](tuning.md)
- [Example 12-2, "Specifying that Overloaded Subprogram Is To Be Inlined"](tuning.md)
- [Example 12-3, "Specifying that Subprogram Is Not To Be Inlined"](tuning.md)
- [Example 12-4, "PRAGMA INLINE... 'NO' Overrides PRAGMA INLINE... 'YES'"](tuning.md)