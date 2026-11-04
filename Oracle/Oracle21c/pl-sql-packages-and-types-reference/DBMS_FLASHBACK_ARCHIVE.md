---
title: PL/SQL Packages and Types Reference
book: Database PL/SQL Packages and Types Reference
doc_id: F31492-25
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/arpls/DBMS_FLASHBACK_ARCHIVE.html
tags:
  - oracle
  - 21c
  - pl-sql-packages-and-types-reference
---

## 78 DBMS\_FLASHBACK\_ARCHIVE

The `DBMS_FLASHBACK_ARCHIVE` package contains procedures for performing various flashback archive tasks.

These include:

- Disassociation and reassociation of a Flashback Archive enabled table from/with its underlying Flashback Time Travel
- Tamper-proofing the tables of an application
- Importing of user history
	Caution:
	Importing user-generated history can lead to inaccurate, or unreliable results. This procedure should only be used after consulting with Oracle Support.
- Enabling and disabling of session-level support for valid-time

See Also:

Oracle Database Development Guide for more information about [Using Flashback Time Travel](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=ADFNS-GUID-06AA782A-3F79-4235-86D5-2D136485F093)

This chapter contains the following topics:

### 78.1 DBMS\_FLASHBACK\_ARCHIVE Overview

Flashback Time Travel provides strict protection on the internal history tables that it creates and maintains for users.

Caution:

The `DBMS_FLASHBACK_ARCHIVE` package does not support migration between databases. It allows you to move Flashback Time Travel history within the same database only, and not outside it. This package does not allow you to move Flashback Time Travel table data. It allows you to import customer history only and not Flashback Time Travel history.

The read-only semantics prohibit users, including a DBA, from doing updates, deletes, and inserts on the Flashback Time Travel internal history tables. Users are also prevented from issuing any DDL statements on these tables. This strict security enforcement helps meet the requirements of applications in regulatory / compliance environments. Flashback Time Travel supports most common DDL statements, including those that alter the table definition or incur data movement. However, some DDL statements are not supported on Flashback Archive enabled tables. Since most application schemas are modified during application software upgrades, the ability to perform DDL operations on tracked tables is critical.

To support schema evolution during application upgrades and other table maintenance tasks that require use of DDL statements not supported by Flashback Time Travel, the `DBMS_FLASHBACK_ARCHIVE` package provides a set of simple-to-use PL/SQL procedures:

- To disassociate a Flashback Archive enabled base table from the underlying Flashback Time Travel
- To reassociate a temporarily disassociated base table with its underlying Flashback Time Travel

After a user has disassociated the base table from its Flashback Archive, it's possible to issue any DDL statements on the base table or the history tables in the Flashback Archive. Having finished with the schema changes, the user can then reassociate the base table with its Flashback Archive so that Flashback Time Travel protection is in operation and automatic tracking and archiving is resumed.

### 78.2 DBMS\_FLASHBACK\_ARCHIVE Security Model

Users need the `FLASHBACK_ARCHIVE_ADMINISTER` privilege to import user-generated history, to set context level, and to tamper-proof tables. After a table is disassociated, users can perform DDL and DML statements on the table if they have the necessary privileges. Enabling and disabling session-level Valid Time Temporal flashback needs no additional privileges.

### 78.3 DBMS\_FLASHBACK\_ARCHIVE Constants

The `DBMS_FLASHBACK_ARCHIVE` package uses the constants shown in the following table.

Table 78-1 DBMS\_FLASHBACK\_ARCHIVE Constants

| Constant | Type | Value | Description |
| --- | --- | --- | --- |
| `NODROP` | `BINARY_INTEGER` | `1` | Do not drop temporary history table |
| `NOCOMMIT` | `BINARY_INTEGER` | `2` | Do not commit transaction |
| `NODELETE` | `BINARY_INTEGER` | `4` | Do not delete data in history table |

### 78.4 Summary of DBMS\_FLASHBACK\_ARCHIVE Subprograms

This table lists the `DBMS_FLASHBACK_ARCHIVE` subprograms and briefly describes them.

Table 78-2 DBMS\_FLASHBACK\_ARCHIVE Package Subprograms

