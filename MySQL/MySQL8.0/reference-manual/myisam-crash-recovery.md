---
title: "9.6.1 Using myisamchk for Crash Recovery"
book: MySQL 8.0 Reference Manual
version: "8.0"
source: "https://dev.mysql.com/doc/refman/8.0/en/myisam-crash-recovery.html"
tags:
  - mysql
  - mysql-8.0
  - reference-manual
---

MySQL 8.0 Reference Manual Including MySQL NDB Cluster 8.0

### 9.6.1 Using myisamchk for Crash Recovery

This section describes how to check for and deal with data corruption in MySQL databases. If your tables become corrupted frequently, you should try to find the reason why. See [Section B.3.3.3, “What to Do If MySQL Keeps Crashing”](crashing.md).

For an explanation of how `MyISAM` tables can become corrupted, see [Section 18.2.4, “MyISAM Table Problems”](myisam-table-problems.md).

If you run [**mysqld**](mysqld.md) with external locking disabled (which is the default), you cannot reliably use [**myisamchk**](myisamchk.md) to check a table when [**mysqld**](mysqld.md) is using the same table. If you can be certain that no one can access the tables using [**mysqld**](mysqld.md) while you run [**myisamchk**](myisamchk.md), you only have to execute [**mysqladmin flush-tables**](mysqladmin.md) before you start checking the tables. If you cannot guarantee this, you must stop [**mysqld**](mysqld.md) while you check the tables. If you run [**myisamchk**](myisamchk.md) to check tables that [**mysqld**](mysqld.md) is updating at the same time, you may get a warning that a table is corrupt even when it is not.

If the server is run with external locking enabled, you can use [**myisamchk**](myisamchk.md) to check tables at any time. In this case, if the server tries to update a table that [**myisamchk**](myisamchk.md) is using, the server waits for [**myisamchk**](myisamchk.md) to finish before it continues.

If you use [**myisamchk**](myisamchk.md) to repair or optimize tables, you *must* always ensure that the [**mysqld**](mysqld.md) server is not using the table (this also applies if external locking is disabled). If you do not stop [**mysqld**](mysqld.md), you should at least do a [**mysqladmin flush-tables**](mysqladmin.md) before you run [**myisamchk**](myisamchk.md). Your tables *may become corrupted* if the server and [**myisamchk**](myisamchk.md) access the tables simultaneously.

When performing crash recovery, it is important to understand that each `MyISAM` table *`tbl_name`* in a database corresponds to the three files in the database directory shown in the following table.

| File | Purpose |
| --- | --- |
| ``*`tbl_name`*.MYD`` | Data file |
| ``*`tbl_name`*.MYI`` | Index file |

Each of these three file types is subject to corruption in various ways, but problems occur most often in data files and index files.

[**myisamchk**](myisamchk.md) works by creating a copy of the `.MYD` data file row by row. It ends the repair stage by removing the old `.MYD` file and renaming the new file to the original file name. If you use [`--quick`](myisamchk-repair-options.md), [**myisamchk**](myisamchk.md) does not create a temporary `.MYD` file, but instead assumes that the `.MYD` file is correct and generates only a new index file without touching the `.MYD` file. This is safe, because [**myisamchk**](myisamchk.md) automatically detects whether the `.MYD` file is corrupt and aborts the repair if it is. You can also specify the [`--quick`](myisamchk-repair-options.md) option twice to [**myisamchk**](myisamchk.md). In this case, [**myisamchk**](myisamchk.md) does not abort on some errors (such as duplicate-key errors) but instead tries to resolve them by modifying the `.MYD` file. Normally the use of two [`--quick`](myisamchk-repair-options.md) options is useful only if you have too little free disk space to perform a normal repair. In this case, you should at least make a backup of the table before running [**myisamchk**](myisamchk.md).