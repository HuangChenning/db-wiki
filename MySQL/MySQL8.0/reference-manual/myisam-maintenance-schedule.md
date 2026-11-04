---
title: "9.6.5 Setting Up a MyISAM Table Maintenance Schedule"
book: MySQL 8.0 Reference Manual
version: "8.0"
source: "https://dev.mysql.com/doc/refman/8.0/en/myisam-maintenance-schedule.html"
tags:
  - mysql
  - mysql-8.0
  - reference-manual
---

MySQL 8.0 Reference Manual Including MySQL NDB Cluster 8.0

### 9.6.5 Setting Up a MyISAM Table Maintenance Schedule

It is a good idea to perform table checks on a regular basis rather than waiting for problems to occur. One way to check and repair `MyISAM` tables is with the [`CHECK TABLE`](check-table.md) and [`REPAIR TABLE`](repair-table.md) statements. See [Section 15.7.3, “Table Maintenance Statements”](table-maintenance-statements.md).

Another way to check tables is to use [**myisamchk**](myisamchk.md). For maintenance purposes, you can use [**myisamchk -s**](myisamchk.md). The `-s` option (short for [`--silent`](myisamchk-general-options.md)) causes [**myisamchk**](myisamchk.md) to run in silent mode, printing messages only when errors occur.

It is also a good idea to enable automatic `MyISAM` table checking. For example, whenever the machine has done a restart in the middle of an update, you usually need to check each table that could have been affected before it is used further. (These are “expected crashed tables.”) To cause the server to check `MyISAM` tables automatically, start it with the [`myisam_recover_options`](server-system-variables.md) system variable set. See [Section 7.1.8, “Server System Variables”](server-system-variables.md).

You should also check your tables regularly during normal system operation. For example, you can run a **cron** job to check important tables once a week, using a line like this in a `crontab` file:

```
35 0 * * 0 /path/to/myisamchk --fast --silent /path/to/datadir/*/*.MYI
```

This prints out information about crashed tables so that you can examine and repair them as necessary.

To start with, execute [**myisamchk -s**](myisamchk.md) each night on all tables that have been updated during the last 24 hours. As you see that problems occur infrequently, you can back off the checking frequency to once a week or so.

Normally, MySQL tables need little maintenance. If you are performing many updates to `MyISAM` tables with dynamic-sized rows (tables with [`VARCHAR`](char.md), [`BLOB`](blob.md), or [`TEXT`](blob.md) columns) or have tables with many deleted rows you may want to defragment/reclaim space from the tables from time to time. You can do this by using [`OPTIMIZE TABLE`](optimize-table.md) on the tables in question. Alternatively, if you can stop the [**mysqld**](mysqld.md) server for a while, change location into the data directory and use this command while the server is stopped:

```
$> myisamchk -r -s --sort-index --myisam_sort_buffer_size=16M */*.MYI
```