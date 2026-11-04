---
title: Database PL/SQL Language Reference
book: Database PL/SQL Language Reference
doc_id: E96448-09
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/cursor-variables.html
tags:
  - oracle
  - 19c
  - pl-sql-language-reference
---

## Cursor Variables

A cursor variable is like an explicit cursor, except that:

- It is not limited to one query.
	You can open a cursor variable for a query, process the result set, and then use the cursor variable for another query.
- You can assign a value to it.
- You can use it in an expression.
- It can be a subprogram parameter.
	You can use cursor variables to pass query result sets between subprograms.
- It can be a host variable.
	You can use cursor variables to pass query result sets between PL/SQL stored subprograms and their clients.
- It cannot accept parameters.
	You cannot pass parameters to a cursor variable, but you can pass whole queries to it. The queries can include variables.

A cursor variable has this flexibility because it is a pointer; that is, its value is the address of an item, not the item itself.

Before you can reference a cursor variable, you must make it point to a SQL work area, either by opening it or by assigning it the value of an open PL/SQL cursor variable or open host cursor variable.

Note:

Cursor variables and explicit cursors are not interchangeable—you cannot use one where the other is expected. For example, you cannot reference a cursor variable in a cursor `FOR` `LOOP` statement.

Topics

See Also:

- " [Explicit Cursors](cursors-overview.md) " for more information about explicit cursors
- " [Restrictions on Cursor Variables](cursor-variable-declaration.md) "
- [Oracle Database Development Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=ADFNS159) for advantages of cursor variables
- [Oracle Database Development Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=ADFNS160) for disadvantages of cursor variables

### Creating Cursor Variables

To create a cursor variable, either declare a variable of the predefined type `SYS_REFCURSOR` or define a `REF` `CURSOR` type and then declare a variable of that type.

Note:

Informally, a cursor variable is sometimes called a `REF` `CURSOR`).

The basic syntax of a `REF` `CURSOR` type definition is:

```
TYPE type_name IS REF CURSOR [ RETURN return_type ]
```

For the complete syntax and semantics, see " [Cursor Variable Declaration](cursor-variable-declaration.md) ".

If you specify `return_type`, then the `REF` `CURSOR` type and cursor variables of that type are strong; if not, they are weak. `SYS_REFCURSOR` and cursor variables of that type are weak.

With a strong cursor variable, you can associate only queries that return the specified type. With a weak cursor variable, you can associate any query.

Weak cursor variables are more error-prone than strong ones, but they are also more flexible. Weak `REF` `CURSOR` types are interchangeable with each other and with the predefined type `SYS_REFCURSOR`. You can assign the value of a weak cursor variable to any other weak cursor variable.

You can assign the value of a strong cursor variable to another strong cursor variable only if both cursor variables have the same type (not merely the same return type).

Note:

You can partition weak cursor variable arguments to table functions only with the `PARTITION` `BY` `ANY` clause, not with `PARTITION` `BY` `RANGE` or `PARTITION` `BY` `HASH`.

For syntax and semantics, see " [PARALLEL\_ENABLE Clause](PARALLEL_ENABLE-clause.md) ".

Example 6-24 Cursor Variable Declarations

This example defines strong and weak `REF` `CURSOR` types, variables of those types, and a variable of the predefined type `SYS_REFCURSOR`.

```
DECLARE
  TYPE empcurtyp IS REF CURSOR RETURN employees%ROWTYPE;  -- strong type
  TYPE genericcurtyp IS REF CURSOR;                       -- weak type

  cursor1  empcurtyp;       -- strong cursor variable
  cursor2  genericcurtyp;   -- weak cursor variable
  my_cursor SYS_REFCURSOR;  -- weak cursor variable

  TYPE deptcurtyp IS REF CURSOR RETURN departments%ROWTYPE;  -- strong type
  dept_cv deptcurtyp;  -- strong cursor variable
BEGIN
  NULL;
END;
/
```

Example 6-25 Cursor Variable with User-Defined Return Type

In this example, `EmpRecTyp` is a user-defined `RECORD` type.

