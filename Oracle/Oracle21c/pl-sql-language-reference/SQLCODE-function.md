---
title: Database PL/SQL Language Reference
book: Database PL/SQL Language Reference
doc_id: F31827-07
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/lnpls/SQLCODE-function.html
tags:
  - oracle
  - 21c
  - pl-sql-language-reference
---

In an exception handler, the `SQLCODE` function returns the numeric code of the exception being handled. (Outside an exception handler, `SQLCODE` returns `0`.)

For an internally defined exception, the numeric code is the number of the associated Oracle Database error. This number is negative except for the error "no data found", whose numeric code is +100.

For a user-defined exception, the numeric code is either +1 (default) or the error code associated with the exception by the `EXCEPTION_INIT` pragma.

A SQL statement cannot invoke `SQLCODE`.

If a function invokes `SQLCODE`, and you use the `RESTRICT_REFERENCES` pragma to assert the purity of the function, then you cannot specify the constraints `WNPS` and `RNPS`.

Topics

Syntax

sqlcode\_function::=

![sqlcode_function](img/sqlcode_function.gif)

> ```
> SQLCODE
> ```
>
> ![Oracle Logo](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/gifs/oracle.gif)[  
> Copyright © 1996, 2024, Oracle and/or its affiliates.](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/html/cpyr.htm)


Examples

- [Example 12-23](plsql-error-handling.md), "Displaying SQLCODE and SQLERRM Values"

Related Topics

In this chapter:

- " [Block](block.md) "
- " [EXCEPTION\_INIT Pragma](EXCEPTION_INIT-pragma.md) "
- " [Exception Handler](exception-handler.md) "
- " [RESTRICT\_REFERENCES Pragma](RESTRICT_REFERENCES-pragma.md) "
- " [SQLERRM Function](SQLERRM-function.md) "

In other chapters:

- " [Retrieving Error Code and Error Message](plsql-error-handling.md) "

See Also:

[Oracle Database Error Messages Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/lnpls&id=ERRMG-GUID-27437B7F-F0C3-4F1F-9C6E-6780706FB0F6) for a list of Oracle Database error messages and information about them, including their numbers