| Subprogram | Description |
| --- | --- |
| ADD\_TABLE\_TO\_APPLICATION Procedure | Takes an application name and adds a table to the application as a security table |
| CREATE\_TEMP\_HISTORY\_TABLE Procedure | Creates a table called `TEMP_HISTORY` with the correct definition in schema |
| DISABLE\_APPLICATION Procedure | Takes an application name and marks a table in it as a security table |
| DISABLE\_ASOF\_VALID\_TIME Procedure | Disables session level valid-time flashback |
| DISASSOCIATE\_FBA Procedure | Disassociates the given table from the Flashback Time Travel |
| DROP\_APPLICATION Procedure | Takes an application name and removes it from the list of applications |
| ENABLE\_APPLICATION Procedure | Takes an application name and enables Flashback Time Travel on all the security tables for this application |
| ENABLE\_AT\_VALID\_TIME Procedure | Enables session level valid time flashback |
| EXTEND\_MAPPINGS Procedure | Extends time mappings to times in the past |
| GET\_SYS\_CONTEXT Function | Gets the context previously selected by the SET\_CONTEXT\_LEVEL Procedure |
| IMPORT\_HISTORY Procedure | Imports history from a table called `TEMP_HISTORY` in the given schema. |
| LOCK\_DOWN\_APPLICATION Procedure | Takes an application name and makes all the security tables read-only. The group called `SYSTEM` cannot be locked |
| PURGE\_CONTEXT Procedure | Purges the context to be saved selected by the SET\_CONTEXT\_LEVEL Procedure |
| REASSOCIATE\_FBA Procedure | Reassociates the given table with the Flashback Time Travel |
| REGISTER\_APPLICATION Procedure | Takes an application name and optionally a Time Travel, and registers an application for database hardening |
| REMOVE\_TABLE\_FROM\_APPLICATION Procedure | Takes an application name and marks a table in it as no longer being a security table |
| SET\_CONTEXT\_LEVEL Procedure | Defines how much of the user context is to be saved |

#### 78.4.1 ADD\_TABLE\_TO\_APPLICATION Procedure

This procedure takes an application name and adds a table to the application as a security table. If the application is enabled for Flashback Time Travel, then this table will also be enabled for Flashback Time Travel.

Syntax

```
DBMS_FLASHBACK_ARCHIVE.ADD_TABLE_TO_APPLICATION (
   application_name           IN   VARCHAR2,
   table_name                 IN   VARCHAR2,
   schema_name                IN   VARCHAR2 := NULL);
```

Parameters

Table 78-3 ADD\_TABLE\_TO\_APPLICATION Procedure Parameters

| Parameter | Description |
| --- | --- |
| `application_name` | Name of the application for which a table has been added as a security table |
| `table_name` | Name of the table to add as a security table for the given application |
| `schema_name` | Name of the schema containing the desired table. If no schema name is specified, the current schema is used. |

#### 78.4.2 CREATE\_TEMP\_HISTORY\_TABLE Procedure

This procedure creates a table called `TEMP_HISTORY` with the correct definition in schema.

Syntax

```
DBMS_FLASHBACK_ARCHIVE.CREATE_TEMP_HISTORY_TABLE (
   owner_name1      IN   VARCHAR2, 
   table_name1      IN   VARCHAR2);
```

Parameters

Table 78-4 CREATE\_TEMP\_HISTORY\_TABLE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `owner_name` 1 | Schema of the Flashback Time Travel-enabled table |
| `table_name` 1 | Name of the Flashback Time Travel-enabled table |

#### 78.4.3 DISABLE\_APPLICATION Procedure

This procedure takes an application name and disables Flashback Time Travel on all of its security tables.

Syntax

```
DBMS_FLASHBACK_ARCHIVE.DISABLE_APPLICATION (
   application_name           IN   VARCHAR2);
```

Parameters

Table 78-5 DISABLE\_APPLICATION Procedure Parameters

| Parameter | Description |
| --- | --- |
| `application_name` | Name of the application whose security tables will be disabled for Flashback Time Travel |

#### 78.4.4 DISABLE\_ASOF\_VALID\_TIME Procedure

This procedure disables session level valid-time flashback.

Syntax

```
DBMS_FLASHBACK_ARCHIVE.DISABLE_ASOF_VALID_TIME;
```

#### 78.4.5 DISASSOCIATE\_FBA Procedure

This procedure disassociates the given table from the Flashback Time Travel.

Syntax

```
DBMS_FLASHBACK_ARCHIVE.DISASSOCIATE_FBA (
   owner_name     IN    VARCHAR2, 
   table_name     IN    VARCHAR2);
```

Parameters

Table 78-6 DISASSOCIATE\_FBA Procedure Parameters

| Parameter | Description |
| --- | --- |
| `owner_name` | Schema of the Flashback Time Travel enabled base table |
| `table_name` | Name of the Flashback Time Travel enabled base table |

Exceptions

Table 78-7 DISASSOCIATE\_FBA Procedure Exceptions

| Exception | Description |
| --- | --- |
| `ORA-55602` | User table is not enabled for Flashback Time Travel |
| `ORA-55634` | Cannot acquire the lock on the table for disassociation |

#### 78.4.6 DROP\_APPLICATION Procedure

