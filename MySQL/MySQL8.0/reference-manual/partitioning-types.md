---
title: "26.2 Partitioning Types"
book: MySQL 8.0 Reference Manual
version: "8.0"
source: "https://dev.mysql.com/doc/refman/8.0/en/partitioning-types.html"
tags:
  - mysql
  - mysql-8.0
  - reference-manual
---

MySQL 8.0 Reference Manual Including MySQL NDB Cluster 8.0

This section discusses the types of partitioning which are available in MySQL 8.0. These include the types listed here:

- **RANGE partitioning.** This type of partitioning assigns rows to partitions based on column values falling within a given range. See [Section 26.2.1, “RANGE Partitioning”](partitioning-range.md). For information about an extension to this type, `RANGE COLUMNS`, see [Section 26.2.3.1, “RANGE COLUMNS partitioning”](partitioning-columns-range.md).
- **LIST partitioning.** Similar to partitioning by `RANGE`, except that the partition is selected based on columns matching one of a set of discrete values. See [Section 26.2.2, “LIST Partitioning”](partitioning-list.md). For information about an extension to this type, `LIST COLUMNS`, see [Section 26.2.3.2, “LIST COLUMNS partitioning”](partitioning-columns-list.md).
- **HASH partitioning.** With this type of partitioning, a partition is selected based on the value returned by a user-defined expression that operates on column values in rows to be inserted into the table. The function may consist of any expression valid in MySQL that yields an integer value. See [Section 26.2.4, “HASH Partitioning”](partitioning-hash.md).
	An extension to this type, `LINEAR HASH`, is also available, see [Section 26.2.4.1, “LINEAR HASH Partitioning”](partitioning-linear-hash.md).
- **KEY partitioning.** This type of partitioning is similar to partitioning by `HASH`, except that only one or more columns to be evaluated are supplied, and the MySQL server provides its own hashing function. These columns can contain other than integer values, since the hashing function supplied by MySQL guarantees an integer result regardless of the column data type. An extension to this type, `LINEAR KEY`, is also available. See [Section 26.2.5, “KEY Partitioning”](partitioning-key.md).

A very common use of database partitioning is to segregate data by date. Some database systems support explicit date partitioning, which MySQL does not implement in 8.0. However, it is not difficult in MySQL to create partitioning schemes based on [`DATE`](datetime.md), [`TIME`](time.md), or [`DATETIME`](datetime.md) columns, or based on expressions making use of such columns.

When partitioning by `KEY` or `LINEAR       KEY`, you can use a [`DATE`](datetime.md), [`TIME`](time.md), or [`DATETIME`](datetime.md) column as the partitioning column without performing any modification of the column value. For example, this table creation statement is perfectly valid in MySQL:

```
CREATE TABLE members (
    firstname VARCHAR(25) NOT NULL,
    lastname VARCHAR(25) NOT NULL,
    username VARCHAR(16) NOT NULL,
    email VARCHAR(35),
    joined DATE NOT NULL
)
PARTITION BY KEY(joined)
PARTITIONS 6;
```

In MySQL 8.0, it is also possible to use a [`DATE`](datetime.md) or [`DATETIME`](datetime.md) column as the partitioning column using `RANGE COLUMNS` and `LIST       COLUMNS` partitioning.

Other partitioning types require a partitioning expression that yields an integer value or `NULL`. If you wish to use date-based partitioning by `RANGE`, `LIST`, `HASH`, or `LINEAR HASH`, you can simply employ a function that operates on a [`DATE`](datetime.md), [`TIME`](time.md), or [`DATETIME`](datetime.md) column and returns such a value, as shown here:

```
CREATE TABLE members (
    firstname VARCHAR(25) NOT NULL,
    lastname VARCHAR(25) NOT NULL,
    username VARCHAR(16) NOT NULL,
    email VARCHAR(35),
    joined DATE NOT NULL
)
PARTITION BY RANGE( YEAR(joined) ) (
    PARTITION p0 VALUES LESS THAN (1960),
    PARTITION p1 VALUES LESS THAN (1970),
    PARTITION p2 VALUES LESS THAN (1980),
    PARTITION p3 VALUES LESS THAN (1990),
    PARTITION p4 VALUES LESS THAN MAXVALUE
);
```

Additional examples of partitioning using dates may be found in the following sections of this chapter:

- [Section 26.2.1, “RANGE Partitioning”](partitioning-range.md)
- [Section 26.2.4, “HASH Partitioning”](partitioning-hash.md)
- [Section 26.2.4.1, “LINEAR HASH Partitioning”](partitioning-linear-hash.md)

For more complex examples of date-based partitioning, see the following sections:

- [Section 26.4, “Partition Pruning”](partitioning-pruning.md)
- [Section 26.2.6, “Subpartitioning”](partitioning-subpartitions.md)

MySQL partitioning is optimized for use with the [`TO_DAYS()`](date-and-time-functions.md), [`YEAR()`](date-and-time-functions.md), and [`TO_SECONDS()`](date-and-time-functions.md) functions. However, you can use other date and time functions that return an integer or `NULL`, such as [`WEEKDAY()`](date-and-time-functions.md), [`DAYOFYEAR()`](date-and-time-functions.md), or [`MONTH()`](date-and-time-functions.md). See [Section 14.7, “Date and Time Functions”](date-and-time-functions.md), for more information about such functions.

It is important to remember—regardless of the type of partitioning that you use—that partitions are always numbered automatically and in sequence when created, starting with `0`. When a new row is inserted into a partitioned table, it is these partition numbers that are used in identifying the correct partition. For example, if your table uses 4 partitions, these partitions are numbered `0`, `1`, `2`, and `3`. For the `RANGE` and `LIST` partitioning types, it is necessary to ensure that there is a partition defined for each partition number. For `HASH` partitioning, the user-supplied expression must evaluate to an integer value. For `KEY` partitioning, this issue is taken care of automatically by the hashing function which the MySQL server employs internally.

Names of partitions generally follow the rules governing other MySQL identifiers, such as those for tables and databases. However, you should note that partition names are not case-sensitive. For example, the following [`CREATE TABLE`](create-table.md) statement fails as shown:

```
mysql> CREATE TABLE t2 (val INT)
    -> PARTITION BY LIST(val)(
    ->     PARTITION mypart VALUES IN (1,3,5),
    ->     PARTITION MyPart VALUES IN (2,4,6)
    -> );
ERROR 1488 (HY000): Duplicate partition name mypart
```

Failure occurs because MySQL sees no difference between the partition names `mypart` and `MyPart`.

When you specify the number of partitions for the table, this must be expressed as a positive, nonzero integer literal with no leading zeros, and may not be an expression such as `0.8E+01` or `6-2`, even if it evaluates to an integer value. Decimal fractions are not permitted.

In the sections that follow, we do not necessarily provide all possible forms for the syntax that can be used for creating each partition type; for this information, see [Section 15.1.20, “CREATE TABLE Statement”](create-table.md).