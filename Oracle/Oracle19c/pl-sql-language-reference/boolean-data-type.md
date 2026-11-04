---
title: Database PL/SQL Language Reference
book: Database PL/SQL Language Reference
doc_id: E96448-09
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/boolean-data-type.html
tags:
  - oracle
  - 19c
  - pl-sql-language-reference
---

## BOOLEAN Data Type

The PL/SQL data type `BOOLEAN` stores logical values, which are the boolean values `TRUE` and `FALSE` and the value `NULL`. `NULL` represents an unknown value.

The syntax for declaring an `BOOLEAN` variable is:

```
variable_name BOOLEAN
```

The only value that you can assign to a `BOOLEAN` variable is a `BOOLEAN` expression. For details, see " [BOOLEAN Expressions](expressions.md) ".

Because SQL has no data type equivalent to `BOOLEAN`, you cannot:

- Assign a `BOOLEAN` value to a database table column
- Select or fetch the value of a database table column into a `BOOLEAN` variable
- Use a `BOOLEAN` value in a SQL function
	(However, a SQL query can invoke a PL/SQL function that has a `BOOLEAN` parameter, as in " Example 3-3 ".)
- Use a `BOOLEAN` expression in a SQL statement, except as an argument to a PL/SQL function invoked in a SQL query, or in a PL/SQL anonymous block.
	Note:
	An argument to a PL/SQL function invoked in a static SQL query cannot be a `BOOLEAN` literal. The workaround is to assign the literal to a variable and then pass the variable to the function, as in " Example 3-3 ".

You cannot pass a `BOOLEAN` value to the `DBMS_OUTPUT`.`PUT` or `DBMS_OUTPUT`.`PUTLINE` subprogram. To print a `BOOLEAN` value, use an `IF` or `CASE` statement to translate it to a character value (for information about these statements, see " [Conditional Selection Statements](conditional-selection-statements.md) ").

Example 3-2 Printing BOOLEAN Values

In this example, the procedure accepts a `BOOLEAN` parameter and uses a `CASE` statement to print `Unknown` if the value of the parameter is `NULL`, `Yes` if it is `TRUE`, and `No` if it is `FALSE`.

See Also:

[Example 2-34](expressions.md), which creates a `print_boolean` procedure that uses an `IF` statement.

```
PROCEDURE print_boolean (b BOOLEAN)
AS
BEGIN
  DBMS_OUTPUT.PUT_LINE (
    CASE
      WHEN b IS NULL THEN 'Unknown'
      WHEN b THEN 'Yes'
      WHEN NOT b THEN 'No'
    END
  );
END;

BEGIN
  print_boolean(TRUE);
  print_boolean(FALSE);
  print_boolean(NULL);
END;
```

Result:

```
Yes
No
Unknown
```

Example 3-3 SQL Statement Invokes PL/SQL Function with BOOLEAN Parameter

In this example, a SQL statement invokes a PL/SQL function that has a `BOOLEAN` parameter.

```
FUNCTION f (x BOOLEAN, y PLS_INTEGER)
  RETURN employees.employee_id%TYPE
  AUTHID CURRENT_USER AS
BEGIN
  IF x THEN
    RETURN y;
  ELSE
    RETURN 2*y;
  END IF;
END;
 
DECLARE
  name employees.last_name%TYPE;
  b BOOLEAN := TRUE;
BEGIN
  SELECT last_name INTO name
  FROM employees
  WHERE employee_id = f(b, 100);
 
  DBMS_OUTPUT.PUT_LINE(name);
 
  b := FALSE;
 
  SELECT last_name INTO name
  FROM employees
  WHERE employee_id = f(b, 100);
 
  DBMS_OUTPUT.PUT_LINE(name);
END;
/
```

Result:

```
King
Whalen
```