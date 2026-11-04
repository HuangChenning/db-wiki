---
title: SQLCODE Function
book: PL/SQL Language Reference
doc_id: E25519-13
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e25519/sqlcode_function.htm
tags:
  - oracle
  - 11g
  - pl-sql-language-reference
---

In an exception handler, the `SQLCODE` function returns the numeric code of the exception being handled. (Outside an exception handler, `SQLCODE` returns `0`.)

For an internally defined exception, the numeric code is the number of the associated Oracle Database error. This number is negative except for the error "no data found", whose numeric code is +100.

For a user-defined exception, the numeric code is either +1 (default) or the error code associated with the exception by the `EXCEPTION_INIT` pragma.

A SQL statement cannot invoke `SQLCODE`.

If a function invokes `SQLCODE`, and you use the `RESTRICT_REFERENCES` pragma to assert the purity of the function, then you cannot specify the constraints `WNPS` and `RNPS`.

Topics

- Syntax
- Examples
- Related Topics

Syntax

sqlcode\_function::=

  
[Description of the illustration sqlcode\_function.gif](https://docs.oracle.com/cd/E11882_01/appdev.112/e25519/img_text/sqlcode_function.htm)  

Examples

- [Example 11-22, "Displaying SQLCODE and SQLERRM Values"](errors.md)

Related Topics

In this chapter:

- ["Block"](block.md)
- ["EXCEPTION\_INIT Pragma"](exceptioninit_pragma.md)
- ["Exception Handler"](exception_handler.md)
- ["RESTRICT\_REFERENCES Pragma"](restrictreferences_pragma.md)
- ["SQLERRM Function"](sqlerrm_function.md)

In other chapters:

- ["Error Code and Error Message Retrieval"](errors.md)

See Also:

[Oracle Database Error Messages](https://docs.oracle.com/cd/E11882_01/server.112/e17766/toc.htm) for a list of Oracle Database error messages and information about them, including their numbers