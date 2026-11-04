---
title: Database PL/SQL Language Reference
book: Database PL/SQL Language Reference
doc_id: E96448-09
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/trigger-design-guidelines.html
tags:
  - oracle
  - 19c
  - pl-sql-language-reference
---

## Trigger Design Guidelines

- Use triggers to ensure that whenever a specific event occurs, any necessary actions are done (regardless of which user or application issues the triggering statement).
	For example, use a trigger to ensure that whenever anyone updates a table, its log file is updated.
- Do not create triggers that duplicate database features.
	For example, do not create a trigger to reject invalid data if you can do the same with constraints (see " [How Triggers and Constraints Differ](reasons-use-triggers.md) ").
- Do not create triggers that depend on the order in which a SQL statement processes rows (which can vary).
	For example, do not assign a value to a global package variable in a row trigger if the current value of the variable depends on the row being processed by the row trigger. If a trigger updates global package variables, initialize those variables in a `BEFORE` statement trigger.
- Use `BEFORE` row triggers to modify the row before writing the row data to disk.
- Use `AFTER` row triggers to obtain the row ID and use it in operations.
	An `AFTER` row trigger fires when the triggering statement results in ORA-02292.
	Note:
	`AFTER` row triggers are slightly more efficient than `BEFORE` row triggers. With `BEFORE` row triggers, affected data blocks are read first for the trigger and then for the triggering statement. With `AFTER` row triggers, affected data blocks are read only for the trigger.
- If the triggering statement of a `BEFORE` row trigger is an `UPDATE` or `DELETE` statement that conflicts with an `UPDATE` statement that is running, then the database does a transparent `ROLLBACK` to `SAVEPOINT` and restarts the triggering statement. The database can do this many times before the triggering statement completes successfully. Each time the database restarts the triggering statement, the trigger fires. The `ROLLBACK` to `SAVEPOINT` does not undo changes to package variables that the trigger references. To ensure that there are no unwanted side effects with each restart, make sure that the `BEFORE` row trigger is idempotent, meaning the trigger should be written so that the result remains the same with each subsequent execution. Any additional work that should not be repeated can be handled in an `AFTER` row trigger. To detect this situation, you can also include a counter variable in the package.
- Do not create recursive triggers.
	For example, do not create an `AFTER` `UPDATE` trigger that issues an `UPDATE` statement on the table on which the trigger is defined. The trigger fires recursively until it runs out of memory.
- If you create a trigger that includes a statement that accesses a remote database, then put the exception handler for that statement in a stored subprogram and invoke the subprogram from the trigger.
	For more information, see " [Remote Exception Handling](exception-handling-triggers.md) ".
- Use `DATABASE` triggers judiciously. They fire every time any database user initiates a triggering event.
- If a trigger runs the following statement, the statement returns the owner of the trigger, not the user who is updating the table:
	```
	SELECT Username FROM USER_USERS;
	```
- Only committed triggers fire.
	A trigger is committed, implicitly, after the `CREATE` `TRIGGER` statement that creates it succeeds. Therefore, the following statement cannot fire the trigger that it creates:
	```
	CREATE OR REPLACE TRIGGER my_trigger
	  AFTER CREATE ON DATABASE
	BEGIN
	  NULL;
	END;
	/
	```
- To allow the modular installation of applications that have triggers on the same tables, create multiple triggers of the same type, rather than a single trigger that runs a sequence of operations.
	Each trigger sees the changes made by the previously fired triggers. Each trigger can see `OLD` and `NEW` values.