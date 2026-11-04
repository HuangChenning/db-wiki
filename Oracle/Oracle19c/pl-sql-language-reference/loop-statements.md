---
title: Database PL/SQL Language Reference
book: Database PL/SQL Language Reference
doc_id: E96448-09
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/loop-statements.html
tags:
  - oracle
  - 19c
  - pl-sql-language-reference
---

## LOOP Statements

Loop statements run the same statements with a series of different values. The loop statements are:

- Basic `LOOP`
- `FOR` `LOOP`
- Cursor `FOR` `LOOP`
- `WHILE` `LOOP`

The statements that exit a loop are:

- `EXIT`
- `EXIT` `WHEN`

The statements that exit the current iteration of a loop are:

- `CONTINUE`
- `CONTINUE` `WHEN`

`EXIT`, `EXIT` `WHEN`, `CONTINUE`, and `CONTINUE` `WHEN` and can appear anywhere inside a loop, but not outside a loop. Oracle recommends using these statements instead of the " [GOTO Statement](sequential-control-statements.md) ", which can exit a loop or the current iteration of a loop by transferring control to a statement outside the loop. (A raised exception also exits a loop. For information about exceptions, see " [Overview of Exception Handling](overview-exception-handling.md) ".)

`LOOP` statements can be labeled, and `LOOP` statements can be nested. Labels are recommended for nested loops to improve readability. You must ensure that the label in the `END` `LOOP` statement matches the label at the beginning of the same loop statement (the compiler does not check).

Topics

For information about the cursor `FOR` `LOOP`, see " [Processing Query Result Sets With Cursor FOR LOOP Statements](processing-query-result-sets.md) ".

### Basic LOOP Statement

The basic `LOOP` statement has this structure:

```
[ label ] LOOP
  statements
END LOOP [ label ];
```

With each iteration of the loop, the `statements` run and control returns to the top of the loop. To prevent an infinite loop, a statement or raised exception must exit the loop.

See Also:

" [Basic LOOP Statement](basic-LOOP-statement.md) "

### EXIT Statement

The `EXIT` statement exits the current iteration of a loop unconditionally and transfers control to the end of either the current loop or an enclosing labeled loop.

In Example 4-9, the `EXIT` statement inside the basic `LOOP` statement transfers control unconditionally to the end of the current loop.

See Also:

" [EXIT Statement](EXIT-statement.md) "

Example 4-9 Basic LOOP Statement with EXIT Statement

```
DECLARE
  x NUMBER := 0;
BEGIN
  LOOP
    DBMS_OUTPUT.PUT_LINE ('Inside loop:  x = ' || TO_CHAR(x));
    x := x + 1;
    IF x > 3 THEN
      EXIT;
    END IF;
  END LOOP;
  -- After EXIT, control resumes here
  DBMS_OUTPUT.PUT_LINE(' After loop:  x = ' || TO_CHAR(x));
END;
/
```

Result:

```
Inside loop:  x = 0
Inside loop:  x = 1
Inside loop:  x = 2
Inside loop:  x = 3
After loop:  x = 4
```

### EXIT WHEN Statement

The `EXIT` `WHEN` statement exits the current iteration of a loop when the condition in its `WHEN` clause is true, and transfers control to the end of either the current loop or an enclosing labeled loop.

Each time control reaches the `EXIT` `WHEN` statement, the condition in its `WHEN` clause is evaluated. If the condition is not true, the `EXIT` `WHEN` statement does nothing. To prevent an infinite loop, a statement inside the loop must make the condition true, as in Example 4-10.

In Example 4-10, the `EXIT` `WHEN` statement inside the basic `LOOP` statement transfers control to the end of the current loop when `x` is greater than 3. Example 4-10 is logically equivalent to Example 4-9.

See Also:

" [EXIT Statement](EXIT-statement.md) "

In Example 4-11, one basic `LOOP` statement is nested inside the other, and both have labels. The inner loop has two `EXIT` `WHEN` statements; one that exits the inner loop and one that exits the outer loop.

An `EXIT` `WHEN` statement in an inner loop can transfer control to an outer loop only if the outer loop is labeled.

