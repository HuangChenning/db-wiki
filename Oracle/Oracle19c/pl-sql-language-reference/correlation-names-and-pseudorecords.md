---
title: Database PL/SQL Language Reference
book: Database PL/SQL Language Reference
doc_id: E96448-09
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/correlation-names-and-pseudorecords.html
tags:
  - oracle
  - 19c
  - pl-sql-language-reference
---

## Correlation Names and Pseudorecords

Note:

This topic applies only to triggers that fire at row level. That is:

- Row-level simple DML triggers
- Compound DML triggers with row-level timing point sections

A trigger that fires at row level can access the data in the row that it is processing by using correlation names. The default correlation names are `OLD`, `NEW`, and `PARENT`. To change the correlation names, use the `REFERENCING` clause of the `CREATE` `TRIGGER` statement (see " [referencing\_clause::=](CREATE-TRIGGER-statement.md) ").

If the trigger is created on a nested table, then `OLD` and `NEW` refer to the current row of the nested table, and `PARENT` refers to the current row of the parent table. If the trigger is created on a table or view, then `OLD` and `NEW` refer to the current row of the table or view, and `PARENT` is undefined.

`OLD`, `NEW`, and `PARENT` are also called pseudorecords, because they have record structure, but are allowed in fewer contexts than records are. The structure of a pseudorecord is `table_name` `%ROWTYPE`, where `table_name` is the name of the table on which the trigger is created (for `OLD` and `NEW`) or the name of the parent table (for `PARENT`).

In the `trigger_body` of a simple trigger or the `tps_body` of a compound trigger, a correlation name is a placeholder for a bind variable. Reference the field of a pseudorecord with this syntax:

```
:pseudorecord_name.field_name
```

In the `WHEN` clause of a conditional trigger, a correlation name is not a placeholder for a bind variable. Therefore, omit the colon in the preceding syntax.

Table 9-4 shows the values of `OLD` and `NEW` fields for the row that the triggering statement is processing.

Table 9-4 OLD and NEW Pseudorecord Field Values

| Triggering Statement | OLD.field Value | NEW.field Value |
| --- | --- | --- |
| `INSERT` | `NULL` | Post-insert value |
| `UPDATE` | Pre-update value | Post-update value |
| `DELETE` | Pre-delete value | `NULL` |

The restrictions on pseudorecords are:

- A pseudorecord cannot appear in a record-level operation.
	For example, the trigger cannot include this statement:
	```
	:NEW := NULL;
	```
- A pseudorecord cannot be an actual subprogram parameter.
	(A pseudorecord field can be an actual subprogram parameter.)
- The trigger cannot change `OLD` field values.
	Trying to do so raises ORA-04085.
- If the triggering statement is `DELETE`, then the trigger cannot change `NEW` field values.
	Trying to do so raises ORA-04084.
- An `AFTER` trigger cannot change `NEW` field values, because the triggering statement runs before the trigger fires.
	Trying to do so raises ORA-04084.

A `BEFORE` trigger can change `NEW` field values before a triggering `INSERT` or `UPDATE` statement puts them in the table.

If a statement triggers both a `BEFORE` trigger and an `AFTER` trigger, and the `BEFORE` trigger changes a `NEW` field value, then the `AFTER` trigger "sees" that change.

Example 9-14 Trigger Logs Changes to EMPLOYEES.SALARY

This example creates a log table and a trigger that inserts a row in the log table after any `UPDATE` statement affects the `SALARY` column of the `EMPLOYEES` table, and then updates `EMPLOYEES`.`SALARY` and shows the log table.

Create log table:

```
DROP TABLE Emp_log;
CREATE TABLE Emp_log (
  Emp_id     NUMBER,
  Log_date   DATE,
  New_salary NUMBER,
  Action     VARCHAR2(20));
```

Create trigger that inserts row in log table after `EMPLOYEES`.`SALARY` is updated:

