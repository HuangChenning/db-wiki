---
title: "MySQL :: MySQL 26.7 Reference Manual :: 13.2.5 Automatic Initialization and Updating for TIMESTAMP and DATETIME"
book: MySQL 26.7 Reference Manual
version: "26.7"
source: "https://dev.mysql.com/doc/refman/26.7/en/timestamp-initialization.html"
tags:
  - mysql
  - mysql-26.7
  - reference-manual
---

### 13.2.5 Automatic Initialization and Updating for TIMESTAMP and DATETIME

[`TIMESTAMP`](datetime.md) and [`DATETIME`](datetime.md) columns can be automatically initialized and updated to the current date and time (that is, the current timestamp).

For any [`TIMESTAMP`](datetime.md) or [`DATETIME`](datetime.md) column in a table, you can assign the current timestamp as the default value, the auto-update value, or both:

- An auto-initialized column is set to the current timestamp for inserted rows that specify no value for the column.
- An auto-updated column is automatically updated to the current timestamp when the value of any other column in the row is changed from its current value. An auto-updated column remains unchanged if all other columns are set to their current values. To prevent an auto-updated column from updating when other columns change, explicitly set it to its current value. To update an auto-updated column even when other columns do not change, explicitly set it to the value it should have (for example, set it to [`CURRENT_TIMESTAMP`](date-and-time-functions.md)).

In addition, if the [`explicit_defaults_for_timestamp`](server-system-variables.md) system variable is disabled, you can initialize or update any [`TIMESTAMP`](datetime.md) (but not `DATETIME`) column to the current date and time by assigning it a `NULL` value, unless it has been defined with the `NULL` attribute to permit `NULL` values.

To specify automatic properties, use the `DEFAULT         CURRENT_TIMESTAMP` and `ON UPDATE         CURRENT_TIMESTAMP` clauses in column definitions. The order of the clauses does not matter. If both are present in a column definition, either can occur first. Any of the synonyms for [`CURRENT_TIMESTAMP`](date-and-time-functions.md) have the same meaning as [`CURRENT_TIMESTAMP`](date-and-time-functions.md). These are [`CURRENT_TIMESTAMP()`](date-and-time-functions.md), [`NOW()`](date-and-time-functions.md), [`LOCALTIME`](date-and-time-functions.md), [`LOCALTIME()`](date-and-time-functions.md), [`LOCALTIMESTAMP`](date-and-time-functions.md), and [`LOCALTIMESTAMP()`](date-and-time-functions.md).

Use of `DEFAULT CURRENT_TIMESTAMP` and `ON UPDATE CURRENT_TIMESTAMP` is specific to [`TIMESTAMP`](datetime.md) and [`DATETIME`](datetime.md). The `DEFAULT` clause also can be used to specify a constant (nonautomatic) default value (for example, `DEFAULT 0` or `DEFAULT '2000-01-01         00:00:00'`).

Note

The following examples use `DEFAULT 0`, a default that can produce warnings or errors depending on whether strict SQL mode or the [`NO_ZERO_DATE`](sql-mode.md) SQL mode is enabled. Be aware that the [`TRADITIONAL`](sql-mode.md) SQL mode includes strict mode and [`NO_ZERO_DATE`](sql-mode.md). See [Section 7.1.11, “Server SQL Modes”](sql-mode.md).

[`TIMESTAMP`](datetime.md) or [`DATETIME`](datetime.md) column definitions can specify the current timestamp for both the default and auto-update values, for one but not the other, or for neither. Different columns can have different combinations of automatic properties. The following rules describe the possibilities:

- With both `DEFAULT CURRENT_TIMESTAMP` and `ON UPDATE CURRENT_TIMESTAMP`, the column has the current timestamp for its default value and is automatically updated to the current timestamp.
	```sql
	CREATE TABLE t1 (
	  ts TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
	  dt DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
	);
	```