```
DECLARE
  TYPE EmpRecTyp IS RECORD (
    employee_id NUMBER,
    last_name VARCHAR2(25),
    salary   NUMBER(8,2));

  TYPE EmpCurTyp IS REF CURSOR RETURN EmpRecTyp;
  emp_cv EmpCurTyp;
BEGIN
  NULL;
END;
/
```

### Opening and Closing Cursor Variables

After declaring a cursor variable, you can open it with the `OPEN` `FOR` statement, which does the following:

1. Associates the cursor variable with a query (typically, the query returns multiple rows)
	The query can include placeholders for bind variables, whose values you specify in the `USING` clause of the `OPEN` `FOR` statement.
2. Allocates database resources to process the query
3. Processes the query; that is:
	1. Identifies the result set
		If the query references variables, their values affect the result set. For details, see " Variables in Cursor Variable Queries ".
		2. If the query has a `FOR` `UPDATE` clause, locks the rows of the result set
		For details, see " [SELECT FOR UPDATE and FOR UPDATE Cursors](transaction-processing-and-control.md) ".
4. Positions the cursor before the first row of the result set

You need not close a cursor variable before reopening it (that is, using it in another `OPEN` `FOR` statement). After you reopen a cursor variable, the query previously associated with it is lost.

When you no longer need a cursor variable, close it with the `CLOSE` statement, thereby allowing its resources to be reused. After closing a cursor variable, you cannot fetch records from its result set or reference its attributes. If you try, PL/SQL raises the predefined exception `INVALID_CURSOR`.

You can reopen a closed cursor variable.

See Also:

- " [OPEN FOR Statement](OPEN-FOR-statement.md) " for its syntax and semantics
- " [CLOSE Statement](CLOSE-statement.md) " for its syntax and semantics

### Fetching Data with Cursor Variables

After opening a cursor variable, you can fetch the rows of the query result set with the `FETCH` statement.

The return type of the cursor variable must be compatible with the `into_clause` of the `FETCH` statement. If the cursor variable is strong, PL/SQL catches incompatibility at compile time. If the cursor variable is weak, PL/SQL catches incompatibility at run time, raising the predefined exception `ROWTYPE_MISMATCH` before the first fetch.

See Also:

- " [Fetching Data with Explicit Cursors](cursors-overview.md) "
- " [FETCH Statement](FETCH-statement.md) " for its complete syntax and semantics
- " [FETCH Statement with BULK COLLECT Clause](bulk-sql-and-bulk-binding.md) " for information about `FETCH` statements that return more than one row at a time

Example 6-26 Fetching Data with Cursor Variables

This example uses one cursor variable to do what [Example 6-6](cursors-overview.md) does with two explicit cursors. The first `OPEN` `FOR` statement includes the query itself. The second `OPEN` `FOR` statement references a variable whose value is a query.

```
DECLARE
  cv SYS_REFCURSOR;  -- cursor variable
 
  v_lastname  employees.last_name%TYPE;  -- variable for last_name
  v_jobid     employees.job_id%TYPE;     -- variable for job_id
 
  query_2 VARCHAR2(200) :=
    'SELECT * FROM employees
    WHERE REGEXP_LIKE (job_id, ''[ACADFIMKSA]_M[ANGR]'')
    ORDER BY job_id';
 
  v_employees employees%ROWTYPE;  -- record variable row of table
 
BEGIN
  OPEN cv FOR
    SELECT last_name, job_id FROM employees
    WHERE REGEXP_LIKE (job_id, 'S[HT]_CLERK')
    ORDER BY last_name;
 
  LOOP  -- Fetches 2 columns into variables
    FETCH cv INTO v_lastname, v_jobid;
    EXIT WHEN cv%NOTFOUND;
    DBMS_OUTPUT.PUT_LINE( RPAD(v_lastname, 25, ' ') || v_jobid );
  END LOOP;
 
  DBMS_OUTPUT.PUT_LINE( '-------------------------------------' );
 
  OPEN cv FOR query_2;
 
  LOOP  -- Fetches entire row into the v_employees record
    FETCH cv INTO v_employees;
    EXIT WHEN cv%NOTFOUND;
    DBMS_OUTPUT.PUT_LINE( RPAD(v_employees.last_name, 25, ' ') ||
                               v_employees.job_id );
  END LOOP;
 
  CLOSE cv;
END;
/
```

