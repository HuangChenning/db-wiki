---
title: "11.7 Comments"
book: MySQL 9.7 Reference Manual
version: "9.7"
source: "https://dev.mysql.com/doc/refman/9.7/en/comments.html"
tags:
  - mysql
  - mysql-9.7
  - reference-manual
---

MySQL 9.7 Reference Manual Including MySQL NDB Cluster 9.7

MySQL Server supports three comment styles:

- From a `#` character to the end of the line.
- From a `-- ` sequence to the end of the line. In MySQL, the `-- ` (double-dash) comment style requires the second dash to be followed by at least one whitespace or control character, such as a space or tab. This syntax differs slightly from standard SQL comment syntax, as discussed in [Section 1.7.2.4, “'--' as the Start of a Comment”](ansi-diff-comments.md).
- From a `/*` sequence to the following `*/` sequence, as in the C programming language. This syntax enables a comment to extend over multiple lines because the beginning and closing sequences need not be on the same line.

The following example demonstrates all three comment styles:

```
mysql> SELECT 1+1;     # This comment continues to the end of line
mysql> SELECT 1+1;     -- This comment continues to the end of line
mysql> SELECT 1 /* this is an in-line comment */ + 1;
mysql> SELECT 1+
/*
this is a
multiple-line comment
*/
1;
```

Nested comments are not supported, and are deprecated; expect them to be removed in a future MySQL release. (Under some conditions, nested comments might be permitted, but usually are not, and users should avoid them.)

MySQL Server supports certain variants of C-style comments. These enable you to write code that includes MySQL extensions, but is still portable, by using comments of the following form:

```
/*! MySQL-specific code */
```

In this case, MySQL Server parses and executes the code within the comment as it would any other SQL statement, but other SQL servers should ignore the extensions. For example, MySQL Server recognizes the `STRAIGHT_JOIN` keyword in the following statement, but other servers should not:

```
SELECT /*! STRAIGHT_JOIN */ col1 FROM table1,table2 WHERE ...
```

If you add a version number after the `!` character, the syntax within the comment is executed only if the MySQL version is greater than or equal to the specified version number. The `KEY_BLOCK_SIZE` keyword in the following comment is executed only by servers from MySQL 5.1.10 or higher:

```
CREATE TABLE t1(a INT, KEY (a)) /*!50110 KEY_BLOCK_SIZE=1024 */;
```

The version number uses the format *`Mmmrr`*, where *`M`* is a major version, *`mm`* is a two-digit minor version, and *`rr`* is a two-digit release number. For example: In a statement to be run only by a MySQL server version 9.7.0 or later, use `90700` in the comment.

In MySQL 9.7, the version number can also optionally be comprised of six digits in *`MMmmrr`* format, where *`MM`* is a two-digit major version, and *`mm`* and *`rr`* are the two-digit minor version and two-digit release numbers, respectively.

The version number should be followed by at least one whitespace character (or the end of the comment). If the comment begins with six digits followed by whitespace, this is interpreted as a six-digit version number. Otherwise, if it begins with at least five digits, these are interpreted as a five-digit version number (and any remaining characters ignored for this purpose); if it begins with fewer than five digits, the comment is handled as a normal MySQL comment.

The comment syntax just described applies to how the [**mysqld**](mysqld.md) server parses SQL statements. The [**mysql**](mysql.md) client program also performs some parsing of statements before sending them to the server. (It does this to determine statement boundaries within a multiple-statement input line.) For information about differences between the server and [**mysql**](mysql.md) client parsers, see [Section 6.5.1.6, “mysql Client Tips”](mysql-tips.md).

Comments in `/*!12345 ... */` format are not stored on the server. If this format is used to comment stored programs, the comments are not retained in the program body.

Another variant of C-style comment syntax is used to specify optimizer hints. Hint comments include a `+` character following the `/*` comment opening sequence. Example:

```
SELECT /*+ BKA(t1) */ FROM ... ;
```

For more information, see [Section 10.9.3, “Optimizer Hints”](optimizer-hints.md).

The use of short-form [**mysql**](mysql.md) commands such as `\C` within multiple-line `/* ...       */` comments is not supported. Short-form commands do work within single-line `/*! ... */` version comments, as do `/*+ ... */` optimizer-hint comments, which are stored in object definitions. If there is a concern that optimizer-hint comments may be stored in object definitions so that dump files when reloaded with `mysql` would result in execution of such commands, either invoke [**mysql**](mysql.md) with the [`--binary-mode`](mysql-command-options.md) option or use a reload client other than [**mysql**](mysql.md).