- With a `DEFAULT` clause but no `ON             UPDATE CURRENT_TIMESTAMP` clause, the column has the given default value and is not automatically updated to the current timestamp.
	The default depends on whether the `DEFAULT` clause specifies `CURRENT_TIMESTAMP` or a constant value. With `CURRENT_TIMESTAMP`, the default is the current timestamp.
	```sql
	CREATE TABLE t1 (
	  ts TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	  dt DATETIME DEFAULT CURRENT_TIMESTAMP
	);
	```
	With a constant, the default is the given value. In this case, the column has no automatic properties at all.
	```sql
	CREATE TABLE t1 (
	  ts TIMESTAMP DEFAULT 0,
	  dt DATETIME DEFAULT 0
	);
	```
- With an `ON UPDATE CURRENT_TIMESTAMP` clause and a constant `DEFAULT` clause, the column is automatically updated to the current timestamp and has the given constant default value.
	```sql
	CREATE TABLE t1 (
	  ts TIMESTAMP DEFAULT 0 ON UPDATE CURRENT_TIMESTAMP,
	  dt DATETIME DEFAULT 0 ON UPDATE CURRENT_TIMESTAMP
	);
	```
- With an `ON UPDATE CURRENT_TIMESTAMP` clause but no `DEFAULT` clause, the column is automatically updated to the current timestamp but does not have the current timestamp for its default value.
	The default in this case is type dependent. [`TIMESTAMP`](datetime.md) has a default of 0 unless defined with the `NULL` attribute, in which case the default is `NULL`.
	```sql
	CREATE TABLE t1 (
	  ts1 TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,     -- default 0
	  ts2 TIMESTAMP NULL ON UPDATE CURRENT_TIMESTAMP -- default NULL
	);
	```
	[`DATETIME`](datetime.md) has a default of `NULL` unless defined with the `NOT             NULL` attribute, in which case the default is 0.
	```sql
	CREATE TABLE t1 (
	  dt1 DATETIME ON UPDATE CURRENT_TIMESTAMP,         -- default NULL
	  dt2 DATETIME NOT NULL ON UPDATE CURRENT_TIMESTAMP -- default 0
	);
	```

[`TIMESTAMP`](datetime.md) and [`DATETIME`](datetime.md) columns have no automatic properties unless they are specified explicitly, with this exception: If the [`explicit_defaults_for_timestamp`](server-system-variables.md) system variable is disabled, the *first* [`TIMESTAMP`](datetime.md) column has both `DEFAULT CURRENT_TIMESTAMP` and `ON         UPDATE CURRENT_TIMESTAMP` if neither is specified explicitly. To suppress automatic properties for the first [`TIMESTAMP`](datetime.md) column, use one of these strategies:

- Enable the [`explicit_defaults_for_timestamp`](server-system-variables.md) system variable. In this case, the `DEFAULT             CURRENT_TIMESTAMP` and `ON UPDATE             CURRENT_TIMESTAMP` clauses that specify automatic initialization and updating are available, but are not assigned to any [`TIMESTAMP`](datetime.md) column unless explicitly included in the column definition.
- Alternatively, if [`explicit_defaults_for_timestamp`](server-system-variables.md) is disabled, do either of the following:
	- Define the column with a `DEFAULT` clause that specifies a constant default value.
	- Specify the `NULL` attribute. This also causes the column to permit `NULL` values, which means that you cannot assign the current timestamp by setting the column to `NULL`. Assigning `NULL` sets the column to `NULL`, not the current timestamp. To assign the current timestamp, set the column to [`CURRENT_TIMESTAMP`](date-and-time-functions.md) or a synonym such as [`NOW()`](date-and-time-functions.md).

Consider these table definitions:

```sql
CREATE TABLE t1 (
  ts1 TIMESTAMP DEFAULT 0,
  ts2 TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                ON UPDATE CURRENT_TIMESTAMP);
CREATE TABLE t2 (
  ts1 TIMESTAMP NULL,
  ts2 TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                ON UPDATE CURRENT_TIMESTAMP);
CREATE TABLE t3 (
  ts1 TIMESTAMP NULL DEFAULT 0,
  ts2 TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                ON UPDATE CURRENT_TIMESTAMP);
```

The tables have these properties:

