---
title: "4.3.5 Making a Partial Backup"
book: "MySQL Enterprise Backup User's Guide (Version 8.0.46)"
version: "8.0"
source: "https://dev.mysql.com/doc/mysql-enterprise-backup/8.0/en/partial.html"
tags:
  - mysql
  - mysql-8.0
  - enterprise-backup
---

MySQL Enterprise Backup User's Guide (Version 8.0.46)

### 4.3.5 Making a Partial Backup

By default, all the files under the database subdirectories in the data directory are included in the backup, so that the backup includes data from all MySQL storage engines, any third-party storage engines, and even any non-database files in that directory. This section explains options you can use to selectively back up or exclude data.

There are various ways to create different kinds of partial backup with MySQL Enterprise Backup:

- Including or excluding specific tables by their names. This uses the [`--include-tables`](backup-partial-options.md) or [`--exclude-tables`](backup-partial-options.md) option.
	Each table is checked against the regular expression specified with the [`--include-tables`](backup-partial-options.md) or [`--exclude-tables`](backup-partial-options.md) option. If the regular expression matches the fully qualified name of the table (in the form of `db_name.table_name)`, the table is included or excluded for the backup. The regular expression syntax used is the extended form specified in the POSIX 1003.2 standard. The options have been implemented with the RE2 regular expression library.
- Including some or all InnoDB tables, but not other table types. This uses the [`--only-innodb`](backup-partial-options.md) option.
- Leaving out files that are present in the MySQL data directory but not actually part of the MySQL instance. This uses the [`--only-known-file-types`](backup-partial-options.md) option.
- Achieving a multiple of selection effects by using a combination of the above mentioned options.
- Backing up a selection of InnoDB tables using [transportable tablespaces (TTS)](glossary.md). This uses the [`--use-tts`](backup-partial-options.md) and the [`--include-tables`](backup-partial-options.md) or [`--exclude-tables`](backup-partial-options.md) (or both) options.

For syntax details on all the options involved, see [Section 20.8, “Partial Backup and Restore Options”](backup-partial-options.md).

Important

Typically, a partial backup is more difficult to restore than a full backup, because the backup data might not include the necessary interrelated pieces to constitute a complete MySQL instance. In particular, InnoDB tables have internal IDs and other data values that can only be restored to the same instance, not a different MySQL server. Always fully test the recovery procedure for any partial backups to understand the relevant procedures and restrictions.

The following are some command samples for partial backups.

Including all tables with names starting with “emp” into the backup:

```
mysqlbackup \
 --host=localhost --user=mysqluser --protocol=TCP --port=3306 \
 --backup-dir=$MEB_TEMP_BACKUP_DIR --backup-image=$MEB_BACKUPS_DIR/my.mbi \
 --include-tables="\.emp" \
 backup-to-image
```

Taking a backup of all tables except tables from the “mysql” and “performance\_schema” databases:

```
mysqlbackup \
 --host=localhost --user=mysqluser --protocol=TCP --port=3306 \
 --backup-dir=$MEB_TEMP_BACKUP_DIR --backup-image=$MEB_BACKUPS_DIR/my.mbi \
 --exclude-tables="^(mysql|performance_schema)\." \
 backup-to-image
```

Taking a backup of all tables in the “sales” database, but excludes the table with the name “hardware”

```
mysqlbackup \
 --host=localhost --user=mysqluser --protocol=TCP --port=3306 \
 ---backup-dir=$MEB_TEMP_BACKUP_DIR --backup-image=$MEB_BACKUPS_DIR/my.mbi \
 --include-tables="^sales\." --exclude-tables="^sales\.hardware$" \
 backup-to-image
```

Taking a backup of all tables in the “sales reps” database, but excludes the table with the name “euro-asia” (special characters like spaces or dashes are supported by the partial backup options):

```
mysqlbackup \
 --host=localhost --user=mysqluser --protocol=TCP --port=3306 \
 --backup-dir=$MEB_TEMP_BACKUP_DIR --backup-image=$MEB_BACKUPS_DIR/my.mbi \
 --include-tables="^sales reps\." --exclude-tables="^sales reps\.euro-asia" \
 backup-to-image
```

Backing up all InnoDB tables:

```
mysqlbackup \
 --host=localhost --user=mysqluser --protocol=TCP --port=3306 \
 --backup-dir=$MEB_TEMP_BACKUP_DIR --backup-image=$MEB_BACKUPS_DIR/my.mbi \
 --only-innodb \
 backup-to-image
```

You can also make [compressed](backup.compressed.md) and other kinds of selective backups by using the appropriate command options.

#### Making a Partial Backup with the Legacy Options (Deprecated)

Important

Information in this subsection is only for using the legacy option of [`--include`](backup-partial-options.md), which has been deprecated. For creating partial backups, use the [`--include-tables`](backup-partial-options.md) and [`--exclude-tables`](backup-partial-options.md) options instead.

Note

Typically, a partial backup is more difficult to restore than a full backup, because the backup data might not include the necessary interrelated pieces to constitute a complete MySQL instance. In particular, InnoDB tables have internal IDs and other data values that can only be restored to the same instance, not a different MySQL server. Always fully test the recovery procedure for any partial backups to understand the relevant procedures and restrictions.

With its [`--include`](backup-partial-options.md) option, **mysqlbackup** can make a backup that includes some InnoDB tables but not others:

- A partial backup with the `--include` option always contains the InnoDB system tablespace and all the tables inside it.
- For the InnoDB tables stored outside the system tablespace, the partial backup includes only those tables whose names match the regular expression specified with the `--include` option.

This operation requires the tables being left out to be stored in separate ``*`table_name`*.ibd`` files. To put an InnoDB table outside the system tablespace, create it while the [`innodb_file_per_table`](https://docs.oracle.com/cd/E17952_01/mysql-8.0-en/innodb-parameters.html#sysvar_innodb_file_per_table) MySQL configuration option is enabled. Each `.ibd` file holds the data and indexes of one table only.

Those InnoDB tables created with `innodb_file_per_table` turned off are stored as usual in the InnoDB [system tablespace](glossary.md), and cannot be left out of the backup.

For each table with a per-table data file a string of the form `db_name.table_name` is checked against the regular expression specified with the [`--include`](backup-partial-options.md) option. If the regular expression matches the complete string `db_name.table_name`, the table is included in the backup. The regular expression syntax used is the extended form specified in the POSIX 1003.2 standard. On Unix-like systems, quote the regular expression appropriately to prevent interpretation of shell meta-characters. This feature has been implemented with the RE2 regular expression library.

The backup directory produced contains a backup log file and copies of InnoDB data files.

**IMPORTANT:** Because the InnoDB system tablespace holds metadata about InnoDB tables from all databases in an instance, restoring a partial backup on a server that includes other databases could cause the system to lose track of those InnoDB tables in other databases. Always restore partial backups on a fresh MySQL server instance without any other InnoDB tables that you want to preserve.

**Example 4.22 Making an Uncompressed Partial Backup of InnoDB Tables**

In this example, we have configured MySQL so that some InnoDB tables have their own tablespaces. We make a partial backup including only those InnoDB tables in `test` database whose name starts with `ib`. The contents of the database directory for `test` database are shown below. Of these 10 tables six (`alex1`, `alex2`, `alex3`, `blobt3`, `ibstest0`, `ibstest09`) are stored in per-table data files (`.ibd` files).

```
$ ls /sqldata/mts/test
alex2.ibd  ibstest0.ibd alex1.ibd  blobt3.ibd  alex3.ibd  ibtest09.ibd
```

We run the **mysqlbackup** with the [`--include`](backup-partial-options.md) option:

```
# Back up some InnoDB tables.
$ mysqlbackup --defaults-file=/home/dbadmin/my.cnf --include="^test\.ib.*" backup

# Contents in the backup directory's subdirectory for the test database:
$ ls /sqldata-backup/test
ibstest0.ibd   ibtest09.ibd
```

The backup directory's subdirectory for the `test` database contains only backups of `ibstest0` and `ibtest09` tables, because other InnoDB tables do not match the include pattern `^test\.ib.*`.

**Example 4.23 Making a Compressed Partial Backup**

We have configured MySQL so that every InnoDB table has its own tablespace. We make a partial backup including only those InnoDB tables whose name starts with `alex` or `blob`. The contents of the database directory for `test` database is shown below.

```
$ ls /sqldata/mts/test
alex2.ibd  ibstest0.ibd  alex1.ibd  blobt3.ibd  alex3.ibd  ibtest09.ibd
```

We run **mysqlbackup** with the [`--compress`](backup-compression-options.md) and [`--include`](backup-partial-options.md) options:

```
$ mysqlbackup --defaults-file=/home/dbadmin/my.cnf --compress \
  --include=".*\.(alex|blob).*" backup
```

The backup directory for the database `test` is shown below. The `.ibz` files are compressed per-table data files.

```
$ ls /sqldata-backup/test
alex1.ibz   alex2.ibz   alex3.ibz   blobt3.ibz
```