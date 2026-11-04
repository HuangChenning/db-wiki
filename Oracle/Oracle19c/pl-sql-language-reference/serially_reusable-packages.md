---
title: Database PL/SQL Language Reference
book: Database PL/SQL Language Reference
doc_id: E96448-09
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/serially_reusable-packages.html
tags:
  - oracle
  - 19c
  - pl-sql-language-reference
---

## SERIALLY\_REUSABLE Packages

`SERIALLY_REUSABLE` packages let you design applications that manage memory better for scalability.

If a package is not `SERIALLY_REUSABLE`, its package state is stored in the user global area (UGA) for each user. Therefore, the amount of UGA memory needed increases linearly with the number of users, limiting scalability. The package state can persist for the life of a session, locking UGA memory until the session ends. In some applications, such as Oracle Office, a typical session lasts several days.

If a package is `SERIALLY_REUSABLE`, its package state is stored in a work area in a small pool in the system global area (SGA). The package state persists only for the life of a server call. After the server call, the work area returns to the pool. If a subsequent server call references the package, then Oracle Database reuses an instantiation from the pool. Reusing an instantiation re-initializes it; therefore, changes made to the package state in previous server calls are invisible. (For information about initialization, see " [Package Instantiation and Initialization](package-instantiation-and-initialization.md) ".)

Note:

Trying to access a `SERIALLY_REUSABLE` package from a database trigger, or from a PL/SQL subprogram invoked by a SQL statement, raises an error.

Topics

### Creating SERIALLY\_REUSABLE Packages

To create a `SERIALLY_REUSABLE` package, include the `SERIALLY_REUSABLE` pragma in the package specification and, if it exists, the package body.

Example 10-4 creates two very simple `SERIALLY_REUSABLE` packages, one with only a specification, and one with both a specification and a body.

See Also:

" [SERIALLY\_REUSABLE Pragma](SERIALLY_REUSABLE-pragma.md) "

Example 10-4 Creating SERIALLY\_REUSABLE Packages

```
-- Create bodiless SERIALLY_REUSABLE package:
 
CREATE OR REPLACE PACKAGE bodiless_pkg AUTHID DEFINER IS
  PRAGMA SERIALLY_REUSABLE;
  n NUMBER := 5;
END;
/
 
-- Create SERIALLY_REUSABLE package with specification and body:
 
CREATE OR REPLACE PACKAGE pkg AUTHID DEFINER IS
  PRAGMA SERIALLY_REUSABLE;
  n NUMBER := 5;
END;
/
 
CREATE OR REPLACE PACKAGE BODY pkg IS
  PRAGMA SERIALLY_REUSABLE;
BEGIN
  n := 5;
END;
/
```

### SERIALLY\_REUSABLE Package Work Unit

For a `SERIALLY_REUSABLE` package, the work unit is a server call.

You must use its public variables only within the work unit.

Note:

If you make a mistake and depend on the value of a public variable that was set in a previous work unit, then your program can fail. PL/SQL cannot check for such cases.

After the work unit (server call) of a `SERIALLY_REUSABLE` package completes, Oracle Database does the following:

- Closes any open cursors.
- Frees some nonreusable memory (for example, memory for collection and long `VARCHAR2` variables)
- Returns the package instantiation to the pool of reusable instantiations kept for this package.

Example 10-5 Effect of SERIALLY\_REUSABLE Pragma

In this example, the bodiless packages `pkg` and `sr_pkg` are the same, except that `sr_pkg` is `SERIALLY_REUSABLE` and `pkg` is not. Each package declares public variable `n` with initial value 5. Then, an anonymous block changes the value of each variable to 10. Next, another anonymous block prints the value of each variable. The value of `pkg`.`n` is still 10, because the state of `pkg` persists for the life of the session. The value of `sr_pkg`.`n` is 5, because the state of `sr_pkg` persists only for the life of the server call.

```
CREATE OR REPLACE PACKAGE pkg IS
  n NUMBER := 5;
END pkg;
/

CREATE OR REPLACE PACKAGE sr_pkg IS
  PRAGMA SERIALLY_REUSABLE;
  n NUMBER := 5;
END sr_pkg;
/

BEGIN
  pkg.n := 10;
  sr_pkg.n := 10;
END;
/

BEGIN
  DBMS_OUTPUT.PUT_LINE('pkg.n: ' || pkg.n);
  DBMS_OUTPUT.PUT_LINE('sr_pkg.n: ' || sr_pkg.n);
END;
/
```

Result:

```
pkg.n: 10
sr_pkg.n: 5
```

### Explicit Cursors in SERIALLY\_REUSABLE Packages

An explicit cursor in a `SERIALLY_REUSABLE` package remains open until either you close it or its work unit (server call) ends. To re-open the cursor, you must make a new server call. A server call can be different from a subprogram invocation, as Example 10-6 shows.

In contrast, an explicit cursor in a package that is not `SERIALLY_REUSABLE` remains open until you either close it or disconnect from the session.

Example 10-6 Cursor in SERIALLY\_REUSABLE Package Open at Call Boundary

```
DROP TABLE people;
CREATE TABLE people (name VARCHAR2(20));
 
INSERT INTO people (name) VALUES ('John Smith');
INSERT INTO people (name) VALUES ('Mary Jones');
INSERT INTO people (name) VALUES ('Joe Brown');
INSERT INTO people (name) VALUES ('Jane White');

CREATE OR REPLACE PACKAGE sr_pkg IS
  PRAGMA SERIALLY_REUSABLE;
  CURSOR c IS SELECT name FROM people;
END sr_pkg;
/
 
CREATE OR REPLACE PROCEDURE fetch_from_cursor IS
  v_name  people.name%TYPE;
BEGIN
  IF sr_pkg.c%ISOPEN THEN
    DBMS_OUTPUT.PUT_LINE('Cursor is open.');
  ELSE
    DBMS_OUTPUT.PUT_LINE('Cursor is closed; opening now.');
    OPEN sr_pkg.c;
  END IF;
 
  FETCH sr_pkg.c INTO v_name;
  DBMS_OUTPUT.PUT_LINE('Fetched: ' || v_name);
 
  FETCH sr_pkg.c INTO v_name;
    DBMS_OUTPUT.PUT_LINE('Fetched: ' || v_name);
  END fetch_from_cursor;
/
```

First call to server:

```
BEGIN
  fetch_from_cursor;
  fetch_from_cursor;
END;
/
```

Result:

```
Cursor is closed; opening now.
Fetched: John Smith
Fetched: Mary Jones
Cursor is open.
Fetched: Joe Brown
Fetched: Jane White
```

New call to server:

```
BEGIN
  fetch_from_cursor;
  fetch_from_cursor;
END;
/
```

Result:

```
Cursor is closed; opening now.
Fetched: John Smith
Fetched: Mary Jones
Cursor is open.
Fetched: Joe Brown
Fetched: Jane White
```