---
title: "MySQL :: MySQL 26.7 Reference Manual :: 30.2 Using the sys Schema"
book: MySQL 26.7 Reference Manual
version: "26.7"
source: "https://dev.mysql.com/doc/refman/26.7/en/sys-schema-usage.html"
tags:
  - mysql
  - mysql-26.7
  - reference-manual
---

## 30.2 Using the sys Schema

You can make the [`sys`](sys-schema.md) schema the default schema so that references to its objects need not be qualified with the schema name:

```sql
mysql> USE sys;
Database changed
mysql> SELECT * FROM version;
+-------------+---------------+
| sys_version | mysql_version |
+-------------+---------------+
| 2.1.1       | 8.4.0-tr      |
+-------------+---------------+
```

(The [`version`](sys-version.md) view shows the [`sys`](sys-schema.md) schema and MySQL server versions.)

To access [`sys`](sys-schema.md) schema objects while a different schema is the default (or simply to be explicit), qualify object references with the schema name:

```sql
mysql> SELECT * FROM sys.version;
+-------------+---------------+
| sys_version | mysql_version |
+-------------+---------------+
| 2.1.1       | 8.4.0-tr      |
+-------------+---------------+
```

The `sys` schema contains many views that summarize Performance Schema tables in various ways. Most of these views come in pairs, such that one member of the pair has the same name as the other member, plus a `x$` prefix. For example, the [`host_summary_by_file_io`](sys-host-summary-by-file-io.md) view summarizes file I/O grouped by host and displays latencies converted from picoseconds to more readable values (with units);

```sql
mysql> SELECT * FROM sys.host_summary_by_file_io;
+------------+-------+------------+
| host       | ios   | io_latency |
+------------+-------+------------+
| localhost  | 67570 | 5.38 s     |
| background |  3468 | 4.18 s     |
+------------+-------+------------+
```

The [`x$host_summary_by_file_io`](sys-host-summary-by-file-io.md) view summarizes the same data but displays unformatted picosecond latencies:

```sql
mysql> SELECT * FROM sys.x$host_summary_by_file_io;
+------------+-------+---------------+
| host       | ios   | io_latency    |
+------------+-------+---------------+
| localhost  | 67574 | 5380678125144 |
| background |  3474 | 4758696829416 |
+------------+-------+---------------+
```

The view without the `x$` prefix is intended to provide output that is more user friendly and easier for humans to read. The view with the `x$` prefix that displays the same values in raw form is intended more for use with other tools that perform their own processing on the data. For additional information about the differences between non- `x$` and `x$` views, see [Section 30.4.3, “sys Schema Views”](sys-schema-views.md).

To examine [`sys`](sys-schema.md) schema object definitions, use the appropriate [`SHOW`](show.md) statement or [`INFORMATION_SCHEMA`](information-schema.md) query. For example, to examine the definitions of the [`session`](sys-session.md) view and [`format_bytes()`](sys-format-bytes.md) function, use these statements:

```sql
mysql> SHOW CREATE VIEW sys.session;
mysql> SHOW CREATE FUNCTION sys.format_bytes;
```

However, those statements display the definitions in relatively unformatted form. To view object definitions with more readable formatting, access the individual `.sql` files found under the `scripts/sys_schema` directory in MySQL source distributions.

[**mysqldump**](mysqldump.md) does not dump the [`sys`](sys-schema.md) schema by default. To generate a dump file, name the [`sys`](sys-schema.md) schema explicitly on the command line using either of these commands:

```svg
mysqldump --databases --routines sys > sys_dump.sql
```

To reinstall the schema from the dump file, use this command:

```svg
mysql < sys_dump.sql
```