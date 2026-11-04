---
title: PL/SQL Packages and Types Reference
book: Database PL/SQL Packages and Types Reference
doc_id: F31492-25
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/arpls/dbms_immutable_table.html
tags:
  - oracle
  - 21c
  - pl-sql-packages-and-types-reference
---

## 94 DBMS\_IMMUTABLE\_TABLE

Immutable tables are read-only tables that protect data against unauthorized modification. They also prevent against accidental data modifications that may be caused by human errors. The `DBMS_IMMUTABLE_TABLE` package allows you to delete the expired rows in an immutable table.

This chapter contains the following topics:

See Also:

- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=ADMIN-GUID-707B02F5-E589-4C20-8E2E-5ED4F7888702)
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=SQLRF54484)
- [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=REFRN)

### 94.1 DBMS\_IMMUTABLE\_TABLE Overview

Immutable tables are `read-only` tables that protect data against unauthorized modification. Immutable tables also prevent against accidental data modifications that may be caused by human errors. You must specify a retention period for the immutable table and for rows within the immutable table. An immutable table can be dropped if it contains no rows or if the specified retention period for the table has lapsed. Rows can be deleted from an immutable table only after the specified retention period for rows in the table has elapsed. Except for increasing the retention periods, you cannot modify the definition of an immutable table.

### 94.2 DBMS\_IMMUTABLE\_TABLE Security Model

The `DBMS_IMMUTABLE_TABLE` package is owned by `SYS` and is installed as part of database installation. The routines in the package are run with invoker's rights and hence run with the privileges of the current user.

### 94.3 Summary of DBMS\_IMMUTABLE\_TABLE Subprograms

This table lists the `DBMS_IMMUTABLE_TABLE` subprograms in alphabetical order and briefly describes them.

Table 94-1 DBMS\_IMMUTABLE\_TABLE Package Subprograms

| Subprogram | Description |
| --- | --- |
| DELETE\_EXPIRED\_ROWS Procedure | This procedure deletes the expired rows. |

#### 94.3.1 DELETE\_EXPIRED\_ROWS Procedure

This procedure deletes some or all of the expired rows from the immutable table. This procedure does not commit.

Syntax

```
DBMS_IMMUTABLE_TABLE.DELETE_EXPIRED_ROWS(
   schema_name                  IN VARCHAR2,
   table_name                   IN VARCHAR2, 
   before_timestamp             IN TIMESTAMP WITH TIME ZONE DEFAULT NULL,
   number_of_rows_deleted       OUT NUMBER);
```

Parameters

Table 94-2 DELETE\_EXPIRED\_ROWS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `schema_name` | The name of the schema. |
| `table_name` | The name of the immutable table. |
| `before_timestamp` | If the parameter is `NULL`, all expired rows in the table are deleted. If the parameter is not `NULL` and older than the timestamp calculated based on current time and row retention time, rows with timestamps less than the parameter value are deleted. If the parameter is younger than the timestamp calculated based on the current time and row retention time, the calculated timestamp is used, and all expired rows are deleted.  The default value is `NULL`. |
| `number_of_rows_deleted` | The number of rows deleted. |