---
title: "MySQL :: MySQL 26.10 Reference Manual :: 14.4.3 Logical Operators"
book: MySQL 26.10 Reference Manual
version: "26.10"
source: "https://dev.mysql.com/doc/refman/26.10/en/logical-operators.html"
tags:
  - mysql
  - mysql-26.10
  - reference-manual
---

### 14.4.3 Logical Operators

**Table 14.5 Logical Operators**

| Name | Description |
| --- | --- |
| `AND`, `&&` | Logical AND |
| `NOT`, `!` | Negates value |
| `OR`, `\|\|` | Logical OR |
| `XOR` | Logical XOR |

In SQL, all logical operators evaluate to `TRUE`, `FALSE`, or `NULL` (`UNKNOWN`). In MySQL, these are implemented as 1 (`TRUE`), 0 (`FALSE`), and `NULL`. Most of this is common to different SQL database servers, although some servers may return any nonzero value for `TRUE`.

MySQL evaluates any nonzero, non- `NULL` value to `TRUE`. For example, the following statements all assess to `TRUE`:

```sql
mysql> SELECT 10 IS TRUE;
-> 1
mysql> SELECT -10 IS TRUE;
-> 1
mysql> SELECT 'string' IS NOT NULL;
-> 1
```

- `NOT`, `!`
	Logical NOT. Evaluates to `1` if the operand is `0`, to `0` if the operand is nonzero, and `NOT NULL` returns `NULL`.
	```sql
	mysql> SELECT NOT 10;
	        -> 0
	mysql> SELECT NOT 0;
	        -> 1
	mysql> SELECT NOT NULL;
	        -> NULL
	mysql> SELECT ! (1+1);
	        -> 0
	mysql> SELECT ! 1+1;
	        -> 1
	```
	The last example produces `1` because the expression evaluates the same way as `(!1)+1`.
	The `!` operator is a nonstandard extension, and is deprecated; expect it to be removed in a future version of MySQL. Applications, where necessary, should be adjusted to use the standard SQL `NOT` operator instead.
- `AND`, `&&`
	Logical AND. Evaluates to `1` if all operands are nonzero and not `NULL`, to `0` if one or more operands are `0`, otherwise `NULL` is returned.
	```sql
	mysql> SELECT 1 AND 1;
	        -> 1
	mysql> SELECT 1 AND 0;
	        -> 0
	mysql> SELECT 1 AND NULL;
	        -> NULL
	mysql> SELECT 0 AND NULL;
	        -> 0
	mysql> SELECT NULL AND 0;
	        -> 0
	```
	The `&&`, operator is a nonstandard extension and is deprecated; expect support for it to be removed in a future version of MySQL. Applications, where necessary, should be adjusted to use the standard SQL `AND` operator instead.
- `OR`, `||`
	Logical OR. When both operands are non- `NULL`, the result is `1` if any operand is nonzero, and `0` otherwise. With a `NULL` operand, the result is `1` if the other operand is nonzero, and `NULL` otherwise. If both operands are `NULL`, the result is `NULL`.
	```sql
	mysql> SELECT 1 OR 1;
	        -> 1
	mysql> SELECT 1 OR 0;
	        -> 1
	mysql> SELECT 0 OR 0;
	        -> 0
	mysql> SELECT 0 OR NULL;
	        -> NULL
	mysql> SELECT 1 OR NULL;
	        -> 1
	```
	Note
	If the [`PIPES_AS_CONCAT`](sql-mode.md) SQL mode is enabled, `||` signifies the SQL-standard string concatenation operator (like [`CONCAT()`](string-functions.md)).
	The `||`, operator is a nonstandard extension, and is deprecated; expect support for it to be removed in a future version of MySQL. Applications, where necessary, should be adjusted to use the standard SQL `OR` operator instead. Exception: Deprecation does not apply if [`PIPES_AS_CONCAT`](sql-mode.md) is enabled because, in that case, `||` signifies string concatenation.
- `XOR`
	Logical XOR. Returns `NULL` if either operand is `NULL`. For non- `NULL` operands, evaluates to `1` if an odd number of operands is nonzero, otherwise `0` is returned.
	```sql
	mysql> SELECT 1 XOR 1;
	        -> 0
	mysql> SELECT 1 XOR 0;
	        -> 1
	mysql> SELECT 1 XOR NULL;
	        -> NULL
	mysql> SELECT 1 XOR 1 XOR 1;
	        -> 1
	```
	`a XOR b` is mathematically equal to `(a AND (NOT b)) OR ((NOT a) and b)`.