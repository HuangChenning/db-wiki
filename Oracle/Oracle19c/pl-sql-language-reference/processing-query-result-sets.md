---
title: Database PL/SQL Language Reference
book: Database PL/SQL Language Reference
doc_id: E96448-09
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/processing-query-result-sets.html
tags:
  - oracle
  - 19c
  - pl-sql-language-reference
---

## Processing Query Result Sets

In PL/SQL, as in traditional database programming, you use cursors to process query result sets. However, in PL/SQL, you can use either implicit or explicit cursors.

The former need less code, but the latter are more flexible. For example, explicit cursors can accept parameters.

The following PL/SQL statements use implicit cursors that PL/SQL defines and manages for you:

- `SELECT` `INTO`
- Implicit cursor `FOR` `LOOP`

The following PL/SQL statements use explicit cursors:

- Explicit cursor `FOR` `LOOP`
	You define the explicit cursor, but PL/SQL manages it while the statement runs.
- `OPEN`, `FETCH`, and `CLOSE`
	You define and manage the explicit cursor.

Note:

If a query returns no rows, PL/SQL raises the exception `NO_DATA_FOUND`.

Topics

See Also:

- " [Explicit Cursors that Accept Parameters](cursors-overview.md) "
- [Oracle Database Development Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=ADFNS00903) for information about returning result sets to clients
- " [Exception Handler](exception-handler.md) " for information about handling exceptions

### Processing Query Result Sets With SELECT INTO Statements

Using an implicit cursor, the `SELECT` `INTO` statement retrieves values from one or more database tables (as the SQL `SELECT` statement does) and stores them in variables (which the SQL `SELECT` statement does not do).

Topics

- Handling Single-Row Result Sets
- Handling Large Multiple-Row Result Sets

See Also:

" [SELECT INTO Statement](SELECT-INTO-statement.md) " for its complete syntax and semantics

#### Handling Single-Row Result Sets

If you expect the query to return only one row, then use the `SELECT` `INTO` statement to store values from that row in either one or more scalar variables, or one record variable.

If the query might return multiple rows, but you care about only the nth row, then restrict the result set to that row with the clause `WHERE` `ROWNUM=` `n`.

See Also:

- " [Assigning Values to Variables with the SELECT INTO Statement](assigning-values-variables.md) "
- " [Using SELECT INTO to Assign a Row to a Record Variable](assigning-values-record-variables.md) "
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=SQLRF00255) for more information about the `ROWNUM` pseudocolumn

#### Handling Large Multiple-Row Result Sets

If you must assign a large quantity of table data to variables, Oracle recommends using the `SELECT` `INTO` statement with the `BULK` `COLLECT` clause.

This statement retrieves an entire result set into one or more collection variables.

For more information, see " [SELECT INTO Statement with BULK COLLECT Clause](bulk-sql-and-bulk-binding.md) ".

### Processing Query Result Sets With Cursor FOR LOOP Statements

The cursor `FOR` `LOOP` statement lets you run a `SELECT` statement and then immediately loop through the rows of the result set.

This statement can use either an implicit or explicit cursor (but not a cursor variable).

If you use the `SELECT` statement only in the cursor `FOR` `LOOP` statement, then specify the `SELECT` statement inside the cursor `FOR` `LOOP` statement, as in Example 6-18. This form of the cursor `FOR` `LOOP` statement uses an implicit cursor, and is called an implicit cursor `FOR` `LOOP` statement. Because the implicit cursor is internal to the statement, you cannot reference it with the name `SQL`.

If you use the `SELECT` statement multiple times in the same PL/SQL unit, then define an explicit cursor for it and specify that cursor in the cursor `FOR` `LOOP` statement, as in Example 6-19. This form of the cursor `FOR` `LOOP` statement is called an explicit cursor `FOR` `LOOP` statement. You can use the same explicit cursor elsewhere in the same PL/SQL unit.

The cursor `FOR` `LOOP` statement implicitly declares its loop index as a `%ROWTYPE` record variable of the type that its cursor returns. This record is local to the loop and exists only during loop execution. Statements inside the loop can reference the record and its fields. They can reference virtual columns only by aliases, as in Example 6-21.

After declaring the loop index record variable, the `FOR` `LOOP` statement opens the specified cursor. With each iteration of the loop, the `FOR` `LOOP` statement fetches a row from the result set and stores it in the record. When there are no more rows to fetch, the cursor `FOR` `LOOP` statement closes the cursor. The cursor also closes if a statement inside the loop transfers control outside the loop or if PL/SQL raises an exception.

See Also:

" [Cursor FOR LOOP Statement](cursor-FOR-LOOP-statement.md) " for its complete syntax and semantics

Note:

When an exception is raised inside a cursor `FOR` `LOOP` statement, the cursor closes before the exception handler runs. Therefore, the values of explicit cursor attributes are not available in the handler.

Example 6-18 Implicit Cursor FOR LOOP Statement

In this example, an implicit cursor `FOR` `LOOP` statement prints the last name and job ID of every clerk whose manager has an ID greater than 120.

```
BEGIN
  FOR item IN (
    SELECT last_name, job_id
    FROM employees
    WHERE job_id LIKE '%CLERK%'
    AND manager_id > 120
    ORDER BY last_name
  )
  LOOP
    DBMS_OUTPUT.PUT_LINE
      ('Name = ' || item.last_name || ', Job = ' || item.job_id);
  END LOOP;
END;
/
```

Result:

```
Name = Atkinson, Job = ST_CLERK
Name = Bell, Job = SH_CLERK
Name = Bissot, Job = ST_CLERK
...
Name = Walsh, Job = SH_CLERK
```

