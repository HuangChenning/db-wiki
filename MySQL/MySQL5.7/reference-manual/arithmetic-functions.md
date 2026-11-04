---
title: "12.6.1 Arithmetic Operators"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/arithmetic-functions.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 12.6.1 Arithmetic Operators

**Table 12.9 Arithmetic Operators**

| Name | Description |
| --- | --- |
| `%`, `MOD` | Modulo operator |
| `*` | Multiplication operator |
| `+` | Addition operator |
| `-` | Minus operator |
| `-` | Change the sign of the argument |
| `/` | Division operator |
| `DIV` | Integer division |

The usual arithmetic operators are available. The result is determined according to the following rules:

- In the case of `-`, `+`, and `*`, the result is calculated with [`BIGINT`](integer-types.md) (64-bit) precision if both operands are integers.
- If both operands are integers and any of them are unsigned, the result is an unsigned integer. For subtraction, if the [`NO_UNSIGNED_SUBTRACTION`](sql-mode.md) SQL mode is enabled, the result is signed even if any operand is unsigned.
- If any of the operands of a `+`, `-`, `/`, `*`, `%` is a real or string value, the precision of the result is the precision of the operand with the maximum precision.
- In division performed with `/`, the scale of the result when using two exact-value operands is the scale of the first operand plus the value of the [`div_precision_increment`](server-system-variables.md) system variable (which is 4 by default). For example, the result of the expression `5.05 / 0.014` has a scale of six decimal places (`360.714286`).

These rules are applied for each operation, such that nested calculations imply the precision of each component. Hence, `(14620 / 9432456) / (24250 / 9432456)`, resolves first to `(0.0014) / (0.0026)`, with the final result having 8 decimal places (`0.60288653`).

Because of these rules and the way they are applied, care should be taken to ensure that components and subcomponents of a calculation use the appropriate level of precision. See [Section 12.10, “Cast Functions and Operators”](cast-functions.md).

For information about handling of overflow in numeric expression evaluation, see [Section 11.1.7, “Out-of-Range and Overflow Handling”](out-of-range-and-overflow.md).

Arithmetic operators apply to numbers. For other types of values, alternative operations may be available. For example, to add date values, use [`DATE_ADD()`](date-and-time-functions.md); see [Section 12.7, “Date and Time Functions”](date-and-time-functions.md).

- `+`
	Addition:
	```
	mysql> SELECT 3+5;
	        -> 8
	```
- `-`
	Subtraction:
	```
	mysql> SELECT 3-5;
	        -> -2
	```
- `-`
	Unary minus. This operator changes the sign of the operand.
	```
	mysql> SELECT - 2;
	        -> -2
	```
	Note
	If this operator is used with a [`BIGINT`](integer-types.md), the return value is also a [`BIGINT`](integer-types.md). This means that you should avoid using `-` on integers that may have the value of −2 <sup>63</sup>.
- `*`
	Multiplication:
	```
	mysql> SELECT 3*5;
	        -> 15
	mysql> SELECT 18014398509481984*18014398509481984.0;
	        -> 324518553658426726783156020576256.0
	mysql> SELECT 18014398509481984*18014398509481984;
	        -> out-of-range error
	```
	The last expression produces an error because the result of the integer multiplication exceeds the 64-bit range of [`BIGINT`](integer-types.md) calculations. (See [Section 11.1, “Numeric Data Types”](numeric-types.md).)
- `/`
	Division:
	```
	mysql> SELECT 3/5;
	        -> 0.60
	```
	Division by zero produces a `NULL` result:
	```
	mysql> SELECT 102/(1-1);
	        -> NULL
	```
	A division is calculated with [`BIGINT`](integer-types.md) arithmetic only if performed in a context where its result is converted to an integer.
- `DIV`
	Integer division. Discards from the division result any fractional part to the right of the decimal point.
	If either operand has a noninteger type, the operands are converted to [`DECIMAL`](fixed-point-types.md) and divided using [`DECIMAL`](fixed-point-types.md) arithmetic before converting the result to [`BIGINT`](integer-types.md). If the result exceeds `BIGINT` range, an error occurs.
	```
	mysql> SELECT 5 DIV 2, -5 DIV 2, 5 DIV -2, -5 DIV -2;
	        -> 2, -2, -2, 2
	```
- ``*`N`*             % *`M`*``, ``*`N`*             MOD *`M`*``
	Modulo operation. Returns the remainder of *`N`* divided by *`M`*. For more information, see the description for the [`MOD()`](mathematical-functions.md) function in [Section 12.6.2, “Mathematical Functions”](mathematical-functions.md).