- In each table definition, the first [`TIMESTAMP`](datetime.md) column has no automatic initialization or updating.
- The tables differ in how the `ts1` column handles `NULL` values. For `t1`, `ts1` is `NOT NULL` and assigning it a value of `NULL` sets it to the current timestamp. For `t2` and `t3`, `ts1` permits `NULL` and assigning it a value of `NULL` sets it to `NULL`.
- `t2` and `t3` differ in the default value for `ts1`. For `t2`, `ts1` is defined to permit `NULL`, so the default is also `NULL` in the absence of an explicit `DEFAULT` clause. For `t3`, `ts1` permits `NULL` but has an explicit default of 0.

If a [`TIMESTAMP`](datetime.md) or [`DATETIME`](datetime.md) column definition includes an explicit fractional seconds precision value anywhere, the same value must be used throughout the column definition. This is permitted:

```sql
CREATE TABLE t1 (
  ts TIMESTAMP(6) DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6)
);
```

This is not permitted:

```sql
CREATE TABLE t1 (
  ts TIMESTAMP(6) DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP(3)
);
```

#### TIMESTAMP Initialization and the NULL Attribute

If the [`explicit_defaults_for_timestamp`](server-system-variables.md) system variable is disabled, [`TIMESTAMP`](datetime.md) columns by default are `NOT NULL`, cannot contain `NULL` values, and assigning `NULL` assigns the current timestamp. To permit a [`TIMESTAMP`](datetime.md) column to contain `NULL`, explicitly declare it with the `NULL` attribute. In this case, the default value also becomes `NULL` unless overridden with a `DEFAULT` clause that specifies a different default value. `DEFAULT NULL` can be used to explicitly specify `NULL` as the default value. (For a [`TIMESTAMP`](datetime.md) column not declared with the `NULL` attribute, `DEFAULT NULL` is invalid.) If a [`TIMESTAMP`](datetime.md) column permits `NULL` values, assigning `NULL` sets it to `NULL`, not to the current timestamp.

The following table contains several [`TIMESTAMP`](datetime.md) columns that permit `NULL` values:

```sql
CREATE TABLE t
(
  ts1 TIMESTAMP NULL DEFAULT NULL,
  ts2 TIMESTAMP NULL DEFAULT 0,
  ts3 TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP
);
```

A [`TIMESTAMP`](datetime.md) column that permits `NULL` values does *not* take on the current timestamp at insert time except under one of the following conditions:

- Its default value is defined as [`CURRENT_TIMESTAMP`](date-and-time-functions.md) and no value is specified for the column
- [`CURRENT_TIMESTAMP`](date-and-time-functions.md) or any of its synonyms such as [`NOW()`](date-and-time-functions.md) is explicitly inserted into the column

In other words, a [`TIMESTAMP`](datetime.md) column defined to permit `NULL` values auto-initializes only if its definition includes `DEFAULT CURRENT_TIMESTAMP`:

```sql
CREATE TABLE t (ts TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP);
```

If the [`TIMESTAMP`](datetime.md) column permits `NULL` values but its definition does not include `DEFAULT CURRENT_TIMESTAMP`, you must explicitly insert a value corresponding to the current date and time. Suppose that tables `t1` and `t2` have these definitions:

```sql
CREATE TABLE t1 (ts TIMESTAMP NULL DEFAULT '0000-00-00 00:00:00');
CREATE TABLE t2 (ts TIMESTAMP NULL DEFAULT NULL);
```

To set the [`TIMESTAMP`](datetime.md) column in either table to the current timestamp at insert time, explicitly assign it that value. For example:

```sql
INSERT INTO t2 VALUES (CURRENT_TIMESTAMP);
INSERT INTO t1 VALUES (NOW());
```

If the [`explicit_defaults_for_timestamp`](server-system-variables.md) system variable is enabled, [`TIMESTAMP`](datetime.md) columns permit `NULL` values only if declared with the `NULL` attribute. Also, [`TIMESTAMP`](datetime.md) columns do not permit assigning `NULL` to assign the current timestamp, whether declared with the `NULL` or `NOT NULL` attribute. To assign the current timestamp, set the column to [`CURRENT_TIMESTAMP`](date-and-time-functions.md) or a synonym such as [`NOW()`](date-and-time-functions.md).