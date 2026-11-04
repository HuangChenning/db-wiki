---
title: "MySQL :: MySQL 26.10 Reference Manual :: 15.1.29 DROP DATABASE Statement"
book: MySQL 26.10 Reference Manual
version: "26.10"
source: "https://dev.mysql.com/doc/refman/26.10/en/drop-database.html"
tags:
  - mysql
  - mysql-26.10
  - reference-manual
---

### 15.1.29 DROP DATABASE Statement

```sql
DROP {DATABASE | SCHEMA} [IF EXISTS] db_name
```

`DROP DATABASE` drops all tables in the database and deletes the database. Be *very* careful with this statement! To use `DROP DATABASE`, you need the [`DROP`](privileges-provided.md) privilege on the database. `DROP       SCHEMA` is a synonym for `DROP       DATABASE`.

Important

When a database is dropped, privileges granted specifically for the database are *not* automatically dropped. They must be dropped manually. See [Section 15.7.1.6, “GRANT Statement”](grant.md).

`IF EXISTS` is used to prevent an error from occurring if the database does not exist.

If the default database is dropped, the default database is unset (the [`DATABASE()`](information-functions.md) function returns `NULL`).

If you use `DROP DATABASE` on a symbolically linked database, both the link and the original database are deleted.

`DROP DATABASE` returns the number of tables that were removed.

The `DROP DATABASE` statement removes from the given database directory those files and directories that MySQL itself may create during normal operation. This includes all files with the extensions shown in the following list:

- `.BAK`
- `.DAT`
- `.HSH`
- `.MRG`
- `.MYD`
- `.MYI`
- `.cfg`
- `.db`
- `.ibd`
- `.ndb`

If other files or directories remain in the database directory after MySQL removes those just listed, the database directory cannot be removed. In this case, you must remove any remaining files or directories manually and issue the `DROP DATABASE` statement again. To keep this from happening, ensure that all tables in the database use a storage engine that supports atomic DDL (see [Section 15.1.1, “Atomic Data Definition Statement Support”](atomic-ddl.md)), such as [`InnoDB`](innodb-storage-engine.md).

Dropping a database does not remove any `TEMPORARY` tables that were created in that database. `TEMPORARY` tables are automatically removed when the session that created them ends. See [Section 15.1.25.2, “CREATE TEMPORARY TABLE Statement”](create-temporary-table.md).

You can also drop databases with [**mysqladmin**](mysqladmin.md). See [Section 6.5.2, “mysqladmin — A MySQL Server Administration Program”](mysqladmin.md).