In Example 4-12, the outer loop is not labeled; therefore, the inner loop cannot transfer control to it.

Example 4-10 Basic LOOP Statement with EXIT WHEN Statement

```
DECLARE
  x NUMBER := 0;
BEGIN
  LOOP
    DBMS_OUTPUT.PUT_LINE('Inside loop:  x = ' || TO_CHAR(x));
    x := x + 1;  -- prevents infinite loop
    EXIT WHEN x > 3;
  END LOOP;
  -- After EXIT statement, control resumes here
  DBMS_OUTPUT.PUT_LINE('After loop:  x = ' || TO_CHAR(x));
END;
/
```

Result:

```
Inside loop:  x = 0
Inside loop:  x = 1
Inside loop:  x = 2
Inside loop:  x = 3
After loop:  x = 4
```

Example 4-11 Nested, Labeled Basic LOOP Statements with EXIT WHEN Statements

```
DECLARE
  s  PLS_INTEGER := 0;
  i  PLS_INTEGER := 0;
  j  PLS_INTEGER;
BEGIN
  <<outer_loop>>
  LOOP
    i := i + 1;
    j := 0;
    <<inner_loop>>
    LOOP
      j := j + 1;
      s := s + i * j; -- Sum several products
      EXIT inner_loop WHEN (j > 5);
      EXIT outer_loop WHEN ((i * j) > 15);
    END LOOP inner_loop;
  END LOOP outer_loop;
  DBMS_OUTPUT.PUT_LINE
    ('The sum of products equals: ' || TO_CHAR(s));
END;
/
```

Result:

```
The sum of products equals: 166
```

Example 4-12 Nested, Unabeled Basic LOOP Statements with EXIT WHEN Statements

```
DECLARE
  i PLS_INTEGER := 0;
  j PLS_INTEGER := 0;
 
BEGIN
  LOOP
    i := i + 1;
    DBMS_OUTPUT.PUT_LINE ('i = ' || i);
    
    LOOP
      j := j + 1;
      DBMS_OUTPUT.PUT_LINE ('j = ' || j);
      EXIT WHEN (j > 3);
    END LOOP;
 
    DBMS_OUTPUT.PUT_LINE ('Exited inner loop');
 
    EXIT WHEN (i > 2);
  END LOOP;
 
  DBMS_OUTPUT.PUT_LINE ('Exited outer loop');
END;
/
```

Result:

```
i = 1
j = 1
j = 2
j = 3
j = 4
Exited inner loop
i = 2
j = 5
Exited inner loop
i = 3
j = 6
Exited inner loop
Exited outer loop
 
PL/SQL procedure successfully completed.
```

### CONTINUE Statement

The `CONTINUE` statement exits the current iteration of a loop unconditionally and transfers control to the next iteration of either the current loop or an enclosing labeled loop.

In Example 4-13, the `CONTINUE` statement inside the basic `LOOP` statement transfers control unconditionally to the next iteration of the current loop.

See Also:

" [CONTINUE Statement](CONTINUE-statement.md) "

Example 4-13 CONTINUE Statement in Basic LOOP Statement

```
DECLARE
  x NUMBER := 0;
BEGIN
  LOOP -- After CONTINUE statement, control resumes here
    DBMS_OUTPUT.PUT_LINE ('Inside loop:  x = ' || TO_CHAR(x));
    x := x + 1;
    IF x < 3 THEN
      CONTINUE;
    END IF;
    DBMS_OUTPUT.PUT_LINE
      ('Inside loop, after CONTINUE:  x = ' || TO_CHAR(x));
    EXIT WHEN x = 5;
  END LOOP;
 
  DBMS_OUTPUT.PUT_LINE (' After loop:  x = ' || TO_CHAR(x));
END;
/
```

Result:

```
Inside loop:  x = 0
Inside loop:  x = 1
Inside loop:  x = 2
Inside loop, after CONTINUE:  x = 3
Inside loop:  x = 3
Inside loop, after CONTINUE:  x = 4
Inside loop:  x = 4
Inside loop, after CONTINUE:  x = 5
After loop:  x = 5
```

