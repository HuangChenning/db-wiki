---
title: Database PL/SQL Language Reference
book: Database PL/SQL Language Reference
doc_id: E96448-09
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/declarations.html
tags:
  - oracle
  - 19c
  - pl-sql-language-reference
---

## Declarations

A declaration allocates storage space for a value of a specified data type, and names the storage location so that you can reference it.

You must declare objects before you can reference them. Declarations can appear in the declarative part of any block, subprogram, or package.

Topics

For information about declaring objects other than variables and constants, see the syntax of `declare_section` in " [Block](block.md) ".

### NOT NULL Constraint

You can impose the `NOT` `NULL` constraint on a scalar variable or constant (or scalar component of a composite variable or constant).

The `NOT` `NULL` constraint prevents assigning a null value to the item. The item can acquire this constraint either implicitly (from its data type) or explicitly.

A scalar variable declaration that specifies `NOT` `NULL`, either implicitly or explicitly, must assign an initial value to the variable (because the default initial value for a scalar variable is `NULL`).

PL/SQL treats any zero-length string as a `NULL` value. This includes values returned by character functions and `BOOLEAN` expressions.

To test for a `NULL` value, use the " [IS \[NOT\] NULL Operator](https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/expressions.html#GUID-D02FA4D0-0074-4227-9624-F01E3D219BAB "The IS NULL operator returns the BOOLEAN value TRUE if its operand is NULL or FALSE if it is not NULL. The IS NOT NULL operator does the opposite.") ".

Examples

Example 2-9 Variable Declaration with NOT NULL Constraint

In this example, the variable `acct_id` acquires the `NOT` `NULL` constraint explicitly, and the variables `a`, `b`, and `c` acquire it from their data types.

```
DECLARE
  acct_id INTEGER(4) NOT NULL := 9999;
  a NATURALN                  := 9999;
  b POSITIVEN                 := 9999;
  c SIMPLE_INTEGER            := 9999;
BEGIN
  NULL;
END;
/
```

Example 2-10 Variables Initialized to NULL Values

In this example, all variables are initialized to `NULL`.

```
DECLARE
  null_string  VARCHAR2(80) := TO_CHAR('');
  address      VARCHAR2(80);
  zip_code     VARCHAR2(80) := SUBSTR(address, 25, 0);
  name         VARCHAR2(80);
  valid        BOOLEAN      := (name != '');
BEGIN
  NULL;
END;
/
```

### Declaring Variables

A variable declaration always specifies the name and data type of the variable.

For most data types, a variable declaration can also specify an initial value.

The variable name must be a valid user-defined identifier.

The data type can be any PL/SQL data type. The PL/SQL data types include the SQL data types. A data type is either scalar (without internal components) or composite (with internal components).

Example

Example 2-11 Scalar Variable Declarations

This example declares several variables with scalar data types.

```
DECLARE
  part_number       NUMBER(6);     -- SQL data type
  part_name         VARCHAR2(20);  -- SQL data type
  in_stock          BOOLEAN;       -- PL/SQL-only data type
  part_price        NUMBER(6,2);   -- SQL data type
  part_description  VARCHAR2(50);  -- SQL data type
BEGIN
  NULL;
END;
/
```

Related Topics

- " [User-Defined Identifiers](lexical-units.md) "
- " [Scalar Variable Declaration](scalar-variable-declaration.md) " for scalar variable declaration syntax
- [PL/SQL Data Types](plsql-data-types.md) for information about scalar data types
- [PL/SQL Collections and Records](plsql-collections-and-records.md), for information about composite data types and variables

### Declaring Constants

A constant holds a value that does not change.

The information in " Declaring Variables " also applies to constant declarations, but a constant declaration has two more requirements: the keyword `CONSTANT` and the initial value of the constant. (The initial value of a constant is its permanent value.)

Example 2-12 Constant Declarations

This example declares three constants with scalar data types.

```
DECLARE
  credit_limit     CONSTANT REAL    := 5000.00;  -- SQL data type
  max_days_in_year CONSTANT INTEGER := 366;      -- SQL data type
  urban_legend     CONSTANT BOOLEAN := FALSE;    -- PL/SQL-only data type
BEGIN
  NULL;
END;
/
```

