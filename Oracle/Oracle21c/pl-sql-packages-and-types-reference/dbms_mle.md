---
title: PL/SQL Packages and Types Reference
book: Database PL/SQL Packages and Types Reference
doc_id: F31492-25
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/arpls/dbms_mle.html
tags:
  - oracle
  - 21c
  - pl-sql-packages-and-types-reference
---

## 117 DBMS\_MLE

The `DBMS_MLE` package allows users to execute JavaScript code inside the Oracle Database and exchange data seamlessly between PL/SQL and JavaScript. The JavaScript code itself can execute PL/SQL and SQL through built-in JavaScript modules. JavaScript data types are automatically mapped to Oracle Database data types and vice versa.

With the `DBMS_MLE` package, developers can write their data processing logic in JavaScript.

This chapter contains the following topics:

### 117.1 DBMS\_MLE Overview

Runtime state for MLE execution is encapsulated in execution contexts that users can explicitly create and destroy. Users can also export values from PL/SQL to MLE, and import values from MLE back into PL/SQL.

The following example captures the typical workflow for MLE execution:

```
set serveroutput on;
declare
  ctx dbms_mle.context_handle_t;
  source clob;
  greeting varchar2(100);
begin
  ctx := dbms_mle.create_context(); -- Create execution context for MLE execution
  dbms_mle.export_to_mle(ctx, 'person', 'World'); -- Export value from PL/SQL
  source := q'~
    var bindings = require("mle-js-bindings");
    var person = bindings.importValue("person"); // Import value previously exported from PL/SQL
    var greeting = "Hello, " + person + "!";
    bindings.exportValue("greeting", greeting); // Export value to PL/SQL
  ~';
  dbms_mle.eval(ctx, 'JAVASCRIPT', source); -- Evaluate the source code snippet in the execution context
  dbms_mle.import_from_mle(ctx, 'greeting', greeting); -- Import value previously exported from MLE
  dbms_output.put_line('Greetings from MLE: ' || greeting);
  dbms_mle.drop_context(ctx); -- Drop the execution context once no longer required
end;
/
```

Executing the above code block produces the following output:

```
Greetings from MLE: Hello, World!
```

### 117.2 DBMS\_MLE Security Model

Access to MLE features is protected by database privileges. The user must have the `EXECUTE DYNAMIC MLE` privilege while calling any of its functions and procedures that pertain to MLE execution. In addition to this, the user must also have the `EXECUTE` privilege on an MLE language (for example, `EXECUTE ON       JAVASCRIPT`) to execute code in that language. An `ORA-01031` error is raised if the user calling any of the `DBMS_MLE` subprograms does not have the appropriate privileges. See the summary of `DBMS_MLE` subprograms for the privileges required to call each `DBMS_MLE` subprogram.

### 117.3 Summary of DBMS\_MLE Subprograms

This table lists the `DBMS_MLE` subprograms and briefly describes them.

Table 117-1 DBMS\_MLE Package Subprograms

