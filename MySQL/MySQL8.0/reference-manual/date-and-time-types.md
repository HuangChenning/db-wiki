---
title: "13.2 Date and Time Data Types"
book: MySQL 8.0 Reference Manual
version: "8.0"
source: "https://dev.mysql.com/doc/refman/8.0/en/date-and-time-types.html"
tags:
  - mysql
  - mysql-8.0
  - reference-manual
---

MySQL 8.0 Reference Manual Including MySQL NDB Cluster 8.0

The date and time data types for representing temporal values are [`DATE`](datetime.md), [`TIME`](time.md), [`DATETIME`](datetime.md), [`TIMESTAMP`](datetime.md), and [`YEAR`](year.md). Each temporal type has a range of valid values, as well as a “zero” value that may be used when you specify an invalid value that MySQL cannot represent. The [`TIMESTAMP`](datetime.md) and [`DATETIME`](datetime.md) types have special automatic updating behavior, described in [Section 13.2.5, “Automatic Initialization and Updating for TIMESTAMP and DATETIME”](timestamp-initialization.md).

For information about storage requirements of the temporal data types, see [Section 13.7, “Data Type Storage Requirements”](storage-requirements.md).

For descriptions of functions that operate on temporal values, see [Section 14.7, “Date and Time Functions”](date-and-time-functions.md).

Keep in mind these general considerations when working with date and time types:

- MySQL retrieves values for a given date or time type in a standard output format, but it attempts to interpret a variety of formats for input values that you supply (for example, when you specify a value to be assigned to or compared to a date or time type). For a description of the permitted formats for date and time types, see [Section 11.1.3, “Date and Time Literals”](date-and-time-literals.md). It is expected that you supply valid values. Unpredictable results may occur if you use values in other formats.
- Although MySQL tries to interpret values in several formats, date parts must always be given in year-month-day order (for example, `'98-09-04'`), rather than in the month-day-year or day-month-year orders commonly used elsewhere (for example, `'09-04-98'`, `'04-09-98'`). To convert strings in other orders to year-month-day order, the [`STR_TO_DATE()`](date-and-time-functions.md) function may be useful.
- Dates containing 2-digit year values are ambiguous because the century is unknown. MySQL interprets 2-digit year values using these rules:
	- Year values in the range `70-99` become `1970-1999`.
	- Year values in the range `00-69` become `2000-2069`.
	See also [Section 13.2.9, “2-Digit Years in Dates”](two-digit-years.md).
- Conversion of values from one temporal type to another occurs according to the rules in [Section 13.2.8, “Conversion Between Date and Time Types”](date-and-time-type-conversion.md).
- MySQL automatically converts a date or time value to a number if the value is used in numeric context and vice versa.
- By default, when MySQL encounters a value for a date or time type that is out of range or otherwise invalid for the type, it converts the value to the “zero” value for that type. The exception is that out-of-range [`TIME`](time.md) values are clipped to the appropriate endpoint of the [`TIME`](time.md) range.
- By setting the SQL mode to the appropriate value, you can specify more exactly what kind of dates you want MySQL to support. (See [Section 7.1.11, “Server SQL Modes”](sql-mode.md).) You can get MySQL to accept certain dates, such as `'2009-11-31'`, by enabling the [`ALLOW_INVALID_DATES`](sql-mode.md) SQL mode. This is useful when you want to store a “possibly wrong” value which the user has specified (for example, in a web form) in the database for future processing. Under this mode, MySQL verifies only that the month is in the range from 1 to 12 and that the day is in the range from 1 to 31.
- MySQL permits you to store dates where the day or month and day are zero in a [`DATE`](datetime.md) or [`DATETIME`](datetime.md) column. This is useful for applications that need to store birthdates for which you may not know the exact date. In this case, you simply store the date as `'2009-00-00'` or `'2009-01-00'`. However, with dates such as these, you should not expect to get correct results for functions such as [`DATE_SUB()`](date-and-time-functions.md) or [`DATE_ADD()`](date-and-time-functions.md) that require complete dates. To disallow zero month or day parts in dates, enable the [`NO_ZERO_IN_DATE`](sql-mode.md) mode.
- MySQL permits you to store a “zero” value of `'0000-00-00'` as a “dummy date.” In some cases, this is more convenient than using `NULL` values, and uses less data and index space. To disallow `'0000-00-00'`, enable the [`NO_ZERO_DATE`](sql-mode.md) mode.
- “Zero” date or time values used through Connector/ODBC are converted automatically to `NULL` because ODBC cannot handle such values.

The following table shows the format of the “zero” value for each type. The “zero” values are special, but you can store or refer to them explicitly using the values shown in the table. You can also do this using the values `'0'` or `0`, which are easier to write. For temporal types that include a date part ([`DATE`](datetime.md), [`DATETIME`](datetime.md), and [`TIMESTAMP`](datetime.md)), use of these values may produce warning or errors. The precise behavior depends on which, if any, of the strict and [`NO_ZERO_DATE`](sql-mode.md) SQL modes are enabled; see [Section 7.1.11, “Server SQL Modes”](sql-mode.md).

| Data Type | “Zero” Value |
| --- | --- |
| [`DATE`](datetime.md) | `'0000-00-00'` |
| [`TIME`](time.md) | `'00:00:00'` |
| [`DATETIME`](datetime.md) | `'0000-00-00 00:00:00'` |
| [`TIMESTAMP`](datetime.md) | `'0000-00-00 00:00:00'` |
| [`YEAR`](year.md) | `0000` |