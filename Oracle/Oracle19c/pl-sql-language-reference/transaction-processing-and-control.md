---
title: Database PL/SQL Language Reference
book: Database PL/SQL Language Reference
doc_id: E96448-09
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/transaction-processing-and-control.html
tags:
  - oracle
  - 19c
  - pl-sql-language-reference
---

## Transaction Processing and Control

Transaction processing is an Oracle Database feature that lets multiple users work on the database concurrently, and ensures that each user sees a consistent version of data and that all changes are applied in the right order.

A transaction is a sequence of one or more SQL statements that Oracle Database treats as a unit: either all of the statements are performed, or none of them are.

Different users can write to the same data structures without harming each other's data or coordinating with each other, because Oracle Database locks data structures automatically. To maximize data availability, Oracle Database locks the minimum amount of data for the minimum amount of time.

You rarely must write extra code to prevent problems with multiple users accessing data concurrently. However, if you do need this level of control, you can manually override the Oracle Database default locking mechanisms.

Topics

See Also:

- [Oracle Database Concepts](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=CNCPT016) for more information about transactions
- [Oracle Database Concepts](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=CNCPT1118) for more information about transaction processing
- [Oracle Database Concepts](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=CNCPT1331) for more information about the Oracle Database locking mechanism
- [Oracle Database Concepts](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=CNCPT1363) for more information about manual data locks

### COMMIT Statement

The `COMMIT` statement ends the current transaction, making its changes permanent and visible to other users.

Note:

A transaction can span multiple blocks, and a block can contain multiple transactions.

The `WRITE` clause of the `COMMIT` statement specifies the priority with which Oracle Database writes to the redo log the information that the commit operation generates.

Note:

The default PL/SQL commit behavior for nondistributed transactions is `BATCH` `NOWAIT` if the `COMMIT_LOGGING` and `COMMIT_WAIT` database initialization parameters have not been set.

See Also:

- [Oracle Database Concepts](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=CNCPT1119) for more information about committing transactions
- [Oracle Database Concepts](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=CNCPT016) for information about distributed transactions
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=SQLRF01110) for information about the `COMMIT` statement
- [Oracle Data Guard Concepts and Administration](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=SBYDB02000) for information about ensuring no loss of data during a failover to a standby database

Example 6-36 COMMIT Statement with COMMENT and WRITE Clauses

In this example, a transaction transfers money from one bank account to another. It is important that the money both leaves one account and enters the other, hence the `COMMIT` `WRITE` `IMMEDIATE` `NOWAIT` statement.

```
DROP TABLE accounts;
CREATE TABLE accounts (
  account_id  NUMBER(6),
  balance     NUMBER (10,2)
);
 
INSERT INTO accounts (account_id, balance)
VALUES (7715, 6350.00);
 
INSERT INTO accounts (account_id, balance)
VALUES (7720, 5100.50);
 
CREATE OR REPLACE PROCEDURE transfer (
  from_acct  NUMBER,
  to_acct    NUMBER,
  amount     NUMBER
) AUTHID CURRENT_USER AS
BEGIN
  UPDATE accounts
  SET balance = balance - amount
  WHERE account_id = from_acct;
 
  UPDATE accounts
  SET balance = balance + amount
  WHERE account_id = to_acct;
 
  COMMIT WRITE IMMEDIATE NOWAIT;
END;
/
```

Query before transfer:

```
SELECT * FROM accounts;
```

Result:

```
ACCOUNT_ID    BALANCE
---------- ----------
      7715       6350
      7720     5100.5
 
BEGIN
  transfer(7715, 7720, 250);
END;
/
```

Query after transfer:

```
SELECT * FROM accounts;
```

Result:

```
ACCOUNT_ID    BALANCE
---------- ----------
      7715       6100
      7720     5350.5
```

### ROLLBACK Statement

The `ROLLBACK` statement ends the current transaction and undoes any changes made during that transaction.

If you make a mistake, such as deleting the wrong row from a table, a rollback restores the original data. If you cannot finish a transaction because a SQL statement fails or PL/SQL raises an exception, a rollback lets you take corrective action and perhaps start over.

See Also:

[Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=SQLRF01601) for more information about the `ROLLBACK` statement

Example 6-37 ROLLBACK Statement

This example inserts information about an employee into three different tables. If an `INSERT` statement tries to store a duplicate employee number, PL/SQL raises the predefined exception `DUP_VAL_ON_INDEX`. To ensure that changes to all three tables are undone, the exception handler runs a `ROLLBACK`.