| Subprogram | Description |
| --- | --- |
| CREATE\_CONTEXT Function | Creates an MLE context for executing snippets in any MLE language. |
| DISABLE\_CTX\_STDERR Procedure | This procedure disables stderr stream of the specified MLE context, so that future writes to stderr are discarded. |
| DISABLE\_CTX\_STDOUT Procedure | This procedure disables stdout stream of the specified MLE context, so that future writes to `stdout` are discarded. |
| DISABLE\_STDERR Procedure | This procedure disables the stderr stream of all MLE contexts, so that future writes to `stderr` are discarded. |
| DISABLE\_STDOUT Procedure | This procedure disables the stdout stream of all MLE contexts, so that future writes to stdout are discarded. |
| DROP\_CONTEXT Procedure | This procedure is used to drop an MLE context that was previously created using the `CREATE_CONTEXT` procedure. After the context is dropped, the context handle is no longer valid and cannot be used anymore. |
| EVAL Procedure | This procedure executes the given MLE language code within the context identified by the context handle. |
| EXPORT\_TO\_MLE Procedure | This procedure allows you to assign the given value, with appropriate conversion, to the named property in the MLE context. The property is created if it is not already present. |
| GET\_AVAILABLE\_LANGUAGES Function | This function returns the set of available MLE languages. |
| GET\_CTX\_ERROR\_STACK Function | This function retrieves the MLE language stack trace for the most recent application error in the given execution context. |
| IMPORT\_FROM\_MLE Procedure | This procedure retrieves the value of the named property from the MLE context and converts it to the requested PL/SQL type. |
| SET\_CTX\_STDERR Procedure | This procedure redirects the stderr stream of the MLE context to the given `CLOB`. |
| SET\_CTX\_STDERR\_TO\_DBMS\_OUTPUT Procedure | This procedure redirects the stderr stream of the MLE context to `DBMS_OUTPUT`. |
| SET\_CTX\_STDOUT Procedure | This procedure redirects the stdout stream of the MLE context to the given `CLOB`. |
| SET\_CTX\_STDOUT\_TO\_DBMS\_OUTPUT Procedure | This procedure redirects the stdout stream of the MLE context to `DBMS_OUTPUT`. |
| SET\_STDERR Procedure | This procedure redirects the stderr stream of all MLE contexts to the given `CLOB`. |
| SET\_STDERR\_TO\_DBMS\_OUTPUT Procedure | This procedure redirects the stderr stream of all MLE contexts to `DBMS_OUTPUT`. |
| SET\_STDOUT Procedure | This procedure redirects the stdout stream of all MLE contexts to the given `CLOB`. |
| SET\_STDOUT\_TO\_DBMS\_OUTPUT Procedure | This procedure redirects the stdout stream of all MLE contexts to `DBMS_OUTPUT`. |

#### 117.3.1 CREATE\_CONTEXT Function

Creates an MLE context for executing snippets in any MLE language. You need the `EXECUTE DYNAMIC MLE` privilege to execute this function.

Syntax

```
DBMS_MLE.CREATE_CONTEXT
 RETURN CONTEXT_HANDLE_T;
```

Return Values

This function returns a handle that uniquely identifies a context within a session for use in subsequent operations, such as `EXPORT_TO_MLE` and `EVAL`.

Usage Notes

A context has a lifetime limited to the session in which it was created. When a client session is terminated, all its contexts are dropped. All MLE contexts created in a session are also dropped when the session state is reset, for example, by calling `DBMS_SESSION.RESET_PACKAGE`. MLE language code is evaluated in the context using the user, roles, and schema that are in effect at the time of context creation.

The procedure may raise the `ORA-01031` error if the caller does not have sufficient privileges.

#### 117.3.2 DISABLE\_CTX\_STDERR Procedure

This procedure disables `stderr` stream of the specified MLE context, so that future writes to `stderr` are discarded. You need the `EXECUTE DYNAMIC MLE` privilege to execute this function.

Syntax

```
DBMS_MLE.DISABLE_CTX_STDERR(
      context_handle            IN            context_handle_t);
```

Parameters

Table 117-2 DISABLE\_CTX\_STDERR Procedure Parameters

| Parameter | Description |
| --- | --- |
| `context_handle` | The handle to an MLE context in the current session. |

Usage Notes

Any output that was buffered so far gets flushed to the pre-existing sink.

The procedure may raise the following errors:
- `ORA-01031`: if the caller does not have sufficient privileges

#### 117.3.3 DISABLE\_CTX\_STDOUT Procedure

This procedure disables `stdout` stream of the specified MLE context, so that future writes to `stdout` are discarded. You need the `EXECUTE DYNAMIC MLE` privilege to execute this function.

Syntax

```
DBMS_MLE.DISABLE_CTX_STDOUT(
      context_handle            IN            context_handle_t);
```

Parameters

Table 117-3 DISABLE\_CTX\_STDOUT Procedure Parameters

| Parameter | Description |
| --- | --- |
| `context_handle` | The handle to an MLE context in the current session. |

Usage Notes

Any output that was buffered so far gets flushed to the pre-existing sink.

The procedure may raise the following errors:
- `ORA-01031`: if the caller does not have sufficient privileges

