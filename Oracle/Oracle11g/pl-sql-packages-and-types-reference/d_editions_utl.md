---
title: DBMS_EDITIONS_UTILITIES
book: PL/SQL Packages and Types Reference
doc_id: E40758-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/d_editions_utl.htm
tags:
  - oracle
  - 11g
  - pl-sql-packages-and-types-reference
---

## 62 DBMS\_EDITIONS\_UTILITIES

The `DBMS_EDITIONS_UTILITIES` package implements the Edition API which provides helper functions for edition-related operations.

The chapter contains the following topics:

- Using DBMS\_EDITIONS\_UTILITIES
- Summary of DBMS\_EDITIONS\_UTILITIES Subprograms

---

## Using DBMS\_EDITIONS\_UTILITIES

---

### Security Model

This package is owned by `SYS` with execute access granted to `PUBLIC`. It runs with invokers rights, that is, with the security profile of the caller.

---

### Exceptions

Table 62-1 DBMS\_EDITIONS\_UTILITIES Error Messages

| Error | Description |
| --- | --- |
| `ORA-38817` | Insufficient privileges |
| `ORA-942` | Missing table |

---

## Summary of DBMS\_EDITIONS\_UTILITIES Subprograms

Table 62-2 DBMS\_EDITIONS\_UTILITIES Package Subprograms

| Subprogram | Description |
| --- | --- |
| SET\_EDITIONING\_VIEWS\_READ\_ONLY Procedure | Given the schema name and table name, this procedure sets the corresponding editioning views in all editions to `READ` `ONLY` or `READ/WRITE` |

---

### SET\_EDITIONING\_VIEWS\_READ\_ONLY Procedure

Given the schema name and table name, this procedure sets the corresponding editioning views in all editions to `READ` `ONLY` or `READ/WRITE`.

Syntax

```
DBMS_EDITIONS_UTILITIES.SET_EDITIONING_VIEWS_READ_ONLY (
   table_name IN VARCHAR2,
   owner      IN VARCHAR2 DEFAULT NULL,
   read_only  IN BOOLEAN  DEFAULT TRUE);
```

Parameters

Table 62-3 SET\_EDITIONING\_VIEWS\_READ\_ONLY Procedure Parameters

| Parameter | Description |
| --- | --- |
| `table_name` | Base table of the editioning views |
| `owner` | Base table schema. The default (or `NULL`) is the current schema. |
| `read_only` | `TRUE` to set the views to read-only; `FALSE` (or `NULL`) sets the views to `READ/WRITE`. Default is `TRUE`. |

Usage Notes

The user must have the following privileges:

- Owner of the table, or have the `ALTER` `ANY` `TABLE` system privileges
- `USE` object privilege on all the editions for which the views are defined