Result:

```
Atkinson                 ST_CLERK
Bell                     SH_CLERK
Bissot                   ST_CLERK
...
Walsh                    SH_CLERK
-------------------------------------
Higgins                  AC_MGR
Greenberg                FI_MGR
Hartstein                MK_MAN
...
Zlotkey                  SA_MAN
```

Example 6-27 Fetching from Cursor Variable into Collections

This example fetches from a cursor variable into two collections (nested tables), using the `BULK` `COLLECT` clause of the `FETCH` statement.

```
DECLARE
  TYPE empcurtyp IS REF CURSOR;
  TYPE namelist IS TABLE OF employees.last_name%TYPE;
  TYPE sallist IS TABLE OF employees.salary%TYPE;
  emp_cv  empcurtyp;
  names   namelist;
  sals    sallist;
BEGIN
  OPEN emp_cv FOR
    SELECT last_name, salary FROM employees
    WHERE job_id = 'SA_REP'
    ORDER BY salary DESC;

  FETCH emp_cv BULK COLLECT INTO names, sals;
  CLOSE emp_cv;
  -- loop through the names and sals collections
  FOR i IN names.FIRST .. names.LAST
  LOOP
    DBMS_OUTPUT.PUT_LINE
      ('Name = ' || names(i) || ', salary = ' || sals(i));
  END LOOP;
END;
/
```

Result:

```
Name = Ozer, salary = 11500
Name = Abel, salary = 11000
Name = Vishney, salary = 10500
...
Name = Kumar, salary = 6100
```

### Assigning Values to Cursor Variables

You can assign to a PL/SQL cursor variable the value of another PL/SQL cursor variable or host cursor variable.

The syntax is:

```
target_cursor_variable := source_cursor_variable;
```

If `source_cursor_variable` is open, then after the assignment, `target_cursor_variable` is also open. The two cursor variables point to the same SQL work area.

If `source_cursor_variable` is not open, opening `target_cursor_variable` after the assignment does not open `source_cursor_variable`.

### Variables in Cursor Variable Queries

The query associated with a cursor variable can reference any variable in its scope.

When you open a cursor variable with the `OPEN` `FOR` statement, PL/SQL evaluates any variables in the query and uses those values when identifying the result set. Changing the values of the variables later does not change the result set.

To change the result set, you must change the value of the variable and then open the cursor variable again for the same query, as in Example 6-29.

Example 6-28 Variable in Cursor Variable Query—No Result Set Change

This example opens a cursor variable for a query that references the variable `factor`, which has the value 2. Therefore, `sal_multiple` is always 2 times `sal`, despite that `factor` is incremented after every fetch.

```
DECLARE
  sal           employees.salary%TYPE;
  sal_multiple  employees.salary%TYPE;
  factor        INTEGER := 2;
 
  cv SYS_REFCURSOR;
 
BEGIN
  OPEN cv FOR
    SELECT salary, salary*factor
    FROM employees
    WHERE job_id LIKE 'AD_%';   -- PL/SQL evaluates factor
 
  LOOP
    FETCH cv INTO sal, sal_multiple;
    EXIT WHEN cv%NOTFOUND;
    DBMS_OUTPUT.PUT_LINE('factor = ' || factor);
    DBMS_OUTPUT.PUT_LINE('sal          = ' || sal);
    DBMS_OUTPUT.PUT_LINE('sal_multiple = ' || sal_multiple);
    factor := factor + 1;  -- Does not affect sal_multiple
  END LOOP;
 
  CLOSE cv;
END;
/
```

Result:

```
factor = 2
sal          = 4400
sal_multiple = 8800
factor = 3
sal          = 24000
sal_multiple = 48000
factor = 4
sal          = 17000
sal_multiple = 34000
factor = 5
sal          = 17000
sal_multiple = 34000
```

