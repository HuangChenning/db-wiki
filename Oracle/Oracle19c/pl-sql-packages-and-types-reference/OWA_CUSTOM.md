---
title: OWA_CUSTOM
book: PL/SQL Packages and Types Reference
doc_id: E96430-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/arpls/OWA_CUSTOM.html
tags:
  - oracle
  - 19c
  - pl-sql-packages-and-types-reference
---

The `OWA_CUSTOM` package provides a Global PLSQL Agent Authorization callback function.

It is used when PLSQL Agent’s authorization scheme is set to `GLOBAL` or `CUSTOM` when there is no overriding `OWA_CUSTOM` package.

**See Also:**

For more information about implementation of this package:

- [*Oracle Fusion Middleware Administrator’s Guide for Oracle HTTP Server*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=HSADM)
- [*Oracle Fusion Middleware User’s Guide for mod\_plsql*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=YPMOD)

The chapter contains the following topics:

- Constants
- Summary of OWA\_CUSTOM Subprograms

### OWA\_CUSTOM Constants

`OWA_CUSTOM` defines several constants to use when specifying parameter values.

- `dbms_server_timezone` `CONSTANT` `VARCHAR2(3)` `:= 'PST';`
- `dbms_server_gmtdiff` `CONSTANT` `NUMBER` `:= NULL`;

### Summary of OWA\_CUSTOM Subprograms

The `AUTHORIZE` function is the only subprogram in the `OWA_CUSTOM` package.

Table 1 *OWA\_CUSTOM Package Subprograms*

| Subprogram | Description |
| --- | --- |
| AUTHORIZE Function | Provides a Global PLSQL Agent Authorization callback function |

### AUTHORIZE Function

This function is used when PLSQL Agent’s authorization scheme is set to `GLOBAL` or `CUSTOM` when there is no overriding `OWA_CUSTOM` package.

**Syntax**

```md
OWA_CUSTOM.AUTHORIZE
  RETURN BOOLEAN;
```