```
DROP TABLE emp_name;
CREATE TABLE emp_name AS 
  SELECT employee_id, last_name
  FROM employees;
 
CREATE UNIQUE INDEX empname_ix
ON emp_name (employee_id);
 
 
DROP TABLE emp_sal;
CREATE TABLE emp_sal AS
  SELECT employee_id, salary
  FROM employees;
 
CREATE UNIQUE INDEX empsal_ix
ON emp_sal (employee_id);
 
 
DROP TABLE emp_job;
CREATE TABLE emp_job AS
  SELECT employee_id, job_id
  FROM employees;
 
CREATE UNIQUE INDEX empjobid_ix
ON emp_job (employee_id);
 
 
DECLARE
  emp_id        NUMBER(6);
  emp_lastname  VARCHAR2(25);
  emp_salary    NUMBER(8,2);
  emp_jobid     VARCHAR2(10);
BEGIN
  SELECT employee_id, last_name, salary, job_id
  INTO emp_id, emp_lastname, emp_salary, emp_jobid
  FROM employees
  WHERE employee_id = 120;
 
  INSERT INTO emp_name (employee_id, last_name)
  VALUES (emp_id, emp_lastname);
 
  INSERT INTO emp_sal (employee_id, salary) 
  VALUES (emp_id, emp_salary);
 
  INSERT INTO emp_job (employee_id, job_id)
  VALUES (emp_id, emp_jobid);
 
EXCEPTION
  WHEN DUP_VAL_ON_INDEX THEN
    ROLLBACK;
    DBMS_OUTPUT.PUT_LINE('Inserts were rolled back');
END;
/
```

### SAVEPOINT Statement

The `SAVEPOINT` statement names and marks the current point in the processing of a transaction.

Savepoints let you roll back part of a transaction instead of the whole transaction. The number of active savepoints for each session is unlimited.

When you roll back to a savepoint, any savepoints marked after that savepoint are erased. The savepoint to which you roll back is not erased. A simple rollback or commit erases all savepoints.

If you mark a savepoint in a recursive subprogram, new instances of the `SAVEPOINT` statement run at each level in the recursive descent, but you can only roll back to the most recently marked savepoint.

Savepoint names are undeclared identifiers. Reusing a savepoint name in a transaction moves the savepoint from its old position to the current point in the transaction, which means that a rollback to the savepoint affects only the current part of the transaction.

See Also:

[Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=SQLRF01705) for more information about the `SET` `TRANSACTION` SQL statement

Example 6-38 SAVEPOINT and ROLLBACK Statements

This example marks a savepoint before doing an insert. If the `INSERT` statement tries to store a duplicate value in the `employee_id` column, PL/SQL raises the predefined exception `DUP_VAL_ON_INDEX` and the transaction rolls back to the savepoint, undoing only the `INSERT` statement.

```
DROP TABLE emp_name;
CREATE TABLE emp_name AS
  SELECT employee_id, last_name, salary
  FROM employees;
 
CREATE UNIQUE INDEX empname_ix
ON emp_name (employee_id);
 
DECLARE
  emp_id        employees.employee_id%TYPE;
  emp_lastname  employees.last_name%TYPE;
  emp_salary    employees.salary%TYPE;
 
BEGIN
  SELECT employee_id, last_name, salary
  INTO emp_id, emp_lastname, emp_salary 
  FROM employees
  WHERE employee_id = 120;
 
  UPDATE emp_name
  SET salary = salary * 1.1
  WHERE employee_id = emp_id;
 
  DELETE FROM emp_name
  WHERE employee_id = 130;
 
  SAVEPOINT do_insert;
 
  INSERT INTO emp_name (employee_id, last_name, salary)
  VALUES (emp_id, emp_lastname, emp_salary);
 
EXCEPTION
  WHEN DUP_VAL_ON_INDEX THEN
    ROLLBACK TO do_insert;
  DBMS_OUTPUT.PUT_LINE('Insert was rolled back');
END;
/
```

Example 6-39 Reusing SAVEPOINT with ROLLBACK

```
DROP TABLE emp_name;
CREATE TABLE emp_name AS
  SELECT employee_id, last_name, salary
  FROM employees;
 
CREATE UNIQUE INDEX empname_ix
ON emp_name (employee_id);
 
DECLARE
  emp_id        employees.employee_id%TYPE;
  emp_lastname  employees.last_name%TYPE;
  emp_salary    employees.salary%TYPE;
 
BEGIN
  SELECT employee_id, last_name, salary
  INTO emp_id, emp_lastname, emp_salary
  FROM employees
  WHERE employee_id = 120;
 
  SAVEPOINT my_savepoint;
 
  UPDATE emp_name
  SET salary = salary * 1.1
  WHERE employee_id = emp_id;
 
  DELETE FROM emp_name
  WHERE employee_id = 130;
 
  SAVEPOINT my_savepoint;
 
  INSERT INTO emp_name (employee_id, last_name, salary)
  VALUES (emp_id, emp_lastname, emp_salary);
 
EXCEPTION
  WHEN DUP_VAL_ON_INDEX THEN
    ROLLBACK TO my_savepoint;
    DBMS_OUTPUT.PUT_LINE('Transaction rolled back.');
END;
/
```

