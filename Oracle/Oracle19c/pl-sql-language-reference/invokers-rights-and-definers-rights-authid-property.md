---
title: Database PL/SQL Language Reference
book: Database PL/SQL Language Reference
doc_id: E96448-09
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/invokers-rights-and-definers-rights-authid-property.html
tags:
  - oracle
  - 19c
  - pl-sql-language-reference
---

## Invoker's Rights and Definer's Rights (AUTHID Property)

The `AUTHID` property of a stored PL/SQL unit affects the name resolution and privilege checking of SQL statements that the unit issues at run time. The `AUTHID` property does not affect compilation, and has no meaning for units that have no code, such as collection types.

`AUTHID` property values are exposed in the static data dictionary view `*_PROCEDURES`. For units for which `AUTHID` has meaning, the view shows the value `CURRENT_USER` or `DEFINER`; for other units, the view shows `NULL`.

For stored PL/SQL units that you create or alter with the following statements, you can use the optional `AUTHID` clause to specify either `DEFINER` (the default, for backward compatibility) or `CURRENT_USER` (the preferred usage):

- " [CREATE FUNCTION Statement](CREATE-FUNCTION-statement.md) "
- " [CREATE PACKAGE Statement](CREATE-PACKAGE-statement.md) "
- " [CREATE PROCEDURE Statement](CREATE-PROCEDURE-statement.md) "
- " [CREATE TYPE Statement](CREATE-TYPE-statement.md) "
- " [ALTER TYPE Statement](ALTER-TYPE-statement.md) "

A unit whose `AUTHID` value is `CURRENT_USER` is called an invoker's rights unit, or IR unit. A unit whose `AUTHID` value is `DEFINER` (the default) is called a definer's rights unit, or DR unit. PL/SQL units and schema objects for which you cannot specify an `AUTHID` value behave like this:

| PL/SQL Unit or Schema Object | Behavior |
| --- | --- |
| Anonymous block | IR unit |
| `BEQUEATH` `CURRENT_USER` view | Somewhat like an IR unit—see [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=DBSEG586). |
| `BEQUEATH` `DEFINER` view | DR unit |
| Trigger | DR unit |

The `AUTHID` property of a unit determines whether the unit is IR or DR, and it affects both name resolution and privilege checking at run time:

- The context for name resolution is `CURRENT_SCHEMA`.
- The privileges checked are those of the `CURRENT_USER` and the enabled roles.

When a session starts, `CURRENT_SCHEMA` has the value of the schema owned by `SESSION_USER`, and `CURRENT_USER` has the same value as `SESSION_USER`. (To get the current value of `CURRENT_SCHEMA`, `CURRENT_USER`, or `SESSION_USER`, use the `SYS_CONTEXT` function, documented in [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=SQLRF06117).)

`CURRENT_SCHEMA` can be changed during the session with the SQL statement `ALTER` `SESSION` `SET` `CURRENT_SCHEMA`. `CURRENT_USER` cannot be changed programmatically, but it might change when a PL/SQL unit or a view is pushed onto, or popped from, the call stack.

Note:

Oracle recommends against issuing `ALTER` `SESSION` `SET` `CURRENT_SCHEMA` from in a stored PL/SQL unit.

During a server call, when a DR unit is pushed onto the call stack, the database stores the currently enabled roles and the current values of `CURRENT_USER` and `CURRENT_SCHEMA`. It then changes both `CURRENT_USER` and `CURRENT_SCHEMA` to the owner of the DR unit, and enables only the role `PUBLIC`. (The stored and new roles and values are not necessarily different.) When the DR unit is popped from the call stack, the database restores the stored roles and values. In contrast, when an IR unit is pushed onto, or popped from, the call stack, the values of `CURRENT_USER` and `CURRENT_SCHEMA`, and the currently enabled roles do not change (unless roles are granted to the IR unit itself—see " Granting Roles to PL/SQL Packages and Standalone Subprograms ").

For dynamic SQL statements issued by a PL/SQL unit, name resolution and privilege checking are done once, at run time. For static SQL statements, name resolution and privilege checking are done twice: first, when the PL/SQL unit is compiled, and then again at run time. At compile time, the `AUTHID` property has no effect—both DR and IR units are treated like DR units. At run time, however, the `AUTHID` property determines whether a unit is IR or DR, and the unit is treated accordingly.

