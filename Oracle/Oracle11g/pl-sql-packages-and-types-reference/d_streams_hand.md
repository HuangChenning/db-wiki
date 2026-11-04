---
title: DBMS_STREAMS_HANDLER_ADM
book: PL/SQL Packages and Types Reference
doc_id: E40758-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/d_streams_hand.htm
tags:
  - oracle
  - 11g
  - pl-sql-packages-and-types-reference
---

## 148 DBMS\_STREAMS\_HANDLER\_ADM

The `DBMS_STREAMS_HANDLER_ADM` package, one of a set of Oracle Streams packages, provides interfaces to manage statement DML handlers.

This chapter contains the following topics:

- Using DBMS\_STREAMS\_HANDLER\_ADM
- Summary of DBMS\_STREAMS\_HANDLER\_ADM Subprograms

---

## Using DBMS\_STREAMS\_HANDLER\_ADM

This section contains topics that relate to using the `DBMS_STREAMS_HANDLER_ADM` package.

---

### Overview

A statement DML handler runs one or more data manipulation language (DML) statements on row logical change records (row LCRs) that are dequeued by an apply process. A single statement DML handler can include multiple statements, and you control the execution order of the statements.

Statement DML handlers are similar to procedure DML handlers for apply processes. Both statement DML handlers and procedure DML handlers provide custom processing of row changes that are encapsulated in row LCRs. Statement DML handlers and procedure DML handlers both run when an apply process dequeues a row LCR. However, statement DML handlers have the following advantages over procedure DML handlers:

- Statement DML handlers typically perform better than procedure DML handlers because statement DML handlers do not require PL/SQL processing.
- The syntax for statement DML handlers is same as DML syntax. Statement DML handlers do not require PL/SQL programming. Procedure DML handlers require PL/SQL programming.
- Statement DML handlers do not require the manipulation of `ANYDATA` values to access the information in row LCRs. Typically, procedure DML handlers must manipulate `ANYDATA` values.
- A statement DML handler can coexist with an error handler for same operation on the same database object. In contrast, you cannot specify both a procedure DML handler and an error handler for the same operation on the same database object.

Note:

You can specify multiple statement DML handlers for the same operation on the database object. In this case, the statement DML handlers can execute in any order, and each statement DML handler receives a copy of the original row LCR that was dequeued by the apply process.

See Also:

[Oracle Streams Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e17069/strms_apply.htm#STRMS175)

---

### Security Model

Security on this package can be controlled in either of the following ways:

- Granting `EXECUTE` on this package to selected users or roles.
- Granting `EXECUTE_CATALOG_ROLE` to selected users or roles.

If subprograms in the package are run from within a stored procedure, then the user who runs the subprograms must be granted `EXECUTE` privilege on the package directly. It cannot be granted through a role.

To ensure that the user who runs the subprograms in this package has the necessary privileges, configure an Oracle Streams administrator and connect as the Oracle Streams administrator when using this package.

See Also:

[Oracle Streams Replication Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e10705/prep_rep.htm#STREP200) for information about configuring an Oracle Streams administrator

---

### Views

The `DBMS_STREAMS_HANDLER_ADM` package uses the views listed in the [Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/toc.htm).

- `DBA_APPLY_DML_HANDLERS`
- `DBA_STREAMS_STMTS`
- `DBA_STREAMS_STMT_HANDLERS`

---

### Operational Notes

The following sections contain operational notes about the `DBMS_STREAMS_HANDLER_ADM` package:

- Statement Execution Order
- Supported SQL Statements
- Supported Row LCR Column Attributes
- Supported Row LCR Attributes
- Supported Row LCR Extra Attributes
- Supported Row LCR Method

#### Statement Execution Order

Each statement in a statement DML handler has a unique execution sequence number. When a statement DML handler is invoked, it executes its statements in order from the statement with the lowest execution sequence number to the statement with the highest execution sequence number.

#### Supported SQL Statements

You can use statement DML handlers for any valid DML operation on a row logical change record (row LCR). For example, a statement DML handler can audit the DML changes made to a table.

The following SQL statements are supported in statement DML handlers:

- `INSERT`
- `UPDATE`
- `DELETE`
- `MERGE`

In addition, define variables are not supported in the SQL statements in a statement DML handler.

However, the SQL statements in a statement DML handler can include calls to member subprograms for the row LCR type (`LCR$_ROW_RECORD`), such as `ADD_COLUMN`, `DELETE_COLUMN`, `KEEP_COLUMNS`, and `RENAME_COLUMN`.

Note:

A statement DML handler cannot modify the value of a column in a row LCR.

See Also:

["LCR$\_ROW\_RECORD Type"](t_lcr.md)

#### Supported Row LCR Column Attributes

Statements in statement DML handlers can contain the row LCR column attributes described in Table 148-1.

Table 148-1 Row LCR Column Attributes

| Attribute | Description |
| --- | --- |
| `new` | Returns the new column value in a row LCR. If the new value does not exist, then this attribute returns the old value. |
| `new_exists` | Returns `TRUE` if a new column value exists in a row LCR.  Returns `FALSE` is a new column value does not exist in a row LCR. |
| `new_only` | Returns the new column value in a row LCR. If the new value does not exist, then this attribute returns `NULL` and does not return the old column value. |
| `old` | Returns the old column value in a row LCR. |
| `old_exists` | Returns `TRUE` if an old column value exists in a row LCR.  Returns `FALSE` is an old column value does not exist in a row LCR. |

Specify these attributes in the following way in a statement:

```
:attribute.column_name
```

For example, to specify the `new_only` attribute for the `salary` column, enter the following in a statement:

```
:new_only.salary
```

#### Supported Row LCR Attributes

Statements in statement DML handlers can contain the row LCR attributes described in Table 148-2.

Table 148-2 Row LCR Attributes

| Attribute | Description |
| --- | --- |
| `command_type` | Returns the type of DML statement that produced the change, either `INSERT`, `UPDATE`, or `DELETE`. `DBMS_LOB` piecewise LOB operations are not supported by statement DML handlers. |
| `commit_scn` | Returns the commit system change number (SCN) of the transaction to which the LCR belongs. |
| `compatible` | Returns the minimal database compatibility required to support the LCR. |
| `instance_number` | Returns the instance number of the database instance that made the change that is encapsulated in the LCR. Typically, the instance number is relevant in an Oracle Real Application Clusters (Oracle RAC) configuration. |
| `object_owner` | Returns the schema name that contains the table with the changed row. |
| `object_name` | Returns the name of the table that contains the changed row. |
| `scn` | Returns the SCN at the time when the change was made. |
| `source_database_name` | Returns the name of the source database where the row change occurred. |
| `source_time` | Returns the time when the change in an LCR captured by a capture process was generated in the redo log of the source database, or the time when a persistent LCR was created. |
| `tag` | Returns a raw tag that can be used to track the LCR. |
| `transaction_id` | Returns the identifier of the transaction in which the DML statement was run. |

Specify these attributes in the following way in a statement:

```
:attribute_name
```

For example, to specify the `source_database_name` attribute for a row LCR, enter the following in a statement:

```
:source_database_name
```

#### Supported Row LCR Extra Attributes

Statements in statement DML handlers can contain the row LCR extra attributes described in Table 148-3.

Table 148-3 Row LCR Extra Attributes

| Attribute | Description |
| --- | --- |
| `row_id` | Returns the rowid of the row changed in a row LCR. |
| `serial#` | Returns the serial number of the session that performed the change captured in the LCR. |
| `session#` | Returns the identifier of the session that performed the change captured in the LCR. |
| `thread#` | Returns the thread number of the instance in which the change captured in the LCR was performed. Typically, the thread number is relevant only in an Oracle RAC configuration. |
| `tx_name` | Returns the name of the transaction that includes the LCR. |
| `username` | Returns the name of the current user who performed the change captured in the LCR. |

Specify these attributes in the following way in a statement:

```
:extra_attribute.attribute_name
```

For example, to specify the `row_id` extra attribute for a row LCR, enter the following in a statement:

```
:extra_attribute.row_id
```

#### Supported Row LCR Method

A statement in a statement DML handler can include a call to the `EXECUTE` member procedure for row LCRs. The `EXECUTE` member procedure executes the row LCR under the security domain of the current user.

A statement that runs the `EXECUTE` member procedure can be placed anywhere in the execution sequence order of the statement DML handler. It is not necessary to execute a row LCR unless the goal is to apply the changes in the row LCR to a table in addition to performing any other SQL statements in the statement DML handler.

When you call the `EXECUTE` member procedure in a statement, the `conflict_resolution` parameter controls whether any conflict resolution defined for the table using the `SET_UPDATE_CONFLICT_HANDLER` procedure in the `DBMS_APPLY_ADM` package is used to resolve conflicts resulting from the execution of the LCR:

```
:lcr.execute TRUE|FALSE
```

A `TRUE` argument indicates that conflict resolution is used. A `FALSE` argument indicates that conflict resolution is not used.

For example, to use conflict resolution, enter the following in a statement:

```
:lcr.execute TRUE
```

An error is raised if this parameter is not specified or is set to `NULL`.

---

## Summary of DBMS\_STREAMS\_HANDLER\_ADM Subprograms

Table 148-4 DBMS\_STREAMS\_HANDLER\_ADM Package Subprograms

| Subprogram | Description |
| --- | --- |
| ADD\_STMT\_TO\_HANDLER Procedure | Adds a statement to a statement DML handler |
| CREATE\_STMT\_HANDLER Procedure | Creates a statement DML handler |
| DROP\_STMT\_HANDLER Procedure | Drops a statement DML handler |
| REMOVE\_STMT\_FROM\_HANDLER Procedure | Removes a statement from a statement DML handler |

Note:

The subprograms in this package do not commit.

---

### ADD\_STMT\_TO\_HANDLER Procedure

This procedure adds a statement to a statement DML handler.

Syntax

```
DBMS_STREAMS_HANDLER_ADM.ADD_STMT_TO_HANDLER(
   handler_name       IN VARCHAR2,  
   statement          IN CLOB,   
   execution_sequence IN NUMBER  DEFAULT NULL);
```

Parameters

Table 148-5 ADD\_STMT\_TO\_HANDLER Procedure Parameters

| Parameter | Description |
| --- | --- |
| `handler_name` | The name of the statement DML handler. |
| `statement` | The text of the SQL statement to add to the statement DML handler.  If `NULL`, then the procedure raises an error. |
| `execution_sequence` | The position of the statement in the statement DML handler at which a SQL statement is to be set to execute. Statements are executed in order from the lowest execution sequence number to the highest execution sequence number.  You can specify a positive or negative integer or decimal, or you can specify 0 (zero).  If you specify an execution sequence number that is used by an existing statement in the statement DML handler, then the statement in the `statement` parameter replaces the existing statement.  If `NULL`, then the statement is added to the statement DML handler with an execution sequence number that is larger than the execution sequence number for any statement in the statement DML handler. |

---

### CREATE\_STMT\_HANDLER Procedure

This procedure creates a statement DML handler.

Syntax

```
DBMS_STREAMS_HANDLER_ADM.CREATE_STMT_HANDLER(
   handler_name IN VARCHAR2,  
   comment      IN VARCHAR2  DEFAULT NULL);
```

Parameters

Table 148-6 CREATE\_STMT\_HANDLER Procedure Parameters

| Parameter | Description |
| --- | --- |
| `handler_name` | The name of the statement DML handler. |