---
title: "11.2.4 Mapping of Identifiers to File Names"
book: MySQL 9.7 Reference Manual
version: "9.7"
source: "https://dev.mysql.com/doc/refman/9.7/en/identifier-mapping.html"
tags:
  - mysql
  - mysql-9.7
  - reference-manual
---

MySQL 9.7 Reference Manual Including MySQL NDB Cluster 9.7

### 11.2.4 Mapping of Identifiers to File Names

There is a correspondence between database and table identifiers and names in the file system. For the basic structure, MySQL represents each database as a directory in the data directory, and depending upon the storage engine, each table may be represented by one or more files in the appropriate database directory.

For the data and index files, the exact representation on disk is storage engine specific. These files may be stored in the database directory, or the information may be stored in a separate file. `InnoDB` data is stored in the InnoDB data files. If you are using tablespaces with `InnoDB`, then the specific tablespace files you create are used instead.

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

The following names are reserved and appended with `@@@` if used in schema or table names:

- CON
- PRN
- AUX
- NUL
- COM1 through COM9
- LPT1 through LPT9

CLOCK$ is also a member of this group of reserved names, but is not appended with `@@@`, but `@0024` instead. That is, if CLOCK$ is used as a schema or table name, it is written to the file system as `CLOCK@0024`. The same is true for any use of $ (dollar sign) in a schema or table name; it is replaced with `@0024` on the filesystem.

Note

These names are also written to [`INNODB_TABLES`](information-schema-innodb-tables-table.md) in their appended forms, but are written to [`TABLES`](information-schema-tables-table.md) in their unappended form, as entered by the user.