### Implicit Rollbacks

Before running an `INSERT`, `UPDATE`, `DELETE`, or `MERGE` statement, the database marks an implicit savepoint (unavailable to you). If the statement fails, the database rolls back to the savepoint.

Usually, just the failed SQL statement is rolled back, not the whole transaction. If the statement raises an unhandled exception, the host environment determines what is rolled back.

The database can also roll back single SQL statements to break deadlocks. The database signals an error to a participating transaction and rolls back the current statement in that transaction.

Before running a SQL statement, the database must parse it, that is, examine it to ensure it follows syntax rules and refers to valid schema objects. Errors detected while running a SQL statement cause a rollback, but errors detected while parsing the statement do not.

If you exit a stored subprogram with an unhandled exception, PL/SQL does not assign values to `OUT` parameters, and does not do any rollback.

For information about handling exceptions, see [PL/SQL Error Handling](plsql-error-handling.md)

### SET TRANSACTION Statement

You use the `SET` `TRANSACTION` statement to begin a read-only or read-write transaction, establish an isolation level, or assign your current transaction to a specified rollback segment.

Read-only transactions are useful for running multiple queries while other users update the same tables.

During a read-only transaction, all queries refer to the same snapshot of the database, providing a multi-table, multi-query, read-consistent view. Other users can continue to query or update data as usual. A commit or rollback ends the transaction.

The `SET` `TRANSACTION` statement must be the first SQL statement in a read-only transaction and can appear only once in a transaction. If you set a transaction to `READ` `ONLY`, subsequent queries see only changes committed before the transaction began. The use of `READ` `ONLY` does not affect other users or transactions.

Only the `SELECT`, `OPEN`, `FETCH`, `CLOSE`, `LOCK` `TABLE`, `COMMIT`, and `ROLLBACK` statements are allowed in a read-only transaction. Queries cannot be `FOR` `UPDATE`.

See Also:

[Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=SQLRF01705) for more information about the SQL statement `SET` `TRANSACTION`

Example 6-40 SET TRANSACTION Statement in Read-Only Transaction

In this example, a read-only transaction gather order totals for the day, the past week, and the past month. The totals are unaffected by other users updating the database during the transaction. The `orders` table is in the sample schema OE.

```
DECLARE
  daily_order_total    NUMBER(12,2);
  weekly_order_total   NUMBER(12,2); 
  monthly_order_total  NUMBER(12,2);
BEGIN
   COMMIT; -- end previous transaction
   SET TRANSACTION READ ONLY NAME 'Calculate Order Totals';

   SELECT SUM (order_total)
   INTO daily_order_total
   FROM orders
   WHERE order_date = SYSDATE;

   SELECT SUM (order_total)
   INTO weekly_order_total
   FROM orders
   WHERE order_date = SYSDATE - 7;

   SELECT SUM (order_total)
   INTO monthly_order_total
   FROM orders
   WHERE order_date = SYSDATE - 30;

   COMMIT; -- ends read-only transaction
END;
/
```

### Overriding Default Locking

By default, Oracle Database locks data structures automatically, which lets different applications write to the same data structures without harming each other's data or coordinating with each other.

If you must have exclusive access to data during a transaction, you can override default locking with these SQL statements:

- `LOCK` `TABLE`, which explicitly locks entire tables.
- `SELECT` with the `FOR` `UPDATE` clause (`SELECT` `FOR` `UPDATE`), which explicitly locks specific rows of a table.

Topics

- LOCK TABLE Statement
- SELECT FOR UPDATE and FOR UPDATE Cursors
- Simulating CURRENT OF Clause with ROWID Pseudocolumn

#### LOCK TABLE Statement

The `LOCK` `TABLE` statement explicitly locks one or more tables in a specified lock mode so that you can share or deny access to them.

The lock mode determines what other locks can be placed on the table. For example, many users can acquire row share locks on a table at the same time, but only one user at a time can acquire an exclusive lock. While one user has an exclusive lock on a table, no other users can insert, delete, or update rows in that table.

A table lock never prevents other users from querying a table, and a query never acquires a table lock. Only if two different transactions try to modify the same row does one transaction wait for the other to complete. The `LOCK` `TABLE` statement lets you specify how long to wait for another transaction to complete.

Table locks are released when the transaction that acquired them is either committed or rolled back.

See Also:

- [Oracle Database Development Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=ADFNS00203) for more information about locking tables explicitly
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=SQLRF01605) for more information about the `LOCK` `TABLE` statement

#### SELECT FOR UPDATE and FOR UPDATE Cursors

