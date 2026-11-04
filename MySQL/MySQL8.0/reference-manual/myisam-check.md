---
title: "9.6.2 How to Check MyISAM Tables for Errors"
book: MySQL 8.0 Reference Manual
version: "8.0"
source: "https://dev.mysql.com/doc/refman/8.0/en/myisam-check.html"
tags:
  - mysql
  - mysql-8.0
  - reference-manual
---

MySQL 8.0 Reference Manual Including MySQL NDB Cluster 8.0

### 9.6.2 How to Check MyISAM Tables for Errors

To check a `MyISAM` table, use the following commands:

- [**myisamchk *`tbl_name`***](myisamchk.md)
	This finds 99.99% of all errors. What it cannot find is corruption that involves *only* the data file (which is very unusual). If you want to check a table, you should normally run [**myisamchk**](myisamchk.md) without options or with the `-s` (silent) option.
- [**myisamchk -m *`tbl_name`***](myisamchk.md)
	This finds 99.999% of all errors. It first checks all index entries for errors and then reads through all rows. It calculates a checksum for all key values in the rows and verifies that the checksum matches the checksum for the keys in the index tree.
- [**myisamchk -e *`tbl_name`***](myisamchk.md)
	This does a complete and thorough check of all data (`-e` means “extended check”). It does a check-read of every key for each row to verify that they indeed point to the correct row. This may take a long time for a large table that has many indexes. Normally, [**myisamchk**](myisamchk.md) stops after the first error it finds. If you want to obtain more information, you can add the `-v` (verbose) option. This causes [**myisamchk**](myisamchk.md) to keep going, up through a maximum of 20 errors.
- [**myisamchk -e -i *`tbl_name`***](myisamchk.md)
	This is like the previous command, but the `-i` option tells [**myisamchk**](myisamchk.md) to print additional statistical information.

In most cases, a simple [**myisamchk**](myisamchk.md) command with no arguments other than the table name is sufficient to check a table.