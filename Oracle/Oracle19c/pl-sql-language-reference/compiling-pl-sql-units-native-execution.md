---
title: Database PL/SQL Language Reference
book: Database PL/SQL Language Reference
doc_id: E96448-09
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/compiling-pl-sql-units-native-execution.html
tags:
  - oracle
  - 19c
  - pl-sql-language-reference
---

## Compiling PL/SQL Units for Native Execution

You can usually speed up PL/SQL units by compiling them into native code (processor-dependent system code), which is stored in the SYSTEM tablespace.

You can natively compile any PL/SQL unit of any type, including those that Oracle Database supplies.

Natively compiled program units work in all server environments, including shared server configuration (formerly called "multithreaded server") and Oracle Real Application Clusters (Oracle RAC).

On most platforms, PL/SQL native compilation requires no special set-up or maintenance. On some platforms, the DBA might want to do some optional configuration.

See Also:

- [Oracle Database Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=ADMIN002) for information about configuring a database
- Platform-specific configuration documentation for your platform

You can test to see how much performance gain you can get by enabling PL/SQL native compilation.

If you have determined that PL/SQL native compilation will provide significant performance gains in database operations, Oracle recommends compiling the entire database for native mode, which requires DBA privileges. This speeds up both your own code and calls to the PL/SQL packages that Oracle Database supplies.

Topics

\* Requires DBA privileges.

### Determining Whether to Use PL/SQL Native Compilation

Whether to compile a PL/SQL unit for native or interpreted mode depends on where you are in the development cycle and on what the program unit does.

While you are debugging program units and recompiling them frequently, interpreted mode has these advantages:

- You can use PL/SQL debugging tools on program units compiled for interpreted mode (but not for those compiled for native mode).
- Compiling for interpreted mode is faster than compiling for native mode.

After the debugging phase of development, in determining whether to compile a PL/SQL unit for native mode, consider:

- PL/SQL native compilation provides the greatest performance gains for computation-intensive procedural operations. Examples are data warehouse applications and applications with extensive server-side transformations of data for display.
- PL/SQL native compilation provides the least performance gains for PL/SQL subprograms that spend most of their time running SQL.
- When many program units (typically over 15,000) are compiled for native execution, and are simultaneously active, the large amount of shared memory required might affect system performance.

### How PL/SQL Native Compilation Works

Without native compilation, the PL/SQL statements in a PL/SQL unit are compiled into an intermediate form, system code, which is stored in the catalog and interpreted at run time.

With PL/SQL native compilation, the PL/SQL statements in a PL/SQL unit are compiled into native code and stored in the catalog. The native code need not be interpreted at run time, so it runs faster.

Because native compilation applies only to PL/SQL statements, a PL/SQL unit that uses only SQL statements might not run faster when natively compiled, but it does run at least as fast as the corresponding interpreted code. The compiled code and the interpreted code make the same library calls, so their action is the same.

The first time a natively compiled PL/SQL unit runs, it is fetched from the SYSTEM tablespace into shared memory. Regardless of how many sessions invoke the program unit, shared memory has only one copy it. If a program unit is not being used, the shared memory it is using might be freed, to reduce memory load.

Natively compiled subprograms and interpreted subprograms can invoke each other.

PL/SQL native compilation works transparently in an Oracle Real Application Clusters (Oracle RAC) environment.

The `PLSQL_CODE_TYPE` compilation parameter determines whether PL/SQL code is natively compiled or interpreted. For information about this compilation parameters, see " [PL/SQL Units and Compilation Parameters](architecture-pl-sql.md) ".

### Dependencies, Invalidation, and Revalidation

Recompilation is automatic with invalidated PL/SQL modules. For example, if an object on which a natively compiled PL/SQL subprogram depends changes, the subprogram is invalidated. The next time the same subprogram is called, the database recompiles the subprogram automatically. Because the `PLSQL_CODE_TYPE` setting is stored inside the library unit for each subprogram, the automatic recompilation uses this stored setting for code type.

Explicit recompilation does not necessarily use the stored `PLSQL_CODE_TYPE` setting. For the conditions under which explicit recompilation uses stored settings, see " [PL/SQL Units and Compilation Parameters](architecture-pl-sql.md) ".

### Setting Up a New Database for PL/SQL Native Compilation

If you have DBA privileges, you can set up a new database for PL/SQL native compilation by setting the compilation parameter `PLSQL_CODE_TYPE` to `NATIVE`. The performance benefits apply to the PL/SQL packages that Oracle Database supplies, which are used for many database operations.

Note:

If you compile the whole database as `NATIVE`, Oracle recommends that you set `PLSQL_CODE_TYPE` at the system level.

### Compiling the Entire Database for PL/SQL Native or Interpreted Compilation

