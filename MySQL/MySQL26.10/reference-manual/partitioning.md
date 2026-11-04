---
title: "MySQL :: MySQL 26.10 Reference Manual :: 26 Partitioning"
book: MySQL 26.10 Reference Manual
version: "26.10"
source: "https://dev.mysql.com/doc/refman/26.10/en/partitioning.html"
tags:
  - mysql
  - mysql-26.10
  - reference-manual
---

## Chapter 26 Partitioning

This chapter discusses user-defined partitioning.

Note

Table partitioning differs from partitioning as used by window functions. For information about window functions, see [Section 14.20, “Window Functions”](window-functions.md).

In MySQL 26.10, partitioning support is provided by the [`InnoDB`](innodb-storage-engine.md) and [`NDB`](mysql-cluster.md) storage engines.

MySQL 26.10 does not currently support partitioning of tables using any storage engine other than `InnoDB` or `NDB`, such as [`MyISAM`](myisam-storage-engine.md). An attempt to create a partitioned tables using a storage engine that does not supply native partitioning support fails with [`ER_CHECK_NOT_IMPLEMENTED`](https://dev.mysql.com/doc/mysql-errors/26.10/en/server-error-reference.html#error_er_check_not_implemented).

If you are compiling MySQL 26.10 from source, configuring the build with `InnoDB` support is sufficient to produce binaries with partition support for `InnoDB` tables. For more information, see [Section 2.8, “Installing MySQL from Source”](source-installation.md).

Nothing further needs to be done to enable partitioning support by `InnoDB` (for example, no special entries are required in the `my.cnf` file).

It is not possible to disable partitioning support by the `InnoDB` storage engine.

See [Section 26.1, “Overview of Partitioning in MySQL”](partitioning-overview.md), for an introduction to partitioning and partitioning concepts.

Several types of partitioning are supported, as well as subpartitioning; see [Section 26.2, “Partitioning Types”](partitioning-types.md), and [Section 26.2.6, “Subpartitioning”](partitioning-subpartitions.md).

[Section 26.3, “Partition Management”](partitioning-management.md), covers methods of adding, removing, and altering partitions in existing partitioned tables.

[Section 26.3.4, “Maintenance of Partitions”](partitioning-maintenance.md), discusses table maintenance commands for use with partitioned tables.

The [`PARTITIONS`](information-schema-partitions-table.md) table in the `INFORMATION_SCHEMA` database provides information about partitions and partitioned tables. See [Section 28.3.26, “The INFORMATION\_SCHEMA PARTITIONS Table”](information-schema-partitions-table.md), for more information; for some examples of queries against this table, see [Section 26.2.7, “How MySQL Partitioning Handles NULL”](partitioning-handling-nulls.md).

For known issues with partitioning in MySQL 26.10, see [Section 26.6, “Restrictions and Limitations on Partitioning”](partitioning-limitations.md).

You may also find the following resources to be useful when working with partitioned tables.

**Additional Resources.** Other sources of information about user-defined partitioning in MySQL include the following:

- [MySQL Partitioning Forum](https://forums.mysql.com/list.php?106)
	This is the official discussion forum for those interested in or experimenting with MySQL Partitioning technology. It features announcements and updates from MySQL developers and others. It is monitored by members of the Partitioning Development and Documentation Teams.
- [PlanetMySQL](http://www.planetmysql.org/)
	A MySQL news site featuring MySQL-related blogs, which should be of interest to anyone using my MySQL. We encourage you to check here for links to blogs kept by those working with MySQL Partitioning, or to have your own blog added to those covered.