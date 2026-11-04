---
title: SQL Language Reference
book: SQL Language Reference
doc_id: E83703-08
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/sqlrf/CHARTOROWID.html
tags:
  - oracle
  - 12c
  - sql-language-reference
---

Syntax

![chartorowid](img/chartorowid.gif)

> ```
> CHARTOROWID(char)
> ```


Purpose

`CHARTOROWID` converts a value from `CHAR`, `VARCHAR2`, `NCHAR`, or `NVARCHAR2` data type to `ROWID` data type.

This function does not support `CLOB` data directly. However, `CLOB` s can be passed in as arguments through implicit data conversion.

See Also:

[Data Type Comparison Rules](Data-Type-Comparison-Rules.md) for more information.

Examples

The following example converts a character rowid representation to a rowid. (The actual rowid is different for each database instance.)

```
SELECT last_name
  FROM employees
  WHERE ROWID = CHARTOROWID('AAAFd1AAFAAAABSAA/');
 
LAST_NAME
-------------------------
Greene
```