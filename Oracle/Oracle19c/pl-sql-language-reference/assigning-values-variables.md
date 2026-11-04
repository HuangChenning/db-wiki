---
title: Database PL/SQL Language Reference
book: Database PL/SQL Language Reference
doc_id: E96448-09
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/assigning-values-variables.html
tags:
  - oracle
  - 19c
  - pl-sql-language-reference
---

## Assigning Values to Variables

After declaring a variable, you can assign a value to it in these ways:

- Use the assignment statement to assign it the value of an expression.
- Use the `SELECT` `INTO` or `FETCH` statement to assign it a value from a table.
- Pass it to a subprogram as an `OUT` or `IN` `OUT` parameter, and then assign the value inside the subprogram.

The variable and the value must have compatible data types. One data type is compatible with another data type if it can be implicitly converted to that type. For information about implicit data conversion, see [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=SQLRF51047).

Topics

See Also:

- " [Assigning Values to Collection Variables](assigning-values-collection-variables.md) "
- " [Assigning Values to Record Variables](assigning-values-record-variables.md) "
- " [FETCH Statement](FETCH-statement.md) "

### Assigning Values to Variables with the Assignment Statement

To assign the value of an expression to a variable, use this form of the assignment statement:

```
variable_name := expression;
```

For the complete syntax of the assignment statement, see " [Assignment Statement](assignment-statement.md) ".

For the syntax of an expression, see " [Expression](expression.md) ".

Example 2-24 Assigning Values to Variables with Assignment Statement

This example declares several variables (specifying initial values for some) and then uses assignment statements to assign the values of expressions to them.

```
DECLARE  -- You can assign initial values here
  wages          NUMBER;
  hours_worked   NUMBER := 40;
  hourly_salary  NUMBER := 22.50;
  bonus          NUMBER := 150;
  country        VARCHAR2(128);
  counter        NUMBER := 0;
  done           BOOLEAN;
  valid_id       BOOLEAN;
  emp_rec1       employees%ROWTYPE;
  emp_rec2       employees%ROWTYPE;
  TYPE commissions IS TABLE OF NUMBER INDEX BY PLS_INTEGER;
  comm_tab       commissions;
 
BEGIN  -- You can assign values here too
  wages := (hours_worked * hourly_salary) + bonus;
  country := 'France';
  country := UPPER('Canada');
  done := (counter > 100);
  valid_id := TRUE;
  emp_rec1.first_name := 'Antonio';
  emp_rec1.last_name := 'Ortiz';
  emp_rec1 := emp_rec2;
  comm_tab(5) := 20000 * 0.15;
END;
/
```

### Assigning Values to Variables with the SELECT INTO Statement

A simple form of the `SELECT` `INTO` statement is:

```
SELECT select_item [, select_item ]... 
INTO variable_name [, variable_name ]...
FROM table_name;
```

For each `select_item`, there must be a corresponding, type-compatible `variable_name`. Because SQL does not have a `BOOLEAN` type, `variable_name` cannot be a `BOOLEAN` variable.

For the complete syntax of the `SELECT` `INTO` statement, see " [SELECT INTO Statement](SELECT-INTO-statement.md) ".

Example 2-25 Assigning Value to Variable with SELECT INTO Statement

This example uses a `SELECT` `INTO` statement to assign to the variable `bonus` the value that is 10% of the salary of the employee whose `employee_id` is 100.

```
DECLARE
  bonus   NUMBER(8,2);
BEGIN
  SELECT salary * 0.10 INTO bonus
  FROM employees
  WHERE employee_id = 100;
END;

DBMS_OUTPUT.PUT_LINE('bonus = ' || TO_CHAR(bonus));
/
```

Result:

```
bonus = 2400
```

### Assigning Values to Variables as Parameters of a Subprogram

If you pass a variable to a subprogram as an `OUT` or `IN` `OUT` parameter, and the subprogram assigns a value to the parameter, the variable retains that value after the subprogram finishes running. For more information, see " [Subprogram Parameters](subprogram-parameters.md) ".

Example 2-26 Assigning Value to Variable as IN OUT Subprogram Parameter

This example passes the variable `new_sal` to the procedure `adjust_salary`. The procedure assigns a value to the corresponding formal parameter, `sal`. Because `sal` is an `IN` `OUT` parameter, the variable `new_sal` retains the assigned value after the procedure finishes running.

```
DECLARE
  emp_salary  NUMBER(8,2);
 
  PROCEDURE adjust_salary (
    emp        NUMBER, 
    sal IN OUT NUMBER,
    adjustment NUMBER
  ) IS
  BEGIN
    sal := sal + adjustment;
  END;
 
BEGIN
  SELECT salary INTO emp_salary
  FROM employees
  WHERE employee_id = 100;
 
  DBMS_OUTPUT.PUT_LINE
   ('Before invoking procedure, emp_salary: ' || emp_salary);
 
  adjust_salary (100, emp_salary, 1000);
 
  DBMS_OUTPUT.PUT_LINE
   ('After invoking procedure, emp_salary: ' || emp_salary);
END;
/
```

Result:

```
Before invoking procedure, emp_salary: 24000
After invoking procedure, emp_salary: 25000
```

### Assigning Values to BOOLEAN Variables

The only values that you can assign to a `BOOLEAN` variable are `TRUE`, `FALSE`, and `NULL`.

For more information about the `BOOLEAN` data type, see " [BOOLEAN Data Type](boolean-data-type.md) ".

Example 2-27 Assigning Value to BOOLEAN Variable

This example initializes the `BOOLEAN` variable `done` to `NULL` by default, assigns it the literal value `FALSE`, compares it to the literal value `TRUE`, and assigns it the value of a `BOOLEAN` expression.

```
DECLARE
  done    BOOLEAN;              -- Initial value is NULL by default
  counter NUMBER := 0;
BEGIN
  done := FALSE;                -- Assign literal value
  WHILE done != TRUE            -- Compare to literal value
    LOOP
      counter := counter + 1;
      done := (counter > 500);  -- Assign value of BOOLEAN expression
    END LOOP;
END;
/
```