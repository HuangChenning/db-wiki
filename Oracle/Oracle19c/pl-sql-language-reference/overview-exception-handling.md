---
title: Database PL/SQL Language Reference
book: Database PL/SQL Language Reference
doc_id: E96448-09
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/overview-exception-handling.html
tags:
  - oracle
  - 19c
  - pl-sql-language-reference
---

## Overview of Exception Handling

Exceptions (PL/SQL runtime errors) can arise from design faults, coding mistakes, hardware failures, and many other sources. You cannot anticipate all possible exceptions, but you can write exception handlers that let your program to continue to operate in their presence.

Any PL/SQL block can have an exception-handling part, which can have one or more exception handlers. For example, an exception-handling part could have this syntax:

```
EXCEPTION
  WHEN ex_name_1 THEN statements_1                 -- Exception handler
  WHEN ex_name_2 OR ex_name_3 THEN statements_2  -- Exception handler
  WHEN OTHERS THEN statements_3                      -- Exception handler
END;
```

In the preceding syntax example, `ex_name_` `n` is the name of an exception and `statements_` `n` is one or more statements. (For complete syntax and semantics, see " [Exception Handler](exception-handler.md) ".)

When an exception is raised in the executable part of the block, the executable part stops and control transfers to the exception-handling part. If `ex_name_1` was raised, then `statements_1` run. If either `ex_name_2` or `ex_name_3` was raised, then `statements_2` run. If any other exception was raised, then `statements_3` run.

After an exception handler runs, control transfers to the next statement of the enclosing block. If there is no enclosing block, then:

- If the exception handler is in a subprogram, then control returns to the invoker, at the statement after the invocation.
- If the exception handler is in an anonymous block, then control transfers to the host environment (for example, SQL\*Plus)

If an exception is raised in a block that has no exception handler for it, then the exception propagates. That is, the exception reproduces itself in successive enclosing blocks until a block has a handler for it or there is no enclosing block (for more information, see " [Exception Propagation](exception-propagation.md) "). If there is no handler for the exception, then PL/SQL returns an unhandled exception error to the invoker or host environment, which determines the outcome (for more information, see " [Unhandled Exceptions](unhandled-exceptions.md) ").

Topics

### Exception Categories

The exception categories are:

- Internally defined
	The runtime system raises internally defined exceptions implicitly (automatically). Examples of internally defined exceptions are ORA-00060 (deadlock detected while waiting for resource) and ORA-27102 (out of memory).
	An internally defined exception always has an error code, but does not have a name unless PL/SQL gives it one or you give it one.
	For more information, see " [Internally Defined Exceptions](internally-defined-exceptions.md) ".
- Predefined
	A predefined exception is an internally defined exception that PL/SQL has given a name. For example, ORA-06500 (PL/SQL: storage error) has the predefined name `STORAGE_ERROR`.
	For more information, see " [Predefined Exceptions](predefined-exceptions.md) ".
- User-defined
	You can declare your own exceptions in the declarative part of any PL/SQL anonymous block, subprogram, or package. For example, you might declare an exception named `insufficient_funds` to flag overdrawn bank accounts.
	You must raise user-defined exceptions explicitly.
	For more information, see " [User-Defined Exceptions](user-defined-exceptions.md) ".

Table 11-2 summarizes the exception categories.

Table 11-2 Exception Categories

| Category | Definer | Has Error Code | Has Name | Raised Implicitly | Raised Explicitly |
| --- | --- | --- | --- | --- | --- |
| Internally defined | Runtime system | Always | Only if you assign one | Yes | Optionally <sup>Foot 1</sup> |
| Predefined | Runtime system | Always | Always | Yes | Optionally <sup>Foot 1</sup> |
| User-defined | User | Only if you assign one | Always | No | Always |

<sup>Footnote 1</sup>

For details, see " [Raising Internally Defined Exception with RAISE Statement](raising-exceptions-explicitly.md) ".

For a named exception, you can write a specific exception handler, instead of handling it with an `OTHERS` exception handler. A specific exception handler is more efficient than an `OTHERS` exception handler, because the latter must invoke a function to determine which exception it is handling. For details, see " [Retrieving Error Code and Error Message](retrieving-error-code-and-error-message.md) ".

### Advantages of Exception Handlers

Using exception handlers for error-handling makes programs easier to write and understand, and reduces the likelihood of unhandled exceptions.

Without exception handlers, you must check for every possible error, everywhere that it might occur, and then handle it. It is easy to overlook a possible error or a place where it might occur, especially if the error is not immediately detectable (for example, bad data might be undetectable until you use it in a calculation). Error-handling code is scattered throughout the program.

With exception handlers, you need not know every possible error or everywhere that it might occur. You need only include an exception-handling part in each block where errors might occur. In the exception-handling part, you can include exception handlers for both specific and unknown errors. If an error occurs anywhere in the block (including inside a sub-block), then an exception handler handles it. Error-handling code is isolated in the exception-handling parts of the blocks.

In Example 11-3, a procedure uses a single exception handler to handle the predefined exception `NO_DATA_FOUND`, which can occur in either of two `SELECT` `INTO` statements.

