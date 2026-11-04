---
title: "14.22 InnoDB Troubleshooting"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/innodb-troubleshooting.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

The following general guidelines apply to troubleshooting `InnoDB` problems:

- When an operation fails or you suspect a bug, look at the MySQL server error log (see [Section 5.4.2, “The Error Log”](error-log.md)). [Server Error Message Reference](https://docs.oracle.com/cd/E17952_01/mysql-errors-5.7-en/server-error-reference.html) provides troubleshooting information for some of the common `InnoDB` -specific errors that you may encounter.
- If the failure is related to a [deadlock](glossary.md), run with the [`innodb_print_all_deadlocks`](innodb-parameters.md) option enabled so that details about each deadlock are printed to the MySQL server error log. For information about deadlocks, see [Section 14.7.5, “Deadlocks in InnoDB”](innodb-deadlocks.md).
- Issues relating to the `InnoDB` data dictionary include failed [`CREATE TABLE`](create-table.md) statements (orphan table files), inability to open `InnoDB` files, and system cannot find the path specified errors. For information about these sorts of problems and errors, see [Section 14.22.3, “Troubleshooting InnoDB Data Dictionary Operations”](innodb-troubleshooting-datadict.md).
- When troubleshooting, it is usually best to run the MySQL server from the command prompt, rather than through [**mysqld\_safe**](mysqld-safe.md) or as a Windows service. You can then see what [**mysqld**](mysqld.md) prints to the console, and so have a better grasp of what is going on. On Windows, start [**mysqld**](mysqld.md) with the [`--console`](server-options.md) option to direct the output to the console window.
- Enable the `InnoDB` Monitors to obtain information about a problem (see [Section 14.18, “InnoDB Monitors”](innodb-monitors.md)). If the problem is performance-related, or your server appears to be hung, you should enable the standard Monitor to print information about the internal state of `InnoDB`. If the problem is with locks, enable the Lock Monitor. If the problem is with table creation, tablespaces, or data dictionary operations, refer to the [InnoDB Information Schema system tables](innodb-information-schema-system-tables.md) to examine contents of the `InnoDB` internal data dictionary.
	`InnoDB` temporarily enables standard `InnoDB` Monitor output under the following conditions:
	- A long semaphore wait
	- `InnoDB` cannot find free blocks in the buffer pool
	- Over 67% of the buffer pool is occupied by lock heaps or the adaptive hash index
- If you suspect that a table is corrupt, run [`CHECK TABLE`](check-table.md) on that table.