### Initial Values of Variables and Constants

In a variable declaration, the initial value is optional unless you specify the `NOT` `NULL` constraint. In a constant declaration, the initial value is required.

If the declaration is in a block or subprogram, the initial value is assigned to the variable or constant every time control passes to the block or subprogram. If the declaration is in a package specification, the initial value is assigned to the variable or constant for each session (whether the variable or constant is public or private).

To specify the initial value, use either the assignment operator (`:=`) or the keyword `DEFAULT`, followed by an expression. The expression can include previously declared constants and previously initialized variables.

If you do not specify an initial value for a variable, assign a value to it before using it in any other context.

Examples

Example 2-13 Variable and Constant Declarations with Initial Values

This example assigns initial values to the constant and variables that it declares. The initial value of `area` depends on the previously declared constant `pi` and the previously initialized variable `radius`.

```
DECLARE
  hours_worked    INTEGER := 40;
  employee_count  INTEGER := 0;

  pi     CONSTANT REAL := 3.14159;
  radius          REAL := 1;
  area            REAL := (pi * radius**2);
BEGIN
  NULL;
END;
/
```

Example 2-14 Variable Initialized to NULL by Default

In this example, the variable `counter` has the initial value `NULL`, by default. The example uses the " [IS \[NOT\] NULL Operator](https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/expressions.html#GUID-D02FA4D0-0074-4227-9624-F01E3D219BAB "The IS NULL operator returns the BOOLEAN value TRUE if its operand is NULL or FALSE if it is not NULL. The IS NOT NULL operator does the opposite.") " to show that `NULL` is different from zero.

```
DECLARE
  counter INTEGER;  -- initial value is NULL by default
BEGIN
  counter := counter + 1;  -- NULL + 1 is still NULL
  
  IF counter IS NULL THEN
    DBMS_OUTPUT.PUT_LINE('counter is NULL.');
  END IF;
END;
/
```

Result:

```
counter is NULL.
```

### Declaring Items using the %TYPE Attribute

The `%TYPE` attribute lets you declare a data item of the same data type as a previously declared variable or column (without knowing what that type is). If the declaration of the referenced item changes, then the declaration of the referencing item changes accordingly.

The syntax of the declaration is:

```
referencing_item referenced_item%TYPE;
```

For the kinds of items that can be referencing and referenced items, see " [%TYPE Attribute](TYPE-attribute.md) ".

The referencing item inherits the following from the referenced item:

- Data type and size
- Constraints (unless the referenced item is a column)

The referencing item does not inherit the initial value of the referenced item. Therefore, if the referencing item specifies or inherits the `NOT` `NULL` constraint, you must specify an initial value for it.

The `%TYPE` attribute is particularly useful when declaring variables to hold database values. The syntax for declaring a variable of the same type as a column is:

```
variable_name table_name.column_name%TYPE;
```

See Also:

" [Declaring Items using the %ROWTYPE Attribute](record-variables.md) ", which lets you declare a record variable that represents either a full or partial row of a database table or view

Examples

Example 2-15 Declaring Variable of Same Type as Column

In this example, the variable `surname` inherits the data type and size of the column `employees`.`last_name`, which has a `NOT` `NULL` constraint. Because `surname` does not inherit the `NOT` `NULL` constraint, its declaration does not need an initial value.

```
DECLARE
  surname  employees.last_name%TYPE;
BEGIN
  DBMS_OUTPUT.PUT_LINE('surname=' || surname);
END;
/
```

Result:

```
surname=
```

Example 2-16 Declaring Variable of Same Type as Another Variable

In this example, the variable `surname` inherits the data type, size, and `NOT` `NULL` constraint of the variable `name`. Because `surname` does not inherit the initial value of `name`, its declaration needs an initial value (which cannot exceed 25 characters).

```
DECLARE
  name     VARCHAR(25) NOT NULL := 'Smith';
  surname  name%TYPE := 'Jones';
BEGIN
  DBMS_OUTPUT.PUT_LINE('name=' || name);
  DBMS_OUTPUT.PUT_LINE('surname=' || surname);
END;
/
```

Result:

```
name=Smith
surname=Jones
```