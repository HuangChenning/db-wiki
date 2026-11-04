---
title: Database PL/SQL Language Reference
book: Database PL/SQL Language Reference
doc_id: E96448-09
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/package-writing-guidelines.html
tags:
  - oracle
  - 19c
  - pl-sql-language-reference
---

## Package Writing Guidelines

- Become familiar with the packages that Oracle Database supplies, and avoid writing packages that duplicate their features.
	For more information about the packages that Oracle Database supplies, see [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=ARPLS-GUID-4AA6AA30-CAEE-4DCD-B214-9AD51D0229B4).
- Keep your packages general so that future applications can reuse them.
- Design and define the package specifications before the package bodies.
- In package specifications, declare only items that must be visible to invoking programs.
	This practice prevents other developers from building unsafe dependencies on your implementation details and reduces the need for recompilation.
	If you change the package specification, you must recompile any subprograms that invoke the public subprograms of the package. If you change only the package body, you need not recompile those subprograms.
- Declare public cursors in package specifications and define them in package bodies, as in Example 10-7.
	This practice lets you hide cursors' queries from package users and change them without changing cursor declarations.
- Assign initial values in the initialization part of the package body instead of in declarations.
	This practice has these advantages:
	- The code for computing the initial values can be more complex and better documented.
		- If computing an initial value raises an exception, the initialization part can handle it with its own exception handler.
- If you implement a database application as several PL/SQL packages—one package that provides the API and helper packages to do the work, then make the helper packages available only to the API package, as in Example 10-8.

In Example 10-7, the declaration and definition of the cursor `c1` are in the specification and body, respectively, of the package `emp_stuff`. The cursor declaration specifies only the data type of the return value, not the query, which appears in the cursor definition (for complete syntax and semantics, see " [Explicit Cursor Declaration and Definition](explicit-cursor-declaration-and-definition.md) ").

Example 10-8 creates an API package and a helper package. Because of the `ACCESSIBLE` `BY` clause in the helper package specification, only the API package can access the helper package.

```
CREATE PACKAGE emp_stuff AS
  CURSOR c1 RETURN employees%ROWTYPE;  -- Declare cursor
END emp_stuff;
/
CREATE PACKAGE BODY emp_stuff AS
  CURSOR c1 RETURN employees%ROWTYPE IS
    SELECT * FROM employees WHERE salary > 2500;  -- Define cursor
END emp_stuff;
/
```

Example 10-8 ACCESSIBLE BY Clause

```
CREATE OR REPLACE PACKAGE helper
  AUTHID DEFINER
  ACCESSIBLE BY (api)
IS
  PROCEDURE h1;
  PROCEDURE h2;
END;
/
 
CREATE OR REPLACE PACKAGE BODY helper
IS
  PROCEDURE h1 IS
  BEGIN
    DBMS_OUTPUT.PUT_LINE('Helper procedure h1');
  END;
 
  PROCEDURE h2 IS
  BEGIN
    DBMS_OUTPUT.PUT_LINE('Helper procedure h2');
  END;
END;
/
 
CREATE OR REPLACE PACKAGE api
  AUTHID DEFINER
IS
  PROCEDURE p1;
  PROCEDURE p2;
END;
/
 
CREATE OR REPLACE PACKAGE BODY api
IS
  PROCEDURE p1 IS
  BEGIN
    DBMS_OUTPUT.PUT_LINE('API procedure p1');
    helper.h1;
  END;
 
  PROCEDURE p2 IS
  BEGIN
    DBMS_OUTPUT.PUT_LINE('API procedure p2');
    helper.h2;
  END;
END;
/
```

Invoke procedures in API package:

```
BEGIN
  api.p1;
  api.p2;
END;
/
```

Result:

```
API procedure p1
Helper procedure h1
API procedure p2
Helper procedure h2
```

Invoke a procedure in helper package:

```
BEGIN
  helper.h1;
END;
/
```

Result:

```
SQL> BEGIN
  2    helper.h1;
  3  END;
  4  /
  helper.h1;
  *
ERROR at line 2:
ORA-06550: line 2, column 3:
PLS-00904: insufficient privilege to access object HELPER
ORA-06550: line 2, column 3:
PL/SQL: Statement ignored
```