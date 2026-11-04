---
title: "MySQL :: MySQL 26.7 Reference Manual :: 12.3.7 The National Character Set"
book: MySQL 26.7 Reference Manual
version: "26.7"
source: "https://dev.mysql.com/doc/refman/26.7/en/charset-national.html"
tags:
  - mysql
  - mysql-26.7
  - reference-manual
---

### 12.3.7 The National Character Set

Standard SQL defines [`NCHAR`](char.md) or [`NATIONAL CHAR`](char.md) as a way to indicate that a [`CHAR`](char.md) column should use some predefined character set. MySQL uses `utf8` as this predefined character set. For example, these data type declarations are equivalent:

```sql
CHAR(10) CHARACTER SET utf8
NATIONAL CHARACTER(10)
NCHAR(10)
```

As are these:

```sql
VARCHAR(10) CHARACTER SET utf8
NATIONAL VARCHAR(10)
NVARCHAR(10)
NCHAR VARCHAR(10)
NATIONAL CHARACTER VARYING(10)
NATIONAL CHAR VARYING(10)
```

You can use ``N'*`literal`*'`` (or ``n'*`literal`*'``) to create a string in the national character set. These statements are equivalent:

```sql
SELECT N'some text';
SELECT n'some text';
SELECT _utf8'some text';
```

MySQL 26.7 interprets the national character set as `utf8mb3`, which is now deprecated. Thus, using `NATIONAL CHARACTER` or one of its synonyms to define the character set for a database, table, or column raises a warning similar to this one:

```sql
NATIONAL/NCHAR/NVARCHAR implies the character set UTF8MB3, which will be
replaced by UTF8MB4 in a future release. Please consider using CHAR(x) CHARACTER
SET UTF8MB4 in order to be unambiguous.
```