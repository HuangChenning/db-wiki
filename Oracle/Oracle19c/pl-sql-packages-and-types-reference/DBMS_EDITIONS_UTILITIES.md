---
title: DBMS_EDITIONS_UTILITIES
book: PL/SQL Packages and Types Reference
doc_id: E96430-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/arpls/DBMS_EDITIONS_UTILITIES.html
tags:
  - oracle
  - 19c
  - pl-sql-packages-and-types-reference
---

The `DBMS_EDITIONS_UTILITIES` package provides helper functions for edition-related operations.

The chapter contains the following topics:

### DBMS\_EDITIONS\_UTILITIES Overview

The `DBMS_EDITIONS_UTILITIES` package implements an interface which provides helper functions for edition-related operations.

### DBMS\_EDITIONS\_UTILITIES Security Model

This package is owned by `SYS` with execute access granted to `PUBLIC`. It runs with invoker’s rights, that is, with the security profile of the caller.

### DBMS\_EDITIONS\_UTILITIES Exceptions

The table in this topic lists exception messages created by DBMS\_EDITIONS\_UTILITIES.

Table 1 DBMS\_EDITIONS\_UTILITIES Error Messages

| Error | Description |
| --- | --- |
| `ORA-38817` | Insufficient privileges |
| `ORA-942` | Missing table |

### Summary of DBMS\_EDITIONS\_UTILITIES Subprograms

This table lists and describes the `DBMS_EDITIONS_UTILITIES` package subprograms.

Table 2 DBMS\_EDITIONS\_UTILITIES Package Subprograms

| Subprogram | Description |
| --- | --- |
| CLEAN\_UNUSABLE\_EDITIONS Procedure | Drops covered objects in unusable editions, and drops empty unusable editions if possible. |
| SET\_EDITIONING\_VIEWS\_READ\_ONLY Procedure | Given the schema name and table name, this procedure sets the corresponding editioning views in all editions to `READ` `ONLY` or `READ/WRITE` |
| SET\_NULL\_COLUMN\_VALUES\_TO\_EXPR Procedure | For use only during an edition-based redefinition (EBR) exercise |

### CLEAN\_UNUSABLE\_EDITIONS Procedure

Drops all covered objects in any unusable editions and drops empty unusable editions.

**Syntax**

The `CLEAN_UNUSABLE_EDITIONS` procedure executes immediately and in its entirety.

```md
<!--Draft comment: <br/>DB18.1.0 Feature# 71314-26-->DBMS_EDITIONS_UTILITIES.CLEAN_UNUSABLE_EDITIONS ( );
```

**Usage Notes**

The `COMPATIBLE` parameter must be set to 12.2.0 or higher for this procedure to execute.

**See Also:**

- [*Oracle Database SQL Language Reference*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=SQLRF-GUID-726082F7-C931-4975-8F2B-5EA814A51AB0) for information about `DROP EDITION`
- [*Oracle Database Development Guide*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=ADFNS-GUID-E6DBE175-2598-430F-9D0A-AB22CAE7DDDA) for more information about using edition-based redefinition

### SET\_EDITIONING\_VIEWS\_READ\_ONLY Procedure

Given the schema name and table name, this procedure sets the corresponding editioning views in all editions to `READ` `ONLY` or `READ/WRITE`.

**Syntax**

```md
DBMS_EDITIONS_UTILITIES.SET_EDITIONING_VIEWS_READ_ONLY (
   table_name IN VARCHAR2,
   owner      IN VARCHAR2 DEFAULT NULL,
   read_only  IN BOOLEAN  DEFAULT TRUE);
```

**Parameters**

Table 3 SET\_EDITIONING\_VIEWS\_READ\_ONLY Procedure Parameters

| Parameter | Description |
| --- | --- |
| `table_name` | Base table of the editioning views |
| `owner` | Base table schema. The default (or `NULL`) is the current schema. |
| `read_only` | `TRUE` to set the views to read-only; `FALSE` (or `NULL`) sets the views to `READ/WRITE`. Default is `TRUE`. |

**Usage Notes**

The user must have the following privileges:

- Owner of the table, or have the `ALTER` `ANY` `TABLE` system privileges
- `USE` object privilege on all the editions for which the views are defined

### SET\_NULL\_COLUMN\_VALUES\_TO\_EXPR Procedure

This procedure replaces `NULL` values in a replacement column with the value of an expression.

The expression evaluation cost is deferred to future updates and queries. The procedure is intended for use only during an edition-based redefinition (EBR) exercise.

**See Also:**

- [*Oracle Database Development Guide*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=ADFNS99907) regarding transforming pre- to post-upgrade representation

**Syntax**

```md
DBMS_EDITIONS_UTILITIES.SET_NULL_COLUMN_VALUES_TO_EXPR;
   table_name    IN  VARCHAR2,
   column_name   IN  VARCHAR2,
   expression    IN  VARCHAR2);
```

**Parameters**

Table 4 SET\_NULL\_COLUMN\_VALUES\_TO\_EXPR Procedure Parameters

| Parameter | Description |
| --- | --- |
| `table_name` | A potentially schema-qualified table name |
| `column_name` | Name of the column to be updated |
| `expression` | An expression composed of columns in the same table, constants, and SQL functions |