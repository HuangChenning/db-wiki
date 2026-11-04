---
title: PL/SQL Packages and Types Reference
book: Database PL/SQL Packages and Types Reference
doc_id: F31492-25
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/arpls/DBMS_EDITIONS_UTILITIES.html
tags:
  - oracle
  - 21c
  - pl-sql-packages-and-types-reference
---

## 71 DBMS\_EDITIONS\_UTILITIES

### 71.1 DBMS\_EDITIONS\_UTILITIES Overview

The `DBMS_EDITIONS_UTILITIES` package implements an interface which provides helper functions for edition-related operations.

### 71.2 DBMS\_EDITIONS\_UTILITIES Security Model

This package is owned by `SYS` with execute access granted to `PUBLIC`. It runs with invoker's rights, that is, with the security profile of the caller.

### 71.3 DBMS\_EDITIONS\_UTILITIES Exceptions

The table in this topic lists exception messages created by DBMS\_EDITIONS\_UTILITIES.

Table 71-1 DBMS\_EDITIONS\_UTILITIES Error Messages

| Error | Description |
| --- | --- |
| `ORA-38817` | Insufficient privileges |
| `ORA-942` | Missing table |

### 71.4 Summary of DBMS\_EDITIONS\_UTILITIES Subprograms

This table lists and describes the `DBMS_EDITIONS_UTILITIES` package subprograms.

Table 71-2 DBMS\_EDITIONS\_UTILITIES Package Subprograms

| Subprogram | Description |
| --- | --- |
| CLEAN\_UNUSABLE\_EDITIONS Procedure | Drops covered objects in unusable editions, and drops empty unusable editions if possible. |
| SET\_EDITIONING\_VIEWS\_READ\_ONLY Procedure | Given the schema name and table name, this procedure sets the corresponding editioning views in all editions to `READ` `ONLY` or `READ/WRITE` |
| SET\_NULL\_COLUMN\_VALUES\_TO\_EXPR Procedure | For use only during an edition-based redefinition (EBR) exercise |

#### 71.4.1 CLEAN\_UNUSABLE\_EDITIONS Procedure

Drops all covered objects in any unusable editions and drops empty unusable editions.

Syntax

The `CLEAN_UNUSABLE_EDITIONS` procedure executes immediately and in its entirety.

```
DBMS_EDITIONS_UTILITIES.CLEAN_UNUSABLE_EDITIONS ( );
```

Usage Notes

The `COMPATIBLE` parameter must be set to 12.2.0 or higher for this procedure to execute.

See Also:

- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=SQLRF-GUID-726082F7-C931-4975-8F2B-5EA814A51AB0) for information about `DROP EDITION`
- [Oracle Database Development Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=ADFNS-GUID-E6DBE175-2598-430F-9D0A-AB22CAE7DDDA) for more information about using edition-based redefinition

#### 71.4.2 SET\_EDITIONING\_VIEWS\_READ\_ONLY Procedure

Given the schema name and table name, this procedure sets the corresponding editioning views in all editions to `READ` `ONLY` or `READ/WRITE`.

Syntax

```
DBMS_EDITIONS_UTILITIES.SET_EDITIONING_VIEWS_READ_ONLY (
   table_name IN VARCHAR2,
   owner      IN VARCHAR2 DEFAULT NULL,
   read_only  IN BOOLEAN  DEFAULT TRUE);
```

Parameters

Table 71-3 SET\_EDITIONING\_VIEWS\_READ\_ONLY Procedure Parameters

| Parameter | Description |
| --- | --- |
| `table_name` | Base table of the editioning views |
| `owner` | Base table schema. The default (or `NULL`) is the current schema. |
| `read_only` | `TRUE` to set the views to read-only; `FALSE` (or `NULL`) sets the views to `READ/WRITE`. Default is `TRUE`. |

Usage Notes

The user must have the following privileges:

- Owner of the table, or have the `ALTER` `ANY` `TABLE` system privileges
- `USE` object privilege on all the editions for which the views are defined

#### 71.4.3 SET\_NULL\_COLUMN\_VALUES\_TO\_EXPR Procedure

This procedure replaces `NULL` values in a replacement column with the value of an expression.

The expression evaluation cost is deferred to future updates and queries. The procedure is intended for use only during an edition-based redefinition (EBR) exercise.

See Also:

- [Oracle Database Development Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=ADFNS99907) regarding transforming pre- to post-upgrade representation

Syntax

```
DBMS_EDITIONS_UTILITIES.SET_NULL_COLUMN_VALUES_TO_EXPR;
   table_name    IN  VARCHAR2,
   column_name   IN  VARCHAR2,
   expression    IN  VARCHAR2);
```

Parameters

Table 71-4 SET\_NULL\_COLUMN\_VALUES\_TO\_EXPR Procedure Parameters

| Parameter | Description |
| --- | --- |
| `table_name` | A potentially schema-qualified table name |
| `column_name` | Name of the column to be updated |
| `expression` | An expression composed of columns in the same table, constants, and SQL functions |