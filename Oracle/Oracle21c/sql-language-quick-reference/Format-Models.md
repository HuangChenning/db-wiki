---
title: SQL Language Quick Reference
book: SQL Language Quick Reference
doc_id: F31302-11
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/sqlqr/Format-Models.html
tags:
  - oracle
  - 21c
  - sql-language-quick-reference
---

This chapter presents the format models for datetime and number data stored in character strings.

This chapter includes the following sections:

### Overview of Format Models

A format model is a character literal that describes the format of `DATETIME` or `NUMBER` data stored in a character string. When you convert a character string into a datetime or number, a format model tells Oracle how to interpret the string.

See Also:

[Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00210) for more information on format models

#### Number Format Models

You can use number format models:

- In the `TO_CHAR` function to translate a value of `NUMBER` data type to `VARCHAR2` data type
- In the `TO_NUMBER` function to translate a value of `CHAR` or `VARCHAR2` data type to `NUMBER` data type

##### Number Format Elements

A number format model is composed of one or more number format elements. The following table lists the elements of a number format model.

Table 7-1 Number Format Elements

| Element | Example | Description |
| --- | --- | --- |
| , (comma) | `9,999` | Returns a comma in the specified position. You can specify multiple commas in a number format model.  Restrictions:  - A comma element cannot begin a number format model. - A comma cannot appear to the right of a decimal character or period in a number format model. |
| . (period) | `99.99` | Returns a decimal point, which is a period (.) in the specified position.  Restriction: You can specify only one period in a number format model. |
| $ | `$9999` | Returns value with a leading dollar sign. |
| 0 | `0999`  `9990` | Returns leading zeros.  Returns trailing zeros. |
| 9 | `9999` | Returns value with the specified number of digits with a leading space if positive or with a leading minus if negative. Leading zeros are blank, except for a zero value, which returns a zero for the integer part of the fixed-point number. |
| B | `B9999` | Returns blanks for the integer part of a fixed-point number when the integer part is zero (regardless of zeros in the format model). |
| C | `C999` | Returns in the specified position the ISO currency symbol (the current value of the `NLS_ISO_CURRENCY` parameter). |
| D | `99D99` | Returns in the specified position the decimal character, which is the current value of the `NLS_NUMERIC_CHARACTER` parameter. The default is a period (.).  Restriction: You can specify only one decimal character in a number format model. |
| EEEE | `9.9EEEE` | Returns a value using in scientific notation. |
| G | `9G999` | Returns in the specified position the group separator (the current value of the `NLS_NUMERIC_CHARACTER` parameter). You can specify multiple group separators in a number format model.  Restriction: A group separator cannot appear to the right of a decimal character or period in a number format model. |
| L | `L999` | Returns in the specified position the local currency symbol (the current value of the `NLS_CURRENCY` parameter). |
| MI | `9999MI` | Returns negative value with a trailing minus sign (-).  Returns positive value with a trailing blank.  Restriction: The MI format element can appear only in the last position of a number format model. |
| PR | `9999PR` | Returns negative value in \<angle brackets>.  Returns positive value with a leading and trailing blank.  Restriction: The PR format element can appear only in the last position of a number format model. |
| RN  rn | `RN`  `rn` | Returns a value as Roman numerals in uppercase.  Returns a value as Roman numerals in lowercase.  Value can be an integer between 1 and 3999. |
| S | `S9999`  `9999S` | Returns negative value with a leading minus sign (-).  Returns positive value with a leading plus sign (+).  Returns negative value with a trailing minus sign (-).  Returns positive value with a trailing plus sign (+).  Restriction: The S format element can appear only in the first or last position of a number format model. |
| TM | `TM` | The text minimum number format model returns (in decimal output) the smallest number of characters possible. This element is case insensitive.  The default is TM9, which returns the number in fixed notation unless the output exceeds 64 characters. If the output exceeds 64 characters, then Oracle Database automatically returns the number in scientific notation.  Restrictions:  - You cannot precede this element with any other element. - You can follow this element only with one 9 or one E (or e), but not with any combination of these. The following statement returns an error: 	`SELECT TO_CHAR(1234, 'TM9e') FROM DUAL; ` |
| U | `U9999` | Returns in the specified position the Euro (or other) dual currency symbol, determined by the current value of the `NLS_DUAL_CURRENCY` parameter. |
| V | `999V99` | Returns a value multiplied by 10 <sup>n</sup> (and if necessary, round it up), where `n` is the number of 9's after the `V`. |
| X | `XXXX`  `xxxx` | Returns the hexadecimal value of the specified number of digits. If the specified number is not an integer, then Oracle Database rounds it to an integer.  Restrictions:  - This element accepts only positive values or 0. Negative values return an error. - You can precede this element only with 0 (which returns leading zeroes) or FM. Any other elements return an error. If you specify neither 0 nor FM with X, then the return always has one leading blank. Refer to [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF30003) for information on the FM format model modifier. |

