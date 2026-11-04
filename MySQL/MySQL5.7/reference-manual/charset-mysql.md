---
title: "10.2 Character Sets and Collations in MySQL"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/charset-mysql.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

MySQL Server supports multiple character sets. To display the available character sets, use the `INFORMATION_SCHEMA` [`CHARACTER_SETS`](information-schema-character-sets-table.md) table or the [`SHOW CHARACTER SET`](show-character-set.md) statement. A partial listing follows. For more complete information, see [Section 10.10, “Supported Character Sets and Collations”](charset-charsets.md).

```
mysql> SHOW CHARACTER SET;
+----------+---------------------------------+---------------------+--------+
| Charset  | Description                     | Default collation   | Maxlen |
+----------+---------------------------------+---------------------+--------+
| big5     | Big5 Traditional Chinese        | big5_chinese_ci     |      2 |
...
| latin1   | cp1252 West European            | latin1_swedish_ci   |      1 |
| latin2   | ISO 8859-2 Central European     | latin2_general_ci   |      1 |
...
| utf8     | UTF-8 Unicode                   | utf8_general_ci     |      3 |
| ucs2     | UCS-2 Unicode                   | ucs2_general_ci     |      2 |
...
| utf8mb4  | UTF-8 Unicode                   | utf8mb4_general_ci  |      4 |
...
| binary   | Binary pseudo charset           | binary              |      1 |
...
```

By default, the [`SHOW CHARACTER SET`](show-character-set.md) statement displays all available character sets. It takes an optional [`LIKE`](string-comparison-functions.md) or `WHERE` clause that indicates which character set names to match. For example:

```
mysql> SHOW CHARACTER SET LIKE 'latin%';
+---------+-----------------------------+-------------------+--------+
| Charset | Description                 | Default collation | Maxlen |
+---------+-----------------------------+-------------------+--------+
| latin1  | cp1252 West European        | latin1_swedish_ci |      1 |
| latin2  | ISO 8859-2 Central European | latin2_general_ci |      1 |
| latin5  | ISO 8859-9 Turkish          | latin5_turkish_ci |      1 |
| latin7  | ISO 8859-13 Baltic          | latin7_general_ci |      1 |
+---------+-----------------------------+-------------------+--------+
```

A given character set always has at least one collation, and most character sets have several. To list the display collations for a character set, use the `INFORMATION_SCHEMA` [`COLLATIONS`](information-schema-collations-table.md) table or the [`SHOW COLLATION`](show-collation.md) statement.

By default, the [`SHOW COLLATION`](show-collation.md) statement displays all available collations. It takes an optional [`LIKE`](string-comparison-functions.md) or `WHERE` clause that indicates which collation names to display. For example, to see the collations for the default character set, `latin1` (cp1252 West European), use this statement:

```
mysql> SHOW COLLATION WHERE Charset = 'latin1';
+-------------------+---------+----+---------+----------+---------+
| Collation         | Charset | Id | Default | Compiled | Sortlen |
+-------------------+---------+----+---------+----------+---------+
| latin1_german1_ci | latin1  |  5 |         | Yes      |       1 |
| latin1_swedish_ci | latin1  |  8 | Yes     | Yes      |       1 |
| latin1_danish_ci  | latin1  | 15 |         | Yes      |       1 |
| latin1_german2_ci | latin1  | 31 |         | Yes      |       2 |
| latin1_bin        | latin1  | 47 |         | Yes      |       1 |
| latin1_general_ci | latin1  | 48 |         | Yes      |       1 |
| latin1_general_cs | latin1  | 49 |         | Yes      |       1 |
| latin1_spanish_ci | latin1  | 94 |         | Yes      |       1 |
+-------------------+---------+----+---------+----------+---------+
```

The `latin1` collations have the following meanings.

| Collation | Meaning |
| --- | --- |
| `latin1_bin` | Binary according to `latin1` encoding |
| `latin1_danish_ci` | Danish/Norwegian |
| `latin1_general_ci` | Multilingual (Western European) |
| `latin1_general_cs` | Multilingual (ISO Western European), case-sensitive |
| `latin1_german1_ci` | German DIN-1 (dictionary order) |
| `latin1_german2_ci` | German DIN-2 (phone book order) |
| `latin1_spanish_ci` | Modern Spanish |
| `latin1_swedish_ci` | Swedish/Finnish |

Collations have these general characteristics:

- Two different character sets cannot have the same collation.
- Each character set has a *default collation*. For example, the default collations for `latin1` and `utf8` are `latin1_swedish_ci` and `utf8_general_ci`, respectively. The `INFORMATION_SCHEMA` [`CHARACTER_SETS`](information-schema-character-sets-table.md) table and the [`SHOW CHARACTER SET`](show-character-set.md) statement indicate the default collation for each character set. The `INFORMATION_SCHEMA` [`COLLATIONS`](information-schema-collations-table.md) table and the [`SHOW COLLATION`](show-collation.md) statement have a column that indicates for each collation whether it is the default for its character set (`Yes` if so, empty if not).
- Collation names start with the name of the character set with which they are associated, generally followed by one or more suffixes indicating other collation characteristics. For additional information about naming conventions, see [Section 10.3.1, “Collation Naming Conventions”](charset-collation-names.md).

When a character set has multiple collations, it might not be clear which collation is most suitable for a given application. To avoid choosing an inappropriate collation, perform some comparisons with representative data values to make sure that a given collation sorts values the way you expect.