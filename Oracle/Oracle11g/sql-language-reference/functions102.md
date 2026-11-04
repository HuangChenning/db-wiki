---
title: MONTHS_BETWEEN
book: SQL Language Reference
doc_id: E41084-04
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e41084/functions102.htm
tags:
  - oracle
  - 11g
  - sql-language-reference
---

Syntax

  
[Description of the illustration ''months\_between.gif''](https://docs.oracle.com/cd/E11882_01/server.112/e41084/img_text/months_between.htm)  
  

Purpose

`MONTHS_BETWEEN` returns number of months between dates `date1` and `date2`. The month and the last day of the month are defined by the parameter `NLS_CALENDAR`. If `date1` is later than `date2`, then the result is positive. If `date1` is earlier than `date2`, then the result is negative. If `date1` and `date2` are either the same days of the month or both last days of months, then the result is always an integer. Otherwise Oracle Database calculates the fractional portion of the result based on a 31-day month and considers the difference in time components `date1` and `date2`.

Examples

The following example calculates the months between two dates:

```
SELECT MONTHS_BETWEEN
       (TO_DATE('02-02-1995','MM-DD-YYYY'),
        TO_DATE('01-01-1995','MM-DD-YYYY') ) "Months"
  FROM DUAL;

    Months
----------
1.03225806
```