See Also:

[Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00211) for more information on number format models

#### Datetime Format Models

You can use datetime format models:

- In the `TO_CHAR`, `TO_DATE`, `TO_TIMESTAMP`, `TO_TIMESTAMP_TZ`, `TO_YMINTERVAL`, and `TO_DSINTERVAL` datetime functions to translate a character string that is in a format other than the default datetime format into a `DATETIME` value
- In the `TO_CHAR` function to translate a `DATETIME` value that is in a format other than the default datetime format into a character string

##### Datetime Format Elements

A datetime format model is composed of one or more datetime format elements. The following table lists the elements of a date format model.

Table 7-2 Datetime Format Elements

| Element | TO\_\* datetime functions? | Description |
| --- | --- | --- |
| ``` - / , . ; : "text" ``` | Yes | Punctuation and quoted text is reproduced in the result. |
| ``` AD A.D. ``` | Yes | AD indicator with or without periods. |
| ``` AM A.M. ``` | Yes | Meridian indicator with or without periods. |
| ``` BC B.C. ``` | Yes | BC indicator with or without periods. |
| ``` CC SCC ``` | No | Century.  - If the last 2 digits of a 4-digit year are between 01 and 99 (inclusive), then the century is one greater than the first 2 digits of that year. - If the last 2 digits of a 4-digit year are 00, then the century is the same as the first 2 digits of that year.  For example, 2002 returns 21; 2000 returns 20. |
| ``` D ``` | Yes | Day of week (1-7). This element depends on the NLS territory of the session. |
| ``` DAY ``` | Yes | Name of day. |
| ``` DD ``` | Yes | Day of month (1-31). |
| ``` DDD ``` | Yes | Day of year (1-366). |
| ``` DL ``` | Yes | Returns a value in the long date format, which is an extension of Oracle Database's `DATE` format, determined by the current value of the `NLS_DATE_FORMAT` parameter. Makes the appearance of the date components (day name, month number, and so forth) depend on the `NLS_TERRITORY` and `NLS_LANGUAGE` parameters. For example, in the `AMERICAN_AMERICA` locale, this is equivalent to specifying the format `'fmDay,` `Month` `dd,` `yyyy'`. In the `GERMAN_GERMANY` locale, it is equivalent to specifying the format ' `fmDay, dd.` `Month yyyy` '.  Restriction: You can specify this format only with the `TS` element, separated by white space. |
| ``` DS ``` | Yes | Returns a value in the short date format. Makes the appearance of the date components (day name, month number, and so forth) depend on the `NLS_TERRITORY` and `NLS_LANGUAGE` parameters. For example, in the `AMERICAN_AMERICA` locale, this is equivalent to specifying the format ' `MM/DD/RRRR` '. In the `ENGLISH_UNITED_KINGDOM` locale, it is equivalent to specifying the format ' `DD/MM/RRRR` '.  Restriction: You can specify this format only with the `TS` element, separated by white space. |
| ``` DY ``` | Yes | Abbreviated name of day. |
| ``` E ``` | Yes | Abbreviated era name (Japanese Imperial, ROC Official, and Thai Buddha calendars). |
| ``` EE ``` | Yes | Full era name (Japanese Imperial, ROC Official, and Thai Buddha calendars). |
| ``` FF [1..9] ``` | Yes | Fractional seconds; no radix character is printed. Use the X format element to add the radix character. Use the numbers 1 to 9 after FF to specify the number of digits in the fractional second portion of the datetime value returned. If you do not specify a digit, then Oracle Database uses the precision specified for the datetime data type or the data type's default precision. Valid in timestamp and interval formats, but not in `DATE` formats.  Examples: `'HH:MI:SS.FF'`  `SELECT TO_CHAR(SYSTIMESTAMP, 'SS.FF3') from dual;` |
| ``` FM ``` | Yes | Returns a value with no leading or trailing blanks.  See Also: [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF30003) for more information on the FM format model modifier |
| ``` FX ``` | Yes | Requires exact matching between the character data and the format model.  See Also: [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF30004) for more information on the FX format model modifier |
| ``` HH HH12 ``` | Yes | Hour of day (1-12). |
| ``` HH24 ``` | Yes | Hour of day (0-23). |
| ``` IW ``` | No | Week of year (1-52 or 1-53) based on the ISO standard. |
| ``` IYY IY I ``` | No | Last 3, 2, or 1 digit(s) of ISO year. |
| ``` IYYY ``` | No | 4-digit year based on the ISO standard. |
| ``` J ``` | Yes | Julian day; the number of days since January 1, 4712 BC. Number specified with J must be integers. |
| ``` MI ``` | Yes | Minute (0-59). |
| ``` MM ``` | Yes | Month (01-12; January = 01). |
| ``` MON ``` | Yes | Abbreviated name of month. |
| ``` MONTH ``` | Yes | Name of month. |
| ``` PM P.M. ``` | Yes | Meridian indicator with or without periods. |
| ``` Q ``` | No | Quarter of year (1, 2, 3, 4; January - March = 1). |
| ``` RM ``` | Yes | Roman numeral month (I-XII; January = I). |
| ``` RR ``` | Yes | Lets you store 20th century dates in the 21st century using only two digits.  See Also: [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00215) for more information on the RR datetime format element |
| ``` RRRR ``` | Yes | Round year. Accepts either 4-digit or 2-digit input. If 2-digit, provides the same return as RR. If you do not want this functionality, then enter the 4-digit year. |
| ``` SS ``` | Yes | Second (0-59). |
| ``` SSSSS ``` | Yes | Seconds past midnight (0-86399). |
| ``` TS ``` | Yes | Returns a value in the short time format. Makes the appearance of the time components (hour, minutes, and so forth) depend on the `NLS_TERRITORY` and `NLS_LANGUAGE` initialization parameters.  Restriction: You can specify this format only with the `DL` or `DS` element, separated by white space. |
| ``` TZD ``` | Yes | Daylight saving information. The TZD value is an abbreviated time zone string with daylight saving information. It must correspond with the region specified in TZR. Valid in timestamp and interval formats, but not in `DATE` formats.  Example: `PST` (for US/Pacific standard time); `PDT` (for US/Pacific daylight time). |
| ``` TZH ``` | Yes | Time zone hour. (See `TZM` format element.) Valid in timestamp and interval formats, but not in `DATE` formats.  Example: `'HH:MI:SS.FFTZH:TZM'`. |
| ``` TZM ``` | Yes | Time zone minute. (See `TZH` format element.) Valid in timestamp and interval formats, but not in `DATE` formats.  Example: `'HH:MI:SS.FFTZH:TZM'`. |
| ``` TZR ``` | Yes | Time zone region information. The value must be one of the time zone regions supported in the database. Valid in timestamp and interval formats, but not in `DATE` formats.  Example: US/Pacific |
| ``` WW ``` | No | Week of year (1-53) where week 1 starts on the first day of the year and continues to the seventh day of the year. |
| ``` W ``` | No | Week of month (1-5) where week 1 starts on the first day of the month and ends on the seventh. |
| ``` X ``` | Yes | Local radix character.  Example: `'HH:MI:SSXFF'`. |
| ``` Y,YYY ``` | Yes | Year with comma in this position. |
| ``` YEAR SYEAR ``` | No | Year, spelled out; `S` prefixes BC dates with a minus sign (-). |
| ``` YYYY SYYYY ``` | Yes | 4-digit year; `S` prefixes BC dates with a minus sign. |
| ``` YYY YY Y ``` | Yes | Last 3, 2, or 1 digit(s) of year. |

See Also:

[Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlqr&id=SQLRF00212) for more information on datetime format models