#### 117.3.4 DISABLE\_STDERR Procedure

This procedure disables the `stderr` stream of all MLE contexts, so that future writes to `stderr` are discarded. This applies to all existing contexts and contexts created in the future. You need the `EXECUTE DYNAMIC MLE` privilege to execute this function.

Syntax

```
DBMS_MLE.DISABLE_STDERR();
```

Usage Notes

Any output that was buffered so far gets flushed to the pre-existing sink.

The procedure may raise the following errors:
- `ORA-01031`: if the caller does not have sufficient privileges

#### 117.3.5 DISABLE\_STDOUT Procedure

This procedure disables the stdout stream of all MLE contexts, so that future writes to `stdout` are discarded. This applies to all existing contexts and contexts created in the future. You need the `EXECUTE DYNAMIC MLE` privilege to execute this function.

Syntax

```
DBMS_MLE.DISABLE_STDOUT();
```

Usage Notes

Any output that was buffered so far gets flushed to the pre-existing sink.

The procedure may raise the following errors:
- `ORA-01031`: if the caller does not have sufficient privileges

#### 117.3.6 DROP\_CONTEXT Procedure

This procedure is used to drop an MLE context that was previously created using the `CREATE_CONTEXT` function. After the context is dropped, the context handle is no longer valid and cannot be used anymore. You need the `EXECUTE DYNAMIC MLE` privilege to execute this procedure.

Syntax

```
DBMS_MLE.DROP_CONTEXT(
   context_handle   IN      context_handle_t);
```

Parameters

Table 117-4 DROP\_CONTEXT Procedure Parameters

| Parameter | Description |
| --- | --- |
| `context_handle` | The handle to an MLE context in the current session. |

Usage Notes

The procedure may raise `ORA-01031` error if the caller does not have sufficient privileges.

#### 117.3.7 EVAL Procedure

This procedure executes the given MLE language code within the context identified by the context handle.

The evaluated code has access to all previous modifications to the state of the context, including variables defined by code previously evaluated in the context and values exported through `EXPORT_TO_MLE()`. The evaluated code can also import MLE built-in modules such as the MLE SQL driver.

You need the `EXECUTE DYNAMIC MLE` privilege to execute this procedure. It also requires the `EXECUTE` privilege for the given language, for example, `EXECUTE ON JAVASCRIPT`.

Syntax

```
DBMS_MLE.EVAL(
   context_handle   IN         context_handle_t,
   language_id      IN         language_t,
   source           IN         CLOB,
   result           IN OUT     NOCOPY CLOB CHARACTER SET ANY_CS);

DBMS_MLE.EVAL(
   context_handle   IN         context_handle_t,
   language_id      IN         language_t,
   source           IN         VARCHAR2,
   result           IN OUT     NOCOPY CLOB CHARACTER SET ANY_CS);

DBMS_MLE.EVAL(
   context_handle   IN         context_handle_t,
   language_id      IN         language_t,
   source           IN         CLOB);

DBMS_MLE.EVAL(
   context_handle   IN         context_handle_t,
   language_id      IN         language_t,
   source           IN         VARCHAR2);
```

Parameters

Table 117-5 EVAL Procedure Parameters

| Parameter | Description |
| --- | --- |
| `context_handle` | The handle to an MLE context. |
| `language_id` | The language of the provided source code. For example, JavaScript. |
| `source` | The source code to be executed. |
| `result` | A non-NULL buffer to which the result of the evaluation of the source code is appended. |

Usage Notes

The procedure may raise the following errors:
- `ORA-01031`: if the caller does not have sufficient privileges
- `ORA-04108`: if the current container, the current user, or the currently enabled roles are different from those in effect at the time of context creation.

#### 117.3.8 EXPORT\_TO\_MLE Procedure

This procedure allows you to assign the given value, with appropriate conversion, to the named property in the MLE context. The property is created if it is not already present. You need the `EXECUTE DYNAMIC MLE` privilege to execute this function.

Syntax

