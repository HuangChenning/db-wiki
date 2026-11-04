---
title: Database PL/SQL Language Reference
book: Database PL/SQL Language Reference
doc_id: E96448-09
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/sequential-control-statements.html
tags:
  - oracle
  - 19c
  - pl-sql-language-reference
---

## Sequential Control Statements

Unlike the `IF` and `LOOP` statements, the sequential control statements `GOTO` and `NULL` are not crucial to PL/SQL programming.

The `GOTO` statement, which goes to a specified statement, is seldom needed. Occasionally, it simplifies logic enough to warrant its use.

The `NULL` statement, which does nothing, can improve readability by making the meaning and action of conditional statements clear.

Topics

- GOTO Statement
- NULL Statement

### GOTO Statement

The `GOTO` statement transfers control to a label unconditionally. The label must be unique in its scope and must precede an executable statement or a PL/SQL block. When run, the `GOTO` statement transfers control to the labeled statement or block. For `GOTO` statement restrictions, see " [GOTO Statement](GOTO-statement.md) ".

Use `GOTO` statements sparingly—overusing them results in code that is hard to understand and maintain. Do not use a `GOTO` statement to transfer control from a deeply nested structure to an exception handler. Instead, raise an exception. For information about the PL/SQL exception-handling mechanism, see [PL/SQL Error Handling](plsql-error-handling.md).

A label can appear only before a block (as in [Example 4-21](loop-statements.md)) or before a statement (as in Example 4-29), not in a statement, as in Example 4-30.

To correct Example 4-30, add a `NULL` statement, as in Example 4-31.

A `GOTO` statement can transfer control to an enclosing block from the current block, as in Example 4-32.

The `GOTO` statement transfers control to the first enclosing block in which the referenced label appears.

The `GOTO` statement in Example 4-33 transfers control into an `IF` statement, causing an error.

Example 4-29 GOTO Statement

```
DECLARE
  p  VARCHAR2(30);
  n  PLS_INTEGER := 37;
BEGIN
  FOR j in 2..ROUND(SQRT(n)) LOOP
    IF n MOD j = 0 THEN
      p := ' is not a prime number';
      GOTO print_now;
    END IF;
  END LOOP;

  p := ' is a prime number';
 
  <<print_now>>
  DBMS_OUTPUT.PUT_LINE(TO_CHAR(n) || p);
END;
/
```

Result:

```
37 is a prime number
```

Example 4-30 Incorrect Label Placement

```
DECLARE
  done  BOOLEAN;
BEGIN
  FOR i IN 1..50 LOOP
    IF done THEN
       GOTO end_loop;
    END IF;
    <<end_loop>>
  END LOOP;
END;
/
```

Result:

```
END LOOP;
  *
ERROR at line 9:
ORA-06550: line 9, column 3:
PLS-00103: Encountered the symbol "END" when expecting one of the following:
( begin case declare exit for goto if loop mod null raise
return select update while with <an identifier>
<a double-quoted delimited-identifier> <a bind variable> <<
continue close current delete fetch lock insert open rollback
savepoint set sql run commit forall merge pipe purge
```

Example 4-31 GOTO Statement Goes to Labeled NULL Statement

```
DECLARE
  done  BOOLEAN;
BEGIN
  FOR i IN 1..50 LOOP
    IF done THEN
      GOTO end_loop;
    END IF;
    <<end_loop>>
    NULL;
  END LOOP;
END;
/
```

Example 4-32 GOTO Statement Transfers Control to Enclosing Block

```
DECLARE
  v_last_name  VARCHAR2(25);
  v_emp_id     NUMBER(6) := 120;
BEGIN
  <<get_name>>
  SELECT last_name INTO v_last_name
  FROM employees
  WHERE employee_id = v_emp_id;
  
  BEGIN
    DBMS_OUTPUT.PUT_LINE (v_last_name);
    v_emp_id := v_emp_id + 5;
 
    IF v_emp_id < 120 THEN
      GOTO get_name;
    END IF;
  END;
END;
/
```

Result:

```
Weiss
```

Example 4-33 GOTO Statement Cannot Transfer Control into IF Statement

```
DECLARE
  valid BOOLEAN := TRUE;
BEGIN
  GOTO update_row;
  
  IF valid THEN
  <<update_row>>
    NULL;
  END IF;
END;
/
```

Result:

```
GOTO update_row;
  *
ERROR at line 4:
ORA-06550: line 4, column 3:
PLS-00375: illegal GOTO statement; this GOTO cannot transfer control to label
'UPDATE_ROW'
ORA-06550: line 6, column 12:
PL/SQL: Statement ignored
```

### NULL Statement

The `NULL` statement only passes control to the next statement. Some languages refer to such an instruction as a no-op (no operation).

Some uses for the `NULL` statement are:

- To provide a target for a `GOTO` statement, as in Example 4-31.
- To improve readability by making the meaning and action of conditional statements clear, as in Example 4-34
- To create placeholders and stub subprograms, as in Example 4-35
- To show that you are aware of a possibility, but that no action is necessary, as in Example 4-36

In Example 4-34, the `NULL` statement emphasizes that only salespersons receive commissions.

In Example 4-35, the `NULL` statement lets you compile this subprogram and fill in the real body later.

Note:

Using the `NULL` statement might raise an `unreachable` `code` warning if warnings are enabled. For information about warnings, see " [Compile-Time Warnings](compile-time-warnings.md) ".

In Example 4-36, the `NULL` statement shows that you have chosen to take no action for grades other than A, B, C, D, and F.

Example 4-34 NULL Statement Showing No Action

```
DECLARE
  v_job_id  VARCHAR2(10);
   v_emp_id  NUMBER(6) := 110;
BEGIN
  SELECT job_id INTO v_job_id
  FROM employees
  WHERE employee_id = v_emp_id;
  
  IF v_job_id = 'SA_REP' THEN
    UPDATE employees
    SET commission_pct = commission_pct * 1.2;
  ELSE
    NULL;  -- Employee is not a sales rep
  END IF;
END;
/
```

Example 4-35 NULL Statement as Placeholder During Subprogram Creation

```
CREATE OR REPLACE PROCEDURE award_bonus (
  emp_id NUMBER,
  bonus NUMBER
) AUTHID DEFINER AS
BEGIN    -- Executable part starts here
  NULL;  -- Placeholder
  -- (raises "unreachable code" if warnings enabled)
END award_bonus;
/
```

Example 4-36 NULL Statement in ELSE Clause of Simple CASE Statement

```
CREATE OR REPLACE PROCEDURE print_grade (
  grade CHAR
) AUTHID DEFINER AS
BEGIN
  CASE grade
    WHEN 'A' THEN DBMS_OUTPUT.PUT_LINE('Excellent');
    WHEN 'B' THEN DBMS_OUTPUT.PUT_LINE('Very Good');
    WHEN 'C' THEN DBMS_OUTPUT.PUT_LINE('Good');
    WHEN 'D' THEN DBMS_OUTPUT.PUT_LINE('Fair');
    WHEN 'F' THEN DBMS_OUTPUT.PUT_LINE('Poor');
    ELSE NULL;
  END CASE;
END;
/
BEGIN
  print_grade('A');
  print_grade('S');
END;
/
```

Result:

```
Excellent
```