---
title: DBMS_APPLY_ADM
book: PL/SQL Packages and Types Reference
doc_id: E40758-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/d_apply.htm
tags:
  - oracle
  - 11g
  - pl-sql-packages-and-types-reference
---

## 21 DBMS\_APPLY\_ADM

The `DBMS_APPLY_ADM` package provides subprograms to configure and manage Oracle Streams apply processes, XStream outbound servers, and XStream inbound servers.

This chapter contains the following topics:

- Using DBMS\_APPLY\_ADM
- Summary of DBMS\_APPLY\_ADM Subprograms

See Also:

- [Oracle Streams Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e17069/strms_apply.htm#STRMS004) and [Oracle Streams Replication Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e10705/toc.htm) for more information about this package and apply processes
- [Oracle Database XStream Guide](https://docs.oracle.com/cd/E11882_01/server.112/e16545/toc.htm) for more information about XStream outbound servers and inbound servers

---

## Using DBMS\_APPLY\_ADM

This section contains topics which relate to using the `DBMS_APPLY_ADM` package.

---

### Overview

This package provides interfaces to start, stop, and configure Oracle Streams apply processes, XStream outbound servers, and XStream inbound servers. This package includes subprograms for configuring apply handlers, setting enqueue destinations for messages, and specifying execution directives for messages. This package also provides administrative subprograms that set the instantiation SCN for objects at a destination database. This package also includes subprograms for managing apply errors.

Note:

- For simplicity, this chapter refers to apply processes, XStream outbound servers, and XStream inbound servers as apply components. This chapter identifies a specific type of apply component when necessary.
- Using XStream requires purchasing a license for the Oracle GoldenGate product.

---

### Security Model

Security on this package can be controlled in either of the following ways:

- Granting `EXECUTE` on this package to selected users or roles.
- Granting `EXECUTE_CATALOG_ROLE` to selected users or roles.

If subprograms in the package are run from within a stored procedure, then the user who runs the subprograms must be granted `EXECUTE` privilege on the package directly. It cannot be granted through a role.

When the `DBMS_APPLY_ADM` package is used to manage an Oracle Streams configuration, it requires that the user is granted the privileges of an Oracle Streams administrator.

When the `DBMS_APPLY_ADM` package is used to manage an XStream configuration, it requires that the user is granted the privileges of an XStream administrator.

Note:

The user must be granted additional privileges to perform some administrative tasks using the subprograms in this package, such as setting an apply user. If additional privileges are required for a subprogram, then the privileges are documented in the section that describes the subprogram.

See Also:

- [Oracle Streams Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e10705/prep_rep.htm#STREP200) for information about configuring an Oracle Streams administrator
- [Oracle Database XStream Guide](https://docs.oracle.com/cd/E11882_01/server.112/e16545/xstrm_config.htm#XSTRM72553) for information about configuring an XStream administrator

---

### Operational Notes

The following sections contain operational notes for this package:

- Deprecated Apply Component Parameter Value

#### Deprecated Apply Component Parameter Value

Note:

Oracle recommends that you do not use deprecated apply component parameter values. Support for deprecated features is for backward compatibility only.

The `NONE` value for the `commit_serialization` apply component parameter is deprecated. It is replaced by the `DEPENDENT_TRANSACTIONS` value.

See Also:

SET\_PARAMETER Procedure

---

## Summary of DBMS\_APPLY\_ADM Subprograms

Table 21-1 DBMS\_APPLY\_ADM Package Subprograms

| Subprogram | Description |
| --- | --- |
| ADD\_STMT\_HANDLER Procedure | Adds a statement DML handler for a specified operation on a specified database object to a single apply component or to all apply components in the database |
| ALTER\_APPLY Procedure | Alters an apply component |
| COMPARE\_OLD\_VALUES Procedure | Specifies whether to compare the old value of one or more columns in a row logical change record (row LCR) with the current value of the corresponding columns at the destination site during apply |
| CREATE\_APPLY Procedure | Creates an apply component |
| CREATE\_OBJECT\_DEPENDENCY Procedure | Creates an object dependency |
| DELETE\_ALL\_ERRORS Procedure | Deletes all the error transactions for the specified apply component |
| DELETE\_ERROR Procedure | Deletes the specified error transaction |
| DROP\_APPLY Procedure | Drops an apply component |
| DROP\_OBJECT\_DEPENDENCY Procedure | Drops an object dependency |
| EXECUTE\_ALL\_ERRORS Procedure | Reexecutes the error transactions for the specified apply component |
| EXECUTE\_ERROR Procedure | Reexecutes the specified error transaction |
| GET\_ERROR\_MESSAGE Function | Returns the message payload from the error queue for the specified message number and transaction identifier |
| REMOVE\_STMT\_HANDLER | Removes a statement DML handler for a specified operation on a specified database object from a single apply component or from all apply components in the database |
| SET\_CHANGE\_HANDLER Procedure | Sets or unsets a statement DML handler that tracks changes for a specified operation on a specified database object for a single apply component |
| SET\_DML\_HANDLER Procedure | Sets a user procedure as a procedure DML handler for a specified operation on a specified database object for a single apply component or for all apply components in the database |
| SET\_ENQUEUE\_DESTINATION Procedure | Sets the queue where the apply component automatically enqueues a message that satisfies the specified rule |
| SET\_EXECUTE Procedure | Specifies whether a message that satisfies the specified rule is executed by an apply component |
| SET\_GLOBAL\_INSTANTIATION\_SCN Procedure | Records the specified instantiation SCN for the specified source database and, optionally, for the schemas at the source database and the tables owned by these schemas |
| SET\_KEY\_COLUMNS Procedures | Records the set of columns to be used as the substitute primary key for local apply purposes and removes existing substitute primary key columns for the specified object if they exist |
| SET\_PARAMETER Procedure | Sets an apply parameter to the specified value |
| SET\_SCHEMA\_INSTANTIATION\_SCN Procedure | Records the specified instantiation SCN for the specified schema in the specified source database and, optionally, for the tables owned by the schema at the source database |
| SET\_TABLE\_INSTANTIATION\_SCN Procedure | Records the specified instantiation SCN for the specified table in the specified source database |
| SET\_UPDATE\_CONFLICT\_HANDLER Procedure | Adds, updates, or drops an update conflict handler for the specified object |
| SET\_VALUE\_DEPENDENCY Procedure | Sets or removes a value dependency |
| START\_APPLY Procedure | Directs the apply component to start applying messages |
| STOP\_APPLY Procedure | Stops the apply component from applying any messages and rolls back any unfinished transactions being applied |

Note:

All procedures commit unless specified otherwise. However, the `GET_ERROR_MESSAGE` function does not commit.

---

### ADD\_STMT\_HANDLER Procedure

This procedure adds a statement DML handler for a specified operation on a specified database object. The procedure adds the statement DML handler to a single apply component or to all apply components in the database.

This procedure is overloaded. One version of this procedure contains the `statement` and `comment` parameters, and the other does not. The `statement` parameter enables you to create the statement DML handler and add it to one or more processes in one step. Otherwise, create the statement DML handler using the `DBMS_STREAMS_HANDLER_ADM` package before adding it to one or more processes.

Syntax

```
DBMS_APPLY_ADM.ADD_STMT_HANDLER(
   object_name     IN  VARCHAR2,
   operation_name  IN  VARCHAR2,
   handler_name    IN  VARCHAR2,
   statement       IN  CLOB,
   apply_name      IN  VARCHAR2  DEFAULT NULL,
   comment         IN  VARCHAR2  DEFAULT NULL);

DBMS_APPLY_ADM.ADD_STMT_HANDLER(
   object_name     IN  VARCHAR2,
   operation_name  IN  VARCHAR2,
   handler_name    IN  VARCHAR2,
   apply_name      IN  VARCHAR2  DEFAULT NULL);
```

Parameters

Table 21-2 ADD\_STMT\_HANDLER Procedure Parameters

| Parameter | Description |
| --- | --- |
| `object_name` | The name of the source object specified as `[``schema_name``.]` `object_name`. For example, `hr.employees`. If the schema is not specified, then the current user is the default. The specified object does not need to exist when you run this procedure.  If `NULL`, then the procedure raises an error. |
| `operation_name` | The name of the operation, which can be specified as:  - `INSERT` - `UPDATE` - `DELETE`  If `NULL`, then the procedure raises an error.  Note: Statement DML handlers cannot be specified for LOB operations. |
| `handler_name` | The name of the statement DML handler.  If the specified statement DML handler exists, then the statement in the `statement` parameter is added to the existing handler. Ensure that the existing statement DML handler is for the same operation on the same database object as the settings for the `operation_name` and `object_name` parameters, respectively. If the existing handler is for a different operation or database object, then an apply error results when the handler is invoked.  If the specified statement DML handler does not exist and a non- `NULL` statement parameter is specified, then this procedure creates the statement DML handler.  If the specified statement DML handler does not exist and the `statement` parameter is not specified or is `NULL`, then this procedure raises an error.  If `NULL`, then the procedure raises an error. |
| `statement` | The text of the SQL statement to add to the statement DML handler.  If `NULL`, then the procedure raises an error. |
| `apply_name` | The name of the apply component that uses the statement DML handler.  If `NULL`, then the procedure adds the statement DML handler as a general handler to all apply components in the database. |