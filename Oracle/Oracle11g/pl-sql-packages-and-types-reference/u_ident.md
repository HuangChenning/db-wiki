---
title: UTL_IDENT
book: PL/SQL Packages and Types Reference
doc_id: E40758-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/u_ident.htm
tags:
  - oracle
  - 11g
  - pl-sql-packages-and-types-reference
---

## 228 UTL\_IDENT

The `UTL_IDENT` package specifies which Database or client PL/SQL is running.

This chapter contains the following topics:

- Using UTL\_IDENT

---

## Using UTL\_IDENT

This section contains topics which relate to using the `UTL_IDENT` package.

---

### Overview

The `UTL_IDENT` package is intended for use for conditional compilation of PL/SQL packages that are supported by Oracle, TimesTen Database, and clients such as Oracle Forms.

---

### Security Model

The `UTL_IDENT` package runs as the package owner `SYS`. The public synonym `UTL_IDENT`, and `EXECUTE` permission on this package is granted to `PUBLIC`.

---

### Constants

The `UTL_IDENT` package uses the constants shown in Table 228-1, "UTL\_IDENT Constants".

Table 228-1 UTL\_IDENT Constants

| Constant | Type | Value | Description |
| --- | --- | --- | --- |
| `IS_ORACLE_SERVER` | `BOOLEAN` | `TRUE/FALSE` | Stipulates if Oracle Server or not |
| `IS_ORACLE_CLIENT` | `BOOLEAN` | `TRUE/FALSE` | Stipulates if Oracle Client or not |
| `IS_TIMESTEN` | `BOOLEAN` | `TRUE/FALSE` | Stipulates if TimesTen or not |
| `IS_ORACLE_FORMS` | `BOOLEAN` | `TRUE/FALSE` | Stipulates if Oracle Forms or not |