---
title: "User's Guide and Reference"
book: "SQL*Plus User's Guide and Reference"
doc_id: E96459-09
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/sqpug/UNDEFINE.html
tags:
  - oracle
  - 19c
  - sqlplus-users-guide-and-reference
---

## 12.50 UNDEFINE

Syntax

```
UNDEF[INE] variable ...
```

where variable represents the name of the substitution variable you want to delete.

Deletes one or more substitution variables that you defined either explicitly (with the DEFINE command) or implicitly (with an argument to the START command).

Examples

To undefine a substitution variable named POS, enter

```
UNDEFINE POS
```

To undefine two substitution variables named MYVAR1 and MYVAR2, enter

```
UNDEFINE MYVAR1 MYVAR2
```