If multiple statements use the same exception handler, and you want to know which statement failed, you can use locator variables, as in Example 11-4.

You determine the precision of your error-handling code. You can have a single exception handler for all division-by-zero errors, bad array indexes, and so on. You can also check for errors in a single statement by putting that statement inside a block with its own exception handler.

Example 11-3 Single Exception Handler for Multiple Exceptions

```
CREATE OR REPLACE PROCEDURE select_item (
  t_column VARCHAR2,
  t_name   VARCHAR2
) AUTHID DEFINER
IS
  temp VARCHAR2(30);
BEGIN
  temp := t_column;  -- For error message if next SELECT fails
 
  -- Fails if table t_name does not have column t_column:
 
  SELECT COLUMN_NAME INTO temp
  FROM USER_TAB_COLS 
  WHERE TABLE_NAME = UPPER(t_name)
  AND COLUMN_NAME = UPPER(t_column);
 
  temp := t_name;  -- For error message if next SELECT fails
 
  -- Fails if there is no table named t_name:
 
  SELECT OBJECT_NAME INTO temp
  FROM USER_OBJECTS
  WHERE OBJECT_NAME = UPPER(t_name)
  AND OBJECT_TYPE = 'TABLE';
 
EXCEPTION
  WHEN NO_DATA_FOUND THEN
    DBMS_OUTPUT.PUT_LINE ('No Data found for SELECT on ' || temp);
  WHEN OTHERS THEN
    DBMS_OUTPUT.PUT_LINE ('Unexpected error');
    RAISE;
END;
/
```

Invoke procedure (there is a `DEPARTMENTS` table, but it does not have a `LAST_NAME` column):

```
BEGIN
  select_item('departments', 'last_name');
END;
/
```

Result:

```
No Data found for SELECT on departments
```

Invoke procedure (there is no `EMP` table):

```
BEGIN
  select_item('emp', 'last_name');
END;
/
```

Result:

```
No Data found for SELECT on emp
```

Example 11-4 Locator Variables for Statements that Share Exception Handler

```
CREATE OR REPLACE PROCEDURE loc_var AUTHID DEFINER IS
  stmt_no  POSITIVE;
  name_    VARCHAR2(100);
BEGIN
  stmt_no := 1;

  SELECT table_name INTO name_
  FROM user_tables
  WHERE table_name LIKE 'ABC%';

  stmt_no := 2;

  SELECT table_name INTO name_
  FROM user_tables
  WHERE table_name LIKE 'XYZ%';
EXCEPTION
  WHEN NO_DATA_FOUND THEN
    DBMS_OUTPUT.PUT_LINE ('Table name not found in query ' || stmt_no);
END;
/
CALL loc_var();
```

Result:

```
Table name not found in query 1
```

### Guidelines for Avoiding and Handling Exceptions

To make your programs as reliable and safe as possible:

- Use both error-checking code and exception handlers.
	Use error-checking code wherever bad input data can cause an error. Examples of bad input data are incorrect or null actual parameters and queries that return no rows or more rows than you expect. Test your code with different combinations of bad input data to see what potential errors arise.
	Sometimes you can use error-checking code to avoid raising an exception, as in [Example 11-7](predefined-exceptions.md).
- Add exception handlers wherever errors can occur.
	Errors are especially likely during arithmetic calculations, string manipulation, and database operations. Errors can also arise from problems that are independent of your code—for example, disk storage or memory hardware failure—but your code still must take corrective action.
- Design your programs to work when the database is not in the state you expect.
	For example, a table you query might have columns added or deleted, or their types might have changed. You can avoid problems by declaring scalar variables with `%TYPE` qualifiers and record variables to hold query results with `%ROWTYPE` qualifiers.
- Whenever possible, write exception handlers for named exceptions instead of using `OTHERS` exception handlers.
	Learn the names and causes of the predefined exceptions. If you know that your database operations might raise specific internally defined exceptions that do not have names, then give them names so that you can write exception handlers specifically for them.
- Have your exception handlers output debugging information.
	If you store the debugging information in a separate table, do it with an autonomous routine, so that you can commit your debugging information even if you roll back the work that the main subprogram did. For information about autonomous routines, see " [AUTONOMOUS\_TRANSACTION Pragma](AUTONOMOUS_TRANSACTION-pragma.md) ".
- For each exception handler, carefully decide whether to have it commit the transaction, roll it back, or let it continue.
	Regardless of the severity of the error, you want to leave the database in a consistent state and avoid storing bad data.
- Avoid unhandled exceptions by including an `OTHERS` exception handler at the top level of every PL/SQL program.
	Make the last statement in the `OTHERS` exception handler either `RAISE` or an invocation of the `RAISE_APPLICATION_ERROR` procedure. (If you do not follow this practice, and PL/SQL warnings are enabled, then you get PLW-06009.) For information about `RAISE` or an invocation of the `RAISE_APPLICATION_ERROR`, see " [Raising Exceptions Explicitly](raising-exceptions-explicitly.md) ".