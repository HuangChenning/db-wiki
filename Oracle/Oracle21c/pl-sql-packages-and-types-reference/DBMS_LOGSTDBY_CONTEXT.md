---
title: PL/SQL Packages and Types Reference
book: Database PL/SQL Packages and Types Reference
doc_id: F31492-25
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/arpls/DBMS_LOGSTDBY_CONTEXT.html
tags:
  - oracle
  - 21c
  - pl-sql-packages-and-types-reference
---

## 109 DBMS\_LOGSTDBY\_CONTEXT

As of Oracle Database 12c release 1 (12.1), SQL Apply processes have access to a context namespace called `LSBY_APPLY_CONTEXT`. You can use the procedures provided in the `DBMS_LOGSTDBY_CONTEXT` package to set and retrieve various parameters associated with `LSBY_APPLY_CONTEXT`. This is useful when writing skip procedures that are registered with SQL Apply using the `DBMS_LOGSTBDY.SKIP` and `DBMS_LOGSTDBY.SKIP_ERROR` procedures.

This chapter contains the following topics:

See Also:

[Oracle Data Guard Concepts and Administration](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=SBYDB-GUID-3666CA35-D993-44B6-8D70-A2B8B9EC8B2E) for more information about SQL Apply and logical standby databases

### 109.1 DBMS\_LOGSTDBY\_CONTEXT Overview

SQL Apply processes have access to a context namespace called `LSBY_APPLY_CONTEXT`.

The following table lists the predefined parameters associated with `LSBY_APPLY_CONTEXT` that you can set and retrieve by using the procedures provided in the `DBMS_LOGSTDBY_CONTEXT` package. The ability to set and retrieve the parameters in this way is useful when writing skip procedures that are registered with SQL Apply using the `DBMS_LOGSTBDY.SKIP` and `DBMS_LOGSTDBY.SKIP_ERROR` procedures.

Table 109-1 Predefined Parameters of Namespace LSBY\_APPLY\_CONTEXT

| Parameter | Description |
| --- | --- |
| `STATEMENT` | First 4000 bytes of the statement that the Apply process is processing. |
| `STATEMENT_TYPE` | See [Table 107-15](DBMS_LOGSTDBY.md) for a list of various statement types. |
| `PACKAGE_SCHEMA` | Schema that owns the PL/SQL package being processed (if applicable). |
| `PACKAGE_NAME` | Name of the PL/SQL package being processed (if applicable). |
| `PROCEDURE_NAME` | Name of the PL/SQL procedure being processed (if applicable). |
| `CURRENT_SCHEMA` | Current schema in effect when the DDL or PL/SQL procedure was executed at the primary. |
| `XIDUSN` | XIDUSN of the transaction at the primary database. |
| `XIDSLT` | XIDSLT of the transaction at the primary database. |
| `XIDSQN` | XIDSQN of the transaction at the primary database. |
| `SCHEMA` | Schema that owns the object being processed by SQL Apply (in the case of DML or DDL operations). |
| `NAME` | Object name being processed by SQL Apply (in case of DML or DDL operations). |
| `CONTAINER_NAME` | Container where the target object or the PL/SQL procedure resides (in the case of a multitenant container database (CDB)). |
| `ERROR` | Text of the original error encountered by the SQL Apply process (if applicable). |
| `NEW_ERROR` | Text of the new error to be raised by the SQL Apply process (if applicable, See the DBMS\_LOGSTDBY [SKIP\_ERROR Procedure](DBMS_LOGSTDBY.md) ). |
| `NEW_STMT` | Text of the replacement statement that SQL Apply must execute (If applicable, See the DBMS\_LOGSTDBY [SKIP Procedure](DBMS_LOGSTDBY.md)). |
| `SKIP_ACTION` | The skip action to be performed by SQL Apply (See the DBMS\_LOGSTDBY [SKIP Procedure](DBMS_LOGSTDBY.md)). |

### 109.2 DBMS\_LOGSTDBY\_CONTEXT Security Model

The security model for the `DBMS_LOGSTDBY_CONTEXT` package is the same as for the `DBMS_LOGSTDBY` package.

See Also:

[DBMS\_LOGSTDBY](DBMS_LOGSTDBY.md)

### 109.3 Summary of DBMS\_LOGSTDBY\_CONTEXT Subprograms

This table lists and briefly describes the `DBMS_LOGSTDBY_CONTEXT` package subprograms.

Table 109-2 DBMS\_LOGSTDBY\_CONTEXT Package Subprograms

| Subprogram | Description |
| --- | --- |
| CLEAR\_ALL\_CONTEXT Procedure | Clears all parameters contained within namespace `LSBY_APPLY_CONTEXT`. |
| CLEAR\_CONTEXT Procedure | Clears the specific parameter. |
| GET\_CONTEXT Procedure | Retrieves the value for the specified parameter. |
| SET\_CONTEXT Procedure | Sets the named parameter with the specified value. |

#### 109.3.1 CLEAR\_ALL\_CONTEXT Procedure

This procedure clears all parameters contained within namespace `LSBY_APPLY_CONTEXT.`

Syntax

```
DBMS_LOGSTDBY_CONTEXT.CLEAR_ALL_CONTEXT;
```

Parameters

None

#### 109.3.2 CLEAR\_CONTEXT Procedure

This procedure clears the specific parameter.

Syntax

```
DBMS_LOGSTDBY_CONTEXT.CLEAR_CONTEXT (
   name            IN VARCHAR2);
```

Parameters

Table 109-3 CLEAR\_CONTEXT Procedure Parameters

| Parameter | Description |
| --- | --- |
| `name` | Name of the parameter to be cleared. |

#### 109.3.3 GET\_CONTEXT Procedure

This procedure retrieves the value for the specified parameter.

Syntax

```
DBMS_LOGSTDBY_CONTEXT.GET_CONTEXT (
   name            IN VARCHAR2,
   value           OUT VARCHAR2);
```

Parameters

Table 109-4 GET\_CONTEXT Procedure Parameters

| Parameter | Description |
| --- | --- |
| `name` | Name of the parameter. |
| value | The value retrieved for the parameter. |

#### 109.3.4 SET\_CONTEXT Procedure

This procedure sets the named parameter with the specified value.

Syntax

```
DBMS_LOGSTDBY_CONTEXT.SET_CONTEXT (
   name            IN VARCHAR2
   value           IN VARCHAR2);
```

Parameters

Table 109-5 SET\_CONTEXT Procedure Parameters

| Parameter | Description |
| --- | --- |
| `name` | Name of the parameter to be set. |
| value | Value to be assigned to the parameter being set. |