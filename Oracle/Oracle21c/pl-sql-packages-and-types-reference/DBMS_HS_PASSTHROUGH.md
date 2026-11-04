---
title: PL/SQL Packages and Types Reference
book: Database PL/SQL Packages and Types Reference
doc_id: F31492-25
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/arpls/DBMS_HS_PASSTHROUGH.html
tags:
  - oracle
  - 21c
  - pl-sql-packages-and-types-reference
---

## 91 DBMS\_HS\_PASSTHROUGH

The `DBMS_HS_PASSTHROUGH` PL/SQL package allows you to send a statement directly to a non-Oracle system without being interpreted by the Oracle server. This can be useful if the non-Oracle system allows operations in statements for which there is no equivalent in Oracle.

This chapter discusses the following topics:

- DBMS\_HS\_PASSTHROUGH Overview
- DBMS\_HS\_PASSTHROUGH Operational Notes
- Summary of DBMS\_HS\_PASSTHROUGH Subprograms
	See Also:
	[Oracle Database Heterogeneous Connectivity User's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=GUID-C9A8CC1A-ABB1-46F0-81C2-11C6014FC5DB) for more information about this package

### 91.1 DBMS\_HS\_PASSTHROUGH Overview

You can execute passthrough SQL statements directly at the non-Oracle system using the PL/SQL package `DBMS_HS_PASSTHROUGH`. Any statement executed with this package is executed in the same transaction as standard SQL statements.

See Also:

[Oracle Database Heterogeneous Connectivity User's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=DMCON001) for information about this package

### 91.2 DBMS\_HS\_PASSTHROUGH Operational Notes

The `DBMS_HS_PASSTHROUGH` package is a virtual package. It conceptually resides at the non-Oracle system. In reality, however, calls to this package are intercepted by Heterogeneous Services and mapped to one or more Heterogeneous Services calls. The driver, in turn, maps these Heterogeneous Services calls to the API of the non-Oracle system. The client application should invoke the procedures in the package through a database link in exactly the same way as it would invoke a non-Oracle system stored procedure. The special processing done by Heterogeneous Services is transparent to the user.

### 91.3 Summary of DBMS\_HS\_PASSTHROUGH Subprograms

This table lists the `DBMS_HS_PASSTHROUGH` subprograms and briefly describes them.

Table 91-1 DBMS\_HS\_PASSTHROUGH Package Subprograms

| Subprogram | Description |
| --- | --- |
| BIND\_INOUT\_VARIABLE Procedure | Binds `IN` `OUT` bind variables |
| BIND\_INOUT\_VARIABLE\_RAW Procedure | Binds `IN` `OUT` bind variables of datatype `RAW` |
| BIND\_OUT\_VARIABLE Procedure | Binds an `OUT` variable with a PL/SQL program variable |
| BIND\_OUT\_VARIABLE\_RAW Procedure | Binds an `OUT` variable of datatype `RAW` with a PL/SQL program variable |
| BIND\_VARIABLE Procedure | Binds an `IN` variable positionally with a PL/SQL program variable |
| BIND\_VARIABLE\_RAW Procedure | Binds `IN` variables of type `RAW` |
| [CLOSE\_CURSOR Procedure](https://docs.oracle.com/en/database/oracle/oracle-database/21/arpls/DBMS_HS_PASSTHROUGH.html#GUID-81AA6A32-E484-4FF0-8DA9-11B91EF7F683 "This function closes the cursor and releases associated memory after the SQL statement has been run at the non-Oracle system. If the cursor was not open, then the operation is a \"no operation\".") | Closes the cursor and releases associated memory after the SQL statement has been run at the non-Oracle system |
| EXECUTE\_IMMEDIATE Procedure | Runs a (non- `SELECT`) SQL statement immediately, without bind variables |
| EXECUTE\_NON\_QUERY Function | Runs a (non- `SELECT`) SQL statement |
| FETCH\_ROW Function | Fetches rows from a query |
| GET\_VALUE Procedure | Retrieves column value from `SELECT` statement, or retrieves `OUT` bind parameters |
| GET\_VALUE\_RAW Procedure | Similar to `GET_VALUE`, but for datatype `RAW` |
| OPEN\_CURSOR Function | Opens a cursor for running a passthrough SQL statement at the non-Oracle system |
| PARSE Procedure | Parses SQL statement at non-Oracle system |

#### 91.3.1 BIND\_INOUT\_VARIABLE Procedure

This procedure binds `IN` `OUT` bind variables.

Syntax

```
DBMS_HS_PASSTHROUGH.BIND_OUT_VARIABLE (
   c      IN  BINARY_INTEGER NOT NULL,
   p      IN  BINARY_INTEGER NULL,
   v      OUT <dty>,
   n      IN  VARCHAR2);
```

`<dty>` is either `DATE`, `NUMBER`, or `VARCHAR2`.

See Also:

For binding `OUT` variables of datatype `RAW`, see BIND\_OUT\_VARIABLE\_RAW Procedure.

Pragmas

```
Purity level defined : WNDS, RNDS
```

Parameters

Table 91-2 BIND\_INOUT\_VARIABLE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `c` | Cursor associated with the passthrough SQL statement. Cursor must be opened and parsed, using the routines `OPEN_CURSOR` and `PARSE` respectively. |
| `p` | Position of the bind variable in the SQL statement: Starts at 1. |
| `v` | This value is used for two purposes:  \- To provide the IN value before the SQL statement is run.  \- To determine the size of the out value. |
| `n` | (Optional) Name of the bind variable.  For example, in `SELECT * FROM emp WHERE ename=:ename`, the position of the bind variable:`ename` is 1, the name is:`ename`. This parameter can be used if the non-Oracle system supports "named binds" instead of positional binds. Passing the position is still required. |

Exceptions

Table 91-3 BIND\_INOUT\_VARIABLE Procedure Exceptions

| Exception | Description |
| --- | --- |
| `ORA-28550` | The cursor passed is invalid. |
| `ORA-28552` | Procedure is not run in right order. (Did you first open the cursor and parse the SQL statement?) |
| `ORA-28553` | The position of the bind variable is out of range. |
| `ORA-28555` | A `NULL` value was passed for a `NOT` `NULL` parameter. |

#### 91.3.2 BIND\_INOUT\_VARIABLE\_RAW Procedure

This procedure binds `IN` `OUT` bind variables of datatype `RAW`.

Syntax

```
DBMS_HS_PASSTHROUGH.BIND_INOUT_VARIABLE_RAW (
   c      IN     BINARY_INTEGER NOT NULL,
   p      IN     BINARY_INTEGER NOT NULL,
   v      IN OUT RAW,
   n      IN     VARCHAR2);
```

Pragmas

```
Purity level defined : WNDS, RNDS
```

Parameters

Table 91-4 BIND\_INOUT\_VARIABLE\_RAW Procedure Parameters

| Parameter | Description |
| --- | --- |
| `c` | Cursor associated with the passthrough SQL statement. Cursor must be opened and parsed using the routines `OPEN_CURSOR` and `PARSE` respectively. |
| `p` | Position of the bind variable in the SQL statement: Starts at 1. |
| `v` | This value is used for two purposes:  \- To provide the IN value before the SQL statement is run.  \- To determine the size of the out value. |
| `n` | (Optional) Name the bind variable.  For example, in `SELECT * FROM emp WHERE ename=:ename`, the position of the bind variable:`ename` is 1, the name is:`ename`. This parameter can be used if the non-Oracle system supports "named binds" instead of positional binds. Passing the position is still required. |

Exceptions

Table 91-5 BIND\_INOUT\_VARIABLE\_RAW Procedure Exceptions

| Exception | Description |
| --- | --- |
| `ORA-28550` | The cursor passed is invalid. |
| `ORA-28552` | Procedure is not run in right order. (Did you first open the cursor and parse the SQL statement?) |
| `ORA-28553` | The position of the bind variable is out of range. |
| `ORA-28555` | A `NULL` value was passed for a `NOT` `NULL` parameter. |

#### 91.3.3 BIND\_OUT\_VARIABLE Procedure

This procedure binds an `OUT` variable with a PL/SQL program variable.

Syntax

```
DBMS_HS_PASSTHROUGH.BIND_OUT_VARIABLE (
   c      IN  BINARY_INTEGER NOT NULL,
   p      IN  BINARY_INTEGER NULL,
   v      OUT <dty>,
   n      IN  VARCHAR2);
```

`<dty>` is either `DATE`, `NUMBER`, or `VARCHAR2`.

See Also:

For binding `OUT` variables of datatype `RAW`, see BIND\_OUT\_VARIABLE\_RAW Procedure.

Pragmas

```
Purity level defined : WNDS, RNDS
```

Parameters

Table 91-6 BIND\_OUT\_VARIABLE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `c` | Cursor associated with the passthrough SQL statement. Cursor must be opened and parsed, using the routines `OPEN_CURSOR` and `PARSE` respectively. |
| `p` | Position of the bind variable in the SQL statement: Starts at 1. |
| `v` | Variable in which the `OUT` bind variable stores its value. The package remembers only the "size" of the variable. After the SQL statement is run, you can use `GET_VALUE` to retrieve the value of the `OUT` parameter. The size of the retrieved value should not exceed the size of the parameter that was passed using `BIND_OUT_VARIABLE`. |
| `n` | (Optional) Name of the bind variable.  For example, in `SELECT * FROM emp WHERE ename=:ename`, the position of the bind variable:`ename` is 1, the name is:`ename`. This parameter can be used if the non-Oracle system supports "named binds" instead of positional binds. Passing the position is still required. |

Exceptions

Table 91-7 BIND\_OUT\_VARIABLE Procedure Exceptions

| Exception | Description |
| --- | --- |
| `ORA-28550` | The cursor passed is invalid. |
| `ORA-28552` | Procedure is not run in right order. (Did you first open the cursor and parse the SQL statement?) |
| `ORA-28553` | The position of the bind variable is out of range. |
| `ORA-28555` | A `NULL` value was passed for a `NOT` `NULL` parameter. |

#### 91.3.4 BIND\_OUT\_VARIABLE\_RAW Procedure

This procedure binds an `OUT` variable of datatype `RAW` with a PL/SQL program variable.

Syntax

```
DBMS_HS_PASSTHROUGH.BIND_OUT_VARIABLE_RAW (
   c     IN  BINARY_INTEGER NOT NULL,
   p     IN  BINARY_INTEGER NOT NULL,
   v     OUT RAW,
   n     IN  VARCHAR2);
```

Pragmas

```
Purity level defined : WNDS, RNDS
```

Parameters

Table 91-8 BIND\_OUT\_VARIABLE\_RAW Procedure Parameters

| Parameter | Description |
| --- | --- |
| `c` | Cursor associated with the passthrough SQL statement. Cursor must be opened and parsed, using the routines `OPEN_CURSOR` and `PARSE` respectively. |
| `p` | Position of the bind variable in the SQL statement: Starts at 1. |
| `v` | Variable in which the `OUT` bind variable stores its value. The package remembers only the "size" of the variable. After the SQL statement is run, you can use `GET_VALUE` to retrieve the value of the `OUT` parameter. The size of the retrieved value should not exceed the size of the parameter that was passed using `BIND_OUT_VARIABLE_RAW`. |
| `n` | (Optional) Name of the bind variable.  For example, in `SELECT * FROM emp WHERE ename=:ename`, the position of the bind variable:`ename` is 1, the name is:`ename`. This parameter can be used if the non-Oracle system supports "named binds" instead of positional binds. Passing the position is still required. |

Exceptions

Table 91-9 BIND\_OUT\_VARIABLE\_RAW Procedure Exceptions

| Exception | Description |
| --- | --- |
| `ORA-28550` | The cursor passed is invalid. |
| `ORA-28552` | Procedure is not run in right order. (Did you first open the cursor and parse the SQL statement?) |
| `ORA-28553` | The position of the bind variable is out of range. |
| `ORA-28555` | A `NULL` value was passed for a `NOT` `NULL` parameter. |

#### 91.3.5 BIND\_VARIABLE Procedure

This procedure binds an `IN` variable positionally with a PL/SQL program variable.

Syntax

```
DBMS_HS_PASSTHROUGH.BIND_VARIABLE (
   c      IN BINARY_INTEGER NOT NULL,
   p      IN BINARY_INTEGER NOT NULL,
   v      IN <dty>,
   n      IN VARCHAR2);
```

`<dty>` is either `DATE`, `NUMBER`, or `VARCHAR2`.

See Also:

To bind `RAW` variables use BIND\_VARIABLE\_RAW Procedure.

Pragmas

```
Purity level defined: WNDS, RNDS
```

Parameters

Table 91-10 BIND\_VARIABLE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `c` | Cursor associated with the passthrough SQL statement. Cursor must be opened and parsed using the routines `OPEN_CURSOR` and `PARSE` respectively. |
| `p` | Position of the bind variable in the SQL statement: Starts at 1. |
| `v` | Value that must be passed to the bind variable name. |
| `n` | (Optional) Name of the bind variable.  For example, in `SELECT * FROM emp WHERE ename=:ename`, the position of the bind variable:`ename` is 1, the name is:`ename`. This parameter can be used if the non-Oracle system supports "named binds" instead of positional binds. Passing the position is still required. |

Exceptions

Table 91-11 BIND\_VARIABLE Procedure Exceptions

| Exception | Description |
| --- | --- |
| `ORA-28550` | The cursor passed is invalid. |
| `ORA-28552` | Procedure is not run in right order. (Did you first open the cursor and parse the SQL statement?) |
| `ORA-28553` | The position of the bind variable is out of range. |
| `ORA-28555` | A `NULL` value was passed for a `NOT` `NULL` parameter. |

#### 91.3.6 BIND\_VARIABLE\_RAW Procedure

This procedure binds `IN` variables of type `RAW`.

Syntax

```
DBMS_HS_PASSTHROUGH.BIND_VARIABLE_RAW (
   c    IN BINARY_INTEGER NOT NULL,
   p    IN BINARY_INTEGER NOT NULL,
   v    IN RAW,  
   n    IN VARCHAR2);
```

Pragmas

```
Purity level defined : WNDS, RNDS
```

Parameters

Table 91-12 BIND\_VARIABLE\_RAW Procedure Parameters

| Parameter | Description |
| --- | --- |
| `c` | Cursor associated with the passthrough SQL statement. Cursor must be opened and parsed, using the routines `OPEN_CURSOR` and `PARSE` respectively. |
| `p` | Position of the bind variable in the SQL statement: Starts at 1. |
| `v` | Value that must be passed to the bind variable. |
| `n` | (Optional) Name of the bind variable.  For example, in `SELECT * FROM emp WHERE ename=:ename`, the position of the bind variable:`ename` is 1, the name is:`ename`. This parameter can be used if the non-Oracle system supports "named binds" instead of positional binds. Passing the position is still required. |

Exceptions

Table 91-13 BIND\_VARIABLE\_RAW Procedure Exceptions

| Exception | Description |
| --- | --- |
| `ORA-28550` | The cursor passed is invalid. |
| `ORA-28552` | Procedure is not run in right order. (Did you first open the cursor and parse the SQL statement?) |
| `ORA-28553` | The position of the bind variable is out of range. |
| `ORA-28555` | A `NULL` value was passed for a `NOT` `NULL` parameter. |

#### 91.3.7 CLOSE\_CURSOR Procedure

This function closes the cursor and releases associated memory after the SQL statement has been run at the non-Oracle system. If the cursor was not open, then the operation is a "no operation".

Syntax

```
DBMS_HS_PASSTHROUGH.CLOSE_CURSOR (
   c IN BINARY_INTEGER NOT NULL);
```

Pragmas

```
Purity level defined : WNDS, RNDS
```

Parameters

Table 91-14 CLOSE\_CURSOR Procedure Parameters

| Parameter | Description |
| --- | --- |
| `c` | Cursor to be released. |

Exceptions

Table 91-15 CLOSE\_CURSOR Procedure Exceptions

| Exception | Description |
| --- | --- |
| `ORA-28555` | A `NULL` value was passed for a `NOT` `NULL` parameter. |

#### 91.3.8 EXECUTE\_IMMEDIATE Procedure

This function runs a SQL statement immediately. Any valid SQL command except `SELECT` can be run immediately.

The statement must not contain any bind variables. The statement is passed in as a `VARCHAR2` in the argument. Internally the SQL statement is run using the `PASSTHROUGH` SQL protocol sequence of `OPEN_CURSOR`, `PARSE`, `EXECUTE_NON_QUERY`, `CLOSE_CURSOR`.

Syntax

```
DBMS_HS_PASSTHROUGH.EXECUTE_IMMEDIATE ( 
   s IN VARCHAR2 NOT NULL)  
RETURN BINARY_INTEGER;
```

Parameters

Table 91-16 EXECUTE\_IMMEDIATE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `s` | `VARCHAR2` variable with the statement to be executed immediately. |

Return Values

The number of rows affected by the execution of the SQL statement.

Exceptions

Table 91-17 EXECUTE\_IMMEDIATE Procedure Exceptions

| Exception | Description |
| --- | --- |
| `ORA-28551` | SQL statement is invalid. |
| `ORA-28554` | Max open cursors. |
| `ORA-28555` | A `NULL` value was passed for a `NOT` `NULL` parameter. |

#### 91.3.9 EXECUTE\_NON\_QUERY Function

This function runs a SQL statement. The SQL statement cannot be a `SELECT` statement. A cursor has to be open and the SQL statement has to be parsed before the SQL statement can be run.

Syntax

```
DBMS_HS_PASSTHROUGH.EXECUTE_NON_QUERY ( 
   c IN BINARY_INTEGER NOT NULL)
  RETURN BINARY_INTEGER;
```

Parameters

Table 91-18 EXECUTE\_NON\_QUERY Function Parameters

| Parameter | Description |
| --- | --- |
| `c` | Cursor associated with the passthrough SQL statement. Cursor must be opened and parsed, using the routines `OPEN_CURSOR` and `PARSE` respectively. |

Return Values

The number of rows affected by the SQL statement in the non-Oracle system

Exceptions

Table 91-19 EXECUTE\_NON\_QUERY Function Exceptions

| Exception | Description |
| --- | --- |
| `ORA-28550` | The cursor passed is invalid. |
| `ORA-28552` | Procedure is not run in right order. (Did you first open the cursor and parse the SQL statement?) |
| `ORA-28555` | A `NULL` value was passed for a `NOT` `NULL` parameter. |

#### 91.3.10 FETCH\_ROW Function

This function fetches rows from a result set.

The result set is defined with a SQL `SELECT` statement. When there are no more rows to be fetched, the exception `NO_DATA_FOUND` is raised. Before the rows can be fetched, a cursor has to be opened, and the SQL statement has to be parsed.

Syntax

```
DBMS_HS_PASSTHROUGH.FETCH_ROW (
   c   IN BINARY_INTEGER NOT NULL,
   f   IN BOOLEAN)
  RETURN BINARY_INTEGER;
```

Pragmas

```
Purity level defined : WNDS
```

Parameters

Table 91-20 FETCH\_ROW Function Parameters

| Parameter | Description |
| --- | --- |
| `c` | Cursor associated with the passthrough SQL statement. Cursor must be opened and parsed, using the routines `OPEN_CURSOR` and `PARSE` respectively. |
| `first` | (Optional) Reexecutes `SELECT` statement. Possible values:  `- TRUE`: reexecute `SELECT` statement.  `- FALSE`: fetch the next row, or if run for the first time, then execute and fetch rows (default). |

Return Values

The returns the number of rows fetched. The function returns "0" if the last row was already fetched.

Exceptions

Table 91-21 FETCH\_ROW Function Exceptions

| Exception | Description |
| --- | --- |
| `ORA-28550` | The cursor passed is invalid. |
| `ORA-28552` | Procedure is not run in right order. (Did you first open the cursor and parse the SQL statement?) |
| `ORA-28555` | A `NULL` value was passed for a `NOT` `NULL` parameter. |

#### 91.3.11 GET\_VALUE Procedure

This procedure has two purposes: it retrieves the select list items of `SELECT` statements after a row has been fetched, and it retrieves the `OUT` bind values, after the SQL statement has been run.

Syntax

```
DBMS_HS_PASSTHROUGH.GET_VALUE (
   c      IN  BINARY_INTEGER NOT NULL,
   p    IN  BINARY_INTEGER NOT NULL,
   v    OUT <dty>);
```

`<dty>` is either `DATE`, `NUMBER`, or `VARCHAR2`.

See Also:

For retrieving values of datatype `RAW`, see GET\_VALUE\_RAW Procedure.

Pragmas

```
Purity level defined : WNDS
```

Parameters

Table 91-22 GET\_VALUE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `c` | Cursor associated with the passthrough SQL statement. Cursor must be opened and parsed, using the routines `OPEN_CURSOR` and `PARSE` respectively. |
| `p` | Position of the bind variable or select list item in the SQL statement: Starts at 1. |
| `v` | Variable in which the `OUT` bind variable or select list item stores its value. |

Exceptions

Table 91-23 GET\_VALUE Procedure Exceptions

| Exception | Description |
| --- | --- |
| `ORA-1403` | Returns `NO_DATA_FOUND` exception when running the `GET_VALUE` after the last row was fetched (that is, `FETCH_ROW` returned "0"). |
| `ORA-28550` | The cursor passed is invalid. |
| `ORA-28552` | Procedure is not run in right order. (Did you first open the cursor and parse the SQL statement?) |
| `ORA-28553` | The position of the bind variable is out of range. |
| `ORA-28555` | A `NULL` value was passed for a `NOT` `NULL` parameter. |

#### 91.3.12 GET\_VALUE\_RAW Procedure

This procedure is similar to `GET_VALUE`, but for datatype `RAW`.

Syntax

```
DBMS_HS_PASSTHROUGH.GET_VALUE_RAW (
   c    IN  BINARY_INTEGER NOT NULL,
   p    IN  BINARY_INTEGER NOT NULL,
   v    OUT RAW);
```

Pragmas

```
Purity level defined : WNDS
```

Parameters

Table 91-24 GET\_VALUE\_RAW Procedure Parameters

| Parameter | Description |
| --- | --- |
| `c` | Cursor associated with the passthrough SQL statement. Cursor must be opened and parsed, using the routines `OPEN_CURSOR` and `PARSE` respectively. |
| `p` | Position of the bind variable or select list item in the SQL statement: Starts at 1. |
| `v` | Variable in which the `OUT` bind variable or select list item stores its value. |

Exceptions

Table 91-25 GET\_VALUE\_RAW Procedure Exceptions

| Exception | Description |
| --- | --- |
| `ORA-1403` | Returns `NO_DATA_FOUND` exception when running the `GET_VALUE` after the last row was fetched (that is, `FETCH_ROW` returned "0"). |
| `ORA-28550` | The cursor passed is invalid. |
| `ORA-28552` | Procedure is not run in right order. (Did you first open the cursor and parse the SQL statement?) |
| `ORA-28553` | The position of the bind variable is out of range. |
| `ORA-28555` | A `NULL` value was passed for a `NOT` `NULL` parameter. |

#### 91.3.13 OPEN\_CURSOR Function

This function opens a cursor for running a passthrough SQL statement at the non-Oracle system. This function must be called for any type of SQL statement.

The function returns a cursor, which must be used in subsequent calls. This call allocates memory. To deallocate the associated memory, call the procedure `CLOSE_CURSOR`.

Syntax

```
DBMS_HS_PASSTHROUGH.OPEN_CURSOR 
  RETURN BINARY_INTEGER;
```

Pragmas

```
Purity level defined : WNDS, RNDS
```

Return Values

The cursor to be used on subsequent procedure and function calls.

Exceptions

Table 91-26 OPEN\_CURSOR Function Exceptions

| Exception | Description |
| --- | --- |
| `ORA-28554` | Maximum number of open cursor has been exceeded. Increase Heterogeneous Services' `OPEN_CURSORS` initialization parameter. |

#### 91.3.14 PARSE Procedure

This procedure parses an SQL statement at a non-Oracle system.

Syntax

```
DBMS_HS_PASSTHROUGH.PARSE (
   c       IN  BINARY_INTEGER NOT NULL,
   stmt    IN  VARCHAR2 NOT NULL);
```

Pragmas

```
Purity level defined : WNDS, RNDS
```

Parameters

Table 91-27 PARSE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `c` | Cursor associated with the passthrough SQL statement. Cursor must be opened using function `OPEN_CURSOR`. |
| `stmt` | Statement to be parsed. |

Exceptions

Table 91-28 PARSE Procedure Exceptions

| Exception | Description |
| --- | --- |
| `ORA-28550` | The cursor passed is invalid. |
| `ORA-28551` | SQL statement is illegal. |
| `ORA-28555` | A `NULL` value was passed for a `NOT` `NULL` parameter. |