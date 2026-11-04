---
title: Database PL/SQL Language Reference
book: Database PL/SQL Language Reference
doc_id: E96448-09
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/cursor-expressions.html
tags:
  - oracle
  - 19c
  - pl-sql-language-reference
---

## CURSOR Expressions

A `CURSOR` expression returns a nested cursor.

It has this syntax:

```
CURSOR ( subquery )
```

You can use a `CURSOR` expression in a `SELECT` statement that is not a subquery (as in Example 6-35) or pass it to a function that accepts a cursor variable parameter (see " [Passing CURSOR Expressions to Pipelined Table Functions](chaining-pipelined-table-functions-multiple-transformations.md) "). You cannot use a cursor expression with an implicit cursor.

See Also:

[Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=SQLRF52077) for more information about `CURSOR` expressions, including restrictions

Example 6-35 CURSOR Expression

This example declares and defines an explicit cursor for a query that includes a cursor expression. For each department in the `departments` table, the nested cursor returns the last name of each employee in that department (which it retrieves from the `employees` table).

```
DECLARE
  TYPE emp_cur_typ IS REF CURSOR;
 
  emp_cur    emp_cur_typ;
  dept_name  departments.department_name%TYPE;
  emp_name   employees.last_name%TYPE;
 
  CURSOR c1 IS
    SELECT department_name,
      CURSOR ( SELECT e.last_name
                FROM employees e
                WHERE e.department_id = d.department_id
                ORDER BY e.last_name
              ) employees
    FROM departments d
    WHERE department_name LIKE 'A%'
    ORDER BY department_name;
BEGIN
  OPEN c1;
  LOOP  -- Process each row of query result set
    FETCH c1 INTO dept_name, emp_cur;
    EXIT WHEN c1%NOTFOUND;
    DBMS_OUTPUT.PUT_LINE('Department: ' || dept_name);
 
    LOOP -- Process each row of subquery result set
      FETCH emp_cur INTO emp_name;
      EXIT WHEN emp_cur%NOTFOUND;
      DBMS_OUTPUT.PUT_LINE('-- Employee: ' || emp_name);
    END LOOP;
  END LOOP;
  CLOSE c1;
END;
/
```

Result:

```
Department: Accounting
-- Employee: Gietz
-- Employee: Higgins
Department: Administration
-- Employee: Whalen
```