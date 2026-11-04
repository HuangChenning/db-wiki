---
title: Database PL/SQL Language Reference
book: Database PL/SQL Language Reference
doc_id: E96448-09
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/compile-time-warnings.html
tags:
  - oracle
  - 19c
  - pl-sql-language-reference
---

## Compile-Time Warnings

While compiling stored PL/SQL units, the PL/SQL compiler generates warnings for conditions that are not serious enough to cause errors and prevent compilation—for example, using a deprecated PL/SQL feature.

To see warnings (and errors) generated during compilation, either query the static data dictionary view `*_ERRORS` or, in the SQL\*Plus environment, use the command `SHOW` `ERRORS`.

The message code of a PL/SQL warning has the form PLW-nnnnn.

Table 11-1 Compile-Time Warning Categories

| Category | Description | Example |
| --- | --- | --- |
| `SEVERE` | Condition might cause unexpected action or wrong results. | Aliasing problems with parameters |
| `PERFORMANCE` | Condition might cause performance problems. | Passing a `VARCHAR2` value to a `NUMBER` column in an `INSERT` statement |
| `INFORMATIONAL` | Condition does not affect performance or correctness, but you might want to change it to make the code more maintainable. | Code that can never run |

By setting the compilation parameter `PLSQL_WARNINGS`, you can:

- Enable and disable all warnings, one or more categories of warnings, or specific warnings
- Treat specific warnings as errors (so that those conditions must be corrected before you can compile the PL/SQL unit)

You can set the value of `PLSQL_WARNINGS` for:

- Your Oracle database instance
	Use the `ALTER` `SYSTEM` statement, described in [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=SQLRF00902).
- Your session
	Use the `ALTER` `SESSION` statement, described in [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=SQLRF00901).
- A stored PL/SQL unit
	Use an `ALTER` statement from " [ALTER Statements](sql-statements-for-stored-plsql-units.md) " with its `compiler_parameters_clause`.

In any of the preceding `ALTER` statements, you set the value of `PLSQL_WARNINGS` with this syntax:

```
PLSQL_WARNINGS = 'value_clause' [, 'value_clause' ] ...
```

For the syntax of `value_clause`, see [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=REFRN10249).

To display the current value of `PLSQL_WARNINGS`, query the static data dictionary view `ALL_PLSQL_OBJECT_SETTINGS`.

See Also:

- [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=REFRN20385) for more information about the static data dictionary view `ALL_PLSQL_OBJECT_SETTINGS`
- [Oracle Database Error Messages Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=ERRMG-GUID-CA5A766D-6CBF-4235-982F-86A6F34266CC) for the message codes of all PL/SQL warnings
- [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=REFRN20065) for more information about the static data dictionary view `*_ERRORS`
- " [PL/SQL Units and Compilation Parameters](architecture-pl-sql.md) " for more information about PL/SQL units and compiler parameters

Example 11-1 Setting Value of PLSQL\_WARNINGS Compilation Parameter

This example shows several `ALTER` statements that set the value of `PLSQL_WARNINGS`.

For the session, enable all warnings—highly recommended during development:

```
ALTER SESSION SET PLSQL_WARNINGS='ENABLE:ALL';
```

For the session, enable `PERFORMANCE` warnings:

```
ALTER SESSION SET PLSQL_WARNINGS='ENABLE:PERFORMANCE';
```

For the procedure `loc_var`, enable `PERFORMANCE` warnings, and reuse settings:

```
ALTER PROCEDURE loc_var
  COMPILE PLSQL_WARNINGS='ENABLE:PERFORMANCE'
  REUSE SETTINGS;
```

For the session, enable `SEVERE` warnings, disable `PERFORMANCE` warnings, and treat PLW-06002 warnings as errors:

```
ALTER SESSION
  SET PLSQL_WARNINGS='ENABLE:SEVERE', 'DISABLE:PERFORMANCE', 'ERROR:06002';
```

For the session, disable all warnings:

```
ALTER SESSION SET PLSQL_WARNINGS='DISABLE:ALL';
```

### DBMS\_WARNING Package

If you are writing PL/SQL units in a development environment that compiles them (such as SQL\*Plus), you can display and set the value of `PLSQL_WARNINGS` by invoking subprograms in the `DBMS_WARNING` package.

Example 11-2 uses an `ALTER` `SESSION` statement to disable all warning messages for the session and then compiles a procedure that has unreachable code. The procedure compiles without warnings. Next, the example enables all warnings for the session by invoking `DBMS_WARNING.set_warning_setting_string` and displays the value of `PLSQL_WARNINGS` by invoking `DBMS_WARNING.get_warning_setting_string`. Finally, the example recompiles the procedure, and the compiler generates a warning about the unreachable code.

Note:

Unreachable code could represent a mistake or be intentionally hidden by a debug flag.

`DBMS_WARNING` subprograms are useful when you are compiling a complex application composed of several nested SQL\*Plus scripts, where different subprograms need different `PLSQL_WARNINGS` settings. With `DBMS_WARNING` subprograms, you can save the current `PLSQL_WARNINGS` setting, change the setting to compile a particular set of subprograms, and then restore the setting to its original value.

See Also:

[Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=ARPLS370) for more information about the `DBMS_WARNING` package

Example 11-2 Displaying and Setting PLSQL\_WARNINGS with DBMS\_WARNING Subprograms

Disable all warning messages for this session:

```
ALTER SESSION SET PLSQL_WARNINGS='DISABLE:ALL';
```

With warnings disabled, this procedure compiles with no warnings:

```
CREATE OR REPLACE PROCEDURE unreachable_code AUTHID DEFINER AS
  x CONSTANT BOOLEAN := TRUE;
BEGIN
  IF x THEN
    DBMS_OUTPUT.PUT_LINE('TRUE');
  ELSE
    DBMS_OUTPUT.PUT_LINE('FALSE');
  END IF;
END unreachable_code;
/
```

Enable all warning messages for this session:

```
CALL DBMS_WARNING.set_warning_setting_string ('ENABLE:ALL', 'SESSION');
```

Check warning setting:

```
SELECT DBMS_WARNING.get_warning_setting_string() FROM DUAL;
```

Result:

```
DBMS_WARNING.GET_WARNING_SETTING_STRING()
-----------------------------------------
 
ENABLE:ALL
 
1 row selected.
```

Recompile procedure:

```
ALTER PROCEDURE unreachable_code COMPILE;
```

Result:

```
SP2-0805: Procedure altered with compilation warnings
```

Show errors:

```
SHOW ERRORS
```

Result:

```
Errors for PROCEDURE UNREACHABLE_CODE:
 
LINE/COL ERROR
-------- -----------------------------------------------------------------
7/5      PLW-06002: Unreachable code
```