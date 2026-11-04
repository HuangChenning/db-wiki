---
title: SQL Language Reference
book: SQL Language Reference
doc_id: E83703-08
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/sqlrf/UID.html
tags:
  - oracle
  - 12c
  - sql-language-reference
---

Syntax

![uid](img/uid.gif)

> ```
> UID
> ```


Purpose

`UID` returns an integer that uniquely identifies the session user (the user who logged on).

See Also:

[USER](USER.md) to learn how Oracle Database determines the session user

Examples

The following example returns the UID of the session user:

```
SELECT UID FROM DUAL;
```