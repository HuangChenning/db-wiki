---
title: "14.8.3 Character Set and Collation of Function Results"
book: MySQL 9.7 Reference Manual
version: "9.7"
source: "https://dev.mysql.com/doc/refman/9.7/en/string-functions-charset.html"
tags:
  - mysql
  - mysql-9.7
  - reference-manual
---

MySQL 9.7 Reference Manual Including MySQL NDB Cluster 9.7

### 14.8.3 Character Set and Collation of Function Results

MySQL has many operators and functions that return a string. This section answers the question: What is the character set and collation of such a string?

For simple functions that take string input and return a string result as output, the output's character set and collation are the same as those of the principal input value. For example, [``UPPER(*`X`*)``](string-functions.md) returns a string with the same character string and collation as *`X`*. The same applies for [`INSTR()`](string-functions.md), [`LCASE()`](string-functions.md), [`LOWER()`](string-functions.md), [`LTRIM()`](string-functions.md), [`MID()`](string-functions.md), [`REPEAT()`](string-functions.md), [`REPLACE()`](string-functions.md), [`REVERSE()`](string-functions.md), [`RIGHT()`](string-functions.md), [`RPAD()`](string-functions.md), [`RTRIM()`](string-functions.md), [`SOUNDEX()`](string-functions.md), [`SUBSTRING()`](string-functions.md), [`TRIM()`](string-functions.md), [`UCASE()`](string-functions.md), and [`UPPER()`](string-functions.md).

Note

The [`REPLACE()`](string-functions.md) function, unlike all other functions, always ignores the collation of the string input and performs a case-sensitive comparison.

If a string input or function result is a binary string, the string has the `binary` character set and collation. This can be checked by using the [`CHARSET()`](information-functions.md) and [`COLLATION()`](information-functions.md) functions, both of which return `binary` for a binary string argument:

```
mysql> SELECT CHARSET(BINARY 'a'), COLLATION(BINARY 'a');
+---------------------+-----------------------+
| CHARSET(BINARY 'a') | COLLATION(BINARY 'a') |
+---------------------+-----------------------+
| binary              | binary                |
+---------------------+-----------------------+
```

For operations that combine multiple string inputs and return a single string output, the “aggregation rules” of standard SQL apply for determining the collation of the result:

- If an explicit ``COLLATE             *`Y`*`` occurs, use *`Y`*.
- If explicit ``COLLATE             *`Y`*`` and ``COLLATE             *`Z`*`` occur, raise an error.
- Otherwise, if all collations are *`Y`*, use *`Y`*.
- Otherwise, the result has no collation.

For example, with ``CASE ... WHEN a THEN b WHEN b THEN c         COLLATE *`X`* END``, the resulting collation is *`X`*. The same applies for [`UNION`](union.md), [`||`](logical-operators.md), [`CONCAT()`](string-functions.md), [`ELT()`](string-functions.md), [`GREATEST()`](comparison-operators.md), [`IF()`](flow-control-functions.md), and [`LEAST()`](comparison-operators.md).

For operations that convert to character data, the character set and collation of the strings that result from the operations are defined by the [`character_set_connection`](server-system-variables.md) and [`collation_connection`](server-system-variables.md) system variables that determine the default connection character set and collation (see [Section 12.4, “Connection Character Sets and Collations”](charset-connection.md)). This applies only to [`BIN_TO_UUID()`](miscellaneous-functions.md), [`CAST()`](cast-functions.md), [`CONV()`](mathematical-functions.md), [`FORMAT()`](string-functions.md), [`HEX()`](string-functions.md), and [`SPACE()`](string-functions.md).

An exception to the preceding principle occurs for expressions for virtual generated columns. In such expressions, the table character set is used for [`BIN_TO_UUID()`](miscellaneous-functions.md), [`CONV()`](mathematical-functions.md), or [`HEX()`](string-functions.md) results, regardless of connection character set.

If there is any question about the character set or collation of the result returned by a string function, use the [`CHARSET()`](information-functions.md) or [`COLLATION()`](information-functions.md) function to find out:

```
mysql> SELECT USER(), CHARSET(USER()), COLLATION(USER());
+----------------+-----------------+--------------------+
| USER()         | CHARSET(USER()) | COLLATION(USER())  |
+----------------+-----------------+--------------------+
| test@localhost | utf8mb3         | utf8mb3_general_ci |
+----------------+-----------------+--------------------+
mysql> SELECT CHARSET(COMPRESS('abc')), COLLATION(COMPRESS('abc'));
+--------------------------+----------------------------+
| CHARSET(COMPRESS('abc')) | COLLATION(COMPRESS('abc')) |
+--------------------------+----------------------------+
| binary                   | binary                     |
+--------------------------+----------------------------+
```