---
title: Database PL/SQL Language Reference
book: Database PL/SQL Language Reference
doc_id: E96448-09
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/internally-defined-exceptions.html
tags:
  - oracle
  - 19c
  - pl-sql-language-reference
---

## Internally Defined Exceptions

Internally defined exceptions (ORA-n errors) are described in [Oracle Database Error Messages Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=ERRMG-GUID-27437B7F-F0C3-4F1F-9C6E-6780706FB0F6). The runtime system raises them implicitly (automatically).

An internally defined exception does not have a name unless either PL/SQL gives it one (see " [Predefined Exceptions](predefined-exceptions.md) ") or you give it one.

If you know that your database operations might raise specific internally defined exceptions that do not have names, then give them names so that you can write exception handlers specifically for them. Otherwise, you can handle them only with `OTHERS` exception handlers.

To give a name to an internally defined exception, do the following in the declarative part of the appropriate anonymous block, subprogram, or package. (To determine the appropriate block, see " [Exception Propagation](exception-propagation.md) ".)

1. Declare the name.
	An exception name declaration has this syntax:
	```
	exception_name EXCEPTION;
	```
	For semantic information, see " [Exception Declaration](exception-declaration.md) ".
2. Associate the name with the error code of the internally defined exception.
	The syntax is:
	```
	PRAGMA EXCEPTION_INIT (exception_name, error_code)
	```
	For semantic information, see " [EXCEPTION\_INIT Pragma](EXCEPTION_INIT-pragma.md) ".

Note:

An internally defined exception with a user-declared name is still an internally defined exception, not a user-defined exception.

Example 11-5 gives the name `deadlock_detected` to the internally defined exception ORA-00060 (deadlock detected while waiting for resource) and uses the name in an exception handler.

See Also:

" [Raising Internally Defined Exception with RAISE Statement](raising-exceptions-explicitly.md) "

Example 11-5 Naming Internally Defined Exception

```
DECLARE
  deadlock_detected EXCEPTION;
  PRAGMA EXCEPTION_INIT(deadlock_detected, -60);
BEGIN
  ...
EXCEPTION
  WHEN deadlock_detected THEN
    ...
END;
/
```