The `SELECT` statement with the `FOR` `UPDATE` clause (`SELECT` `FOR` `UPDATE` statement) selects the rows of the result set and locks them. `SELECT` `FOR` `UPDATE` lets you base an update on the existing values in the rows, because it ensures that no other user can change those values before you update them. You can also use `SELECT` `FOR` `UPDATE` to lock rows that you do not want to update, as in [Example 9-6](dml-triggers.md).

Note:

In tables compressed with Hybrid Columnar Compression (HCC), DML statements lock compression units rather than rows. HCC, a feature of certain Oracle storage systems, is described in [Oracle Database Concepts](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=CNCPT89198).

By default, the `SELECT` `FOR` `UPDATE` statement waits until the requested row lock is acquired. To change this behavior, use the `NOWAIT`, `WAIT`, or `SKIP` `LOCKED` clause of the `SELECT` `FOR` `UPDATE` statement. For information about these clauses, see [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=SQLRF01702).

When `SELECT` `FOR` `UPDATE` is associated with an explicit cursor, the cursor is called a `FOR` `UPDATE` cursor. Only a `FOR` `UPDATE` cursor can appear in the `CURRENT` `OF` clause of an `UPDATE` or `DELETE` statement. (The `CURRENT` `OF` clause, a PL/SQL extension to the `WHERE` clause of the SQL statements `UPDATE` and `DELETE`, restricts the statement to the current row of the cursor.)

When `SELECT` `FOR` `UPDATE` queries multiple tables, it locks only rows whose columns appear in the `FOR` `UPDATE` clause.

#### Simulating CURRENT OF Clause with ROWID Pseudocolumn

The rows of the result set are locked when you open a `FOR` `UPDATE` cursor, not as they are fetched, that is, unless the `SKIP` `LOCKED` clause is specified by the `FOR` `UPDATE` cursor, in which case the rows are locked during the `FETCH` phase of the cursor. The rows are unlocked when you commit or roll back the transaction. After the rows are unlocked, you cannot fetch from the `FOR` `UPDATE` cursor, as Example 6-41 shows (the result is the same if you substitute `ROLLBACK` for `COMMIT`).

The workaround is to simulate the `CURRENT` `OF` clause with the `ROWID` pseudocolumn (described in [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=SQLRF00254)). Select the rowid of each row into a `UROWID` variable and use the rowid to identify the current row during subsequent updates and deletes, as in Example 6-42. (To print the value of a `UROWID` variable, convert it to `VARCHAR2`, using the `ROWIDTOCHAR` function described in [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=SQLRF06101).)

Note:

When you update a row in a table compressed with Hybrid Columnar Compression (HCC), the `ROWID` of the row changes. HCC, a feature of certain Oracle storage systems, is described in [Oracle Database Concepts](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=CNCPT89198).

Caution:

Because no `FOR` `UPDATE` clause locks the fetched rows, other users might unintentionally overwrite your changes.

Note:

The extra space needed for read consistency is not released until the cursor is closed, which can slow down processing for large updates.

Example 6-41 FETCH with FOR UPDATE Cursor After COMMIT Statement

```
DROP TABLE emp;
CREATE TABLE emp AS SELECT * FROM employees;
 
DECLARE
  CURSOR c1 IS
    SELECT * FROM emp
    FOR UPDATE OF salary
    ORDER BY employee_id;
 
  emp_rec  emp%ROWTYPE;
BEGIN
  OPEN c1;
  LOOP
    FETCH c1 INTO emp_rec;  -- fails on second iteration
    EXIT WHEN c1%NOTFOUND;
    DBMS_OUTPUT.PUT_LINE (
      'emp_rec.employee_id = ' ||
      TO_CHAR(emp_rec.employee_id)
    );
    
    UPDATE emp
    SET salary = salary * 1.05
    WHERE employee_id = 105;
 
    COMMIT;  -- releases locks
  END LOOP;
END;
/
```

Result:

```
emp_rec.employee_id = 100
DECLARE
*
ERROR at line 1:
ORA-01002: fetch out of sequence
ORA-06512: at line 11
```

Example 6-42 Simulating CURRENT OF Clause with ROWID Pseudocolumn

```
DROP TABLE emp;
CREATE TABLE emp AS SELECT * FROM employees;
 
DECLARE
  CURSOR c1 IS
    SELECT last_name, job_id, rowid
    FROM emp;  -- no FOR UPDATE clause
 
  my_lastname   employees.last_name%TYPE;
  my_jobid      employees.job_id%TYPE;
  my_rowid      UROWID;
BEGIN
  OPEN c1;
  LOOP
    FETCH c1 INTO my_lastname, my_jobid, my_rowid;
    EXIT WHEN c1%NOTFOUND;
 
    UPDATE emp
    SET salary = salary * 1.02
    WHERE rowid = my_rowid;  -- simulates WHERE CURRENT OF c1
 
    COMMIT;
  END LOOP;
  CLOSE c1;
END;
/
```