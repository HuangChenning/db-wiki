---
title: FROM_TZ
book: SQL Language Reference
doc_id: E96310-37
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/FROM_TZ.html
tags:
  - oracle
  - 19c
  - sql-language-reference
---

## Syntax

![from_tz](img/from_tz.gif)

> ```
> FROM_TZ(timestamp_value, time_zone_value)
> ```
>
> [Copyright ©](https://docs.oracle.com/pls/topic/lookup?ctx=en/legal&id=cpyr) 2026,1996, Oracle and/or its affiliates.


[Description of the illustration from\_tz.eps](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/img_text/from_tz.html)

## Purpose

`FROM_TZ` converts a timestamp value and a time zone to a `TIMESTAMP` `WITH` `TIME` `ZONE` value. *time\_zone\_value* is a character string in the format `'TZH:TZM'` or a character expression that returns a string in `TZR` with optional `TZD` format.

## Examples

The following example returns a timestamp value to `TIMESTAMP` `WITH` `TIME` `ZONE`:

```md
SELECT FROM_TZ(TIMESTAMP '2000-03-28 08:00:00', '3:00')
  FROM DUAL;

FROM_TZ(TIMESTAMP'2000-03-2808:00:00','3:00')
---------------------------------------------------------------
28-MAR-00 08.00.000000000 AM +03:00
```