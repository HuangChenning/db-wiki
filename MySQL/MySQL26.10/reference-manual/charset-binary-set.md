---
title: "MySQL :: MySQL 26.10 Reference Manual :: 12.10.8 The Binary Character Set"
book: MySQL 26.10 Reference Manual
version: "26.10"
source: "https://dev.mysql.com/doc/refman/26.10/en/charset-binary-set.html"
tags:
  - mysql
  - mysql-26.10
  - reference-manual
---

### 12.10.8 The Binary Character Set

The `binary` character set is the character set for binary strings, which are sequences of bytes. The `binary` character set has one collation, also named `binary`. Comparison and sorting are based on numeric byte values, rather than on numeric character code values (which for multibyte characters differ from numeric byte values). For information about the differences between the `binary` collation of the `binary` character set and the `_bin` collations of nonbinary character sets, see [Section 12.8.5, “The binary Collation Compared to \_bin Collations”](charset-binary-collations.md).

For the `binary` character set, the concepts of lettercase and accent equivalence do not apply:

- For single-byte characters stored as binary strings, character and byte boundaries are the same, so lettercase and accent differences are significant in comparisons. That is, the `binary` collation is case-sensitive and accent-sensitive.
	```sql
	mysql> SET NAMES 'binary';
	mysql> SELECT CHARSET('abc'), COLLATION('abc');
	+----------------+------------------+
	| CHARSET('abc') | COLLATION('abc') |
	+----------------+------------------+
	| binary         | binary           |
	+----------------+------------------+
	mysql> SELECT 'abc' = 'ABC', 'a' = 'ä';
	+---------------+------------+
	| 'abc' = 'ABC' | 'a' = 'ä'  |
	+---------------+------------+
	|             0 |          0 |
	+---------------+------------+
	```
- For multibyte characters stored as binary strings, character and byte boundaries differ. Character boundaries are lost, so comparisons that depend on them are not meaningful.

To perform lettercase conversion of a binary string, first convert it to a nonbinary string using a character set appropriate for the data stored in the string:

```sql
mysql> SET @str = BINARY 'New York';
mysql> SELECT LOWER(@str), LOWER(CONVERT(@str USING utf8mb4));
+-------------+------------------------------------+
| LOWER(@str) | LOWER(CONVERT(@str USING utf8mb4)) |
+-------------+------------------------------------+
| New York    | new york                           |
+-------------+------------------------------------+
```

To convert a string expression to a binary string, these constructs are equivalent:

```sql
BINARY expr
CAST(expr AS BINARY)
CONVERT(expr USING BINARY)
```

If a value is a character string literal, the `_binary` introducer may be used to designate it as a binary string. For example:

```sql
_binary 'a'
```

The `_binary` introducer is permitted for hexadecimal literals and bit-value literals as well, but unnecessary; such literals are binary strings by default.

For more information about introducers, see [Section 12.3.8, “Character Set Introducers”](charset-introducer.md).

Note

Within the [**mysql**](mysql.md) client, binary strings display using hexadecimal notation, depending on the value of the [`--binary-as-hex`](mysql-command-options.md). For more information about that option, see [Section 6.5.1, “mysql — The MySQL Command-Line Client”](mysql.md).