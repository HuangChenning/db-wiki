---
title: "MySQL :: MySQL 26.10 Reference Manual :: 14.4 Operators"
book: MySQL 26.10 Reference Manual
version: "26.10"
source: "https://dev.mysql.com/doc/refman/26.10/en/non-typed-operators.html"
tags:
  - mysql
  - mysql-26.10
  - reference-manual
---

## 14.4 Operators

**Table 14.3 Operators**

| Name | Description | Deprecated |
| --- | --- | --- |
| [`&`](bit-functions.md) | Bitwise AND |  |
| [`>`](comparison-operators.md) | Greater than operator |  |
| [`>>`](bit-functions.md) | Right shift |  |
| [`>=`](comparison-operators.md) | Greater than or equal operator |  |
| [`<`](comparison-operators.md) | Less than operator |  |
| [`<>`, `!=`](comparison-operators.md) | Not equal operator |  |
| [`<<`](bit-functions.md) | Left shift |  |
| [`<=`](comparison-operators.md) | Less than or equal operator |  |
| [`<=>`](comparison-operators.md) | NULL-safe equal to operator |  |
| [`%`, `MOD`](arithmetic-functions.md) | Modulo operator |  |
| [`*`](arithmetic-functions.md) | Multiplication operator |  |
| [`+`](arithmetic-functions.md) | Addition operator |  |
| [`-`](arithmetic-functions.md) | Minus operator |  |
| [`-`](arithmetic-functions.md) | Change the sign of the argument |  |
| [`->`](json-search-functions.md) | Return value from JSON column after evaluating path; equivalent to JSON\_EXTRACT(). |  |
| [`->>`](json-search-functions.md) | Return value from JSON column after evaluating path and unquoting the result; equivalent to JSON\_UNQUOTE(JSON\_EXTRACT()). |  |
| [`/`](arithmetic-functions.md) | Division operator |  |
| [`:=`](assignment-operators.md) | Assign a value |  |
| [`=`](assignment-operators.md) | Assign a value (as part of a [`SET`](set-variable.md) statement, or as part of the `SET` clause in an [`UPDATE`](update.md) statement) |  |
| [`=`](comparison-operators.md) | Equal operator |  |
| [`^`](bit-functions.md) | Bitwise XOR |  |
| [`AND`, `&&`](logical-operators.md) | Logical AND |  |
| [`BETWEEN ... AND ...`](comparison-operators.md) | Whether a value is within a range of values |  |
| [`BINARY`](cast-functions.md) | Cast a string to a binary string | Yes |
| [`CASE`](flow-control-functions.md) | Case operator |  |
| [`DIV`](arithmetic-functions.md) | Integer division |  |
| [`EXISTS()`](comparison-operators.md) | Whether the result of a query contains any rows |  |
| [`IN()`](comparison-operators.md) | Whether a value is within a set of values |  |
| [`IS`](comparison-operators.md) | Test a value against a boolean |  |
| [`IS NOT`](comparison-operators.md) | Test a value against a boolean |  |
| [`IS NOT NULL`](comparison-operators.md) | NOT NULL value test |  |
| [`IS NULL`](comparison-operators.md) | NULL value test |  |
| [`LIKE`](string-comparison-functions.md) | Simple pattern matching |  |
| [`MEMBER OF()`](json-search-functions.md) | Returns true (1) if first operand matches any element of JSON array passed as second operand, otherwise returns false (0) |  |
| [`NOT`, `!`](logical-operators.md) | Negates value |  |
| [`NOT BETWEEN ... AND ...`](comparison-operators.md) | Whether a value is not within a range of values |  |
| [`NOT EXISTS()`](comparison-operators.md) | Whether the result of a query contains no rows |  |
| [`NOT IN()`](comparison-operators.md) | Whether a value is not within a set of values |  |
| [`NOT LIKE`](string-comparison-functions.md) | Negation of simple pattern matching |  |
| [`NOT REGEXP`](regexp.md) | Negation of REGEXP |  |
| [`OR`, `\|\|`](logical-operators.md) | Logical OR |  |
| [`REGEXP`](regexp.md) | Whether string matches regular expression |  |
| [`RLIKE`](regexp.md) | Whether string matches regular expression |  |
| [`SOUNDS LIKE`](string-functions.md) | Compare sounds |  |
| [`XOR`](logical-operators.md) | Logical XOR |  |
| [`\|`](bit-functions.md) | Bitwise OR |  |
| [`~`](bit-functions.md) | Bitwise inversion |  |