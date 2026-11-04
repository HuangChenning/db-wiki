---
title: "9.6 MyISAM Table Maintenance and Crash Recovery"
book: MySQL 8.0 Reference Manual
version: "8.0"
source: "https://dev.mysql.com/doc/refman/8.0/en/myisam-table-maintenance.html"
tags:
  - mysql
  - mysql-8.0
  - reference-manual
---

MySQL 8.0 Reference Manual Including MySQL NDB Cluster 8.0

This section discusses how to use [**myisamchk**](myisamchk.md) to check or repair `MyISAM` tables (tables that have `.MYD` and `.MYI` files for storing data and indexes). For general [**myisamchk**](myisamchk.md) background, see [Section 6.6.4, “myisamchk — MyISAM Table-Maintenance Utility”](myisamchk.md). Other table-repair information can be found at [Section 3.14, “Rebuilding or Repairing Tables or Indexes”](rebuilding-tables.md).

You can use [**myisamchk**](myisamchk.md) to check, repair, or optimize database tables. The following sections describe how to perform these operations and how to set up a table maintenance schedule. For information about using [**myisamchk**](myisamchk.md) to get information about your tables, see [Section 6.6.4.5, “Obtaining Table Information with myisamchk”](myisamchk-table-info.md).

Even though table repair with [**myisamchk**](myisamchk.md) is quite secure, it is always a good idea to make a backup *before* doing a repair or any maintenance operation that could make a lot of changes to a table.

[**myisamchk**](myisamchk.md) operations that affect indexes can cause `MyISAM` `FULLTEXT` indexes to be rebuilt with full-text parameters that are incompatible with the values used by the MySQL server. To avoid this problem, follow the guidelines in [Section 6.6.4.1, “myisamchk General Options”](myisamchk-general-options.md).

`MyISAM` table maintenance can also be done using the SQL statements that perform operations similar to what [**myisamchk**](myisamchk.md) can do:

For additional information about these statements, see [Section 15.7.3, “Table Maintenance Statements”](table-maintenance-statements.md).

These statements can be used directly or by means of the [**mysqlcheck**](mysqlcheck.md) client program. One advantage of these statements over [**myisamchk**](myisamchk.md) is that the server does all the work. With [**myisamchk**](myisamchk.md), you must make sure that the server does not use the tables at the same time so that there is no unwanted interaction between [**myisamchk**](myisamchk.md) and the server.