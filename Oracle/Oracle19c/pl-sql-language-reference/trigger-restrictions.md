---
title: Database PL/SQL Language Reference
book: Database PL/SQL Language Reference
doc_id: E96448-09
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/trigger-restrictions.html
tags:
  - oracle
  - 19c
  - pl-sql-language-reference
---

## Trigger Restrictions

In addition to the restrictions that apply to all PL/SQL units (see [Table C-1](plsql-program-limits.md)), triggers have these restrictions:

- Trigger Size Restriction
- Trigger LONG and LONG RAW Data Type Restrictions
- Mutating-Table Restriction
- Only an autonomous trigger can run TCL or DDL statements.
	For information about autonomous triggers, see " [Autonomous Triggers](autonomous-transactions.md) ".
- A trigger cannot invoke a subprogram that runs transaction control statements, because the subprogram runs in the context of the trigger body.
	For more information about subprograms invoked by triggers, see " [Subprograms Invoked by Triggers](subprograms-invoked-triggers.md) ".
- A trigger cannot access a `SERIALLY_REUSABLE` package.
	For information about `SERIALLY_REUSABLE` packages, see " [SERIALLY\_REUSABLE Packages](serially_reusable-packages.md) ".

See Also:

" [Compound DML Trigger Restrictions](dml-triggers.md) "

### Trigger Size Restriction

The size of the trigger cannot exceed 32K.

If the logic for your trigger requires much more than 60 lines of PL/SQL source text, then put most of the source text in a stored subprogram and invoke the subprogram from the trigger. For information about subprograms invoked by triggers, see " [Subprograms Invoked by Triggers](subprograms-invoked-triggers.md) ".

### Trigger LONG and LONG RAW Data Type Restrictions

Note:

Oracle supports the `LONG` and `LONG` `RAW` data types only for backward compatibility with existing applications.

In addition to the restrictions that apply to all PL/SQL units (see " [LONG and LONG RAW Variables](sql-data-types.md) "), triggers have these restrictions:

- A trigger cannot declare a variable of the `LONG` or `LONG` `RAW` data type.
- A SQL statement in a trigger can reference a `LONG` or `LONG` `RAW` column only if the column data can be converted to the data type `CHAR` or `VARCHAR2`.
- A trigger cannot use the correlation name `NEW` or `PARENT` with a `LONG` or `LONG` `RAW` column.

### Mutating-Table Restriction

Note:

This topic applies only to row-level simple DML triggers.

A mutating table is a table that is being modified by a DML statement (possibly by the effects of a `DELETE` `CASCADE` constraint). (A view being modified by an `INSTEAD` `OF` trigger is not considered to be mutating.)

The mutating-table restriction prevents the trigger from querying or modifying the table that the triggering statement is modifying. When a row-level trigger encounters a mutating table, ORA-04091 occurs, the effects of the trigger and triggering statement are rolled back, and control returns to the user or application that issued the triggering statement, as Example 9-26 shows.

Caution:

Oracle Database does not enforce the mutating-table restriction for a trigger that accesses remote nodes, because the database does not support declarative referential constraints between tables on different nodes of a distributed database.

Similarly, the database does not enforce the mutating-table restriction for tables in the same database that are connected by loop-back database links. A loop-back database link makes a local table appear remote by defining an Oracle Net path back to the database that contains the link.

If you must use a trigger to update a mutating table, you can avoid the mutating-table error in either of these ways:

- Use a compound DML trigger (see " [Using Compound DML Triggers to Avoid Mutating-Table Error](dml-triggers.md) ").
- Use a temporary table.
	For example, instead of using one `AFTER` each row trigger that updates the mutating table, use two triggers—an `AFTER` each row trigger that updates the temporary table and an `AFTER` statement trigger that updates the mutating table with the values from the temporary table.

Mutating-Table Restriction Relaxed

As of Oracle Database 8g Release 1, a deletion from the parent table causes `BEFORE` and `AFTER` triggers to fire once. Therefore, you can create row-level and statement-level triggers that query and modify the parent and child tables. This allows most foreign key constraint actions to be implemented through their after-row triggers (unless the constraint is self-referential). Update cascade, update set null, update set default, delete set default, inserting a missing parent, and maintaining a count of children can all be implemented easily—see " [Triggers for Ensuring Referential Integrity](dml-triggers.md) ".