If you have DBA privileges, you can recompile all PL/SQL modules in an existing database to `NATIVE` or `INTERPRETED`, using the `dbmsupgnv`.`sql` and `dbmsupgin`.`sql` scripts respectively during the process explained in this section. Before making the conversion, review " Determining Whether to Use PL/SQL Native Compilation ".

Note:

- If you compile the whole database as `NATIVE`, Oracle recommends that you set `PLSQL_CODE_TYPE` at the system level.
- If Database Vault is enabled, then you can run `dbmsupgnv`.`sql` only if the Database Vault administrator has granted you the `DV_PATCH_ADMIN` role.
- The conversion process described here affects only the current container's units. Units in other containers are not affected.

During the conversion to native compilation, `TYPE` specifications are not recompiled by `dbmsupgnv`.`sql` to `NATIVE` because these specifications do not contain executable code.

Package specifications seldom contain executable code so the runtime benefits of compiling to `NATIVE` are not measurable. You can use the `TRUE` command-line parameter with the `dbmsupgnv`.`sql` script to exclude package specs from recompilation to `NATIVE`, saving time in the conversion process.

When converting to interpreted compilation, the `dbmsupgin`.`sql` script does not accept any parameters and does not exclude any PL/SQL units.

Note:

The following procedure describes the conversion to native compilation. If you must recompile all PL/SQL modules to interpreted compilation, make these changes in the steps.

- Skip the first step.
- Set the `PLSQL_CODE_TYPE` compilation parameter to `INTERPRETED` rather than `NATIVE`.
- Substitute `dbmsupgin`.`sql` for the `dbmsupgnv`.`sql` script.

1. Ensure that a test PL/SQL unit can be compiled. For example:
	```
	ALTER PROCEDURE my_proc COMPILE PLSQL_CODE_TYPE=NATIVE REUSE SETTINGS;
	```
2. Shut down application services, the listener, and the database.
	- Shut down all of the Application services including the Forms Processes, Web Servers, Reports Servers, and Concurrent Manager Servers. After shutting down all of the Application services, ensure that all of the connections to the database were terminated.
	- Shut down the TNS listener of the database to ensure that no new connections are made.
	- Shut down the database in normal or immediate mode as the user `SYS`. See [Oracle Database Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=ADMIN004).
3. Set `PLSQL_CODE_TYPE` to `NATIVE` in the compilation parameter file. If the database is using a server parameter file, then set this after the database has started.
	The value of `PLSQL_CODE_TYPE` does not affect the conversion of the PL/SQL units in these steps. However, it does affect all subsequently compiled units, so explicitly set it to the desired compilation type.
