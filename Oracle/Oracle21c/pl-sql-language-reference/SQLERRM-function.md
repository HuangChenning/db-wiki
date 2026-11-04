---
title: Database PL/SQL Language Reference
book: Database PL/SQL Language Reference
doc_id: F31827-07
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/lnpls/SQLERRM-function.html
tags:
  - oracle
  - 21c
  - pl-sql-language-reference
---

The `SQLERRM` function returns the error message associated with an error code.

Note:

The language of the error message depends on the `NLS_LANGUAGE` parameter. For information about this parameter, see [Oracle Database Globalization Support Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/lnpls&id=NLSPG199).

A SQL statement cannot invoke `SQLERRM`.

If a function invokes `SQLERRM`, and you use the `RESTRICT_REFERENCES` pragma to assert the purity of the function, then you cannot specify the constraints `WNPS` and `RNPS`.

Note:

`DBMS_UTILITY`.`FORMAT_ERROR_STACK` is recommended over `SQLERRM`, unless you use the `FORALL` statement with its `SAVE` `EXCEPTIONS` clause. For more information, see " [Retrieving Error Code and Error Message](plsql-error-handling.md) ".

Topics

Syntax

sqlerrm\_function::=

![sqlerrm_function](img/sqlerrm_function.gif)

> ```
> SQLERRM [ ( error_code ) ]
> ```
>
> ![Oracle Logo](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/gifs/oracle.gif)[  
> Copyright © 1996, 2024, Oracle and/or its affiliates.](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/html/cpyr.htm)


Semantics

sqlerrm\_function

error\_code

Expression whose value is an Oracle Database error code.

Default: error code associated with the current value of `SQLCODE`.

Like `SQLCODE`, `SQLERRM` without `error_code` is useful only in an exception handler. Outside an exception handler, or if the value of `error_code` is zero, `SQLERRM` returns ORA-0000.

If the value of `error_code` is +100, `SQLERRM` returns ORA-01403.

If the value of `error_code` is a positive number other than +100, `SQLERRM` returns this message:

```
-error_code: non-ORACLE exception
```

If the value of `error_code` is a negative number whose absolute value is an Oracle Database error code, `SQLERRM` returns the error message associated with that error code. For example:

```
BEGIN
  DBMS_OUTPUT.PUT_LINE('SQLERRM(-6511): ' || TO_CHAR(SQLERRM(-6511)));
END;
/
```

Result:

```
SQLERRM(-6511): ORA-06511: PL/SQL: cursor already open
```

If the value of `error_code` is a negative number whose absolute value is not an Oracle Database error code, `SQLERRM` returns this message:

```
ORA-error_code: Message error_code not found; product=RDBMS;
facility=ORA
```

For example:

```
BEGIN
  DBMS_OUTPUT.PUT_LINE('SQLERRM(-50000): ' || TO_CHAR(SQLERRM(-50000)));
END;
/
```

Result:

```
SQLERRM(-50000): ORA-50000: Message 50000 not found; product=RDBMS;
facility=ORA
```

Examples

- [Example 12-23](plsql-error-handling.md), "Displaying SQLCODE and SQLERRM Values"
- [Example 13-13](plsql-optimization-and-tuning.md), "Handling FORALL Exceptions After FORALL Statement Completes"
- [Example 13-13](plsql-optimization-and-tuning.md), "Handling FORALL Exceptions After FORALL Statement Completes"

Related Topics

In this chapter:

- " [Block](block.md) "
- " [EXCEPTION\_INIT Pragma](EXCEPTION_INIT-pragma.md) "
- " [RESTRICT\_REFERENCES Pragma](RESTRICT_REFERENCES-pragma.md) "
- " [SQLCODE Function](SQLCODE-function.md) "

In other chapters:

- " [Retrieving Error Code and Error Message](plsql-error-handling.md) "

See Also:

[Oracle Database Error Messages Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/lnpls&id=ERRMG-GUID-27437B7F-F0C3-4F1F-9C6E-6780706FB0F6) for a list of Oracle Database error messages and information about them