This procedure takes an application name and removes it from the list of applications. As part of this procedure, Flashback Time Travel will be disabled on all security-enabled tables and all history data will be lost. The group called `SYSTEM` cannot be dropped.

Syntax

```
DBMS_FLASHBACK_ARCHIVE.DROP_APPLICATION (
   application_name           IN   VARCHAR2);
```

Parameters

Table 78-8 DROP\_APPLICATION Procedure Parameters

| Parameter | Description |
| --- | --- |
| `application_name` | Name of the application for which a table has been added as a security table |

#### 78.4.7 ENABLE\_APPLICATION Procedure

This procedure takes an application name and enables Flashback Time Travel on all the security tables for this application. Once an application is enabled, every change to an Flashback Time Travel enabled table will be tracked.

Syntax

```
DBMS_FLASHBACK_ARCHIVE.ENABLE_APPLICATION (
   application_name           IN   VARCHAR2);
```

Parameters

Table 78-9 ENABLE\_APPLICATION Procedure Parameters

| Parameter | Description |
| --- | --- |
| `application_name` | Name of the application for which to enable Flashback Time Travel on all its security tables |

#### 78.4.8 ENABLE\_AT\_VALID\_TIME Procedure

This procedure enables session level valid time flashback.

Syntax

```
DBMS_FLASHBACK_ARCHIVE.ENABLE_AT_VALID_TIME (
   level          IN    VARCHAR2, 
   query_time     IN    TIMESTAMP DEFAULT SYSTIMESTAMP);
```

Parameters

Table 78-10 ENABLE\_AT\_VALID\_TIME Procedure Parameters

| Parameter | Description |
| --- | --- |
| `level` | Options:  - `All` - Sets the visibility of temporal data to the full table, which is the default temporal table visibility - `CURRENT` - Sets the visibility of temporal data to currently valid data within the valid time period at the session level - `ASOF` - Sets the visibility of temporal data to data valid as of the given time as defined by the timestamp |
| `query_time` | Used only if level is `ASOF`. Data which is valid at this `query_time` will only be shown. |

#### 78.4.9 EXTEND\_MAPPINGS Procedure

This procedure extends time mappings to times in the past.

Syntax

```
DBMS_FLASHBACK_ARCHIVE.EXTEND_MAPPINGS;
```

#### 78.4.10 GET\_SYS\_CONTEXT Function

This function gets the context previously selected by the SET\_CONTEXT\_LEVEL Procedure.

Syntax

```
DBMS_FLASHBACK_ARCHIVE.GET_SYS_CONTEXT (
   xid            IN   RAW, 
   namespace      IN   VARCHAR2, 
   parameter      IN   VARCHAR2)
 RETURN VARCHAR2;
```

Parameters

Table 78-11 GET\_SYS\_CONTEXT Function Parameters

| Parameter | Description |
| --- | --- |
| `xid` | Transaction identifier is an opaque handle to a transaction obtained from the versions query |
| `namespace` | Namespace |
| `parameter` | If undefined, the subprogram returns `NULL` |

#### 78.4.11 IMPORT\_HISTORY Procedure

This procedure is called after invoking the CREATE\_TEMP\_HISTORY\_TABLE procedure, and after the `TEMP_HISTORY` table is populated with user-generated history data

Caution:

Importing user-generated history can lead to inaccurate, or unreliable results. This procedure should only be used after consulting with Oracle Support.

The `DBMS_FLASHBACK_ARCHIVE` package does not support migration between databases. It allows you to move Flashback Time Travel history within the same database only, and not outside it. This package does not allow you to move Flashback Time Travel table data. It allows you to import customer history only and not Flashback Time Travel history.

Syntax

```
DBMS_FLASHBACK_ARCHIVE.IMPORT_HISTORY (
   owner_name1         IN   VARCHAR2, 
   table_name1         IN   VARCHAR2 
   temp_history_name   IN   VARCHAR2 DEFAULT 'TEMP_HISTORY',
   options             IN   BINARY_INTEGER DEFAULT 0);
```

Parameters

Table 78-12 IMPORT\_HISTORY Procedure Parameters

| Parameter | Description |
| --- | --- |
| `owner_name` 1 | Schema of the Flashback Time Travel-enabled table |
| `table_name` 1 | Name of the Flashback Time Travel-enabled table |
| `temp_history_name` | Optional temporary history table from which we import history data |
| `options` | One (or a combination) of constants (`NODROP`, `NOCOMMIT`, and `NODELETE`) to specify if we want to drop, commit changes of, or truncate the temporary history table |

Usage Notes

The database function [`TIMESTAMP_TO_SCN`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=SQLRF51858) can be used to convert times to SCN when populating the temporary history table.