### CONTINUE WHEN Statement

The `CONTINUE` `WHEN` statement exits the current iteration of a loop when the condition in its `WHEN` clause is true, and transfers control to the next iteration of either the current loop or an enclosing labeled loop.

Each time control reaches the `CONTINUE` `WHEN` statement, the condition in its `WHEN` clause is evaluated. If the condition is not true, the `CONTINUE` `WHEN` statement does nothing.

In Example 4-14, the `CONTINUE` `WHEN` statement inside the basic `LOOP` statement transfers control to the next iteration of the current loop when `x` is less than 3. Example 4-14 is logically equivalent to Example 4-13.

See Also:

" [CONTINUE Statement](CONTINUE-statement.md) "

Example 4-14 CONTINUE WHEN Statement in Basic LOOP Statement

```
DECLARE
  x NUMBER := 0;
BEGIN
  LOOP -- After CONTINUE statement, control resumes here
    DBMS_OUTPUT.PUT_LINE ('Inside loop:  x = ' || TO_CHAR(x));
    x := x + 1;
    CONTINUE WHEN x < 3;
    DBMS_OUTPUT.PUT_LINE
      ('Inside loop, after CONTINUE:  x = ' || TO_CHAR(x));
    EXIT WHEN x = 5;
  END LOOP;
  DBMS_OUTPUT.PUT_LINE (' After loop:  x = ' || TO_CHAR(x));
END;
/
```

Result:

```
Inside loop:  x = 0
Inside loop:  x = 1
Inside loop:  x = 2
Inside loop, after CONTINUE:  x = 3
Inside loop:  x = 3
Inside loop, after CONTINUE:  x = 4
Inside loop:  x = 4
Inside loop, after CONTINUE:  x = 5
After loop:  x = 5
```

### FOR LOOP Statement

The `FOR` `LOOP` statement runs one or more statements while the loop index is in a specified range. The statement has this structure:

```
[ label ] FOR index IN [ REVERSE ] lower_bound..upper_bound LOOP
  statements
END LOOP [ label ];
```

Without `REVERSE`, the value of `index` starts at `lower_bound` and increases by one with each iteration of the loop until it reaches `upper_bound`. If `lower_bound` is greater than `upper_bound`, then the `statements` never run.

With `REVERSE`, the value of `index` starts at `upper_bound` and decreases by one with each iteration of the loop until it reaches `lower_bound`. If `upper_bound` is less than `lower_bound`, then the `statements` never run.

An `EXIT`, `EXIT` `WHEN`, `CONTINUE`, or `CONTINUE` `WHEN` in the `statements` can cause the loop or the current iteration of the loop to end early.

Tip:

To process the rows of a query result set, use a cursor `FOR` `LOOP`, which has a query instead of a range of integers. For details, see " [Processing Query Result Sets With Cursor FOR LOOP Statements](processing-query-result-sets.md) ".

See Also:

" [FOR LOOP Statement](FOR-LOOP-statement.md) "

In Example 4-15, `index` is `i`, `lower_bound` is 1, and `upper_bound` is 3. The loop prints the numbers from 1 to 3.

The `FOR` `LOOP` statement in Example 4-16 is the reverse of the one in Example 4-15: It prints the numbers from 3 to 1.

In some languages, the `FOR` `LOOP` has a `STEP` clause that lets you specify a loop index increment other than 1. To simulate the `STEP` clause in PL/SQL, multiply each reference to the loop index by the desired increment.

In Example 4-17, the `FOR` `LOOP` effectively increments the index by five.

Topics

- FOR LOOP Index
- Lower Bound and Upper Bound
- EXIT WHEN or CONTINUE WHEN Statement in FOR LOOP Statement

Example 4-15 FOR LOOP Statements

