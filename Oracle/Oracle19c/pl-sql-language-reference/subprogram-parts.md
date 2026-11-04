---
title: Database PL/SQL Language Reference
book: Database PL/SQL Language Reference
doc_id: E96448-09
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/subprogram-parts.html
tags:
  - oracle
  - 19c
  - pl-sql-language-reference
---

## Subprogram Parts

A subprogram begins with a subprogram heading, which specifies its name and (optionally) its parameter list.

Like an anonymous block, a subprogram has these parts:

- Declarative part (optional)
	This part declares and defines local types, cursors, constants, variables, exceptions, and nested subprograms. These items cease to exist when the subprogram completes execution.
	This part can also specify pragmas.
	Note:
	The declarative part of a subprogram does not begin with the keyword `DECLARE`, as the declarative part of an anonymous block does.
- Executable part (required)
	This part contains one or more statements that assign values, control execution, and manipulate data. (Early in the application design process, this part might contain only a `NULL` statement, as in [Example 4-35](sequential-control-statements.md).)
- Exception-handling part (optional)
	This part contains code that handles runtime errors.

Topics

- Additional Parts for Functions
- RETURN Statement

Example 8-1 Declaring, Defining, and Invoking a Simple PL/SQL Procedure

In this example, an anonymous block simultaneously declares and defines a procedure and invokes it three times. The third invocation raises the exception that the exception-handling part of the procedure handles.

```
DECLARE
  first_name employees.first_name%TYPE;
  last_name  employees.last_name%TYPE;
  email      employees.email%TYPE;
  employer   VARCHAR2(8) := 'AcmeCorp';
 
  -- Declare and define procedure
 
  PROCEDURE create_email (  -- Subprogram heading begins
    name1   VARCHAR2,
    name2   VARCHAR2,
    company VARCHAR2
  )                         -- Subprogram heading ends
  IS
                            -- Declarative part begins
    error_message VARCHAR2(30) := 'Email address is too long.';
  BEGIN                     -- Executable part begins
    email := name1 || '.' || name2 || '@' || company;
  EXCEPTION                      -- Exception-handling part begins
    WHEN VALUE_ERROR THEN
      DBMS_OUTPUT.PUT_LINE(error_message);
  END create_email;
 
BEGIN
  first_name := 'John';
  last_name  := 'Doe';
 
  create_email(first_name, last_name, employer);  -- invocation
  DBMS_OUTPUT.PUT_LINE ('With first name first, email is: ' || email);
 
  create_email(last_name, first_name, employer);  -- invocation
  DBMS_OUTPUT.PUT_LINE ('With last name first, email is: ' || email);
 
  first_name := 'Elizabeth';
  last_name  := 'MacDonald';
  create_email(first_name, last_name, employer);  -- invocation
END;
/
```

Result:

```
With first name first, email is: John.Doe@AcmeCorp
With last name first, email is: Doe.John@AcmeCorp
Email address is too long.
```

### Additional Parts for Functions

A function has the same structure as a procedure, except that:

- A function heading must include a `RETURN` clause, which specifies the data type of the value that the function returns. (A procedure heading cannot have a `RETURN` clause.)
- In the executable part of a function, every execution path must lead to a `RETURN` statement. Otherwise, the PL/SQL compiler issues a compile-time warning. (In a procedure, the `RETURN` statement is optional and not recommended. For details, see " RETURN Statement ".)
- A function declaration can include these options:

| Option | Description |
| --- | --- |
| `DETERMINISTIC` option | Helps the optimizer avoid redundant function invocations. |
| `PARALLEL_ENABLE` option | Enables the function for parallel execution, making it safe for use in concurrent sessions of parallel DML evaluations. |
| `PIPELINED` option | Makes a table function pipelined, for use as a row source. |
| `RESULT_CACHE` option | Stores function results in the PL/SQL function result cache. |

See Also:

- " [Function Declaration and Definition](function-declaration-and-definition.md) " for the syntax of function declarations and definitions, including descriptions of the items in the preceding table
- " [PL/SQL Function Result Cache](pl-sql-function-result-cache.md) " for more information about the `RESULT_CACHE` option

Example 8-2 Declaring, Defining, and Invoking a Simple PL/SQL Function

In this example, an anonymous block simultaneously declares and defines a function and invokes it.

```
DECLARE
  -- Declare and define function

  FUNCTION square (original NUMBER)   -- parameter list
    RETURN NUMBER                     -- RETURN clause
  AS
                                      -- Declarative part begins
    original_squared NUMBER;
  BEGIN                               -- Executable part begins
    original_squared := original * original;
    RETURN original_squared;          -- RETURN statement
  END;
BEGIN
  DBMS_OUTPUT.PUT_LINE(square(100));  -- invocation
END;
/
```

