---
title: "Chapter 26 MySQL sys Schema"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/sys-schema.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

MySQL 5.7 includes the `sys` schema, a set of objects that helps DBAs and developers interpret data collected by the Performance Schema. `sys` schema objects can be used for typical tuning and diagnosis use cases. Objects in this schema include:

- Views that summarize Performance Schema data into more easily understandable form.
- Stored procedures that perform operations such as Performance Schema configuration and generating diagnostic reports.
- Stored functions that query Performance Schema configuration and provide formatting services.

For new installations, the `sys` schema is installed by default during data directory initialization if you use [**mysqld**](mysqld.md) with the [`--initialize`](server-options.md) or [`--initialize-insecure`](server-options.md) option. You can drop the `sys` schema manually after initialization if it is unneeded.

For upgrades, [**mysql\_upgrade**](mysql-upgrade.md) installs the `sys` schema if it is not installed, and upgrades it to the current version otherwise. To permit this behavior to be suppressed, [**mysql\_upgrade**](mysql-upgrade.md) has a [`--skip-sys-schema`](mysql-upgrade.md) option.

[**mysql\_upgrade**](mysql-upgrade.md) returns an error if a `sys` schema exists but has no [`version`](sys-version.md) view, on the assumption that absence of this view indicates a user-created `sys` schema. To upgrade in this case, remove or rename the existing `sys` schema first.

`sys` schema objects have a `DEFINER` of `'mysql.sys'@'localhost'`. Use of the dedicated `mysql.sys` account avoids problems that occur if a DBA renames or removes the `root` account.