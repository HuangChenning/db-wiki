---
title: SQL Language Reference
book: SQL Language Reference
doc_id: F31301-19
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/sqlrf/UID.html
tags:
  - oracle
  - 21c
  - sql-language-reference
---

## UID

Syntax

![uid](img/uid.gif)

> ```
> UID
> ```
>
> ![Oracle Logo](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/gifs/oracle.gif)[  
> Copyright © 1996, 2025, Oracle and/or its affiliates.](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/html/cpyr.htm)


Purpose

`UID` returns an integer that uniquely identifies the session user (the user who logged on).

See Also:

[USER](USER.md) to learn how Oracle Database determines the session user

Examples

The following example returns the UID of the session user:

```
SELECT UID FROM DUAL;
```