```
CREATE OR REPLACE TRIGGER log_salary_increase
  AFTER UPDATE OF salary ON employees
  FOR EACH ROW
BEGIN
  INSERT INTO Emp_log (Emp_id, Log_date, New_salary, Action)
  VALUES (:NEW.employee_id, SYSDATE, :NEW.salary, 'New Salary');
END;
/
```

Update `EMPLOYEES`.`SALARY`:

```
UPDATE employees
SET salary = salary + 1000.0
WHERE Department_id = 20;
```

Result:

```
2 rows updated.
```

Show log table:

```
SELECT * FROM Emp_log;
```

Result:

```
EMP_ID LOG_DATE  NEW_SALARY ACTION
---------- --------- ---------- --------------------
       201 28-APR-10      13650 New Salary
       202 28-APR-10       6300 New Salary
 
2 rows selected.
```

Example 9-15 Conditional Trigger Prints Salary Change Information

This example creates a conditional trigger that prints salary change information whenever a `DELETE`, `INSERT`, or `UPDATE` statement affects the `EMPLOYEES` table—unless that information is about the President. The database evaluates the `WHEN` condition for each affected row. If the `WHEN` condition is `TRUE` for an affected row, then the trigger fires for that row before the triggering statement runs. If the `WHEN` condition is not `TRUE` for an affected row, then trigger does not fire for that row, but the triggering statement still runs.

```
CREATE OR REPLACE TRIGGER print_salary_changes
  BEFORE DELETE OR INSERT OR UPDATE ON employees
  FOR EACH ROW
  WHEN (NEW.job_id <> 'AD_PRES')  -- do not print information about President
DECLARE
  sal_diff  NUMBER;
BEGIN
  sal_diff  := :NEW.salary  - :OLD.salary;
  DBMS_OUTPUT.PUT(:NEW.last_name || ': ');
  DBMS_OUTPUT.PUT('Old salary = ' || :OLD.salary || ', ');
  DBMS_OUTPUT.PUT('New salary = ' || :NEW.salary || ', ');
  DBMS_OUTPUT.PUT_LINE('Difference: ' || sal_diff);
END;
/
```

Query:

```
SELECT last_name, department_id, salary, job_id
FROM employees
WHERE department_id IN (10, 20, 90)
ORDER BY department_id, last_name;
```

Result:

```
LAST_NAME                 DEPARTMENT_ID     SALARY JOB_ID
------------------------- ------------- ---------- ----------
Whalen                               10       4200 AD_ASST
Fay                                  20       6000 MK_REP
Hartstein                            20      13000 MK_MAN
De Haan                              90      17000 AD_VP
King                                 90      24000 AD_PRES
Kochhar                              90      17000 AD_VP
 
6 rows selected.
```

Triggering statement:

```
UPDATE employees
SET salary = salary * 1.05
WHERE department_id IN (10, 20, 90);
```

Result:

```
Whalen: Old salary = 4200, New salary = 4410, Difference: 210
Hartstein: Old salary = 13000, New salary = 13650, Difference: 650
Fay: Old salary = 6000, New salary = 6300, Difference: 300
Kochhar: Old salary = 17000, New salary = 17850, Difference: 850
De Haan: Old salary = 17000, New salary = 17850, Difference: 850
 
6 rows updated.
```

Query:

```
SELECT salary FROM employees WHERE job_id = 'AD_PRES';
```

Result:

```
SALARY
----------
     25200
 
1 row selected.
```

Example 9-16 Trigger Modifies CLOB Columns

This example creates an `UPDATE` trigger that modifies `CLOB` columns.

For information about `TO_CLOB` and other conversion functions, see [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=SQLRF20034).

