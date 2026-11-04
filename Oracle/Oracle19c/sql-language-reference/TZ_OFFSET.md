---
title: TZ_OFFSET
book: SQL Language Reference
doc_id: E96310-37
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/TZ_OFFSET.html
tags:
  - oracle
  - 19c
  - sql-language-reference
---

## Syntax

![tz_offset](img/tz_offset.gif)

> ```
> TZ_OFFSET({ 'time_zone_name'
>           | '{ + | - } hh : mi'
>           | SESSIONTIMEZONE
>           | DBTIMEZONE
>           }
>          )
> ```
>
> [Copyright ©](https://docs.oracle.com/pls/topic/lookup?ctx=en/legal&id=cpyr) 2026,1996, Oracle and/or its affiliates.


[Description of the illustration tz\_offset.eps](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/img_text/tz_offset.html)

## Purpose

`TZ_OFFSET` returns the time zone offset corresponding to the argument based on the date the statement is executed. You can enter a valid time zone region name, a time zone offset from UTC (which simply returns itself), or the keyword `SESSIONTIMEZONE` or `DBTIMEZONE`. For a listing of valid values for *time\_zone\_name*, query the `TZNAME` column of the `V$TIMEZONE_NAMES` dynamic performance view.

**Note:** Time zone region names are needed by the daylight saving feature. These names are stored in two types of time zone files: one large and one small. One of these files is the default file, depending on your environment and the release of Oracle Database you are using. For more information regarding time zone files and names, see [*Oracle Database Globalization Support Guide*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/sqlrf&id=NLSPG014).

**See Also:**

- in [*Oracle Database Globalization Support Guide*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/sqlrf&id=NLSPG-GUID-AFCE41ED-775B-4A00-AF38-C436776AE0C5) for the collation derivation rules, which define the collation assigned to the character return value of `TZ_OFFSET`

## Examples

The following example returns the time zone offset of the US/Eastern time zone from UTC:

```md
SELECT TZ_OFFSET('US/Eastern') FROM DUAL;

TZ_OFFS
-------
-04:00
```