Upon entry into an IR unit, the runtime system checks privileges before doing any initialization or running any code. If the unit owner has neither the `INHERIT` `PRIVILEGES` privilege on the invoker nor the `INHERIT` `ANY` `PRIVILEGES` privilege, then the runtime system raises error ORA-06598.

Note:

If the unit owner has the required privilege, then one of these statements granted it:

```
GRANT INHERIT PRIVILEGES ON current_user TO PUBLIC
GRANT INHERIT PRIVILEGES ON current_user TO unit_owner
GRANT INHERIT ANY PRIVILEGES TO unit_owner
```

For information about the `GRANT` statement, see [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=SQLRF01603).

See Also:

- [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=DBSEG658) for information about managing security for DR and IR units
- [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=DBSEG-GUID-44CB644B-7B59-4B3B-B375-9F9B96F60186) for information about capturing privileges that are required to compile DR and IR program units

Topics

- Granting Roles to PL/SQL Packages and Standalone Subprograms
- IR Units Need Template Objects

### Granting Roles to PL/SQL Packages and Standalone Subprograms

Using the SQL `GRANT` command, you can grant roles to PL/SQL packages and standalone subprograms. Roles granted to a PL/SQL unit do not affect compilation. They affect the privilege checking of SQL statements that the unit issues at run time: The unit runs with the privileges of both its own roles and any other currently enabled roles.

Typically, you grant roles to an IR unit, so that users with lower privileges than yours can run the unit with only the privileges needed to do so. You grant roles to a DR unit (whose invokers run it with all your privileges) only if the DR unit issues dynamic SQL, which is checked only at run time.

The basic syntax for granting roles to PL/SQL units is:

```
GRANT role [, role ]... TO unit [, unit ]...
```

For example, this command grants the roles `read` and `execute` to the function `scott`.`func` and the package `sys`.`pkg`:

```
GRANT read, execute TO FUNCTION scott.func, PACKAGE sys.pkg
```

For the complete syntax and semantics of the `GRANT` command, see [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=SQLRF01603).

See Also:

- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=SQLRF01609) for information about the `REVOKE` command, which lets you revoke roles from PL/SQL units
- [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=DBSEG977) for more information about configuring application users and application roles

### IR Units Need Template Objects

One user (that is, one schema) owns an IR unit and other users run it in their schemas. If the IR unit issues static SQL statements, then the schema objects that these statements affect must exist in the owner's schema at compile time (so that the compiler can resolve references) and in the invoker's schema at run time. The definitions of corresponding schema objects must match (for example, corresponding tables must have the same names and columns); otherwise, you get an error or unexpected results. However, the objects in the owner's schema need not contain data, because the compiler does not need it; therefore, they are called template objects.

### Connected User Database Links in DR Units

If you include a connected user database link in a DR unit (definer's rights unit), then you must grant the user who will run the DR unit the `INHERIT REMOTE PRIVILEGES` privilege.

Granting the user this privilege enables the user to execute the DR unit; otherwise, the execution will fail with an `ORA-25433: User  does not have INHERIT REMOTE PRIVILEGES` error. To include a connected user database link from within a definer's rights (DR) procedure, include `@database_link` in the procedure.

The following example shows how a DR unit can use a database link called `dblink` to access the `EMPLOYEE_ID` column of the `HR.EMPLOYEES` table:

Example 8-43 Database Link in a DR Unit

```
CREATE OR REPLACE PROCEDURE hr_remote_db_link
AS
v_employee_id VARCHAR(50);
BEGIN  
    EXECUTE IMMEDIATE 'SELECT employee_id FROM employees@dblink' into v_employee_id;
    DBMS_OUTPUT.PUT_LINE('employee_id: ' || v_employee_id);
END ;
/
```

See Also:

[Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=DBSEG-GUID-B354724F-BD35-47C7-A699-93C2B6389555) for more information about using the `INHERIT REMOTE PRIVILEGES` privilege, including a tutorial on how a DR unit can use a database link