```
DBMS_MLE.EXPORT_TO_MLE (
   context_handle   IN      context_handle_t,
   property_name    IN      VARCHAR2,
   property_value   IN      BINARY_INTEGER);

DBMS_MLE.EXPORT_TO_MLE (
   context_handle   IN      context_handle_t,
   property_name    IN      VARCHAR2,
   property_value   IN      BINARY_DOUBLE);

DBMS_MLE.EXPORT_TO_MLE (
   context_handle   IN      context_handle_t,
   property_name    IN      VARCHAR2,
   property_value   IN      BINARY_FLOAT);

DBMS_MLE.EXPORT_TO_MLE (
   context_handle   IN      context_handle_t,
   property_name    IN      VARCHAR2,
   property_value   IN      BLOB);

DBMS_MLE.EXPORT_TO_MLE (
   context_handle   IN      context_handle_t,
   property_name    IN      VARCHAR2,
   property_value   IN      BOOLEAN);

DBMS_MLE.EXPORT_TO_MLE (
   context_handle   IN      context_handle_t,
   property_name    IN      VARCHAR2,
   property_value   IN      CLOB CHARACTER SET ANY_CS);

DBMS_MLE.EXPORT_TO_MLE (
   context_handle   IN      context_handle_t,
   property_name    IN      VARCHAR2,
   property_value   IN      DATE);

DBMS_MLE.EXPORT_TO_MLE (
   context_handle   IN      context_handle_t,
   property_name   IN      VARCHAR2,
   property_value   IN      DSINTERVAL_UNCONSTRAINED);

DBMS_MLE.EXPORT_TO_MLE (
   context_handle   IN      context_handle_t,
   property_name   IN      VARCHAR2,
   property_value   IN      NUMBER);

DBMS_MLE.EXPORT_TO_MLE (
   context_handle   IN      context_handle_t,
   property_name   IN      VARCHAR2,
   property_value   IN      TIMESTAMP_TZ_UNCONSTRAINED);

DBMS_MLE.EXPORT_TO_MLE (
   context_handle   IN      context_handle_t,
   property_name   IN      VARCHAR2,
   property_value   IN      TIMESTAMP_UNCONSTRAINED);

DBMS_MLE.EXPORT_UROWID (
   context_handle   IN      context_handle_t,
   property_name   IN      VARCHAR2,
   property_value   IN      UROWID);

DBMS_MLE.EXPORT_TO_MLE (
   context_handle   IN      context_handle_t,
   property_name   IN      VARCHAR2,
   property_value   IN      VARCHAR2 CHARACTER SET ANY_CS);

DBMS_MLE.EXPORT_TO_MLE (
   context_handle   IN      context_handle_t,
   property_name   IN      VARCHAR2,
   property_value   IN      YMINTERVAL_UNCONSTRAINED);

DBMS_MLE.EXPORT_CHAR (
   context_handle   IN      context_handle_t,
   property_name   IN      VARCHAR2,
   property_value   IN      CHAR CHARACTER SET ANY_CS);

DBMS_MLE.EXPORT_RAW (
   context_handle   IN      context_handle_t,
   property_name   IN      VARCHAR2,
   property_value   IN      RAW);
```

Parameters

Table 117-6 EXPORT\_TO\_MLE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `context_handle` | The handle to an MLE context in the current session. |
| `property_name` | The name of the variable to be set. If the `property_name` value is `NULL` or an empty string, `ORA-04157` error is thrown. |
| `property_value` | The value to which the variable should be set. |

Usage Notes

The procedure may raise the following errors:
- `ORA-01031`: if the caller does not have sufficient privileges.
- `ORA-04157`: if the value of the passed property\_name is `NULL` or an empty string.
- `ORA-04108`: if the current container, the current user, or the currently enabled roles are different from those in effect at the time of context creation.

#### 117.3.9 GET\_AVAILABLE\_LANGUAGES Function

This function returns the set of available MLE languages.

Syntax

```
DBMS_MLE.GET_AVAILABLE_LANGUAGES()
  RETURN languages_t;
```

Return Values

A set of available MLE languages as a table of language identifiers as they can be used as an argument to `DBMS_MLE.EVAL()`.

