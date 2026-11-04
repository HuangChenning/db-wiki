---
title: "MySQL :: MySQL 26.7 Reference Manual :: 26.6.3 Partitioning Limitations Relating to Functions"
book: MySQL 26.7 Reference Manual
version: "26.7"
source: "https://dev.mysql.com/doc/refman/26.7/en/partitioning-limitations-functions.html"
tags:
  - mysql
  - mysql-26.7
  - reference-manual
---

### 26.6.3 Partitioning Limitations Relating to Functions

This section discusses limitations in MySQL Partitioning relating specifically to functions used in partitioning expressions.

Only the MySQL functions shown in the following list are allowed in partitioning expressions:

- [`ABS()`](mathematical-functions.md)
- [`CEILING()`](mathematical-functions.md) (see CEILING() and FLOOR())
- [`DATEDIFF()`](date-and-time-functions.md)
- [`DAY()`](date-and-time-functions.md)
- [`DAYOFMONTH()`](date-and-time-functions.md)
- [`DAYOFWEEK()`](date-and-time-functions.md)
- [`DAYOFYEAR()`](date-and-time-functions.md)
- [`EXTRACT()`](date-and-time-functions.md) (see EXTRACT() function with WEEK specifier)
- [`FLOOR()`](mathematical-functions.md) (see CEILING() and FLOOR())
- [`HOUR()`](date-and-time-functions.md)
- [`MICROSECOND()`](date-and-time-functions.md)
- [`MINUTE()`](date-and-time-functions.md)
- [`MOD()`](mathematical-functions.md)
- [`MONTH()`](date-and-time-functions.md)
- [`QUARTER()`](date-and-time-functions.md)
- [`SECOND()`](date-and-time-functions.md)
- [`TIME_TO_SEC()`](date-and-time-functions.md)
- [`TO_DAYS()`](date-and-time-functions.md)
- [`TO_SECONDS()`](date-and-time-functions.md)
- [`UNIX_TIMESTAMP()`](date-and-time-functions.md) (with [`TIMESTAMP`](datetime.md) columns)
- [`WEEKDAY()`](date-and-time-functions.md)
- [`YEAR()`](date-and-time-functions.md)
- [`YEARWEEK()`](date-and-time-functions.md)

In MySQL 26.7, partition pruning is supported for the [`TO_DAYS()`](date-and-time-functions.md), [`TO_SECONDS()`](date-and-time-functions.md), [`YEAR()`](date-and-time-functions.md), and [`UNIX_TIMESTAMP()`](date-and-time-functions.md) functions. See [Section 26.4, “Partition Pruning”](partitioning-pruning.md), for more information.

**CEILING() and FLOOR().** Each of these functions returns an integer only if it is passed an argument of an exact numeric type, such as one of the [`INT`](integer-types.md) types or [`DECIMAL`](fixed-point-types.md). This means, for example, that the following [`CREATE           TABLE`](create-table.md) statement fails with an error, as shown here:

```sql
mysql> CREATE TABLE t (c FLOAT) PARTITION BY LIST( FLOOR(c) )(
    ->     PARTITION p0 VALUES IN (1,3,5),
    ->     PARTITION p1 VALUES IN (2,4,6)
    -> );
ERROR 1490 (HY000): The PARTITION function returns the wrong type
```

**EXTRACT() function with WEEK specifier.** The value returned by the [`EXTRACT()`](date-and-time-functions.md) function, when used as [``EXTRACT(WEEK FROM           *`col`*)``](date-and-time-functions.md), depends on the value of the [`default_week_format`](server-system-variables.md) system variable. For this reason, [`EXTRACT()`](date-and-time-functions.md) is not permitted as a partitioning function when it specifies the unit as `WEEK`. (Bug #54483)

See [Section 14.6.2, “Mathematical Functions”](mathematical-functions.md), for more information about the return types of these functions, as well as [Section 13.1, “Numeric Data Types”](numeric-types.md).