```
BEGIN
  DBMS_OUTPUT.PUT_LINE ('lower_bound < upper_bound');
 
  FOR i IN 1..3 LOOP
    DBMS_OUTPUT.PUT_LINE (i);
  END LOOP;
 
  DBMS_OUTPUT.PUT_LINE ('lower_bound = upper_bound');
 
  FOR i IN 2..2 LOOP
    DBMS_OUTPUT.PUT_LINE (i);
  END LOOP;
 
  DBMS_OUTPUT.PUT_LINE ('lower_bound > upper_bound');
 
  FOR i IN 3..1 LOOP
    DBMS_OUTPUT.PUT_LINE (i);
  END LOOP;
END;
/
```

Result:

```
lower_bound < upper_bound
1
2
3
lower_bound = upper_bound
2
lower_bound > upper_bound
```

Example 4-16 Reverse FOR LOOP Statements

```
BEGIN
  DBMS_OUTPUT.PUT_LINE ('upper_bound > lower_bound');
 
  FOR i IN REVERSE 1..3 LOOP
    DBMS_OUTPUT.PUT_LINE (i);
  END LOOP;
 
  DBMS_OUTPUT.PUT_LINE ('upper_bound = lower_bound');
 
  FOR i IN REVERSE 2..2 LOOP
    DBMS_OUTPUT.PUT_LINE (i);
  END LOOP;
 
  DBMS_OUTPUT.PUT_LINE ('upper_bound < lower_bound');
 
  FOR i IN REVERSE 3..1 LOOP
    DBMS_OUTPUT.PUT_LINE (i);
  END LOOP;
END;
/
```

Result:

```
upper_bound > lower_bound
3
2
1
upper_bound = lower_bound
2
upper_bound < lower_bound
```

Example 4-17 Simulating STEP Clause in FOR LOOP Statement

```
DECLARE
  step  PLS_INTEGER := 5;
BEGIN
  FOR i IN 1..3 LOOP
    DBMS_OUTPUT.PUT_LINE (i*step);
  END LOOP;
END;
/
```

Result:

```
5
10
15
```

#### FOR LOOP Index

The index of a `FOR` `LOOP` statement is implicitly declared as a variable of type `PLS_INTEGER` that is local to the loop. The statements in the loop can read the value of the index, but cannot change it. Statements outside the loop cannot reference the index. After the `FOR` `LOOP` statement runs, the index is undefined. (A loop index is sometimes called a loop counter.)

In Example 4-18, the `FOR` `LOOP` statement tries to change the value of its index, causing an error.

In Example 4-19, a statement outside the `FOR` `LOOP` statement references the loop index, causing an error.

If the index of a `FOR` `LOOP` statement has the same name as a variable declared in an enclosing block, the local implicit declaration hides the other declaration, as Example 4-20 shows.

Example 4-21 shows how to change Example 4-20 to allow the statement inside the loop to reference the variable declared in the enclosing block.

In Example 4-22, the indexes of the nested `FOR` `LOOP` statements have the same name. The inner loop references the index of the outer loop by qualifying the reference with the label of the outer loop. For clarity only, the inner loop also qualifies the reference to its own index with its own label.

Example 4-18 FOR LOOP Statement Tries to Change Index Value

```
BEGIN
  FOR i IN 1..3 LOOP
    IF i < 3 THEN
      DBMS_OUTPUT.PUT_LINE (TO_CHAR(i));
    ELSE
      i := 2;
    END IF;
  END LOOP;
END;
/
```

Result:

```
i := 2;
       *
ERROR at line 6:
ORA-06550: line 6, column 8:
PLS-00363: expression 'I' cannot be used as an assignment target
ORA-06550: line 6, column 8:
PL/SQL: Statement ignored
```

Example 4-19 Outside Statement References FOR LOOP Statement Index

```
BEGIN
  FOR i IN 1..3 LOOP
    DBMS_OUTPUT.PUT_LINE ('Inside loop, i is ' || TO_CHAR(i));
  END LOOP;
  
  DBMS_OUTPUT.PUT_LINE ('Outside loop, i is ' || TO_CHAR(i));
END;
/
```

Result:

```
DBMS_OUTPUT.PUT_LINE ('Outside loop, i is ' || TO_CHAR(i));
                                                         *
ERROR at line 6:
ORA-06550: line 6, column 58:
PLS-00201: identifier 'I' must be declared
ORA-06550: line 6, column 3:
PL/SQL: Statement ignored
```

