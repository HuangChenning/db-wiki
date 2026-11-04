---
title: Database PL/SQL Language Reference
book: Database PL/SQL Language Reference
doc_id: E96448-09
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/record-variables.html
tags:
  - oracle
  - 19c
  - pl-sql-language-reference
---

## Record Variables

You can create a record variable in any of these ways:

- Define a `RECORD` type and then declare a variable of that type.
- Use `%ROWTYPE` to declare a record variable that represents either a full or partial row of a database table or view.
- Use `%TYPE` to declare a record variable of the same type as a previously declared record variable.

For syntax and semantics, see " [Record Variable Declaration](record-variable-declaration.md) ".

Topics

### Initial Values of Record Variables

For a record variable of a `RECORD` type, the initial value of each field is `NULL` unless you specify a different initial value for it when you define the type.

For a record variable declared with `%ROWTYPE` or `%TYPE`, the initial value of each field is `NULL`. The variable does not inherit the initial value of the referenced item.

### Declaring Record Constants

When declaring a record constant, you must create a function that populates the record with its initial value and then invoke the function in the constant declaration.

Example 5-35 Declaring Record Constant

This example creates a function that populates the record with its initial value and then invoke the function in the constant declaration.

Live SQL:

You can view and run this example on Oracle Live SQL at [Declaring Record Constant](https://livesql.oracle.com/apex/livesql/docs/lnpls/plsql-collections-and-records/tdlnplscomposites90.html)

```
CREATE OR REPLACE PACKAGE My_Types AUTHID CURRENT_USER IS
  TYPE My_Rec IS RECORD (a NUMBER, b NUMBER);
  FUNCTION Init_My_Rec RETURN My_Rec;
END My_Types;
/
CREATE OR REPLACE PACKAGE BODY My_Types IS
  FUNCTION Init_My_Rec RETURN My_Rec IS
    Rec My_Rec;
  BEGIN
    Rec.a := 0;
    Rec.b := 1;
    RETURN Rec;
  END Init_My_Rec;
END My_Types;
/
DECLARE
  r CONSTANT My_Types.My_Rec := My_Types.Init_My_Rec();
BEGIN
  DBMS_OUTPUT.PUT_LINE('r.a = ' || r.a);
  DBMS_OUTPUT.PUT_LINE('r.b = ' || r.b);
END;
/
```

Result:

```
r.a = 0
r.b = 1
 
PL/SQL procedure successfully completed.
```

### RECORD Types

A `RECORD` type defined in a PL/SQL block is a local type. It is available only in the block, and is stored in the database only if the block is in a standalone or package subprogram.

A `RECORD` type defined in a package specification is a public item. You can reference it from outside the package by qualifying it with the package name (`package_name.type_name`). It is stored in the database until you drop the package with the `DROP` `PACKAGE` statement.

You cannot create a `RECORD` type at schema level. Therefore, a `RECORD` type cannot be an ADT attribute data type.

To define a `RECORD` type, specify its name and define its fields. To define a field, specify its name and data type. By default, the initial value of a field is `NULL`. You can specify the `NOT` `NULL` constraint for a field, in which case you must also specify a non- `NULL` initial value. Without the `NOT` `NULL` constraint, a non- `NULL` initial value is optional.

A `RECORD` type defined in a package specification is incompatible with an identically defined local `RECORD` type.

Example 5-36 RECORD Type Definition and Variable Declaration

This example defines a `RECORD` type named `DeptRecTyp`, specifying an initial value for each field. Then it declares a variable of that type named `dept_rec` and prints its fields.

Live SQL:

You can view and run this example on Oracle Live SQL at [RECORD Type Definition and Variable Declaration](https://livesql.oracle.com/apex/livesql/docs/lnpls/plsql-collections-and-records/tdlnplscomposites76.html)

```
DECLARE
  TYPE DeptRecTyp IS RECORD (
    dept_id    NUMBER(4) NOT NULL := 10,
    dept_name  VARCHAR2(30) NOT NULL := 'Administration',
    mgr_id     NUMBER(6) := 200,
    loc_id     NUMBER(4) := 1700
  );
 
  dept_rec DeptRecTyp;
BEGIN
  DBMS_OUTPUT.PUT_LINE('dept_id:   ' || dept_rec.dept_id);
  DBMS_OUTPUT.PUT_LINE('dept_name: ' || dept_rec.dept_name);
  DBMS_OUTPUT.PUT_LINE('mgr_id:    ' || dept_rec.mgr_id);
  DBMS_OUTPUT.PUT_LINE('loc_id:    ' || dept_rec.loc_id);
END;
/
```

Result:

```
dept_id:   10
dept_name: Administration
mgr_id:    200
loc_id:    1700
```

Example 5-37 RECORD Type with RECORD Field (Nested Record)

This example defines two `RECORD` types, `name_rec` and `contact`. The type `contact` has a field of type `name_rec`.

Live SQL:

You can view and run this example on Oracle Live SQL at [RECORD Type with RECORD Field (Nested Record)](https://livesql.oracle.com/apex/livesql/docs/lnpls/plsql-collections-and-records/tdlnplscomposites77.html)

```
DECLARE
  TYPE name_rec IS RECORD (
    first  employees.first_name%TYPE,
    last   employees.last_name%TYPE
  );
 
  TYPE contact IS RECORD (
    name  name_rec,                    -- nested record
    phone employees.phone_number%TYPE
  );
 
  friend contact;
BEGIN
  friend.name.first := 'John';
  friend.name.last := 'Smith';
  friend.phone := '1-650-555-1234';
  
  DBMS_OUTPUT.PUT_LINE (
    friend.name.first  || ' ' ||
    friend.name.last   || ', ' ||
    friend.phone
  );
END;
/
```

Result:

```
John Smith, 1-650-555-1234
```

Example 5-38 RECORD Type with Varray Field

This defines a `VARRAY` type, `full_name`, and a `RECORD` type, `contact`. The type `contact` has a field of type `full_name`.

Live SQL:

You can view and run this example on Oracle Live SQL at [RECORD Type with Varray Field](https://livesql.oracle.com/apex/livesql/docs/lnpls/plsql-collections-and-records/tdlnplscomposites78.html)

```
DECLARE
  TYPE full_name IS VARRAY(2) OF VARCHAR2(20);
 
  TYPE contact IS RECORD (
    name  full_name := full_name('John', 'Smith'),  -- varray field
    phone employees.phone_number%TYPE
  );
 
  friend contact;
BEGIN
  friend.phone := '1-650-555-1234';
  
  DBMS_OUTPUT.PUT_LINE (
    friend.name(1) || ' ' ||
    friend.name(2) || ', ' ||
    friend.phone
  );
END;
/
```

Result:

```
John Smith, 1-650-555-1234
```

Example 5-39 Identically Defined Package and Local RECORD Types

In this example, the package `pkg` and the anonymous block define the `RECORD` type `rec_type` identically. The package defines a procedure, `print_rec_type`, which has a `rec_type` parameter. The anonymous block declares the variable `r1` of the package type (`pkg.rec_type`) and the variable `r2` of the local type (`rec_type`). The anonymous block can pass `r1` to `print_rec_type`, but it cannot pass `r2` to `print_rec_type`.

Live SQL:

You can view and run this example on Oracle Live SQL at [Identically Defined Package and Local RECORD Types](https://livesql.oracle.com/apex/livesql/docs/lnpls/plsql-collections-and-records/tdlnplscomposites75err.html)

```
CREATE OR REPLACE PACKAGE pkg AS
  TYPE rec_type IS RECORD (       -- package RECORD type
    f1 INTEGER,
    f2 VARCHAR2(4)
  );
  PROCEDURE print_rec_type (rec rec_type);
END pkg;
/
CREATE OR REPLACE PACKAGE BODY pkg AS
  PROCEDURE print_rec_type (rec rec_type) IS
  BEGIN
    DBMS_OUTPUT.PUT_LINE(rec.f1);
    DBMS_OUTPUT.PUT_LINE(rec.f2);
  END; 
END pkg;
/
DECLARE
  TYPE rec_type IS RECORD (       -- local RECORD type
    f1 INTEGER,
    f2 VARCHAR2(4)
  );
  r1 pkg.rec_type;                -- package type
  r2     rec_type;                -- local type
 
BEGIN
  r1.f1 := 10; r1.f2 := 'abcd';
  r2.f1 := 25; r2.f2 := 'wxyz';
 
  pkg.print_rec_type(r1);  -- succeeds
  pkg.print_rec_type(r2);  -- fails
END;
/
```

Result:

```
pkg.print_rec_type(r2);  -- fails
  *
ERROR at line 14:
ORA-06550: line 14, column 3:
PLS-00306: wrong number or types of arguments in call to 'PRINT_REC_TYPE'
```

### Declaring Items using the %ROWTYPE Attribute

The `%ROWTYPE` attribute lets you declare a record variable that represents either a full or partial row of a database table or view.

For the syntax and semantics details, see [%ROWTYPE Attribute](ROWTYPE-attribute.md).

Topics

#### Declaring a Record Variable that Always Represents Full Row

To declare a record variable that always represents a full row of a database table or view, use this syntax:

```
variable_name table_or_view_name%ROWTYPE;
```

For every column of the table or view, the record has a field with the same name and data type.

See Also:

" [%ROWTYPE Attribute](ROWTYPE-attribute.md) " for more information about `%ROWTYPE`

Example 5-40 %ROWTYPE Variable Represents Full Database Table Row

This example declares a record variable that represents a row of the table `departments`, assigns values to its fields, and prints them. Compare this example to Example 5-36.

Live SQL:

You can view and run this example on Oracle Live SQL at [%ROWTYPE Variable Represents Full Database Table Row](https://livesql.oracle.com/apex/livesql/docs/lnpls/plsql-collections-and-records/tdlnplscomposites80.html)

```
DECLARE
  dept_rec departments%ROWTYPE;
BEGIN
  -- Assign values to fields:
  
  dept_rec.department_id   := 10;
  dept_rec.department_name := 'Administration';
  dept_rec.manager_id      := 200;
  dept_rec.location_id     := 1700;
 
  -- Print fields:
 
  DBMS_OUTPUT.PUT_LINE('dept_id:   ' || dept_rec.department_id);
  DBMS_OUTPUT.PUT_LINE('dept_name: ' || dept_rec.department_name);
  DBMS_OUTPUT.PUT_LINE('mgr_id:    ' || dept_rec.manager_id);
  DBMS_OUTPUT.PUT_LINE('loc_id:    ' || dept_rec.location_id);
END;
/
```

Result:

```
dept_id:   10
dept_name: Administration
mgr_id:    200
loc_id:    1700
```

Example 5-41 %ROWTYPE Variable Does Not Inherit Initial Values or Constraints

This example creates a table with two columns, each with an initial value and a `NOT` `NULL` constraint. Then it declares a record variable that represents a row of the table and prints its fields, showing that they did not inherit the initial values or `NOT` `NULL` constraints.

Live SQL:

You can view and run this example on Oracle Live SQL at [%ROWTYPE Variable Does Not Inherit Initial Values or Constraints](https://livesql.oracle.com/apex/livesql/docs/lnpls/plsql-collections-and-records/tdlnplscomposites79.html)

```
DROP TABLE t1;
CREATE TABLE t1 (
  c1 INTEGER DEFAULT 0 NOT NULL,
  c2 INTEGER DEFAULT 1 NOT NULL
);
 
DECLARE
  t1_row t1%ROWTYPE;
BEGIN
  DBMS_OUTPUT.PUT('t1.c1 = ');
  DBMS_OUTPUT.PUT_LINE(NVL(TO_CHAR(t1_row.c1), 'NULL'));

  DBMS_OUTPUT.PUT('t1.c2 = '); print(t1_row.c2);
  DBMS_OUTPUT.PUT_LINE(NVL(TO_CHAR(t1_row.c2), 'NULL'));
END;
/
```

Result:

```
t1.c1 = NULL
t1.c2 = NULL
```

#### Declaring a Record Variable that Can Represent Partial Row

To declare a record variable that can represent a partial row of a database table or view, use this syntax:

```
variable_name cursor%ROWTYPE;
```

A cursor is associated with a query. For every column that the query selects, the record variable must have a corresponding, type-compatible field. If the query selects every column of the table or view, then the variable represents a full row; otherwise, the variable represents a partial row. The cursor must be either an explicit cursor or a strong cursor variable.

See Also:

- " [FETCH Statement](FETCH-statement.md) " for complete syntax
- " [Cursors Overview](cursors-overview.md) " for information about cursors
- " [Explicit Cursors](cursors-overview.md) " for information about explicit cursors
- " [Cursor Variables](cursor-variables.md) " for information about cursor variables
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=SQLRF30046) for information about joins

Example 5-42 %ROWTYPE Variable Represents Partial Database Table Row

This example defines an explicit cursor whose query selects only the columns `first_name`, `last_name`, and `phone_number` from the `employees` table in the sample schema `HR`. Then the example declares a record variable that has a field for each column that the cursor selects. The variable represents a partial row of `employees`. Compare this example to Example 5-37.

Live SQL:

You can view and run this example on Oracle Live SQL at [%ROWTYPE Variable Represents Partial Database Table Row](https://livesql.oracle.com/apex/livesql/docs/lnpls/plsql-collections-and-records/tdlnplscomposites81.html)

```
DECLARE
  CURSOR c IS
    SELECT first_name, last_name, phone_number
    FROM employees;
 
  friend c%ROWTYPE;
BEGIN
  friend.first_name   := 'John';
  friend.last_name    := 'Smith';
  friend.phone_number := '1-650-555-1234';
  
  DBMS_OUTPUT.PUT_LINE (
    friend.first_name  || ' ' ||
    friend.last_name   || ', ' ||
    friend.phone_number
  );
END;
/
```

Result:

```
John Smith, 1-650-555-1234
```

Example 5-43 %ROWTYPE Variable Represents Join Row

This example defines an explicit cursor whose query is a join and then declares a record variable that has a field for each column that the cursor selects.

Live SQL:

You can view and run this example on Oracle Live SQL at [%ROWTYPE Variable Represents Join Row](https://livesql.oracle.com/apex/livesql/docs/lnpls/plsql-collections-and-records/tdlnplscomposites82.html)

```
DECLARE
  CURSOR c2 IS
    SELECT employee_id, email, employees.manager_id, location_id
    FROM employees, departments
    WHERE employees.department_id = departments.department_id;
  
  join_rec c2%ROWTYPE;  -- includes columns from two tables
  
BEGIN
  NULL;
END;
/
```

#### %ROWTYPE Attribute and Virtual Columns

If you use the `%ROWTYPE` attribute to define a record variable that represents a full row of a table that has a virtual column, then you cannot insert that record into the table. Instead, you must insert the individual record fields into the table, excluding the virtual column.

Example 5-44 Inserting %ROWTYPE Record into Table (Wrong)

This example creates a record variable that represents a full row of a table that has a virtual column, populates the record, and inserts the record into the table, causing ORA-54013.

```
DROP TABLE plch_departure;
 
CREATE TABLE plch_departure (
  destination    VARCHAR2(100),
  departure_time DATE,
  delay          NUMBER(10),
  expected       GENERATED ALWAYS AS (departure_time + delay/24/60/60)
);
 
 
DECLARE
 dep_rec plch_departure%ROWTYPE;
BEGIN
  dep_rec.destination := 'X'; 
  dep_rec.departure_time := SYSDATE;
  dep_rec.delay := 1500;
 
  INSERT INTO plch_departure VALUES dep_rec;
END;
/
```

Result:

```
DECLARE
*
ERROR at line 1:
ORA-54013: INSERT operation disallowed on virtual columns
ORA-06512: at line 8
```

Example 5-45 Inserting %ROWTYPE Record into Table (Right)

This solves the problem in Example 5-44 by inserting the individual record fields into the table, excluding the virtual column.

```
DECLARE
  dep_rec plch_departure%rowtype;
BEGIN
  dep_rec.destination := 'X';
  dep_rec.departure_time := SYSDATE;
  dep_rec.delay := 1500;
 
  INSERT INTO plch_departure (destination, departure_time, delay)
  VALUES (dep_rec.destination, dep_rec.departure_time, dep_rec.delay);
end;
/
```

Result:

```
PL/SQL procedure successfully completed.
```

#### %ROWTYPE Attribute and Invisible Columns

Suppose that you use the `%ROWTYPE` attribute to define a record variable that represents a row of a table that has an invisible column, and then you make the invisible column visible.

If you define the record variable with a cursor, as in " Declaring a Record Variable that Can Represent Partial Row ", then making the invisible column visible does not change the structure of the record variable.

However, if you define the record variable as in " Declaring a Record Variable that Always Represents Full Row " and use a `SELECT` `*` `INTO` statement to assign values to the record, then making the invisible column visible does change the structure of the record—see Example 5-46.

See Also:

[Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=SQLRF55897) for general information about invisible columns

Example 5-46 %ROWTYPE Affected by Making Invisible Column Visible

```
CREATE TABLE t (a INT, b INT, c INT INVISIBLE);
INSERT INTO t (a, b, c) VALUES (1, 2, 3);
COMMIT;

DECLARE
  t_rec t%ROWTYPE;  -- t_rec has fields a and b, but not c
BEGIN
  SELECT * INTO t_rec FROM t WHERE ROWNUM < 2;  -- t_rec(a)=1, t_rec(b)=2
  DBMS_OUTPUT.PUT_LINE('c = ' || t_rec.c);
END;
/
```

Result:

```
DBMS_OUTPUT.PUT_LINE('c = ' || t_rec.c);
                                       *
ERROR at line 5:
ORA-06550: line 5, column 40:
PLS-00302: component 'C' must be declared
ORA-06550: line 5, column 3:
PL/SQL: Statement ignored
```

Make invisible column visible:

```
ALTER TABLE t MODIFY (c VISIBLE);
```

Result:

```
Table altered.
```

Repeat preceding anonymous block:

```
DECLARE
  t_rec t%ROWTYPE;  -- t_rec has fields a, b, and c
BEGIN
  SELECT * INTO t_rec FROM t WHERE ROWNUM < 2;  -- t_rec(a)=1, t_rec(b)=2,
                                                  -- t_rec(c)=3
  DBMS_OUTPUT.PUT_LINE('c = ' || t_rec.c);
END;
/
```

Result:

```
c = 3
 
PL/SQL procedure successfully completed.
```