#### 117.3.10 GET\_CTX\_ERROR\_STACK Function

This function retrieves the MLE language stack trace for the most recent application error in the given execution context. You need the `EXECUTE DYNAMIC                   MLE` privilege to execute this function.

Syntax

```
DBMS_MLE.GET_CTX_ERROR_STACK(
      context_handle            IN            context_handle_t)
RETURN error_frames_t;
```

Parameters

Table 117-7 GET\_CTX\_ERROR\_STACK Function Parameters

| Parameter | Description |
| --- | --- |
| `context_handle` | The handle to an MLE context in the current session. |

Return Values

A collection of error stack frames, each of type error\_frame\_t. An empty collection is returned if there is no error stack to report.

Usage Notes

The Function may raise the following errors:
- `ORA-01031`: if the caller does not have sufficient privileges

#### 117.3.11 IMPORT\_FROM\_MLE Procedure

This procedure retrieves the value of the named property from the MLE context and converts it to the requested PL/SQL type. You need the `EXECUTE DYNAMIC          MLE` privilege to execute this procedure.

Syntax

```
DBMS_MLE.IMPORT_FROM_MLE (
   context_handle   IN      context_handle_t,
   property_name    IN      VARCHAR2,
   target           OUT     NOCOPY BINARY_INTEGER);

DBMS_MLE.IMPORT_FROM_MLE (
   context_handle   IN      context_handle_t,
   property_name    IN      VARCHAR2,
   target           OUT     NOCOPY BINARY_DOUBLE);

DBMS_MLE.IMPORT_FROM_MLE (
   context_handle   IN      context_handle_t,
   property_name    IN      VARCHAR2,
   target           OUT     NOCOPY BINARY_FLOAT);

DBMS_MLE.IMPORT_FROM_MLE (
   context_handle   IN      context_handle_t,
   property_name    IN      VARCHAR2,
   target           OUT     NOCOPY BLOB);

DBMS_MLE.IMPORT_FROM_MLE (
   context_handle   IN      context_handle_t,
   property_name    IN      VARCHAR2,
   target           OUT     NOCOPY BOOLEAN);

DBMS_MLE.IMPORT_FROM_MLE (
   context_handle   IN      context_handle_t,
   property_name    IN      VARCHAR2,
   target           OUT     NOCOPY CLOB CHARACTER SET ANY_CS);

DBMS_MLE.IMPORT_FROM_MLE (
   context_handle   IN      context_handle_t,
   property_name    IN      VARCHAR2,
   target           OUT     NOCOPY DATE);

DBMS_MLE.IMPORT_FROM_MLE (
   context_handle   IN      context_handle_t,
   property_name    IN      VARCHAR2,
   target           OUT     NOCOPY DSINTERVAL_UNCONSTRAINED);

DBMS_MLE.IMPORT_FROM_MLE (
   context_handle   IN      context_handle_t,
   property_name   IN      VARCHAR2,
   target            OUT   NOCOPY NUMBER);

DBMS_MLE.IMPORT_FROM_MLE (
   context_handle   IN      context_handle_t,
   property_name   IN      VARCHAR2,
   target            OUT   NOCOPY TIMESTAMP_TZ_UNCONSTRAINED);

DBMS_MLE.IMPORT_FROM_MLE (
   context_handle   IN      context_handle_t,
   property_name   IN      VARCHAR2,
   target            OUT   NOCOPY TIMESTAMP_UNCONSTRAINED);

DBMS_MLE.IMPORT_UROWID (
   context_handle   IN      context_handle_t,
   property_name   IN      VARCHAR2,
   target            OUT   NOCOPY UROWID);

DBMS_MLE.IMPORT_FROM_MLE (
   context_handle   IN      context_handle_t,
   property_name   IN      VARCHAR2,
   target            OUT   NOCOPY VARCHAR2 CHARACTER SET ANY_CS);

DBMS_MLE.IMPORT_FROM_MLE (
   context_handle   IN      context_handle_t,
   property_name   IN      VARCHAR2,
   target            OUT   NOCOPY YMINTERVAL_UNCONSTRAINED);

DBMS_MLE.IMPORT_CHAR (
   context_handle   IN      context_handle_t,
   property_name   IN      VARCHAR2,
   target            OUT   CHAR CHARACTER SET ANY_CS);

DBMS_MLE.IMPORT_RAW (
   context_handle   IN      context_handle_t,
   property_name   IN      VARCHAR2,
   target            OUT   RAW);
```

