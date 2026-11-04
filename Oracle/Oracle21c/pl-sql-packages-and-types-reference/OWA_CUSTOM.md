---
title: PL/SQL Packages and Types Reference
book: Database PL/SQL Packages and Types Reference
doc_id: F31492-25
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/arpls/OWA_CUSTOM.html
tags:
  - oracle
  - 21c
  - pl-sql-packages-and-types-reference
---

## 228 OWA\_CUSTOM

The `OWA_CUSTOM` package provides a Global PLSQL Agent Authorization callback function.

It is used when PLSQL Agent's authorization scheme is set to `GLOBAL` or `CUSTOM` when there is no overriding `OWA_CUSTOM` package.

See Also:

For more information about implementation of this package:

- [Oracle Fusion Middleware Administrator's Guide for Oracle HTTP Server](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=HSADM)
- [Oracle Fusion Middleware User's Guide for mod\_plsql](https://docs.oracle.com/cd/E23943_01/portal.1111/e12041/toc.htm)

The chapter contains the following topics:

- Constants
- Summary of OWA\_CUSTOM Subprograms

### 228.1 OWA\_CUSTOM Constants

`OWA_CUSTOM` defines several constants to use when specifying parameter values.

- `dbms_server_timezone` `CONSTANT` `VARCHAR2(3)` `:= 'PST';`
- `dbms_server_gmtdiff` `CONSTANT` `NUMBER` `:= NULL`;

### 228.2 Summary of OWA\_CUSTOM Subprograms

The `AUTHORIZE` function is the only subprogram in the `OWA_CUSTOM` package.

Table 228-1 OWA\_CUSTOM Package Subprograms

| Subprogram | Description |
| --- | --- |
| AUTHORIZE Function | Provides a Global PLSQL Agent Authorization callback function |

#### 228.2.1 AUTHORIZE Function

This function is used when PLSQL Agent's authorization scheme is set to `GLOBAL` or `CUSTOM` when there is no overriding `OWA_CUSTOM` package.

Syntax

```
OWA_CUSTOM.AUTHORIZE 
  RETURN BOOLEAN;
```