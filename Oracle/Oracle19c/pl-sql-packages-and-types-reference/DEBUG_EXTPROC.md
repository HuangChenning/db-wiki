---
title: DEBUG_EXTPROC
book: PL/SQL Packages and Types Reference
doc_id: E96430-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/arpls/DEBUG_EXTPROC.html
tags:
  - oracle
  - 19c
  - pl-sql-packages-and-types-reference
---

The `DEBUG_EXTPROC` package enables you to start up the extproc agent within a session. This utility package can help you debug external procedures.

This chapter contains the following topics:

### DEBUG\_EXTPROC Security Model

Your Oracle account must have `EXECUTE` privileges on the package and `CREATE LIBRARY` privileges.

### DEBUG\_EXTPROC Operational Notes

These operational notes apply to `DEBUG_EXTPROC`.

To install the package, run the script `DBGEXTP`.`SQL`.

- Install/load this package in the Oracle USER where you want to debug the ‘extproc’ process.
- Ensure that you have execute privileges on package `DEBUG_EXTPROC`
```md
SELECT SUBSTR(OBJECT_NAME, 1, 20)
FROM USER_OBJECTS
WHERE OBJECT_NAME = 'DEBUG_EXTPROC';
```
- You can install this package as any other user, as long as you have `EXECUTE` privileges on the package.
	**Note:** These notes assumes that you built your shared library with debug symbols to aid in the debugging process. Please check the C compiler manual pages for the appropriate C compiler switches to build the shared library with debug symbols.

Having installed the package, proceed accordingly:

- Start a new Oracle session through SQL\*Plus or OCI program by connecting to `ORACLE`.
- Execute procedure `DEBUG_EXTPROC`.`STARTUP_EXTPROC_AGENT` to startup the extproc agent in this session; for example, execute `DEBUG_EXTPROC`.`STARTUP_EXTPROC_AGENT`; Do not exit this session, because that terminates the extproc agent.
- Determine the PID of the extproc agent that was started up for this session.
- Using a debugger (for example, gdb, dbx, or the native system debugger), load the extproc executable and attach to the running process.
- Set a breakpoint on function ‘pextproc’ and let the debugger continue with its execution.
- Now execute your external procedure in the same session where you first executed `DEBUG_EXTPROC`.`STARTUP_EXTPROC_AGENT`
- Your debugger should now break in function ‘pextproc’. At this point in time, the shared library referenced by your PL/SQL external function would have been loaded and the function resolved. Now set a breakpoint in your C function and let the debugger continue its execution.

Because PL/SQL loads the shared library at runtime, the debugger you use may or may not automatically be able to track the new symbols from the shared library. You may have to issue some debugger command to load the symbols (for example, ‘share’ in gdb)

- The debugger should now break in your C function. Its assumed that you had built the shared library with debugging symbols.
- Now proceed with your debugging.

### Rules and Limits

`DEBUG_EXTPROC` works only on platforms with debuggers that can attach to a running process.

### Summary of DEBUG\_EXTPROC Subprograms

The `STARTUP_EXTPROC_AGENT` procedure is the only `DEBUG_EXTPROC` subprogram.

Table 1 DEBUG\_EXTPROC Package Subprograms

| Subprogram | Description |
| --- | --- |
| STARTUP\_EXTPROC\_AGENT Procedure | Starts up the extproc agent process in the session |

### STARTUP\_EXTPROC\_AGENT Procedure

This procedure starts up the extproc agent process in the session. This enables you to get the PID of the executing process. This PID is needed to be able to attach to the running process using a debugger.

**Syntax**

```md
DEBUG_EXTPROC.STARTUP_EXTPROC_AGENT;
```