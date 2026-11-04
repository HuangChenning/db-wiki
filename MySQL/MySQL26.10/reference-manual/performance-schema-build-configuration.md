---
title: "MySQL :: MySQL 26.10 Reference Manual :: 29.2 Performance Schema Build Configuration"
book: MySQL 26.10 Reference Manual
version: "26.10"
source: "https://dev.mysql.com/doc/refman/26.10/en/performance-schema-build-configuration.html"
tags:
  - mysql
  - mysql-26.10
  - reference-manual
---

## 29.2 Performance Schema Build Configuration

The Performance Schema is mandatory and always compiled in. It is possible to exclude certain parts of the Performance Schema instrumentation. For example, to exclude stage and statement instrumentation, do this:

```svg
$> cmake . \
        -DDISABLE_PSI_STAGE=1 \
        -DDISABLE_PSI_STATEMENT=1
```

For more information, see the descriptions of the ``DISABLE_PSI_*`XXX`*`` **CMake** options in [Section 2.8.7, “MySQL Source-Configuration Options”](source-configuration-options.md).

If you install MySQL over a previous installation that was configured without the Performance Schema (or with an older version of the Performance Schema that has missing or out-of-date tables). One indication of this issue is the presence of messages such as the following in the error log:

```svg
[ERROR] Native table 'performance_schema'.'events_waits_history'
has the wrong structure
[ERROR] Native table 'performance_schema'.'events_waits_history_long'
has the wrong structure
...
```

To correct that problem, perform the MySQL upgrade procedure. See [Chapter 3, *Upgrading MySQL*](upgrading.md).

Because the Performance Schema is configured into the server at build time, a row for [`PERFORMANCE_SCHEMA`](performance-schema.md) appears in the output from [`SHOW ENGINES`](show-engines.md). This means that the Performance Schema is available, not that it is enabled. To enable it, you must do so at server startup, as described in the next section.