Example 6-29 Variable in Cursor Variable Query—Result Set Change

```
DECLARE
  sal           employees.salary%TYPE;
  sal_multiple  employees.salary%TYPE;
  factor        INTEGER := 2;
 
  cv SYS_REFCURSOR;
 
BEGIN
  DBMS_OUTPUT.PUT_LINE('factor = ' || factor);
 
  OPEN cv FOR
    SELECT salary, salary*factor
    FROM employees
    WHERE job_id LIKE 'AD_%';   -- PL/SQL evaluates factor
 
  LOOP
    FETCH cv INTO sal, sal_multiple;
    EXIT WHEN cv%NOTFOUND;
    DBMS_OUTPUT.PUT_LINE('sal          = ' || sal);
    DBMS_OUTPUT.PUT_LINE('sal_multiple = ' || sal_multiple);
  END LOOP;
 
  factor := factor + 1;
 
  DBMS_OUTPUT.PUT_LINE('factor = ' || factor);
 
  OPEN cv FOR
    SELECT salary, salary*factor
    FROM employees
    WHERE job_id LIKE 'AD_%';   -- PL/SQL evaluates factor
 
  LOOP
    FETCH cv INTO sal, sal_multiple;
    EXIT WHEN cv%NOTFOUND;
    DBMS_OUTPUT.PUT_LINE('sal          = ' || sal);
    DBMS_OUTPUT.PUT_LINE('sal_multiple = ' || sal_multiple);
  END LOOP;
 
  CLOSE cv;
END;
/
```

Result:

```
factor = 2
sal          = 4400
sal_multiple = 8800
sal          = 24000
sal_multiple = 48000
sal          = 17000
sal_multiple = 34000
sal          = 17000
sal_multiple = 34000
factor = 3
sal          = 4400
sal_multiple = 13200
sal          = 24000
sal_multiple = 72000
sal          = 17000
sal_multiple = 51000
sal          = 17000
sal_multiple = 51000
```

### Querying a Collection

You can query a collection if all of the following are true:

- The data type of the collection was either created at schema level or declared in a package specification.
- The data type of the collection element is either a scalar data type, a user-defined type, or a record type.

In the query `FROM` clause, the collection appears in `table_collection_expression` as the argument of the `TABLE` operator.

Note:

In SQL contexts, you cannot use a function whose return type was declared in a package specification.

See Also:

- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=SQLRF55241) for information about the `table_collection_expression`
- " [CREATE PACKAGE Statement](CREATE-PACKAGE-statement.md) " for information about the `CREATE` `PACKAGE` statement
- " [PL/SQL Collections and Records](plsql-collections-and-records.md) " for information about collection types and collection variables
- [Example 7-9](native-dynamic-sql.md), "Querying a Collection with Native Dynamic SQL"

Example 6-30 Querying a Collection with Static SQL

In this example, the cursor variable is associated with a query on an associative array of records. The nested table type, `mytab`, is declared in a package specification.

```
CREATE OR REPLACE PACKAGE pkg AUTHID DEFINER AS
  TYPE rec IS RECORD(f1 NUMBER, f2 VARCHAR2(30));
  TYPE mytab IS TABLE OF rec INDEX BY pls_integer;
END;

DECLARE
  v1 pkg.mytab;  -- collection of records
  v2 pkg.rec;
  c1 SYS_REFCURSOR;
BEGIN
  v1(1).f1 := 1;
  v1(1).f2 := 'one';
  OPEN c1 FOR SELECT * FROM TABLE(v1);
  FETCH c1 INTO v2;
  CLOSE c1;
  DBMS_OUTPUT.PUT_LINE('Values in record are ' || v2.f1 || ' and ' || v2.f2);
END;
/
```

Result:

```
Values in record are 1 and one
```

### Cursor Variable Attributes

A cursor variable has the same attributes as an explicit cursor (see [Explicit Cursor Attributes](cursors-overview.md).). The syntax for the value of a cursor variable attribute is `cursor_variable_name` immediately followed by `attribute` (for example, `cv%ISOPEN`). If a cursor variable is not open, referencing any attribute except `%ISOPEN` raises the predefined exception `INVALID_CURSOR`.

