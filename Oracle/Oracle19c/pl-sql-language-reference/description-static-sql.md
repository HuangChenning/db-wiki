---
title: Database PL/SQL Language Reference
book: Database PL/SQL Language Reference
doc_id: E96448-09
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/description-static-sql.html
tags:
  - oracle
  - 19c
  - pl-sql-language-reference
---

## Description of Static SQL

Static SQL has the same syntax as SQL, except as noted.

Topics

### Statements

These are the PL/SQL static SQL statements, which have the same syntax as the corresponding SQL statements, except as noted:

- `SELECT` (this statement is also called a query)
	For the PL/SQL syntax, see " [SELECT INTO Statement](SELECT-INTO-statement.md) ".
- Data manipulation language (DML) statements:
	- `INSERT`
		For the PL/SQL syntax, see " [INSERT Statement Extension](INSERT-statement-extension.md) ".
		- `UPDATE`
		For the PL/SQL syntax, see " [UPDATE Statement Extensions](UPDATE-statement-extensions.md) ".
		- `DELETE`
		For the PL/SQL syntax, see " [DELETE Statement Extension](DELETE-statement-extension.md) ".
		- `MERGE` (for syntax, see [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=SQLRF01606))
	Note:
	[Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=SQLRF30042) defines DML differently.
- Transaction control language (TCL) statements:
	- `COMMIT` (for syntax, see [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=SQLRF01110))
		- `ROLLBACK` (for syntax, see [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=SQLRF01610))
		- `SAVEPOINT` (for syntax, see [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=SQLRF01701))
		- `SET` `TRANSACTION` (for syntax, see [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=SQLRF01705))
- `LOCK` `TABLE` (for syntax, see [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=SQLRF01605))

A PL/SQL static SQL statement can have a PL/SQL identifier wherever its SQL counterpart can have a placeholder for a bind variable. The PL/SQL identifier must identify either a variable or a formal parameter.

To use PL/SQL identifiers for table names, column names, and so on, use the `EXECUTE` `IMMEDIATE` statement, explained in " [Native Dynamic SQL](native-dynamic-sql.md) "

Note:

After PL/SQL code runs a DML statement, the values of some variables are undefined. For example:

- After a `FETCH` or `SELECT` statement raises an exception, the values of the define variables after that statement are undefined.
- After a DML statement that affects zero rows, the values of the `OUT` bind variables are undefined, unless the DML statement is a `BULK` or multiple-row operation.

Example 6-1 Static SQL Statements

In this example, a PL/SQL anonymous block declares three PL/SQL variables and uses them in the static SQL statements `INSERT`, `UPDATE`, `DELETE`. The block also uses the static SQL statement `COMMIT`.

```
DROP TABLE employees_temp;
CREATE TABLE employees_temp AS
  SELECT employee_id, first_name, last_name 
  FROM employees;
 
DECLARE
  emp_id          employees_temp.employee_id%TYPE := 299;
  emp_first_name  employees_temp.first_name%TYPE  := 'Bob';
  emp_last_name   employees_temp.last_name%TYPE   := 'Henry';
BEGIN
  INSERT INTO employees_temp (employee_id, first_name, last_name) 
  VALUES (emp_id, emp_first_name, emp_last_name);
 
  UPDATE employees_temp
  SET first_name = 'Robert'
  WHERE employee_id = emp_id;
 
  DELETE FROM employees_temp
  WHERE employee_id = emp_id
  RETURNING first_name, last_name
  INTO emp_first_name, emp_last_name;
 
  COMMIT;
  DBMS_OUTPUT.PUT_LINE (emp_first_name || ' ' || emp_last_name);
END;
/
```

Result:

```
Robert Henry
```

### Pseudocolumns

A pseudocolumn behaves like a table column, but it is not stored in the table.

For general information about pseudocolumns, including restrictions, see [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=SQLRF0025).

Static SQL includes these SQL pseudocolumns:

- `CURRVAL` and `NEXTVAL`, described in " CURRVAL and NEXTVAL in PL/SQL ".
- `LEVEL`, described in [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=SQLRF50942)
- `OBJECT_VALUE`, described in [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=SQLRF50952)
	See Also:
	" [OBJECT\_VALUE Pseudocolumn](correlation-names-and-pseudorecords.md) " for information about using `OBJECT_VALUE` in triggers
- `ROWID`, described in [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=SQLRF00254)
	See Also:
	" [Simulating CURRENT OF Clause with ROWID Pseudocolumn](transaction-processing-and-control.md) "
- `ROWNUM`, described in [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=SQLRF00255)

#### CURRVAL and NEXTVAL in PL/SQL

After a sequence is created, you can access its values in SQL statements with the `CURRVAL` pseudocolumn, which returns the current value of the sequence, or the `NEXTVAL` pseudocolumn, which increments the sequence and returns the new value.

To reference these pseudocolumns, use dot notation—for example, `sequence_name`.`CURRVAL`.

Note:

Each time you reference `sequence_name`.`NEXTVAL`, the sequence is incremented immediately and permanently, whether you commit or roll back the transaction.

You can use `sequence_name`.`CURRVAL` and `sequence_name`.`NEXTVAL` in a PL/SQL expression wherever you can use a `NUMBER` expression. However:

- Using `sequence_name`.`CURRVAL` or `sequence_name`.`NEXTVAL` to provide a default value for an ADT method parameter causes a compilation error.
- PL/SQL evaluates every occurrence of `sequence_name`.`CURRVAL` and `sequence_name`.`NEXTVAL` (unlike SQL, which evaluates a sequence expression for every row in which it appears).

See Also:

- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=SQLRF01314) for general information about sequences
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=SQLRF00253) for `CURRVAL` and `NEXTVAL` complete syntax

Example 6-2 CURRVAL and NEXTVAL Pseudocolumns

This example generates a sequence number for the sequence `HR.EMPLOYEES_SEQ` and refers to that number in multiple statements.

```
DROP TABLE employees_temp;
CREATE TABLE employees_temp AS
  SELECT employee_id, first_name, last_name
  FROM employees;
 
DROP TABLE employees_temp2;
CREATE TABLE employees_temp2 AS
  SELECT employee_id, first_name, last_name
  FROM employees;
 
DECLARE
  seq_value NUMBER;
BEGIN
  -- Generate initial sequence number
 
  seq_value := employees_seq.NEXTVAL;
 
  -- Print initial sequence number:
 
  DBMS_OUTPUT.PUT_LINE (
    'Initial sequence value: ' || TO_CHAR(seq_value)
  );
 
  -- Use NEXTVAL to create unique number when inserting data:
 
     INSERT INTO employees_temp (employee_id, first_name, last_name) 
     VALUES (employees_seq.NEXTVAL, 'Lynette', 'Smith');
 
  -- Use CURRVAL to store same value somewhere else:
 
     INSERT INTO employees_temp2 VALUES (employees_seq.CURRVAL,
                                         'Morgan', 'Smith');
 
  /* Because NEXTVAL values might be referenced
     by different users and applications,
     and some NEXTVAL values might not be stored in database,
     there might be gaps in sequence. */
 
  -- Use CURRVAL to specify record to delete:
 
     seq_value := employees_seq.CURRVAL;
 
     DELETE FROM employees_temp2
     WHERE employee_id = seq_value;
 
  -- Update employee_id with NEXTVAL for specified record:
 
     UPDATE employees_temp
     SET employee_id = employees_seq.NEXTVAL
     WHERE first_name = 'Lynette'
     AND last_name = 'Smith';
 
  -- Display final value of CURRVAL:
 
     seq_value := employees_seq.CURRVAL;
 
     DBMS_OUTPUT.PUT_LINE (
       'Ending sequence value: ' || TO_CHAR(seq_value)
     );
END;
/
```