Example 4-20 FOR LOOP Statement Index with Same Name as Variable

```
DECLARE
  i NUMBER := 5;
BEGIN
  FOR i IN 1..3 LOOP
    DBMS_OUTPUT.PUT_LINE ('Inside loop, i is ' || TO_CHAR(i));
  END LOOP;
  
  DBMS_OUTPUT.PUT_LINE ('Outside loop, i is ' || TO_CHAR(i));
END;
/
```

Result:

```
Inside loop, i is 1
Inside loop, i is 2
Inside loop, i is 3
Outside loop, i is 5
```

Example 4-21 FOR LOOP Statement References Variable with Same Name as Index

```
<<main>>  -- Label block.
DECLARE
  i NUMBER := 5;
BEGIN
  FOR i IN 1..3 LOOP
    DBMS_OUTPUT.PUT_LINE (
      'local: ' || TO_CHAR(i) || ', global: ' ||
      TO_CHAR(main.i)  -- Qualify reference with block label.
    );
  END LOOP;
END main;
/
```

Result:

```
local: 1, global: 5
local: 2, global: 5
local: 3, global: 5
```

Example 4-22 Nested FOR LOOP Statements with Same Index Name

```
BEGIN
  <<outer_loop>>
  FOR i IN 1..3 LOOP
    <<inner_loop>>
    FOR i IN 1..3 LOOP
      IF outer_loop.i = 2 THEN
        DBMS_OUTPUT.PUT_LINE
          ('outer: ' || TO_CHAR(outer_loop.i) || ' inner: '
           || TO_CHAR(inner_loop.i));
      END IF;
    END LOOP inner_loop;
  END LOOP outer_loop;
END;
/
```

Result:

```
outer: 2 inner: 1
outer: 2 inner: 2
outer: 2 inner: 3
```

#### Lower Bound and Upper Bound

The lower and upper bounds of a `FOR` `LOOP` statement can be either numeric literals, numeric variables, or numeric expressions. If a bound does not have a numeric value, then PL/SQL raises the predefined exception `VALUE_ERROR`.

In Example 4-24, the upper bound of the `FOR` `LOOP` statement is a variable whose value is determined at run time.

Example 4-23 FOR LOOP Statement Bounds

```
DECLARE
  first  INTEGER := 1;
  last   INTEGER := 10;
  high   INTEGER := 100;
  low    INTEGER := 12;
BEGIN
  -- Bounds are numeric literals:
  FOR j IN -5..5 LOOP
    NULL;
  END LOOP;
 
  -- Bounds are numeric variables:
  FOR k IN REVERSE first..last LOOP
    NULL;
  END LOOP;
 
 -- Lower bound is numeric literal,
 -- Upper bound is numeric expression:
  FOR step IN 0..(TRUNC(high/low) * 2) LOOP
    NULL;
  END LOOP;
END;
/
```

Example 4-24 Specifying FOR LOOP Statement Bounds at Run Time

```
DROP TABLE temp;
CREATE TABLE temp (
  emp_no      NUMBER,
  email_addr  VARCHAR2(50)
);
 
DECLARE
  emp_count  NUMBER;
BEGIN
  SELECT COUNT(employee_id) INTO emp_count
  FROM employees;
  
  FOR i IN 1..emp_count LOOP
    INSERT INTO temp (emp_no, email_addr)
    VALUES(i, 'to be added later');
  END LOOP;
END;
/
```

#### EXIT WHEN or CONTINUE WHEN Statement in FOR LOOP Statement

Suppose that you must exit a `FOR` `LOOP` statement immediately if a certain condition arises. You can put the condition in an `EXIT` `WHEN` statement inside the `FOR` `LOOP` statement.

In Example 4-25, the `FOR` `LOOP` statement executes 10 times unless the `FETCH` statement inside it fails to return a row, in which case it ends immediately.