### Cursor Variables as Subprogram Parameters

You can use a cursor variable as a subprogram parameter, which makes it useful for passing query results between subprograms.

For example:

- You can open a cursor variable in one subprogram and process it in a different subprogram.
- In a multilanguage application, a PL/SQL subprogram can use a cursor variable to return a result set to a subprogram written in a different language.

Note:

The invoking and invoked subprograms must be in the same database instance. You cannot pass or return cursor variables to subprograms invoked through database links.

Caution:

Because cursor variables are pointers, using them as subprogram parameters increases the likelihood of subprogram parameter aliasing, which can have unintended results. For more information, see " [Subprogram Parameter Aliasing with Cursor Variable Parameters](subprogram-parameters.md) ".

When declaring a cursor variable as the formal parameter of a subprogram:

- If the subprogram opens or assigns a value to the cursor variable, then the parameter mode must be `IN` `OUT`.
- If the subprogram only fetches from, or closes, the cursor variable, then the parameter mode can be either `IN` or `IN` `OUT`.

Corresponding formal and actual cursor variable parameters must have compatible return types. Otherwise, PL/SQL raises the predefined exception `ROWTYPE_MISMATCH`.

To pass a cursor variable parameter between subprograms in different PL/SQL units, define the `REF` `CURSOR` type of the parameter in a package. When the type is in a package, multiple subprograms can use it. One subprogram can declare a formal parameter of that type, and other subprograms can declare variables of that type and pass them to the first subprogram.

See Also:

- " [Subprogram Parameters](subprogram-parameters.md) " for more information about subprogram parameters
- " [CURSOR Expressions](cursor-expressions.md) " for information about `CURSOR` expressions, which can be actual parameters for formal cursor variable parameters
- [PL/SQL Packages](plsql-packages.md), for more information about packages

Example 6-31 Procedure to Open Cursor Variable for One Query

This example defines, in a package, a `REF` `CURSOR` type and a procedure that opens a cursor variable parameter of that type.

```
CREATE OR REPLACE PACKAGE emp_data AUTHID DEFINER AS
  TYPE empcurtyp IS REF CURSOR RETURN employees%ROWTYPE;
  PROCEDURE open_emp_cv (emp_cv IN OUT empcurtyp);
END emp_data;
/
CREATE OR REPLACE PACKAGE BODY emp_data AS
  PROCEDURE open_emp_cv (emp_cv IN OUT EmpCurTyp) IS
  BEGIN
    OPEN emp_cv FOR SELECT * FROM employees;
  END open_emp_cv;
END emp_data;
/
```

Example 6-32 Opening Cursor Variable for Chosen Query (Same Return Type)

In this example,the stored procedure opens its cursor variable parameter for a chosen query. The queries have the same return type.

```
CREATE OR REPLACE PACKAGE emp_data AUTHID DEFINER AS
  TYPE empcurtyp IS REF CURSOR RETURN employees%ROWTYPE;
  PROCEDURE open_emp_cv (emp_cv IN OUT empcurtyp, choice INT);
END emp_data;
/
CREATE OR REPLACE PACKAGE BODY emp_data AS
  PROCEDURE open_emp_cv (emp_cv IN OUT empcurtyp, choice INT) IS
  BEGIN
    IF choice = 1 THEN
      OPEN emp_cv FOR SELECT *
      FROM employees
      WHERE commission_pct IS NOT NULL;
    ELSIF choice = 2 THEN
      OPEN emp_cv FOR SELECT *
      FROM employees
      WHERE salary > 2500;
    ELSIF choice = 3 THEN
      OPEN emp_cv FOR SELECT *
      FROM employees
      WHERE department_id = 100;
    END IF;
  END;
END emp_data;
/
```

Example 6-33 Opening Cursor Variable for Chosen Query (Different Return Types)

In this example,the stored procedure opens its cursor variable parameter for a chosen query. The queries have the different return types.

