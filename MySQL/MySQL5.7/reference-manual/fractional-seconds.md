---
title: "11.2.7 Fractional Seconds in Time Values"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/fractional-seconds.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 11.2.7 Fractional Seconds in Time Values

MySQL has fractional seconds support for [`TIME`](time.md), [`DATETIME`](datetime.md), and [`TIMESTAMP`](datetime.md) values, with up to microseconds (6 digits) precision:

- To define a column that includes a fractional seconds part, use the syntax ``*`type_name`*(*`fsp`*)``, where *`type_name`* is [`TIME`](time.md), [`DATETIME`](datetime.md), or [`TIMESTAMP`](datetime.md), and *`fsp`* is the fractional seconds precision. For example:
	```
	CREATE TABLE t1 (t TIME(3), dt DATETIME(6));
	```
	The *`fsp`* value, if given, must be in the range 0 to 6. A value of 0 signifies that there is no fractional part. If omitted, the default precision is 0. (This differs from the standard SQL default of 6, for compatibility with previous MySQL versions.)
- Inserting a [`TIME`](time.md), [`DATE`](datetime.md), or [`TIMESTAMP`](datetime.md) value with a fractional seconds part into a column of the same type but having fewer fractional digits results in rounding. Consider a table created and populated as follows:
	```
	CREATE TABLE fractest( c1 TIME(2), c2 DATETIME(2), c3 TIMESTAMP(2) );
	INSERT INTO fractest VALUES
	('17:51:04.777', '2018-09-08 17:51:04.777', '2018-09-08 17:51:04.777');
	```
	The temporal values are inserted into the table with rounding:
	```
	mysql> SELECT * FROM fractest;
	+-------------+------------------------+------------------------+
	| c1          | c2                     | c3                     |
	+-------------+------------------------+------------------------+
	| 17:51:04.78 | 2018-09-08 17:51:04.78 | 2018-09-08 17:51:04.78 |
	+-------------+------------------------+------------------------+
	```
	No warning or error is given when such rounding occurs. This behavior follows the SQL standard, and is not affected by the server [`sql_mode`](server-system-variables.md) setting.
- Functions that take temporal arguments accept values with fractional seconds. Return values from temporal functions include fractional seconds as appropriate. For example, [`NOW()`](date-and-time-functions.md) with no argument returns the current date and time with no fractional part, but takes an optional argument from 0 to 6 to specify that the return value includes a fractional seconds part of that many digits.
- Syntax for temporal literals produces temporal values: ``DATE '*`str`*'``, ``TIME '*`str`*'``, and ``TIMESTAMP             '*`str`*'``, and the ODBC-syntax equivalents. The resulting value includes a trailing fractional seconds part if specified. Previously, the temporal type keyword was ignored and these constructs produced the string value. See [Standard SQL and ODBC Date and Time Literals](date-and-time-literals.md)