Now suppose that the `FOR` `LOOP` statement that you must exit early is nested inside another `FOR` `LOOP` statement. If, when you exit the inner loop early, you also want to exit the outer loop, then label the outer loop and specify its name in the `EXIT` `WHEN` statement, as in Example 4-26.

If you want to exit the inner loop early but complete the current iteration of the outer loop, then label the outer loop and specify its name in the `CONTINUE` `WHEN` statement, as in Example 4-27.

See Also:

" [Overview of Exception Handling](overview-exception-handling.md) " for information about exceptions, which can also cause a loop to end immediately if a certain condition arises

Example 4-25 EXIT WHEN Statement in FOR LOOP Statement

```
DECLARE
  v_employees employees%ROWTYPE;
  CURSOR c1 is SELECT * FROM employees;
BEGIN
  OPEN c1;
  -- Fetch entire row into v_employees record:
  FOR i IN 1..10 LOOP
    FETCH c1 INTO v_employees;
    EXIT WHEN c1%NOTFOUND;
    -- Process data here
  END LOOP;
  CLOSE c1;
END;
/
```

Example 4-26 EXIT WHEN Statement in Inner FOR LOOP Statement

```
DECLARE
  v_employees employees%ROWTYPE;
  CURSOR c1 is SELECT * FROM employees;
BEGIN
  OPEN c1;
  
  -- Fetch entire row into v_employees record:
  <<outer_loop>>
  FOR i IN 1..10 LOOP
    -- Process data here
    FOR j IN 1..10 LOOP
      FETCH c1 INTO v_employees;
      EXIT outer_loop WHEN c1%NOTFOUND;
      -- Process data here
    END LOOP;
  END LOOP outer_loop;
 
  CLOSE c1;
END;
/
```

Example 4-27 CONTINUE WHEN Statement in Inner FOR LOOP Statement

```
DECLARE
  v_employees employees%ROWTYPE;
  CURSOR c1 is SELECT * FROM employees;
BEGIN
  OPEN c1;
  
  -- Fetch entire row into v_employees record:
  <<outer_loop>>
  FOR i IN 1..10 LOOP
    -- Process data here
    FOR j IN 1..10 LOOP
      FETCH c1 INTO v_employees;
      CONTINUE outer_loop WHEN c1%NOTFOUND;
      -- Process data here
    END LOOP;
  END LOOP outer_loop;
 
  CLOSE c1;
END;
/
```

### WHILE LOOP Statement

The `WHILE` `LOOP` statement runs one or more statements while a condition is true. It has this structure:

```
[ label ] WHILE condition LOOP
  statements
END LOOP [ label ];
```

If the `condition` is true, the `statements` run and control returns to the top of the loop, where `condition` is evaluated again. If the `condition` is not true, control transfers to the statement after the `WHILE` `LOOP` statement. To prevent an infinite loop, a statement inside the loop must make the condition false or null. For complete syntax, see " [WHILE LOOP Statement](WHILE-LOOP-statement.md) ".

An `EXIT`, `EXIT` `WHEN`, `CONTINUE`, or `CONTINUE` `WHEN` in the `statements` can cause the loop or the current iteration of the loop to end early.

Some languages have a `LOOP` `UNTIL` or `REPEAT` `UNTIL` structure, which tests a condition at the bottom of the loop instead of at the top, so that the statements run at least once. To simulate this structure in PL/SQL, use a basic `LOOP` statement with an `EXIT` `WHEN` statement:

```
LOOP
  statements
  EXIT WHEN condition;
END LOOP;
```

In Example 4-28, the statements in the first `WHILE` `LOOP` statement never run, and the statements in the second `WHILE` `LOOP` statement run once.

Example 4-28 WHILE LOOP Statements

```
DECLARE
  done  BOOLEAN := FALSE;
BEGIN
  WHILE done LOOP
    DBMS_OUTPUT.PUT_LINE ('This line does not print.');
    done := TRUE;  -- This assignment is not made.
  END LOOP;

  WHILE NOT done LOOP
    DBMS_OUTPUT.PUT_LINE ('Hello, world!');
    done := TRUE;
  END LOOP;
END;
/
```

Result:

```
Hello, world!
```