#### 78.4.12 LOCK\_DOWN\_APPLICATION Procedure

This procedure takes an application name and makes all the security tables read-only. The group called `SYSTEM` cannot be locked.

Syntax

```
DBMS_FLASHBACK_ARCHIVE.LOCK_DOWN_APPLICATION (
   application_name           IN   VARCHAR2);
```

Parameters

Table 78-13 LOCK\_DOWN\_APPLICATION Procedure Parameters

| Parameter | Description |
| --- | --- |
| `application_name` | Name of the application for which a table has been added as a security table |

#### 78.4.13 PURGE\_CONTEXT Procedure

This procedure purges the context to be saved selected by the SET\_CONTEXT\_LEVEL Procedure.

Syntax

```
DBMS_FLASHBACK_ARCHIVE.PURGE_CONTEXT;
```

#### 78.4.14 REASSOCIATE\_FBA Procedure

This procedure reassociates the given table with the Flashback Time Travel.

Syntax

```
DBMS_FLASHBACK_ARCHIVE.REASSOCIATE_FBA (
   owner_name      VARCHAR2, 
   table_name      VARCHAR2);
```

Parameters

Table 78-14 REASSOCIATE\_FBA Procedure Parameters

| Parameter | Description |
| --- | --- |
| `owner_name` | Schema of the Flashback Time Travel enabled base table |
| `table_name` | Name of the Flashback Time Travel enabled base table |

Exceptions

Table 78-15 REASSOCIATE\_FBA Procedure Exceptions

| Parameter | Description |
| --- | --- |
| `ORA-55602` | User table is not enabled for Flashback Time Travel |
| `ORA-55636` | Table definition validation failed |

Usage Notes

- The procedure will signal an error if the base table and the history table do not have identical data definitions. For example, when columns are added or table is split, the resulting base table and history table need to have the same schema.
- The Flashback Time Travel internal history table schema has some row versions metadata columns. The procedure will signal an error if any metadata column is dropped by users.

#### 78.4.15 REGISTER\_APPLICATION Procedure

This procedure takes an application name and optionally a Flashback Archive, and registers an application for database hardening.

When database hardening is enabled, then all the security tables for that application are enabled for Flashback Archive using the given Flashback Archive. If no Flashback Archive is specified, the default Flashback Archive is used.

See Also:

[Using Flashback Time Travel](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=ADFNS-GUID-06AA782A-3F79-4235-86D5-2D136485F093) in Oracle Database Development Guide regarding database hardening

Syntax

```
DBMS_FLASHBACK_ARCHIVE.REGISTER_APPLICATION (
   application_name           IN   VARCHAR2,
   flashback_archive_name     IN    VARCHAR2 := NULL);
```

Parameters

Table 78-16 REGISTER\_APPLICATION Procedure Parameters

| Parameter | Description |
| --- | --- |
| `application_name` | Name of the application which is being registered. The application `SYSTEM` is already registered when the package is created and is populated with list of tables needed for database hardening. |
| `flashback_archive_name` | Name of the Flashback Archive in which the historical data for the security tables for given application is stored. If no Flashback Archive is specified, the default Flashback Archive is used. |

#### 78.4.16 REMOVE\_TABLE\_FROM\_APPLICATION Procedure

This procedure takes an application name and marks a table in it as no longer being a security table.

If the application is already enabled for Flashback Archive, Flashback Archive will be disabled for this table.

Syntax

```
DBMS_FLASHBACK_ARCHIVE.REMOVE_TABLE_TO_APPLICATION (
   application_name           IN   VARCHAR2,
   table_name                 IN   VARCHAR2,
   schema_name                IN   VARCHAR2 := NULL);
```

Parameters

Table 78-17 REMOVE\_TABLE\_FROM\_APPLICATION Procedure Parameters

| Parameter | Description |
| --- | --- |
| `application_name` | Name of the application for which a table is being removed from the list of security tables |
| `table_name` | Name of the table to mark as being no longer a security table for the given application |
| `schema_name` | Name of the schema containing the desired table. If no schema name is specified, the current schema is used. |

#### 78.4.17 SET\_CONTEXT\_LEVEL Procedure

This procedure defines how much of the user context is to be saved.

Syntax

```
DBMS_FLASHBACK_ARCHIVE.SET_CONTEXT_LEVEL (
   level          VARCHAR2);
```

Parameters

Table 78-18 SET\_CONTEXT\_LEVEL Procedure Parameters

| Parameter | Description |
| --- | --- |
| `level` | Depending on how much of the user context needs to be saved:  - `ALL` - the entire `SYS_CONTEXT` - `TYPICAL` - the user ID, global user ID and the hostname - `NONE` - nothing |