---
title: NEXT_DAY
book: SQL Language Reference
doc_id: E96310-37
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/NEXT_DAY.html
tags:
  - oracle
  - 19c
  - sql-language-reference
---

## Syntax

![next_day](img/next_day.gif)

> ```
> NEXT_DAY(date, char)
> ```
>
> [Copyright ©](https://docs.oracle.com/pls/topic/lookup?ctx=en/legal&id=cpyr) 2026,1996, Oracle and/or its affiliates.


[Description of the illustration next\_day.eps](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/img_text/next_day.html)

## Purpose

`NEXT_DAY` returns the date of the first weekday named by *char* that is later than the date *date*. The return type is always `DATE`, regardless of the data type of *date*. The argument *char* must be a day of the week in the date language of your session, either the full name or the abbreviation. The minimum number of letters required is the number of letters in the abbreviated version. Any characters immediately following the valid abbreviation are ignored. The return value has the same hours, minutes, and seconds component as the argument *date*.

## Examples

This example returns the date of the next Tuesday after October 15, 2009:

```md
SELECT NEXT_DAY('15-OCT-2009','TUESDAY') "NEXT DAY"
  FROM DUAL;

NEXT DAY
--------------------
20-OCT-2009 00:00:00
```