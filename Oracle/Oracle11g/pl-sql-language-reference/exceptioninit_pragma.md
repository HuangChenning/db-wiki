---
title: EXCEPTION_INIT Pragma
book: PL/SQL Language Reference
doc_id: E25519-13
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e25519/exceptioninit_pragma.htm
tags:
  - oracle
  - 11g
  - pl-sql-language-reference
---

The `EXCEPTION_INIT` pragma associates a user-defined exception name with an error code.

The `EXCEPTION_INIT` pragma can appear only in the same declarative part as its associated exception, anywhere after the exception declaration.

Topics

Syntax

exception\_init\_pragma::=

  
[Description of the illustration exception\_init\_pragma.gif](https://docs.oracle.com/cd/E11882_01/appdev.112/e25519/img_text/exception_init_pragma.htm)  

Semantics

exception

Name of a previously declared user-defined exception.

error\_code

Error code to be associated with `exception`. `error_code` can be either 100 (the numeric code for "no data found" that ["SQLCODE Function"](sqlcode_function.md) returns) or any negative integer greater than -10000000 except -1403 (another numeric code for "no data found").

Note:

`NO_DATA_FOUND` is a predefined exception.

If two `EXCEPTION_INIT` pragmas assign different error codes to the same user-defined exception, then the later pragma overrides the earlier pragma.