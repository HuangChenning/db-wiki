---
title: "MySQL :: MySQL 26.7 Reference Manual :: 14.26.3 Expression Handling"
book: MySQL 26.7 Reference Manual
version: "26.7"
source: "https://dev.mysql.com/doc/refman/26.7/en/precision-math-expressions.html"
tags:
  - mysql
  - mysql-26.7
  - reference-manual
---

### 14.26.3 Expression Handling

With precision math, exact-value numbers are used as given whenever possible. For example, numbers in comparisons are used exactly as given without a change in value. In strict SQL mode, for [`INSERT`](insert.md) into a column with an exact data type ([`DECIMAL`](fixed-point-types.md) or integer), a number is inserted with its exact value if it is within the column range. When retrieved, the value should be the same as what was inserted. (If strict SQL mode is not enabled, truncation for [`INSERT`](insert.md) is permissible.)

Handling of a numeric expression depends on what kind of values the expression contains:

- If any approximate values are present, the expression is approximate and is evaluated using floating-point arithmetic.
- If no approximate values are present, the expression contains only exact values. If any exact value contains a fractional part (a value following the decimal point), the expression is evaluated using [`DECIMAL`](fixed-point-types.md) exact arithmetic and has a precision of 65 digits. The term “exact” is subject to the limits of what can be represented in binary. For example, `1.0/3.0` can be approximated in decimal notation as `.333...`, but not written as an exact number, so `(1.0/3.0)*3.0` does not evaluate to exactly `1.0`.
- Otherwise, the expression contains only integer values. The expression is exact and is evaluated using integer arithmetic and has a precision the same as [`BIGINT`](integer-types.md) (64 bits).

If a numeric expression contains any strings, they are converted to double-precision floating-point values and the expression is approximate.

Inserts into numeric columns are affected by the SQL mode, which is controlled by the [`sql_mode`](server-system-variables.md) system variable. (See [Section 7.1.11, “Server SQL Modes”](sql-mode.md).) The following discussion mentions strict mode (selected by the [`STRICT_ALL_TABLES`](sql-mode.md) or [`STRICT_TRANS_TABLES`](sql-mode.md) mode values) and [`ERROR_FOR_DIVISION_BY_ZERO`](sql-mode.md). To turn on all restrictions, you can simply use [`TRADITIONAL`](sql-mode.md) mode, which includes both strict mode values and [`ERROR_FOR_DIVISION_BY_ZERO`](sql-mode.md):

```sql
SET sql_mode='TRADITIONAL';
```

If a number is inserted into an exact type column ([`DECIMAL`](fixed-point-types.md) or integer), it is inserted with its exact value if it is within the column range and precision.

If the value has too many digits in the fractional part, rounding occurs and a note is generated. Rounding is done as described in [Section 14.26.4, “Rounding Behavior”](precision-math-rounding.md). Truncation due to rounding of the fractional part is not an error, even in strict mode.

If the value has too many digits in the integer part, it is too large (out of range) and is handled as follows:

- If strict mode is not enabled, the value is truncated to the nearest legal value and a warning is generated.
- If strict mode is enabled, an overflow error occurs.

Underflow is not detected, so underflow handling is undefined.

For inserts of strings into numeric columns, conversion from string to number is handled as follows if the string has nonnumeric contents:

- A string that does not begin with a number cannot be used as a number and produces an error in strict mode, or a warning otherwise. This includes the empty string.
- A string that begins with a number can be converted, but the trailing nonnumeric portion is truncated. If the truncated portion contains anything other than spaces, this produces an error in strict mode, or a warning otherwise.

By default, division by zero produces a result of `NULL` and no warning. By setting the SQL mode appropriately, division by zero can be restricted.

With the [`ERROR_FOR_DIVISION_BY_ZERO`](sql-mode.md) SQL mode enabled, MySQL handles division by zero differently:

- If strict mode is not enabled, a warning occurs.
- If strict mode is enabled, inserts and updates involving division by zero are prohibited, and an error occurs.

In other words, inserts and updates involving expressions that perform division by zero can be treated as errors, but this requires [`ERROR_FOR_DIVISION_BY_ZERO`](sql-mode.md) in addition to strict mode.

Suppose that we have this statement:

```sql
INSERT INTO t SET i = 1/0;
```

This is what happens for combinations of strict and [`ERROR_FOR_DIVISION_BY_ZERO`](sql-mode.md) modes.

| [`sql_mode`](server-system-variables.md) Value | Result |
| --- | --- |
| `''` (Default) | No warning, no error; `i` is set to `NULL`. |
| strict | No warning, no error; `i` is set to `NULL`. |
| [`ERROR_FOR_DIVISION_BY_ZERO`](sql-mode.md) | Warning, no error; `i` is set to `NULL`. |
| strict,[`ERROR_FOR_DIVISION_BY_ZERO`](sql-mode.md) | Error condition; no row is inserted. |