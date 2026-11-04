---
title: Database PL/SQL Language Reference
book: Database PL/SQL Language Reference
doc_id: E96448-09
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/system-triggers.html
tags:
  - oracle
  - 19c
  - pl-sql-language-reference
---

## System Triggers

A system trigger is created on either a schema or the database.

Its triggering event is composed of either DDL statements (listed in " [ddl\_event](CREATE-TRIGGER-statement.md) ") or database operation statements (listed in " [database\_event](CREATE-TRIGGER-statement.md) ").

A system trigger fires at exactly one of these timing points:

- Before the triggering statement runs
	(The trigger is called a `BEFORE` statement trigger or statement-level `BEFORE` trigger.)
- After the triggering statement runs
	(The trigger is called a `AFTER` statement trigger or statement-level `AFTER` trigger.)
- Instead of the triggering `CREATE` statement
	(The trigger is called an `INSTEAD` `OF` `CREATE` trigger.)

Topics

### SCHEMA Triggers

A `SCHEMA` trigger is created on a schema and fires whenever the user who owns it is the current user and initiates the triggering event.

Suppose that both user1 and user2 own schema triggers, and user1 invokes a DR unit owned by user2. Inside the DR unit, user2 is the current user. Therefore, if the DR unit initiates the triggering event of a schema trigger that user2 owns, then that trigger fires. However, if the DR unit initiates the triggering event of a schema trigger that user1 owns, then that trigger does not fire.

Example 9-19 creates a `BEFORE` statement trigger on the sample schema `HR`. When a user connected as `HR` tries to drop a database object, the database fires the trigger before dropping the object.

Example 9-19 BEFORE Statement Trigger on Sample Schema HR

```
CREATE OR REPLACE TRIGGER drop_trigger
  BEFORE DROP ON hr.SCHEMA
  BEGIN
    RAISE_APPLICATION_ERROR (
      num => -20000,
      msg => 'Cannot drop object');
  END;
/
```

### DATABASE Triggers

A `DATABASE` trigger is created on the database and fires whenever any database user initiates the triggering event.

Example 9-20 shows the basic syntax for a trigger to log errors. This trigger fires after an unsuccessful statement execution, such as unsuccessful logon.

Note:

An `AFTER` `SERVERERROR` trigger fires only if Oracle relational database management system (RDBMS) determines that it is safe to fire error triggers. For more information about `AFTER` `SERVERERROR` triggers, see [CREATE TRIGGER Statement](CREATE-TRIGGER-statement.md).

The trigger in Example 9-21 runs the procedure `check_user` after a user logs onto the database.

Example 9-20 AFTER Statement Trigger on Database

```
CREATE TRIGGER log_errors
  AFTER SERVERERROR ON DATABASE
  BEGIN
    IF (IS_SERVERERROR (1017)) THEN
      NULL;  -- (substitute code that processes logon error)
    ELSE
      NULL;  -- (substitute code that logs error code)
    END IF;
  END;
/
```

Example 9-21 Trigger Monitors Logons

```
CREATE OR REPLACE TRIGGER check_user
  AFTER LOGON ON DATABASE
  BEGIN
    check_user;
  EXCEPTION
    WHEN OTHERS THEN
      RAISE_APPLICATION_ERROR
        (-20000, 'Unexpected error: '|| DBMS_Utility.Format_Error_Stack);
 END;
/
```

### INSTEAD OF CREATE Triggers

An `INSTEAD` `OF` `CREATE` trigger is a `SCHEMA` trigger whose triggering event is a `CREATE` statement. The database fires the trigger instead of executing its triggering statement.

Example 9-22 shows the basic syntax for an `INSTEAD` `OF` `CREATE` trigger on the current schema. This trigger fires when the owner of the current schema issues a `CREATE` statement in the current schema.

Example 9-22 INSTEAD OF CREATE Trigger on Schema

```
CREATE OR REPLACE TRIGGER t
  INSTEAD OF CREATE ON SCHEMA
  BEGIN
    EXECUTE IMMEDIATE 'CREATE TABLE T (n NUMBER, m NUMBER)';
  END;
/
```