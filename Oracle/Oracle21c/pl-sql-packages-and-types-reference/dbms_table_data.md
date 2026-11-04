---
title: PL/SQL Packages and Types Reference
book: Database PL/SQL Packages and Types Reference
doc_id: F31492-25
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/arpls/dbms_table_data.html
tags:
  - oracle
  - 21c
  - pl-sql-packages-and-types-reference
---

## 180 DBMS\_TABLE\_DATA

The `DBMS_TABLE_DATA` package provides procedures that can be used to retrieve the byte value of a single column, or a series of columns, in any table. These procedures, along with a publicly documented meta-data structure for columns, can be used to retrieve the row content for row data on which the hash or user signature is computed.

This chapter contains the following topics:

### 180.1 DBMS\_TABLE\_DATA Overview

The `DBMS_TABLE_DATA` package can be used to retrieve the byte value of a single column, or a series of columns, in any table.

These procedures, along with a publicly documented meta-data structure for columns, can be used to retrieve the `row content` for row data on which the hash or user signature is computed.

The procedures provide platform-neutral binary values for columns.

The procedures give you fine-grained control over the scope of a digital signature or cryptographic hash in terms of the columns you extract and the order in which you assemble the results.

### 180.2 DBMS\_TABLE\_DATA Security Model

The `DBMS_TABLE_DATA` package is owned by `SYS` and is installed as part of database installation. The routines in the package are run with invokers' rights (run with the privileges of the current user). The current user needs `SELECT` privileges on the table to extract column data.

### 180.3 Summary of DBMS\_TABLE\_DATA Subprograms

The `DBMS_TABLE_DATA` package uses `GET_BYTES_FOR_COLUMN`, `GET_BYTES_FOR_COLUMNS`, and `GET_BYTES_FOR_ROW` subprograms to perform various functions.

Table 180-1 DBMS\_TABLE\_DATA Package Subprograms

| Subprogram | Description |
| --- | --- |
| GET\_BYTES\_FOR\_COLUMN Procedure | Returns the `column_data` in bytes for the particular column with name `column_name for row_id` row in the particular table identified by `schema_name.table_name`. |
| GET\_BYTES\_FOR\_COLUMNS Procedure | Returns a concatenated array of column byte values in `column_data` in the order of columns specified in the `column_names` array. |
| GET\_BYTES\_FOR\_ROW Procedure | Returns a concatenated array of column byte values in `column_data` in the order of column positions for the particular row identified by `row_id`. |

#### 180.3.1 GET\_BYTES\_FOR\_COLUMN Procedure

This procedure returns the `column_data` in bytes for the particular column with name `column_name` for `row_id` row in the particular table identified by `schema_name.table_name`.

Syntax

```
DBMS_TABLE_DATA.GET_BYTES_FOR_COLUMN(
   schema_name          IN VARCHAR2,
   table_name              IN VARCHAR2, 
   row_id                  IN ROWID,
   column_name             IN VARCHAR2, 
   column_data             IN OUT BLOB);
```

Parameters

Table 180-2 GET\_BYTES\_FOR\_COLUMN Procedure Parameters

| Parameter | Description |
| --- | --- |
| `schema_name` | The name of the schema. |
| `table_name` | The name of the table. |
| `row_id` | The row id. |
| `column_name` | The column name. |
| `column_data` | The data in the column. |

Usage Notes

All arguments are required.

#### 180.3.2 GET\_BYTES\_FOR\_COLUMNS Procedure

This procedure returns a concatenated array of column byte values in `column_data` in the order of columns specified in the `column_names` array.

Syntax

```
DBMS_TABLE_DATA.GET_BYTES_FOR_COLUMNS(
   schema_name          IN VARCHAR2,
   table_name              IN VARCHAR2, 
   row_id                  IN ROWID,
   column_names            IN VARCHAR2, 
   column_data             IN OUT BLOB);
```

Parameters

Table 180-3 GET\_BYTES\_FOR\_COLUMNS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `schema_name` | The name of the schema. |
| `table_name` | The name of the table. |
| `row_id` | The row id. |
| `column_names` | The names of the columns. |
| `column_data` | The data in the columns. |

Usage Notes

All arguments are required.

#### 180.3.3 GET\_BYTES\_FOR\_ROW Procedure

This procedure returns a concatenated array of column byte values in `column_data` in the order of column positions for the particular row identified by `row_id`.

Syntax

```
DBMS_TABLE_DATA.GET_BYTES_FOR_ROW(
   schema_name          IN VARCHAR2,
   table_name              IN VARCHAR2, 
   row_id                  IN ROWID,
   column_data             IN OUT BLOB);
```

Parameters

Table 180-4 GET\_BYTES\_FOR\_ROW Procedure Parameters

| Parameter | Description |
| --- | --- |
| `schema_name` | The name of the schema. |
| `table_name` | The name of the table. |
| `row_id` | The row id. |
| `column_data` | The data in the row. |

Usage Notes

All arguments are required.