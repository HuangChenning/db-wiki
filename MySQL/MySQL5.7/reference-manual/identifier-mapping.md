---
title: "9.2.4 Mapping of Identifiers to File Names"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/identifier-mapping.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 9.2.4 Mapping of Identifiers to File Names

There is a correspondence between database and table identifiers and names in the file system. For the basic structure, MySQL represents each database as a directory in the data directory, and each table by one or more files in the appropriate database directory. For the table format files (`.FRM`), the data is always stored in this structure and location.

For the data and index files, the exact representation on disk is storage engine specific. These files may be stored in the same location as the `FRM` files, or the information may be stored in a separate file. `InnoDB` data is stored in the InnoDB data files. If you are using tablespaces with `InnoDB`, then the specific tablespace files you create are used instead.

Any character is legal in database or table identifiers except ASCII NUL (`X'00'`). MySQL encodes any characters that are problematic in the corresponding file system objects when it creates database directories or table files:

- Basic Latin letters (`a..zA..Z`), digits (`0..9`) and underscore (`_`) are encoded as is. Consequently, their case sensitivity directly depends on file system features.
- All other national letters from alphabets that have uppercase/lowercase mapping are encoded as shown in the following table. Values in the Code Range column are UCS-2 values.
	| Code Range | Pattern | Number | Used | Unused | Blocks |
	| --- | --- | --- | --- | --- | --- |
	| 00C0..017F | \[@\]\[0..4\]\[g..z\] | 5\*20= 100 | 97 | 3 | Latin-1 Supplement + Latin Extended-A |
	| 0370..03FF | \[@\]\[5..9\]\[g..z\] | 5\*20= 100 | 88 | 12 | Greek and Coptic |
	| 0400..052F | \[@\]\[g..z\]\[0..6\] | 20\*7= 140 | 137 | 3 | Cyrillic + Cyrillic Supplement |
	| 0530..058F | \[@\]\[g..z\]\[7..8\] | 20\*2= 40 | 38 | 2 | Armenian |
	| 2160..217F | \[@\]\[g..z\]\[9\] | 20\*1= 20 | 16 | 4 | Number Forms |
	| 0180..02AF | \[@\]\[g..z\]\[a..k\] | 20\*11=220 | 203 | 17 | Latin Extended-B + IPA Extensions |
	| 1E00..1EFF | \[@\]\[g..z\]\[l..r\] | 20\*7= 140 | 136 | 4 | Latin Extended Additional |
	| 1F00..1FFF | \[@\]\[g..z\]\[s..z\] | 20\*8= 160 | 144 | 16 | Greek Extended |
	| ........ | \[@\]\[a..f\]\[g..z\] | 6\*20= 120 | 0 | 120 | RESERVED |
	| 24B6..24E9 | \[@\]\[@\]\[a..z\] | 26 | 26 | 0 | Enclosed Alphanumerics |
	| FF21..FF5A | \[@\]\[a..z\]\[@\] | 26 | 26 | 0 | Halfwidth and Fullwidth forms |
	One of the bytes in the sequence encodes lettercase. For example: `LATIN CAPITAL LETTER A WITH             GRAVE` is encoded as `@0G`, whereas `LATIN SMALL LETTER A WITH GRAVE` is encoded as `@0g`. Here the third byte (`G` or `g`) indicates lettercase. (On a case-insensitive file system, both letters are treated as the same.)
	For some blocks, such as Cyrillic, the second byte determines lettercase. For other blocks, such as Latin1 Supplement, the third byte determines lettercase. If two bytes in the sequence are letters (as in Greek Extended), the leftmost letter character stands for lettercase. All other letter bytes must be in lowercase.
- All nonletter characters except underscore (`_`), as well as letters from alphabets that do not have uppercase/lowercase mapping (such as Hebrew) are encoded using hexadecimal representation using lowercase letters for hexadecimal digits `a..f`:
	```
	0x003F -> @003f
	0xFFFF -> @ffff
	```
	The hexadecimal values correspond to character values in the `ucs2` double-byte character set.

On Windows, some names such as `nul`, `prn`, and `aux` are encoded by appending `@@@` to the name when the server creates the corresponding file or directory. This occurs on all platforms for portability of the corresponding database object between platforms.

If you have databases or tables from a version of MySQL older than 5.1.6 that contain special characters and for which the underlying directory names or file names have not been updated to use the new encoding, the server displays their names with a prefix of `#mysql50#` in the output from `INFORMATION_SCHEMA` tables or [`SHOW`](show.md) statements. For example, if you have a table named `a@b` and its name encoding has not been updated, [`SHOW         TABLES`](show-tables.md) displays it like this:

```
mysql> SHOW TABLES;
+----------------+
| Tables_in_test |
+----------------+
| #mysql50#a@b   |
+----------------+
```

To refer to such a name for which the encoding has not been updated, you must supply the `#mysql50#` prefix:

```
mysql> SHOW COLUMNS FROM \`a@b\`;
ERROR 1146 (42S02): Table 'test.a@b' doesn't exist

mysql> SHOW COLUMNS FROM \`#mysql50#a@b\`;
+-------+---------+------+-----+---------+-------+
| Field | Type    | Null | Key | Default | Extra |
+-------+---------+------+-----+---------+-------+
| i     | int(11) | YES  |     | NULL    |       |
+-------+---------+------+-----+---------+-------+
```

To update old names to eliminate the need to use the special prefix to refer to them, re-encode them with [**mysqlcheck**](mysqlcheck.md). The following commands update all names to the new encoding:

```
mysqlcheck --check-upgrade --all-databases
mysqlcheck --fix-db-names --fix-table-names --all-databases
```

To check only specific databases or tables, omit [`--all-databases`](mysqlcheck.md) and provide the appropriate database or table arguments. For information about [**mysqlcheck**](mysqlcheck.md) invocation syntax, see [Section 4.5.3, “mysqlcheck — A Table Maintenance Program”](mysqlcheck.md).

Note

The `#mysql50#` prefix is intended only to be used internally by the server. You should not create databases or tables with names that use this prefix.

Also, [**mysqlcheck**](mysqlcheck.md) cannot fix names that contain literal instances of the `@` character that is used for encoding special characters. If you have databases or tables that contain this character, use [**mysqldump**](mysqldump.md) to dump them before upgrading to MySQL 5.1.6 or later, and then reload the dump file after upgrading.

Note

Conversion of pre-MySQL 5.1 database names containing special characters to 5.1 format with the addition of a `#mysql50#` prefix is deprecated; expect it to be removed in a future version of MySQL. Because such conversions are deprecated, the [`--fix-db-names`](mysqlcheck.md) and [`--fix-table-names`](mysqlcheck.md) options for [**mysqlcheck**](mysqlcheck.md) and the `UPGRADE           DATA DIRECTORY NAME` clause for the [`ALTER DATABASE`](alter-database.md) statement are also deprecated.

Upgrades are supported only from one release series to another (for example, 5.0 to 5.1, or 5.1 to 5.5), so there should be little remaining need for conversion of older 5.0 database names to current versions of MySQL. As a workaround, upgrade a MySQL 5.0 installation to MySQL 5.1 before upgrading to a more recent release.