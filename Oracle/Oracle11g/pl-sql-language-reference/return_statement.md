---
title: RETURN Statement
book: PL/SQL Language Reference
doc_id: E25519-13
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e25519/return_statement.htm
tags:
  - oracle
  - 11g
  - pl-sql-language-reference
---

The `RETURN` statement immediately ends the execution of the subprogram or anonymous block that contains it.

In a function, the `RETURN` statement assigns a specified value to the function identifier and returns control to the invoker, where execution resumes immediately after the invocation (possibly inside the invoking statement). Every execution path in a function must lead to a `RETURN` statement (otherwise, the PL/SQL compiler issues compile-time warning PLW-05005).

In a procedure, the `RETURN` statement returns control to the invoker, where execution resumes immediately after the invocation.

In an anonymous block, the `RETURN` statement exits its own block and all enclosing blocks.

A subprogram or anonymous block can contain multiple `RETURN` statements.

Note:

The `RETURN` statement differs from the `RETURN` clause in a function heading, which specifies the data type of the return value.

Topics

- Syntax
- Semantics
- Examples
- Related Topics

Syntax

return\_statement::=

![return_statement](img/return_statement.gif)

> ```
> RETURN [ expression ] ;
> ```
>
> [Copyright © 1996, 2014, Oracle and/or its affiliates. All rights reserved.](https://docs.oracle.com/cd/E11882_01/dcommon/html/cpyr.htm)
  

See ["expression::="](expression.md).

Semantics

expression

Optional when the `RETURN` statement is in a pipelined table function. Required when the `RETURN` statement is in any other function. Not allowed when the `RETURN` statement is in a procedure or anonymous block.

The `RETURN` statement assigns the value of `expression` to the function identifier. Therefore, the data type of `expression` must be compatible with the data type in the `RETURN` clause of the function. For information about expressions, see ["Expression"](expression.md).

Examples

- [Example 8-3, "Execution Resumes After RETURN Statement in Function"](subprograms.md)
- [Example 8-4, "Function Where Not Every Execution Path Leads to RETURN Statement"](subprograms.md)
- [Example 8-5, "Function Where Every Execution Path Leads to RETURN Statement"](subprograms.md)
- [Example 8-6, "Execution Resumes After RETURN Statement in Procedure"](subprograms.md)
- [Example 8-7, "Execution Resumes After RETURN Statement in Anonymous Block"](subprograms.md)