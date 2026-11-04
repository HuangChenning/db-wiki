---
title: ROUND and TRUNC Date Functions
book: SQL Language Reference
doc_id: E96310-37
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/ROUND-and-TRUNC-Date-Functions.html
tags:
  - oracle
  - 19c
  - sql-language-reference
---

Table 7-13 lists the format models you can use with the `ROUND` and `TRUNC` date functions and the units to which they round and truncate dates. The default model, ‘DD’, returns the date rounded or truncated to the day with a time of midnight.

Table 13 Date Format Models for the ROUND and TRUNC Date Functions

| Format Model | Rounding or Truncating Unit |
| --- | --- |
| ```md CC SCC ``` | One greater than the first two digits of a four-digit year |
| ```md SYYYY YYYY YEAR SYEAR YYY YY Y ``` | Year (rounds up on July 1) |
| ```md IYYY IY IY I ``` | Year containing the calendar week, as defined by the ISO 8601 standard |
| ```md Q ``` | Quarter (rounds up on the sixteenth day of the second month of the quarter) |
| ```md MONTH MON MM RM ``` | Month (rounds up on the sixteenth day) |
| ```md WW ``` | Same day of the week as the first day of the year |
| ```md IW ``` | Same day of the week as the first day of the calendar week as defined by the ISO 8601 standard, which is Monday |
| ```md W ``` | Same day of the week as the first day of the month |
| ```md DDD DD J ``` | Day |
| ```md DAY DY D ``` | Starting day of the week |
| ```md HH HH12 HH24 ``` | Hour |
| ```md MI ``` | Minute |

The starting day of the week used by the format models DAY, DY, and D is specified implicitly by the initialization parameter `NLS_TERRITORY`.

**See Also:** [*Oracle Database Reference*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/sqlrf&id=REFRN10128) and [*Oracle Database Globalization Support Guide*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/sqlrf&id=NLSPG003) for information on this parameter