Parameters

Table 117-8 IMPORT\_FROM\_MLE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `context_handle` | The handle to an MLE context in the current session. |
| `property_name` | The name of the property to be retrieved. If the `property_name` is `NULL` or an empty string, `ORA-04157` error is thrown. |
| `target` | A PL/SQL variable into which the retrieved property is stored. |

Usage Notes

The `IMPORT_FROM_MLE` procedure may throw the following exceptions:
- `ORA-01031`: if the caller does not have sufficient privileges.
- `ORA-04108`: if the current container, the current user, or the currently enabled roles are different from those in effect at the time of context creation.
- `ORA-04157`: if the value of the passed property\_name is `NULL` or an empty string.
- `ORA-04205`: the value cannot be converted to the target PL/SQL type.
- `ORA-06502`: the buffer of the PL/SQL variable is too small to hold the retrieved value.

#### 117.3.12 SET\_CTX\_STDERR Procedure

This procedure redirects the `stderr` stream of the MLE context to the given `CLOB`. You need the `EXECUTE DYNAMIC                   MLE` privilege to execute this function.

Syntax

```
DBMS_MLE.SET_CTX_STDERR(
      context_handle  IN            context_handle_t,
      sink            IN OUT        NOCOPY CLOB CHARACTER SET ANY_CS);
```

Parameters

Table 117-9 SET\_CTX\_STDERR Procedure Parameters

| Parameter | Description |
| --- | --- |
| `context_handle` | Handle to an MLE context in the current session. |
| `sink` | The CLOB sink to redirect stderr to. Providing a `NULL` value will result in `ORA-06530` error. |

Usage Notes

Any output that was buffered so far gets flushed to the pre-existing sink before redirecting to the new sink.

The procedure may raise the following errors:
- `ORA-01031`: if the caller does not have sufficient privileges
- `ORA-06530`: if the sink is `NULL`.

#### 117.3.13 SET\_CTX\_STDERR\_TO\_DBMS\_OUTPUT Procedure

This procedure redirects the `stderr` stream of the MLE context to `DBMS_OUTPUT`. You need the `EXECUTE DYNAMIC MLE` privilege to execute this function.

Syntax

```
DBMS_MLE.SET_CTX_STDERR_TO_DBMS_OUTPUT(
   context_handle      IN      context_handle_t);
```

Parameters

Table 117-10 SET\_CTX\_STDERR\_TO\_DBMS\_OUTPUT Procedure Parameters

| Parameter | Description |
| --- | --- |
| `context_handle` | Handle to an MLE context in the current session. |

Usage Notes

Any output that was buffered so far gets flushed to the pre-existing sink before redirecting to `DBMS_OUTPUT`.

The procedure may raise the following errors:
- `ORA-01031`: if the caller does not have sufficient privileges

#### 117.3.14 SET\_CTX\_STDOUT Procedure

This procedure redirects the `stdout` stream of the MLE context to the given CLOB. You need the `EXECUTE DYNAMIC MLE` privilege to execute this function.

Syntax

```
DBMS_MLE.SET_CTX_STDOUT(
   context_handle      IN context_handle_t,
   sink                IN OUT NOCOPY CLOB CHARACTER SET ANY_CS);
```

Parameters

Table 117-11 SET\_CTX\_STDOUT Procedure Parameters

| Parameter | Description |
| --- | --- |
| `context_handle` | The handle to an MLE context in the current session. |
| `sink` | The `CLOB` to redirect `stdout` to. Providing a `NULL` value will result in `ORA-06530` error. |

Usage Notes

Any output that was buffered so far gets flushed to the pre-existing sink before redirecting to the new sink.