4. Start up the database in upgrade mode, using the `UPGRADE` option. For information about SQL\*Plus `STARTUP`, see [SQL\*Plus User's Guide and Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=SQPUG127).
5. Run this code to list the invalid PL/SQL units. You can save the output of the query for future reference with the SQL `SPOOL` statement:
	```
	-- To save the output of the query to a file:
	  SPOOL pre_update_invalid.log
	SELECT o.OWNER, o.OBJECT_NAME, o.OBJECT_TYPE 
	FROM DBA_OBJECTS o, DBA_PLSQL_OBJECT_SETTINGS s 
	WHERE o.OBJECT_NAME = s.NAME AND o.STATUS='INVALID';
	-- To stop spooling the output: SPOOL OFF
	```
	If any Oracle supplied units are invalid, try to validate them by recompiling them. For example:
	```
	ALTER PACKAGE SYS.DBMS_OUTPUT COMPILE BODY REUSE SETTINGS;
	```
	If the units cannot be validated, save the spooled log for future resolution and continue.
6. Run this query to determine how many objects are compiled `NATIVE` and `INTERPRETED` (to save the output, use the SQL `SPOOL` statement):
	```
	SELECT TYPE, PLSQL_CODE_TYPE, COUNT(*)
	FROM DBA_PLSQL_OBJECT_SETTINGS
	WHERE PLSQL_CODE_TYPE IS NOT NULL AND ORIGIN_CON_ID=SYS_CONTEXT('USERENV', 'CON_ID')
	GROUP BY TYPE, PLSQL_CODE_TYPE
	ORDER BY TYPE, PLSQL_CODE_TYPE;
	```
	Any objects with a `NULL` `plsql_code_type` are special internal objects and can be ignored.
7. Run the `$ORACLE_HOME/rdbms/admin/dbmsupgnv`.`sql` script as the user `SYS` to update the `plsql_code_type` setting to `NATIVE` in the dictionary tables for all PL/SQL units. This process also invalidates the units. Use `TRUE` with the script to exclude package specifications; `FALSE` to include the package specifications.
	This update must be done when the database is in `UPGRADE` mode. The script is guaranteed to complete successfully or rollback all the changes.
8. Shut down the database and restart in `NORMAL` mode.
9. Before you run the `utlrp`.`sql` script, Oracle recommends that no other sessions are connected to avoid possible problems. You can ensure this with this statement:
	```
	ALTER SYSTEM ENABLE RESTRICTED SESSION;
	```
10. Run the `$ORACLE_HOME/rdbms/admin/utlrp`.`sql` script as the user `SYS`. This script recompiles all the PL/SQL modules using a default degree of parallelism. See the comments in the script for information about setting the degree explicitly.
	If for any reason the script is terminated atypically, rerun the `utlrp`.`sql` script to recompile any remaining invalid PL/SQL modules.
11. After the compilation completes successfully, verify that there are no invalid PL/SQL units using the query in step [^1]. You can spool the output of the query to the `post_upgrade_invalid`.`log` file and compare the contents with the `pre_upgrade_invalid`.`log` file, if it was created previously.
12. Re-run the query in step [^2]. If recompiling with `dbmsupgnv`.`sql`, confirm that all PL/SQL units, except `TYPE` specifications and package specifications if excluded, are `NATIVE`. If recompiling with `dbmsupgin`.`sql`, confirm that all PL/SQL units are `INTERPRETED`.
13. Disable the restricted session mode for the database, then start the services that you previously shut down. To disable restricted session mode, use this statement:
	```
	ALTER SYSTEM DISABLE RESTRICTED SESSION;
	```

[^1]: Run this code to list the invalid PL/SQL units. You can save the output of the query for future reference with the SQL `SPOOL` statement:

```
-- To save the output of the query to a file:
  SPOOL pre_update_invalid.log
SELECT o.OWNER, o.OBJECT_NAME, o.OBJECT_TYPE 
FROM DBA_OBJECTS o, DBA_PLSQL_OBJECT_SETTINGS s 
WHERE o.OBJECT_NAME = s.NAME AND o.STATUS='INVALID';
-- To stop spooling the output: SPOOL OFF
```

If any Oracle supplied units are invalid, try to validate them by recompiling them. For example:

```
ALTER PACKAGE SYS.DBMS_OUTPUT COMPILE BODY REUSE SETTINGS;
```

If the units cannot be validated, save the spooled log for future resolution and continue.

[^2]: Run this query to determine how many objects are compiled `NATIVE` and `INTERPRETED` (to save the output, use the SQL `SPOOL` statement):

```
SELECT TYPE, PLSQL_CODE_TYPE, COUNT(*)
FROM DBA_PLSQL_OBJECT_SETTINGS
WHERE PLSQL_CODE_TYPE IS NOT NULL AND ORIGIN_CON_ID=SYS_CONTEXT('USERENV', 'CON_ID')
GROUP BY TYPE, PLSQL_CODE_TYPE
ORDER BY TYPE, PLSQL_CODE_TYPE;
```

Any objects with a `NULL` `plsql_code_type` are special internal objects and can be ignored.

[^undefined]: Run the `$ORACLE_HOME/rdbms/admin/dbmsupgnv`.`sql` script as the user `SYS` to update the `plsql_code_type` setting to `NATIVE` in the dictionary tables for all PL/SQL units. This process also invalidates the units. Use `TRUE` with the script to exclude package specifications; `FALSE` to include the package specifications.

This update must be done when the database is in `UPGRADE` mode. The script is guaranteed to complete successfully or rollback all the changes.

[^undefined]: Shut down the database and restart in `NORMAL` mode.

[^undefined]: Before you run the `utlrp`.`sql` script, Oracle recommends that no other sessions are connected to avoid possible problems. You can ensure this with this statement:

```
ALTER SYSTEM ENABLE RESTRICTED SESSION;
```

[^undefined]: Run the `$ORACLE_HOME/rdbms/admin/utlrp`.`sql` script as the user `SYS`. This script recompiles all the PL/SQL modules using a default degree of parallelism. See the comments in the script for information about setting the degree explicitly.

If for any reason the script is terminated atypically, rerun the `utlrp`.`sql` script to recompile any remaining invalid PL/SQL modules.

[^undefined]: After the compilation completes successfully, verify that there are no invalid PL/SQL units using the query in step 5. You can spool the output of the query to the `post_upgrade_invalid`.`log` file and compare the contents with the `pre_upgrade_invalid`.`log` file, if it was created previously.

[^undefined]: Re-run the query in step 6. If recompiling with `dbmsupgnv`.`sql`, confirm that all PL/SQL units, except `TYPE` specifications and package specifications if excluded, are `NATIVE`. If recompiling with `dbmsupgin`.`sql`, confirm that all PL/SQL units are `INTERPRETED`.

[^undefined]: Disable the restricted session mode for the database, then start the services that you previously shut down. To disable restricted session mode, use this statement:

```
ALTER SYSTEM DISABLE RESTRICTED SESSION;
```