However, cascades require care for multiple-row foreign key updates. The trigger cannot miss rows that were changed but not committed by another transaction, because the foreign key constraint guarantees that no matching foreign key rows are locked before the after-row trigger is invoked.

In Example 9-27, the triggering statement updates `p` correctly but causes problems when the trigger updates `f`. First, the triggering statement changes (1) to (2) in `p`, and the trigger updates (1) to (2) in `f`, leaving two rows of value (2) in `f`. Next, the triggering statement updates (2) to (3) in `p`, and the trigger updates both rows of value (2) to (3) in `f`. Finally, the statement updates (3) to (4) in `p`, and the trigger updates all three rows in f from (3) to (4). The relationship between the data items in `p` and `f` is lost.

To avoid this problem, either forbid multiple-row updates to `p` that change the primary key and reuse existing primary key values, or track updates to foreign key values and modify the trigger to ensure that no row is updated twice.

Example 9-26 Trigger Causes Mutating-Table Error

```
-- Create log table
 
DROP TABLE log;
CREATE TABLE log (
  emp_id  NUMBER(6),
  l_name  VARCHAR2(25),
  f_name  VARCHAR2(20)
);
 
-- Create trigger that updates log and then reads employees
 
CREATE OR REPLACE TRIGGER log_deletions
  AFTER DELETE ON employees
  FOR EACH ROW
DECLARE
  n INTEGER;
BEGIN
  INSERT INTO log VALUES (
    :OLD.employee_id,
    :OLD.last_name,
    :OLD.first_name
  );
 
  SELECT COUNT(*) INTO n FROM employees;
  DBMS_OUTPUT.PUT_LINE('There are now ' || n || ' employees.');
END;
/
 
-- Issue triggering statement:
 
DELETE FROM employees WHERE employee_id = 197;
```

Result:

```
DELETE FROM employees WHERE employee_id = 197
            *
ERROR at line 1:
ORA-04091: table HR.EMPLOYEES is mutating, trigger/function might not see it
ORA-06512: at "HR.LOG_DELETIONS", line 10
ORA-04088: error during execution of trigger 'HR.LOG_DELETIONS'
```

Show that effect of trigger was rolled back:

```
SELECT count(*) FROM log;
```

Result:

```
COUNT(*)
----------
         0
 
1 row selected.
```

Show that effect of triggering statement was rolled back:

```
SELECT employee_id, last_name FROM employees WHERE employee_id = 197;
```

Result:

```
EMPLOYEE_ID LAST_NAME
----------- -------------------------
        197 Feeney
 
1 row selected.
```

Example 9-27 Update Cascade

```
DROP TABLE p;
CREATE TABLE p (p1 NUMBER CONSTRAINT pk_p_p1 PRIMARY KEY);
INSERT INTO p VALUES (1);
INSERT INTO p VALUES (2);
INSERT INTO p VALUES (3);
 
DROP TABLE f;
CREATE TABLE f (f1 NUMBER CONSTRAINT fk_f_f1 REFERENCES p);
INSERT INTO f VALUES (1);
INSERT INTO f VALUES (2);
INSERT INTO f VALUES (3);
 
CREATE TRIGGER pt
  AFTER UPDATE ON p
  FOR EACH ROW
BEGIN
  UPDATE f SET f1 = :NEW.p1 WHERE f1 = :OLD.p1;
END;
/
```

Query:

```
SELECT * FROM p ORDER BY p1;
```

Result:

```
P1
----------
         1
         2
         3
```

Query:

```
SELECT * FROM f ORDER BY f1;
```

Result:

```
F1
----------
         1
         2
         3
```

Issue triggering statement:

```
UPDATE p SET p1 = p1+1;
```

Query:

```
SELECT * FROM p ORDER BY p1;
```

Result:

```
P1
----------
         2
         3
         4
```

Query:

```
SELECT * FROM f ORDER BY f1;
```

Result:

```
F1
----------
         4
         4
         4
```