```
CREATE OR REPLACE PACKAGE admin_data AUTHID DEFINER AS
  TYPE gencurtyp IS REF CURSOR;
  PROCEDURE open_cv (generic_cv IN OUT gencurtyp, choice INT);
END admin_data;
/
CREATE OR REPLACE PACKAGE BODY admin_data AS
  PROCEDURE open_cv (generic_cv IN OUT gencurtyp, choice INT) IS
  BEGIN
    IF choice = 1 THEN
      OPEN generic_cv FOR SELECT * FROM employees;
    ELSIF choice = 2 THEN
      OPEN generic_cv FOR SELECT * FROM departments;
    ELSIF choice = 3 THEN
      OPEN generic_cv FOR SELECT * FROM jobs;
    END IF;
  END;
END admin_data;
/
```

### Cursor Variables as Host Variables

You can use a cursor variable as a host variable, which makes it useful for passing query results between PL/SQL stored subprograms and their clients.

When a cursor variable is a host variable, PL/SQL and the client (the host environment) share a pointer to the SQL work area that stores the result set.

To use a cursor variable as a host variable, declare the cursor variable in the host environment and then pass it as an input host variable (bind variable) to PL/SQL. Host cursor variables are compatible with any query return type (like weak PL/SQL cursor variables).

A SQL work area remains accessible while any cursor variable points to it, even if you pass the value of a cursor variable from one scope to another. For example, in Example 6-34, the Pro\*C program passes a host cursor variable to an embedded PL/SQL anonymous block. After the block runs, the cursor variable still points to the SQL work area.

If you have a PL/SQL engine on the client side, calls from client to server impose no restrictions. For example, you can declare a cursor variable on the client side, open and fetch from it on the server side, and continue to fetch from it on the client side. You can also reduce network traffic with a PL/SQL anonymous block that opens or closes several host cursor variables in a single round trip. For example:

```
/* PL/SQL anonymous block in host environment */
BEGIN
  OPEN :emp_cv FOR SELECT * FROM employees;
  OPEN :dept_cv FOR SELECT * FROM departments;
  OPEN :loc_cv FOR SELECT * FROM locations;
END;
/
```

Because the cursor variables still point to the SQL work areas after the PL/SQL anonymous block runs, the client program can use them. When the client program no longer needs the cursors, it can use a PL/SQL anonymous block to close them. For example:

```
/* PL/SQL anonymous block in host environment */
BEGIN
  CLOSE :emp_cv;
  CLOSE :dept_cv;
  CLOSE :loc_cv;
END;
/
```

This technique is useful for populating a multiblock form, as in Oracle Forms. For example, you can open several SQL work areas in a single round trip, like this:

```
/* PL/SQL anonymous block in host environment */
BEGIN
  OPEN :c1 FOR SELECT 1 FROM DUAL;
  OPEN :c2 FOR SELECT 1 FROM DUAL;
  OPEN :c3 FOR SELECT 1 FROM DUAL;
END;
/
```

Note:

If you bind a host cursor variable into PL/SQL from an Oracle Call Interface (OCI) client, then you cannot fetch from it on the server side unless you also open it there on the same server call.

Example 6-34 Cursor Variable as Host Variable in Pro\*C Client Program

In this example, a Pro\*C client program declares a cursor variable and a selector and passes them as host variables to a PL/SQL anonymous block, which opens the cursor variable for the selected query.

```
EXEC SQL BEGIN DECLARE SECTION;
  SQL_CURSOR  generic_cv;  -- Declare host cursor variable.
  int         choice;      -- Declare selector.
EXEC SQL END DECLARE SECTION;
EXEC SQL ALLOCATE :generic_cv;  -- Initialize host cursor variable.
-- Pass host cursor variable and selector to PL/SQL block.
/
EXEC SQL EXECUTE
BEGIN
  IF :choice = 1 THEN
    OPEN :generic_cv FOR SELECT * FROM employees;
  ELSIF :choice = 2 THEN
    OPEN :generic_cv FOR SELECT * FROM departments;
  ELSIF :choice = 3 THEN
    OPEN :generic_cv FOR SELECT * FROM jobs;
  END IF;
END;
END-EXEC;
```