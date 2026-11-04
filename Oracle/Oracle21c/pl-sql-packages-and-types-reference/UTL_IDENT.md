---
title: PL/SQL Packages and Types Reference
book: Database PL/SQL Packages and Types Reference
doc_id: F31492-25
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/arpls/UTL_IDENT.html
tags:
  - oracle
  - 21c
  - pl-sql-packages-and-types-reference
---

## 270 UTL\_IDENT

The `UTL_IDENT` package specifies which Database or client PL/SQL is running.

This chapter contains the following topics:

### 270.1 UTL\_IDENT Overview

The `UTL_IDENT` package is intended for use for conditional compilation of PL/SQL packages that are supported by Oracle, TimesTen Database, and clients such as Oracle Forms.

### 270.2 UTL\_IDENT Security Model

The `UTL_IDENT` package runs as the package owner `SYS`. The public synonym `UTL_IDENT`, and `EXECUTE` permission on this package is granted to `PUBLIC`.

### 270.3 UTL\_IDENT Constants

The `UTL_IDENT` package defines several constants to use when specifying parameter values.

These constants are shown in the following table.

Table 270-1 UTL\_IDENT Constants

| Constant | Type | Value | Description |
| --- | --- | --- | --- |
| `IS_ORACLE_SERVER` | `BOOLEAN` | `TRUE/FALSE` | Stipulates if Oracle Server or not |
| `IS_ORACLE_CLIENT` | `BOOLEAN` | `TRUE/FALSE` | Stipulates if Oracle Client or not |
| `IS_TIMESTEN` | `BOOLEAN` | `TRUE/FALSE` | Stipulates if TimesTen or not |
| `IS_ORACLE_FORMS` | `BOOLEAN` | `TRUE/FALSE` | Stipulates if Oracle Forms or not |