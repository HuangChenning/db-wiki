---
title: "3.14 Rebuilding or Repairing Tables or Indexes"
book: MySQL 8.0 Reference Manual
version: "8.0"
source: "https://dev.mysql.com/doc/refman/8.0/en/rebuilding-tables.html"
tags:
  - mysql
  - mysql-8.0
  - reference-manual
---

MySQL 8.0 Reference Manual Including MySQL NDB Cluster 8.0

This section describes how to rebuild or repair tables or indexes, which may be necessitated by:

- Changes to how MySQL handles data types or character sets. For example, an error in a collation might have been corrected, necessitating a table rebuild to update the indexes for character columns that use the collation.
- Required table repairs or upgrades reported by [`CHECK TABLE`](check-table.md), [**mysqlcheck**](mysqlcheck.md), or [**mysql\_upgrade**](mysql-upgrade.md).

Methods for rebuilding a table include:

### Dump and Reload Method

If you are rebuilding tables because a different version of MySQL cannot handle them after a binary (in-place) upgrade or downgrade, you must use the dump-and-reload method. Dump the tables *before* upgrading or downgrading using your original version of MySQL. Then reload the tables *after* upgrading or downgrading.

If you use the dump-and-reload method of rebuilding tables only for the purpose of rebuilding indexes, you can perform the dump either before or after upgrading or downgrading. Reloading still must be done afterward.

If you need to rebuild an `InnoDB` table because a [`CHECK TABLE`](check-table.md) operation indicates that a table upgrade is required, use [**mysqldump**](mysqldump.md) to create a dump file and [**mysql**](mysql.md) to reload the file. If the [`CHECK TABLE`](check-table.md) operation indicates that there is a corruption or causes `InnoDB` to fail, refer to [Section 17.21.3, “Forcing InnoDB Recovery”](forcing-innodb-recovery.md) for information about using the [`innodb_force_recovery`](innodb-parameters.md) option to restart `InnoDB`. To understand the type of problem that [`CHECK TABLE`](check-table.md) may be encountering, refer to the `InnoDB` notes in [Section 15.7.3.2, “CHECK TABLE Statement”](check-table.md).

To rebuild a table by dumping and reloading it, use [**mysqldump**](mysqldump.md) to create a dump file and [**mysql**](mysql.md) to reload the file:

```
mysqldump db_name t1 > dump.sql
mysql db_name < dump.sql
```

To rebuild all the tables in a single database, specify the database name without any following table name:

```
mysqldump db_name > dump.sql
mysql db_name < dump.sql
```

To rebuild all tables in all databases, use the [`--all-databases`](mysqldump.md) option:

```
mysqldump --all-databases > dump.sql
mysql < dump.sql
```

### ALTER TABLE Method

To rebuild a table with [`ALTER         TABLE`](alter-table.md), use a “null” alteration; that is, an [`ALTER TABLE`](alter-table.md) statement that “changes” the table to use the storage engine that it already has. For example, if `t1` is an `InnoDB` table, use this statement:

```
ALTER TABLE t1 ENGINE = InnoDB;
```

If you are not sure which storage engine to specify in the [`ALTER TABLE`](alter-table.md) statement, use [`SHOW CREATE TABLE`](show-create-table.md) to display the table definition.

### REPAIR TABLE Method

The [`REPAIR TABLE`](repair-table.md) method is only applicable to `MyISAM`, `ARCHIVE`, and `CSV` tables.

You can use [`REPAIR TABLE`](repair-table.md) if the table checking operation indicates that there is a corruption or that an upgrade is required. For example, to repair a `MyISAM` table, use this statement:

```
REPAIR TABLE t1;
```

[**mysqlcheck --repair**](mysqlcheck.md) provides command-line access to the [`REPAIR TABLE`](repair-table.md) statement. This can be a more convenient means of repairing tables because you can use the [`--databases`](mysqlcheck.md) or [`--all-databases`](mysqlcheck.md) option to repair all tables in specific databases or all databases, respectively:

```
mysqlcheck --repair --databases db_name ...
mysqlcheck --repair --all-databases
```