```
DROP TABLE tab1;
CREATE TABLE tab1 (c1 CLOB);
INSERT INTO tab1 VALUES ('<h1>HTML Document Fragment</h1><p>Some text.', 3);

CREATE OR REPLACE TRIGGER trg1
  BEFORE UPDATE ON tab1
  FOR EACH ROW
BEGIN
  DBMS_OUTPUT.PUT_LINE('Old value of CLOB column: '||:OLD.c1);
  DBMS_OUTPUT.PUT_LINE('Proposed new value of CLOB column: '||:NEW.c1);

  :NEW.c1 := :NEW.c1 || TO_CLOB('<hr><p>Standard footer paragraph.');

  DBMS_OUTPUT.PUT_LINE('Final value of CLOB column: '||:NEW.c1);
END;
/ 

SET SERVEROUTPUT ON;
UPDATE tab1 SET c1 = '<h1>Different Document Fragment</h1><p>Different text.';

SELECT * FROM tab1;
```

Example 9-17 Trigger with REFERENCING Clause

This example creates a table with the same name as a correlation name, `new`, and then creates a trigger on that table. To avoid conflict between the table name and the correlation name, the trigger references the correlation name as `Newest`.

```
CREATE TABLE new (
  field1  NUMBER,
  field2  VARCHAR2(20)
);

CREATE OR REPLACE TRIGGER Print_salary_changes
BEFORE UPDATE ON new
REFERENCING new AS Newest
FOR EACH ROW
BEGIN
  :Newest.Field2 := TO_CHAR (:newest.field1);
END;
/
```

### OBJECT\_VALUE Pseudocolumn

A DML trigger on an object table can reference the SQL pseudocolumn `OBJECT_VALUE`, which returns system-generated names for the columns of the object table. The trigger can also invoke a PL/SQL subprogram that has a formal `IN` parameter whose data type is `OBJECT_VALUE`.

See Also:

- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=SQLRF50952) for more information about `OBJECT_VALUE`
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=SQLRF0025) for general information about pseudocolumns

Example 9-18 creates object table `tbl`, table `tbl_history` for logging updates to `tbl`, and trigger `Tbl_Trg`. The trigger runs for each row of `tb1` that is affected by a DML statement, causing the old and new values of the object `t` in `tbl` to be written in `tbl_history`. The old and new values are:`OLD`.`OBJECT_VALUE` and:`NEW`.`OBJECT_VALUE`.

All values of column `n` were increased by 1. The value of `m` remains 0.

Example 9-18 Trigger References OBJECT\_VALUE Pseudocolumn

Create, populate, and show object table:

```
CREATE OR REPLACE TYPE t AUTHID DEFINER AS OBJECT (n NUMBER, m NUMBER)
/
CREATE TABLE tbl OF t
/
BEGIN
  FOR j IN 1..5 LOOP
    INSERT INTO tbl VALUES (t(j, 0));
  END LOOP;
END;
/
SELECT * FROM tbl ORDER BY n;
```

Result:

```
N          M
---------- ----------
         1          0
         2          0
         3          0
         4          0
         5          0

5 rows selected.
```

Create history table and trigger:

```
CREATE TABLE tbl_history ( d DATE, old_obj t, new_obj t)
/
CREATE OR REPLACE TRIGGER Tbl_Trg
  AFTER UPDATE ON tbl
  FOR EACH ROW
BEGIN
  INSERT INTO tbl_history (d, old_obj, new_obj)
  VALUES (SYSDATE, :OLD.OBJECT_VALUE, :NEW.OBJECT_VALUE);
END Tbl_Trg;
/
```

Update object table:

```
UPDATE tbl SET tbl.n = tbl.n+1
/
```

Result:

```
5 rows updated.
```

Show old and new values:

```
BEGIN
  FOR j IN (SELECT d, old_obj, new_obj FROM tbl_history) LOOP
    DBMS_OUTPUT.PUT_LINE (
      j.d ||
      ' -- old: ' || j.old_obj.n || ' ' || j.old_obj.m ||
      ' -- new: ' || j.new_obj.n || ' ' || j.new_obj.m
    );
  END LOOP;
END;
/
```

Result:

```
28-APR-10 -- old: 1 0 -- new: 2 0
28-APR-10 -- old: 2 0 -- new: 3 0
28-APR-10 -- old: 3 0 -- new: 4 0
28-APR-10 -- old: 4 0 -- new: 5 0
28-APR-10 -- old: 5 0 -- new: 6 0
```