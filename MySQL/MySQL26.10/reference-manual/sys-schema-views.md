---
title: "MySQL :: MySQL 26.10 Reference Manual :: 30.4.3 sys Schema Views"
book: MySQL 26.10 Reference Manual
version: "26.10"
source: "https://dev.mysql.com/doc/refman/26.10/en/sys-schema-views.html"
tags:
  - mysql
  - mysql-26.10
  - reference-manual
---

### 30.4.3 sys Schema Views

The following sections describe [`sys`](sys-schema.md) schema views.

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

The view without the `x$` prefix is intended to provide output that is more user friendly and easier to read. The view with the `x$` prefix that displays the same values in raw form is intended more for use with other tools that perform their own processing on the data.

Views without the `x$` prefix differ from the corresponding `x$` views in these ways:

- Byte counts are formatted with size units using [`format_bytes()`](sys-format-bytes.md).
- Time values are formatted with temporal units using [`format_time()`](sys-format-time.md).
- SQL statements are truncated to a maximum display width using [`format_statement()`](sys-format-statement.md).
- Path name are shortened using [`format_path()`](sys-format-path.md).