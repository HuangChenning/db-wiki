---
title: OWA_CUSTOM
book: PL/SQL Packages and Types Reference
doc_id: E40758-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/w_custom.htm
tags:
  - oracle
  - 11g
  - pl-sql-packages-and-types-reference
---

## 189 OWA\_CUSTOM

The `OWA_CUSTOM` package provides a Global PLSQL Agent Authorization callback function. It is used when PLSQL Agent's authorization scheme is set to `GLOBAL` or `CUSTOM` when there is no overriding `OWA_CUSTOM` package.

See Also:

For more information about implementation of this package:
- [Oracle Fusion Middleware Administrator's Guide for Oracle HTTP Server](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=HSADM)
- [Oracle Fusion Middleware User's Guide for mod\_plsql](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=YPMOD)

The chapter contains the following topics:

- Using OWA\_CUSTOM
	- Constants
- Summary of OWA\_CUSTOM Subprograms

---

## Using OWA\_CUSTOM

- Constants

---

### Constants

- `dbms_server_timezone` `CONSTANT` `VARCHAR2(3)` `:= 'PST';`
- `dbms_server_gmtdiff` `CONSTANT` `NUMBER` `:= NULL`;

---

## Summary of OWA\_CUSTOM Subprograms

Table 189-1 OWA\_CUSTOM Package Subprograms

| Subprogram | Description |
| --- | --- |
| AUTHORIZE Function | Provides a Global PLSQL Agent Authorization callback function |

---

### AUTHORIZE Function

This function is used when PLSQL Agent's authorization scheme is set to `GLOBAL` or `CUSTOM` when there is no overriding `OWA_CUSTOM` package.

Syntax

```
OWA_CUSTOM.AUTHORIZE 
  RETURN BOOLEAN;
```