Example 6-19 Explicit Cursor FOR LOOP Statement

This exmaple is like Example 6-18, except that it uses an explicit cursor `FOR` `LOOP` statement.

```
DECLARE
  CURSOR c1 IS
    SELECT last_name, job_id FROM employees
    WHERE job_id LIKE '%CLERK%' AND manager_id > 120
    ORDER BY last_name;
BEGIN
  FOR item IN c1
  LOOP
    DBMS_OUTPUT.PUT_LINE
      ('Name = ' || item.last_name || ', Job = ' || item.job_id);
  END LOOP;
END;
/
```

Result:

```
Name = Atkinson, Job = ST_CLERK
Name = Bell, Job = SH_CLERK
Name = Bissot, Job = ST_CLERK
...
Name = Walsh, Job = SH_CLERK
```

Example 6-20 Passing Parameters to Explicit Cursor FOR LOOP Statement

This example declares and defines an explicit cursor that accepts two parameters, and then uses it in an explicit cursor `FOR` `LOOP` statement to display the wages paid to employees who earn more than a specified wage in a specified department.

```
DECLARE
  CURSOR c1 (job VARCHAR2, max_wage NUMBER) IS
    SELECT * FROM employees
    WHERE job_id = job
    AND salary > max_wage;
BEGIN
  FOR person IN c1('ST_CLERK', 3000)
  LOOP
     -- process data record
    DBMS_OUTPUT.PUT_LINE (
      'Name = ' || person.last_name || ', salary = ' ||
      person.salary || ', Job Id = ' || person.job_id
    );
  END LOOP;
END;
/
```

Result:

```
Name = Nayer, salary = 3200, Job Id = ST_CLERK
Name = Bissot, salary = 3300, Job Id = ST_CLERK
Name = Mallin, salary = 3300, Job Id = ST_CLERK
Name = Ladwig, salary = 3600, Job Id = ST_CLERK
Name = Stiles, salary = 3200, Job Id = ST_CLERK
Name = Rajs, salary = 3500, Job Id = ST_CLERK
Name = Davies, salary = 3100, Job Id = ST_CLERK
```

Example 6-21 Cursor FOR Loop References Virtual Columns

In this example, the implicit cursor `FOR` `LOOP` references virtual columns by their aliases, `full_name` and `dream_salary`.

```
BEGIN
  FOR item IN (
    SELECT first_name || ' ' || last_name AS full_name,
           salary * 10                    AS dream_salary 
    FROM employees
    WHERE ROWNUM <= 5
    ORDER BY dream_salary DESC, last_name ASC
  ) LOOP
    DBMS_OUTPUT.PUT_LINE
      (item.full_name || ' dreams of making ' || item.dream_salary);
  END LOOP;
END;
/
```

Result:

```
Stephen King dreams of making 240000
Lex De Haan dreams of making 170000
Neena Kochhar dreams of making 170000
Alexander Hunold dreams of making 90000
Bruce Ernst dreams of making 60000
```

### Processing Query Result Sets With Explicit Cursors, OPEN, FETCH, and CLOSE

For full control over query result set processing, declare explicit cursors and manage them with the statements OPEN, FETCH, and CLOSE.

This result set processing technique is more complicated than the others, but it is also more flexible. For example, you can:

- Process multiple result sets in parallel, using multiple cursors.
- Process multiple rows in a single loop iteration, skip rows, or split the processing into multiple loops.
- Specify the query in one PL/SQL unit but retrieve the rows in another.

For instructions and examples, see " [Explicit Cursors](cursors-overview.md) ".

### Processing Query Result Sets with Subqueries

If you process a query result set by looping through it and running another query for each row, then you can improve performance by removing the second query from inside the loop and making it a subquery of the first query.

While an ordinary subquery is evaluated for each table, a correlated subquery is evaluated for each row.

For more information about subqueries, see [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=SQLRF52357).

Example 6-22 Subquery in FROM Clause of Parent Query

This example defines explicit cursor `c1` with a query whose `FROM` clause contains a subquery.

```
DECLARE
  CURSOR c1 IS
    SELECT t1.department_id, department_name, staff
    FROM departments t1,
         ( SELECT department_id, COUNT(*) AS staff
           FROM employees
           GROUP BY department_id
         ) t2
    WHERE (t1.department_id = t2.department_id) AND staff >= 5
    ORDER BY staff;

BEGIN
   FOR dept IN c1
   LOOP
     DBMS_OUTPUT.PUT_LINE ('Department = '
       || dept.department_name || ', staff = ' || dept.staff);
   END LOOP;
END;
/
```

Result:

```
Department = IT, staff = 5
Department = Finance, staff = 6
Department = Purchasing, staff = 6
Department = Sales, staff = 34
Department = Shipping, staff = 45
```

Example 6-23 Correlated Subquery

This example returns the name and salary of each employee whose salary exceeds the departmental average. For each row in the table, the correlated subquery computes the average salary for the corresponding department.

```
DECLARE
  CURSOR c1 IS
    SELECT department_id, last_name, salary
    FROM employees t
    WHERE salary > ( SELECT AVG(salary)
                     FROM employees
                     WHERE t.department_id = department_id
                   )
    ORDER BY department_id, last_name;
BEGIN
  FOR person IN c1
  LOOP
    DBMS_OUTPUT.PUT_LINE('Making above-average salary = ' || person.last_name);
  END LOOP;
END;
/
```

Result:

```
Making above-average salary = Hartstein
Making above-average salary = Raphaely
Making above-average salary = Bell
...
Making above-average salary = Higgins
```