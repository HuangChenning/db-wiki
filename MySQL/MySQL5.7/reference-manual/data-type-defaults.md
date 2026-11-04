---
title: "11.6 Data Type Default Values"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/data-type-defaults.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

Data type specifications can have explicit or implicit default values.

### Explicit Default Handling

A ``DEFAULT *`value`*`` clause in a data type specification explicitly indicates a default value for a column. Examples:

```
CREATE TABLE t1 (
  i     INT DEFAULT -1,
  c     VARCHAR(10) DEFAULT '',
  price DOUBLE(16,2) DEFAULT '0.00'
);
```

`SERIAL DEFAULT VALUE` is a special case. In the definition of an integer column, it is an alias for `NOT NULL AUTO_INCREMENT UNIQUE`.

With one exception, the default value specified in a `DEFAULT` clause must be a literal constant; it cannot be a function or an expression. This means, for example, that you cannot set the default for a date column to be the value of a function such as [`NOW()`](date-and-time-functions.md) or [`CURRENT_DATE`](date-and-time-functions.md). The exception is that, for [`TIMESTAMP`](datetime.md) and [`DATETIME`](datetime.md) columns, you can specify [`CURRENT_TIMESTAMP`](date-and-time-functions.md) as the default. See [Section 11.2.6, “Automatic Initialization and Updating for TIMESTAMP and DATETIME”](timestamp-initialization.md).

The [`BLOB`](blob.md), [`TEXT`](blob.md), `GEOMETRY`, and [`JSON`](json.md) data types cannot be assigned a default value.

### Implicit Default Handling

If a data type specification includes no explicit `DEFAULT` value, MySQL determines the default value as follows:

If the column can take `NULL` as a value, the column is defined with an explicit `DEFAULT         NULL` clause.

If the column cannot take `NULL` as a value, MySQL defines the column with no explicit `DEFAULT` clause.

For data entry into a `NOT NULL` column that has no explicit `DEFAULT` clause, if an [`INSERT`](insert.md) or [`REPLACE`](replace.md) statement includes no value for the column, or an [`UPDATE`](update.md) statement sets the column to `NULL`, MySQL handles the column according to the SQL mode in effect at the time:

- If strict SQL mode is enabled, an error occurs for transactional tables and the statement is rolled back. For nontransactional tables, an error occurs, but if this happens for the second or subsequent row of a multiple-row statement, any rows preceding the error have already been inserted.
- If strict mode is not enabled, MySQL sets the column to the implicit default value for the column data type.

Suppose that a table `t` is defined as follows:

```
CREATE TABLE t (i INT NOT NULL);
```

In this case, `i` has no explicit default, so in strict mode each of the following statements produce an error and no row is inserted. When not using strict mode, only the third statement produces an error; the implicit default is inserted for the first two statements, but the third fails because [`DEFAULT(i)`](miscellaneous-functions.md) cannot produce a value:

```
INSERT INTO t VALUES();
INSERT INTO t VALUES(DEFAULT);
INSERT INTO t VALUES(DEFAULT(i));
```

See [Section 5.1.10, “Server SQL Modes”](sql-mode.md).

For a given table, the [`SHOW CREATE         TABLE`](show-create-table.md) statement displays which columns have an explicit `DEFAULT` clause.

Implicit defaults are defined as follows:

- For numeric types, the default is `0`, with the exception that for integer or floating-point types declared with the `AUTO_INCREMENT` attribute, the default is the next value in the sequence.
- For date and time types other than [`TIMESTAMP`](datetime.md), the default is the appropriate “zero” value for the type. This is also true for [`TIMESTAMP`](datetime.md) if the [`explicit_defaults_for_timestamp`](server-system-variables.md) system variable is enabled (see [Section 5.1.7, “Server System Variables”](server-system-variables.md)). Otherwise, for the first [`TIMESTAMP`](datetime.md) column in a table, the default value is the current date and time. See [Section 11.2, “Date and Time Data Types”](date-and-time-types.md).
- For string types other than [`ENUM`](enum.md), the default value is the empty string. For [`ENUM`](enum.md), the default is the first enumeration value.