Result:

```
10000
```

### RETURN Statement

The `RETURN` statement immediately ends the execution of the subprogram or anonymous block that contains it. A subprogram or anonymous block can contain multiple `RETURN` statements.

Topics

#### RETURN Statement in Function

In a function, every execution path must lead to a `RETURN` statement and every `RETURN` statement must specify an expression. The `RETURN` statement assigns the value of the expression to the function identifier and returns control to the invoker, where execution resumes immediately after the invocation.

Note:

In a pipelined table function, a `RETURN` statement need not specify an expression. For information about the parts of a pipelined table function, see " [Creating Pipelined Table Functions](chaining-pipelined-table-functions-multiple-transformations.md) ".

In Example 8-3, the anonymous block invokes the same function twice. The first time, the `RETURN` statement returns control to the inside of the invoking statement. The second time, the `RETURN` statement returns control to the statement immediately after the invoking statement.

In Example 8-4, the function has multiple `RETURN` statements, but if the parameter is not 0 or 1, then no execution path leads to a `RETURN` statement. The function compiles with warning PLW-05005: subprogram F returns without value at line 11.

Example 8-5 is like Example 8-4, except for the addition of the `ELSE` clause. Every execution path leads to a `RETURN` statement, and the function compiles without warning PLW-05005.

Example 8-3 Execution Resumes After RETURN Statement in Function

```
DECLARE
  x INTEGER;
 
  FUNCTION f (n INTEGER)
  RETURN INTEGER
  IS
  BEGIN
    RETURN (n*n);
  END;
 
BEGIN
  DBMS_OUTPUT.PUT_LINE (
    'f returns ' || f(2) || '. Execution returns here (1).'
  );
  
  x := f(2);
  DBMS_OUTPUT.PUT_LINE('Execution returns here (2).');
END;
/
```

Result:

```
f returns 4. Execution returns here (1).Execution returns here (2).
```

Example 8-4 Function Where Not Every Execution Path Leads to RETURN Statement

```
CREATE OR REPLACE FUNCTION f (n INTEGER)
  RETURN INTEGER
  AUTHID DEFINER
IS
BEGIN
  IF n = 0 THEN
    RETURN 1;
  ELSIF n = 1 THEN
    RETURN n;
  END IF;
END;
/
```

Example 8-5 Function Where Every Execution Path Leads to RETURN Statement

```
CREATE OR REPLACE FUNCTION f (n INTEGER)
  RETURN INTEGER
  AUTHID DEFINER
IS
BEGIN
  IF n = 0 THEN
    RETURN 1;
  ELSIF n = 1 THEN
    RETURN n;
  ELSE
    RETURN n*n;
  END IF;
END;
/
BEGIN
  FOR i IN 0 .. 3 LOOP
    DBMS_OUTPUT.PUT_LINE('f(' || i || ') = ' || f(i));
  END LOOP;
END;
/
```

Result:

```
f(0) = 1
f(1) = 1
f(2) = 4
f(3) = 9
```

#### RETURN Statement in Procedure

In a procedure, the `RETURN` statement returns control to the invoker, where execution resumes immediately after the invocation. The `RETURN` statement cannot specify an expression.

In Example 8-6, the `RETURN` statement returns control to the statement immediately after the invoking statement.

Example 8-6 Execution Resumes After RETURN Statement in Procedure

```
DECLARE
  PROCEDURE p IS
  BEGIN
    DBMS_OUTPUT.PUT_LINE('Inside p');
    RETURN;
    DBMS_OUTPUT.PUT_LINE('Unreachable statement.');
  END;
BEGIN
  p;
  DBMS_OUTPUT.PUT_LINE('Control returns here.');
END;
/
```

Result:

```
Inside p
Control returns here.
```

#### RETURN Statement in Anonymous Block

In an anonymous block, the `RETURN` statement exits its own block and all enclosing blocks. The `RETURN` statement cannot specify an expression.

In Example 8-7, the `RETURN` statement exits both the inner and outer block.

Example 8-7 Execution Resumes After RETURN Statement in Anonymous Block

```
BEGIN
  BEGIN
    DBMS_OUTPUT.PUT_LINE('Inside inner block.');
    RETURN;
    DBMS_OUTPUT.PUT_LINE('Unreachable statement.');
  END;
  DBMS_OUTPUT.PUT_LINE('Inside outer block. Unreachable statement.');
END;
/
```

Result:

```
Inside inner block.
```