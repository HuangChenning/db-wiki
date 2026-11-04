---
title: "14.4.1 Operator Precedence"
book: MySQL 8.4 Reference Manual
version: "8.4"
source: "https://dev.mysql.com/doc/refman/8.4/en/operator-precedence.html"
tags:
  - mysql
  - mysql-8.4
  - reference-manual
---

MySQL 8.4 Reference Manual Including MySQL NDB Cluster 8.4

### 14.4.1 Operator Precedence

Operator precedences are shown in the following list, from highest precedence to the lowest. Operators that are shown together on a line have the same precedence.

```
INTERVAL
BINARY, COLLATE
!
- (unary minus), ~ (unary bit inversion)
^
*, /, DIV, %, MOD
-, +
<<, >>
&
|
= (comparison), <=>, >=, >, <=, <, <>, !=, IS, LIKE, REGEXP, IN, MEMBER OF
BETWEEN, CASE, WHEN, THEN, ELSE
NOT
AND, &&
XOR
OR, ||
= (assignment), :=
```

The precedence of `=` depends on whether it is used as a comparison operator ([`=`](comparison-operators.md)) or as an assignment operator ([`=`](assignment-operators.md)). When used as a comparison operator, it has the same precedence as [`<=>`](comparison-operators.md), [`>=`](comparison-operators.md), [`>`](comparison-operators.md), [`<=`](comparison-operators.md), [`<`](comparison-operators.md), [`<>`](comparison-operators.md), [`!=`](comparison-operators.md), [`IS`](comparison-operators.md), [`LIKE`](string-comparison-functions.md), [`REGEXP`](regexp.md), and [`IN()`](comparison-operators.md). When used as an assignment operator, it has the same precedence as [`:=`](assignment-operators.md). [Section 15.7.6.1, “SET Syntax for Variable Assignment”](set-variable.md), and [Section 11.4, “User-Defined Variables”](user-variables.md), explain how MySQL determines which interpretation of `=` should apply.

For operators that occur at the same precedence level within an expression, evaluation proceeds left to right, with the exception that assignments evaluate right to left.

The precedence and meaning of some operators depends on the SQL mode:

- By default, [`||`](logical-operators.md) is a logical [`OR`](logical-operators.md) operator. With [`PIPES_AS_CONCAT`](sql-mode.md) enabled, [`||`](logical-operators.md) is string concatenation, with a precedence between [`^`](bit-functions.md) and the unary operators.
- By default, [`!`](logical-operators.md) has a higher precedence than `NOT`. With [`HIGH_NOT_PRECEDENCE`](sql-mode.md) enabled, [`!`](logical-operators.md) and `NOT` have the same precedence.

See [Section 7.1.11, “Server SQL Modes”](sql-mode.md).

The precedence of operators determines the order of evaluation of terms in an expression. To override this order and group terms explicitly, use parentheses. For example:

```
mysql> SELECT 1+2*3;
        -> 7
mysql> SELECT (1+2)*3;
        -> 9
```