This procedure may raise the following errors:
- `ORA-01031`: if the caller does not have sufficient privileges
- `ORA-06530`: if the sink is `NULL`.

#### 117.3.15 SET\_CTX\_STDOUT\_TO\_DBMS\_OUTPUT Procedure

This procedure redirects the `stdout` stream of the MLE context to `DBMS_OUTPUT`. You need the `EXECUTE DYNAMIC MLE` privilege to execute this function.

Syntax

```
DBMS_MLE.SET_CTX_STDOUT_TO_DBMS_OUTPUT(
   context_handle      IN      context_handle_t);
```

Parameters

Table 117-12 SET\_CTX\_STDOUT\_TO\_DBMS\_OUTPUT Procedure Parameters

| Parameter | Description |
| --- | --- |
| `context_handle` | The handle to an MLE context in the current session. |

Usage Notes

Any output that was buffered so far gets flushed to the pre-existing sink before redirecting to `DBMS_OUTPUT`.

The procedure may raise the following errors:
- `ORA-01031`: if the caller does not have sufficient privileges

#### 117.3.16 SET\_STDERR Procedure

This procedure redirects the `stderr` stream of all MLE contexts to the given `CLOB`. This applies to all existing contexts and contexts created in the future. You need the `EXECUTE DYNAMIC MLE` privilege to execute this function.

Syntax

```
DBMS_MLE.SET_STDERR(
      sink            IN OUT       NOCOPY CLOB CHARACTER SET ANY_CS);
```

Parameters

Table 117-13 SET\_STDERR Procedure Parameters

| Parameter | Description |
| --- | --- |
| `sink` | The CLOB to redirect `stdout` to. |

Usage Notes

Any output that was buffered so far gets flushed to the pre-existing sink before redirecting to the new sink.

The procedure may raise the following errors:
- `ORA-01031`: if the caller does not have sufficient privileges
- `ORA-06530`: if the sink is `NULL`.

#### 117.3.17 SET\_STDERR\_TO\_DBMS\_OUTPUT Procedure

This procedure redirects the `stderr` stream of all MLE contexts to `DBMS_OUTPUT`. This applies to all existing contexts and contexts created in the future. You need the `EXECUTE DYNAMIC MLE` privilege to execute this function.

Syntax

```
DBMS_MLE.SET_STDERR_TO_DBMS_OUTPUT();
```

Usage Notes

Any output that was buffered so far gets flushed to the pre-existing sink before redirecting to `DBMS_OUTPUT`.

The procedure may raise the following errors:
- `ORA-01031`: if the caller does not have sufficient privileges

#### 117.3.18 SET\_STDOUT Procedure

This procedure redirects the `stdout` stream of all MLE contexts to the given `CLOB`. This applies to all existing contexts and contexts created in the future. You need the `EXECUTE DYNAMIC MLE` privilege to execute this function.

Syntax

```
DBMS_MLE.SET_STDOUT(
   sink       IN OUT   NOCOPY CLOB CHARACTER SET ANY_CS);
```

Parameters

Table 117-14 SET\_STDOUT Procedure Parameters

| Parameter | Description |
| --- | --- |
| `sink` | The CLOB to redirect stdout to. |

Usage Notes

Any output that was buffered so far gets flushed to the pre-existing sink before redirecting to the new sink.

The procedure may raise the following errors:
- `ORA-01031`: if the caller does not have sufficient privileges
- `ORA-06530`: if the sink is `NULL`.

#### 117.3.19 SET\_STDOUT\_TO\_DBMS\_OUTPUT Procedure

This procedure redirects the `stdout` stream of all MLE contexts to `DBMS_OUTPUT`. This applies to all existing contexts and contexts created in the future. You need the `EXECUTE DYNAMIC MLE` privilege to execute this function.

Syntax

```
DBMS_MLE.SET_STDOUT_TO_DBMS_OUTPUT();
```

Usage Notes

Any output that was buffered so far gets flushed to the pre-existing sink before redirecting to `DBMS_OUTPUT`.

The procedure may raise the following errors:
- `ORA-01031`: if the caller does not have sufficient privileges