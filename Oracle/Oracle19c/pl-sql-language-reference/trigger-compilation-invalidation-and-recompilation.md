---
title: Database PL/SQL Language Reference
book: Database PL/SQL Language Reference
doc_id: E96448-09
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/trigger-compilation-invalidation-and-recompilation.html
tags:
  - oracle
  - 19c
  - pl-sql-language-reference
---

## Trigger Compilation, Invalidation, and Recompilation

The `CREATE` `TRIGGER` statement compiles the trigger and stores its code in the database. If a compilation error occurs, the trigger is still created, but its triggering statement fails, except in these cases:

- The trigger was created in the disabled state.
- The triggering event is `AFTER` `STARTUP` `ON` `DATABASE`.
- The triggering event is either `AFTER` `LOGON` `ON` `DATABASE` or `AFTER` `LOGON` `ON` `SCHEMA`, and someone logs on as `SYSTEM`.

To see trigger compilation errors, either use the `SHOW` `ERRORS` command in SQL\*Plus or Enterprise Manager, or query the static data dictionary view `*_ERRORS` (described in [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=REFRN26065)).

If a trigger does not compile successfully, then its exception handler cannot run. For an example, see " [Remote Exception Handling](exception-handling-triggers.md) ".

If a trigger references another object, such as a subprogram or package, and that object is modified or dropped, then the trigger becomes invalid. The next time the triggering event occurs, the compiler tries to revalidate the trigger (for details, see [Oracle Database Development Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=ADFNS99967)).

Note:

Because the `DBMS_AQ` package is used to enqueue a message, dependency between triggers and queues cannot be maintained.

To recompile a trigger manually, use the `ALTER` `TRIGGER` statement, described in " [ALTER TRIGGER Statement](ALTER-TRIGGER-statement.md) ".