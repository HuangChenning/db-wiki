---
title: SQL Language Reference
book: SQL Language Reference
doc_id: E83703-08
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/sqlrf/ROUND-date.html
tags:
  - oracle
  - 12c
  - sql-language-reference
---

Syntax

round\_date::=

![round_date](img/round_date.gif)

> ```
> ROUND(date [, fmt ])
> ```


Purpose

`ROUND` returns `date` rounded to the unit specified by the format model `fmt`. This function is not sensitive to the `NLS_CALENDAR` session parameter. It operates according to the rules of the Gregorian calendar. The value returned is always of data type `DATE`, even if you specify a different datetime data type for `date`. If you omit `fmt`, then `date` is rounded to the nearest day. The `date` expression must resolve to a `DATE` value.

See Also:

" [ROUND and TRUNC Date Functions](ROUND-and-TRUNC-Date-Functions.md) " for the permitted format models to use in `fmt`

Examples

The following example rounds a date to the first day of the following year:

```
SELECT ROUND (TO_DATE ('27-OCT-00'),'YEAR')
   "New Year" FROM DUAL;
 
New Year
---------
01-JAN-01
```