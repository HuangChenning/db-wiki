---
title: Database PL/SQL Language Reference
book: Database PL/SQL Language Reference
doc_id: F31827-07
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/lnpls/EXCEPTION_INIT-pragma.html
tags:
  - oracle
  - 21c
  - pl-sql-language-reference
---

The `EXCEPTION_INIT` pragma associates a user-defined exception name with an error code.

The `EXCEPTION_INIT` pragma can appear only in the same declarative part as its associated exception, anywhere after the exception declaration.

Topics

Syntax

exception\_init\_pragma::=

![exception_init_pragma](img/exception_init_pragma.gif)

> ```
> PRAGMA EXCEPTION_INIT ( exception, error_code ) ;
> ```
>
> ![Oracle Logo](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/gifs/oracle.gif)[  
> Copyright © 1996, 2024, Oracle and/or its affiliates.](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/html/cpyr.htm)


Semantics

exception\_init\_pragma

exception

Name of a previously declared user-defined exception.

error\_code

Error code to be associated with `exception`. `error_code` can be either 100 (the numeric code for "no data found" that " [SQLCODE Function](SQLCODE-function.md) " returns) or any negative integer greater than -1000000 except -1403 (another numeric code for "no data found").

Note:

`NO_DATA_FOUND` is a predefined exception.

If two `EXCEPTION_INIT` pragmas assign different error codes to the same user-defined exception, then the later pragma overrides the earlier pragma.

Usage Notes

The `EXCEPTION_INIT` pragma should only be used to associate an exception with an error number that is already meaningfully defined by Oracle. Note that any error number may be used by Oracle in the future, which can create conflicts with unrelated application use of that number.

Negative integers greater than -65536 are only partially supported. Currently, if left unhandled beyond the current layer of entry into PL/SQL, the exception is converted to `ORA-6515` and the original exception is not recognized in the outer PL/SQL layer or client program.

Application-declared exceptions that are only raised and caught locally within a layer of entry into PL/SQL do not need the `EXCEPTION_INIT` pragma. The `RAISE_APPLICATION_ERROR` procedure and associated -20000 to -20999 range of error numbers should be used by application-declared exceptions that are intended to be recognizable in outer PL/SQL layers or in the client program.

Examples

- [Example 12-5](plsql-error-handling.md), "Naming Internally Defined Exception"
- [Example 12-13](plsql-error-handling.md), "Raising User-Defined Exception with RAISE\_APPLICATION\_ERROR"
- [Example 13-13](plsql-optimization-and-tuning.md), "Handling FORALL Exceptions After FORALL Statement Completes"